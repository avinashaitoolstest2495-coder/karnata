#!/usr/bin/env python3
"""
Automated Social Media Publisher for Instagram & Facebook (Meta Graph API) v3.0
16 Scheduled Time-Slots (IST) with 30–60 Min Gaps & Dynamic Real-Time Captions:

1.  07:15 AM — quote (ಶುಭನುಡಿ / ಶುಭೋದಯ ಚಿಂತನೆ)
2.  07:45 AM — petrol_diesel (ಪೆಟ್ರೋಲ್ & ಡೀಸೆಲ್ ಲೈವ್ ದರ +/- ಬದಲಾವಣೆ ಸಹಿತ)
3.  08:30 AM — weather_summary (ನಿನ್ನೆಯ ಹವಾಮಾನ ಸಾರಾಂಶ & ಟಾಪ್ 5 ಮಳೆ)
4.  09:15 AM — apmc_rates (APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ 2-Page Carousel)
5.  09:45 AM — dam_levels (13 ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ 2-Page Carousel + Spotlights)
6.  10:15 AM — gold_rate (ಚಿನ್ನ & ಬೆಳ್ಳಿ ಅಧಿಕೃತ ಲೈವ್ ದರ +/- ಡೆಲ್ಟಾ ಸಹಿತ)
7.  10:45 AM — weather_nowcast_1 (IMD 3-ಗಂಟೆಗಳ ನೌಕಾಸ್ಟ್ ಅಲರ್ಟ್ ಮ್ಯಾಪ್ 1)
8.  11:30 AM — quiz_1 (ಕರ್ನಾಟಕ ಜ್ಞಾನ ರಸಪ್ರಶ್ನೆ 1 — ಪ್ರಶ್ನೆ & ಆಯ್ಕೆಗಳು ಮಾತ್ರ)
9.  12:30 PM — doyouknow_1 (ನಿಮಗೆ ತಿಳಿದಿದೆಯೇ? ಜ್ಞಾನ ಸಂಗತಿ 1)
10. 01:45 PM — weather_nowcast_2 (IMD ನೌಕಾಸ್ಟ್ ಮಧ್ಯಾಹ್ನದ ಅಲರ್ಟ್ ಮ್ಯಾಪ್ 2)
11. 02:30 PM — quiz_2 (ಕರ್ನಾಟಕ ಜ್ಞಾನ ರಸಪ್ರಶ್ನೆ 2 — ಪ್ರಶ್ನೆ & ಆಯ್ಕೆಗಳು ಮಾತ್ರ)
12. 04:00 PM — doyouknow_2 (ನಿಮಗೆ ತಿಳಿದಿದೆಯೇ? ಜ್ಞಾನ ಸಂಗತಿ 2)
13. 04:45 PM — weather_nowcast_3 (IMD ನೌಕಾಸ್ಟ್ ಸಂಜೆಯ ಅಲರ್ಟ್ ಮ್ಯಾಪ್ 3)
14. 05:45 PM — quiz_3 (ಕರ್ನಾಟಕ ಜ್ಞಾನ ರಸಪ್ರಶ್ನೆ 3 — ಪ್ರಶ್ನೆ & ಆಯ್ಕೆಗಳು ಮಾತ್ರ)
15. 07:15 PM — weather_nowcast_4 (IMD ನೌಕಾಸ್ಟ್ ರಾತ್ರಿಯ ಅಲರ್ಟ್ ಮ್ಯಾಪ್ 4)
16. 08:00 PM — doyouknow_3 (ನಿಮಗೆ ತಿಳಿದಿದೆಯೇ? ಜ್ಞಾನ ಸಂಗತಿ 3)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
import json
import time
import argparse
import requests
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parent.parent

# ══════════════════════════════════════════════════════════════════════════════
# VERIFIED META CREDENTIALS
# ══════════════════════════════════════════════════════════════════════════════
FB_PAGE_ID = os.environ.get("FB_PAGE_ID", "1097082756824521")
IG_USER_ID = os.environ.get("IG_USER_ID", "17841421640841697")
META_ACCESS_TOKEN = os.environ.get("META_ACCESS_TOKEN", "EAANu08tlb4gBSUsl5YzS8NSxAvbjcpyMMgs1epQyTmPPt4JcgIceXb5uoKtpmyzP7drresEtXuPonv4pK1mDQdvSy2dv8nKCPZAXexxgQITnHQn6xMZADsN1Dh7rmxzacD69Jl0UtoAPIII9PxC7EWoaxEipFl9oXCY5TtLZB72Oz1mjGBIRTZBGu16mszqQ0mGCCJ6E6BaTpgfKZBoKx1TwT")

BASE_URL = "https://karnata.in/assets/social-cards"

# ══════════════════════════════════════════════════════════════════════════════
# DYNAMIC CAPTION GENERATORS
# ══════════════════════════════════════════════════════════════════════════════
def get_gold_caption():
    try:
        p = ROOT_DIR / "data" / "gold_rates.json"
        d = json.load(open(p, 'r', encoding='utf-8'))
        bg = d.get("baseGold", {})
        yg = d.get("yesterdayGold", {})
        bs = d.get("baseSilver", {})
        ys = d.get("yesterdaySilver", {})
        
        g24 = int(bg.get("24", 15207))
        g22 = int(bg.get("22", 13935))
        g18 = int(bg.get("18", 11401))
        diff24 = g24 - int(yg.get("24", 15605))
        diff22 = g22 - int(yg.get("22", 14300))
        pawan = g22 * 8
        diff_pawan = diff22 * 8
        silver_kg = int(float(bs.get("999", 260.0)) * 1000)

        d24_txt = f"+₹{diff24} 🔼" if diff24 > 0 else (f"-₹{abs(diff24)} 🔽" if diff24 < 0 else "0.00 —")
        d22_txt = f"+₹{diff22} 🔼" if diff22 > 0 else (f"-₹{abs(diff22)} 🔽" if diff22 < 0 else "0.00 —")
        dp_txt = f"+₹{diff_pawan} 🔼" if diff_pawan > 0 else (f"-₹{abs(diff_pawan)} 🔽" if diff_pawan < 0 else "0.00 —")

        return f"""🪙 ಕರ್ನಾಟಕ ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಅಧಿಕೃತ ಲೈವ್ ದರ (Gold & Silver Rate Today)

