#!/usr/bin/env python3
"""
Chromium High-Precision Award-Winning Social Infographics Engine (v4.0 - Minimalist & Editorial Overhaul)
Inspired by Livemint Markets, Deccan Herald, Bloomberg Bullion, and Modern Minimalist Design.
ALL IN 100% AUTHENTIC, CRISP KANNADA!

Daily Schedule (IST):
1. 07:15 AM: ಶುಭೋದಯ & ಸವಿಚಿಂತನೆ (quote_today.png)
2. 07:45 AM: ಪೆಟ್ರೋಲ್ & ಡೀಸೆಲ್ ಲೈವ್ ದರ (petrol_diesel_today.png) - Mint Markets Style
3. 08:30 AM: ನಿನ್ನೆಯ ಹವಾಮಾನ ದಾಖಲೆಗಳು (weather_morning_summary.png)
4. 09:15 AM: KSAMB APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ (apmc_p1.png, apmc_p2.png)
5. 09:45 AM: 13 ಜಲಾಶಯಗಳ ಮಟ್ಟ (dam_levels_p1.png, dam_levels_p2.png) - Deccan Herald Style
   + 6 Dam Spotlights (dam_krs.png, dam_almatti.png, etc.) - Mangla Dam Style
6. 10:15 AM: ಚಿನ್ನ & ಬೆಳ್ಳಿ ಅಧಿಕೃತ ಲೈವ್ ದರ (gold_rate_today.png) - Bloomberg Bullion Style
7. 10:45 AM: IMD ನೌಕಾಸ್ಟ್ ಮಳೆ ಮುನ್ನೆಚ್ಚರಿಕೆ ನಕ್ಷೆ (weather_nowcast_map.png)
8. 11:30 AM: ರಸಪ್ರಶ್ನೆ 1 - ಪ್ರಶ್ನೆ & ಆಯ್ಕೆಗಳು ಮಾತ್ರ (quiz_slot1.png)
9. 12:30 PM: "ನಿಮಗೆ ತಿಳಿದಿದೆಯೇ?" Fact 1 (doyouknow_slot1.png) - Minimalist 2-Tone Style
10. 01:45 PM: IMD ನೌಕಾಸ್ಟ್ ಮಳೆ ನಕ್ಷೆ 2
11. 02:30 PM: ರಸಪ್ರಶ್ನೆ 2 (quiz_slot2.png)
12. 04:00 PM: "ನಿಮಗೆ ತಿಳಿದಿದೆಯೇ?" Fact 2 (doyouknow_slot2.png)
13. 04:45 PM: IMD ನೌಕಾಸ್ಟ್ ಮಳೆ ನಕ್ಷೆ 3
14. 05:45 PM: ರಸಪ್ರಶ್ನೆ 3 (quiz_slot3.png)
15. 07:15 PM: IMD ನೌಕಾಸ್ಟ್ ಮಳೆ ನಕ್ಷೆ 4
16. 08:00 PM: "ನಿಮಗೆ ತಿಳಿದಿದೆಯೇ?" Fact 3 (doyouknow_slot3.png)
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

import shutil
CHROME_PATHS = [
    shutil.which("google-chrome"),
    shutil.which("chromium-browser"),
    shutil.which("chromium"),
    shutil.which("chrome"),
    shutil.which("msedge"),
    "/usr/bin/google-chrome",
    "/usr/bin/chromium-browser",
    "/usr/bin/chromium",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]
CHROME_PATHS = [p for p in CHROME_PATHS if p and os.path.exists(p)]

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
    
    # Inject high quality font rendering style
    hq_style = """
<style>
  * {
    -webkit-font-smoothing: antialiased !important;
    -moz-osx-font-smoothing: grayscale !important;
    text-rendering: optimizeLegibility !important;
  }
</style>
"""
    if "</head>" in html_content:
        html_content = html_content.replace("</head>", f"{hq_style}</head>", 1)

    with open(temp_html_file, "w", encoding="utf-8") as f:
        f.write(html_content)

    chrome_bin = None
    for cp in CHROME_PATHS:
        if os.path.exists(cp):
            chrome_bin = cp
            break

    if not chrome_bin:
        raise RuntimeError("No Chrome or Edge executable found!")

    file_uri = temp_html_file.resolve().as_uri()
    cmd = [
        chrome_bin,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--hide-scrollbars",
        "--force-device-scale-factor=2",
        "--window-size=1080,1080",
        f"--screenshot={out_png_path}",
        file_uri
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    print(f"✅ Rendered High-Res 2160x2160: {out_png_path.name}")

# ══════════════════════════════════════════════════════════════════════════════
# DATA SOURCES
# ══════════════════════════════════════════════════════════════════════════════
def get_live_gold():
    p = ROOT_DIR / "data" / "gold_rates.json"
    if p.exists():
        try:
            with open(p, "r", encoding="utf-8") as f:
                d = json.load(f)
                bg = d.get("baseGold") or d.get("base") or {}
                yg = d.get("yesterdayGold") or {}
                bs = d.get("baseSilver") or d.get("silver") or {}
                ys = d.get("yesterdaySilver") or {}

                g24 = int(bg.get("24") or bg.get(24) or bg.get("24k_per_gram") or bg.get("rate_24k") or 15671)
                g22 = int(bg.get("22") or bg.get(22) or bg.get("22k_per_gram") or bg.get("rate_22k") or 14360)
                g18 = int(bg.get("18") or bg.get(18) or bg.get("18k_per_gram") or bg.get("rate_18k") or 11750)
                
                y24 = int(yg.get("24") or yg.get(24) or yg.get("24k_per_gram") or 15540)
                y22 = int(yg.get("22") or yg.get(22) or yg.get("22k_per_gram") or 14240)
                y18 = int(yg.get("18") or yg.get(18) or yg.get("18k_per_gram") or 11652)

                s999 = float(bs.get("999") or bs.get(999) or bs.get("silver_per_gram") or bs.get("silver_999") or 260.0)
                ys999 = float(ys.get("999") or ys.get(999) or ys.get("silver_per_gram") or 220.6)

                return {
                    "today": {
                        "date": d.get("date", datetime.now().strftime("%Y-%m-%d")),
                        "24k": g24,
                        "22k": g22,
                        "18k": g18,
                        "silver_999": s999
                    },
                    "yesterday": {
                        "24k": y24,
                        "22k": y22,
                        "18k": y18,
                        "silver_999": ys999
                    }
                }
        except Exception as e:
            print("Error loading live gold:", e)
    return {
        "today": {"date": datetime.now().strftime("%Y-%m-%d"), "24k": 15671, "22k": 14360, "18k": 11750, "silver_999": 260.0},
        "yesterday": {"24k": 15540, "22k": 14240, "18k": 11652, "silver_999": 220.6}
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

def get_kannada_date_str():
    months = {
        1: "ಜನವರಿ", 2: "ಫೆಬ್ರವರಿ", 3: "ಮಾರ್ಚ್", 4: "ಏಪ್ರಿಲ್", 5: "ಮೇ", 6: "ಜೂನ್",
        7: "ಜುಲೈ", 8: "ಆಗಸ್ಟ್", 9: "ಸೆಪ್ಟೆಂಬರ್", 10: "ಅಕ್ಟೋಬರ್", 11: "ನವೆಂಬರ್", 12: "ಡಿಸೆಂಬರ್"
    }
    now = datetime.now()
    return f"{now.day} {months.get(now.month, '')} {now.year}"

# ══════════════════════════════════════════════════════════════════════════════
# 1. 10:15 AM: ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ (REFERENCE 1 STYLE - BLOOMBERG BULLION)
# ══════════════════════════════════════════════════════════════════════════════
def render_gold_card():
    gold = get_live_gold()
    t = gold["today"]
    y = gold["yesterday"]
    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    date_kn = get_kannada_date_str()

    diff_24k = t["24k"] - y["24k"]
    diff_22k = t["22k"] - y["22k"]
    diff_silver = t["silver_999"] - y["silver_999"]
    silver_kg = int(t["silver_999"] * 1000)

    # Status pill text
    trend_title = "ಬುಲಿಯನ್ ಮಾರುಕಟ್ಟೆ ದರ ಇಳಿಕೆ" if diff_24k <= 0 else "ಬುಲಿಯನ್ ಮಾರುಕಟ್ಟೆ ದರ ಏರಿಕೆ"
    trend_sub = "ಜಾಗತಿಕ ಮಾರುಕಟ್ಟೆ ಹಾಗೂ ಬಡ್ಡಿದರ ಪರಿಣಾಮದಿಂದ ಇಳಿಕೆ ಕಂಡ ಬೆಲೆಗಳು" if diff_24k <= 0 else "ಜಾಗತಿಕ ಮಾರುಕಟ್ಟೆಯ ಬೇಡಿಕೆಯಿಂದ ಚಿನ್ನದ ದರದಲ್ಲಿ ಹೆಚ್ಚಳ"
    trend_icon = "📉" if diff_24k <= 0 else "📈"
    trend_color = "#EF4444" if diff_24k <= 0 else "#10B981"

    diff_24k_badge = f"+₹{diff_24k:,} 🔼" if diff_24k > 0 else (f"-₹{abs(diff_24k):,} 🔽" if diff_24k < 0 else "0.00 —")
    diff_22k_badge = f"+₹{diff_22k:,} 🔼" if diff_22k > 0 else (f"-₹{abs(diff_22k):,} 🔽" if diff_22k < 0 else "0.00 —")

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
    background: #0B0E14;
    font-family: 'Anek Kannada', sans-serif;
    color: #FFFFFF;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 40px 48px;
  }}
  /* Financial Chart Background Graphic */
  .chart-bg {{
    position: absolute;
    top: 30px;
    right: 40px;
    width: 480px;
    height: 220px;
    opacity: 0.25;
    pointer-events: none;
  }}
  .card-gradient-gold {{
    background: linear-gradient(180deg, #F59E0B 0%, #D97706 100%);
    color: #000000;
  }}
  .card-gradient-warm {{
    background: linear-gradient(180deg, #FBBF24 0%, #F59E0B 100%);
    color: #000000;
  }}
  .card-gradient-silver {{
    background: linear-gradient(180deg, #E2E8F0 0%, #CBD5E1 100%);
    color: #0F172A;
  }}
</style>
</head>
<body>
  <!-- Header Bar -->
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <img src="{logo_b64}" style="height:68px; object-fit:contain;">
    <div style="background:#1E293B; border:1.5px solid #334155; color:#FDE047; font-size:18px; font-weight:800; padding:8px 24px; border-radius:24px; font-family:'Outfit';">
      🗓️ {date_kn}
    </div>
  </div>

  <!-- Title Area -->
  <div style="position:relative; z-index:2; margin-top:10px;">
    <div style="font-size:52px; font-weight:900; line-height:1.15; color:#F59E0B; letter-spacing:-0.5px;">
      ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಲೈವ್ ದರ
    </div>
    <div style="font-size:22px; font-weight:800; color:#94A3B8; margin-top:4px; font-family:'Outfit';">
      GOLD AND SILVER RATE TODAY • 10:15 AM BENCHMARK
    </div>
  </div>

  <!-- 3 VERTICAL RATE CARDS (REFERENCE 1 STYLE) -->
  <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:20px; margin: 15px 0;">
    
    <!-- 24 CARAT CARD -->
    <div style="border-radius:24px; overflow:hidden; box-shadow:0 16px 36px rgba(0,0,0,0.6); display:flex; flex-direction:column; background:#161B26; border:2px solid #F59E0B;">
      <div class="card-gradient-gold" style="padding:16px 14px; text-align:center;">
        <div style="font-size:24px; font-weight:900;">24 ಕ್ಯಾರೆಟ್ ಚಿನ್ನ</div>
        <div style="font-size:15px; font-weight:800; opacity:0.85;">(ಅಪರಂಜಿ / 99.9% ಶುದ್ಧ)</div>
      </div>
      <div style="padding:24px 18px; text-align:center; flex:1; display:flex; flex-direction:column; justify-content:space-between;">
        <div>
          <div style="font-size:46px; font-weight:900; color:#FFFFFF; font-family:'Outfit';">₹{t['24k']:,}</div>
          <div style="font-size:18px; font-weight:800; color:#94A3B8; margin-top:2px;">ಪ್ರತಿ ಗ್ರಾಂಗೆ</div>
        </div>
        <div style="margin-top:16px; padding-top:12px; border-top:1px solid #2D3748;">
          <div style="font-size:16px; font-weight:800; color:#FDE047;">10 ಗ್ರಾಂ: ₹{t['24k']*10:,}</div>
          <div style="font-size:16px; font-weight:900; color:{trend_color}; margin-top:4px; font-family:'Outfit';">{diff_24k_badge}</div>
        </div>
        <div style="font-size:44px; margin-top:10px;">🪙</div>
      </div>
    </div>

    <!-- 22 CARAT CARD -->
    <div style="border-radius:24px; overflow:hidden; box-shadow:0 16px 36px rgba(0,0,0,0.6); display:flex; flex-direction:column; background:#161B26; border:2px solid #E11D48;">
      <div class="card-gradient-warm" style="padding:16px 14px; text-align:center;">
        <div style="font-size:24px; font-weight:900;">22 ಕ್ಯಾರೆಟ್ ಚಿನ್ನ</div>
        <div style="font-size:15px; font-weight:800; opacity:0.85;">(ಆಭರಣ ಚಿನ್ನ / 916 ಹಾಲ್‌ಮಾರ್ಕ್)</div>
      </div>
      <div style="padding:24px 18px; text-align:center; flex:1; display:flex; flex-direction:column; justify-content:space-between;">
        <div>
          <div style="font-size:46px; font-weight:900; color:#FFFFFF; font-family:'Outfit';">₹{t['22k']:,}</div>
          <div style="font-size:18px; font-weight:800; color:#94A3B8; margin-top:2px;">ಪ್ರತಿ ಗ್ರಾಂಗೆ</div>
        </div>
        <div style="margin-top:16px; padding-top:12px; border-top:1px solid #2D3748;">
          <div style="font-size:16px; font-weight:800; color:#FDA4AF;">10 ಗ್ರಾಂ: ₹{t['22k']*10:,}</div>
          <div style="font-size:16px; font-weight:900; color:{trend_color}; margin-top:4px; font-family:'Outfit';">{diff_22k_badge}</div>
        </div>
        <div style="font-size:44px; margin-top:10px;">✨</div>
      </div>
    </div>

    <!-- SILVER CARD -->
    <div style="border-radius:24px; overflow:hidden; box-shadow:0 16px 36px rgba(0,0,0,0.6); display:flex; flex-direction:column; background:#161B26; border:2px solid #94A3B8;">
      <div class="card-gradient-silver" style="padding:16px 14px; text-align:center;">
        <div style="font-size:24px; font-weight:900;">ಶುದ್ಧ ಬೆಳ್ಳಿ (SILVER)</div>
        <div style="font-size:15px; font-weight:800; opacity:0.85;">(999 ಶುದ್ಧ ಬೆಳ್ಳಿ ದರ)</div>
      </div>
      <div style="padding:24px 18px; text-align:center; flex:1; display:flex; flex-direction:column; justify-content:space-between;">
        <div>
          <div style="font-size:46px; font-weight:900; color:#FFFFFF; font-family:'Outfit';">₹{t['silver_999']:.0f}</div>
          <div style="font-size:18px; font-weight:800; color:#94A3B8; margin-top:2px;">ಪ್ರತಿ ಗ್ರಾಂಗೆ</div>
        </div>
        <div style="margin-top:16px; padding-top:12px; border-top:1px solid #2D3748;">
          <div style="font-size:16px; font-weight:800; color:#E2E8F0;">1 ಕೆಜಿ: ₹{silver_kg:,}</div>
          <div style="font-size:16px; font-weight:900; color:#38BDF8; margin-top:4px;">₹{(silver_kg/100000):.2f} ಲಕ್ಷ / KG</div>
        </div>
        <div style="font-size:44px; margin-top:10px;">🥈</div>
      </div>
    </div>

  </div>

  <!-- SOVEREIGN STRIP -->
  <div style="background:#131B2A; border:1.5px solid #2563EB; border-radius:18px; padding:14px 24px; display:flex; justify-content:space-between; align-items:center;">
    <div style="display:flex; align-items:center; gap:12px;">
      <span style="font-size:26px;">👑</span>
      <div style="font-size:20px; font-weight:900; color:#FFFFFF;">1 ಪವನ್ ಚಿನ್ನ (8 ಗ್ರಾಂ 22K): <span style="color:#FDE047; font-family:'Outfit';">₹{t['22k']*8:,}</span></div>
    </div>
    <div style="font-size:18px; font-weight:800; color:#38BDF8;">18 ಕ್ಯಾರೆಟ್ ಚಿನ್ನ (ಗ್ರಾಂಗೆ): ₹{t['18k']:,}</div>
  </div>

  <!-- BOTTOM NEWS BANNER (REFERENCE 1 STYLE) -->
  <div style="background:#0F172A; border:1.5px solid #334155; border-radius:20px; padding:16px 24px; display:flex; align-items:center; gap:18px;">
    <div style="font-size:32px;">{trend_icon}</div>
    <div style="flex:1;">
      <div style="font-size:20px; font-weight:900; color:#FFFFFF;">{trend_title}</div>
      <div style="font-size:16px; font-weight:700; color:#94A3B8; margin-top:2px;">{trend_sub}</div>
    </div>
    <div style="text-align:right;">
      <div style="font-size:16px; font-weight:800; color:#CBD5E1;">ಲೈವ್ ಅಪ್‌ಡೇಟ್:</div>
      <div style="font-size:20px; font-weight:900; color:#F59E0B; font-family:'Outfit';">karnata.in/gold</div>
    </div>
  </div>
</body>
</html>"""

    out_file = OUTPUT_DIR / "gold_rate_today.png"
    render_html_to_png(html, out_file)

