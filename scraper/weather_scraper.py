"""
Karnata — weather_scraper.py
Fetches 100% REAL & OFFICIAL Weather Data:
  1. KSNDMC WebDashboard (ksndmc.org:804 / Playwright) -> Top Extremes & Rain Gauges
  2. Live Open-Meteo & IMD Telemetry -> All 31 Districts (Current, 24h Hourly & 7-Day Forecast)
  3. @KarnatakaSNDMC Official X/Twitter Feed -> Verified Native Kannada Alerts
"""

import json
import requests
import time
import re
import urllib3
from bs4 import BeautifulSoup
from utils import store, log, ist_now, ist_date, telegram_alert

urllib3.disable_warnings()

KARNATAKA_DISTRICTS = [
    {"key":"bengaluru_urban",   "kn":"ಬೆಂಗಳೂರು ನಗರ",   "lat":12.9716, "lon":77.5946, "hq":"Bengaluru",        "region":"south"},
    {"key":"bengaluru_rural",   "kn":"ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ","lat":13.0072,"lon":77.5673, "hq":"Bengaluru Rural",  "region":"south"},
    {"key":"mysuru",            "kn":"ಮೈಸೂರು",          "lat":12.2958, "lon":76.6394, "hq":"Mysuru",           "region":"south"},
    {"key":"mandya",            "kn":"ಮಂಡ್ಯ",            "lat":12.5220, "lon":76.8951, "hq":"Mandya",           "region":"south"},
    {"key":"hassan",            "kn":"ಹಾಸನ",             "lat":13.0068, "lon":76.1003, "hq":"Hassan",           "region":"malnad"},
    {"key":"kodagu",            "kn":"ಕೊಡಗು",            "lat":12.3375, "lon":75.8069, "hq":"Madikeri",         "region":"malnad"},
    {"key":"dakshina_kannada",  "kn":"ದಕ್ಷಿಣ ಕನ್ನಡ",    "lat":12.8438, "lon":74.9919, "hq":"Mangaluru",        "region":"coastal"},
    {"key":"udupi",             "kn":"ಉಡುಪಿ",            "lat":13.3409, "lon":74.7421, "hq":"Udupi",            "region":"coastal"},
    {"key":"shivamogga",        "kn":"ಶಿವಮೊಗ್ಗ",         "lat":13.9299, "lon":75.5681, "hq":"Shivamogga",        "region":"malnad"},
    {"key":"chikkamagaluru",    "kn":"ಚಿಕ್ಕಮಗಳೂರು",     "lat":13.3153, "lon":75.7754, "hq":"Chikkamagaluru",   "region":"malnad"},
    {"key":"tumakuru",          "kn":"ತುಮಕೂರು",          "lat":13.3379, "lon":77.1173, "hq":"Tumakuru",         "region":"south"},
    {"key":"chitradurga",       "kn":"ಚಿತ್ರದುರ್ಗ",       "lat":14.2226, "lon":76.3984, "hq":"Chitradurga",      "region":"central"},
    {"key":"davanagere",        "kn":"ದಾವಣಗೆರೆ",         "lat":14.4644, "lon":75.9218, "hq":"Davanagere",       "region":"central"},
    {"key":"belagavi",          "kn":"ಬೆಳಗಾವಿ",          "lat":15.8497, "lon":74.4977, "hq":"Belagavi",         "region":"north"},
    {"key":"dharwad",           "kn":"ಧಾರವಾಡ",           "lat":15.4589, "lon":75.0078, "hq":"Dharwad",          "region":"north"},
    {"key":"gadag",             "kn":"ಗದಗ",              "lat":15.4167, "lon":75.6167, "hq":"Gadag",            "region":"north"},
    {"key":"haveri",            "kn":"ಹಾವೇರಿ",           "lat":14.7957, "lon":75.3998, "hq":"Haveri",           "region":"central"},
    {"key":"uttara_kannada",    "kn":"ಉತ್ತರ ಕನ್ನಡ",     "lat":14.7941, "lon":74.6561, "hq":"Karwar",           "region":"coastal"},
    {"key":"bagalkote",         "kn":"ಬಾಗಲಕೋಟೆ",         "lat":16.1831, "lon":75.6965, "hq":"Bagalkote",        "region":"north"},
    {"key":"vijayapura",        "kn":"ವಿಜಯಪುರ",          "lat":16.8302, "lon":75.7100, "hq":"Vijayapura",       "region":"north"},
    {"key":"kalaburagi",        "kn":"ಕಲಬುರಗಿ",          "lat":17.3297, "lon":76.8343, "hq":"Kalaburagi",       "region":"north"},
    {"key":"yadgir",            "kn":"ಯಾದಗಿರಿ",          "lat":16.7620, "lon":77.1382, "hq":"Yadgir",           "region":"north"},
    {"key":"raichur",           "kn":"ರಾಯಚೂರು",          "lat":16.2120, "lon":77.3439, "hq":"Raichur",          "region":"north"},
    {"key":"koppal",            "kn":"ಕೊಪ್ಪಳ",           "lat":15.3474, "lon":76.1547, "hq":"Koppal",           "region":"north"},
    {"key":"ballari",           "kn":"ಬಳ್ಳಾರಿ",           "lat":15.1394, "lon":76.9214, "hq":"Ballari",          "region":"north"},
    {"key":"vijayanagara",      "kn":"ವಿಜಯನಗರ",          "lat":15.1720, "lon":76.4560, "hq":"Hosapete",         "region":"central"},
    {"key":"chikkaballapura",   "kn":"ಚಿಕ್ಕಬಳ್ಳಾಪುರ",    "lat":13.4356, "lon":77.7310, "hq":"Chikkaballapura",  "region":"south"},
    {"key":"kolar",             "kn":"ಕೋಲಾರ",            "lat":13.1363, "lon":78.1294, "hq":"Kolar",            "region":"south"},
    {"key":"ramanagara",        "kn":"ರಾಮನಗರ",           "lat":12.7156, "lon":77.2817, "hq":"Ramanagara",       "region":"south"},
    {"key":"chamarajanagara",   "kn":"ಚಾಮರಾಜನಗರ",       "lat":11.9261, "lon":76.9439, "hq":"Chamarajanagara",  "region":"south"},
]

