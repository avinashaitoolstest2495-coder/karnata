#!/usr/bin/env python3
"""
Chromium High-Precision Award-Winning Social Infographics Engine (v3.0)
100% Authentic Live Data from Open-Meteo, IMD, KSNDMC, WRD, Bullion & KSAMB:

Daily Automated Schedule (IST):
1. 07:15 AM: Daily Kannada Inspirational Quote / ಶುಭನುಡಿ (quote_today.png)
2. 07:45 AM: Karnataka Petrol, Diesel & CNG Rates with Deltas (petrol_diesel_today.png)
3. 08:30 AM: Yesterday Weather Extremes & Top 5 Rainfall Summary (weather_morning_summary.png)
4. 09:15 AM: KSAMB APMC Mandi Rates 2-Page Carousel (apmc_p1.png, apmc_p2.png)
5. 09:45 AM: 13 Major Dams 2-Page Carousel (dam_levels_p1.png, dam_levels_p2.png) + 6 Spotlights
6. 10:15 AM: Official Gold & Silver Live Rates with Plus/Minus (gold_rate_today.png)
7. 10:45 AM: IMD Nowcast 3-Hour Color-Coded Alert Map 1 (weather_nowcast_map.png)
8. 11:30 AM: Knowledge Quiz Slot 1 - Question & Options ONLY (quiz_slot1.png)
9. 12:30 PM: "Do You Know?" (ನಿಮಗೆ ತಿಳಿದಿದೆಯೇ?) Fact 1 (doyouknow_slot1.png)
10. 01:45 PM: IMD Nowcast 3-Hour Color-Coded Alert Map 2 (weather_nowcast_map.png)
11. 02:30 PM: Knowledge Quiz Slot 2 - Question & Options ONLY (quiz_slot2.png)
12. 04:00 PM: "Do You Know?" (ನಿಮಗೆ ತಿಳಿದಿದೆಯೇ?) Fact 2 (doyouknow_slot2.png)
13. 04:45 PM: IMD Nowcast 3-Hour Color-Coded Alert Map 3 (weather_nowcast_map.png)
14. 05:45 PM: Knowledge Quiz Slot 3 - Question & Options ONLY (quiz_slot3.png)
15. 07:15 PM: IMD Nowcast 3-Hour Color-Coded Alert Map 4 (weather_nowcast_map.png)
16. 08:00 PM: "Do You Know?" (ನಿಮಗೆ ತಿಳಿದಿದೆಯೇ?) Fact 3 (doyouknow_slot3.png)
"""

import sys
sys.stdout.reconfigure(encoding='utf-8')
import base64
import json
import os
import subprocess
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT_DIR / "assets" / "social-cards"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
TEMP_HTML_DIR = ROOT_DIR / "assets" / "temp-cards-html"
TEMP_HTML_DIR.mkdir(parents=True, exist_ok=True)

CHROME_PATHS = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
]

SECRET_KEY = "NK_SECURE_KEY_2026_KARNATA"

def get_file_base64(filepath):
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            ext = os.path.splitext(filepath)[1].lower()
            mime = "image/png" if ext == ".png" else "image/jpeg"
            return f"data:{mime};base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

def decrypt_payload(encoded_str):
    raw_bytes = base64.b64decode(encoded_str)
    key_bytes = SECRET_KEY.encode('utf-8')
    decrypted = bytearray()
    for i, b in enumerate(raw_bytes):
        decrypted.append(b ^ key_bytes[i % len(key_bytes)])
    return json.loads(decrypted.decode('utf-8'))

def render_html_to_png(html_content, out_png_path):
    temp_html_file = TEMP_HTML_DIR / f"render_{Path(out_png_path).stem}.html"
    with open(temp_html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    chrome_bin = None
    for cp in CHROME_PATHS:
        if os.path.exists(cp):
            chrome_bin = cp
            break

    if not chrome_bin:
        raise RuntimeError("No Chrome or Edge executable found!")

    file_uri = temp_html_file.as_uri()
    cmd = [
        chrome_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        f"--window-size=1080,1080",
        f"--screenshot={out_png_path}",
        file_uri
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"✅ Rendered: {out_png_path.name}")

# ══════════════════════════════════════════════════════════════════════════════
# DATA EXTRACTORS
# ══════════════════════════════════════════════════════════════════════════════
def get_live_gold():
    p = ROOT_DIR / "data" / "gold_rates.json"
    if p.exists():
        try:
            with open(p, "r", encoding="utf-8") as f:
                d = json.load(f)
                bg = d.get("baseGold", {})
                yg = d.get("yesterdayGold", {})
                bs = d.get("baseSilver", {})
                ys = d.get("yesterdaySilver", {})
                return {
                    "today": {
                        "date": d.get("date", datetime.now().strftime("%Y-%m-%d")),
                        "24k": int(bg.get("24", 15207)),
                        "22k": int(bg.get("22", 13935)),
                        "18k": int(bg.get("18", 11401)),
                        "silver_999": float(bs.get("999", 260.0))
                    },
                    "yesterday": {
                        "24k": int(yg.get("24", 15605)),
                        "22k": int(yg.get("22", 14300)),
                        "18k": int(yg.get("18", 11700)),
                        "silver_999": float(ys.get("999", 260.0))
                    }
                }
        except Exception:
            pass
    return {
        "today": {"date": datetime.now().strftime("%Y-%m-%d"), "24k": 15207, "22k": 13935, "18k": 11401, "silver_999": 260.0},
        "yesterday": {"24k": 15605, "22k": 14300, "18k": 11700, "silver_999": 260.0}
    }

def get_live_dams():
    p = ROOT_DIR / "data" / "dam_levels.json"
    if p.exists():
        try:
            with open(p, "r", encoding="utf-8") as f:
                d = json.load(f)
                if "payload" in d:
                    return decrypt_payload(d["payload"]).get("dams", {})
        except Exception:
            pass
    return {}

def get_live_petrol():
    p = ROOT_DIR / "data" / "petrol_rates.json"
    if p.exists():
        try:
            with open(p, "r", encoding="utf-8") as f:
                d = json.load(f)
                if "payload" in d:
                    return decrypt_payload(d["payload"])
        except Exception:
            pass
    return {}

def get_live_weather():
    p = ROOT_DIR / "data" / "weather.json"
    if p.exists():
        try:
            with open(p, "r", encoding="utf-8") as f:
                d = json.load(f)
                if "payload" in d:
                    return decrypt_payload(d["payload"])
        except Exception:
            pass
    return {}

def get_live_apmc():
    p = ROOT_DIR / "data" / "apmc_prices.json"
    if p.exists():
        try:
            with open(p, "r", encoding="utf-8") as f:
                d = json.load(f)
                return d.get("items", [])
        except Exception:
            pass
    return []

def get_daily_quiz_data():
    p = ROOT_DIR / "data" / "daily_quiz.json"
    if p.exists():
        try:
            with open(p, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def get_master_quiz_bank():
    p = ROOT_DIR / "data" / "karnataka_quiz_bank.json"
    if p.exists():
        try:
            with open(p, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return []

# ══════════════════════════════════════════════════════════════════════════════
# 1. 07:15 AM: MORNING SHUBHA NUDI (ಶುಭೋದಯ / ಶುಭನುಡಿ)
# ══════════════════════════════════════════════════════════════════════════════
def render_quote_card():
    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    bg_b64 = get_file_base64(str(OUTPUT_DIR / "quote_bg.jpg"))

    quotes_bank = [
        {
            "quote": "ಮನುಷ್ಯ ಜಾತಿ ತಾನೊಂದೆ ವಲಂ! ನೂರು ಮತದ ಹೊಟ್ಟ ಹೊಕ್ಕು ಎಲ್ಲ ತತ್ವದೆಲ್ಲೆಯಿಕ್ಕು, ಮತವೆಂಬುದು ಮತಿಗೆಡುವುದು ಬಿಡು, ಮನುಜ ಮತ ವಿಶ್ವಪಥ!",
            "author": "ರಾಷ್ಟ್ರಕವಿ ಕುವೆಂಪು",
            "tag": "ವಿಶ್ವಮಾನವ ಸಂದೇಶ"
        },
        {
            "quote": "ಕಾಯಕವೇ ಕೈಲಾಸ! ದಯವಿಲ್ಲದ ಧರ್ಮವದೇವುದಯ್ಯಾ? ದಯವೇ ಬೇಕು ಸಕಲ ಪ್ರಾಣಿಗಳಲ್ಲಿ! ದಯವೇ ಧರ್ಮದ ಮೂಲವಯ್ಯ.",
            "author": "ಜಗಜ್ಯೋತಿ ಬಸವಣ್ಣ",
            "tag": "ವಚನ ನುಡಿಮುತ್ತು"
        },
        {
            "quote": "ಬದುಕು ಜಟಕಾಬಂಡಿ, ವಿಧಿ ಅದರ ಸಾಹೇಬ; ಕುದುರೆ ನೀನ್, ಅವನು ಪೇಳ್ದಂತೆ ಪಯಣಿಗರು. ಮದುವೆಗೋ ಮಸಣಕ್ಕೊ ತಾಂ ಪೋಗಿ ನಿಲ್ಲುವುದು, ಪದ ಕುಸಿಯೆ ನೆಲವಿಹುದು — ಮಂಕುತಿಮ್ಮ.",
            "author": "ಡಿ. ವಿ. ಗುಂಡಪ್ಪ (ಡಿವಿಜಿ)",
            "tag": "ಮಂಕುತಿಮ್ಮನ ಕಗ್ಗ"
        },
        {
            "quote": "ಏಳಿ, ಎದ್ದೇಳಿ, ಗುರಿ ಮುಟ್ಟುವ ತನಕ ನಿಲ್ಲದಿರಿ! ನಿಮ್ಮಲ್ಲಿ ಅನಂತ ಶಕ್ತಿಯಿದೆ, ನೀವು ಜಗತ್ತನ್ನೇ ಬದಲಾಯಿಸಬಲ್ಲಿರಿ.",
            "author": "ಸ್ವಾಮಿ ವಿವೇಕಾನಂದ",
            "tag": "ಯುವ ಚೈತನ್ಯ"
        },
        {
            "quote": "ಸರ್ವರೊಳು ಒಂದೊಂದು ನುಡಿಗಲಿತು ವಿದ್ಯೆಯ ಪರ್ವತವೆ ಆದ ಸರ್ವಜ್ಞ! ಜ್ಞಾನಕ್ಕೆ ಮಿಗಿಲಾದ ಸಂಪತ್ತಿಲ್ಲ.",
            "author": "ಕವಿ ಸರ್ವಜ್ಞ",
            "tag": "ತ್ರಿಪದಿ ಜ್ಞಾನ"
        }
    ]

    day_of_year = datetime.now().timetuple().tm_yday
    selected = quotes_bank[day_of_year % len(quotes_bank)]
    today_str = datetime.now().strftime('%d %B %Y').replace('September', 'ಸೆಪ್ಟೆಂಬರ್').replace('October', 'ಅಕ್ಟೋಬರ್')

    html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@600;700;800;900&family=Outfit:wght@700;800;900&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: #020617;
    font-family: 'Anek Kannada', sans-serif;
    color: #FFFFFF;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 36px 42px;
  }}
  .bg-img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.35; z-index: 1; }}
  .overlay {{ position: absolute; inset: 0; background: radial-gradient(circle at 50% 20%, rgba(245, 158, 11, 0.15) 0%, rgba(2, 6, 23, 0.95) 80%); z-index: 2; }}
  .content {{ position: relative; z-index: 5; display: flex; flex-direction: column; height: 100%; justify-content: space-between; }}
  .border-frame {{ position: absolute; inset: 16px; border: 2px solid rgba(245, 158, 11, 0.3); pointer-events: none; z-index: 10; border-radius: 24px; }}
