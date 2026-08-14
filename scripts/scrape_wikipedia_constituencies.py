"""
Karnata — scrape_wikipedia_constituencies.py
Concurrent Wikipedia Scraper for 224 Karnataka Assembly Seats.
Extracts candidate-by-candidate election tables for 2023, 2018, 2013 (Party, Candidate, Votes, %, Margin).
Saves output into data/wikipedia_constituency_data.json.
"""

import os
import sys
import json
import re
import ssl
import base64
import urllib.request
from pathlib import Path
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT_DIR = Path(__file__).parent.parent
DATA_PATH = ROOT_DIR / "data" / "elections_data.json"
OUTPUT_PATH = ROOT_DIR / "data" / "wikipedia_constituency_data.json"

sys.path.append(str(ROOT_DIR / "scripts"))
from kannada_dictionary import get_party_kn, get_district_kn, get_term_kn

ctx = ssl._create_unverified_context()

def load_elections_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        raw = json.load(f)
        if "payload" in raw:
            SECRET_KEY = "NK_SECURE_KEY_2026_KARNATA"
            b_str = base64.b64decode(raw["payload"])
            dec_bytes = bytes([b_str[i] ^ ord(SECRET_KEY[i % len(SECRET_KEY)]) for i in range(len(b_str))])
            return json.loads(dec_bytes.decode("utf-8"))
        return raw

def fetch_wikipedia_constituency(ac_no, name_en):
    clean_name = name_en.replace("-", " ").strip()
    slug_candidates = [
        clean_name.replace(" ", "_") + "_Assembly_constituency",
        name_en.replace(" ", "_") + "_Assembly_constituency",
        clean_name.replace(" ", "") + "_Assembly_constituency"
    ]

    overrides = {
        "Gangavathi": "Gangavati_Assembly_constituency",
        "Chikkodi-Sadalga": "Chikkodi-Sadalga_Assembly_constituency",
        "Belagavi Uttar": "Belgaum_Uttar_Assembly_constituency",
        "Belagavi Dakshin": "Belgaum_Dakshin_Assembly_constituency",
        "Belagavi Rural": "Belgaum_Rural_Assembly_constituency",
        "Saundatti Yellamma": "Saundatti_Yellamma_Assembly_constituency",
        "Devar Hippargi": "Devara_Hippargi_Assembly_constituency",
        "Basavana Bagevadi": "Basavana_Bagevadi_Assembly_constituency",
        "Vijayapura City": "Bijapur_City_Assembly_constituency",
        "Gulbarga Rural": "Gulbarga_Rural_Assembly_constituency",
        "Gulbarga Dakshin": "Gulbarga_Dakshin_Assembly_constituency",
        "Gulbarga Uttar": "Gulbarga_Uttar_Assembly_constituency",
        "Shimoga Rural": "Shimoga_Rural_Assembly_constituency",
        "Shimoga": "Shimoga_Assembly_constituency",
        "Tirthahalli": "Thirthahalli_Assembly_constituency",
        "Byndoor": "Baindur_Assembly_constituency",
        "Kundapura": "Kundapur_Assembly_constituency",
        "Bantval": "Bantwal_Assembly_constituency",
        "Mangalore City North": "Mangalore_City_North_Assembly_constituency",
        "Mangalore City South": "Mangalore_City_South_Assembly_constituency",
        "Mangalore": "Mangalore_Assembly_constituency",
        "Chamaraja": "Chamaraja_Assembly_constituency",
        "Krishnaraja": "Krishnaraja_Assembly_constituency",
        "Narasimharaja": "Narasimharaja_Assembly_constituency"
    }

    if name_en in overrides:
        slug_candidates.insert(0, overrides[name_en])

    html = None
    for slug in slug_candidates:
        url = f"https://en.wikipedia.org/wiki/{slug}"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            res = urllib.request.urlopen(req, context=ctx, timeout=5)
            if res.status == 200:
                html = res.read().decode('utf-8')
                break
        except Exception:
            continue

    if not html:
        return ac_no, None

    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table', {'class': 'wikitable'})

    parsed_elections = {}

    for t in tables:
        caption = t.find('caption')
        cap_text = caption.get_text() if caption else t.get_text()[:150]
        year_match = re.search(r'\b(2023|2018|2013)\b', cap_text)
        if not year_match:
            continue

        yr = year_match.group(1)
        candidates = []
        margin_info = None

        for tr in t.find_all('tr'):
            tds = [re.sub(r'\[.*?\]', '', td.get_text().strip()) for td in tr.find_all(['td', 'th'])]
            if not tds:
                continue

            row_str = " ".join(tds).lower()
            if "margin of victory" in row_str or "majority" in row_str:
                margin_info = tds
                continue

            if len(tds) >= 4:
                party_val = tds[1] if len(tds) > 4 and tds[0] == '' else tds[0]
                cand_val = tds[2] if len(tds) > 4 and tds[0] == '' else tds[1]
                votes_val = tds[3] if len(tds) > 4 and tds[0] == '' else (tds[2] if len(tds) > 2 else "0")
                pct_val = tds[4] if len(tds) > 4 and tds[0] == '' else (tds[3] if len(tds) > 3 else "0")

                if any(p in party_val.upper() for p in ['INC', 'BJP', 'JD(S)', 'JDS', 'KRPP', 'IND', 'KJP', 'BSRCP', 'CPI', 'CPM', 'AAP', 'BSP', 'NOTA', 'POLITICAL']):
                    candidates.append({
                        "party_en": party_val,
                        "party_kn": get_party_kn(party_val),
                        "candidate_en": cand_val,
                        "candidate_kn": cand_val,
                        "votes": votes_val,
                        "vote_share": pct_val
                    })

        if candidates:
            parsed_elections[yr] = {
                "year": int(yr),
                "candidates": candidates,
                "margin_info": margin_info
            }

    return ac_no, parsed_elections

def run():
    print("Scraping Wikipedia candidate-by-candidate data for 224 Karnataka constituencies...", flush=True)
    elections_data = load_elections_data()
    records_by_year = elections_data["records"]

    constituencies_map = {}
    for r in records_by_year.get("2023", []):
        ac_no = r["ac_no"]
        name_en = r["constituency"]
        constituencies_map[ac_no] = name_en

    wiki_results = {}
    success_count = 0

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(fetch_wikipedia_constituency, ac_no, name_en) for ac_no, name_en in constituencies_map.items()]
        for future in as_completed(futures):
            ac_no, res = future.result()
            if res:
                wiki_results[str(ac_no)] = res
                success_count += 1

    payload = {
        "updated_at": "2026-08-14T09:00:00",
        "total_fetched": success_count,
        "data": wiki_results
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"SUCCESS: Successfully parsed Wikipedia election data for {success_count}/224 constituencies in {OUTPUT_PATH}", flush=True)

if __name__ == "__main__":
    run()
