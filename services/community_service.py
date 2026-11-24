import json
import os
import sqlite3
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
POSTS_FILE = DATA_DIR / "community_posts.json"
CHATS_FILE = DATA_DIR / "farmer_chats.json"

DEFAULT_POSTS = [
    {
        "id": 1,
        "author": "Shiney",
        "district": "Guntur",
        "crop": "Chilli",
        "tag": "తెగుళ్ల నివారణ",
        "title": "Handling Black Thrips (నల్ల తామర పురుగులు) in Tenali region",
        "message": "గత వారంలో మిరపలో నల్ల తామర పురుగు ఉధృతిని గమనించాను. నీలి రంగు జిగురు అట్టలు (ఎకరాకు 30) ఏర్పాటు చేశాను మరియు వేపనూనె (5 మి.లీ/లీ) పిచికారీ చేశాను. ఉధృతి బాగా తగ్గింది.",
        "date": "18 Nov 2026, 11:30 AM",
        "likes": 18,
        "liked": False,
        "replies": [
            {
                "author": "Venkat Reddy",
                "district": "Kurnool",
                "time": "18 Nov 2026, 12:15 PM",
                "text": "చాలా మంచి సలహా షైనీ గారు. నీలి అట్టలు పెట్టడం వల్ల రసాయన మందుల ఖర్చు చాలా తగ్గింది."
            }
        ]
    },
    {
        "id": 2,
        "author": "Venkat Reddy",
        "district": "Kurnool",
        "crop": "Groundnut",
        "tag": "ఎరువుల యాజమాన్యం",
        "title": "Gypsum application in pegging stage (వేరుశనగలో జిప్సం ప్రాముఖ్యత)",
        "message": "వేరుశనగలో ఊడలు దిగే దశలో (40-45 రోజులు) ఎకరాకు 200 కిలోల జిప్సం వేసి మట్టి ఎగదోశాను. కాయ నాణ్యత మరియు గింజ పరిమాణం గణనీయంగా పెరిగాయి.",
        "date": "16 Nov 2026, 04:20 PM",
        "likes": 25,
        "liked": False,
        "replies": [
            {
                "author": "Archana",
                "district": "Vijayawada",
                "time": "17 Nov 2026, 09:10 AM",
                "text": "జిప్సంలో ఉండే కాల్షియం మరియు సల్ఫర్ గింజ గట్టిపడటానికి ఎంతో దోహదపడతాయి."
            }
        ]
    },
    {
        "id": 3,
        "author": "Apparao",
        "district": "East Godavari",
        "crop": "Paddy",
        "tag": "విత్తనాలు & మార్కెట్",
        "title": "BPT 5204 (సాంబ మసూరి) certified seed availability near Rajahmundry",
        "message": "మా వద్ద నాణ్యమైన బి.పి.టి 5204 సర్టిఫైడ్ వరి విత్తనాలు అందుబాటులో ఉన్నాయి. అవసరమైన తోటి రైతులు సంప్రదించవచ్చు.",
        "date": "15 Nov 2026, 02:45 PM",
        "likes": 14,
        "liked": False,
        "replies": []
    }
]

