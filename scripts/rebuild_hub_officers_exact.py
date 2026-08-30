# -*- coding: utf-8 -*-
"""
Karnata — scripts/rebuild_hub_officers_exact.py
Updates the exact DC and SP names on districts/index.html and districts.html.
"""

import os
import json
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

DC_SP_EXACT = {
    "bengaluru-urban": ("ಶ್ರೀ ಬಾಲಚಂದ್ರ ಎಸ್. ಎನ್.", "ಡಾ|| ಶಿವಕುಮಾರ್"),
    "bengaluru-rural": ("ಶ್ರೀ ಎನ್. ಭಾಸ್ಕರ್", "ಶ್ರೀ ಸಿ. ಕೆ. ಬಾಬಾ"),
    "ramanagara": ("ಶ್ರೀ ಯಶವಂತ್ ವಿ. ಗುರುಕರ್", "ಶ್ರೀ ಕಾರ್ತಿಕ್ ರೆಡ್ಡಿ"),
    "chikkaballapura": ("ಶ್ರೀ ಪಿ.ಎನ್. ರವೀಂದ್ರ", "ಶ್ರೀ ಕುಶಾಲ್ ಚೌಕ್ಸೆ"),
    "kolar": ("ಶ್ರೀ ಅಕ್ರಮ್ ಪಾಷ", "ಶ್ರೀ ನಿಖಿಲ್ ಬಿ."),
    "tumakuru": ("ಶ್ರೀ ಶುಭ ಕಲ್ಯಾಣ್", "ಶ್ರೀ ಕೆ.ವಿ. ಅಶೋಕ್"),
    "mysuru": ("ಶ್ರೀ ಲಕ್ಷ್ಮೀಕಾಂತ್ ರೆಡ್ಡಿ ಜಿ.", "ಶ್ರೀ ವಿಷ್ಣುವರ್ಧನ್"),
    "mandya": ("ಶ್ರೀ ಡಾ. ಕುಮಾರ್", "ಶ್ರೀ ಮಲ್ಲಿಕಾರ್ಜುನ ಬಾಲದಂಡಿ"),
    "chamarajanagara": ("ಶ್ರೀ ಶಿಲ್ಪಾ ಶರ್ಮಾ", "ಶ್ರೀ ಡಾ. ಬಿ.ಟಿ. ಕವಿತಾ"),
    "hassan": ("ಶ್ರೀ ಸಿ. ಸತ್ಯಭಾಮ", "ಶ್ರೀ ಮೊಹಮ್ಮದ್ ಸುಜೀತಾ"),
    "kodagu": ("ಶ್ರೀ ವೆಂಕಟ್ ರಾಜಾ", "ಶ್ರೀ ಕೆ. ರಾಮರಾಜನ್"),
    "chikkamagaluru": ("ಶ್ರೀ ಮೀನಾ ನಾಗರಾಜ್ ಸಿ.ಎನ್.", "ಶ್ರೀ ವಿಕ್ರಮ್ ಆಮ್ಟೆ"),
    "shivamogga": ("ಶ್ರೀ ಗುರುದತ್ತ ಹೆಗಡೆ", "ಶ್ರೀ ಜಿ.ಕೆ. ಮಿಥುನ್ ಕುಮಾರ್"),
    "dakshina-kannada": ("ಶ್ರೀ ಮುಲ್ಲೈ ಮುಹಿಲನ್ ಎಂ.ಪಿ.", "ಶ್ರೀ ಯತೀಶ್ ಎನ್."),
    "udupi": ("ಶ್ರೀ ಡಾ. ಕೆ. ವಿದ್ಯಾಕುಮಾರಿ", "ಶ್ರೀ ಡಾ. ಅರುಣ್ ಕೆ."),
    "uttara-kannada": ("ಶ್ರೀ ಕೆ. ಲಕ್ಷ್ಮೀಪ್ರಿಯಾ", "ಶ್ರೀ ಎಂ. ನಾರಾಯಣ"),
    "belagavi": ("ಶ್ರೀ ಮೊಹಮ್ಮದ್ ರೋಷನ್", "ಶ್ರೀ ಭೀಮಾಶಂಕರ್ ಗುಳೇದ್"),
    "dharwad": ("ಶ್ರೀ ದಿವ್ಯಾ ಪ್ರಭು ಜಿ.ಆರ್.ಜೆ.", "ಶ್ರೀ ಗೋಪಾಲ್ ಎಂ. ಬ್ಯಾಕೋಡ್"),
    "gadag": ("ಶ್ರೀ ಗೋವಿಂದ ರೆಡ್ಡಿ", "ಶ್ರೀ ಬಿ.ಎಸ್. ನೇಮಗೌಡ"),
    "haveri": ("ಶ್ರೀ ಡಾ. ವಿಜಯಮಹಾಂತೇಶ್ ದಾನಮ್ಮನವರ್", "ಶ್ರೀ ಅಂಶು ಕುಮಾರ್"),
    "bagalkote": ("ಶ್ರೀ ಜಾನಕಿ ಕೆ.ಎಂ.", "ಶ್ರೀ ಅಮರನಾಥ್ ರೆಡ್ಡಿ ವೈ."),
    "vijayapura": ("ಶ್ರೀ ಟಿ. ಭೂಬಾಲನ್", "ಶ್ರೀ ಲಕ್ಷ್ಮಣ ನಿಂಬರಗಿ"),
    "kalaburagi": ("ಶ್ರೀ ಬಿ. ಫೌಜಿಯಾ ತರನ್ನುಮ್", "ಶ್ರೀ ಅಡ್ಡೂರು ಶ್ರೀನಿವಾಸಲು"),
    "yadgir": ("ಶ್ರೀ ಡಾ. ಸುಶೀಲ ಬಿ.", "ಶ್ರೀ ಜಿ. ಸಂಗೀತಾ"),
    "bidar": ("ಶ್ರೀ ಶಿಲ್ಪಾ ಎಂ.", "ಶ್ರೀ ಪ್ರದೀಪ್ ಗುಂಟಿ"),
    "raichur": ("ಶ್ರೀ ನಿತೀಶ್ ಕೆ.", "ಶ್ರೀ ಎಂ. ಪುಟ್ಟಮಾದಯ್ಯ"),
    "koppal": ("ಶ್ರೀ ಸುರೇಶ್ ಬಿ. ಇಟ್ನಾಲ್", "ಡಾ|| ರಾಮ್ ಎಲ್ ಅರಸಿದ್ದಿ"),
    "ballari": ("ಶ್ರೀ ಪ್ರಶಾಂತ್ ಕುಮಾರ್ ಮಿಶ್ರಾ", "ಶ್ರೀ ಶೋಭಾರಾಣಿ ವಿ.ಜೆ."),
    "vijayanagara": ("ಶ್ರೀ ಎಂ.ಎಸ್. ದಿವಾಕರ್", "ಶ್ರೀ ಶ್ರೀಹರಿಬಾಬು ಬಿ.ಎಲ್."),
    "davangere": ("ಶ್ರೀ ಜಿ.ಎಂ. ಗಂಗಾಧರಸ್ವಾಮಿ", "ಶ್ರೀ ಉಮಾ ಪ್ರಶಾಂತ್"),
    "chitradurga": ("ಶ್ರೀ ಟಿ. ವೆಂಕಟೇಶ್", "ಶ್ರೀ ಧರ್ಮೇಂದ್ರ ಕುಮಾರ್ ಮೀನಾ")
}

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

    # Update sidebar 2026 rates
    html = re.sub(r'₹14,505\s*/g', '₹16,304 /g', html)
    html = re.sub(r'₹14,080\s*/g', '₹16,304 /g', html)
    html = re.sub(r'ಬೆಳ್ಳಿ:\s*₹220\.00/g', 'ಬೆಳ್ಳಿ: ₹260.00/g', html)
    html = re.sub(r'ಬೆಳ್ಳಿ:\s*₹220/g', 'ಬೆಳ್ಳಿ: ₹260/g', html)
    html = re.sub(r'₹110\.89', '₹102.86', html)

    for slug, (dc, sp) in DC_SP_EXACT.items():
        # Match the card for this slug
        card_pattern = rf'(<a href="/districts/{slug}\.html"[\s\S]*?<div>🏛️ <strong>DC:</strong>\s*)([^&<]+)(&nbsp;·&nbsp;[\s\S]*?<strong>SP:</strong>\s*)([^<]+)(</div>)'
        
        def make_repl(d_name, s_name):
            def repl(m):
                return f"{m.group(1)}{d_name} (IAS) {m.group(3)}{s_name} (IPS){m.group(5)}"
            return repl

        html = re.sub(card_pattern, make_repl(dc, sp), html)

    with open(hpath, 'w', encoding='utf-8') as f:
        f.write(html)

print("SUCCESS_REBUILT_HUB_OFFICERS_EXACT")
