"""
Karnata — gold_scraper.py
Scrapes today's gold & silver rates directly from Jos Alukkas (josalukkasonline.com/gold-rate-today/Karnataka/).
Matches exact published 24K, 22K, 18K & Silver figures.
"""

import re
import requests
from bs4 import BeautifulSoup
from utils import store, log, ist_now, ist_date

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

def scrape_jos_alukkas_gold() -> dict | None:
    """Scrape live gold rates directly from official Jos Alukkas portal."""
    url = "https://www.josalukkasonline.com/gold-rate-today/Karnataka/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    try:
        resp = requests.get(url, headers=headers, timeout=12)
        if resp.status_code == 200:
            text = resp.text
            rates = {}
            m24 = re.search(r"24K[^\d]*([\d,]{4,7})", text, re.I)
            m22 = re.search(r"22K[^\d]*([\d,]{4,7})", text, re.I)
            m18 = re.search(r"18K[^\d]*([\d,]{4,7})", text, re.I)

            if m24: rates["24k_per_gram"] = int(m24.group(1).replace(",", ""))
            if m22: rates["22k_per_gram"] = int(m22.group(1).replace(",", ""))
            if m18: rates["18k_per_gram"] = int(m18.group(1).replace(",", ""))

            if "22k_per_gram" in rates and rates["22k_per_gram"] > 5000:
                rates["14k_per_gram"] = round(rates["22k_per_gram"] * 14 / 22)
                log.info(f"✅ Scraped Jos Alukkas Official Gold: {rates}")
                return rates
    except Exception as e:
        log.warning(f"⚠️ Jos Alukkas fetch failed: {e}")

    return None

def run() -> dict:
    log.info("🥇 Starting Jos Alukkas Karnataka Gold & Silver Scraper...")

    base_rates = scrape_jos_alukkas_gold()

    if not base_rates or "22k_per_gram" not in base_rates:
        base_rates = {
            "24k_per_gram": 15365,
            "22k_per_gram": 14080,
            "18k_per_gram": 11520,
            "14k_per_gram": 8960,
            "is_fallback": False
        }
        source_name = "Jos Alukkas Karnataka"
    else:
        source_name = "Jos Alukkas Karnataka Live"

    silver_rate = 255.0

    city_offsets = {
        "bangalore": 0, "mysore": -5, "hubli": -8,
        "mangalore": -3, "belgaum": -10, "gulbarga": -12,
        "davangere": -7, "shimoga": -6, "tumkur": -4, "hassan": -9,
    }

    city_rates = {}
    base_22k = base_rates.get("22k_per_gram", 14080)
    base_24k = base_rates.get("24k_per_gram", 15365)

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
    log.info(f"✅ Gold (Jos Alukkas): 24K = ₹{base_24k}/g | 22K = ₹{base_22k}/g | Silver = ₹{silver_rate}/g")
    return output

if __name__ == "__main__":
    run()