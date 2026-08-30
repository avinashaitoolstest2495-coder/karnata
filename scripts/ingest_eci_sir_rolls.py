#!/usr/bin/env python3
"""
scripts/ingest_eci_sir_rolls.py
Comprehensive Official ECI SIR Draft Electoral Roll Metadata Ingestion for Karnataka (S10)
Sources:
  - Official Common Constituencies: https://gateway-voters.eci.gov.in/api/v1/common/constituencies?stateCode=S10
  - Official Common Districts: https://gateway-voters.eci.gov.in/api/v1/common/districts/S10
  - Official Citizen Gateway: https://gateway-voters.eci.gov.in/api/v1/citizen/sir/

Compiles 100% of all Karnataka Polling Stations (AC 1 to 224, Parts 1 to N)
with Direct Official PDF Download URLs for Kannada (KAN) and English (ENG).
"""

import os
import sys
import json
import time
import argparse
import urllib.request
import ssl
from datetime import datetime

# UTF-8 stdout configuration
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# SSL context
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE_URL = "https://gateway-voters.eci.gov.in"
STATE_CODE = "S10"
STATE_NAME = "Karnataka"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Referer': f'https://voters.eci.gov.in/download-eroll?stateCode={STATE_CODE}',
    'Origin': 'https://voters.eci.gov.in',
    'state': STATE_CODE,
    'Content-Type': 'application/json'
}

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'sir_voter_rolls')

def fetch_json(endpoint, max_retries=3, delay=0.8):
    url = f"{BASE_URL}{endpoint}" if endpoint.startswith('/') else endpoint
    req = urllib.request.Request(url, headers=HEADERS)
    for attempt in range(1, max_retries + 1):
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=20) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                return data
        except Exception as e:
            if attempt == max_retries:
                print(f"[ERROR] Failed to fetch {url}: {e}")
                return None
            time.sleep(delay * attempt)

def get_now_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")

def get_direct_pdf_url(ac_no, part_no, lang="KAN"):
    return f"https://voters.eci.gov.in/eroll/2026/s10/sir-draftroll/{ac_no}/2026-EROLLGEN-S10-{ac_no}-SIR-DraftRoll-Revision1-{lang.upper()}-{part_no}-WI.pdf"

def ingest_master_directory():
    print("Fetching official Karnataka Districts & 224 Constituencies from ECI...")
    dist_list = fetch_json(f"/api/v1/common/districts/{STATE_CODE}")
    const_list = fetch_json(f"/api/v1/common/constituencies?stateCode={STATE_CODE}")

    if not dist_list or not const_list:
        print("[FATAL] Unable to fetch master directory from ECI.")
        return None, None

    dist_map = {}
    for d in dist_list:
        d_cd = d.get("districtCd")
        d_name = d.get("districtValue", "").strip()
        d_no_str = d.get("districtNo", "0")
        try:
            d_no = int(d_no_str)
        except:
            d_no = 0
        dist_map[d_cd] = {
            "district_cd": d_cd,
            "district_no": d_no,
            "district_name": d_name,
            "district_name_kn": d_name,
            "acs": []
        }

    all_acs = []
    ac_map = {}

    for c in const_list:
        ac_no = c.get("asmblyNo")
        ac_name = (c.get("asmblyName") or "").strip()
        ac_name_kn = (c.get("asmblyNameL1") or ac_name).strip()
        d_cd = c.get("districtCd")
        d_info = dist_map.get(d_cd, {})
        d_name = d_info.get("district_name", "Karnataka")

        ac_record = {
            "ac_number": ac_no,
            "ac_name": ac_name,
            "ac_name_kn": ac_name_kn,
            "district_cd": d_cd,
            "district_no": d_info.get("district_no", 0),
            "district_name": d_name,
            "district_name_kn": d_info.get("district_name_kn", d_name),
            "category": c.get("category", "GEN"),
            "category_kn": c.get("categoryL1", "ಸಾಮಾನ್ಯ"),
            "parliament_name_kn": c.get("prlmntNameL1", ""),
            "parliament_no": c.get("pcNo", "")
        }

        all_acs.append(ac_record)
        ac_map[ac_no] = ac_record

        if d_cd in dist_map:
            dist_map[d_cd]["acs"].append(ac_record)

    all_acs_sorted = sorted(all_acs, key=lambda x: x["ac_number"])

    # Organize districts
    districts_structured = []
    for d_cd, d_obj in sorted(dist_map.items(), key=lambda x: x[1]["district_name"]):
        if d_obj["acs"]:
            d_obj["acs"] = sorted(d_obj["acs"], key=lambda x: x["ac_number"])
            d_obj["ac_count"] = len(d_obj["acs"])
            districts_structured.append(d_obj)

    os.makedirs(DATA_DIR, exist_ok=True)

    index_data = {
        "state": STATE_NAME,
        "state_code": STATE_CODE,
        "roll_name": "Karnataka SIR 2026 Draft Electoral Roll",
        "official_portal_url": f"https://voters.eci.gov.in/download-eroll?stateCode={STATE_CODE}",
        "total_districts": len(districts_structured),
        "total_acs": len(all_acs_sorted),
        "source": "Election Commission of India",
        "last_verified": get_now_timestamp(),
        "districts": districts_structured,
        "constituencies": all_acs_sorted
    }

    index_file = os.path.join(DATA_DIR, "index.json")
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    print(f"[OK] Saved official index.json: {len(districts_structured)} districts and {len(all_acs_sorted)} ACs.")
    return index_data, ac_map

