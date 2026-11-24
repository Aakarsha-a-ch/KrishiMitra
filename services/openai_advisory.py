import os
from pathlib import Path

def get_api_key():
    env_file = Path(__file__).resolve().parents[1] / ".env"
    if env_file.exists():
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("LLM_API_KEY="):
                    return line.split("=", 1)[1].strip()
    return os.getenv("LLM_API_KEY", "")

# Expert ANGRAU & CIBRC treatment database for instant offline/quota fallback
ANGRAU_TREATMENTS = {
    "early blight": {
        "English": {
            "symptoms": "Concentric dark brown rings ('bullseye' target spots) on older foliage, yellowing surrounding leaves, defoliation.",
            "organic": "Spray 1% Bordeaux mixture or *Pseudomonas fluorescens* (20g/L). Apply Neem oil (5ml/L) with soap emulsifier weekly.",
            "chemical": "Foliar spray of Mancozeb (Dithane M-45) @ 2-2.5g/L or Chlorothalonil @ 2g/L at early onset of disease.",
            "prevention": "Ensure wide spacing for air circulation, avoid overhead sprinkler irrigation, practice crop rotation, and mulch around base."
        },
        "Telugu": {
            "symptoms": "ముదిరిన ఆకులపై వలయాకారపు ముదురు గోధుమరంగు మచ్చలు (లక్ష్యపు బిందువు వలె), ఆకులు పసుపుబారి రాలిపోవడం.",
            "organic": "1% బోర్డో మిశ్రమం లేదా సూడోమోనాస్ ఫ్లోరొసెన్స్ (20 గ్రా/లీటర్) పిచికారీ చేయాలి. వేపనూనె (5 మి.లీ/లీటర్) వారానికోసారి వాడాలి.",
            "chemical": "మాంకోజెబ్ (డైథేన్ M-45) 2-2.5 గ్రా/లీటర్ లేదా క్లోరోథలోనిల్ 2 గ్రా/లీటర్ నీటిలో కలిపి తెగులు ప్రారంభ దశలోనే పిచికారీ చేయాలి.",
            "prevention": "మొక్కల మధ్య సరైన దూరం పాటించాలి, పంట మార్పిడి చేయాలి మరియు వ్యాధి సోకిన ఆకులను నాశనం చేయాలి."
        }
    },
    "late blight": {
        "English": {
            "symptoms": "Water-soaked lesions on leaf margins turning purplish-black, rapid blighting, white fungal mildew under humid conditions.",
            "organic": "Spray 1% Bordeaux mixture prophylactically before rainy periods. Apply *Trichoderma viride* or *Pseudomonas* to soil and foliage.",
            "chemical": "Spray Metalaxyl + Mancozeb (Ridomil MZ @ 2g/L) or Cymoxanil + Mancozeb @ 2g/L at first appearance.",
            "prevention": "Avoid waterlogging, destroy infected plant debris, ensure proper ridge planting for soil drainage."
        },
        "Telugu": {
            "symptoms": "ఆకుల అంచులపై నీటి మచ్చలు ఏర్పడి నల్లగా మారడం, తేమతో కూడిన వాతావరణంలో ఆకుల అడుగున తెల్లటి బూజు పెరగడం.",
            "organic": "వర్షాలకు ముందు 1% బోర్డో మిశ్రమం నివారణగా పిచికారీ చేయాలి. ట్రైకోడెర్మా విరిడెను సేంద్రీయ ఎరువులతో కలిపి నేలలో వేయాలి.",
            "chemical": "మెటలాక్సిల్ + మాంకోజెబ్ (రిడోమిల్ MZ 2 గ్రా/లీటర్) లేదా సైమోక్సానిల్ + మాంకోజెబ్ 2 గ్రా/లీటర్ నీటికి కలిపి పిచికారీ చేయాలి.",
            "prevention": "పొలంలో నీరు నిల్వ ఉండకుండా మురుగు కాలువలు తీయాలి, తెగులు సోకిన మొక్కల భాగాలను కాల్చివేయాలి."
        }
    },
    "bacterial spot": {
        "English": {
            "symptoms": "Small, water-soaked, dark brown angular spots with yellow halos on leaves, rough scabby lesions on fruits.",
            "organic": "Foliar spray of *Pseudomonas fluorescens* (20g/L). Dip roots/seedlings in Pseudomonas suspension for 30 minutes before planting.",
            "chemical": "Spray Copper Oxychloride (COC @ 2.5g/L) combined with Streptocycline / Plantomycin (0.1g/L - 100 ppm).",
            "prevention": "Use certified disease-free seeds, practice hot water seed treatment (50°C for 25 mins), avoid working in wet fields."
        },
        "Telugu": {
            "symptoms": "ఆకులపై పసుపు రంగు అంచులతో కూడిన చిన్న గోధుమరంగు నీటి మచ్చలు, కాయలపై గరుకైన మచ్చలు.",
            "organic": "సూడోమోనాస్ ఫ్లోరొసెన్స్ (20 గ్రా/లీటర్) ఆకులపై పిచికారీ చేయాలి మరియు నాటే ముందు నారు వేర్లను ద్రావణంలో నానబెట్టాలి.",
            "chemical": "కాపర్ ఆక్సిక్లోరైడ్ (COC 2.5 గ్రా) + స్ట్రెప్టోసైక్లిన్ / ప్లాంటోమైసిన్ (1 గ్రాము / 10 లీటర్లకు) కలిపి పిచికారీ చేయాలి.",
            "prevention": "ధృవీకరించిన విత్తనాలను వాడాలి, విత్తన శుద్ధి తప్పనిసరిగా చేయాలి, పొలంలో అధిక తేమ లేకుండా చూడాలి."
        }
    },
    "rust": {
        "English": {
            "symptoms": "Reddish-orange or golden powdery pustules primarily on lower leaf surfaces, leaf chlorosis and drying.",
            "organic": "Dust with fine sulfur powder or apply wettable sulfur (2g/L). Neem kernel extract (5%) spray.",
            "chemical": "Spray Propiconazole (Tilt 25 EC @ 1ml/L) or Hexaconazole @ 1ml/L at initiation of pustules.",
            "prevention": "Plant resistant cultivars, balance nitrogen fertilizer (avoid excessive urea), remove alternate host weeds."
        },
        "Telugu": {
            "symptoms": "ఆకుల అడుగు భాగంలో తుప్పు వంటి ఎరుపు-నారింజ రంగు పొడి బుడిపెలు, ఆకులు ఎండి రాలిపోవడం.",
            "organic": "నీటిలో కరిగే గంధకం (వెట్టబుల్ సల్ఫర్ 2 గ్రా/లీటర్) లేదా 5% వేప గింజల కషాయం పిచికారీ చేయాలి.",
            "chemical": "ప్రొపికొనాజోల్ (టిల్ట్ 1 మి.లీ/లీటర్) లేదా హెక్సాకొనాజోల్ 1 మి.లీ/లీటర్ నీటిలో కలిపి తెగులు లక్షణాలు కనిపించిన వెంటనే పిచికారీ చేయాలి.",
            "prevention": "యూరియా మోతాదును మించకుండా సమతుల్య ఎరువులు వేయాలి, తుప్పు తెగులును తట్టుకునే రకాలను ఎంచుకోవాలి."
        }
    },
    "leaf spot": {
        "English": {
            "symptoms": "Circular or irregular brown necrotic spots on leaves with distinct borders, premature leaf drop.",
            "organic": "Foliar spray of 1% Bordeaux mixture or fermented buttermilk-garlic mixture (1:10 dilution).",
            "chemical": "Spray Carbendazim @ 1g/L or Mancozeb @ 2g/L at 14-day intervals.",
            "prevention": "Clean pruning, destroy diseased leaves, promote healthy root aeration."
        },
        "Telugu": {
            "symptoms": "ఆకులపై గుండ్రటి లేదా అసమాన గోధుమరంగు మచ్చలు, తీవ్రత ఎక్కువైతే ఆకులు ఎండి రాలిపోవడం.",
            "organic": "1% బోర్డో మిశ్రమం లేదా పులిసిన మజ్జిగ-వెల్లుల్లి ద్రావణాన్ని పిచికారీ చేయాలి.",
            "chemical": "కార్బెండజిమ్ (1 గ్రా/లీటర్) లేదా మాంకోజెబ్ (2 గ్రా/లీటర్) నీటికి కలిపి 10-14 రోజుల వ్యవధిలో పిచికారీ చేయాలి.",
            "prevention": "రాలిన తెగులు సోకిన ఆకులను ఏరి నాశనం చేయాలి, నేలలో గాలి ప్రసరణ బాగుండేలా చూడాలి."
        }
    },
    "healthy": {
        "English": {
            "symptoms": "Vibrant green foliage, no necrotic lesions, optimal vigor and healthy leaf turgor.",
            "organic": "Apply Panchagavya (3% spray) or Jeevamrutham every 15-20 days to promote vegetative growth and immunity.",
            "chemical": "Maintain recommended balanced NPK dosage for the crop. Avoid unnecessary chemical sprays.",
            "prevention": "Continue regular monitoring, maintain soil organic mulch, adhere to scheduled irrigation."
        },
        "Telugu": {
            "symptoms": "ఆరోగ్యకరమైన పచ్చటి ఆకులు, తెగులు లేదా పురుగుల లక్షణాలు లేవు.",
            "organic": "మొక్కల రోగనిరోధక శక్తిని పెంచడానికి ప్రతి 15-20 రోజులకు 3% పంచగవ్య లేదా జీవామృతం పిచికారీ చేయాలి.",
            "chemical": "సిఫార్సు చేసిన మోతాదులో మాత్రమే సమతుల్య NPK ఎరువులను అందించాలి. అనవసర రసాయనాలు వాడవద్దు.",
            "prevention": "సరైన నీటి యాజమాన్యం మరియు పచ్చిరొట్ట ఎరువుల వాడకాన్ని కొనసాగించండి."
        }
    }
}

