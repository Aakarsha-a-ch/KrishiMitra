/**
 * KrishiMitra - Modern Zero-Lag Frontend Controller
 * Developed by: Aakarsha Archana & Shiney (B.Tech AIML)
 */

// Application State
let currentLang = 'te'; // 'te' (Telugu) | 'en' (English)
let activeTab = 'home';
let currentUser = {
  name: 'Archana',
  phone: '9440123456',
  district: 'Vijayawada (Krishna)',
  village: 'ఏనికపాడు (Enikepadu), విజయవాడ రూరల్',
  crop: 'Paddy',
  cropTe: 'వరి (Paddy BPT 5204)',
  acres: 3.5,
  avatar: '👩‍🌾'
};

let selectedLeafFile = null;
let currentDirectContact = 'వెంకట్రావు (వరి రైతు)';

// 100% Complete Bilingual Dictionary
const translations = {
  te: {
    // Menu Names (One-Line Desktop Nav - Fits without cutting off)
    nav_item_1: "హోమ్",
    nav_item_2: "తెగుళ్ల స్కానర్",
    nav_item_3: "ప్రత్యక్ష వాతావరణం",
    nav_item_4: "నేల ఆరోగ్యం",
    nav_item_5: "పంట సిఫార్సు",
    nav_item_6: "రైతు వేదిక",
    nav_item_7: "AI అసిస్టెంట్",
    nav_item_8: "రైతు ప్రొఫైల్",
    nav_item_9: "ప్రాజెక్ట్ వివరాలు",

    // Mobile Bottom Bar
    nav_b_home: "హోమ్",
    nav_b_health: "స్కానర్",
    nav_b_weather: "వాతావరణం",
    nav_b_soil: "నేల",
    nav_b_ai: "AI Assistant",
    nav_b_comm: "వేదిక",
    nav_b_about: "వివరాలు",

    // Sidebar & Common Labels
    lbl_language: "భాష / Language",
    lbl_location: "ప్రాంతం (Location)",
    lbl_primary_crop: "ప్రధాన పంట (Primary Crop)",
    lbl_nav_menu: "నావిగేషన్ మెనూ",
    btn_signout: "లాగ్ అవుట్ / రైతును మార్చండి",
    btn_signout_short: "లాగ్ అవుట్",
    btn_login_top: "ప్రవేశం",

    // Hero Section
    hero_greeting: "నమస్కారం, {name} గారు! 🌾",
    hero_inst: "👩‍💻 ఆకర్ష అర్చన & షైనీ | B.Tech AIML",
    hero_desc: "కృష్ణా డెల్టా మరియు ఆంధ్రప్రదేశ్ రైతుల కోసం రూపొందించిన ఆధునిక AI వ్యవసాయ నిర్ణయ వేదిక. మొబైల్ నెట్ తెగుళ్ల గుర్తింపు, లైవ్ విజయవాడ వాతావరణం, సమగ్ర నేల ఎరువుల లెక్కలు మరియు మార్కెట్ ధరలు ఒకే చోట.",
    home_weather_title: "లైవ్ విజయవాడ వాతావరణం",
    view_full_weather: "పూర్తి వాతావరణం చూడండి",
    core_features_title: "ప్రధాన సేవలు",
    core_features_sub: "మీ పంట రక్షణ, నేల ఆరోగ్యం మరియు దిగుబడి కోసం ఆధునిక డిజిటల్ ఉపకరణాలు:",

    // Dashboard Cards
    card_scanner_title: "పంట ఆరోగ్యం (తెగుళ్ల స్కానర్)",
    card_scanner_desc: "ఆకు ఫోటో తీసి అప్‌లోడ్ చేయండి. మొబైల్‌నెట్ AI తక్షణమే తెగులును గుర్తించి సేంద్రీయ మరియు రసాయన నివారణలను సూచిస్తుంది.",
    btn_scan_now: "ఆకును స్కాన్ చేయండి",
    card_weather_title: "వాతావరణం (విజయవాడ ప్రత్యక్ష సమాచారం)",
    card_weather_desc: "విజయవాడ, గుంటూరు మరియు ఏపీ జిల్లాల గంట గంట వర్షం, ఉష్ణోగ్రత మరియు మందుల పిచికారీ అనుకూల సమయం.",
    btn_check_weather: "వాతావరణం చూడండి",
    card_soil_title: "నేల ఆరోగ్యం",
    card_soil_desc: "NPK విలువలను బట్టి మీ పంటకు సరిపోయే యూరియా, డీఏపీ, ఎంఓపీ బస్తాల మోతాదు మరియు విడతల వారీ షెడ్యూల్.",
    btn_calc_soil: "ఎరువులు లెక్కించండి",
    card_rec_title: "పంట ఎంపిక సిఫార్సు",
    card_rec_desc: "మీ నేల స్వభావం, వర్షపాతం మరియు ఉష్ణోగ్రత ఆధారంగా అధిక దిగుబడినిచ్చే అత్యుత్తమ పంటలను తెలుసుకోండి.",
    btn_get_rec: "పంట సిఫార్సు పొందండి",
    card_chat_title: "ఎఐ సహాయకుడు (Chatbot)",
    card_chat_desc: "తెలుగు మరియు ఆంగ్లంలో 24/7 వ్యవసాయ ప్రశ్నలకు తక్షణ శాస్త్రీయ సమాధానాలు, సలహాలు మరియు పథకాల వివరాలు.",
    btn_ask_ai: "సందేహం అడగండి",
    card_community_title: "రైతు సంభాషణ & వేదిక",
    card_community_desc: "కృష్ణా, గుంటూరు మరియు ఆంధ్రప్రదేశ్ తోటి రైతులతో అనుభవాలు, మార్కెట్ ధరలు మరియు సలహాలు పంచుకోండి.",
    btn_open_community: "రైతులతో మాట్లాడండి",
    mandi_rates_title: "ఆంధ్రప్రదేశ్ మార్కెట్ యార్డ్ లైవ్ ధరలు (AP Mandi Rates)",
    btn_show_more_mandi: "మరిన్ని పంటల ధరలు చూడండి (Show All 15 Crops)",
    btn_show_less_mandi: "తక్కువ చూపించు (Show Top Crops Only)",
    helpline_title: "అత్యవసర రైతు సంప్రదింపు నంబర్లు (AP Government & KVK)",

    // Emergency Helpline
    hl_kisan: "కిసాన్ కాల్ సెంటర్:",
    hl_tollfree: "టోల్ ఫ్రీ",
    hl_rbk: "వైఎస్సార్ రైతు భరోసా కేంద్రం:",
    hl_kvk: "కృష్ణా జిల్లా కృషి విజ్ఞాన కేంద్రం:",

    // Crop Health (Scanner)
    scanner_header: "పంట ఆరోగ్యం (తెగుళ్ల స్కానర్)",
    scanner_sub: "ఆకుపై మచ్చలు, రంగు మార్పు లేదా తెగులు ఉన్న భాగాన్ని ఫోటో తీసి అప్‌లోడ్ చేయండి:",
    upload_prompt: "ఫోటో ఎంచుకోండి లేదా కెమెరాతో తీయండి",
    upload_hint: "JPG, PNG లేదా WEBP ఫార్మాట్ (గరిష్టం 10 MB)",
    btn_start_analysis: "AI తెగుళ్ల విశ్లేషణ ప్రారంభించండి",
    scanner_waiting: "ఫోటో అప్‌లోడ్ చేసి విశ్లేషణ బటన్ నొక్కండి",
    scanner_hint: "మొబైల్‌నెట్ AI మోడల్ 38 రకాల పంట వ్యాధులను మరియు ఆరోగ్యకరమైన ఆకులను తక్షణమే గుర్తిస్తుంది.",
    analyzing: "చిత్రాన్ని విశ్లేషిస్తోంది... దయచేసి వేచి ఉండండి",

    // Weather
    weather_header: "వాతావరణం (విజయవాడ ప్రత్యక్ష సమాచారం)",
    weather_sub: "కృష్ణా డెల్టా మరియు ఏపీ జిల్లాల ఖచ్చితమైన వాతావరణ నివేదిక:",
    select_district: "జిల్లా / ప్రాంతాన్ని ఎంచుకోండి:",
    refresh: "తాజాకరించు",
    metric_temp: "ఉష్ణోగ్రత",
    metric_humidity: "గాలిలో తేమ (Humidity)",
    metric_wind: "గాలి వేగం",
    metric_rain: "వర్షపాతం అవకాశం",
    metric_optimal: "పంటలకు అనుకూలం",
    rain_low: "వర్షం సూచన లేదు",
    spray_advisory_title: "రైతు పిచికారీ అనుకూల సూచిక (Spraying Window)",
    forecast_title: "రాబోయే 5 రోజుల సూచన",

    // Soil
    soil_header: "నేల ఆరోగ్యం",
    soil_sub: "మీ భూమి సాయిల్ టెస్ట్ రిపోర్ట్ (NPK) ఆధారంగా సమగ్ర ఎరువుల విడతల మోతాదు:",
    label_crop: "పంటను ఎంచుకోండి:",
    lbl_ph: "నేల pH:",
    lbl_n: "నత్రజని (Nitrogen - N) kg/హెక్టార్:",
    lbl_p: "భాస్వరం (Phosphorus - P) kg/హెక్టార్:",
    lbl_k: "పొటాషియం (Potassium - K) kg/హెక్టార్:",
    btn_calculate_split: "ఎరువుల మోతాదును విశ్లేషించండి",
    soil_rec_title: "📋 ఎకరానికి సిఫార్సు చేయబడిన ఎరువులు",

    // Crop Rec
    rec_header: "పంట ఎంపిక సిఫార్సు",
    rec_sub: "రైతు నేల మరియు స్థానిక వాతావరణ పరిస్థితుల ఆధారంగా అత్యంత లాభదాయక పంటను లెక్కించండి:",
    lbl_rainfall: "వార్షిక వర్షపాతం (Rainfall mm):",
    btn_run_rec: "సిఫార్సు చేయబడిన పంటను లెక్కించండి",
    rec_waiting: "విలువలను నమోదు చేసి బటన్ నొక్కండి",
    rec_hint: "మెషిన్ లెర్నింగ్ మోడల్ మీ నేల మరియు వాతావరణానికి అనువైన టాప్ పంటలను సిఫార్సు చేస్తుంది.",

    // Assistant
    chat_header: "ఎఐ సహాయకుడు (Chatbot)",
    chat_sub: "వ్యవసాయ శాస్త్రవేత్తల పరిశోధన ఆధారిత జ్ఞానంతో తెలుగు మరియు ఆంగ్లంలో సమాధానాలు:",
    btn_send: "పంపండి",

    // Community
    comm_header: "రైతు సంభాషణ & వేదిక (Farmer Connect & Forum)",
    comm_sub: "ఆంధ్రప్రదేశ్ కృష్ణా, గుంటూరు, గోదావరి జిల్లాల తోటి రైతులతో అనుభవాలు, మార్కెట్ ధరలు మరియు తెగుళ్ల నివారణపై ప్రత్యక్ష చర్చ:",
    create_post_title: "రైతు వేదికపై కొత్త సమాచారం లేదా ప్రశ్న పోస్ట్ చేయండి:",
    opt_pest: "🛡️ తెగుళ్ల నివారణ (Pest & Disease)",
    opt_market: "💰 మార్కెట్ ధరలు (Market Rates)",
    opt_fert: "🧪 ఎరువుల యాజమాన్యం (Fertilizers)",
    opt_seeds: "🌱 విత్తనాలు (Seeds)",
    opt_general: "🌾 సాధారణ చర్చ (General)",
    post_author_hint: "👨‍🌾 మీ పేరుతో నేరుగా ప్రచురించబడుతుంది",
    filter_all: "అన్నీ (All)",
    filter_pests: "🛡️ తెగుళ్లు",
    filter_market: "💰 మార్కెట్",
    filter_fert: "🧪 ఎరువులు",
    filter_seeds: "🌱 విత్తనాలు",
    btn_post: "పోస్ట్ చేయండి",
    direct_chat_title: "రైతులతో ప్రత్యక్ష సంభాషణ",
    btn_direct_send: "పంపండి",

    // Profile
    profile_header: "రైతు ప్రొఫైల్",
    profile_sub: "మీ వ్యక్తిగత వివరాలు, క్షేత్ర సమాచారం మరియు సాగు వివరాల నిర్వహణ:",
    verified_farmer: "✓ ప్రామాణీకరించబడిన రైతు",
    btn_edit_profile: "ప్రొఫైల్ సవరించండి (Edit Profile)",
    lbl_acres: "వ్యవసాయ భూమి",
    lbl_primary_crop: "ప్రధాన పంట",
    lbl_location: "ప్రాంతం",
    lbl_irrigation: "సాగునీటి విధానం",
    irrigation_val: "కాలువ & బోరు బావి",
    soil_type_val: "సారవంతమైన డెల్టా ఒండ్రు నేల",
    edit_profile_title: "✏️ రైతు ప్రొఫైల్ వివరాల సవరణ (Edit Farm Profile)",
    btn_cancel_edit: "రద్దు చేయండి (Cancel)",
    btn_cancel_short: "✕ రద్దు (Cancel)",
    btn_save_profile: "💾 వివరాలు భద్రపరచండి (Save Changes)",
    lbl_scheme: "రైతు పథకం",
    prof_personal_sec: "👤 రైతు వ్యక్తిగత సమాచారం:",
    lbl_farmer_name: "రైతు పేరు:",
    lbl_registered_phone: "నమోదిత ఫోన్:",
    lbl_district: "జిల్లా:",
    lbl_village_mandal: "గ్రామం / మండలం:",
    prof_crop_land_sec: "🚜 పంట & భూమి వివరాలు:",
    lbl_land_holding: "భూమి విస్తీర్ణం:",
    lbl_soil_nature: "నేల స్వభావం:",
    lbl_welfare_scheme: "రైతు సంక్షేమ పథకం:",
    scheme_val: "వైఎస్సార్ రైతు భరోసా, పీఎం కిసాన్ సమ్మాన్ నిధి",

    // About
    about_header: "ప్రాజెక్ట్ వివరాలు (About)",
    about_sub: "కృషిమిత్ర ప్రాజెక్ట్ సృష్టికర్తలు మరియు సాంకేతిక విశేషాలు:",
    clarification_title: "డెవలపర్లు (Developers):",
    clarification_body_te: "కృషిమిత్ర ప్రాజెక్ట్ డెవలపర్లు: ఆకర్ష అర్చన & షైనీ (B.Tech AIML).",
    clarification_body_en: "(Project Developers: Aakarsha Archana & Shiney - B.Tech AIML).",
    team_title: "డెవలపర్లు (Developers)",
    dev_role_1: "కోర్సు",
    dev_desc_1: "B.Tech AIML",
    dev_role_2: "కోర్సు",
    dev_desc_2: "B.Tech AIML",
    tech_title: "సాంకేతిక విశేషాలు (Technical Architecture)",

    // Login Portal
    demo_quick_title: "⚡ ఒక్క ట్యాప్‌తో ప్రవేశించండి (డెమో రైతులు)",
    demo_quick_sub: "పాస్‌వర్డ్ అవసరం లేకుండా వెంటనే డాష్‌బోర్డ్ తెరవండి:",
    auth_tab_login: "🔑 లాగిన్ (Mobile Login)",
    auth_tab_register: "📝 కొత్త రైతు నమోదు (Register)",
    lbl_auth_user: "ఫోన్ నంబర్ లేదా పేరు:",
    lbl_auth_pass: "పాస్‌వర్డ్ (Password):",
    btn_submit_login: "ఖాతాలోకి ప్రవేశించండి (Sign In)",
    btn_submit_reg: "కొత్త ఖాతా సృష్టించండి (Register)",
    back_to_dashboard: "డాష్‌బోర్డ్‌కి వెళ్లండి (Back to Dashboard)",

    // Extra Localized UI Elements
    brand_sub: "కృషిమిత్ర",
    hero_instant_speed: "⚡ 0ms తక్షణ వేగం",
    wind_dir_east: "తూర్పు దిశ",
    lbl_temp_c: "ఉష్ణోగ్రత (°C):",
    lbl_humidity_pct: "తేమ (%):",
    prof_student_credit: "👩‍💻 ఆకర్ష అర్చన & షైనీ (B.Tech AIML)",
    prof_sub_holding: "కృష్ణా డెల్టా వ్యవసాయ హోల్డింగ్",
    prof_sub_variety: "BPT 5204 సాంబా మసూరి",
    prof_sub_canal: "కృష్ణా తూర్పు ప్రధాన కాలువ",
    prof_spec_title: "📋 క్షేత్ర & రైతు వివరాల నివేదిక (Farm Specifications)",
    prof_reg_season: "నమోదు: నవంబర్ 2026 (ఖరీఫ్ సీజన్)",
    lbl_edit_name: "పూర్తి పేరు (Farmer Full Name):",
    lbl_edit_phone: "మొబైల్ ఖాతా (Mobile Number):",
    lbl_edit_district: "జిల్లా (District):",
    lbl_edit_village: "గ్రామం / మండలం (Village / Mandal):",
    lbl_edit_crop: "ప్రధాన పంట (Primary Crop):",
    lbl_edit_acres: "వ్యవసాయ భూమి విస్తీర్ణం - ఎకరాల్లో (Land Size in Acres):",
    lbl_reg_name: "పూర్తి పేరు (Full Name):",
    lbl_reg_phone: "మొబైల్ నంబర్ (10 అంకెలు):",
    lbl_reg_dist: "జిల్లా:",
    lbl_reg_crop: "ప్రధాన పంట:",
    lbl_reg_acres: "ఎకరాలు (Acres):",
    lbl_reg_pass: "పాస్‌వర్డ్ (కనీసం 6 అక్షరాలు):",
    tech_vision_title: "🌿 విజన్ మోడల్:",
    tech_vision_desc: "MobileNetV2 డీప్ లెర్నింగ్ మోడల్ (54,305 ఆకుల చిత్రాలతో 97.15% ఖచ్చితత్వంతో శిక్షణ).",
    tech_frontend_title: "⚡ ఫ్రంటెండ్:",
    tech_frontend_desc: "స్వచ్ఛమైన Semantic HTML5, CSS3, SVGs, Vanilla JS (0ms తక్షణ టాబ్ నావిగేషన్).",
    tech_weather_title: "⛅ వాతావరణం:",
    tech_weather_desc: "ఓపెన్-మెటియో API ద్వారా లైవ్ విజయవాడ మరియు ఏపీ జిల్లాల స్ప్రే విండో అడ్వైజరీ.",
    tech_ai_title: "🤖 AI అసిస్టెంట్:",
    tech_ai_desc: "హైబ్రిడ్ RAG, ANGRAU ప్యాకేజ్ ఆఫ్ ప్రాక్టీసెస్ మరియు వెబ్ సెర్చ్ అగ్రిగేషన్."
  },

  en: {
    // Menu Names (Exact from Original Streamlit)
    nav_item_1: "Home",
    nav_item_2: "Disease Scanner",
    nav_item_3: "Live Weather",
    nav_item_4: "Soil Health",
    nav_item_5: "Crop Advisory",
    nav_item_6: "Farmer Chat",
    nav_item_7: "AI Assistant",
    nav_item_8: "Profile",
    nav_item_9: "About",

    // Mobile Bottom Bar
    nav_b_home: "Home",
    nav_b_health: "Scanner",
    nav_b_weather: "Weather",
    nav_b_soil: "Soil",
    nav_b_ai: "AI Assistant",
    nav_b_comm: "Connect",
    nav_b_about: "About",

    // Sidebar & Common Labels
    lbl_language: "Language",
    lbl_location: "Location",
    lbl_primary_crop: "Primary Crop",
    lbl_nav_menu: "Navigation Menu",
    btn_signout: "Sign Out / Switch User",
    btn_signout_short: "Sign Out",
    btn_login_top: "Sign In",

    // Hero Section
    hero_greeting: "Welcome, {name}! 🌾",
    hero_inst: "👩‍💻 Aakarsha Archana & Shiney | B.Tech AIML",
    hero_desc: "Advanced Agricultural Decision Support System engineered for farmers across Krishna Delta and Andhra Pradesh. Instant MobileNet disease diagnosis, Open-Meteo live weather telemetry, soil NPK fertilizer scheduling, and live AP Mandi rates.",
    home_weather_title: "Live Vijayawada Weather",
    view_full_weather: "View Detailed Weather",
    core_features_title: "Core Services",
    core_features_sub: "Modern digital tools engineered for crop protection, soil health, and maximizing yield:",

    // Dashboard Cards
    card_scanner_title: "Crop Health (Disease Scanner)",
    card_scanner_desc: "Upload or capture a photo of an affected leaf. MobileNet AI identifies diseases in milliseconds and provides organic & chemical remedies.",
    btn_scan_now: "Scan Leaf Now",
    card_weather_title: "Weather (Vijayawada Telemetry)",
    card_weather_desc: "Hour-by-hour rainfall, temperature, and pesticide spraying advisory for Vijayawada, Guntur, and AP districts.",
    btn_check_weather: "Check Weather",
    card_soil_title: "Soil Health",
    card_soil_desc: "Calculates precise per-acre Urea, DAP, and MOP bag requirements along with split schedules from NPK lab values.",
    btn_calc_soil: "Calculate Fertilizers",
    card_rec_title: "Crop Recommendation",
    card_rec_desc: "Recommends top high-yielding crops suited to your soil profile, rainfall, and temperature conditions.",
    btn_get_rec: "Get Recommendation",
    card_chat_title: "AI Assistant (AI Agro Assistant)",
    card_chat_desc: "24/7 bilingual agricultural advisory assistant powered by research-backed agronomy databases and AP schemes.",
    btn_ask_ai: "Ask Assistant",
    card_community_title: "Farmer Connect & Chat",
    card_community_desc: "Connect, share market insights, and message fellow farmers across Krishna and Guntur districts.",
    btn_open_community: "Join Forum",
    mandi_rates_title: "Live Andhra Pradesh Mandi Market Rates",
    btn_show_more_mandi: "Show All Crop Prices (15 Crops)",
    btn_show_less_mandi: "Show Top Crops Only",
    helpline_title: "Emergency Agricultural Helpline Numbers (AP Government & KVK)",
    hl_kisan: "Kisan Call Centre:",
    hl_tollfree: "Toll-Free",
    hl_rbk: "Rythu Bharosa Kendra:",
    hl_kvk: "Krishna Krishi Vigyan Kendra (KVK):",

    // Crop Health (Scanner)
    scanner_header: "Crop Health (Disease Scanner)",
    scanner_sub: "Upload or take a photo of an affected leaf for instant AI diagnostics:",
    upload_prompt: "Select photo or capture with camera",
    upload_hint: "JPG, PNG or WEBP format (Max 10 MB)",
    btn_start_analysis: "Start AI Disease Analysis",
    scanner_waiting: "Upload a leaf photo and click Analyze",
    scanner_hint: "MobileNet AI model identifies 38 crop disease classes and healthy leaves with 97%+ accuracy.",
    analyzing: "Analyzing leaf image with MobileNet AI... Please wait",

    // Weather
    weather_header: "Weather (Vijayawada Telemetry)",
    weather_sub: "Real-time telemetry and 5-day agro-meteorological forecast for AP districts:",
    select_district: "Select District / Location:",
    refresh: "Refresh",
    metric_temp: "Temperature",
    metric_humidity: "Humidity",
    metric_wind: "Wind Speed",
    metric_rain: "Rainfall Chance",
    metric_optimal: "Optimal for crops",
    rain_low: "No rain expected",
    spray_advisory_title: "Farmer Spraying Window Advisory",
    forecast_title: "Next 5 Days Agro-Forecast",

    // Soil
    soil_header: "Soil Health",
    soil_sub: "Calculate exact per-acre fertilizer requirements and split stages based on NPK soil tests:",
    label_crop: "Select Crop:",
    lbl_ph: "Soil pH:",
    lbl_n: "Nitrogen (N) kg/ha:",
    lbl_p: "Phosphorus (P) kg/ha:",
    lbl_k: "Potassium (K) kg/ha:",
    btn_calculate_split: "Calculate Fertilizer Doses",
    soil_rec_title: "📋 Recommended Fertilizers Per Acre",

    // Crop Rec
    rec_header: "Crop Recommendation",
    rec_sub: "Determine the most profitable and suitable crop for your soil and climate parameters:",
    lbl_rainfall: "Annual Rainfall (mm):",
    btn_run_rec: "Calculate Suitable Crop",
    rec_waiting: "Enter soil test values and click Calculate",
    rec_hint: "Machine Learning model computes the highest yielding crops for your soil profile.",

    // Assistant
    chat_header: "AI Assistant (AI Agro Assistant)",
    chat_sub: "Research-grounded agricultural advisory in Telugu and English:",
    btn_send: "Send",

    // Community
    comm_header: "Farmer Connect & Chat (Community Forum)",
    comm_sub: "Engage with fellow farmers across Krishna Delta on market prices, pest control, and field tips:",
    create_post_title: "Post New Information or Query to Farmer Forum:",
    opt_pest: "🛡️ Pest & Disease Control",
    opt_market: "💰 Mandi Market Rates",
    opt_fert: "🧪 Fertilizer Management",
    opt_seeds: "🌱 Seed Availability",
    opt_general: "🌾 General Farming Discussion",
    post_author_hint: "👨‍🌾 Published under your farmer profile",
    filter_all: "All Discussions",
    filter_pests: "🛡️ Pests",
    filter_market: "💰 Market",
    filter_fert: "🧪 Fertilizers",
    filter_seeds: "🌱 Seeds",
    btn_post: "Publish Post",
    direct_chat_title: "Direct Farmer Chat",
    btn_direct_send: "Send",

    // Profile
    profile_header: "Farmer Profile",
    profile_sub: "Manage farm specifications, registered crops, and personal profile details:",
    verified_farmer: "✓ Verified Farmer",
    btn_edit_profile: "Edit Profile",
    lbl_acres: "Land Size",
    lbl_primary_crop: "Primary Crop",
    lbl_location: "Location",
    lbl_irrigation: "Irrigation System",
    irrigation_val: "Canal & Borewell",
    soil_type_val: "Fertile Delta Alluvial Soil",
    edit_profile_title: "✏️ Edit Farm Profile",
    btn_cancel_edit: "Cancel",
    btn_cancel_short: "✕ Cancel",
    btn_save_profile: "💾 Save Changes",
    lbl_scheme: "Farmer Welfare Scheme",
    prof_personal_sec: "👤 Farmer Identity & Contact:",
    lbl_farmer_name: "Farmer Name:",
    lbl_registered_phone: "Registered Mobile:",
    lbl_district: "District:",
    lbl_village_mandal: "Village / Mandal:",
    prof_crop_land_sec: "🚜 Farm Specifications & Land:",
    lbl_land_holding: "Land Holding:",
    lbl_soil_nature: "Soil Type:",
    lbl_welfare_scheme: "Welfare Scheme:",
    scheme_val: "YSR Rythu Bharosa, PM-Kisan Samman Nidhi",

    // About
    about_header: "About",
    about_sub: "KrishiMitra project creators and technical architecture:",
    clarification_title: "Developers:",
    clarification_body_te: "Project Developers: Aakarsha Archana & Shiney (B.Tech AIML).",
    clarification_body_en: "(Project Developers: Aakarsha Archana & Shiney - B.Tech AIML).",
    team_title: "Developers",
    dev_role_1: "Course",
    dev_desc_1: "B.Tech AIML",
    dev_role_2: "Course",
    dev_desc_2: "B.Tech AIML",
    tech_title: "Technical Architecture",

    // Login Portal
    demo_quick_title: "⚡ 1-Tap Quick Access (Demo Profiles)",
    demo_quick_sub: "Enter instantly without entering a password:",
    auth_tab_login: "🔑 Mobile Login",
    auth_tab_register: "📝 New Registration",
    lbl_auth_user: "Mobile Number or Username:",
    lbl_auth_pass: "Password:",
    btn_submit_login: "Sign In to Farm Portal",
    btn_submit_reg: "Register New Account",
    back_to_dashboard: "Continue to Dashboard (Back)",

    // Extra Localized UI Elements
    brand_sub: "KrishiMitra",
    hero_instant_speed: "⚡ 0ms Instant Speed",
    wind_dir_east: "East Direction",
    lbl_temp_c: "Temperature (°C):",
    lbl_humidity_pct: "Humidity (%):",
    prof_student_credit: "👩‍💻 Aakarsha Archana & Shiney (B.Tech AIML)",
    prof_sub_holding: "Krishna Delta Farm Holding",
    prof_sub_variety: "BPT 5204 Samba Mahsuri",
    prof_sub_canal: "Krishna East Main Canal",
    prof_spec_title: "📋 Farm & Farmer Specifications Report",
    prof_reg_season: "Registered: November 2026 (Kharif Season)",
    lbl_edit_name: "Farmer Full Name:",
    lbl_edit_phone: "Mobile Number:",
    lbl_edit_district: "District:",
    lbl_edit_village: "Village / Mandal:",
    lbl_edit_crop: "Primary Crop:",
    lbl_edit_acres: "Land Size (in Acres):",
    lbl_reg_name: "Full Name:",
    lbl_reg_phone: "Mobile Number (10 digits):",
    lbl_reg_dist: "District:",
    lbl_reg_crop: "Primary Crop:",
    lbl_reg_acres: "Land Size (Acres):",
    lbl_reg_pass: "Password (min 6 chars):",
    tech_vision_title: "🌿 Vision Model:",
    tech_vision_desc: "MobileNetV2 Deep Learning model (trained on 54,305 leaf images with 97.15% accuracy).",
    tech_frontend_title: "⚡ Frontend:",
    tech_frontend_desc: "Pure Semantic HTML5, CSS3, SVGs, Vanilla JS (0ms instant tab navigation).",
    tech_weather_title: "⛅ Weather:",
    tech_weather_desc: "Live Vijayawada & AP district spray window advisory via Open-Meteo API.",
    tech_ai_title: "🤖 AI Assistant:",
    tech_ai_desc: "Hybrid RAG, ANGRAU Package of Practices and live agricultural web search aggregation."
  }
};

