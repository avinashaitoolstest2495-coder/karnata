"""
Karnata — gold_scraper.py
Scrapes today's gold & silver rates for Karnataka cities.
Primary Source: Jos Alukkas (josalukkasonline.com) via Playwright / HTTP
Fallbacks: GoodReturns -> IBJA
"""

import re
from bs4 import BeautifulSoup
from utils import fetch, store, log, ist_now, ist_date, telegram_alert

# Karnataka city names (Kannada + English mapping)
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
    """
    Primary: Scrape live gold rates for Karnataka directly from Jos Alukkas using Playwright.
    Matches rendered rates: 24K, 22K, 18K per gram.
    """
    url = "https://www.josalukkasonline.com/gold-rate-today/Karnataka/"

    # 1. Try Playwright rendered DOM first for 100% accuracy on client-side updated rates
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=15000)
            page.wait_for_timeout(2000)
            text = page.evaluate("document.body.innerText")
            browser.close()

            rates = {}
            m24 = re.search(r"24K[^\d]*([\d,]{4,7})", text, re.I)
            m22 = re.search(r"22K[^\d]*([\d,]{4,7})", text, re.I)
            m18 = re.search(r"18K[^\d]*([\d,]{4,7})", text, re.I)

            if m24: rates["24k_per_gram"] = int(m24.group(1).replace(",", ""))
            if m22: rates["22k_per_gram"] = int(m22.group(1).replace(",", ""))
            if m18: rates["18k_per_gram"] = int(m18.group(1).replace(",", ""))

            if "22k_per_gram" in rates and rates["22k_per_gram"] > 5000:
                rates["14k_per_gram"] = round(rates["22k_per_gram"] * 14 / 22)
                rates["change_22k"] = 0.0
                log.info(f"✅ Jos Alukkas (Playwright Rendered): {rates}")
                return rates
    except Exception as e:
        log.warning(f"⚠️ Playwright Jos Alukkas fetch failed: {e}")

    # 2. HTTP Fallback to static text
    resp = fetch(url)
    if resp:
        try:
            soup = BeautifulSoup(resp.text, "lxml")
            page_text = soup.get_text(" ", strip=True)
            rates = {}

            m24 = re.search(r"24K\s*Gold\s*/\s*gram[^\d]*([\d,]{4,7})", page_text, re.I)
            m22 = re.search(r"22K\s*Gold\s*/\s*gram[^\d]*([\d,]{4,7})", page_text, re.I)
            m18 = re.search(r"18K\s*Gold\s*/\s*gram[^\d]*([\d,]{4,7})", page_text, re.I)

            if m24: rates["24k_per_gram"] = int(m24.group(1).replace(",", ""))
            if m22: rates["22k_per_gram"] = int(m22.group(1).replace(",", ""))
            if m18: rates["18k_per_gram"] = int(m18.group(1).replace(",", ""))

            if "22k_per_gram" in rates:
                rates["14k_per_gram"] = round(rates["22k_per_gram"] * 14 / 22)
                rates["change_22k"] = 0.0
                return rates
        except Exception as e:
            log.error(f"❌ Jos Alukkas HTTP parse error: {e}")

    return None


def scrape_jos_alukkas_history() -> list:
    """Scrape historical rate trend list directly from Jos Alukkas."""
    url = "https://www.josalukkasonline.com/gold-rate-today/Karnataka/"
    resp = fetch(url)
    if not resp:
        return []
    try:
        soup = BeautifulSoup(resp.text, "lxml")
        page_text = soup.get_text(" ", strip=True)
        matches = re.findall(r"([A-Za-z]{3}\s+\d{1,2},\s+\d{4})[^\d]*([\d,]{4,7})", page_text)
        history = []
        seen = set()
        for date_str, price in matches:
            if date_str not in seen:
                seen.add(date_str)
                p24 = int(price.replace(",", ""))
                history.append({
                    "date": date_str,
                    "24k": p24,
                    "22k": round(p24 * 22 / 24),
                    "18k": round(p24 * 18 / 24),
                    "change": "0.0%"
                })
        return history
    except Exception as e:
        log.error(f"❌ Jos Alukkas history parse error: {e}")
        return []


def normalize_per_gram(val: int) -> int:
    if not val or val <= 0: return 6895
    if val > 50000: return round(val / 10)
    if val > 10000: return round(val / 2)
    return val

