"""
Karnata — generate_morning_bulletin.py
Generates the comprehensive Daily Morning Customized Notification & Bulletin.
Includes: Petrol rate, respective dam level, weather, top 5 news, gold rate, and important update.
"""

import os
import json
import base64
from datetime import datetime
from pathlib import Path

DATA_DIR = Path(__file__).parent / "../data"
SECRET = "NK_SECURE_KEY_2026_KARNATA"

def load_data(fname: str) -> dict | None:
    path = DATA_DIR / fname
    if not path.exists():
        return None
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(raw, dict) and "payload" in raw:
            binary = base64.b64decode(raw["payload"])
            key_bytes = SECRET.encode('utf-8')
            xor_bytes = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(binary)])
            return json.loads(xor_bytes.decode('utf-8'))
        return raw
    except Exception as e:
        print(f"Error loading {fname}: {e}")
        return None

def generate_bulletin(district_key: str = "bengaluru-urban") -> dict:
    gold = load_data("gold_rates.json")
    petrol = load_data("petrol_rates.json")
    dams = load_data("dam_levels.json")
    weather = load_data("weather.json")
    cms = load_data("cms_articles.json")
    local_news = load_data("local_news.json")

    # 1. Gold Rate
    g22 = gold.get("base", {}).get("22k_per_gram", 14080) if gold else 14080
    g24 = gold.get("base", {}).get("24k_per_gram", 15365) if gold else 15365
    silver = gold.get("silver", {}).get("999_per_gram", 239.90) if gold else 239.90
    g_change = gold.get("changes", {}).get("22k", 45) if gold else 45

    # 2. Petrol Rate
    p_rate = 102.86
    d_rate = 88.94
    if petrol and "districts" in petrol:
        dist_info = petrol["districts"].get(district_key, petrol["districts"].get("bengaluru-urban", {}))
        p_rate = dist_info.get("petrol", 102.86)
        d_rate = dist_info.get("diesel", 88.94)

    # 3. Respective Dam Level
    dam_name = "KRS (ಕೃಷ್ಣರಾಜ ಸಾಗರ)"
    dam_pct = 100
    dam_tmc = 49.45
    if dams and "dams" in dams:
        # Match nearest dam by district
        dam_map = {
            "mandya": "krs", "mysuru": "kabini", "bengaluru-urban": "krs", "bengaluru-rural": "krs",
            "bagalkote": "almatti", "vijayapura": "almatti", "belagavi": "malaprabha",
            "ballari": "tungabhadra", "koppal": "tungabhadra", "shivamogga": "bhadra",
            "uttara-kannada": "supa", "chitradurga": "vanivilasa", "kodagu": "harangi"
        }
        dam_id = dam_map.get(district_key, "krs")
        dam_obj = dams["dams"].get(dam_id, dams["dams"].get("krs", {}))
        dam_name = dam_obj.get("name_kn", "ಕೆಆರ್‌ಎಸ್")
        dam_pct = dam_obj.get("storage_pct", 100)
        dam_tmc = dam_obj.get("current_storage_tmc", 49.45)

    # 4. Weather
    temp_str = "24°C"
    condition = "ಹಗುರ ಮಳೆ ನಿರೀಕ್ಷೆ"
    if weather and "districts" in weather:
        w_obj = weather["districts"].get(district_key, weather["districts"].get("bengaluru-urban", {})).get("current", {})
        temp_str = f"{w_obj.get('temp_c', 24)}°C"
        condition = w_obj.get("condition_kn", "ಸಾಧಾರಣ ಮೋಡ")

    # 5. Top 5 News
    top_news = []
    if cms and "articles" in cms:
        for a in cms["articles"]:
            top_news.append(a.get("title_kn", ""))
    if local_news and "district_buckets" in local_news:
        for a in local_news["district_buckets"].get(district_key, local_news["district_buckets"].get("bengaluru-urban", [])):
            if len(top_news) < 5:
                t = a.get("title_kn", a.get("title", "")).strip()
                if t and t not in top_news:
                    top_news.append(t)

    top_news = top_news[:5]

    bulletin = {
        "updated_at": datetime.now().isoformat(),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "title": "🌅 ಮುಂಜಾನೆಯ ಕರ್ನಾಟಕ ಲೈವ್ ಬುಲೆಟಿನ್",
        "summary": f"🥇 ಚಿನ್ನ ₹{g22} | ⛽ ಪೆಟ್ರೋಲ್ ₹{p_rate} | 💧 {dam_name} {dam_pct}% | 🌦️ {temp_str} {condition}",
        "sections": {
            "gold": {
                "title": "🥇 ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ (Joyalukkas)",
                "g22": g22,
                "g24": g24,
                "silver": silver,
                "change": g_change,
                "display": f"22K: ₹{g22}/g (▲ +₹{g_change}) · 24K: ₹{g24}/g · ಬೆಳ್ಳಿ: ₹{silver}/g"
            },
            "fuel": {
                "title": "⛽ ಇಂಧನ ದರ (Fuel Rates)",
                "petrol": p_rate,
                "diesel": d_rate,
                "display": f"ಪೆಟ್ರೋಲ್: ₹{p_rate}/ಲೀ · ಡೀಸೆಲ್: ₹{d_rate}/ಲೀ"
            },
            "dam": {
                "title": "💧 ಜಲಾಶಯದ ನೀರಿನ ಮಟ್ಟ (Dam Level)",
                "name": dam_name,
                "storage_pct": dam_pct,
                "storage_tmc": dam_tmc,
                "display": f"{dam_name}: {dam_tmc} TMC ({dam_pct}% ಭರ್ತಿ)"
            },
            "weather": {
                "title": "🌦️ ಇಂದಿನ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ (Weather)",
                "temp": temp_str,
                "condition": condition,
                "display": f"{temp_str}, {condition}"
            },
            "top_5_news": top_news,
            "important_update": "🚨 ನಮ್ಮ ಮೆಟ್ರೋ ಹಂತ 2B ಕಾಮಗಾರಿ ಹಿನ್ನೆಲೆಯಲ್ಲಿ ವಿಮಾನ ನಿಲ್ದಾಣ ರಸ್ತೆಯಲ್ಲಿ ಸಂಚಾರ ಬದಲಾವಣೆ ಜಾರಿಯಲ್ಲಿದೆ ಹಾಗೂ ಕಾವೇರಿ ಕಣಿವೆ ಜಲಾಶಯಗಳಲ್ಲಿ ಒಳಹರಿವು ಹೆಚ್ಚಳವಾಗಿದೆ."
        }
    }

    out_file = DATA_DIR / "morning_bulletin.json"
    out_file.write_text(json.dumps(bulletin, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Generated morning_bulletin.json successfully!")
    return bulletin

if __name__ == "__main__":
    generate_bulletin()
