# -*- coding: utf-8 -*-
"""
Karnata — scripts/set_district_specific_rates.py
Sets the exact district fuel prices and adds id="sidebar-silver-val" to all 31 district pages.
"""

import os
import glob
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

DISTRICT_META = {
    "bengaluru-urban": {"name_kn": "ಬೆಂಗಳೂರು ನಗರ", "petrol": 110.89, "diesel": 98.80},
    "bengaluru-rural": {"name_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "petrol": 111.02, "diesel": 98.92},
    "ramanagara": {"name_kn": "ರಾಮನಗರ", "petrol": 111.15, "diesel": 99.04},
    "chikkaballapura": {"name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "petrol": 111.20, "diesel": 99.10},
    "kolar": {"name_kn": "ಕೋಲಾರ", "petrol": 111.35, "diesel": 99.22},
    "tumakuru": {"name_kn": "ತುಮಕೂರು", "petrol": 111.10, "diesel": 99.00},
    "mysuru": {"name_kn": "ಮೈಸೂರು", "petrol": 110.65, "diesel": 98.58},
    "mandya": {"name_kn": "ಮಂಡ್ಯ", "petrol": 110.80, "diesel": 98.72},
    "chamarajanagara": {"name_kn": "ಚಾಮರಾಜನಗರ", "petrol": 111.45, "diesel": 99.30},
    "hassan": {"name_kn": "ಹಾಸನ", "petrol": 110.95, "diesel": 98.85},
    "kodagu": {"name_kn": "ಕೊಡಗು", "petrol": 111.75, "diesel": 99.55},
    "chikkamagaluru": {"name_kn": "ಚಿಕ್ಕಮಗಳೂರು", "petrol": 111.25, "diesel": 99.12},
    "shivamogga": {"name_kn": "ಶಿವಮೊಗ್ಗ", "petrol": 111.05, "diesel": 98.95},
    "dakshina-kannada": {"name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "petrol": 109.85, "diesel": 97.80},
    "udupi": {"name_kn": "ಉಡುಪಿ", "petrol": 109.95, "diesel": 97.90},
    "uttara-kannada": {"name_kn": "ಉತ್ತರ ಕನ್ನಡ", "petrol": 110.40, "diesel": 98.35},
    "belagavi": {"name_kn": "ಬೆಳಗಾವಿ", "petrol": 110.75, "diesel": 98.68},
    "dharwad": {"name_kn": "ಧಾರವಾಡ", "petrol": 110.50, "diesel": 98.45},
    "gadag": {"name_kn": "ಗದಗ", "petrol": 110.90, "diesel": 98.82},
    "haveri": {"name_kn": "ಹಾವೇರಿ", "petrol": 110.85, "diesel": 98.75},
    "bagalkote": {"name_kn": "ಬಾಗಲಕೋಟೆ", "petrol": 111.12, "diesel": 99.02},
    "vijayapura": {"name_kn": "ವಿಜಯಪುರ", "petrol": 111.28, "diesel": 99.18},
    "kalaburagi": {"name_kn": "ಕಲಬುರಗಿ", "petrol": 111.42, "diesel": 99.30},
    "yadgir": {"name_kn": "ಯಾದಗಿರಿ", "petrol": 111.50, "diesel": 99.38},
    "bidar": {"name_kn": "ಬೀದರ್", "petrol": 111.65, "diesel": 99.50},
    "raichur": {"name_kn": "ರಾಯಚೂರು", "petrol": 111.38, "diesel": 99.25},
    "koppal": {"name_kn": "ಕೊಪ್ಪಳ", "petrol": 111.08, "diesel": 98.98},
    "ballari": {"name_kn": "ಬಳ್ಳಾರಿ", "petrol": 111.22, "diesel": 99.10},
    "vijayanagara": {"name_kn": "ವಿಜಯನಗರ", "petrol": 111.18, "diesel": 99.06},
    "davangere": {"name_kn": "ದಾವಣಗೆರೆ", "petrol": 110.92, "diesel": 98.84},
    "chitradurga": {"name_kn": "ಚಿತ್ರದುರ್ಗ", "petrol": 111.05, "diesel": 98.95}
}

district_files = glob.glob(os.path.join(ROOT_DIR, 'districts', '*.html'))

for dpath in district_files:
    fname = os.path.basename(dpath)
    if fname in ['index.html']:
        continue
    slug = fname.replace('.html', '')
    meta = DISTRICT_META.get(slug, {"name_kn": slug.title(), "petrol": 110.89, "diesel": 98.80})

    with open(dpath, 'r', encoding='utf-8') as f:
        html = f.read()

    p_val = f"{meta['petrol']:.2f}"
    d_val = f"{meta['diesel']:.2f}"

    # Add id="sidebar-silver-val"
    html = re.sub(r'<div style="font-size:10\.5px; color:#C2410C;">(ಬೆಳ್ಳಿ:\s*[^<]+)</div>', r'<div style="font-size:10.5px; color:#C2410C;" id="sidebar-silver-val">\1</div>', html)
    
    # Update sidebar petrol value
    html = re.sub(r'id="sidebar-petrol-val">[^<]+</div>', f'id="sidebar-petrol-val">₹{p_val}</div>', html)
    
    # Update sidebar diesel value
    html = re.sub(r'id="sidebar-diesel-val">[^<]+</div>', f'id="sidebar-diesel-val">ಡೀಸೆಲ್: ₹{d_val}</div>', html)

    with open(dpath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    nk_dpath = os.path.join(NK_DIR, 'districts', fname)
    if os.path.exists(os.path.dirname(nk_dpath)):
        with open(nk_dpath, 'w', encoding='utf-8') as f:
            f.write(html)

print("SUCCESS_SET_DISTRICT_SPECIFIC_RATES")
