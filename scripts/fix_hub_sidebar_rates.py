# -*- coding: utf-8 -*-
"""
Karnata — scripts/fix_hub_sidebar_rates.py
Updates the sidebar rates in districts/index.html and districts.html to 2026 rates.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

hub_files = [
    os.path.join(ROOT_DIR, 'districts', 'index.html'),
    os.path.join(ROOT_DIR, 'districts.html'),
    os.path.join(NK_DIR, 'districts', 'index.html'),
    os.path.join(NK_DIR, 'districts.html')
]

for hpath in hub_files:
    if not os.path.exists(hpath): continue
    with open(hpath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update gold rate
    html = re.sub(r'id="hub-gold-val">[^<]+</div>', 'id="hub-gold-val">₹16,304 / ಗ್ರಾಂ</div>', html)
    html = re.sub(r'ಬೆಳ್ಳಿ:\s*₹?92\.50/g', 'ಬೆಳ್ಳಿ: ₹260.00 / ಗ್ರಾಂ', html)
    html = re.sub(r'ಬೆಳ್ಳಿ:\s*₹?220\.00/g', 'ಬೆಳ್ಳಿ: ₹260.00 / ಗ್ರಾಂ', html)
    html = re.sub(r'ಬೆಳ್ಳಿ:\s*₹?232\.50/g', 'ಬೆಳ್ಳಿ: ₹260.00 / ಗ್ರಾಂ', html)
    
    # Update fuel rate
    html = re.sub(r'₹110\.89', '₹102.86', html)
    html = re.sub(r'ಡೀಸೆಲ್:\s*₹?98\.80', 'ಡೀಸೆಲ್: ₹88.94', html)

    with open(hpath, 'w', encoding='utf-8') as f:
        f.write(html)

print("SUCCESS_FIXED_HUB_SIDEBAR_RATES")