DEFAULT_CHATS = {
    "Shiney (Guntur • Chilli)": {
        "name": "Shiney",
        "district": "Guntur",
        "crop": "Chilli (తేజా మిర్చి)",
        "avatar": "👩‍🌾",
        "online": True,
        "messages": [
            {"sender": "Shiney", "text": "నమస్కారం! గుంటూరు మరియు విజయవాడ మిర్చి యార్డులో ఈ రోజు తేజా రకం క్వింటాల్ ₹20,500 వరకు పలుకుతోంది.", "time": "10:15 AM"},
            {"sender": "You", "text": "నమస్కారం షైనీ గారు, నల్ల తామర పురుగుల నివారణకు మీరు ఏం వాడుతున్నారు?", "time": "10:20 AM"},
            {"sender": "Shiney", "text": "ఎకరాకు 35 నీలి జిగురు అట్టలు పెట్టాను. వేపనూనె 10000 ppm పిచికారీ చేయడం వల్ల ఉధృతి బాగా తగ్గింది.", "time": "10:22 AM"}
        ]
    },
    "Venkat Reddy (Kurnool • Groundnut)": {
        "name": "Venkat Reddy",
        "district": "Kurnool",
        "crop": "Groundnut (వేరుశనగ K-6)",
        "avatar": "🧔",
        "online": True,
        "messages": [
            {"sender": "Venkat Reddy", "text": "నమస్కారం! మీ ప్రాంతంలో వర్షాలు ఎలా ఉన్నాయి?", "time": "Yesterday, 03:10 PM"},
            {"sender": "You", "text": "నిన్న తేలికపాటి వర్షం పడింది వెంకట్ రెడ్డి గారు, తేమ బాగుంది.", "time": "Yesterday, 03:25 PM"},
            {"sender": "Venkat Reddy", "text": "మంచిది, ఊడలు దిగే సమయంలో ఎకరాకు 200 కిలోల జిప్సం వేయడం మర్చిపోకండి.", "time": "Yesterday, 03:30 PM"}
        ]
    },
    "Apparao (Godavari • Paddy)": {
        "name": "Apparao",
        "district": "East Godavari",
        "crop": "Paddy (వరి BPT 5204)",
        "avatar": "🌾",
        "online": True,
        "messages": [
            {"sender": "Apparao", "text": "నమస్కారం! మా వైపు గోదావరి కాల్వల ద్వారా నీటి సరఫరా బాగా జరుగుతోంది.", "time": "2 days ago"},
            {"sender": "You", "text": "వరిలో అగ్గి తెగులు నివారణకు ఏ మందు పిచికారీ చేశారు?", "time": "2 days ago"},
            {"sender": "Apparao", "text": "ట్రైసైక్లాజోల్ (బీమ్) 0.6 గ్రాము లేదా కాసుగామైసిన్ 2.5 మి.లీ/లీటర్ నీటికి కలిపి స్ప్రే చేశాం. బాగా పనిచేసింది.", "time": "2 days ago"}
        ]
    },
    "Srinivasulu (Anantapur • Horticulture)": {
        "name": "Srinivasulu",
        "district": "Anantapur",
        "crop": "Sweet Lime & Pomegranate (బత్తాయి)",
        "avatar": "🍊",
        "online": True,
        "messages": [
            {"sender": "Srinivasulu", "text": "నమస్కారం! బత్తాయి తోటలో బిందు సేద్యం (Drip) ద్వారా ఫెర్టిగేషన్ అందిస్తున్నాం.", "time": "Yesterday, 09:30 AM"},
            {"sender": "You", "text": "సూక్ష్మ పోషకాలు డ్రిప్ ద్వారా ఇస్తున్నారా?", "time": "Yesterday, 09:45 AM"},
            {"sender": "Srinivasulu", "text": "అవును, జింక్ సల్ఫేట్ మరియు బోరాన్ అందిస్తున్నాం. కాయ రంగు మరియు సైజు బాగుంది.", "time": "Yesterday, 09:50 AM"}
        ]
    }
}

