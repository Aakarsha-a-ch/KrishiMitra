import json
from pathlib import Path
import joblib

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "crop_recommendation_model.joblib"
META_PATH = ROOT / "models" / "crop_recommendation_metadata.json"

_CACHED_BUNDLE = None

def load_model():
    global _CACHED_BUNDLE
    if _CACHED_BUNDLE is not None:
        return _CACHED_BUNDLE
    bundle = joblib.load(MODEL_PATH)
    if not isinstance(bundle, dict) or not all(k in bundle for k in ("model", "label_encoder", "features")):
        raise ValueError("Unexpected model bundle format")
    _CACHED_BUNDLE = bundle
    return _CACHED_BUNDLE
