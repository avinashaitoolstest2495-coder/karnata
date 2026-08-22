"""
Karnata — local_news_scraper.py
Deep High-Volume Multi-Publisher Karnataka District News Scraper
- Scrapes deeply across all top publishers (100+ articles per publisher)
- Strict filtration: NO horoscope/astrology, NO lifestyle/recipes, NO world news, NO irrelevant national news
- State-of-the-art multi-tier district classifier for all 31 Karnataka districts & 240+ taluks
- Strict timestamp ordering: latest fresh news always comes on top, preserving historical archive
"""

import os
import re
import json
import time
import html
from collections import Counter
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from bs4 import BeautifulSoup
import warnings
from bs4 import XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

from utils import save_json, log, ist_now, ist_date

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

# Exhaustive Bilingual & Vibhakti District & Taluk Keywords
DISTRICT_KEYWORDS = {
    "bengaluru-urban": [
        "ಬೆಂಗಳೂರು", "ಬೆಂಗಳೂರಿ", "bengaluru", "bangalore", "bbmp", "ಬಿಬಿಎಂಪಿ", "bda", "ಬಿಡಿಎ",
        "ನಮ್ಮ ಮೆಟ್ರೋ", "namma metro", "ಯಲಹಂಕ", "yelahanka", "ವೈಟ್‌ಫೀಲ್ಡ್", "whitefield",
        "ಜಯನಗರ", "jayanagar", "ಕೋರಮಂಗಲ", "koramangala", "ಇಂದಿರಾನಗರ", "indiranagar", "ಹೆಬ್ಬಾಳ", "hebbal",
        "ಮೆಜೆಸ್ಟಿಕ್", "majestic", "ಮಲ್ಲೇಶ್ವರಂ", "malleswaram", "ರಾಜಾಜಿನಗರ", "rajajinagar",
        "ಕಬ್ಬನ್ ಪಾರ್ಕ್", "cubbon park", "ಲಾಲ್‌ಬಾಗ್", "lalbagh", "ವಿಧಾನಸೌಧ", "ವಿಕಾಸಸೌಧ", "ಕೆಂಪೇಗೌಡ"
    ],
    "bengaluru-rural": [
        "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "bengaluru rural", "bangalore rural", "ದೇವನಹಳ್ಳಿ", "devanahalli",
        "ನೆಲಮಂಗಲ", "nelamangala", "ದೊಡ್ಡಬಳ್ಳಾಪುರ", "doddaballapur", "ಹೊಸಕೋಟೆ", "hoskote"
    ],
    "ramanagara": [
        "ರಾಮನಗರ", "ramanagara", "ramanagar", "ಚನ್ನಪಟ್ಟಣ", "channapatna", "ಕನಕಪುರ", "kanakapura",
        "ಮಾಗಡಿ", "magadi", "ಹಾರೋಹಳ್ಳಿ", "harohalli", "ಬಿಡದಿ", "bidadi", "ಮೇಕೆದಾಟು", "mekedatu"
    ],
    "chikkaballapura": [
        "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "chikkaballapur", "chikkaballapura", "chikballapur", "ಗೌರಿಬಿದನೂರು", "gauribidanur",
        "ಬಾಗೇಪಲ್ಲಿ", "bagepalli", "ಶಿಡ್ಲಘಟ್ಟ", "sidlaghatta", "ಚಿಂತಾಮಣಿ", "chintamani",
        "ಗುಡಿಬಂಡೆ", "gudibande", "ನಂದಿ ಬೆಟ್ಟ", "nandi hills"
    ],
    "kolar": [
        "ಕೋಲಾರ", "kolar", "ಮಾಲೂರು", "malur", "ಬಂಗಾರಪೇಟೆ", "bangarapet", "ಕೆಜಿಎಫ್", "kgf",
        "ಶ್ರೀನಿವಾಸಪುರ", "srinivaspur", "ಮುಳಬಾಗಿಲು", "mulbagal"
    ],
    "tumakuru": [
        "ತುಮಕೂರು", "ತುಮಕೂರಿ", "tumakuru", "tumkur", "ತಿಪಟೂರು", "tiptur", "ಕುಣಿಗಲ್", "kunigal",
        "ಸಿರಾ", "sira", "ಮಧುಗಿರಿ", "madhugiri", "ಪಾವಗಡ", "pavagada", "ತುರುವೇಕೆರೆ", "turuvekere",
        "ಗುಬ್ಬಿ", "gubbi", "ಕೊರಟಗೆರೆ", "koratagere", "ಚಿಕ್ಕನಾಯಕನಹಳ್ಳಿ", "chikkanayakanahalli", "ಸಿದ್ಧಗಂಗಾ", "siddaganga"
    ],
    "chitradurga": [
        "ಚಿತ್ರದುರ್ಗ", "chitradurga", "ಚಳ್ಳಕೆರೆ", "challakere", "ಹಿರಿಯೂರು", "hiriyur",
        "ಹೊಲಲ್ಕೆರೆ", "holalkere", "ಹೊಸದುರ್ಗ", "hosadurga", "ಮೊಳಕಾಲ್ಮೂರು", "molakalmuru", "ವಾಣಿ ವಿಲಾಸ", "vani vilasa"
    ],
    "davanagere": [
        "ದಾವಣಗೆರೆ", "davanagere", "davangere", "ಹರಿಹರ", "harihar", "ಜಗಳೂರು", "jagalur",
        "ಚನ್ನಗಿರಿ", "channagiri", "ಹೊನ್ನಾಳಿ", "honnali", "ನ್ಯಾಮತಿ", "nyamati"
    ],
    "shivamogga": [
        "ಶಿವಮೊಗ್ಗ", "shivamogga", "shimoga", "ಸಾಗರ", "sagara", "ಶಿಕಾರಿಪುರ", "shikaripura",
        "ತೀರ್ಥಹಳ್ಳಿ", "thirthahalli", "ಭದ್ರಾವತಿ", "bhadravathi", "ಸೊರಬ", "soraba", "ಹೊಸನಗರ", "hosanagara",
        "ಜೋಗ್", "jog falls", "ಲಿಂಗನಮಕ್ಕಿ", "linganamakki", "ಆಗುಂಬೆ", "agumbe"
    ],
    "mysuru": [
        "ಮೈಸೂರು", "ಮೈಸೂರಿ", "mysuru", "mysore", "ನಂಜನಗೂಡು", "nanjangud", "ಹುಣಸೂರು", "hunsur",
        "ಟಿ.ನರಸೀಪುರ", "t narasipura", "ಪಿರಿಯಾಪಟ್ಟಣ", "periyapatna", "ಕೆ.ಆರ್.ನಗರ", "kr nagar",
        "ಸರಗೂರು", "saragur", "ಹೆಚ್.ಡಿ.ಕೋಟೆ", "hd kote", "ಚಾಮುಂಡಿ", "chamundi", "ಕಬಿನಿ", "kabini"
    ],
    "mandya": [
        "ಮಂಡ್ಯ", "mandya", "ಮದ್ದೂರು", "maddur", "ಮಳವಳ್ಳಿ", "malavalli", "ಶ್ರೀರಂಗಪಟ್ಟಣ", "srirangapatna",
        "ಪಾಂಡವಪುರ", "pandavapura", "ಕೆ.ಆರ್.ಪೇಟೆ", "kr pet", "ನಾಗಮಂಗಲ", "nagamangala",
        "ಕೆಆರ್‌ಎಸ್", "krs dam", "ಕಾವೇರಿ", "cauvery", "ರಂಗನತಿಟ್ಟು", "ranganathittu", "ಶಿವನಸಮುದ್ರ", "shivanasamudra"
    ],
    "hassan": [
        "ಹಾಸನ", "ಹಾಸನದ", "ಹಾಸನದಲ್ಲಿ", "hassan", "ಅರಸೀಕೆರೆ", "arsikere", "ಚನ್ನರಾಯಪಟ್ಟಣ", "channarayapatna",
        "ಹೊಳೆನರಸೀಪುರ", "holenarasipura", "ಸಕಲೇಶಪುರ", "sakleshpur", "ಬೇಲೂರು", "belur", "ಹಳೇಬೀಡು", "halebidu",
        "ಆಲೂರು", "alur", "ಅರಕಲಗೂಡು", "arkalgud", "ಶ್ರವಣಬೆಳಗೊಳ", "shravanabelagola", "ಹೇಮಾವತಿ", "hemavathi"
    ],
    "kodagu": [
        "ಕೊಡಗು", "ಕೊಡಗಿನ", "kodagu", "coorg", "ಮಡಿಕೇರಿ", "madikeri", "ಸೋಮವಾರಪೇಟೆ", "somwarpet",
        "ವಿರಾಜಪೇಟೆ", "virajpet", "ಪೊನ್ನಂಪೇಟೆ", "ponnampet", "ಕುಶಾಲನಗರ", "kushalnagar",
        "ತಲಕಾವೇರಿ", "talacauvery", "ಭಾಗಮಂಡಲ", "bhagamandala"
    ],
    "chamarajanagara": [
        "ಚಾಮರಾಜನಗರ", "chamarajanagar", "chamarajanagara", "ಕೊಳ್ಳೇಗಾಲ", "kollegal", "ಗುಂಡ್ಲುಪೇಟೆ", "gundlupet",
        "ಯಳಂದೂರು", "yelandur", "ಹನೂರು", "hanur", "ಬಂಡೀಪುರ", "bandipur", "ಮಲೆ ಮಹದೇಶ್ವರ", "male mahadeshwara", "ಬಿಳಿಗಿರಿರಂಗನ", "br hills"
    ],
    "chikkamagaluru": [
        "ಚಿಕ್ಕಮಗಳೂರು", "ಚಿಕ್ಕಮಗಳೂರಿ", "chikkamagaluru", "chikmagalur", "ತಾರೀಕೆರೆ", "tarikere", "ಕಡೂರು", "kadur",
        "ಮೂಡಿಗೆರೆ", "mudigere", "ಶೃಂಗೇರಿ", "sringeri", "ಕೊಪ್ಪ", "koppa", "ನರಸಿಂಹರಾಜಪುರ", "nr pura",
        "ಕಳಸ", "kalasa", "ಅಜ್ಜಂಪುರ", "ajjampura", "ಮುಳ್ಳಯ್ಯನಗಿರಿ", "mullayanagiri", "ಕುದುರೆಮುಖ", "kudremukh", "ಹೊರನಾಡು", "horanadu"
    ],
    "dakshina-kannada": [
        "ದಕ್ಷಿಣ ಕನ್ನಡ", "dakshina kannada", "south canara", "ಮಂಗಳೂರು", "ಮಂಗಳೂರಿ", "mangaluru", "mangalore",
        "ಪುತ್ತೂರು", "puttur", "ಬೆಳ್ತಂಗಡಿ", "belthangady", "ಬಂಟ್ವಾಳ", "bantwal", "ಸುಳ್ಯ", "sullia",
        "ಮೂಡುಬಿದಿರೆ", "moodbidri", "ಕಡಬ", "kadaba", "ಧರ್ಮಸ್ಥಳ", "dharmasthala", "ಕುಕ್ಕೆ", "kukke",
        "ಸುಬ್ರಹ್ಮಣ್ಯ", "subrahmanya", "ಪಣಂಬೂರು", "panambur", "ಉಳ್ಳಾಲ", "ullal"
    ],
    "udupi": [
        "ಉಡುಪಿ", "udupi", "ಕಾರ್ಕಳ", "karkala", "ಕುಂದಾಪುರ", "kundapura", "kundapur", "ಬ್ರಹ್ಮಾವರ", "brahmavar",
        "ಕಾಪು", "kaup", "ಬೈಂದೂರು", "byndoor", "ಮಲ್ಪೆ", "malpe", "ಹೆಬ್ರಿ", "hebri", "ಕೊಲ್ಲೂರು", "kollur", "ಮಣಿಪಾಲ", "manipal"
    ],
    "uttara-kannada": [
        "ಉತ್ತರ ಕನ್ನಡ", "uttara kannada", "north canara", "ಕಾರವಾರ", "karwar", "ಅಂಕೋಲಾ", "ankola",
        "ಕುಮಟಾ", "kumta", "ಹೊನ್ನಾವರ", "honnavar", "ಭಟ್ಕಳ", "bhatkal", "ಶಿರಸಿ", "sirsi", "ಗೋಕರ್ಣ", "gokarna",
        "ದಾಂಡೇಲಿ", "dandeli", "ಯಲ್ಲಾಪುರ", "yellapur", "ಮುಂಡಗೋಡ", "mundgod", "ಜೋಯಿಡಾ", "joida",
        "ಸಿದ್ದಾಪುರ", "siddapur", "ಹಳಿಯಾಳ", "haliyal", "ಮುರುಡೇಶ್ವರ", "murudeshwar"
    ],
    "belagavi": [
        "ಬೆಳಗಾವಿ", "belagavi", "belgaum", "ಗೋಕಾಕ್", "gokak", "ಚಿಕ್ಕೋಡಿ", "chikkodi", "ಅಥಣಿ", "athani",
        "ಬೈಲಹೊಂಗಲ", "bailhongal", "ಖಾನಾಪುರ", "khanapur", "ನಿಪ್ಪಾಣಿ", "nippani", "ಸುವರ್ಣ ಸೌಧ", "suvarna soudha",
        "ರಾಯಭಾಗ", "raybag", "ಹುಕ್ಕೇರಿ", "hukkeri", "ಸವದತ್ತಿ", "saundatti", "ರಾಮದುರ್ಗ", "ramdurg",
        "ಕಾಗವಾಡ", "kagwad", "ಮೂಡಲಗಿ", "mudalgi", "ಕಿತ್ತೂರು", "kittur"
    ],
    "dharwad": [
        "ಧಾರವಾಡ", "dharwad", "ಹುಬ್ಬಳ್ಳಿ", "ಹುಬ್ಬಳ್ಳಿಯಿ", "ಹುಬ್ಬಳ್ಳಿಯಲ್ಲಿ", "hubballi", "hubli",
        "ಕಲಘಟಗಿ", "kalghatgi", "ನವಲಗುಂದ", "navalgund", "ಅಣ್ಣಿಗೇರಿ", "annigeri", "ಕುಂದಗೋಳ", "kundgol", "ಅಳ್ನಾವರ", "alnavar"
    ],
    "gadag": [
        "ಗದಗ", "gadag", "ಬೆಟಗೇರಿ", "betageri", "ರೋಣ", "ron", "ಶಿರಹಟ್ಟಿ", "shirahatti",
        "ಮುಂಡರಗಿ", "mundargi", "ನರಗುಂದ", "nargund", "ಲಕ್ಷ್ಮೇಶ್ವರ", "lakshmeshwar", "ಗಜೇಂದ್ರಗಡ", "gajendragad"
    ],
    "haveri": [
        "ಹಾವೇರಿ", "haveri", "ರಾಣೇಬೆನ್ನೂರು", "ranebennur", "ಬ್ಯಾಡಗಿ", "byadgi", "ಹಾನಗಲ್", "hangal",
        "ಹಿರೇಕೆರೂರು", "hirekerur", "ಶಿಗ್ಗಾಂವಿ", "shiggaon", "ಸವಣೂರು", "savanur", "ರಟ್ಟೀಹಳ್ಳಿ", "rattihalli"
    ],
    "bagalkote": [
        "ಬಾಗಲಕೋಟೆ", "bagalkote", "bagalkot", "ಜಮಖಂಡಿ", "jamkhandi", "ಮುಧೋಳ", "mudhol",
        "ಬಾದಾಮಿ", "badami", "ಹುನಗುಂದ", "hungund", "ಇಳಕಲ್", "ilkal", "ಆಲಮಟ್ಟಿ", "almatti",
        "ಪಟ್ಟದಕಲ್ಲು", "pattadakal", "ಕೂಡಲಸಂಗಮ", "kudalasangama", "ಬೀಳಗಿ", "bilagi", "ಗುಳೇದಗುಡ್ಡ", "guledgudda", "ರಬಕವಿ ಬನಹಟ್ಟಿ", "banhatti", "ಐಹೊಳೆ", "aihole"
    ],
    "vijayapura": [
        "ವಿಜಯಪುರ", "ವಿಜಯಪುರದ", "vijayapura", "bijapur", "ಇಂಡಿ", "indi", "ಮುದ್ದೇಬಿಹಾಳ", "muddebihal",
        "ಬಬಲೇಶ್ವರ", "bableshwar", "ಬಸವನ ಬಾಗೇವಾಡಿ", "basavana bagewadi", "ಸಿಂದಗಿ", "sindagi",
        "ಗೋಳಗುಮ್ಮಟ", "gol gumbaz", "ತಾಳಿಕೋಟೆ", "talikote", "ಚಡಚಣ", "chadchan", "ದೇವರ ಹಿಪ್ಪರಗಿ", "devar hippargi",
        "ಕೊಲ್ಹಾರ", "kolhar", "ನಿಡಗುಂದಿ", "nidagundi", "ತಿಕೋಟಾ", "tikota"
    ],
    "kalaburagi": [
        "ಕಲಬುರಗಿ", "kalaburagi", "gulbarga", "ಗುಲ್ಬರ್ಗಾ", "ಸೇಡಂ", "sedam", "ಚಿತ್ತಾಪುರ", "chittapur",
        "ಆಳಂದ", "aland", "ಅಫ್ಜಲ್ಪುರ", "afzalpur", "ಜೇವರ್ಗಿ", "jevaragi", "ಚಿಂಚೋಳಿ", "chincholi",
        "ಕಮಲಾಪುರ", "kamalapur", "ಕಾಳಗಿ", "kalagi", "ಯಡ್ರಾಮಿ", "yadrami", "ಶಹಾಬಾದ್", "shahabad", "ಗಾಣಗಾಪುರ", "ganagapur"
    ],
    "yadgir": [
        "ಯಾದಗಿರಿ", "ಯಾದಗಿರಿಯ", "yadgir", "yadgiri", "ಶಹಾಪುರ", "shahapur", "ಸುರಪುರ", "surapur",
        "ಶೋರಾಪುರ", "shorapur", "ಗುರುಮಿಟ್ಕಲ್", "gurmitkal", "ಹುಣಸಗಿ", "hunasagi", "ವಡಗೇರಾ", "wadgera", "ಕಂದಕೂರ", "kandakur"
    ],
    "raichur": [
        "ರಾಯಚೂರು", "ರಾಯಚೂರಿ", "raichur", "ಮಾನ್ವಿ", "manvi", "ಸಿಂಧನೂರು", "sindhanur",
        "ದೇವದುರ್ಗ", "devadurga", "ಲಿಂಗಸುಗೂರು", "lingasugur", "ಮಸ್ಕಿ", "maski", "ಸಿರವಾರ", "sirwar", "ಮಂತ್ರಾಲಯ", "mantralayam"
    ],
    "koppal": [
        "ಕೊಪ್ಪಳ", "koppal", "ಗಂಗಾವತಿ", "gangavathi", "ಕುಷ್ಟಗಿ", "kushtagi", "ಯಲಬುರ್ಗಾ", "yelburga",
        "ಕಾರಟಗಿ", "karatagi", "ಕುಕನೂರು", "kukanur", "ಕನಕಗಿರಿ", "kanakagiri", "ಆನೆಗುಂದಿ", "anegundi"
    ],
    "ballari": [
        "ಬಳ್ಳಾರಿ", "ಬಳ್ಳಾರಿಯ", "ballari", "bellary", "ಕಂಪ್ಲಿ", "kampli", "ಸಿರುಗುಪ್ಪ", "siruguppa",
        "ಕುರುಗೋಡು", "kurugodu", "ಸಂದೂರು", "sandur", "ತೋರಣಗಲ್ಲು", "toranagallu"
    ],
    "vijayanagara": [
        "ವಿಜಯನಗರ", "vijayanagara", "vijayanagar", "ಹೊಸಪೇಟೆ", "hosapete", "hospet", "ಹಂಪಿ", "hampi",
        "ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ", "hagaribommanahalli", "ಹೂವಿನಹಡಗಲಿ", "hoovina hadagali", "ಕೂಡ್ಲಿಗಿ", "kudligi",
        "ಕೊಟ್ಟೂರು", "kotturu", "ಹರಪನಹಳ್ಳಿ", "harapanahalli", "ತುಂಗಭದ್ರಾ", "tungabhadra"
    ],
    "bidar": [
        "ಬೀದರ್", "ಬೀದರ್‌ನ", "bidar", "ಹುಮ್ನಾಬಾದ್", "humnabad", "ಭಾಲ್ಕಿ", "bhalki",
        "ಬಸವಕಲ್ಯಾಣ", "basavakalyan", "ಔರಾದ್", "aurad", "ಕಮಲನಗರ", "kamalanagar", "ಚಿಟಗುಪ್ಪ", "chitaguppa", "ಹುಲಸೂರು", "hulasuru"
    ]
}