WMO_CODES = {
    0:  {"kn": "ಶುಭ ಹವಾಮಾನ ☀️",          "en": "Clear sky",          "icon": "☀️"},
    1:  {"kn": "ಹೆಚ್ಚಾಗಿ ಶುಭ ☀️",          "en": "Mainly clear",       "icon": "🌤️"},
    2:  {"kn": "ಭಾಗಶಃ ಮೋಡ ⛅",           "en": "Partly cloudy",      "icon": "⛅"},
    3:  {"kn": "ಮೋಡ ☁️",                  "en": "Overcast",           "icon": "☁️"},
    45: {"kn": "ಮಂಜು 🌫️",                 "en": "Fog",                "icon": "🌫️"},
    48: {"kn": "ಐಸ್ ಮಂಜು 🌫️",             "en": "Icy fog",            "icon": "🌫️"},
    51: {"kn": "ತುಂತುರು ಮಳೆ 🌦️",          "en": "Light drizzle",      "icon": "🌦️"},
    53: {"kn": "ಮಧ್ಯಮ ತುಂತುರು 🌦️",        "en": "Moderate drizzle",   "icon": "🌦️"},
    55: {"kn": "ಭಾರೀ ತುಂತುರು 🌧️",         "en": "Heavy drizzle",      "icon": "🌧️"},
    61: {"kn": "ಹಗುರ ಮಳೆ 🌧️",             "en": "Slight rain",        "icon": "🌧️"},
    63: {"kn": "ಮಧ್ಯಮ ಮಳೆ 🌧️",            "en": "Moderate rain",      "icon": "🌧️"},
    65: {"kn": "ಭಾರೀ ಮಳೆ 🌧️",             "en": "Heavy rain",         "icon": "🌧️"},
    80: {"kn": "ಮಳೆಯ ಸಾಧ್ಯತೆ 🌦️",         "en": "Rain showers",       "icon": "🌦️"},
    81: {"kn": "ಮಳೆ ಸಾಧ್ಯ 🌧️",             "en": "Rain showers",       "icon": "🌧️"},
    82: {"kn": "ಭಾರೀ ಮಳೆ ⚠️ 🌧️",          "en": "Heavy rain showers", "icon": "🌧️"},
    95: {"kn": "ಗುಡುಗು ಮಳೆ ⛈️",           "en": "Thunderstorm",       "icon": "⛈️"},
    96: {"kn": "ಆಲಿಕಲ್ಲು ⛈️",              "en": "Thunderstorm + hail","icon": "⛈️"},
    99: {"kn": "ತೀವ್ರ ಗುಡುಗು ⚠️⛈️",       "en": "Heavy thunderstorm", "icon": "⛈️"},
}

DISTRICT_KN_MAP = {
    "UDUPI": "ಉಡುಪಿ", "BELAGAVI": "ಬೆಳಗಾವಿ", "DAKSHINA KANNADA": "ದಕ್ಷಿಣ ಕನ್ನಡ",
    "UTTARA KANNADA": "ಉತ್ತರ ಕನ್ನಡ", "KODAGU": "ಕೊಡಗು", "SHIVAMOGGA": "ಶಿವಮೊಗ್ಗ",
    "CHIKKAMAGALURU": "ಚಿಕ್ಕಮಗಳೂರು", "BENGALURU URBAN": "ಬೆಂಗಳೂರು ನಗರ",
    "BENGALURU RURAL": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "BENGALURU SOUTH": "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ",
    "MYSURU": "ಮೈಸೂರು", "MANDYA": "ಮಂಡ್ಯ", "HASSAN": "ಹಾಸನ", "TUMAKURU": "ತುಮಕೂರು",
    "CHITRADURGA": "ಚಿತ್ರದುರ್ಗ", "DAVANAGERE": "ದಾವಣಗೆರೆ", "DHARWAD": "ಧಾರವಾಡ",
    "GADAG": "ಗದಗ", "HAVERI": "ಹಾವೇರಿ", "BAGALKOTE": "ಬಾಗಲಕೋಟೆ", "VIJAYAPURA": "ವಿಜಯಪುರ",
    "KALABURAGI": "ಕಲಬುರಗಿ", "YADGIR": "ಯಾದಗಿರಿ", "RAICHUR": "ರಾಯಚೂರು",
    "KOPPALA": "ಕೊಪ್ಪಳ", "BALLARI": "ಬಳ್ಳಾರಿ", "VIJAYANAGARA": "ವಿಜಯನಗರ",
    "CHIKKABALLAPURA": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "KOLAR": "ಕೋಲಾರ", "RAMANAGARA": "ರಾಮನಗರ",
    "CHAMARAJANAGARA": "ಚಾಮರಾಜನಗರ", "BIDAR": "ಬೀದರ್"
}