def load_posts():
    if not POSTS_FILE.exists():
        os.makedirs(POSTS_FILE.parent, exist_ok=True)
        with open(POSTS_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_POSTS, f, indent=2, ensure_ascii=False)
        return DEFAULT_POSTS
    try:
        with open(POSTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return DEFAULT_POSTS

def save_posts(posts):
    with open(POSTS_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)

def load_chats():
    if not CHATS_FILE.exists():
        os.makedirs(CHATS_FILE.parent, exist_ok=True)
        with open(CHATS_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_CHATS, f, indent=2, ensure_ascii=False)
        return DEFAULT_CHATS
    try:
        with open(CHATS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return DEFAULT_CHATS

def save_chats(chats):
    with open(CHATS_FILE, "w", encoding="utf-8") as f:
        json.dump(chats, f, indent=2, ensure_ascii=False)

def generate_farmer_reply(contact: str, user_text: str) -> str:
    """Generate realistic, helpful farmer replies from Andhra Pradesh peers."""
    t = user_text.lower()
    
    if "shiney" in contact.lower():
        if any(w in t for w in ["ధర", "రేటు", "ధరలు", "price", "rate", "మార", "క్వింటా"]):
            return "గుంటూరు మిర్చి యార్డులో తేజా రకం ₹20,000 - ₹21,500 వరకు పలుకుతోంది. తాలు లేకుండా నాణ్యంగా ఉంటే మంచి ధర వస్తుంది."
        elif any(w in t for w in ["తామర", "పురుగు", "thrips", "pest", "మందు", "స్ప్రే"]):
            return "ఎకరాకు 35 నీలి జిగురు అట్టలు పెట్టండి. అవసరమైతే స్పైరోటెట్రామాట్ లేదా ఎసిఫేట్ 1.5 గ్రా/లీటర్ నీటికి కలిపి సాయంత్రం వేళ స్ప్రే చేయండి."
        elif any(w in t for w in ["వర్ష", "rain", "వాతావరణ"]):
            return "గుంటూరులో ప్రస్తుతానికి ఆకాశం నిర్మలంగా ఉంది. ఎండ ఎక్కువగా ఉండటం వల్ల పిచికారీకి అనుకూలంగా ఉంది."
        else:
            return "నమస్కారం తోటి రైతు మిత్రమా! మిరపలో ప్రస్తుత పూత మరియు కాయల దశ చాలా కీలకం. తేమ సమానంగా ఉండేలా చూసుకోండి."
            
    elif "venkat" in contact.lower():
        if any(w in t for w in ["జిప్సం", "gypsum", "ఎరువు", "fertilizer", "dose"]):
            return "వేరుశనగలో పూత పూర్తయి ఊడలు నేలలోకి దిగే 40-45 రోజుల దశలో ఎకరాకు 200 కిలోల జిప్సం వేసి మట్టి ఎగదోయాలి. దీనివల్ల కాయలు బాగా లావెక్కి దిగుబడి 20% పెరుగుతుంది."
        elif any(w in t for w in ["వర్ష", "తేమ", "నీరు", "rain", "water"]):
            return "కర్నూలు వైపు నిన్న తేలికపాటి జల్లులు పడ్డాయి. నేలలో తగినంత తేమ ఉన్నప్పుడు మాత్రమే జిప్సం లేదా ఎరువులు చల్లడం మంచిది."
        else:
            return "నమస్కారం అండి! మీ పొలంలో వేరుశనగ పంట ఏ దశలో ఉంది? ఆకుమచ్చ లేదా తిక్క తెగులు లక్షణాలు కనిపిస్తే వెంటనే తెలియజేయండి."
            
    elif "apparao" in contact.lower():
        if any(w in t for w in ["అగ్గి", "తెగులు", "blast", "మచ్చ", "disease"]):
            return "వరిలో అగ్గితెగులు (Rice Blast) నివారణకు ట్రైసైక్లాజోల్ (Tricyclazole 75% WP) 0.6 గ్రా/లీ లేదా కాసుగామైసిన్ 2.5 మి.లీ/లీటర్ నీటికి కలిపి పిచికారీ చేయండి."
        elif any(w in t for w in ["విత్తన", "seed", "bpt", "ధాన్యం", "ధర"]):
            return "మా వద్ద BPT 5204 సర్టిఫైడ్ విత్తనాలు సిద్ధంగా ఉన్నాయి. ప్రభుత్వం క్వింటాలుకు ₹2,320 మద్దతు ధర అందిస్తోంది."
        else:
            return "నమస్కారం! గోదావరి డెల్టాలో కాల్వల ద్వారా సమృద్ధిగా సాగునీరు అందుతోంది. మీ పంట ఏపుగా ఎదగడానికి జింక్ సల్ఫేట్ లోపం లేకుండా చూసుకోండి."
            
    elif "srinivasulu" in contact.lower():
        if any(w in t for w in ["డ్రిప్", "నీరు", "drip", "water"]):
            return "అనంతపురంలో నీటి ఎద్దడి రాకుండా బిందు సేద్యం (Drip) ద్వారా వారానికి రెండు సార్లు తడులు ఇస్తున్నాం. నేల తేమ నిలుపుకోవడానికి మల్చింగ్ షీట్లు వాడటం మంచిది."
        else:
            return "నమస్కారం! తోట పంటల్లో సూక్ష్మ పోషకాలైన బోరాన్ మరియు జింక్ ఫెర్టిగేషన్ ద్వారా అందిస్తే కాయ నాణ్యత బాగుంటుంది."
            
    return "నమస్కారం! మీ సమాచారం అందింది. పంటలో ఏదైనా సమస్య ఉంటే కలిసి చర్చించి పరిష్కరించుకుందాం."

RYTHU_BHAROSA_DIRECTORY = {
    "Vijayawada (Krishna)": {
        "office": "Joint Director of Agriculture (JDA), Vijayawada",
        "phone": "0866-2576688",
        "address": "Near PWD Grounds, Bandar Road, Vijayawada - 520002",
        "kisan_mitra": "Kisan Call Center / Agri Support Desk: 1800-180-1551 / 155251"
    },
    "Guntur": {
        "office": "Joint Director of Agriculture (JDA), Guntur",
        "phone": "0863-2234062",
        "address": "Collectorate Complex, Guntur - 522004",
        "kisan_mitra": "Rythu Bharosa Kendra Helpline: 155251 (Toll-Free)"
    },
    "Krishna": {
        "office": "Joint Director of Agriculture (JDA), Krishna",
        "phone": "08672-252445",
        "address": "Chilakalapudi, Machilipatnam / Vijayawada - 521002",
        "kisan_mitra": "Kisan Call Center: 1800-180-1551 (Toll-Free)"
    },
    "East Godavari": {
        "office": "Joint Director of Agriculture (JDA), East Godavari",
        "phone": "0884-2361734",
        "address": "Near Sub-Collector Office, Kakinada / Rajahmundry",
        "kisan_mitra": "Kisan Call Centre: 1800-180-1551 (Toll-Free)"
    },
    "Kurnool": {
        "office": "Joint Director of Agriculture (JDA), Kurnool",
        "phone": "08518-220464",
        "address": "Collectorate Road, Kurnool - 518002",
        "kisan_mitra": "Regional Agricultural Research Station (RARS) Nandyal: 08514-242224"
    },
    "Anantapur": {
        "office": "Joint Director of Agriculture (JDA), Anantapur",
        "phone": "08554-274152",
        "address": "Opposite Zilla Parishad, Anantapur - 515001",
        "kisan_mitra": "Agricultural Research Station (ARS) Anantapur: 08554-200088"
    }
}

MARKET_DB = DATA_DIR / "marketplace.sqlite3"
DISTRICTS = [
    "Anantapur", "Chittoor", "East Godavari", "Guntur", "Kadapa",
    "Krishna", "Kurnool", "Nellore", "Prakasam", "Srikakulam",
    "Visakhapatnam", "Vizianagaram", "West Godavari"
]

def marketplace_connection():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(MARKET_DB, timeout=15)
    conn.row_factory = sqlite3.Row
    conn.execute("""CREATE TABLE IF NOT EXISTS listings (
        id TEXT PRIMARY KEY, owner_id TEXT NOT NULL, owner_name TEXT NOT NULL,
        item TEXT NOT NULL, category TEXT NOT NULL, listing_type TEXT NOT NULL,
        district TEXT NOT NULL, description TEXT NOT NULL,
        price REAL, unit TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'Available',
        created_at TEXT NOT NULL)""")
    conn.commit()
    return conn
