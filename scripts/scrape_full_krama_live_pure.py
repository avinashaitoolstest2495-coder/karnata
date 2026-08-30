# -*- coding: utf-8 -*-
"""
Karnata — scripts/scrape_full_krama_live_pure.py
100% PURE Official Scraper directly from Karnataka Agricultural Marketing Board (KRAMA - krama.karnataka.gov.in).
NO SYNTHETIC DATA. NO MOCK GENERATION.
"""

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import json
import re
import time
from datetime import datetime

DATE_STR = "28/08/2026"

DISTRICT_MAP = {
    "BAGALKOT": "ಬಾಗಲಕೋಟೆ", "BADAMI": "ಬಾಗಲಕೋಟೆ", "BILAGI": "ಬಾಗಲಕೋಟೆ", "HUNGUND": "ಬಾಗಲಕೋಟೆ", "JAMAKHANDI": "ಬಾಗಲಕೋಟೆ", "MUDHOL": "ಬಾಗಲಕೋಟೆ",
    "BANGARPET": "ಕೋಲಾರ", "KOLAR": "ಕೋಲಾರ", "MALUR": "ಕೋಲಾರ", "MULBAGAL": "ಕೋಲಾರ", "SRINIVASPUR": "ಕೋಲಾರ",
    "BELAGAVI": "ಬೆಳಗಾವಿ", "ATHANI": "ಬೆಳಗಾವಿ", "BAILHONGAL": "ಬೆಳಗಾವಿ", "CHIKODI": "ಬೆಳಗಾವಿ", "GOKAK": "ಬೆಳಗಾವಿ", "HUKKERI": "ಬೆಳಗಾವಿ", "KHANAPUR": "ಬೆಳಗಾವಿ", "RAMDURG": "ಬೆಳಗಾವಿ", "RAYBAG": "ಬೆಳಗಾವಿ", "SAUNDATTI": "ಬೆಳಗಾವಿ",
    "BELUR": "ಹಾಸನ", "HASSAN": "ಹಾಸನ", "ALUR": "ಹಾಸನ", "ARAKALGUD": "ಹಾಸನ", "ARSIKERE": "ಹಾಸನ", "CHANNARAYAPATNA": "ಹಾಸನ", "HOLENARASIPURA": "ಹಾಸನ", "SAKLESHPUR": "ಹಾಸನ",
    "BENGALURU": "ಬೆಂಗಳೂರು ನಗರ", "BINNY MILL": "ಬೆಂಗಳೂರು ನಗರ", "YASHAWANTHAPURA": "ಬೆಂಗಳೂರು ನಗರ",
    "CHICKBALLAPUR": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "BAGEPALLI": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "CHINTAMANI": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "GOWRIBIDNUR": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "GUDIBANDE": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "SIDLAGHATTA": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
    "CHIKKAMAGALURU": "ಚಿಕ್ಕಮಗಳೂರು", "KADUR": "ಚಿಕ್ಕಮಗಳೂರು", "KOPPA": "ಚಿಕ್ಕಮಗಳೂರು", "MUDIGERE": "ಚಿಕ್ಕಮಗಳೂರು", "NR PURA": "ಚಿಕ್ಕಮಗಳೂರು", "SRINGERI": "ಚಿಕ್ಕಮಗಳೂರು", "TARIKERE": "ಚಿಕ್ಕಮಗಳೂರು",
    "DAVANAGERE": "ದಾವಣಗೆರೆ", "CHANNAGIRI": "ದಾವಣಗೆರೆ", "HARIHARA": "ದಾವಣಗೆರೆ", "HONNALI": "ದಾವಣಗೆರೆ", "JAGALUR": "ದಾವಣಗೆರೆ", "NYAMATHI": "ದಾವಣಗೆರೆ",
    "DODDABALLAPUR": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "DEVANAHALLI": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "HOSKOTE": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "NELAMANGALA": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ",
    "HOSAPETE": "ವಿಜಯನಗರ", "HADAGALI": "ವಿಜಯನಗರ", "HAGARIBOMMANAHALLI": "ವಿಜಯನಗರ", "HARAPANAHALLI": "ವಿಜಯನಗರ", "KOTTURU": "ವಿಜಯನಗರ", "KUDLIGI": "ವಿಜಯನಗರ",
    "HUBBALLI": "ಧಾರವಾಡ", "DHARWAD": "ಧಾರವಾಡ", "ALNAVAR": "ಧಾರವಾಡ", "KALGHATGI": "ಧಾರವಾಡ", "KUNDGOL": "ಧಾರವಾಡ", "NAVALGUND": "ಧಾರವಾಡ",
    "KALABURAGI": "ಕಲಬುರಗಿ", "AFZALPUR": "ಕಲಬುರಗಿ", "ALAND": "ಕಲಬುರಗಿ", "CHINCHOLI": "ಕಲಬುರಗಿ", "CHITTAPUR": "ಕಲಬುರಗಿ", "JEVARGI": "ಕಲಬುರಗಿ", "SEDAM": "ಕಲಬುರಗಿ",
    "MANGALURU": "ದಕ್ಷಿಣ ಕನ್ನಡ", "BANTWAL": "ದಕ್ಷಿಣ ಕನ್ನಡ", "BELTHANGADY": "ದಕ್ಷಿಣ ಕನ್ನಡ", "PUTTUR": "ದಕ್ಷಿಣ ಕನ್ನಡ", "SULLIA": "ದಕ್ಷಿಣ ಕನ್ನಡ",
    "MYSURU": "ಮೈಸೂರು", "H D KOTE": "ಮೈಸೂರು", "HUNSUR": "ಮೈಸೂರು", "KR NAGAR": "ಮೈಸೂರು", "NANJANGUD": "ಮೈಸೂರು", "PIRIYAPATNA": "ಮೈಸೂರು", "TN PURA": "ಮೈಸೂರು",
    "SHIVAMOGGA": "ಶಿವಮೊಗ್ಗ", "BHADRAVATHI": "ಶಿವಮೊಗ್ಗ", "HOSANAGARA": "ಶಿವಮೊಗ್ಗ", "SAGAR": "ಶಿವಮೊಗ್ಗ", "SHIKARIPURA": "ಶಿವಮೊಗ್ಗ", "SORABA": "ಶಿವಮೊಗ್ಗ", "THIRTHAHALLI": "ಶಿವಮೊಗ್ಗ",
    "BALLARI": "ಬಳ್ಳಾರಿ", "KAMPLI": "ಬಳ್ಳಾರಿ", "KURUGODU": "ಬಳ್ಳಾರಿ", "SANDUR": "ಬಳ್ಳಾರಿ", "SIRUGUPPA": "ಬಳ್ಳಾರಿ",
    "BIDAR": "ಬೀದರ್", "AURAD": "ಬೀದರ್", "BASAVAKALYAN": "ಬೀದರ್", "BHALKI": "ಬೀದರ್", "HUMNABAD": "ಬೀದರ್",
    "CHAMARAJANAGAR": "ಚಾಮರಾಜನಗರ", "C.R.NAGAR": "ಚಾಮರಾಜನಗರ", "GUNDLUPET": "ಚಾಮರಾಜನಗರ", "KOLLEGAL": "ಚಾಮರಾಜನಗರ", "YELANDUR": "ಚಾಮರಾಜನಗರ",
    "CHITRADURGA": "ಚಿತ್ರದುರ್ಗ", "CHALLAKERE": "ಚಿತ್ರದುರ್ಗ", "HIRIYUR": "ಚಿತ್ರದುರ್ಗ", "HOLALKERE": "ಚಿತ್ರದುರ್ಗ", "HOSADURGA": "ಚಿತ್ರದುರ್ಗ", "MOLAKALMURU": "ಚಿತ್ರದುರ್ಗ",
    "GADAG": "ಗದಗ", "GAJENDRA GAD": "ಗದಗ", "LAKSHMESHWAR": "ಗದಗ", "MUNDARGI": "ಗದಗ", "NARAGUND": "ಗದಗ", "RON": "ಗದಗ", "SHIRHATTI": "ಗದಗ",
    "HAVERI": "ಹಾವೇರಿ", "BYADGI": "ಹಾವೇರಿ", "HANGAL": "ಹಾವೇರಿ", "HIREKERUR": "ಹಾವೇರಿ", "RANEBENNUR": "ಹಾವೇರಿ", "SAVANUR": "ಹಾವೇರಿ", "SHIGGAON": "ಹಾವೇರಿ",
    "KOPPAL": "ಕೊಪ್ಪಳ", "GANGAVATHI": "ಕೊಪ್ಪಳ", "KUSHTAGI": "ಕೊಪ್ಪಳ", "YELBURGA": "ಕೊಪ್ಪಳ",
    "MANDYA": "ಮಂಡ್ಯ", "KR PET": "ಮಂಡ್ಯ", "MADDUR": "ಮಂಡ್ಯ", "MALAVALLI": "ಮಂಡ್ಯ", "NAGAMANGALA": "ಮಂಡ್ಯ", "PANDAVAPURA": "ಮಂಡ್ಯ", "SRIRANGAPATNA": "ಮಂಡ್ಯ",
    "RAICHUR": "ರಾಯಚೂರು", "DEVADURGA": "ರಾಯಚೂರು", "LINGASUGUR": "ರಾಯಚೂರು", "MANVI": "ರಾಯಚೂರು", "MASKI": "ರಾಯಚೂರು", "SINDHANUR": "ರಾಯಚೂರು", "SIRWAR": "ರಾಯಚೂರು",
    "RAMANAGARA": "ರಾಮನಗರ", "CHANNAPATNA": "ರಾಮನಗರ", "KANAKAPURA": "ರಾಮನಗರ", "MAGADI": "ರಾಮನಗರ",
    "TUMKUR": "ತುಮಕೂರು", "CHIKKANAYAKANAHALLI": "ತುಮಕೂರು", "GUBBI": "ತುಮಕೂರು", "KORATAGERE": "ತುಮಕೂರು", "KUNIGAL": "ತುಮಕೂರು", "MADHUGIRI": "ತುಮಕೂರು", "PAVAGADA": "ತುಮಕೂರು", "SIRA": "ತುಮಕೂರು", "TIPTUR": "ತುಮಕೂರು", "TURUVEKERE": "ತುಮಕೂರು",
    "UDUPI": "ಉಡುಪಿ", "KARKALA": "ಉಡುಪಿ", "KUNDAPURA": "ಉಡುಪಿ",
    "UTTARA KANNADA": "ಉತ್ತರ ಕನ್ನಡ", "SIRSI": "ಉತ್ತರ ಕನ್ನಡ", "SHIRSI": "ಉತ್ತರ ಕನ್ನಡ", "ANKOLA": "ಉತ್ತರ ಕನ್ನಡ", "BHATKAL": "ಉತ್ತರ ಕನ್ನಡ", "HALIYAL": "ಉತ್ತರ ಕನ್ನಡ", "HONNAVAR": "ಉತ್ತರ ಕನ್ನಡ", "KARWAR": "ಉತ್ತರ ಕನ್ನಡ", "KUMTA": "ಉತ್ತರ ಕನ್ನಡ", "MUNDGOD": "ಉತ್ತರ ಕನ್ನಡ", "SIDDAPUR": "ಉತ್ತರ ಕನ್ನಡ", "YELLAPUR": "ಉತ್ತರ ಕನ್ನಡ",
    "VIJAYAPURA": "ವಿಜಯಪುರ", "BASAVANA BAGEWADI": "ವಿಜಯಪುರ", "INDI": "ವಿಜಯಪುರ", "MUDDEBIHAL": "ವಿಜಯಪುರ", "SINDAGI": "ವಿಜಯಪುರ",
    "YADGIR": "ಯಾದಗಿರಿ", "SHAHAPUR": "ಯಾದಗಿರಿ", "SHORAPUR": "ಯಾದಗಿರಿ", "GURMITKAL": "ಯಾದಗಿರಿ", "HUNSGI": "ಯಾದಗಿರಿ", "WADAGERA": "ಯಾದಗಿರಿ"
}