# Strict Exclusions: NO Horoscope, Astrology, Lifestyle, Gossip
HOROSCOPE_LIFESTYLE_EXCLUSIONS = [
    "ರಾಶಿ ಭವಿಷ್ಯ", "ದಿನ ಭವಿಷ್ಯ", "ಜ್ಯೋತಿಷ್ಯ", "ಜಾತಕ", "ಪಂಚಾಂಗ", "ವಾಸ್ತು", "horoscope",
    "astrology", "zodiac", "ದಿನಭವಿಷ್ಯ", "ವಾರಭವಿಷ್ಯ", "ವರ್ಷಭವಿಷ್ಯ", "ರಾಶಿಫಲ", "ರೆಸಿಪಿ",
    "ಫಿಟ್‌ನೆಸ್", "ಸಿನಿಮಾ ಗಾಳಿಸುದ್ದಿ", "ಫ್ಯಾಷನ್", "ಲೈಫ್‌ಸ್ಟೈಲ್", "lifestyle", "beauty tips",
    "ಸೌಂದರ್ಯ ಟಿಪ್ಸ್", "ಅಡುಗೆ ಟಿಪ್ಸ್", "ಮನೆಮದ್ದು", "ಕುಂಡಲಿ", "ನಿಮ್ಮ ರಾಶಿ", "ಗ್ರಹಗತಿ"
]

