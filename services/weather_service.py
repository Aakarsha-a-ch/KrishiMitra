import requests
from functools import lru_cache

AP_DISTRICTS = {
    "Vijayawada (Krishna)": (16.5062, 80.6480),
    "Guntur": (16.3067, 80.4365),
    "Amaravati": (16.5131, 80.5165),
    "East Godavari": (16.9891, 82.2475),
    "West Godavari": (16.7107, 81.0952),
    "Visakhapatnam": (17.6868, 83.2185),
    "Kurnool": (15.8281, 78.0373),
    "Anantapur": (14.6819, 77.6006),
    "Chittoor": (13.2172, 79.1003),
    "Kadapa": (14.4673, 78.8242),
    "Nellore": (14.4426, 79.9865),
    "Prakasam": (15.5057, 80.0499),
    "Srikakulam": (18.2949, 83.8938),
    "Vizianagaram": (18.1067, 83.3956)
}

@lru_cache(maxsize=128)
def geocode_location(location_name: str):
    """Geocode any Andhra Pradesh village, mandal, or town via Open-Meteo Geocoding."""
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={requests.utils.quote(location_name)}&count=1&language=en&format=json"
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            results = data.get("results")
            if results and len(results) > 0:
                item = results[0]
                return {
                    "name": item.get("name"),
                    "admin1": item.get("admin1", "Andhra Pradesh"),
                    "lat": item.get("latitude"),
                    "lon": item.get("longitude")
                }
    except Exception:
        pass
    return None

def auto_detect_ip_location():
    """Detect approximate live location from IP."""
    try:
        resp = requests.get("https://ipapi.co/json/", timeout=4)
        if resp.status_code == 200:
            d = resp.json()
            return {
                "name": f"{d.get('city', 'Vijayawada')}, {d.get('region', '')}",
                "lat": float(d.get('latitude', 16.5062)),
                "lon": float(d.get('longitude', 80.6480))
            }
    except Exception:
        pass
    return None

def fetch_weather(lat: float, lon: float):
    """Fetch high-resolution hourly and current weather metrics from Open-Meteo."""
    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
        "&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,rain,weather_code,cloud_cover,wind_speed_10m,wind_direction_10m"
        "&hourly=precipitation_probability,precipitation,temperature_2m"
        "&daily=precipitation_sum,precipitation_probability_max,temperature_2m_max,temperature_2m_min"
        "&timezone=auto"
    )
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        pass
    return None