// ================= Custom HTML5 Canvas Icon Drawer (NO EMOJIS) =================
// Canvas rendering deprecated in favor of scalable vector SVGs
function drawCustomCanvasIcon(canvas, iconName, isActive = false) {}
function renderAllCanvasIcons() {}

// 0ms Instant Client-Side Tab Switching
// 0ms Instant Client-Side Tab Switching
function showTab(tabId) {
  activeTab = tabId;

  // Toggle main views
  document.querySelectorAll('.km-view').forEach(view => {
    view.classList.remove('active');
  });
  const targetView = document.getElementById(`view-${tabId}`);
  if (targetView) targetView.classList.add('active');

  // Toggle sidebar menu items
  document.querySelectorAll('.km-menu-link').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-tab') === tabId);
  });

  // Toggle mobile bottom nav items
  document.querySelectorAll('.km-nav-item').forEach(item => {
    item.classList.toggle('active', item.getAttribute('data-tab') === tabId);
  });

  // Close mobile sidebar if open
  const sidebar = document.getElementById('km-sidebar');
  if (sidebar) sidebar.classList.remove('open');

  window.scrollTo({ top: 0, behavior: 'instant' });
}

// Mobile Sidebar Toggle
function toggleMobileSidebar() {
  const sidebar = document.getElementById('km-sidebar');
  if (sidebar) sidebar.classList.toggle('open');
}