# Strict Exclusions: NO World News
WORLD_EXCLUSIONS = [
    "ಅಮೆರಿಕ", "ಟ್ರಂಪ್", "ಬೈಡನ್", "ಇಸ್ರೇಲ್", "ಇರಾನ್", "ಗಾಜಾ", "ರಷ್ಯಾ", "ಉಕ್ರೇನ್",
    "ಚೀನಾ", "ಪಾಕಿಸ್ತಾನ", "ಬಾಂಗ್ಲಾದೇಶ", "ಶ್ರೀಲಂಕಾ", "ವಿಶ್ವ ಸಂಸ್ಥೆ", "ವಿದೇಶ", "ಅಂತರರಾಷ್ಟ್ರೀಯ",
    "ನೇಪಾಳ", "ವೈಟ್‌ಹೌಸ್", "trump", "biden", "israel", "gaza", "russia", "ukraine",
    "china", "pakistan", "bangladesh", "sri lanka", "white house", "world news", "putin", "netanyahu"
]

# Strict Exclusions: NO Non-Karnataka State Politics
NON_KARNATAKA_NATIONAL_EXCLUSIONS = [
    "ಉತ್ತರ ಪ್ರದೇಶ", "ಯೋಗಿ ಆದಿತ್ಯನಾಥ್", "ಬಿಹಾರ", "ನಿತೀಶ್ ಕುಮಾರ್", "ಪಶ್ಚಿಮ ಬಂಗಾಳ", "ಮಮತಾ ಬ್ಯಾನರ್ಜಿ",
    "ಮಹಾರಾಷ್ಟ್ರ ಸಿಎಂ", "ಏಕನಾಥ್ ಶಿಂಧೆ", "ಉದ್ಧವ್ ಠಾಕ್ರೆ", "ಫಡ್ನವೀಸ್", "ತಮಿಳುನಾಡು ಸಿಎಂ ಸ್ಟಾಲಿನ್",
    "ಕೇರಳ ಸಿಎಂ ಪಿಣರಾಯಿ", "ದೆಹಲಿ ಸಿಎಂ", "ಕೇಜ್ರಿವಾಲ್", "ಆತಿಶಿ", "ಮಾಯಾವತಿ", "ಅಖಿಲೇಶ್ ಯಾದವ್"
]