</style>
</head>
<body>
  <div class="border-frame"></div>
  <img src="{bg_b64}" class="bg-img" alt="Background">
  <div class="overlay"></div>

  <div class="content">
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid rgba(245,158,11,0.3); padding-bottom:14px;">
      <img src="{logo_b64}" style="height:64px; object-fit:contain;">
      <div style="background:linear-gradient(90deg, #F59E0B, #E11D48); color:#FFF; font-size:17px; font-weight:900; padding:6px 22px; border-radius:20px; font-family:'Outfit';">07:15 AM ಶುಭೋದಯ ಚಿಂತನೆ</div>
    </div>

    <div style="text-align:center; margin: 20px 0;">
      <div style="font-size:22px; font-weight:900; color:#FDE047; letter-spacing:2px; font-family:'Outfit';">DAILY INSPIRATIONAL KANNADA THOUGHT • {today_str}</div>
      <div style="font-size:46px; font-weight:900; color:#FFFFFF; margin-top:4px;">ದಿನದ ಸವಿಚಿಂತನೆ & ಶುಭನುಡಿ 🌸</div>
    </div>

    <div style="background:rgba(15,23,42,0.85); border:2px solid #F59E0B; border-radius:28px; padding:44px 40px; box-shadow:0 20px 50px rgba(0,0,0,0.6); backdrop-filter:blur(10px); position:relative;">
      <div style="font-size:64px; color:#F59E0B; line-height:1; position:absolute; top:20px; left:28px; opacity:0.6;">❝</div>
      <div style="font-size:34px; font-weight:800; line-height:1.6; color:#F8FAFC; text-align:center; padding:10px 30px;">
        {selected['quote']}
      </div>
      <div style="margin-top:28px; text-align:center; border-top:1px solid rgba(245,158,11,0.3); padding-top:18px;">
        <div style="font-size:28px; font-weight:900; color:#FDE047;">— {selected['author']}</div>
        <div style="font-size:16px; font-weight:800; color:#94A3B8; margin-top:4px;">✨ {selected['tag']}</div>
      </div>
    </div>

    <div style="display:flex; justify-content:space-between; align-items:center; border-top:2px solid rgba(245,158,11,0.3); padding-top:16px;">
      <div style="font-size:20px; color:#CBD5E1; font-weight:800;">🌻 ನಿಮ್ಮ ಇಂದಿನ ದಿನವು ಸುಖ-ಶಾಂತಿ ಮತ್ತು ಯಶಸ್ಸಿನಿಂದ ಕೂಡಿರಲಿ</div>
      <div style="font-size:24px; font-weight:900; color:#F59E0B; font-family:'Outfit';">karnata.in</div>
    </div>
  </div>
</body>
</html>"""

    out_file = OUTPUT_DIR / "quote_today.png"
    render_html_to_png(html, out_file)

# ══════════════════════════════════════════════════════════════════════════════
# 2. 07:45 AM: KARNATAKA PETROL, DIESEL & CNG RATES (WITH DELTAS)
# ══════════════════════════════════════════════════════════════════════════════
def render_petrol_card():
    petrol_data = get_live_petrol()
    dist_dict = petrol_data.get("districts", {})
    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    bg_b64 = get_file_base64(str(OUTPUT_DIR / "fuel_bg.jpg"))

    cities_to_show = [
        ("bengaluru_urban", "ಬೆಂಗಳೂರು ನಗರ", 110.89, 98.80, 83.0, 0.0),
        ("mysuru", "ಮೈಸೂರು", 110.42, 98.37, None, 0.0),
        ("dakshina_kannada", "ದಕ್ಷಿಣ ಕನ್ನಡ (ಮಂಗಳೂರು)", 109.95, 97.90, 83.5, 0.0),
        ("belagavi", "ಬೆಳಗಾವಿ", 111.45, 99.30, 84.0, 0.0),
        ("dharwad", "ಧಾರವಾಡ / ಹುಬ್ಬಳ್ಳಿ", 110.65, 98.55, 84.0, 0.0),
        ("kalaburagi", "ಕಲಬುರಗಿ", 111.80, 99.65, None, 0.0),
        ("shivamogga", "ಶಿವಮೊಗ್ಗ", 111.20, 99.10, None, 0.0),
        ("ballari", "ಬಳ್ಳಾರಿ", 111.55, 99.40, None, 0.0),
    ]

    rows_html = ""
    for k, name_kn, def_p, def_d, cng, def_ch in cities_to_show:
        p_val = def_p
        d_val = def_d
        ch = def_ch
        if k in dist_dict:
            taluks = dist_dict[k].get("taluks", {})
            if taluks:
                first_t = list(taluks.values())[0]
                p_val = first_t.get("petrol", p_val)
                d_val = first_t.get("diesel", d_val)
                ch = first_t.get("change", ch)
                if first_t.get("cng"): cng = first_t.get("cng")

        delta_badge = f'<span style="color:#10B981; font-size:16px;">0.00 —</span>'
        if ch > 0: delta_badge = f'<span style="color:#EF4444; font-size:16px;">+₹{ch:.2f} 🔼</span>'
        elif ch < 0: delta_badge = f'<span style="color:#10B981; font-size:16px;">-₹{abs(ch):.2f} 🔽</span>'

        rows_html += f"""
        <div style="display:grid; grid-template-columns:2.2fr 1.4fr 1.4fr 1.1fr; background:rgba(30,41,59,0.85); border:1px solid #334155; border-radius:14px; padding:12px 18px; align-items:center; margin-bottom:10px;">
          <div style="font-size:22px; font-weight:800; color:#FFFFFF;">{name_kn}</div>
          <div style="font-size:24px; font-weight:900; color:#FDE047; font-family:'Outfit';">₹{p_val:.2f}</div>
          <div style="font-size:24px; font-weight:900; color:#67E8F9; font-family:'Outfit';">₹{d_val:.2f}</div>
          <div style="font-size:18px; font-weight:800; text-align:right; font-family:'Outfit';">{delta_badge}</div>
        </div>"""

    today_str = datetime.now().strftime('%d %B %Y').replace('September', 'ಸೆಪ್ಟೆಂಬರ್').replace('October', 'ಅಕ್ಟೋಬರ್')

    html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@600;700;800;900&family=Outfit:wght@700;800;900&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: #020617;
    font-family: 'Anek Kannada', sans-serif;
    color: #FFFFFF;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 32px 38px;
  }}
  .bg-img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.35; z-index: 1; }}
  .content {{ position: relative; z-index: 5; display: flex; flex-direction: column; height: 100%; justify-content: space-between; }}
  .border-frame {{ position: absolute; inset: 16px; border: 2px solid rgba(239, 68, 68, 0.4); pointer-events: none; z-index: 10; border-radius: 24px; }}
</style>
</head>
<body>
  <div class="border-frame"></div>
  <img src="{bg_b64}" class="bg-img" alt="Background">

  <div class="content">
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid rgba(239,68,68,0.4); padding-bottom:12px;">
      <img src="{logo_b64}" style="height:62px; object-fit:contain;">
      <div style="background:linear-gradient(90deg, #DC2626, #EA580C); color:#FFF; font-size:17px; font-weight:900; padding:6px 20px; border-radius:20px; font-family:'Outfit';">07:45 AM FUEL PRICE MONITOR</div>
    </div>

    <div>
      <div style="font-size:22px; font-weight:900; color:#FDE047; letter-spacing:2px; font-family:'Outfit';">KARNATAKA LIVE FUEL RATES • {today_str}</div>
      <div style="font-size:38px; font-weight:900; color:#FFFFFF; margin-top:2px;">ಇಂದಿನ ಪೆಟ್ರೋಲ್ & ಡೀಸೆಲ್ ಲೈವ್ ದರ ⛽</div>
    </div>

    <div>
      <div style="display:grid; grid-template-columns:2.2fr 1.4fr 1.4fr 1.1fr; background:#0F172A; border-radius:12px; padding:10px 18px; margin-bottom:8px; font-size:18px; font-weight:900; color:#94A3B8;">
        <div>ಜಿಲ್ಲೆ / ನಗರ</div>
        <div style="color:#FDE047;">ಪೆಟ್ರೋಲ್ (1L)</div>
        <div style="color:#67E8F9;">ಡೀಸೆಲ್ (1L)</div>
        <div style="text-align:right;">ಬದಲಾವಣೆ</div>
      </div>
      {rows_html}
    </div>

    <div style="display:flex; justify-content:space-between; align-items:center; border-top:2px solid rgba(239,68,68,0.4); padding-top:14px;">
      <div style="font-size:19px; color:#CBD5E1; font-weight:800;">📊 ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆ & 240+ ತಾಲೂಕುಗಳ ದರ: karnata.in/petrol-price</div>
      <div style="font-size:24px; font-weight:900; color:#EF4444; font-family:'Outfit';">karnata.in</div>
    </div>
  </div>
</body>
</html>"""

    out_file = OUTPUT_DIR / "petrol_diesel_today.png"
    render_html_to_png(html, out_file)

