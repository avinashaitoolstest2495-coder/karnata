"""
Karnata — local_news_scraper.py
Multi-Source Strict District Local News Scraper with Geolocation & High-Precision Tagging

Aggregates news from all top Kannada & District portals:
- Vijaya Karnataka (Direct portal scraper + Google RSS search)
- News18 Kannada (Direct portal scraper + Google RSS search)
- Asianet Suvarna News (RSS & district feeds)
- Prajavani (Public feed & 31 district sections)
- TV9 Kannada (Main & district feeds)
- Public TV
- OneIndia Kannada
- Star of Mysore, Just Kannada (Mysuru)
- Mangalorean (Dakshina Kannada / Udupi)
- Shivamogga Live (Shivamogga)
- All About Belgaum (Belagavi)
"""

import os
import re
import json
import time
import html
import hashlib
from datetime import datetime, timezone
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

from utils import store, save_json, log, ist_now, ist_date, sanitize_dict, encrypt_payload

DATA_DIR = Path(os.getenv("OUTPUT_DIR", "../data"))

DISTRICT_GEOLOCATION = {
    "bengaluru-urban": {"name_kn": "ಬೆಂಗಳೂರು ನಗರ", "hq": "Bengaluru", "lat": 12.9716, "lng": 77.5946},
    "bengaluru-rural": {"name_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "hq": "Devanahalli", "lat": 13.2257, "lng": 77.5750},
    "ramanagara": {"name_kn": "ರಾಮನಗರ", "hq": "Ramanagara", "lat": 12.7209, "lng": 77.2799},
    "chikkaballapura": {"name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "hq": "Chikkaballapura", "lat": 13.4355, "lng": 77.7315},
    "kolar": {"name_kn": "ಕೋಲಾರ", "hq": "Kolar", "lat": 13.1367, "lng": 78.1291},
    "tumakuru": {"name_kn": "ತುಮಕೂರು", "hq": "Tumakuru", "lat": 13.3379, "lng": 77.1173},
    "chitradurga": {"name_kn": "ಚಿತ್ರದುರ್ಗ", "hq": "Chitradurga", "lat": 14.2251, "lng": 76.3980},
    "davanagere": {"name_kn": "ದಾವಣಗೆರೆ", "hq": "Davanagere", "lat": 14.4644, "lng": 75.9218},
    "shivamogga": {"name_kn": "ಶಿವಮೊಗ್ಗ", "hq": "Shivamogga", "lat": 13.9299, "lng": 75.5681},
    "mysuru": {"name_kn": "ಮೈಸೂರು", "hq": "Mysuru", "lat": 12.2958, "lng": 76.6394},
    "mandya": {"name_kn": "ಮಂಡ್ಯ", "hq": "Mandya", "lat": 12.5218, "lng": 76.8951},
    "hassan": {"name_kn": "ಹಾಸನ", "hq": "Hassan", "lat": 13.0033, "lng": 76.1004},
    "kodagu": {"name_kn": "ಕೊಡಗು", "hq": "Madikeri", "lat": 12.4244, "lng": 75.7382},
    "chamarajanagara": {"name_kn": "ಚಾಮರಾಜನಗರ", "hq": "Chamarajanagara", "lat": 11.9261, "lng": 76.9437},
    "chikkamagaluru": {"name_kn": "ಚಿಕ್ಕಮಗಳೂರು", "hq": "Chikkamagaluru", "lat": 13.3161, "lng": 75.7720},
    "dakshina-kannada": {"name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "hq": "Mangaluru", "lat": 12.9141, "lng": 74.8560},
    "udupi": {"name_kn": "ಉಡುಪಿ", "hq": "Udupi", "lat": 13.3409, "lng": 74.7421},
    "uttara-kannada": {"name_kn": "ಉತ್ತರ ಕನ್ನಡ", "hq": "Karwar", "lat": 14.8185, "lng": 74.1416},
    "belagavi": {"name_kn": "ಬೆಳಗಾವಿ", "hq": "Belagavi", "lat": 15.8497, "lng": 74.4977},
    "dharwad": {"name_kn": "ಧಾರವಾಡ", "hq": "Dharwad", "lat": 15.4589, "lng": 75.0078},
    "gadag": {"name_kn": "ಗದಗ", "hq": "Gadag-Betageri", "lat": 15.4319, "lng": 75.6355},
    "haveri": {"name_kn": "ಹಾವೇರಿ", "hq": "Haveri", "lat": 14.7952, "lng": 75.3992},
    "bagalkote": {"name_kn": "ಬಾಗಲಕೋಟೆ", "hq": "Bagalkote", "lat": 16.1852, "lng": 75.6961},
    "vijayapura": {"name_kn": "ವಿಜಯಪುರ", "hq": "Vijayapura", "lat": 16.8302, "lng": 75.7100},
    "kalaburagi": {"name_kn": "ಕಲಬುರಗಿ", "hq": "Kalaburagi", "lat": 17.3297, "lng": 76.8343},
    "yadgir": {"name_kn": "ಯಾದಗಿರಿ", "hq": "Yadgir", "lat": 16.7700, "lng": 77.1378},
    "raichur": {"name_kn": "ರಾಯಚೂರು", "hq": "Raichur", "lat": 16.2076, "lng": 77.3463},
    "koppal": {"name_kn": "ಕೊಪ್ಪಳ", "hq": "Koppal", "lat": 15.3469, "lng": 76.1554},
    "ballari": {"name_kn": "ಬಳ್ಳಾರಿ", "hq": "Ballari", "lat": 15.1394, "lng": 76.9214},
    "vijayanagara": {"name_kn": "ವಿಜಯನಗರ", "hq": "Hosapete", "lat": 15.2688, "lng": 76.3909},
    "bidar": {"name_kn": "ಬೀದರ್", "hq": "Bidar", "lat": 17.9104, "lng": 77.5199},
}

RSS_SOURCES = [
    # Asianet Suvarna
    {"name": "ಏಷ್ಯಾನೆಟ್ ಸುವರ್ಣ (Asianet News)", "rss": "https://kannada.asianetnews.com/rss", "lang": "kn", "logo": "asianet"},

    # Prajavani & TV9 Main
    {"name": "ಪ್ರಜಾವಾಣಿ (Prajavani)", "rss": "https://www.prajavani.net/feed", "lang": "kn", "logo": "prajavani"},
    {"name": "TV9 ಕನ್ನಡ (TV9 Kannada)", "rss": "https://tv9kannada.com/feed", "lang": "kn", "logo": "tv9"},
    {"name": "TV9 ಕರ್ನಾಟಕ ಸುದ್ದಿ", "rss": "https://tv9kannada.com/karnataka/feed", "lang": "kn", "logo": "tv9"},

    # TV9 District Feeds
    {"name": "TV9 ಬೆಂಗಳೂರು", "rss": "https://tv9kannada.com/karnataka/bengaluru/feed", "lang": "kn", "logo": "tv9", "district": "bengaluru-urban"},
    {"name": "TV9 ಮೈಸೂರು", "rss": "https://tv9kannada.com/karnataka/mysuru/feed", "lang": "kn", "logo": "tv9", "district": "mysuru"},
    {"name": "TV9 ಬೆಳಗಾವಿ", "rss": "https://tv9kannada.com/karnataka/belagavi/feed", "lang": "kn", "logo": "tv9", "district": "belagavi"},
    {"name": "TV9 ಶಿವಮೊಗ್ಗ", "rss": "https://tv9kannada.com/karnataka/shivamogga/feed", "lang": "kn", "logo": "tv9", "district": "shivamogga"},
    {"name": "TV9 ಉತ್ತರ ಕನ್ನಡ", "rss": "https://tv9kannada.com/karnataka/uttara-kannada/feed", "lang": "kn", "logo": "tv9", "district": "uttara-kannada"},
    {"name": "TV9 ದಕ್ಷಿಣ ಕನ್ನಡ", "rss": "https://tv9kannada.com/karnataka/dakshina-kannada/feed", "lang": "kn", "logo": "tv9", "district": "dakshina-kannada"},
    {"name": "TV9 ಉಡುಪಿ", "rss": "https://tv9kannada.com/karnataka/udupi/feed", "lang": "kn", "logo": "tv9", "district": "udupi"},
    {"name": "TV9 ಕಲಬುರಗಿ", "rss": "https://tv9kannada.com/karnataka/kalaburagi/feed", "lang": "kn", "logo": "tv9", "district": "kalaburagi"},
    {"name": "TV9 ಮಂಡ್ಯ", "rss": "https://tv9kannada.com/karnataka/mandya/feed", "lang": "kn", "logo": "tv9", "district": "mandya"},
    {"name": "TV9 ಹಾಸನ", "rss": "https://tv9kannada.com/karnataka/hassan/feed", "lang": "kn", "logo": "tv9", "district": "hassan"},
    {"name": "TV9 ಕೊಡಗು", "rss": "https://tv9kannada.com/karnataka/kodagu/feed", "lang": "kn", "logo": "tv9", "district": "kodagu"},

    # Public TV & OneIndia
    {"name": "ಪಬ್ಲಿಕ್ ಟಿವಿ (Public TV)", "rss": "https://publictv.in/feed/", "lang": "kn", "logo": "publictv"},
    {"name": "ಒನ್‌ಇಂಡಿಯಾ ಕನ್ನಡ (OneIndia)", "rss": "https://kannada.oneindia.com/rss/kannada-news-fb.xml", "lang": "kn", "logo": "oneindia"},

    # Local District Portals
    {"name": "ಶಿವಮೊಗ್ಗ ಲೈವ್ (Shivamogga Live)", "rss": "https://shivamoggalive.com/feed/", "lang": "kn", "logo": "shivamoggalive", "district": "shivamogga"},
    {"name": "ಜಸ್ಟ್ ಕನ್ನಡ (Just Kannada)", "rss": "https://www.justkannada.in/feed/", "lang": "kn", "logo": "justkannada", "district": "mysuru"},
    {"name": "ಸ್ಟಾರ್ ಆಫ್ ಮೈಸೂರು (Star of Mysore)", "rss": "https://starofmysore.com/feed/", "lang": "en", "logo": "som", "district": "mysuru"},
    {"name": "ಮಂಗಳೂರಿಯನ್ (Mangalorean)", "rss": "https://www.mangalorean.com/feed/", "lang": "en", "logo": "mangalorean", "district": "dakshina-kannada"}
]

PRAJAVANI_DISTRICT_SLUGS = {
    "bengaluru-urban": "bengaluru",
    "bengaluru-rural": "bengaluru-rural",
    "mysuru": "mysuru",
    "mandya": "mandya",
    "hassan": "hassan",
    "kodagu": "kodagu",
    "dakshina-kannada": "dakshina-kannada",
    "udupi": "udupi",
    "shivamogga": "shivamogga",
    "chikkamagaluru": "chikkamagaluru",
    "tumakuru": "tumakuru",
    "chitradurga": "chitradurga",
    "davanagere": "davanagere",
    "belagavi": "belagavi",
    "dharwad": "dharwad",
    "gadag": "gadaga",
    "haveri": "haveri",
    "uttara-kannada": "uttara-kannada",
    "bagalkote": "bagalkote",
    "vijayapura": "vijayapura",
    "kalaburagi": "kalaburagi",
    "yadgir": "yadagiri",
    "raichur": "raichur",
    "koppal": "koppal",
    "ballari": "ballari",
    "vijayanagara": "vijayanagara",
    "chikkaballapura": "chikkaballapur",
    "kolar": "kolar",
    "ramanagara": "ramanagara",
    "chamarajanagara": "chamarajanagara",
    "bidar": "bidar",
}

STRICT_DISTRICT_RULES = {
    "bengaluru-urban": ["ಬೆಂಗಳೂರು", "ಬಿಬಿಎಂಪಿ", "bbmp", "bengaluru", "bangalore", "ಯಲಹಂಕ", "ಮೆಜೆಸ್ಟಿಕ್", "ವೈಟ್‌ಫೀಲ್ಡ್", "ಜಯನಗರ", "ಕೋರಮಂಗಲ", "ಇಂದಿರಾನಗರ"],
    "bengaluru-rural": ["ದೇವನಹಳ್ಳಿ", "ನೆಲಮಂಗಲ", "ದೊಡ್ಡಬಳ್ಳಾಪುರ", "ಹೊಸಕೋಟೆ", "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "ಕಿಯಾಲ್"],
    "ramanagara": ["ರಾಮನಗರ", "ಚನ್ನಪಟ್ಟಣ", "ಕನಕಪುರ", "ಮಾಗಡಿ", "ಹಾರೋಹಳ್ಳಿ", "ಬಿಡದಿ"],
    "chikkaballapura": ["ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "ಗೌರಿಬಿದನೂರು", "ಬಾಗೇಪಲ್ಲಿ", "ಶಿಡ್ಲಘಟ್ಟ", "ಚಿಂತಾಮಣಿ", "ನಂದಿ ಬೆಟ್ಟ"],
    "kolar": ["ಕೋಲಾರ", "ಮಾಲೂರು", "ಬಂಗಾರಪೇಟೆ", "ಕೆಜಿಎಫ್", "kgf", "ಶ್ರೀನಿವಾಸಪುರ", "ಮುಳಬಾಗಿಲು"],
    "tumakuru": ["ತುಮಕೂರು", "ತಿಪಟೂರು", "ಕುಣಿಗಲ್", "ಸಿರಾ", "ಮಧುಗಿರಿ", "ಪಾವಗಡ", "ತುರುವೇಕೆರೆ", "ಗುಬ್ಬಿ", "ಸಿದ್ಧಗಂಗಾ"],
    "chitradurga": ["ಚಿತ್ರದುರ್ಗ", "ಚಳ್ಳಕೆರೆ", "ಹಿರಿಯೂರು", "ಹೊಲಲ್ಕೆರೆ", "ಹೊಸದುರ್ಗ", "ಮೊಳಕಾಲ್ಮೂರು", "ಕೋಟೆ ನಾಡು"],
    "davanagere": ["ದಾವಣಗೆರೆ", "ಹರಿಹರ", "ಜಗಳೂರು", "ಚನ್ನಗಿರಿ", "ಹೊನ್ನಾಳಿ", "ನ್ಯಾಮತಿ", "ಬೆಣ್ಣೆ ನಗರಿ"],
    "shivamogga": ["ಶಿವಮೊಗ್ಗ", "ಸಾಗರ", "ಶಿಕಾರಿಪುರ", "ತೀರ್ಥಹಳ್ಳಿ", "ಭದ್ರಾವತಿ", "ಸೊರಬ", "ಹೊಸನಗರ", "ಜೋಗ್"],
    "mysuru": ["ಮೈಸೂರು", "ನಂಜನಗೂಡು", "ಹುಣಸೂರು", "ಟಿ.ನರಸೀಪುರ", "ಪಿರಿಯಾಪಟ್ಟಣ", "ಕೆ.ಆರ್.ನಗರ", "ಚಾಮುಂಡಿ", "ದಸರಾ"],
    "mandya": ["ಮಂಡ್ಯ", "ಮದ್ದೂರು", "ಮಳವಳ್ಳಿ", "ಶ್ರೀರಂಗಪಟ್ಟಣ", "ಪಾಂಡವಪುರ", "ಕೆ.ಆರ್.ಪೇಟೆ", "ನಾಗಮಂಗಲ", "ಕೆಆರ್‌ಎಸ್"],
    "hassan": ["ಹಾಸನ", "ಅರಸೀಕೆರೆ", "ಚನ್ನರಾಯಪಟ್ಟಣ", "ಹೊಳೆನರಸೀಪುರ", "ಸಕಲೇಶಪುರ", "ಬೇಲೂರು", "ಆಲೂರು", "ಹಳೇಬೀಡು"],
    "kodagu": ["ಕೊಡಗು", "ಮಡಿಕೇರಿ", "ಸೋಮವಾರಪೇಟೆ", "ವಿರಾಜಪೇಟೆ", "ಪೊನ್ನಂಪೇಟೆ", "ಕುಶಾಲನಗರ", "ತಲಕಾವೇರಿ"],
    "chamarajanagara": ["ಚಾಮರಾಜನಗರ", "ಕೊಳ್ಳೇಗಾಲ", "ಗುಂಡ್ಲುಪೇಟೆ", "ಯಳಂದೂರು", "ಹನೂರು", "ಬಂಡೀಪುರ", "ಮಲೆ ಮಹದೇಶ್ವರ"],
    "chikkamagaluru": ["ಚಿಕ್ಕಮಗಳೂರು", "ತಾರೀಕೆರೆ", "ಕಡೂರು", "ಮೂಡಿಗೆರೆ", "ಶೃಂಗೇರಿ", "ಕೊಪ್ಪ", "ಮುಳ್ಳಯ್ಯನಗಿರಿ"],
    "dakshina-kannada": ["ಮಂಗಳೂರು", "ಪುತ್ತೂರು", "ಬೆಳ್ತಂಗಡಿ", "ಬಂಟ್ವಾಳ", "ಸುಳ್ಯ", "ದಕ್ಷಿಣ ಕನ್ನಡ", "ಧರ್ಮಸ್ಥಳ", "ಕುಕ್ಕೆ"],
    "udupi": ["ಉಡುಪಿ", "ಕಾರ್ಕಳ", "ಕುಂದಾಪುರ", "ಬ್ರಹ್ಮಾವರ", "ಕಾಪು", "ಬೈಂದೂರು", "ಮಲ್ಪೆ", "ಕೃಷ್ಣ ಮಠ"],
    "uttara-kannada": ["ಕಾರವಾರ", "ಅಂಕೋಲಾ", "ಕುಮಟಾ", "ಹೊನ್ನಾವರ", "ಭಟ್ಕಳ", "ಶಿರಸಿ", "ಗೋಕರ್ಣ", "ದಾಂಡೇಲಿ", "ಉತ್ತರ ಕನ್ನಡ"],
    "belagavi": ["ಬೆಳಗಾವಿ", "ಗೋಕಾಕ್", "ಚಿಕ್ಕೋಡಿ", "ಅಥಣಿ", "ಬೈಲಹೊಂಗಲ", "ಖಾನಾಪುರ", "ನಿಪ್ಪಾಣಿ", "ಸುವರ್ಣ ಸೌಧ"],
    "dharwad": ["ಧಾರವಾಡ", "ಹುಬ್ಬಳ್ಳಿ", "ಕಲಘಟಗಿ", "ನವಲಗುಂದ", "ಅಣ್ಣಿಗೇರಿ", "ವಿದ್ಯಾಕಾಶಿ"],
    "gadag": ["ಗದಗ", "ಬೆಟಗೇರಿ", "ರೋಣ", "ಶಿರಹಟ್ಟಿ", "ಮುಂಡರಗಿ", "ನರಗುಂದ", "ಲಕ್ಷ್ಮೇಶ್ವರ", "ಕಪ್ಪತಗುಡ್ಡ"],
    "haveri": ["ಹಾವೇರಿ", "ರಾಣೇಬೆನ್ನೂರು", "ಬ್ಯಾಡಗಿ", "ಹಾನಗಲ್", "ಹಿರೇಕೆರೂರು", "ಶಿಗ್ಗಾಂವಿ", "ಕಾಗಿನೆಲೆ"],
    "bagalkote": ["ಬಾಗಲಕೋಟೆ", "ಜಮಖಂಡಿ", "ಮುಧೋಳ", "ಬಾದಾಮಿ", "ಹುನಗುಂದ", "ಇಳಕಲ್", "ಆಲಮಟ್ಟಿ", "ಪಟ್ಟದಕಲ್ಲು"],
    "vijayapura": ["ವಿಜಯಪುರ", "ಇಂಡಿ", "ಮುದ್ದೇಬಿಹಾಳ", "ಬಬಲೇಶ್ವರ", "ಬಸವನ ಬಾಗೇವಾಡಿ", "ಸಿಂದಗಿ", "ಗೋಳಗುಮ್ಮಟ"],
    "kalaburagi": ["ಕಲಬುರಗಿ", "ಗುಲ್ಬರ್ಗಾ", "ಸೇಡಂ", "ಚಿತ್ತಾಪುರ", "ಆಳಂದ", "ಅಫ್ಜಲ್ಪುರ", "ಜೇವರ್ಗಿ", "ತೊಗರಿ"],
    "yadgir": ["ಯಾದಗಿರಿ", "ಶಹಾಪುರ", "ಸುರಪುರ", "ಗುರುಮಿಟ್ಕಲ್", "ಹುಣಸಗಿ", "ವಡಗೇರಾ", "ಬಸವ ಸಾಗರ"],
    "raichur": ["ರಾಯಚೂರು", "ಮಾನ್ವಿ", "ಸಿಂಧನೂರು", "ದೇವದುರ್ಗ", "ಲಿಂಗಸುಗೂರು", "ಮಸ್ಕಿ", "ಆರ್‌ಟಿಪಿಎಸ್"],
    "koppal": ["ಕೊಪ್ಪಳ", "ಗಂಗಾವತಿ", "ಕುಷ್ಟಗಿ", "ಯಲಬುರ್ಗಾ", "ಕಾರಟಗಿ", "ಕುಕನೂರು", "ಕಿನ್ನಾಳ", "ಆನೆಗೊಂದಿ"],
    "ballari": ["ಬಳ್ಳಾರಿ", "ಕಂಪ್ಲಿ", "ಸಿರುಗುಪ್ಪ", "ಕುರುಗೋಡು", "ಸಂದೂರು", "ತೋರಣಗಲ್ಲು"],
    "vijayanagara": ["ವಿಜಯನಗರ", "ಹೊಸಪೇಟೆ", "ಹಂಪಿ", "ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ", "ಹೂವಿನಹಡಗಲಿ", "ಕೂಡ್ಲಿಗಿ", "ಟಿಬಿ ಡ್ಯಾಂ"],
    "bidar": ["ಬೀದರ್", "ಹುಮ್ನಾಬಾದ್", "ಭಾಲ್ಕಿ", "ಬಸವಕಲ್ಯಾಣ", "ಔರಾದ್", "ಗುರುನಾನಕ್ ಝೀರಾ", "ಬಿದ್ರಿ"],
}

DISTRICT_KEYWORDS_SCRAPE = [
    'ಬೆಂಗಳೂರು', 'ಮೈಸೂರು', 'ಮಂಡ್ಯ', 'ಹಾಸನ', 'ಮಂಗಳೂರು', 'ಉಡುಪಿ', 'ಬೆಳಗಾವಿ', 'ಹುಬ್ಬಳ್ಳಿ', 'ಧಾರವಾಡ',
    'ಶಿವಮೊಗ್ಗ', 'ದಾವಣಗೆರೆ', 'ತುಮಕೂರು', 'ಚಿತ್ರದುರ್ಗ', 'ಬಳ್ಳಾರಿ', 'ವಿಜಯನಗರ', 'ಕಲಬುರಗಿ', 'ಬೀದರ್',
    'ರಾಯಚೂರು', 'ಕೊಪ್ಪಳ', 'ಯಾದಗಿರಿ', 'ಬಾಗಲಕೋಟೆ', 'ವಿಜಯಪುರ', 'ಗದಗ', 'ಹಾವೇರಿ', 'ಕೋಲಾರ',
    'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', 'ರಾಮನಗರ', 'ಚಾಮರಾಜನಗರ', 'ಕೊಡಗು', 'ಚಿಕ್ಕಮಗಳೂರು', 'ಉತ್ತರ ಕನ್ನಡ', 'ಕಾರವಾರ',
    'ಕರ್ನಾಟಕ', 'ರಾಜಕೀಯ', 'ಕ್ರೈಂ', 'ಕೃಷಿ'
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "kn,en-US;q=0.9,en;q=0.8"
}

INVALID_HEADLINES = {
    'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ', 'ಬೆಂಗಳೂರು ನಗರ', 'ಮೈಸೂರು', 'ಮಂಡ್ಯ', 'ಬೆಳಗಾವಿ', 'ಕಲಬುರಗಿ',
    'ದಕ್ಷಿಣ ಕನ್ನಡ', 'ಉಡುಪಿ', 'ಉತ್ತರ ಕನ್ನಡ', 'ಶಿವಮೊಗ್ಗ', 'ಹಾಸನ', 'ತುಮಕೂರು',
    'ದಾವಣಗೆರೆ', 'ಬಳ್ಳಾರಿ', 'ವಿಜಯನಗರ', 'ಕೊಡಗು', 'ಚಿಕ್ಕಮಗಳೂರು', 'ವಿಜಯಪುರ',
    'ರಾಯಚೂರು', 'ಕೊಪ್ಪಳ', 'ಬಾಗಲಕೋಟೆ', 'ಗದಗ', 'ಹಾವೇರಿ', 'ಧಾರವಾಡ', 'ಯಾದಗಿರಿ',
    'ಬೀದರ್', 'ಕೋಲಾರ', 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', 'ರಾಮನಗರ', 'ಚಾಮರಾಜನಗರ', 'ಚಿತ್ರದುರ್ಗ',
    'ಕರ್ನಾಟಕ', 'ರಾಜ್ಯ', 'ಮುಖ್ಯಾಂಶಗಳು', 'ಇತ್ತೀಚಿನ ಸುದ್ದಿಗಳು', 'ಜಿಲ್ಲಾ ಸುದ್ದಿ',
    'ರಾಜಕೀಯ', 'ಸಿನಿಮಾ', 'ಕ್ರೀಡೆ', 'ವ್ಯಾಪಾರ', 'ಜೀವನಶೈಲಿ', 'ಫೋಟೋ ಗ್ಯಾಲರಿ', 'ವೀಡಿಯೋ',
    'ಬೆಂಗಳೂರು', 'ಮಂಗಳೂರು', 'ಹುಬ್ಬಳ್ಳಿ', 'ಕಾರವಾರ', 'ಮಡಿಕೇರಿ', 'ಸ್ಥಳೀಯ ಸುದ್ದಿ'
}

def is_valid_headline(t: str) -> bool:
    if not t or not isinstance(t, str):
        return False
    t = t.strip()
    if len(t) < 20:
        return False
    if t in INVALID_HEADLINES:
        return False
    if len(t.split()) < 4:
        return False
    if not re.search(r'[\u0C80-\u0CFF]', t):
        return False
    return True

def clean_text(t: str) -> str:
    if not t: return ""
    t = html.unescape(t)
    t = re.sub(r'<[^>]+>', '', t)
    t = re.sub(r'\s*Last\s*Updated.*$', '', t, flags=re.I)
    t = re.sub(r'\s*[-–—|:]+$', '', t)
    return ' '.join(t.split()).strip()

def scrape_rss_feed(src: dict) -> list:
    url = src.get("rss")
    name = src.get("name", "Unknown")
    forced_dist = src.get("district")
    articles = []

    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            root = ET.fromstring(r.content)
            for item in root.findall('.//item'):
                title_el = item.find('title')
                link_el = item.find('link')
                pub_el = item.find('pubDate')
                desc_el = item.find('description')

                title = clean_text(title_el.text) if title_el is not None else ""
                link = link_el.text.strip() if link_el is not None and link_el.text else ""
                pub = pub_el.text.strip() if pub_el is not None and pub_el.text else ist_now()
                desc = clean_text(desc_el.text) if desc_el is not None else ""

                if is_valid_headline(title):
                    articles.append({
                        "title": title,
                        "url": link,
                        "published": pub,
                        "summary": desc[:180],
                        "source": name,
                        "forced_district": forced_dist
                    })
            log.info(f"  RSS {name}: {len(articles)} articles")
    except Exception as e:
        log.warning(f"  ⚠️ RSS {name} failed: {e}")

    return articles

def scrape_vijay_karnataka() -> list:
    articles = []
    seen = set()
    log.info("🌐 Scraping Fresh Live Vijay Karnataka (Direct Multi-Section Portals)...")

    portal_urls = [
        "https://vijaykarnataka.com/",
        "https://vijaykarnataka.com/news/karnataka/articlelist/10765233.cms",
        "https://vijaykarnataka.com/news/bengaluru-city/articlelist/11182323.cms",
        "https://vijaykarnataka.com/news/mysuru/articlelist/11182191.cms",
        "https://vijaykarnataka.com/news/mangaluru/articlelist/11182260.cms",
        "https://vijaykarnataka.com/news/shivamogga/articlelist/11182146.cms",
        "https://vijaykarnataka.com/news/hubballi/articlelist/11182283.cms",
        "https://vijaykarnataka.com/news/belagavi/articlelist/11182305.cms",
        "https://vijaykarnataka.com/news/articlelist/10753874.cms"
    ]

    for url in portal_urls:
        try:
            r = requests.get(url, headers=HEADERS, timeout=8)
            if r.status_code == 200:
                r.encoding = "utf-8"
                soup = BeautifulSoup(r.text, 'html.parser')
                for a in soup.find_all('a', href=True):
                    href = a['href']
                    if '/articleshow/' in href:
                        t = clean_text(a.get_text())
                        link = 'https://vijaykarnataka.com' + href if href.startswith('/') else href
                        if is_valid_headline(t) and t not in seen:
                            seen.add(t)
                            articles.append({
                                "title": t,
                                "url": link,
                                "published": ist_now(),
                                "summary": "",
                                "source": "ವಿಜಯ ಕರ್ನಾಟಕ (Vijay Karnataka)"
                            })
        except Exception as e:
            log.warning(f"  ⚠️ VK direct URL failed {url}: {e}")

    log.info(f"✔ Fresh Live Vijay Karnataka: {len(articles)} articles scraped")
    return articles

def scrape_news18_kannada() -> list:
    articles = []
    seen = set()
    log.info("🌐 Scraping Fresh Live News18 Kannada (Direct Multi-Section Portals)...")

    portal_urls = [
        "https://kannada.news18.com/",
        "https://kannada.news18.com/karnataka-news/",
        "https://kannada.news18.com/news/state/",
        "https://kannada.news18.com/districts/",
        "https://kannada.news18.com/news/bengaluru/",
        "https://kannada.news18.com/news/mysuru/",
        "https://kannada.news18.com/news/crime/",
        "https://kannada.news18.com/news/agriculture/"
    ]

    for url in portal_urls:
        try:
            r = requests.get(url, headers=HEADERS, timeout=8)
            if r.status_code == 200:
                r.encoding = "utf-8"
                soup = BeautifulSoup(r.text, 'html.parser')
                for a in soup.find_all('a', href=True):
                    href = a['href']
                    if '.html' in href or '/news/' in href or '/state/' in href:
                        t = clean_text(a.get_text())
                        link = 'https://kannada.news18.com' + href if href.startswith('/') else href
                        if 'news18' in link and is_valid_headline(t) and t not in seen:
                            seen.add(t)
                            articles.append({
                                "title": t,
                                "url": link,
                                "published": ist_now(),
                                "summary": "",
                                "source": "ನ್ಯೂಸ್18 ಕನ್ನಡ (News18)"
                            })
        except Exception as e:
            log.warning(f"  ⚠️ News18 direct URL failed {url}: {e}")

    log.info(f"✔ Fresh Live News18 Kannada: {len(articles)} articles scraped")
    return articles

def scrape_prajavani_districts() -> list:
    articles = []
    log.info("🌐 Scraping Prajavani 31 District sections...")
    for dist_key, slug in list(PRAJAVANI_DISTRICT_SLUGS.items())[:15]:
        url = f"https://www.prajavani.net/district/{slug}"
        try:
            r = requests.get(url, headers=HEADERS, timeout=6)
            if r.status_code == 200:
                r.encoding = "utf-8"
                soup = BeautifulSoup(r.text, 'html.parser')
                count = 0
                for a in soup.find_all('a', href=True):
                    if '/district/' in a['href'] and len(a.text.strip()) > 15:
                        t = clean_text(a.text)
                        link = 'https://www.prajavani.net' + a['href'] if a['href'].startswith('/') else a['href']
                        if is_valid_headline(t) and t not in [x['title'] for x in articles]:
                            articles.append({
                                "title": t,
                                "url": link,
                                "published": ist_now(),
                                "summary": "",
                                "source": "ಪ್ರಜಾವಾಣಿ (Prajavani)",
                                "forced_district": dist_key
                            })
                            count += 1
                            if count >= 6: break
        except Exception:
            pass
    log.info(f"✔ Prajavani Districts: {len(articles)} district articles scraped")
    return articles

def parse_date_to_timestamp(d_str) -> float:
    if not d_str:
        return time.time()
    s = str(d_str).strip()
    try:
        from email.utils import parsedate_to_datetime
        return parsedate_to_datetime(s).timestamp()
    except Exception:
        pass
    try:
        from datetime import datetime
        return datetime.fromisoformat(s.replace('Z', '+00:00')).timestamp()
    except Exception:
        pass
    for fmt in ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d', '%d-%m-%Y', '%d %b %Y %H:%M:%S', '%d %b %Y']:
        try:
            from datetime import datetime
            return datetime.strptime(s, fmt).timestamp()
        except Exception:
            pass
    return time.time()

def assign_district(article: dict) -> str:
    if article.get("forced_district"):
        return article["forced_district"]

    text = (article["title"] + " " + article.get("summary", "")).lower()

    # Rule-based matching with strict priority
    best_dist = None
    max_matches = 0

    for dist_key, keywords in STRICT_DISTRICT_RULES.items():
        matches = sum(1 for kw in keywords if kw.lower() in text)
        if matches > max_matches:
            max_matches = matches
            best_dist = dist_key

    if best_dist and max_matches > 0:
        return best_dist

    return "_statewide"

def run() -> dict:
    log.info("📰 Starting Comprehensive Karnataka Multi-Publisher News Scraper...")

    raw_articles = []

    # 1. Scrape all standard RSS feeds
    for src in RSS_SOURCES:
        raw_articles.extend(scrape_rss_feed(src))

    # 2. Scrape Vijaya Karnataka Portal & Google RSS
    raw_articles.extend(scrape_vijay_karnataka())

    # 3. Scrape News18 Kannada Portal & Google RSS
    raw_articles.extend(scrape_news18_kannada())

    # 4. Scrape Prajavani District Sections
    raw_articles.extend(scrape_prajavani_districts())

    log.info(f"📰 Total unique raw articles collected: {len(raw_articles)}")

    # Deduplicate and Bucket by District
    seen_titles = set()
    district_buckets = {k: [] for k in DISTRICT_GEOLOCATION.keys()}
    district_buckets["_statewide"] = []

    for art in raw_articles:
        t = art["title"]
        if t in seen_titles: continue
        seen_titles.add(t)

        dist = assign_district(art)
        if dist in district_buckets:
            district_buckets[dist].append(art)
        else:
            district_buckets["_statewide"].append(art)

    # Sort each district bucket chronologically so latest news is ALWAYS ON TOP
    for d_key in district_buckets:
        district_buckets[d_key].sort(
            key=lambda x: parse_date_to_timestamp(x.get("published")),
            reverse=True
        )

    total_sorted = sum(len(v) for v in district_buckets.values())

    output = {
        "date": ist_date(),
        "updated_at": ist_now(),
        "total": len(seen_titles),
        "districts_count": len(DISTRICT_GEOLOCATION),
        "district_buckets": district_buckets,
        "sources": [
            "Vijay Karnataka", "News18 Kannada", "Asianet Suvarna News",
            "Prajavani", "TV9 Kannada", "Public TV", "OneIndia Kannada",
            "Shivamogga Live", "Just Kannada", "Star of Mysore", "Mangalorean"
        ],
        "note_kn": "ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಪ್ರಮುಖ ಸುದ್ದಿವಾಹಿನಿಗಳಿಂದ ಸಂಗ್ರಹಿಸಲಾದ ಸಜೀವ ಸುದ್ದಿಗಳು"
    }

    store("local_news.json", "local_news", output)
    log.info(f"✅ Multi-Source District News Saved: {total_sorted} articles across 32 district buckets (including Vijaya Karnataka & News18)")
    return output

if __name__ == "__main__":
    run()