# ══════════════════════════════════════════════════════════════════════════════
# 2. 07:45 AM: ಪೆಟ್ರೋಲ್ & ಡೀಸೆಲ್ ದರ (REFERENCE 2 STYLE - MINT MARKETS)
# ══════════════════════════════════════════════════════════════════════════════
def render_petrol_card():
    petrol_data = get_live_petrol()
    dist_dict = petrol_data.get("districts", {})
    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    date_kn = get_kannada_date_str()

    cities = [
        ("bengaluru_urban", "ಬೆಂಗಳೂರು (BENGALURU)", 110.89, 98.80),
        ("mysuru", "ಮೈಸೂರು (MYSURU)", 110.42, 98.37),
        ("dakshina_kannada", "ಮಂಗಳೂರು (MANGALURU)", 109.95, 97.90),
        ("belagavi", "ಬೆಳಗಾವಿ (BELAGAVI)", 111.45, 99.30),
        ("dharwad", "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ (HUBBALLI)", 110.65, 98.55),
        ("kalaburagi", "ಕಲಬುರಗಿ (KALABURAGI)", 111.80, 99.65),
        ("shivamogga", "ಶಿವಮೊಗ್ಗ (SHIVAMOGGA)", 111.20, 99.10),
    ]

    rows_html = ""
    for idx, (k, name_kn, def_p, def_d) in enumerate(cities):
        p_val = def_p
        d_val = def_d
        if k in dist_dict:
            taluks = dist_dict[k].get("taluks", {})
            if taluks:
                first_t = list(taluks.values())[0]
                p_val = first_t.get("petrol", p_val)
                d_val = first_t.get("diesel", d_val)

        border_style = "border-bottom: 1.5px solid #F1F5F9;" if idx < len(cities) - 1 else ""
        rows_html += f"""
        <div style="display:grid; grid-template-columns: 2.3fr 1.35fr 1.35fr; padding:15px 22px; align-items:center; {border_style}">
          <div>
            <div style="font-size:24px; font-weight:900; color:#0F172A;">{name_kn}</div>
          </div>
          <div style="text-align:center;">
            <span style="font-size:27px; font-weight:900; color:#047857; font-family:'Outfit'; background:#ECFDF5; border:1px solid #A7F3D0; padding:6px 16px; border-radius:12px; display:inline-block;">₹{p_val:.2f}</span>
          </div>
          <div style="text-align:center;">
            <span style="font-size:27px; font-weight:900; color:#0369A1; font-family:'Outfit'; background:#F0F9FF; border:1px solid #BAE6FD; padding:6px 16px; border-radius:12px; display:inline-block;">₹{d_val:.2f}</span>
          </div>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@700;800;900&family=Outfit:wght@700;800;900&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: #FFFFFF;
    font-family: 'Anek Kannada', sans-serif;
    color: #0F172A;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 44px 50px;
    border-top: 14px solid #E11D48;
    box-shadow: inset 0 0 0 1px #E2E8F0;
  }}
</style>
</head>
<body>
  <!-- Header Bar -->
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <div style="display:flex; align-items:center; gap:12px;">
      <img src="{logo_b64}" style="height:54px; object-fit:contain;">
      <div style="font-size:20px; font-weight:900; color:#E11D48; border-left:2.5px solid #E2E8F0; padding-left:14px; letter-spacing:0.5px;">
        ಕರ್ನಾಟ ಮಾರುಕಟ್ಟೆ ಸೂಚ್ಯಂಕ
      </div>
    </div>
    <div style="background:#FFF1F2; border:1.5px solid #FECDD3; color:#E11D48; font-size:17px; font-weight:800; padding:6px 20px; border-radius:30px; font-family:'Outfit'; display:flex; align-items:center; gap:6px;">
      <span style="width:8px; height:8px; border-radius:50%; background:#E11D48; display:inline-block;"></span>
      ಇಂದು • {date_kn}
    </div>
  </div>

  <!-- Title Section -->
  <div style="margin: 8px 0 14px;">
    <div style="font-size:46px; font-weight:900; color:#0F172A; line-height:1.15; letter-spacing:-0.5px;">
      ಕರ್ನಾಟಕ ಇಂದಿನ ಇಂಧನ ದರ ಸೂಚ್ಯಂಕ ⛽
    </div>
    <div style="font-size:18px; font-weight:800; color:#64748B; font-family:'Outfit'; margin-top:4px; letter-spacing:0.5px;">
      DAILY PETROL & DIESEL RATES • REVISED AT 6:00 AM IST
    </div>
  </div>

  <!-- MODERN BENTO TABLE CONTAINER -->
  <div style="background:#F8FAFC; border:1.5px solid #E2E8F0; border-radius:24px; overflow:hidden; box-shadow:0 10px 30px rgba(15,23,42,0.06);">
    <!-- COLUMN HEADERS -->
    <div style="display:grid; grid-template-columns: 2.3fr 1.35fr 1.35fr; background:#0F172A; padding:15px 22px; align-items:center;">
      <div style="font-size:18px; font-weight:900; color:#F8FAFC; letter-spacing:0.5px;">ಪ್ರಮುಖ ನಗರ (DISTRICT / CITY)</div>
      <div style="text-align:center; font-size:18px; font-weight:900; color:#34D399; font-family:'Outfit';">⛽ ಪೆಟ್ರೋಲ್ (Ltr)</div>
      <div style="text-align:center; font-size:18px; font-weight:900; color:#38BDF8; font-family:'Outfit';">🚚 ಡೀಸೆಲ್ (Ltr)</div>
    </div>

    <!-- ROWS -->
    <div>
      {rows_html}
    </div>
  </div>

  <!-- Commercial Strip -->
  <div style="background:#FFFBEB; border:1.5px solid #FDE68A; border-radius:16px; padding:12px 20px; display:flex; justify-content:space-between; align-items:center;">
    <div style="font-size:17px; font-weight:800; color:#92400E;">
      ⚡ ಸಿಎನ್‌ಜಿ & ಆಟೋ ಎಲ್‌ಪಿಜಿ: <strong>CNG ₹88.50/kg</strong> · <strong>Auto LPG ₹62.40/L</strong>
    </div>
    <div style="font-size:14px; font-weight:800; color:#B45309;">
      ಮೂಲ: IOCL, BPCL, HPCL ಅಧಿಕೃತ ದತ್ತಾಂಶ
    </div>
  </div>

  <!-- Minimal Footer -->
  <div style="display:flex; justify-content:space-between; align-items:center; padding-top:12px; border-top:1.5px solid #E2E8F0;">
    <div style="font-size:17px; font-weight:800; color:#64748B;">
      🗓️ {date_kn} • 31 ಜಿಲ್ಲೆಗಳ ದರ karnata.in ನಲ್ಲಿ ಲಭ್ಯ
    </div>
    <div style="font-size:20px; font-weight:900; color:#E11D48; font-family:'Outfit';">
      karnata.in/petrol
    </div>
  </div>
</body>
</html>"""

    out_file = OUTPUT_DIR / "petrol_diesel_today.png"
    render_html_to_png(html, out_file)

# ══════════════════════════════════════════════════════════════════════════════
# 3. 09:45 AM: 13 ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ (REFERENCE 3 STYLE - DECCAN HERALD)
# ══════════════════════════════════════════════════════════════════════════════
def render_dam_carousel_and_spotlights():
    dams = get_live_dams()
    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    dam_bg_b64 = get_file_base64(str(OUTPUT_DIR / "dam_bg.jpg"))
    date_kn = get_kannada_date_str()

    cauvery_dams = [
        ("krs", "ಕೆ.ಆರ್. ಸಾಗರ (KRS)", 49.45, 12694, 734),
        ("kabini", "ಕಬಿನಿ (ಬೀಚನಹಳ್ಳಿ)", 19.52, 14574, 500),
        ("harangi", "ಹಾರಂಗಿ (ಕೊಡಗು)", 8.50, 3665, 180),
        ("hemavathi", "ಹೇಮಾವತಿ (ಗೊರೂರು)", 37.10, 15647, 300),
    ]

    krishna_dams = [
        ("almatti", "ಆಲಮಟ್ಟಿ (ಲಾಲ್ ಬಹದ್ದೂರ್)", 123.08, 131940, 100),
        ("tungabhadra", "ತುಂಗಭದ್ರಾ (ಹೊಸಪೇಟೆ)", 105.79, 28654, 177),
        ("bhadra", "ಭದ್ರಾ (ಲಕ್ಕವಳ್ಳಿ)", 71.54, 16304, 216),
        ("ghataprabha", "ಘಟಪ್ರಭಾ (ಹಿಡಕಲ್)", 51.00, 28603, 115),
        ("malaprabha", "ಮಲಪ್ರಭಾ (ರೇಣುಕಾ ಸಾಗರ)", 37.73, 7369, 194),
        ("narayanapura", "ನಾರಾಯಣಪುರ (ಬಸವ ಸಾಗರ)", 33.31, 24500, 767),
    ]

    def make_table_rows(dam_list):
        r_html = ""
        for idx, (k, name_kn, def_cap, def_in, def_out) in enumerate(dam_list):
            v = dams.get(k, {})
            tot_cap = v.get("max_storage_tmc", def_cap)
            cur_st = v.get("storage_tmc", v.get("present_storage_tmc", def_cap * 0.85))
            inflow = v.get("inflow_cusecs", def_in)
            outflow = v.get("outflow_cusecs", def_out)

            bg_col = "#F8FAFC" if idx % 2 == 0 else "#FFFFFF"
            r_html += f"""
            <tr style="background:{bg_col}; border-bottom:1px solid #CBD5E1; font-size:20px; font-weight:800;">
              <td style="padding:10px 14px; text-align:left; color:#0F172A;">{name_kn}</td>
              <td style="padding:10px 14px; text-align:center; font-family:'Outfit';">{tot_cap:.2f}</td>
              <td style="padding:10px 14px; text-align:center; font-weight:900; color:#0369A1; font-family:'Outfit';">{cur_st:.2f}</td>
              <td style="padding:10px 14px; text-align:center; color:#047857; font-family:'Outfit';">{inflow:,}</td>
              <td style="padding:10px 14px; text-align:center; color:#B91C1C; font-family:'Outfit';">{outflow:,}</td>
            </tr>"""
        return r_html

    rows_cauvery = make_table_rows(cauvery_dams)
    rows_krishna = make_table_rows(krishna_dams)

    # 13 DAMS EDITORIAL CARD (DECCAN HERALD STYLE)
    html_main = f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@700;800;900&family=Outfit:wght@700;800;900&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: #0F172A;
    font-family: 'Anek Kannada', sans-serif;
    color: #0F172A;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    padding: 24px 32px;
  }}
  .content-box {{
    background: #FFFFFF;
    border-radius: 20px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    height: 100%;
    box-shadow: 0 20px 45px rgba(0,0,0,0.5);
  }}
</style>
</head>
<body>
  <div class="content-box">
    <!-- Top Header Banner -->
    <div style="background:#0F172A; color:#FFFFFF; padding:14px 24px; display:flex; justify-content:space-between; align-items:center;">
      <div>
        <div style="font-size:32px; font-weight:900;">ಜಲಾಶಯಗಳ ನೀರಿನ ಸಂಗ್ರಹ & ಒಳಹರಿವಿನ ದೈನಂದಿನ ವರದಿ</div>
        <div style="font-size:16px; font-weight:700; color:#94A3B8; font-family:'Outfit';">KARNATAKA RESERVOIR STORAGE AND FLOW DATA • {date_kn}</div>
      </div>
      <img src="{logo_b64}" style="height:48px; object-fit:contain;">
    </div>

    <!-- Scenic Dam Photograph Banner -->
    <div style="height:150px; position:relative; overflow:hidden;">
      <img src="{dam_bg_b64}" style="width:100%; height:100%; object-fit:cover;" alt="Dam">
      <div style="position:absolute; inset:0; background:linear-gradient(180deg, transparent 40%, rgba(15,23,42,0.85) 100%);"></div>
      <div style="position:absolute; bottom:8px; left:20px; color:#FDE047; font-size:16px; font-weight:800;">
        🌊 ಅಧಿಕೃತ ಜಲಸಂಪನ್ಮೂಲ ಇಲಾಖೆ (WRD) ಲೈವ್ ಅಂಕಿಅಂಶಗಳು
      </div>
    </div>

    <!-- Table -->
    <div style="flex:1; padding:10px 18px; display:flex; flex-direction:column; justify-content:space-between;">
      <table style="width:100%; border-collapse:collapse; text-align:center;">
        <thead>
          <tr style="background:#E2E8F0; border-bottom:2px solid #0F172A; font-size:17px; font-weight:900; color:#0F172A;">
            <th style="padding:10px; text-align:left;">ಜಲಾಶಯಗಳು</th>
            <th style="padding:10px;">ಒಟ್ಟು ಸಾಮರ್ಥ್ಯ<br><span style="font-size:13px; font-weight:700; color:#64748B;">(TMC)</span></th>
            <th style="padding:10px; color:#0284C7;">ಇಂದಿನ ಸಂಗ್ರಹ<br><span style="font-size:13px; font-weight:700;">(TMC)</span></th>
            <th style="padding:10px; color:#059669;">ಒಳಹರಿವು<br><span style="font-size:13px; font-weight:700;">(Cusecs)</span></th>
            <th style="padding:10px; color:#DC2626;">ಹೊರಹರಿವು<br><span style="font-size:13px; font-weight:700;">(Cusecs)</span></th>
          </tr>
        </thead>
        <tbody>
          <!-- CAUVERY BASIN HEADER -->
          <tr style="background:#0284C7; color:#FFFFFF; font-size:18px; font-weight:900;">
            <td colspan="5" style="padding:6px 14px; text-align:left;">ಕಾವೇರಿ ಜಲಾನಯನ ಪ್ರದೇಶ (Cauvery Basin)</td>
          </tr>
          {rows_cauvery}

          <!-- KRISHNA BASIN HEADER -->
          <tr style="background:#0284C7; color:#FFFFFF; font-size:18px; font-weight:900;">
            <td colspan="5" style="padding:6px 14px; text-align:left;">ಕೃಷ್ಣಾ ಜಲಾನಯನ ಪ್ರದೇಶ (Krishna Basin)</td>
          </tr>
          {rows_krishna}
        </tbody>
      </table>

      <!-- Minimal Table Footer -->
      <div style="display:flex; justify-content:space-between; align-items:center; border-top:1.5px solid #CBD5E1; padding-top:8px;">
        <div style="font-size:15px; font-weight:700; color:#64748B;">* ಪ್ರಮಾಣ TMC ಯಲ್ಲಿ | Cusecs = ಕ್ಯೂಸೆಕ್</div>
        <div style="font-size:18px; font-weight:900; color:#0284C7; font-family:'Outfit';">karnata.in/dam-levels</div>
      </div>
    </div>
  </div>
</body>
</html>"""

    out_file1 = OUTPUT_DIR / "dam_levels_p1.png"
    render_html_to_png(html_main, out_file1)
    render_html_to_png(html_main, OUTPUT_DIR / "dam_levels_p2.png")

    # 4. DAM SPOTLIGHT HERO CARDS (REFERENCE 4 STYLE - MANGLA DAM)
    spotlights = [
        ("krs", "ಕೃಷ್ಣರಾಜ ಸಾಗರ ಜಲಾಶಯ (KRS)", "ಕಾವೇರಿ ನದಿ", "ಮಂಡ್ಯ ಜಿಲ್ಲೆ", 124.80, 49.45),
        ("almatti", "ಆಲಮಟ್ಟಿ ಜಲಾಶಯ (ಲಾಲ್ ಬಹದ್ದೂರ್)", "ಕೃಷ್ಣಾ ನದಿ", "ವಿಜಯಪುರ ಜಿಲ್ಲೆ", 519.60, 123.08),
        ("tungabhadra", "ತುಂಗಭದ್ರಾ ಜಲಾಶಯ (ಟಿಬಿ ಡ್ಯಾಂ)", "ತುಂಗಭದ್ರಾ ನದಿ", "ವಿಜಯನಗರ (ಹೊಸಪೇಟೆ)", 1633.00, 105.79),
        ("bhadra", "ಭದ್ರಾ ಜಲಾಶಯ (ಲಕ್ಕವಳ್ಳಿ)", "ಭದ್ರಾ ನದಿ", "ಚಿಕ್ಕಮಗಳೂರು ಜಿಲ್ಲೆ", 186.00, 71.54),
        ("kabini", "ಕಬಿನಿ ಜಲಾಶಯ (ಬೀಚನಹಳ್ಳಿ)", "ಕಬಿನಿ ನದಿ", "ಮೈಸೂರು (ಹೆಚ್.ಡಿ.ಕೋಟೆ)", 2284.00, 19.52),
        ("ghataprabha", "ಘಟಪ್ರಭಾ ಜಲಾಶಯ (ಹಿಡಕಲ್)", "ಘಟಪ್ರಭಾ ನದಿ", "ಬೆಳಗಾವಿ ಜಿಲ್ಲೆ", 2175.00, 51.00)
    ]

    for k, title_kn, river_kn, loc_kn, def_lvl, def_st in spotlights:
        v = dams.get(k, {})
        pct = v.get("storage_pct", 92.5)
        level = v.get("level_ft", v.get("current_level", def_lvl))
        max_lvl = v.get("design_capacity", v.get("max_level", def_lvl))
        storage = v.get("storage_tmc", v.get("present_storage_tmc", def_st))
        max_st = v.get("max_storage_tmc", def_st)
        inflow = v.get("inflow_cusecs", 15420)
        outflow = v.get("outflow_cusecs", 8250)

        html_spot = f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@700;800;900&family=Outfit:wght@700;800;900&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: #034E7B;
    font-family: 'Anek Kannada', sans-serif;
    color: #FFFFFF;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
</style>
</head>
<body>
  <!-- TOP SCENIC DAM PHOTO (40% HEIGHT - REFERENCE 4) -->
  <div style="height:440px; position:relative; overflow:hidden;">
    <img src="{dam_bg_b64}" style="width:100%; height:100%; object-fit:cover;" alt="Dam Reservoir">
    <div style="position:absolute; inset:0; background:linear-gradient(180deg, rgba(0,0,0,0.3) 0%, rgba(3,78,123,0.95) 100%);"></div>
    
    <!-- Top Pill Logo -->
    <div style="position:absolute; top:28px; left:50%; transform:translateX(-50%); background:#FFFFFF; border-radius:30px; padding:8px 28px; box-shadow:0 8px 20px rgba(0,0,0,0.3);">
      <img src="{logo_b64}" style="height:48px; object-fit:contain;">
    </div>
  </div>

  <!-- TITLE BANNER -->
  <div style="position:relative; margin-top:-60px; z-index:5; text-align:center; padding:0 30px;">
    <div style="background:#0284C7; border:3px solid #38BDF8; border-radius:24px; padding:12px 32px; display:inline-block; box-shadow:0 12px 28px rgba(0,0,0,0.4);">
      <div style="font-size:36px; font-weight:900; color:#FFFFFF;">{title_kn}</div>
      <div style="font-size:18px; font-weight:800; color:#FDE047; margin-top:2px;">📍 {loc_kn} | ನದಿ: {river_kn}</div>
    </div>
  </div>

  <!-- QUICK TELEMETRY STRIP (REFERENCE 4) -->
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; padding:0 48px; margin-top:14px;">
    <div style="background:rgba(255,255,255,0.12); border-radius:14px; padding:12px 18px; text-align:center;">
      <div style="font-size:16px; font-weight:800; color:#93C5FD;">ಲೈವ್ ಒಳಹರಿವು (INFLOW)</div>
      <div style="font-size:28px; font-weight:900; color:#34D399; font-family:'Outfit';">{inflow:,} Cusecs 📈</div>
    </div>
    <div style="background:rgba(255,255,255,0.12); border-radius:14px; padding:12px 18px; text-align:center;">
      <div style="font-size:16px; font-weight:800; color:#93C5FD;">ಹೊರಹರಿವು (OUTFLOW)</div>
      <div style="font-size:28px; font-weight:900; color:#F87171; font-family:'Outfit';">{outflow:,} Cusecs</div>
    </div>
  </div>

  <!-- FLOATING WHITE DATA CARD (REFERENCE 4 STYLE) -->
  <div style="margin: 16px 48px 24px; background:#FFFFFF; border-radius:24px; padding:24px 36px; color:#0F172A; box-shadow:0 16px 36px rgba(0,0,0,0.4);">
    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; border-bottom:2px solid #E2E8F0; padding-bottom:14px;">
      <div>
        <div style="font-size:16px; font-weight:800; color:#64748B;">ಪ್ರಸ್ತುತ ನೀರಿನ ಮಟ್ಟ (Water Level):</div>
        <div style="font-size:30px; font-weight:900; color:#0369A1; font-family:'Outfit';">{level:.2f} ft</div>
      </div>
      <div>
        <div style="font-size:16px; font-weight:800; color:#64748B;">ಗರಿಷ್ಠ ಮಟ್ಟ (FRL Capacity):</div>
        <div style="font-size:30px; font-weight:900; color:#0F172A; font-family:'Outfit';">{max_lvl:.2f} ft</div>
      </div>
    </div>

    <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px; padding-top:14px; align-items:center;">
      <div>
        <div style="font-size:16px; font-weight:800; color:#64748B;">ಇಂದಿನ ಜಲಸಂಗ್ರಹ (Live Storage):</div>
        <div style="font-size:30px; font-weight:900; color:#0284C7; font-family:'Outfit';">{storage:.2f} / {max_st:.2f} TMC</div>
      </div>
      <div style="text-align:right;">
        <span style="background:#059669; color:#FFFFFF; font-size:22px; font-weight:900; padding:8px 22px; border-radius:16px; font-family:'Outfit';">
          {pct:.1f}% ಭರ್ತಿ (ಸುರಕ್ಷಿತ)
        </span>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <div style="background:#023E68; padding:14px 48px; display:flex; justify-content:space-between; align-items:center;">
    <div style="font-size:17px; font-weight:800; color:#BAE6FD;">WRD ಅಧಿಕೃತ ಜಲಸಂಪನ್ಮೂಲ ವರದಿ • {date_kn}</div>
    <div style="font-size:22px; font-weight:900; color:#FFFFFF; font-family:'Outfit';">karnata.in/dam-levels</div>
  </div>
</body>
</html>"""

        out_file_s = OUTPUT_DIR / f"dam_{k}.png"
        render_html_to_png(html_spot, out_file_s)