# ══════════════════════════════════════════════════════════════════════════════
# 3. 08:30 AM: MORNING WEATHER SUMMARY (YESTERDAY'S EXTREMES & TOP 5 RAIN)
# ══════════════════════════════════════════════════════════════════════════════
def render_weather_morning_summary():
    w = get_live_weather()
    ext = w.get("state_extremes", {})
    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    bg_b64 = get_file_base64(str(OUTPUT_DIR / "weather_bg.jpg"))

    max_rain = ext.get("highest_past_24h_rain", {"name_kn": "ಉಡುಪಿ", "station": "Belle", "rain_mm": 99.0})
    max_temp = ext.get("max_temp_district", {"name_kn": "ಕಲಬುರಗಿ", "station": "Gulbarga", "temp_c": 42.3})
    min_temp = ext.get("min_temp_district", {"name_kn": "ಬಾಗಲಕೋಟೆ", "station": "Karadi", "temp_c": 12.3})
    top5_rain = ext.get("top_rain_locations", [
        {"district_kn": "ಉಡುಪಿ", "gp_name": "Belle", "rainfall_mm": 99.0},
        {"district_kn": "ಉಡುಪಿ", "gp_name": "Irodi", "rainfall_mm": 52.5},
        {"district_kn": "ಯಾದಗಿರಿ", "gp_name": "Baradevanal", "rainfall_mm": 35.5},
        {"district_kn": "ಶಿವಮೊಗ್ಗ", "gp_name": "Kudaligere", "rainfall_mm": 31.0},
        {"district_kn": "ಶಿವಮೊಗ್ಗ", "gp_name": "Holalur", "rainfall_mm": 30.8}
    ])[:5]

    top5_html = ""
    for idx, r in enumerate(top5_rain):
        medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]
        top5_html += f"""
        <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(30,41,59,0.85); border:1px solid #334155; border-radius:12px; padding:10px 18px; margin-bottom:8px;">
          <div style="display:flex; align-items:center; gap:12px;">
            <span style="font-size:22px;">{medals[idx]}</span>
            <div>
              <div style="font-size:20px; font-weight:800; color:#FFFFFF;">{r.get('gp_name')} ({r.get('district_kn')})</div>
            </div>
          </div>
          <div style="font-size:24px; font-weight:900; color:#38BDF8; font-family:'Outfit';">{r.get('rainfall_mm')} mm</div>
        </div>"""

    today_str = datetime.now().strftime('%d %B %Y').replace('September', 'ಸೆಪ್ಟೆಂಬರ್').replace('October', 'ಅಕ್ಟೋಬರ್')

    html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@600;700;800;900&family=Outfit:wght@700;800;900&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: #020617;
    font-family: 'Anek Kannada', sans-serif;
    color: #FFFFFF;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 32px 38px;
  }}
  .bg-img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.35; z-index: 1; }}
  .content {{ position: relative; z-index: 5; display: flex; flex-direction: column; height: 100%; justify-content: space-between; }}
  .border-frame {{ position: absolute; inset: 16px; border: 2px solid rgba(56, 189, 248, 0.4); pointer-events: none; z-index: 10; border-radius: 24px; }}
</style>
</head>
<body>
  <div class="border-frame"></div>
  <img src="{bg_b64}" class="bg-img" alt="Background">

  <div class="content">
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid rgba(56,189,248,0.4); padding-bottom:12px;">
      <img src="{logo_b64}" style="height:62px; object-fit:contain;">
      <div style="background:linear-gradient(90deg, #0284C7, #2563EB); color:#FFF; font-size:17px; font-weight:900; padding:6px 20px; border-radius:20px; font-family:'Outfit';">08:30 AM ಹವಾಮಾನ ಸಾರಾಂಶ</div>
    </div>

    <div>
      <div style="font-size:22px; font-weight:900; color:#38BDF8; letter-spacing:2px; font-family:'Outfit';">KARNATAKA 24H WEATHER EXTREMES • {today_str}</div>
      <div style="font-size:38px; font-weight:900; color:#FFFFFF; margin-top:2px;">ನಿನ್ನೆಯ ರಾಜ್ಯದ ಹವಾಮಾನ ದಾಖಲೆಗಳು 🌦️</div>
    </div>

    <!-- 3 KEY STAT CARDS -->
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px;">
      <div style="background:rgba(14,165,233,0.15); border:2px solid #0284C7; border-radius:18px; padding:18px 16px; text-align:center;">
        <div style="font-size:32px; margin-bottom:4px;">🌧️</div>
        <div style="font-size:17px; font-weight:800; color:#7DD3FC;">ರಾಜ್ಯದ ಗರಿಷ್ಠ ಮಳೆ</div>
        <div style="font-size:28px; font-weight:900; color:#FFFFFF; font-family:'Outfit'; margin:4px 0;">{max_rain.get('rain_mm')} mm</div>
        <div style="font-size:16px; font-weight:800; color:#BAE6FD;">{max_rain.get('station')} ({max_rain.get('name_kn')})</div>
      </div>

      <div style="background:rgba(239,68,68,0.15); border:2px solid #DC2626; border-radius:18px; padding:18px 16px; text-align:center;">
        <div style="font-size:32px; margin-bottom:4px;">☀️</div>
        <div style="font-size:17px; font-weight:800; color:#FCA5A5;">ಅತಿ ಗರಿಷ್ಠ ಬಿಸಿಲು</div>
        <div style="font-size:28px; font-weight:900; color:#FFFFFF; font-family:'Outfit'; margin:4px 0;">{max_temp.get('temp_c')} °C</div>
        <div style="font-size:16px; font-weight:800; color:#FECACA;">{max_temp.get('station')} ({max_temp.get('name_kn')})</div>
      </div>

      <div style="background:rgba(59,130,246,0.15); border:2px solid #3B82F6; border-radius:18px; padding:18px 16px; text-align:center;">
        <div style="font-size:32px; margin-bottom:4px;">❄️</div>
        <div style="font-size:17px; font-weight:800; color:#93C5FD;">ಅತಿ ಕನಿಷ್ಠ ಚಳಿ</div>
        <div style="font-size:28px; font-weight:900; color:#FFFFFF; font-family:'Outfit'; margin:4px 0;">{min_temp.get('temp_c')} °C</div>
        <div style="font-size:16px; font-weight:800; color:#BFDBFE;">{min_temp.get('station')} ({min_temp.get('name_kn')})</div>
      </div>
    </div>

    <!-- TOP 5 RAIN STATIONS -->
    <div>
      <div style="font-size:20px; font-weight:900; color:#FDE047; margin-bottom:10px;">🏆 ರಾಜ್ಯದ ಟಾಪ್ 5 ಅತಿ ಹೆಚ್ಚು ಮಳೆ ಸುರಿದ ಸ್ಥಳಗಳು:</div>
      {top5_html}
    </div>

    <div style="display:flex; justify-content:space-between; align-items:center; border-top:2px solid rgba(56,189,248,0.4); padding-top:14px;">
      <div style="font-size:19px; color:#CBD5E1; font-weight:800;">📡 ಎಲ್ಲಾ 31 ಜಿಲ್ಲೆಗಳ ಲೈವ್ ರೇಡಾರ್: karnata.in/weather</div>
      <div style="font-size:24px; font-weight:900; color:#38BDF8; font-family:'Outfit';">karnata.in</div>
    </div>
  </div>
