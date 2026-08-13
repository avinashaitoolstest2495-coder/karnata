"""
Karnata — process_elections_data.py
Processes karnataka_elections_1978_2023.xlsx and karnataka_assembly_224.json
Translates all constituency names, candidate names, parties, and categories to Kannada.
Outputs data/elections_data.json with payload obfuscation wrapper.
"""

import os
import re
import sys
import json
import pandas as pd
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "scraper"))
from utils import store, sanitize_dict, encrypt_payload

EXCEL_PATH = Path(__file__).parent.parent / "karnataka_elections_1978_2023.xlsx"
GEOJSON_PATH = Path(__file__).parent.parent / "karnataka_assembly_224.json"

PARTY_COLORS = {
    "INC": "#1f77b4", "INC(I)": "#3182bd",
    "BJP": "#ff7f0e", "JNP": "#ff7f0e",
    "JD": "#2ca02c", "JD(S)": "#31a354",
    "KRPP": "#9467bd", "SKP": "#e377c2",
    "IND": "#7f7f7f",
    "CPI": "#de2d26", "CPM": "#a50f15",
    "RPI": "#8c564b", "MUL": "#3182bd", "NCP": "#0d9488"
}
DEFAULT_COLOR = "#64748b"

PARTY_KANNADA = {
    "INC": "ಕಾಂಗ್ರೆಸ್ (INC)",
    "INC(I)": "ಕಾಂಗ್ರೆಸ್ ಐ (INC-I)",
    "BJP": "ಬಿಜೆಪಿ (BJP)",
    "JNP": "ಜನತಾ ಪಕ್ಷ (JNP)",
    "JD(S)": "ಜೆಡಿಎಸ್ (JD-S)",
    "JD": "ಜನತಾ ದಳ (JD)",
    "IND": "ಪಕ್ಷೇತರ (IND)",
    "KRPP": "ಕೆಆರ್‌ಪಿಪಿ (KRPP)",
    "SKP": "ಎಸ್‌.ಕೆ.ಪಿ (SKP)",
    "CPI": "ಸಿಪಿಐ (CPI)",
    "CPM": "ಸಿಪಿಎಂ (CPM)",
    "RPI": "ಆರ್‌ಪಿಐ (RPI)",
    "NCP": "ಎನ್‌ಸಿಪಿ (NCP)"
}