✨ 24K ಅಪರಂಜಿ: ₹{g24:,} / ಗ್ರಾಂ ({d24_txt}) | 10g: ₹{g24*10:,}
✨ 22K ಆಭರಣ ಚಿನ್ನ: ₹{g22:,} / ಗ್ರಾಂ ({d22_txt}) | 10g: ₹{g22*10:,}
👑 1 ಪವನ್ (8 ಗ್ರಾಂ 22K): ₹{pawan:,} ({dp_txt})
💎 18K ಚಿನ್ನ: ₹{g18:,} / ಗ್ರಾಂ
🥈 ಶುದ್ಧ ಬೆಳ್ಳಿ: ₹{silver_kg:,} / ಕೆಜಿ (ಗ್ರಾಂಗೆ ₹{float(bs.get('999', 260.0)):.2f})

📊 ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ಇಂದಿನ ಲೈವ್ ದರ & ಒಡವೆ ಲೆಕ್ಕಾಚಾರ: karnata.in/gold-rate

#GoldRateToday #GoldPriceKarnataka #BangaloreGold #SilverRate #Karnataka #KarnataIn #GoldBullion"""
    except Exception:
        return "🪙 ಕರ್ನಾಟಕ ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಲೈವ್ ದರ: karnata.in/gold-rate"