def get_fallback_advisory(crop_name: str, disease_name: str, confidence: float, language: str = "English") -> str:
    """Return comprehensive ANGRAU-aligned package of practices treatment when API is offline or quota-exceeded."""
    d_lower = disease_name.lower()
    
    # Match best category
    matched_key = "leaf spot"
    if "healthy" in d_lower:
        matched_key = "healthy"
    elif "early blight" in d_lower:
        matched_key = "early blight"
    elif "late blight" in d_lower:
        matched_key = "late blight"
    elif "bacterial" in d_lower or "spot" in d_lower:
        matched_key = "bacterial spot"
    elif "rust" in d_lower:
        matched_key = "rust"
    
    is_tel = (language in ["Telugu", "తెలుగు"])
    lang_key = "Telugu" if is_tel else "English"
    entry = ANGRAU_TREATMENTS[matched_key].get(lang_key, ANGRAU_TREATMENTS[matched_key]["English"])
    
    if is_tel:
        return f"""### 🌾 కృషిమిత్ర శాస్త్రీయ తెగుళ్ల నివారణ మార్గదర్శి (ANGRAU మార్గదర్శకాలు)

**గుర్తించిన పరిస్థితి:** {crop_name} - {disease_name} (ఖచ్చితత్వం: {confidence*100:.1f}%)

---
#### 1. 🔍 తెగులు లక్షణాలు (Symptoms)
{entry['symptoms']}

#### 2. 🌿 సేంద్రీయ & జీవ నియంత్రణ పద్ధతులు (Organic & Biological Control)
{entry['organic']}

#### 3. 🧪 శాస్త్రీయ రసాయన నివారణ చర్యలు (Chemical Management)
{entry['chemical']}

#### 4. 🛡️ సస్యరక్షణ & నివారణ పద్ధతులు (Preventive Practices)
{entry['prevention']}

*(ఆచార్య ఎన్.జి.రంగా వ్యవసాయ విశ్వవిద్యాలయం - ANGRAU మార్గదర్శకాల ఆధారంగా రూపొందించబడింది).*
"""
    else:
        return f"""### 🌾 KrishiMitra Scientific Advisory & Treatment Guide

**Diagnosis:** {crop_name} - {disease_name} (Confidence: {confidence*100:.1f}%)

---
#### 1. 🔍 Disease Verification & Symptoms
{entry['symptoms']}

#### 2. 🌿 Biological & Organic Management
{entry['organic']}

#### 3. 🧪 Approved Chemical Control (ANGRAU Guidelines)
{entry['chemical']}

#### 4. 🛡️ Cultural & Preventive Field Measures
{entry['prevention']}

*(Advisory based on ANGRAU standard Package of Practices for Andhra Pradesh).*
"""

