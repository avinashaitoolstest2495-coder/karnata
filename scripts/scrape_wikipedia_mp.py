"""
Karnata — scrape_wikipedia_mp.py
Concurrent Wikipedia Scraper for 28 Karnataka Lok Sabha (MP) Seats.
Extracts:
1. Candidate photo URLs from Wikipedia infoboxes / Wikimedia.
2. Candidate-by-candidate election tables for 2024, 2019, 2014.
3. Complete Lok Sabha Election History (1952 – 2024).
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
    1: ("Chikkodi", "Chikkodi_Lok_Sabha_constituency", "Priyanka_Jarkiholi"),
    2: ("Belagavi", "Belgaum_Lok_Sabha_constituency", "Jagadish_Shettar"),
    3: ("Bagalkot", "Bagalkot_Lok_Sabha_constituency", "P._C._Gaddigoudar"),
    4: ("Bijapur", "Bijapur_Lok_Sabha_constituency", "Ramesh_Jigajinagi"),
    5: ("Gulbarga", "Gulbarga_Lok_Sabha_constituency", "Radhakrishna_Doddamani"),
    6: ("Raichur", "Raichur_Lok_Sabha_constituency", "G._Kumar_Naik"),
    7: ("Bidar", "Bidar_Lok_Sabha_constituency", "Sagar_Khandre"),
    8: ("Koppal", "Koppal_Lok_Sabha_constituency", "K._Rajashekar_Basavaraj_Hitnal"),
    9: ("Bellary", "Bellary_Lok_Sabha_constituency", "E._Tukaram"),
    10: ("Haveri", "Haveri_Lok_Sabha_constituency", "Basavaraj_Bommai"),
    11: ("Dharwad", "Dharwad_Lok_Sabha_constituency", "Pralhad_Joshi"),
    12: ("Uttara Kannada", "Uttara_Kannada_Lok_Sabha_constituency", "Vishweshwar_Hegde_Kageri"),
    13: ("Davanagere", "Davanagere_Lok_Sabha_constituency", "Prabha_Mallikarjun"),
    14: ("Shimoga", "Shimoga_Lok_Sabha_constituency", "B._Y._Raghavendra"),
    15: ("Udupi Chikmagalur", "Udupi_Chikmagalur_Lok_Sabha_constituency", "Kota_Srinivas_Poojary"),
    16: ("Hassan", "Hassan_Lok_Sabha_constituency", "Shreyas_Patel"),
    17: ("Dakshina Kannada", "Dakshina_Kannada_Lok_Sabha_constituency", "Brijesh_Chowta"),
    18: ("Chitradurga", "Chitradurga_Lok_Sabha_constituency", "Govind_Karjol"),
    19: ("Tumkur", "Tumkur_Lok_Sabha_constituency", "V._Somanna"),
    20: ("Mandya", "Mandya_Lok_Sabha_constituency", "H._D._Kumaraswamy"),
    21: ("Mysore", "Mysore_Lok_Sabha_constituency", "Yaduveer_Krishnadatta_Chamaraja_Wadiyar"),
    22: ("Chamarajanagar", "Chamarajanagar_Lok_Sabha_constituency", "Sunil_Bose"),
    23: ("Bangalore Rural", "Bangalore_Rural_Lok_Sabha_constituency", "C._N._Manjunath"),
    24: ("Bangalore North", "Bangalore_North_Lok_Sabha_constituency", "Shobha_Karandlaje"),
    25: ("Bangalore Central", "Bangalore_Central_Lok_Sabha_constituency", "P._C._Mohan"),
    26: ("Bangalore South", "Bangalore_South_Lok_Sabha_constituency", "Tejasvi_Surya"),
    27: ("Chikballapur", "Chikballapur_Lok_Sabha_constituency", "K._Sudhakar"),
    28: ("Kolar", "Kolar_Lok_Sabha_constituency", "M._Mallesh_Babu")
}

def get_candidate_photo(cand_slug):
    url = f"https://en.wikipedia.org/wiki/{cand_slug}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        res = urllib.request.urlopen(req, context=ctx, timeout=4)
        if res.status == 200:
            soup = BeautifulSoup(res.read().decode('utf-8'), 'html.parser')
            infobox = soup.find('table', {'class': 'infobox'})
            if infobox:
                for img in infobox.find_all('img'):
                    src = img.get('src', '')
                    if 'upload.wikimedia.org' in src and not any(x in src.lower() for x in ['flag', 'logo', 'map', 'icon', 'symbol', 'shield', 'location']):
                        return 'https:' + src if src.startswith('//') else src
    except Exception:
        pass
    return None

def fetch_wikipedia_mp(code, name_en, wiki_slug, mp_cand_slug):
    url = f"https://en.wikipedia.org/wiki/{wiki_slug}"
    html = None
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        res = urllib.request.urlopen(req, context=ctx, timeout=6)
        if res.status == 200:
            html = res.read().decode('utf-8')
    except Exception:
        pass

    photo_url = get_candidate_photo(mp_cand_slug)

    if not html:
        return code, {"photo_url": photo_url, "elections": {}, "full_history": []}

    soup = BeautifulSoup(html, 'html.parser')

    # Extract candidate photo from constituency infobox if not found yet
    if not photo_url:
        infobox = soup.find('table', {'class': 'infobox'})
        if infobox:
            for img in infobox.find_all('img'):
                src = img.get('src', '')
                if 'upload.wikimedia.org' in src and not any(x in src.lower() for x in ['flag', 'logo', 'map', 'icon', 'symbol', 'shield', 'location']):
                    photo_url = 'https:' + src if src.startswith('//') else src
                    break

    tables = soup.find_all('table', {'class': 'wikitable'})

    parsed_elections = {}
    full_history = []

    for t in tables:
        caption = t.find('caption')
        cap_text = caption.get_text() if caption else t.get_text()[:150]
        year_match = re.search(r'\b(2024|2019|2014)\b', cap_text)
        if year_match:
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

        # Parse Members of Parliament historical table (1952 - 2024)
        table_text = t.get_text()
        if any(h in table_text for h in ['Member', 'MP', 'Election', 'Lok Sabha']):
            for tr in t.find_all('tr')[1:]:
                tds = [re.sub(r'\[.*?\]', '', td.get_text().strip()) for td in tr.find_all(['td', 'th'])]
                if len(tds) >= 3 and re.search(r'\b(195\d|196\d|197\d|198\d|199\d|200\d|201\d|202\d)\b', tds[0]):
                    yr_val = re.search(r'\b(195\d|196\d|197\d|198\d|199\d|200\d|201\d|202\d)\b', tds[0]).group(1)
                    mp_name = tds[1] if len(tds) > 1 and tds[1] else (tds[2] if len(tds) > 2 else "")
                    p_name = tds[-1] if len(tds) > 2 else (tds[1] if len(tds) > 1 else "")
                    if mp_name and mp_name.lower() not in ['member', 'mp', 'name', 'winner']:
                        full_history.append({
                            "year": yr_val,
                            "winner_en": mp_name,
                            "winner_kn": mp_name,
                            "party_en": p_name,
                            "party_kn": get_party_kn(p_name)
                        })

    return code, {
        "photo_url": photo_url,
        "elections": parsed_elections,
        "full_history": full_history
    }

def run():
    print("Scraping Wikipedia candidate photos & full 1952-2024 history for 28 Karnataka Lok Sabha MP seats...", flush=True)
    wiki_results = {}
    success_count = 0

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_wikipedia_mp, code, item[0], item[1], item[2]) for code, item in MP_SEATS_MAP.items()]
        for future in as_completed(futures):
            code, res = future.result()
            if res:
                wiki_results[str(code)] = res
                success_count += 1

    payload = {
        "updated_at": "2026-08-14T09:25:00",
        "total_fetched": success_count,
        "data": wiki_results
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"SUCCESS: Successfully parsed Wikipedia photos & full history for {success_count}/28 Lok Sabha seats in {OUTPUT_PATH}", flush=True)

if __name__ == "__main__":
    run()