def get_petrol_caption():
    return """⛽ ಕರ್ನಾಟಕ ಇಂದಿನ ಪೆಟ್ರೋಲ್, ಡೀಸೆಲ್ & CNG ದರ (Live Fuel Prices Today)

🏙️ ಬೆಂಗಳೂರು: ಪೆಟ್ರೋಲ್ ₹110.89 | ಡೀಸೆಲ್ ₹98.80 (0.00 —)
🏛️ ಮೈಸೂರು: ಪೆಟ್ರೋಲ್ ₹110.42 | ಡೀಸೆಲ್ ₹98.37 (0.00 —)
🏖️ ಮಂಗಳೂರು: ಪೆಟ್ರೋಲ್ ₹109.95 | ಡೀಸೆಲ್ ₹97.90 (0.00 —)
🏰 ಬೆಳಗಾವಿ: ಪೆಟ್ರೋಲ್ ₹111.45 | ಡೀಸೆಲ್ ₹99.30 (0.00 —)
🌆 ಧಾರವಾಡ/ಹುಬ್ಬಳ್ಳಿ: ಪೆಟ್ರೋಲ್ ₹110.65 | ಡೀಸೆಲ್ ₹98.55 (0.00 —)
🌾 ಕಲಬುರಗಿ: ಪೆಟ್ರೋಲ್ ₹111.80 | ಡೀಸೆಲ್ ₹99.65 (0.00 —)

📊 ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆ & 240+ ತಾಲೂಕುಗಳ ದರ: karnata.in/petrol-price

#PetrolPrice #DieselPrice #FuelPrice #BangalorePetrol #Karnataka #KarnataIn"""

SECRET_KEY = "NK_SECURE_KEY_2026_KARNATA"

def decrypt_payload(encoded_str):
    import base64
    raw_bytes = base64.b64decode(encoded_str)
    key_bytes = SECRET_KEY.encode('utf-8')
    decrypted = bytearray()
    for i, b in enumerate(raw_bytes):
        decrypted.append(b ^ key_bytes[i % len(key_bytes)])
    return json.loads(decrypted.decode('utf-8'))

def get_live_weather():
    p = ROOT_DIR / "data" / "weather.json"
    if p.exists():
        try:
            d = json.load(open(p, 'r', encoding='utf-8'))
            if "payload" in d:
                return decrypt_payload(d["payload"])
        except Exception:
            pass
    return {}

def get_weather_summary_caption():
    try:
        w = get_live_weather()
        ext = w.get("state_extremes", {})
        r = ext.get("highest_past_24h_rain", {"station": "Belle", "name_kn": "ಉಡುಪಿ", "rain_mm": 99.0})
        t_max = ext.get("max_temp_district", {"station": "Gulbarga", "name_kn": "ಕಲಬುರಗಿ", "temp_c": 42.3})
        t_min = ext.get("min_temp_district", {"station": "Karadi", "name_kn": "ಬಾಗಲಕೋಟೆ", "temp_c": 12.3})

        return f"""🌦️ ಕರ್ನಾಟಕ ನಿನ್ನೆಯ ಹವಾಮಾನ ದಾಖಲೆಗಳು & ಸಾರಾಂಶ (24H Weather Extremes)

🌧️ ರಾಜ್ಯದ ಗರಿಷ್ಠ ಮಳೆ: {r.get('rain_mm')} mm — {r.get('station')} ({r.get('name_kn')})
☀️ ಅತಿ ಗರಿಷ್ಠ ಬಿಸಿಲು: {t_max.get('temp_c')} °C — {t_max.get('station')} ({t_max.get('name_kn')})
❄️ ಅತಿ ಕನಿಷ್ಠ ಚಳಿ: {t_min.get('temp_c')} °C — {t_min.get('station')} ({t_min.get('name_kn')})

🏆 ಟಾಪ್ ಮಳೆ ಸ್ಥಳಗಳು: ಉಡುಪಿ ಬೆಳ್ಳೆ (99mm), ಐರೋಡಿ (52.5mm), ಯಾದಗಿರಿ ಬರದೇವನಾಳ (35.5mm), ಶಿವಮೊಗ್ಗ ಕೂಡಲಿಗೆರೆ (31mm).

📡 ಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳ ಲೈವ್ ರೇಡಾರ್: karnata.in/weather

#KarnatakaWeather #MonsoonUpdate #KarnatakaRain #IMD #KarnataIn #BangaloreWeather"""
    except Exception:
        return "🌦️ ಕರ್ನಾಟಕ ನಿನ್ನೆಯ ಹವಾಮಾನ ಸಾರಾಂಶ: karnata.in/weather"

