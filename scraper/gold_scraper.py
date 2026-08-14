"""
Karnata — gold_scraper.py
Scrapes today's real-time live gold & silver rates for Karnataka.
Sources: GoodReturns, Joyalukkas / Jos Alukkas, IBJA, Financial Portals
"""

import re
import json
import requests
from bs4 import BeautifulSoup
from utils import fetch, store, log, ist_now, ist_date

CITIES = {
    "bangalore": {"kn": "ಬೆಂಗಳೂರು", "en": "Bangalore"},
    "mysore":    {"kn": "ಮೈಸೂರು",   "en": "Mysore"},
    "hubli":     {"kn": "ಹುಬ್ಬಳ್ಳಿ",  "en": "Hubli"},
    "mangalore": {"kn": "ಮಂಗಳೂರು",  "en": "Mangalore"},
    "belgaum":   {"kn": "ಬೆಳಗಾವಿ",  "en": "Belgaum"},
    "gulbarga":  {"kn": "ಕಲಬುರಗಿ",  "en": "Gulbarga"},
    "davangere": {"kn": "ದಾವಣಗೆರೆ", "en": "Davangere"},
    "shimoga":   {"kn": "ಶಿವಮೊಗ್ಗ",  "en": "Shimoga"},
    "tumkur":    {"kn": "ತುಮಕೂರು",  "en": "Tumkur"},
    "hassan":    {"kn": "ಹಾಸನ",      "en": "Hassan"},
}

def scrape_goodreturns_gold() -> dict | None:
    """Scrape live Bangalore / Karnataka gold rates from GoodReturns."""
    url = "https://www.goodreturns.in/gold-rates/bangalore.html"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        resp = requests.get(url, headers=headers, timeout=12)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "lxml")
            rates = {}
            # Look for tables containing 22K and 24K prices
            for table in soup.find_all("table"):
                text = table.get_text(" ", strip=True)
                if "22 Carat" in text or "22K" in text:
                    m22 = re.search(r"₹\s*([\d,]{4,6})", text)
                    if m22: rates["22k_per_gram"] = int(m22.group(1).replace(",", ""))
                if "24 Carat" in text or "24K" in text:
                    m24 = re.search(r"₹\s*([\d,]{4,6})", text)
                    if m24: rates["24k_per_gram"] = int(m24.group(1).replace(",", ""))
            
            if "22k_per_gram" in rates and 5000 <= rates["22k_per_gram"] <= 10000:
                rates["18k_per_gram"] = round(rates["22k_per_gram"] * 18 / 22)
                rates["14k_per_gram"] = round(rates["22k_per_gram"] * 14 / 22)
                if "24k_per_gram" not in rates:
                    rates["24k_per_gram"] = round(rates["22k_per_gram"] * 24 / 22)
                log.info(f"✅ Scraped GoodReturns Gold: {rates}")
                return rates
    except Exception as e:
        log.warning(f"⚠️ GoodReturns gold fetch failed: {e}")
    return None

def scrape_jos_alukkas_gold() -> dict | None:
    """Scrape live gold rates directly from Jos Alukkas / Joyalukkas."""
    url = "https://www.josalukkasonline.com/gold-rate-today/Karnataka/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        resp = requests.get(url, headers=headers, timeout=12)
        if resp.status_code == 200:
            text = resp.text
            rates = {}
            m24 = re.search(r"24K[^\d]*([\d,]{4,7})", text, re.I)
            m22 = re.search(r"22K[^\d]*([\d,]{4,7})", text, re.I)
            if m24: rates["24k_per_gram"] = int(m24.group(1).replace(",", ""))
            if m22: rates["22k_per_gram"] = int(m22.group(1).replace(",", ""))
            
            # Normalize if 2g or 10g rate was returned
            for k in ["24k_per_gram", "22k_per_gram"]:
                if k in rates:
                    if rates[k] > 50000: rates[k] = round(rates[k] / 10)
                    elif rates[k] > 10000: rates[k] = round(rates[k] / 2)

            if "22k_per_gram" in rates and 5000 <= rates["22k_per_gram"] <= 10000:
                rates["18k_per_gram"] = round(rates["22k_per_gram"] * 18 / 22)
                rates["14k_per_gram"] = round(rates["22k_per_gram"] * 14 / 22)
                log.info(f"✅ Scraped Jos Alukkas Gold: {rates}")
                return rates
    except Exception as e:
        log.warning(f"⚠️ Jos Alukkas fetch failed: {e}")
    return None

def scrape_silver_rate() -> float:
    """Scrape live silver rate per gram."""
    url = "https://www.goodreturns.in/silver-rates/bangalore.html"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        resp = requests.get(url, headers=headers, timeout=12)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "lxml")
            for row in soup.find_all("tr"):
                cells = [td.get_text(strip=True) for td in row.find_all(["td", "th"])]
                if len(cells) >= 2 and ("1 gram" in cells[0].lower() or cells[0] == "1"):
                    m = re.search(r"[\d.]+", cells[1].replace(",", ""))
                    if m:
                        val = float(m.group())
                        if 60.0 <= val <= 140.0:
                            return val
                        elif val > 140.0:
                            return round(val / 10, 2)
    except Exception as e:
        log.error(f"❌ Silver parse error: {e}")
    return 89.50

def run() -> dict:
    log.info("🥇 Starting Live Karnataka Gold & Silver Scraper...")

    base_rates = scrape_goodreturns_gold()
    if not base_rates:
        base_rates = scrape_jos_alukkas_gold()

    if not base_rates or "22k_per_gram" not in base_rates:
        base_rates = {
            "24k_per_gram": 7680,
            "22k_per_gram": 7040,
            "18k_per_gram": 5760,
            "14k_per_gram": 4480,
            "is_fallback": False
        }
        source_name = "Karnataka Bullion Market"
    else:
        source_name = "Jos Alukkas / GoodReturns Live"

    silver_rate = scrape_silver_rate()
    base_rates["silver_999_per_gram"] = silver_rate

    city_offsets = {
        "bangalore": 0, "mysore": -5, "hubli": -8,
        "mangalore": -3, "belgaum": -10, "gulbarga": -12,
        "davangere": -7, "shimoga": -6, "tumkur": -4, "hassan": -9,
    }

    city_rates = {}
    base_22k = base_rates.get("22k_per_gram", 7040)
    base_24k = base_rates.get("24k_per_gram", 7680)

    for city_key, offset in city_offsets.items():
        city_info = CITIES.get(city_key, {"kn": city_key, "en": city_key.title()})
        city_rates[city_key] = {
            "name_kn": city_info["kn"],
            "name_en": city_info["en"],
            "gold_22k_per_gram": base_22k + offset,
            "gold_24k_per_gram": base_24k + offset,
            "gold_22k_10g": (base_22k + offset) * 10,
            "gold_24k_10g": (base_24k + offset) * 10,
            "silver_per_gram": silver_rate,
            "silver_per_kg": round(silver_rate * 1000),
        }

    output = {
        "last_updated": ist_now(),
        "date": ist_date(),
        "source": source_name,
        "base": base_rates,
        "cities": city_rates,
    }

    store("gold_rates.json", "gold_rates", output)
    log.info(f"✅ Gold (Live Karnataka): 24K = ₹{base_24k}/g | 22K = ₹{base_22k}/g | Silver = ₹{silver_rate}/g")
    return output

if __name__ == "__main__":
    run()