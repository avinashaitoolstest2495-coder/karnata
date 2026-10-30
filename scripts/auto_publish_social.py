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
print("[STOPPED] Social media auto-posting has been permanently DISABLED by user request.")
sys.exit(0)

import os
import json
import time
import argparse
import requests
from pathlib import Path
from datetime import datetime
try:
    from scripts.generate_daily_social_graphics import DOYOUKNOW_FACTS
except Exception:
    try:
        from generate_daily_social_graphics import DOYOUKNOW_FACTS
    except Exception:
        DOYOUKNOW_FACTS = []

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

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
def get_kannada_date_str():
    months = {
        1: "ಜನವರಿ", 2: "ಫೆಬ್ರವರಿ", 3: "ಮಾರ್ಚ್", 4: "ಏಪ್ರಿಲ್", 5: "ಮೇ", 6: "ಜೂನ್",
        7: "ಜುಲೈ", 8: "ಆಗಸ್ಟ್", 9: "ಸೆಪ್ಟೆಂಬರ್", 10: "ಅಕ್ಟೋಬರ್", 11: "ನವೆಂಬರ್", 12: "ಡಿಸೆಂಬರ್"
    }
    now = datetime.now()
    return f"{now.day} {months.get(now.month, '')} {now.year}"

def get_gold_caption():
    try:
        p = ROOT_DIR / "data" / "gold_rates.json"
        d = json.load(open(p, 'r', encoding='utf-8'))
        bg = d.get("baseGold") or d.get("base") or {}
        yg = d.get("yesterdayGold") or {}
        bs = d.get("baseSilver") or d.get("silver") or {}
        ys = d.get("yesterdaySilver") or {}
        
        g24 = int(bg.get("24") or bg.get(24) or bg.get("24k_per_gram") or bg.get("rate_24k") or 14335)
        g22 = int(bg.get("22") or bg.get(22) or bg.get("22k_per_gram") or bg.get("rate_22k") or 13135)
        g18 = int(bg.get("18") or bg.get(18) or bg.get("18k_per_gram") or bg.get("rate_18k") or 10750)

        y24 = int(yg.get("24") or yg.get(24) or yg.get("24k_per_gram") or 14280)
        y22 = int(yg.get("22") or yg.get(22) or yg.get("22k_per_gram") or 13085)
        
        diff24 = g24 - y24
        diff22 = g22 - y22
        pawan = g22 * 8
        diff_pawan = diff22 * 8
        s999 = float(bs.get("999") or bs.get(999) or bs.get("silver_per_gram") or bs.get("silver_999") or 260.0)
        silver_kg = int(s999 * 1000)

        d24_txt = f"+₹{diff24:,} 🔼" if diff24 > 0 else (f"-₹{abs(diff24):,} 🔽" if diff24 < 0 else "0.00 —")
        d22_txt = f"+₹{diff22:,} 🔼" if diff22 > 0 else (f"-₹{abs(diff22):,} 🔽" if diff22 < 0 else "0.00 —")
        dp_txt = f"+₹{diff_pawan:,} 🔼" if diff_pawan > 0 else (f"-₹{abs(diff_pawan):,} 🔽" if diff_pawan < 0 else "0.00 —")

        months = {1: "ಜನವರಿ", 2: "ಫೆಬ್ರವರಿ", 3: "ಮಾರ್ಚ್", 4: "ಏಪ್ರಿಲ್", 5: "ಮೇ", 6: "ಜೂನ್", 7: "ಜುಲೈ", 8: "ಆಗಸ್ಟ್", 9: "ಸೆಪ್ಟೆಂಬರ್", 10: "ಅಕ್ಟೋಬರ್", 11: "ನವೆಂಬರ್", 12: "ಡಿಸೆಂಬರ್"}
        now = datetime.now()
        date_kn = f"{now.day} {months.get(now.month, '')} {now.year}"

        return f"""🪙 ಕರ್ನಾಟಕ ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಅಧಿಕೃತ ಲೈವ್ ದರ (Gold & Silver Rate Today)
📅 ದಿನಾಂಕ: {date_kn} ({now.strftime('%d-%m-%Y')})

✨ 24K ಅಪರಂಜಿ: ₹{g24:,} / ಗ್ರಾಂ ({d24_txt}) | 10g: ₹{g24*10:,}
✨ 22K ಆಭರಣ ಚಿನ್ನ: ₹{g22:,} / ಗ್ರಾಂ ({d22_txt}) | 10g: ₹{g22*10:,}
👑 1 ಪವನ್ (8 ಗ್ರಾಂ 22K): ₹{pawan:,} ({dp_txt})
💎 18K ಚಿನ್ನ: ₹{g18:,} / ಗ್ರಾಂ
🥈 ಶುದ್ಧ ಬೆಳ್ಳಿ: ₹{silver_kg:,} / ಕೆಜಿ (ಗ್ರಾಂಗೆ ₹{s999:.2f})

📊 ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ಇಂದಿನ ಲೈವ್ ದರ & ಒಡವೆ ಲೆಕ್ಕಾಚಾರ:
🌐 https://karnata.in/gold-rate
📲 ಬಯೋದಲ್ಲಿ ಲಿಂಕ್ ಇದೆ (Link in Bio: @karnata.in)

#GoldRateToday #GoldPriceKarnataka #BangaloreGold #SilverRate #Karnataka #KarnataIn #GoldBullion"""
    except Exception:
        return "🪙 ಕರ್ನಾಟಕ ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಲೈವ್ ದರ: https://karnata.in/gold-rate"