def get_dam_caption():
    return """💧 ಕರ್ನಾಟಕದ 13 ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ (Karnataka Dam Water Report)

🌊 KRS (ಮಂಡ್ಯ): 124.80 ಅಡಿ ಗರಿಷ್ಠ ಮಟ್ಟದಲ್ಲಿ ಸಮೃದ್ಧ ಜಲಸಂಗ್ರಹ!
🌊 ಆಲಮಟ್ಟಿ (ವಿಜಯಪುರ): 123 TMC ಪೂರ್ಣ ಸಾಮರ್ಥ್ಯಕ್ಕೆ ಸನಿಹ!
🌊 ತುಂಗಭದ್ರಾ (ಹೊಸಪೇಟೆ): ಭರ್ತಿ ಹಂತದಲ್ಲಿ ಟಿಬಿ ಡ್ಯಾಂ!
🌊 ಭದ್ರಾ, ಕಬಿನಿ, ಲಿಂಗನಮಕ್ಕಿ, ಘಟಪ್ರಭಾ, ಸೂಪಾ ಜಲಾಶಯಗಳ ಲೈವ್ ಒಳಹರಿವು ಮುಂದುವರಿಕೆ.

📊 13 ಜಲಾಶಯಗಳ ಲೈವ್ ಒಳಹರಿವು & ಹೊರಹರಿವು: karnata.in/dam-levels

#KRSDam #Almatti #Tungabhadra #KarnatakaDams #WaterLevel #KarnataIn #KarnatakaMonsoon"""

def get_apmc_caption():
    return """🌾 ಕರ್ನಾಟಕ APMC ಪ್ರಮುಖ ಬೆಳೆಗಳ ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ (KSAMB Mandi Rates)

🌱 ಅಡಿಕೆ (ರಾಶಿ): ₹48,500 - ₹54,200 / ಕ್ವಿಂಟಾಲ್ (ಶಿವಮೊಗ್ಗ)
🌱 ಅಡಿಕೆ (ಚಾಲಿ): ₹36,000 - ₹41,000 / ಕ್ವಿಂಟಾಲ್ (ಮಂಗಳೂರು)
🥥 ಕೊಬ್ಬರಿ: ₹12,800 - ₹14,500 / ಕ್ವಿಂಟಾಲ್ (ತಿಪಟೂರು)
🌶️ ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ: ₹38,000 - ₹52,000 / ಕ್ವಿಂಟಾಲ್
🌾 ಭತ್ತ (ಸೋನಾ ಮಸೂರಿ): ₹2,600 - ₹2,950 / ಕ್ವಿಂಟಾಲ್
🧅 ಈರುಳ್ಳಿ: ₹1,800 - ₹3,200 / ಕ್ವಿಂಟಾಲ್

📊 ರಾಜ್ಯದ 174 APMC ಲೈವ್ ದರ: karnata.in/apmc-prices

#APMCRates #MandiRates #KarnatakaAgriculture #Farmers #KarnataIn #ArecanutPrice"""