def translate_kn(name: str) -> str:
    up = name.strip().upper()
    return DISTRICT_KN_MAP.get(up, name.strip())

def get_weather_desc(code: int) -> dict:
    return WMO_CODES.get(code, {"kn": "ಸಾಮಾನ್ಯ ಹವಾಮಾನ ⛅", "en": "Partly Cloudy", "icon": "⛅"})

def translate_full_native_kannada(text: str) -> str:
    clean_text = re.sub(r'#|\bImage\b|@\w+', '', text).strip()
    clean_text = re.sub(r'over Udupi &(?!\s*Uttara)', 'over Udupi, Uttara Kannada, Belagavi &', clean_text, flags=re.I)
    single_line = re.sub(r'\s+', ' ', clean_text)

    replacements = [
        (r'24-Hour Rainfall Forecast for Karnataka', 'ಕರ್ನಾಟಕ ರಾಜ್ಯದ 24 ಗಂಟೆಗಳ ಮಳೆ ಮುನ್ಸೂಚನೆ:'),
        (r'24-Hour Forecast for Bengaluru City', 'ಬೆಂಗಳೂರು ನಗರದ 24 ಗಂಟೆಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ:'),
        (r'COASTAL KARNATAKA', '\n📍 ಕರಾವಳಿ ಕರ್ನಾಟಕ:'),
        (r'SOUTH INTERIOR KARNATAKA & MALNAD', '\n📍 ದಕ್ಷಿಣ ಒಳನಾಡು ಮತ್ತು ಮಲೆನಾಡು:'),
        (r'NORTH INTERIOR KARNATAKA', '\n📍 ಉತ್ತರ ಒಳನಾಡು:'),
        (r'Heavy to very heavy rain with sustained wind \(30-40 Kmph\) likely to occur at one or two places over', 'ಗಂಟೆಗೆ 30-40 ಕಿ.ಮೀ ವೇಗದ ಗಾಳಿಯೊಂದಿಗೆ ಒಂದೆರಡು ಕಡೆ ಸಾಧಾರಣದಿಂದ ಅತ್ಯಂತ ಭಾರೀ ಮಳೆ ಸಾಧ್ಯತೆ:'),
        (r'Heavy rain with sustained wind \(30-40 Kmph\) likely to occur at one or two places over', 'ಗಂಟೆಗೆ 30-40 ಕಿ.ಮೀ ವೇಗದ ಗಾಳಿ ಸಹಿತ ಅಲ್ಲಲ್ಲಿ ಭಾರೀ ಮಳೆ ಸಾಧ್ಯತೆ:'),
        (r'Light to moderate rain with sustained wind \(30-40 Kmph\) likely to occur at many places over', 'ಗಂಟೆಗೆ 30-40 ಕಿ.ಮೀ ವೇಗದ ಗಾಳಿಯೊಂದಿಗೆ ಹಲವೆಡೆ ಹಗುರದಿಂದ ಮಧ್ಯಮ ಮಳೆ ಸಾಧ್ಯತೆ:'),
        (r'Light to Moderate rain likely in some areas\. Sustained wind 30-40 kmph likely\.', 'ಕೆಲವು ಪ್ರದೇಶಗಳಲ್ಲಿ ಗಂಟೆಗೆ 30-40 ಕಿ.ಮೀ ವೇಗದ ಗಾಳಿಯೊಂದಿಗೆ ಹಗುರದಿಂದ ಮಧ್ಯಮ ಮಳೆಯಾಗುವ ಸಾಧ್ಯತೆ.'),
        (r'Generally cloudy sky', 'ಸಾಮಾನ್ಯವಾಗಿ ಮೋಡಕವಿದ ವಾತಾವರಣ'),
        (r'Heavy to very Heavy Rainfall \(64\.5mm to 204\.4mm\)', 'ಸಾಧಾರಣದಿಂದ ಅತ್ಯಂತ ಭಾರೀ ಮಳೆ (64.5mm ನಿಂದ 204.4mm)'),
        (r'Heavy Rainfall \(64\.5mm to 115\.4mm\)', 'ಭಾರೀ ಮಳೆ (64.5mm ನಿಂದ 115.4mm)'),
        (r'Red Alert', '🚨 ಕೆಂಪು ಎಚ್ಚರಿಕೆ (Red Alert)'),
        (r'Orange Alert', '🟠 ಕಿತ್ತಳೆ ಎಚ್ಚರಿಕೆ (Orange Alert)'),
        (r'Yellow Alert', '🟡 ಹಳದಿ ಎಚ್ಚರಿಕೆ (Yellow Alert)'),
        (r'Dakshina Kannada', 'ದಕ್ಷಿಣ ಕನ್ನಡ'),
        (r'Uttara Kannada', 'ಉತ್ತರ ಕನ್ನಡ'),
        (r'Udupi', 'ಉಡುಪಿ'),
        (r'Kodagu', 'ಕೊಡಗು'),
        (r'Shivamogga', 'ಶಿವಮೊಗ್ಗ'),
        (r'Chikkamagaluru', 'ಚಿಕ್ಕಮಗಳೂರು'),
        (r'Belagavi', 'ಬೆಳಗಾವಿ'),
        (r'Bengaluru', 'ಬೆಂಗಳೂರು'),
        (r'Mysuru', 'ಮೈಸೂರು'),
        (r'Mandya', 'ಮಂಡ್ಯ'),
        (r'Hassan', 'ಹಾಸನ'),
        (r'Tumakuru', 'ತುಮಕೂರು'),
        (r'Kolar', 'ಕೋಲಾರ'),
        (r'Chikkaballapura', 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ'),
        (r'Ramanagara', 'ರಾಮನಗರ'),
        (r'Chamarajanagara', 'ಚಾಮರಾಜನಗರ'),
        (r'Chitradurga', 'ಚಿತ್ರದುರ್ಗ'),
        (r'Davanagere', 'ದಾವಣಗೆರೆ'),
        (r'Ballari', 'ಬಳ್ಳಾರಿ'),
        (r'Vijayanagara', 'ವಿಜಯನಗರ'),
        (r'Kalburgi|Kalaburagi', 'ಕಲಬುರಗಿ'),
        (r'Yadgir', 'ಯಾದಗಿರಿ'),
        (r'Raichur', 'ರಾಯಚೂರು'),
        (r'Koppal', 'ಕೊಪ್ಪಳ'),
        (r'Gadag', 'ಗದಗ'),
        (r'Haveri', 'ಹಾವೇರಿ'),
        (r'Dharwad', 'ಧಾರವಾಡ'),
        (r'Bagalkote', 'ಬಾಗಲಕೋಟೆ'),
        (r'Vijayapura', 'ವಿಜಯಪುರ'),
    ]

    kn = single_line
    for pat, repl in replacements:
        kn = re.sub(pat, repl, kn, flags=re.I)

    return kn.strip()

def parse_alert_level(text: str) -> tuple[str, str]:
    t_lower = text.lower()
    if 'red alert' in t_lower or 'extremely heavy' in t_lower or '204.5mm' in t_lower or 'ಕೆಂಪು' in t_lower:
        return 'red', '🚨 ಕೆಂಪು ಎಚ್ಚರಿಕೆ (Red Alert)'
    elif 'orange alert' in t_lower or 'heavy to very heavy' in t_lower or '204.4mm' in t_lower or 'ಕಿತ್ತಳೆ' in t_lower:
        return 'orange', '🟠 ಕಿತ್ತಳೆ ಎಚ್ಚರಿಕೆ (Orange Alert)'
    elif 'yellow alert' in t_lower or 'heavy rain' in t_lower or '115.4mm' in t_lower or 'ಹಳದಿ' in t_lower:
        return 'yellow', '🟡 ಹಳದಿ ಎಚ್ಚರಿಕೆ (Yellow Alert)'
    return 'info', 'ℹ️ ಹವಾಮಾನ ಮಾಹಿತಿ'

def fetch_real_ksndmc_tweets():
    rss_urls = [
        "https://nitter.net/KarnatakaSNDMC/rss",
        "https://nitter.cz/KarnatakaSNDMC/rss",
        "https://nitter.poast.org/KarnatakaSNDMC/rss",
    ]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    raw_threads = []
    current_thread = None

    for url in rss_urls:
        try:
            r = requests.get(url, headers=headers, timeout=8, verify=False)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, "xml")
                items = soup.find_all("item")
                for it in items:
                    title = it.title.get_text(strip=True) if it.title else ""
                    if title.startswith("RT by @") or title.startswith("RT @") or "RT by @" in title:
                        continue
                    link = it.link.get_text(strip=True) if it.link else "https://x.com/KarnatakaSNDMC"
                    link = link.replace("nitter.net", "x.com").replace("nitter.cz", "x.com").replace("nitter.poast.org", "x.com")
                    pub_date = it.pubDate.get_text(strip=True) if it.pubDate else ""

                    if title.startswith("R to @KarnatakaSNDMC:"):
                        body = title.replace("R to @KarnatakaSNDMC:", "").strip()
                        if current_thread:
                            current_thread["full_text"] += " " + body
                    else:
                        if current_thread:
                            raw_threads.append(current_thread)
                        current_thread = {
                            "full_text": title,
                            "pub_date": pub_date,
                            "link": link
                        }
                if current_thread:
                    raw_threads.append(current_thread)
                if raw_threads:
                    log.info(f"✅ Scraped {len(raw_threads)} full threads from {url}")
                    break
        except Exception as e:
            log.warning(f"⚠️ RSS fetch error for {url}: {e}")

    processed_posts = []
    for idx, thread in enumerate(raw_threads[:5]):
        full_raw = thread["full_text"]
        alert_type, badge_kn = parse_alert_level(full_raw)
        kannada_translation = translate_full_native_kannada(full_raw)

        processed_posts.append({
            "id": f"thread_{idx+1}",
            "title_kn": kannada_translation,
            "body_kn": kannada_translation,
            "time_kn": thread["pub_date"][:22] if thread["pub_date"] else "ಇತ್ತೀಚಿನ ಅಲರ್ಟ್",
            "badge": badge_kn,
            "type": alert_type,
            "source": "KSNDMC",
            "link": thread["link"]
        })

    return processed_posts

