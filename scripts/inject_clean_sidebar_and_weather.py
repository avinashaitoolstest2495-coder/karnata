# -*- coding: utf-8 -*-
"""
Karnata — scripts/inject_clean_sidebar_and_weather.py
Clean replacement of sidebar and creative weather in all 31 districts.
"""

import os
import glob
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

DISTRICT_META = {
    "bengaluru-urban": {"name_kn": "ಬೆಂಗಳೂರು ನಗರ", "name_en": "Bengaluru Urban", "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", "temp": "26°C", "humidity": "68%", "wind": "14 km/h", "uv": "6 (ಮಧ್ಯಮ)", "aqi": "58 (ಉತ್ತಮ)", "cond": "ಭಾಗಶಃ ಮೋಡ", "imd_alert": "🟢 ಶುಷ್ಕ ಹಾಗೂ ಆಹ್ಲಾದಕರ ವಾತಾವರಣ", "imd_color": "#16A34A", "petrol": 110.89, "diesel": 98.80},
    "bengaluru-rural": {"name_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "name_en": "Bengaluru Rural", "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", "temp": "27°C", "humidity": "65%", "wind": "12 km/h", "uv": "7 (ಹೆಚ್ಚು)", "aqi": "52 (ಉತ್ತಮ)", "cond": "ಸ್ವಚ್ಛ ಆಕಾಶ", "imd_alert": "🟢 ಶುಷ್ಕ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 111.02, "diesel": 98.92},
    "ramanagara": {"name_kn": "ರಾಮನಗರ", "name_en": "Ramanagara", "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", "temp": "28°C", "humidity": "64%", "wind": "11 km/h", "uv": "7 (ಹೆಚ್ಚು)", "aqi": "48 (ಉತ್ತಮ)", "cond": "ಸ್ವಚ್ಛ ಬಿಸಿಲು", "imd_alert": "🟢 ಸಾಮಾನ್ಯ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 111.15, "diesel": 99.04},
    "chikkaballapura": {"name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "name_en": "Chikkaballapura", "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", "temp": "27°C", "humidity": "62%", "wind": "15 km/h", "uv": "6 (ಮಧ್ಯಮ)", "aqi": "45 (ಉತ್ತಮ)", "cond": "ತಂಪಾದ ಗಾಳಿ", "imd_alert": "🟢 ಶುಷ್ಕ ವಾತಾವರಣ", "imd_color": "#16A34A", "petrol": 111.20, "diesel": 99.10},
    "kolar": {"name_kn": "ಕೋಲಾರ", "name_en": "Kolar", "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", "temp": "28°C", "humidity": "60%", "wind": "14 km/h", "uv": "7 (ಹೆಚ್ಚು)", "aqi": "50 (ಉತ್ತಮ)", "cond": "ಸ್ವಚ್ಛ ಆಕಾಶ", "imd_alert": "🟢 ಸಾಮಾನ್ಯ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 111.35, "diesel": 99.22},
    "tumakuru": {"name_kn": "ತುಮಕೂರು", "name_en": "Tumakuru", "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", "temp": "29°C", "humidity": "58%", "wind": "13 km/h", "uv": "7 (ಹೆಚ್ಚು)", "aqi": "54 (ಉತ್ತಮ)", "cond": "ಬಿಸಿಲು", "imd_alert": "🟢 ಶುಷ್ಕ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 111.10, "diesel": 99.00},
    "mysuru": {"name_kn": "ಮೈಸೂರು", "name_en": "Mysuru", "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", "temp": "27°C", "humidity": "72%", "wind": "10 km/h", "uv": "5 (ಮಧ್ಯಮ)", "aqi": "42 (ಅತ್ಯುತ್ತಮ)", "cond": "ತಂಪಾದ ಮೋಡ", "imd_alert": "🟡 ಸಂಜೆ ಸಾಧಾರಣ ಮಳೆ ಸಂಭವ", "imd_color": "#D97706", "petrol": 110.65, "diesel": 98.58},
    "mandya": {"name_kn": "ಮಂಡ್ಯ", "name_en": "Mandya", "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", "temp": "28°C", "humidity": "70%", "wind": "12 km/h", "uv": "6 (ಮಧ್ಯಮ)", "aqi": "46 (ಉತ್ತಮ)", "cond": "ಭಾಗಶಃ ಮೋಡ", "imd_alert": "🟢 ಸಾಮಾನ್ಯ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 110.80, "diesel": 98.72},
    "chamarajanagara": {"name_kn": "ಚಾಮರಾಜನಗರ", "name_en": "Chamarajanagara", "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", "temp": "28°C", "humidity": "74%", "wind": "9 km/h", "uv": "6 (ಮಧ್ಯಮ)", "aqi": "38 (ಅತ್ಯುತ್ತಮ)", "cond": "ಮೋಡ ಕವಿದ ವಾತಾವರಣ", "imd_alert": "🟡 ಹಗುರ ಮಳೆ ಮುನ್ನೆಚ್ಚರಿಕೆ", "imd_color": "#D97706", "petrol": 111.45, "diesel": 99.30},
    "hassan": {"name_kn": "ಹಾಸನ", "name_en": "Hassan", "region": "ಮಲೆನಾಡು", "temp": "24°C", "humidity": "82%", "wind": "16 km/h", "uv": "4 (ಕಡಿಮೆ)", "aqi": "35 (ಅತ್ಯುತ್ತಮ)", "cond": "ಮಂಜು ಮುಸುಕಿದ ವಾತಾವರಣ", "imd_alert": "🟡 ಸಾಧಾರಣ ಮಳೆ ಸಂಭವ", "imd_color": "#D97706", "petrol": 110.95, "diesel": 98.85},
    "kodagu": {"name_kn": "ಕೊಡಗು", "name_en": "Kodagu", "region": "ಮಲೆನಾಡು", "temp": "22°C", "humidity": "88%", "wind": "18 km/h", "uv": "4 (ಕಡಿಮೆ)", "aqi": "28 (ಅತ್ಯುತ್ತಮ)", "cond": "ಹಗುರ ತುಂತುರು ಮಳೆ", "imd_alert": "🟡 ಹಳದಿ ಅಲರ್ಟ್: ಮಲೆನಾಡು ಮಳೆ", "imd_color": "#D97706", "petrol": 111.75, "diesel": 99.55},
    "chikkamagaluru": {"name_kn": "ಚಿಕ್ಕಮಗಳೂರು", "name_en": "Chikkamagaluru", "region": "ಮಲೆನಾಡು", "temp": "23°C", "humidity": "85%", "wind": "15 km/h", "uv": "4 (ಕಡಿಮೆ)", "aqi": "32 (ಅತ್ಯುತ್ತಮ)", "cond": "ತಂಪಾದ ಗಾಳಿ & ಮೋಡ", "imd_alert": "🟡 ಹಗುರ ಮಳೆ ಮುನ್ಸೂಚನೆ", "imd_color": "#D97706", "petrol": 111.25, "diesel": 99.12},
    "shivamogga": {"name_kn": "ಶಿವಮೊಗ್ಗ", "name_en": "Shivamogga", "region": "ಮಲೆನಾಡು", "temp": "26°C", "humidity": "80%", "wind": "14 km/h", "uv": "5 (ಮಧ್ಯಮ)", "aqi": "40 (ಅತ್ಯುತ್ತಮ)", "cond": "ಭಾಗಶಃ ಮೋಡ", "imd_alert": "🟢 ಸಾಮಾನ್ಯ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 111.05, "diesel": 98.95},
    "dakshina-kannada": {"name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "name_en": "Dakshina Kannada", "region": "ಕರಾವಳಿ", "temp": "29°C", "humidity": "84%", "wind": "20 km/h", "uv": "7 (ಹೆಚ್ಚು)", "aqi": "45 (ಉತ್ತಮ)", "cond": "ಕರಾವಳಿ ತಂಗಾಳಿ", "imd_alert": "🟡 ಕರಾವಳಿ ಹಗುರ ಮಳೆ ಅಲರ್ಟ್", "imd_color": "#D97706", "petrol": 109.85, "diesel": 97.80},
    "udupi": {"name_kn": "ಉಡುಪಿ", "name_en": "Udupi", "region": "ಕರಾವಳಿ", "temp": "29°C", "humidity": "83%", "wind": "21 km/h", "uv": "7 (ಹೆಚ್ಚು)", "aqi": "44 (ಉತ್ತಮ)", "cond": "ಆರ್ದ್ರತೆಯುಕ್ತ ವಾತಾವರಣ", "imd_alert": "🟡 ಕರಾವಳಿ ಗಾಳಿ ಮುನ್ಸೂಚನೆ", "imd_color": "#D97706", "petrol": 109.95, "diesel": 97.90},
    "uttara-kannada": {"name_kn": "ಉತ್ತರ ಕನ್ನಡ", "name_en": "Uttara Kannada", "region": "ಕರಾವಳಿ", "temp": "28°C", "humidity": "82%", "wind": "19 km/h", "uv": "6 (ಮಧ್ಯಮ)", "aqi": "36 (ಅತ್ಯುತ್ತಮ)", "cond": "ಮೋಡ & ತಂಗಾಳಿ", "imd_alert": "🟢 ಸಾಮಾನ್ಯ ಕರಾವಳಿ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 110.40, "diesel": 98.35},
    "belagavi": {"name_kn": "ಬೆಳಗಾವಿ", "name_en": "Belagavi", "region": "ಉತ್ತರ ಕರ್ನಾಟಕ", "temp": "26°C", "humidity": "72%", "wind": "16 km/h", "uv": "6 (ಮಧ್ಯಮ)", "aqi": "50 (ಉತ್ತಮ)", "cond": "ತಂಪಾದ ಆಹ್ಲಾದಕರ ವಾತಾವರಣ", "imd_alert": "🟢 ಶುಷ್ಕ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 110.75, "diesel": 98.68},
    "dharwad": {"name_kn": "ಧಾರವಾಡ", "name_en": "Dharwad", "region": "ಉತ್ತರ ಕರ್ನಾಟಕ", "temp": "27°C", "humidity": "66%", "wind": "15 km/h", "uv": "6 (ಮಧ್ಯಮ)", "aqi": "48 (ಉತ್ತಮ)", "cond": "ಭಾಗಶಃ ಬಿಸಿಲು", "imd_alert": "🟢 ಸಾಮಾನ್ಯ ವಾತಾವರಣ", "imd_color": "#16A34A", "petrol": 110.50, "diesel": 98.45},
    "gadag": {"name_kn": "ಗದಗ", "name_en": "Gadag", "region": "ಉತ್ತರ ಕರ್ನಾಟಕ", "temp": "30°C", "humidity": "54%", "wind": "14 km/h", "uv": "8 (ಬಹಳ ಹೆಚ್ಚು)", "aqi": "52 (ಉತ್ತಮ)", "cond": "ಸ್ವಚ್ಛ ಬಿಸಿಲು", "imd_alert": "🟢 ಶುಷ್ಕ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 110.90, "diesel": 98.82},
    "haveri": {"name_kn": "ಹಾವೇರಿ", "name_en": "Haveri", "region": "ಉತ್ತರ ಕರ್ನಾಟಕ", "temp": "28°C", "humidity": "64%", "wind": "13 km/h", "uv": "7 (ಹೆಚ್ಚು)", "aqi": "46 (ಉತ್ತಮ)", "cond": "ಆಹ್ಲಾದಕರ ಬಿಸಿಲು", "imd_alert": "🟢 ಸಾಮಾನ್ಯ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 110.85, "diesel": 98.75},
    "bagalkote": {"name_kn": "ಬಾಗಲಕೋಟೆ", "name_en": "Bagalkote", "region": "ಉತ್ತರ ಕರ್ನಾಟಕ", "temp": "31°C", "humidity": "52%", "wind": "12 km/h", "uv": "8 (ಬಹಳ ಹೆಚ್ಚು)", "aqi": "55 (ಉತ್ತಮ)", "cond": "ಬಿಸಿಲು", "imd_alert": "🟢 ಶುಷ್ಕ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 111.12, "diesel": 99.02},
    "vijayapura": {"name_kn": "ವಿಜಯಪುರ", "name_en": "Vijayapura", "region": "ಉತ್ತರ ಕರ್ನಾಟಕ", "temp": "32°C", "humidity": "48%", "wind": "13 km/h", "uv": "8 (ಬಹಳ ಹೆಚ್ಚು)", "aqi": "58 (ಉತ್ತಮ)", "cond": "ಬಿಸಿಲು & ಶುಷ್ಕ ಗಾಳಿ", "imd_alert": "🟢 ಶುಷ್ಕ ವಾತಾವರಣ", "imd_color": "#16A34A", "petrol": 111.28, "diesel": 99.18},
    "kalaburagi": {"name_kn": "ಕಲಬುರಗಿ", "name_en": "Kalaburagi", "region": "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ", "temp": "33°C", "humidity": "46%", "wind": "14 km/h", "uv": "8 (ಬಹಳ ಹೆಚ್ಚು)", "aqi": "62 (ಸಾಧಾರಣ)", "cond": "ಪ್ರಖರ ಬಿಸಿಲು", "imd_alert": "🟢 ಶುಷ್ಕ ಹಾಗೂ ಬಿಸಿಲಿನ ವಾತಾವರಣ", "imd_color": "#16A34A", "petrol": 111.42, "diesel": 99.30},
    "yadgir": {"name_kn": "ಯಾದಗಿರಿ", "name_en": "Yadgir", "region": "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ", "temp": "33°C", "humidity": "45%", "wind": "13 km/h", "uv": "8 (ಬಹಳ ಹೆಚ್ಚು)", "aqi": "56 (ಉತ್ತಮ)", "cond": "ಬಿಸಿಲು", "imd_alert": "🟢 ಶುಷ್ಕ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 111.50, "diesel": 99.38},
    "bidar": {"name_kn": "ಬೀದರ್", "name_en": "Bidar", "region": "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ", "temp": "30°C", "humidity": "50%", "wind": "15 km/h", "uv": "7 (ಹೆಚ್ಚು)", "aqi": "54 (ಉತ್ತಮ)", "cond": "ಸ್ವಚ್ಛ ಆಕಾಶ", "imd_alert": "🟢 ಸಾಮಾನ್ಯ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 111.65, "diesel": 99.50},
    "raichur": {"name_kn": "ರಾಯಚೂರು", "name_en": "Raichur", "region": "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ", "temp": "34°C", "humidity": "44%", "wind": "12 km/h", "uv": "9 (ಅತ್ಯಧಿಕ)", "aqi": "60 (ಸಾಧಾರಣ)", "cond": "ಬಿಸಿಲಿನ ತಾಪ", "imd_alert": "🟢 ಶುಷ್ಕ ವಾತಾವರಣ", "imd_color": "#16A34A", "petrol": 111.38, "diesel": 99.25},
    "koppal": {"name_kn": "ಕೊಪ್ಪಳ", "name_en": "Koppal", "region": "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ", "temp": "31°C", "humidity": "51%", "wind": "13 km/h", "uv": "8 (ಬಹಳ ಹೆಚ್ಚು)", "aqi": "48 (ಉತ್ತಮ)", "cond": "ಬಿಸಿಲು", "imd_alert": "🟢 ಸಾಮಾನ್ಯ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 111.08, "diesel": 98.98},
    "ballari": {"name_kn": "ಬಳ್ಳಾರಿ", "name_en": "Ballari", "region": "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ", "temp": "33°C", "humidity": "47%", "wind": "14 km/h", "uv": "8 (ಬಹಳ ಹೆಚ್ಚು)", "aqi": "65 (ಸಾಧಾರಣ)", "cond": "ಬಿಸಿಲು & ಶುಷ್ಕ ಗಾಳಿ", "imd_alert": "🟢 ಶುಷ್ಕ ವಾತಾವರಣ", "imd_color": "#16A34A", "petrol": 111.22, "diesel": 99.10},
    "vijayanagara": {"name_kn": "ವಿಜಯನಗರ", "name_en": "Vijayanagara", "region": "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ", "temp": "32°C", "humidity": "49%", "wind": "13 km/h", "uv": "8 (ಬಹಳ ಹೆಚ್ಚು)", "aqi": "52 (ಉತ್ತಮ)", "cond": "ಸ್ವಚ್ಛ ಬಿಸಿಲು", "imd_alert": "🟢 ಸಾಮಾನ್ಯ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 111.18, "diesel": 99.06},
    "davangere": {"name_kn": "ದಾವಣಗೆರೆ", "name_en": "Davangere", "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", "temp": "29°C", "humidity": "56%", "wind": "14 km/h", "uv": "7 (ಹೆಚ್ಚು)", "aqi": "49 (ಉತ್ತಮ)", "cond": "ಭಾಗಶಃ ಮೋಡ", "imd_alert": "🟢 ಶುಷ್ಕ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 110.92, "diesel": 98.84},
    "chitradurga": {"name_kn": "ಚಿತ್ರದುರ್ಗ", "name_en": "Chitradurga", "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ", "temp": "30°C", "humidity": "52%", "wind": "17 km/h", "uv": "7 (ಹೆಚ್ಚು)", "aqi": "47 (ಉತ್ತಮ)", "cond": "ಗಾಳಿಯುಕ್ತ ಬಿಸಿಲು", "imd_alert": "🟢 ಶುಷ್ಕ ವಾತಾವರಣ", "imd_color": "#16A34A", "petrol": 111.05, "diesel": 98.95}
}

district_files = glob.glob(os.path.join(ROOT_DIR, 'districts', '*.html'))

for dpath in district_files:
    fname = os.path.basename(dpath)
    if fname in ['index.html']:
        continue
    slug = fname.replace('.html', '')
    meta = DISTRICT_META.get(slug, {
        "name_kn": slug.title(), "name_en": slug.title(), "region": "ಕರ್ನಾಟಕ", "temp": "28°C", "humidity": "65%", "wind": "13 km/h", "uv": "6 (ಮಧ್ಯಮ)", "aqi": "50 (ಉತ್ತಮ)", "cond": "ಭಾಗಶಃ ಮೋಡ", "imd_alert": "🟢 ಶುಷ್ಕ ಹವಾಮಾನ", "imd_color": "#16A34A", "petrol": 110.89, "diesel": 98.80
    })

    with open(dpath, 'r', encoding='utf-8') as f:
        html = f.read()

    p_val = f"{meta['petrol']:.2f}"
    d_val = f"{meta['diesel']:.2f}"

    clean_sidebar_box = f"""<aside class="d-sidebar">

    <!-- LIVE PRICES CARD (DYNAMICALLY SYNCED WITH MAIN PAGES) -->
    <div class="d-sec" style="border-left: 4px solid var(--k-crimson);">
      <div class="d-sec-title" style="font-size:16px;"><span>⚡ ಲೈವ್ ಮಾರುಕಟ್ಟೆ &amp; ದರಗಳು (Live Prices)</span></div>
      
      <div style="display:flex; flex-direction:column; gap:10px; margin-bottom:14px;">
        <div style="background:#FFF7ED; border:1px solid #FFEDD5; border-radius:12px; padding:12px 14px; display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-size:12.5px; font-weight:900; color:#EA580C;">🥇 24k / 22k ಚಿನ್ನದ ಬೆಲೆ</div>
            <div style="font-size:11px; color:#9A3412;">ಇಂದಿನ ರಾಜ್ಯದ ಅಧಿಕೃತ ದರ</div>
          </div>
          <div style="text-align:right;">
            <div style="font-size:16px; font-weight:900; color:#EA580C; font-family:var(--font-en);" id="sidebar-gold-val">₹15,829 /g</div>
            <div style="font-size:10.5px; color:#C2410C;" id="sidebar-silver-val">ಬೆಳ್ಳಿ: ₹260.00/g</div>
          </div>
        </div>

        <div style="background:#F0FDF4; border:1px solid #BBF7D0; border-radius:12px; padding:12px 14px; display:flex; justify-content:space-between; align-items:center;">
          <div>
            <div style="font-size:12.5px; font-weight:900; color:#15803D;">⛽ ಪೆಟ್ರೋಲ್ &amp; ಡೀಸೆಲ್ ದರ</div>
            <div style="font-size:11px; color:#166534;">{meta['name_kn']} ಸ್ಥಳೀಯ ಬೆಲೆ</div>
          </div>
          <div style="text-align:right;">
            <div style="font-size:16px; font-weight:900; color:#15803D; font-family:var(--font-en);" id="sidebar-petrol-val">₹{p_val}</div>
            <div style="font-size:10.5px; color:#166534;" id="sidebar-diesel-val">ಡೀಸೆಲ್: ₹{d_val}</div>
          </div>
        </div>
      </div>

      <div style="font-size:13px; font-weight:800; color:var(--k-dark); margin-bottom:8px;">🌾 ಪ್ರಮುಖ APMC ಬೆಳೆಗಳು:</div>
      <div style="font-size:12.5px; color:#475569; line-height:1.6; background:#F8FAFC; padding:10px 12px; border-radius:10px; border:1px solid #E2E8F0;">
        {meta['name_kn']} ಕೃಷಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ನಿತ್ಯವೂ ಪ್ರಮುಖ ಕೃಷಿ ಉತ್ಪನ್ನಗಳ ವಹಿವಾಟು ಅಧಿಕೃತ APMC ದರದಲ್ಲಿ ನಡೆಯುತ್ತದೆ.
      </div>
    </div>"""

    # Replace from `<aside class="d-sidebar">` to `<!-- OTHER 31 DISTRICTS SWITCHER -->`
    html = re.sub(r'<aside class="d-sidebar">[\s\S]*?<!-- OTHER 31 DISTRICTS SWITCHER -->', clean_sidebar_box + '\n\n    <!-- OTHER 31 DISTRICTS SWITCHER -->', html)

    with open(dpath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    nk_dpath = os.path.join(NK_DIR, 'districts', fname)
    if os.path.exists(os.path.dirname(nk_dpath)):
        with open(nk_dpath, 'w', encoding='utf-8') as f:
            f.write(html)

print("SUCCESS_CLEANED_SIDEBAR_ACROSS_ALL_DISTRICTS")