def generate_disease_advisory(crop_name: str, disease_name: str, confidence: float, language: str = "English") -> str:
    """Generate agronomic treatment and management recommendations via OpenAI API with ANGRAU fallback."""
    api_key = get_api_key()
    if not api_key:
        return get_fallback_advisory(crop_name, disease_name, confidence, language)

    from openai import OpenAI
    client = OpenAI(api_key=api_key)
    is_tel = (language in ["Telugu", "తెలుగు"])
    
    if "healthy" in disease_name.lower():
        prompt = (
            f"The plant '{crop_name}' is diagnosed as HEALTHY with {confidence*100:.1f}% confidence. "
            f"Provide best agronomic practices under ANGRAU guidelines: organic growth promoters, "
            f"seasonal preventive care against common pests in Vijayawada and Andhra Pradesh, and soil nutrition maintenance. "
            f"Write the response in {'clear Telugu (తెలుగులో)' if is_tel else 'clear structured English markdown'}."
        )
    else:
        prompt = (
            f"A plant leaf image for '{crop_name}' has been diagnosed with '{disease_name}' with {confidence*100:.1f}% confidence. "
            f"As an Agronomist and Plant Pathologist at KrishiMitra, provide a comprehensive advisory:\n"
            f"1. **Symptoms & Field Identification**\n"
            f"2. **Immediate Organic & Biological Remedies** (e.g. Pseudomonas fluorescens, Neem oil, Bordeaux mixture, Trichoderma with exact dosages)\n"
            f"3. **Chemical Fungicide Treatment** (Approved dosages per liter of water)\n"
            f"4. **Field Prevention & Cultural Hygiene for Vijayawada and AP region**\n"
            f"Write the response in {'clear Telugu (తెలుగులో)' if is_tel else 'English markdown'}."
        )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert agronomist and plant pathologist for KrishiMitra. "
                        "Give highly actionable, scientifically accurate, and farmer-friendly advice for crops in Vijayawada, Krishna Delta, and Andhra Pradesh."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=850
        )
        return response.choices[0].message.content
    except Exception as e:
        fallback = get_fallback_advisory(crop_name, disease_name, confidence, language)
        err_msg = str(e)
        if "429" in err_msg or "credit" in err_msg.lower():
            notice = "> ℹ️ *Note: OpenAI API reported quota limit/no credits remaining. Loaded verified ANGRAU Package of Practices guidance below:*\n\n"
        else:
            notice = f"> ℹ️ *Notice: OpenAI connection ({err_msg[:80]}...). Using verified ANGRAU guidelines below:*\n\n"
        return notice + fallback
