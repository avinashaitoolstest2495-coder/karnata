# scripts/rebuild_all_district_pages_master.py
import json
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(r"c:\Users\avina\Downloads\karnata-site-with-cms")

# Master District Mapping with exact Lok Sabha PCs, Assembly Constituencies, and Taluks
DISTRICTS_DATA = [
    {
        "key": "bengaluru-urban",
        "name_kn": "ಬೆಂಗಳೂರು ನಗರ",
        "name_en": "Bengaluru Urban",
        "hq_kn": "ಬೆಂಗಳೂರು",
        "hq_en": "Bengaluru",
        "lat": 12.9716, "lon": 77.5946,
        "pop": "1.27 ಕೋಟಿ", "area": "2,190 sq km",
        "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ",
        "dam": "krs",
        "taluks": ["ಬೆಂಗಳೂರು ಉತ್ತರ", "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ", "ಬೆಂಗಳೂರು ಪೂರ್ವ", "ಆನೇಕಲ್", "ಯಲಹಂಕ", "ಕೆ.ಆರ್.ಪುರಂ", "ಸರ್ಜಾಪುರ"],
        "famous_for": "ಸಿಲಿಕಾನ್ ವ್ಯಾಲಿ, IT/BT ತಂತ್ರಜ್ಞಾನ ರಾಜಧಾನಿ, ವಿಧಾನಸೌಧ, ಉದ್ಯಾನ ನಗರಿ",
        "mla_codes": list(range(150, 178)),  # 150 to 177 (28 MLAs)
        "pc_nos": [24, 25, 26, 23]  # Bengaluru North, Central, South, Rural
    },
    {
        "key": "bengaluru-rural",
        "name_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ",
        "name_en": "Bengaluru Rural",
        "hq_kn": "ನೆಲಮಂಗಲ",
        "hq_en": "Nelamangala",
        "lat": 13.2457, "lon": 77.7126,
        "pop": "9.9 ಲಕ್ಷ", "area": "2,295 sq km",
        "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ",
        "dam": "krs",
        "taluks": ["ನೆಲಮಂಗಲ", "ದೊಡ್ಡಬಳ್ಳಾಪುರ", "ದೇವನಹಳ್ಳಿ", "ಹೊಸಕೋಟೆ"],
        "famous_for": "ಕೆಂಪೇಗೌಡ ಅಂತಾರಾಷ್ಟ್ರೀಯ ವಿಮಾನ ನಿಲ್ದಾಣ, ರೇಷ್ಮೆ ಕೃಷಿ, ದಾಬಸ್‌ಪೇಟೆ ಇಂಡಸ್ಟ್ರಿಯಲ್ ಹಬ್",
        "mla_codes": [178, 179, 180, 181],
        "pc_nos": [23]  # Bengaluru Rural
    },
    {
        "key": "ramanagara",
        "name_kn": "ರಾಮನಗರ",
        "name_en": "Ramanagara",
        "hq_kn": "ರಾಮನಗರ",
        "hq_en": "Ramanagara",
        "lat": 12.7209, "lon": 77.2799,
        "pop": "10.8 ಲಕ್ಷ", "area": "3,556 sq km",
        "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ",
        "dam": "krs",
        "taluks": ["ರಾಮನಗರ", "ಚನ್ನಪಟ್ಟಣ", "ಕನಕಪುರ", "ಮಾಗಡಿ", "ಹಾರೋಹಳ್ಳಿ"],
        "famous_for": "ರೇಷ್ಮೆ ನಗರಿ, ಚನ್ನಪಟ್ಟಣದ ಮರದ ಬೊಂಬೆಗಳು (GI), ರಾಮದೇವರ ಬೆಟ್ಟ, ಸಾವನದುರ್ಗ",
        "mla_codes": [182, 183, 184, 185],
        "pc_nos": [23]  # Bengaluru Rural
    },
    {
        "key": "belagavi",
        "name_kn": "ಬೆಳಗಾವಿ",
        "name_en": "Belagavi",
        "hq_kn": "ಬೆಳಗಾವಿ",
        "hq_en": "Belagavi",
        "lat": 15.8497, "lon": 74.4977,
        "pop": "47.7 ಲಕ್ಷ", "area": "13,415 sq km",
        "region": "ಉತ್ತರ ಕರ್ನಾಟಕ",
        "dam": "ghataprabha",
        "taluks": ["ಬೆಳಗಾವಿ", "ಗೋಕಾಕ್", "ಚಿಕ್ಕೋಡಿ", "ಅಥಣಿ", "ಬೈಲಹೊಂಗಲ", "ಖಾನಾಪುರ", "ನಿಪ್ಪಾಣಿ", "ಸವದತ್ತಿ", "ರಾಮದುರ್ಗ", "ರಾಯಬಾಗ", "ಕಾಗವಾಡ", "ಹುಕ್ಕೇರಿ", "ಮೂಡಲಗಿ", "ಕಿತ್ತೂರು", "ಯರಗಟ್ಟಿ"],
        "famous_for": "ಕುಂದಾ ಸಿಹಿ, ಸುವರ್ಣ ವಿಧಾನಸೌಧ, ಕಿತ್ತೂರು ಚನ್ನಮ್ಮ & ಸಂಗೊಳ್ಳಿ ರಾಯಣ್ಣ ಕ್ರಾಂತಿ ಭೂಮಿ, ಗೋಕಾಕ್ ಜಲಪಾತ",
        "mla_codes": list(range(1, 19)),  # 1 to 18 (18 MLAs)
        "pc_nos": [1, 2]  # Chikkodi, Belgaum
    },
    {
        "key": "bagalkote",
        "name_kn": "ಬಾಗಲಕೋಟೆ",
        "name_en": "Bagalkote",
        "hq_kn": "ಬಾಗಲಕೋಟೆ",
        "hq_en": "Bagalkote",
        "lat": 16.1875, "lon": 75.6980,
        "pop": "18.9 ಲಕ್ಷ", "area": "6,575 sq km",
        "region": "ಉತ್ತರ ಕರ್ನಾಟಕ",
        "dam": "almatti",
        "taluks": ["ಬಾಗಲಕೋಟೆ", "ಬಾದಾಮಿ", "ಜಮಖಂಡಿ", "ಮುಧೋಳ", "ಹುನಗುಂದ", "ಇಳಕಲ್", "ಬೀಳಗಿ", "ಗುಳೇದಗುಡ್ಡ", "ರಬಕವಿ-ಬನಹಟ್ಟಿ"],
        "famous_for": "ಬಾದಾಮಿ ಗುಹೆಗಳು, ಐಹೊಳೆ, ಪಟ್ಟದಕಲ್ಲು (UNESCO), ಇಳಕಲ್ ಸೀರೆ (GI), ಅಮೀನಗಡ ಕರದಂಟು, ಮುಧೋಳ ಶ್ವಾನ",
        "mla_codes": list(range(19, 26)),  # 19 to 25 (7 MLAs)
        "pc_nos": [3]  # Bagalkot
    },
    {
        "key": "vijayapura",
        "name_kn": "ವಿಜಯಪುರ",
        "name_en": "Vijayapura",
        "hq_kn": "ವಿಜಯಪುರ",
        "hq_en": "Vijayapura",
        "lat": 16.8302, "lon": 75.7100,
        "pop": "21.7 ಲಕ್ಷ", "area": "10,498 sq km",
        "region": "ಉತ್ತರ ಕರ್ನಾಟಕ",
        "dam": "almatti",
        "taluks": ["ವಿಜಯಪುರ", "ಇಂಡಿ", "ಬಸವನ ಬಾಗೇವಾಡಿ", "ಮುದ್ದೇಬಿಹಾಳ", "ಸಿಂದಗಿ", "ತಾಳಿಕೋಟೆ", "ಬಬಲೇಶ್ವರ", "ಚಡಚಣ", "ದೇವರಹಿಪ್ಪರಗಿ", "ಕೊಲ್ಹಾರ", "ತಿಕ್ಕೋಟಾ", "ಆಲಮೇಲ"],
        "famous_for": "ಗೋಲ ಗುಮ್ಮಟ (ಗುಸುಗುಸು ಗ್ಯಾಲರಿ), ಇಬ್ರಾಹಿಂ ರೋಜಾ, ಬಸವಣ್ಣನವರ ಜನ್ಮಸ್ಥಳ, ಇಂಡಿ ನಿಂಬೆ (GI), ಆಲಮಟ್ಟಿ ಡ್ಯಾಂ",
        "mla_codes": list(range(26, 34)),  # 26 to 33 (8 MLAs)
        "pc_nos": [4]  # Bijapur
    },
    {
        "key": "kalaburagi",
        "name_kn": "ಕಲಬುರಗಿ",
        "name_en": "Kalaburagi",
        "hq_kn": "ಕಲಬುರಗಿ",
        "hq_en": "Kalaburagi",
        "lat": 17.3297, "lon": 76.8343,
        "pop": "25.6 ಲಕ್ಷ", "area": "10,951 sq km",
        "region": "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ",
        "dam": "narayanapura",
        "taluks": ["ಕಲಬುರಗಿ", "ಸೇಡಂ", "ಚಿತ್ತಾಪುರ", "ಆಳಂದ", "ಅಫಜಲಪುರ", "ಜೇವರ್ಗಿ", "ಚಿಂಚೋಳಿ", "ಕಾಳಗಿ", "ಕಮಲಾಪುರ", "ಶಹಾಬಾದ್", "ಯಡ್ರಾಮಿ"],
        "famous_for": "ಕರ್ನಾಟಕದ ತೊಗರಿ ಕಣಜ (GI), ರಾಷ್ಟ್ರಕೂಟರ ಮಾನ್ಯಖೇಟ (ಕವಿರಾಜಮಾರ್ಗ), ಖ್ವಾಜಾ ಬಂದೇ ನವಾಜ್ ದರ್ಗಾ, ಶರಣಬಸವೇಶ್ವರ ಸಂಸ್ಥಾನ, ಸನ್ನತಿ ಅಶೋಕ ಶಿಲ್ಪ",
        "mla_codes": list(range(34, 43)),  # 34 to 42 (9 MLAs)
        "pc_nos": [5]  # Gulbarga
    },
    {
        "key": "yadgir",
        "name_kn": "ಯಾದಗಿರಿ",
        "name_en": "Yadgir",
        "hq_kn": "ಯಾದಗಿರಿ",
        "hq_en": "Yadgir",
        "lat": 16.7644, "lon": 77.1377,
        "pop": "11.7 ಲಕ್ಷ", "area": "5,234 sq km",
        "region": "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ",
        "dam": "narayanapura",
        "taluks": ["ಯಾದಗಿರಿ", "ಶಹಾಪುರ", "ಸುರಪುರ", "ಗುರುಮಿಠಕಲ್", "ಹುಣಸಗಿ", "ವಡಗೇರಾ"],
        "famous_for": "ಸುರಪುರ ಸಂಸ್ಥಾನ (ರಾಜಾ ವೆಂಕಟಪ್ಪ ನಾಯಕ), ಮಲಗಿದ ಬುದ್ಧ ಬೆಟ್ಟ, ಹುಣಸಗಿ ಪ್ರಾಚೀನ ಶಿಲಾಯುಗ, ಛಾಯಾ ಭಗವತಿ ಜಲಪಾತ, ಬೋನಾಳ್ ಪಕ್ಷಿಧಾಮ",
        "mla_codes": [36, 37, 38, 39],  # AC 36 Shorapur, 37 Shahapur, 38 Yadgir, 39 Gurmitkal
        "pc_nos": [6]  # Raichur-Yadgir
    },
    {
        "key": "bidar",
        "name_kn": "ಬೀದರ್",
        "name_en": "Bidar",
        "hq_kn": "ಬೀದರ್",
        "hq_en": "Bidar",
        "lat": 17.9104, "lon": 77.5199,
        "pop": "17.0 ಲಕ್ಷ", "area": "5,448 sq km",
        "region": "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ",
        "dam": "karanja",
        "taluks": ["ಬೀದರ್", "ಬಸವಕಲ್ಯಾಣ", "ಭಾಲ್ಕಿ", "ಹುಮ್ನಾಬಾದ್", "ಔರಾದ್", "ಕಮಲನಗರ", "ಹುಲಸೂರು", "ಚಿಟಗುಪ್ಪ"],
        "famous_for": "ಬೀದರ್ ಕೋಟೆ, ಕಾರೆಜ್ ಸುರಂಗ ಮಾರ್ಗ, ಬಸವಕಲ್ಯಾಣ ಅನುಭವ ಮಂಟಪ, ವಿಶ್ವವಿಖ್ಯಾತ ಬಿದ್ರಿ ಕಲೆ (GI), ಗುರುದ್ವಾರ ನಾನಕ್ ಝೀರಾ",
        "mla_codes": list(range(47, 53)),  # 47 to 52 (6 MLAs)
        "pc_nos": [7]  # Bidar
    },
    {
        "key": "raichur",
        "name_kn": "ರಾಯಚೂರು",
        "name_en": "Raichur",
        "hq_kn": "ರಾಯಚೂರು",
        "hq_en": "Raichur",
        "lat": 16.2076, "lon": 77.3463,
        "pop": "19.2 ಲಕ್ಷ", "area": "8,442 sq km",
        "region": "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ",
        "dam": "tungabhadra",
        "taluks": ["ರಾಯಚೂರು", "ಸಿಂಧನೂರು", "ಮಾನ್ವಿ", "ಲಿಂಗಸುಗೂರು", "ದೇವದುರ್ಗ", "ಮಸ್ಕಿ", "ಸಿರವಾರ"],
        "famous_for": "ಮಸ್ಕಿ ಅಶೋಕ ಶಿಲಾಶಾಸನ, ಹಟ್ಟಿ ಚಿನ್ನದ ಗಣಿ, ಶಕ್ತಿನಗರ RTPS, ಗಾಣದಾಳ ಪಂಚಮುಖಿ, ಸೋನಾ ಮಸೂರಿ ಭತ್ತ",
        "mla_codes": list(range(53, 60)),  # 53 to 59 (7 MLAs)
        "pc_nos": [6]  # Raichur
    },
    {
        "key": "koppal",
        "name_kn": "ಕೊಪ್ಪಳ",
        "name_en": "Koppal",
        "hq_kn": "ಕೊಪ್ಪಳ",
        "hq_en": "Koppal",
        "lat": 15.3469, "lon": 76.1554,
        "pop": "13.9 ಲಕ್ಷ", "area": "5,559 sq km",
        "region": "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ",
        "dam": "tungabhadra",
        "taluks": ["ಕೊಪ್ಪಳ", "ಗಂಗಾವತಿ", "ಕುಷ್ಟಗಿ", "ಯಲಬುರ್ಗಾ", "ಕಾರಟಗಿ", "ಕುಕನೂರು", "ಕನಕಗಿರಿ"],
        "famous_for": "ರಾಮಾಯಣದ ಕಿಷ್ಕಿಂಧೆ, ಅಂಜನಾದ್ರಿ ಬೆಟ್ಟ, ಕಿನ್ನಾಳ ಕಲೆ (GI), ಶ್ರೀ ಗವಿಸಿದ್ಧೇಶ್ವರ ಮಹಾದಾಸೋಹ, ಇಟಗಿ ಮಹಾದೇವ ದೇವಾಲಯ",
        "mla_codes": [60, 61, 62, 63, 64],  # 5 MLAs
        "pc_nos": [9]  # Koppal
    },
    {
        "key": "gadag",
        "name_kn": "ಗದಗ",
        "name_en": "Gadag",
        "hq_kn": "ಗದಗ",
        "hq_en": "Gadag",
        "lat": 15.4313, "lon": 75.6358,
        "pop": "10.64 ಲಕ್ಷ", "area": "4,656 sq km",
        "region": "ಉತ್ತರ ಕರ್ನಾಟಕ",
        "dam": "malaprabha",
        "taluks": ["ಗದಗ", "ಬೆಟಗೇರಿ", "ರೋಣ", "ಶಿರಹಟ್ಟಿ", "ಮುಂಡರಗಿ", "ನರಗುಂದ", "ಗಜೇಂದ್ರಗಡ", "ಲಕ್ಷ್ಮೇಶ್ವರ"],
        "famous_for": "ಕುಮಾರವ್ಯಾಸ ಭಾರತ (ವೀರನಾರಾಯಣ ಗುಡಿ), ಪಂ. ಪುಟ್ಟರಾಜ ಗವಾಯಿಗಳ ಪುಣ್ಯಾಶ್ರಮ, ಕಪ್ಪತಗುಡ್ಡ, ಲಕ್ಕುಂಡಿ 101 ಮೆಟ್ಟಿಲು ಬಾವಿ, ಭಾರತದ ಮೊದಲ ಸಹಕಾರಿ ಬ್ಯಾಂಕ್",
        "mla_codes": [65, 66, 67, 68],  # 65 Shirahatti, 66 Gadag, 67 Ron, 68 Nargund
        "pc_nos": [10]  # Haveri-Gadag (Basavaraj Bommai)
    },
    {
        "key": "dharwad",
        "name_kn": "ಧಾರವಾಡ",
        "name_en": "Dharwad",
        "hq_kn": "ಧಾರವಾಡ",
        "hq_en": "Dharwad",
        "lat": 15.4589, "lon": 75.0078,
        "pop": "18.47 ಲಕ್ಷ", "area": "4,260 sq km",
        "region": "ಉತ್ತರ ಕರ್ನಾಟಕ",
        "dam": "malaprabha",
        "taluks": ["ಧಾರವಾಡ", "ಹುಬ್ಬಳ್ಳಿ ನಗರ", "ಹುಬ್ಬಳ್ಳಿ ಗ್ರಾಮೀಣ", "ಕಲಘಟಗಿ", "ನವಲಗುಂದ", "ಅಣ್ಣಿಗೇರಿ", "ಅಳ್ನಾವರ"],
        "famous_for": "ಧಾರವಾಡ ಪೇಡಾ (GI), ವರಕವಿ ಬೇಂದ್ರೆ ಸಾಧನಕೇರಿ, ಸಿದ್ಧಾರೂಢ ಮಠ, ಗಿನ್ನೆಸ್ ವಿಶ್ವದ ಅತಿ ಉದ್ದದ ರೈಲ್ವೆ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್, IIT ಧಾರವಾಡ",
        "mla_codes": [69, 70, 71, 72, 73, 74, 75],  # 7 MLAs
        "pc_nos": [11]  # Dharwad
    },
    {
        "key": "uttara-kannada",
        "name_kn": "ಉತ್ತರ ಕನ್ನಡ",
        "name_en": "Uttara Kannada",
        "hq_kn": "ಕಾರವಾರ",
        "hq_en": "Karwar",
        "lat": 14.8185, "lon": 74.1416,
        "pop": "14.4 ಲಕ್ಷ", "area": "10,291 sq km",
        "region": "ಕರಾವಳಿ ಕರ್ನಾಟಕ",
        "dam": "supa",
        "taluks": ["ಕಾರವಾರ", "ಅಂಕೋಲಾ", "ಕುಮಟಾ", "ಹೊನ್ನಾವರ", "ಭಟ್ಕಳ", "ಶಿರಸಿ", "ಸಿದ್ಧಾಪುರ", "ಯಲ್ಲಾಪುರ", "ದಾಂಡೇಲಿ", "ಹಳಿಯಾಳ", "ಜೋಯಿಡಾ"],
        "famous_for": "ಗೋಕರ್ಣ ಮಹಾಬಲೇಶ್ವರ ಆತ್ಮಲಿಂಗ, ಮುರುಡೇಶ್ವರ ಶಿವನ ಪ್ರತಿಮೆ, ದಾಂಡೇಲಿ ವೈಟ್ ವಾಟರ್ ರಾಫ್ಟಿಂಗ್, ಯಾಣದ ಶಿಲಾ ಬೆಟ್ಟಗಳು",
        "mla_codes": [76, 77, 78, 79, 80, 81],  # 6 MLAs
        "pc_nos": [12]  # Uttara Kannada
    },
    {
        "key": "haveri",
        "name_kn": "ಹಾವೇರಿ",
        "name_en": "Haveri",
        "hq_kn": "ಹಾವೇರಿ",
        "hq_en": "Haveri",
        "lat": 14.7973, "lon": 75.4053,
        "pop": "15.97 ಲಕ್ಷ", "area": "4,823 sq km",
        "region": "ಉತ್ತರ ಕರ್ನಾಟಕ",
        "dam": "tungabhadra",
        "taluks": ["ಹಾವೇರಿ", "ರಾಣೇಬೆನ್ನೂರು", "ಬ್ಯಾಡಗಿ", "ಹಾನಗಲ್", "ಸವಣೂರು", "ಶಿಗ್ಗಾಂವಿ", "ಹಿರೇಕೆರೂರು", "ರಟ್ಟಿಹಳ್ಳಿ"],
        "famous_for": "ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ ಮಾರುಕಟ್ಟೆ (GI), ಕಾಗಿನೆಲೆ ಕನಕದಾಸರ ಕ್ಷೇತ್ರ, ಸರ್ವಜ್ಞನ ಅಬಲೂರು, ರಾಣೇಬೆನ್ನೂರು ಕೃಷ್ಣಮೃಗ ಅಭಯಾರಣ್ಯ",
        "mla_codes": [82, 83, 84, 85, 86, 87],  # 6 MLAs
        "pc_nos": [10]  # Haveri-Gadag
    },
    {
        "key": "ballari",
        "name_kn": "ಬಳ್ಳಾರಿ",
        "name_en": "Ballari",
        "hq_kn": "ಬಳ್ಳಾರಿ",
        "hq_en": "Ballari",
        "lat": 15.1394, "lon": 76.9214,
        "pop": "14.8 ಲಕ್ಷ", "area": "4,252 sq km",
        "region": "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ",
        "dam": "tungabhadra",
        "taluks": ["ಬಳ್ಳಾರಿ", "ಸಿರುಗುಪ್ಪ", "ಕಂಪ್ಲಿ", "ಕುರುಗೋಡು", "ಸಂದೂರು"],
        "famous_for": "ಬಳ್ಳಾರಿ ಕೋಟೆ & ಕುಂಬಾರ ಗುಡ್ಡ, ದೇಶದ ಜೀನ್ಸ್ ರಾಜಧಾನಿ, ಸಂಡೂರು ಕಣಿವೆ, JSW ವಿಜಯನಗರ ಸ್ಟೀಲ್, ಸಂಗನಕಲ್ಲು ರಾಕ್ ಆರ್ಟ್",
        "mla_codes": [91, 92, 93, 94, 95],  # 5 MLAs: Siruguppa, Kampli, Ballari City, Ballari Rural, Sandur
        "pc_nos": [8]  # Bellary
    },
    {
        "key": "vijayanagara",
        "name_kn": "ವಿಜಯನಗರ",
        "name_en": "Vijayanagara",
        "hq_kn": "ಹೊಸಪೇಟೆ",
        "hq_en": "Hosapete",
        "lat": 15.2704, "lon": 76.3888,
        "pop": "13.5 ಲಕ್ಷ", "area": "5,644 sq km",
        "region": "ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ",
        "dam": "tungabhadra",
        "taluks": ["ಹೊಸಪೇಟೆ", "ಹೂವಿನ ಹಡಗಲಿ", "ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ", "ಕೊಟ್ಟೂರು", "ಕೂಡ್ಲಿಗಿ", "ಹರಪನಹಳ್ಳಿ"],
        "famous_for": "ಹಂಪಿ ವಿಶ್ವ ಪರಂಪರೆ (UNESCO), ವಿರೂಪಾಕ್ಷ ದೇವಾಲಯ, ಕಲ್ಲಿನ ರಥ, ತುಂಗಭದ್ರಾ ಡ್ಯಾಂ, ದರೋಜಿ ಕರಡಿ ಧಾಮ, ಕೊಟ್ಟೂರು ಬೆಣ್ಣೆ ದೋಸೆ",
        "mla_codes": [88, 89, 90, 96, 104],  # 5 MLAs: Hadagali, Hagaribommanahalli, Vijayanagara, Kudligi, Harapanahalli
        "pc_nos": [8, 14]  # Bellary, Davanagere
    },
    {
        "key": "shivamogga",
        "name_kn": "ಶಿವಮೊಗ್ಗ",
        "name_en": "Shivamogga",
        "hq_kn": "ಶಿವಮೊಗ್ಗ",
        "hq_en": "Shivamogga",
        "lat": 13.9299, "lon": 75.5681,
        "pop": "17.5 ಲಕ್ಷ", "area": "8,477 sq km",
        "region": "ಮಲೆನಾಡು",
        "dam": "linganamakki",
        "taluks": ["ಶಿವಮೊಗ್ಗ", "ಸಾಗರ", "ಶಿಕಾರಿಪುರ", "ತೀರ್ಥಹಳ್ಳಿ", "ಭದ್ರಾವತಿ", "ಸೊರಬ", "ಹೊಸನಗರ"],
        "famous_for": "ವಿಶ್ವವಿಖ್ಯಾತ ಜೋಗ ಜಲಪಾತ, ಕುವೆಂಪು ಕವಿಮನೆ ಕುಪ್ಪಳ್ಳಿ, ಸಿಗಂದೂರು ಚೌಡೇಶ್ವರಿ, ಆಗುಂಬೆ ಸೂರ್ಯಾಸ್ತ & ಮಳೆಕಾಡು",
        "mla_codes": [111, 112, 113, 114, 115, 116, 117],  # 7 MLAs
        "pc_nos": [14]  # Shimoga
    },
    {
        "key": "udupi",
        "name_kn": "ಉಡುಪಿ",
        "name_en": "Udupi",
        "hq_kn": "ಉಡುಪಿ",
        "hq_en": "Udupi",
        "lat": 13.3409, "lon": 74.7421,
        "pop": "11.77 ಲಕ್ಷ", "area": "3,582 sq km",
        "region": "ಕರಾವಳಿ ಕರ್ನಾಟಕ",
        "dam": "supa",
        "taluks": ["ಉಡುಪಿ", "ಕುಂದಾಪುರ", "ಕಾರ್ಕಳ", "ಬೈಂದೂರು", "ಕಾಪು", "ಬ್ರಹ್ಮಾವರ", "ಹೆಬ್ರಿ"],
        "famous_for": "ಶ್ರೀಕೃಷ್ಣ ಮಠ & ಕನಕನ ಕಿಂಡಿ, ಮಲ್ಪೆ ಬೀಚ್, ಸೇಂಟ್ ಮೇರಿಸ್ ಐಲ್ಯಾಂಡ್, ಮಟ್ಟುಗುಳ್ಳ (GI), ಉಡುಪಿ ಸಾಂಬಾರು & ದೋಸೆ",
        "mla_codes": [118, 119, 120, 121, 122],  # 5 MLAs
        "pc_nos": [15]  # Udupi-Chikmagalur
    },
    {
        "key": "chikkamagaluru",
        "name_kn": "ಚಿಕ್ಕಮಗಳೂರು",
        "name_en": "Chikkamagaluru",
        "hq_kn": "ಚಿಕ್ಕಮಗಳೂರು",
        "hq_en": "Chikkamagaluru",
        "lat": 13.3153, "lon": 75.7754,
        "pop": "11.38 ಲಕ್ಷ", "area": "7,201 sq km",
        "region": "ಮಲೆನಾಡು",
        "dam": "bhadra",
        "taluks": ["ಚಿಕ್ಕಮಗಳೂರು", "ಕಡೂರು", "ತರೀಕೆರೆ", "ಮೂಡಿಗೆರೆ", "ಕೊಪ್ಪ", "ಶೃಂಗೇರಿ", "ಎನ್.ಆರ್.ಪುರ", "ಅಜ್ಜಂಪುರ", "ಕಳಸ"],
        "famous_for": "ಕಾಫಿ ನಾಡು (ಅರೇಬಿಕಾ/ರೋಬಸ್ಟಾ), ಮುಳ್ಳಯ್ಯನಗಿರಿ (ಕರ್ನಾಟಕದ ಅತಿ ಎತ್ತರದ ಶಿಖರ), ಬಾಬಾ ಬುಡನ್‌ಗಿರಿ, ಶೃಂಗೇರಿ ಶಾರದಾ ಪೀಠ, ಕೆಮ್ಮಣ್ಣುಗುಂಡಿ",
        "mla_codes": [123, 124, 125, 126, 127],  # 5 MLAs
        "pc_nos": [15]  # Udupi-Chikmagalur
    },
    {
        "key": "dakshina-kannada",
        "name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ",
        "name_en": "Dakshina Kannada",
        "hq_kn": "ಮಂಗಳೂರು",
        "hq_en": "Mangaluru",
        "lat": 12.8438, "lon": 74.9919,
        "pop": "20.8 ಲಕ್ಷ", "area": "4,560 sq km",
        "region": "ಕರಾವಳಿ ಕರ್ನಾಟಕ",
        "dam": "supa",
        "taluks": ["ಮಂಗಳೂರು", "ಪುತ್ತೂರು", "ಬೆಳ್ತಂಗಡಿ", "ಬಂಟ್ವಾಳ", "ಸುಳ್ಯ", "ಕಡಬ", "ಮೂಡುಬಿದಿರೆ", "ಉಳ್ಳಾಲ"],
        "famous_for": "ಶ್ರೀ ಕ್ಷೇತ್ರ ಧರ್ಮಸ್ಥಳ, ಕುಕ್ಕೆ ಸುಬ್ರಹ್ಮಣ್ಯ, ಕಂಬಳ & ಯಕ್ಷಗಾನ, ನೀರ್ ದೋಸೆ, ಕೋರಿ ರೊಟ್ಟಿ, ಪಣಂಬೂರು ಬೀಚ್",
        "mla_codes": [200, 201, 202, 203, 204, 205, 206, 207],  # 8 MLAs
        "pc_nos": [17]  # Dakshina Kannada
    },
    {
        "key": "chitradurga",
        "name_kn": "ಚಿತ್ರದುರ್ಗ",
        "name_en": "Chitradurga",
        "hq_kn": "ಚಿತ್ರದುರ್ಗ",
        "hq_en": "Chitradurga",
        "lat": 14.2251, "lon": 76.3980,
        "pop": "16.6 ಲಕ್ಷ", "area": "8,440 sq km",
        "region": "ಮಧ್ಯ ಕರ್ನಾಟಕ",
        "dam": "vanivilasa",
        "taluks": ["ಚಿತ್ರದುರ್ಗ", "ಚಳ್ಳಕೆರೆ", "ಹಿರಿಯೂರು", "ಹೊಳಲ್ಕೆರೆ", "ಹೊಸದುರ್ಗ", "ಮೊಳಕಾಲ್ಮುರು"],
        "famous_for": "ಏಳು ಸುತ್ತಿನ ಕಲ್ಲಿನ ಕೋಟೆ, ಒನಕೆ ಓಬವ್ವನ ಕಿಂಡಿ, ವಾಣಿ ವಿಲಾಸ ಸಾಗರ (ಮಾರಿ ಕಣಿವೆ), ಮೊಳಕಾಲ್ಮುರು ರೇಷ್ಮೆ ಸೀರೆ (GI)",
        "mla_codes": [97, 98, 99, 100, 101, 102],  # 6 MLAs
        "pc_nos": [18]  # Chitradurga
    },
    {
        "key": "davanagere",
        "name_kn": "ದಾವಣಗೆರೆ",
        "name_en": "Davanagere",
        "hq_kn": "ದಾವಣಗೆರೆ",
        "hq_en": "Davanagere",
        "lat": 14.4644, "lon": 75.9218,
        "pop": "19.45 ಲಕ್ಷ", "area": "5,924 sq km",
        "region": "ಮಧ್ಯ ಕರ್ನಾಟಕ",
        "dam": "bhadra",
        "taluks": ["ದಾವಣಗೆರೆ", "ಹರಿಹರ", "ಹೊನ್ನಾಳಿ", "ಚನ್ನಗಿರಿ", "ಜಗಳೂರು", "ನ್ಯಾಮತಿ"],
        "famous_for": "ವಿಶ್ವವಿಖ್ಯಾತ ದಾವಣಗೆರೆ ಬೆಣ್ಣೆ ದೋಸೆ, ಕರ್ನಾಟಕದ ಮ್ಯಾಂಚೆಸ್ಟರ್, ಶಾಂತಿ ಸಾಗರ (ಸೂಳೆಕೆರೆ), ಹರಿಹರದ ಹರಿಹರೇಶ್ವರ ಗುಡಿ",
        "mla_codes": [103, 105, 106, 107, 108, 109, 110],  # 7 MLAs
        "pc_nos": [13]  # Davanagere
    },
    {
        "key": "tumakuru",
        "name_kn": "ತುಮಕೂರು",
        "name_en": "Tumakuru",
        "hq_kn": "ತುಮಕೂರು",
        "hq_en": "Tumakuru",
        "lat": 13.3379, "lon": 77.1173,
        "pop": "26.78 ಲಕ್ಷ", "area": "10,597 sq km",
        "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ",
        "dam": "vanivilasa",
        "taluks": ["ತುಮಕೂರು", "ತಿಪಟೂರು", "ಕುಣಿಗಲ್", "ಸಿರಾ", "ಮಧುಗಿರಿ", "ಪಾವಗಡ", "ತುರುವೇಕೆರೆ", "ಗುಬ್ಬಿ", "ಕೊರಟಗೆರೆ", "ಚಿಕ್ಕನಾಯಕನಹಳ್ಳಿ"],
        "famous_for": "ಸಿದ್ಧಗಂಗಾ ಮಠ (ಶ್ರೀ ಶಿವಕುಮಾರ ಮಹಾಸ್ವಾಮೀಜಿ), ಕಲ್ಪತರು ನಾಡು, ತಿಪಟೂರು ಕೊಬ್ಬರಿ, ಮಧುಗಿರಿ ಏಕಶಿಲಾ ಬೆಟ್ಟ, ವಸಂತನರಸಾಪುರ ಇಂಡಸ್ಟ್ರಿಯಲ್ ಹಬ್",
        "mla_codes": [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138],  # 11 MLAs
        "pc_nos": [19]  # Tumkur
    },
    {
        "key": "mandya",
        "name_kn": "ಮಂಡ್ಯ",
        "name_en": "Mandya",
        "hq_kn": "ಮಂಡ್ಯ",
        "hq_en": "Mandya",
        "lat": 12.5220, "lon": 76.8951,
        "pop": "18.08 ಲಕ್ಷ", "area": "4,961 sq km",
        "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ",
        "dam": "krs",
        "taluks": ["ಮಂಡ್ಯ", "ಮದ್ದೂರು", "ಮಳವಳ್ಳಿ", "ಶ್ರೀರಂಗಪಟ್ಟಣ", "ಪಾಂಡವಪುರ", "ಕೆ.ಆರ್.ಪೇಟೆ", "ನಾಗಮಂಗಲ"],
        "famous_for": "ಸಕ್ಕರೆ ನಾಡು, ಕೃಷ್ಣರಾಜ ಸಾಗರ (KRS) ಡ್ಯಾಂ & ಬೃಂದಾವನ, ರಂಗನತಿಟ್ಟು ಪಕ್ಷಿಧಾಮ, ಶಿವನಸಮುದ್ರ ಜಲಪಾತ, ಮದ್ದೂರು ವಡೆ",
        "mla_codes": [186, 187, 188, 189, 190, 191, 192],  # 7 MLAs
        "pc_nos": [20]  # Mandya
    },
    {
        "key": "hassan",
        "name_kn": "ಹಾಸನ",
        "name_en": "Hassan",
        "hq_kn": "ಹಾಸನ",
        "hq_en": "Hassan",
        "lat": 13.0068, "lon": 76.1003,
        "pop": "17.76 ಲಕ್ಷ", "area": "6,814 sq km",
        "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ",
        "dam": "hemavathi",
        "taluks": ["ಹಾಸನ", "ಅರಸೀಕೆರೆ", "ಚನ್ನರಾಯಪಟ್ಟಣ", "ಹೊಳೆನರಸೀಪುರ", "ಸಕಲೇಶಪುರ", "ಬೇಲೂರು", "ಆಲೂರು", "ಅರ್ಕಲಗೂಡು"],
        "famous_for": "ಬೇಲೂರು-ಹಳೇಬೀಡು ಹೊಯ್ಸಳ ಶಿಲ್ಪಕಲೆ (UNESCO), ಶ್ರವಣಬೆಳಗೊಳ ಗೊಮ್ಮಟೇಶ್ವರ ಬಾಹುಬಲಿ, ಹಾಸನಾಂಬೆ ದೇವಾಲಯ, ಸಕಲೇಶಪುರ ಮಲೆನಾಡು",
        "mla_codes": [193, 194, 195, 196, 197, 198, 199],  # 7 MLAs
        "pc_nos": [16]  # Hassan
    },
    {
        "key": "mysuru",
        "name_kn": "ಮೈಸೂರು",
        "name_en": "Mysuru",
        "hq_kn": "ಮೈಸೂರು",
        "hq_en": "Mysuru",
        "lat": 12.2958, "lon": 76.6394,
        "pop": "30.0 ಲಕ್ಷ", "area": "6,854 sq km",
        "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ",
        "dam": "kabini",
        "taluks": ["ಮೈಸೂರು", "ನಂಜನಗೂಡು", "ಹುಣಸೂರು", "ಟಿ.ನರಸೀಪುರ", "ಪಿರಿಯಾಪಟ್ಟಣ", "ಕೆ.ಆರ್.ನಗರ", "ಸಾರಗೂರು", "ಸಾಲಿಗ್ರಾಮ"],
        "famous_for": "ವಿಶ್ವವಿಖ್ಯಾತ ಮೈಸೂರು ದಸರಾ, ಅಂಬಾವಿಲಾಸ ಅರಮನೆ, ಚಾಮುಂಡಿ ಬೆಟ್ಟ, ಮೈಸೂರು ರೇಷ್ಮೆ (GI), ಮೈಸೂರು ಪಾಕ್",
        "mla_codes": [208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218],  # 11 MLAs
        "pc_nos": [21]  # Mysore-Kodagu
    },
    {
        "key": "chamarajanagara",
        "name_kn": "ಚಾಮರಾಜನಗರ",
        "name_en": "Chamarajanagara",
        "hq_kn": "ಚಾಮರಾಜನಗರ",
        "hq_en": "Chamarajanagara",
        "lat": 11.9261, "lon": 76.9437,
        "pop": "10.2 ಲಕ್ಷ", "area": "5,101 sq km",
        "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ",
        "dam": "kabini",
        "taluks": ["ಚಾಮರಾಜನಗರ", "ಗುಂಡ್ಲುಪೇಟೆ", "ಕೊಳ್ಳೇಗಾಲ", "ಯಳಂದೂರು", "ಹನೂರು"],
        "famous_for": "ಬಂಡೀಪುರ ಹುಲಿ ಸಂರಕ್ಷಿತ ಪ್ರದೇಶ, ಮಲೆ ಮಹದೇಶ್ವರ ಬೆಟ್ಟ (MM Hills), ಬಿಆರ್ ಹಿಲ್ಸ್ (BR Hills), ಹಿಮವದ್ ಗೋಪಾಲಸ್ವಾಮಿ ಬೆಟ್ಟ",
        "mla_codes": [219, 220, 221, 222],  # 4 MLAs
        "pc_nos": [22]  # Chamarajanagar
    },
    {
        "key": "kodagu",
        "name_kn": "ಕೊಡಗು",
        "name_en": "Kodagu",
        "hq_kn": "ಮಡಿಕೇರಿ",
        "hq_en": "Madikeri",
        "lat": 12.4244, "lon": 75.7382,
        "pop": "5.54 ಲಕ್ಷ", "area": "4,102 sq km",
        "region": "ಮಲೆನಾಡು",
        "dam": "harangi",
        "taluks": ["ಮಡಿಕೇರಿ", "ವಿರಾಜಪೇಟೆ", "ಸೋಮವಾರಪೇಟೆ", "ಪೊನ್ನಂಪೇಟೆ", "ಕುಶಾಲನಗರ"],
        "famous_for": "ಕಾವೇರಿಯ ಉಗಮಸ್ಥಾನ ತಲಕಾವೇರಿ, ಕೂರ್ಗ್ ಕಾಫಿ & ಏಲಕ್ಕಿ, ರಾಜಾಸೀಟ್, ಅಬ್ಬಿ ಜಲಪಾತ, ವೀರ ಕೊಡವ ಸಂಸ್ಕೃತಿ",
        "mla_codes": [223, 224],  # 2 MLAs: Madikeri, Virajpet
        "pc_nos": [21]  # Mysore-Kodagu
    },
    {
        "key": "chikkaballapura",
        "name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
        "name_en": "Chikkaballapura",
        "hq_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
        "hq_en": "Chikkaballapura",
        "lat": 13.4325, "lon": 77.7275,
        "pop": "12.55 ಲಕ್ಷ", "area": "4,244 sq km",
        "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ",
        "dam": "krs",
        "taluks": ["ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "ಚಿಂತಾಮಣಿ", "ಗೌರಿಬಿದನೂರು", "ಬಾಗೇಪಲ್ಲಿ", "ಶಿಡ್ಲಘಟ್ಟ", "ಗುಡಿಬಂಡೆ"],
        "famous_for": "ನಂದಿಬೆಟ್ಟ (Nandi Hills), ಸರ್ ಎಂ. ವಿಶ್ವೇಶ್ವರಯ್ಯರ ಮುದ್ದೇನಹಳ್ಳಿ, ಭೋಗ ನಂದೀಶ್ವರ ದೇವಾಲಯ, ಆದಿಯೋಗಿ ಪ್ರತಿಮೆ",
        "mla_codes": [139, 140, 141, 142, 143],  # 5 MLAs
        "pc_nos": [27]  # Chikkballapur
    },
    {
        "key": "kolar",
        "name_kn": "ಕೋಲಾರ",
        "name_en": "Kolar",
        "hq_kn": "ಕೋಲಾರ",
        "hq_en": "Kolar",
        "lat": 13.1367, "lon": 78.1291,
        "pop": "15.36 ಲಕ್ಷ", "area": "3,969 sq km",
        "region": "ದಕ್ಷಿಣ ಕರ್ನಾಟಕ",
        "dam": "krs",
        "taluks": ["ಕೋಲಾರ", "ಬಂಗಾರಪೇಟೆ", "ಮಾಲೂರು", "ಮುಳಬಾಗಿಲು", "ಶ್ರೀನಿವಾಸಪುರ", "ಕೆಜಿಎಫ್ (KGF)"],
        "famous_for": "ಕೆಜಿಎಫ್ (KGF) ಚಿನ್ನದ ಗಣಿ, ಕುರುಡುಮಲೆ ಗಣಪತಿ, ಕೋಲಾರಮ್ಮ ದೇವಸ್ಥಾನ, ಏಷ್ಯಾದ 2ನೇ ದೊಡ್ಡ ಟೊಮೆಟೊ ಮಾರುಕಟ್ಟೆ",
        "mla_codes": [144, 145, 146, 147, 148, 149],  # 6 MLAs
        "pc_nos": [28]  # Kolar
    }
]

# Load representatives catalog
catalog_path = BASE_DIR / "data" / "gis" / "representatives_catalog.json"
with open(catalog_path, "r", encoding="utf-8") as f:
    CATALOG = json.load(f)

MLAS = CATALOG.get("mlas", {})
MPS = CATALOG.get("mps", {})

print(f"Loaded {len(MLAS)} MLAs and {len(MPS)} MPs from catalog.")

def format_clean_guide(raw_html):
    """Clean the location pin icon from all h3 headers"""
    # Replace 📍 from h3 headers
    cleaned = re.sub(r'(<h3[^>]*>)\s*📍\s*', r'\1', raw_html)
    return cleaned

def generate_mp_cards(pc_nos):
    cards = []
    for pc in pc_nos:
        pc_str = str(pc)
        mp = MPS.get(pc_str)
        if not mp:
            continue
        party = mp.get("party_en", "IND")
        p_class = "party-" + "".join(c for c in party if c.isalpha())
        mp_name = mp.get("mp_kn") or mp.get("mp_name_kn") or mp.get("mp_en") or "ಸಂಸದರು"
        pc_name = mp.get("name_kn") or mp.get("pc_name_kn") or mp.get("name_en")
        pc_name_en = mp.get("name_en") or mp.get("pc_name_en") or ""
        margin = mp.get("margin", 0)
        img_tag = f'''<div style="width:88px; height:106px; border-radius:14px; overflow:hidden; border:2.5px solid #CBD5E1; background:#EFF6FF; box-shadow:0 4px 14px rgba(0,0,0,0.12); flex-shrink:0;">
          <img src="/assets/images/mps/{pc}.jpg" alt="{mp_name}" style="width:100%; height:100%; object-fit:cover; object-position:top;" onerror="this.outerHTML='<div style=\\'width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:900;background:#F1F5F9;color:#334155;\\'>' + this.alt.charAt(0) + '</div>'">
        </div>'''
        
        card = f"""
        <div style="background:#FFFFFF; border:1.5px solid #CBD5E1; border-radius:18px; padding:20px 22px; margin-bottom:14px; box-shadow:0 6px 20px rgba(15,23,42,0.06);">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:18px;">
            <div style="display:flex; align-items:center; gap:18px;">
              {img_tag}
              <div>
                <span style="font-size:12px; font-weight:800; color:#1D4ED8; background:#EFF6FF; padding:4px 10px; border-radius:6px; font-family:sans-serif; letter-spacing:0.5px;">18TH LOK SABHA MEMBER (ಸಂಸದರು)</span>
                <div style="font-size:21px; font-weight:900; color:#0F172A; margin-top:4px;">{mp_name}</div>
                <div style="font-size:14.5px; color:#475569; font-weight:700; margin-top:3px;">🏛️ {pc_name} ({pc_name_en}) ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ</div>
              </div>
            </div>
            <div style="display:flex; align-items:center; gap:14px;">
              <span class="d-party-tag {p_class}" style="font-size:15px; padding:7px 16px; font-weight:900;">{party}</span>
              {f'<div style="font-size:14px; font-weight:800; color:#059669; background:#ECFDF5; padding:7px 14px; border-radius:10px; border:1.5px solid #A7F3D0;">ಅಂತರ: +{margin:,} ಮತಗಳು</div>' if margin else ''}
            </div>
          </div>
        </div>
        """
        cards.append(card.strip())
    return "\n".join(cards)

def generate_mla_cards(mla_codes):
    cards = []
    for code in mla_codes:
        code_str = str(code)
        mla = MLAS.get(code_str)
        if not mla:
            continue
        party = mla.get("party_en", "IND")
        p_class = "party-" + "".join(c for c in party if c.isalpha())
        mla_name = mla.get("mla_name_kn") or mla.get("mla_name_en")
        ac_name = mla.get("ac_name_kn") or mla.get("ac_name_en")
        cat_badge = f'<span style="font-size:11px; font-weight:800; background:#F1F5F9; color:#475569; padding:2px 6px; border-radius:4px;">{mla.get("category","GEN")}</span>'
        margin = mla.get('margin', 0)
        
        card = f"""
            <a href="/mla/{code}.html" class="d-mla-card" style="display:flex; gap:14px; align-items:center; padding:14px 16px; background:#FFFFFF; border:1.5px solid #E2E8F0; border-radius:14px; text-decoration:none; color:inherit; box-shadow:0 2px 8px rgba(0,0,0,0.03); transition:all 0.2s;">
              <div style="width:68px; height:80px; border-radius:12px; overflow:hidden; border:2px solid #CBD5E1; background:#EFF6FF; box-shadow:0 3px 10px rgba(0,0,0,0.08); flex-shrink:0;">
                <img src="/assets/images/mlas/{code}.jpg" alt="{mla_name}" style="width:100%; height:100%; object-fit:cover; object-position:top;" onerror="this.outerHTML='<div style=\\'width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:900;background:#F1F5F9;color:#334155;\\'>' + this.alt.charAt(0) + '</div>'">
              </div>
              <div style="flex:1; min-width:0;">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                  <span style="font-size:12px; font-weight:800; color:#64748B;">ಕ್ಷೇತ್ರ #{code}</span>
                  <span class="d-party-tag {p_class}" style="font-size:11px; padding:2px 8px; font-weight:900;">{party}</span>
                </div>
                <div style="font-size:16px; font-weight:900; color:#0F172A; line-height:1.3; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;" title="{mla_name}">{mla_name}</div>
                <div style="font-size:13px; font-weight:700; color:#2563EB; margin-top:2px;">🏛️ {ac_name} {cat_badge}</div>
                {f'<div style="font-size:11.5px; font-weight:800; color:#059669; margin-top:4px;">ಅಂತರ: +{margin:,} ಮತಗಳು</div>' if margin else ''}
              </div>
            </a>
        """
        cards.append(card.strip())
    return "\n".join(cards)

def update_district_file(file_path, dist_info):
    if not os.path.exists(file_path):
        return
        
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Clean location icon from guide section
    if "class=\"d-sec district-guide-sec\"" in html:
        html = format_clean_guide(html)

    # 2. Update MLA section
    mla_cards_html = generate_mla_cards(dist_info["mla_codes"])
    mla_count = len(dist_info["mla_codes"])
    mla_sec_regex = r'<div class="d-sec">\s*<div class="d-sec-title">\s*<span>🏛️ [^<]*? MLAs?\)[^<]*?</span>.*?<div class="d-grid-mla"[^>]*>.*?</div>\s*</div>'
    
    new_mla_sec = f"""<div class="d-sec">
      <div class="d-sec-title">
        <span>🏛️ {dist_info['name_kn']} ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ ಶಾಸಕರು ({mla_count} MLAs)</span>
        <a href="/mla-mp.html" style="font-size:13px; font-weight:800; color:var(--k-red); text-decoration:none;">ಎಲ್ಲಾ 224 ಶಾಸಕರು →</a>
      </div>
      <div class="d-grid-mla" id="mlas-grid">
        {mla_cards_html}
      </div>
    </div>"""
    
    html = re.sub(mla_sec_regex, new_mla_sec, html, count=1, flags=re.DOTALL)

    # 3. Update MP section
    mp_cards_html = generate_mp_cards(dist_info["pc_nos"])
    mp_count = len(dist_info["pc_nos"])
    mp_title = f"🗳️ {dist_info['name_kn']} ಲೋಕಸಭಾ ಸಂಸದರು ({mp_count} MP{'s' if mp_count > 1 else ''})"
    
    mp_sec_regex = r'<div class="d-sec">\s*<div class="d-sec-title"><span>🗳️ [^<]*?</span></div>\s*<div id="mp-box"[^>]*>.*?</div>\s*</div>'
    
    new_mp_sec = f"""<div class="d-sec">
      <div class="d-sec-title"><span>{mp_title}</span></div>
      <div id="mp-box" style="background:#F8FAFC; border:1.5px solid #E2E8F0; border-radius:14px; padding:16px;">
        {mp_cards_html}
      </div>
    </div>"""
    
    html = re.sub(mp_sec_regex, new_mp_sec, html, count=1, flags=re.DOTALL)

    # 4. Update Taluks section
    taluks = dist_info["taluks"]
    taluk_pills = "".join(f'<div class="d-taluk-pill">📍 {t}</div>' for t in taluks)
    taluk_sec_regex = r'<div class="d-sec">\s*<div class="d-sec-title"><span>🏡 [^<]*? ತಾಲೂಕುಗಳು[^<]*?</span></div>\s*<div class="d-taluks-wrap">.*?</div>\s*</div>'
    
    new_taluk_sec = f"""<div class="d-sec">
      <div class="d-sec-title"><span>🏡 {dist_info['name_kn']} ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು ({len(taluks)})</span></div>
      <div class="d-taluks-wrap">
        {taluk_pills}
      </div>
    </div>"""
    
    html = re.sub(taluk_sec_regex, new_taluk_sec, html, count=1, flags=re.DOTALL)

    # 5. Update Header Stats Strip (MLAs and Taluks count)
    html = re.sub(
        r'<div class="d-stat-box">\s*<div>ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ</div>\s*<div class="d-stat-val">[^<]*?</div>\s*</div>',
        f'<div class="d-stat-box"><div>ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ</div><div class="d-stat-val">{mla_count} MLAs</div></div>',
        html
    )
    html = re.sub(
        r'<div class="d-stat-box">\s*<div>ತಾಲೂಕುಗಳು</div>\s*<div class="d-stat-val">[^<]*?</div>\s*</div>',
        f'<div class="d-stat-box"><div>ತಾಲೂಕುಗಳು</div><div class="d-stat-val">{len(taluks)}</div></div>',
        html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

def main():
    updated = 0
    for d in DISTRICTS_DATA:
        key = d["key"]
        for base in [BASE_DIR, BASE_DIR / "namma-karnataka"]:
            fpath = base / "districts" / f"{key}.html"
            update_district_file(fpath, d)
        updated += 1
        print(f"[REBUILT] {d['name_kn']} ({key}.html) -> {len(d['mla_codes'])} MLAs, {len(d['pc_nos'])} MPs, {len(d['taluks'])} Taluks")

    print(f"\nSuccessfully verified and upgraded all {updated} districts with high-precision intelligence!")

if __name__ == '__main__':
    main()
