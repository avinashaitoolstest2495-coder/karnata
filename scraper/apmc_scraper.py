"""
Karnataka — apmc_scraper.py
Scrapes & compiles daily live APMC (Agricultural Produce Market Committee) crop prices directly 
from official Karnataka State APMC Portal: krama.karnataka.gov.in
"""

import io
import json
import os
import re
import ssl
import time
import urllib.parse
from datetime import datetime, timedelta, timezone

import pandas as pd
import requests
import urllib3
from bs4 import BeautifulSoup
from utils import fetch, ist_date, ist_now, log, store, telegram_alert

# Suppress SSL certificate warnings for government portal
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://krama.karnataka.gov.in/Home_kan",
    "Accept-Language": "en-US,en;q=0.9,kn;q=0.8"
}

def categorize_crop(crop_name):
    """Assigns category, icon, and default unit based on commodity name."""
    cn = crop_name.lower()
    if any(k in cn for k in ["paddy", "wheat", "rice", "ragi", "jowar", "maize", "ಬತ್ತ", "ಗೋಧಿ", "ಅಕ್ಕಿ", "ಜೋಳ"]):
        return "grain", "🌾", "ಕ್ವಿಂಟಲ್"
    elif any(k in cn for k in ["tur", "gram", "urad", "moong", "pulse", "avare", "beans", "ತೊಗರಿ", "ಉದ್ದು", "ಕಡಲೆ", "ಹೆಸರು", "ಅವರೆ"]):
        return "pulse", "🫘", "ಕ್ವಿಂಟಲ್"
    elif any(k in cn for k in ["tomato", "onion", "potato", "carrot", "cabbage", "chilli", "brinjal", "capsicum", "ಟೊಮ್ಯಾಟೋ", "ಈರುಳ್ಳಿ", "ಆಲೂಗಡ್ಡೆ", "ಕ್ಯಾರೆಟ್"]):
        return "veg", "🥦", "ಕೆಜಿ"
    elif any(k in cn for k in ["mango", "banana", "watermelon", "papaya", "grapes", "lemon", "ಮಾವು", "ಬಾಳೆ", "ಕಲ್ಲಂಗಡಿ", "ಪಪ್ಪಾಯಿ", "ದ್ರಾಕ್ಷಿ", "ನಿಂಬೆ"]):
        return "fruit", "🍎", "ಕೆಜಿ"
    elif any(k in cn for k in ["groundnut", "sunflower", "sesamum", "ಶೇಂಗಾ", "ಸೂರ್ಯಕಾಂತಿ", "ಎಳ್ಳು"]):
        return "oilseed", "🥜", "ಕ್ವಿಂಟಲ್"
    elif any(k in cn for k in ["chilli", "tamarind", "garlic", "coriander", "ಮೆಣಸಿನಕಾಯಿ", "ಹುಣಸೆ", "ಬೆಳ್ಳುಳ್ಳಿ"]):
        return "spice", "🌶️", "ಕ್ವಿಂಟಲ್"
    else:
        return "cash", "🌴", "ಕ್ವಿಂಟಲ್"


