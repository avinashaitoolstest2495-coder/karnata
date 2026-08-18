"""
Karnata — local_news_scraper.py
Multi-Source Strict District Local News Scraper with Geolocation & High-Precision Tagging

Aggregates news from all top Kannada & District portals:
- Vijaya Karnataka (Direct portal scraper + true JSON-LD / meta timestamp extraction)
- News18 Kannada (Direct portal scraper + true JSON-LD / meta timestamp extraction)
- Asianet Suvarna News (RSS & district feeds)
- Prajavani (Public feed & 31 district sections)
- TV9 Kannada (Main & district feeds)
- Public TV
- OneIndia Kannada
- Star of Mysore, Just Kannada (Mysuru)
- Mangalorean (Dakshina Kannada / Udupi)
- Shivamogga Live (Shivamogga)
"""

import os
import re
import json
import time
import html
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
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
    "bengaluru-urban": ["ಬಿಬಿಎಂಪಿ", "bbmp", "ಮೆಜೆಸ್ಟಿಕ್", "ವೈಟ್‌ಫೀಲ್ಡ್", "ಜಯನಗರ", "ಕೋರಮಂಗಲ", "ಇಂದಿರಾನಗರ", "ಹೆಬ್ಬಾಳ", "ಬಿಡಿಎ", "bda", "ಜಲಮಂಡಳಿ", "ನಮ್ಮ ಮೆಟ್ರೋ", "ಕೆಂಪೇಗೌಡ ನಿಲ್ದಾಣ", "ಸಿಲಿಕಾನ್ ಸಿಟಿ", "ಬೆಂಗಳೂರು ನಗರ"],
    "bengaluru-rural": ["ದೇವನಹಳ್ಳಿ", "ನೆಲಮಂಗಲ", "ದೊಡ್ಡಬಳ್ಳಾಪುರ", "ಹೊಸಕೋಟೆ", "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "ಕಿಯಾಲ್"],
    "ramanagara": ["ರಾಮನಗರ", "ಚನ್ನಪಟ್ಟಣ", "ಕನಕಪುರ", "ಮಾಗಡಿ", "ಹಾರೋಹಳ್ಳಿ", "ಬಿಡದಿ"],
    "chikkaballapura": ["ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "ಗೌರಿಬಿದನೂರು", "ಬಾಗೇಪಲ್ಲಿ", "ಶಿಡ್ಲಘಟ್ಟ", "ಚಿಂತಾಮಣಿ", "ನಂದಿ ಬೆಟ್ಟ", "ಗುಡಿಬಂಡೆ"],
    "kolar": ["ಕೋಲಾರ", "ಮಾಲೂರು", "ಬಂಗಾರಪೇಟೆ", "ಕೆಜಿಎಫ್", "kgf", "ಶ್ರೀನಿವಾಸಪುರ", "ಮುಳಬಾಗಿಲು", "ಅಂತರಗಂಗೆ"],
    "tumakuru": ["ತುಮಕೂರು", "ತಿಪಟೂರು", "ಕುಣಿಗಲ್", "ಸಿರಾ", "ಮಧುಗಿರಿ", "ಪಾವಗಡ", "ತುರುವೇಕೆರೆ", "ಗುಬ್ಬಿ", "ಸಿದ್ಧಗಂಗಾ", "ಕೊರಟಗೆರೆ", "ಚಿಕ್ಕನಾಯಕನಹಳ್ಳಿ"],
    "chitradurga": ["ಚಿತ್ರದುರ್ಗ", "ಚಳ್ಳಕೆರೆ", "ಹಿರಿಯೂರು", "ಹೊಲಲ್ಕೆರೆ", "ಹೊಸದುರ್ಗ", "ಮೊಳಕಾಲ್ಮೂರು", "ಕೋಟೆ ನಾಡು", "ವಾಣಿ ವಿಲಾಸ"],
    "davanagere": ["ದಾವಣಗೆರೆ", "ಹರಿಹರ", "ಜಗಳೂರು", "ಚನ್ನಗಿರಿ", "ಹೊನ್ನಾಳಿ", "ನ್ಯಾಮತಿ", "ಬೆಣ್ಣೆ ನಗರಿ"],
    "shivamogga": ["ಶಿವಮೊಗ್ಗ", "ಸಾಗರ", "ಶಿಕಾರಿಪುರ", "ತೀರ್ಥಹಳ್ಳಿ", "ಭದ್ರಾವತಿ", "ಸೊರಬ", "ಹೊಸನಗರ", "ಜೋಗ್", "ಶರಾವತಿ"],
    "mysuru": ["ಮೈಸೂರು", "ನಂಜನಗೂಡು", "ಹುಣಸೂರು", "ಟಿ.ನರಸೀಪುರ", "ಪಿರಿಯಾಪಟ್ಟಣ", "ಕೆ.ಆರ್.ನಗರ", "ಚಾಮುಂಡಿ ಬೆಟ್ಟ", "ಮೈಸೂರು ದಸರಾ", "ಬನ್ನಿಮಂಟಪ", "ಸರಗೂರು"],
    "mandya": ["ಮಂಡ್ಯ", "ಮದ್ದೂರು", "ಮಳವಳ್ಳಿ", "ಶ್ರೀರಂಗಪಟ್ಟಣ", "ಪಾಂಡವಪುರ", "ಕೆ.ಆರ್.ಪೇಟೆ", "ನಾಗಮಂಗಲ", "ಕೆಆರ್‌ಎಸ್", "ಶಿವನಸಮುದ್ರ"],
    "hassan": ["ಹಾಸನ", "ಅರಸೀಕೆರೆ", "ಚನ್ನರಾಯಪಟ್ಟಣ", "ಹೊಳೆನರಸೀಪುರ", "ಸಕಲೇಶಪುರ", "ಬೇಲೂರು", "ಆಲೂರು", "ಹಳೇಬೀಡು", "ಶ್ರವಣಬೆಳಗೊಳ", "ಅರಕಲಗೂಡು"],
    "kodagu": ["ಕೊಡಗು", "ಮಡಿಕೇರಿ", "ಸೋಮವಾರಪೇಟೆ", "ವಿರಾಜಪೇಟೆ", "ಪೊನ್ನಂಪೇಟೆ", "ಕುಶಾಲನಗರ", "ತಲಕಾವೇರಿ", "ಭಾಗಮಂಡಲ"],
    "chamarajanagara": ["ಚಾಮರಾಜನಗರ", "ಕೊಳ್ಳೇಗಾಲ", "ಗುಂಡ್ಲುಪೇಟೆ", "ಯಳಂದೂರು", "ಹನೂರು", "ಬಂಡೀಪುರ", "ಮಲೆ ಮಹದೇಶ್ವರ", "ಬಿಳಿಗಿರಿರಂಗನ"],
    "chikkamagaluru": ["ಚಿಕ್ಕಮಗಳೂರು", "ತಾರೀಕೆರೆ", "ಕಡೂರು", "ಮೂಡಿಗೆರೆ", "ಶೃಂಗೇರಿ", "ಕೊಪ್ಪ", "ಮುಳ್ಳಯ್ಯನಗಿರಿ", "ಕಳಸ", "ಬಾಬಾಬುಡನ್‌ಗಿರಿ", "ಕುದುರೆಮುಖ"],
    "dakshina-kannada": ["ಮಂಗಳೂರು", "ಪುತ್ತೂರು", "ಬೆಳ್ತಂಗಡಿ", "ಬಂಟ್ವಾಳ", "ಸುಳ್ಯ", "ದಕ್ಷಿಣ ಕನ್ನಡ", "ಧರ್ಮಸ್ಥಳ", "ಕುಕ್ಕೆ ಸುಬ್ರಹ್ಮಣ್ಯ", "ಕಟೀಲು", "ಮೂಡುಬಿದಿರೆ"],
    "udupi": ["ಉಡುಪಿ", "ಕಾರ್ಕಳ", "ಕುಂದಾಪುರ", "ಬ್ರಹ್ಮಾವರ", "ಕಾಪು", "ಬೈಂದೂರು", "ಮಲ್ಪೆ", "ಕೃಷ್ಣ ಮಠ", "ಕೊಲ್ಲೂರು", "ಮಂದಾರ್ತಿ", "ಹೆಬ್ರಿ"],
    "uttara-kannada": ["ಕಾರವಾರ", "ಅಂಕೋಲಾ", "ಕುಮಟಾ", "ಹೊನ್ನಾವರ", "ಭಟ್ಕಳ", "ಶಿರಸಿ", "ಗೋಕರ್ಣ", "ದಾಂಡೇಲಿ", "ಉತ್ತರ ಕನ್ನಡ", "ಯಲ್ಲಾಪುರ", "ಮುಂಡಗೋಡ", "ಜೋಯಿಡಾ"],
    "belagavi": ["ಬೆಳಗಾವಿ", "ಗೋಕಾಕ್", "ಚಿಕ್ಕೋಡಿ", "ಅಥಣಿ", "ಬೈಲಹೊಂಗಲ", "ಖಾನಾಪುರ", "ನಿಪ್ಪಾಣಿ", "ಸುವರ್ಣ ಸೌಧ", "ರಾಯಭಾಗ", "ಹುಕ್ಕೇರಿ", "ಸವದತ್ತಿ"],
    "dharwad": ["ಧಾರವಾಡ", "ಹುಬ್ಬಳ್ಳಿ", "ಕಲಘಟಗಿ", "ನವಲಗುಂದ", "ಅಣ್ಣಿಗೇರಿ", "ವಿದ್ಯಾಕಾಶಿ", "ಕುಂದಗೋಳ", "ಅಳ್ನಾವರ"],
    "gadag": ["ಗದಗ", "ಬೆಟಗೇರಿ", "ರೋಣ", "ಶಿರಹಟ್ಟಿ", "ಮುಂಡರಗಿ", "ನರಗುಂದ", "ಲಕ್ಷ್ಮೇಶ್ವರ", "ಕಪ್ಪತಗುಡ್ಡ", "ಗಜೇಂದ್ರಗಡ"],
    "haveri": ["ಹಾವೇರಿ", "ರಾಣೇಬೆನ್ನೂರು", "ಬ್ಯಾಡಗಿ", "ಹಾನಗಲ್", "ಹಿರೇಕೆರೂರು", "ಶಿಗ್ಗಾಂವಿ", "ಕಾಗಿನೆಲೆ", "ಸವಣೂರು", "ರಟ್ಟೀಹಳ್ಳಿ"],
    "bagalkote": ["ಬಾಗಲಕೋಟೆ", "ಜಮಖಂಡಿ", "ಮುಧೋಳ", "ಬಾದಾಮಿ", "ಹುನಗುಂದ", "ಇಳಕಲ್", "ಆಲಮಟ್ಟಿ", "ಪಟ್ಟದಕಲ್ಲು", "ಕೂಡಲಸಂಗಮ", "ಬೀಳಗಿ", "ಮಹಾಕೂಟ"],
    "vijayapura": ["ವಿಜಯಪುರ", "ಇಂಡಿ", "ಮುದ್ದೇಬಿಹಾಳ", "ಬಬಲೇಶ್ವರ", "ಬಸವನ ಬಾಗೇವಾಡಿ", "ಸಿಂದಗಿ", "ಗೋಳಗುಮ್ಮಟ", "ತಾಳಿಕೋಟೆ", "ಚಡಚಣ", "ಆಲಮಟ್ಟಿ"],
    "kalaburagi": ["ಕಲಬುರಗಿ", "ಗುಲ್ಬರ್ಗಾ", "ಸೇಡಂ", "ಚಿತ್ತಾಪುರ", "ಆಳಂದ", "ಅಫ್ಜಲ್ಪುರ", "ಜೇವರ್ಗಿ", "ತೊಗರಿ ಕಣಜ", "ಚಿಂಚೋಳಿ", "ಗಾಣಗಾಪುರ", "ಖ್ವಾಜಾ ಬಂದೇ ನವಾಜ್"],
    "yadgir": ["ಯಾದಗಿರಿ", "ಶಹಾಪುರ", "ಸುರಪುರ", "ಗುರುಮಿಟ್ಕಲ್", "ಹುಣಸಗಿ", "ವಡಗೇರಾ", "ಬಸವ ಸಾಗರ", "ಛಾಯಾ ಭಗವತಿ"],
    "raichur": ["ರಾಯಚೂರು", "ಮಾನ್ವಿ", "ಸಿಂಧನೂರು", "ದೇವದುರ್ಗ", "ಲಿಂಗಸುಗೂರು", "ಮಸ್ಕಿ", "ಆರ್‌ಟಿಪಿಎಸ್", "ಹಟ್ಟಿ ಚಿನ್ನದ ಗಣಿ", "ಸಿರವಾರ"],
    "koppal": ["ಕೊಪ್ಪಳ", "ಗಂಗಾವತಿ", "ಕುಷ್ಟಗಿ", "ಯಲಬುರ್ಗಾ", "ಕಾರಟಗಿ", "ಕುಕನೂರು", "ಕಿನ್ನಾಳ", "ಆನೆಗೊಂದಿ", "ಕನಕಗಿರಿ", "ಮುನಿರಾಬಾದ್"],
    "ballari": ["ಬಳ್ಳಾರಿ", "ಕಂಪ್ಲಿ", "ಸಿರುಗುಪ್ಪ", "ಕುರುಗೋಡು", "ಸಂದೂರು", "ತೋರಣಗಲ್ಲು", "ಕನಕದುರ್ಗ"],
    "vijayanagara": ["ವಿಜಯನಗರ", "ಹೊಸಪೇಟೆ", "ಹಂಪಿ", "ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ", "ಹೂವಿನಹಡಗಲಿ", "ಕೂಡ್ಲಿಗಿ", "ಟಿಬಿ ಡ್ಯಾಂ", "ಕೊಟ್ಟೂರು", "ಕಮಲಾಪುರ"],
    "bidar": ["ಬೀದರ್", "ಹುಮ್ನಾಬಾದ್", "ಭಾಲ್ಕಿ", "ಬಸವಕಲ್ಯಾಣ", "ಔರಾದ್", "ಗುರುನಾನಕ್ ಝೀರಾ", "ಬಿದ್ರಿ ಕಲೆ", "ಕಮಲನಗರ", "ಚಿಟಗುಪ್ಪ"],
}

# Statewide indicators (prevent these from wrongly going into bengaluru-urban)
STATEWIDE_PATTERNS = [
    "ಸಚಿವ ಸಂಪುಟ", "ಮುಖ್ಯಮಂತ್ರಿ ಸಿದ್ದರಾಮಯ್ಯ", "ಸಿಎಂ ಸಿದ್ದರಾಮಯ್ಯ", "ಡಿಕೆ ಶಿವಕುಮಾರ್", "ವಿಧಾನಸೌಧ",
    "ರಾಜ್ಯ ಸರ್ಕಾರ", "ಕರ್ನಾಟಕ ಸರ್ಕಾರ", "ಗ್ಯಾರಂಟಿ ಯೋಜನೆ", "ಗೃಹಲಕ್ಷ್ಮಿ", "ಯುವನಿಧಿ", "ಶಕ್ತಿ ಯೋಜನೆ",
    "ಅನ್ನಭಾಗ್ಯ", "ಹೈಕೋರ್ಟ್", "ಲೋಕಸಭೆ", "ವಿಧಾನಸಭೆ", "ಕೆಪಿಸಿಸಿ", "ಬಿಜೆಪಿ ರಾಜ್ಯಾಧ್ಯಕ್ಷ", "ಜೆಡಿಎಸ್",
    "ರಾಜ್ಯಪಾಲ", "ಬಜೆಟ್", "ಕೇಂದ್ರ ಸರ್ಕಾರ"
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

def clean_title(t: str) -> str:
    """Thoroughly cleans titles removing photo counters, media prefixes, and trailing publisher suffixes."""
    if not t or not isinstance(t, str):
        return ""
    t = html.unescape(t)
    t = re.sub(r'<[^>]+>', '', t)
    # Remove photo/video badge prefixes like '+8 Photos', '+10 Photos', 'Photos:', 'Photo Gallery:'
    t = re.sub(r'^\+\d+\s*(photos?|ಚಿತ್ರಗಳು?|ವೀಡಿಯೊ|ವಿಡಿಯೋ|videos?)\s*', '', t, flags=re.I)
    t = re.sub(r'^(photos?|ಚಿತ್ರಗಳು|ವೀಡಿಯೊ|ವಿಡಿಯೋ|videos?|watch|breaking|exclusive|live\s*updates?|explainer)\s*[:|-]\s*', '', t, flags=re.I)
    t = re.sub(r'\s*Last\s*Updated.*$', '', t, flags=re.I)
    # Remove trailing publisher watermarks/dashes
    t = re.sub(r'\s*[-–—|:]\s*(ಪ್ರಾಜಾವಾಣಿ|ಪ್ರಜಾವಾಣಿ|prajavani|ವಿಜಯ\s*ಕರ್ನಾಟಕ|vijay\s*karnataka|news18|n18v|tv9|asianet|suvarna|public\s*tv|oneindia|kannada|som|star\s*of\s*mysore).*$', '', t, flags=re.I)
    t = re.sub(r'\s*[-–—|:]+$', '', t)
    return ' '.join(t.split()).strip()

def is_valid_headline(t: str) -> bool:
    if not t or not isinstance(t, str):
        return False
    t = clean_title(t)
    if len(t) < 18:
        return False
    if t in INVALID_HEADLINES:
        return False
    if len(t.split()) < 3:
        return False
    if not re.search(r'[\u0C80-\u0CFF]', t):
        return False
    return True

def parse_date_to_timestamp(d_str) -> float:
    if not d_str:
        return 0.0
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
    for fmt in ['%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d', '%d-%m-%Y', '%d %b %Y %H:%M:%S', '%d %b %Y']:
        try:
            from datetime import datetime
            return datetime.strptime(s, fmt).timestamp()
        except Exception:
            pass
    return 0.0

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

                raw_title = title_el.text if title_el is not None and title_el.text else ""
                title = clean_title(raw_title)
                link = link_el.text.strip() if link_el is not None and link_el.text else ""
                pub = pub_el.text.strip() if pub_el is not None and pub_el.text else ""
                desc = clean_title(desc_el.text) if desc_el is not None and desc_el.text else ""

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

def fetch_article_timestamp_and_title(item: dict) -> dict:
    """Concurrently fetches true ISO published date from HTML metadata/JSON-LD for portal articles."""
    url = item.get("url", "")
    if not url or not url.startswith("http"):
        return item

    try:
        r = requests.get(url, headers=HEADERS, timeout=4)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            
            # Check og:title / title if cleaner
            og_t = soup.find('meta', property='og:title')
            if og_t and og_t.get('content'):
                clean_og = clean_title(og_t['content'])
                if is_valid_headline(clean_og):
                    item["title"] = clean_og

            # Check meta published_time
            meta_pub = soup.find('meta', property=['article:published_time', 'og:published_time', 'pubdate'])
            if meta_pub and meta_pub.get('content'):
                item["published"] = meta_pub['content'].strip()
                return item

            # Check JSON-LD schema
            for s in soup.find_all('script', type='application/ld+json'):
                try:
                    if not s.string: continue
                    d = json.loads(s.string)
                    if isinstance(d, dict):
                        pub = d.get('datePublished') or d.get('dateCreated') or d.get('uploadDate')
                        if pub:
                            item["published"] = str(pub).strip()
                            return item
                    elif isinstance(d, list):
                        for x in d:
                            if isinstance(x, dict):
                                pub = x.get('datePublished') or x.get('dateCreated')
                                if pub:
                                    item["published"] = str(pub).strip()
                                    return item
                except Exception:
                    pass
    except Exception:
        pass

    return item

def scrape_vijay_karnataka() -> list:
    articles = []
    seen = set()
    log.info("🌐 Scraping Fresh Live Vijay Karnataka...")

    portal_urls = [
        "https://vijaykarnataka.com/news/karnataka/articlelist/10765233.cms",
        "https://vijaykarnataka.com/news/bengaluru-city/articlelist/11182323.cms",
        "https://vijaykarnataka.com/news/mysuru/articlelist/11182191.cms",
        "https://vijaykarnataka.com/news/mangaluru/articlelist/11182260.cms",
        "https://vijaykarnataka.com/news/shivamogga/articlelist/11182146.cms",
        "https://vijaykarnataka.com/news/hubballi/articlelist/11182283.cms",
        "https://vijaykarnataka.com/news/belagavi/articlelist/11182305.cms",
        "https://vijaykarnataka.com/news/articlelist/10753874.cms"
    ]

    raw_candidates = []
    for url in portal_urls:
        try:
            r = requests.get(url, headers=HEADERS, timeout=6)
            if r.status_code == 200:
                r.encoding = "utf-8"
                soup = BeautifulSoup(r.text, 'html.parser')
                for a in soup.find_all('a', href=True):
                    href = a['href']
                    if '/articleshow/' in href:
                        t = clean_title(a.get_text())
                        link = 'https://vijaykarnataka.com' + href if href.startswith('/') else href
                        if is_valid_headline(t) and t not in seen:
                            seen.add(t)
                            raw_candidates.append({
                                "title": t,
                                "url": link,
                                "published": "",
                                "summary": "",
                                "source": "ವಿಜಯ ಕರ್ನಾಟಕ (Vijay Karnataka)"
                            })
        except Exception as e:
            log.warning(f"  ⚠️ VK direct URL failed {url}: {e}")

    # Fetch timestamps concurrently for top 30 candidates
    log.info(f"  Extracting exact published timestamps for {len(raw_candidates[:30])} Vijay Karnataka articles...")
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_article_timestamp_and_title, art) for art in raw_candidates[:30]]
        for f in as_completed(futures):
            try:
                res = f.result()
                if res and res.get("title"):
                    articles.append(res)
            except Exception:
                pass

    log.info(f"✔ Fresh Live Vijay Karnataka: {len(articles)} articles scraped with timestamps")
    return articles