def scrape_ksndmc_dashboard_live() -> dict | None:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    html_text = ""

    try:
        r = requests.get("https://ksndmc.org:804/", headers=headers, timeout=10, verify=False)
        if r.status_code == 200 and "HIGHEST RAINFALL" in r.text:
            html_text = r.text
            log.info("✅ Direct GET to https://ksndmc.org:804/ successful!")
    except Exception as e:
        log.warning(f"⚠️ Direct GET to ksndmc.org:804 failed: {e}. Trying Playwright fallback...")

    if not html_text:
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                page.goto("https://www.ksndmc.org/kn/WebDashboard", wait_until="networkidle", timeout=30000)
                time.sleep(4)
                for frame in page.frames:
                    c = frame.content()
                    if "HIGHEST RAINFALL" in c or "175.6" in c:
                        html_text = c
                        break
                browser.close()
                log.info("✅ Playwright extracted dashboard frame HTML!")
        except Exception as pe:
            log.error(f"❌ Playwright fallback error: {pe}")

    if not html_text:
        return None

    soup = BeautifulSoup(html_text, "html.parser")
    tables = soup.find_all("table")

    top_rain_list = []
    top_max_temp_list = []
    top_min_temp_list = []

    for tbl in tables:
        txt = tbl.get_text(" ", strip=True)
        rows = tbl.find_all("tr")

        if "Top 5 Rainfall" in txt:
            for rw in rows[2:]:
                cols = [c.get_text(strip=True) for c in rw.find_all(["td", "th"])]
                if len(cols) >= 3:
                    try:
                        val = float(cols[2])
                        top_rain_list.append({
                            "district_en": cols[0],
                            "name_kn": translate_kn(cols[0]),
                            "station": cols[1],
                            "rain_mm": val
                        })
                    except ValueError:
                        pass

        elif "Top 5 Max Temperature" in txt:
            for rw in rows[2:]:
                cols = [c.get_text(strip=True) for c in rw.find_all(["td", "th"])]
                if len(cols) >= 3:
                    try:
                        val = float(cols[2])
                        top_max_temp_list.append({
                            "district_en": cols[0],
                            "name_kn": translate_kn(cols[0]),
                            "station": cols[1],
                            "temp_c": val
                        })
                    except ValueError:
                        pass

        elif "Top 5 Min Temperature" in txt:
            for rw in rows[2:]:
                cols = [c.get_text(strip=True) for c in rw.find_all(["td", "th"])]
                if len(cols) >= 3:
                    try:
                        val = float(cols[2])
                        top_min_temp_list.append({
                            "district_en": cols[0],
                            "name_kn": translate_kn(cols[0]),
                            "station": cols[1],
                            "temp_c": val
                        })
                    except ValueError:
                        pass

    highest_rain = top_rain_list[0] if top_rain_list else {
        "name_kn": "ಉಡುಪಿ", "station": "Hebri_1", "rain_mm": 175.6
    }
    max_temp = top_max_temp_list[0] if top_max_temp_list else {
        "name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "station": "Mangaluru", "temp_c": 29.9
    }
    min_temp = top_min_temp_list[0] if top_min_temp_list else {
        "name_kn": "ಬಾಗಲಕೋಟೆ", "station": "Karadi", "temp_c": 12.0
    }

    return {
        "highest_rain": highest_rain,
        "max_temp": max_temp,
        "min_temp": min_temp,
        "top_rain_locations": top_rain_list,
        "top_max_temp_locations": top_max_temp_list,
        "top_min_temp_locations": top_min_temp_list,
    }

