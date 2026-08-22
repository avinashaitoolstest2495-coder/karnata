#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
KARNATAKA TAHSILDARS DIRECTORY SCRAPER (240+ TALUKS)
Source: https://ceg.karnataka.gov.in/aadhaar/public/page/Contact+Us/Contact+details+of+Tahsildars/kn
Centre for e-Governance (CeG), Government of Karnataka
=============================================================================
"""

import os
import sys
import json
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import urllib3
urllib3.disable_warnings()

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

CEG_URL = "https://ceg.karnataka.gov.in/aadhaar/public/page/Contact+Us/Contact+details+of+Tahsildars/kn"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

DISTRICT_MAP = {
    "ಬಾಗಲಕೋಟೆ": "bagalkote",
    "ಬೆಂಗಳೂರು ನಗರ": "bengaluru_urban",
    "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ": "bengaluru_rural",
    "ಬೆಳಗಾವಿ": "belagavi",
    "ಬಳ್ಳಾರಿ": "ballari",
    "ಬೀದರ್": "bidar",
    "ವಿಜಯಪುರ": "vijayapura",
    "ಚಾಮರಾಜನಗರ": "chamarajanagar",
    "ಚಿಕ್ಕಬಳ್ಳಾಪುರ": "chikkaballapura",
    "ಚಿಕ್ಕಮಗಳೂರು": "chikkamagaluru",
    "ಚಿತ್ರದುರ್ಗ": "chitradurga",
    "ದಕ್ಷಿಣ ಕನ್ನಡ": "dakshina_kannada",
    "ದಾವಣಗೆರೆ": "davanagere",
    "ಧಾರವಾಡ": "dharwad",
    "ಗದಗ": "gadag",
    "ಹಾಸನ": "hassan",
    "ಹಾವೇರಿ": "haveri",
    "ಕಲಬುರಗಿ": "kalaburagi",
    "ಗುಲ್ಬರ್ಗ": "kalaburagi",
    "ಕೊಡಗು": "kodagu",
    "ಕೋಲಾರ": "kolar",
    "ಕೊಪ್ಪಳ": "koppal",
    "ಮಂಡ್ಯ": "mandya",
    "ಮೈಸೂರು": "mysuru",
    "ರಾಯಚೂರು": "raichur",
    "ರಾಮನಗರ": "ramanagara",
    "ಶಿವಮೊಗ್ಗ": "shivamogga",
    "ತುಮಕೂರು": "tumakuru",
    "ಉಡುಪಿ": "udupi",
    "ಉತ್ತರ ಕನ್ನಡ": "uttara_kannada",
    "ಯಾದಗಿರಿ": "yadgir",
    "ವಿಜಯನಗರ": "vijayanagara"
}

def clean_txt(s):
    if not s:
        return ""
    return re.sub(r'\s+', ' ', str(s)).strip()

def scrape_tahsildars():
    print("🌾 Live Scraping All Karnataka Taluk Tahsildars from CEG Portal...")
    try:
        r = requests.get(CEG_URL, headers=HEADERS, verify=False, timeout=15)
        if r.status_code != 200:
            print(f"❌ Failed to fetch CEG page (Status: {r.status_code})")
            return []
        
        soup = BeautifulSoup(r.text, 'html.parser')
        tables = soup.find_all('table')
        if not tables:
            print("❌ No tables found on CEG page.")
            return []

        table = tables[0]
        rows = table.find_all('tr')
        print(f"✅ Found {len(rows)} table rows on CEG portal")

        tahsildars_list = []
        current_district_kn = ""
        current_district_key = "bagalkote"

        for row in rows:
            cells = [clean_txt(td.get_text()) for td in row.find_all(['td', 'th'])]
            if not cells or len(cells) < 4:
                continue
            
            # Header check
            if any('ತಾಲ್ಲೂಕು' in c or 'ತಹಶೀಲ್ದಾರ್' in c for c in cells):
                continue
            
            # Check row structure (Some rows have 7 cells with district, some have 5-6 without district repeating)
            if len(cells) == 7 and not cells[0].isdigit():
                # 0: District, 1: Taluk, 2: Name, 3: Mobile, 4: Phone, 5: Email
                current_district_kn = cells[0]
                taluk = cells[1]
                name = cells[2]
                mobile = cells[3]
                phone = cells[4]
                email = cells[5]
            elif len(cells) == 7 and cells[0].isdigit():
                # 0: SlNo, 1: District, 2: Taluk, 3: Name, 4: Mobile, 5: Phone, 6: Email
                current_district_kn = cells[1]
                taluk = cells[2]
                name = cells[3]
                mobile = cells[4]
                phone = cells[5]
                email = cells[6]
            elif len(cells) == 6 and not cells[0].isdigit():
                taluk = cells[0]
                name = cells[1]
                mobile = cells[2]
                phone = cells[3]
                email = cells[4]
            elif len(cells) == 5:
                taluk = cells[0]
                name = cells[1]
                mobile = cells[2]
                phone = cells[3]
                email = cells[4]
            elif len(cells) == 4:
                taluk = cells[0]
                name = cells[1]
                mobile = cells[2]
                phone = ""
                email = cells[3]
            else:
                continue

            # Update district key
            for d_kn, d_key in DISTRICT_MAP.items():
                if d_kn in current_district_kn:
                    current_district_key = d_key
                    break

            if taluk and name and len(name) > 2 and not name.isdigit():
                tahsildar_obj = {
                    "id": f"TAH-{current_district_key}-{clean_txt(taluk)}",
                    "district_kn": current_district_kn or "ಕರ್ನಾಟಕ",
                    "district_key": current_district_key,
                    "taluk_kn": taluk,
                    "name_kn": name,
                    "designation": f"ತಹಶೀಲ್ದಾರ್, {taluk} ತಾಲೂಕು",
                    "mobile": mobile,
                    "phone": phone,
                    "email": email,
                    "cadre": "KAS",
                    "cadre_badge": "📜 KAS",
                    "source": "CEG Karnataka"
                }
                tahsildars_list.append(tahsildar_obj)

        print(f"✅ Extracted {len(tahsildars_list)} Real Taluk Tahsildars!")

        # Save to data/tahsildars.json
        out_path = os.path.join(DATA_DIR, "tahsildars.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump({
                "updated_at": datetime.now().isoformat(),
                "source": "https://ceg.karnataka.gov.in (Centre for e-Governance)",
                "total_tahsildars": len(tahsildars_list),
                "tahsildars": tahsildars_list
            }, f, ensure_ascii=False, indent=2)
        print(f"✅ Saved to {out_path}")

        return tahsildars_list
    except Exception as e:
        print(f"❌ Error scraping CEG Tahsildars: {e}")
        return []

if __name__ == "__main__":
    scrape_tahsildars()