# Complete 224 Kannada Constituency Dictionary
KANNADA_DICT = {
    "nippani": "ನಿಪ್ಪಾಣಿ",
    "chikkodi-sadalga": "ಚಿಕ್ಕೋಡಿ - ಸಡಲಗಾ",
    "chikkodi - sadalga": "ಚಿಕ್ಕೋಡಿ - ಸಡಲಗಾ",
    "chikkodi": "ಚಿಕ್ಕೋಡಿ",
    "athani": "ಅಥಣಿ",
    "kagwad": "ಕಾಗವಾಡ",
    "kudachi": "ಕುಡಚಿ",
    "raybag": "ರಾಯಬಾಗ",
    "hukkeri": "ಹುಕ್ಕೇರಿ",
    "arabhavi": "ಅರಭಾವಿ",
    "gokak": "ಗೋಕಾಕ್",
    "yemkanmardi": "ಯಮಕನಮರಡಿ",
    "belgaum uttar": "ಬೆಳಗಾವಿ ಉತ್ತರ",
    "belagavi uttar": "ಬೆಳಗಾವಿ ಉತ್ತರ",
    "belgaum dakshin": "ಬೆಳಗಾವಿ ದಕ್ಷಿಣ",
    "belagavi dakshin": "ಬೆಳಗಾವಿ ದಕ್ಷಿಣ",
    "belgaum rural": "ಬೆಳಗಾವಿ ಗ್ರಾಮಾಂತರ",
    "belagavi rural": "ಬೆಳಗಾವಿ ಗ್ರಾಮಾಂತರ",
    "khanapur": "ಖಾನಾಪುರ",
    "kittur": "ಕಿತ್ತೂರು",
    "bailhongal": "ಬೈಲಹೊಂಗಲ",
    "saudatti yellamma": "ಸವದತ್ತಿ ಯಲ್ಲಮ್ಮ",
    "ramdurg": "ರಾಮದುರ್ಗ",
    "mudhol": "ಮುಧೋಳ",
    "terdal": "ತೇರದಾಳ",
    "jamkhandi": "ಜಮಖಂಡಿ",
    "bagalkot": "ಬಾಗಲಕೋಟೆ",
    "hunagunda": "ಹುನಗುಂದ",
    "hungund": "ಹುನಗುಂದ",
    "ilkal": "ಇಳಕಲ್ಲ",
    "badami": "ಬಾದಾಮಿ",
    "navalgund": "ನವಲಗುಂದ",
    "kundgol": "ಕುಂದಗೋಳ",
    "dharwad": "ಧಾರವಾಡ",
    "hubli-dharwad central": "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ ಕೇಂದ್ರ",
    "hubli-dharwad east": "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ ಪೂರ್ವ",
    "hubli-dharwad west": "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ ಪಶ್ಚಿಮ",
    "kalghatgi": "ಕಲಘಟಗಿ",
    "haliyal": "ಹಳಿಯಾಳ",
    "karwar": "காரவார (ಕಾರವಾರ)",
    "karwar": "ಕಾರವಾರ",
    "kumta": "ಕುಮಟಾ",
    "bhatkal": "ಭಟ್ಕಳ",
    "sirsi": "ಶಿರಸಿ",
    "yellapur": "ಯಲ್ಲಾಪುರ",
    "haveri": "ಹಾವೇರಿ",
    "byadgi": "ಬ್ಯಾಡಗಿ",
    "hirekerur": "ಹಿರೇಕೆರೂರು",
    "ranibennur": "ರಾಣೆಬೆನ್ನೂರು",
    "shiggaon": "ಶಿಗ್ಗಾಂವಿ",
    "hangal": "ಹಾನಗಲ್",
    "gadag": "ಗದಗ",
    "ron": "ರೋಣ",
    "nargund": "ನರಗುಂದ",
    "shirahatti": "ಶಿರಹಟ್ಟಿ",
    "baramati": "ಬಾರಾಮತಿ",
    "afzalpur": "ಅಫ್ಜಲ್ ಪುರ",
    "jewargi": "ಜೇವರ್ಗಿ",
    "gurmitkal": "ಗುರಮಿಟ್ಕಲ್",
    "shorapur": "ಶೋರಾಪುರ",
    "shahapur": "ಶಹಾಪುರ",
    "yadgir": "ಯಾದಗಿರಿ",
    "sedam": "ಸೇಡಂ",
    "chincholi": "ಚಿಂಚೋಳಿ",
    "kalaburagi kamalapur": "ಕಲಬುರಗಿ ಕಮಲಾಪುರ",
    "kalaburagi rural": "ಕಲಬುರಗಿ ಗ್ರಾಮಾಂತರ",
    "gulbarga rural": "ಕಲಬುರಗಿ ಗ್ರಾಮಾಂತರ",
    "kalaburagi dakshin": "ಕಲಬುರಗಿ ದಕ್ಷಿಣ",
    "gulbarga dakshin": "ಕಲಬುರಗಿ ದಕ್ಷಿಣ",
    "kalaburagi uttar": "ಕಲಬುರಗಿ ಉತ್ತರ",
    "gulbarga uttar": "ಕಲಬುರಗಿ ಉತ್ತರ",
    "aland": "ಆಳಂದ",
    "alland": "ಆಳಂದ",
    "basavakalyan": "ಬಸವಕಲ್ಯಾಣ",
    "humnabad": "ಹುಮ್ನಾಬಾದ್",
    "bidar south": "ಬೀದರ್ ದಕ್ಷಿಣ",
    "bidar": "ಬೀದರ್",
    "bhalki": "ಭಾಲ್ಕಿ",
    "aurad": "ಔರಾದ್",
    "raichur rural": "ರಾಯಚೂರು ಗ್ರಾಮಾಂತರ",
    "raichur": "ರಾಯಚೂರು",
    "manvi": "ಮಾನ್ವಿ",
    "devadurga": "ದೇವದುರ್ಗ",
    "lingasugur": "ಲಿಂಗಸುಗೂರು",
    "sindhanur": "ಸಿಂಧನೂರು",
    "maski": "ಮಾಸ್ಕಿ",
    "kushtagi": "ಕುಷ್ಟಗಿ",
    "kanakagiri": "ಕನಕಗಿರಿ",
    "gangavati": "ಗಂಗಾವತಿ",
    "gangavathi": "ಗಂಗಾವತಿ",
    "yelburga": "ಯಲಬುರ್ಗಾ",
    "koppal": "ಕೊಪ್ಪಳ",
    "harapanahalli": "ಹರಪನಹಳ್ಳಿ",
    "hadagalli": "ಹೂವಿನಹಡಗಲಿ",
    "hagaribommanahalli": "ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ",
    "vijayanagara": "ವಿಜಯನಗರ",
    "hospet": "ಹೊಸಪೇಟೆ",
    "kudligi": "ಕೂಡ್ಲಿಗಿ",
    "sandur": "ಸಂಡೂರು",
    "siruguppa": "ಸಿರುಗುಪ್ಪ",
    "ballari": "ಬಳ್ಳಾರಿ",
    "bellary": "ಬಳ್ಳಾರಿ",
    "ballari city": "ಬಳ್ಳಾರಿ ನಗರ",
    "bellary city": "ಬಳ್ಳಾರಿ ನಗರ",
    "kampli": "ಕಂಪ್ಲಿ",
    "molakalmuru": "ಮೊಳಕಾಲ್ಮೂರು",
    "challakere": "ಚಳ್ಳಕೆರೆ",
    "chitradurga": "ಚಿತ್ರದುರ್ಗ",
    "hiriyur": "ಹಿರಿಯೂರು",
    "hosadurga": "ಹೊಸದುರ್ಗ",
    "holalkere": "ಹೊಳಲ್ಕೆರೆ",
    "jagamalur": "ಜಗಳೂರು",
    "jagalur": "ಜಗಳೂರು",
    "davanagere north": "ದಾವಣಗೆರೆ ಉತ್ತರ",
    "davangere north": "ದಾವಣಗೆರೆ ಉತ್ತರ",
    "davanagere south": "ದಾವಣಗೆರೆ ದಕ್ಷಿಣ",
    "davangere south": "ದಾವಣಗೆರೆ ದಕ್ಷಿಣ",
    "mayakonda": "ಮಾಯಾಕೊಂಡ",
    "channagiri": "ಚನ್ನಗಿರಿ",
    "honnali": "ಹೊನ್ನಾಳಿ",
    "shimoga rural": "ಶಿವಮೊಗ್ಗ ಗ್ರಾಮಾಂತರ",
    "shivamogga rural": "ಶಿವಮೊಗ್ಗ ಗ್ರಾಮಾಂತರ",
    "shimoga": "ಶಿವಮೊಗ್ಗ",
    "shivamogga": "ಶಿವಮೊಗ್ಗ",
    "bhadravati": "ಭದ್ರಾವತಿ",
    "tirthahalli": "ತೀರ್ಥಹಳ್ಳಿ",
    "thirthahalli": "ತೀರ್ಥಹಳ್ಳಿ",
    "shikaripura": "ಶಿಕಾರಿಪುರ",
    "sorab": "ಸೊರಬ",
    "sagar": "ಸಾಗರ",
    "byndoor": "ಬೈಂದೂರು",
    "kundapura": "ಕುಂದಾಪುರ",
    "udupi": "ಉಡುಪಿ",
    "kaup": "ಕಾಪು",
    "karkala": "ಕಾರ್ಕಳ",
    "sullia": "ಸುಳ್ಯ",
    "puttur": "ಪುತ್ತೂರು",
    "bantval": "ಬಂಟ್ವಾಳ",
    "mangalore city north": "ಮಂಗಳೂರು ನಗರ ಉತ್ತರ",
    "mangalore city south": "ಮಂಗಳೂರು ನಗರ ದಕ್ಷಿಣ",
    "mangalore": "ಮಂಗಳೂರು",
    "moodabidri": "ಮೂಡಬಿದಿರೆ",
    "belthangady": "ಬೆಳ್ತಂಗಡಿ",
    "mudigere": "ಮೂಡಿಗೆರೆ",
    "chikmagalur": "ಚಿಕ್ಕಮಗಳೂರು",
    "chikkamagaluru": "ಚಿಕ್ಕಮಗಳೂರು",
    "tarikere": "ತಾರೀಕೆರೆ",
    "kadur": "ಕಡೂರು",
    "sringeri": "ಶೃಂಗೇರಿ",
    "chikkanayakanahalli": "ಚಿಕ್ಕನಾಯಕನಹಳ್ಳಿ",
    "tiptur": "ತಿಪಟೂರು",
    "turuvekere": "ತುರುವೇಕೆರೆ",
    "kunigal": "ಕುಣಿಗಲ್",
    "tumkur city": "ತುಮಕೂರು ನಗರ",
    "tumakuru city": "ತುಮಕೂರು ನಗರ",
    "tumkur rural": "ತುಮಕೂರು ಗ್ರಾಮಾಂತರ",
    "tumakuru rural": "ತುಮಕೂರು ಗ್ರಾಮಾಂತರ",
    "koratagere": "ಕೊರಟಗೆರೆ",
    "gubb": "ಗುಬ್ಬಿ",
    "gubbi": "ಗುಬ್ಬಿ",
    "sira": "ಸಿರಾ",
    "pavagada": "ಪಾವಗಡ",
    "madhugiri": "ಮಧುಗಿರಿ",
    "gauribidanur": "ಗೌರಿಬಿದನೂರು",
    "bagepalli": "ಬಾಗೇಪಲ್ಲಿ",
    "chikkaballapur": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
    "sidlaghatta": "ಶಿಡ್ಲಘಟ್ಟ",
    "chintamani": "ಚಿಂತಾಮಣಿ",
    "srinivasapur": "ಶ್ರೀನಿವಾಸಪುರ",
    "mulbagal": "ಮುಳಬಾಗಿಲು",
    "kolar gold field": "ಕೋಲಾರ ಗೋಲ್ಡ್ ಫೀಲ್ಡ್ (KGF)",
    "kgf": "ಕೋಲಾರ ಗೋಲ್ಡ್ ಫೀಲ್ಡ್ (KGF)",
    "bangarapet": "ಬಂಗಾರಪೇಟೆ",
    "kolar": "ಕೋಲಾರ",
    "malur": "ಮಲೂರು",
    "yelahanka": "ಯಲಹಂಕ",
    "krpuram": "ಕೆ.ಆರ್. ಪುರಂ",
    "k.r. puram": "ಕೆ.ಆರ್. ಪುರಂ",
    "byatarayanapura": "ಬ್ಯಾಟರಾಯನಪುರ",
    "yeshwanthpur": "ಯಶವಂತಪುರ",
    "rajarajeshwarinagar": "ರಾಜರಾಜೇಶ್ವರಿನಗರ",
    "dasarahalli": "ದಾಸರಹಳ್ಳಿ",
    "mahalakshmi layout": "ಮಹಾಲಕ್ಷ್ಮಿ ಲೇಔಟ್",
    "malleshwaram": "ಮಲ್ಲೇಶ್ವರಂ",
    "hebal": "ಹೆಬ್ಬಾಳ",
    "hebbal": "ಹೆಬ್ಬಾಳ",
    "pulakeshinagar": "ಪುಲಕೇಸಿನಗರ",
    "sarvagnanagar": "ಸರ್ವಜ್ಞನಗರ",
    "cv raman nagar": "ಸಿ.ವಿ. ರಾಮನ್ ನಗರ",
    "shivajinagar": "ಶಿವಾಜಿನಗರ",
    "shanti nagar": "ಶಾಂತಿ ನಗರ",
    "shanthinagar": "ಶಾಂತಿ ನಗರ",
    "gandhi nagar": "ಗಾಂಧಿ ನಗರ",
    "gandhinagar": "ಗಾಂಧಿ ನಗರ",
    "rajaji nagar": "ರಾಜಾಜಿ ನಗರ",
    "rajajinagar": "ರಾಜಾಜಿ ನಗರ",
    "govindraj nagar": "ಗೋವಿಂದರಾಜ ನಗರ",
    "vijaya nagar": "ವಿಜಯ ನಗರ",
    "vijayanagar": "ವಿಜಯ ನಗರ",
    "chamarajpet": "ಚಾಮರಾಜಪೇಟೆ",
    "chickpet": "ಚಿಕ್ಕಪೇಟೆ",
    "basavanagudi": "ಬಸವನಗುಡಿ",
    "padmanaba nagar": "ಪದ್ಮನಾಭ ನಗರ",
    "btm layout": "ಬಿ.ಟಿ.ಎಂ. ಲೇಔಟ್",
    "jayanagar": "ಜಯನಗರ",
    "mahadevapura": "ಮಹದೇವಪುರ",
    "bommanahalli": "ಬೊಮ್ಮನಹಳ್ಳಿ",
    "bangalore south": "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ",
    "bengaluru south": "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ",
    "anekal": "ಆನೇಕಲ್",
    "hosakote": "ಹೊಸಕೋಟೆ",
    "devanahalli": "ದೇವನಹಳ್ಳಿ",
    "doddaballapur": "ದೊಡ್ಡಬಳ್ಳಾಪುರ",
    "nelamangala": "ನೆಲಮಂಗಲ",
    "magadi": "ಮಾಗಡಿ",
    "ramanagara": "ರಾಮನಗರ",
    "kanakapura": "ಕನಕಪುರ",
    "channapatna": "ಚನ್ನಪಟ್ಟಣ",
    "malavalli": "ಮಳವಳ್ಳಿ",
    "maddur": "ಮದ್ದೂರು",
    "melukote": "ಮೇಲುಕೋಟೆ",
    "mandya": "ಮಂಡ್ಯ",
    "shranganapatna": "ಶ್ರೀರಂಗಪಟ್ಟಣ",
    "srirangapatna": "ಶ್ರೀರಂಗಪಟ್ಟಣ",
    "nagamangala": "ನಾಗಮಂಗಲ",
    "krishanarajanagara": "ಕೃಷ್ಣರಾಜನಗರ",
    "krnagara": "ಕೃಷ್ಣರಾಜನಗರ",
    "sakleshpur": "ಸಕಲೇಶಪುರ",
    "belur": "ಬೇಲೂರು",
    "halebeedu": "ಹಳೇಬೀಡು",
    "hassan": "ಹಾಸನ",
    "holenarasipur": "ಹೊಳೆನರಸೀಪುರ",
    "arkalgud": "ಅರಕಲಗೂಡು",
    "arsikere": "ಅರಸೀಕೆರೆ",
    "shravanabelagola": "ಶ್ರವಣಬೆಳಗೊಳ",
    "madikeri": "ಮಡಿಕೇರಿ",
    "virajpet": "ವಿರಾಜಪೇಟೆ",
    "piriyapatna": "ಪಿರಿಯಾಪಟ್ಟಣ",
    "periyapatna": "ಪಿರಿಯಾಪಟ್ಟಣ",
    "hunsur": "ಹುಣಸೂರು",
    "nanjangud": "ನಂಜನಗೂಡು",
    "chamundeshwari": "ಚಾಮುಂಡೇಶ್ವರಿ",
    "krishanaraja": "ಕೃಷ್ಣರಾಜ",
    "kr raja": "ಕೃಷ್ಣರಾಜ",
    "chamaraja": "ಚಾಮರಾಜ",
    "narasimharaja": "ನರಸಿಂಹರಾಜ",
    "varuna": "ವರುಣ",
    "t narasipura": "ಟಿ. ನರಸೀಪುರ",
    "t.narasipura": "ಟಿ. ನರಸೀಪುರ",
    "hanur": "ಹನೂರು",
    "kollegal": "ಕೊಳ್ಳೇಗಾಲ",
    "chamarajanagar": "ಚಾಮರಾಜನಗರ",
    "gundlupet": "ಗುಂಡ್ಲುಪೇಟೆ",

    "sc": "ಪರಿಶಿಷ್ಟ ಜಾತಿ (SC)",
    "st": "ಪರಿಶಿಷ್ಟ ಪಂಗಡ (ST)",
    "none": "ಸಾಮಾನ್ಯ",
    "general": "ಸಾಮಾನ್ಯ",
    "gen": "ಸಾಮಾನ್ಯ"
}