RSS_SOURCES = [
    {"name": "ಏಷ್ಯಾನೆಟ್ ಸುವರ್ಣ", "rss": "https://kannada.asianetnews.com/rss", "lang": "kn"},
    {"name": "ಪ್ರಜಾವಾಣಿ", "rss": "https://www.prajavani.net/feed", "lang": "kn"},
    {"name": "TV9 ಕನ್ನಡ", "rss": "https://tv9kannada.com/feed", "lang": "kn"},
    {"name": "TV9 ಕನ್ನಡ", "rss": "https://tv9kannada.com/karnataka/feed", "lang": "kn"},
    {"name": "TV9 ಕನ್ನಡ", "rss": "https://tv9kannada.com/karnataka/bengaluru/feed", "lang": "kn", "district": "bengaluru-urban"},
    {"name": "TV9 ಕನ್ನಡ", "rss": "https://tv9kannada.com/karnataka/mysuru/feed", "lang": "kn", "district": "mysuru"},
    {"name": "TV9 ಕನ್ನಡ", "rss": "https://tv9kannada.com/karnataka/belagavi/feed", "lang": "kn", "district": "belagavi"},
    {"name": "TV9 ಕನ್ನಡ", "rss": "https://tv9kannada.com/karnataka/shivamogga/feed", "lang": "kn", "district": "shivamogga"},
    {"name": "TV9 ಕನ್ನಡ", "rss": "https://tv9kannada.com/karnataka/uttara-kannada/feed", "lang": "kn", "district": "uttara-kannada"},
    {"name": "TV9 ಕನ್ನಡ", "rss": "https://tv9kannada.com/karnataka/dakshina-kannada/feed", "lang": "kn", "district": "dakshina-kannada"},
    {"name": "TV9 ಕನ್ನಡ", "rss": "https://tv9kannada.com/karnataka/udupi/feed", "lang": "kn", "district": "udupi"},
    {"name": "TV9 ಕನ್ನಡ", "rss": "https://tv9kannada.com/karnataka/kalaburagi/feed", "lang": "kn", "district": "kalaburagi"},
    {"name": "TV9 ಕನ್ನಡ", "rss": "https://tv9kannada.com/karnataka/mandya/feed", "lang": "kn", "district": "mandya"},
    {"name": "TV9 ಕನ್ನಡ", "rss": "https://tv9kannada.com/karnataka/hassan/feed", "lang": "kn", "district": "hassan"},
    {"name": "TV9 ಕನ್ನಡ", "rss": "https://tv9kannada.com/karnataka/kodagu/feed", "lang": "kn", "district": "kodagu"},
    {"name": "ಉದಯವಾಣಿ", "rss": "https://www.udayavani.com/feed", "lang": "kn"},
    {"name": "ಉದಯವಾಣಿ", "rss": "https://www.udayavani.com/kannada/news/state-news/feed", "lang": "kn"},
    {"name": "ಉದಯವಾಣಿ", "rss": "https://www.udayavani.com/kannada/news/karavali-news/feed", "lang": "kn", "district": "dakshina-kannada"},
    {"name": "ಪಬ್ಲಿಕ್ ಟಿವಿ", "rss": "https://publictv.in/feed/", "lang": "kn"},
    {"name": "ಹೊಸ ದಿಗಂತ", "rss": "https://hosadigantha.com/feed/", "lang": "kn"},
    {"name": "ಸಂಯುಕ್ತ ಕರ್ನಾಟಕ", "rss": "https://samyuktakarnataka.in/feed/", "lang": "kn"},
    {"name": "ಈ ಸಂಜೆ", "rss": "https://eesanje.com/feed/", "lang": "kn"},
    {"name": "ಒನ್‌ಇಂಡಿಯಾ", "rss": "https://kannada.oneindia.com/rss/kannada-news-fb.xml", "lang": "kn"},
    {"name": "ಶಿವಮೊಗ್ಗ ಲೈವ್", "rss": "https://shivamoggalive.com/feed/", "lang": "kn", "district": "shivamogga"},
    {"name": "ಜಸ್ಟ್ ಕನ್ನಡ", "rss": "https://www.justkannada.in/feed/", "lang": "kn", "district": "mysuru"}
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

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "kn,en-US;q=0.9,en;q=0.8"
}

