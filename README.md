# 🌱 KrishiMitra (కృషిమిత్ర)
### AI-Powered Smart Agricultural Decision Support Platform
#### Developed by: **Aakarsha Archana** & **Shiney** (B.Tech AIML)

---

## 📖 Executive Overview

**KrishiMitra (కృషిమిత్ర)** is an end-to-end, full-stack agricultural decision support platform engineered specifically for farmers in Vijayawada, Krishna Delta, Guntur, and Andhra Pradesh agro-climatic zones.

The platform bridges the gap between complex agricultural science and field-level execution by unifying:
1. **Computer Vision Deep Learning** (MobileNetV2) for plant leaf disease diagnosis.
2. **Tabular Machine Learning** (Random Forest) for climate-soil-yield crop recommendations.
3. **Hyper-Local Agro-Meteorology** (Open-Meteo) providing real-time telemetry and safe chemical spraying window advisories.
4. **Soil Chemistry & Split Fertilizer Algorithms** translating NPK laboratory tests into exact per-acre Urea, DAP, and MOP commercial bags and timing schedules.
5. **Hybrid Retrieval-Augmented Generation (RAG)** combining BM25 keyword matching, quantized ONNX multilingual semantic embeddings, and live agricultural web search with Acharya N.G. Ranga Agricultural University (ANGRAU) package of practices.
6. **Direct Peer Farmer Connect & Community Forum** facilitating WhatsApp-style direct messaging with regional farmer personas and community discussions.
7. **Live AP Mandi Market Rates** tracking 15 major staples, cash crops, pulses, fruits, and vegetables across regional yards with price trend tracking.
8. **100% Real-Time Bilingual Interface** providing 0ms client-side translation between **Telugu (తెలుగు)** and **English**.

---

## 👥 Developers

- **Aakarsha Archana** — B.Tech AIML
- **Shiney** — B.Tech AIML

- **Focus Region:** Krishna Delta & Andhra Pradesh Agro-Climatic Zones.
- **Primary Languages Supported:** Telugu (తెలుగు) & English.

---

## 🚀 Key Functional Modules

### 1. 🌿 Crop Health (MobileNetV2 Leaf Disease Scanner)
- Instant diagnosis of **38 crop disease classes** and healthy foliage from uploaded leaf photos.
- Trained on **54,305 curated leaf images** with **97.15% validation accuracy**.
- Outputs tailored, research-grounded **organic remedies**, **recommended chemical treatments**, and **long-term prevention protocols** matched with ANGRAU guidelines.

### 2. 🌦️ Live Weather & Spray Window Advisory
- Real-time weather telemetry centered on Vijayawada (`16.5062° N, 80.6480° E`) and 13 Andhra Pradesh districts via Open-Meteo.
- Tracks temperature, apparent temperature ("feels like"), relative humidity, wind speed, wind direction, and precipitation probability.
- **Automated Spraying Window Algorithm:** Analyzes rain probability and wind velocity to inform farmers whether chemical spraying is safe or risky.
- 5-day daily agro-forecast with maximum/minimum temperature and expected rainfall (mm).

### 3. 🧪 Soil Health & NPK Fertilizer Split Calculator
- Input soil test parameters: **pH, Nitrogen (N), Phosphorus (P), Potassium (K)** in kg/hectare.
- Tailored for 14 major crops: Paddy, Chilli, Cotton, Maize, Groundnut, Sugarcane, Turmeric, Blackgram, Greengram, Redgram, Banana, Mango, Tomato, and Tobacco.
- Computes exact commercial bag requirements per acre:
  - **Urea (46% N)** 45 kg bags
  - **DAP (18% N, 46% P₂O₅)** 50 kg bags
  - **MOP (60% K₂O)** 50 kg bags
- Generates staged split-dosage timelines (Basal application at transplanting, active tillering / vegetative stage, panicle initiation / flowering stage).
- Detects acidic or alkaline soil imbalances and calculates corrective soil amendments (Agricultural Lime or Gypsum per acre).

### 4. 🌾 Machine Learning Crop Recommendation
- Random Forest multi-class model predicting optimal crops from 7 soil and climatic parameters (N, P, K, pH, Temperature, Humidity, Annual Rainfall).
- Returns the primary recommended crop with model confidence and top-3 ranked candidate alternatives.

### 5. 🤖 Conversational Agro AI Assistant
- Bilingual conversational agent delivering scientific, actionable advisory in Telugu and English.
- **Hybrid RAG Pipeline:**
  - Lexical keyword search (BM25) over curated ANGRAU Package of Practices.
  - Semantic vector search using quantized ONNX Paraphrase-Multilingual-MiniLM embeddings.
  - Live agricultural web search integration (DuckDuckGo Search) for real-time market news and weather conditions.
  - Dynamic synthesis with prompt engineering tailored for Andhra Pradesh agriculture, schemes (PM-Kisan, YSR Rythu Bharosa), and organic pest control (Jeevamrutham, Neem oil).