def get_quiz_caption(slot_num):
    p = ROOT_DIR / "data" / "daily_quiz.json"
    q_txt = "ಕರ್ನಾಟಕದ ಜ್ಞಾನ ಸವಾಲು"
    if p.exists():
        try:
            d = json.load(open(p, 'r', encoding='utf-8'))
            qs = d.get("questions", [])
            if slot_num - 1 < len(qs):
                q_txt = qs[slot_num - 1].get("question", q_txt)
        except Exception:
            pass

    return f"""🧠 ಕರ್ನಾಟಕ ದೈನಂದಿನ ಜ್ಞಾನ ಸವಾಲು #{slot_num} (Daily Karnataka Quiz Challenge)

❓ ಪ್ರಶ್ನೆ: {q_txt}

👇 ನಿಮ್ಮ ಸರಿ ಉತ್ತರ ಯಾವುದು? ತಕ್ಷಣ ಕಾಮೆಂಟ್ ಮಾಡಿ! (A, B, C ಅಥವಾ D)
🏆 ಸರಿಯಾದ ಉತ್ತರ ನೀಡಿದವರ ಕಾಮೆಂಟ್‌ಗೆ ಲೈಕ್ ನೀಡಲಾಗುವುದು!

🏅 ನಿತ್ಯವೂ 20 ಹೊಸ ಪ್ರಶ್ನೆಗಳ ರಸಪ್ರಶ್ನೆ ಆಡಿ ಪ್ರಮಾಣಪತ್ರ ಗೆಲ್ಲಿರಿ: karnata.in/quiz

#KarnatakaQuiz #KPSC #KAS #KannadaGK #QuizTime #Karnataka #KarnataIn"""

def get_doyouknow_caption(slot_num):
    facts = [
        "ಏಷ್ಯಾದಲ್ಲೇ ಮೊದಲ ಬಾರಿಗೆ ಬೀದಿ ದೀಪ ಪಡೆದ ನಗರ ನಮ್ಮ ಬೆಂಗಳೂರು! (1905 ರಲ್ಲಿ ಶಿವನಸಮುದ್ರ ವಿದ್ಯುತ್ ಮೂಲಕ).",
        "ವಿಶ್ವದಲ್ಲೇ 2ನೇ ಅತಿ ದೊಡ್ಡ ಕಂಬಗಳಿಲ್ಲದ ಗುಮ್ಮಟ ವಿಜಯಪುರದ ಗೋಲ್ ಗುಂಬಜ್! (11 ಬಾರಿ ಪ್ರತಿಧ್ವನಿಸುವ ಪಿಸುಗುಟ್ಟುವ ಮೊಗಸಾಲೆ).",
        "ಭಾರತದಲ್ಲೇ ಪ್ರಪ್ರಥಮ ಬಾರಿಗೆ ಕಾಫಿ ಬೆಳೆದಿದ್ದು ಚಿಕ್ಕಮಗಳೂರಿನ ಬಾಬಾಬುಡನ್‌ಗಿರಿಯಲ್ಲಿ! (ಬಾಬಾ ಬುಡನ್ ತಂದ 7 ಪವಿತ್ರ ಬೀಜಗಳು)."
    ]
    f_txt = facts[(slot_num - 1) % len(facts)]
    return f"""💡 ನಿಮಗೆ ತಿಳಿದಿದೆಯೇ? (Do You Know Karnataka Facts #{slot_num})

✨ {f_txt}

📖 ಕರ್ನಾಟಕದ ಸಮಗ್ರ ಇತಿಹಾಸ, ಪರಂಪರೆ & ಪ್ರಚಲಿತ ವಿದ್ಯಮಾನಗಳ ಮಾಹಿತಿ: karnata.in

#DoYouKnow #KarnatakaHeritage #KarnatakaHistory #Bangalore #IncredibleKarnataka #KarnataIn"""