def clean_title(t: str) -> str:
    if not t or not isinstance(t, str):
        return ""
    t = html.unescape(t)
    t = re.sub(r'<[^>]+>', '', t)
    t = re.sub(r'^\+\d+\s*(photos?|ಚಿತ್ರಗಳು?|ವೀಡಿಯೊ|ವಿಡಿಯೋ|videos?)\s*', '', t, flags=re.I)
    t = re.sub(r'^(photos?|ಚಿತ್ರಗಳು|ವೀಡಿಯೊ|ವಿಡಿಯೋ|videos?|watch|breaking|exclusive|live\s*updates?|explainer)\s*[:|-]\s*', '', t, flags=re.I)
    t = re.sub(r'\s*Last\s*Updated.*$', '', t, flags=re.I)
    t = re.sub(r'\s*[-–—|:]\s*(ಪ್ರಾಜಾವಾಣಿ|ಪ್ರಜಾವಾಣಿ|prajavani|ವಿಜಯ\s*ಕರ್ನಾಟಕ|vijay\s*karnataka|ವಿಜಯವಾಣಿ|vijayavani|ಉದಯವಾಣಿ|udayavani|ಕನ್ನಡ\s*ಪ್ರಭ|kannadaprabha|ಹೊಸ\s*ದಿಗಂತ|hosadigantha|ಸಂಯುಕ್ತ\s*ಕರ್ನಾಟಕ|samyuktakarnataka|news18|n18v|tv9|asianet|suvarna|public\s*tv|oneindia|kannada|som|star\s*of\s*mysore|eesanje|ಈ\s*ಸಂಜೆ).*$', '', t, flags=re.I)
    t = re.sub(r'\s*[-–—|:]+$', '', t)
    return ' '.join(t.split()).strip()