### 6. 👨‍🌾 Farmer Connect & WhatsApp-Style Direct Chat
- **Community Forum:** Category-filtered feed (Pest Control, Mandi Rates, Fertilizers, Seeds, General) with live like counters and collapsible comment threads.
- **Direct 1-on-1 Farmer Chat:** Interactive chat interface featuring active Andhra Pradesh farmer personas:
  - **Shiney** (Guntur • Teja Chilli)
  - **Venkat Reddy** (Kurnool • Groundnut K-6)
  - **Apparao** (East Godavari • Paddy BPT 5204)
  - **Srinivasulu** (Anantapur • Horticulture / Sweet Orange)
- Features instant persona switching, typing indicators, quick inquiry suggestion chips, and responsive agronomic guidance.

### 7. 💰 Live AP Mandi Market Rates
- Live market prices for **15 Andhra Pradesh crops**:
  - **Top 6 Primary Staples/Cash Crops:** Paddy (BPT 5204), Teja Chilli, Cotton (Bunny), Maize, Groundnut (K-6), Sugarcane.
  - **9 Regional Crops:** Tomato, Blackgram (Urad), Redgram (Toor), Duggirala Turmeric, Bellary Onion, Virginia Tobacco, Banganapalli Mango, Karpura Banana, Sweet Orange (Mosambi).
- Displays primary yard (Vijayawada, Guntur, Tenali, Kurnool, Madanapalle, Duggirala, Ongole, Rajahmundry), price units (Quintal, Ton, Crate, Bunch), and daily percentage trend indicators.

### 8. 🚨 Emergency Helplines & AP Schemes
- One-click contact info for Kisan Call Centre (Toll-free 1800-180-1551), Rythu Bharosa Kendras (RBK - 155251), and Krishna Krishi Vigyan Kendra (KVK - 08674-245236).

### 9. 🌐 Instant Client-Side Bilingual Localization
- One-click toggle between **తెలుగు** and **English**.
- Real-time client-side rendering with 0ms latency covering all 178+ navigation labels, cards, form placeholders, dropdown selections, telemetry readouts, and assistant prompts.

---

## 🛠️ Technology Stack & Architecture

```
                          ┌──────────────────────────────────────┐
                          │         CLIENT BROWSER (SPA)         │
                          │   HTML5 • Glassmorphic CSS3 • JS     │
                          │      0ms Bilingual Translation       │
                          └──────────────────┬───────────────────┘
                                             │ HTTP / JSON
                                             ▼
                          ┌──────────────────────────────────────┐
                          │          FASTAPI BACKEND             │
                          │        (Uvicorn ASGI Server)         │
                          └───────┬──────────┬───────────┬───────┘
                                  │          │           │
            ┌─────────────────────┘          │           └────────────────────┐
            ▼                                ▼                                ▼
  ┌───────────────────┐            ┌───────────────────┐            ┌───────────────────┐
  │   COMPUTER VISION │            │  MACHINE LEARNING │            │    HYBRID RAG     │
  │    MobileNetV2    │            │   Random Forest   │            │   BM25 + ONNX     │
  │   Leaf Diseases   │            │  Crop Recommender │            │  MiniLM Embeddings│
  └───────────────────┘            └───────────────────┘            └───────────────────┘
```

| Layer | Technologies Used | Purpose |
| :--- | :--- | :--- |
| **Backend Framework** | **FastAPI**, **Uvicorn** (ASGI), Pydantic | High-speed asynchronous REST API, request validation, static file serving |
| **Frontend** | Semantic **HTML5**, **CSS3** (Glassmorphism & SVGs), **Vanilla JS** | Zero-latency single-page application, 0ms tab switching, no build overhead |
| **Deep Learning** | **PyTorch**, **Torchvision**, MobileNetV2 | Plant disease diagnosis on 38 classes with 97.15% accuracy |
| **Machine Learning** | **Scikit-learn**, pandas, numpy, joblib | Multi-class Random Forest model for crop recommendation |
| **Vector Search & RAG**| **ONNX Runtime**, Hugging Face Tokenizers, `rank_bm25` | Hybrid semantic + lexical retrieval over ANGRAU documents |
| **Live Meteorology** | **Open-Meteo API** (Open-Meteo REST & Geocoding) | Real-time weather and 5-day daily agricultural forecasts |
| **Web Intelligence** | **DuckDuckGo Search** (`duckduckgo-search`) | Live agronomic web search for real-time market and field advice |
| **Security & Auth** | **Argon2-cffi**, JSON / In-memory session store | Secure password hashing, multi-user accounts, 1-tap demo access |