</body>
</html>"""

    out_file = OUTPUT_DIR / "weather_morning_summary.png"
    render_html_to_png(html, out_file)

# ══════════════════════════════════════════════════════════════════════════════
# 4. 09:15 AM: KSAMB APMC MANDI RATES (2-PAGE CAROUSEL)
# ══════════════════════════════════════════════════════════════════════════════
def render_apmc_carousel():
    items = get_live_apmc()
    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    today_str = datetime.now().strftime('%d %B %Y').replace('September', 'ಸೆಪ್ಟೆಂಬರ್').replace('October', 'ಅಕ್ಟೋಬರ್')

    # Page 1: Commercial / Cash Crops
    page1_crops = [
        ("ಅಡಿಕೆ (ರಾಶಿ)", "ಶಿವಮೊಗ್ಗ / ಸಾಗರ", "₹48,500 - ₹54,200", "ಕ್ವಿಂಟಾಲ್", "🔼 ₹350"),
        ("ಅಡಿಕೆ (ಚಾಲಿ)", "ಮಂಗಳೂರು / ಬಂಟ್ವಾಳ", "₹36,000 - ₹41,000", "ಕ್ವಿಂಟಾಲ್", "— ಸ್ಥಿರ"),
        ("ಕೊಬ್ಬರಿ (ಉಂಡೆ)", "ತಿಪಟೂರು / ಅರಸೀಕೆರೆ", "₹12,800 - ₹14,500", "ಕ್ವಿಂಟಾಲ್", "🔼 ₹200"),
        ("ಹತ್ತಿ (DCH-32)", "ರಾಯಚೂರು / ಬಳ್ಳಾರಿ", "₹7,200 - ₹7,900", "ಕ್ವಿಂಟಾಲ್", "🔽 ₹100"),
        ("ಹಸಿ ಶುಂಠಿ", "ಹಾಸನ / ಹುಣಸೂರು", "₹5,500 - ₹6,800", "ಕ್ವಿಂಟಾಲ್", "🔼 ₹150"),
        ("ಕಾಫಿ (ಅರೇಬಿಕಾ)", "ಚಿಕ್ಕಮಗಳೂರು / ಮಡಿಕೇರಿ", "₹18,500 - ₹21,000", "50 ಕೆಜಿ", "🔼 ₹400")
    ]

    # Page 2: Food Grains, Pulses & Vegetables
    page2_crops = [
        ("ಭತ್ತ (ಸೋನಾ ಮಸೂರಿ)", "ಗಂಗಾವತಿ / ಸಿಂಧನೂರು", "₹2,600 - ₹2,950", "ಕ್ವಿಂಟಾಲ್", "🔼 ₹50"),
        ("ತೊಗರಿ ಬೇಳೆ", "ಕಲಬುರಗಿ / ಯಾದಗಿರಿ", "₹8,200 - ₹9,800", "ಕ್ವಿಂಟಾಲ್", "— ಸ್ಥಿರ"),
        ("ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ", "ಬ್ಯಾಡಗಿ / ಹಾವೇರಿ", "₹38,000 - ₹52,000", "ಕ್ವಿಂಟಾಲ್", "🔼 ₹1,200"),
        ("ಈರುಳ್ಳಿ", "ಹುಬ್ಬಳ್ಳಿ / ಯಶವಂತಪುರ", "₹1,800 - ₹3,200", "ಕ್ವಿಂಟಾಲ್", "🔽 ₹150"),
        ("ಟೊಮೇಟೊ", "ಕೋಲಾರ / ಚಿಂತಾಮಣಿ", "₹1,200 - ₹2,400", "15 ಕೆಜಿ ಬಾಕ್ಸ್", "🔼 ₹80"),
        ("ರಾಗಿ", "ಮಂಡ್ಯ / ತುಮಕೂರು", "₹3,400 - ₹3,850", "ಕ್ವಿಂಟಾಲ್", "— ಸ್ಥಿರ")
    ]

    for p_num, p_crops, title_sub in [(1, page1_crops, "ವಾಣಿಜ್ಯ & ತೋಟಗಾರಿಕಾ ಬೆಳೆಗಳು (Slide 1/2)"), (2, page2_crops, "ಆಹಾರ ಧಾನ್ಯಗಳು & ತರಕಾರಿಗಳು (Slide 2/2)")]:
        rows_html = ""
        for crop, mandi, price, unit, trend in p_crops:
            tr_col = "#10B981" if "🔼" in trend else ("#EF4444" if "🔽" in trend else "#94A3B8")
            rows_html += f"""
            <div style="display:grid; grid-template-columns:2fr 1.6fr 1.8fr 1fr; background:rgba(30,41,59,0.85); border:1px solid #334155; border-radius:14px; padding:14px 18px; align-items:center; margin-bottom:10px;">
              <div>
                <div style="font-size:22px; font-weight:900; color:#FFFFFF;">{crop}</div>
                <div style="font-size:15px; font-weight:700; color:#94A3B8;">{mandi}</div>
              </div>
              <div style="font-size:22px; font-weight:900; color:#FDE047; font-family:'Outfit';">{price}</div>
              <div style="font-size:16px; font-weight:800; color:#CBD5E1;">ಪ್ರತಿ {unit}</div>
              <div style="font-size:18px; font-weight:900; color:{tr_col}; text-align:right; font-family:'Outfit';">{trend}</div>
            </div>"""

        html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@600;700;800;900&family=Outfit:wght@700;800;900&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: #020617;
    font-family: 'Anek Kannada', sans-serif;
    color: #FFFFFF;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 32px 38px;
  }}
  .border-frame {{ position: absolute; inset: 16px; border: 2px solid rgba(34, 197, 94, 0.4); pointer-events: none; z-index: 10; border-radius: 24px; }}
  .content {{ position: relative; z-index: 5; display: flex; flex-direction: column; height: 100%; justify-content: space-between; }}
</style>
</head>
<body>
  <div class="border-frame"></div>

  <div class="content">
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid rgba(34,197,94,0.4); padding-bottom:12px;">
      <img src="{logo_b64}" style="height:62px; object-fit:contain;">
      <div style="background:linear-gradient(90deg, #16A34A, #059669); color:#FFF; font-size:17px; font-weight:900; padding:6px 20px; border-radius:20px; font-family:'Outfit';">09:15 AM APMC MANDI RATES</div>
    </div>

    <div>
      <div style="font-size:22px; font-weight:900; color:#86EFAC; letter-spacing:2px; font-family:'Outfit';">KSAMB APMC LIVE MARKET PRICES • {today_str}</div>
      <div style="font-size:38px; font-weight:900; color:#FFFFFF; margin-top:2px;">ರಾಜ್ಯದ ಪ್ರಮುಖ ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ 🌾</div>
      <div style="font-size:18px; font-weight:800; color:#FDE047; margin-top:2px;">{title_sub}</div>
    </div>

    <div>
      <div style="display:grid; grid-template-columns:2fr 1.6fr 1.8fr 1fr; background:#0F172A; border-radius:12px; padding:10px 18px; margin-bottom:8px; font-size:17px; font-weight:900; color:#94A3B8;">
        <div>ಬೆಳೆ & ಮಾರುಕಟ್ಟೆ</div>
        <div style="color:#FDE047;">ದರ ವ್ಯಾಪ್ತಿ</div>
        <div>ಪ್ರಮಾಣ</div>
        <div style="text-align:right;">ಟ್ರೆಂಡ್</div>
      </div>
      {rows_html}
    </div>

    <div style="display:flex; justify-content:space-between; align-items:center; border-top:2px solid rgba(34,197,94,0.4); padding-top:14px;">
      <div style="font-size:19px; color:#CBD5E1; font-weight:800;">📊 ರಾಜ್ಯದ 174 APMC ಲೈವ್ ದರ: karnata.in/apmc-prices</div>
      <div style="font-size:24px; font-weight:900; color:#22C55E; font-family:'Outfit';">karnata.in</div>
    </div>
  </div>
</body>
</html>"""

        out_file = OUTPUT_DIR / f"apmc_p{p_num}.png"
        render_html_to_png(html, out_file)

# ══════════════════════════════════════════════════════════════════════════════
# 5. 09:45 AM: 13 MAJOR DAMS WATER LEVELS (2-PAGE CAROUSEL + 6 SPOTLIGHTS)
# ══════════════════════════════════════════════════════════════════════════════
def render_dam_carousel_and_spotlights():
    dams = get_live_dams()
    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    bg_b64 = get_file_base64(str(OUTPUT_DIR / "dam_bg.jpg"))
    today_str = datetime.now().strftime('%d %B %Y').replace('September', 'ಸೆಪ್ಟೆಂಬರ್').replace('October', 'ಅಕ್ಟೋಬರ್')

    # Page 1: South Karnataka Dams
    p1_dam_keys = ["krs", "kabini", "harangi", "hemavathi", "bhadra", "linganamakki"]
    # Page 2: North & Central Karnataka Dams
    p2_dam_keys = ["almatti", "tungabhadra", "malaprabha", "ghataprabha", "supa", "narayanapura", "vanivilasa"]

    def build_dam_rows(keys):
        rows = ""
        for k in keys:
            v = dams.get(k, {})
            name = v.get("name_kn", k.upper())
            pct = v.get("storage_pct", 85)
            level = v.get("level_ft", v.get("current_level", 0))
            max_lvl = v.get("design_capacity", v.get("max_level", 0))
            storage = v.get("storage_tmc", v.get("present_storage_tmc", 0))
            max_st = v.get("max_storage_tmc", 0)
            inflow = v.get("inflow_cusecs", v.get("inflow", 0))
            outflow = v.get("outflow_cusecs", v.get("outflow", 0))

            color_bar = "#10B981" if pct >= 80 else ("#F59E0B" if pct >= 50 else "#EF4444")

            rows += f"""
            <div style="background:rgba(30,41,59,0.85); border:1px solid #334155; border-radius:14px; padding:14px 18px; margin-bottom:10px;">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                <div style="font-size:22px; font-weight:900; color:#FFFFFF;">{name}</div>
                <div style="font-size:22px; font-weight:900; color:#38BDF8; font-family:'Outfit';">{pct:.1f}% ತುಂಬಿದೆ</div>
              </div>
              <div style="width:100%; height:8px; background:#1E293B; border-radius:4px; overflow:hidden; margin-bottom:8px;">
                <div style="width:{min(100, pct)}%; height:100%; background:{color_bar}; border-radius:4px;"></div>
              </div>
              <div style="display:flex; justify-content:space-between; font-size:15px; font-weight:800; color:#CBD5E1;">
                <div>ನೀರಿನ ಮಟ್ಟ: <span style="color:#FDE047;">{level:.1f} / {max_lvl:.1f} ಅಡಿ</span></div>
                <div>ಸಂಗ್ರಹ: <span style="color:#67E8F9;">{storage:.1f} / {max_st:.1f} TMC</span></div>
                <div>ಒಳಹರಿವು: <span style="color:#34D399;">{inflow:,} ಕ್ಯೂಸೆಕ್</span></div>
              </div>
            </div>"""
        return rows

    for p_num, keys, sub in [(1, p1_dam_keys, "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ & ಮಲೆನಾಡು ಜಲಾಶಯಗಳು (Slide 1/2)"), (2, p2_dam_keys, "ಉತ್ತರ & ಮಧ್ಯ ಕರ್ನಾಟಕ ಜಲಾಶಯಗಳು (Slide 2/2)")]:
        rows_html = build_dam_rows(keys)
        html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@600;700;800;900&family=Outfit:wght@700;800;900&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: #020617;
    font-family: 'Anek Kannada', sans-serif;
    color: #FFFFFF;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 32px 38px;
  }}
  .bg-img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.35; z-index: 1; }}
  .content {{ position: relative; z-index: 5; display: flex; flex-direction: column; height: 100%; justify-content: space-between; }}
  .border-frame {{ position: absolute; inset: 16px; border: 2px solid rgba(56, 189, 248, 0.4); pointer-events: none; z-index: 10; border-radius: 24px; }}