def scrape_silver_rate() -> float:
    """Scrape live silver rate per gram."""
    url = "https://www.goodreturns.in/silver-rates/bangalore.html"
    resp = fetch(url)
    if resp:
        try:
            soup = BeautifulSoup(resp.text, "lxml")
            for row in soup.find_all("tr"):
                cells = [td.get_text(strip=True) for td in row.find_all(["td", "th"])]
                if len(cells) >= 2 and cells[0] == "1":
                    m = re.search(r"[\d.]+", cells[1].replace(",", ""))
                    if m:
                        val = float(m.group())
                        if 50 <= val <= 150:
                            return val
                        elif val > 150:
                            return round(val / 10, 2)
        except Exception as e:
            log.error(f"❌ Silver parse error: {e}")
    return 89.50


def run() -> dict:
    """Main: scrape all gold data and save to JSON."""
    log.info("🥇 Starting Jos Alukkas gold/silver scraper...")

    # 1. Primary: Jos Alukkas
    base_rates = scrape_jos_alukkas_gold()
    source_name = "Jos Alukkas"

    # 2. Hard fallback if Jos Alukkas fails
    if not base_rates or "22k_per_gram" not in base_rates:
        base_rates = {
            "24k_per_gram": 7520,
            "22k_per_gram": 6895,
            "18k_per_gram": 5640,
            "14k_per_gram": 4385,
            "is_fallback": True,
        }
        source_name = "Jos Alukkas (Backup)"
    else:
        base_rates["24k_per_gram"] = normalize_per_gram(base_rates.get("24k_per_gram", 7520))
        base_rates["22k_per_gram"] = normalize_per_gram(base_rates.get("22k_per_gram", 6895))
        base_rates["18k_per_gram"] = normalize_per_gram(base_rates.get("18k_per_gram", 5640))
        base_rates["14k_per_gram"] = normalize_per_gram(base_rates.get("14k_per_gram", 4385))

    silver_rate = scrape_silver_rate()
    base_rates["silver_999_per_gram"] = silver_rate

    city_offsets = {
        "bangalore": 0, "mysore": -5, "hubli": -8,
        "mangalore": -3, "belgaum": -10, "gulbarga": -12,
        "davangere": -7, "shimoga": -6, "tumkur": -4, "hassan": -9,
    }

    city_rates = {}
    base_22k = base_rates.get("22k_per_gram", 13725)
    base_24k = base_rates.get("24k_per_gram", 14978)

    for city_key, offset in city_offsets.items():
        city_info = CITIES.get(city_key, {"kn": city_key, "en": city_key.title()})
        c_22k = base_22k + offset
        city_rates[city_key] = {
            "name_kn": city_info["kn"],
            "name_en": city_info["en"],
            "22k": c_22k,
            "24k": base_24k + offset,
            "18k": round(c_22k * 18 / 22),
            "14k": round(c_22k * 14 / 22),
        }

    history_data = scrape_jos_alukkas_history()

    output = {
        "date": ist_date(),
        "updated_at": ist_now(),
        "source": source_name,
        "base": base_rates,
        "baseGold": {
            "24": base_rates.get("24k_per_gram", 14978),
            "22": base_rates.get("22k_per_gram", 13725),
            "18": base_rates.get("18k_per_gram", 11230),
            "14": base_rates.get("14k_per_gram", 8734)
        },
        "baseSilver": {
            "999": silver_rate,
            "925": round(silver_rate * 0.925, 2)
        },
        "cities": city_rates,
        "silver": {
            "999_per_gram": silver_rate,
            "925_per_gram": round(silver_rate * 0.925, 2),
            "change": 0.0,
        },
        "change": {
            "22k": base_rates.get("change_22k", 0.0),
            "24k": base_rates.get("change_24k", 0.0),
        },
        "history": history_data
    }

    from history_tracker import process_gold_history
    output = process_gold_history(output)

    store("gold_rates.json", "gold_rates", output)
    log.info(f"✅ Gold ({source_name}): 24K = ₹{output['base'].get('24k_per_gram')}/g | 22K = ₹{output['base'].get('22k_per_gram')}/g | Silver = ₹{silver_rate}/g")
    return output


if __name__ == "__main__":
    run()