NAME_WORD_MAP = {
    "dr": "ಡಾ.", "dr.": "ಡಾ.", "prof": "ಪ್ರೊ.", "adv": "ಅಡ್ವೋಕೇಟ್",
    "a": "ಎ.", "b": "ಬಿ.", "c": "ಸಿ.", "d": "ಡಿ.", "e": "ಇ.", "f": "ಎಫ್.",
    "g": "ಜಿ.", "h": "ಎಚ್.", "i": "ಐ.", "j": "ಜೆ.", "k": "ಕೆ.", "l": "ಎಲ್.",
    "m": "ಎಂ.", "n": "ಎನ್.", "o": "ಓ.", "p": "ಪಿ.", "q": "ಕ್ಯೂ.", "r": "ಆರ್.",
    "s": "ಎಸ್.", "t": "ಟಿ.", "u": "ಯು.", "v": "ವಿ.", "w": "ಡಬ್ಲ್ಯೂ.", "x": "ಎಕ್ಸ್.",
    "y": "ವೈ.", "z": "ಜೆಡ್.",

    "patil": "ಪಾಟೀಲ್", "gowda": "ಗೌಡ", "reddy": "ರೆಡ್ಡಿ", "shettar": "ಶೆಟ್ಟರ್",
    "desai": "ದೇಸಾಯಿ", "guttedar": "ಗುತ್ತೇದಾರ್", "jarkiholi": "ಜಾರಕಿಹೊಳಿ", "bommai": "ಬೊಮ್ಮಾಯಿ",
    "shivakumar": "ಶಿವಕುಮಾರ್", "siddaramaiah": "ಸಿದ್ದರಾಮಯ್ಯ", "rao": "ರಾವ್", "kumar": "ಕುಮಾರ್",
    "naik": "ನಾಯಕ್", "pujari": "ಪೂಜಾರಿ", "poojary": "ಪೂಜಾರಿ", "hegde": "ಹೆಗಡೆ", "swamy": "ಸ್ವಾಮಿ",
    "swami": "ಸ್ವಾಮಿ", "prabhu": "ಪ್ರಭು", "chauhan": "ಚೌಹಾಣ್", "chavan": "ಚವಾಣ್", "shivanna": "ಶಿವಣ್ಣ",
    "bhojaraj": "ಭೋಜರಾಜ್", "manju": "ಮಂಜು", "kumathalli": "ಕುಮಟಳ್ಳಿ", "ramalinga": "ರಾಮಲಿಂಗ",
    "srinivas": "ಶ್ರೀನಿವಾಸ್", "srinivasa": "ಶ್ರೀನಿವಾಸ", "hullahalli": "ಹುಲ್ಲಹಳ್ಳಿ", "jolle": "ಜೋಲ್ಲೆ",
    "shashikala": "ಶಶಿಕಲಾ", "annasaheb": "ಅಣ್ಣಾಸಾಹೇಬ್", "ganesh": "ಗಣೇಶ್", "prakash": "ಪ್ರಕಾಶ್",
    "hukkeri": "ಹುಕ್ಕೇರಿ", "laxman": "ಲಕ್ಷ್ಮಣ್", "lakshmana": "ಲಕ್ಷ್ಮಣ", "sangappa": "ಸಂಗ್ಲಪ್ಪ",
    "savadi": "ಸವದಿ", "bharamgouda": "ಭರಮಗೌಡ", "alagouda": "ಆಲಗೌಡ", "kage": "ಕಾಪೇ", "kage": "ಕಾගේ",
    "mahendra": "ಮಹೇಂದ್ರ", "kallappa": "ಕಲ್ಲಪ್ಪ", "tammannavar": "ತಮ್ಮಣ್ಣವರ್", "aihole": "ಐಹೊಳೆ",
    "duryodhan": "ದುರ್ಯೋಧನ", "mahalingappa": "ಮಹಾಲಿಂಗಪ್ಪ", "katti": "ಕತ್ತಿ", "nikhil": "ನಿಖಿಲ್",
    "umesh": "ಉಮೇಶ್", "balachandra": "ಬಾಲಚಂದ್ರ", "laxmanrao": "ಲಕ್ಷ್ಮಣರಾವ್", "ramesh": "ರಮೇಶ್",
    "satish": "ಸತೀಶ್", "asif": "ಆಸಿಫ್", "raju": "ರಾಜು", "sait": "ಸೇಟ್", "siddu": "ಸಿದ್ದು",
    "anand": "ಆನಂದ್", "chandrashekhar": "ಚಂದ್ರಶೇಖರ್", "mamani": "ಮಾಮನಿ", "mahadevappa": "ಮಹಾದೇವಪ್ಪ",
    "shivalingappa": "ಶಿವಲಿಂಗಪ್ಪ", "yadawad": "ಯಾದವಾಡ", "channaraj": "ಚನ್ನರಾಜ್", "balappa": "ಬಾಳಪ್ಪ",
    "hattiholi": "ಹಟ್ಟಿಹೊಳಿ", "lakshmi": "ಲಕ್ಷ್ಮಿ", "hebbalkar": "ಹೆಬ್ಬಾಳಕರ್", "abhay": "ಅಭಯ್",
    "yediyurappa": "ಯಡಿಯೂರಪ್ಪ", "khadre": "ಖಾದ್ರೆ", "kharge": "ಖರ್ಗೆ", "mallikarjun": "ಮಲ್ಲಿಕಾರ್ಜುನ್",
    "priyank": "ಪ್ರಿಯಾಂಕ್", "eshwarappa": "ಈಶ್ವರಪ್ಪ", "byrathi": "ಬೈರತಿ", "basavaraj": "ಬಸವರಾಜ್",
    "uttam": "ಉತ್ತಮ್", "raosaheb": "ರಾವ್ಸಾಹೇಬ್", "kakaso": "ಕಾಕಾಸೋ", "pandurang": "ಪಾಂಡುರಂಗ"
}