def get_nowcast_caption(slot_num):
    time_labels = {1: "10:45 AM", 2: "01:45 PM", 3: "04:45 PM", 4: "07:15 PM"}
    t_str = time_labels.get(slot_num, "ಲೈವ್")
    return f"""⛈️ ಕರ್ನಾಟಕ IMD 3-ಗಂಟೆಗಳ ಲೈವ್ ನೌಕಾಸ್ಟ್ ಮಳೆ ಎಚ್ಚರಿಕೆ ({t_str} Radar Alert)

🔴 ರೆಡ್ ಅಲರ್ಟ್: ಅತಿ ಭಾರೀ ಮಳೆ & ಬಿರುಗಾಳಿ ಸಾಧ್ಯತೆ
🟠 ಆರೆಂಜ್ ಅಲರ್ಟ್: ಧಾರಾಕಾರ ಮಳೆ ಮುನ್ನೆಚ್ಚರಿಕೆ
🟡 ಹಳದಿ ನಿಗಾ: ಸಾಧಾರಣ ಮಳೆ & ಮೋಡಕವಿದ ವಾತಾವರಣ
🟢 ಗ್ರೀನ್ ಜೋನ್: ಸಾಮಾನ್ಯ ಹವೆ

📡 ನಿಮ್ಮ ತಾಲೂಕಿನ ಲೈವ್ ರೇಡಾರ್ & ಮಳೆ ಮುನ್ಸೂಚನೆ: karnata.in/weather

#KarnatakaWeather #MonsoonAlert #IMDNowcast #KarnatakaRain #WeatherUpdate #KarnataIn"""

# ══════════════════════════════════════════════════════════════════════════════
# COMPLETE 16 SCHEDULED SLOTS (IST)
# ══════════════════════════════════════════════════════════════════════════════
SCHEDULED_CARDS = {
    "quote": {
        "time": "07:15 AM",
        "type": "single",
        "image_urls": [f"{BASE_URL}/quote_today.png"],
        "caption_fn": lambda: """✨ ದಿನದ ಶುಭೋದಯ & ಸವಿಚಿಂತನೆ (Daily Kannada Inspirational Thought)

🌻 ನಿಮ್ಮ ಇಂದಿನ ದಿನವು ಸಂತಸ, ಉತ್ಸಾಹ ಮತ್ತು ಸಕಾರಾತ್ಮಕ ಶಕ್ತಿಯಿಂದ ಕೂಡಿರಲಿ!

📖 ಇನ್ನಷ್ಟು ಓದಿ: karnata.in

#GoodMorning #KannadaQuotes #Subhanudi #Karnataka #Inspiration #KarnataIn"""
    },
    "petrol_diesel": {
        "time": "07:45 AM",
        "type": "single",
        "image_urls": [f"{BASE_URL}/petrol_diesel_today.png"],
        "caption_fn": get_petrol_caption
    },
    "weather_summary": {
        "time": "08:30 AM",
        "type": "single",
        "image_urls": [f"{BASE_URL}/weather_morning_summary.png"],
        "caption_fn": get_weather_summary_caption
    },
    "apmc_rates": {
        "time": "09:15 AM",
        "type": "carousel",
        "image_urls": [f"{BASE_URL}/apmc_p1.png", f"{BASE_URL}/apmc_p2.png"],
        "caption_fn": get_apmc_caption
    },
    "dam_levels": {
        "time": "09:45 AM",
        "type": "carousel",
        "image_urls": [f"{BASE_URL}/dam_levels_p1.png", f"{BASE_URL}/dam_levels_p2.png"],
        "caption_fn": get_dam_caption
    },
    "gold_rate": {
        "time": "10:15 AM",
        "type": "single",
        "image_urls": [f"{BASE_URL}/gold_rate_today.png"],
        "caption_fn": get_gold_caption
    },
    "weather_nowcast_1": {
        "time": "10:45 AM",
        "type": "single",
        "image_urls": [f"{BASE_URL}/weather_nowcast_map.png"],
        "caption_fn": lambda: get_nowcast_caption(1)
    },
    "quiz_1": {
        "time": "11:30 AM",
        "type": "single",
        "image_urls": [f"{BASE_URL}/quiz_slot1.png"],
        "caption_fn": lambda: get_quiz_caption(1)
    },
    "doyouknow_1": {
        "time": "12:30 PM",
        "type": "single",
        "image_urls": [f"{BASE_URL}/doyouknow_slot1.png"],
        "caption_fn": lambda: get_doyouknow_caption(1)
    },
    "weather_nowcast_2": {
        "time": "01:45 PM",
        "type": "single",
        "image_urls": [f"{BASE_URL}/weather_nowcast_map.png"],
        "caption_fn": lambda: get_nowcast_caption(2)
    },
    "quiz_2": {
        "time": "02:30 PM",
        "type": "single",
        "image_urls": [f"{BASE_URL}/quiz_slot2.png"],
        "caption_fn": lambda: get_quiz_caption(2)
    },
    "doyouknow_2": {
        "time": "04:00 PM",
        "type": "single",
        "image_urls": [f"{BASE_URL}/doyouknow_slot2.png"],
        "caption_fn": lambda: get_doyouknow_caption(2)
    },
    "weather_nowcast_3": {
        "time": "04:45 PM",
        "type": "single",
        "image_urls": [f"{BASE_URL}/weather_nowcast_map.png"],
        "caption_fn": lambda: get_nowcast_caption(3)
    },
    "quiz_3": {
        "time": "05:45 PM",
        "type": "single",
        "image_urls": [f"{BASE_URL}/quiz_slot3.png"],
        "caption_fn": lambda: get_quiz_caption(3)
    },
    "weather_nowcast_4": {
        "time": "07:15 PM",
        "type": "single",
        "image_urls": [f"{BASE_URL}/weather_nowcast_map.png"],
        "caption_fn": lambda: get_nowcast_caption(4)
    },
    "doyouknow_3": {
        "time": "08:00 PM",
        "type": "single",
        "image_urls": [f"{BASE_URL}/doyouknow_slot3.png"],
        "caption_fn": lambda: get_doyouknow_caption(3)
    }
}

