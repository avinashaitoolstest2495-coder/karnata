# -*- coding: utf-8 -*-
"""
Karnata — scripts/rebuild_sidebar_cards_properly.py
Properly replaces the Live Prices Card in all 31 district pages with dynamic IDs and district-specific rates.
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

    # Target the entire Live Prices Card inside sidebar
    pattern = r'<div class="d-sec" style="border-left:\s*4px solid var\(--k-crimson\);">[\s\S]*?</div>\s*</div>\s*</div>'
    
    clean_card = f"""<div class="d-sec" style="border-left: 4px solid var(--k-crimson);">
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

    # Check if pattern matches, else fallback to search & replace
    if re.search(r'id="sidebar-gold-val"', html):
        html = re.sub(r'<div class="d-sec" style="border-left:\s*4px solid var\(--k-crimson\);">[\s\S]*?</div>\s*</div>\s*(?=\s*<!-- OTHER 31 DISTRICTS SWITCHER -->|<div class="d-sec">)', clean_card + '\n\n    ', html)
    
    with open(dpath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    nk_dpath = os.path.join(NK_DIR, 'districts', fname)
    if os.path.exists(os.path.dirname(nk_dpath)):
        with open(nk_dpath, 'w', encoding='utf-8') as f:
            f.write(html)

print("SUCCESS_REBUILT_SIDEBAR_CARDS_PROPERLY")