def is_valid_karnataka_news(t: str, summary: str = "") -> bool:
    if not t or not isinstance(t, str):
        return False
    t = clean_title(t)
    if len(t) < 12:
        return False
    # STRICT: MUST CONTAIN KANNADA CHARACTERS (\u0C80-\u0CFF) — NO ENGLISH NEWS
    if not re.search(r'[\u0C80-\u0CFF]', t):
        return False

    full_text = (t + " " + summary).lower()

    # 1. Reject Horoscope & Lifestyle
    for h in HOROSCOPE_LIFESTYLE_EXCLUSIONS:
        if h.lower() in full_text:
            return False

    # 2. Reject World News
    for w in WORLD_EXCLUSIONS:
        if w.lower() in full_text:
            return False

    # 3. Reject Non-Karnataka National News
    for nat in NON_KARNATAKA_NATIONAL_EXCLUSIONS:
        if nat.lower() in full_text:
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
            text = r.text
            items = re.findall(r'<item[\s>](.*?)</item>', text, flags=re.DOTALL | re.IGNORECASE)
            for raw_item in items:
                title_m = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', raw_item, flags=re.DOTALL | re.IGNORECASE)
                link_m = re.search(r'<link>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>', raw_item, flags=re.DOTALL | re.IGNORECASE)
                if not link_m:
                    link_m = re.search(r'<guid[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</guid>', raw_item, flags=re.DOTALL | re.IGNORECASE)
                pub_m = re.search(r'<(?:pubDate|dc:date)>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</(?:pubDate|dc:date)>', raw_item, flags=re.DOTALL | re.IGNORECASE)
                desc_m = re.search(r'<description>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</description>', raw_item, flags=re.DOTALL | re.IGNORECASE)

                raw_title = title_m.group(1).strip() if title_m else ""
                title = clean_title(raw_title)
                link = link_m.group(1).strip() if link_m else ""
                pub = pub_m.group(1).strip() if pub_m else ""
                desc = clean_title(desc_m.group(1)) if desc_m else ""

                if is_valid_karnataka_news(title, desc):
                    articles.append({
                        "title": title,
                        "url": link,
                        "published": pub,
                        "summary": desc[:180],
                        "source": name,
                        "forced_district": forced_dist
                    })
    except Exception as e:
        log.warning(f"  ⚠️ RSS {name} failed: {e}")

    return articles

def fetch_article_timestamp_and_title(item: dict) -> dict:
    url = item.get("url", "")
    if not url or not url.startswith("http"):
        return item

    try:
        r = requests.get(url, headers=HEADERS, timeout=4)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            
            og_t = soup.find('meta', property='og:title')
            if og_t and og_t.get('content'):
                clean_og = clean_title(og_t['content'])
                if is_valid_karnataka_news(clean_og):
                    item["title"] = clean_og

            meta_pub = soup.find('meta', property=['article:published_time', 'og:published_time', 'pubdate'])
            if meta_pub and meta_pub.get('content'):
                item["published"] = meta_pub['content'].strip()
                return item

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

def scrape_vijay_karnataka_deep() -> list:
    articles = []
    seen = set()
    portal_urls = [
        ("https://vijaykarnataka.com/news/karnataka/articlelist/10765233.cms", None),
        ("https://vijaykarnataka.com/news/bengaluru-city/articlelist/11182323.cms", "bengaluru-urban"),
        ("https://vijaykarnataka.com/news/mysuru/articlelist/11182191.cms", "mysuru"),
        ("https://vijaykarnataka.com/news/mangaluru/articlelist/11182260.cms", "dakshina-kannada"),
        ("https://vijaykarnataka.com/news/shivamogga/articlelist/11182146.cms", "shivamogga"),
        ("https://vijaykarnataka.com/news/hubballi/articlelist/11182283.cms", "dharwad"),
        ("https://vijaykarnataka.com/news/belagavi/articlelist/11182305.cms", "belagavi"),
        ("https://vijaykarnataka.com/news/karnataka/articlelist/10765233.cms?curpg=2", None),
        ("https://vijaykarnataka.com/news/karnataka/articlelist/10765233.cms?curpg=3", None),
        ("https://vijaykarnataka.com/news/karnataka/articlelist/10765233.cms?curpg=4", None)
    ]

    raw_candidates = []
    for url, f_dist in portal_urls:
        try:
            r = requests.get(url, headers=HEADERS, timeout=6)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                for a in soup.find_all('a', href=True):
                    href = a['href']
                    if '/articleshow/' in href:
                        t = clean_title(a.get_text())
                        link = 'https://vijaykarnataka.com' + href if href.startswith('/') else href
                        if is_valid_karnataka_news(t) and t not in seen:
                            seen.add(t)
                            raw_candidates.append({
                                "title": t,
                                "url": link,
                                "published": "",
                                "summary": "",
                                "source": "ವಿಜಯ ಕರ್ನಾಟಕ",
                                "forced_district": f_dist
                            })
        except Exception:
            pass

    with ThreadPoolExecutor(max_workers=14) as executor:
        futures = [executor.submit(fetch_article_timestamp_and_title, art) for art in raw_candidates[:120]]
        for f in as_completed(futures):
            try:
                res = f.result()
                if res and res.get("title"):
                    articles.append(res)
            except Exception:
                pass

    return articles

def scrape_news18_kannada_deep() -> list:
    articles = []
    seen = set()
    portal_urls = [
        ("https://kannada.news18.com/news/state/", None),
        ("https://kannada.news18.com/news/state/page-2/", None),
        ("https://kannada.news18.com/news/state/page-3/", None),
        ("https://kannada.news18.com/news/bengaluru/", "bengaluru-urban"),
        ("https://kannada.news18.com/news/mysuru/", "mysuru"),
        ("https://kannada.news18.com/news/agriculture/", None)
    ]

    raw_candidates = []
    for url, f_dist in portal_urls:
        try:
            r = requests.get(url, headers=HEADERS, timeout=6)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                for a in soup.find_all('a', href=True):
                    href = a['href']
                    if ('.html' in href or '/news/' in href or '/state/' in href) and '/photogallery/' not in href:
                        t = clean_title(a.get_text())
                        link = 'https://kannada.news18.com' + href if href.startswith('/') else href
                        if 'news18' in link and is_valid_karnataka_news(t) and t not in seen:
                            seen.add(t)
                            raw_candidates.append({
                                "title": t,
                                "url": link,
                                "published": "",
                                "summary": "",
                                "source": "ನ್ಯೂಸ್18 ಕನ್ನಡ",
                                "forced_district": f_dist
                            })
        except Exception:
            pass

    with ThreadPoolExecutor(max_workers=14) as executor:
        futures = [executor.submit(fetch_article_timestamp_and_title, art) for art in raw_candidates[:120]]
        for f in as_completed(futures):
            try:
                res = f.result()
                if res and res.get("title"):
                    articles.append(res)
            except Exception:
                pass

    return articles