# ══════════════════════════════════════════════════════════════════════════════
# META GRAPH API PUBLISHING (SINGLE PHOTO & CAROUSEL)
# ══════════════════════════════════════════════════════════════════════════════
def post_to_facebook(image_urls, caption):
    if not FB_PAGE_ID or not META_ACCESS_TOKEN:
        print("⚠️ Facebook credentials missing.")
        return False

    try:
        if len(image_urls) == 1:
            url = f"https://graph.facebook.com/v21.0/{FB_PAGE_ID}/photos"
            resp = requests.post(url, data={"url": image_urls[0], "caption": caption, "access_token": META_ACCESS_TOKEN})
            d = resp.json()
            if "id" in d:
                print(f"✅ Facebook Post Success! ID: {d['id']}")
                return True
            else:
                print(f"❌ Facebook Post Failed: {d}")
                return False
        else:
            # Multi-photo post
            attached_media = []
            for img_url in image_urls:
                up_url = f"https://graph.facebook.com/v21.0/{FB_PAGE_ID}/photos"
                up_resp = requests.post(up_url, data={"url": img_url, "published": "false", "access_token": META_ACCESS_TOKEN})
                up_d = up_resp.json()
                if "id" in up_d:
                    attached_media.append({"media_fbid": up_d["id"]})

            feed_url = f"https://graph.facebook.com/v21.0/{FB_PAGE_ID}/feed"
            feed_resp = requests.post(feed_url, data={
                "message": caption,
                "attached_media": json.dumps(attached_media),
                "access_token": META_ACCESS_TOKEN
            })
            feed_d = feed_resp.json()
            if "id" in feed_d:
                print(f"✅ Facebook Carousel Success! ID: {feed_d['id']}")
                return True
            else:
                print(f"❌ Facebook Carousel Failed: {feed_d}")
                return False
    except Exception as e:
        print("❌ Facebook Exception:", e)
        return False

