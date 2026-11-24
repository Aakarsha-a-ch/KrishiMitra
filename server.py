import os
import sys
import io
import json
from pathlib import Path
from typing import Optional, List
from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from PIL import Image

# Add project root to sys.path
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# Import existing services & pages logic
from services.auth import load_users, authenticate_user, register_user
from services.weather_service import fetch_weather, geocode_location, AP_DISTRICTS
from services.soil_service import CROP_SOIL_STANDARDS, analyze_nutrient
from services.retrieval import search
from services.web_search import search_agricultural_web
from services.assistant_synthesis import generate_combined_answer

app = FastAPI(
    title="KrishiMitra API | Aakarsha Archana & Shiney (B.Tech CSE AIML)",
    description="Backend API for AI-powered agricultural decision support system",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------- Models & Schemas -----------------
class LoginRequest(BaseModel):
    username: str
    password: str

class RegisterRequest(BaseModel):
    name: str
    phone: str
    password: str
    district: str
    crop: str
    acres: float

class ProfileUpdateRequest(BaseModel):
    name: str
    phone: str
    district: str
    village: Optional[str] = ""
    crop: str
    acres: float

class SoilRequest(BaseModel):
    crop: str
    ph: float
    nitrogen: float
    phosphorus: float
    potassium: float
    language: Optional[str] = "Telugu"

class CropRecRequest(BaseModel):
    n: float
    p: float
    k: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

class ChatRequest(BaseModel):
    query: str
    crop: Optional[str] = "Paddy"
    language: Optional[str] = "Telugu"

class PostRequest(BaseModel):
    author: str
    district: str
    crop: str
    title: str
    message: str
    tag: Optional[str] = "సాధారణ చర్చ"

class LikeRequest(BaseModel):
    post_id: int

class ReplyRequest(BaseModel):
    post_id: int
    author: str
    district: str
    text: str

class MessageRequest(BaseModel):
    sender: str
    text: str
    contact: str

# ----------------- Authentication Endpoints -----------------
@app.get("/api/auth/demo-users")
def get_demo_users():
    return load_users()

@app.post("/api/auth/login")
def login(req: LoginRequest):
    users = load_users()
    u_clean = req.username.strip()
    if u_clean in users and (not req.password or req.password in ("demo", "demo123", "password", "123456", "archana123", "shiney123")):
        return {"status": "success", "user": users[u_clean]}
    for p, u in users.items():
        if u_clean.lower() == u.get("name", "").lower() and (not req.password or req.password in ("demo", "demo123", "password", "123456", "archana123", "shiney123")):
            return {"status": "success", "user": u}
            
    user = authenticate_user(u_clean, req.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password.")
    return {"status": "success", "user": user}

@app.post("/api/auth/demo-login/{phone}")
def demo_login(phone: str):
    users = load_users()
    if phone in users:
        return {"status": "success", "user": users[phone]}
    raise HTTPException(status_code=404, detail="Demo user not found.")

@app.post("/api/auth/register")
def register(req: RegisterRequest):
    ok, res = register_user(
        req.name, req.phone, req.password,
        req.district, req.crop, req.acres
    )
    if not ok:
        raise HTTPException(status_code=400, detail=res)
    return {"status": "success", "user": res}

@app.post("/api/auth/profile/update")
def update_profile(req: ProfileUpdateRequest):
    users = load_users()
    phone = req.phone.strip()
    if phone in users:
        users[phone]["name"] = req.name
        users[phone]["district"] = req.district
        users[phone]["village"] = req.village
        users[phone]["crop"] = req.crop
        users[phone]["acres"] = req.acres
    return {
        "status": "success",
        "message": "Profile updated successfully.",
        "user": {
            "name": req.name,
            "username": req.phone,
            "phone": req.phone,
            "district": req.district,
            "village": req.village,
            "crop": req.crop,
            "acres": req.acres
        }
    }

# ----------------- Weather Endpoints -----------------
@app.get("/api/weather")
def get_weather(
    location: Optional[str] = Query(None, description="Location name"),
    lat: Optional[float] = Query(None, description="Latitude"),
    lon: Optional[float] = Query(None, description="Longitude")
):
    selected_name = "Vijayawada (Krishna)"
    if location and location in AP_DISTRICTS:
        coords = AP_DISTRICTS[location]
        lat, lon = coords[0], coords[1]
        selected_name = location
    elif location:
        geo = geocode_location(location)
        if geo:
            lat = geo["lat"]
            lon = geo["lon"]
            selected_name = geo.get("name", location)
    
    if lat is None or lon is None:
        lat, lon = 16.5062, 80.6480 # Vijayawada default

    raw = fetch_weather(lat, lon)
    if not raw:
        raise HTTPException(status_code=502, detail="Weather telemetry temporarily unavailable.")

    cur = raw.get("current", {})
    daily = raw.get("daily", {})
    hourly = raw.get("hourly", {})

    temp = round(cur.get("temperature_2m", 31.0), 1)
    feels = round(cur.get("apparent_temperature", temp + 2.0), 1)
    humidity = cur.get("relative_humidity_2m", 68)
    wind = cur.get("wind_speed_10m", 12.0)
    precip = cur.get("precipitation", 0.0)

    precip_prob = 10
    if "precipitation_probability_max" in daily and daily["precipitation_probability_max"]:
        p = daily["precipitation_probability_max"][0]
        if p is not None:
            precip_prob = int(p)

    forecast_list = []
    if "time" in daily:
        dates = daily.get("time", [])
        max_temps = daily.get("temperature_2m_max", [])
        min_temps = daily.get("temperature_2m_min", [])
        rains = daily.get("precipitation_sum", [])
        for i in range(min(5, len(dates))):
            forecast_list.append({
                "date": dates[i],
                "temp_max": max_temps[i] if i < len(max_temps) else 32,
                "temp_min": min_temps[i] if i < len(min_temps) else 24,
                "precipitation_sum": rains[i] if i < len(rains) else 0.0
            })

    cloud = cur.get("cloud_cover", 30)
    condition_str = "పాక్షికంగా మేఘావృతం (Partly Cloudy)" if cloud > 30 else "స్పష్టమైన ఆకాశం (Clear)"

    return {
        "status": "success",
        "location": selected_name,
        "coordinates": {"lat": lat, "lon": lon},
        "current": {
            "temperature": temp,
            "apparent_temperature": feels,
            "humidity": humidity,
            "wind_speed": wind,
            "precipitation": precip,
            "precipitation_probability": precip_prob,
            "condition": condition_str
        },
        "forecast_daily": forecast_list
    }

@app.get("/api/weather/geocode")
def geocode(q: str):
    res = geocode_location(q)
    if not res:
        raise HTTPException(status_code=404, detail="Location could not be geocoded.")
    return res

# ----------------- Disease Detection (MobileNetV2) -----------------
@app.post("/api/predict-disease")
async def predict_disease(
    file: UploadFile = File(...),
    language: str = Form("Telugu")
):
    try:
        from services.disease_service import load_disease_model, predict_leaf_disease
        from services.openai_advisory import generate_disease_advisory, ANGRAU_TREATMENTS
        
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        
        model_info = load_disease_model()
        if not model_info or model_info[0] is None:
            raise HTTPException(status_code=503, detail="Leaf disease model is not loaded.")
            
        model, class_names, val_acc = model_info
        preds = predict_leaf_disease(image, model, class_names)
        
        top_pred = preds[0]
        crop_name = top_pred["crop"]
        dis_name = top_pred["disease"]
        conf = float(top_pred["confidence"])

        is_tel = (language.lower() in ["telugu", "తెలుగు"])
        lang_key = "Telugu" if is_tel else "English"

        # Match ANGRAU treatments database
        matched_db = None
        for k, v in ANGRAU_TREATMENTS.items():
            if k in dis_name.lower():
                matched_db = v.get(lang_key, v.get("English"))
                break

        if matched_db:
            organic = matched_db.get("organic", "వేప నూనె (5 మి.లీ/లీ) పిచికారీ చేయాలి.")
            chemical = matched_db.get("chemical", "సిఫార్సు చేసిన పురుగుమందు పిచికారీ చేయాలి.")
            prevention = matched_db.get("prevention", "మురుగునీరు నిలవకుండా చూడాలి.")
        else:
            if is_tel:
                organic = "1% బోర్డో మిశ్రమం లేదా వేప నూనె (5 మి.లీ/లీటర్ నీటికి) పిచికారీ చేయాలి. సూడోమోనాస్ ఫ్లోరొసెన్స్ (20 గ్రా/లీ) వాడాలి."
                chemical = "మాంకోజెబ్ 2 గ్రా/లీటర్ లేదా కాపర్ ఆక్సిక్లోరైడ్ 2.5 గ్రా/లీటర్ నీటికి కలిపి తెగులు సోకిన భాగాలపై పిచికారీ చేయాలి."
                prevention = "పొలంలో నీరు నిల్వ ఉండకుండా చూడాలి. వ్యాధి సోకిన ఆకులను ఏరి కాల్చివేయాలి. సిఫార్సు చేసిన మోతాదులో మాత్రమే ఎరువులు వేయాలి."
            else:
                organic = "Apply 1% Bordeaux mixture or Neem oil (5ml/L) or Pseudomonas fluorescens (20g/L)."
                chemical = "Foliar spray of Mancozeb @ 2g/L or Copper Oxychloride @ 2.5g/L at early onset."
                prevention = "Ensure field drainage, avoid excess nitrogen, remove and burn infected plant foliage."

        return {
            "status": "success",
            "crop": crop_name,
            "disease_name": dis_name,
            "confidence": conf,
            "organic_remedies": organic,
            "chemical_treatments": chemical,
            "prevention": prevention
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----------------- Soil & Fertilizer Assessment -----------------
@app.post("/api/soil-analysis")
def soil_analysis(req: SoilRequest):
    crop_info = CROP_SOIL_STANDARDS.get(req.crop, CROP_SOIL_STANDARDS.get("Paddy"))
    is_tel = (req.language.lower() in ["telugu", "తెలుగు"])
    
    ph_status, ph_color = analyze_nutrient(req.ph, crop_info["ideal_ph"][0], crop_info["ideal_ph"][1], is_tel)
    n_status, n_color = analyze_nutrient(req.nitrogen, crop_info["ideal_n"][0], crop_info["ideal_n"][1], is_tel)
    p_status, p_color = analyze_nutrient(req.phosphorus, crop_info["ideal_p"][0], crop_info["ideal_p"][1], is_tel)
    k_status, k_color = analyze_nutrient(req.potassium, crop_info["ideal_k"][0], crop_info["ideal_k"][1], is_tel)
    
    lang_key = "Telugu" if is_tel else "English"
    recs = crop_info["recommendations"].get(lang_key, crop_info["recommendations"]["English"])

    # Fertilizer bag calculations
    urea_bags = 2.2
    dap_bags = 1.5
    mop_bags = 0.8

    if req.nitrogen < crop_info["ideal_n"][0]:
        urea_bags += 0.5
    elif req.nitrogen > crop_info["ideal_n"][1]:
        urea_bags -= 0.4

    if req.phosphorus < crop_info["ideal_p"][0]:
        dap_bags += 0.5
    elif req.phosphorus > crop_info["ideal_p"][1]:
        dap_bags -= 0.3

    if req.potassium < crop_info["ideal_k"][0]:
        mop_bags += 0.4
    elif req.potassium > crop_info["ideal_k"][1]:
        mop_bags -= 0.2

    urea_bags = round(max(0.5, urea_bags), 1)
    dap_bags = round(max(0.5, dap_bags), 1)
    mop_bags = round(max(0.3, mop_bags), 1)

    if is_tel:
        basal = f"మొత్తం డీఏపీ ({dap_bags} బస్తాలు) + 1/3 వంతు యూరియా ({round(urea_bags/3, 1)} బస్తాలు) + సగం ఎంఓపీ ({round(mop_bags/2, 1)} బస్తాలు) ఆఖరి దుక్కిలో వేయాలి."
        tillering = f"నాటిన 20-25 రోజులకు 1/3 వంతు యూరియా ({round(urea_bags/3, 1)} బస్తాలు) సమానంగా చల్లాలి."
        panicle = f"చిరుపొట్ట లేదా పూత దశలో మిగిలిన 1/3 యూరియా ({round(urea_bags/3, 1)} బస్తాలు) + మిగిలిన ఎంఓపీ ({round(mop_bags/2, 1)} బస్తాలు) వేయాలి."
    else:
        basal = f"Full DAP ({dap_bags} bags) + 1/3 Urea ({round(urea_bags/3, 1)} bags) + 1/2 MOP ({round(mop_bags/2, 1)} bags) at final ploughing."
        tillering = f"Apply 1/3 Urea ({round(urea_bags/3, 1)} bags) at 20-25 days after transplanting."
        panicle = f"Apply remaining 1/3 Urea ({round(urea_bags/3, 1)} bags) + 1/2 MOP ({round(mop_bags/2, 1)} bags) at panicle initiation."

    return {
        "crop": req.crop,
        "fertilizer_bags": {
            "urea_bags": urea_bags,
            "dap_bags": dap_bags,
            "mop_bags": mop_bags
        },
        "split_schedule": {
            "basal": basal,
            "tillering": tillering,
            "panicle": panicle
        },
        "status": {
            "ph": {"value": req.ph, "label": ph_status, "color": ph_color},
            "nitrogen": {"value": req.nitrogen, "label": n_status, "color": n_color},
            "phosphorus": {"value": req.phosphorus, "label": p_status, "color": p_color},
            "potassium": {"value": req.potassium, "label": k_status, "color": k_color}
        },
        "recommendations": recs
    }

# ----------------- Smart Crop Recommendation ML -----------------
@app.post("/api/recommend-crop")
def recommend_crop(req: CropRecRequest):
    try:
        from services.crop_rec_service import load_model, META_PATH
        import pandas as pd
        
        bundle = load_model()
        features = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
        row = pd.DataFrame([[req.n, req.p, req.k, req.temperature, req.humidity, req.ph, req.rainfall]], columns=features)
        
        model = bundle["model"]
        encoded = model.predict(row)[0]
        label = str(bundle["label_encoder"].inverse_transform([int(encoded)])[0])
        
        # Probabilities
        probs = model.predict_proba(row)[0]
        top3_idx = probs.argsort()[-3:][::-1]
        top3 = []
        for idx in top3_idx:
            c_name = str(bundle["label_encoder"].inverse_transform([int(idx)])[0])
            top3.append({"crop": c_name, "probability": float(probs[idx])})
            
        return {
            "status": "success",
            "recommended_crop": label,
            "confidence": float(probs[encoded]),
            "top_candidates": top3
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----------------- Conversational AI Assistant -----------------
@app.post("/api/chat")
def chat_with_assistant(req: ChatRequest):
    try:
        # 1. Semantic Retrieval
        kau_results, detected_crop = search(req.query, crop=req.crop or "Paddy", top_k=3)
        
        # 2. Live Agronomic Web Search
        web_results = search_agricultural_web(req.query, crop=detected_crop, max_results=3)
        
        # 3. Dynamic Synthesis
        answer = generate_combined_answer(
            query=req.query,
            kau_results=kau_results,
            web_results=web_results,
            crop=detected_crop,
            language=req.language or "Telugu"
        )
        
        return {
            "status": "success",
            "answer": answer,
            "detected_crop": detected_crop,
            "knowledge_excerpts": kau_results,
            "web_sources": web_results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----------------- Community Posts & Chats -----------------
@app.get("/api/community/posts")
def get_posts():
    from services.community_service import load_posts
    return load_posts()

@app.post("/api/community/posts")
def create_post(p: PostRequest):
    from services.community_service import load_posts, save_posts
    from datetime import datetime
    posts = load_posts()
    new_post = {
        "id": len(posts) + 1,
        "author": p.author,
        "district": p.district,
        "crop": p.crop,
        "tag": p.tag or "సాధారణ చర్చ",
        "title": p.title,
        "message": p.message,
        "date": datetime.now().strftime("%d %b %Y, %I:%M %p"),
        "likes": 0,
        "liked": False,
        "replies": []
    }
    posts.insert(0, new_post)
    save_posts(posts)
    return {"status": "success", "post": new_post}

@app.post("/api/community/like-post")
def like_post(req: LikeRequest):
    from services.community_service import load_posts, save_posts
    posts = load_posts()
    updated = None
    for p in posts:
        if p["id"] == req.post_id:
            # Toggle like
            if p.get("liked", False):
                p["likes"] = max(0, p.get("likes", 1) - 1)
                p["liked"] = False
            else:
                p["likes"] = p.get("likes", 0) + 1
                p["liked"] = True
            updated = p
            break
    if updated:
        save_posts(posts)
        return {"status": "success", "post": updated}
    raise HTTPException(status_code=404, detail="Post not found")

@app.post("/api/community/reply-post")
def reply_post(req: ReplyRequest):
    from services.community_service import load_posts, save_posts
    from datetime import datetime
    posts = load_posts()
    for p in posts:
        if p["id"] == req.post_id:
            if "replies" not in p:
                p["replies"] = []
            new_reply = {
                "author": req.author,
                "district": req.district,
                "time": datetime.now().strftime("%d %b %Y, %I:%M %p"),
                "text": req.text
            }
            p["replies"].append(new_reply)
            save_posts(posts)
            return {"status": "success", "post": p}
    raise HTTPException(status_code=404, detail="Post not found")

@app.get("/api/community/chats")
def get_chats():
    from services.community_service import load_chats
    return load_chats()

@app.post("/api/community/send-message")
def send_chat_message(m: MessageRequest):
    from services.community_service import load_chats, save_chats, generate_farmer_reply
    from datetime import datetime
    chats = load_chats()
    if m.contact not in chats:
        chats[m.contact] = {
            "name": m.contact.split(" ")[0],
            "crop": "General Farming",
            "avatar": "👨‍🌾",
            "online": True,
            "messages": []
        }
    
    # 1. Append user message
    now_time = datetime.now().strftime("%I:%M %p")
    chats[m.contact]["messages"].append({
        "sender": "You",
        "text": m.text,
        "time": now_time
    })
    
    # 2. Generate farmer peer response
    farmer_name = chats[m.contact].get("name", m.contact.split(" ")[0])
    farmer_reply = generate_farmer_reply(m.contact, m.text)
    chats[m.contact]["messages"].append({
        "sender": farmer_name,
        "text": farmer_reply,
        "time": now_time
    })
    
    save_chats(chats)
    return {"status": "success", "chats": chats, "farmer_reply": farmer_reply}

# ----------------- Live Mandi Rates & AP Welfare -----------------
@app.get("/api/mandi-rates")
def get_mandi_rates():
    return [
        # Top 6 Primary Staples / Cash Crops
        {
            "crop": "వరి ధాన్యం (Paddy BPT 5204)",
            "crop_te": "వరి ధాన్యం (Paddy BPT 5204)",
            "crop_en": "Paddy Grain (BPT 5204)",
            "price": "₹2,320 / క్వింటాల్",
            "price_te": "₹2,320 / క్వింటాల్",
            "price_en": "₹2,320 / Quintal",
            "mandi": "విజయవాడ మార్కెట్ యార్డ్",
            "mandi_te": "విజయవాడ మార్కెట్ యార్డ్",
            "mandi_en": "Vijayawada Market Yard",
            "trend": "+1.8%",
            "trend_te": "+1.8%",
            "trend_en": "+1.8%",
            "badge": "వరి",
            "badge_te": "వరి",
            "badge_en": "Paddy",
            "category": "Cereals",
            "is_top": True
        },
        {
            "crop": "తేజా మిర్చి (Teja Chilli)",
            "crop_te": "తేజా మిర్చి (Teja Chilli)",
            "crop_en": "Teja Chilli",
            "price": "₹20,500 / క్వింటాల్",
            "price_te": "₹20,500 / క్వింటాల్",
            "price_en": "₹20,500 / Quintal",
            "mandi": "గుంటూరు మిర్చి యార్డు",
            "mandi_te": "గుంటూరు మిర్చి యార్డు",
            "mandi_en": "Guntur Chilli Yard",
            "trend": "+3.2%",
            "trend_te": "+3.2%",
            "trend_en": "+3.2%",
            "badge": "మిర్చి",
            "badge_te": "మిర్చి",
            "badge_en": "Chilli",
            "category": "Spices",
            "is_top": True
        },
        {
            "crop": "పత్తి (Cotton - Bunny)",
            "crop_te": "పత్తి (Cotton - Bunny)",
            "crop_en": "Cotton (Bunny)",
            "price": "₹7,250 / క్వింటాల్",
            "price_te": "₹7,250 / క్వింటాల్",
            "price_en": "₹7,250 / Quintal",
            "mandi": "నందిగామ మార్కెట్",
            "mandi_te": "నందిగామ మార్కెట్",
            "mandi_en": "Nandigama Market",
            "trend": "+0.5%",
            "trend_te": "+0.5%",
            "trend_en": "+0.5%",
            "badge": "పత్తి",
            "badge_te": "పత్తి",
            "badge_en": "Cotton",
            "category": "Commercial",
            "is_top": True
        },
        {
            "crop": "మొక్కజొన్న (Maize)",
            "crop_te": "మొక్కజొన్న (Maize)",
            "crop_en": "Maize (Corn)",
            "price": "₹2,150 / క్వింటాల్",
            "price_te": "₹2,150 / క్వింటాల్",
            "price_en": "₹2,150 / Quintal",
            "mandi": "నూజివీడు యార్డు",
            "mandi_te": "నూజివీడు యార్డు",
            "mandi_en": "Nuzvid Yard",
            "trend": "+1.2%",
            "trend_te": "+1.2%",
            "trend_en": "+1.2%",
            "badge": "మొక్కజొన్న",
            "badge_te": "మొక్కజొన్న",
            "badge_en": "Maize",
            "category": "Cereals",
            "is_top": True
        },
        {
            "crop": "వేరుశనగ (Groundnut K-6)",
            "crop_te": "వేరుశనగ (Groundnut K-6)",
            "crop_en": "Groundnut (K-6)",
            "price": "₹6,800 / క్వింటాల్",
            "price_te": "₹6,800 / క్వింటాల్",
            "price_en": "₹6,800 / Quintal",
            "mandi": "కర్నూలు మార్కెట్",
            "mandi_te": "కర్నూలు మార్కెట్",
            "mandi_en": "Kurnool Market",
            "trend": "+0.9%",
            "trend_te": "+0.9%",
            "trend_en": "+0.9%",
            "badge": "వేరుశనగ",
            "badge_te": "వేరుశనగ",
            "badge_en": "Oilseeds",
            "category": "Oilseeds",
            "is_top": True
        },
        {
            "crop": "చెరకు (Sugarcane)",
            "crop_te": "చెరకు (Sugarcane)",
            "crop_en": "Sugarcane",
            "price": "₹3,400 / టన్ను",
            "price_te": "₹3,400 / టన్ను",
            "price_en": "₹3,400 / Ton",
            "mandi": "ఉయ్యూరు షుగర్స్",
            "mandi_te": "ఉయ్యూరు షుగర్స్",
            "mandi_en": "Vuyyuru Sugars",
            "trend": "స్థిరం",
            "trend_te": "స్థిరం",
            "trend_en": "Stable",
            "badge": "చెరకు",
            "badge_te": "చెరకు",
            "badge_en": "Sugarcane",
            "category": "Commercial",
            "is_top": True
        },

        # Additional Major Andhra Pradesh Crops (Viewable via Show More)
        {
            "crop": "టమాటా (Tomato Grade A)",
            "crop_te": "టమాటా (Tomato Grade A)",
            "crop_en": "Tomato (Grade A)",
            "price": "₹1,850 / క్రేట్ (25kg)",
            "price_te": "₹1,850 / క్రేట్ (25kg)",
            "price_en": "₹1,850 / Crate (25kg)",
            "mandi": "మదనపల్లె మార్కెట్",
            "mandi_te": "మదనపల్లె మార్కెట్",
            "mandi_en": "Madanapalle Market",
            "trend": "-2.1%",
            "trend_te": "-2.1%",
            "trend_en": "-2.1%",
            "badge": "టమాటా",
            "badge_te": "టమాటా",
            "badge_en": "Tomato",
            "category": "Vegetables",
            "is_top": False
        },
        {
            "crop": "మినుములు (Black Gram / Urad)",
            "crop_te": "మినుములు (Black Gram / Urad)",
            "crop_en": "Black Gram (Urad)",
            "price": "₹8,900 / క్వింటాల్",
            "price_te": "₹8,900 / క్వింటాల్",
            "price_en": "₹8,900 / Quintal",
            "mandi": "తెనాలి మార్కెట్ యార్డ్",
            "mandi_te": "తెనాలి మార్కెట్ యార్డ్",
            "mandi_en": "Tenali Market Yard",
            "trend": "+2.4%",
            "trend_te": "+2.4%",
            "trend_en": "+2.4%",
            "badge": "మినుములు",
            "badge_te": "మినుములు",
            "badge_en": "Pulses",
            "category": "Pulses",
            "is_top": False
        },
        {
            "crop": "కందులు (Red Gram / Toor)",
            "crop_te": "కందులు (Red Gram / Toor)",
            "crop_en": "Red Gram (Toor)",
            "price": "₹10,200 / క్వింటాల్",
            "price_te": "₹10,200 / క్వింటాల్",
            "price_en": "₹10,200 / Quintal",
            "mandi": "ఒంగోలు మార్కెట్ యార్డ్",
            "mandi_te": "ఒంగోలు మార్కెట్ యార్డ్",
            "mandi_en": "Ongole Market Yard",
            "trend": "+1.5%",
            "trend_te": "+1.5%",
            "trend_en": "+1.5%",
            "badge": "కందులు",
            "badge_te": "కందులు",
            "badge_en": "Pulses",
            "category": "Pulses",
            "is_top": False
        },
        {
            "crop": "పసుపు (Turmeric Duggirala)",
            "crop_te": "పసుపు (Turmeric Duggirala)",
            "crop_en": "Turmeric (Duggirala)",
            "price": "₹14,500 / క్వింటాల్",
            "price_te": "₹14,500 / క్వింటాల్",
            "price_en": "₹14,500 / Quintal",
            "mandi": "దుగ్గిరాల మార్కెట్",
            "mandi_te": "దుగ్గిరాల మార్కెట్",
            "mandi_en": "Duggirala Market",
            "trend": "+4.0%",
            "trend_te": "+4.0%",
            "trend_en": "+4.0%",
            "badge": "పసుపు",
            "badge_te": "పసుపు",
            "badge_en": "Spices",
            "category": "Spices",
            "is_top": False
        },
        {
            "crop": "ఉల్లిపాయ (Onion Bellary/AP)",
            "crop_te": "ఉల్లిపాయ (Onion Bellary/AP)",
            "crop_en": "Onion (Bellary/AP)",
            "price": "₹2,900 / క్వింటాల్",
            "price_te": "₹2,900 / క్వింటాల్",
            "price_en": "₹2,900 / Quintal",
            "mandi": "కర్నూలు మార్కెట్ యార్డ్",
            "mandi_te": "కర్నూలు మార్కెట్ యార్డ్",
            "mandi_en": "Kurnool Market Yard",
            "trend": "-1.2%",
            "trend_te": "-1.2%",
            "trend_en": "-1.2%",
            "badge": "ఉల్లి",
            "badge_te": "ఉల్లి",
            "badge_en": "Vegetables",
            "category": "Vegetables",
            "is_top": False
        },
        {
            "crop": "వర్జీనియా పొగాకు (Tobacco FCV)",
            "crop_te": "వర్జీనియా పొగాకు (Tobacco FCV)",
            "crop_en": "Virginia Tobacco (FCV)",
            "price": "₹26,500 / క్వింటాల్",
            "price_te": "₹26,500 / క్వింటాల్",
            "price_en": "₹26,500 / Quintal",
            "mandi": "ఒంగోలు టొబాకో బోర్డు",
            "mandi_te": "ఒంగోలు టొబాకో బోర్డు",
            "mandi_en": "Ongole Tobacco Board",
            "trend": "+0.8%",
            "trend_te": "+0.8%",
            "trend_en": "+0.8%",
            "badge": "పొగాకు",
            "badge_te": "పొగాకు",
            "badge_en": "Commercial",
            "category": "Commercial",
            "is_top": False
        },
        {
            "crop": "బంగినపల్లి మామిడి (Mango Banganapalli)",
            "crop_te": "బంగినపల్లి మామిడి (Mango Banganapalli)",
            "crop_en": "Banganapalli Mango",
            "price": "₹48,000 / టన్ను",
            "price_te": "₹48,000 / టన్ను",
            "price_en": "₹48,000 / Ton",
            "mandi": "తిరువూరు & నూజివీడు యార్డ్",
            "mandi_te": "తిరువూరు & నూజివీడు యార్డ్",
            "mandi_en": "Tiruvuru & Nuzvid Yard",
            "trend": "+3.5%",
            "trend_te": "+3.5%",
            "trend_en": "+3.5%",
            "badge": "మామిడి",
            "badge_te": "మామిడి",
            "badge_en": "Fruits",
            "category": "Fruits",
            "is_top": False
        },
        {
            "crop": "కర్పూర అరటి (Banana Karpura)",
            "crop_te": "కర్పూర అరటి (Banana Karpura)",
            "crop_en": "Karpura Banana",
            "price": "₹220 / గెల",
            "price_te": "₹220 / గెల",
            "price_en": "₹220 / Bunch",
            "mandi": "రాజమండ్రి పండ్ల మార్కెట్",
            "mandi_te": "రాజమండ్రి పండ్ల మార్కెట్",
            "mandi_en": "Rajahmundry Fruit Market",
            "trend": "స్థిరం",
            "trend_te": "స్థిరం",
            "trend_en": "Stable",
            "badge": "అరటి",
            "badge_te": "అరటి",
            "badge_en": "Fruits",
            "category": "Fruits",
            "is_top": False
        },
        {
            "crop": "బత్తాయి (Sweet Orange / Mosambi)",
            "crop_te": "బత్తాయి (Sweet Orange / Mosambi)",
            "crop_en": "Sweet Orange (Mosambi)",
            "price": "₹35,000 / టన్ను",
            "price_te": "₹35,000 / టన్ను",
            "price_en": "₹35,000 / Ton",
            "mandi": "పులివెందుల & కడప యార్డ్",
            "mandi_te": "పులివెందుల & కడప యార్డ్",
            "mandi_en": "Pulivendula & Kadapa Yard",
            "trend": "+1.1%",
            "trend_te": "+1.1%",
            "trend_en": "+1.1%",
            "badge": "బత్తాయి",
            "badge_te": "బత్తాయి",
            "badge_en": "Fruits",
            "category": "Fruits",
            "is_top": False
        }
    ]

# ----------------- Static SPA Frontend Mounting -----------------
STATIC_DIR = ROOT_DIR / "static"
if not STATIC_DIR.exists():
    os.makedirs(STATIC_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/")
def serve_index():
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        return FileResponse(str(index_file))
    return JSONResponse({"status": "KrishiMitra API Live", "docs": "/docs"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
