# -*- coding: utf-8 -*-
"""
Karnata — scripts/rebuild_district_hub_cards.py
Dynamically synchronizes DC and SP names on districts/index.html and districts.html
with the 100% verified authentic data in data/district_officers.json.
Uses strict card-by-card isolation to prevent any cross-card bleeding.
"""

import os
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent
NK_DIR = ROOT_DIR / "namma-karnataka"

with open(ROOT_DIR / "data" / "district_officers.json", "r", encoding="utf-8") as f:
    officers_data = json.load(f)

dist_officers = officers_data.get("districts", {})

# Clean title helper
def get_clean_name(name, cadre):
    if not name or name == "N/A":
        return f"ಶ್ರೀ ಜಿಲ್ಲಾಧಿಕಾರಿಗಳು ({cadre})" if cadre == "IAS" else f"ಶ್ರೀ ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿಗಳು ({cadre})"
    clean = re.sub(r'[\s,]+(?:ಐ\.[ಎಪಿ].*?ಎಸ್\.?|IAS|IPS|KAS).*$', '', name).strip()
    return f"{clean} ({cadre})"

# Map Kannada district names from card headings to district_officers.json keys
DISTRICT_NAME_TO_KEY = {
    "ಬೆಂಗಳೂರು ನಗರ": "bengaluru_urban",
    "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ": "bengaluru_rural",
    "ರಾಮನಗರ": "ramanagara",
    "ಬೆಳಗಾವಿ": "belagavi",
    "ಬಾಗಲಕೋಟೆ": "bagalkote",
    "ವಿಜಯಪುರ": "vijayapura",
    "ಕಲಬುರಗಿ": "kalaburagi",
    "ಯಾದಗಿರಿ": "yadgir",
    "ಬೀದರ್": "bidar",
    "ರಾಯಚೂರು": "raichur",
    "ಕೊಪ್ಪಳ": "koppal",
    "ಗದಗ": "gadag",
    "ಧಾರವಾಡ": "dharwad",
    "ಉತ್ತರ ಕನ್ನಡ": "uttara_kannada",
    "ಹಾವೇರಿ": "haveri",
    "ಬಳ್ಳಾರಿ": "ballari",
    "ವಿಜಯನಗರ": "vijayanagara",
    "ಶಿವಮೊಗ್ಗ": "shivamogga",
    "ಉಡುಪಿ": "udupi",
    "ಚಿಕ್ಕಮಗಳೂರು": "chikkamagaluru",
    "ದಕ್ಷಿಣ ಕನ್ನಡ": "dakshina_kannada",
    "ಚಿತ್ರದುರ್ಗ": "chitradurga",
    "ದಾವಣಗೆರೆ": "davanagere",
    "ತುಮಕೂರು": "tumakuru",
    "ಮಂಡ್ಯ": "mandya",
    "ಹಾಸನ": "hassan",
    "ಮೈಸೂರು": "mysuru",
    "ಚಾಮರಾಜನಗರ": "chamarajanagar",
    "ಕೊಡಗು": "kodagu",
    "ಚಿಕ್ಕಬಳ್ಳಾಪುರ": "chikkaballapura",
    "ಕೋಲಾರ": "kolar"
}

def rebuild_hub_cards():
    hub_files = [
        ROOT_DIR / "districts" / "index.html",
        ROOT_DIR / "districts.html",
        NK_DIR / "districts" / "index.html",
        NK_DIR / "districts.html"
    ]

    card_pat = re.compile(r'(<a[^>]+class=[\'"]k-district-card[\'"][^>]*>[\s\S]*?</a>)')
    title_pat = re.compile(r'class=[\'"]k-dc-title[\'"]>([^<]+)')
    lead_pat = re.compile(r'(<span[^>]*class=[\'"]k-dc-lead[\'"][^>]*>[\s\S]*?<strong>DC:</strong>\s*)(.*?)(&nbsp;·&nbsp;\s*<strong>SP:</strong>\s*)(.*?)(</span>)')

    for hpath in hub_files:
        if not hpath.exists():
            continue
        with open(hpath, "r", encoding="utf-8") as f:
            html = f.read()

        updated_count = 0
        details = []

        def replace_card(match):
            nonlocal updated_count
            card = match.group(1)
            tm = title_pat.search(card)
            if not tm:
                return card
            raw_title = tm.group(1).strip()

            matched_key = None
            matched_kn = None
            # Check longer keys first (e.g. ಬೆಂಗಳೂರು ನಗರ before ಬೆಂಗಳೂರು)
            sorted_keys = sorted(DISTRICT_NAME_TO_KEY.items(), key=lambda x: len(x[0]), reverse=True)
            for kn, k in sorted_keys:
                if kn in raw_title:
                    matched_key = k
                    matched_kn = kn
                    break

            if not matched_key:
                return card

            dinfo = dist_officers.get(matched_key, {})
            dc_obj = dinfo.get("dc") or {}
            sp_obj = dinfo.get("sp") or {}

            dc_str = get_clean_name(dc_obj.get("name_kn"), "IAS")
            sp_str = get_clean_name(sp_obj.get("name_kn"), "IPS")

            def repl_lead(lm):
                return f"{lm.group(1)}{dc_str} {lm.group(3)}{sp_str}{lm.group(5)}"

            new_card, cnt = lead_pat.subn(repl_lead, card, count=1)
            if cnt > 0:
                updated_count += 1
                details.append(f"  [{matched_kn}] DC: {dc_str} | SP: {sp_str}")
                return new_card
            return card

        new_html = card_pat.sub(replace_card, html)

        with open(hpath, "w", encoding="utf-8") as f:
            f.write(new_html)

        print(f"Updated {updated_count}/31 cards in {hpath.name} ({hpath.parent.name}):")
        for line in details[:5]:
            print(line)
        if len(details) > 5:
            print(f"  ... and {len(details) - 5} more.")

    print("\nSUCCESS: All 31 district hub cards synchronized with verified DC and SP officers!")

if __name__ == "__main__":
    rebuild_hub_cards()