def get_petrol_caption():
    try:
        p_data = get_live_petrol()
        dist_dict = p_data.get("districts", {})
        
        cities = [
            ("bengaluru_urban", "🏙️ ಬೆಂಗಳೂರು"),
            ("mysuru", "🏛️ ಮೈಸೂರು"),
            ("dakshina_kannada", "🏖️ ಮಂಗಳೂರು"),
            ("belagavi", "🏰 ಬೆಳಗಾವಿ"),
            ("dharwad", "🌆 ಧಾರವಾಡ/ಹುಬ್ಬಳ್ಳಿ"),
            ("kalaburagi", "🌾 ಕಲಬುರಗಿ"),
            ("shivamogga", "🌲 ಶಿವಮೊಗ್ಗ")
        ]
        
        lines = []
        for k, name in cities:
            p_val = 110.89
            d_val = 98.80
            if k in dist_dict:
                taluks = dist_dict[k].get("taluks", {})
                if taluks:
                    t = list(taluks.values())[0]
                    p_val = t.get("petrol", p_val)
                    d_val = t.get("diesel", d_val)
            lines.append(f"{name}: ಪೆಟ್ರೋಲ್ ₹{p_val:.2f} | ಡೀಸೆಲ್ ₹{d_val:.2f}")
            
        rate_str = "\n".join(lines)
        return f"""⛽ ಕರ್ನಾಟಕ ಇಂದಿನ ಪೆಟ್ರೋಲ್, ಡೀಸೆಲ್ & ಇಂಧನ ದರ (Live Fuel Prices Today)

{rate_str}

📊 ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆ & 240+ ತಾಲೂಕುಗಳ ದರ: karnata.in/petrol-price

#PetrolPrice #DieselPrice #FuelPrice #BangalorePetrol #Karnataka #KarnataIn"""
    except Exception:
        return """⛽ ಕರ್ನಾಟಕ ಇಂದಿನ ಪೆಟ್ರೋಲ್ & ಡೀಸೆಲ್ ಲೈವ್ ದರ: karnata.in/petrol-price"""

SECRET_KEY = "NK_SECURE_KEY_2026_KARNATA"

def decrypt_payload(encoded_str):
    import base64
    raw_bytes = base64.b64decode(encoded_str)
    key_bytes = SECRET_KEY.encode('utf-8')
    decrypted = bytearray()
    for i, b in enumerate(raw_bytes):
        decrypted.append(b ^ key_bytes[i % len(key_bytes)])
    return json.loads(decrypted.decode('utf-8'))