// Language Controller: 100% Consistent Language Application
// Dropdown Option Dictionaries for Consistent Bilingual Display
const DISTRICT_LABELS = {
  "Vijayawada (Krishna)": { te: "విజయవాడ (కృష్ణా)", en: "Vijayawada (Krishna)" },
  "Guntur": { te: "గుంటూరు", en: "Guntur" },
  "Machilipatnam": { te: "మచిలీపట్నం", en: "Machilipatnam" },
  "Amaravati": { te: "అమరావతి", en: "Amaravati" },
  "Eluru": { te: "ఏలూరు", en: "Eluru" },
  "West Godavari": { te: "పశ్చిమ గోదావరి", en: "West Godavari" },
  "East Godavari": { te: "తూర్పు గోదావరి", en: "East Godavari" },
  "Rajahmundry": { te: "రాజమండ్రి", en: "Rajahmundry" },
  "Kakinada": { te: "కాకినాడ", en: "Kakinada" },
  "Nellore": { te: "నెల్లూరు", en: "Nellore" },
  "Kurnool": { te: "కర్నూలు", en: "Kurnool" },
  "Anantapur": { te: "అనంతపురం", en: "Anantapur" },
  "Chittoor": { te: "చిత్తూరు", en: "Chittoor" },
  "Kadapa": { te: "కడప", en: "Kadapa" },
  "Prakasam": { te: "ప్రకాశం", en: "Prakasam" },
  "Tirupati": { te: "తిరుపతి", en: "Tirupati" },
  "Visakhapatnam": { te: "విశాఖపట్నం", en: "Visakhapatnam" }
};

const CROP_LABELS = {
  "Paddy": { te: "వరి (Paddy / Rice)", en: "Paddy (Rice)" },
  "Chilli": { te: "మిర్చి (Chilli)", en: "Chilli (Mirchi)" },
  "Cotton": { te: "పత్తి (Cotton)", en: "Cotton" },
  "Maize": { te: "మొక్కజొన్న (Maize)", en: "Maize (Corn)" },
  "Groundnut": { te: "వేరుశనగ (Groundnut)", en: "Groundnut (Peanut)" },
  "Sugarcane": { te: "చెరకు (Sugarcane)", en: "Sugarcane" },
  "Turmeric": { te: "పసుపు (Turmeric)", en: "Turmeric" },
  "Blackgram": { te: "మినుము (Blackgram)", en: "Blackgram (Urad)" },
  "Greengram": { te: "పెసర (Greengram)", en: "Greengram (Moong)" },
  "Redgram": { te: "కందులు (Redgram)", en: "Redgram (Toor)" },
  "Banana": { te: "అరటి (Banana)", en: "Banana" },
  "Mango": { te: "మామిడి (Mango)", en: "Mango" },
  "Tomato": { te: "టమోటా (Tomato)", en: "Tomato" },
  "Tobacco": { te: "పొగాకు (Tobacco)", en: "Tobacco" }
};

function updateDropdownsLanguage(isTel) {
  const langKey = isTel ? 'te' : 'en';
  document.querySelectorAll('select').forEach(sel => {
    Array.from(sel.options).forEach(opt => {
      if (DISTRICT_LABELS[opt.value]) {
        opt.text = DISTRICT_LABELS[opt.value][langKey];
      } else if (CROP_LABELS[opt.value]) {
        opt.text = CROP_LABELS[opt.value][langKey];
      }
    });
  });
}

function setLanguage(lang) {
  currentLang = lang;
  applyLanguage();
}

function toggleLanguage() {
  currentLang = (currentLang === 'te') ? 'en' : 'te';
  applyLanguage();
}

