# 🌾 KrishiMitra (కృషిమిత్ర) — Complete A-Z Project Architecture, Rationale & User Guide

### 👩‍💻 Developed by:
- **Aakarsha Archana** — B.Tech CSE (AIML)
- **Shiney** — B.Tech CSE (AIML)

---

# 📑 Table of Contents
1. [Executive Summary & Background](#1-executive-summary--background)
2. [Why KrishiMitra Was Built](#2-why-krishimitra-was-built)
3. [PART 1: Technology Stack — For Which We Used What and WHY](#part-1-technology-stack--for-which-we-used-what-and-why)
   - [1.1 Backend: FastAPI & Uvicorn ASGI](#11-backend-fastapi--uvicorn-asgi)
   - [1.2 Frontend: Vanilla JS, Semantic HTML5 & Glassmorphism CSS](#12-frontend-vanilla-js-semantic-html5--glassmorphism-css)
   - [1.3 Deep Learning: PyTorch & MobileNetV2 (Leaf Disease Classifier)](#13-deep-learning-pytorch--mobilenetv2-leaf-disease-classifier)
   - [1.4 Machine Learning: Scikit-Learn Random Forest (Crop Recommender)](#14-machine-learning-scikit-learn-random-forest-crop-recommender)
   - [1.5 Conversational AI: Hybrid RAG (BM25 + ONNX MiniLM + Web Search)](#15-conversational-ai-hybrid-rag-bm25--onnx-minilm--web-search)
   - [1.6 Agro-Meteorology: Open-Meteo High-Resolution API](#16-agro-meteorology-open-meteo-high-resolution-api)
   - [1.7 Soil Science: Agronomic NPK Fertilizer Split Calculations](#17-soil-science-agronomic-npk-fertilizer-split-calculations)
   - [1.8 Security & Persistence: Argon2-cffi & Structured JSON Store](#18-security--persistence-argon2-cffi--structured-json-store)
   - [1.9 Localization: 0ms Client-Side Bilingual Engine](#19-localization-0ms-client-side-bilingual-engine)
4. [PART 2: Complete Feature Breakdown](#part-2-complete-feature-breakdown)
   - [2.1 Home Dashboard & Live Telemetry](#21-home-dashboard--live-telemetry)
   - [2.2 Crop Health: AI Leaf Disease Scanner](#22-crop-health-ai-leaf-disease-scanner)
   - [2.3 Live Weather & Spraying Window Advisory](#23-live-weather--spraying-window-advisory)
   - [2.4 Soil Health: NPK Commercial Fertilizer Bag Calculator](#24-soil-health-npk-commercial-fertilizer-bag-calculator)
   - [2.5 Machine Learning Crop Recommendation](#25-machine-learning-crop-recommendation)
   - [2.6 Farmer Connect & WhatsApp-Style Direct Chat](#26-farmer-connect--whatsapp-style-direct-chat)
   - [2.7 Conversational AI Assistant](#27-conversational-ai-assistant)
   - [2.8 Live Andhra Pradesh Mandi Market Rates](#28-live-andhra-pradesh-mandi-market-rates)
   - [2.9 Emergency Helplines & AP Welfare Schemes](#29-emergency-helplines--ap-welfare-schemes)
   - [2.10 Farmer Digital Identity & Profile Management](#210-farmer-digital-identity--profile-management)
   - [2.11 Project Details & Student Innovation (About View)](#211-project-details--student-innovation-about-view)
5. [PART 3: Step-by-Step User Manual — How Users Can Access Each Feature](#part-3-step-by-step-user-manual--how-users-can-access-each-feature)
   - [Step 1: Starting the Platform & Opening in Browser](#step-1-starting-the-platform--opening-in-browser)
   - [Step 2: Signing In (1-Tap Demo vs Registration)](#step-2-signing-in-1-tap-demo-vs-registration)
   - [Step 3: Switching Languages (తెలుగు ⟷ English)](#step-3-switching-languages-తెలుగు--english)
   - [Step 4: Scanning an Affected Crop Leaf](#step-4-scanning-an-affected-crop-leaf)
   - [Step 5: Checking Spraying Window & Weather Forecast](#step-5-checking-spraying-window--weather-forecast)
   - [Step 6: Calculating Fertilizers from Soil Test](#step-6-calculating-fertilizers-from-soil-test)
   - [Step 7: Recommending Crops for New Land](#step-7-recommending-crops-for-new-land)
   - [Step 8: Engaging in Farmer Discussions & Direct Peer Chat](#step-8-engaging-in-farmer-discussions--direct-peer-chat)
   - [Step 9: Consulting the AI Agricultural Assistant](#step-9-consulting-the-ai-agricultural-assistant)
   - [Step 10: Viewing AP Mandi Market Rates](#step-10-viewing-ap-mandi-market-rates)
   - [Step 11: Editing and Customizing Farm Profile](#step-11-editing-and-customizing-farm-profile)

---

# 1. Executive Summary & Background

**KrishiMitra (కృషిమిత్ర)** is an intelligent agricultural decision support system engineered by **Aakarsha Archana** and **Shiney** (B.Tech CSE AIML).

The platform is designed to provide farmers in the **Krishna Delta**, **Guntur**, **Godavari**, and broader **Andhra Pradesh** farming belts with instant, data-driven, and research-backed agricultural guidance directly accessible from mobile phones or desktop browsers.

---

# 2. Why KrishiMitra Was Built

Agriculture in Andhra Pradesh faces several critical challenges that directly impact smallholder farmer livelihood:
1. **Pest & Disease Losses**: Emerging pests such as **Black Thrips (*Thrips parvispinus*)** in Chilli and **Rice Blast (*Magnaporthe oryzae*)** in Paddy cause massive crop damage. Farmers often purchase expensive, incorrect chemicals from local dealers without knowing the exact disease.
2. **NPK Imbalance & Soil Degradation**: Farmers often over-apply Nitrogen (Urea) because it makes crops look instantly greener, leading to pest outbreaks, soil acidification, and wasted money. They lack tools to convert lab NPK readings into actual bag counts.
3. **Pesticide Spray Waste due to Weather**: Spraying pesticides right before rain or in strong winds washes away chemicals or causes spray drift, wasting thousands of rupees per acre and polluting waterways.
4. **Price Asymmetry in Mandis**: Middlemen take advantage of farmers who lack access to real-time daily prices across major AP market yards like Guntur, Vijayawada, Kurnool, and Tenali.
5. **Language Barrier**: Scientific recommendations published by universities (like ANGRAU) are often written in English or academic terms that rural farmers cannot easily understand or access.

**KrishiMitra** solves every single one of these problems within one unified, accessible web portal.

---

# PART 1: Technology Stack — For Which We Used What and WHY

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       KRISHIMITRA TECHNOLOGY STACK                          │
├───────────────────────┬─────────────────────────────────────────────────────┤
│ Component             │ Technology Chosen                                   │
├───────────────────────┼─────────────────────────────────────────────────────┤
│ Backend Server        │ FastAPI (Python 3.10+) + Uvicorn ASGI               │
│ Frontend Architecture │ Vanilla JavaScript + Semantic HTML5 + CSS3 (No Node)│
│ Leaf Disease Vision   │ PyTorch + MobileNetV2 (38 classes, 97.15% accuracy) │
│ Crop Recommendation   │ Scikit-Learn Random Forest Classifier (22 classes)  │
│ AI Conversational RAG │ Hybrid BM25 + ONNX Quantized MiniLM + DDG Web Search│
│ Agro-Meteorology      │ Open-Meteo High-Resolution Telemetry & Geocoding    │
│ Authentication        │ Argon2-cffi Password Hasher + JSON Session Store    │
│ UI & Design Tokens    │ Custom Emerald Glassmorphism CSS3 + Pure SVGs       │
└───────────────────────┴─────────────────────────────────────────────────────┘
```

### 1.1 Backend: FastAPI & Uvicorn ASGI
- **What We Used:** FastAPI framework with Uvicorn ASGI server and Pydantic data validation schemas.
- **Why We Used It Over Flask / Django / Streamlit:**
  - *Streamlit Limitations:* Streamlit re-executes the entire Python script on every button click or slider movement, creating substantial latency (2-5 seconds), consuming excessive server memory, and making mobile browsing sluggish.
  - *FastAPI Benefits:* FastAPI is one of the fastest Python web frameworks available. It utilizes native asynchronous event loops (`asyncio`), processes requests in sub-millisecond times, automatically validates API payloads using Pydantic, and cleanly separates the frontend user interface from backend AI inference engines.

### 1.2 Frontend: Vanilla JS, Semantic HTML5 & Glassmorphism CSS
- **What We Used:** Pure Vanilla JavaScript (ES6+), Semantic HTML5 markup, custom Glassmorphism CSS, and crisp SVG vector icons.
- **Why We Used It Over React / Next.js / Vue:**
  - *Zero Build Tools & Instant Loading:* No `npm`, `webpack`, or Node.js runtime required on the server. The entire frontend loads in under **150 milliseconds** even over 3G/4G rural mobile connections.
  - *0ms Client-Side Routing:* Tab switching (`showTab()`) toggles DOM CSS classes instantaneously without round-tripping to the server.
  - *Clean UI without Emojis:* Employs SVG vector icons for agricultural tools, crop leaves, weather elements, and navigation icons, giving the platform a polished, professional aesthetic.

### 1.3 Deep Learning: PyTorch & MobileNetV2 (Leaf Disease Classifier)
- **What We Used:** A custom deep convolutional neural network based on **MobileNetV2** pre-trained on ImageNet and fine-tuned on **54,305 plant leaf images** across 38 distinct disease classes and healthy foliage.
- **Why We Used MobileNetV2 Over ResNet-50 / VGG-16 / YOLO:**
  - *Depthwise Separable Convolutions:* MobileNetV2 replaces standard 3x3 convolutions with depthwise separable layers, shrinking the model weights down to only **~14 MB** (compared to ~100 MB for ResNet-50 and ~500 MB for VGG-16).
  - *Instant CPU Inference:* Delivers sub-40 millisecond inference directly on standard server CPUs without requiring expensive GPU infrastructure.
  - *Accuracy:* Achieves **97.15% validation accuracy** across 38 classes (including tomato early/late blight, pepper bacterial spot, apple scab, potato blight, etc.).

### 1.4 Machine Learning: Scikit-Learn Random Forest (Crop Recommender)
- **What We Used:** Scikit-Learn **Random Forest Classifier** trained on tabular agricultural soil parameters (Nitrogen, Phosphorus, Potassium, Soil pH) and climatic indicators (Temperature, Relative Humidity, Annual Rainfall) predicting 22 crop classes.
- **Why We Used Random Forest Over Logistic Regression / Neural Networks:**
  - *Non-Linear Boundaries:* Soil-crop relationships are non-linear; for instance, high rainfall favors Paddy but destroys Groundnut, while high Nitrogen benefits Maize but delays flowering in other crops. Decision tree ensembles model these interactions naturally.
  - *Confidence & Probabilities:* Random Forest provides `predict_proba()`, allowing the platform to return not just the top recommended crop, but the top-3 ranked candidate alternatives with exact probability percentages.

### 1.5 Conversational AI: Hybrid RAG (BM25 + ONNX MiniLM + Web Search)
- **What We Used:** A **Hybrid Retrieval-Augmented Generation (RAG)** pipeline combining:
  1. Lexical search via `rank_bm25` over curated ANGRAU package of practices text chunks.
  2. Dense vector search using a quantized ONNX runtime implementation of `paraphrase-multilingual-MiniLM-L12-v2`.
  3. Real-time agricultural web search via DuckDuckGo Search (`duckduckgo-search`).
  4. Specialized synthesis engine grounded in Andhra Pradesh agricultural practices.
- **Why We Used Hybrid RAG Over Plain LLM APIs:**
  - *Zero Hallucination on Chemicals:* Standard general LLMs often hallucinate pesticide brand names, improper chemical concentrations, or illegal banned pesticides. Grounding the response in ANGRAU guidelines ensures safe chemical recommendations.
  - *Offline Capability:* If the external LLM API is unavailable, the specialized dynamic synthesis engine instantly generates structured, highly accurate agronomic advice.
  - *Live Agricultural News & Weather:* General LLMs lack knowledge of today's Vijayawada weather or today's Guntur mandi rates. The web search integration fetches real-time field intelligence dynamically.

### 1.6 Agro-Meteorology: Open-Meteo High-Resolution API
- **What We Used:** Open-Meteo REST API queried with hyper-local coordinates for Vijayawada (`16.5062° N, 80.6480° E`) and 13 Andhra Pradesh districts.
- **Why We Used Open-Meteo Over OpenWeatherMap / AccuWeather:**
  - *No API Key Gatekeeping:* Open-Meteo requires no paid subscription or rate-limited API keys, ensuring uninterrupted service.
  - *High-Resolution Agricultural Telemetry:* Provides precise 10-meter wind speed, soil temperature, relative humidity, and precipitation probability, allowing the automated computation of the **Farmer Spraying Window**.

### 1.7 Soil Science: Agronomic NPK Fertilizer Split Calculations
- **What We Used:** Specialized agronomic formulas converting raw laboratory soil test values (N, P, K in kg/hectare) into actual commercial fertilizer bags per acre:
  - Urea (46% Nitrogen) in 45 kg bags
  - DAP (18% Nitrogen, 46% P₂O₅) in 50 kg bags
  - MOP (Muriate of Potash - 60% K₂O) in 50 kg bags
- **Why We Developed This:**
  - Farmers do not buy elemental "Nitrogen" or "Phosphorus"; they buy commercial bags of Urea and DAP.
  - Over-application of Nitrogen burns crops and attracts pests; under-application lowers yield.
  - The engine splits the total requirement across 3 distinct crop growth stages (Basal, Vegetative Tillering, and Flowering) and calculates Lime or Gypsum amendments for soil pH reclamation.

### 1.8 Security & Persistence: Argon2-cffi & Structured JSON Store
- **What We Used:** Password hashing using **Argon2id** (via `argon2-cffi`) combined with atomic JSON document persistence.
- **Why We Used It:**
  - *Security:* Argon2 is the winner of the Password Hashing Competition (PHC) and the OWASP-recommended standard against GPU brute-force attacks.
  - *Reliability:* Storing user profiles and community forum threads in atomic JSON allows the application to run self-contained without demanding complex external database setup.

### 1.9 Localization: 0ms Client-Side Bilingual Engine
- **What We Used:** Custom DOM-level dictionary internationalization engine covering **178 distinct translation keys** in Telugu (తెలుగు) and English.
- **Why We Used Client-Side Dictionary Over Google Translate Widget:**
  - *Zero Latency:* Translates every element, form input, dropdown option, and telemetry tile in **0 milliseconds** without reloading the page.
  - *Authentic Agronomic Telugu:* Machine translation widgets often butcher local agricultural terminology. Our hand-curated Telugu dictionary uses authentic terms familiar to Krishna Delta farmers (e.g., *వరి అగ్గితెగులు*, *మిర్చి నల్ల తామర పురుగులు*, *యూరియా విడతల మోతాదు*, *జిప్సం సమతుల్యత*).

---

# PART 2: Complete Feature Breakdown

### 2.1 Home Dashboard & Live Telemetry
- **Welcome Hero Banner**: Displays customized farmer greetings, verified farmer ID, land size in acres, and primary crop.
- **Live Vijayawada Weather Banner**: Displays current temperature, weather conditions, relative humidity, and a quick-link button to full meteorology.
- **6 Core Services Cards**: Interactive navigation cards for Disease Scanner, Weather, Soil Health, Crop Recommendation, AI Assistant, and Farmer Forum.
- **Live AP Mandi Market Rates Grid**: Instant view of top crops (Paddy, Chilli, Cotton, Maize, Groundnut, Sugarcane) with expandable view for 15 crops.
- **Emergency Helpline Bar**: Direct toll-free contact numbers for Kisan Call Centre, Rythu Bharosa Kendras, and Krishna KVK.

### 2.2 Crop Health: AI Leaf Disease Scanner
- **Dual Upload System**: Allows farmers to upload an image from mobile gallery or capture live via device camera.
- **Instant Model Inference**: Processes the leaf image through MobileNetV2 and outputs:
  - Detected Crop Name & Disease Diagnosis (or Healthy foliage).
  - Model Confidence Score (e.g., 98.4%).
  - **Organic Remedies**: Neem oil (5ml/L), *Pseudomonas fluorescens*, *Trichoderma viride*, Bordeaux mixture.
  - **Chemical Treatments**: Exact CIBRC-registered active ingredients (e.g., Mancozeb, Copper Oxychloride, Metalaxyl) with exact dilution dosages per liter.
  - **Long-Term Prevention**: Field drainage, crop rotation, solarization, and infected foliage disposal.

### 2.3 Live Weather & Spraying Window Advisory
- **District Selector**: Real-time switching between Vijayawada (Krishna), Guntur, Machilipatnam, Eluru, Rajahmundry, Kakinada, Nellore, Kurnool, Anantapur, Tirupati, and Visakhapatnam.
- **4 Telemetry Metrics**: Temperature, Relative Humidity, Wind Speed & Direction, and Rain Probability.
- **Spraying Window Engine**: Evaluates weather conditions in real-time:
  - *Safe for Spraying (Green)*: Wind speed < 20 km/h and rain probability < 40%. Suggests early morning spraying (7 AM - 10 AM) with wetting agent.
  - *Not Recommended (Red)*: High winds (>20 km/h) or expected rain (>40%) will cause chemical runoff or spray drift.
- **5-Day Agro-Forecast**: Daily maximum/minimum temperature and expected rainfall (mm) for field work planning.

### 2.4 Soil Health: NPK Commercial Fertilizer Bag Calculator
- **Inputs**: Crop selector (14 crops) + Soil pH (4.0 - 9.5) + Nitrogen (kg/ha) + Phosphorus (kg/ha) + Potassium (kg/ha).
- **Outputs**:
  - Total per-acre commercial bag count for **Urea (45kg)**, **DAP (50kg)**, and **MOP (50kg)**.
  - **3-Stage Split Schedule**: Exact proportion to apply at Basal planting, active tillering/vegetative phase, and panicle initiation/flowering phase.
  - **Soil Reclamation Advice**: Automatically calculates Agricultural Lime requirement for acidic soil (pH < 6.5) or Gypsum requirement for alkaline/sodic soil (pH > 7.5).

### 2.5 Machine Learning Crop Recommendation
- **Inputs**: Soil Nitrogen (N), Phosphorus (P), Potassium (K), Soil pH, Temperature (°C), Relative Humidity (%), and Annual Rainfall (mm).
- **Outputs**:
  - Highest-yielding recommended crop suited for the input conditions.
  - Model confidence percentage.
  - Top-3 candidate crops with individual probability rankings.

### 2.6 Farmer Connect & WhatsApp-Style Direct Chat
- **Farmer Community Forum**:
  - Category tags: *Pest & Disease Control*, *Mandi Market Rates*, *Fertilizers*, *Seeds*, and *General Discussion*.
  - Create new posts with custom titles and detailed field inquiries.
  - Interactive **Like** button with instant state update.
  - Collapsible **Replies** thread allowing direct inline comments from fellow farmers.
- **WhatsApp-Style Direct Peer Chat**:
  - Real-time chat interface connected to 4 regional Andhra farmer personas:
    1. **Shiney** (Guntur • Teja Chilli)
    2. **Venkat Reddy** (Kurnool • Groundnut K-6)
    3. **Apparao** (East Godavari • Paddy BPT 5204)
    4. **Srinivasulu** (Anantapur • Horticulture / Sweet Orange)
  - Features typing indicator, online presence status, quick inquiry preset buttons (*Market Rates*, *Black Thrips*, *Gypsum Dose*, *Rain Outlook*), and agronomic responses.

### 2.7 Conversational AI Assistant
- **Natural Language Interaction**: Farmers can ask questions in Telugu, English, or conversational mixed text.
- **Quick Inquiry Chips**: Instant one-click queries for *Paddy Blast*, *Chilli Black Thrips*, *Urea & DAP Dosage*, *Vijayawada Weather*, *PM-Kisan & Welfare Schemes*, and *Jeevamrutham Preparation*.
- **Comprehensive Answers**: Returns structured markdown responses detailing key scientific findings, exact chemical dosages, organic alternatives, and local RBK contact recommendations.

### 2.8 Live Andhra Pradesh Mandi Market Rates
- **15 Tracked Commodities**:
  - *Cereals*: Paddy (BPT 5204), Maize (Corn)
  - *Spices*: Teja Chilli, Duggirala Turmeric
  - *Commercial*: Cotton (Bunny), Sugarcane, Virginia Tobacco
  - *Oilseeds*: Groundnut (K-6)
  - *Pulses*: Blackgram (Urad), Redgram (Toor)
  - *Vegetables*: Tomato (Grade A), Bellary Onion
  - *Fruits*: Banganapalli Mango, Karpura Banana, Sweet Orange (Mosambi)
- Displays current price, price units (per Quintal, per Ton, per Crate, per Bunch), market yard location, and percentage price movement trend.

### 2.9 Emergency Helplines & AP Welfare Schemes
- Instant contact cards for official government agricultural assistance:
  - **Kisan Call Centre**: 1800-180-1551 (Toll-Free, 22 languages)
  - **Rythu Bharosa Kendra (RBK)**: 155251 (Village level agronomy support)
  - **Krishna Krishi Vigyan Kendra (KVK, Garikapadu)**: 08674-245236

### 2.10 Farmer Digital Identity & Profile Management
- Displays farmer credentials: Name, registered mobile number, district, village, primary crop, land size in acres, soil nature, and enrolled welfare schemes (PM-Kisan, YSR Rythu Bharosa).
- **Interactive Edit Mode**: Farmers can edit full name, phone number, district, village/mandal, crop, and land acreage, persisting changes instantly across the entire dashboard.

### 2.11 Project Details & Developers (About View)
- Features developer profiles of **Aakarsha Archana** and **Shiney** (B.Tech CSE AIML).
- Details the technical architecture of the MobileNet vision model, Open-Meteo telemetry, and Hybrid RAG.

---

# PART 3: Step-by-Step User Manual — How Users Can Access Each Feature

### Step 1: Starting the Platform & Opening in Browser
1. Open PowerShell or Terminal in the project root directory.
2. Launch the application server:
   ```bash
   python -m uvicorn server:app --host 0.0.0.0 --port 8000 --reload
   ```
3. Open your browser and visit: **`http://localhost:8000`**

---

### Step 2: Signing In (1-Tap Demo vs Registration)
1. **1-Tap Quick Access (Recommended)**:
   - On the login screen, click **Archana (అర్చన)** or **Shiney (షైనీ)** to enter the dashboard instantly without entering a password.
2. **Standard Mobile Sign In**:
   - Enter your registered phone number (e.g., `9440123456`) and password (`demo123`).
3. **Register New Account**:
   - Click the **📝 New Registration** tab.
   - Enter your name, 10-digit mobile number, district, primary crop, land acreage, and password.
   - Click **Register New Account** to create and log in to your custom farmer dashboard.

---

### Step 3: Switching Languages (తెలుగు ⟷ English)
1. Locate the language toggle in the **left sidebar** (`🇮🇳 తెలుగు` / `🌐 English`) or the top header bar.
2. Click **🌐 English** to switch all navigation items, cards, inputs, dropdowns, and weather advisories to English.
3. Click **🇮🇳 తెలుగు** to switch the entire application back to Telugu.
4. *Notice*: The change is instantaneous (0ms) with zero page reload.

---

### Step 4: Scanning an Affected Crop Leaf
1. Click **Crop Health (తెగుళ్ల స్కానర్)** from the sidebar menu or click **Scan Leaf Now** on the home dashboard.
2. Click the upload box or drag-and-drop a photo of an affected plant leaf (supports JPG, PNG, or WEBP up to 10 MB).
3. A preview of the selected leaf will appear.
4. Click **Start AI Disease Analysis (ఆకును విశ్లేషించండి)**.
5. In less than 1 second, the platform displays:
   - Disease Name & Confidence Percentage.
   - 🌿 **Organic Remedies** (biological and herbal sprays).
   - 🧪 **Chemical Treatments** (exact active ingredients and dosage per liter).
   - 🛡️ **Long-Term Prevention Protocols**.

---

### Step 5: Checking Spraying Window & Weather Forecast
1. Click **Live Weather (ప్రత్యక్ష వాతావరణం)** from the sidebar.
2. Choose your district from the dropdown (default: *Vijayawada (Krishna)*).
3. Review the **Spraying Window Banner**:
   - If **Green**: Weather is optimal. Proceed with early morning spraying.
   - If **Red**: High winds or rain expected. Delay chemical spraying to prevent chemical wash-off.
4. Scroll down to review the **5-Day Agro-Forecast** cards showing daily high/low temperatures and expected rainfall in mm.

---

### Step 6: Calculating Fertilizers from Soil Test
1. Click **Soil Health (నేల ఆరోగ్యం)** from the sidebar.
2. Select your crop (e.g., *Paddy*, *Chilli*, *Cotton*, *Maize*).
3. Adjust the sliders according to your Soil Health Card:
   - Soil pH (e.g., `6.8`)
   - Nitrogen (N) kg/ha (e.g., `180`)
   - Phosphorus (P) kg/ha (e.g., `22`)
   - Potassium (K) kg/ha (e.g., `140`)
4. Click **Calculate Fertilizer Doses (ఎరువుల మోతాదును విశ్లేషించండి)**.
5. Review the output card:
   - Total commercial bags of Urea, DAP, and MOP required per acre.
   - **3-Stage Split Timing**: Exact bags to apply at Basal planting, active tillering, and flowering.
   - Lime or Gypsum requirement for soil reclamation.

---

### Step 7: Recommending Crops for New Land
1. Click **Crop Advisory (పంట సిఫార్సు)** from the sidebar.
2. Enter your soil N-P-K readings, soil pH, local temperature, humidity, and annual rainfall (mm).
3. Click **Calculate Suitable Crop (అనువైన పంటను లెక్కించండి)**.
4. Review the AI recommendation card showing the primary recommended crop with model confidence and top-3 ranked alternatives.

---

### Step 8: Engaging in Farmer Discussions & Direct Peer Chat
1. Click **Farmer Chat (రైతు వేదిక)** from the sidebar.
2. **Community Forum (Left Side)**:
   - Filter discussions by clicking chips: *All*, *Pests*, *Market*, *Fertilizers*, or *Seeds*.
   - To post a new query: Select a category, enter a title and message, and click **Publish Post**.
   - To like a post: Click the **👍 Like** button.
   - To reply: Click **💬 Replies**, type your comment, and click **Reply**.
3. **Direct 1-on-1 Farmer Chat (Right Side)**:
   - Click any farmer persona pill at the top: **Shiney** (Chilli), **Venkat Reddy** (Groundnut), **Apparao** (Paddy), or **Srinivasulu** (Horticulture).
   - Click a quick prompt (e.g., *💰 Market Rates* or *🌶️ Black Thrips*) or type your message into the input bar and press Enter.
   - Observe the live typing indicator (*"✍️ Fellow farmer is typing..."*) followed by an instant agronomic response.

---

### Step 9: Consulting the AI Agricultural Assistant
1. Click **AI Assistant (AI అసిస్టెంట్)** from the sidebar.
2. Click any of the pre-configured prompt chips (e.g., *🌾 Rice Blast Control*, *🌶️ Chilli Black Thrips*, *🧪 Urea & DAP Dosage*, or *⛅ Vijayawada Weather*).
3. Or type any free-form farming question in Telugu or English into the bottom text box and press Enter.
4. The assistant performs hybrid retrieval over ANGRAU documents and live agricultural web sources to deliver a structured, actionable advisory.

---

### Step 10: Viewing AP Mandi Market Rates
1. On the **Home** dashboard, scroll down to the **Live Andhra Pradesh Mandi Market Rates** section.
2. Review the top-6 primary crops (Paddy, Chilli, Cotton, Maize, Groundnut, Sugarcane) with live prices and mandi yards.
3. Click **🔽 Show All Crop Prices (15 Crops)** to expand the full table, displaying prices for Tomato, Blackgram, Redgram, Turmeric, Onion, Tobacco, Mango, Banana, and Orange.
4. Click **⬆️ Show Top Crops Only** to collapse back to the compact view.

---

### Step 11: Editing and Customizing Farm Profile
1. Click **Profile (రైతు ప్రొఫైల్)** from the sidebar.
2. Review your digital farmer identity card and 4 quick agro-metric cards.
3. Click **Edit Profile (ప్రొఫైల్ సవరించండి)**.
4. Modify your full name, mobile number, district, village/mandal, primary crop, or land size in acres.
5. Click **💾 Save Changes (వివరాలు భద్రపరచండి)**.
6. The updated profile details will immediately update across the entire application.

---

# 🎓 Attribution & Recognition

This project stands as a testament to practical engineering applied to rural and grassroots agricultural development. 

- **Developers**: **Aakarsha Archana** & **Shiney**
- **Course**: **B.Tech CSE (AIML)**
- **Year of Development**: 2026

*Empowering Andhra Pradesh farmers through intelligent, accessible, and compassionate technology.*