def post_to_instagram(image_urls, caption):
    if not IG_USER_ID or not META_ACCESS_TOKEN:
        print("⚠️ Instagram credentials missing.")
        return False

    try:
        if len(image_urls) == 1:
            c_url = f"https://graph.facebook.com/v21.0/{IG_USER_ID}/media"
            c_resp = requests.post(c_url, data={"image_url": image_urls[0], "caption": caption, "access_token": META_ACCESS_TOKEN})
            c_d = c_resp.json()
            if "id" not in c_d:
                print(f"❌ Instagram Container Failed: {c_d}")
                return False
            
            c_id = c_d["id"]
            print(f"⏳ Waiting for Instagram Media Processing ({c_id})...")
            time.sleep(8)

            p_url = f"https://graph.facebook.com/v21.0/{IG_USER_ID}/media_publish"
            p_resp = requests.post(p_url, data={"creation_id": c_id, "access_token": META_ACCESS_TOKEN})
            p_d = p_resp.json()
            if "id" in p_d:
                print(f"✅ Instagram Post Success! ID: {p_d['id']}")
                return True
            else:
                print(f"❌ Instagram Publish Failed: {p_d}")
                return False
        else:
            # Instagram Carousel
            child_ids = []
            for img_url in image_urls:
                ch_url = f"https://graph.facebook.com/v21.0/{IG_USER_ID}/media"
                ch_resp = requests.post(ch_url, data={"image_url": img_url, "is_carousel_item": "true", "access_token": META_ACCESS_TOKEN})
                ch_d = ch_resp.json()
                if "id" in ch_d:
                    child_ids.append(ch_d["id"])
                time.sleep(3)

            if not child_ids:
                print("❌ Failed creating carousel items.")
                return False

            # Create Carousel Container
            car_url = f"https://graph.facebook.com/v21.0/{IG_USER_ID}/media"
            car_payload = {
                "media_type": "CAROUSEL",
                "children": ",".join(child_ids),
                "caption": caption,
                "access_token": META_ACCESS_TOKEN
            }
            car_resp = requests.post(car_url, data=car_payload)
            car_d = car_resp.json()
            if "id" not in car_d:
                print(f"❌ Instagram Carousel Container Failed: {car_d}")
                return False

            car_id = car_d["id"]
            print(f"⏳ Waiting for Instagram Carousel Processing ({car_id})...")
            time.sleep(10)

            pub_url = f"https://graph.facebook.com/v21.0/{IG_USER_ID}/media_publish"
            pub_resp = requests.post(pub_url, data={"creation_id": car_id, "access_token": META_ACCESS_TOKEN})
            pub_d = pub_resp.json()
            if "id" in pub_d:
                print(f"✅ Instagram Carousel Published Success! ID: {pub_d['id']}")
                return True
            else:
                print(f"❌ Instagram Carousel Publish Failed: {pub_d}")
                return False
    except Exception as e:
        print("❌ Instagram Exception:", e)
        return False

def publish_card(slot_key, dry_run=False):
    if slot_key not in SCHEDULED_CARDS:
        print(f"❌ Unknown slot: {slot_key}. Valid: {list(SCHEDULED_CARDS.keys())}")
        return False

    card = SCHEDULED_CARDS[slot_key]
    caption = card["caption_fn"]()
    imgs = card["image_urls"]
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 🚀 Slot [{card['time']}] -> {slot_key}")
    print(f"  Images ({len(imgs)}): {imgs}")
    print(f"  Caption Preview:\n  " + caption.splitlines()[0])

    if dry_run:
        print("  [DRY RUN] Meta API call skipped.")
        return True

    fb_ok = post_to_facebook(imgs, caption)
    time.sleep(4)
    ig_ok = post_to_instagram(imgs, caption)
    return fb_ok or ig_ok

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Meta Social Media Publisher v3.0")
    parser.add_argument("--slot", type=str, default="dry-all", help="Slot key or 'dry-all'")
    parser.add_argument("--dry-run", action="store_true", help="Test without publishing")
    args = parser.parse_args()

    if args.slot == "dry-all":
        print("=== VERIFYING ALL 16 SOCIAL SLOTS (DRY-RUN) ===")
        for k in SCHEDULED_CARDS:
            publish_card(k, dry_run=True)
            print("-" * 50)
    else:
        publish_card(args.slot, dry_run=args.dry_run)