def classify_cat(comm_name):
    cn = comm_name.lower()
    if any(k in cn for k in ["arecanut", "copra", "coconut", "cotton", "coffee", "silk", "tobacco", "jaggery", "sugarcane"]):
        return "cash"
    if any(k in cn for k in ["paddy", "rice", "wheat", "jowar", "ragi", "maize", "bajra", "navane", "same", "millet"]):
        return "grain"
    if any(k in cn for k in ["tur", "gram", "urad", "moong", "alsandi", "cowpea", "dal", "chana", "arhar", "horsegram"]):
        return "pulse"
    if any(k in cn for k in ["onion", "tomato", "potato", "chilly", "garlic", "ginger", "cabbage", "brinjal", "carrot", "beans", "cucumber", "radish", "capsicum", "cauliflower"]):
        return "veg"
    if any(k in cn for k in ["banana", "mango", "apple", "grapes", "orange", "sapota", "papaya", "watermelon", "pomegranate", "lemon", "guava", "pineapple", "muskmelon"]):
        return "fruit"
    if any(k in cn for k in ["dry chilli", "turmeric", "pepper", "cardamom", "coriander", "cumin", "fenugreek", "clove", "mustard"]):
        return "spice"
    if any(k in cn for k in ["groundnut", "sunflower", "sesamum", "soyabean", "safflower", "castor", "gingelly", "linseed"]):
        return "oilseed"
    return "other"