def scrape_kannada_prabha_deep() -> list:
    articles = []
    seen = set()
    portal_urls = [
        "https://www.kannadaprabha.com/karnataka",
        "https://www.kannadaprabha.com/districts",
        "https://www.kannadaprabha.com/karnataka?page=2",
        "https://www.kannadaprabha.com/districts?page=2"
    ]

    raw_candidates = []
    for url in portal_urls:
        try:
            r = requests.get(url, headers=HEADERS, timeout=6)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                for a in soup.find_all('a', href=True):
                    href = a['href']
                    if '/karnataka/' in href or '/districts/' in href:
                        t = clean_title(a.get_text())
                        link = 'https://www.kannadaprabha.com' + href if href.startswith('/') else href
                        if is_valid_karnataka_news(t) and t not in seen:
                            seen.add(t)
                            raw_candidates.append({
                                "title": t,
                                "url": link,
                                "published": "",
                                "summary": "",
                                "source": "ಕನ್ನಡ ಪ್ರಭ"
                            })
        except Exception:
            pass

    with ThreadPoolExecutor(max_workers=14) as executor:
        futures = [executor.submit(fetch_article_timestamp_and_title, art) for art in raw_candidates[:120]]
        for f in as_completed(futures):
            try:
                res = f.result()
                if res and res.get("title"):
                    articles.append(res)
            except Exception:
                pass

    return articles

def scrape_prajavani_districts_deep() -> list:
    articles = []
    raw_candidates = []

    for dist_key, slug in list(PRAJAVANI_DISTRICT_SLUGS.items()):
        url = f"https://www.prajavani.net/district/{slug}"
        try:
            r = requests.get(url, headers=HEADERS, timeout=5)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                count = 0
                for a in soup.find_all('a', href=True):
                    if '/district/' in a['href'] and len(a.text.strip()) > 15:
                        t = clean_title(a.text)
                        link = 'https://www.prajavani.net' + a['href'] if a['href'].startswith('/') else a['href']
                        if is_valid_karnataka_news(t) and t not in [x['title'] for x in raw_candidates]:
                            raw_candidates.append({
                                "title": t,
                                "url": link,
                                "published": "",
                                "summary": "",
                                "source": "ಪ್ರಜಾವಾಣಿ",
                                "forced_district": dist_key
                            })
                            count += 1
                            if count >= 8: break
        except Exception:
            pass

    with ThreadPoolExecutor(max_workers=14) as executor:
        futures = [executor.submit(fetch_article_timestamp_and_title, art) for art in raw_candidates[:120]]
        for f in as_completed(futures):
            try:
                res = f.result()
                if res and res.get("title"):
                    articles.append(res)
            except Exception:
                pass

    return articles

def scrape_vijayavani_deep() -> list:
    articles = []
    seen = set()
    portal_urls = [
        "https://www.vijayavani.net/category/karnataka/",
        "https://www.vijayavani.net/category/karnataka/page/2/",
        "https://www.vijayavani.net/category/karnataka/page/3/"
    ]
    raw_candidates = []
    for url in portal_urls:
        try:
            r = requests.get(url, headers=HEADERS, timeout=6)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                for a in soup.find_all('a', href=True):
                    t = clean_title(a.get_text())
                    href = a['href']
                    if len(t) > 16 and is_valid_karnataka_news(t) and t not in seen:
                        seen.add(t)
                        raw_candidates.append({
                            "title": t,
                            "url": href,
                            "published": "",
                            "summary": "",
                            "source": "ವಿಜಯವಾಣಿ"
                        })
        except Exception:
            pass

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(fetch_article_timestamp_and_title, art) for art in raw_candidates[:60]]
        for f in as_completed(futures):
            try:
                res = f.result()
                if res and res.get("title"):
                    articles.append(res)
            except Exception:
                pass

    return articles

def assign_district(article: dict) -> str:
    if article.get("forced_district") and article["forced_district"] in DISTRICT_GEOLOCATION:
        return article["forced_district"]

    title = article.get("title", "")
    summary = article.get("summary", "")
    url = article.get("url", "")
    full_text = (title + " " + summary + " " + url).lower()

    # Priority 1: Check Dateline Prefix in title (e.g. "ಮಂಗಳೂರು: ...", "Kolar | ...", "ಯಾದಗಿರಿ: ...")
    dateline = re.match(r'^([\u0C80-\u0CFFa-zA-Z\s]+)[:|-]', title)
    if dateline:
        dl_word = dateline.group(1).strip().lower()
        for dist_key, kw_list in DISTRICT_KEYWORDS.items():
            if any(kw.lower() in dl_word for kw in kw_list):
                return dist_key

    # Priority 2: Check all non-Bengaluru districts in Headline first (Strongest Match)
    for dist_key, kw_list in DISTRICT_KEYWORDS.items():
        if dist_key != "bengaluru-urban":
            for kw in kw_list:
                kw_l = kw.lower()
                if kw_l in title.lower():
                    return dist_key

    # Priority 3: Check all non-Bengaluru districts in Summary/Text/URL
    for dist_key, kw_list in DISTRICT_KEYWORDS.items():
        if dist_key != "bengaluru-urban":
            for kw in kw_list:
                kw_l = kw.lower()
                if kw_l in full_text:
                    return dist_key

    # Priority 4: Bengaluru Urban
    for kw in DISTRICT_KEYWORDS["bengaluru-urban"]:
        if kw.lower() in full_text:
            return "bengaluru-urban"

    return "_statewide"

