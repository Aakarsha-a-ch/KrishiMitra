import json
import re
from pathlib import Path
import numpy as np
import onnxruntime as ort
from tokenizers import Tokenizer
from huggingface_hub import hf_hub_download

# Paths relative to project root
ROOT_DIR = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT_DIR / "models" / "multilingual_minilm"
DATA_PATH = ROOT_DIR / "data" / "processed" / "kau_crop_chunks.json"
EMBEDDINGS_PATH = ROOT_DIR / "data" / "processed" / "kau_embeddings.npy"
MODEL_PATH = MODEL_DIR / "onnx" / "model_quint8_avx2.onnx"

# Lazy-loaded globals to ensure instant startup and page navigation
_documents = None
_embeddings = None
_tokenizer = None
_session = None

def _ensure_loaded():
    global _documents, _embeddings, _tokenizer, _session
    if _session is not None:
        return

    # Download the ONNX model automatically if it is missing.
    if not MODEL_PATH.is_file():
        hf_hub_download(
            repo_id="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2",
            filename="onnx/model_quint8_avx2.onnx",
            local_dir=MODEL_DIR,
        )

    # Load data once
    with open(DATA_PATH, encoding="utf-8") as f:
        _documents = json.load(f)
    _embeddings = np.load(EMBEDDINGS_PATH)

    # Load tokenizer and ONNX model
    _tokenizer = Tokenizer.from_file(str(MODEL_DIR / "tokenizer.json"))
    _tokenizer.enable_truncation(max_length=128)
    _tokenizer.enable_padding()

    _session = ort.InferenceSession(str(MODEL_PATH), providers=["CPUExecutionProvider"])

# Broad agricultural crop dictionary with Telugu keywords
KNOWN_CROPS = {
    "apple": ["apple", "apples", "ఆపిల్"],
    "banana": ["banana", "bananas", "అరటి", "నంద్రాన్", "రోబస్టా", "musa"],
    "rice": ["rice", "paddy", "వరి", "వరిధాన్యం", "బియ్యం", "బాస్మతి", "వడ్లు", "వరిచేను"],
    "cotton": ["cotton", "పత్తి", "ప్రత్తి", "దూది"],
    "chilli": ["chilli", "chillies", "chili", "మిరప", "మిరపకాయ", "మిర్చి"],
    "groundnut": ["groundnut", "peanut", "వేరుశనగ", "పల్లీ", "వేరుశెనగ"],
    "coconut": ["coconut", "coconuts", "కొబ్బరి", "కొబ్బరిచెట్టు", "కొబ్బరికాయ"],
    "pepper": ["pepper", "black pepper", "మిరియాలు", "నల్ల మిరియాలు"],
    "tomato": ["tomato", "tomatoes", "టమాటా", "టమోటా"],
    "potato": ["potato", "potatoes", "బంగాళాదుంప", "ఆలూ"],
    "mango": ["mango", "mangoes", "మామిడి", "మామిడికాయ"],
    "maize": ["maize", "corn", "మొక్కజొన్న"],
    "sugarcane": ["sugarcane", "చెరకు"],
    "turmeric": ["turmeric", "పసుపు"],
    "tobacco": ["tobacco", "పొగాకు"],
    "onion": ["onion", "ఉల్లిపాయ", "ఉల్లి"],
    "redgram": ["redgram", "pigeonpea", "కందులు"],
    "bengalgram": ["bengalgram", "chickpea", "శనగలు"],
    "blackgram": ["blackgram", "మినుములు"],
    "greengram": ["greengram", "పెసలు"]
}

def detect_crop_from_query(query: str, fallback_crop: str = "Paddy") -> str:
    """Detect crop entity from user question. If user asks about cotton, returns cotton, not fallback."""
    q_lower = query.lower()
    
    # Check known crops first
    for crop_name, keywords in KNOWN_CROPS.items():
        for kw in keywords:
            # Word boundary matching to avoid false substring triggers
            if re.search(r'\b' + re.escape(kw) + r'\b', q_lower):
                return crop_name
    
    # Check if fallback crop matches
    fb = fallback_crop.lower()
    for crop_name, keywords in KNOWN_CROPS.items():
        if crop_name in fb:
            return crop_name
        for kw in keywords:
            if kw in fb:
                return crop_name
                
    return fallback_crop.lower()

def _encode_query(query: str) -> np.ndarray:
    """Encode a query string to a normalized 384‑dim vector using the ONNX model."""
    _ensure_loaded()
    encoding = _tokenizer.encode(query)
    inputs = {
        "input_ids": np.array([encoding.ids], dtype=np.int64),
        "attention_mask": np.array([encoding.attention_mask], dtype=np.int64),
        "token_type_ids": np.array([encoding.type_ids], dtype=np.int64),
    }
    token_embeddings = _session.run(None, inputs)[0]
    mask = inputs["attention_mask"][..., None]
    pooled = np.sum(token_embeddings * mask, axis=1) / np.maximum(np.sum(mask, axis=1), 1)
    norm = np.linalg.norm(pooled, axis=1, keepdims=True)
    norm = np.maximum(norm, 1e-12)
    pooled = pooled / norm
    return pooled[0].astype(np.float32)

def search(query: str, crop: str = "rice", top_k: int = 4):
    """Return the top‑k most similar chunks for *query*.
    Intelligently identifies crop from query and retrieves matching corpus.
    """
    _ensure_loaded()
    effective_crop = detect_crop_from_query(query, fallback_crop=crop)
    query_vec = _encode_query(query)
    
    # Check if effective_crop has direct documents in knowledge base
    crop_indices = [i for i, doc in enumerate(_documents) if doc.get("crop", "").lower() == effective_crop]
    
    # If crop is not in base sub-dataset, search across entire corpus for semantic matches (nutrition/soil/pest)
    is_external_crop = False
    if not crop_indices:
        crop_indices = list(range(len(_documents)))
        is_external_crop = True
        
    sims = _embeddings[crop_indices] @ query_vec
    top_idxs = np.argsort(sims)[::-1][:top_k]
    
    results = []
    for rank, idx in enumerate(top_idxs, start=1):
        doc_idx = crop_indices[idx]
        doc = _documents[doc_idx]
        results.append(
            {
                "rank": rank,
                "similarity": float(sims[idx]),
                "crop": doc.get("crop"),
                "pdf_page": doc.get("pdf_page"),
                "chunk_id": doc.get("chunk_id"),
                "text": doc.get("text", "").strip(),
                "is_external_crop": is_external_crop
            }
        )
    return results, effective_crop

def retrieve_answer(query: str, crop: str = "rice", top_k: int = 4):
    """Retrieve top chunks as formatted strings for chatbot/LLM context."""
    results, _ = search(query, crop=crop, top_k=top_k)
    return [r.get("text", "") for r in results if r.get("text")]