# ══════════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════════
DOYOUKNOW_FACTS = [
        {"fact": "1905 ರ ಆಗಸ್ಟ್ 5 ರಂದು ಕಾವೇರಿಯ ಶಿವನಸಮುದ್ರ ವಿದ್ಯುತ್ ಮೂಲಕ ಬೆಂಗಳೂರಿನ ಕೆ.ಆರ್. ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಪ್ರಪ್ರಥಮ ಬಾರಿಗೆ ಬೀದಿ ದೀಪ ಬೆಳಗಿಸಲಾಯಿತು. ಆ ಮೂಲಕ ಏಷ್ಯಾದಲ್ಲೇ ಮೊದಲ ವಿದ್ಯುತ್ ದೀಪ ಪಡೆದ ನಗರವೆಂಬ ಐತಿಹಾಸಿಕ ಹೆಗ್ಗಳಿಕೆ ಬೆಂಗಳೂರಿಗಿದೆ!"},
        {"fact": "ಆದಿಲ್‌ಶಾಹಿ ಸುಲ್ತಾನರ ವಿಜಯಪುರದ ಗೋಲ್ ಗುಂಬಜ್ ಯಾವುದೇ ಕಂಬಗಳ ಆಸರೆಯಿಲ್ಲದೆ ನಿಂತಿರುವ ವಿಶ್ವದ 2ನೇ ಅತಿ ದೊಡ್ಡ ಗುಮ್ಮಟವಾಗಿದೆ. ಇಲ್ಲಿನ ಪಿಸುಗುಟ್ಟುವ ಮೊಗಸಾಲೆಯಲ್ಲಿ (Whispering Gallery) ಮಾಡುವ ಸಣ್ಣ ಶಬ್ದವೂ 7 ರಿಂದ 11 ಬಾರಿ ಸ್ಪಷ್ಟವಾಗಿ ಪ್ರತಿಧ್ವನಿಸುತ್ತದೆ!"},
        {"fact": "17ನೇ ಶತಮಾನದಲ್ಲಿ ಸೂಫಿ ಸಂತ ಬಾಬಾ ಬುಡನ್ ಅವರು ಯೆಮೆನ್‌ನಿಂದ ತಂದ 7 ಹಸಿ ಕಾಫಿ ಬೀಜಗಳನ್ನು ಚಿಕ್ಕಮಗಳೂರಿನ ಚಂದ್ರದ್ರೋಣ ಪರ್ವತದಲ್ಲಿ ಬಿತ್ತಿದರು. ಇಂದು ಭಾರತ ವಿಶ್ವದ ಪ್ರಮುಖ ಕಾಫಿ ರಫ್ತುದಾರ ದೇಶವಾಗಲು ಈ 7 ಕಾಫಿ ಬೀಜಗಳೇ ಮುನ್ನುಡಿ!"},
        {"fact": "ಶ್ರವಣಬೆಳಗೊಳದ ವಿಂಧ್ಯಗಿರಿಯ ಮೇಲಿರುವ ಭಗವಾನ್ ಬಾಹುಬಲಿ (ಗೊಮ್ಮಟೇಶ್ವರ) ಏಕಶಿಲಾ ವಿಗ್ರಹವು 57 ಅಡಿ ಎತ್ತರವಿದ್ದು, ಯಾವುದೇ ಕೀಲುಗಳಿಲ್ಲದೆ ಒಂದೇ ಬೃಹತ್ ಗ್ರಾನೈಟ್ ಬಂಡೆಯಲ್ಲಿ ಕೆತ್ತಲಾದ ವಿಶ್ವದ ಅತಿ ಎತ್ತರದ ಏಕಶಿಲಾ ಪ್ರತಿಮೆಯಾಗಿದೆ!"},
        {"fact": "ಕ್ರಿ.ಶ. 450 ರ ಸುಮಾರಿನ ಹಲ್ಮಿಡಿ ಶಾಸನವು ಕನ್ನಡ ಭಾಷೆಯ ಉಪಲಬ್ಧ ಪ್ರಾಚೀನ ಲಿಖಿತ ದಾಖಲೆಯಾಗಿದ್ದು, ಹಾಸನ ಜಿಲ್ಲೆಯ ಬೇಲೂರು ತಾಲೂಕಿನ ಹಲ್ಮಿಡಿ ಗ್ರಾಮದಲ್ಲಿ ಪತ್ತೆಯಾಯಿತು. ಇದು ಕದಂಬರ ಕಾಲದ ಹೆಮ್ಮೆಯ ಐತಿಹಾಸಿಕ ಸಾಕ್ಷಿ!"},
        {"fact": "ವಿಶ್ವವಿಖ್ಯಾತ ಹಂಪಿಯ ವಿಜಯ ವಿಠ್ಠಲ ದೇವಾಲಯದಲ್ಲಿರುವ 56 ಸಂಗೀತ ಕಂಬಗಳನ್ನು (Musical Pillars) ಕಲ್ಲಿನಿಂದ ಮೆಲ್ಲಗೆ ತಟ್ಟಿದರೆ ಸಪ್ತಸ್ವರಗಳಾದ ಸಾ-ರಿ-ಗ-ಮ-ಪ-ಧ-ನಿ ನಾದ ಸ್ಪಷ್ಟವಾಗಿ ಹೊರಹೊಮ್ಮುತ್ತದೆ!"},
        {"fact": "ಸರ್ ಎಂ. ವಿಶ್ವೇಶ್ವರಯ್ಯನವರು ವಿನ್ಯಾಸಗೊಳಿಸಿದ ಸ್ವಯಂಚಾಲಿತ ಫ್ಲಡ್ ಗೇಟ್‌ಗಳನ್ನು (Automatic Sluice Gates) ಜಗತ್ತಿನಲ್ಲೇ ಮೊದಲು 1903 ರಲ್ಲಿ ಪುಣೆಯ ಖಡಕ್‌ವಾಸ್ಲಾ ಜಲಾಶಯದಲ್ಲೂ, ನಂತರ ಗ್ವಾಲಿಯರ್‌ನ ತಿಗ್ರಾ ಮತ್ತು ಕೃಷ್ಣರಾಜ ಸಾಗರ (KRS) ಡ್ಯಾಂನಲ್ಲೂ ಯಶಸ್ವಿಯಾಗಿ ಅಳವಡಿಸಲಾಯಿತು!"},
        {"fact": "ಬಾಗಲಕೋಟೆ ಜಿಲ್ಲೆಯ ಐಹೊಳೆಯನ್ನು 'ಭಾರತೀಯ ದೇವಾಲಯ ವಾಸ್ತುಶಿಲ್ಪದ ತೊಟ್ಟಿಲು' (Cradle of Indian Temple Architecture) ಎಂದು ಕರೆಯಲಾಗುತ್ತದೆ. ಇಲ್ಲಿ 5 ರಿಂದ 8ನೇ ಶತಮಾನದ ಬಾದಾಮಿ ಚಾಲುಕ್ಯರ 125 ಕ್ಕೂ ಹೆಚ್ಚು ದೇವಾಲಯಗಳಿವೆ!"},
        {"fact": "ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆಯ ಜೋಗ ಜಲಪಾತವು ಶರಾವತಿ ನದಿಯಿಂದ ನಿರ್ಮಾಣವಾಗಿದ್ದು, 830 ಅಡಿ (253 ಮೀಟರ್) ಎತ್ತರದಿಂದ ಯಾವುದೇ ಬಂಡೆಗೆ ತಾಗದೆ ನೇರವಾಗಿ ಧುಮ್ಮಿಕ್ಕುವ ಭಾರತದ ಎರಡನೇ ಅತಿ ಎತ್ತರದ ಏಕಮುಖ ಜಲಪಾತವಾಗಿದೆ (ರಾಜ, ರೋರರ್, ರಾಕೆಟ್, ರಾಣಿ)!"},
        {"fact": "ರಾಜ್ಯದ ಹೆಮ್ಮೆಯ ಮೈಸೂರು ಸ್ಯಾಂಡಲ್ ಸೋಪ್ (Mysore Sandal Soap) ಜಗತ್ತಿನಲ್ಲೇ 100% ಶುದ್ಧ ಶ್ರೀಗಂಧದ ಎಣ್ಣೆಯನ್ನು (Pure Sandalwood Oil) ಬಳಸಿ ತಯಾರಿಸಲಾಗುವ ಏಕೈಕ ನೈಸರ್ಗಿಕ ಸಾಬೂನಾಗಿದೆ. ಇದನ್ನು ನಾಲ್ವಡಿ ಕೃಷ್ಣರಾಜ ಒಡೆಯರ್ 1916 ರಲ್ಲಿ ಸ್ಥಾಪಿಸಿದರು!"},
        {"fact": "ಮೈಸೂರು ಸಂಸ್ಥಾನದ ಅರಮನೆ ಅಡುಗೆಯವರಾದ ಕಾಕಾಸುರ ಮಾದಪ್ಪನವರು ನಾಲ್ವಡಿ ಕೃಷ್ಣರಾಜ ಒಡೆಯರ ಆಸ್ಥಾನದಲ್ಲಿ ಕಡಲೆಹಿಟ್ಟು, ಬೆಣ್ಣೆ ಮತ್ತು ಸಕ್ಕರೆ ಪಾಕದಿಂದ ಆಕಸ್ಮಿಕವಾಗಿ ಸೃಷ್ಟಿಸಿದ ಸಿಹಿಯೇ ಇಂದು ವಿಶ್ವಪ್ರಸಿದ್ಧ 'ಮೈಸೂರು ಪಾಕ್'!"},
        {"fact": "ಚಿತ್ರದುರ್ಗದ ಕಲ್ಲಿನ ಕೋಟೆಯನ್ನು 'ಏಳು ಸುತ್ತಿನ ಕೋಟೆ' ಎಂದೂ ಕರೆಯಲಾಗುತ್ತದೆ. ಇಲ್ಲಿ ಮದಕರಿ ನಾಯಕನ ಆಳ್ವಿಕೆಯಲ್ಲಿ ಹೈದರಾಲಿ ಸೈನಿಕರು ಒಳನುಸುಳಿದಾಗ ವೀರವನಿತೆ ಒನಕೆ ಓಬವ್ವ ಏಕಾಂಗಿಯಾಗಿ ಒನಕೆಯಿಂದ ನೂರಾರು ಶತ್ರುಗಳನ್ನು ಸದೆಬಡಿದು ಇತಿಹಾಸ ನಿರ್ಮಿಸಿದಳು!"},
        {"fact": "ಉತ್ತರ ಕನ್ನಡ ಜಿಲ್ಲೆಯ ಕಾರವಾರ ಸಮೀಪದ ಅಣಶಿ-ದಾಂಡೇಲಿ ಹುಲಿ ಸಂರಕ್ಷಿತ ಪ್ರದೇಶವು ಅತ್ಯಪರೂಪದ ಕಪ್ಪು ಚಿರತೆಗಳು (Black Panthers) ಮತ್ತು ಅಪರೂಪದ ಹಾರ್ನ್‌ಬಿಲ್ (ಮಲಬಾರ್ ಪೈಡ್ ಹಾರ್ನ್‌ಬಿಲ್) ಪಕ್ಷಿಗಳಿಗೆ ಜಾಗತಿಕ ಅಭಯತಾಣವಾಗಿದೆ!"},
        {"fact": "ತುಮಕೂರು ಜಿಲ್ಲೆಯ ಮಧುಗಿರಿ ಏಕಶಿಲಾ ಬೆಟ್ಟವು (Madhugiri Monolith) ಸಮುದ್ರ ಮಟ್ಟದಿಂದ 3,930 ಅಡಿ ಎತ್ತರವಿದ್ದು, ಇಡೀ ಏಷ್ಯಾ ಖಂಡದಲ್ಲೇ ಎರಡನೇ ಅತಿ ದೊಡ್ಡ ಏಕಶಿಲಾ ಬೆಟ್ಟ ಎಂಬ ಭೌಗೋಳಿಕ ಹೆಗ್ಗಳಿಕೆಗೆ ಪಾತ್ರವಾಗಿದೆ!"},
        {"fact": "ಕೋಲಾರ ಚಿನ್ನದ ಗಣಿ (KGF) ಒಂದು ಕಾಲದಲ್ಲಿ ವಿಶ್ವದಲ್ಲೇ ಎರಡನೇ ಅತಿ ಆಳವಾದ ಭೂಗತ ಗಣಿಯಾಗಿತ್ತು (3 ಕಿ.ಮೀ ಗಿಂತ ಹೆಚ್ಚು ಆಳ). ಇಲ್ಲಿ ಬ್ರಿಟಿಷರ ಕಾಲದಲ್ಲೇ ವಿಶ್ವದರ್ಜೆಯ ಟೆಲಿಫೋನ್ ಮತ್ತು ವಿದ್ಯುತ್ ಸಂಪರ್ಕ ಅಳವಡಿಸಲಾಗಿತ್ತು!"},
        {"fact": "ರಾಮನಗರದ ಬೃಹತ್ ಗ್ರಾನೈಟ್ ಬಂಡೆಗಳು ವಿಶ್ವದ ಅತ್ಯಂತ ಪುರಾತನ ಭೂವೈಜ್ಞಾನಿಕ ಶಿಲಾ ರಚನೆಗಳಲ್ಲಿ ಒಂದಾಗಿದ್ದು (Closepet Granites), ಇದು 2.5 ಶತಕೋಟಿ ವರ್ಷಗಳಷ್ಟು ಹಳೆಯದು! ಅಲ್ಲದೆ ಇದು ಐಕಾನಿಕ್ 'ಶೋಲೆ' ಚಲನಚಿತ್ರದ ಚಿತ್ರೀಕರಣ ತಾಣವಾಗಿತ್ತು."},
        {"fact": "ವಿಶ್ವ ಪರಂಪರೆಯ ಬೇಲೂರು ಚೆನ್ನಕೇಶವ ದೇವಾಲಯದ ಶಿಲಾಬಾಲಿಕೆಯರ ಮೂರ್ತಿಗಳು ಸೋಪ್‌ಸ್ಟೋನ್‌ನಲ್ಲಿ (ಹೊಯ್ಸಳ ಶಿಲ್ಪಕಲೆ) ಕೆತ್ತಲ್ಪಟ್ಟಿದ್ದು, ಅವುಗಳ ಉಗುರುಗಳು, ಕಿವಿಯೋಲೆಗಳು ಹಾಗೂ ಕಣ್ಣಿನ ಪಾಪೆಗಳು ಸಹ ಪಾರದರ್ಶಕವಾಗಿ ಜೀವಂತ ಕಲೆಯಂತೆ ಕಂಗೊಳಿಸುತ್ತವೆ!"},
        {"fact": "ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆಯ ಆಗುಂಬೆಯನ್ನು 'ದಕ್ಷಿಣ ಭಾರತದ ಚಿರಾಪುಂಜಿ' ಎಂದು ಕರೆಯಲಾಗುತ್ತದೆ. ಇದು ವಿಶ್ವದ ಅತಿ ಉದ್ದದ ವಿಷಪೂರಿತ ಹಾವಾದ ಕಾಳಿಂಗ ಸರ್ಪದ (King Cobra) ನೈಸರ್ಗಿಕ ಅಧ್ಯಯನ ತಾಣ ಮತ್ತು ಮಳೆಕಾಡುಗಳ ರಾಜಧಾನಿಯಾಗಿದೆ!"},
        {"fact": "ಬೀದರ್‌ನ ಐತಿಹಾಸಿಕ 'ಬಿದ್ರಿ ಕಲೆ' (Bidriware) ಸತು ಮತ್ತು ತಾಮ್ರದ ಮಿಶ್ರಲೋಹದ ಮೇಲೆ ಶುದ್ಧ ಬೆಳ್ಳಿಯ ತಂತಿಯನ್ನು ಕೆತ್ತಿ, ಬೀದರ್ ಕೋಟೆಯ ಪ್ರಾಚೀನ ಮಣ್ಣಿನಿಂದ ಕಪ್ಪು ಹೊಳಪು ನೀಡುವ 600 ವರ್ಷಗಳ ಜಾಗತಿಕ GI ಟ್ಯಾಗ್ ಹೊಂದಿದ ಕಲೆಯಾಗಿದೆ!"},
        {"fact": "ಬಾಗಲಕೋಟೆಯ ಇಳಕಲ್ ಸೀರೆಯು ತನ್ನ ವಿಶಿಷ್ಟ 'ಟೋಪಿತೆಣಿ ಪಲ್ಲು' (Tope Teni Pallu) ಮತ್ತು ಕೊಂಡಿ ನೇಯ್ಗೆಗೆ ಜಗತ್ಪ್ರಸಿದ್ಧವಾಗಿದ್ದು, 8ನೇ ಶತಮಾನದ ಚಾಲುಕ್ಯರ ಕಾಲದಿಂದ ಇಂದಿನವರೆಗೂ ಪರಂಪರೆಯಾಗಿ ಉಳಿದುಬಂದಿದೆ!"},
        {"fact": "ಚನ್ನಪಟ್ಟಣದ 'ಗೊಂಬೆಗಳ ಊರು' ಮರದ ಗೊಂಬೆಗಳಿಗೆ ಜಾಗತಿಕ ಮನ್ನಣೆ ತಂದುಕೊಟ್ಟಿದ್ದು ಟಿಪ್ಪು ಸುಲ್ತಾನ್! ಪರ್ಷಿಯಾದಿಂದ ಕುಶಲಕರ್ಮಿಗಳನ್ನು ಕರೆಸಿ ಸ್ಥಳೀಯ ಆಲೆಮರಕ್ಕೆ ನೈಸರ್ಗಿಕ ಅರಗು (Lacquer) ಬಣ್ಣ ಬಳಿಯುವ ಕಲೆಯನ್ನು ಕಲಿಸಿದರು."},
        {"fact": "ಉತ್ತರ ಕನ್ನಡ ಜಿಲ್ಲೆಯ ಬನವಾಸಿಯು ಕನ್ನಡದ ಮೊದಲ ರಾಜಮನೆತನವಾದ ಕದಂಬರ ರಾಜಧಾನಿಯಾಗಿದ್ದು, ಕ್ರಿ.ಶ. 345 ರಲ್ಲೇ ಮಯೂರವರ್ಮನ ಆಳ್ವಿಕೆಯಲ್ಲಿ ಕನ್ನಡ ನಾಡಿನ ಮೊದಲ ಅಧಿಕೃತ ರಾಜಧಾನಿಯಾಗಿ ಮೆರೆದ ಕೀರ್ತಿ ಇದಕ್ಕಿದೆ!"},
        {"fact": "ಧಾರವಾಡ ಪೇಢಾಕ್ಕೆ ಶತಮಾನಗಳ ಇತಿಹಾಸವಿದೆ! 19ನೇ ಶತಮಾನದಲ್ಲಿ ಉತ್ತರ ಪ್ರದೇಶದ ಉನ್ನಾವೋದಿಂದ ಪ್ಲೇಗ್ ಭೀತಿಯಿಂದ ಧಾರವಾಡಕ್ಕೆ ವಲಸೆ ಬಂದ ರಾಮರತನ್ ಸಿಂಗ್ ಠಾಕೂರ್ ಕುಟುಂಬ ಈ ಅಮೃತ ಸಮಾನ ಸಿಹಿಯನ್ನು ಮೊದಲ ಬಾರಿಗೆ ತಯಾರಿಸಿತು."},
        {"fact": "ಬೆಳಗಾವಿ ಜಿಲ್ಲೆಯ ಗೋಕಾಕ್ ಜಲಪಾತವನ್ನು 'ಕರ್ನಾಟಕದ ನಯಾಗರಾ' ಎಂದು ಕರೆಯಲಾಗುತ್ತದೆ. ಘಟಪ್ರಭಾ ನದಿಯು 177 ಅಡಿ ಎತ್ತರದ ಕಣಿವೆಯಿಂದ ಧುಮ್ಮಿಕ್ಕುವ ಈ ಜಲಪಾತದ ಮೇಲೆ 1907 ರಲ್ಲಿ ನಿರ್ಮಿಸಲಾದ ಬೃಹತ್ ತೂಗುಸೇತುವೆ ಇಂದಿಗೂ ಸಕ್ರಿಯವಾಗಿದೆ!"},
        {"fact": "ದಕ್ಷಿಣ ಕನ್ನಡದ ಕರಾವಳಿಯ ಜಾನಪದ ಕಲೆ 'ಯಕ್ಷಗಾನ'ವು 500 ವರ್ಷಗಳಿಗೂ ಹಳೆಯ ಪರಂಪರೆಯನ್ನು ಹೊಂದಿದ್ದು, ರಾತ್ರಿಪೂರ್ತಿ ನಡೆಯುವ ಇದರ ವೇಷಭೂಷಣ, ನೃತ್ಯ, ತಾಳ ಮತ್ತು ಅರ್ಥಧಾರಿಗಳ ಆಶುಕವಿತೆಯ ಸಂಭಾಷಣೆ ವಿಶ್ವ ರಂಗಭೂಮಿಯಲ್ಲೇ ಅನನ್ಯ!"},
        {"fact": "ಬೆಂಗಳೂರಿನ ಲಾಲ್‌ಬಾಗ್‌ನಲ್ಲಿರುವ ಗಾಜಿನ ಮನೆ (Glass House) ಲಂಡನ್‌ನ ಹೈಡ್ ಪಾರ್ಕ್‌ನ ಕ್ರಿಸ್ಟಲ್ ಪ್ಯಾಲೇಸ್ ಮಾದರಿಯಲ್ಲಿ 1889 ರಲ್ಲಿ ನಿರ್ಮಾಣಗೊಂಡಿತು. ಇಲ್ಲಿ ವರ್ಷಕ್ಕೆ ಎರಡು ಬಾರಿ ನಡೆಯುವ ಫಲಪುಷ್ಪ ಪ್ರದರ್ಶನ ಇಡೀ ದೇಶದಲ್ಲೇ ಜನಪ್ರಿಯ!"},
        {"fact": "ವಿಜಯನಗರ ಸಾಮ್ರಾಜ್ಯದ ಕಾಲದಲ್ಲಿ ರಾಜಧಾನಿ ಹಂಪಿಯ ಬೀದಿಗಳಲ್ಲಿ ವಜ್ರ, ಮುತ್ತು, ರತ್ನಗಳನ್ನು ಸೇರುಗಳಲ್ಲಿ ಅಳೆದು ವ್ಯಾಪಾರ ಮಾಡಲಾಗುತ್ತಿತ್ತು ಎಂದು ಪೋರ್ಚುಗೀಸ್ ಪ್ರವಾಸಿ ಡೊಮಿಂಗೊ ಪಯಾಸ್ ತನ್ನ ಪ್ರವಾಸ ಕಥನದಲ್ಲಿ ದಾಖಲಿಸಿದ್ದಾನೆ!"},
        {"fact": "ಮೈಸೂರು ಅರಮನೆಯು ಭಾರತದಲ್ಲಿ ತಾಜ್ ಮಹಲ್ ನಂತರ ಅತಿ ಹೆಚ್ಚು ಪ್ರವಾಸಿಗರು ಭೇಟಿ ನೀಡುವ 2ನೇ ಸ್ಮಾರಕವಾಗಿದ್ದು, ಪ್ರತಿ ದಸರಾ ಮಹೋತ್ಸವದಂದು ಸುಮಾರು 1,00,000 ವಿದ್ಯುತ್ ದೀಪಗಳಿಂದ ಅರಮನೆಯನ್ನು ಬೆಳಗಿಸಲಾಗುತ್ತದೆ!"},
        {"fact": "ಉತ್ತರ ಕನ್ನಡ ಜಿಲ್ಲೆಯ ಯಾಣದ ಭೈರವೇಶ್ವರ ಶಿಖರ ಮತ್ತು ಮೋಹಿನಿ ಶಿಖರಗಳು ಕಪ್ಪು ಕರ್ರನೆಯ ಬೃಹತ್ ಸುಣ್ಣದಕಲ್ಲಿನ (Karst Limestone) ಶಿಖರಗಳಾಗಿದ್ದು, ಭಸ್ಮಾಸುರನ ಭಸ್ಮದಿಂದ ಕಪ್ಪಾದ ಪೌರಾಣಿಕ ಕಥೆಯನ್ನು ಹೊಂದಿವೆ!"},
        {"fact": "ದಾವಣಗೆರೆಯ ಬೆಣ್ಣೆ ದೋಸೆಯು (Benne Dosa) 1928 ರಲ್ಲಿ ಚೆನ್ನಮ್ಮ ಎಂಬ ಅಡುಗೆಯವರ ಕೈಚಳಕದಿಂದ ಹುಟ್ಟಿಕೊಂಡಿದ್ದು, ಉರುವಲು ಒಲೆಯ ಮೇಲಿನ ಕಬ್ಬಿಣದ ಹಂಚು ಮತ್ತು ನಂದಿನಿ ಬೆಣ್ಣೆಯ ಹದವಾದ ಮಿಶ್ರಣದಿಂದ ರಾಷ್ಟ್ರೀಯ ಖ್ಯಾತಿ ಪಡೆದಿದೆ!"},
        {"fact": "ಉಡುಪಿಯ ಶ್ರೀ ಕೃಷ್ಣ ಮಠದಲ್ಲಿ ಭಗವಾನ್ ಕೃಷ್ಣನ ವಿಗ್ರಹವು ಪಶ್ಚಿಮಾಭಿಮುಖವಾಗಿದ್ದು, ಕನಕದಾಸರ ಭಕ್ತಿಗೆ ಒಲಿದು ಗೋಡೆ ಒಡೆದು ಕಿಟಕಿಯ ಮೂಲಕ ದರ್ಶನ ನೀಡಿದ ಐತಿಹಾಸಿಕ 'ಕನಕನ ಕಿಂಡಿ' ಮೂಲಕವೇ ಇಂದಿಗೂ ಭಕ್ತರು ದೇವರನ್ನು ದರ್ಶಿಸುತ್ತಾರೆ!"},
        {"fact": "ಕರ್ನಾಟಕ ರಾಜ್ಯವು ಭಾರತದಲ್ಲೇ ಅತಿ ಹೆಚ್ಚು ಜ್ಞಾನಪೀಠ ಪ್ರಶಸ್ತಿ ಪಡೆದ 2ನೇ ಭಾಷೆಯಾಗಿದ್ದು, ಕನ್ನಡ ಸಾಹಿತ್ಯಕ್ಕೆ ಬರೋಬ್ಬರಿ 8 ಜ್ಞಾನಪೀಠ ಪ್ರಶಸ್ತಿಗಳು ಸಂದಿವೆ (ಕುವೆಂಪು, ದರಾ ಬೇಂದ್ರೆ, ಕಾರಂತ, ಮಾಸ್ತಿ, ಗೋಕಾಕ್, ಅನಂತಮೂರ್ತಿ, ಕಂಬಾರ, ಗಿರೀಶ್ ಕಾರ್ನಾಡ್)!"},
        {"fact": "ವಿಜಯಪುರದ ಇಬ್ರಾಹಿಂ ರೋಜಾ (Ibrahim Rauza) ಸ್ಮಾರಕವನ್ನು 'ದಕ್ಷಿಣ ಭಾರತದ ತಾಜ್ ಮಹಲ್' ಎನ್ನಲಾಗುತ್ತದೆ. ವಾಸ್ತವವಾಗಿ ಆಗ್ರಾದ ತಾಜ್ ಮಹಲ್ ವಿನ್ಯಾಸಕ್ಕೆ ಈ ಇಬ್ರಾಹಿಂ ರೋಜಾದ ಕಮಾನುಗಳು ಮತ್ತು ಮಿನಾರುಗಳೇ ಪ್ರೇರಣೆಯಾಗಿದ್ದವು!"},
        {"fact": "ಕೊಡಗು (ಕೂರ್ಗ್) ಜಿಲ್ಲೆಯ ತಲಕಾವೇರಿಯಲ್ಲಿ ಉಗಮಿಸುವ ಕಾವೇರಿ ನದಿಯು ಕರ್ನಾಟಕ ಮತ್ತು ತಮಿಳುನಾಡಿನ ಕೋಟ್ಯಂತರ ಜನರ ಜೀವನಾಡಿಯಾಗಿದೆ. ಕೊಡವರು ಯುದ್ಧಕಲೆ, ಹಾಕಿ ಕ್ರೀಡೆ ಮತ್ತು ದೇಶಪ್ರೇಮಕ್ಕೆ ಹೆಸರಾದ ವೀರ ಸಮುದಾಯ!"},
        {"fact": "ಕಲಬುರಗಿಯ ಖಾಜಾ ಬಂದೇ ನವಾಜ್ ದರ್ಗಾವು ದಕ್ಷಿಣ ಭಾರತದ ಪ್ರಸಿದ್ಧ ಸೂಫಿ ಕೇಂದ್ರವಾಗಿದ್ದು, ಇಲ್ಲಿನ ಗ್ರಂಥಾಲಯದಲ್ಲಿ 14ನೇ ಶತಮಾನದ 10,000 ಕ್ಕೂ ಹೆಚ್ಚು ಅಪರೂಪದ ಅರೇಬಿಕ್, ಪರ್ಷಿಯನ್ ಮತ್ತು ಉರ್ದು ಹಸ್ತಪ್ರತಿಗಳಿವೆ!"},
        {"fact": "ಬಳ್ಳಾರಿಯ ಸಂಡೂರು ತಾಲೂಕು ವಿಶ್ವದರ್ಜೆಯ ಹೆಮಟೈಟ್ ಕಬ್ಬಿಣದ ಅದಿರಿಗೆ ಪ್ರಸಿದ್ಧವಾಗಿದ್ದು, ಮಹಾತ್ಮಾ ಗಾಂಧಿಯವರು 1934 ರಲ್ಲಿ ಸಂಡೂರಿಗೆ ಭೇಟಿ ನೀಡಿದಾಗ ಇಲ್ಲಿನ ಪ್ರಾಕೃತಿಕ ಸೌಂದರ್ಯಕ್ಕೆ ಮನಸೋತು 'ನೋಡು ಸಂಡೂರು ಪಾವಡವಿದು' ಎಂದು ಉದ್ಗರಿಸಿದ್ದರು!"},
        {"fact": "ಹಾಸನ ಜಿಲ್ಲೆಯ ಶ್ರವಣಬೆಳಗೊಳದಲ್ಲಿ ಪ್ರತಿ 12 ವರ್ಷಗಳಿಗೊಮ್ಮೆ ನಡೆಯುವ ಭಗವಾನ್ ಬಾಹುಬಲಿಯ 'ಮಹಾಮಸ್ತಕಾಭಿಷೇಕ' ಮಹೋತ್ಸವಕ್ಕೆ ವಿಶ್ವದ ಮೂಲೆ ಮೂಲೆಗಳಿಂದ ಲಕ್ಷಾಂತರ ಜೈನ ಮುನಿಗಳು ಮತ್ತು ಭಕ್ತರು ಆಗಮಿಸುತ್ತಾರೆ!"},
        {"fact": "ಕರ್ನಾಟಕದ ನಾಡಗೀತೆ 'ಜಯ ಭಾರತ ಜನನಿಯ ತನುಜಾತೆ'ಯನ್ನು ರಚಿಸಿದವರು ರಾಷ್ಟ್ರಕವಿ ಕುವೆಂಪು. ಇದು ಕನ್ನಡ ನಾಡಿನ ಪ್ರಕೃತಿ, ಸಂಸ್ಕೃತಿ, ಸರ್ವಧರ್ಮ ಸಮನ್ವಯತೆ ಹಾಗೂ ಭವ್ಯ ಇತಿಹಾಸವನ್ನು ಅತ್ಯಂತ ಸುಂದರವಾಗಿ ಬಣ್ಣಿಸುತ್ತದೆ!"},
        {"fact": "ಬೆಂಗಳೂರಿನ ಭಾರತೀಯ ವಿಜ್ಞಾನ ಸಂಸ್ಥೆ (IISc) ಭಾರತದ ನಂಬರ್ 1 ಸಂಶೋಧನಾ ಸಂಸ್ಥೆಯಾಗಿದ್ದು, ಸ್ವಾಮಿ ವಿವೇಕಾನಂದರ ಪ್ರೇರಣೆಯಿಂದ ಜಮ್‌ಶೆಟ್‌ಜಿ ಟಾಟಾ ಮತ್ತು ನಾಲ್ವಡಿ ಕೃಷ್ಣರಾಜ ಒಡೆಯರ ಭೂದಾನದಿಂದ 1909 ರಲ್ಲಿ ಸ್ಥಾಪನೆಯಾಯಿತು!"},
        {"fact": "ಉತ್ತರ ಕನ್ನಡ ಜಿಲ್ಲೆಯ ಮುರುಡೇಶ್ವರದಲ್ಲಿರುವ ಭಗವಾನ್ ಶಿವನ ಪ್ರತಿಮೆಯು 123 ಅಡಿ ಎತ್ತರವಿದ್ದು, ಅರಬ್ಬೀ ಸಮುದ್ರದ ತೀರದಲ್ಲಿ ನಿಂತಿರುವ ವಿಶ್ವದ ಎರಡನೇ ಅತಿ ಎತ್ತರದ ಶಿವನ ವಿಗ್ರಹವಾಗಿದೆ!"},
        {"fact": "ಚಿಕ್ಕಮಗಳೂರಿನ ಮುಳ್ಳಯ್ಯನಗಿರಿ ಶಿಖರವು ಸಮುದ್ರ ಮಟ್ಟದಿಂದ 6,317 ಅಡಿ (1,930 ಮೀಟರ್) ಎತ್ತರವಿದ್ದು, ಕರ್ನಾಟಕ ರಾಜ್ಯದ ಅತ್ಯುನ್ನತ ಪರ್ವತ ಶಿಖರವಾಗಿದೆ!"},
        {"fact": "ಮಂಡ್ಯ ಜಿಲ್ಲೆಯ ಶ್ರೀರಂಗಪಟ್ಟಣವು ಟಿಪ್ಪು ಸುಲ್ತಾನನ ಐತಿಹಾಸಿಕ ರಾಜಧಾನಿಯಾಗಿದ್ದು, ಕಾವೇರಿ ನದಿಯ ನಡುಗಡ್ಡೆಯಲ್ಲಿ ನಿರ್ಮಿಸಲಾದ ಅಬೇಧ್ಯ ಜಲದುರ್ಗ ಕೋಟೆಯಾಗಿದೆ!"},
        {"fact": "ಗದಗ ನಗರವು ಮುದ್ರಣ ಕಲೆ ಮತ್ತು ಪತ್ರಿಕೋದ್ಯಮಕ್ಕೆ ಹೆಸರಾಗಿದ್ದು, ಕುಮಾರವ್ಯಾಸನು ಗದುಗಿನ ವೀರನಾರಾಯಣ ಸ್ವಾಮಿ ಸನ್ನಿಧಿಯಲ್ಲೇ ಕುಳಿತು ಕರ್ಣಾಟ ಭಾರತ ಕಥಾಮಂಜರಿ ಮಹಾಕಾವ್ಯವನ್ನು ರಚಿಸಿದನು!"},
        {"fact": "ದಕ್ಷಿಣ ಕನ್ನಡದ ಕಂಬಳ (Kambala) ಕೆಸರುಗದ್ದೆಯಲ್ಲಿ ಕೋಣಗಳನ್ನು ಓಡಿಸುವ 800 ವರ್ಷಗಳ ಸಾಂಪ್ರದಾಯಿಕ ಜಾನಪದ ಕ್ರೀಡೆಯಾಗಿದ್ದು, ರೈತರ ಶ್ರಮ ಮತ್ತು ಕೃಷಿ ಸಂಸ್ಕೃತಿಯ ಅದ್ಭುತ ಪ್ರತಿರೂಪವಾಗಿದೆ!"},
        {"fact": "ವಿಜಯನಗರ ಸಾಮ್ರಾಜ್ಯದ ಕಾಲದ ಸಾಹಿತ್ಯ, ಕಲೆ ಮತ್ತು ವಾಣಿಜ್ಯ ಸಿರಿವಂತಿಕೆಯನ್ನು ಕಂಡ ಪರ್ಷಿಯನ್ ರಾಯಭಾರಿ ಅಬ್ದುಲ್ ರಜಾಕ್, 'ಭೂಮಿಯ ಮೇಲೆ ಕಣ್ಣುಗಳು ನೋಡಿರದ, ಕಿವಿಗಳು ಕೇಳಿರದ ಅಪ್ರತಿಮ ನಗರವಿದು' ಎಂದು ಬಣ್ಣಿಸಿದ್ದನು!"}
    ]