function applyLanguage() {
  const dict = translations[currentLang];
  const isTel = (currentLang === 'te');

  // Update language toggle label on header
  const langLabel = document.getElementById('lang-label');
  if (langLabel) langLabel.innerText = isTel ? 'తెలుగు' : 'English';

  // Update language buttons active state (if present in sidebar)
  const btnTe = document.getElementById('btn-lang-te');
  const btnEn = document.getElementById('btn-lang-en');
  if (btnTe && btnEn) {
    btnTe.classList.toggle('active', isTel);
    btnEn.classList.toggle('active', !isTel);
  }

  // Update Sidebar Language Toggle Buttons
  const sbLangTe = document.getElementById('sidebar-lang-te');
  const sbLangEn = document.getElementById('sidebar-lang-en');
  if (sbLangTe && sbLangEn) {
    sbLangTe.classList.toggle('active', isTel);
    sbLangEn.classList.toggle('active', !isTel);
  }

  // Update Sign In Page Language Toggle Buttons
  const signinTe = document.getElementById('signin-lang-te');
  const signinEn = document.getElementById('signin-lang-en');
  if (signinTe && signinEn) {
    signinTe.classList.toggle('active', isTel);
    signinEn.classList.toggle('active', !isTel);
  }

  const mobLang = document.getElementById('mobile-lang-label');
  if (mobLang) mobLang.innerText = isTel ? 'తెలుగు' : 'English';

  // 1. Translate every element with [data-i18n]
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (dict[key]) {
      el.innerText = dict[key];
    }
  });

  // 1.1 Update dropdown options (Crops and Districts)
  updateDropdownsLanguage(isTel);

  // 2. Hero Section Dynamic Texts
  const greetingEl = document.getElementById('hero-greeting');
  if (greetingEl) {
    greetingEl.innerText = dict.hero_greeting.replace('{name}', currentUser.name);
  }

  // 3. AI Assistant Welcome Text & Quick Chips
  const welcomeTextEl = document.getElementById('chat-welcome-text');
  if (welcomeTextEl) {
    welcomeTextEl.innerText = isTel
      ? 'నమస్కారం! నేను కృషిమిత్ర AI సహాయకుడిని (డెవలపర్లు: ఆకర్ష అర్చన & షైనీ - B.Tech AIML). మీ పంట తెగుళ్లు, ఎరువుల మోతాదు, వాతావరణం లేదా ప్రభుత్వ పథకాల గురించి ఏ ప్రశ్నైనా నన్ను అడగవచ్చు.'
      : 'Hello! I am KrishiMitra AI Assistant (Developed by: Aakarsha Archana & Shiney - B.Tech AIML). Ask me anything about crop diseases, fertilizers, weather, or government schemes.';
  }

  const assistantChipsContainer = document.getElementById('assistant-chips-container');
  if (assistantChipsContainer) {
    const quickChips = isTel ? [
      { text: '🌾 వరి అగ్గితెగులు నివారణ', query: 'వరి అగ్గితెగులు నివారణ ఏమిటి?' },
      { text: '🌶️ మిర్చి తామర పురుగులు', query: 'మిర్చి తామర పురుగుల నియంత్రణ మందులు?' },
      { text: '🧪 యూరియా, డీఏపీ మోతాదు', query: 'వరికి యూరియా, డీఏపీ ఎంత మోతాదులో వేయాలి?' },
      { text: '⛅ విజయవాడ వర్షం సూచన', query: 'ఈరోజు విజయవాడలో వర్షం పడుతుందా?' },
      { text: '🏛️ రైతు పథకాలు', query: 'పీఎం కిసాన్ / వైఎస్సార్ రైతు భరోసా స్టేటస్ ఎలా చూడాలి?' },
      { text: '🌿 జీవామృతం తయారీ', query: 'సేంద్రీయ జీవామృతం తయారీ విధానం చెప్పండి' }
    ] : [
      { text: '🌾 Rice Blast Control', query: 'How to control Rice Blast disease?' },
      { text: '🌶️ Chilli Black Thrips', query: 'Remedies for Chilli Black Thrips?' },
      { text: '🧪 Urea & DAP Dosage', query: 'How much Urea and DAP to apply for Paddy?' },
      { text: '⛅ Vijayawada Weather', query: 'Will it rain in Vijayawada today?' },
      { text: '🏛️ PM-Kisan & Schemes', query: 'How to check PM-Kisan and Rythu Bharosa status?' },
      { text: '🌿 Jeevamrutham Recipe', query: 'How to prepare organic Jeevamrutham?' }
    ];

    assistantChipsContainer.innerHTML = quickChips.map(c => `
      <button class="km-chip-btn" onclick="sendQuickQuery('${c.query}')">${c.text}</button>
    `).join('');
  }

  // 4. Form Placeholders
  const chatInput = document.getElementById('chat-input');
  if (chatInput) {
    chatInput.placeholder = isTel 
      ? 'మీ వ్యవసాయ సందేహాన్ని ఇక్కడ టైప్ చేయండి...' 
      : 'Ask any farming, fertilizer, or crop question...';
  }

  const postTitleInput = document.getElementById('post-title-input');
  if (postTitleInput) {
    postTitleInput.placeholder = isTel
      ? 'శీర్షిక (ఉదా: విజయవాడ మార్కెట్లో తేజా మిర్చి ధరలు ఎలా ఉన్నాయి?)...'
      : 'Title (e.g., How are Teja Chilli prices in Guntur mandi?)...';
  }

  const postBodyInput = document.getElementById('post-body-input');
  if (postBodyInput) {
    postBodyInput.placeholder = isTel
      ? 'మీ క్షేత్రస్థాయి అనుభవం లేదా ప్రశ్నను ఇక్కడ వివరంగా రాయండి...'
      : 'Share your field experience or ask a question in detail...';
  }

  const directChatInput = document.getElementById('direct-chat-input');
  if (directChatInput) {
    directChatInput.placeholder = isTel
      ? 'తోటి రైతుకు సందేశం పంపండి...'
      : 'Type a message to fellow farmer...';
  }

  // 5. Direct Farmer Chat Quick Inquiry Suggestions
  const directQuickPrompts = document.getElementById('direct-quick-prompts');
  if (directQuickPrompts) {
    const directPresets = isTel ? [
      { label: '💰 మార్కెట్ ధరలు', text: 'ఈరోజు మీ మార్కెట్ యార్డులో ధరలు ఎలా ఉన్నాయి?' },
      { label: '🌶️ తామర పురుగులు', text: 'నల్ల తామర పురుగుల నివారణకు ఏ మందు పిచికారీ చేయాలి?' },
      { label: '🧪 జిప్సం మోతాదు', text: 'ఎకరాకు జిప్సం ఎంత మోతాదులో వేయాలి?' },
      { label: '🌧️ వర్ష సూచన', text: 'మీ ప్రాంతంలో వర్షాలు మరియు కాలువల నీరు ఎలా ఉంది?' }
    ] : [
      { label: '💰 Market Rates', text: 'How are the crop market rates in your yard today?' },
      { label: '🌶️ Black Thrips', text: 'Which pesticide should be sprayed for Black Thrips?' },
      { label: '🧪 Gypsum Dose', text: 'What is the recommended Gypsum dose per acre?' },
      { label: '🌧️ Rain Outlook', text: 'How is the rain and canal water supply in your area?' }
    ];

    directQuickPrompts.innerHTML = directPresets.map(p => `
      <button class="km-chip-btn" style="font-size: 0.76rem; padding: 4px 10px;" onclick="sendDirectPreset('${p.text}')">${p.label}</button>
    `).join('');
  }

  // 6. Direct Chat Online Status & Typing Text
  const onlineLabel = document.getElementById('direct-chat-online-label');
  if (onlineLabel) onlineLabel.innerText = isTel ? 'ఆన్‌లైన్ (Online)' : 'Online';

  const typingText = document.getElementById('farmer-typing-text');
  if (typingText) typingText.innerText = isTel ? '✍️ రైతు సమాధానం టైప్ చేస్తున్నారు...' : '✍️ Fellow farmer is typing...';

  // 7. Update Active Direct Chat Meta
  if (typeof DIRECT_CONTACTS !== 'undefined') {
    const contact = DIRECT_CONTACTS.find(c => c.key === currentDirectContact) || DIRECT_CONTACTS[0];
    const metaEl = document.getElementById('direct-chat-contact-meta');
    if (metaEl) {
      metaEl.innerText = isTel ? `${contact.district} • ${contact.crop}` : `${contact.district} • Farmer`;
    }
  }

  // 8. Re-render Mandi Rates, Forum Posts & User Displays
  updateUserDisplay();
  if (typeof renderMandiRates === 'function' && typeof allMandiData !== 'undefined' && allMandiData.length) {
    renderMandiRates();
  }
  if (typeof renderCommunityPosts === 'function' && typeof allCommunityPosts !== 'undefined' && allCommunityPosts.length) {
    renderCommunityPosts();
  }
  if (typeof renderDirectContacts === 'function') {
    renderDirectContacts();
  }
}

function updateUserDisplay() {
  const un = document.getElementById('user-name');
  if (un) un.innerText = currentUser.name;

  const sbUserName = document.getElementById('sidebar-user-name');
  if (sbUserName) sbUserName.innerText = currentUser.name;

  const sbCropInfo = document.getElementById('sidebar-crop-info');
  if (sbCropInfo) {
    const cropText = (currentLang === 'te') 
      ? `${currentUser.cropTe || currentUser.crop} • ${currentUser.district.split(' ')[0]}` 
      : `${currentUser.crop} • ${currentUser.district.split(' ')[0]}`;
    sbCropInfo.innerText = cropText;
  }

  const sbName = document.getElementById('sidebar-name');
  if (sbName) sbName.innerText = currentUser.name;
  const sbSub = document.getElementById('sidebar-sub');
  if (sbSub) sbSub.innerText = `📍 ${currentUser.district.split(' ')[0]} • ${currentUser.acres} Ac`;

  // Profile Header Display
  const pName = document.getElementById('profile-name-display');
  if (pName) pName.innerText = currentUser.name;
  const pPhone = document.getElementById('profile-phone-display');
  if (pPhone) pPhone.innerText = currentUser.phone;
  const pDist = document.getElementById('profile-district-display');
  if (pDist) pDist.innerText = currentUser.district;
  const pCrop = document.getElementById('profile-crop-display');
  if (pCrop) pCrop.innerText = (currentLang === 'te') ? (currentUser.cropTe || currentUser.crop) : currentUser.crop;
  const pAcres = document.getElementById('profile-acres-display');
  if (pAcres) pAcres.innerText = `${currentUser.acres} ${(currentLang === 'te') ? 'ఎకరాలు' : 'Acres'}`;

  // Quick Agro-Metric Cards
  const pmAcres = document.getElementById('profile-metric-acres');
  if (pmAcres) pmAcres.innerText = `${currentUser.acres} ${(currentLang === 'te') ? 'ఎకరాలు' : 'Acres'}`;
  const pmCrop = document.getElementById('profile-metric-crop');
  if (pmCrop) pmCrop.innerText = (currentLang === 'te') ? (currentUser.cropTe || currentUser.crop) : currentUser.crop;
  const pmDist = document.getElementById('profile-metric-district');
  if (pmDist) pmDist.innerText = currentUser.district.split(' ')[0];
  const pmVill = document.getElementById('profile-metric-village');
  if (pmVill) pmVill.innerText = currentUser.village || (currentLang === 'te' ? 'ఏనికపాడు గ్రామం' : 'Enikepadu Village');

  // Detailed Farm Specs (View Mode)
  const pdName = document.getElementById('profile-detail-name');
  if (pdName) pdName.innerText = currentUser.name;
  const pdPhone = document.getElementById('profile-detail-phone');
  if (pdPhone) pdPhone.innerText = currentUser.phone;
  const pdDist = document.getElementById('profile-detail-district');
  if (pdDist) pdDist.innerText = currentUser.district;
  const pdVill = document.getElementById('profile-detail-village');
  if (pdVill) pdVill.innerText = currentUser.village || 'ఏనికపాడు (Enikepadu), విజయవాడ రూరల్';
  const pdCrop = document.getElementById('profile-detail-crop');
  if (pdCrop) pdCrop.innerText = (currentLang === 'te') ? (currentUser.cropTe || currentUser.crop) : currentUser.crop;
  const pdAcres = document.getElementById('profile-detail-acres');
  if (pdAcres) pdAcres.innerText = `${currentUser.acres} ${(currentLang === 'te') ? 'ఎకరాలు' : 'Acres'}`;

  // Hero displays
  const heroLoc = document.getElementById('hero-location');
  if (heroLoc) heroLoc.innerText = (currentLang === 'te') ? `${currentUser.district.split(' ')[0]} (కృష్ణా జిల్లా)` : currentUser.district;

  const heroCrop = document.getElementById('hero-crop');
  if (heroCrop) heroCrop.innerText = (currentLang === 'te') ? (currentUser.cropTe || currentUser.crop) : currentUser.crop;

  const heroAcres = document.getElementById('hero-acres');
  if (heroAcres) heroAcres.innerText = `${currentUser.acres} ${(currentLang === 'te') ? 'ఎకరాలు' : 'Acres'}`;
}