def ingest_ac_parts(ac_info):
    ac_no = ac_info["ac_number"]
    ac_name = ac_info["ac_name"]
    d_name = ac_info["district_name"]
    d_cd = ac_info.get("district_cd", "")
    now_str = get_now_timestamp()

    # Fetch parts from pre-draft and regular endpoints
    predraft_resp = fetch_json(f"/api/v1/citizen/sir/getPartPreDraftByAc?Asmbly={ac_no}")
    predraft_parts = predraft_resp.get("payload", []) if predraft_resp else []

    regular_resp = fetch_json(f"/api/v1/citizen/sir/getPartByAc?Asmbly={ac_no}")
    regular_parts = regular_resp.get("payload", []) if regular_resp else []

    parts_map = {}

    for p in predraft_parts:
        part_no = p.get("partNumber")
        if part_no is None:
            continue
        part_name_en = (p.get("partName") or "").strip()
        part_name_kn = (p.get("partNameL1") or "").strip()
        address = (p.get("psBuildingDetail") or part_name_kn or part_name_en).strip()

        parts_map[part_no] = {
            "part_number": part_no,
            "polling_station_en": part_name_en,
            "polling_station_kn": part_name_kn,
            "address": address,
            "ps_type": p.get("psTypeEng") or p.get("psTypeV1") or "GENERAL",
            "ward_number": p.get("wardNumber"),
            "pdf_url_kan": get_direct_pdf_url(ac_no, part_no, "KAN"),
            "pdf_url_eng": get_direct_pdf_url(ac_no, part_no, "ENG"),
            "official_pdf_url": get_direct_pdf_url(ac_no, part_no, "KAN"),
            "availability_status": "AVAILABLE",
            "source": "Election Commission of India",
            "last_verified": now_str
        }

    for p in regular_parts:
        part_no = p.get("partNumber")
        if part_no is None:
            continue
        part_name_en = (p.get("partName") or "").strip()
        part_name_kn = (p.get("partNameV1") or "").strip()

        if part_no not in parts_map:
            parts_map[part_no] = {
                "part_number": part_no,
                "polling_station_en": part_name_en,
                "polling_station_kn": part_name_kn,
                "address": part_name_kn or part_name_en,
                "ps_type": "GENERAL",
                "ward_number": None,
                "pdf_url_kan": get_direct_pdf_url(ac_no, part_no, "KAN"),
                "pdf_url_eng": get_direct_pdf_url(ac_no, part_no, "ENG"),
                "official_pdf_url": get_direct_pdf_url(ac_no, part_no, "KAN"),
                "availability_status": "AVAILABLE",
                "source": "Election Commission of India",
                "last_verified": now_str
            }
        else:
            if not parts_map[part_no]["polling_station_kn"] and part_name_kn:
                parts_map[part_no]["polling_station_kn"] = part_name_kn
            if not parts_map[part_no]["polling_station_en"] and part_name_en:
                parts_map[part_no]["polling_station_en"] = part_name_en

    sorted_parts = sorted(parts_map.values(), key=lambda x: x["part_number"])

    ac_file_data = {
        "state": STATE_NAME,
        "state_code": STATE_CODE,
        "district_cd": d_cd,
        "district_name": d_name,
        "district_name_kn": ac_info.get("district_name_kn", d_name),
        "ac_number": ac_no,
        "ac_name": ac_name,
        "ac_name_kn": ac_info.get("ac_name_kn", ac_name),
        "roll_name": "Karnataka SIR 2026 Draft Electoral Roll",
        "total_parts": len(sorted_parts),
        "source": "Election Commission of India",
        "last_verified": now_str,
        "parts": sorted_parts
    }

    ac_file_path = os.path.join(DATA_DIR, f"ac_{ac_no}.json")
    with open(ac_file_path, "w", encoding="utf-8") as f:
        json.dump(ac_file_data, f, ensure_ascii=False, indent=2)

    return ac_file_data