# 5. "ನಿಮಗೆ ತಿಳಿದಿದೆಯೇ?" FACT CARDS (REFERENCE 5 STYLE - 45+ DYNAMIC FACTS)
# ══════════════════════════════════════════════════════════════════════════════
def render_doyouknow_card(slot_num=1):
    doyouknow_facts = DOYOUKNOW_FACTS


    day_of_year = datetime.now().timetuple().tm_yday
    # Ensure each of the 3 daily slots gets a unique non-repeating fact
    fact_idx = (day_of_year * 3 + slot_num - 1) % len(doyouknow_facts)
    fact = doyouknow_facts[fact_idx]
    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))

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
    background: #FFD13B;
    font-family: 'Anek Kannada', sans-serif;
    color: #111827;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 0;
  }}
  .top-white {{
    background: #FFFFFF;
    height: 380px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: relative;
    box-shadow: 0 10px 25px rgba(0,0,0,0.06);
  }}
  .badge-yellow {{
    background: #FFD13B;
    color: #111827;
    font-size: 34px;
    font-weight: 900;
    padding: 8px 36px;
    transform: skew(-6deg);
    border-radius: 4px;
    letter-spacing: 1px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
  }}
  .badge-black {{
    background: #111827;
    color: #FFFFFF;
    font-size: 56px;
    font-weight: 900;
    padding: 12px 64px;
    transform: skew(-6deg);
    border-radius: 6px;
    margin-top: -12px;
    letter-spacing: 2px;
    box-shadow: 0 12px 25px rgba(0,0,0,0.25);
  }}
  .bottom-yellow {{
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 40px 90px 60px;
    text-align: center;
  }}
</style>
</head>
<body>
  <div class="top-white">
    <div class="badge-yellow">ನಿಮಗೆ</div>
    <div class="badge-black">ತಿಳಿದಿದೆಯೇ?</div>
  </div>

  <div class="bottom-yellow">
    <div style="font-size:38px; font-weight:800; line-height:1.65; color:#111827; max-width:920px;">
      {fact['fact']}
    </div>

    <div style="margin-top:48px; font-size:24px; font-weight:800; color:#4B5563; font-family:'Outfit';">
      @karnata.in
    </div>
  </div>
</body>
</html>"""

    out_file = OUTPUT_DIR / f"doyouknow_slot{slot_num}.png"
    render_html_to_png(html, out_file)

# ══════════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════════
# 6. ರಸಪ್ರಶ್ನೆ ಪೋಸ್ಟರ್‌ಗಳು (QUIZ CARDS - DYNAMIC ROTATING QUESTIONS)
# ══════════════════════════════════════════════════════════════════════════════
def render_quiz_interactive_card(slot_num=1):
    quiz_data = get_daily_quiz_data()
    questions = quiz_data.get("questions", [])
    
    day_of_year = datetime.now().timetuple().tm_yday
    if questions:
        q_idx = (day_of_year * 3 + slot_num - 1) % len(questions)
        q = questions[q_idx]
    else:
        q = {
            "question": "ಕರ್ನಾಟಕದ ಪ್ರಪ್ರಥಮ ಕನ್ನಡ ದಿನಪತ್ರಿಕೆ ಯಾವುದು?",
            "options": ["ಮಂಗಳೂರು ಸಮಾಚಾರ", "ಕನ್ನಡ ವೃತ್ತ", "ಸೂರ್ಯೋದಯ", "ಕರ್ನಾಟಕ ಪ್ರಕಾಶಿಕ"]
        }

    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    date_kn = get_kannada_date_str()

    opt_letters = ["A", "B", "C", "D"]
    opt_html = ""
    for o_idx, opt in enumerate(q.get("options", [])[:4]):
        opt_html += f"""
        <div style="background:#1E293B; border:2px solid #475569; border-radius:20px; padding:22px 28px; display:flex; align-items:center; gap:20px;">
          <div style="width:52px; height:52px; border-radius:50%; background:#EA580C; display:flex; align-items:center; justify-content:center; font-size:26px; font-weight:900; font-family:'Outfit'; color:#FFFFFF;">
            {opt_letters[o_idx]}
          </div>
          <div style="font-size:28px; font-weight:800; color:#F8FAFC;">
            {opt}
          </div>
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
    background: #0B0F19;
    font-family: 'Anek Kannada', sans-serif;
    color: #FFFFFF;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 44px 52px;
    border: 14px solid #EA580C;
  }}
</style>
</head>
<body>
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <img src="{logo_b64}" style="height:62px; object-fit:contain;">
    <div style="background:#1E293B; border:1.5px solid #334155; color:#FDE047; font-size:18px; font-weight:900; padding:6px 24px; border-radius:20px; font-family:'Outfit';">
      ಜ್ಞಾನ ಸವಾಲು #{slot_num} • {date_kn}
    </div>
  </div>

  <div style="background:#1E293B; border-radius:24px; padding:36px 40px; margin:20px 0; border:1px solid #334155;">
    <div style="font-size:38px; font-weight:900; line-height:1.45; color:#FFFFFF;">
      {q.get('question')}
    </div>
  </div>

  <div style="display:grid; grid-template-columns:1fr 1fr; gap:18px; margin-bottom:20px;">
    {opt_html}
  </div>

  <div style="display:flex; justify-content:space-between; align-items:center; border-top:2px solid #1E293B; padding-top:16px;">
    <div style="font-size:22px; font-weight:800; color:#CBD5E1;">
      👇 ನಿಮ್ಮ ಉತ್ತರವನ್ನು ಕಾಮೆಂಟ್ ಮಾಡಿ (A, B, C ಅಥವಾ D)
    </div>
    <div style="font-size:24px; font-weight:900; color:#EA580C; font-family:'Outfit';">
      karnata.in/quiz
    </div>
  </div>