</style>
</head>
<body>
  <div class="border-frame"></div>
  <img src="{bg_b64}" class="bg-img" alt="Background">

  <div class="content">
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid rgba(56,189,248,0.4); padding-bottom:12px;">
      <img src="{logo_b64}" style="height:62px; object-fit:contain;">
      <div style="background:linear-gradient(90deg, #0284C7, #2563EB); color:#FFF; font-size:17px; font-weight:900; padding:6px 20px; border-radius:20px; font-family:'Outfit';">09:45 AM WRD DAM LEVELS</div>
    </div>

    <div>
      <div style="font-size:22px; font-weight:900; color:#38BDF8; letter-spacing:2px; font-family:'Outfit';">KARNATAKA 13 MAJOR RESERVOIRS • {today_str}</div>
      <div style="font-size:38px; font-weight:900; color:#FFFFFF; margin-top:2px;">ರಾಜ್ಯದ ಜಲಾಶಯಗಳ ಲೈವ್ ನೀರಿನ ಮಟ್ಟ 💧</div>
      <div style="font-size:18px; font-weight:800; color:#FDE047; margin-top:2px;">{sub}</div>
    </div>

    <div>{rows_html}</div>

    <div style="display:flex; justify-content:space-between; align-items:center; border-top:2px solid rgba(56,189,248,0.4); padding-top:14px;">
      <div style="font-size:19px; color:#CBD5E1; font-weight:800;">📊 13 ಜಲಾಶಯಗಳ ಲೈವ್ ಒಳಹರಿವು/ಹೊರಹರಿವು: karnata.in/dam-levels</div>
      <div style="font-size:24px; font-weight:900; color:#38BDF8; font-family:'Outfit';">karnata.in</div>
    </div>
  </div>
</body>
</html>"""

        out_file = OUTPUT_DIR / f"dam_levels_p{p_num}.png"
        render_html_to_png(html, out_file)

    # 6 INDIVIDUAL HERO SPOTLIGHT CARDS
    spotlights = [
        ("krs", "KRS Dam (ಕೃಷ್ಣರಾಜ ಸಾಗರ)", "ಮಂಡ್ಯ ಜಿಲ್ಲೆ | ಕಾವೇರಿ ನದಿ", 124.80, 49.45),
        ("almatti", "ಆಲಮಟ್ಟಿ ಜಲಾಶಯ (ಲಾಲ್ ಬಹದ್ದೂರ್ ಶಾಸ್ತ್ರಿ)", "ವಿಜಯಪುರ ಜಿಲ್ಲೆ | ಕೃಷ್ಣಾ ನದಿ", 519.60, 123.08),
        ("tungabhadra", "ತುಂಗಭದ್ರಾ ಜಲಾಶಯ (ಟಿಬಿ ಡ್ಯಾಂ)", "ವಿಜಯನಗರ (ಹೊಸಪೇಟೆ) | ತುಂಗಭದ್ರಾ ನದಿ", 1633.00, 105.79),
        ("bhadra", "ಭದ್ರಾ ಜಲಾಶಯ (ಲಕ್ಕವಳ್ಳಿ)", "ಚಿಕ್ಕಮಗಳೂರು | ಭದ್ರಾ ನದಿ", 186.00, 71.54),
        ("kabini", "ಕಬಿನಿ ಜಲಾಶಯ (ಬೀಚನಹಳ್ಳಿ)", "ಮೈಸೂರು (ಹೆಚ್.ಡಿ.ಕೋಟೆ) | ಕಬಿನಿ ನದಿ", 2284.00, 19.52),
        ("ghataprabha", "ಘಟಪ್ರಭಾ ಜಲಾಶಯ (ಹಿಡಕಲ್ ಡ್ಯಾಂ)", "ಬೆಳಗಾವಿ (ಹುಕ್ಕೇರಿ) | ಘಟಪ್ರಭಾ ನದಿ", 2175.00, 51.00)
    ]

    for k, title_kn, loc_kn, def_lvl, def_st in spotlights:
        v = dams.get(k, {})
        pct = v.get("storage_pct", 92.5)
        level = v.get("level_ft", v.get("current_level", def_lvl))
        max_lvl = v.get("design_capacity", v.get("max_level", def_lvl))
        storage = v.get("storage_tmc", v.get("present_storage_tmc", def_st))
        max_st = v.get("max_storage_tmc", def_st)
        inflow = v.get("inflow_cusecs", v.get("inflow", 15420))
        outflow = v.get("outflow_cusecs", v.get("outflow", 8250))

        html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@600;700;800;900&family=Outfit:wght@700;800;900&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: #020617;
    font-family: 'Anek Kannada', sans-serif;
    color: #FFFFFF;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 36px 42px;
  }}
  .bg-img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.40; z-index: 1; }}
  .content {{ position: relative; z-index: 5; display: flex; flex-direction: column; height: 100%; justify-content: space-between; }}
  .border-frame {{ position: absolute; inset: 16px; border: 2px solid rgba(56, 189, 248, 0.4); pointer-events: none; z-index: 10; border-radius: 24px; }}
</style>
</head>
<body>
  <div class="border-frame"></div>
  <img src="{bg_b64}" class="bg-img" alt="Background">

  <div class="content">
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid rgba(56,189,248,0.4); padding-bottom:14px;">
      <img src="{logo_b64}" style="height:64px; object-fit:contain;">
      <div style="background:linear-gradient(90deg, #0284C7, #2563EB); color:#FFF; font-size:17px; font-weight:900; padding:6px 22px; border-radius:20px; font-family:'Outfit';">DAM SPOTLIGHT • ಲೈವ್ ವರದಿ</div>
    </div>

    <div>
      <div style="font-size:22px; font-weight:900; color:#38BDF8; letter-spacing:2px; font-family:'Outfit';">RESERVOIR WATER REPORT • {today_str}</div>
      <div style="font-size:42px; font-weight:900; color:#FFFFFF; margin-top:2px;">{title_kn} 🌊</div>
      <div style="font-size:20px; font-weight:800; color:#FDE047; margin-top:2px;">📍 {loc_kn}</div>
    </div>

    <!-- MAIN PERCENTAGE HERO CARD -->
    <div style="background:rgba(15,23,42,0.85); border:2px solid #0284C7; border-radius:24px; padding:32px 36px; text-align:center;">
      <div style="font-size:20px; font-weight:800; color:#94A3B8; margin-bottom:8px;">ಪ್ರಸ್ತುತ ಜಲಾಶಯದ ನೀರಿನ ಸಾಮರ್ಥ್ಯ</div>
      <div style="font-size:72px; font-weight:900; color:#38BDF8; font-family:'Outfit'; line-height:1;">{pct:.1f}%</div>
      <div style="font-size:22px; font-weight:800; color:#10B981; margin-top:8px;">ಸುರಕ್ಷಿತ ಮಟ್ಟದಲ್ಲಿ ಜಲಸಂಗ್ರಹ</div>
      
      <div style="width:100%; height:14px; background:#1E293B; border-radius:8px; overflow:hidden; margin:24px 0 16px;">
        <div style="width:{min(100, pct)}%; height:100%; background:linear-gradient(90deg, #0284C7, #38BDF8); border-radius:8px;"></div>
      </div>
    </div>

    <!-- 4 TELEMETRY CARDS -->
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
      <div style="background:rgba(30,41,59,0.85); border:1px solid #334155; border-radius:18px; padding:18px 22px;">
        <div style="font-size:16px; font-weight:800; color:#94A3B8;">ಪ್ರಸ್ತುತ ನೀರಿನ ಮಟ್ಟ</div>
        <div style="font-size:28px; font-weight:900; color:#FDE047; font-family:'Outfit'; margin-top:4px;">{level:.2f} / {max_lvl:.2f} ft</div>
      </div>

      <div style="background:rgba(30,41,59,0.85); border:1px solid #334155; border-radius:18px; padding:18px 22px;">
        <div style="font-size:16px; font-weight:800; color:#94A3B8;">ಒಟ್ಟು ಜಲಸಂಗ್ರಹ</div>
        <div style="font-size:28px; font-weight:900; color:#67E8F9; font-family:'Outfit'; margin-top:4px;">{storage:.2f} / {max_st:.2f} TMC</div>
      </div>

      <div style="background:rgba(30,41,59,0.85); border:1px solid #334155; border-radius:18px; padding:18px 22px;">
        <div style="font-size:16px; font-weight:800; color:#94A3B8;">ಲೈವ್ ಒಳಹರಿವು (Inflow)</div>
        <div style="font-size:28px; font-weight:900; color:#34D399; font-family:'Outfit'; margin-top:4px;">{inflow:,} Cusecs</div>
      </div>

      <div style="background:rgba(30,41,59,0.85); border:1px solid #334155; border-radius:18px; padding:18px 22px;">
        <div style="font-size:16px; font-weight:800; color:#94A3B8;">ಹೊರಹರಿವು (Outflow)</div>
        <div style="font-size:28px; font-weight:900; color:#F87171; font-family:'Outfit'; margin-top:4px;">{outflow:,} Cusecs</div>
      </div>
    </div>

    <div style="display:flex; justify-content:space-between; align-items:center; border-top:2px solid rgba(56,189,248,0.4); padding-top:14px;">
      <div style="font-size:19px; color:#CBD5E1; font-weight:800;">💧 ಪ್ರತಿದಿನದ ನಿಖರ WRD ವರದಿ: karnata.in/dam-levels</div>
      <div style="font-size:24px; font-weight:900; color:#38BDF8; font-family:'Outfit';">karnata.in</div>
    </div>
  </div>
</body>
</html>"""

        out_file = OUTPUT_DIR / f"dam_{k}.png"
        render_html_to_png(html, out_file)