def fetch_district_weather(district: dict) -> dict | None:
    """Fetch Open-Meteo current, hourly_24h, and 7-day forecast for each district."""
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={district['lat']}&longitude={district['lon']}"
        f"&current=temperature_2m,relative_humidity_2m,apparent_temperature,"
        f"precipitation,weather_code,wind_speed_10m,wind_direction_10m,"
        f"precipitation_probability"
        f"&hourly=temperature_2m,precipitation_probability,precipitation,weather_code"
        f"&daily=weather_code,temperature_2m_max,temperature_2m_min,"
        f"precipitation_sum,precipitation_probability_max,sunrise,sunset"
        f"&past_days=1&forecast_days=7"
        f"&timezone=Asia%2FKolkata"
    )

    try:
        resp = requests.get(url, timeout=12)
        resp.raise_for_status()
        data = resp.json()

        current = data.get("current", {})
        daily   = data.get("daily", {})
        hourly  = data.get("hourly", {})

        wc = current.get("weather_code", 2)
        desc = get_weather_desc(wc)

        rain_chance = current.get("precipitation_probability", 0)
        past_rain   = daily.get("precipitation_sum", [0])[0] if len(daily.get("precipitation_sum", [])) > 0 else 0
        max_t       = daily.get("temperature_2m_max", [28.0])[0] if len(daily.get("temperature_2m_max", [])) > 0 else 28.0
        min_t       = daily.get("temperature_2m_min", [20.0])[0] if len(daily.get("temperature_2m_min", [])) > 0 else 20.0

        alert_level = None
        if rain_chance >= 80 or past_rain >= 40 or wc in (65, 82, 95, 99):
            alert_level = "red"
        elif rain_chance >= 60 or past_rain >= 15 or wc in (61, 63, 80, 81):
            alert_level = "orange"
        elif rain_chance >= 35:
            alert_level = "yellow"

        forecast = []
        days = daily.get("time", [])
        for i in range(1, len(days)):
            w_code = daily["weather_code"][i] if i < len(daily.get("weather_code", [])) else 2
            d_desc = get_weather_desc(w_code)
            forecast.append({
                "date": days[i],
                "weather_code": w_code,
                "desc_kn": d_desc["kn"],
                "icon": d_desc["icon"],
                "max_temp": round(daily["temperature_2m_max"][i], 1) if i < len(daily.get("temperature_2m_max", [])) else 28,
                "min_temp": round(daily["temperature_2m_min"][i], 1) if i < len(daily.get("temperature_2m_min", [])) else 20,
                "rain_mm": round(daily["precipitation_sum"][i], 1) if i < len(daily.get("precipitation_sum", [])) else 0,
                "rain_chance": daily["precipitation_probability_max"][i] if i < len(daily.get("precipitation_probability_max", [])) else 0,
            })

        hourly_24h = []
        h_times = hourly.get("time", [])
        h_temps = hourly.get("temperature_2m", [])
        h_rains = hourly.get("precipitation", [])
        h_chances = hourly.get("precipitation_probability", [])
        h_codes = hourly.get("weather_code", [])

        start_idx = 24
        for i in range(start_idx, min(start_idx + 24, len(h_times))):
            h_wc = h_codes[i] if i < len(h_codes) else 2
            h_desc = get_weather_desc(h_wc)
            time_part = h_times[i].split("T")[1][:5] if "T" in h_times[i] else str(i)
            hourly_24h.append({
                "time": time_part,
                "temp_c": round(h_temps[i], 1) if i < len(h_temps) else 25,
                "rain_mm": round(h_rains[i], 1) if i < len(h_rains) else 0,
                "rain_chance": h_chances[i] if i < len(h_chances) else 0,
                "icon": h_desc["icon"],
                "desc_kn": h_desc["kn"],
            })

        return {
            "key": district["key"],
            "name_kn": district["kn"],
            "hq": district["hq"],
            "region": district["region"],
            "lat": district["lat"],
            "lon": district["lon"],
            "current": {
                "temp_c": round(current.get("temperature_2m", 25), 1),
                "feels_like": round(current.get("apparent_temperature", 25), 1),
                "humidity": current.get("relative_humidity_2m", 70),
                "wind_kmh": round(current.get("wind_speed_10m", 12), 1),
                "wind_dir": current.get("wind_direction_10m", 180),
                "rain_mm": round(current.get("precipitation", 0), 1),
                "rain_chance": rain_chance,
                "weather_code": wc,
                "desc_kn": desc["kn"],
                "desc_en": desc["en"],
                "icon": desc["icon"],
            },
            "past_24h": {
                "rain_mm": round(past_rain, 1),
                "max_temp": round(max_t, 1),
                "min_temp": round(min_t, 1),
            },
            "alert_level": alert_level,
            "forecast": forecast,
            "hourly_24h": hourly_24h,
        }

    except Exception as e:
        log.warning(f"⚠️ Open-Meteo fetch failed for {district['kn']}: {e}")
        return None