function toggleProfileEdit(show) {
  const viewMode = document.getElementById('profile-view-mode');
  const editMode = document.getElementById('profile-edit-mode');
  const btnToggle = document.getElementById('btn-toggle-edit-profile');

  const isEdit = (show !== undefined) ? show : (editMode.style.display === 'none' || !editMode.style.display);
  if (viewMode) viewMode.style.display = isEdit ? 'none' : 'block';
  if (editMode) editMode.style.display = isEdit ? 'block' : 'none';
  if (btnToggle) btnToggle.style.display = isEdit ? 'none' : 'flex';

  if (isEdit) {
    const editName = document.getElementById('edit-name');
    if (editName) editName.value = currentUser.name || '';
    const editPhone = document.getElementById('edit-phone');
    if (editPhone) editPhone.value = currentUser.phone || '';
    const editDist = document.getElementById('edit-district');
    if (editDist) editDist.value = currentUser.district || 'Vijayawada (Krishna)';
    const editVill = document.getElementById('edit-village');
    if (editVill) editVill.value = currentUser.village || 'ఏనికపాడు (Enikepadu), విజయవాడ రూరల్';
    const editCrop = document.getElementById('edit-crop');
    if (editCrop) editCrop.value = currentUser.crop || 'Paddy';
    const editAcres = document.getElementById('edit-acres');
    if (editAcres) editAcres.value = currentUser.acres || 3.5;
  }
}

async function saveProfileChanges() {
  const nameInput = document.getElementById('edit-name');
  const phoneInput = document.getElementById('edit-phone');
  const distInput = document.getElementById('edit-district');
  const villInput = document.getElementById('edit-village');
  const cropInput = document.getElementById('edit-crop');
  const acresInput = document.getElementById('edit-acres');

  const name = nameInput ? nameInput.value.trim() : '';
  const phone = phoneInput ? phoneInput.value.trim() : '';
  const district = distInput ? distInput.value : 'Vijayawada (Krishna)';
  const village = villInput ? villInput.value.trim() : 'ఏనికపాడు (Enikepadu)';
  const crop = cropInput ? cropInput.value : 'Paddy';
  const acres = acresInput ? parseFloat(acresInput.value) || 3.0 : 3.0;

  if (!name) return alert('దయచేసి రైతు పేరు నమోదు చేయండి. (Please enter farmer name)');
  if (!phone) return alert('దయచేసి మొబైల్ నంబర్ నమోదు చేయండి. (Please enter mobile number)');

  // Update in-memory state
  currentUser.name = name;
  currentUser.phone = phone;
  currentUser.district = district;
  currentUser.village = village;
  currentUser.crop = crop;
  currentUser.cropTe = (crop === 'Chilli') ? 'తేజా మిర్చి (Teja Chilli)' : (crop === 'Paddy' ? 'వరి (Paddy BPT 5204)' : crop);
  currentUser.acres = acres;

  // Refresh all components across app
  updateUserDisplay();
  applyLanguage();
  loadWeatherForDistrict(district);
  toggleProfileEdit(false);

  // Sync with backend API
  try {
    await fetch('/api/auth/profile/update', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, phone, district, village, crop, acres })
    });
  } catch (err) {
    console.warn('Profile sync note:', err);
  }

  alert(currentLang === 'te' 
    ? '✅ మీ ప్రొఫైల్ వివరాలు విజయవంతంగా భద్రపరచబడ్డాయి!' 
    : '✅ Profile details updated successfully!');
}

// ----------------- Auth & Dedicated Sign In Page -----------------
function signOutToLoginPage() {
  const appShell = document.getElementById('km-app-shell');
  if (appShell) appShell.style.display = 'none';
  const signinPage = document.getElementById('km-signin-page');
  if (signinPage) signinPage.classList.add('show');
  window.scrollTo({ top: 0, behavior: 'instant' });
}

function returnToDashboard() {
  const signinPage = document.getElementById('km-signin-page');
  if (signinPage) signinPage.classList.remove('show');
  const appShell = document.getElementById('km-app-shell');
  if (appShell) appShell.style.display = 'block';
  renderAllCanvasIcons();
  window.scrollTo({ top: 0, behavior: 'instant' });
}

// Backward compatibility alias
function openLoginPortal() {
  signOutToLoginPage();
}

function closeLoginPortal() {
  returnToDashboard();
}

function showAuthTab(type) {
  const isLogin = (type === 'login');
  document.getElementById('auth-panel-login').style.display = isLogin ? 'block' : 'none';
  document.getElementById('auth-panel-register').style.display = isLogin ? 'none' : 'block';

  document.getElementById('tab-btn-login').classList.toggle('active', isLogin);
  document.getElementById('tab-btn-register').classList.toggle('active', !isLogin);
}

const DEMO_PROFILES = {
  '9440123456': {
    name: 'Archana',
    phone: '9440123456',
    district: 'Vijayawada (Krishna)',
    village: 'ఏనికపాడు (Enikepadu), విజయవాడ రూరల్',
    crop: 'Paddy',
    cropTe: 'వరి (Paddy BPT 5204)',
    acres: 3.5,
    avatar: '👩‍🌾'
  },
  '9848054321': {
    name: 'Shiney',
    phone: '9848054321',
    district: 'Vijayawada (Krishna)',
    village: 'తాడిగడప (Tadigadapa), విజయవాడ రూరల్',
    crop: 'Chilli',
    cropTe: 'తేజా మిర్చి (Teja Chilli)',
    acres: 4.0,
    avatar: '👩‍🌾'
  }
};

async function loginDemo(phone) {
  // 1. Immediately apply the profile locally so user enters with 0ms latency
  if (DEMO_PROFILES[phone]) {
    applyLoggedInUser(DEMO_PROFILES[phone]);
  }

  // 2. Also sync with backend API
  try {
    const res = await fetch(`/api/auth/demo-login/${phone}`, { method: 'POST' });
    if (res.ok) {
      const data = await res.json();
      if (data.status === 'success' && data.user) {
        applyLoggedInUser(data.user);
      }
    }
  } catch (err) {
    console.warn('Demo login background sync note:', err);
  }
}

async function submitLogin() {
  const username = document.getElementById('login-username-input').value.trim();
  const password = document.getElementById('login-password-input').value;
  if (!username) return alert('దయచేసి మొబైల్ నంబర్ లేదా యూజర్‌నేమ్ నమోదు చేయండి.');

  try {
    const res = await fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    const data = await res.json();
    if (res.ok && data.status === 'success') {
      applyLoggedInUser(data.user);
    } else {
      alert(data.detail || 'లాగిన్ విఫలమైంది. దయచేసి వివరాలను సరిచూసుకోండి.');
    }
  } catch (err) {
    alert('సర్వర్ కనెక్షన్ లోపం.');
  }
}

async function submitRegister() {
  const name = document.getElementById('reg-name').value.trim();
  const phone = document.getElementById('reg-phone').value.trim();
  const district = document.getElementById('reg-district').value;
  const crop = document.getElementById('reg-crop').value;
  const acres = parseFloat(document.getElementById('reg-acres').value) || 2.0;
  const password = document.getElementById('reg-password').value;

  if (!name || phone.length !== 10 || password.length < 6) {
    return alert('దయచేసి అన్ని వివరాలు సరిగ్గా పూరించండి (ఫోన్ 10 అంకెలు, పాస్‌వర్డ్ కనీసం 6 అక్షరాలు).');
  }

  try {
    const res = await fetch('/api/auth/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, phone, district, crop, acres, password })
    });
    const data = await res.json();
    if (res.ok && data.status === 'success') {
      alert('నమోదు విజయవంతమైంది! మీ ఖాతాలోకి ప్రవేశిస్తున్నారు...');
      applyLoggedInUser(data.user);
    } else {
      alert(data.detail || 'నమోదు విఫలమైంది.');
    }
  } catch (err) {
    alert('సర్వర్ కనెక్షన్ లోపం.');
  }
}

function applyLoggedInUser(user) {
  currentUser = {
    name: user.name || 'Farmer',
    phone: user.username || user.phone || '9440123456',
    district: user.district || 'Vijayawada (Krishna)',
    village: user.village || 'ఏనికపాడు (Enikepadu), విజయవాడ రూరల్',
    crop: user.crop || 'Paddy',
    cropTe: (user.crop === 'Chilli') ? 'తేజా మిర్చి (Teja Chilli)' : 'వరి (Paddy BPT 5204)',
    acres: user.acres || 3.0,
    avatar: '👩‍🌾'
  };

  updateUserDisplay();
  applyLanguage();
  loadWeatherForDistrict(currentUser.district);
  returnToDashboard();
  showTab('home');
}

// User Switching from Profile Page
function switchUser(userKey) {
  if (userKey === 'archana') {
    loginDemo('9440123456');
  } else {
    loginDemo('9848054321');
  }
}

// Sidebar Dropdown Handlers
function onLocationChange(loc) {
  loadWeatherForDistrict(loc);
}

function onCropChange(crp) {
  currentUser.crop = crp;
  currentUser.cropTe = crp;
  updateUserDisplay();
}

// ----------------- Mandi Rates Fetcher with Top Crops & Show More -----------------
let allMandiData = [];
let isMandiExpanded = false;

async function loadMandiRates() {
  try {
    const res = await fetch('/api/mandi-rates');
    allMandiData = await res.json();
    renderMandiRates();
  } catch (err) {
    console.error('Error loading Mandi rates:', err);
  }
}

function renderMandiRates() {
  const container = document.getElementById('mandi-rates-grid');
  if (!container || !allMandiData.length) return;

  const isTel = (currentLang === 'te');
  const itemsToShow = isMandiExpanded 
    ? allMandiData 
    : allMandiData.filter(item => item.is_top !== false);

  container.innerHTML = itemsToShow.map(item => {
    const cropName = isTel ? (item.crop_te || item.crop) : (item.crop_en || item.crop);
    let priceVal = isTel ? (item.price_te || item.price) : (item.price_en || item.price);
    if (!isTel && priceVal) {
      priceVal = priceVal
        .replace('క్వింటాల్', 'Quintal')
        .replace('టన్ను', 'Ton')
        .replace('క్రేట్', 'Crate')
        .replace('గెల', 'Bunch');
    }
    const mandiName = isTel ? (item.mandi_te || item.mandi) : (item.mandi_en || item.mandi);
    let trendVal = isTel ? (item.trend_te || item.trend) : (item.trend_en || item.trend);
    if (!isTel && trendVal === 'స్థిరం') trendVal = 'Stable';
    const badgeText = isTel ? (item.badge_te || item.badge) : (item.badge_en || item.badge);

    let trendColor = '#94a3b8';
    if (trendVal && trendVal.startsWith('+')) trendColor = '#34d399';
    else if (trendVal && trendVal.startsWith('-')) trendColor = '#f87171';
    else if (trendVal === 'స్థిరం' || trendVal === 'Stable') trendColor = '#60a5fa';

    return `
      <div class="km-glass" style="padding: 16px 20px; display: flex; flex-direction: column; justify-content: space-between; border-radius: 16px; transition: transform 0.2s ease, border-color 0.2s ease;">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 8px; gap: 8px;">
          <div style="font-weight: 700; font-size: 1.05rem; color: #ffffff;">${cropName}</div>
          <span class="km-chip" style="font-size: 0.75rem; padding: 3px 8px; background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(52, 211, 153, 0.35); color: #6ee7b7; white-space: nowrap;">${badgeText}</span>
        </div>
        <div style="font-size: 1.55rem; font-weight: 800; color: #fbbf24; margin-bottom: 6px;">${priceVal}</div>
        <div style="font-size: 0.82rem; color: #cbd5e1; display: flex; justify-content: space-between; align-items: center; margin-top: 6px;">
          <span>📍 ${mandiName}</span>
          <span style="color: ${trendColor}; font-weight: 700; background: rgba(0, 0, 0, 0.25); padding: 2px 7px; border-radius: 6px;">${trendVal}</span>
        </div>
      </div>
    `;
  }).join('');

  // Update Toggle Button & Badge text
  const btnText = document.getElementById('mandi-btn-text');
  const btnIcon = document.getElementById('mandi-btn-icon');
  const countLabel = document.getElementById('mandi-count-label');

  if (btnText) {
    if (isMandiExpanded) {
      btnText.innerText = (currentLang === 'te') 
        ? '⬆️ తక్కువ చూపించు (Show Top Crops Only)' 
        : '⬆️ Show Top Crops Only';
    } else {
      btnText.innerText = (currentLang === 'te') 
        ? `🔽 మరిన్ని పంటల ధరలు చూడండి (Show All ${allMandiData.length} Crops)` 
        : `🔽 Show All Crop Prices (${allMandiData.length} Crops)`;
    }
  }

  if (btnIcon) {
    btnIcon.innerHTML = isMandiExpanded 
      ? '<polyline points="18 15 12 9 6 15"></polyline>' 
      : '<polyline points="6 9 12 15 18 9"></polyline>';
  }

  if (countLabel) {
    countLabel.innerText = isMandiExpanded
      ? (currentLang === 'te' ? `అన్ని పంటలు (${allMandiData.length} Crops)` : `All ${allMandiData.length} Crops`)
      : (currentLang === 'te' ? `ప్రధాన పంటలు (Top ${itemsToShow.length} Crops)` : `Top ${itemsToShow.length} Crops`);
  }
}