def main():
    parser = argparse.ArgumentParser(description="Official ECI SIR voter rolls ingestion for Karnataka")
    parser.add_argument("--all", action="store_true", help="Ingest all 224 ACs across Karnataka")
    parser.add_argument("--test-ac", type=int, help="Ingest single AC for testing (e.g. 61)")
    args = parser.parse_args()

    index_data, ac_map = ingest_master_directory()
    if not index_data:
        sys.exit(1)

    if args.test_ac:
        target_ac = ac_map.get(args.test_ac)
        if not target_ac:
            print(f"[ERROR] AC #{args.test_ac} not found in official directory.")
            sys.exit(1)
        print(f"Testing ingestion for AC #{args.test_ac}: {target_ac['ac_name']} ({target_ac['district_name']})...")
        ac_data = ingest_ac_parts(target_ac)
        print(f"[OK] Ingested {ac_data['total_parts']} parts for AC #{args.test_ac}.")
        if ac_data["parts"]:
            print("First part:", ac_data["parts"][0])
            print("Part 260:", [p for p in ac_data["parts"] if p["part_number"] == 260])

    elif args.all:
        print(f"\nStarting comprehensive ingestion for all {len(index_data['constituencies'])} official ACs...")
        total = len(index_data["constituencies"])
        success_count = 0
        total_parts_count = 0

        for idx, ac_info in enumerate(index_data["constituencies"], 1):
            ac_no = ac_info["ac_number"]
            ac_name = ac_info["ac_name"]
            try:
                ac_data = ingest_ac_parts(ac_info)
                parts_count = ac_data["total_parts"]
                total_parts_count += parts_count
                success_count += 1
                if idx % 15 == 0 or idx == total:
                    print(f"[{idx}/{total}] AC #{ac_no:03d} {ac_name}: {parts_count} parts (Total parts: {total_parts_count})")
            except Exception as e:
                print(f"[ERROR] Failed AC #{ac_no} {ac_name}: {e}")
            time.sleep(0.06)

        index_data["total_verified_parts"] = total_parts_count
        with open(os.path.join(DATA_DIR, "index.json"), "w", encoding="utf-8") as f:
            json.dump(index_data, f, ensure_ascii=False, indent=2)

        print(f"\n[COMPLETED] Ingested all {success_count}/{total} official ACs with {total_parts_count} verified parts!")

if __name__ == "__main__":
    main()