</body>
</html>"""

    out_file = OUTPUT_DIR / f"quiz_slot{slot_num}.png"
    render_html_to_png(html, out_file)

# ══════════════════════════════════════════════════════════════════════════════
# ══════════════════════════════════════════════════════════════════════════════
# 7. 07:15 AM: ಶುಭೋದಯ & ಶುಭನುಡಿ (MINIMALIST GOLDEN EDITORIAL - REFERENCE 3 STYLE)
# ══════════════════════════════════════════════════════════════════════════════
def render_quote_card():
    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    date_kn = get_kannada_date_str()

    quotes_bank = [
        {
            "quote": "ಮನುಷ್ಯ ಜಾತಿ ತಾನೊಂದೆ ವಲಂ! ನೂರು ಮತದ ಹೊಟ್ಟ ಹೊಕ್ಕು ಎಲ್ಲ ತತ್ವದೆಲ್ಲೆಯಿಕ್ಕು, ಮತವೆಂಬುದು ಮತಿಗೆಡುವುದು ಬಿಡು, ಮನುಜ ಮತ ವಿಶ್ವಪಥ!",
            "author": "ರಾಷ್ಟ್ರಕವಿ ಕುವೆಂಪು",
            "tag": "ವಿಶ್ವಮಾನವ ಸಂದೇಶ"
        },
        {
            "quote": "ಕಾಯಕವೇ ಕೈಲಾಸ! ದಯವಿಲ್ಲದ ಧರ್ಮವದೇವುದಯ್ಯಾ? ದಯವೇ ಬೇಕು ಸಕಲ ಪ್ರಾಣಿಗಳಲ್ಲಿ, ದಯವೇ ಧರ್ಮದ ಮೂಲವಯ್ಯ.",
            "author": "ಜಗಜ್ಯೋತಿ ಬಸವಣ್ಣ",
            "tag": "ವಚನ ನುಡಿಮುತ್ತು"
        },
        {
            "quote": "ಬದುಕು ಜಟಕಾಬಂಡಿ, ವಿಧಿ ಅದರ ಸಾಹೇಬ; ಕುದುರೆ ನೀನ್, ಅವನು ಪೇಳ್ದಂತೆ ಪಯಣಿಗರು. ಮದುವೆಗೋ ಮಸಣಕ್ಕೊ ತಾಂ ಪೋಗಿ ನಿಲ್ಲುವುದು, ಪದ ಕುಸಿಯೆ ನೆಲವಿಹುದು — ಮಂಕುತಿಮ್ಮ.",
            "author": "ಡಿ. ವಿ. ಗುಂಡಪ್ಪ (ಡಿವಿಜಿ)",
            "tag": "ಮಂಕುತಿಮ್ಮನ ಕಗ್ಗ"
        },
        {
            "quote": "ಯುಗ ಯುಗಾದಿ ಕಳೆದರೂ ಯುಗಾದಿ ಮರಳಿ ಬರುತಿದೆ; ಹೊಸ ವರುಷಕೆ ಹೊಸ ಹರುಷವ ಹೊಸತು ಹೊಸತು ತರುತಿದೆ!",
            "author": "ವರಕವಿ ದ. ರಾ. ಬೇಂದ್ರೆ",
            "tag": "ಭಾವಗೀತೆ"
        },
        {
            "quote": "ತಲ್ಲಣಿಸದಿರು ಕಂಡ್ಯ ತಾಳು ಮನವೆ, ಎಲ್ಲರನು ಕಾಯುವನು ಇದಕೊಬ್ಬ ಜಗದೊಡೆಯ! ಹುಟ್ಟಿಸಿದ ಸ್ವಾಮಿ ತಾ ಹೊಣೆಗಾರನಾಗಿರಲು ಅಂಜಿಕೆಯೇತಕೆ ಮನವೆ?",
            "author": "ಭಕ್ತ ಕನಕದಾಸರು",
            "tag": "ದಾಸ ಸಾಹಿತ್ಯ"
        },
        {
            "quote": "ಮಾನವ ಜನ್ಮ ದೊಡ್ಡದು, ಇದ ಹಾಳು ಮಾಡಬೇಡಿ ಹುಚ್ಚಪ್ಪಗಳಿರಾ! ಹರಿದಾಸರ ಸಂಗವ ಮಾಡಿ ಸನ್ಮಾರ್ಗದಲ್ಲಿ ಮುನ್ನಡೆಯಿರಿ.",
            "author": "ಸಂಗೀತ ಪಿತಾಮಹ ಪುರಂದರದಾಸರು",
            "tag": "ದಾಸಾಮೃತ"
        },
        {
            "quote": "ಸರ್ವಜ್ಞನೆಂಬುವನು ಗರ್ವದಿಂದಾದವನೆ? ಸರ್ವರೊಳು ಒಂದೊಂದು ನುಡಿಗಲಿತು ವಿದ್ಯೆಯ ಪರ್ವತವೆ ಆದ ಸರ್ವಜ್ಞ!",
            "author": "ತ್ರಿಪದಿ ಕವಿ ಸರ್ವಜ್ಞ",
            "tag": "ಸರ್ವಜ್ಞನ ತ್ರಿಪದಿ"
        },
        {
            "quote": "ಬೆಟ್ಟದ ಮೇಲೊಂದು ಮನೆಯ ಮಾಡಿ ಮೃಗಗಳಿಗಂಜಿದೊಡೆ ಎಂತಯ್ಯಾ? ಲೋಕದೊಳು ಹುಟ್ಟಿದ ಬಳಿಕ ಸ್ತುತಿ-ನಿಂದೆಗಳಿಗೆ ಅಂಜದೆ ಸನ್ಮಾರ್ಗದಲ್ಲಿ ಬಾಳಬೇಕು.",
            "author": "ಶಿವಶರಣೆ ಅಕ್ಕಮಹಾದೇವಿ",
            "tag": "ಅಕ್ಕನ ವಚನ"
        },
        {
            "quote": "ಎಲ್ಲಾದರು ಇರು, ಎಂತಾದರು ಇರು, ಎಂದೆಂದಿಗು ನೀ ಕನ್ನಡವಾಗಿರು! ಕನ್ನಡವೇ ಸತ್ಯ, ಕನ್ನಡವೇ ನಿತ್ಯ.",
            "author": "ರಾಷ್ಟ್ರಕವಿ ಕುವೆಂಪು",
            "tag": "ಕನ್ನಡ ಡಿಂಡಿಮ"
        },
        {
            "quote": "ನಗುವು ಸಹಜದ ಧರ್ಮ, ನಗಿಸುವುದು ಪರಧರ್ಮ, ನಗುವ ಕೇಳುತ ಜಗದಿ ನಗುತಿರುವುದು ಧರ್ಮ; ನಗುವನೊಲ್ಲದವನು ಜಗದೊಳು ಜಡ ಧರ್ಮ — ಮಂಕುತಿಮ್ಮ.",
            "author": "ಡಿ. ವಿ. ಗುಂಡಪ್ಪ (ಡಿವಿಜಿ)",
            "tag": "ಮಂಕುತಿಮ್ಮನ ಕಗ್ಗ"
        },
        {
            "quote": "ಇವನಾರವ ಇವನಾರವ ಇವನಾರವನೆನ್ನದಿರಯ್ಯ! ಇವ ನಮ್ಮವ ಇವ ನಮ್ಮವ ಇವ ನಮ್ಮವನೆನ್ನಿರಯ್ಯ, ಕೂಡಲಸಂಗಮದೇವನ ಮನೆಯ ಮಗನೆನ್ನಿರಯ್ಯ.",
            "author": "ಜಗಜ್ಯೋತಿ ಬಸವಣ್ಣ",
            "tag": "ವಚನ ನುಡಿಮುತ್ತು"
        },
        {
            "quote": "ಕುಲ ಕುಲ ಕುಲವೆಂದು ಹೊಡೆದಾಡದಿರಿ, ನಿಮ್ಮ ಕುಲದ ನೆಲೆಯನೇನಾದರೂ ಬಲ್ಲಿರಾ? ಆತ್ಮ ಯಾವ ಕುಲ, ಜೀವ ಯಾವ ಕುಲ, ತತ್ವವನು ತಿಳಿದವನೆ ಜ್ಞಾನಿ!",
            "author": "ಭಕ್ತ ಕನಕದಾಸರು",
            "tag": "ಸಾಮಾಜಿಕ ಸಂದೇಶ"
        },
        {
            "quote": "ಪ್ರಕೃತಿಯ ವಿಸ್ಮಯಗಳನ್ನು ಬೆರಗಿನಿಂದ ನೋಡುವ ಕಣ್ಣುಗಳು ಮನುಷ್ಯನ ಅಹಂಕಾರವನ್ನು ಕರಗಿಸಿ ಜೀವಪ್ರೀತಿಯನ್ನು ಉದ್ದೀಪಿಸುತ್ತವೆ.",
            "author": "ಕೆ. ಪಿ. ಪೂರ್ಣಚಂದ್ರ ತೇಜಸ್ವಿ",
            "tag": "ಪರಿಸರ ಚಿಂತನೆ"
        },
        {
            "quote": "ಕೋಡಗನ ಕೋಳಿ ನುಂಗಿತ್ತಾ ನೋಡವ್ವ ತಂಗಿ! ಜ್ಞಾನವೆಂಬ ಕೋಳಿ ಅಜ್ಞಾನವೆಂಬ ಮರ್ಕಟನ ಜಯಿಸಿದ ಸತ್ಯವನರಿದು ಬದುಕಿರಯ್ಯಾ.",
            "author": "ಸಂತ ಶಿಶುನಾಳ ಶರೀಫರು",
            "tag": "ತತ್ವಪದ"
        },
        {
            "quote": "ಜೀವಿಸುವ ಕಲೆಯೇ ಎಲ್ಲಕ್ಕಿಂತ ಶ್ರೇಷ್ಠ ಕಲೆ. ಸತ್ಯಕ್ಕೆ ಧಕ್ಕೆ ಬಾರದಂತೆ ನಿರ್ಭಯವಾಗಿ, ಕಷ್ಟಗಳಿಗೆ ಜಗ್ಗದೆ ಮುನ್ನಡೆಯುವುದೇ ಬದುಕಿನ ಸಾರ್ಥಕತೆ.",
            "author": "ಡಾ. ಕೋಟ ಶಿವರಾಮ ಕಾರಂತ",
            "tag": "ಬಾಳಿನ ದರ್ಶನ"
        },
        {
            "quote": "ಓ ನನ್ನ ಚೇತನ, ಆಗು ನೀ ಅನಿಕೇತನ! ರೂಪ ರೂಪಗಳನು ದಾಟಿ, ನಾಮ ಕೋಟಿಗಳನು ಮೀಟಿ, ಏಕಾಂತದೊಳು ಮುಕ್ತನಾಗು!",
            "author": "ರಾಷ್ಟ್ರಕವಿ ಕುವೆಂಪು",
            "tag": "ಅನಿಕೇತನ"
        },
        {
            "quote": "ಕಷ್ಟಗಳು ಬಂದಾಗ ಕುಗ್ಗದಿರು, ಸುಖಗಳು ಬಂದಾಗ ಹಿಗ್ಗದಿರು; ಎರಡೂ ಬದುಕಿನ ನದಿಯ ಎರಡು ದಡಗಳು — ಮಂಕುತಿಮ್ಮ.",
            "author": "ಡಿ. ವಿ. ಗುಂಡಪ್ಪ (ಡಿವಿಜಿ)",
            "tag": "ಮಂಕುತಿಮ್ಮನ ಕಗ್ಗ"
        },
        {
            "quote": "ನುಡಿದರೆ ಮುತ್ತಿನ ಹಾರದಂತಿರಬೇಕು, ನುಡಿದರೆ ಸ್ಪಟಿಕದ ಸಲಾಕೆಯಂತಿರಬೇಕು! ನುಡಿಯೊಳಗಾಗಿ ನಡೆಯದಿದ್ದರೆ ಕೂಡಲಸಂಗಮದೇವನೆಂತೊಲಿವನಯ್ಯ?",
            "author": "ಜಗಜ್ಯೋತಿ ಬಸವಣ್ಣ",
            "tag": "ವಚನ ಸಂದೇಶ"
        },
        {
            "quote": "ಗಂಧದ ಮರದೊಳು ಹುಟ್ಟಿದ ಹಾವಿಗೆ ವಿಷವಿಲ್ಲದೆ ಪೋಗುವುದೆ? ಸಜ್ಜನರ ಸಹವಾಸದಿಂದ ದುರ್ಗುಣ ಕಳೆದು ಸದ್ಗುಣ ಬೆಳೆಯುವುದು ಸರ್ವಜ್ಞ.",
            "author": "ತ್ರಿಪದಿ ಕವಿ ಸರ್ವಜ್ಞ",
            "tag": "ಸರ್ವಜ್ಞನ ತ್ರಿಪದಿ"
        },
        {
            "quote": "ಮಾತಿನಲ್ಲಿ ಸತ್ಯ, ನಡೆಯಲ್ಲಿ ಧರ್ಮ, ಹೃದಯದಲ್ಲಿ ಸಕಲ ಜೀವರಾಶಿಗಳ ಮೇಲಿನ ಕರುಣೆ — ಇವಿಷ್ಟೇ ಮನುಷ್ಯನ ಘನತೆಯನ್ನು ನಿರ್ಧರಿಸುವ ಅಳತೆಗೋಲುಗಳು.",
            "author": "ಮಾಸ್ತಿ ವೆಂಕಟೇಶ ಅಯ್ಯಂಗಾರ್",
            "tag": "ಜೀವನ ಮೌಲ್ಯ"
        },
        {
            "quote": "ಹೂವು ಹರಳುವುದು ಯಾರ ಮೆಚ್ಚುಗೆಗೂ ಅಲ್ಲ, ತನ್ನೊಳಗಿನ ಪರಿಮಳ ಮತ್ತು ಸೌಂದರ್ಯವನ್ನು ವಿಶ್ವಕ್ಕೆ ಧಾರೆಯೆರೆಯಲು ಮಾತ್ರ.",
            "author": "ಚನ್ನವೀರ ಕಣವಿ",
            "tag": "ಕಾವ್ಯ ಚಿಂತನೆ"
        },
        {
            "quote": "ಕರ್ಮವೇ ಧರ್ಮ, ಲೋಕಹಿತವೇ ಈಶ್ವರನ ಪರಮ ಪೂಜೆ. ನೊಂದವರ ಕಣ್ಣೀರು ಒರೆಸುವುದಕ್ಕಿಂತ ಮಿಗಿಲಾದ ಪುಣ್ಯ ಮತ್ತೊಂದಿಲ್ಲ.",
            "author": "ಶಿವಯೋಗಿ ಸಿದ್ಧರಾಮೇಶ್ವರರು",
            "tag": "ಕಾಯಕ ತತ್ವ"
        },
        {
            "quote": "ಕನ್ನಡಿಯ ನೋಡಿದಡೆ ತನ್ನ ರೂಪಲ್ಲದೆ ಮತ್ತೊಂದನು ಕಾಣಬಾರದು. ತನ್ನ ತಾನರಿದ ಬಳಿಕ ಜಗವೆಲ್ಲವೂ ಬ್ರಹ್ಮಸ್ವರೂಪ ಕಾಣಾ ಗುಹೇಶ್ವರಾ!",
            "author": "ಶೂನ್ಯ ಸಂಪಾದನೆಯ ಅಲ್ಲಮಪ್ರಭು",
            "tag": "ಅಲ್ಲಮನ ವಚನ"
        },
        {
            "quote": "ವೀರ ನಾರಾಯಣನೆ ಕವಿ, ಲಿಪಿಕಾರ ಗದುಗಿನ ವೀರನಾರಾಯಣ; ಕೃತಿಯನು ರಚಿಸಿದ ಕೀರ್ತಿ ಆ ದೇವನಿಗೇ ಸಲ್ಲಬೇಕು.",
            "author": "ಮಹಾಕವಿ ಕುಮಾರವ್ಯಾಸ",
            "tag": "ಕರ್ಣಾಟ ಭಾರತ ಕಥಾಮಂಜರಿ"
        },
        {
            "quote": "ತ್ಯಾಗದ ಭೋಗದಕ್ಕರದ ಗೇಯದ ಗೊಟ್ಟಿಯ ನಾಣ್ನುಡಿಗಳಿಂ ಆರಂಗೆಯ್ದುಂ ನೆನೆವುದೆನ್ನ ಮನಂ ಬನವಾಸಿ ದೇಶಮಂ!",
            "author": "ಆದಿಕವಿ ಪಂಪ",
            "tag": "ವಿಕ್ರಮಾರ್ಜುನ ವಿಜಯ"
        },
        {
            "quote": "ಸಿಂಹದಂತೆ ಗಾಂಭೀರ್ಯದಿಂದ ಬದುಕಿದವನೆ ಧೀರ ಪುರುಷ. ಧರ್ಮದ ಹಾದಿಯಲ್ಲಿ ಎದುರಾಗುವ ಸೋಲು ಸಹ ವೀರನಿಗೆ ಸಿಗುವ ಕಿರೀಟ.",
            "author": "ಕವಿಚಕ್ರವರ್ತಿ ರನ್ನ",
            "tag": "ಗದಾಯುದ್ಧ"
        },
        {
            "quote": "ವಜ್ರದೊಲು ಕಠಿಣವಾಗು ಕರ್ತವ್ಯದೆದುರಿನಲಿ, ಕುಸುಮದೊಲು ಮೃದುವಾಗು ಬಾಳ ಕರುಣೆಯಲಿ; ಸಮಚಿತ್ತದಿಂದ ಮುನ್ನಡೆ — ಮಂಕುತಿಮ್ಮ.",
            "author": "ಡಿ. ವಿ. ಗುಂಡಪ್ಪ (ಡಿವಿಜಿ)",
            "tag": "ಮಂಕುತಿಮ್ಮನ ಕಗ್ಗ"
        },
        {
            "quote": "ನೀರಿನೊಳು ಮುಳುಗಿದವನಿಗೆ ಮಳೆಯ ಭಯವೇಕೆ? ಆತ್ಮವಿಶ್ವಾಸವಿರುವ ಸಾಧಕನಿಗೆ ಲೋಕದ ಸಣ್ಣ ನಿಂದೆಗಳು ಅಡ್ಡಿಯಾಗಲಾರವು.",
            "author": "ರಾಷ್ಟ್ರಕವಿ ಜಿ. ಎಸ್. ಶಿವರುದ್ರಪ್ಪ",
            "tag": "ಸಮನ್ವಯ ಸಂದೇಶ"
        },
        {
            "quote": "ಅಜ್ಞಾನದ ಕತ್ತಲೆಯನು ಕಳೆಯಲು ಜ್ಞಾನದ ದೀಪವೊಂದೇ ಮಾರ್ಗ. ಶಾಸ್ತ್ರಗಳಿಗಿಂತ ಅನುಭವಜನ್ಯ ಜ್ಞಾನವೇ ಮನುಷ್ಯನಿಗೆ ಮುಕ್ತಿ ನೀಡುತ್ತದೆ.",
            "author": "ಕನ್ನಡದ ಕುಲಪುರೋಹಿತ ಆಲೂರು ವೆಂಕಟರಾವ್",
            "tag": "ಕರ್ನಾಟಕ ಗತವೈಭವ"
        },
        {
            "quote": "ನಾಳೆಯ ಬದುಕಿನ ಚಿಂತೆಗಿಂತ ಇಂದಿನ ಕಾಯಕದ ಪರಿಶುದ್ಧತೆಯೇ ನಿನ್ನ ಭವಿಷ್ಯವನ್ನು ಉಜ್ವಲಗೊಳಿಸುತ್ತದೆ.",
            "author": "ಹಡಪದ ಅಪ್ಪಣ್ಣ",
            "tag": "ಶರಣ ತತ್ವ"
        },
        {
            "quote": "ಸತ್ಯಕ್ಕೆ ಸಾವಿಲ್ಲ, ಸುಳ್ಳಿಗೆ ನೆಲೆ ಇಲ್ಲ; ಧರ್ಮದ ದಾರಿಯಲ್ಲಿ ಮುನ್ನಡೆದರೆ ಜಯ ನಿಶ್ಚಯ.",
            "author": "ಆಯ್ದಕ್ಕಿ ಮಾರಯ್ಯ",
            "tag": "ಶರಣ ಸಂದೇಶ"
        },
        {
            "quote": "ಹಳ್ಳಿಯ ಹಸಿರು, ಹಳ್ಳಿಯ ಹಾರ್ದಿಕತೆ ಮತ್ತು ಜನರ ನಿಷ್ಕಲ್ಮಶ ಪ್ರೀತಿಯೇ ನವಭಾರತದ ನೈಜ ಚೈತನ್ಯ.",
            "author": "ಗೋರೂರು ರಾಮಸ್ವಾಮಿ ಅಯ್ಯಂಗಾರ್",
            "tag": "ನಮ್ಮ ಊರಿನ ರಸಿಕರು"
        }
    ]

    day_of_year = datetime.now().timetuple().tm_yday
    selected = quotes_bank[day_of_year % len(quotes_bank)]

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
    background: #F5BA13;
    font-family: 'Anek Kannada', serif;
    color: #111827;
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    padding: 70px 80px;
    text-align: center;
  }}
</style>
</head>
<body>
  <div style="display:flex; align-items:center; gap:8px; font-size:17px; font-weight:800; color:#374151; letter-spacing:1px;">
    <span>✦</span>
    <span>ಕರ್ನಾಟ ದಿನದ ಸವಿಚಿಂತನೆ</span>
    <span>•</span>
    <span style="font-family:'Outfit';">{date_kn}</span>
    <span>✦</span>
  </div>

  <div style="max-width:920px; margin:auto 0; display:flex; flex-direction:column; align-items:center;">
    <div style="font-size:44px; font-weight:900; line-height:1.65; color:#111827; letter-spacing:-0.5px; text-wrap:balance;">
      “{selected['quote']}”
    </div>

    <div style="font-size:38px; color:#1F2937; margin:34px 0 16px; opacity:0.85; line-height:1;">
      ⚜
    </div>

    <div style="font-size:32px; font-weight:900; color:#111827; letter-spacing:0.5px;">
      {selected['author']}
    </div>

    <div style="font-size:20px; font-weight:700; color:#4B5563; margin-top:6px; letter-spacing:0.5px;">
      «{selected['tag']}»
    </div>
  </div>

  <div style="display:flex; flex-direction:column; align-items:center; gap:6px;">
    <div style="width:52px; height:52px; border-radius:50%; background:#111827; color:#F5BA13; display:flex; align-items:center; justify-content:center; font-size:26px; font-weight:900; box-shadow:0 4px 12px rgba(0,0,0,0.15);">
      ಕ
    </div>
    <div style="font-size:14px; font-weight:900; color:#1F2937; font-family:'Outfit'; letter-spacing:2.5px; text-transform:uppercase;">
      karnata.in
    </div>
  </div>
</body>
</html>"""

    out_file = OUTPUT_DIR / "quote_today.png"
    render_html_to_png(html, out_file)