function toggleMandiRates() {
  isMandiExpanded = !isMandiExpanded;
  renderMandiRates();
}

// ----------------- Weather Fetcher -----------------
async function loadWeatherForDistrict(district) {
  try {
    const res = await fetch(`/api/weather?location=${encodeURIComponent(district)}`);
    const data = await res.json();

    if (data.status === 'success') {
      const cur = data.current;
      document.getElementById('metric-temp').innerText = `${cur.temperature}°C`;
      document.getElementById('metric-feels').innerText = (currentLang === 'te') ? `అనిపిస్తున్నది: ${cur.apparent_temperature}°C` : `Feels like: ${cur.apparent_temperature}°C`;
      document.getElementById('metric-humidity').innerText = `${cur.humidity}%`;
      document.getElementById('metric-wind').innerText = `${cur.wind_speed} km/h`;
      document.getElementById('metric-rain').innerText = `${cur.precipitation_probability}%`;

      const homeTemp = document.getElementById('home-weather-temp');
      if (homeTemp) homeTemp.innerText = `${cur.temperature}°C`;
      const homeCond = document.getElementById('home-weather-cond');
      if (homeCond) homeCond.innerText = `${cur.condition} • ${(currentLang === 'te') ? 'తేమ' : 'Humidity'}: ${cur.humidity}%`;

      const sprayEl = document.getElementById('spray-advisory-text');
      const rainRisk = cur.precipitation_probability > 40;
      const windRisk = cur.wind_speed > 20;

      if (!rainRisk && !windRisk) {
        sprayEl.innerHTML = (currentLang === 'te')
          ? `ప్రస్తుత ${district} వాతావరణం మందుల పిచికారీకి <strong style="color:#6ee7b7;">చాలా అనుకూలంగా ఉంది</strong>. గాలి వేగం ${cur.wind_speed} km/h లోపే ఉంది, వర్షం ముప్పు లేదు (${cur.precipitation_probability}%).`
          : `Current weather in ${district} is <strong style="color:#6ee7b7;">highly optimal for spraying</strong>. Wind speed is gentle (${cur.wind_speed} km/h) and rain risk is low (${cur.precipitation_probability}%).`;
      } else {
        sprayEl.innerHTML = (currentLang === 'te')
          ? `ప్రస్తుత ${district} వాతావరణం పిచికారీకి <strong style="color:#f87171;">అనుకూలం కాదు</strong>. ${rainRisk ? 'వర్షం పడే అవకాశం ఉంది.' : ''} ${windRisk ? 'గాలి వేగం ఎక్కువగా ఉంది.' : ''}`
          : `Current weather in ${district} is <strong style="color:#f87171;">not recommended for spraying</strong>. ${rainRisk ? 'Rain expected.' : ''} ${windRisk ? 'High wind speed.' : ''}`;
      }

      const forecastGrid = document.getElementById('weather-forecast-grid');
      if (forecastGrid && data.forecast_daily && data.forecast_daily.length > 0) {
        forecastGrid.innerHTML = data.forecast_daily.slice(0, 5).map(day => `
          <div class="km-glass" style="padding: 14px; text-align: center;">
            <div style="font-size: 0.82rem; font-weight: 700; color: #94a3b8;">${day.date.split('-').slice(1).join('/')}</div>
            <div style="font-size: 1.8rem; margin: 4px 0;">⛅</div>
            <div style="font-weight: 800; font-size: 1.1rem; color: #ffffff;">${day.temp_max}°</div>
            <div style="font-size: 0.8rem; color: #94a3b8;">${day.temp_min}°C</div>
            <div style="font-size: 0.75rem; color: #6ee7b7; margin-top: 4px;">🌧️ ${day.precipitation_sum} mm</div>
          </div>
        `).join('');
      }
    }
  } catch (err) {
    console.error('Weather load error:', err);
  }
}

// ----------------- Disease Scanner -----------------
function handleLeafSelect(event) {
  const file = event.target.files[0];
  if (!file) return;
  selectedLeafFile = file;

  const reader = new FileReader();
  reader.onload = function(e) {
    document.getElementById('leaf-preview-img').src = e.target.result;
    document.getElementById('scanner-preview-box').style.display = 'block';
    document.getElementById('scanner-empty-state').style.display = 'none';
    document.getElementById('scanner-result-content').style.display = 'none';
  };
  reader.readAsDataURL(file);
}

async function analyzeLeafImage() {
  if (!selectedLeafFile) return;

  const loadingEl = document.getElementById('scanner-loading');
  const emptyEl = document.getElementById('scanner-empty-state');
  const resultEl = document.getElementById('scanner-result-content');

  emptyEl.style.display = 'none';
  resultEl.style.display = 'none';
  loadingEl.style.display = 'block';

  try {
    const formData = new FormData();
    formData.append('file', selectedLeafFile);
    formData.append('language', (currentLang === 'te') ? 'Telugu' : 'English');

    const res = await fetch('/api/predict-disease', {
      method: 'POST',
      body: formData
    });
    const data = await res.json();
    loadingEl.style.display = 'none';

    if (data.status === 'success') {
      const isTel = (currentLang === 'te');
      resultEl.innerHTML = `
        <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid var(--km-border); border-radius: 12px; padding: 16px; margin-bottom: 14px;">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <span class="km-chip" style="font-size: 0.8rem;">${isTel ? 'పంట' : 'Crop'}: ${data.crop}</span>
            <span style="font-size: 0.9rem; font-weight: 700; color: #6ee7b7;">${isTel ? 'ఖచ్చితత్వం' : 'Confidence'}: ${(data.confidence * 100).toFixed(1)}%</span>
          </div>
          <div style="font-size: 1.4rem; font-weight: 800; color: #ffffff; margin-top: 8px;">
            ${data.disease_name}
          </div>
        </div>

        <div style="margin-bottom: 14px;">
          <div style="font-weight: 700; color: #34d399; font-size: 1.02rem; margin-bottom: 6px;">🌿 ${isTel ? 'సేంద్రీయ నివారణ (Organic Remedy)' : 'Organic & Biological Remedy'}:</div>
          <p style="font-size: 0.92rem; color: #e2e8f0; line-height: 1.5;">${data.organic_remedies}</p>
        </div>

        <div style="margin-bottom: 14px;">
          <div style="font-weight: 700; color: #fbbf24; font-size: 1.02rem; margin-bottom: 6px;">🧪 ${isTel ? 'రసాయన మందుల యాజమాన్యం (Chemical Control)' : 'Approved Chemical Fungicide'}:</div>
          <p style="font-size: 0.92rem; color: #e2e8f0; line-height: 1.5;">${data.chemical_treatments}</p>
        </div>

        <div>
          <div style="font-weight: 700; color: #60a5fa; font-size: 1.02rem; margin-bottom: 6px;">🛡️ ${isTel ? 'ముందుజాగ్రత్త చర్యలు (Prevention)' : 'Cultural Hygiene & Prevention'}:</div>
          <p style="font-size: 0.92rem; color: #e2e8f0; line-height: 1.5;">${data.prevention}</p>
        </div>
      `;
      resultEl.style.display = 'block';
    }
  } catch (err) {
    loadingEl.style.display = 'none';
    resultEl.innerHTML = `<div style="color: #f87171;">లోపం జరిగింది: దయచేసి మళ్లీ ప్రయత్నించండి.</div>`;
    resultEl.style.display = 'block';
  }
}

// ----------------- Soil & Fertilizer Assessment -----------------
async function calculateSoilFertilizers() {
  const crop = document.getElementById('soil-crop-select').value;
  const ph = parseFloat(document.getElementById('input-ph').value);
  const n = parseFloat(document.getElementById('input-n').value);
  const p = parseFloat(document.getElementById('input-p').value);
  const k = parseFloat(document.getElementById('input-k').value);

  try {
    const res = await fetch('/api/soil-analysis', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        crop: crop,
        ph: ph,
        nitrogen: n,
        phosphorus: p,
        potassium: k,
        language: (currentLang === 'te') ? 'Telugu' : 'English'
      })
    });
    const data = await res.json();
    const resultBox = document.getElementById('soil-fert-result');
    const isTel = (currentLang === 'te');

    resultBox.innerHTML = `
      <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid var(--km-border); border-radius: 12px; padding: 16px; margin-bottom: 14px;">
        <div style="font-weight: 800; color: #6ee7b7; font-size: 1.15rem;">
          🌾 ${crop} - ${isTel ? 'ఎకరాకు సిఫార్సు చేసిన ఎరువుల బస్తాల మోతాదు:' : 'Recommended Fertilizer Bags Per Acre:'}
        </div>
        <ul style="margin: 10px 0 0 20px; line-height: 1.8; font-size: 0.95rem; color: #f1f5f9;">
          <li><strong>${isTel ? 'యూరియా' : 'Urea'}:</strong> ${data.fertilizer_bags.urea_bags} ${isTel ? 'బస్తాలు' : 'bags'}</li>
          <li><strong>${isTel ? 'డీఏపీ' : 'DAP'}:</strong> ${data.fertilizer_bags.dap_bags} ${isTel ? 'బస్తాలు' : 'bags'}</li>
          <li><strong>${isTel ? 'ఎంఓపీ' : 'MOP'}:</strong> ${data.fertilizer_bags.mop_bags} ${isTel ? 'బస్తాలు' : 'bags'}</li>
        </ul>
      </div>

      <div style="font-size: 1.05rem; font-weight: 700; color: #fbbf24; margin-bottom: 8px;">
        ⏱️ ${isTel ? 'విడతల వారీ షెడ్యూల్ (Split Application Schedule):' : 'Stage-wise Application Schedule:'}
      </div>
      <div style="display: flex; flex-direction: column; gap: 8px; font-size: 0.9rem;">
        <div style="background: rgba(0,0,0,0.25); padding: 10px 14px; border-radius: 8px;">
          <strong>1. ${isTel ? 'ఆఖరి దుక్కిలో (Basal Dose)' : 'Basal Dose'}:</strong> ${data.split_schedule.basal}
        </div>
        <div style="background: rgba(0,0,0,0.25); padding: 10px 14px; border-radius: 8px;">
          <strong>2. ${isTel ? 'దుబ్బు చేసే దశ (Tillering)' : 'Tillering Stage'}:</strong> ${data.split_schedule.tillering}
        </div>
        <div style="background: rgba(0,0,0,0.25); padding: 10px 14px; border-radius: 8px;">
          <strong>3. ${isTel ? 'చిరుపొట్ట దశ (Panicle Initiation)' : 'Panicle Initiation'}:</strong> ${data.split_schedule.panicle}
        </div>
      </div>
    `;
  } catch (err) {
    console.error('Soil calc error:', err);
  }
}