def scrape_news18_kannada() -> list:
    articles = []
    seen = set()
    log.info("🌐 Scraping Fresh Live News18 Kannada...")

    portal_urls = [
        "https://kannada.news18.com/karnataka-news/",
        "https://kannada.news18.com/news/state/",
        "https://kannada.news18.com/districts/",
        "https://kannada.news18.com/news/bengaluru/",
        "https://kannada.news18.com/news/mysuru/",
        "https://kannada.news18.com/news/crime/",
        "https://kannada.news18.com/news/agriculture/"
    ]

    raw_candidates = []
    for url in portal_urls:
        try:
            r = requests.get(url, headers=HEADERS, timeout=6)
            if r.status_code == 200:
                r.encoding = "utf-8"
                soup = BeautifulSoup(r.text, 'html.parser')
                for a in soup.find_all('a', href=True):
                    href = a['href']
                    if ('.html' in href or '/news/' in href or '/state/' in href) and '/photogallery/' not in href:
                        t = clean_title(a.get_text())
                        link = 'https://kannada.news18.com' + href if href.startswith('/') else href
                        if 'news18' in link and is_valid_headline(t) and t not in seen:
                            seen.add(t)
                            raw_candidates.append({
                                "title": t,
                                "url": link,
                                "published": "",
                                "summary": "",
                                "source": "ನ್ಯೂಸ್18 ಕನ್ನಡ (News18)"
                            })
        except Exception as e:
            log.warning(f"  ⚠️ News18 direct URL failed {url}: {e}")

    # Fetch timestamps concurrently for top 30 candidates
    log.info(f"  Extracting exact published timestamps for {len(raw_candidates[:30])} News18 articles...")
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_article_timestamp_and_title, art) for art in raw_candidates[:30]]
        for f in as_completed(futures):
            try:
                res = f.result()
                if res and res.get("title"):
                    articles.append(res)
            except Exception:
                pass

    log.info(f"✔ Fresh Live News18 Kannada: {len(articles)} articles scraped with timestamps")
    return articles