def to_kannada(text):
    if not text or pd.isna(text):
        return ""
    s_raw = str(text).strip()
    s_clean = s_raw.lower()
    
    if s_clean in KANNADA_DICT:
        return KANNADA_DICT[s_clean]
        
    if re.search(r'[\u0C80-\u0CFF]', s_raw):
        return s_raw

    # Clean out stray periods between words e.g. "Laxman. Sangappa. Savadi"
    s_cleaned = re.sub(r'\.\s*', ' ', s_raw).strip()
    words = re.findall(r'\w+|\(|\)', s_cleaned)
    out_words = []
    for w in words:
        wl = w.lower()
        if wl in NAME_WORD_MAP:
            out_words.append(NAME_WORD_MAP[wl])
        elif len(w) == 1 and w.isalpha():
            out_words.append(NAME_WORD_MAP.get(w.lower(), w))
        else:
            out_words.append(w.title())
            
    return " ".join(out_words)

def clean_str(val):
    if not val:
        return ""
    s = str(val).lower()
    s = re.sub(r'\s*\((sc|st)\)', '', s)
    s = re.sub(r'[^a-z0-9]', '', s)
    return s

def make_slug(val):
    if not val:
        return ""
    s = str(val).lower()
    s = re.sub(r'[^a-z0-9\s_]', '', s)
    s = re.sub(r'\s+', '_', s.strip())
    if not s.endswith('_assembly_constituency'):
        s = s + '_assembly_constituency'
    return s