---

## 📂 Repository File Structure

```text
krishimitra/
├── server.py                   # High-performance FastAPI backend server (Endpoints & Static Mounting)
├── requirements.txt            # Production Python package dependencies
├── README.md                   # Comprehensive project documentation & guide
├── PROJECT_EXPLANATION.md      # In-depth architectural rationale & feature user guide (A-Z)
├── .gitignore                  # Git ignore specifications
├── static/                     # Single-Page Application (SPA) Web Frontend
│   ├── index.html              # Clean semantic HTML5 markup with data-i18n tags
│   ├── styles.css              # Custom responsive glassmorphic styling, animations & SVG rules
│   └── app.js                  # Client-side 0ms router, bilingual dictionaries, and API controllers
├── services/                   # Modular Backend Service Architecture
│   ├── assistant_synthesis.py  # Conversational AI hybrid synthesis engine
│   ├── auth.py                 # Multi-user session management & Argon2 password hashing
│   ├── community_service.py    # Community forum data store & Andhra farmer personas
│   ├── crop_rec_service.py     # Crop recommendation Random Forest inference engine
│   ├── database.py             # User account database and persistence
│   ├── disease_service.py      # MobileNetV2 leaf disease classification engine
│   ├── openai_advisory.py      # ANGRAU offline treatment guidelines & OpenAI fallback
│   ├── retrieval.py            # BM25 + ONNX quantized semantic search engine
│   ├── soil_service.py         # NPK commercial fertilizer bag & split stage calculator
│   ├── weather_service.py      # Live Open-Meteo telemetry & spraying window evaluator
│   └── web_search.py           # Real-time agronomic web search module
├── models/                     # Trained ML Checkpoints & Metadata
│   ├── mobilenetv2_leaf.pt     # MobileNetV2 deep learning weights (97.15% accuracy)
│   ├── crop_recommendation.pkl # Random Forest model bundle & label encoder
│   └── class_names.json        # 38 plant disease class mapping
├── data/                       # Verified Agricultural Datasets & Vectors
│   ├── documents.jsonl         # ANGRAU package of practices text chunks
│   ├── onnx_embeddings.npy     # Multilingual MiniLM embeddings
│   ├── bm25_index.pkl          # BM25 lexical search index
│   ├── community_posts.json    # Forum posts with likes and replies
│   └── farmer_chats.json       # Direct WhatsApp-style chat histories
└── scripts/                    # Model Training & Data Preparation
    ├── prepare_leaf_dataset.py # Leaf dataset verification & directory structuring
    ├── train_leaf_model.py     # PyTorch MobileNetV2 fine-tuning script
    ├── train_crop_recommendation.py # Random Forest model training & evaluation script
    └── fix_leaf_extensions.py  # Image dataset sanitization utility
```

---

## 💻 Running the Application

### 1. Start the Application Server
Run either of the following commands in your terminal or PowerShell:
```bash
python server.py
```
*Or directly via Uvicorn:*
```bash
python -m uvicorn server:app --host 0.0.0.0 --port 8000 --reload
```

### 2. Open Your Browser
Open your browser and navigate to:
```
http://localhost:8000
```

*(Note: Virtual environment activation is completely optional. If using a custom venv on Windows PowerShell, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` if script execution is blocked).*

---

## 👥 Demo Farmer Profiles (1-Tap Quick Access)

The portal provides pre-configured verified farmer profiles for instant evaluation without entering a password:

| Profile | Name | Phone Number | Location | Primary Crop | Land Size |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 👩‍🌾 **Demo 1** | **Archana** | `9440123456` | Vijayawada (Krishna) | Paddy (వరి BPT 5204) | 3.5 Acres |
| 👩‍🌾 **Demo 2** | **Shiney** | `9848054321` | Vijayawada (Krishna) | Chilli (తేజా మిర్చి) | 2.5 Acres |

---

## 📜 Academic Attribution & Citation

If you use or reference **KrishiMitra** in your academic research, project report, or conference proceedings, please cite:

```bibtex
@misc{krishimitra2026,
  author = {Aakarsha Archana and Shiney},
  title = {KrishiMitra: AI-Powered Smart Agricultural Decision Support Platform for Andhra Pradesh Farmers},
  year = {2026},
  course = {B.Tech AIML}
}
```

---

*Engineered with precision for the farming community of Vijayawada and Andhra Pradesh by **Aakarsha Archana & Shiney (B.Tech AIML)**.*