def compute_dynamic_trending_tags(articles: list) -> list:
    entity_counts = Counter()
    
    curated_trending_entities = [
        "ಮುಡಾ", "ವಾಲ್ಮೀಕಿ ನಿಗಮ", "ಸಚಿವ ಸಂಪುಟ", "ಸಿದ್ದರಾಮಯ್ಯ", "ಡಿಕೆ ಶಿವಕುಮಾರ್",
        "ನಮ್ಮ ಮೆಟ್ರೋ", "ಮುಂಗಾರು ಮಳೆ", "ಕಾವೇರಿ ನೀರು", "ಕೆಆರ್‌ಎಸ್ ಜಲಾಶಯ", "ತುಂಗಭದ್ರಾ ಡ್ಯಾಂ",
        "ಆಲಮಟ್ಟಿ", "ಅಡಿಕೆ ಬೆಲೆ", "ರೈತರ ಪ್ರತಿಭಟನೆ", "ಗ್ಯಾರಂಟಿ ಯೋಜನೆ", "ಗೃಹಲಕ್ಷ್ಮಿ",
        "ಯುವನಿಧಿ", "ಶಕ್ತಿ ಯೋಜನೆ", "ಅನ್ನಭಾಗ್ಯ", "ಚನ್ನಪಟ್ಟಣ", "ಲೋಕಾಯುಕ್ತ", "ಹೈಕೋರ್ಟ್",
        "ಚಿನ್ನದ ಬೆಲೆ", "ಪೆಟ್ರೋಲ್ ಬೆಲೆ", "ವಿದ್ಯುತ್ ದರ", "ದಸರಾ ಮಹೋತ್ಸವ",
        "ಬೆಂಗಳೂರು ಟ್ರಾಫಿಕ್", "ಮೈಸೂರು ಅರಮನೆ", "ಕಾಂಗ್ರೆಸ್", "ಬಿಜೆಪಿ", "ಜೆಡಿಎಸ್"
    ]

    for a in articles:
        text = (a.get("title", "") + " " + a.get("summary", "")).lower()
        for ent in curated_trending_entities:
            if ent.lower() in text:
                entity_counts[ent] += 1

    top_tags = []
    for ent, count in entity_counts.most_common(12):
        if count >= 2:
            top_tags.append({"tag": ent, "count": count})

    return top_tags

def load_existing_database() -> dict:
    existing_buckets = {k: [] for k in DISTRICT_GEOLOCATION.keys()}
    existing_buckets["_statewide"] = []
    
    file_path = DATA_DIR / "local_news.json"
    if not file_path.exists():
        return existing_buckets

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            raw = json.load(f)
            buckets = raw.get("district_buckets") or raw.get("districts") or {}
            for k, items in buckets.items():
                if k in existing_buckets and isinstance(items, list):
                    # Filter out old horoscope/lifestyle
                    cleaned = [it for it in items if is_valid_karnataka_news(it.get("title", ""), it.get("summary", ""))]
                    existing_buckets[k] = cleaned
    except Exception as e:
        log.warning(f"Could not load previous database: {e}")

    return existing_buckets

def run() -> dict:
    log.info("📰 Starting Deep High-Volume Karnataka District News Scraper...")

    raw_articles = []

    for src in RSS_SOURCES:
        raw_articles.extend(scrape_rss_feed(src))

    raw_articles.extend(scrape_vijay_karnataka_deep())
    raw_articles.extend(scrape_news18_kannada_deep())
    raw_articles.extend(scrape_kannada_prabha_deep())
    raw_articles.extend(scrape_prajavani_districts_deep())
    raw_articles.extend(scrape_vijayavani_deep())

    log.info(f"📰 Total freshly scraped Karnataka articles across all publishers: {len(raw_articles)}")

    district_buckets = load_existing_database()

    seen_urls = set()
    seen_titles = set()

    for k, items in district_buckets.items():
        for it in items:
            if it.get("url"): seen_urls.add(it["url"])
            if it.get("title"): seen_titles.add(clean_title(it["title"]).lower())

    new_added = 0
    for art in raw_articles:
        t = clean_title(art["title"])
        if not is_valid_karnataka_news(t, art.get("summary", "")):
            continue
        art["title"] = t
        norm_t = t.lower()
        url = art.get("url", "")

        if (url and url in seen_urls) or norm_t in seen_titles:
            continue

        if url: seen_urls.add(url)
        seen_titles.add(norm_t)

        dist = assign_district(art)
        art["district"] = dist
        art["districtKey"] = dist

        if dist in district_buckets:
            district_buckets[dist].append(art)
        else:
            district_buckets["_statewide"].append(art)
        new_added += 1

    log.info(f"✨ Merged {new_added} brand-new articles into cumulative historical database.")

    # Flatten and sort — latest articles first!
    all_flat = []
    for d_key in district_buckets:
        for item in district_buckets[d_key]:
            item["district"] = d_key
            item["districtKey"] = d_key

        district_buckets[d_key].sort(
            key=lambda x: parse_date_to_timestamp(x.get("published")),
            reverse=True
        )
        max_limit = 1200 if d_key == "_statewide" else 200
        district_buckets[d_key] = district_buckets[d_key][:max_limit]
        all_flat.extend(district_buckets[d_key])

    all_flat.sort(
        key=lambda x: parse_date_to_timestamp(x.get("published")),
        reverse=True
    )

    trending_tags = compute_dynamic_trending_tags(all_flat)

    total_articles = len(all_flat)

    if total_articles > 0:
        output = {
            "date": ist_date(),
            "updated_at": ist_now(),
            "total": total_articles,
            "districts_count": len(DISTRICT_GEOLOCATION),
            "district_buckets": district_buckets,
            "articles": all_flat,
            "trending_tags": trending_tags,
            "sources": [
                "ವಿಜಯ ಕರ್ನಾಟಕ", "ಪ್ರಜಾವಾಣಿ", "TV9 ಕನ್ನಡ", "ಏಷ್ಯಾನೆಟ್ ಸುವರ್ಣ",
                "ನ್ಯೂಸ್18 ಕನ್ನಡ", "ಕನ್ನಡ ಪ್ರಭ", "ಪಬ್ಲಿಕ್ ಟಿವಿ", "ಹೊಸ ದಿಗಂತ",
                "ಸಂಯುಕ್ತ ಕರ್ನಾಟಕ", "ಈ ಸಂಜೆ", "ಉದಯವಾಣಿ", "ವಿಜಯವಾಣಿ", "ಒನ್‌ಇಂಡಿಯಾ", "ಶಿವಮೊಗ್ಗ ಲೈವ್", "ಜಸ್ಟ್ ಕನ್ನಡ"
            ],
            "note_kn": "ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಪ್ರಮುಖ ಸುದ್ದಿವಾಹಿನಿಗಳಿಂದ ಸಂಗ್ರಹಿಸಲಾದ ಸಜೀವ ಸುದ್ದಿಗಳು"
        }

        save_json("local_news.json", output)
        log.info(f"✅ Karnataka Multi-Source News Saved: {total_articles} articles across 32 district buckets with Dynamic Trending Tags")
        return output
    else:
        log.warning("⚠️ 0 articles in cumulative database — keeping existing local_news.json intact.")
        from utils import load_json
        return load_json("local_news.json", {})

if __name__ == "__main__":
    run()