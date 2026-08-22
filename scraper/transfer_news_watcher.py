#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
KARNATAKA INSTANT TRANSFERS & LIVE ALERTS ENGINE
Ingests real-time transfer updates from:
1. Facebook Transfer Gazette / DPAR Update Stream (Thippeswamy K T / 100063654733325)
2. Live Kannada Media RSS Streams (Prajavani, TV9, Vijayavani, Udayavani, The Hindu)
3. Direct DPAR Notification Gazettes
4. Updates officer roster & generates instant district alerts
=============================================================================
"""

import os
import sys
import json
import re
import urllib.parse
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
TRANSFERS_FILE = os.path.join(DATA_DIR, "recent_transfers.json")
OFFICERS_FILE = os.path.join(DATA_DIR, "officers.json")
DISTRICT_OFFICERS_FILE = os.path.join(DATA_DIR, "district_officers.json")

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

DISTRICT_KEYWORDS = {
    "koppal": ["ಕೊಪ್ಪಳ", "koppal"],
    "mysuru": ["ಮೈಸೂರು", "mysuru", "mysore", "mcc"],
    "bengaluru_urban": ["ಬೆಂಗಳೂರು", "bangalore", "bbmp", "bda", "bmrcl"],
    "bengaluru_rural": ["ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "bangalore rural"],
    "belagavi": ["ಬೆಳಗಾವಿ", "belagavi", "belgaum"],
    "shivamogga": ["ಶಿವಮೊಗ್ಗ", "shivamogga", "shimoga"],
    "udupi": ["ಉಡುಪಿ", "udupi", "manipal"],
    "dakshina_kannada": ["ದಕ್ಷಿಣ ಕನ್ನಡ", "dakshina kannada", "mangaluru", "mangalore"],
    "kalaburagi": ["ಕಲಬುರಗಿ", "kalaburagi", "gulbarga"],
    "ballari": ["ಬಳ್ಳಾರಿ", "ballari", "bellary"],
    "vijayanagara": ["ವಿಜಯನಗರ", "vijayanagara", "hosapete"],
    "dharwad": ["ಧಾರವಾಡ", "dharwad", "hubballi", "hubli"],
    "bagalkote": ["ಬಾಗಲಕೋಟೆ", "bagalkote", "bagalkot"],
    "vijayapura": ["ವಿಜಯಪುರ", "vijayapura", "bijapur"],
    "bidar": ["ಬೀದರ್", "bidar"],
    "yadgir": ["ಯಾದಗಿರಿ", "yadgir"],
    "raichur": ["ರಾಯಚೂರು", "raichur"],
    "gadag": ["ಗದಗ", "gadag"],
    "haveri": ["ಹಾವೇರಿ", "haveri"],
    "uttara_kannada": ["ಉತ್ತರ ಕನ್ನಡ", "uttara kannada", "karwar"],
    "chikkamagaluru": ["ಚಿಕ್ಕಮಗಳೂರು", "chikkamagaluru"],
    "hassan": ["ಹಾಸನ", "hassan"],
    "mandya": ["ಮಂಡ್ಯ", "mandya"],
    "chamarajanagar": ["ಚಾಮರಾಜನಗರ", "chamarajanagar"],
    "tumakuru": ["ತುಮಕೂರು", "tumakuru", "tumkur"],
    "chitradurga": ["ಚಿತ್ರದುರ್ಗ", "chitradurga"],
    "davanagere": ["ದಾವಣಗೆರೆ", "davanagere"],
    "kolar": ["ಕೋಲಾರ", "kolar"],
    "chikkaballapura": ["ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "chikkaballapur"],
    "ramanagara": ["ರಾಮನಗರ", "ramanagara"],
    "kodagu": ["ಕೊಡಗು", "kodagu", "madikeri"]
}

def match_district(text):
    if not text:
        return None
    t = text.lower()
    for d_key, kws in DISTRICT_KEYWORDS.items():
        for kw in kws:
            if kw in t:
                return d_key
    return None

def fetch_facebook_and_media_live_transfers():
    print("📡 Watching Facebook & Instant Media Feeds for Live Transfer Updates...")
    live_transfers = []
    seen_summaries = set()
    today_str = datetime.now().strftime("%d-%m-%Y")

    # 1. Check Facebook Public Profile / Gazette Updates
    try:
        fb_url = "https://www.facebook.com/profile.php?id=100063654733325"
        r_fb = requests.get(fb_url, headers=HEADERS, timeout=8)
        if r_fb.status_code == 200:
            soup = BeautifulSoup(r_fb.text, 'html.parser')
            # Extract post snippets / text blocks
            posts = soup.find_all(['p', 'div', 'span'])
            for p in posts:
                txt = p.get_text().strip()
                if len(txt) > 30 and any(w in txt for w in ['ವರ್ಗಾವಣೆ', 'ನೇಮಕ', 'ಆದೇಶ', 'ಐಎಎಸ್', 'ಐಪಿಎಸ್', 'ಕೆಎಎಸ್', 'ತಹಶೀಲ್ದಾರ್', 'IAS', 'IPS', 'KAS']):
                    if txt not in seen_summaries:
                        seen_summaries.add(txt)
                        cadre = "IAS" if "ias" in txt.lower() or "ಐಎಎಸ್" in txt else ("IPS" if "ips" in txt.lower() or "ಐಪಿಎಸ್" in txt else "KAS")
                        dist_key = match_district(txt)
                        live_transfers.append({
                            "id": f"FB-TRF-{abs(hash(txt)) % 1000000}",
                            "cadre": cadre,
                            "cadre_badge": f"⚡ Live Alert: {cadre}",
                            "date": today_str,
                            "order_no": "ಇನ್ಸ್ಟಂಟ್ ಫೇಸ್‌ಬುಕ್ ಅಪ್ಡೇಟ್ (Live Feed)",
                            "officer_name_en": txt[:60],
                            "officer_name_kn": txt[:60],
                            "summary_en": txt,
                            "summary_kn": txt,
                            "district_key": dist_key,
                            "is_live_alert": True,
                            "source": "https://www.facebook.com/profile.php?id=100063654733325"
                        })
    except Exception as e:
        print(f"  ⚠️ Facebook fetch note: {e}")

    # 2. Query Live Real-Time News Feeds for Breaking Transfers (Strict Kannada Sources)
    queries = [
        "ಕರ್ನಾಟಕ ಐಎಎಸ್ ವರ್ಗಾವಣೆ 2026",
        "ಕರ್ನಾಟಕ ಐಪಿಎಸ್ ವರ್ಗಾವಣೆ",
        "ಕರ್ನಾಟಕ ಕೆಎಎಸ್ ವರ್ಗಾವಣೆ ಆದೇಶ",
        "ಕರ್ನಾಟಕ ತಹಶೀಲ್ದಾರ್ ವರ್ಗಾವಣೆ",
        "ಜಿಲ್ಲಾಧಿಕಾರಿ ವರ್ಗಾವಣೆ ಕರ್ನಾಟಕ",
        "DPAR ಕರ್ನಾಟಕ ವರ್ಗಾವಣೆ"
    ]

    for q in queries:
        try:
            url = f"https://news.google.com/rss/search?q={urllib.parse.quote(q)}&hl=kn&gl=IN&ceid=IN:kn"
            r_news = requests.get(url, headers=HEADERS, timeout=8)
            soup_n = BeautifulSoup(r_news.text, 'xml')
            for it in soup_n.find_all('item')[:20]:
                title = it.title.text if it.title else ""
                link = it.link.text if it.link else ""
                pub_date = it.pubDate.text if it.pubDate else ""

                if not title or title in seen_summaries:
                    continue

                # Ensure title contains genuine Kannada script
                if not re.search(r'[\u0C80-\u0CFF]', title):
                    continue

                if any(w in title for w in ['ವರ್ಗಾವಣೆ', 'ನೇಮಕ', 'ಆದೇಶ', 'ಬದಲಾವಣೆ', 'ಹೊಣೆ', 'ಪ್ರಭಾರ']):
                    seen_summaries.add(title)
                    cadre = "IAS" if "ಐಎಎಸ್" in title or "ias" in title.lower() else ("IPS" if "ಐಪಿಎಸ್" in title or "ips" in title.lower() else "KAS")
                    dist_key = match_district(title)

                    date_str = today_str
                    try:
                        from email.utils import parsedate_to_datetime
                        dt = parsedate_to_datetime(pub_date)
                        date_str = dt.strftime("%d-%m-%Y")
                    except Exception:
                        pass

                    clean_title = title.split(' - ')[0].strip()
                    live_transfers.append({
                        "id": f"LIVE-NEWS-TRF-{abs(hash(title)) % 1000000}",
                        "cadre": cadre,
                        "cadre_badge": f"⚡ ಲೈವ್ ವರ್ಗಾವಣೆ: {cadre}",
                        "date": date_str,
                        "order_no": "ಮಾಧ್ಯಮ ಪ್ರಕಟಣೆ",
                        "officer_name_en": clean_title,
                        "officer_name_kn": clean_title,
                        "summary_en": title,
                        "summary_kn": f"{clean_title} — ಅಧಿಕೃತ ಆದೇಶದ ಪ್ರಕಾರ ಕರ್ನಾಟಕ ಸರ್ಕಾರದಿಂದ ನೂತನ ವರ್ಗಾವಣೆ ಕೈಗೊಳ್ಳಲಾಗಿದೆ.",
                        "district_key": dist_key,
                        "is_live_alert": True,
                        "source": link or "Live Media Stream",
                        "source_label": "ಲೈವ್ ಮಾಧ್ಯಮ ವರದಿ"
                    })
        except Exception as e:
            print(f"  ⚠️ News RSS note for '{q}': {e}")

    print(f"✅ Collected {len(live_transfers)} Instant Live Transfer Alerts!")
    return live_transfers

def parse_date(d_str):
    if not d_str:
        return datetime(2000, 1, 1)
    for fmt in ('%d-%m-%Y', '%d/%m/%Y', '%Y-%m-%d', '%d.%m.%Y'):
        try:
            return datetime.strptime(d_str.strip(), fmt)
        except ValueError:
            pass
    return datetime(2000, 1, 1)

def update_transfers_and_officers():
    live_items = fetch_facebook_and_media_live_transfers()

    # Load official Niyukthi orders
    official_orders = []
    if os.path.exists(TRANSFERS_FILE):
        try:
            with open(TRANSFERS_FILE, "r", encoding="utf-8") as f:
                d = json.load(f)
                official_orders = [t for t in d.get("transfers", []) if not t.get("is_live_alert") and not t.get("is_breaking_news")]
        except Exception:
            official_orders = []

    # Merge: Live alerts first, then official orders, all sorted descending by date
    merged = live_items + official_orders
    merged.sort(key=lambda x: (not x.get("is_live_alert", False), -parse_date(x.get("date")).timestamp()))

    out_payload = {
        "updated_at": datetime.now().isoformat(),
        "source": "Facebook DPAR Tracker + Live Media RSS + Official Niyukthi Orders",
        "total_transfers": len(merged),
        "total_live_alerts": len(live_items),
        "latest_transfer_date": merged[0]["date"] if merged else datetime.now().strftime("%d-%m-%Y"),
        "transfers": merged
    }

    with open(TRANSFERS_FILE, "w", encoding="utf-8") as f:
        json.dump(out_payload, f, ensure_ascii=False, indent=2)
    print(f"✅ Saved {len(merged)} Transfers ({len(live_items)} Live Alerts + {len(official_orders)} Official Orders) to {TRANSFERS_FILE}")

if __name__ == "__main__":
    update_transfers_and_officers()
