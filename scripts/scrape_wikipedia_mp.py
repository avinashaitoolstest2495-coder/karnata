"""
Karnata — scrape_wikipedia_mp.py
Concurrent Wikipedia Scraper for 28 Karnataka Lok Sabha (MP) Seats.
Extracts candidate-by-candidate election tables for 2024, 2019, 2014 (Party, Candidate, Votes, %, Margin).
Saves output into data/wikipedia_mp_data.json.
"""

import os
import sys
import json
import re
import ssl
import urllib.request
from pathlib import Path
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT_DIR = Path(__file__).parent.parent
OUTPUT_PATH = ROOT_DIR / "data" / "wikipedia_mp_data.json"

sys.path.append(str(ROOT_DIR / "scripts"))
from kannada_dictionary import get_party_kn, get_district_kn, get_term_kn

ctx = ssl._create_unverified_context()

MP_SEATS_MAP = {
    1: ("Chikkodi", "Chikkodi_Lok_Sabha_constituency"),
    2: ("Belagavi", "Belgaum_Lok_Sabha_constituency"),
    3: ("Bagalkot", "Bagalkot_Lok_Sabha_constituency"),
    4: ("Bijapur", "Bijapur_Lok_Sabha_constituency"),
    5: ("Gulbarga", "Gulbarga_Lok_Sabha_constituency"),
    6: ("Raichur", "Raichur_Lok_Sabha_constituency"),
    7: ("Bidar", "Bidar_Lok_Sabha_constituency"),
    8: ("Koppal", "Koppal_Lok_Sabha_constituency"),
    9: ("Bellary", "Bellary_Lok_Sabha_constituency"),
    10: ("Haveri", "Haveri_Lok_Sabha_constituency"),
    11: ("Dharwad", "Dharwad_Lok_Sabha_constituency"),
    12: ("Uttara Kannada", "Uttara_Kannada_Lok_Sabha_constituency"),
    13: ("Davanagere", "Davanagere_Lok_Sabha_constituency"),
    14: ("Shimoga", "Shimoga_Lok_Sabha_constituency"),
    15: ("Udupi Chikmagalur", "Udupi_Chikmagalur_Lok_Sabha_constituency"),
    16: ("Hassan", "Hassan_Lok_Sabha_constituency"),
    17: ("Dakshina Kannada", "Dakshina_Kannada_Lok_Sabha_constituency"),
    18: ("Chitradurga", "Chitradurga_Lok_Sabha_constituency"),
    19: ("Tumkur", "Tumkur_Lok_Sabha_constituency"),
    20: ("Mandya", "Mandya_Lok_Sabha_constituency"),
    21: ("Mysore", "Mysore_Lok_Sabha_constituency"),
    22: ("Chamarajanagar", "Chamarajanagar_Lok_Sabha_constituency"),
    23: ("Bangalore Rural", "Bangalore_Rural_Lok_Sabha_constituency"),
    24: ("Bangalore North", "Bangalore_North_Lok_Sabha_constituency"),
    25: ("Bangalore Central", "Bangalore_Central_Lok_Sabha_constituency"),
    26: ("Bangalore South", "Bangalore_South_Lok_Sabha_constituency"),
    27: ("Chikballapur", "Chikballapur_Lok_Sabha_constituency"),
    28: ("Kolar", "Kolar_Lok_Sabha_constituency")
}

def fetch_wikipedia_mp(code, name_en, wiki_slug):
    url = f"https://en.wikipedia.org/wiki/{wiki_slug}"
    html = None
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        res = urllib.request.urlopen(req, context=ctx, timeout=6)
        if res.status == 200:
            html = res.read().decode('utf-8')
    except Exception:
        pass

    if not html:
        return code, None

    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table', {'class': 'wikitable'})

    parsed_elections = {}

    for t in tables:
        caption = t.find('caption')
        cap_text = caption.get_text() if caption else t.get_text()[:150]
        year_match = re.search(r'\b(2024|2019|2014)\b', cap_text)
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

                if any(p in party_val.upper() for p in ['INC', 'BJP', 'JD(S)', 'JDS', 'KRPP', 'IND', 'AAP', 'BSP', 'NOTA', 'POLITICAL']):
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

    return code, parsed_elections

def run():
    print("Scraping Wikipedia Lok Sabha election data for 28 Karnataka MP constituencies...", flush=True)
    wiki_results = {}
    success_count = 0

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_wikipedia_mp, code, item[0], item[1]) for code, item in MP_SEATS_MAP.items()]
        for future in as_completed(futures):
            code, res = future.result()
            if res:
                wiki_results[str(code)] = res
                success_count += 1

    payload = {
        "updated_at": "2026-08-14T09:20:00",
        "total_fetched": success_count,
        "data": wiki_results
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"SUCCESS: Successfully parsed Wikipedia MP election data for {success_count}/28 Lok Sabha seats in {OUTPUT_PATH}", flush=True)

if __name__ == "__main__":
    run()