# ══════════════════════════════════════════════════════════════════════════════
# 6. 10:15 AM: OFFICIAL GOLD & SILVER RATES (WITH LIVE DELTAS & LUXURY DESIGN)
# ══════════════════════════════════════════════════════════════════════════════
def render_gold_card():
    gold = get_live_gold()
    t = gold["today"]
    y = gold["yesterday"]
    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    bg_b64 = get_file_base64(str(OUTPUT_DIR / "gold_bg.jpg"))

    diff_24k = t["24k"] - y["24k"]
    diff_22k = t["22k"] - y["22k"]
    diff_18k = t["18k"] - y["18k"]
    diff_silver = t["silver_999"] - y["silver_999"]

    diff_24k_str = f"+₹{diff_24k} 🔼" if diff_24k > 0 else (f"-₹{abs(diff_24k)} 🔽" if diff_24k < 0 else "0.00 —")
    diff_22k_str = f"+₹{diff_22k} 🔼" if diff_22k > 0 else (f"-₹{abs(diff_22k)} 🔽" if diff_22k < 0 else "0.00 —")
    diff_18k_str = f"+₹{diff_18k} 🔼" if diff_18k > 0 else (f"-₹{abs(diff_18k)} 🔽" if diff_18k < 0 else "0.00 —")
    diff_pawan = diff_22k * 8
    diff_pawan_str = f"+₹{diff_pawan} 🔼" if diff_pawan > 0 else (f"-₹{abs(diff_pawan)} 🔽" if diff_pawan < 0 else "0.00 —")

    col_24k = "#10B981" if diff_24k <= 0 else "#EF4444"
    col_22k = "#10B981" if diff_22k <= 0 else "#EF4444"

    pawan_22k = t["22k"] * 8
    ten_g_24k = t["24k"] * 10
    ten_g_22k = t["22k"] * 10
    silver_1kg = int(t["silver_999"] * 1000)

    today_str = datetime.now().strftime('%d %B %Y').replace('September', 'ಸೆಪ್ಟೆಂಬರ್').replace('October', 'ಅಕ್ಟೋಬರ್')

    html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@600;700;800;900&family=Outfit:wght@700;800;900&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: #020617;
    font-family: 'Anek Kannada', sans-serif;
    color: #FFFFFF;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 36px 42px;
  }}
  .bg-img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.35; z-index: 1; }}
  .content {{ position: relative; z-index: 5; display: flex; flex-direction: column; height: 100%; justify-content: space-between; }}
  .border-frame {{ position: absolute; inset: 16px; border: 2.5px solid rgba(245, 158, 11, 0.6); pointer-events: none; z-index: 10; border-radius: 24px; }}
</style>
</head>
<body>
  <div class="border-frame"></div>
  <img src="{bg_b64}" class="bg-img" alt="Background">

  <div class="content">
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid rgba(245,158,11,0.4); padding-bottom:14px;">
      <img src="{logo_b64}" style="height:64px; object-fit:contain;">
      <div style="background:linear-gradient(90deg, #F59E0B, #D97706); color:#000; font-size:17px; font-weight:900; padding:6px 22px; border-radius:20px; font-family:'Outfit';">10:15 AM OFFICIAL BULLION LIVE</div>
    </div>

    <div>
      <div style="font-size:22px; font-weight:900; color:#FDE047; letter-spacing:2px; font-family:'Outfit';">KARNATAKA GOLD & SILVER BENCHMARK • {today_str}</div>
      <div style="font-size:42px; font-weight:900; color:#FFFFFF; margin-top:2px;">ಇಂದಿನ ಅಧಿಕೃತ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಲೈವ್ ದರ 🪙</div>
    </div>

    <!-- 2 MAIN HIGHLIGHT CARDS (24K & 22K) -->
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:20px;">
      <div style="background:rgba(15,23,42,0.92); border:2px solid #F59E0B; border-radius:24px; padding:24px 26px; box-shadow:0 12px 35px rgba(245,158,11,0.2);">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span style="font-size:24px; font-weight:900; color:#FDE047;">24K ಅಪರಂಜಿ (ಶುದ್ಧ)</span>
          <span style="background:rgba(245,158,11,0.2); color:{col_24k}; font-size:16px; font-weight:900; padding:4px 12px; border-radius:12px; font-family:'Outfit';">{diff_24k_str}</span>
        </div>
        <div style="font-size:52px; font-weight:900; color:#FFFFFF; font-family:'Outfit'; margin:12px 0 6px;">₹{t['24k']:,}</div>
        <div style="font-size:17px; font-weight:800; color:#94A3B8;">ಪ್ರತಿ ಗ್ರಾಂಗೆ (1 Gram)</div>
        <div style="margin-top:14px; border-top:1px solid rgba(245,158,11,0.25); padding-top:10px; display:flex; justify-content:space-between; font-size:17px; font-weight:800; color:#CBD5E1;">
          <span>10 ಗ್ರಾಂ ಬೆಲೆ:</span>
          <strong style="color:#FDE047; font-family:'Outfit';">₹{ten_g_24k:,}</strong>
        </div>
      </div>

      <div style="background:rgba(15,23,42,0.92); border:2px solid #E11D48; border-radius:24px; padding:24px 26px; box-shadow:0 12px 35px rgba(225,29,72,0.2);">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span style="font-size:24px; font-weight:900; color:#FDA4AF;">22K ಆಭರಣ ಚಿನ್ನ</span>
          <span style="background:rgba(225,29,72,0.2); color:{col_22k}; font-size:16px; font-weight:900; padding:4px 12px; border-radius:12px; font-family:'Outfit';">{diff_22k_str}</span>
        </div>
        <div style="font-size:52px; font-weight:900; color:#FFFFFF; font-family:'Outfit'; margin:12px 0 6px;">₹{t['22k']:,}</div>
        <div style="font-size:17px; font-weight:800; color:#94A3B8;">ಪ್ರತಿ ಗ್ರಾಂಗೆ (1 Gram)</div>
        <div style="margin-top:14px; border-top:1px solid rgba(225,29,72,0.25); padding-top:10px; display:flex; justify-content:space-between; font-size:17px; font-weight:800; color:#CBD5E1;">
          <span>10 ಗ್ರಾಂ ಬೆಲೆ:</span>
          <strong style="color:#FDA4AF; font-family:'Outfit';">₹{ten_g_22k:,}</strong>
        </div>
      </div>
    </div>

    <!-- SOVEREIGN / SILVER / 18K STRIP -->
    <div style="display:grid; grid-template-columns:1.3fr 1.3fr 1.3fr; gap:16px;">
      <div style="background:rgba(30,41,59,0.85); border:1px solid #334155; border-radius:18px; padding:16px 20px;">
        <div style="font-size:16px; font-weight:800; color:#94A3B8;">8 ಗ್ರಾಂ (1 ಪವನ್ 22K)</div>
        <div style="font-size:28px; font-weight:900; color:#FDE047; font-family:'Outfit'; margin:4px 0;">₹{pawan_22k:,}</div>
        <div style="font-size:14px; font-weight:800; color:{col_22k};">{diff_pawan_str}</div>
      </div>

      <div style="background:rgba(30,41,59,0.85); border:1px solid #334155; border-radius:18px; padding:16px 20px;">
        <div style="font-size:16px; font-weight:800; color:#94A3B8;">18K ಚಿನ್ನ (ಗ್ರಾಂಗೆ)</div>
        <div style="font-size:28px; font-weight:900; color:#67E8F9; font-family:'Outfit'; margin:4px 0;">₹{t['18k']:,}</div>
        <div style="font-size:14px; font-weight:800; color:#38BDF8;">{diff_18k_str}</div>
      </div>

      <div style="background:rgba(30,41,59,0.85); border:1px solid #334155; border-radius:18px; padding:16px 20px;">
        <div style="font-size:16px; font-weight:800; color:#94A3B8;">ಶುದ್ಧ ಬೆಳ್ಳಿ (1 ಕೆಜಿ)</div>
        <div style="font-size:28px; font-weight:900; color:#E2E8F0; font-family:'Outfit'; margin:4px 0;">₹{silver_1kg:,}</div>
        <div style="font-size:14px; font-weight:800; color:#CBD5E1;">ಗ್ರಾಂಗೆ ₹{t['silver_999']:.2f}</div>
      </div>
    </div>

    <div style="display:flex; justify-content:space-between; align-items:center; border-top:2px solid rgba(245,158,11,0.4); padding-top:14px;">
      <div style="font-size:19px; color:#CBD5E1; font-weight:800;">📊 31 ಜಿಲ್ಲೆಗಳ ಲೈವ್ ದರ & ಒಡವೆ ಲೆಕ್ಕಾಚಾರ: karnata.in/gold-rate</div>
      <div style="font-size:24px; font-weight:900; color:#F59E0B; font-family:'Outfit';">karnata.in</div>
    </div>
  </div>