def scrape_prajavani_districts() -> list:
    articles = []
    log.info("🌐 Scraping Prajavani District sections...")
    raw_candidates = []

    for dist_key, slug in list(PRAJAVANI_DISTRICT_SLUGS.items())[:16]:
        url = f"https://www.prajavani.net/district/{slug}"
        try:
            r = requests.get(url, headers=HEADERS, timeout=5)
            if r.status_code == 200:
                r.encoding = "utf-8"
                soup = BeautifulSoup(r.text, 'html.parser')
                count = 0
                for a in soup.find_all('a', href=True):
                    if '/district/' in a['href'] and len(a.text.strip()) > 15:
                        t = clean_title(a.text)
                        link = 'https://www.prajavani.net' + a['href'] if a['href'].startswith('/') else a['href']
                        if is_valid_headline(t) and t not in [x['title'] for x in raw_candidates]:
                            raw_candidates.append({
                                "title": t,
                                "url": link,
                                "published": "",
                                "summary": "",
                                "source": "ಪ್ರಜಾವಾಣಿ (Prajavani)",
                                "forced_district": dist_key
                            })
                            count += 1
                            if count >= 4: break
        except Exception:
            pass

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(fetch_article_timestamp_and_title, art) for art in raw_candidates[:25]]
        for f in as_completed(futures):
            try:
                res = f.result()
                if res and res.get("title"):
                    articles.append(res)
            except Exception:
                pass

    log.info(f"✔ Prajavani Districts: {len(articles)} district articles scraped")
    return articles