// ----------------- ML Crop Recommendation -----------------
async function runCropRecommendation() {
  const n = parseFloat(document.getElementById('rec-n').value);
  const p = parseFloat(document.getElementById('rec-p').value);
  const k = parseFloat(document.getElementById('rec-k').value);
  const ph = parseFloat(document.getElementById('rec-ph').value);
  const temp = parseFloat(document.getElementById('rec-temp').value);
  const hum = parseFloat(document.getElementById('rec-hum').value);
  const rain = parseFloat(document.getElementById('rec-rain').value);

  const emptyEl = document.getElementById('rec-empty-state');
  const outputEl = document.getElementById('rec-output-content');
  const isTel = (currentLang === 'te');

  try {
    const res = await fetch('/api/recommend-crop', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ n, p, k, ph, temperature: temp, humidity: hum, rainfall: rain })
    });
    const data = await res.json();
    emptyEl.style.display = 'none';

    outputEl.innerHTML = `
      <div style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.25) 0%, rgba(5, 150, 105, 0.35) 100%); border: 1px solid #34d399; border-radius: 14px; padding: 20px; text-align: center; margin-bottom: 16px;">
        <div style="font-size: 0.85rem; color: #a7f3d0; font-weight: 700; text-transform: uppercase;">${isTel ? 'అత్యంత అనువైన పంట' : 'Top Recommended Crop'}</div>
        <div style="font-size: 2.2rem; font-weight: 800; color: #ffffff; margin: 6px 0;">${data.top_crop || data.recommended_crop}</div>
        <div style="font-size: 0.95rem; color: #fbbf24; font-weight: 700;">${isTel ? 'అనుకూలత స్కోర్' : 'Confidence Match'}: ${(data.confidence * 100).toFixed(0)}%</div>
      </div>

      <div style="font-size: 0.95rem; font-weight: 700; color: #cbd5e1; margin-bottom: 10px;">${isTel ? 'టాప్ ప్రత్యామ్నాయ పంటలు:' : 'Alternative Crop Candidates:'}</div>
      <div style="display: flex; flex-direction: column; gap: 8px;">
        ${(data.top_candidates || data.candidates || []).map(c => `
          <div style="background: rgba(0,0,0,0.25); border-radius: 8px; padding: 10px 14px; display: flex; justify-content: space-between; align-items: center;">
            <span style="font-weight: 700; color: #ffffff;">${c.crop}</span>
            <span style="color: #6ee7b7; font-weight: 700;">${(c.probability * 100).toFixed(0)}%</span>
          </div>
        `).join('')}
      </div>
    `;
    outputEl.style.display = 'block';
  } catch (err) {
    console.error('Crop rec error:', err);
  }
}

// ----------------- AI Chatbot -----------------
let isChatSending = false;