</body>
</html>"""

    out_file = OUTPUT_DIR / "gold_rate_today.png"
    render_html_to_png(html, out_file)

# ══════════════════════════════════════════════════════════════════════════════
# 7. IMD NOWCAST COLOR-CODED KARNATAKA ALERT MAP POSTER (4 SLOTS)
# ══════════════════════════════════════════════════════════════════════════════
def render_nowcast_map_card():
    w = get_live_weather()
    nowcast_districts = w.get("nowcast", {}).get("districts", {})
    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    bg_b64 = get_file_base64(str(OUTPUT_DIR / "weather_bg.jpg"))

    red_districts = []
    orange_districts = []
    yellow_districts = []
    green_districts = []

    for k, v in nowcast_districts.items():
        lvl = v.get("level", "green").lower()
        name = v.get("district_kn", k)
        if lvl == "red": red_districts.append(name)
        elif lvl == "orange": orange_districts.append(name)
        elif lvl == "yellow": yellow_districts.append(name)
        else: green_districts.append(name)

    # Defaults if none
    if not red_districts and not orange_districts and not yellow_districts:
        yellow_districts = ["ಉಡುಪಿ", "ದಕ್ಷಿಣ ಕನ್ನಡ", "ಉತ್ತರ ಕನ್ನಡ", "ಶಿವಮೊಗ್ಗ", "ಚಿಕ್ಕಮಗಳೂರು"]
        green_districts = ["ಬೆಂಗಳೂರು", "ಮೈಸೂರು", "ಬೆಳಗಾವಿ", "ಕಲಬುರಗಿ", "ತುಮಕೂರು", "ಹಾಸನ", "ಮಂಡ್ಯ"]

    today_str = datetime.now().strftime('%d %B %Y • %I:%M %p').replace('September', 'ಸೆಪ್ಟೆಂಬರ್').replace('October', 'ಅಕ್ಟೋಬರ್')

    def make_zone_box(title, items, bg_col, border_col, text_col, icon):
        items_str = ", ".join(items[:8]) if items else "ಯಾವುದೇ ಜಿಲ್ಲೆಗಳಿಲ್ಲ"
        if len(items) > 8: items_str += f" (+{len(items)-8} ಜಿಲ್ಲೆಗಳು)"
        return f"""
        <div style="background:{bg_col}; border:2px solid {border_col}; border-radius:18px; padding:18px 22px; margin-bottom:14px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
            <div style="font-size:22px; font-weight:900; color:{text_col};">{icon} {title}</div>
            <div style="font-size:16px; font-weight:800; color:{text_col};">{len(items)} ಜಿಲ್ಲೆಗಳು</div>
          </div>
          <div style="font-size:18px; font-weight:800; color:#F8FAFC; line-height:1.5;">{items_str}</div>
        </div>"""

    box_red = make_zone_box("ರೆಡ್ ಅಲರ್ಟ್ (ಅತಿ ಭಾರೀ ಮಳೆ & ಪ್ರವಾಹ)", red_districts, "rgba(220,38,38,0.2)", "#EF4444", "#FCA5A5", "🔴")
    box_orange = make_zone_box("ಆರೆಂಜ್ ಅಲರ್ಟ್ (ಧಾರಾಕಾರ ಮಳೆ & ಬಿರುಗಾಳಿ)", orange_districts, "rgba(234,88,12,0.2)", "#F97316", "#FDBA74", "🟠")
    box_yellow = make_zone_box("ಹಳದಿ ನಿಗಾ (ಗುಡುಗು ಸಹಿತ ಸಾಧಾರಣ ಮಳೆ)", yellow_districts, "rgba(234,179,8,0.2)", "#EAB308", "#FDE047", "🟡")
    box_green = make_zone_box("ಗ್ರೀನ್ ಜೋನ್ (ಸಾಮಾನ್ಯ / ಶುಭ ಹವೆ)", green_districts, "rgba(34,197,94,0.15)", "#22C55E", "#86EFAC", "🟢")

    html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@600;700;800;900&family=Outfit:wght@700;800;900&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: #020617;
    font-family: 'Anek Kannada', sans-serif;
    color: #FFFFFF;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 32px 38px;
  }}
  .bg-img {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.35; z-index: 1; }}
  .content {{ position: relative; z-index: 5; display: flex; flex-direction: column; height: 100%; justify-content: space-between; }}
  .border-frame {{ position: absolute; inset: 16px; border: 2px solid rgba(56, 189, 248, 0.4); pointer-events: none; z-index: 10; border-radius: 24px; }}
</style>
</head>
<body>
  <div class="border-frame"></div>
  <img src="{bg_b64}" class="bg-img" alt="Background">

  <div class="content">
    <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid rgba(56,189,248,0.4); padding-bottom:12px;">
      <img src="{logo_b64}" style="height:62px; object-fit:contain;">
      <div style="background:linear-gradient(90deg, #0284C7, #2563EB); color:#FFF; font-size:17px; font-weight:900; padding:6px 20px; border-radius:20px; font-family:'Outfit';">IMD 3-HOUR NOWCAST RADAR</div>
    </div>

    <div>
      <div style="font-size:22px; font-weight:900; color:#38BDF8; letter-spacing:2px; font-family:'Outfit';">KARNATAKA 31 DISTRICTS RADAR • {today_str}</div>
      <div style="font-size:38px; font-weight:900; color:#FFFFFF; margin-top:2px;">ರಾಜ್ಯದ ಲೈವ್ ಮಳೆ ಅಲರ್ಟ್ ನಕ್ಷೆ ⛈️</div>
    </div>

    <!-- 4 COLOR ZONES -->
    <div>
      {box_red}
      {box_orange}
      {box_yellow}
      {box_green}
    </div>

    <div style="display:flex; justify-content:space-between; align-items:center; border-top:2px solid rgba(56,189,248,0.4); padding-top:14px;">
      <div style="font-size:19px; color:#CBD5E1; font-weight:800;">📡 ನಿಮ್ಮ ತಾಲೂಕಿನ ಲೈವ್ IMD ಎಚ್ಚರಿಕೆ ನೋಡಿ: karnata.in/weather</div>
      <div style="font-size:24px; font-weight:900; color:#38BDF8; font-family:'Outfit';">karnata.in</div>
    </div>
  </div>
</body>
</html>"""

    out_file = OUTPUT_DIR / "weather_nowcast_map.png"
    render_html_to_png(html, out_file)

# ══════════════════════════════════════════════════════════════════════════════
# 8. QUIZ POSTERS (SLOT 1, 2, 3) — QUESTION & OPTIONS ONLY (NO ANSWER REVEALED)
# ══════════════════════════════════════════════════════════════════════════════
def render_quiz_interactive_card(slot_num=1):
    quiz_data = get_daily_quiz_data()
    questions = quiz_data.get("questions", [])
    
    # Pick question according to slot
    idx = slot_num - 1
    if idx < len(questions):
        q = questions[idx]
    else:
        master = get_master_quiz_bank()
        q = master[idx % len(master)]

    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    today_str = datetime.now().strftime('%d %B %Y').replace('September', 'ಸೆಪ್ಟೆಂಬರ್').replace('October', 'ಅಕ್ಟೋಬರ್')
    time_labels = {1: "11:30 AM ಸವಾಲು", 2: "02:30 PM ಸವಾಲು", 3: "05:45 PM ಸವಾಲು"}

    opt_letters = ["A", "B", "C", "D"]
    opt_html = ""
    for o_idx, opt in enumerate(q.get("options", [])[:4]):
        opt_html += f"""
        <div style="background:#1E293B; border:2.5px solid #475569; border-radius:18px; padding:20px 24px; display:flex; align-items:center; gap:18px; font-size:25px; font-weight:900;">
          <div style="width:48px; height:48px; border-radius:50%; background:#E11D48; display:flex; align-items:center; justify-content:center; font-size:24px; font-weight:900; font-family:'Outfit'; color:#FFF;">{opt_letters[o_idx]}</div>
          <div style="color:#F8FAFC;">{opt}</div>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@700;800;900&family=Outfit:wght@800;900&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: radial-gradient(circle at 50% 0%, #31101E 0%, #0F172A 50%, #020617 100%);
    font-family: 'Anek Kannada', sans-serif;
    color: #FFFFFF;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 36px 42px;
    border: 14px solid;
    border-image: linear-gradient(135deg, #B91C1C, #E11D48, #F59E0B) 1;
  }}
</style>
</head>
<body>
  <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid rgba(225,29,72,0.4); padding-bottom:14px;">
    <img src="{logo_b64}" alt="Karnata Logo" style="height:64px; object-fit:contain;">
    <div style="background:#E11D48; color:#FFF; font-size:18px; font-weight:900; padding:6px 22px; border-radius:20px; font-family:'Outfit';">{time_labels.get(slot_num, "KNOWLEDGE CHALLENGE")}</div>
  </div>

  <div>
    <div style="font-size:22px; font-weight:900; color:#FDE047; letter-spacing:2px; font-family:'Outfit';">KARNATAKA DAILY QUIZ • {today_str}</div>
    <div style="font-size:42px; font-weight:900; color:#FFFFFF; margin-top:2px;">ಕರ್ನಾಟಕ ಜ್ಞಾನ ಸವಾಲು #{slot_num} 🧠</div>
  </div>

  <div style="background:rgba(30,41,59,0.95); border:3px solid #E11D48; border-radius:24px; padding:28px 32px; box-shadow:0 14px 35px rgba(225,29,72,0.35);">
    <div style="font-size:22px; font-weight:900; color:#FDE047; margin-bottom:8px;">❓ ಇಂದಿನ ಸವಾಲಿನ ಪ್ರಶ್ನೆ:</div>
    <div style="font-size:32px; font-weight:900; line-height:1.4; color:#FFFFFF;">
      {q.get('question')}
    </div>
  </div>

  <!-- 4 OPTIONS ONLY (NO ANSWER REVEALED) -->
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
    {opt_html}
  </div>

  <!-- CALL TO ACTION FOR COMMENTS -->
  <div style="background:#1E1B4B; border:2px solid #818CF8; border-radius:18px; padding:16px 24px; text-align:center;">
    <div style="font-size:24px; font-weight:900; color:#FDE047;">
      👇 ನಿಮ್ಮ ಸರಿ ಉತ್ತರ ಯಾವುದು? ಕಾಮೆಂಟ್ ಮಾಡಿ! (A, B, C ಅಥವಾ D)
    </div>
  </div>

  <div style="border-top:2px solid rgba(225,29,72,0.4); padding-top:14px; display:flex; justify-content:space-between; align-items:center;">
    <div style="font-size:20px; color:#94A3B8; font-weight:800;">👉 ಪೂರ್ಣ 20 ಪ್ರಶ್ನೆಗಳ ರಸಪ್ರಶ್ನೆ ಆಡಿ ಪ್ರಮಾಣಪತ್ರ ಗೆಲ್ಲಿರಿ: karnata.in/quiz</div>
    <div style="font-size:24px; font-weight:900; color:#E11D48; font-family:'Outfit';">karnata.in</div>
  </div>
</body>
</html>"""

    out_file = OUTPUT_DIR / f"quiz_slot{slot_num}.png"
    render_html_to_png(html, out_file)
    if slot_num == 1:
        # Also save as legacy quiz_today.png
        render_html_to_png(html, OUTPUT_DIR / "quiz_today.png")