def process_all_years():
    xl = pd.ExcelFile(EXCEL_PATH)
    years = [sheet for sheet in xl.sheet_names if sheet.isdigit()]
    years.sort(key=int, reverse=True)

    master_records = {}

    for yr in years:
        df = xl.parse(yr)
        df.columns = [str(c).strip() for c in df.columns]
        
        records = []
        for idx, row in df.iterrows():
            ac_no = int(row.get("AC_NO", row.get("AC_No", idx + 1)))
            constituency = str(row.get("Constituency", f"Constituency #{ac_no}")).strip()
            cat = str(row.get("Category", "GEN")).strip()
            winner = str(row.get("Winner", "Abhyarthi")).strip()
            w_party = str(row.get("Winner_Party", "IND")).strip()
            w_votes = int(float(str(row.get("Winner_Votes", 0)).replace(",", ""))) if pd.notna(row.get("Winner_Votes")) else 0
            vote_share = float(str(row.get("Vote_Share", 0)).replace("%", "").strip()) if pd.notna(row.get("Vote_Share")) else 0.0
            runner = str(row.get("Runner_Up", "Runner")).strip()
            r_party = str(row.get("Runner_Up_Party", "IND")).strip()
            r_votes = int(float(str(row.get("Runner_Up_Votes", 0)).replace(",", ""))) if pd.notna(row.get("Runner_Up_Votes")) else 0
            margin = int(float(str(row.get("Margin", 0)).replace(",", ""))) if pd.notna(row.get("Margin")) else 0

            slug = make_slug(constituency)

            records.append({
                "year": int(yr),
                "ac_no": ac_no,
                "constituency": constituency,
                "constituency_kn": to_kannada(constituency),
                "clean_constituency": clean_str(constituency),
                "slug": slug,
                "category": cat,
                "category_kn": KANNADA_DICT.get(cat.lower(), "ಸಾಮಾನ್ಯ"),
                "winner": winner,
                "winner_kn": to_kannada(winner),
                "winner_party": w_party,
                "winner_party_kn": PARTY_KANNADA.get(w_party, w_party),
                "winner_votes": w_votes,
                "vote_share": vote_share,
                "runner_up": runner,
                "runner_up_kn": to_kannada(runner),
                "runner_up_party": r_party,
                "runner_up_party_kn": PARTY_KANNADA.get(r_party, r_party),
                "runner_up_votes": r_votes,
                "margin": margin,
                "color": PARTY_COLORS.get(w_party, DEFAULT_COLOR)
            })

        master_records[yr] = records

    output = {
        "title": "ಕರ್ನಾಟಕ ವಿಧಾನಸಭೆ ಚುನಾವಣಾ ಫಲಿತಾಂಶಗಳು (1978 – 2023)",
        "years": [int(y) for y in years],
        "party_colors": PARTY_COLORS,
        "party_kannada": PARTY_KANNADA,
        "records": master_records
    }

    store("elections_data.json", "elections_data", output)
    
    flat_rows = []
    for yr, r_list in master_records.items():
        flat_rows.extend(r_list)
    df_csv = pd.DataFrame(flat_rows)
    df_csv.to_csv(Path(__file__).parent.parent / "karnataka_elections_1978_2023.csv", index=False, encoding="utf-8-sig")

    print(f"Processed {len(years)} election years into data/elections_data.json & karnataka_elections_1978_2023.csv!")

if __name__ == "__main__":
    process_all_years()