def assign_district(article: dict) -> str:
    if article.get("forced_district"):
        return article["forced_district"]

    title = article.get("title", "")
    summary = article.get("summary", "")
    full_text = (title + " " + summary).lower()

    # If it's a general statewide political/governance headline without explicit local civic terms, keep as statewide
    is_statewide_topic = any(pattern.lower() in full_text for pattern in STATEWIDE_PATTERNS)
    has_bengaluru_civic = any(w in full_text for w in ["ಬಿಬಿಎಂಪಿ", "bbmp", "ಮೆಜೆಸ್ಟಿಕ್", "ವೈಟ್‌ಫೀಲ್ಡ್", "ಜಯನಗರ", "ಕೋರಮಂಗಲ", "ಇಂದಿರಾನಗರ", "ಹೆಬ್ಬಾಳ", "ಬಿಡಿಎ", "bda", "ಜಲಮಂಡಳಿ", "ನಮ್ಮ ಮೆಟ್ರೋ", "ಸಿಲಿಕಾನ್ ಸಿಟಿ"])

    # Check non-Bengaluru districts first with high priority
    best_dist = None
    max_matches = 0

    for dist_key, keywords in STRICT_DISTRICT_RULES.items():
        if dist_key == "bengaluru-urban":
            continue
        matches = sum(1 for kw in keywords if kw.lower() in full_text)
        if matches > max_matches:
            max_matches = matches
            best_dist = dist_key

    if best_dist and max_matches >= 1:
        return best_dist

    # Check Bengaluru Urban specifically
    if has_bengaluru_civic or (not is_statewide_topic and any(kw.lower() in full_text for kw in STRICT_DISTRICT_RULES["bengaluru-urban"])):
        return "bengaluru-urban"

    return "_statewide"