def run_pure_krama_scraper():
    print("Scraping 100% genuine official KRAMA portal data...")
    url = "https://krama.karnataka.gov.in/"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', errors='ignore')
    soup = BeautifulSoup(html, 'html.parser')

    comm_map = {}
    for ca in soup.find_all('a', href=re.compile(r'LB_Com_(\d+)')):
        cm = re.search(r'LB_Com_(\d+)', ca['href'])
        if cm:
            comm_map[int(cm.group(1))] = ca.get_text(strip=True)

    links = soup.find_all('a', href=re.compile(r'LB_Var_(\d+)_(\d+)'))
    print(f"Found {len(links)} varieties across {len(comm_map)} commodities on KRAMA.")

    seen_keys = set()
    all_records = []

    for idx, a in enumerate(links):
        m = re.search(r'LB_Var_(\d+)_(\d+)', a['href'])
        if not m:
            continue
        c_code = int(m.group(1))
        v_code = int(m.group(2))
        v_raw = a.get_text(strip=True).replace('(*)', '').strip()
        c_raw = comm_map.get(c_code, 'Commodity')

        rep_url = f"https://krama.karnataka.gov.in/MainPage/DailyMrktPriceRep2?Rep=Com&CommCode={c_code}&VarCode={v_code}&Date={DATE_STR}&CommName={urllib.parse.quote(c_raw)}&VarName={urllib.parse.quote(v_raw)}"
        try:
            r = urllib.request.Request(rep_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            res_html = urllib.request.urlopen(r, timeout=6).read().decode('utf-8', errors='ignore')
            t_soup = BeautifulSoup(res_html, 'html.parser')
            table = t_soup.find('table')
            if table:
                rows = table.find_all('tr')
                for r_elem in rows[1:]:
                    cols = [c.get_text(strip=True) for c in r_elem.find_all(['td', 'th'])]
                    if len(cols) >= 7:
                        mkt = cols[0].strip().upper()
                        mkt_date = cols[1].strip()
                        variety = cols[2].strip()
                        try: arrivals = int(re.sub(r'[^\d]', '', cols[3])) if cols[3] else 0
                        except: arrivals = 0
                        try: min_p = int(re.sub(r'[^\d]', '', cols[4])) if cols[4] else 0
                        except: min_p = 0
                        try: max_p = int(re.sub(r'[^\d]', '', cols[5])) if cols[5] else 0
                        except: max_p = 0
                        try: modal_p = int(re.sub(r'[^\d]', '', cols[6])) if cols[6] else 0
                        except: modal_p = 0

                        if modal_p > 0:
                            uniq_key = (mkt, c_code, v_code, variety, modal_p)
                            if uniq_key in seen_keys:
                                continue
                            seen_keys.add(uniq_key)

                            dist = DISTRICT_MAP.get(mkt, "ಕರ್ನಾಟಕ")
                            cat = classify_cat(c_raw)

                            parts = [p.strip() for p in c_raw.split('/') if p.strip()]
                            crop_en = parts[0] if len(parts) > 0 else c_raw
                            crop_kn = parts[1] if len(parts) > 1 else crop_en

                            all_records.append({
                                "crop": crop_en,
                                "cropKn": crop_kn,
                                "cropEn": f"{crop_en} ({variety})",
                                "variety": variety,
                                "market": mkt,
                                "district": dist,
                                "date": mkt_date,
                                "arrivals": arrivals,
                                "min": min_p,
                                "max": max_p,
                                "avg": modal_p,
                                "unit": "ಕ್ವಿಂಟಾಲ್",
                                "cat": cat
                            })
        except Exception:
            pass
        time.sleep(0.04)

    print(f"DONE: Scraped {len(all_records)} 100% GENUINE official KRAMA records!")
    return all_records

if __name__ == "__main__":
    pure_records = run_pure_krama_scraper()
    output_data = {
        "date": "2026-08-28",
        "updated_at": datetime.now().isoformat(),
        "source": "Official KRAMA (krama.karnataka.gov.in)",
        "total_records": len(pure_records),
        "items": pure_records
    }
    with open("data/apmc_prices.json", "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print(f"SUCCESS: data/apmc_prices.json populated with {len(pure_records)} records.")
