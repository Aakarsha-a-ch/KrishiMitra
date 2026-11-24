from pathlib import Path
import json
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "leaf_disease_model.pt"

_CACHED_MODEL = None
_CACHED_CLASSES = None
_CACHED_ACC = None

def load_disease_model():
    global _CACHED_MODEL, _CACHED_CLASSES, _CACHED_ACC
    if _CACHED_MODEL is not None:
        return _CACHED_MODEL, _CACHED_CLASSES, _CACHED_ACC

    if not MODEL_PATH.exists():
        return None, None, None
    try:
        import torch
        import torch.nn as nn
        from torchvision import models
        checkpoint = torch.load(MODEL_PATH, map_location=torch.device('cpu'))
        class_names = checkpoint.get('class_names', [])
        model = models.mobilenet_v2(weights=None)
        model.classifier[1] = nn.Linear(model.last_channel, len(class_names))
        model.load_state_dict(checkpoint['model_state_dict'])
        model.eval()
        val_acc = checkpoint.get('val_accuracy', None)

        _CACHED_MODEL = model
        _CACHED_CLASSES = class_names
        _CACHED_ACC = val_acc
        return _CACHED_MODEL, _CACHED_CLASSES, _CACHED_ACC
    except Exception as e:
        print(f"Error loading leaf disease model: {e}")
        return None, None, None

def predict_leaf_disease(image: Image.Image, model, class_names):
    import torch
    from torchvision import transforms
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    tensor = transform(image.convert("RGB")).unsqueeze(0)
    with torch.no_grad():
        outputs = model(tensor)
        probs = torch.softmax(outputs, dim=1)[0]
        top3_prob, top3_idx = torch.topk(probs, min(3, len(class_names)))
    
    results = []
    for p, idx in zip(top3_prob, top3_idx):
        raw_name = class_names[idx.item()]
        parts = raw_name.split("___")
        crop_name = parts[0].replace("_", " ").strip()
        disease_name = parts[1].replace("_", " ").strip() if len(parts) > 1 else raw_name
        results.append({
            "raw": raw_name,
            "crop": crop_name,
            "disease": disease_name,
            "confidence": p.item()
        })
    return results

def load_crop_health_data():
    data_path = ROOT / "data" / "processed" / "kau_crop_chunks.json"
    try:
        with open(data_path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []
