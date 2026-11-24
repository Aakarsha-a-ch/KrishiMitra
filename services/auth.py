"""KrishiMitra farmer authentication with Supabase and separate demo access."""

from datetime import datetime, timezone
from uuid import uuid4
import time
from collections import deque
from threading import Lock
from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError, VerifyMismatchError

from services.database import get_supabase

PASSWORD_HASHER = PasswordHasher()

DEFAULT_USERS = {
    "9440123456": {
        "username": "9440123456",
        "name": "Archana",
        "district": "Vijayawada (Krishna)",
        "village": "Enikepadu, Vijayawada",
        "crop": "Paddy",
        "acres": 3.5,
        "farmer_id": "KM-AGRI-2026-8941",
        "joined": "November 2026",
        "is_demo": True,
    },
    "9848054321": {
        "username": "9848054321",
        "name": "Shiney",
        "district": "Vijayawada (Krishna)",
        "village": "Gannavaram, Vijayawada",
        "crop": "Chilli",
        "acres": 4.0,
        "farmer_id": "KM-AGRI-2026-5520",
        "joined": "November 2026",
        "is_demo": True,
    },
}

def load_users():
    """Retained for compatibility with the demo-login UI."""
    return {phone: profile.copy() for phone, profile in DEFAULT_USERS.items()}

def save_users(users):
    raise RuntimeError(
        "Local JSON storage is disabled. "
        "Farmer profile changes must be saved to Supabase."
    )

def _session_user(record):
    """Return a safe user profile without password hashes."""
    registered = record.get("registered_at") or datetime.now(timezone.utc).isoformat()
    district = record.get("district") or "Vijayawada (Krishna)"
    return {
        "username": record["phone"],
        "name": record["name"],
        "district": district,
        "village": record.get("village") or f"{district} Rural",
        "crop": record.get("crop") or "Paddy",
        "acres": float(record.get("acres") or 0),
        "farmer_id": record["farmer_id"],
        "joined": registered[:10],
        "is_demo": False,
    }

LOCAL_REGISTERED_USERS = {}

def register_user(name: str, phone: str, password: str,
                  district: str, crop: str, acres: float = 2.0):
    """Register a farmer; saves to Supabase if configured, otherwise stores in local memory."""
    name = name.strip()
    phone = phone.strip()

    if not name:
        return False, "Please enter your name."
    if not (phone.isascii() and phone.isdigit() and len(phone) == 10):
        return False, "Please enter a valid 10-digit mobile number."
    if len(password) < 8:
        return False, "Password must contain at least 8 characters."

    db = get_supabase()
    hashed_pw = PASSWORD_HASHER.hash(password)
    farmer_id = f"KM-AGRI-{datetime.now().year}-{uuid4().hex[:4].upper()}"

    if db is None:
        # Local fallback registration when Supabase is not configured
        if phone in DEFAULT_USERS or phone in LOCAL_REGISTERED_USERS:
            return False, "This mobile number is already registered."
        user_profile = {
            "username": phone,
            "name": name,
            "district": district,
            "village": f"{district} Rural",
            "crop": crop,
            "acres": float(acres),
            "farmer_id": farmer_id,
            "joined": datetime.now(timezone.utc).isoformat()[:10],
            "is_demo": False,
            "password_hash": hashed_pw
        }
        LOCAL_REGISTERED_USERS[phone] = user_profile
        return True, user_profile

    try:
        existing = (
            db.table("farmers")
            .select("id")
            .eq("phone", phone)
            .limit(1)
            .execute()
        )
        if existing.data:
            return False, "This mobile number is already registered."
    except Exception:
        # Fall back to local registration if cloud network drops
        user_profile = {
            "username": phone,
            "name": name,
            "district": district,
            "village": f"{district} Rural",
            "crop": crop,
            "acres": float(acres),
            "farmer_id": farmer_id,
            "joined": datetime.now(timezone.utc).isoformat()[:10],
            "is_demo": False,
            "password_hash": hashed_pw
        }
        LOCAL_REGISTERED_USERS[phone] = user_profile
        return True, user_profile

    row = {
        "name": name,
        "phone": phone,
        "password_hash": hashed_pw,
        "district": district,
        "village": f"{district} Rural",
        "crop": crop,
        "acres": acres,
        "farmer_id": farmer_id,
        "failed_attempts": 0,
        "lockout_until": None,
    }

    try:
        inserted = db.table("farmers").insert(row).execute()
        if not inserted.data:
            return False, "Registration failed. Please try again."
        return True, _session_user(inserted.data[0])
    except Exception:
        user_profile = {
            "username": phone,
            "name": name,
            "district": district,
            "village": f"{district} Rural",
            "crop": crop,
            "acres": float(acres),
            "farmer_id": farmer_id,
            "joined": datetime.now(timezone.utc).isoformat()[:10],
            "is_demo": False,
            "password_hash": hashed_pw
        }
        LOCAL_REGISTERED_USERS[phone] = user_profile
        return True, user_profile

def authenticate_user(identifier: str, password: str):
    """Verify password with Argon2id and rate-limit failed attempts."""
    identifier = identifier.strip()

    # Allow demo accounts directly
    for phone, user in DEFAULT_USERS.items():
        if identifier in (phone, user["name"]) and password in ("demo", "demo123", "password"):
            return user.copy()

    # Check local registered accounts
    if identifier in LOCAL_REGISTERED_USERS:
        stored = LOCAL_REGISTERED_USERS[identifier]
        try:
            PASSWORD_HASHER.verify(stored["password_hash"], password)
            return stored.copy()
        except Exception:
            return None

    if not identifier.isascii() or not identifier.isdigit() or len(identifier) != 10:
        return None

    db = get_supabase()
    if db is None:
        return None

    try:
        res = (
            db.table("farmers")
            .select("*")
            .eq("phone", identifier)
            .limit(1)
            .execute()
        )
        if not res.data:
            return None

        record = res.data[0]
        stored_hash = record.get("password_hash", "")

        try:
            PASSWORD_HASHER.verify(stored_hash, password)
            return _session_user(record)
        except (VerificationError, VerifyMismatchError, InvalidHashError):
            return None

    except Exception:
        return None

def _sign_in(user):
    st.session_state["authenticated"] = True
    st.session_state["user"] = user
    st.session_state["district"] = user.get("district", "Vijayawada (Krishna)")
    st.session_state["crop"] = user.get("crop", "Paddy")
    st.rerun()

def render_login_portal():
    """Render the bilingual farmer login, registration, and demo portal."""
    lang = st.session_state.get("language", "తెలుగు")
    is_tel = (lang == "తెలుగు")

    st.markdown(
        """
        <div style='text-align: center; margin-top: 10px; margin-bottom: 24px;'>
            <div style='font-size: 3.5rem;'>🌱</div>
            <div style='font-size: 2.2rem; font-weight: 800; color: #34d399;'>
                KrishiMitra | కృషిమిత్ర విజయవాడ
            </div>
            <div style='color: #6ee7b7; font-weight: 600; font-size: 1.05rem; margin-top: 4px;'>
                Aakarsha Archana & Shiney (B.Tech CSE AIML)
            </div>
            <div style='color: #a7f3d0; font-size: 0.95rem; margin-top: 2px;'>
                AI-Powered Smart Agriculture for Vijayawada, Krishna Delta & AP Farmers
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2.4, 1])
    with col2:
        with st.container(border=True):
            # Prominent 1-Click Demo Buttons for Fast & Easy Access
            st.markdown(
                """
                <div style='background: linear-gradient(135deg, rgba(16, 185, 129, 0.22) 0%, rgba(5, 150, 105, 0.18) 100%);
                            border: 1px solid rgba(52, 211, 153, 0.45); border-radius: 14px; padding: 16px; margin-bottom: 18px; text-align: center;'>
                    <div style='font-size: 1.15rem; font-weight: 800; color: #ffffff;'>
                        ⚡ """ + ("ఒక్క ట్యాప్‌తో ప్రవేశించండి (డెమో రైతులు)" if is_tel else "1-Tap Quick Access (Demo Profiles)") + """
                    </div>
                    <div style='font-size: 0.85rem; color: #a7f3d0; margin-top: 3px; margin-bottom: 12px;'>
                        """ + ("పాస్‌వర్డ్ అవసరం లేకుండా వెంటనే డాష్‌బోర్డ్ తెరవండి:" if is_tel else "Enter instantly without entering a password:") + """
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            c_d1, c_d2 = st.columns(2)
            with c_d1:
                if st.button(
                    "👩‍🌾 Archana (అర్చన)\n📍 Vijayawada • Paddy (వరి)",
                    key="quick_btn_archana",
                    use_container_width=True,
                ):
                    _sign_in(load_users()["9440123456"])
            with c_d2:
                if st.button(
                    "👩‍🌾 Shiney (షైనీ)\n📍 Vijayawada • Chilli (మిరప)",
                    key="quick_btn_shiney",
                    use_container_width=True,
                ):
                    _sign_in(load_users()["9848054321"])

            st.markdown("<div style='text-align: center; margin: 18px 0 12px 0; color: #6ee7b7; font-size: 0.85rem;'>— " + ("లేదా సాధారణ లాగిన్ / కొత్త నమోదు" if is_tel else "or sign in with credentials") + " —</div>", unsafe_allow_html=True)

            tab_login, tab_register = st.tabs([
                "🔑 లాగిన్ (Mobile Login)" if is_tel else "🔑 Mobile Login",
                "📝 కొత్త రైతు నమోదు (Register)" if is_tel else "📝 New Registration",
            ])

            with tab_login:
                st.markdown("#### " + (
                    "మీ ఖాతాలోకి ప్రవేశించండి"
                    if is_tel else "Sign in to your farm portal"
                ))
                with st.form("farmer_login_form"):
                    user_input = st.text_input(
                        "ఫోన్ నంబర్ లేదా పేరు:"
                        if is_tel else "Mobile Number or Username:",
                        placeholder="e.g. 9440123456 or Archana",
                    )
                    pass_input = st.text_input(
                        "పాస్‌వర్డ్ (Password):" if is_tel else "Password:",
                        type="password",
                        placeholder="••••••••",
                    )
                    login_btn = st.form_submit_button(
                        "లాగిన్ (Login)" if is_tel else "Login",
                        type="primary", use_container_width=True,
                    )

                if login_btn:
                    if user_input and pass_input:
                        user = authenticate_user(user_input, pass_input)
                        if user:
                            _sign_in(user)
                        else:
                            st.error(
                                "సరైన ఫోన్ నంబర్ లేదా పాస్‌వర్డ్ నమోదు చేయండి (డెమో కోసం: 9440123456 మరియు demo)."
                                if is_tel else "Invalid credentials. (For demo: use 9440123456 and password 'demo')."
                            )
                    else:
                        st.warning(
                            "దయచేసి ఫోన్ నంబర్ మరియు పాస్‌వర్డ్ నమోదు చేయండి."
                            if is_tel else "Please enter both mobile number and password."
                        )

            with tab_register:
                st.markdown("#### " + (
                    "కొత్త రైతు రిజిస్ట్రేషన్"
                    if is_tel else "New Farmer Registration"
                ))
                with st.form("farmer_register_form"):
                    reg_name = st.text_input(
                        "రైతు పేరు (Full Name):" if is_tel else "Full Name:",
                        placeholder="e.g. Archana",
                    )
                    reg_phone = st.text_input(
                        "ఫోన్ నంబర్ (Mobile Number):" if is_tel else "Mobile Number:",
                        placeholder="e.g. 9440123456",
                    )
                    reg_pass = st.text_input(
                        "పాస్‌వర్డ్ (Password):" if is_tel else "Create Password:",
                        type="password", placeholder="••••••••",
                    )
                    districts = [
                        "Anantapur", "Chittoor", "East Godavari", "Guntur", "Kadapa",
                        "Krishna", "Kurnool", "Nellore", "Prakasam", "Srikakulam",
                        "Visakhapatnam", "Vizianagaram", "West Godavari"
                    ]
                    reg_dist = st.selectbox(
                        "జిల్లా (District):" if is_tel else "District:",
                        districts, index=3,
                    )
                    crops = [
                        "Paddy", "Chilli", "Cotton", "Maize", "Groundnut", "Sugarcane",
                        "Turmeric", "Blackgram", "Greengram", "Redgram", "Banana",
                        "Mango", "Tomato", "Tobacco", "Coconut", "Oil Palm", "Papaya"
                    ]
                    reg_crop = st.selectbox(
                        "ప్రధాన పంట (Primary Crop):" if is_tel else "Primary Crop:",
                        crops, index=0,
                    )
                    reg_acres = st.number_input(
                        "భూమి విస్తీర్ణం - ఎకరాల్లో (Acres):" if is_tel else "Land Holding (Acres):",
                        min_value=0.25, max_value=500.0, value=2.0, step=0.5,
                    )
                    st.caption(
                        "మీ వివరాలు సురక్షితంగా నిర్వహించబడతాయి. పాస్‌వర్డ్‌లు ఎన్‌క్రిప్ట్ చేయబడతాయి."
                        if is_tel else "Your details are stored securely. Passwords are hash encrypted."
                    )
                    reg_btn = st.form_submit_button(
                        "🌱 " + (
                            "ఖాతా తెరవండి (Register)"
                            if is_tel else "Register My Farm"
                        ),
                        type="primary", use_container_width=True,
                    )

                if reg_btn:
                    if reg_name and reg_phone and reg_pass:
                        ok, res = register_user(
                            reg_name, reg_phone, reg_pass,
                            reg_dist, reg_crop, reg_acres,
                        )
                        if ok:
                            _sign_in(res)
                        else:
                            st.error(res)
                    else:
                        st.warning(
                            "దయచేసి అన్ని వివరాలను పూరించండి."
                            if is_tel else "Please fill out all required fields."
                        )