def get_live_petrol():
    p = ROOT_DIR / "data" / "petrol_rates.json"
    if p.exists():
        try:
            d = json.load(open(p, 'r', encoding='utf-8'))
            if "payload" in d:
                return decrypt_payload(d["payload"])
        except Exception:
            pass
    return {}

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
        r = ext.get("highest_past_24h_rain", {"station": "Devachalla", "name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "rain_mm": 53.0})
        t_max = ext.get("max_temp_district", {"station": "Gulbarga", "name_kn": "ಕಲಬುರಗಿ", "temp_c": 38.8})
        t_min = ext.get("min_temp_district", {"station": "Chadchan", "name_kn": "ವಿಜಯಪುರ", "temp_c": 13.4})

        top_r = ext.get("top_rainfall_locations") or ext.get("heavy_rain_locations") or []
        top_r_str = []
        for loc in top_r[:5]:
            dist = loc.get("district_kn") or loc.get("name_kn") or loc.get("district_en")
            if dist == "Bengaluru South": dist = "ಬೆಂ.ದಕ್ಷಿಣ"
            st = loc.get("gp_name") or loc.get("station") or dist
            mm = loc.get("rainfall_mm") or loc.get("rain_mm") or 0
            top_r_str.append(f"{st} ({dist} - {mm}mm)")

        top_hot = ext.get("top_max_temp_locations") or []
        top_hot_str = []
        for loc in top_hot[:3]:
            dist = loc.get("district_kn") or loc.get("name_kn") or loc.get("district_en")
            st = loc.get("hobli") or loc.get("station") or dist
            tc = loc.get("temp_c") or 0
            top_hot_str.append(f"{dist} {st} ({tc}°C)")

        top_cold = ext.get("top_min_temp_locations") or []
        top_cold_str = []
        for loc in top_cold[:3]:
            dist = loc.get("district_kn") or loc.get("name_kn") or loc.get("district_en")
            st = loc.get("hobli") or loc.get("station") or dist
            tc = loc.get("temp_c") or 0
            top_cold_str.append(f"{dist} {st} ({tc}°C)")

        r_txt = "\n".join([f"  • {s}" for s in top_r_str]) if top_r_str else f"  • {r.get('name_kn')} ({r.get('rain_mm')}mm)"
        hot_txt = ", ".join(top_hot_str) if top_hot_str else f"{t_max.get('name_kn')} ({t_max.get('temp_c')}°C)"
        cold_txt = ", ".join(top_cold_str) if top_cold_str else f"{t_min.get('name_kn')} ({t_min.get('temp_c')}°C)"

        return f"""🌦️ ಕರ್ನಾಟಕ ನಿನ್ನೆಯ ಹವಾಮಾನ ದಾಖಲೆಗಳು & ಅಧಿಕೃತ ಸಾರಾಂಶ (24H Weather Extremes)

🌧️ ರಾಜ್ಯದ ಗರಿಷ್ಠ ಮಳೆ: {r.get('rain_mm')} mm — {r.get('station')} ({r.get('name_kn')} ಜಿಲ್ಲೆ)
☀️ ಅತಿ ಗರಿಷ್ಠ ಬಿಸಿಲು: {t_max.get('temp_c')} °C — {t_max.get('station')} ({t_max.get('name_kn')} ಜಿಲ್ಲೆ)
❄️ ಅತಿ ಕನಿಷ್ಠ ಚಳಿ: {t_min.get('temp_c')} °C — {t_min.get('station')} ({t_min.get('name_kn')} ಜಿಲ್ಲೆ)

🌧️ ಅತಿ ಹೆಚ್ಚು ಮಳೆ ಬಂದ ಪ್ರದೇಶಗಳು (Top 5):
{r_txt}

🔥 ಗರಿಷ್ಠ ತಾಪಮಾನ (Top 3): {hot_txt}
❄️ ಕನಿಷ್ಠ ತಾಪಮಾನ (Top 3): {cold_txt}

📡 ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳ ಲೈವ್ ರೇಡಾರ್ & ಹವಾಮಾನ ವಿವರ: karnata.in/weather

#KarnatakaWeather #MonsoonUpdate #KarnatakaRain #IMD #KarnataIn #BangaloreWeather #WeatherReport"""
    except Exception:
        return "🌦️ ಕರ್ನಾಟಕ ನಿನ್ನೆಯ ಹವಾಮಾನ ಸಾರಾಂಶ: karnata.in/weather"

def get_live_dams():
    p = ROOT_DIR / "data" / "dam_levels.json"
    if p.exists():
        try:
            d = json.load(open(p, 'r', encoding='utf-8'))
            if "payload" in d:
                return decrypt_payload(d["payload"]).get("dams", {})
        except Exception:
            pass
    return {}

def get_dam_caption():
    try:
        dams = get_live_dams()
        krs = dams.get("krs", {})
        alm = dams.get("almatti", {})
        tb = dams.get("tungabhadra", {})
        bhd = dams.get("bhadra", {})
        
        krs_st = krs.get("storage_tmc", 27.5)
        krs_in = int(krs.get("inflow_cusecs", 4934))
        alm_st = alm.get("storage_tmc", 122.6)
        alm_in = int(alm.get("inflow_cusecs", 522))
        tb_st = tb.get("storage_tmc", 85.8)
        bhd_st = bhd.get("storage_tmc", 65.0)

        months = {1: "ಜನವರಿ", 2: "ಫೆಬ್ರವರಿ", 3: "ಮಾರ್ಚ್", 4: "ಏಪ್ರಿಲ್", 5: "ಮೇ", 6: "ಜೂನ್", 7: "ಜುಲೈ", 8: "ಆಗಸ್ಟ್", 9: "ಸೆಪ್ಟೆಂಬರ್", 10: "ಅಕ್ಟೋಬರ್", 11: "ನವೆಂಬರ್", 12: "ಡಿಸೆಂಬರ್"}
        now = datetime.now()
        date_kn = f"{now.day} {months.get(now.month, '')} {now.year}"
        
        return f"""💧 ಕರ್ನಾಟಕದ 13 ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ (Karnataka Dam Water Live Report)
📅 ದಿನಾಂಕ: {date_kn} ({now.strftime('%d-%m-%Y')})

🌊 KRS (ಮಂಡ್ಯ): ಸಂಗ್ರಹ {krs_st:.2f} TMC (ಒಳಹರಿವು: {krs_in:,} ಕ್ಯೂಸೆಕ್)
🌊 ಆಲಮಟ್ಟಿ (ವಿಜಯಪುರ): ಸಂಗ್ರಹ {alm_st:.2f} TMC / 123 TMC (ಭರ್ತಿ ಸ್ಥಿತಿ)
🌊 ತುಂಗಭದ್ರಾ (ಹೊಸಪೇಟೆ): ಸಂಗ್ರಹ {tb_st:.2f} TMC / 105 TMC
🌊 ಭದ್ರಾ (ಚಿಕ್ಕಮಗಳೂರು): ಸಂಗ್ರಹ {bhd_st:.2f} TMC
🌊 ಕಬಿನಿ, ಲಿಂಗನಮಕ್ಕಿ, ಘಟಪ್ರಭಾ, ಸೂಪಾ ಜಲಾಶಯಗಳ ಲೈವ್ ಒಳಹರಿವು ವಿವರ.

📊 ಎಲ್ಲಾ 13 ಜಲಾಶಯಗಳ ಲೈವ್ ಮಟ್ಟ & ಒಳಹರಿವು:
🌐 https://karnata.in/dam-levels
📲 ಬಯೋದಲ್ಲಿ ಲಿಂಕ್ ಇದೆ (Link in Bio: @karnata.in)

#KRSDam #Almatti #Tungabhadra #KarnatakaDams #WaterLevel #KarnataIn #KarnatakaMonsoon"""
    except Exception:
        return "💧 ಕರ್ನಾಟಕದ 13 ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ: https://karnata.in/dam-levels"

def get_apmc_caption():
    try:
        p = ROOT_DIR / "data" / "apmc_prices.json"
        d = json.load(open(p, 'r', encoding='utf-8'))
        items = d.get("items", [])
        
        highlights = []
        for item in items:
            c = (item.get("crop", "") + " " + item.get("cropKn", "")).lower()
            m = item.get("market", "")
            if "arecanut" in c and any(k in m for k in ["SHIVAMOGGA", "BANTWALA", "SAGAR"]):
                highlights.append(f"🌱 ಅಡಿಕೆ: ₹{item['min']:,} - ₹{item['max']:,} / ಕ್ವಿಂ ({item['market'].title()})")
                break
        for item in items:
            c = (item.get("crop", "") + " " + item.get("cropKn", "")).lower()
            if "chilli" in c and "BYADGI" in item.get("market", ""):
                highlights.append(f"🌶️ ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ: ₹{item['min']:,} - ₹{item['max']:,} / ಕ್ವಿಂ")
                break
        for item in items:
            c = (item.get("crop", "") + " " + item.get("cropKn", "")).lower()
            if "copra" in c and any(k in item.get("market", "") for k in ["ARSIKERE", "TIPTUR"]):
                highlights.append(f"🥥 ಕೊಬ್ಬರಿ: ₹{item['min']:,} - ₹{item['max']:,} / ಕ್ವಿಂ ({item['market'].title()})")
                break
        for item in items:
            c = (item.get("crop", "") + " " + item.get("cropKn", "")).lower()
            if "paddy" in c and any(k in item.get("market", "") for k in ["GANGAVATI", "DAVANAGERE"]):
                highlights.append(f"🌾 ಭತ್ತ: ₹{item['min']:,} - ₹{item['max']:,} / ಕ್ವಿಂ ({item['market'].title()})")
                break
        for item in items:
            c = (item.get("crop", "") + " " + item.get("cropKn", "")).lower()
            if "onion" in c and any(k in item.get("market", "") for k in ["BAGALKOT", "HUBBALLI", "BANGARPET"]):
                highlights.append(f"🧅 ಈರುಳ್ಳಿ: ₹{item['min']:,} - ₹{item['max']:,} / ಕ್ವಿಂ ({item['market'].title()})")
                break
                
        h_str = "\n".join(highlights) if highlights else "🌱 ಅಡಿಕೆ, ಕೊಬ್ಬರಿ, ಹತ್ತಿ, ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ, ಭತ್ತ, ಈರುಳ್ಳಿ ಧಾರಣೆ ಲಭ್ಯ."
        return f"""🌾 ಕರ್ನಾಟಕ APMC ಪ್ರಮುಖ ಬೆಳೆಗಳ ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ (KSAMB Mandi Rates Today)

{h_str}

📊 ರಾಜ್ಯದ 174 APMC ಅಧಿಕೃತ ಲೈವ್ ದರ: karnata.in/apmc-prices

#APMCRates #MandiRates #KarnatakaAgriculture #Farmers #KarnataIn #ArecanutPrice"""
    except Exception:
        return "🌾 ಕರ್ನಾಟಕ APMC ಪ್ರಮುಖ ಬೆಳೆಗಳ ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ: karnata.in/apmc-prices"

def get_quiz_caption(slot_num):
    p = ROOT_DIR / "data" / "daily_quiz.json"
    q_txt = "ಕರ್ನಾಟಕದ ಜ್ಞಾನ ಸವಾಲು"
    options = []
    if p.exists():
        try:
            d = json.load(open(p, 'r', encoding='utf-8'))
            qs = d.get("questions", [])
            day_of_year = datetime.now().timetuple().tm_yday
            if qs:
                q_idx = (day_of_year * 3 + slot_num - 1) % len(qs)
                q_item = qs[q_idx]
                q_txt = q_item.get("question", q_txt)
                options = q_item.get("options", [])
        except Exception:
            pass

    opt_letters = ["A", "B", "C", "D"]
    opt_lines = "\n".join([f"{opt_letters[i]}) {opt}" for i, opt in enumerate(options[:4])]) if options else ""

    return f"""🧠 ಕರ್ನಾಟಕ ದೈನಂದಿನ ಜ್ಞಾನ ಸವಾಲು #{slot_num} (Daily Karnataka Quiz Challenge)

❓ ಪ್ರಶ್ನೆ: {q_txt}

{opt_lines}

👇 ನಿಮ್ಮ ಸರಿ ಉತ್ತರ ಯಾವುದು? ತಕ್ಷಣ ಕಾಮೆಂಟ್ ಮಾಡಿ! (A, B, C ಅಥವಾ D)
🏆 ಸರಿಯಾದ ಉತ್ತರ ನೀಡಿದವರ ಕಾಮೆಂಟ್‌ಗೆ ಲೈಕ್ & ಶೌಟೌಟ್ ನೀಡಲಾಗುವುದು!

🏅 ನಿತ್ಯವೂ 20 ಹೊಸ ಪ್ರಶ್ನೆಗಳ ರಸಪ್ರಶ್ನೆ ಆಡಿ ಆನ್‌ಲೈನ್ ಪ್ರಮಾಣಪತ್ರ ಪಡೆಯಿರಿ:
🌐 https://karnata.in/quiz
📲 ಬಯೋದಲ್ಲಿ ಲಿಂಕ್ ಇದೆ (Link in Bio: @karnata.in)

#KarnatakaQuiz #KPSC #KAS #KannadaGK #QuizTime #Karnataka #KarnataIn #GeneralKnowledge #KarnatakaGovt"""

def get_doyouknow_caption(slot_num):
    day_of_year = datetime.now().timetuple().tm_yday
    if DOYOUKNOW_FACTS:
        fact_idx = (day_of_year * 3 + slot_num - 1) % len(DOYOUKNOW_FACTS)
        f_txt = DOYOUKNOW_FACTS[fact_idx].get("fact", "")
    else:
        f_txt = "ಕರ್ನಾಟಕದ ಸಮಗ್ರ ಇತಿಹಾಸ, ಸಂಸ್ಕೃತಿ ಮತ್ತು ಪರಂಪರೆ."

    return f"""💡 ನಿಮಗೆ ತಿಳಿದಿದೆಯೇ? #{slot_num} (Did You Know Karnataka)

✨ {f_txt}

📖 ಕರ್ನಾಟಕದ ಸಮಗ್ರ ಇತಿಹಾಸ, ಪರಂಪರೆ & ಪ್ರಚಲಿತ ವಿದ್ಯಮಾನಗಳ ಮಾಹಿತಿ:
🌐 https://karnata.in
📲 Instagram ಬಯೋದಲ್ಲಿ (Bio Link) ನೇರ ಲಿಂಕ್ ಲಭ್ಯವಿದೆ: @karnata.in

#DoYouKnow #KarnatakaHeritage #KarnatakaHistory #Bangalore #IncredibleKarnataka #KarnataIn #KannadaGK #KarnatakaFacts"""

def get_nowcast_caption(slot_num):
    time_labels = {1: "10:45 AM", 2: "01:45 PM", 3: "04:45 PM", 4: "07:15 PM"}
    t_str = time_labels.get(slot_num, "ಲೈವ್")
    date_kn = get_kannada_date_str()
    try:
        w = get_live_weather()
        ext = w.get("state_extremes", {})
        r = ext.get("highest_past_24h_rain", {})
        t_max = ext.get("max_temp_district", {})
        t_min = ext.get("min_temp_district", {})

        r_dst = r.get('name_kn') or r.get('district_en', '')
        r_st = r.get('station', '')
        r_loc = f"{r_dst} ({r_st})" if r_st and r_dst else (r_dst or r_st)
        r_txt = f"🌧️ 24H ಗರಿಷ್ಠ ಮಳೆ: {float(r.get('rain_mm', 0.0)):.1f} mm — {r_loc}" if r_loc else "🌧️ 24H ಅಧಿಕೃತ ಲೈವ್ ಮಳೆ ದಾಖಲೆ"

        max_dst = t_max.get('name_kn') or t_max.get('district_en', '')
        min_dst = t_min.get('name_kn') or t_min.get('district_en', '')
        t_txt = f"☀️ ಗರಿಷ್ಠ: {float(t_max.get('temp_c', 0.0)):.1f}°C ({max_dst}) | ❄️ ಕನಿಷ್ಠ: {float(t_min.get('temp_c', 0.0)):.1f}°C ({min_dst})"

        warnings = w.get("imd_warnings", {})
        red_dists = [v.get("district_kn", k) for k, v in warnings.items() if v.get("level") == "red"]
        orange_dists = [v.get("district_kn", k) for k, v in warnings.items() if v.get("level") == "orange"]
        yellow_dists = [v.get("district_kn", k) for k, v in warnings.items() if v.get("level") == "yellow"]
        green_dists = [v.get("district_kn", k) for k, v in warnings.items() if v.get("level") == "green" or not v.get("level")]

        if not red_dists and not orange_dists and not yellow_dists:
            alert_lines = (
                f"🟢 ಗ್ರೀನ್ ಜೋನ್ (Green Zone): ರಾಜ್ಯದ ಎಲ್ಲಾ {len(green_dists) or 31} ಜಿಲ್ಲೆಗಳಲ್ಲೂ ಶಾಂತ ಹವೆ & ಸಾಮಾನ್ಯ ವಾತಾವರಣ (ಯಾವುದೇ ಭಾರಿ ಮಳೆ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ).\n"
                f"🔴 ರೆಡ್ / 🟠 ಆರೆಂಜ್ / 🟡 ಯೆಲ್ಲೋ ಅಲರ್ಟ್: ಸದ್ಯ ರಾಜ್ಯದ ಯಾವುದೇ ಜಿಲ್ಲೆಗಳಿಗೂ ಇಲ್ಲ (0 ಜಿಲ್ಲೆ)."
            )
        else:
            parts = []
            if red_dists:
                parts.append(f"🔴 ರೆಡ್ ಅಲರ್ಟ್ ({len(red_dists)} ಜಿಲ್ಲೆ): {', '.join(red_dists[:5])}{'...' if len(red_dists) > 5 else ''}")
            if orange_dists:
                parts.append(f"🟠 ಆರೆಂಜ್ ಅಲರ್ಟ್ ({len(orange_dists)} ಜಿಲ್ಲೆ): {', '.join(orange_dists[:5])}{'...' if len(orange_dists) > 5 else ''}")
            if yellow_dists:
                parts.append(f"🟡 ಹಳದಿ ಎಚ್ಚರಿಕೆ ({len(yellow_dists)} ಜಿಲ್ಲೆ): {', '.join(yellow_dists[:6])}{'...' if len(yellow_dists) > 6 else ''}")
            if green_dists:
                parts.append(f"🟢 ಗ್ರೀನ್ ಜೋನ್ ({len(green_dists)} ಜಿಲ್ಲೆ): ಸಾಮಾನ್ಯ ತಿಳಿ ಹವೆ.")
            alert_lines = "\n".join(parts)
    except Exception as e:
        r_txt = "🌧️ 24H ಅಧಿಕೃತ ಲೈವ್ ಮಳೆ ದಾಖಲೆ"
        t_txt = "☀️ ಅಧಿಕೃತ ತಾಪಮಾನ ವಿವರ"
        alert_lines = "🟢 ಗ್ರೀನ್ ಜೋನ್ (Green Zone): ರಾಜ್ಯಾದ್ಯಂತ ಸಾಧಾರಣ ವಾತಾವರಣ."

    return f"""⛈️ ಕರ್ನಾಟಕ IMD ಲೈವ್ ನೌಕಾಸ್ಟ್ ಮಳೆ ಮುನ್ನೆಚ್ಚರಿಕೆ ({t_str} • {date_kn})

{r_txt}
{t_txt}

{alert_lines}

📡 ನಿಮ್ಮ ತಾಲೂಕು & ಗ್ರಾಮ ಪಂಚಾಯಿತಿಯ ನಿಖರ ಲೈವ್ ರೇಡಾರ್ ಮ್ಯಾಪ್:
🌐 https://karnata.in/weather
📲 Instagram ಬಯೋದಲ್ಲಿ (Bio Link) ನೇರ ಲಿಂಕ್ ಲಭ್ಯವಿದೆ: @karnata.in

#KarnatakaWeather #MonsoonAlert #IMDNowcast #KarnatakaRain #WeatherUpdate #KarnataIn #BangaloreRains #WeatherForecast"""


# ══════════════════════════════════════════════════════════════════════════════
# COMPLETE 16 SCHEDULED SLOTS (IST)
# ══════════════════════════════════════════════════════════════════════════════
SLOT_ALIASES = {
    "weather": "weather_summary",
    "quiz": "quiz_1",
    "useful_info": "doyouknow_1",
    "doyouknow": "doyouknow_1",
    "nowcast": "weather_nowcast_1",
    "fuel": "petrol_diesel",
    "gold": "gold_rate",
    "dams": "dam_levels",
    "apmc": "apmc_rates"
}

def resolve_slot_key(slot_key):
    if not slot_key:
        return slot_key
    key = slot_key.strip().lower()
    return SLOT_ALIASES.get(key, key)

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
def get_local_path(img_url):
    fn = img_url.split("/")[-1].split("?")[0]
    p = ROOT_DIR / "assets" / "social-cards" / fn
    return p if p.exists() else None

def sync_card_to_edge(img_url):
    """Uploads local image to Cloudflare Edge KV endpoint so Instagram gets fresh image without cache."""
    try:
        fn = img_url.split("/")[-1].split("?")[0]
        local_p = get_local_path(img_url)
        if local_p:
            edge_upload_url = f"https://karnata.in/api/social-card?name={fn}&key=karnata_social_2026"
            with open(local_p, "rb") as f:
                r = requests.post(edge_upload_url, data=f.read(), timeout=15)
                if r.ok:
                    d = r.json()
                    return d.get("url", f"https://karnata.in/api/social-card?name={fn}&v={int(time.time())}")
    except Exception as e:
        print("  [Notice] Edge sync note:", e)
    return img_url + f"?v={int(time.time())}"

def post_to_facebook(image_urls, caption):
    if not FB_PAGE_ID or not META_ACCESS_TOKEN:
        print("⚠️ Facebook credentials missing.")
        return False

    try:
        if len(image_urls) == 1:
            url = f"https://graph.facebook.com/v21.0/{FB_PAGE_ID}/photos"
            local_p = get_local_path(image_urls[0])
            if local_p:
                print(f"  📤 Direct uploading local file {local_p.name} to Facebook...")
                with open(local_p, "rb") as img_file:
                    resp = requests.post(url, files={"source": img_file}, data={"caption": caption, "access_token": META_ACCESS_TOKEN})
            else:
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
                local_p = get_local_path(img_url)
                if local_p:
                    with open(local_p, "rb") as img_file:
                        up_resp = requests.post(up_url, files={"source": img_file}, data={"published": "false", "access_token": META_ACCESS_TOKEN})
                else:
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
        fresh_urls = [sync_card_to_edge(u) for u in image_urls]
        if len(fresh_urls) == 1:
            c_url = f"https://graph.facebook.com/v21.0/{IG_USER_ID}/media"
            c_resp = requests.post(c_url, data={"image_url": fresh_urls[0], "caption": caption, "access_token": META_ACCESS_TOKEN})
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
            for img_url in fresh_urls:
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

def ensure_graphic_rendered(slot_key):
    try:
        from scripts.generate_daily_social_graphics import (
            render_quote_card, render_petrol_card, render_weather_morning_summary,
            render_apmc_carousel, render_dam_carousel_and_spotlights,
            render_gold_card, render_nowcast_map_card, render_quiz_interactive_card,
            render_doyouknow_card
        )
        fn_map = {
            "quote": render_quote_card,
            "petrol_diesel": render_petrol_card,
            "weather_summary": render_weather_morning_summary,
            "apmc_rates": render_apmc_carousel,
            "dam_levels": render_dam_carousel_and_spotlights,
            "gold_rate": render_gold_card,
            "weather_nowcast_1": render_nowcast_map_card,
            "quiz_1": lambda: render_quiz_interactive_card(1),
            "doyouknow_1": lambda: render_doyouknow_card(1),
            "weather_nowcast_2": render_nowcast_map_card,
            "quiz_2": lambda: render_quiz_interactive_card(2),
            "doyouknow_2": lambda: render_doyouknow_card(2),
            "weather_nowcast_3": render_nowcast_map_card,
            "quiz_3": lambda: render_quiz_interactive_card(3),
            "weather_nowcast_4": render_nowcast_map_card,
            "doyouknow_3": lambda: render_doyouknow_card(3),
        }
        if slot_key in fn_map:
            print(f"  🎨 Freshly rendering graphic for {slot_key}...")
            fn_map[slot_key]()
    except Exception as e:
        print("  [Notice] Render notice:", e)

def ensure_graphic_freshness(slot_key):
    try:
        from scripts.generate_daily_social_graphics import (
            render_quote_card, render_petrol_card, render_weather_morning_summary,
            render_apmc_carousel, render_dam_carousel_and_spotlights,
            render_gold_card, render_nowcast_map_card, render_quiz_interactive_card,
            render_doyouknow_card
        )
        fn_map = {
            "quote": render_quote_card,
            "petrol_diesel": render_petrol_card,
            "weather_summary": render_weather_morning_summary,
            "apmc_rates": render_apmc_carousel,
            "dam_levels": render_dam_carousel_and_spotlights,
            "gold_rate": render_gold_card,
            "weather_nowcast_1": render_nowcast_map_card,
            "quiz_1": lambda: render_quiz_interactive_card(1),
            "doyouknow_1": lambda: render_doyouknow_card(1),
            "weather_nowcast_2": render_nowcast_map_card,
            "quiz_2": lambda: render_quiz_interactive_card(2),
            "doyouknow_2": lambda: render_doyouknow_card(2),
            "weather_nowcast_3": render_nowcast_map_card,
            "quiz_3": lambda: render_quiz_interactive_card(3),
            "weather_nowcast_4": render_nowcast_map_card,
            "doyouknow_3": lambda: render_doyouknow_card(3),
        }
        if slot_key in fn_map:
            print(f"  🎨 Generating / refreshing fresh graphic for {slot_key}...")
            fn_map[slot_key]()
    except Exception as e:
        print(f"  [Notice] Graphic generator notice for {slot_key}:", e)

def publish_card(slot_key, dry_run=False):
    slot_key = resolve_slot_key(slot_key)
    ensure_graphic_freshness(slot_key)
    if slot_key not in SCHEDULED_CARDS:
        print(f"❌ Unknown slot: {slot_key}. Valid: {list(SCHEDULED_CARDS.keys())}")
        return False

    ensure_graphic_rendered(slot_key)
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