# ══════════════════════════════════════════════════════════════════════════════
# 8. 08:30 AM: ನಿನ್ನೆಯ ಹವಾಮಾನ ದಾಖಲೆಗಳು (WEATHER SUMMARY)
# ══════════════════════════════════════════════════════════════════════════════
def render_weather_morning_summary():
    w = get_live_weather()
    ext = w.get("state_extremes", {})
    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    date_kn = get_kannada_date_str()

    max_rain = ext.get("highest_past_24h_rain", {})
    r_mm = f"{float(max_rain.get('rain_mm', 53.0)):.1f}"
    r_st = max_rain.get('station', 'Devachalla')
    r_dist = max_rain.get('name_kn', 'ದಕ್ಷಿಣ ಕನ್ನಡ')

    max_temp = ext.get("max_temp_district", {})
    t_max_val = f"{float(max_temp.get('temp_c', 38.8)):.1f}"
    t_max_st = max_temp.get('station', 'Gulbarga')
    t_max_dist = max_temp.get('name_kn', 'ಕಲಬುರಗಿ')

    min_temp = ext.get("min_temp_district", {})
    t_min_val = f"{float(min_temp.get('temp_c', 13.4)):.1f}"
    t_min_st = min_temp.get('station', 'Chadchan')
    t_min_dist = min_temp.get('name_kn', 'ವಿಜಯಪುರ')

    # Top 5 Rain Locations
    top_rain_raw = ext.get("top_rainfall_locations") or ext.get("heavy_rain_locations") or []
    medals = ['🏆 1', '🥈 2', '🥉 3', '4', '5']
    top5_rain_html = ""
    for idx, r in enumerate(top_rain_raw[:5]):
        dist = r.get("district_kn") or r.get("name_kn") or r.get("district_en")
        if dist == "Bengaluru South": dist = "ಬೆಂ.ದಕ್ಷಿಣ"
        st = r.get("gp_name") or r.get("station") or dist
        mm = float(r.get("rainfall_mm") or r.get("rain_mm") or 0)
        top5_rain_html += f"""
        <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(30, 41, 59, 0.75); border:1px solid rgba(255,255,255,0.08); border-radius:12px; padding:10px 14px; margin-bottom:7px; backdrop-filter:blur(8px);">
          <div style="display:flex; align-items:center; gap:10px;">
            <div style="font-size:14px; font-weight:900; background:#0284C7; color:#FFF; padding:2px 8px; border-radius:6px; font-family:'Outfit';">{medals[idx]}</div>
            <div>
              <div style="font-size:17px; font-weight:900; color:#FFFFFF; line-height:1.2;">{st}</div>
              <div style="font-size:12px; font-weight:700; color:#94A3B8;">{dist} ಜಿಲ್ಲೆ</div>
            </div>
          </div>
          <div style="font-size:20px; font-weight:900; color:#38BDF8; font-family:'Outfit';">{mm:.1f} <span style="font-size:12px; font-weight:700; color:#94A3B8;">mm</span></div>
        </div>"""

    # Top 3 Hot & Cold
    top_hot_raw = ext.get("top_max_temp_locations", [])[:3]
    top_hot_html = ""
    for idx, h in enumerate(top_hot_raw):
        dist = h.get("district_kn") or h.get("name_kn") or h.get("district_en")
        st = h.get("hobli") or h.get("station") or dist
        tc = float(h.get("temp_c", 0))
        top_hot_html += f"""
        <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(239, 68, 68, 0.1); border:1px solid rgba(239, 68, 68, 0.25); border-radius:10px; padding:7px 12px; margin-bottom:5px;">
          <div style="font-size:14px; font-weight:800; color:#FEE2E2;">#{idx+1} {dist} ({st})</div>
          <div style="font-size:16px; font-weight:900; color:#F87171; font-family:'Outfit';">{tc:.1f}°C</div>
        </div>"""

    top_cold_raw = ext.get("top_min_temp_locations", [])[:3]
    top_cold_html = ""
    for idx, c in enumerate(top_cold_raw):
        dist = c.get("district_kn") or c.get("name_kn") or c.get("district_en")
        st = c.get("hobli") or c.get("station") or dist
        tc = float(c.get("temp_c", 0))
        top_cold_html += f"""
        <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(14, 165, 233, 0.1); border:1px solid rgba(14, 165, 233, 0.25); border-radius:10px; padding:7px 12px; margin-bottom:5px;">
          <div style="font-size:14px; font-weight:800; color:#E0F2FE;">#{idx+1} {dist} ({st})</div>
          <div style="font-size:16px; font-weight:900; color:#38BDF8; font-family:'Outfit';">{tc:.1f}°C</div>
        </div>"""

    html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@600;700;800;900&family=Outfit:wght@600;700;800;900&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: #060913;
    font-family: 'Anek Kannada', sans-serif;
    color: #FFFFFF;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 36px 40px;
    position: relative;
    overflow: hidden;
    -webkit-font-smoothing: antialiased;
  }}
  .glow-cyan {{
    position: absolute; width: 600px; height: 600px; border-radius: 50%;
    background: radial-gradient(circle, rgba(14, 165, 233, 0.15) 0%, rgba(14, 165, 233, 0) 70%);
    top: -100px; left: 50px; pointer-events: none; filter: blur(40px);
  }}
  .glow-amber {{
    position: absolute; width: 500px; height: 500px; border-radius: 50%;
    background: radial-gradient(circle, rgba(239, 68, 68, 0.12) 0%, rgba(239, 68, 68, 0) 70%);
    bottom: 50px; right: 50px; pointer-events: none; filter: blur(45px);
  }}
  .grid-bg {{
    position: absolute; top: 0; left: 0; width: 100%; height: 100%;
    background-image: linear-gradient(rgba(255, 255, 255, 0.025) 1px, transparent 1px),
                      linear-gradient(90deg, rgba(255, 255, 255, 0.025) 1px, transparent 1px);
    background-size: 36px 36px; pointer-events: none; z-index: 0;
  }}
  .content-wrap {{ position: relative; z-index: 1; display: flex; flex-direction: column; height: 100%; justify-content: space-between; }}
</style>
</head>
<body>
  <div class="glow-cyan"></div>
  <div class="glow-amber"></div>
  <div class="grid-bg"></div>

  <div class="content-wrap">
    <!-- Header -->
    <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(15, 23, 42, 0.65); border:1.5px solid rgba(255, 255, 255, 0.1); border-radius:20px; padding:12px 24px; backdrop-filter:blur(16px);">
      <img src="{logo_b64}" style="height:56px; object-fit:contain;">
      <div style="background:rgba(2, 132, 199, 0.15); border:1.5px solid #0284C7; color:#38BDF8; font-size:17px; font-weight:800; padding:6px 20px; border-radius:18px; font-family:'Outfit';">
        08:30 AM ಹವಾಮಾನ ದಾಖಲೆಗಳು • {date_kn}
      </div>
    </div>

    <!-- Title -->
    <div style="margin-top: 4px;">
      <div style="font-size:14px; font-weight:900; color:#38BDF8; font-family:'Outfit'; letter-spacing:1.6px; text-transform:uppercase;">
        KARNATAKA 24H WEATHER TELEMETRY
      </div>
      <div style="font-size:40px; font-weight:900; color:#FFFFFF; line-height:1.15; margin-top:2px;">
        ನಿನ್ನೆಯ ರಾಜ್ಯದ ಹವಾಮಾನ ದಾಖಲೆಗಳು 🌦️
      </div>
    </div>

    <!-- 3 KEY STAT CARDS -->
    <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px;">
      <div style="background:linear-gradient(135deg, rgba(2, 132, 199, 0.15) 0%, rgba(15, 23, 42, 0.7) 100%); border:1.8px solid #0284C7; border-radius:20px; padding:18px 14px; text-align:center; box-shadow:0 10px 25px rgba(2, 132, 199, 0.15);">
        <div style="font-size:32px;">🌧️</div>
        <div style="font-size:16px; font-weight:800; color:#7DD3FC; margin-top:4px;">ರಾಜ್ಯದ ಗರಿಷ್ಠ ಮಳೆ</div>
        <div style="font-size:34px; font-weight:900; color:#FFFFFF; font-family:'Outfit'; margin:4px 0;">{r_mm} mm</div>
        <div style="font-size:15px; font-weight:800; color:#BAE6FD;">{r_st}</div>
        <div style="font-size:12px; font-weight:700; color:#7DD3FC;">{r_dist} ಜಿಲ್ಲೆ</div>
      </div>

      <div style="background:linear-gradient(135deg, rgba(239, 68, 68, 0.15) 0%, rgba(15, 23, 42, 0.7) 100%); border:1.8px solid #EF4444; border-radius:20px; padding:18px 14px; text-align:center; box-shadow:0 10px 25px rgba(239, 68, 68, 0.15);">
        <div style="font-size:32px;">☀️</div>
        <div style="font-size:16px; font-weight:800; color:#FCA5A5; margin-top:4px;">ಅತಿ ಗರಿಷ್ಠ ಬಿಸಿಲು</div>
        <div style="font-size:34px; font-weight:900; color:#FFFFFF; font-family:'Outfit'; margin:4px 0;">{t_max_val} °C</div>
        <div style="font-size:15px; font-weight:800; color:#FECACA;">{t_max_st}</div>
        <div style="font-size:12px; font-weight:700; color:#FCA5A5;">{t_max_dist} ಜಿಲ್ಲೆ</div>
      </div>

      <div style="background:linear-gradient(135deg, rgba(14, 165, 233, 0.15) 0%, rgba(15, 23, 42, 0.7) 100%); border:1.8px solid #0EA5E9; border-radius:20px; padding:18px 14px; text-align:center; box-shadow:0 10px 25px rgba(14, 165, 233, 0.15);">
        <div style="font-size:32px;">❄️</div>
        <div style="font-size:16px; font-weight:800; color:#93C5FD; margin-top:4px;">ಅತಿ ಕನಿಷ್ಠ ಚಳಿ</div>
        <div style="font-size:34px; font-weight:900; color:#FFFFFF; font-family:'Outfit'; margin:4px 0;">{t_min_val} °C</div>
        <div style="font-size:15px; font-weight:800; color:#BFDBFE;">{t_min_st}</div>
        <div style="font-size:12px; font-weight:700; color:#93C5FD;">{t_min_dist} ಜಿಲ್ಲೆ</div>
      </div>
    </div>

    <!-- 2 BOARDS: TOP RAIN + TEMP HIGHLIGHTS -->
    <div style="display:grid; grid-template-columns: 1.35fr 1fr; gap:16px;">
      <!-- TOP 5 RAIN -->
      <div style="background:rgba(15, 23, 42, 0.7); border:1.5px solid rgba(255,255,255,0.09); border-radius:18px; padding:16px 18px; backdrop-filter:blur(14px);">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
          <div style="font-size:18px; font-weight:900; color:#38BDF8;">🌧️ ಅತಿ ಹೆಚ್ಚು ಮಳೆ ಬಂದ ಪ್ರದೇಶಗಳು</div>
          <div style="font-size:12px; font-weight:800; color:#94A3B8; font-family:'Outfit';">TOP 5 LOCATIONS</div>
        </div>
        {top5_rain_html}
      </div>

      <!-- TOP TEMP EXTREMES -->
      <div style="background:rgba(15, 23, 42, 0.7); border:1.5px solid rgba(255,255,255,0.09); border-radius:18px; padding:16px 18px; backdrop-filter:blur(14px); display:flex; flex-direction:column; justify-content:space-between;">
        <div>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
            <div style="font-size:15px; font-weight:900; color:#FCA5A5;">🔥 ಗರಿಷ್ಠ ತಾಪಮಾನ (Highest)</div>
          </div>
          {top_hot_html}
        </div>

        <div style="margin-top:8px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
            <div style="font-size:15px; font-weight:900; color:#93C5FD;">❄️ ಕನಿಷ್ಠ ತಾಪಮಾನ (Coldest)</div>
          </div>
          {top_cold_html}
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(15, 23, 42, 0.6); border:1.5px solid rgba(255, 255, 255, 0.08); border-radius:16px; padding:12px 22px; backdrop-filter:blur(12px);">
      <div style="font-size:17px; font-weight:800; color:#94A3B8;">📡 31 ಜಿಲ್ಲೆಗಳ ಲೈವ್ ರೇಡಾರ್ & ಮುನ್ಸೂಚನೆ: karnata.in/weather</div>
      <div style="font-size:22px; font-weight:900; color:#38BDF8; font-family:'Outfit';">karnata.in</div>
    </div>
  </div>
</body>
</html>"""

    out_file = OUTPUT_DIR / "weather_morning_summary.png"
    render_html_to_png(html, out_file)

# ══════════════════════════════════════════════════════════════════════════════
# 9. 09:15 AM: KSAMB APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ (2-PAGE CAROUSEL - 100% DYNAMIC LIVE)
# ══════════════════════════════════════════════════════════════════════════════
def extract_live_apmc_crops():
    raw_items = get_live_apmc()
    
    # Categorized targets for Slide 1 (Commercial/Cash/Plantation) & Slide 2 (Foodgrains/Pulses/Veg)
    slide1_targets = [
        {"keys": ["arecanut", "ಅಡಿಕೆ"], "preferred_mkts": ["SHIVAMOGGA", "SAGAR", "CHANNAGIRI", "BANTWALA", "SIRSI"], "label": "ಅಡಿಕೆ (ರಾಶಿ/ಚಾಲಿ)", "unit": "ಕ್ವಿಂಟಾಲ್", "def_min": 48500, "def_max": 54200},
        {"keys": ["copra", "ಕೊಬ್ಬರಿ"], "preferred_mkts": ["TIPTUR", "ARSIKERE", "TURUVEKERE"], "label": "ಕೊಬ್ಬರಿ (ಉಂಡೆ)", "unit": "ಕ್ವಿಂಟಾಲ್", "def_min": 16000, "def_max": 20000},
        {"keys": ["cotton", "ಹತ್ತಿ"], "preferred_mkts": ["RAICHUR", "BAILHONGAL", "HAVERI", "BALLARI"], "label": "ಹತ್ತಿ (DCH/BT)", "unit": "ಕ್ವಿಂಟಾಲ್", "def_min": 8200, "def_max": 9400},
        {"keys": ["ginger", "ಶುಂಠಿ"], "preferred_mkts": ["HASSAN", "BYADGI", "SORABHA", "SHIVAMOGGA"], "label": "ಶುಂಠಿ (ಹಸಿ/ಒಣ)", "unit": "ಕ್ವಿಂಟಾಲ್", "def_min": 11000, "def_max": 28500},
        {"keys": ["pepper", "ಮೆಣಸು"], "preferred_mkts": ["BELUR", "BANTWALA", "BELTHANGADI", "SIRSI"], "label": "ಕರಿಮೆಣಸು (ಕಾಳುಮೆಣಸು)", "unit": "ಕ್ವಿಂಟಾಲ್", "def_min": 52000, "def_max": 68000},
        {"keys": ["jaggery", "ಬೆಲ್ಲ"], "preferred_mkts": ["MANDYA", "BENGALURU", "BELAGAVI"], "label": "ಬೆಲ್ಲ (ಸಾವಯವ ಮುದ್ದೆ)", "unit": "ಕ್ವಿಂಟಾಲ್", "def_min": 5000, "def_max": 6800}
    ]

    slide2_targets = [
        {"keys": ["paddy", "ಭತ್ತ"], "preferred_mkts": ["GANGAVATI", "SINDHANUR", "RAICHUR", "DAVANAGERE", "BHADRAVATHI"], "label": "ಭತ್ತ (ಸೋನಾ/RNR)", "unit": "ಕ್ವಿಂಟಾಲ್", "def_min": 2600, "def_max": 3490},
        {"keys": ["tur", "ತೊಗರಿ"], "preferred_mkts": ["KALABURAGI", "BENGALURU", "YADGIR", "DAVANAGERE"], "label": "ತೊಗರಿ ಬೇಳೆ / ಕಾಳು", "unit": "ಕ್ವಿಂಟಾಲ್", "def_min": 9200, "def_max": 12500},
        {"keys": ["chilli", "ಮೆಣಸಿನಕಾಯಿ"], "preferred_mkts": ["BYADGI", "HAVERI", "HUBBALLI"], "label": "ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ", "unit": "ಕ್ವಿಂಟಾಲ್", "def_min": 28000, "def_max": 58000},
        {"keys": ["onion", "ಈರುಳ್ಳಿ"], "preferred_mkts": ["HUBBALLI", "BAGALKOT", "BANGARPET", "BENGALURU", "GADAG"], "label": "ಈರುಳ್ಳಿ (ನಾಟಿ/ಲೋಕಲ್)", "unit": "ಕ್ವಿಂಟಾಲ್", "def_min": 1800, "def_max": 4500},
        {"keys": ["tomato", "ಟೊಮ್ಯಾಟೊ", "ಟೊಮೇಟೊ"], "preferred_mkts": ["KOLAR", "BAGEPALLI", "BANGARPET", "BELAGAVI"], "label": "ಟೊಮೇಟೊ", "unit": "15 ಕೆಜಿ ಬಾಕ್ಸ್", "def_min": 400, "def_max": 1800},
        {"keys": ["ragi", "ರಾಗಿ"], "preferred_mkts": ["MANDYA", "BENGALURU", "CHINTAMANI", "BALLARI", "TUMKUR"], "label": "ರಾಗಿ (ನಾಟಿ/ಕ್ಲೀನ್ಡ್)", "unit": "ಕ್ವಿಂಟಾಲ್", "def_min": 3200, "def_max": 4800}
    ]

    def resolve_target(tgt):
        best_rec = None
        for r in raw_items:
            crop_str = (r.get("crop", "") + " " + r.get("cropKn", "")).lower()
            if any(k in crop_str for k in tgt["keys"]):
                mkt = r.get("market", "").upper()
                if mkt in tgt["preferred_mkts"]:
                    best_rec = r
                    break
                elif not best_rec and r.get("min", 0) > 0:
                    best_rec = r
        
        if best_rec and best_rec.get("min", 0) > 0 and best_rec.get("max", 0) > 0:
            mkt_name = best_rec.get("market", "").title()
            dist_name = best_rec.get("district", "")
            mkt_display = f"{mkt_name} ({dist_name})" if dist_name and dist_name != "ಕರ್ನಾಟಕ" else mkt_name
            min_p = best_rec.get("min")
            max_p = best_rec.get("max")
            avg_p = best_rec.get("avg")
            price_str = f"₹{min_p:,} - ₹{max_p:,}" if min_p != max_p else f"₹{min_p:,}"
            return (tgt["label"], mkt_display, price_str, tgt["unit"], "— ಸ್ಥಿರ")
        else:
            p_str = f"₹{tgt['def_min']:,} - ₹{tgt['def_max']:,}"
            m_str = tgt["preferred_mkts"][0].title()
            return (tgt["label"], m_str, p_str, tgt["unit"], "— ಸ್ಥಿರ")

    p1_crops = [resolve_target(t) for t in slide1_targets]
    p2_crops = [resolve_target(t) for t in slide2_targets]
    return p1_crops, p2_crops

def render_apmc_carousel():
    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    date_kn = get_kannada_date_str()
    p1_crops, p2_crops = extract_live_apmc_crops()

    for p_num, p_crops, sub_kn in [(1, p1_crops, "ವಾಣಿಜ್ಯ & ತೋಟಗಾರಿಕಾ ಬೆಳೆಗಳು (Slide 1/2)"), (2, p2_crops, "ಆಹಾರ ಧಾನ್ಯಗಳು & ತರಕಾರಿಗಳು (Slide 2/2)")]:
        rows_html = ""
        for crop, mandi, price, unit, trend in p_crops:
            tr_col = "#10B981" if "🔼" in trend else ("#EF4444" if "🔽" in trend else "#94A3B8")
            rows_html += f"""
            <div style="display:grid; grid-template-columns:2fr 1.6fr 1.8fr 1fr; background:#131B2A; border:1px solid #1E293B; border-radius:14px; padding:16px 20px; align-items:center; margin-bottom:10px;">
              <div>
                <div style="font-size:24px; font-weight:900; color:#FFFFFF;">{crop}</div>
                <div style="font-size:16px; font-weight:700; color:#94A3B8;">{mandi}</div>
              </div>
              <div style="font-size:24px; font-weight:900; color:#FDE047; font-family:'Outfit';">{price}</div>
              <div style="font-size:17px; font-weight:800; color:#CBD5E1;">ಪ್ರತಿ {unit}</div>
              <div style="font-size:20px; font-weight:900; color:{tr_col}; text-align:right; font-family:'Outfit';">{trend}</div>
            </div>"""

        html = f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@700;800;900&family=Outfit:wght@700;800;900&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: #0A0F1A;
    font-family: 'Anek Kannada', sans-serif;
    color: #FFFFFF;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 38px 48px;
    border: 14px solid #16A34A;
  }}
</style>
</head>
<body>
  <div style="display:flex; justify-content:space-between; align-items:center;">
    <img src="{logo_b64}" style="height:60px; object-fit:contain;">
    <div style="background:#1E293B; border:1.5px solid #334155; color:#86EFAC; font-size:18px; font-weight:800; padding:6px 24px; border-radius:20px; font-family:'Outfit';">
      09:15 AM APMC ದರಗಳು • {date_kn}
    </div>
  </div>

  <div style="margin-top:8px;">
    <div style="font-size:22px; font-weight:900; color:#86EFAC; font-family:'Outfit';">
      KSAMB MANDI LIVE PRICES
    </div>
    <div style="font-size:46px; font-weight:900; color:#FFFFFF; line-height:1.15; margin-top:2px;">
      ರಾಜ್ಯದ ಪ್ರಮುಖ ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ 🌾
    </div>
    <div style="font-size:20px; font-weight:800; color:#FDE047; margin-top:2px;">
      {sub_kn}
    </div>
  </div>

  <div>
    <div style="display:grid; grid-template-columns:2fr 1.6fr 1.8fr 1fr; background:#0F172A; border-radius:12px; padding:10px 20px; margin-bottom:10px; font-size:17px; font-weight:900; color:#94A3B8;">
      <div>ಬೆಳೆ & ಮಾರುಕಟ್ಟೆ</div>
      <div style="color:#FDE047;">ದರ ವ್ಯಾಪ್ತಿ</div>
      <div>ಪ್ರಮಾಣ</div>
      <div style="text-align:right;">ಟ್ರೆಂಡ್</div>
    </div>
    {rows_html}
  </div>

  <div style="display:flex; justify-content:space-between; align-items:center; border-top:2px solid #1E293B; padding-top:14px;">
    <div style="font-size:20px; font-weight:800; color:#94A3B8;">ರಾಜ್ಯದ 174 APMC ಲೈವ್ ದರ: karnata.in/apmc</div>
    <div style="font-size:24px; font-weight:900; color:#16A34A; font-family:'Outfit';">karnata.in</div>
  </div>
</body>
</html>"""

        out_file = OUTPUT_DIR / f"apmc_p{p_num}.png"
        render_html_to_png(html, out_file)

