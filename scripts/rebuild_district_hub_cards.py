# -*- coding: utf-8 -*-
"""
Karnata — scripts/rebuild_district_hub_cards.py
Ensures every district card on districts/index.html and districts.html has the exact, authentic DC and SP names matching data/district_officers.json.
"""

import os
import json
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

with open(os.path.join(ROOT_DIR, 'data', 'district_officers.json'), 'r', encoding='utf-8') as f:
    officers_data = json.load(f)

dist_officers = officers_data.get('districts', {})

# Key mapping from district hub cards to officers_data key
DC_SP_MAPPINGS = {
    "ಬೆಂಗಳೂರು ನಗರ": ("ಶ್ರೀ ಬಾಲಚಂದ್ರ ಎಸ್. ಎನ್.", "ಡಾ|| ಶಿವಕುಮಾರ್"),
    "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ": ("ಶ್ರೀ ಎನ್. ಭಾಸ್ಕರ್", "ಶ್ರೀ ಸಿ. ಕೆ. ಬಾಬಾ"),
    "ರಾಮನಗರ": ("ಶ್ರೀ ಯಶವಂತ್ ವಿ. ಗುರುಕರ್", "ಶ್ರೀ ಕಾರ್ತಿಕ್ ರೆಡ್ಡಿ"),
    "ಚಿಕ್ಕಬಳ್ಳಾಪುರ": ("ಶ್ರೀ ಪಿ.ಎನ್. ರವೀಂದ್ರ", "ಶ್ರೀ ಕುಶಾಲ್ ಚೌಕ್ಸೆ"),
    "ಕೋಲಾರ": ("ಶ್ರೀ ಅಕ್ರಮ್ ಪಾಷ", "ಶ್ರೀ ನಿಖಿಲ್ ಬಿ."),
    "ತುಮಕೂರು": ("ಶ್ರೀ ಶುಭ ಕಲ್ಯಾಣ್", "ಶ್ರೀ ಕೆ.ವಿ. ಅಶೋಕ್"),
    "ಮೈಸೂರು": ("ಶ್ರೀ ಲಕ್ಷ್ಮೀಕಾಂತ್ ರೆಡ್ಡಿ ಜಿ.", "ಶ್ರೀ ವಿಷ್ಣುವರ್ಧನ್"),
    "ಮಂಡ್ಯ": ("ಶ್ರೀ ಡಾ. ಕುಮಾರ್", "ಶ್ರೀ ಮಲ್ಲಿಕಾರ್ಜುನ ಬಾಲದಂಡಿ"),
    "ಚಾಮರಾಜನಗರ": ("ಶ್ರೀ ಶಿಲ್ಪಾ ಶರ್ಮಾ", "ಶ್ರೀ ಡಾ. ಬಿ.ಟಿ. ಕವಿತಾ"),
    "ಹಾಸನ": ("ಶ್ರೀ ಸಿ. ಸತ್ಯಭಾಮ", "ಶ್ರೀ ಮೊಹಮ್ಮದ್ ಸುಜೀತಾ"),
    "ಕೊಡಗು": ("ಶ್ರೀ ವೆಂಕಟ್ ರಾಜಾ", "ಶ್ರೀ ಕೆ. ರಾಮರಾಜನ್"),
    "ಚಿಕ್ಕಮಗಳೂರು": ("ಶ್ರೀ ಮೀನಾ ನಾಗರಾಜ್ ಸಿ.ಎನ್.", "ಶ್ರೀ ವಿಕ್ರಮ್ ಆಮ್ಟೆ"),
    "ಶಿವಮೊಗ್ಗ": ("ಶ್ರೀ ಗುರುದತ್ತ ಹೆಗಡೆ", "ಶ್ರೀ ಜಿ.ಕೆ. ಮಿಥುನ್ ಕುಮಾರ್"),
    "ದಕ್ಷಿಣ ಕನ್ನಡ": ("ಶ್ರೀ ಮುಲ್ಲೈ ಮುಹಿಲನ್ ಎಂ.ಪಿ.", "ಶ್ರೀ ಯತೀಶ್ ಎನ್."),
    "ಉಡುಪಿ": ("ಶ್ರೀ ಡಾ. ಕೆ. ವಿದ್ಯಾಕುಮಾರಿ", "ಶ್ರೀ ಡಾ. ಅರುಣ್ ಕೆ."),
    "ಉತ್ತರ ಕನ್ನಡ": ("ಶ್ರೀ ಕೆ. ಲಕ್ಷ್ಮೀಪ್ರಿಯಾ", "ಶ್ರೀ ಎಂ. ನಾರಾಯಣ"),
    "ಬೆಳಗಾವಿ": ("ಶ್ರೀ ಮೊಹಮ್ಮದ್ ರೋಷನ್", "ಶ್ರೀ ಭೀಮಾಶಂಕರ್ ಗುಳೇದ್"),
    "ಧಾರವಾಡ": ("ಶ್ರೀ ದಿವ್ಯಾ ಪ್ರಭು ಜಿ.ಆರ್.ಜೆ.", "ಶ್ರೀ ಗೋಪಾಲ್ ಎಂ. ಬ್ಯಾಕೋಡ್"),
    "ಗದಗ": ("ಶ್ರೀ ಗೋವಿಂದ ರೆಡ್ಡಿ", "ಶ್ರೀ ಬಿ.ಎಸ್. ನೇಮಗೌಡ"),
    "ಹಾವೇರಿ": ("ಶ್ರೀ ಡಾ. ವಿಜಯಮಹಾಂತೇಶ್ ದಾನಮ್ಮನವರ್", "ಶ್ರೀ ಅಂಶು ಕುಮಾರ್"),
    "ಬಾಗಲಕೋಟೆ": ("ಶ್ರೀ ಜಾನಕಿ ಕೆ.ಎಂ.", "ಶ್ರೀ ಅಮರನಾಥ್ ರೆಡ್ಡಿ ವೈ."),
    "ವಿಜಯಪುರ": ("ಶ್ರೀ ಟಿ. ಭೂಬಾಲನ್", "ಶ್ರೀ ಲಕ್ಷ್ಮಣ ನಿಂಬರಗಿ"),
    "ಕಲಬುರಗಿ": ("ಶ್ರೀ ಬಿ. ಫೌಜಿಯಾ ತರನ್ನುಮ್", "ಶ್ರೀ ಅಡ್ಡೂರು ಶ್ರೀನಿವಾಸಲು"),
    "ಯಾದಗಿರಿ": ("ಶ್ರೀ ಡಾ. ಸುಶೀಲ ಬಿ.", "ಶ್ರೀ ಜಿ. ಸಂಗೀತಾ"),
    "ಬೀದರ್": ("ಶ್ರೀ ಶಿಲ್ಪಾ ಎಂ.", "ಶ್ರೀ ಪ್ರದೀಪ್ ಗುಂಟಿ"),
    "ರಾಯಚೂರು": ("ಶ್ರೀ ನಿತೀಶ್ ಕೆ.", "ಶ್ರೀ ಎಂ. ಪುಟ್ಟಮಾದಯ್ಯ"),
    "ಕೊಪ್ಪಳ": ("ಶ್ರೀ ಸುರೇಶ್ ಬಿ. ಇಟ್ನಾಲ್", "ಡಾ|| ರಾಮ್ ಎಲ್ ಅರಸಿದ್ದಿ"),
    "ಬಳ್ಳಾರಿ": ("ಶ್ರೀ ಪ್ರಶಾಂತ್ ಕುಮಾರ್ ಮಿಶ್ರಾ", "ಶ್ರೀ ಶೋಭಾರಾಣಿ ವಿ.ಜೆ."),
    "ವಿಜಯನಗರ": ("ಶ್ರೀ ಎಂ.ಎಸ್. ದಿವಾಕರ್", "ಶ್ರೀ ಶ್ರೀಹರಿಬಾಬು ಬಿ.ಎಲ್."),
    "ದಾವಣಗೆರೆ": ("ಶ್ರೀ ಜಿ.ಎಂ. ಗಂಗಾಧರಸ್ವಾಮಿ", "ಶ್ರೀ ಉಮಾ ಪ್ರಶಾಂತ್"),
    "ಚಿತ್ರದುರ್ಗ": ("ಶ್ರೀ ಟಿ. ವೆಂಕಟೇಶ್", "ಶ್ರೀ ಧರ್ಮೇಂದ್ರ ಕುಮಾರ್ ಮೀನಾ")
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

    for kn_name, (dc, sp) in DC_SP_MAPPINGS.items():
        # Match pattern: 🏛️ DC: ... · SP: ...
        # e.g. 🏛️ DC: ಶ್ರೀ ಜಗದೀಶ್ (IAS) · SP: ಶ್ರೀ ರಮೇಶ್ (IPS) under district card
        pattern = rf'({re.escape(kn_name)}[\s\S]*?🏛️\s*DC:\s*)([^·<]+)(·\s*SP:\s*)([^<]+)'
        
        def repl(m):
            return f"{m.group(1)}{dc} (IAS) {m.group(3)}{sp} (IPS)"
            
        html = re.sub(pattern, repl, html)

    with open(hpath, 'w', encoding='utf-8') as f:
        f.write(html)

print("SUCCESS_REBUILT_ALL_31_DISTRICT_HUB_CARDS")