def run() -> dict:
    log.info("📰 Starting Comprehensive Karnataka Multi-Publisher News Scraper...")

    raw_articles = []

    # 1. Scrape standard RSS feeds (with accurate pubDate)
    for src in RSS_SOURCES:
        raw_articles.extend(scrape_rss_feed(src))

    # 2. Scrape Vijaya Karnataka with true JSON-LD / meta timestamps
    raw_articles.extend(scrape_vijay_karnataka())

    # 3. Scrape News18 Kannada with true JSON-LD / meta timestamps
    raw_articles.extend(scrape_news18_kannada())

    # 4. Scrape Prajavani District Sections
    raw_articles.extend(scrape_prajavani_districts())

    log.info(f"📰 Total raw articles collected: {len(raw_articles)}")

    # Deduplicate and Bucket by District
    seen_titles = set()
    district_buckets = {k: [] for k in DISTRICT_GEOLOCATION.keys()}
    district_buckets["_statewide"] = []

    for art in raw_articles:
        t = clean_title(art["title"])
        if not is_valid_headline(t):
            continue
        art["title"] = t
        if t in seen_titles:
            continue
        seen_titles.add(t)

        dist = assign_district(art)
        if dist in district_buckets:
            district_buckets[dist].append(art)
        else:
            district_buckets["_statewide"].append(art)

    # Sort each district bucket strictly chronologically (newest first)
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
    log.info(f"✅ Multi-Source District News Saved: {total_sorted} articles across 32 district buckets")
    return output

if __name__ == "__main__":
    run()