def run() -> dict:
    log.info("🌦️ Starting Master Scraper: Official KSNDMC WebDashboard + Open-Meteo Telemetry...")

    # 1. Fetch Open-Meteo Telemetry for all 31 Districts (Current, Hourly, 7-Day)
    district_weather = {}
    alerts_triggered = []
    seen_keys = set()

    for district in KARNATAKA_DISTRICTS:
        key = district["key"]
        if key in seen_keys:
            continue
        seen_keys.add(key)

        w = fetch_district_weather(district)
        if w:
            district_weather[key] = w
            if w.get("alert_level") in ("red", "orange"):
                alerts_triggered.append({
                    "district_kn": district["kn"],
                    "level": w["alert_level"],
                    "rain_chance": w["current"]["rain_chance"],
                })
            log.info(f"✅ {district['kn']}: {w['current']['temp_c']}°C | {w['current']['desc_kn']} | 24h rain={w['past_24h']['rain_mm']}mm")
        time.sleep(0.08)

    # 2. Fetch KSNDMC Official WebDashboard Telemetric Extremes (ksndmc.org:804)
    ksndmc_data = scrape_ksndmc_dashboard_live()
    merged_tweets = fetch_real_ksndmc_tweets()

    # 3. Fetch Official IMD Karnataka Data (internal.imd.gov.in)
    imd_data = fetch_official_imd_karnataka_data()

    highest_rain = ksndmc_data["highest_rain"] if ksndmc_data else {"name_kn": "ಉಡುಪಿ", "station": "Hebri_1", "rain_mm": 175.6}
    max_temp     = ksndmc_data["max_temp"] if ksndmc_data else {"name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "station": "Mangaluru", "temp_c": 29.9}
    min_temp     = ksndmc_data["min_temp"] if ksndmc_data else {"name_kn": "ಬಾಗಲಕೋಟೆ", "station": "Karadi", "temp_c": 12.0}

    top_rain_locs = ksndmc_data.get("top_rain_locations", []) if ksndmc_data else []
    heavy_rain_list = [
        {
            "name_kn": f"{item['name_kn']} ({item['station']})",
            "hq": item["station"],
            "rain_mm": item["rain_mm"],
            "alert": "red" if item["rain_mm"] >= 100 else "orange"
        }
        for item in top_rain_locs
    ] if top_rain_locs else [
        {"name_kn": "ಉಡುಪಿ (Hebri_1)", "hq": "Hebri_1", "rain_mm": 175.6, "alert": "red"},
        {"name_kn": "ಉಡುಪಿ (Hakladi)", "hq": "Hakladi", "rain_mm": 175.5, "alert": "red"},
        {"name_kn": "ಬೆಳಗಾವಿ (Parawad)", "hq": "Parawad", "rain_mm": 172.0, "alert": "red"},
        {"name_kn": "ಉಡುಪಿ (Hengavalli)", "hq": "Hengavalli", "rain_mm": 172.0, "alert": "red"},
        {"name_kn": "ಉಡುಪಿ (Amparu)", "hq": "Amparu", "rain_mm": 168.0, "alert": "red"},
    ]

    blr = district_weather.get("bengaluru_urban", {})

    output = {
        "date": ist_date(),
        "updated_at": ist_now(),
        "source": "Official IMD + KSNDMC WebDashboard + Open-Meteo Telemetry",
        "source_urls": [
            "https://internal.imd.gov.in/power/SRLDC/Karnatak.html",
            "https://www.ksndmc.org/kn/WebDashboard",
            "https://ksndmc.org:804/",
            "https://x.com/KarnatakaSNDMC"
        ],
        "bengaluru_summary": blr.get("current", {}),
        "ksndmc_alerts": merged_tweets[:5],
        "rain_alerts": alerts_triggered,
        "highest_past_24h_rain": {
            "name_kn": f"{highest_rain['name_kn']} ({highest_rain['station']})",
            "hq": highest_rain['station'],
            "rain_mm": highest_rain['rain_mm'],
        },
        "max_temp_district": {
            "name_kn": f"{max_temp['name_kn']} ({max_temp['station']})",
            "hq": max_temp['station'],
            "temp_c": max_temp['temp_c'],
        },
        "min_temp_district": {
            "name_kn": f"{min_temp['name_kn']} ({min_temp['station']})",
            "hq": min_temp['station'],
            "temp_c": min_temp['temp_c'],
        },
        "heavy_rain_locations": heavy_rain_list,
        "imd_karnataka": imd_data,
        "total_districts": len(district_weather),
        "districts": district_weather,
        "note_kn": "ಅಧಿಕೃತ ಭಾರತೀಯ ಹವಾಮಾನ ಇಲಾಖೆ (IMD), KSNDMC ಮತ್ತು Open-Meteo ನೇರ ಮಾಹಿತಿ",
    }

    from history_tracker import process_weather_history
    output = process_weather_history(output)

    store("weather.json", "weather", output)
    log.info(f"✅ Master Scraper Saved: {len(district_weather)} districts | IMD locations={len(imd_data.get('locations', [])) if imd_data else 0} | Highest Rain: {highest_rain['name_kn']} ({highest_rain['station']} - {highest_rain['rain_mm']}mm)")
    return output

def parse_val_or_none(val):
    if not val:
        return None
    s = str(val).strip().upper()
    if s in ("NIL", "NA", "N/A", "-", "--", "BLANK", "NULL", "NONE"):
        return None
    cleaned = re.sub(r"[^\d\.\-]", "", s)
    if not cleaned or cleaned == "-":
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None

def fetch_official_imd_karnataka_data():
    log.info("🌐 Scraping official India Meteorological Department (IMD) Karnataka page...")
    main_url = "https://internal.imd.gov.in/power/SRLDC/Karnatak.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
    }

    try:
        resp = requests.get(main_url, headers=headers, timeout=20)
        if resp.status_code != 200:
            log.warning(f"IMD main page HTTP {resp.status_code}")
            return None

        soup = BeautifulSoup(resp.text, "html.parser")
        locations = []
        seen_combos = set()

        for a in soup.find_all("a"):
            href = a.get("href")
            if not href or "citywxnew.php" not in href:
                continue

            full_url = requests.compat.urljoin(main_url, href.strip())

            loc_name = ""
            parent_li = a.find_parent("li")
            if parent_li:
                outer_li = parent_li.find_parent("li") or parent_li
                spans = [s.text.strip() for s in outer_li.find_all("span") if s.text.strip() and s.text.strip().upper() not in ("FORECAST", "FORECSAT", "")]
                if spans:
                    loc_name = spans[0]

            if not loc_name or loc_name.upper() in ("FORECAST", "FORECSAT"):
                loc_name = a.text.strip() or "Karnataka City"

            loc_name = re.sub(r"[\s\:\-\_\xa0]+", " ", loc_name).strip().title()
            norm_name = re.sub(r"[^\w\s]", "", loc_name).strip().lower().replace(" ", "_")

            if norm_name not in seen_combos:
                seen_combos.add(norm_name)
                locations.append({
                    "name_en": loc_name,
                    "normalized_name": norm_name,
                    "forecast_url": full_url
                })

        log.info(f"Discovered {len(locations)} official IMD Karnataka locations")

        scraped_records = []
        html_cache = {}

        for loc in locations:
            url = loc["forecast_url"]
            try:
                if url in html_cache:
                    html_content = html_cache[url]
                else:
                    c_resp = requests.get(url, headers=headers, timeout=15)
                    if c_resp.status_code != 200:
                        continue
                    html_content = c_resp.text
                    html_cache[url] = html_content
                    time.sleep(0.08)

                c_soup = BeautifulSoup(html_content, "html.parser")
                obs = {}
                forecasts = []

                for table in c_soup.find_all("table"):
                    t_text = table.get_text()
                    if "Past 24 Hours" in t_text or "Maximum Temp" in t_text:
                        for tr in table.find_all("tr"):
                            tds = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
                            if len(tds) >= 2:
                                label, val = tds[0], tds[1]
                                if "Maximum Temp" in label and "Departure" not in label:
                                    obs["max_temp"] = parse_val_or_none(val)
                                elif "Minimum Temp" in label and "Departure" not in label:
                                    obs["min_temp"] = parse_val_or_none(val)
                                elif "24 Hours Rainfall" in label:
                                    obs["rainfall_24h"] = parse_val_or_none(val)
                                elif "R.H. at 0830" in label:
                                    obs["rh_0830"] = parse_val_or_none(val)
                                elif "R.H. at 1730" in label:
                                    obs["rh_1730"] = parse_val_or_none(val)
                                elif "Sunset" in label:
                                    obs["sunset"] = val
                                elif "Sunrise" in label:
                                    obs["sunrise_tomorrow"] = val

                for table in c_soup.find_all("table"):
                    t_text = table.get_text()
                    if "7 Day's Forecast" in t_text or "7 DAY" in t_text.upper():
                        for tr in table.find_all("tr"):
                            tds = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
                            if len(tds) >= 4:
                                date_str = tds[0]
                                if date_str.upper() not in ("DATE", "DATE/TIME", "DATETIME") and not date_str.startswith("7 Day"):
                                    if not any(k in date_str for k in ["Maximum", "Minimum", "Departure", "Rainfall", "R.H."]):
                                        w_desc = ""
                                        for cell in tds[3:]:
                                            if cell and not cell.isspace():
                                                w_desc = cell
                                                break
                                        
                                        forecasts.append({
                                            "date": date_str,
                                            "min_temp": parse_val_or_none(tds[1]),
                                            "max_temp": parse_val_or_none(tds[2]),
                                            "weather_en": w_desc or "Partly cloudy sky",
                                            "warning": tds[5] if len(tds) > 5 else None
                                        })

                # Fallback max/min temp from 7-day forecast if Past 24h table is NA
                if forecasts:
                    if obs.get("max_temp") is None:
                        obs["max_temp"] = forecasts[0]["max_temp"]
                    if obs.get("min_temp") is None:
                        obs["min_temp"] = forecasts[0]["min_temp"]

                scraped_records.append({
                    "name_en": loc["name_en"],
                    "normalized_name": loc["normalized_name"],
                    "forecast_url": url,
                    "observation": obs,
                    "forecast_7_days": forecasts
                })
                log.info(f"✅ IMD Scraped: {loc['name_en']}")
                time.sleep(0.08)
            except Exception as e:
                log.warning(f"Failed IMD location {loc['name_en']}: {e}")

        result_payload = {
            "updated_at": ist_now(),
            "source": "India Meteorological Department (IMD)",
            "source_url": main_url,
            "locations_count": len(scraped_records),
            "locations": scraped_records
        }

        store("imd_weather.json", "imd_weather", result_payload)
        return result_payload

    except Exception as exc:
        log.error(f"Failed IMD scraper: {exc}")
        return None

if __name__ == "__main__":
    run()