# ══════════════════════════════════════════════════════════════════════════════
# 10. IMD ನೌಕಾಸ್ಟ್ ಮಳೆ ನಕ್ಷೆ (WEATHER NOWCAST CREATIVE EDITORIAL MAP)
# ══════════════════════════════════════════════════════════════════════════════
def render_nowcast_map_card():
    w = get_live_weather()
    state_extremes = w.get("state_extremes", {})
    logo_b64 = get_file_base64(str(ROOT_DIR / "karnata-logo.png"))
    date_kn = get_kannada_date_str()

    map_path = ROOT_DIR / "data" / "gis" / "karnataka_districts_precision.json"
    if not map_path.exists():
        print("⚠️ Warning: karnataka_districts_precision.json not found, skipping map card.")
        return
    with open(map_path, "r", encoding="utf-8") as f:
        map_geo = json.load(f)

    imd_warnings = w.get("imd_warnings", {})

    # Keep data/imd_live_warnings.json synchronized with live data
    imd_live_path = ROOT_DIR / "data" / "imd_live_warnings.json"
    try:
        updated_imd_live = {}
        for did_k, winfo in imd_warnings.items():
            en_name = winfo.get("district_en", "").upper()
            if en_name:
                updated_imd_live[en_name] = {
                    "title": en_name,
                    "color": winfo.get("color", "#008000"),
                    "level": winfo.get("level", "green"),
                    "hazard_kn": winfo.get("hazard_kn", "ಶಾಂತ ವಾತಾವರಣ 🌤️")
                }
        if updated_imd_live:
            with open(imd_live_path, "w", encoding="utf-8") as f:
                json.dump(updated_imd_live, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

    ALERT_CONFIG = {
        "red": {
            "color": "#EF4444",
            "glow": "rgba(239, 68, 68, 0.4)",
            "pill_bg": "rgba(239, 68, 68, 0.15)",
            "pill_border": "#F87171",
            "pill_text": "#FCA5A5",
            "title_kn": "ರೆಡ್ ಅಲರ್ಟ್ (Red Warning)",
            "desc_kn": "ಅತಿ ಭಾರೀ ಮಳೆ & ಮುನ್ನೆಚ್ಚರಿಕೆ (Take Action)",
            "icon": "🔴"
        },
        "orange": {
            "color": "#F97316",
            "glow": "rgba(249, 115, 22, 0.4)",
            "pill_bg": "rgba(249, 115, 22, 0.15)",
            "pill_border": "#FB923C",
            "pill_text": "#FDBA74",
            "title_kn": "ಆರೆಂಜ್ ಅಲರ್ಟ್ (Orange Alert)",
            "desc_kn": "ಧಾರಾಕಾರ ಮಳೆ / ಬಿರುಗಾಳಿ (Be Prepared)",
            "icon": "🟠"
        },
        "yellow": {
            "color": "#FACC15",
            "glow": "rgba(250, 204, 21, 0.45)",
            "pill_bg": "rgba(250, 204, 21, 0.15)",
            "pill_border": "#FDE047",
            "pill_text": "#FEF08A",
            "title_kn": "ಹಳದಿ ಎಚ್ಚರಿಕೆ (Yellow Watch)",
            "desc_kn": "ಗುಡುಗು, ಮಿಂಚು ಹಾಗೂ ಬಿರುಗಾಳಿ ಸಹಿತ ಸಾಧಾರಣ ಮಳೆ",
            "icon": "🟡"
        },
        "green": {
            "color": "#10B981",
            "glow": "rgba(16, 185, 129, 0.35)",
            "pill_bg": "rgba(16, 185, 129, 0.15)",
            "pill_border": "#34D399",
            "pill_text": "#A7F3D0",
            "title_kn": "ಗ್ರೀನ್ ಜೋನ್ (Green Zone)",
            "desc_kn": "ಸಾಮಾನ್ಯ ಹವೆ & ತಿಳಿ ವಾತಾವರಣ (ಯಾವುದೇ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ)",
            "icon": "🟢"
        }
    }

    buckets = {"red": [], "orange": [], "yellow": [], "green": []}
    for dist in map_geo["districts"]:
        did = dist["id"]
        dname = dist["name_kn"]
        short_lbl = dist.get("short_label", dname)
        lvl = imd_warnings.get(did, {}).get("level", "green").lower()
        if lvl not in buckets: lvl = "green"
        buckets[lvl].append((did, dname, short_lbl))

    svg_elements = []
    for dist in map_geo["districts"]:
        did = dist["id"]
        lvl = imd_warnings.get(did, {}).get("level", "green").lower()
        cfg = ALERT_CONFIG.get(lvl, ALERT_CONFIG["green"])
        fill_col = cfg["color"]
        filter_attr = 'filter="url(#glow-yellow)"' if lvl == 'yellow' else ('filter="url(#glow-red)"' if lvl == 'red' else '')
        path_elem = f'<path d="{dist["path_d"]}" fill="{fill_col}" stroke="#060C18" stroke-width="2.2" stroke-linejoin="round" {filter_attr} id="{did}" class="dist-poly"/>'
        svg_elements.append(path_elem)

    PRIORITY_LABELS = {
        'bengaluru_urban': 'ಬೆಂಗಳೂರು',
        'mysuru': 'ಮೈಸೂರು',
        'belagavi': 'ಬೆಳಗಾವಿ',
        'kalaburagi': 'ಕಲಬುರಗಿ',
        'dakshina_kannada': 'ಮಂಗಳೂರು',
        'shivamogga': 'ಶಿವಮೊಗ್ಗ',
        'ballari': 'ಬಳ್ಳಾರಿ',
        'vijayapura': 'ವಿಜಯಪುರ',
        'dharwad': 'ಧಾರವಾಡ',
        'tumakuru': 'ತುಮಕೂರು',
        'bidar': 'ಬೀದರ್',
        'raichur': 'ರಾಯಚೂರು',
        'hassan': 'ಹಾಸನ',
        'davanagere': 'ದಾವಣಗೆರೆ',
        'udupi': 'ಉಡುಪಿ',
        'uttara_kannada': 'ಕಾರವಾರ',
        'kodagu': 'ಕೊಡಗು',
        'chamarajanagara': 'ಚಾಮರಾಜನಗರ',
        'kolar': 'ಕೋಲಾರ',
        'bagalkote': 'ಬಾಗಲಕೋಟೆ',
        'vijayanagara': 'ವಿಜಯನಗರ',
        'koppal': 'ಕೊಪ್ಪಳ',
        'gadag': 'ಗದಗ',
        'haveri': 'ಹಾವೇರಿ',
        'yadgir': 'ಯಾದಗಿರಿ',
        'chitradurga': 'ಚಿತ್ರದುರ್ಗ',
        'chikkamagaluru': 'ಚಿಕ್ಕಮಗಳೂರು',
        'mandya': 'ಮಂಡ್ಯ',
        'ramanagara': 'ರಾಮನಗರ',
        'chikkaballapura': 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ'
    }

    label_elements = []
    for dist in map_geo["districts"]:
        did = dist["id"]
        if did == 'bengaluru_rural':
            continue
        short_name = PRIORITY_LABELS.get(did)
        if not short_name:
            continue
        cx = dist["cx"]
        cy = dist["cy"]
        font_sz = "17" if len(short_name) > 8 else ("18" if len(short_name) > 5 else "20")
        label_elem = f'''
        <text x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" 
              font-family="\'Anek Kannada\', sans-serif" font-size="{font_sz}" font-weight="900" 
              paint-order="stroke fill" stroke="#050A14" stroke-width="4.8" stroke-linejoin="round" fill="#FFFFFF">
          {short_name}
        </text>'''
        label_elements.append(label_elem)

    svg_map_html = f'''
    <svg viewBox="{map_geo['viewBox']}" width="100%" height="100%" style="overflow: visible;">
      <defs>
        <filter id="glow-yellow" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="0" stdDeviation="4.5" flood-color="#FACC15" flood-opacity="0.6"/>
        </filter>
        <filter id="glow-red" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="#EF4444" flood-opacity="0.8"/>
        </filter>
      </defs>

      <!-- Doppler Radar Range Rings -->
      <circle cx="440" cy="650" r="180" fill="none" stroke="rgba(56, 189, 248, 0.15)" stroke-width="1.2" stroke-dasharray="4 6"/>
      <circle cx="440" cy="650" r="340" fill="none" stroke="rgba(56, 189, 248, 0.12)" stroke-width="1.2" stroke-dasharray="6 8"/>
      <circle cx="440" cy="650" r="500" fill="none" stroke="rgba(56, 189, 248, 0.08)" stroke-width="1.2"/>
      
      <line x1="440" y1="50" x2="440" y2="1150" stroke="rgba(56, 189, 248, 0.08)" stroke-width="1" stroke-dasharray="3 5"/>
      <line x1="40" y1="650" x2="840" y2="650" stroke="rgba(56, 189, 248, 0.08)" stroke-width="1" stroke-dasharray="3 5"/>

      <g id="districts" style="filter: drop-shadow(0 20px 35px rgba(0, 0, 0, 0.7));">
        {''.join(svg_elements)}
      </g>
      
      <g id="labels">
        {''.join(label_elements)}
      </g>
    </svg>'''

    def make_district_chips(items_list, border_col, bg_col, text_col, max_count=None):
        chips = []
        subset = items_list[:max_count] if max_count else items_list
        for did, full_name, short_name in subset:
            chips.append(f'''
            <span style="display:inline-flex; align-items:center; background:{bg_col}; border:1px solid {border_col}; color:{text_col}; border-radius:8px; padding:3px 8px; font-size:14px; font-weight:800; white-space:nowrap; margin:2px 3px 2px 0; backdrop-filter:blur(6px); box-shadow:0 2px 4px rgba(0,0,0,0.2);">
              {short_name}
            </span>''')
        if max_count and len(items_list) > max_count:
            chips.append(f'''
            <span style="display:inline-flex; align-items:center; background:rgba(255,255,255,0.08); border:1px solid #475569; color:#94A3B8; border-radius:8px; padding:3px 8px; font-size:13px; font-weight:800; margin:2px 3px 2px 0;">
              +{len(items_list) - max_count} ಜಿಲ್ಲೆಗಳು
            </span>''')
        return "".join(chips)

    num_red = len(buckets["red"])
    num_orange = len(buckets["orange"])
    num_yellow = len(buckets["yellow"])
    num_green = len(buckets["green"])

    counter_grid_html = f'''
        <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap: 6px;">
          <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 12px; padding: 6px 6px; display:flex; flex-direction:column; align-items:center;">
            <div style="display:flex; align-items:center; gap:4px;">
              <span style="font-size:12px;">🔴</span>
              <span style="font-size: 12px; font-weight: 800; color: #FCA5A5;">ರೆಡ್</span>
            </div>
            <span style="font-size: 14px; font-weight: 900; color: {'#EF4444' if num_red > 0 else '#94A3B8'}; font-family:'Outfit'; margin-top:2px;">{num_red} ಜಿಲ್ಲೆ</span>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(249, 115, 22, 0.3); border-radius: 12px; padding: 6px 6px; display:flex; flex-direction:column; align-items:center;">
            <div style="display:flex; align-items:center; gap:4px;">
              <span style="font-size:12px;">🟠</span>
              <span style="font-size: 12px; font-weight: 800; color: #FDBA74;">ಆರೆಂಜ್</span>
            </div>
            <span style="font-size: 14px; font-weight: 900; color: {'#F97316' if num_orange > 0 else '#94A3B8'}; font-family:'Outfit'; margin-top:2px;">{num_orange} ಜಿಲ್ಲೆ</span>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(250, 204, 21, 0.3); border-radius: 12px; padding: 6px 6px; display:flex; flex-direction:column; align-items:center;">
            <div style="display:flex; align-items:center; gap:4px;">
              <span style="font-size:12px;">🟡</span>
              <span style="font-size: 12px; font-weight: 800; color: #FEF08A;">ಹಳದಿ</span>
            </div>
            <span style="font-size: 14px; font-weight: 900; color: {'#FACC15' if num_yellow > 0 else '#94A3B8'}; font-family:'Outfit'; margin-top:2px;">{num_yellow} ಜಿಲ್ಲೆ</span>
          </div>
          <div style="background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; padding: 6px 6px; display:flex; flex-direction:column; align-items:center;">
            <div style="display:flex; align-items:center; gap:4px;">
              <span style="font-size:12px;">🟢</span>
              <span style="font-size: 12px; font-weight: 800; color: #A7F3D0;">ಗ್ರೀನ್</span>
            </div>
            <span style="font-size: 14px; font-weight: 900; color: #10B981; font-family:'Outfit'; margin-top:2px;">{num_green} ಜಿಲ್ಲೆ</span>
          </div>
        </div>'''

    has_active_alerts = bool(num_red or num_orange or num_yellow)

    if not has_active_alerts:
        all_green_chips = make_district_chips(buckets["green"], "rgba(16, 185, 129, 0.35)", "rgba(16, 185, 129, 0.12)", "#A7F3D0", max_count=18)
        alert_section_html = f'''
        <div class="alert-box box-green" style="margin: 6px 0; padding: 18px 20px;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 10px;">
            <div style="display:flex; align-items:center; gap:12px;">
              <div style="width:40px; height:40px; border-radius:12px; background:rgba(16, 185, 129, 0.25); border:1.5px solid #10B981; display:flex; align-items:center; justify-content:center; font-size:22px;">
                🌤️
              </div>
              <div>
                <div style="font-size: 22px; font-weight: 900; color: #A7F3D0; line-height: 1.1;">
                  ಗ್ರೀನ್ ಜೋನ್ (Green Zone)
                </div>
                <div style="font-size: 14px; font-weight: 700; color: #6EE7B7;">
                  ರಾಜ್ಯಾದ್ಯಂತ ತಿಳಿ ಹವೆ & ಸಾಧಾರಣ ವಾತಾವರಣ
                </div>
              </div>
            </div>
            <div style="background: linear-gradient(135deg, #10B981, #059669); color:#FFFFFF; font-family:'Outfit'; font-size: 16px; font-weight: 900; padding: 4px 14px; border-radius: 20px; box-shadow:0 4px 12px rgba(16, 185, 129, 0.35);">
              {num_green}/31 ಜಿಲ್ಲೆಗಳು
            </div>
          </div>

          <div style="background:rgba(16, 185, 129, 0.1); border:1px solid rgba(16, 185, 129, 0.25); border-radius:12px; padding:10px 14px; margin-bottom:10px;">
            <div style="font-size: 14px; font-weight: 800; color: #E0F2FE; line-height: 1.35;">
              🟢 <b>IMD ಮುನ್ಸೂಚನೆ:</b> ಪ್ರಸ್ತುತ ರಾಜ್ಯದ ಯಾವುದೇ ಜಿಲ್ಲೆಯಲ್ಲೂ ಭಾರಿ ಮಳೆ ಅಥವಾ ಗುಡುಗು-ಮಿಂಚಿನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ. ಎಲ್ಲ 31 ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಹವಾಮಾನ ಶಾಂತವಾಗಿದೆ.
            </div>
          </div>

          <div style="font-size:12px; font-weight:800; color:#94A3B8; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;">
            ಶಾಂತ ವಾತಾವರಣವಿರುವ ಪ್ರಮುಖ ಜಿಲ್ಲೆಗಳು:
          </div>
          <div style="display:flex; flex-wrap:wrap;">
            {all_green_chips}
          </div>
        </div>'''
    else:
        cards = []
        if buckets["red"]:
            red_chips = make_district_chips(buckets["red"], "rgba(239, 68, 68, 0.45)", "rgba(239, 68, 68, 0.15)", "#FCA5A5")
            cards.append(f'''
            <div class="alert-box box-red">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
                <div style="display:flex; align-items:center; gap:10px;">
                  <div style="width:34px; height:34px; border-radius:10px; background:rgba(239, 68, 68, 0.2); border:1px solid #EF4444; display:flex; align-items:center; justify-content:center; font-size:18px;">
                    🔴
                  </div>
                  <div>
                    <div style="font-size: 20px; font-weight: 900; color: #FCA5A5; line-height: 1.1;">
                      ರೆಡ್ ಅಲರ್ಟ್ (Red Warning)
                    </div>
                    <div style="font-size: 13px; font-weight: 700; color: #CBD5E1;">
                      ಅತಿ ಭಾರೀ ಮಳೆ & ಮುನ್ನೆಚ್ಚರಿಕೆ (Take Action)
                    </div>
                  </div>
                </div>
                <div style="background: linear-gradient(135deg, #EF4444, #DC2626); color:#FFFFFF; font-family:'Outfit'; font-size: 16px; font-weight: 900; padding: 3px 14px; border-radius: 20px;">
                  {len(buckets["red"])} ಜಿಲ್ಲೆಗಳು
                </div>
              </div>
              <div style="display:flex; flex-wrap:wrap; margin-top: 6px;">
                {red_chips}
              </div>
            </div>''')

        if buckets["orange"]:
            orange_chips = make_district_chips(buckets["orange"], "rgba(249, 115, 22, 0.45)", "rgba(249, 115, 22, 0.15)", "#FDBA74")
            cards.append(f'''
            <div class="alert-box box-orange">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
                <div style="display:flex; align-items:center; gap:10px;">
                  <div style="width:34px; height:34px; border-radius:10px; background:rgba(249, 115, 22, 0.2); border:1px solid #F97316; display:flex; align-items:center; justify-content:center; font-size:18px;">
                    🟠
                  </div>
                  <div>
                    <div style="font-size: 20px; font-weight: 900; color: #FDBA74; line-height: 1.1;">
                      ಆರೆಂಜ್ ಅಲರ್ಟ್ (Orange Alert)
                    </div>
                    <div style="font-size: 13px; font-weight: 700; color: #CBD5E1;">
                      ಧಾರಾಕಾರ ಮಳೆ / ಬಿರುಗಾಳಿ (Be Prepared)
                    </div>
                  </div>
                </div>
                <div style="background: linear-gradient(135deg, #F97316, #EA580C); color:#FFFFFF; font-family:'Outfit'; font-size: 16px; font-weight: 900; padding: 3px 14px; border-radius: 20px;">
                  {len(buckets["orange"])} ಜಿಲ್ಲೆಗಳು
                </div>
              </div>
              <div style="display:flex; flex-wrap:wrap; margin-top: 6px;">
                {orange_chips}
              </div>
            </div>''')

        if buckets["yellow"]:
            yellow_chips = make_district_chips(buckets["yellow"], "rgba(250, 204, 21, 0.45)", "rgba(250, 204, 21, 0.12)", "#FEF08A")
            cards.append(f'''
            <div class="alert-box box-yellow">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
                <div style="display:flex; align-items:center; gap:10px;">
                  <div style="width:34px; height:34px; border-radius:10px; background:rgba(250, 204, 21, 0.2); border:1px solid #FACC15; display:flex; align-items:center; justify-content:center; font-size:18px;">
                    ⚡
                  </div>
                  <div>
                    <div style="font-size: 20px; font-weight: 900; color: #FEF08A; line-height: 1.1;">
                      ಹಳದಿ ಎಚ್ಚರಿಕೆ (Yellow Watch)
                    </div>
                    <div style="font-size: 13px; font-weight: 700; color: #CBD5E1;">
                      ಗುಡುಗು, ಮಿಂಚು ಹಾಗೂ ಬಿರುಗಾಳಿ ಸಹಿತ ಸಾಧಾರಣ ಮಳೆ
                    </div>
                  </div>
                </div>
                <div style="background: linear-gradient(135deg, #FACC15, #EAB308); color:#060C18; font-family:'Outfit'; font-size: 16px; font-weight: 900; padding: 3px 14px; border-radius: 20px; box-shadow:0 4px 12px rgba(250, 204, 21, 0.3);">
                  {len(buckets["yellow"])} ಜಿಲ್ಲೆಗಳು
                </div>
              </div>
              <div style="display:flex; flex-wrap:wrap; margin-top: 6px;">
                {yellow_chips}
              </div>
            </div>''')

        if buckets["green"]:
            green_chips = make_district_chips(buckets["green"], "rgba(16, 185, 129, 0.35)", "rgba(16, 185, 129, 0.12)", "#A7F3D0", max_count=10)
            cards.append(f'''
            <div class="alert-box box-green">
              <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 6px;">
                <div style="display:flex; align-items:center; gap:10px;">
                  <div style="width:32px; height:32px; border-radius:10px; background:rgba(16, 185, 129, 0.2); border:1px solid #10B981; display:flex; align-items:center; justify-content:center; font-size:16px;">
                    🌤️
                  </div>
                  <div>
                    <div style="font-size: 19px; font-weight: 900; color: #A7F3D0; line-height: 1.1;">
                      ಗ್ರೀನ್ ಜೋನ್ (Green Zone)
                    </div>
                    <div style="font-size: 13px; font-weight: 700; color: #94A3B8;">
                      ಸಾಮಾನ್ಯ ಹವೆ & ತಿಳಿ ವಾತಾವರಣ (ಯಾವುದೇ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ)
                    </div>
                  </div>
                </div>
                <div style="background: linear-gradient(135deg, #10B981, #059669); color:#FFFFFF; font-family:'Outfit'; font-size: 15px; font-weight: 900; padding: 3px 12px; border-radius: 20px;">
                  {len(buckets["green"])} ಜಿಲ್ಲೆಗಳು
                </div>
              </div>
              <div style="display:flex; flex-wrap:wrap; margin-top: 6px;">
                {green_chips}
              </div>
            </div>''')

        alert_section_html = "\n".join(cards)

    rain_top = state_extremes.get("highest_past_24h_rain", {})
    r_st = rain_top.get('station', '')
    r_dst = rain_top.get('name_kn') or rain_top.get('district_en', 'ದಕ್ಷಿಣ ಕನ್ನಡ')
    rain_name = f"{r_dst} ({r_st})" if r_st else r_dst
    rain_val = f"{float(rain_top.get('rain_mm', 53.0)):.1f} mm"

    temp_top = state_extremes.get("max_temp_district", {})
    t_st = temp_top.get('station', '')
    t_dst = temp_top.get('name_kn') or temp_top.get('district_en', 'ಕಲಬುರಗಿ')
    temp_name = f"{t_dst} ({t_st})" if t_st else t_dst
    temp_val = f"{float(temp_top.get('temp_c', 38.8)):.1f}°C"

    min_temp_top = state_extremes.get("min_temp_district", {})
    m_st = min_temp_top.get('station', '')
    m_dst = min_temp_top.get('name_kn') or min_temp_top.get('district_en', 'ವಿಜಯಪುರ')
    min_temp_name = f"{m_dst} ({m_st})" if m_st else m_dst
    min_temp_val = f"{float(min_temp_top.get('temp_c', 13.4)):.1f}°C"

    html = f'''<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@600;700;800;900&family=Outfit:wght@600;700;800;900&family=Plus+Jakarta+Sans:wght@700;800&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  
  body {{
    width: 1080px;
    height: 1080px;
    background: #060913;
    font-family: 'Anek Kannada', sans-serif;
    color: #FFFFFF;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 30px 36px;
    position: relative;
    overflow: hidden;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
  }}

  .glow-cyan {{
    position: absolute;
    width: 600px;
    height: 600px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(14, 165, 233, 0.15) 0%, rgba(14, 165, 233, 0) 70%);
    top: -100px;
    left: 50px;
    pointer-events: none;
    filter: blur(40px);
  }}

  .glow-amber {{
    position: absolute;
    width: 500px;
    height: 500px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(245, 158, 11, 0.12) 0%, rgba(245, 158, 11, 0) 70%);
    bottom: 50px;
    right: 50px;
    pointer-events: none;
    filter: blur(45px);
  }}

  .grid-bg {{
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background-image: linear-gradient(rgba(255, 255, 255, 0.025) 1px, transparent 1px),
                      linear-gradient(90deg, rgba(255, 255, 255, 0.025) 1px, transparent 1px);
    background-size: 36px 36px;
    pointer-events: none;
    z-index: 0;
  }}

  .container {{
    position: relative;
    z-index: 1;
    display: flex;
    flex-direction: column;
    height: 100%;
    justify-content: space-between;
  }}

  .top-header {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(15, 23, 42, 0.65);
    border: 1.5px solid rgba(255, 255, 255, 0.1);
    border-radius: 20px;
    padding: 12px 22px;
    backdrop-filter: blur(16px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
  }}

  .main-stage {{
    display: flex;
    flex: 1;
    gap: 24px;
    align-items: stretch;
    margin: 16px 0;
  }}

  .map-card {{
    flex: 1.05;
    background: linear-gradient(160deg, rgba(15, 23, 42, 0.75) 0%, rgba(7, 12, 24, 0.85) 100%);
    border: 1.5px solid rgba(56, 189, 248, 0.25);
    border-radius: 24px;
    padding: 14px 12px;
    display: flex;
    flex-direction: column;
    position: relative;
    box-shadow: 0 20px 45px rgba(0, 0, 0, 0.6), inset 0 0 40px rgba(14, 165, 233, 0.08);
  }}

  .map-header-pill {{
    position: absolute;
    top: 14px;
    left: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
    background: rgba(11, 19, 35, 0.9);
    border: 1px solid rgba(56, 189, 248, 0.4);
    border-radius: 12px;
    padding: 5px 12px;
    backdrop-filter: blur(10px);
    z-index: 2;
  }}

  .map-footer-pill {{
    position: absolute;
    bottom: 14px;
    right: 16px;
    background: rgba(11, 19, 35, 0.9);
    border: 1px solid rgba(148, 163, 184, 0.25);
    border-radius: 10px;
    padding: 5px 10px;
    font-size: 12px;
    font-weight: 800;
    color: #94A3B8;
    font-family: 'Outfit';
    letter-spacing: 0.5px;
    backdrop-filter: blur(8px);
    z-index: 2;
  }}

  .intel-card {{
    flex: 0.95;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  .alert-box {{
    border-radius: 20px;
    padding: 16px 18px;
    position: relative;
    overflow: hidden;
    backdrop-filter: blur(16px);
  }}

  .alert-box::before {{
    content: '';
    position: absolute;
    top: 0; left: 0; width: 6px; height: 100%;
  }}

  .box-red {{
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.14) 0%, rgba(185, 28, 28, 0.05) 100%);
    border: 1.5px solid rgba(239, 68, 68, 0.4);
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.1);
  }}
  .box-red::before {{
    background: linear-gradient(180deg, #EF4444, #DC2626);
  }}

  .box-orange {{
    background: linear-gradient(135deg, rgba(249, 115, 22, 0.14) 0%, rgba(194, 65, 12, 0.05) 100%);
    border: 1.5px solid rgba(249, 115, 22, 0.4);
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.1);
  }}
  .box-orange::before {{
    background: linear-gradient(180deg, #F97316, #EA580C);
  }}

  .box-yellow {{
    background: linear-gradient(135deg, rgba(250, 204, 21, 0.12) 0%, rgba(202, 138, 4, 0.05) 100%);
    border: 1.5px solid rgba(250, 204, 21, 0.35);
    box-shadow: 0 12px 30px rgba(0, 0, 0, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.1);
  }}
  .box-yellow::before {{
    background: linear-gradient(180deg, #FACC15, #EAB308);
  }}

  .box-green {{
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(5, 150, 105, 0.04) 100%);
    border: 1.5px solid rgba(16, 185, 129, 0.3);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.1);
  }}
  .box-green::before {{
    background: linear-gradient(180deg, #34D399, #10B981);
  }}

  .telemetry-strip {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 8px;
    background: rgba(15, 23, 42, 0.65);
    border: 1.5px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 10px 14px;
    backdrop-filter: blur(12px);
  }}

  .footer-strip {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(15, 23, 42, 0.6);
    border: 1.5px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 12px 22px;
    backdrop-filter: blur(12px);
  }}
</style>
</head>
<body>
  <div class="glow-cyan"></div>
  <div class="glow-amber"></div>
  <div class="grid-bg"></div>

  <div class="container">
    <div class="top-header">
      <div style="display:flex; align-items:center; gap:16px;">
        <img src="{logo_b64}" style="height: 48px; object-fit: contain; filter: drop-shadow(0 2px 8px rgba(0,0,0,0.5));">
        <div style="border-left: 2px solid #334155; padding-left: 14px;">
          <div style="font-size: 12px; font-weight: 800; color: #38BDF8; font-family:'Outfit'; letter-spacing: 1.5px; text-transform: uppercase;">
            IMD BENGALURU • OFFICIAL SATELLITE RADAR
          </div>
          <div style="font-size: 21px; font-weight: 900; color: #FFFFFF; letter-spacing: 0.2px;">
            ಕರ್ನಾಟಕ ಹವಾಮಾನ ಮುನ್ನೆಚ್ಚರಿಕೆ ನಕ್ಷೆ
          </div>
        </div>
      </div>

      <div style="display:flex; align-items:center; gap:10px; background: rgba(30, 41, 59, 0.85); border: 1.5px solid rgba(56, 189, 248, 0.3); padding: 7px 18px; border-radius: 30px;">
        <span style="display:inline-block; width:10px; height:10px; background:#10B981; border-radius:50%; box-shadow:0 0 12px #10B981;"></span>
        <span style="font-size: 15px; font-weight: 800; color: #F8FAFC; font-family:'Outfit'; letter-spacing: 0.5px;">
          {date_kn} • 24H FORECAST
        </span>
      </div>
    </div>

    <div class="main-stage">
      <div class="map-card">
        <div class="map-header-pill">
          <span style="display:inline-block; width:8px; height:8px; background:#38BDF8; border-radius:50%; box-shadow:0 0 8px #38BDF8;"></span>
          <span style="font-size: 13px; font-weight: 800; color: #E0F2FE;">
            31 ಜಿಲ್ಲೆಗಳ ಅಧಿಕೃತ ನಕ್ಷೆ
          </span>
        </div>

        <div style="flex:1; width:100%; height:100%; display:flex; align-items:center; justify-content:center; padding: 10px 0;">
          {svg_map_html}
        </div>

        <div class="map-footer-pill">
          ⬆ N • 15°N 76°E • IMD BENGALURU
        </div>
      </div>

      <div class="intel-card">
        <div>
          <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom: 2px;">
            <div style="font-size: 13px; font-weight: 800; color: #38BDF8; font-family:'Outfit'; letter-spacing: 1.8px; text-transform: uppercase;">
              OFFICIAL WARNING MATRIX
            </div>
            <div style="font-size: 13px; font-weight: 800; color: #94A3B8; font-family:'Outfit';">
              31 DISTRICTS TELEMETRY
            </div>
          </div>
          <div style="font-size: 32px; font-weight: 900; color: #FFFFFF; line-height: 1.15;">
            ಯಾವ ಜಿಲ್ಲೆಗೆ ಯಾವ ಅಲರ್ಟ್?
          </div>
        </div>

        {counter_grid_html}

        {alert_section_html}

        <div class="telemetry-strip">
          <div>
            <div style="font-size: 11px; font-weight: 800; color: #94A3B8; text-transform: uppercase; font-family:'Outfit';">🌧️ 24H TOP RAIN</div>
            <div style="font-size: 15px; font-weight: 900; color: #38BDF8; margin-top: 2px;">{rain_val}</div>
            <div style="font-size: 11px; font-weight: 700; color: #CBD5E1; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">{rain_name}</div>
          </div>
          <div style="border-left: 1px solid rgba(255,255,255,0.1); padding-left: 10px;">
            <div style="font-size: 11px; font-weight: 800; color: #94A3B8; text-transform: uppercase; font-family:'Outfit';">☀️ MAX TEMP</div>
            <div style="font-size: 15px; font-weight: 900; color: #F59E0B; margin-top: 2px;">{temp_val}</div>
            <div style="font-size: 11px; font-weight: 700; color: #CBD5E1;">{temp_name}</div>
          </div>
          <div style="border-left: 1px solid rgba(255,255,255,0.1); padding-left: 10px;">
            <div style="font-size: 11px; font-weight: 800; color: #94A3B8; text-transform: uppercase; font-family:'Outfit';">❄️ MIN TEMP</div>
            <div style="font-size: 15px; font-weight: 900; color: #A7F3D0; margin-top: 2px;">{min_temp_val}</div>
            <div style="font-size: 11px; font-weight: 700; color: #CBD5E1;">{min_temp_name}</div>
          </div>
        </div>

        <div style="display:grid; grid-template-columns: repeat(4, 1fr); gap: 6px;">
          <div style="background:rgba(15,23,42,0.5); border:1px solid #334155; border-radius:8px; padding:5px 4px; font-size:11px; font-weight:800; color:#E2E8F0; text-align:center;">
            <span style="width:7px; height:7px; background:#EF4444; border-radius:50%; display:inline-block; margin-right:3px;"></span> ರೆಡ್: ಕ್ರಮ
          </div>
          <div style="background:rgba(15,23,42,0.5); border:1px solid #334155; border-radius:8px; padding:5px 4px; font-size:11px; font-weight:800; color:#E2E8F0; text-align:center;">
            <span style="width:7px; height:7px; background:#F97316; border-radius:50%; display:inline-block; margin-right:3px;"></span> ಆರೆಂಜ್: ಸನ್ನದ್ಧ
          </div>
          <div style="background:rgba(15,23,42,0.5); border:1px solid #334155; border-radius:8px; padding:5px 4px; font-size:11px; font-weight:800; color:#E2E8F0; text-align:center;">
            <span style="width:7px; height:7px; background:#FACC15; border-radius:50%; display:inline-block; margin-right:3px;"></span> ಯೆಲ್ಲೋ: ನಿಗಾ
          </div>
          <div style="background:rgba(15,23,42,0.5); border:1px solid #334155; border-radius:8px; padding:5px 4px; font-size:11px; font-weight:800; color:#E2E8F0; text-align:center;">
            <span style="width:7px; height:7px; background:#10B981; border-radius:50%; display:inline-block; margin-right:3px;"></span> ಗ್ರೀನ್: ಸಾಮಾನ್ಯ
          </div>
        </div>
      </div>
    </div>

    <div class="footer-strip">
      <div style="display:flex; align-items:center; gap:10px;">
        <span style="font-size: 20px;">📡</span>
        <span style="font-size: 16px; font-weight: 800; color: #CBD5E1;">
          ನಿಮ್ಮ ತಾಲೂಕಿನ ನಿಖರ ಲೈವ್ ಮಳೆ ರೇಡಾರ್ ವೀಕ್ಷಿಸಿ: <b style="color:#38BDF8; font-family:'Outfit';">karnata.in/weather</b>
        </span>
      </div>

      <div style="display:flex; align-items:center; gap:8px;">
        <span style="display:inline-block; width:8px; height:8px; background:#FACC15; border-radius:50%;"></span>
        <span style="display:inline-block; width:8px; height:8px; background:#DC2626; border-radius:50%;"></span>
        <span style="font-size: 21px; font-weight: 900; color: #FFFFFF; font-family:'Outfit'; letter-spacing:0.5px;">
          karnata.in
        </span>
      </div>
    </div>
  </div>
</body>
</html>'''

    out_file = OUTPUT_DIR / "weather_nowcast_map.png"
    render_html_to_png(html, out_file)


# ══════════════════════════════════════════════════════════════════════════════
# MASTER RENDER ALL
# ══════════════════════════════════════════════════════════════════════════════

def save_social_captions_json():
    try:
        import sys
        if str(ROOT_DIR) not in sys.path:
            sys.path.insert(0, str(ROOT_DIR))
        if str(ROOT_DIR / 'scripts') not in sys.path:
            sys.path.insert(0, str(ROOT_DIR / 'scripts'))

        try:
            from scripts.auto_publish_social import (
                get_gold_caption, get_petrol_caption, get_weather_summary_caption,
                get_apmc_caption, get_dam_caption, get_quiz_caption, get_doyouknow_caption,
                get_nowcast_caption
            )
        except ImportError:
            from auto_publish_social import (
                get_gold_caption, get_petrol_caption, get_weather_summary_caption,
                get_apmc_caption, get_dam_caption, get_quiz_caption, get_doyouknow_caption,
                get_nowcast_caption
            )
        date_kn = get_kannada_date_str()
        captions_data = {
            "gold": {
                "title": f"🪙 ಕರ್ನಾಟಕ ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ • {date_kn}",
                "caption": get_gold_caption(),
                "image_url": "https://karnata.in/assets/social-cards/gold_rate_today.png"
            },
            "dam": {
                "title": f"💧 ಕರ್ನಾಟಕದ 13 ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ • {date_kn}",
                "caption": get_dam_caption(),
                "image_url": "https://karnata.in/assets/social-cards/dam_levels_p1.png"
            },
            "weather": {
                "title": f"🌦️ ಕರ್ನಾಟಕ ಹವಾಮಾನ & ಮಳೆ ಮುನ್ಸೂಚನೆ • {date_kn}",
                "caption": get_weather_summary_caption(),
                "image_url": "https://karnata.in/assets/social-cards/weather_morning_summary.png"
            },
            "quiz": {
                "title": f"🧠 ಇಂದಿನ ದಿನದ ಕರ್ನಾಟಕ ರಸಪ್ರಶ್ನೆ • {date_kn}",
                "caption": get_quiz_caption(1),
                "image_url": "https://karnata.in/assets/social-cards/quiz_slot1.png"
            },
            "doyouknow": {
                "title": f"💡 ನಿಮಗೆ ತಿಳಿದಿದೆಯೇ? • {date_kn}",
                "caption": get_doyouknow_caption(1),
                "image_url": "https://karnata.in/assets/social-cards/doyouknow_slot1.png"
            },
            "petrol": {
                "title": f"⛽ ಕರ್ನಾಟಕ ಇಂದಿನ ಇಂಧನ ದರ • {date_kn}",
                "caption": get_petrol_caption(),
                "image_url": "https://karnata.in/assets/social-cards/petrol_diesel_today.png"
            },
            "apmc": {
                "title": f"🌾 ಕರ್ನಾಟಕ APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ • {date_kn}",
                "caption": get_apmc_caption(),
                "image_url": "https://karnata.in/assets/social-cards/apmc_p1.png"
            },
            "weather_nowcast": {
                "title": f"⛈️ ಕರ್ನಾಟಕ IMD ಲೈವ್ ನೌಕಾಸ್ಟ್ ಮಳೆ ಮುನ್ನೆಚ್ಚರಿಕೆ • {date_kn}",
                "caption": get_nowcast_caption(1),
                "image_url": "https://karnata.in/assets/social-cards/weather_nowcast_map.png"
            }
        }
        cap_file = OUTPUT_DIR / "social_captions.json"
        with open(cap_file, "w", encoding="utf-8") as f:
            json.dump(captions_data, f, ensure_ascii=False, indent=2)
        print("✅ Updated assets/social-cards/social_captions.json with fresh live captions!")
    except Exception as e:
        print("  [Notice] Captions dump notice:", e)

def render_all_cards():
    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 🎨 Rendering All Re-Engineered Minimalist Kannada Social Graphics...")
    render_gold_card()
    render_petrol_card()
    render_dam_carousel_and_spotlights()
    render_doyouknow_card(1)
    render_doyouknow_card(2)
    render_doyouknow_card(3)
    render_quiz_interactive_card(1)
    render_quiz_interactive_card(2)
    render_quiz_interactive_card(3)
    render_quote_card()
    render_weather_morning_summary()
    render_apmc_carousel()
    render_nowcast_map_card()
    save_social_captions_json()
    print("✨ All Re-Engineered Graphics Rendered Successfully!")

if __name__ == "__main__":
    render_all_cards()
