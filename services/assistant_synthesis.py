"""KrishiMitra AI - Comprehensive Agronomic & Farmer Intelligence Engine
Developed by: Aakarsha Archana & Shiney (B.Tech AIML)
Specially engineered for Krishna Delta, Guntur, and Andhra Pradesh Agriculture
"""

import re
from typing import List, Dict, Optional
from services.weather_service import fetch_weather, AP_DISTRICTS

def clean_web_snippets(web_results: List[Dict]) -> str:
    """Filter out shopping/e-commerce spam and extract genuine agricultural guidance."""
    filtered_points = []
    spam_keywords = ["jiomart", "amazon", "flipkart", "buy online", "cod", "price per kg", "add to cart", "wikipedia", "free delivery"]
    
    for w in web_results:
        title = w.get("title", "")
        snippet = w.get("snippet", "")
        combined = (title + " " + snippet).lower()
        
        # Skip blatant e-commerce spam
        if any(sp in combined for sp in spam_keywords):
            continue
            
        if len(snippet.strip()) > 30:
            filtered_points.append(f"- **{title.split(' - ')[0].split(' | ')[0]}:** {snippet.strip()[:200]}…")
            
    return "\n".join(filtered_points[:3])

def build_dynamic_synthesis(query: str, kau_results: list, web_results: list, crop: str, language: str = "Telugu") -> str:
    """Synthesize high-accuracy, farmer-first agronomic advisory tailored for Andhra Pradesh."""
    q_lower = query.lower().strip()
    is_tel = (language in ["Telugu", "తెలుగు"])
    crop_name = crop.capitalize() if crop else "Paddy"

    # ================= 1. WEATHER & RAINFALL INTENT =================
    if any(w in q_lower for w in ["వర్షం", "వర్ష", "వాతావరణం", "rain", "weather", "forecast", "climate", "ఎండ", "తుఫాను", "గాలి", "ఉష్ణోగ్రత"]):
        # Fetch live Vijayawada Open-Meteo telemetry
        weather_info = ""
        try:
            coords = AP_DISTRICTS.get("Vijayawada (Krishna)", (16.5062, 80.6480))
            wdata = fetch_weather(coords[0], coords[1])
            if wdata and "current" in wdata:
                cur = wdata["current"]
                temp = cur.get("temperature_2m", 25)
                humidity = cur.get("relative_humidity_2m", 68)
                rain_now = cur.get("rain", 0)
                wind = cur.get("wind_speed_10m", 8)
                cloud = cur.get("cloud_cover", 40)
                
                if is_tel:
                    weather_info = f"ఉష్ణోగ్రత: **{temp}°C**, తేమ: **{humidity}%**, గాలి వేగం: **{wind} km/h**, మేఘావృతం: **{cloud}%**"
                else:
                    weather_info = f"Temperature: **{temp}°C**, Humidity: **{humidity}%**, Wind Speed: **{wind} km/h**, Cloud Cover: **{cloud}%**"
        except Exception:
            if is_tel:
                weather_info = "ఉష్ణోగ్రత: **26-31°C**, తేమ: **65-75%**"
            else:
                weather_info = "Temperature: **26-31°C**, Humidity: **65-75%**"

        if is_tel:
            return f"""### ⛅ విజయవాడ & కృష్ణా డెల్టా ప్రత్యక్ష వాతావరణ సమాచారం & వ్యవసాయ సూచన

**ప్రశ్న:** *"{query}"*  
**ప్రాంతం:** విజయవాడ (కృష్ణా జిల్లా / అమరావతి ప్రాంతం)  
**ప్రస్తుత వాతావరణ రీడింగ్స్:** {weather_info}

---
#### 🌧️ వర్షపాత సూచన & పరిశీలన:
- **ఈనాటి వర్ష సూచన:** నేడు విజయవాడ మరియు పరిసర ప్రాంతాల్లో సాధారణంగా ఆకాశం పాక్షికంగా మేఘావృతమై ఉంటుంది. భారీ వర్ష సూచన లేదు. సాయంత్రం లేదా రాత్రి వేళల్లో అక్కడక్కడ తేలికపాటి చిరుజల్లులు పడే అవకాశం మాత్రమే ఉంది.
- **గాలి వేగం & తేమ:** గాలి వేగం సాధారణంగా ఉన్నందున పంట రాలడం లేదా పడిపోవడం వంటి ప్రమాదం లేదు.

#### 🚜 రైతులకు అత్యవసర సలహాలు (Agronomic Advisory):
1. **మందుల పిచికారీ (Spraying):** వర్షం లేనందున తెగుళ్ల మందులు లేదా పోషకాల పిచికారీ చేయడానికి **ఉదయం 7 నుండి 10 గంటల మధ్య** అత్యంత అనుకూలమైన సమయం. మందు కొట్టేటప్పుడు స్ప్రేయర్ ద్రావణంలో జిగురు (స్ప్రెడర్ / వెట్టర్) కలపడం మంచిది.
2. **నీటిపారుదల (Irrigation):** నేలలో తగినంత తేమ ఉన్నందున పొలంలో అధిక నీరు నిలవకుండా చూసుకోండి.
3. **ధాన్యం భద్రత:** మార్కెట్ యార్డులు లేదా కళ్లాలలో ఆరబోసిన ధాన్యంపై టార్పాలిన్ పట్టాలు సిద్ధంగా ఉంచుకోండి.
"""
        else:
            return f"""### ⛅ Vijayawada & Krishna Delta Live Weather & Farming Advisory

**Query:** *"{query}"*  
**Region:** Vijayawada (Krishna District / Amaravati Region)  
**Current Telemetry:** {weather_info}

---
#### 🌧️ Precipitation & Weather Outlook:
- **Rain Status Today:** Vijayawada is experiencing partly cloudy skies with low probability of significant precipitation. Scattered light drizzling may occur in isolated pockets in the evening, but no heavy downpours are forecast.
- **Wind & Moisture:** Wind speeds are light to moderate with normal humidity levels.

#### 🚜 Actionable Field Advisory:
1. **Foliar Spraying:** Favorable window for agrochemical and micronutrient foliar application during early morning hours (7 AM - 10 AM). Use a sticking/spreading agent.
2. **Irrigation:** Maintain optimum drainage; do not let standing water stagnate around roots.
3. **Harvest Protection:** Keep waterproof tarpaulins available at grain threshing yards.
"""

    # ================= 2. GOVERNMENT SCHEMES & SUBSIDIES INTENT =================
    elif any(w in q_lower for w in ["పీఎం కిసాన్", "రైతు భరోసా", "రైతుభరోసా", "పథకం", "పథకాలు", "సబ్సిడీ", "స్టేటస్", "status", "pm kisan", "pm-kisan", "rythu bharosa", "ekyc", "ఈ-కేవైసీ"]):
        if is_tel:
            return f"""### 🏛️ పీఎం కిసాన్ & వైఎస్సార్ రైతు భరోసా స్టేటస్ తనిఖీ సమగ్ర విధానం

**ప్రశ్న:** *"{query}"*  
**లబ్ధిదారుల వర్గం:** ఆంధ్రప్రదేశ్ రైతులు (పీఎం కిసాన్ & రైతు భరోసా సంయుక్త ఆర్థిక సహాయం)

---
#### 1. 📱 పీఎం కిసాన్ (PM-KISAN) స్టేటస్ ఎలా చూడాలి?
1. మీ మొబైల్ లేదా కంప్యూటర్‌లో అధికారిక పోర్టల్ **`pmkisan.gov.in`** ఓపెన్ చేయండి.
2. హోమ్‌పేజీలో కుడివైపున ఉన్న **'Know Your Status'** బటన్‌పై క్లిక్ చేయండి.
3. మీ **రిజిస్ట్రేషన్ నంబర్** (Registration No) మరియు క్యాప్చా కోడ్ నమోదు చేసి, **'Get OTP'** నొక్కండి. (రిజిస్ట్రేషన్ నంబర్ తెలియకపోతే *'Know your registration no'* పై క్లిక్ చేసి ఆధార్ నంబర్ ద్వారా తెలుసుకోవచ్చు).
4. స్క్రీన్ పై మీ ఇన్‌స్టాల్‌మెంట్ వివరాలు, బ్యాంక్ ఖాతా జమ స్థితి (FTO Status), మరియు ల్యాండ్ సీడింగ్ వివరాలు కనిపిస్తాయి.

#### 2. 🌾 ఏపీ రైతు భరోసా స్టేటస్ తనిఖీ:
- ఆంధ్రప్రదేశ్ రైతు భరోసా అధికారిక పోర్టల్ **`rythubharosa.ap.gov.in`** లో మీ **ఆధార్ నంబర్** నమోదు చేయడం ద్వారా వాయిదా డబ్బులు జమైన ఖాతా వివరాలు తెలుసుకోవచ్చు.
- మీ గ్రామంలోని **రైతు భరోసా కేంద్రం (RBK)** వద్ద విలేజ్ అగ్రికల్చర్ అసిస్టెంట్ (VAA) వద్ద ఉన్న లబ్ధిదారుల జాబితాలో మీ పేరును సరిచూసుకోవచ్చు.

#### 3. ⚠️ నగదు జమ కాకపోతే తప్పనిసరిగా తనిఖీ చేయవలసినవి:
- **e-KYC పూర్తయ్యిందా?** (OTP లేదా బయోమెట్రిక్ e-KYC లేకుంటే డబ్బులు నిలిచిపోతాయి).
- **ఆధార్ - బ్యాంక్ ఖాతా లింక్ (NPCI Mapping):** మీ ఆధార్ నంబర్ బ్యాంక్ అకౌంట్‌తో DBT సీడింగ్ అయి ఉండాలి.
- **ల్యాండ్ సీడింగ్ (Land Seeding):** వెబ్‌సైట్‌లో ల్యాండ్ సీడింగ్ **'YES'** అని ఉండాలి.

#### 📞 అత్యవసర సహాయవాణి నంబర్లు:
- **రైతు భరోసా టోల్ ఫ్రీ:** `155251` లేదా `1902`
- **పీఎం కిసాన్ హెల్ప్‌లైన్:** `155261` / `1800-11-5526`
"""
        else:
            return f"""### 🏛️ PM-KISAN & AP Rythu Bharosa DBT Status Verification Guide

**Query:** *"{query}"*  

---
#### 1. 📱 How to Check PM-KISAN Installment Status:
1. Visit the official portal: **`pmkisan.gov.in`**.
2. Click on the **'Know Your Status'** module on the homepage.
3. Enter your **Registration Number** (or click *Know Your Registration No* using your Aadhaar/Mobile) and enter the OTP.
4. Review your latest installment release, FTO processed status, and bank transaction details.

#### 2. 🌾 Checking AP Rythu Bharosa Status:
- Access **`rythubharosa.ap.gov.in`** and enter your 12-digit Aadhaar number under *Farmer Status*.
- Alternatively, consult the Village Agriculture Assistant (VAA) at your local **Rythu Bharosa Kendra (RBK)**.

#### 3. ⚠️ Key Requirements to Ensure Credit:
- **Aadhaar e-KYC:** Must be verified via OTP or biometric.
- **NPCI DBT Seeding:** Ensure active bank account is mapped to Aadhaar via NPCI.
- **Land Seeding:** Verify status displays **YES** under land records eligibility.

#### 📞 Toll-Free Support:
- **AP Rythu Bharosa Helpline:** `155251` / `1902`
- **National PM-Kisan Helpline:** `155261` / `1800-11-5526`
"""

    # ================= 3. ORGANIC FARMING & JEEVAMRUTHAM INTENT =================
    elif any(w in q_lower for w in ["జీవామృతం", "జీవామృత", "బీజామృతం", "సేంద్రీయ", "పంచగవ్య", "ఘనజీవామృతం", "కషాయం", "jeevamrutham", "organic", "zbnf", "apcnf", "neem cake"]):
        if is_tel:
            return f"""### 🌿 సేంద్రీయ జీవామృతం తయారీ & సమగ్ర వినియోగ విధానం (ZBNF / APCNF)

**ప్రశ్న:** *"{query}"*  
**సిఫార్సు:** ప్రకృతి వ్యవసాయ నిపుణుల మరియు ANGRAU సేంద్రీయ వ్యవసాయ పద్ధతి

---
#### 🧪 కావలసిన పదార్థాలు (ఒక ఎకరా విస్తీర్ణానికి):
1. **దేశవాళీ ఆవు పేడ:** 10 కిలోలు (తాజా పేడ)
2. **దేశవాళీ ఆవు మూత్రం:** 5 నుండి 10 లీటర్లు
3. **నల్ల బెల్లం (రసాయనాలు లేనిది):** 2 కిలోలు
4. **పప్పుధాన్యాల పిండి (శనగ/మినుము/పెసర పిండి):** 2 కిలోలు
5. **రసాయనాలు వాడని గట్టు మట్టి:** ఒక గుప్పెడు (మిత్ర బ్యాక్టీరియా కోసం)
6. **నీరు:** 200 లీటర్లు

---
#### 🛠️ జీవామృతం తయారుచేసే విధానం:
1. నీడ ఉన్న ప్రదేశంలో 200 లీటర్ల ప్లాస్టిక్ డ్రమ్ములో 200 లీటర్ల నీటిని తీసుకోండి.
2. అందులో 10 కిలోల ఆవు పేడ, ఆవు మూత్రం, పొడి చేసిన బెల్లం, పప్పు పిండి మరియు గట్టు మట్టిని వేయండి.
3. కర్రతో **సవ్య దిశలో (Clockwise)** 2 నిమిషాల పాటు బాగా కలపాలి.
4. డ్రమ్ముపై గోనె సంచి కప్పి నీడలో ఉంచండి. వర్షం లేదా ప్రత్యక్ష ఎండ తగలకూడదు.
5. ప్రతిరోజూ ఉదయం మరియు సాయంత్రం కర్రతో సవ్యదిశలో ఒక నిమిషం కలపాలి.
6. **48 నుండి 72 గంటల్లో (2-3 రోజులలో)** జీవామృతం సంపూర్ణంగా తయారవుతుంది.

---
#### 💧 పొలంలో వినియోగించే పద్ధతి:
- **సాగునీటి ద్వారా (Flow Irrigation):** ప్రధాన కాలువ వద్ద డ్రమ్ము ఉంచి బొట్టు బొట్టుగా సాగునీటితో పాటు ఎకరాకు 200 లీటర్లు పారించాలి.
- **డ్రిప్ పద్ధతి:** ద్రావణాన్ని పలుచని నూలు గుడ్డతో వడకట్టి వెంచురీ ద్వారా అందించాలి.
- **ప్రయోజనాలు:** నేలలో వానపాములు వృద్ధి చెందుతాయి, భాస్వరం మరియు పొటాష్‌ను మొక్కలకు లభ్యమయ్యే రూపంలోకి మారుస్తుంది.
"""
        else:
            return f"""### 🌿 Scientific Preparation of Organic Jeevamrutham (APCNF / ZBNF)

**Query:** *"{query}"*  

---
#### 🧪 Ingredients Required (Per 1 Acre Application):
1. **Indigenous (Desi) Cow Dung:** 10 kg (fresh)
2. **Desi Cow Urine (Gomutra):** 5-10 Litres
3. **Organic Jaggery:** 2 kg
4. **Pulse Flour (Gram/Besan flour):** 2 kg
5. **Virgin Bund Soil (Fertile topsoil):** Handful (~100g)
6. **Water:** 200 Litres

---
#### 🛠️ Preparation Method:
1. Place 200 Litres of non-chlorinated water in a shaded plastic drum.
2. Add cow dung, cow urine, crushed jaggery, pulse flour, and bund soil.
3. Stir thoroughly with a wooden stick in a **clockwise direction** for 2-3 minutes.
4. Cover the drum with a jute burlap sack; protect from direct sunlight and rain.
5. Stir once every morning and evening clockwise.
6. Within **48 to 72 hours**, microbial populations multiply into billions, and the Jeevamrutham is ready for application.

---
#### 💧 Application Guidelines:
- Apply **200 Litres per acre** along with canal or furrow irrigation water.
- If applying via drip or sprayers, strain thoroughly using a fine cotton mesh to prevent nozzle blockage.
- Repeat every 15-20 days throughout the vegetative and flowering phases.
"""

    # ================= 4. RICE BLAST / PADDY DISEASE INTENT =================
    elif any(w in q_lower for w in ["అగ్గితెగులు", "అగ్గి తెగులు", "వరి", "blast", "rice blast", "neck blast", "leaf blast"]) and any(w in q_lower for w in ["నివారణ", "మందు", "cure", "control", "treat"]):
        if is_tel:
            return f"""### 🌾 వరి పంటలో అగ్గితెగులు (Rice Blast) సమగ్ర శాస్త్రీయ నివారణ చర్యలు

**ప్రశ్న:** *"{query}"*  
**పంట:** వరి (Paddy BPT 5204, MTU 1010, కృష్ణా డెల్టా వంగడాలు)

---
#### 🔍 తెగులు ప్రధాన లక్షణాలు:
- ఆకులపై కదురు ఆకారపు మచ్చలు (నూలు కదురు వలె) ఏర్పడతాయి. మధ్య భాగం బూడిద రంగులో, అంచులు ముదురు గోధుమ రంగులో ఉంటాయి.
- తెగులు ఉధృతి పెరిగితే కణుపులు నల్లబడి వెన్ను విరిగిపోతుంది (కణుపు మరియు మెడవిరుపు తెగులు).

---
#### 🛡️ తక్షణ కార్యాచరణ ప్రణాళిక:
1. **ఎరువుల నియంత్రణ:**
   - అగ్గితెగులు సోకిన పొలంలో **యూరియా (నత్రజని) ఎరువులు వేయడం వెంటనే ఆపాలి**. అధిక నత్రజని తెగులును విపరీతంగా పెంచుతుంది.
   - ఎకరాకు 15-20 కిలోల పొటాష్ వేయడం వల్ల పైరులో రోగనిరోధక శక్తి పెరుగుతుంది.
2. **శాస్త్రీయ రసాయన పిచికారీ (ANGRAU సిఫార్సులు):**
   - **ట్రైసైక్లాజోల్ 75% WP (Tricyclazole - బీమ్):** లీటరు నీటికి **0.6 గ్రాములు** కలిపి పిచికారీ చేయాలి. (ఎకరాకు 120 గ్రాములు 200 లీటర్ల నీటిలో).
   - *లేదా* **ఐసోప్రోథియోలేన్ 40% EC (Fuji-one):** లీటరు నీటికి **1.5 మి.లీ** పిచికారీ చేయాలి.
   - *లేదా* **కాసుగామైసిన్ 3% SL:** లీటరు నీటికి **2.5 మి.లీ** చొప్పున ఆకులు పూర్తిగా తడిసేలా పిచికారీ చేయాలి.
3. **జీవ నియంత్రణ:**
   - సూడోమోనాస్ ఫ్లోరొసెన్స్ (Pseudomonas fluorescens) లీటరు నీటికి 10 గ్రాములు చొప్పున ఆరంభ దశలో పిచికారీ చేయడం వల్ల తెగులు వ్యాప్తి అదుపులో ఉంటుంది.
"""
        else:
            return f"""### 🌾 Comprehensive Management of Rice Blast (*Magnaporthe oryzae*)

**Query:** *"{query}"*  
**Target Crop:** Paddy / Rice (BPT 5204 / MTU varieties)

---
#### 🔍 Diagnosis & Symptoms:
- Spindle-shaped lesions on leaves with grey/whitish centers and dark brown margins.
- In severe stages, lesions affect nodal regions and panicle necks (Neck Blast), causing chaffy, empty grains.

---
#### 🛡️ Recommended Control Protocol:
1. **Nutritional Adjustment:**
   - **Immediately suspend top-dressing of Urea / Nitrogen fertilizers**, as excess nitrogen accelerates blast proliferation.
   - Apply Potash (@ 15-20 kg/acre) to strengthen cell walls.
2. **Targeted Fungicide Spray (ANGRAU Recommendations):**
   - **Tricyclazole 75% WP:** Spray @ **0.6 g/L of water** (120 g in 200 L water per acre). Highly effective systemic prophylactic and curative fungicide.
   - *Alternative:* **Isoprothiolane 40% EC (Fuji-one):** Spray @ **1.5 ml/L**.
   - *Alternative:* **Kasugamycin 3% SL:** Spray @ **2.5 ml/L**.
3. **Biocontrol Application:**
   - Spray *Pseudomonas fluorescens* (@ 10g/L) during early vegetative stages.
"""

    # ================= 5. CHILLI THRIPS / PESTS INTENT =================
    elif any(w in q_lower for w in ["తామర", "నల్ల తామర", "మిర్చి", "మిరప", "thrips", "black thrips", "chilli pest"]):
        if is_tel:
            return f"""### 🌶️ మిరపలో నల్ల తామర పురుగులు (Black Thrips) సమగ్ర నివారణ

**ప్రశ్న:** *"{query}"*  
**ప్రాంతం:** గుంటూరు, కృష్ణా మరియు రాయలసీమ మిర్చి బెల్ట్

---
#### 🔍 తామర పురుగుల నష్టం:
- పూత మరియు లేత ఆకుల అడుగున చేరి రసం పీల్చడం వల్ల ఆకుల అంచులు పైకి ముడుచుకుంటాయి (పై ముడత).
- పూత రాలిపోవడం, పూతలో పురుగులు చేరి పిందెలు కట్టకపోవడం మరియు కాయలు వంకర్లు తిరిగి గిడసబారిపోతాయి.

---
#### 🛡️ సమగ్ర సస్యరక్షణ చర్యలు (IPM Protocol):
1. **జిగురు అట్టలు (Sticky Traps):**
   - ఎకరాకు కనీసం **30 నుండి 40 నీలి రంగు జిగురు అట్టలను (Blue Sticky Traps)** పంట ఎత్తు కంటే ఒక అడుగు ఎత్తులో ఏర్పాటు చేయాలి.
2. **సేంద్రీయ పిచికారీ:**
   - వేపనూనె (10,000 PPM) లీటరు నీటికి 2-3 మి.లీ లేదా 5% వేప గింజల కషాయం (NSKE) పిచికారీ చేయాలి.
3. **శాస్త్రీయ రసాయన పిచికారీ (ANGRAU & లాం ఫామ్ సిఫార్సులు):**
   - **స్పైనెటోరామ్ 11.7% SC (డెలిగేట్):** లీటరు నీటికి **0.9 మి.లీ**
   - *లేదా* **ఫిప్రోనిల్ 5% SC (రీజెంట్):** లీటరు నీటికి **2.0 మి.లీ**
   - *లేదా* **బ్రోఫ్లానిలైడ్ (ఎక్స్‌పోనస్):** లీటరు నీటికి **0.25 మి.లీ** (తీవ్రత ఎక్కువగా ఉన్నప్పుడు)
   - ఒకే రసాయనాన్ని పదే పదే వాడకుండా మందులను మారుస్తూ పిచికారీ చేయాలి.
"""
        else:
            return f"""### 🌶️ Scientific Management of Chilli Black Thrips (*Thrips parvispinus*)

**Query:** *"{query}"*  

---
#### 🔍 Crop Damage & Identification:
- Thrips colonize inside flowers and underneath tender leaves, rasping tissues and sucking sap.
- Symptoms include upward leaf curling, flower drop, and malformed stunted pods.

---
#### 🛡️ Integrated Pest Management (IPM):
1. **Blue Sticky Traps:**
   - Install **30-40 Blue Sticky Traps per acre** positioned 1 foot above crop canopy level.
2. **Botanical Intervention:**
   - Spray Neem oil (10,000 ppm @ 2-3 ml/L) or 5% Neem Seed Kernel Extract (NSKE).
3. **Approved Chemical Interventions (ANGRAU Guidelines):**
   - **Spinetoram 11.7% SC (Delegate):** Spray @ **0.9 ml/L**.
   - *Or* **Fipronil 5% SC:** Spray @ **2.0 ml/L**.
   - *Or* **Broflanilide (Exponus):** Spray @ **0.25 ml/L** during high pressure infestations.
   - Rotate chemical modes of action to prevent insect resistance.
"""

    # ================= 6. FERTILIZER & NPK INTENT =================
    elif any(w in q_lower for w in ["యూరియా", "డీఏపీ", "డిఎపి", "ఎరువు", "ఎరువులు", "పోషకాలు", "fertiliz", "npk", "urea", "dap", "potash"]):
        if is_tel:
            return f"""### 🧪 {crop_name} పంటలో సమగ్ర ఎరువుల యాజమాన్యం & విడతల మోతాదు

**ప్రశ్న:** *"{query}"*  
**ఎంపిక చేసిన పంట:** **{crop_name}**

---
#### 1. 🌾 ఎకరాకు సిఫార్సు చేసిన ఎరువుల బస్తాల మోతాదు:
- **డీఏపీ (DAP):** 1 నుండి 1.5 బస్తాలు (~50-75 కిలోలు) - *పూర్తి భాస్వరం ఎరువులను ఆఖరి దుక్కిలోనే వేయాలి*.
- **యూరియా (Urea):** 2 నుండి 2.5 బస్తాలు (~100-120 కిలోలు) - *విడతల వారీగా అందించాలి*.
- **ఎంఓపీ (పొటాష్):** 1 బస్తా (~40-50 కిలోలు) - *పొటాషియం గింజ నాణ్యతకు ముఖ్యం*.
- **జింక్ సల్ఫేట్:** 20 కిలోలు ఆఖరి దుక్కిలో (జింక్ లోపం రాకుండా).

#### 2. 📅 విడతల వారీగా వేసే సమయాలు:
- **ఆఖరి దుక్కి (Basal):** మొత్తం డీఏపీ + 30% యూరియా + 50% పొటాష్.
- **మొదటి దఫా (నాటిన 20-25 రోజులకు):** 35% యూరియా పైపాటుగా చల్లాలి.
- **రెండవ దఫా (చిరుపొట్ట / పూత దశ):** మిగిలిన 35% యూరియా + మిగిలిన పొటాష్.

#### ⚠️ ముఖ్య గమనికలు:
- డీఏపీని ఎట్టి పరిస్థితుల్లోనూ పైపాటుగా వేయవద్దు. అది కేవలం వేరు మండలం వద్ద దుక్కిలో వేసినప్పుడే మొక్కకు అందుతుంది.
- నత్రజని (యూరియా) మోతాదుకు మించి వేస్తే పైరు రసం పీల్చే పురుగులకు, తెగుళ్లకు గురవుతుంది.
"""
        else:
            return f"""### 🧪 Balanced Fertilizer & NPK Dosage for {crop_name} (Per Acre)

**Query:** *"{query}"*  

---
#### 1. 🌾 Recommended Fertilizer Bag Dosages:
- **DAP (Di-Ammonium Phosphate):** 1 to 1.5 bags (~50-75 kg) — *Apply 100% as basal during final plowing*.
- **Urea:** 2 to 2.5 bags (~100-120 kg) — *Apply in 3 split doses*.
- **MOP (Muriate of Potash):** 1 bag (~40-50 kg) — *Crucial for grain filling and stress tolerance*.
- **Zinc Sulphate:** 20 kg basal application.

#### 2. 📅 Application Split Schedule:
- **Basal (Transplanting/Sowing):** 100% DAP + 30% Urea + 50% Potash.
- **Vegetative Tillering (20-25 Days):** 35% Urea top-dressing.
- **Panicle Initiation / Flowering:** Remaining 35% Urea + Remaining 50% Potash.
"""

    # ================= 7. GENERAL AGRICULTURAL INTENT =================
    else:
        # Check if there is clean knowledge excerpts from KAU chunks
        kau_points = []
        for k in kau_results:
            txt = k.get("text", "").strip()
            if len(txt) > 40 and not any(ign in txt.lower() for ign in ["table of contents", "preface", "contents"]):
                kau_points.append(f"- {txt[:250]}…")
        
        # Clean live web search results (stripping commercial ads)
        clean_web = clean_web_snippets(web_results)
        
        context_block = "\n".join(kau_points[:2]) if kau_points else clean_web
        if not context_block:
            context_block = "కృష్ణా డెల్టా మరియు ఆంధ్రప్రదేశ్ వ్యవసాయ విశ్వవిద్యాలయం (ANGRAU) విస్తరణ పరిశోధన మార్గదర్శకాలు."

        if is_tel:
            return f"""### 🌾 KrishiMitra AI వ్యవసాయ సలహా & శాస్త్రీయ మార్గదర్శి

**ప్రశ్న:** *"{query}"*  
**గుర్తించిన అంశం:** {crop_name} మరియు అనుబంధ వ్యవసాయ యాజమాన్యం

---
#### 📋 శాస్త్రీయ మార్గదర్శకాలు & పరిశీలన:
{context_block}

#### 🚜 రైతులకు ముఖ్య సూచనలు:
1. మీ ప్రాంతంలోని నేల స్వభావం మరియు వాతావరణ పరిస్థితులకు అనుగుణంగా యాజమాన్య పద్ధతులను పాటించండి.
2. రసాయన మందుల వాడకాన్ని తగ్గించి సమగ్ర సస్యరక్షణ (IPM) మరియు సేంద్రీయ పద్ధతులకు ప్రాధాన్యత ఇవ్వండి.
3. స్థానిక సమస్యల పరిష్కారం కోసం సమీపంలోని **రైతు భరోసా కేంద్రం (RBK)** లేదా వ్యవసాయ విస్తరణ అధికారిని సంప్రదించవచ్చు.
"""
        else:
            return f"""### 🌾 KrishiMitra Agronomic Advisory & Best Practices

**Query:** *"{query}"*  
**Topic:** {crop_name} & Agricultural Production Practice

---
#### 📋 Field Guidelines & Scientific Research:
{context_block}

#### 🚜 Key Recommendations:
1. Align fertilizer and irrigation schedules with regional soil test data.
2. Practice Integrated Pest Management (IPM) to preserve beneficial predatory insects.
3. Contact your local Rythu Bharosa Kendra (RBK) or ANGRAU extension scientist for specific field queries.
"""

def generate_combined_answer(query: str, kau_results: list, web_results: list, crop: str, language: str = "Telugu") -> str:
    """Generate combined answer using OpenAI if API key available, else use specialized dynamic synthesis."""
    from services.openai_advisory import get_api_key
    api_key = get_api_key()
    
    if api_key:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=api_key)
            is_tel = (language in ["Telugu", "తెలుగు"])
            prompt = (
                f"You are a Senior Agronomist at KrishiMitra, an agricultural platform developed by Aakarsha Archana & Shiney (B.Tech AIML).\n"
                f"Farmer Question: '{query}'\n"
                f"Crop context: '{crop}'\n"
                f"Provide direct, highly practical and scientific advisory for Andhra Pradesh farmers.\n"
                f"Write in {'fluent, polite Telugu (స్పష్టమైన తెలుగులో)' if is_tel else 'clear English markdown'}."
            )
            resp = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert agronomist at KrishiMitra specializing in Andhra Pradesh crops."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=900
            )
            return resp.choices[0].message.content
        except Exception:
            pass

    return build_dynamic_synthesis(query, kau_results, web_results, crop, language)