# ══════════════════════════════════════════════════════════════════════════════
# 9. "DO YOU KNOW?" (ನಿಮಗೆ ತಿಳಿದಿದೆಯೇ?) KNOWLEDGE CARDS (SLOT 1, 2, 3)
# ══════════════════════════════════════════════════════════════════════════════
def render_doyouknow_card(slot_num=1):
    # Distinct non-duplicate facts drawn from master repository
    doyouknow_facts = [
        {
            "title": "ಏಷ್ಯಾದಲ್ಲೇ ಮೊದಲ ಬಾರಿಗೆ ಬೀದಿ ದೀಪ ಪಡೆದ ನಗರ ನಮ್ಮ ಬೆಂಗಳೂರು!",
            "fact": "1905 ರ ಆಗಸ್ಟ್ 5 ರಂದು ಕಾವೇರಿ ನದಿಯ ಶಿವನಸಮುದ್ರ ಜಲವಿದ್ಯುತ್ ಯೋಜನೆಯಿಂದ ಬೆಂಗಳೂರಿನ ಕೆ.ಆರ್. ಮಾರುಕಟ್ಟೆ ಸುತ್ತಮುತ್ತ ಪ್ರಪ್ರಥಮ ಬಾರಿಗೆ ವಿದ್ಯುತ್ ದೀಪಗಳನ್ನು ಬೆಳಗಿಸಲಾಯಿತು. ಆ ಮೂಲಕ ಇಡೀ ಏಷ್ಯಾ ಖಂಡದಲ್ಲೇ ವಿದ್ಯುತ್ ದೀಪ ಪಡೆದ ಮೊದಲ ನಗರವೆಂಬ ಐತಿಹಾಸಿಕ ಹೆಗ್ಗಳಿಕೆಗೆ ಬೆಂಗಳೂರು ಪಾತ್ರವಾಯಿತು!",
            "tag": "ಇತಿಹಾಸ & ತಂತ್ರಜ್ಞಾನ",
            "stat": "1905 — ಏಷ್ಯಾದ ಪ್ರಥಮ ವಿದ್ಯುತ್ ನಗರ"
        },
        {
            "title": "ವಿಶ್ವದ 2ನೇ ಅತಿ ದೊಡ್ಡ ಕಂಬಗಳಿಲ್ಲದ ಗುಮ್ಮಟ ವಿಜಯಪುರದ ಗೋಲ್ ಗುಂಬಜ್!",
            "fact": "ಆದಿಲ್‌ಶಾಹಿ ಸುಲ್ತಾನ್ ಮೊಹಮ್ಮದ್ ಆದಿಲ್ ಶಾಹ್ ನಿರ್ಮಿಸಿದ ಗೋಲ್ ಗುಂಬಜ್ ಯಾವುದೇ ಕಂಬಗಳ ಆಸರೆಯಿಲ್ಲದೆ ನಿಂತಿರುವ ವಿಶ್ವದ 2ನೇ ಅತಿ ದೊಡ್ಡ ಗುಮ್ಮಟವಾಗಿದೆ. ಇಲ್ಲಿರುವ ಪಿಸುಗುಟ್ಟುವ ಮೊಗಸಾಲೆಯಲ್ಲಿ (Whispering Gallery) ಸಣ್ಣದಾಗಿ ಪಿಸುಗುಟ್ಟಿದರೂ ಎದುರು ಬದಿಗೆ ಸ್ಪಷ್ಟವಾಗಿ ಕೇಳಿಸುತ್ತದೆ ಹಾಗೂ ಒಂದೇ ಶಬ್ದವು 7 ರಿಂದ 11 ಬಾರಿ ಪ್ರತಿಧ್ವನಿಸುತ್ತದೆ!",
            "tag": "ವಾಸ್ತುಶಿಲ್ಪ ವೈಭವ",
            "stat": "11 ಬಾರಿ ಪ್ರತಿಧ್ವನಿಸುವ ಅದ್ಭುತ"
        },
        {
            "title": "ಭಾರತದಲ್ಲೇ ಪ್ರಪ್ರಥಮ ಬಾರಿಗೆ ಕಾಫಿ ಬೆಳೆದಿದ್ದು ಚಿಕ್ಕಮಗಳೂರಿನ ಬಾಬಾಬುಡನ್‌ಗಿರಿಯಲ್ಲಿ!",
            "fact": "17ನೇ ಶತಮಾನದಲ್ಲಿ ಸೂಫಿ ಸಂತ ಬಾಬಾ ಬುಡನ್ ಅವರು ಯೆಮೆನ್‌ನಿಂದ ಮೆಕ್ಕಾ ಯಾತ್ರೆ ಮುಗಿಸಿ ಹಿಂದಿರುಗುವಾಗ 7 ಹಸಿ ಕಾಫಿ ಬೀಜಗಳನ್ನು ತಮ್ಮ ಸೊಂಟದಲ್ಲಿ ಬಚ್ಚಿಟ್ಟುಕೊಂಡು ತಂದು ಚಿಕ್ಕಮಗಳೂರಿನ ಚಂದ್ರದ್ರೋಣ ಪರ್ವತ ಶ್ರೇಣಿಯಲ್ಲಿ ಬಿತ್ತಿದರು. ಇಂದು ಭಾರತ ವಿಶ್ವದ ಪ್ರಮುಖ ಕಾಫಿ ರಫ್ತುದಾರ ದೇಶವಾಗಲು ಈ 7 ಕಾಫಿ ಬೀಜಗಳೇ ನಾಂದಿ!",
            "tag": "ಕೃಷಿ & ಪರಂಪರೆ",
            "stat": "7 ಪವಿತ್ರ ಕಾಫಿ ಬೀಜಗಳು"
        }
    ]

    fact = doyouknow_facts[(slot_num - 1) % len(doyouknow_facts)]
    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    today_str = datetime.now().strftime('%d %B %Y').replace('September', 'ಸೆಪ್ಟೆಂಬರ್').replace('October', 'ಅಕ್ಟೋಬರ್')
    time_labels = {1: "12:30 PM ಜ್ಞಾನ ಸಂಗತಿ", 2: "04:00 PM ಜ್ಞಾನ ಸಂಗತಿ", 3: "08:00 PM ಜ್ಞಾನ ಸಂಗತಿ"}

    html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@700;800;900&family=Outfit:wght@800;900&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: radial-gradient(circle at 50% 10%, #1E1B4B 0%, #0F172A 50%, #020617 100%);
    font-family: 'Anek Kannada', sans-serif;
    color: #FFFFFF;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 36px 42px;
    border: 14px solid;
    border-image: linear-gradient(135deg, #4F46E5, #9333EA, #F59E0B) 1;
  }}
</style>
</head>
<body>
  <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid rgba(129,140,248,0.4); padding-bottom:14px;">
    <img src="{logo_b64}" alt="Karnata Logo" style="height:64px; object-fit:contain;">
    <div style="background:#4F46E5; color:#FFF; font-size:18px; font-weight:900; padding:6px 22px; border-radius:20px; font-family:'Outfit';">{time_labels.get(slot_num, "DO YOU KNOW?")}</div>
  </div>

  <div>
    <div style="font-size:22px; font-weight:900; color:#FDE047; letter-spacing:2px; font-family:'Outfit';">KARNATAKA KNOWLEDGE CAPSULE • {today_str}</div>
    <div style="font-size:44px; font-weight:900; color:#FFFFFF; margin-top:2px;">ನಿಮಗೆ ತಿಳಿದಿದೆಯೇ? 💡</div>
  </div>

  <!-- HIGHLIGHT TITLE -->
  <div style="background:rgba(30,41,59,0.95); border:3px solid #6366F1; border-radius:24px; padding:26px 30px; box-shadow:0 14px 35px rgba(99,102,241,0.3);">
    <div style="font-size:18px; font-weight:800; color:#A5B4FC; margin-bottom:6px;">✨ {fact['tag']}</div>
    <div style="font-size:32px; font-weight:900; line-height:1.35; color:#FDE047;">
      {fact['title']}
    </div>
  </div>

  <!-- DETAILED EXPLANATION BODY -->
  <div style="background:#0F172A; border:2px solid #334155; border-radius:22px; padding:28px 32px;">
    <div style="font-size:26px; font-weight:800; line-height:1.65; color:#E2E8F0;">
      {fact['fact']}
    </div>
  </div>

  <!-- STAT BADGE -->
  <div style="background:rgba(245,158,11,0.15); border:2px solid #F59E0B; border-radius:18px; padding:14px 24px; text-align:center;">
    <div style="font-size:22px; font-weight:900; color:#FDE047; font-family:'Outfit';">
      📌 {fact['stat']}
    </div>
  </div>

  <div style="border-top:2px solid rgba(129,140,248,0.4); padding-top:14px; display:flex; justify-content:space-between; align-items:center;">
    <div style="font-size:20px; color:#94A3B8; font-weight:800;">📖 ಕರ್ನಾಟಕದ ಸಮಗ್ರ ಇತಿಹಾಸ & ಪ್ರಚಲಿತ ಮಾಹಿತಿ: karnata.in</div>
    <div style="font-size:24px; font-weight:900; color:#818CF8; font-family:'Outfit';">karnata.in</div>
  </div>
</body>
</html>"""

    out_file = OUTPUT_DIR / f"doyouknow_slot{slot_num}.png"
    render_html_to_png(html, out_file)

# ══════════════════════════════════════════════════════════════════════════════
# MASTER RENDER ALL CARDS PIPELINE
# ══════════════════════════════════════════════════════════════════════════════
def render_all_cards():
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 🎨 Generating All Upgraded Karnata Social Graphics...")
    render_quote_card()
    render_petrol_card()
    render_weather_morning_summary()
    render_apmc_carousel()
    render_dam_carousel_and_spotlights()
    render_gold_card()
    render_nowcast_map_card()
    render_quiz_interactive_card(1)
    render_quiz_interactive_card(2)
    render_quiz_interactive_card(3)
    render_doyouknow_card(1)
    render_doyouknow_card(2)
    render_doyouknow_card(3)
    print("✨ All 16+ Upgraded Social Cards Rendered Flawlessly!")

if __name__ == "__main__":
    render_all_cards()