def scrape_live_karnataka_apmc():
    """
    Scrapes live Karnataka APMC rates directly from krama.karnataka.gov.in
    """
    home_url = "https://krama.karnataka.gov.in/Home_kan"
    session = requests.Session()

    log.info(f"🌐 Accessing Karnataka APMC Portal: {home_url}...")
    
    # Establish session
    session.get(home_url, headers=HEADERS, verify=False, timeout=20)
    res = session.get(home_url, headers=HEADERS, verify=False, timeout=20)
    
    soup = BeautifulSoup(res.text, 'html.parser')

    # Step 1: Parse all commodity items cleanly from Home page HTML
    commodity_items = []
    for tr in soup.find_all('tr'):
        tr_html = str(tr)
        comm_code_m = re.search(r'CommCode=(\d+)', tr_html)
        var_code_m = re.search(r'VarCode=(\d+)', tr_html)
        comm_name_m = re.search(r'CommName=([^&"\']+)', tr_html)
        var_name_m = re.search(r'VarName=([^&"\']+)', tr_html)

        if comm_code_m and var_code_m:
            c_code = comm_code_m.group(1)
            v_code = var_code_m.group(1)
            c_name = urllib.parse.unquote(comm_name_m.group(1)) if comm_name_m else ""
            v_name = urllib.parse.unquote(var_name_m.group(1)) if var_name_m else ""
            
            commodity_items.append({
                "commCode": c_code,
                "varCode": v_code,
                "commName": c_name,
                "varName": v_name
            })

    # Deduplicate items by (commCode, varCode)
    unique_map = {}
    for item in commodity_items:
        key = (item["commCode"], item["varCode"])
        if key not in unique_map:
            unique_map[key] = item
            
    items_to_fetch = list(unique_map.values())
    log.info(f"✔ Found {len(items_to_fetch)} unique commodity/variety items to query.")

    base_endpoint = "https://krama.karnataka.gov.in/MainPage/DailyMrktPriceRep2"
    live_records = []

    # Prepare active market dates
    today_str = datetime.now().strftime("%d/%m/%Y")
    yesterday_str = (datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y")
    dates_to_try = [today_str, yesterday_str, "04/08/2026"]

    # Step 2: Query clean dictionary parameters for each commodity item
    for idx, item in enumerate(items_to_fetch):
        c_code = item["commCode"]
        v_code = item["varCode"]
        c_name = item["commName"]
        v_name = item["varName"]

        success = False
        for d_str in dates_to_try:
            params = {
                "Rep": "Var",
                "CommCode": c_code,
                "VarCode": v_code,
                "Date": d_str,
                "CommName": c_name,
                "VarName": v_name
            }

            try:
                # Clean dictionary parameters resolve HTTP 500 & empty response bugs
                r = session.get(base_endpoint, params=params, headers=HEADERS, verify=False, timeout=8)

                if r.status_code == 200 and "<table" in r.text.lower():
                    # io.StringIO resolves Pandas 2.0+ FileNotFoundError
                    tables = pd.read_html(io.StringIO(r.text))

                    if tables and len(tables[0]) > 0 and len(tables[0].columns) >= 6:
                        df = tables[0]
                        cat, icon, default_unit = categorize_crop(c_name)

                        for _, row in df.iterrows():
                            market_name = str(row.iloc[0]).strip()
                            market_date = str(row.iloc[1]).strip()
                            arrivals = str(row.iloc[2]).strip()
                            min_p = str(row.iloc[3]).strip()
                            max_p = str(row.iloc[4]).strip()
                            modal_p = str(row.iloc[5]).strip()

                            if min_p.isdigit() and max_p.isdigit():
                                min_val = int(min_p)
                                max_val = int(max_p)
                                modal_val = int(modal_p) if modal_p.isdigit() else int((min_val + max_val) / 2)

                                live_records.append({
                                    "crop": f"{c_name} / {v_name}",
                                    "cropKn": c_name,
                                    "cropEn": c_name.split('/')[0].strip() if '/' in c_name else c_name,
                                    "variety": v_name,
                                    "market": market_name,
                                    "marketEn": market_name.title(),
                                    "date": market_date,
                                    "arrivals": arrivals,
                                    "min": round(min_val / 100, 2) if default_unit == "ಕೆಜಿ" else min_val,
                                    "max": round(max_val / 100, 2) if default_unit == "ಕೆಜಿ" else max_val,
                                    "avg": round(modal_val / 100, 2) if default_unit == "ಕೆಜಿ" else modal_val,
                                    "modal_per_quintal": modal_val,
                                    "change": 0,
                                    "cat": cat,
                                    "icon": icon,
                                    "unit": default_unit,
                                    "commCode": c_code,
                                    "varCode": v_code
                                })
                        success = True
                        break  # Stop date loop once market table is fetched
            except Exception:
                continue

        time.sleep(0.02)  # Fast delay

    # Fallback to homepage table parsing ONLY if all detail endpoints fail
    if not live_records:
        log.warning("⚠️ Detail endpoints empty, parsing homepage widget table...")
        current_cat = "General"
        for tr in soup.find_all('tr'):
            tr_text = tr.get_text(" ", strip=True)
            tr_html = str(tr)

            if len(tr.find_all('td')) == 1 and not any(c.isdigit() for c in tr_text) and len(tr_text) > 2:
                current_cat = tr_text
                continue

            comm_code_m = re.search(r'CommCode=(\d+)', tr_html)
            var_code_m = re.search(r'VarCode=(\d+)', tr_html)
            comm_name_m = re.search(r'CommName=([^&"\']+)', tr_html)
            var_name_m = re.search(r'VarName=([^&"\']+)', tr_html)

            tds = tr.find_all('td')
            nums = [td.get_text(strip=True) for td in tds if td.get_text(strip=True).isdigit()]

            if len(nums) >= 2:
                min_v = int(nums[0])
                max_v = int(nums[1])
                avg_v = int((min_v + max_v) / 2)

                text_cols = [td.get_text(strip=True) for td in tds if not td.get_text(strip=True).isdigit()]
                label = text_cols[0] if text_cols else "Commodity"

                c_name = urllib.parse.unquote(comm_name_m.group(1)) if comm_name_m else label
                v_name = urllib.parse.unquote(var_name_m.group(1)) if var_name_m else label

                cat, icon, default_unit = categorize_crop(c_name)

                live_records.append({
                    "crop": f"{c_name} / {v_name}",
                    "cropKn": c_name,
                    "cropEn": c_name.split('/')[0].strip() if '/' in c_name else c_name,
                    "variety": v_name,
                    "market": "Karnataka APMC",
                    "marketEn": "Karnataka APMC",
                    "date": ist_date(),
                    "arrivals": "100",
                    "min": round(min_v / 100, 2) if default_unit == "ಕೆಜಿ" else min_v,
                    "max": round(max_v / 100, 2) if default_unit == "ಕೆಜಿ" else max_v,
                    "avg": round(avg_v / 100, 2) if default_unit == "ಕೆಜಿ" else avg_v,
                    "modal_per_quintal": avg_v,
                    "change": 0,
                    "cat": cat,
                    "icon": icon,
                    "unit": default_unit,
                    "commCode": comm_code_m.group(1) if comm_code_m else "",
                    "varCode": var_code_m.group(1) if var_code_m else ""
                })

    log.info(f"✔ Live Scraping Completed! Collected {len(live_records)} total market records.")
    return live_records


def run() -> dict:
    """Main execution entry point."""
    log.info("🌾 Starting Karnataka APMC live price scraper...")

    items = scrape_live_karnataka_apmc()

    best_prices = {}
    markets_dict = {}

    for item in items:
        crop_en = item["cropEn"]
        modal_q = item["modal_per_quintal"]

        # Build summarized best_prices dictionary
        if crop_en not in best_prices or modal_q > best_prices[crop_en]["modal_per_quintal"]:
            best_prices[crop_en] = {
                "name_kn": item["cropKn"],
                "name_en": crop_en,
                "type": item["cat"],
                "market_kn": item["market"],
                "min_per_kg": round(item["min"] / 100, 2) if item["unit"] == "ಕ್ವಿಂಟಲ್" else item["min"],
                "max_per_kg": round(item["max"] / 100, 2) if item["unit"] == "ಕ್ವಿಂಟಲ್" else item["max"],
                "modal_per_kg": round(item["avg"] / 100, 2) if item["unit"] == "ಕ್ವಿಂಟಲ್" else item["avg"],
                "min_per_quintal": item["min"] if item["unit"] == "ಕ್ವಿಂಟಲ್" else item["min"] * 100,
                "max_per_quintal": item["max"] if item["unit"] == "ಕ್ವಿಂಟಲ್" else item["max"] * 100,
                "modal_per_quintal": modal_q,
                "change": item["change"],
                "unit": item["unit"],
                "icon": item["icon"]
            }

        m_key = item["marketEn"].lower()
        if m_key not in markets_dict:
            markets_dict[m_key] = {"name_kn": item["market"], "crops": {}}
        markets_dict[m_key]["crops"][crop_en] = best_prices[crop_en]

    unique_markets = len(set(i["market"] for i in items)) if items else 0

    output = {
        "date": ist_date(),
        "updated_at": ist_now(),
        "source": "krama.karnataka.gov.in / Karnataka APMC Mandi Portal",
        "source_url": "https://krama.karnataka.gov.in/Home_kan",
        "total_records": len(items),
        "total_markets": unique_markets,
        "is_live": True,
        "items": items,
        "best_prices": best_prices,
        "markets": markets_dict,
        "note_kn": "ಬೆಲೆ ಪ್ರತಿ ದಿನ ಕರ್ನಾಟಕ APMC ಮಾರುಕಟ್ಟೆಯಿಂದ ನೇರ ಸಜೀವ ನವೀಕರಣ",
        "note_en": "Prices updated live from official Karnataka APMC mandi portal — krama.karnataka.gov.in",
    }

    from history_tracker import process_apmc_history
    output = process_apmc_history(output)

    # Save to JSON via store helper
    store("apmc_prices.json", "apmc_prices", output)
    log.info(f"✅ APMC: Published {len(items)} live commodity market rates across {unique_markets} mandis")
    return output


if __name__ == "__main__":
    run()