function formatMarkdown(text) {
  if (!text) return '';
  return text
    .replace(/^### (.*$)/gim, '<h4>$1</h4>')
    .replace(/^#### (.*$)/gim, '<h5>$1</h5>')
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\*(.*?)\*/g, '<em>$1</em>')
    .replace(/`([^`]+)`/g, '<code style="background:rgba(0,0,0,0.35); color:#fbbf24; padding:2px 6px; border-radius:4px; font-family:monospace;">$1</code>')
    .replace(/^---$/gim, '<hr style="border:none; border-top:1px solid rgba(52,211,153,0.25); margin:10px 0;">')
    .replace(/^- (.*$)/gim, '<li style="margin-left: 18px; margin-bottom: 4px;">$1</li>')
    .replace(/^\d+\. (.*$)/gim, '<li style="margin-left: 18px; margin-bottom: 4px;">$1</li>')
    .replace(/\n\n/g, '<br><br>')
    .replace(/\n/g, '<br>');
}

function sendQuickQuery(query) {
  if (isChatSending) return;
  const inputEl = document.getElementById('chat-input');
  if (inputEl) inputEl.value = query;
  handleChatSend();
}

async function handleChatSend() {
  if (isChatSending) return;
  const inputEl = document.getElementById('chat-input');
  const query = inputEl.value.trim();
  if (!query) return;

  isChatSending = true;
  const container = document.getElementById('chat-messages-container');
  const isTel = (currentLang === 'te');

  // Append user bubble
  const userBubble = document.createElement('div');
  userBubble.className = 'km-chat-bubble km-bubble-user';
  userBubble.innerText = query;
  container.appendChild(userBubble);
  inputEl.value = '';

  // Append thinking bubble
  const botBubble = document.createElement('div');
  botBubble.className = 'km-chat-bubble km-bubble-bot';
  botBubble.innerHTML = isTel 
    ? '<span style="display:inline-flex; align-items:center; gap:8px;">⏳ <em>సమాధానం సిద్ధం చేస్తోంది...</em></span>' 
    : '<span style="display:inline-flex; align-items:center; gap:8px;">⏳ <em>Analyzing agricultural query...</em></span>';
  container.appendChild(botBubble);
  container.scrollTop = container.scrollHeight;

  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        query: query,
        crop: currentUser.crop,
        language: (currentLang === 'te') ? 'Telugu' : 'English'
      })
    });
    
    if (!res.ok) {
      throw new Error(`Server returned HTTP ${res.status}`);
    }
    
    const data = await res.json();
    const formatted = formatMarkdown(data.answer);
    botBubble.innerHTML = `<div style="font-weight:700; color:#34d399; margin-bottom:6px;">🌾 KrishiMitra AI:</div>${formatted}`;
    container.scrollTop = container.scrollHeight;
  } catch (err) {
    console.error('Chat error:', err);
    botBubble.innerHTML = isTel 
      ? '<span style="color:#f87171;">⚠️ క్షమించండి, సర్వర్ కనెక్షన్ సమస్య ఎదురైంది. దయచేసి మరోసారి ప్రయత్నించండి.</span>' 
      : '<span style="color:#f87171;">⚠️ Error contacting server. Please try again in a moment.</span>';
  } finally {
    isChatSending = false;
  }
}

// ----------------- Community Discussions & Forum -----------------
let allCommunityPosts = [];
let currentForumFilter = 'all';

async function loadCommunityPosts() {
  try {
    const res = await fetch('/api/community/posts');
    allCommunityPosts = await res.json();
    renderCommunityPosts();
  } catch (err) {
    console.error('Community posts error:', err);
  }
}

function filterForumPosts(category, btnEl) {
  currentForumFilter = category;
  document.querySelectorAll('#forum-filter-chips .km-chip-btn').forEach(btn => {
    btn.classList.remove('active');
  });
  if (btnEl) btnEl.classList.add('active');
  renderCommunityPosts();
}

function renderCommunityPosts() {
  const container = document.getElementById('community-posts-feed');
  if (!container) return;

  const filtered = (currentForumFilter === 'all')
    ? allCommunityPosts
    : allCommunityPosts.filter(p => (p.tag === currentForumFilter || p.title.includes(currentForumFilter)));

  if (!filtered.length) {
    container.innerHTML = `
      <div class="km-glass" style="padding: 24px; text-align: center; color: #94a3b8; border-radius: 14px;">
        <div style="font-size: 2rem; margin-bottom: 6px;">🌾</div>
        <div>${(currentLang === 'te') ? 'ఈ విభాగంలో ఇంకా పోస్టులు లేవు. మొదటి ప్రశ్న లేదా సమాచారాన్ని పోస్ట్ చేయండి!' : 'No posts yet in this category. Be the first to share an inquiry or tip!'}</div>
      </div>
    `;
    return;
  }

  const tagMap = {
    'తెగుళ్ల నివారణ': '🛡️ Pest Control',
    'మార్కెట్ ధరలు': '💰 Market Rates',
    'ఎరువుల యాజమాన్యం': '🧪 Fertilizers',
    'విత్తనాలు & మార్కెట్': '🌱 Seeds & Varieties',
    'సాధారణ చర్చ': '🌾 General Discussion'
  };

  container.innerHTML = filtered.map((post) => {
    const isTel = (currentLang === 'te');
    let dateStr = post.date || post.timestamp || (isTel ? 'ఈరోజు' : 'Today');
    if (!isTel) {
      dateStr = dateStr
        .replace('నిన్న', 'Yesterday')
        .replace('ఈరోజు', 'Today')
        .replace('రోజులు క్రితం', 'days ago')
        .replace('గంటల క్రితం', 'hours ago');
    }
    const tag = post.tag || 'సాధారణ చర్చ';
    const displayTag = isTel ? tag : (tagMap[tag] || tag);
    const likesCount = post.likes || 0;
    const isLiked = post.liked || false;
    const replies = post.replies || [];

    return `
      <div class="km-glass" style="padding: 18px 20px; border-radius: 16px; border: 1px solid var(--km-border); transition: transform 0.2s ease;">
        <!-- Header: Author, Location, Date, Tag -->
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px; gap: 10px; flex-wrap: wrap;">
          <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 36px; height: 36px; border-radius: 50%; background: rgba(16, 185, 129, 0.2); border: 1.5px solid #34d399; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; color: #34d399;">
              👨‍🌾
            </div>
            <div>
              <div style="font-weight: 800; color: #ffffff; font-size: 0.98rem; line-height: 1.2;">
                ${post.author}
                <span style="font-size: 0.75rem; color: #6ee7b7; font-weight: 600; margin-left: 6px;">
                  📍 ${post.district} • ${post.crop}
                </span>
              </div>
              <div style="font-size: 0.74rem; color: #94a3b8; margin-top: 2px;">
                🕒 ${dateStr}
              </div>
            </div>
          </div>
          <span class="km-chip" style="font-size: 0.74rem; padding: 3px 10px; background: rgba(16, 185, 129, 0.15); border: 1px solid rgba(52, 211, 153, 0.35); color: #a7f3d0; white-space: nowrap;">
            ${displayTag}
          </span>
        </div>

        <!-- Post Title & Content -->
        <div style="font-weight: 800; font-size: 1.08rem; color: #ffffff; margin-bottom: 8px; line-height: 1.4;">
          ${post.title}
        </div>
        <div style="font-size: 0.92rem; color: #e2e8f0; line-height: 1.55; margin-bottom: 14px; white-space: pre-line;">
          ${post.message}
        </div>

        <!-- Action Bar: Like & Reply Toggle -->
        <div style="display: flex; gap: 12px; align-items: center; border-top: 1px solid rgba(52, 211, 153, 0.15); padding-top: 10px;">
          <button class="km-chip-btn ${isLiked ? 'active' : ''}" 
                  onclick="likeCommunityPost(${post.id})" 
                  style="padding: 5px 14px; font-weight: 700; display: inline-flex; align-items: center; gap: 6px;">
            <span>${isLiked ? '❤️' : '👍'}</span>
            <span>${likesCount} ${isTel ? 'లైకులు' : 'Likes'}</span>
          </button>

          <button class="km-chip-btn" 
                  onclick="togglePostReplies(${post.id})" 
                  style="padding: 5px 14px; font-weight: 700; display: inline-flex; align-items: center; gap: 6px;">
            <span>💬</span>
            <span>${replies.length} ${isTel ? 'సమాధానాలు' : 'Replies'}</span>
          </button>
        </div>

        <!-- Collapsible Replies Thread -->
        <div id="replies-container-${post.id}" style="display: none; margin-top: 12px; border-top: 1px dashed rgba(52, 211, 153, 0.2); padding-top: 12px;">
          <!-- Existing Replies -->
          <div id="replies-list-${post.id}" style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 10px;">
            ${replies.map(r => `
              <div style="background: rgba(4, 24, 16, 0.7); border: 1px solid rgba(52, 211, 153, 0.15); border-radius: 10px; padding: 8px 12px; font-size: 0.88rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 3px;">
                  <strong style="color: #6ee7b7; font-size: 0.8rem;">👨‍🌾 ${r.author} (${r.district || 'AP'})</strong>
                  <span style="color: #94a3b8; font-size: 0.72rem;">${r.time || ''}</span>
                </div>
                <div style="color: #cbd5e1; line-height: 1.4;">${r.text}</div>
              </div>
            `).join('')}
          </div>

          <!-- Add Reply Box -->
          <div style="display: flex; gap: 8px;">
            <input type="text" id="reply-input-${post.id}" class="km-input" 
                   placeholder="${isTel ? 'తోటి రైతుకు సమాధానం రాయండి...' : 'Write a helpful reply...'}" 
                   style="font-size: 0.85rem; padding: 8px 12px;"
                   onkeypress="if(event.key === 'Enter') submitCommunityReply(${post.id})">
            <button class="km-btn" onclick="submitCommunityReply(${post.id})" style="padding: 8px 14px; font-size: 0.85rem; flex-shrink: 0;">
              ${isTel ? 'పంపు' : 'Reply'}
            </button>
          </div>
        </div>
      </div>
    `;
  }).join('');
}

async function likeCommunityPost(postId) {
  try {
    const res = await fetch('/api/community/like-post', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ post_id: postId })
    });
    const data = await res.json();
    if (data.status === 'success' && data.post) {
      const idx = allCommunityPosts.findIndex(p => p.id === postId);
      if (idx !== -1) {
        allCommunityPosts[idx].likes = data.post.likes;
        allCommunityPosts[idx].liked = data.post.liked;
        renderCommunityPosts();
      }
    }
  } catch (err) {
    console.error('Like error:', err);
  }
}

function togglePostReplies(postId) {
  const container = document.getElementById(`replies-container-${postId}`);
  if (container) {
    container.style.display = (container.style.display === 'none' || !container.style.display) ? 'block' : 'none';
  }
}

async function submitCommunityReply(postId) {
  const inputEl = document.getElementById(`reply-input-${postId}`);
  const text = inputEl ? inputEl.value.trim() : '';
  if (!text) return;

  try {
    const res = await fetch('/api/community/reply-post', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        post_id: postId,
        author: currentUser.name || 'Archana',
        district: (currentUser.district || 'Vijayawada').split(' ')[0],
        text: text
      })
    });
    const data = await res.json();
    if (data.status === 'success' && data.post) {
      const idx = allCommunityPosts.findIndex(p => p.id === postId);
      if (idx !== -1) {
        allCommunityPosts[idx].replies = data.post.replies;
        renderCommunityPosts();
        // Keep replies open
        const container = document.getElementById(`replies-container-${postId}`);
        if (container) container.style.display = 'block';
      }
    }
  } catch (err) {
    console.error('Reply submit error:', err);
  }
}

async function submitCommunityPost() {
  const titleInput = document.getElementById('post-title-input');
  const bodyInput = document.getElementById('post-body-input');
  const tagSelect = document.getElementById('post-category-select');

  const title = titleInput ? titleInput.value.trim() : '';
  const body = bodyInput ? bodyInput.value.trim() : '';
  const tag = tagSelect ? tagSelect.value : 'సాధారణ చర్చ';

  if (!title || !body) {
    alert(currentLang === 'te' 
      ? 'దయచేసి శీర్షిక మరియు సందేశాన్ని రెండింటినీ నమోదు చేయండి.' 
      : 'Please enter both title and message.');
    return;
  }

  try {
    const res = await fetch('/api/community/posts', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        author: currentUser.name || 'Archana',
        district: (currentUser.district || 'Vijayawada').split(' ')[0],
        crop: currentUser.crop || 'Paddy',
        tag: tag,
        title: title,
        message: body
      })
    });
    
    if (res.ok) {
      if (titleInput) titleInput.value = '';
      if (bodyInput) bodyInput.value = '';
      await loadCommunityPosts();
    }
  } catch (err) {
    console.error('Submit post error:', err);
  }
}

// ----------------- 1-on-1 Direct Farmer Chat (Andhra Peers) -----------------
const DIRECT_CONTACTS = [
  { 
    key: 'Shiney (Guntur • Chilli)', 
    name: 'Shiney', 
    district: 'గుంటూరు', 
    district_en: 'Guntur', 
    crop: 'తేజా మిర్చి రైతు', 
    crop_en: 'Teja Chilli Farmer', 
    avatar: '👩‍🌾' 
  },
  { 
    key: 'Venkat Reddy (Kurnool • Groundnut)', 
    name: 'Venkat Reddy', 
    district: 'కర్నూలు', 
    district_en: 'Kurnool', 
    crop: 'వేరుశనగ K-6 రైతు', 
    crop_en: 'Groundnut K-6 Farmer', 
    avatar: '🧔' 
  },
  { 
    key: 'Apparao (Godavari • Paddy)', 
    name: 'Apparao', 
    district: 'తూర్పు గోదావరి', 
    district_en: 'East Godavari', 
    crop: 'వరి BPT 5204 రైతు', 
    crop_en: 'Paddy BPT 5204 Farmer', 
    avatar: '🌾' 
  },
  { 
    key: 'Srinivasulu (Anantapur • Horticulture)', 
    name: 'Srinivasulu', 
    district: 'అనంతపురం', 
    district_en: 'Anantapur', 
    crop: 'బత్తాయి తోటల రైతు', 
    crop_en: 'Sweet Orange / Orchard Farmer', 
    avatar: '🍊' 
  }
];

currentDirectContact = DIRECT_CONTACTS[0].key;

function renderDirectContacts() {
  const container = document.getElementById('direct-chat-contacts');
  if (!container) return;

  const isTel = (currentLang === 'te');
  container.innerHTML = DIRECT_CONTACTS.map(c => `
    <button class="km-chip-btn ${c.key === currentDirectContact ? 'active' : ''}" 
            onclick="switchDirectContact('${c.key}')" 
            style="display: flex; align-items: center; gap: 6px; padding: 6px 14px; font-weight: 700;">
      <span>${c.avatar}</span>
      <span>${c.name} (${isTel ? c.district : c.district_en})</span>
    </button>
  `).join('');
}

function switchDirectContact(contactKey) {
  currentDirectContact = contactKey;
  const contact = DIRECT_CONTACTS.find(c => c.key === contactKey) || DIRECT_CONTACTS[0];
  const isTel = (currentLang === 'te');

  const avEl = document.getElementById('direct-chat-avatar');
  if (avEl) avEl.innerText = contact.avatar;
  const nameEl = document.getElementById('direct-chat-contact-name');
  if (nameEl) nameEl.innerText = contact.name;
  const metaEl = document.getElementById('direct-chat-contact-meta');
  if (metaEl) metaEl.innerText = isTel ? `${contact.district} • ${contact.crop}` : `${contact.district_en} • ${contact.crop_en}`;

  renderDirectContacts();
  loadDirectChats();
}

async function loadDirectChats() {
  try {
    const res = await fetch('/api/community/chats');
    const chats = await res.json();
    const box = document.getElementById('direct-messages-box');
    if (!box) return;

    const contactData = chats[currentDirectContact] || { messages: [] };
    const contact = DIRECT_CONTACTS.find(c => c.key === currentDirectContact) || DIRECT_CONTACTS[0];
    const isTel = (currentLang === 'te');

    box.innerHTML = contactData.messages.map(m => {
      const isMe = (m.sender === 'You' || m.sender === currentUser.name || m.sender === 'రైతు');
      const senderTitle = isMe 
        ? (isTel ? 'మీరు (You)' : 'You')
        : `${contact.avatar} ${m.sender} (${isTel ? contact.district : contact.district_en})`;

      return `
        <div style="align-self: ${isMe ? 'flex-end' : 'flex-start'}; 
                    background: ${isMe ? 'linear-gradient(135deg, #10b981 0%, #059669 100%)' : 'rgba(16, 62, 46, 0.95)'}; 
                    border: 1px solid ${isMe ? 'transparent' : 'rgba(52, 211, 153, 0.35)'}; 
                    color: #ffffff; 
                    padding: 10px 14px; 
                    border-radius: ${isMe ? '14px 14px 2px 14px' : '14px 14px 14px 2px'}; 
                    max-width: 82%; 
                    font-size: 0.92rem;
                    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);">
          <div style="font-weight: 700; font-size: 0.72rem; color: ${isMe ? '#a7f3d0' : '#6ee7b7'}; margin-bottom: 3px;">
            ${senderTitle} • ${m.time}
          </div>
          <div style="line-height: 1.45; word-wrap: break-word;">${m.text}</div>
        </div>
      `;
    }).join('');
    box.scrollTop = box.scrollHeight;
  } catch (err) {
    console.error('Direct chat load error:', err);
  }
}

function sendDirectPreset(text) {
  const input = document.getElementById('direct-chat-input');
  if (input) input.value = text;
  sendDirectMessage();
}

async function sendDirectMessage() {
  const input = document.getElementById('direct-chat-input');
  const text = input ? input.value.trim() : '';
  if (!text) return;

  const box = document.getElementById('direct-messages-box');
  const now = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

  // 1. Immediately append user bubble for zero perceived latency
  if (box) {
    const userMsg = document.createElement('div');
    userMsg.style.cssText = 'align-self: flex-end; background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: #ffffff; padding: 10px 14px; border-radius: 14px 14px 2px 14px; max-width: 82%; font-size: 0.92rem; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.25);';
    userMsg.innerHTML = `<div style="font-weight: 700; font-size: 0.72rem; color: #a7f3d0; margin-bottom: 2px;">మీరు (You) • ${now}</div><div style="line-height: 1.45;">${text}</div>`;
    box.appendChild(userMsg);
    box.scrollTop = box.scrollHeight;
  }
  input.value = '';

  // 2. Show typing indicator
  const typingEl = document.getElementById('farmer-typing-indicator');
  if (typingEl) typingEl.style.display = 'block';

  try {
    const res = await fetch('/api/community/send-message', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        sender: currentUser.name || 'Archana',
        contact: currentDirectContact,
        text: text
      })
    });
    const data = await res.json();
    
    // Simulate brief typing delay for realistic interaction
    setTimeout(() => {
      if (typingEl) typingEl.style.display = 'none';
      if (box && data.farmer_reply) {
        const contact = DIRECT_CONTACTS.find(c => c.key === currentDirectContact) || DIRECT_CONTACTS[0];
        const botMsg = document.createElement('div');
        botMsg.style.cssText = 'align-self: flex-start; background: rgba(16, 62, 46, 0.95); border: 1px solid rgba(52, 211, 153, 0.35); color: #f1f5f9; padding: 10px 14px; border-radius: 14px 14px 14px 2px; max-width: 82%; font-size: 0.92rem; box-shadow: 0 4px 14px rgba(0,0,0,0.3);';
        botMsg.innerHTML = `<div style="font-weight: 700; font-size: 0.72rem; color: #6ee7b7; margin-bottom: 3px;">${contact.avatar} ${contact.name} (${contact.district}) • ${now}</div><div style="line-height: 1.45;">${data.farmer_reply}</div>`;
        box.appendChild(botMsg);
        box.scrollTop = box.scrollHeight;
      }
    }, 600);
  } catch (err) {
    if (typingEl) typingEl.style.display = 'none';
    console.error('Send direct message error:', err);
  }
}

// ----------------- App Bootstrapper -----------------
document.addEventListener('DOMContentLoaded', () => {
  applyLanguage();
  renderAllCanvasIcons();
  loadMandiRates();
  loadWeatherForDistrict('Vijayawada (Krishna)');
  loadCommunityPosts();
  renderDirectContacts();
  loadDirectChats();
});

window.addEventListener('resize', () => {
  renderAllCanvasIcons();
});
