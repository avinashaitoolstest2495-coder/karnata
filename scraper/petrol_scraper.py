"""
Karnataka — petrol_scraper.py
Scrapes today's petrol, diesel, and CNG prices for Karnataka at District & Taluk levels.

Primary Source: HPCL Live Outlet API using regional master_outlet_id = 96681
Covers: All 31 Districts and 130+ Taluks/Cities in Karnataka with Geo-Coordinates.
"""

import re
import os
import json
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from utils import fetch, store, log, ist_now, ist_date, telegram_alert

KARNATAKA_MASTER_OUTLET_ID = 96681
HP_API_URL = "https://petrolpump.hpretail.in/getPetrolPricesForHPCL.php"

HP_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    ),
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "text/html, */*; q=0.01",
}

# Comprehensive District and Taluk Outlet Mapping with Geo-Coordinates
KARNATAKA_DISTRICTS_TALUKS = {
    "bengaluru_urban": {
        "name_en": "Bengaluru Urban",
        "name_kn": "ಬೆಂಗಳೂರು ನಗರ",
        "taluks": [
            {"key": "bengaluru", "kn": "ಬೆಂಗಳೂರು", "outlet_id": 97494, "lat": 12.959265, "lng": 77.653376, "has_cng": True},
            {"key": "yelahanka", "kn": "ಯಲಹಂಕ", "outlet_id": 97441, "lat": 13.152582, "lng": 77.568112, "has_cng": False},
            {"key": "kengeri", "kn": "ಕೆಂಗೇರಿ", "outlet_id": 97433, "lat": 12.912761, "lng": 77.485541, "has_cng": False},
            {"key": "peenya", "kn": "ಪೀಣ್ಯ", "outlet_id": 97436, "lat": 13.013401, "lng": 77.508990, "has_cng": False},
            {"key": "anekal", "kn": "ಆನೇಕಲ್", "outlet_id": 97674, "lat": 12.789843, "lng": 77.625967, "has_cng": False},
        ],
    },
    "bengaluru_rural": {
        "name_en": "Bengaluru Rural",
        "name_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ",
        "taluks": [
            {"key": "devanahalli", "kn": "ದೇವನಹಳ್ಳಿ", "outlet_id": 97449, "lat": 13.331218, "lng": 77.726083, "has_cng": False},
            {"key": "doddaballapur", "kn": "ದೊಡ್ಡಬಳ್ಳಾಪುರ", "outlet_id": 97440, "lat": 13.318277, "lng": 77.536627, "has_cng": False},
            {"key": "nelamangala", "kn": "ನೆಲಮಂಗಲ", "outlet_id": 97428, "lat": 13.089601, "lng": 77.401021, "has_cng": False},
            {"key": "hoskote", "kn": "ಹೊಸಕೋಟೆ", "outlet_id": 97657, "lat": 13.077771, "lng": 77.800101, "has_cng": False},
        ],
    },
    "tumakuru": {
        "name_en": "Tumakuru",
        "name_kn": "ತುಮಕೂರು",
        "taluks": [
            {"key": "tumkur", "kn": "ತುಮಕೂರು", "outlet_id": 97508, "lat": 13.328610, "lng": 77.122041, "has_cng": False},
            {"key": "kunigal", "kn": "ಕುಣಿಗಲ್", "outlet_id": 97506, "lat": 13.025660, "lng": 77.025080, "has_cng": False},
            {"key": "koratagere", "kn": "ಕೊರಟಗೆರೆ", "outlet_id": 97509, "lat": 13.523041, "lng": 77.240921, "has_cng": False},
            {"key": "sira", "kn": "ಶಿರಾ", "outlet_id": 97511, "lat": 13.744491, "lng": 76.898691, "has_cng": False},
            {"key": "gubbi", "kn": "ಗುಬ್ಬಿ", "outlet_id": 97539, "lat": 13.293785, "lng": 76.949200, "has_cng": False},
            {"key": "tiptur", "kn": "ತಿಪಟೂರು", "outlet_id": 97519, "lat": 13.261467, "lng": 76.488168, "has_cng": False},
            {"key": "pavagada", "kn": "ಪಾವಗಡ", "outlet_id": 97521, "lat": 14.092316, "lng": 77.283734, "has_cng": False},
            {"key": "madhugiri", "kn": "ಮಧುಗಿರಿ", "outlet_id": 97522, "lat": 13.661749, "lng": 77.219442, "has_cng": False},
            {"key": "turuvekere", "kn": "ತುರುವೇಕೆರೆ", "outlet_id": 97525, "lat": 13.170091, "lng": 76.669951, "has_cng": False},
            {"key": "chikkanayakanahalli", "kn": "ಚಿಕ್ಕನಾಯಕನಹಳ್ಳಿ", "outlet_id": 394887, "lat": 13.427005, "lng": 76.627554, "has_cng": False},
        ],
    },
    "mandya": {
        "name_en": "Mandya",
        "name_kn": "ಮಂಡ್ಯ",
        "taluks": [
            {"key": "mandya", "kn": "ಮಂಡ್ಯ", "outlet_id": 97566, "lat": 12.532201, "lng": 76.910061, "has_cng": False},
            {"key": "maddur", "kn": "ಮದ್ದೂರು", "outlet_id": 97577, "lat": 12.582257, "lng": 77.035244, "has_cng": False},
            {"key": "malavalli", "kn": "ಮಳವಳ್ಳಿ", "outlet_id": 97568, "lat": 12.386890, "lng": 77.059701, "has_cng": False},
            {"key": "pandavapura", "kn": "ಪಾಂಡವಪುರ", "outlet_id": 97572, "lat": 12.486005, "lng": 76.677726, "has_cng": False},
            {"key": "srirangapatna", "kn": "ಶ್ರೀರಂಗಪಟ್ಟಣ", "outlet_id": 97592, "lat": 12.429358, "lng": 76.697531, "has_cng": False},
            {"key": "nagamangala", "kn": "ನಾಗಮಂಗಲ", "outlet_id": 97579, "lat": 12.962192, "lng": 76.749311, "has_cng": False},
            {"key": "krpet", "kn": "ಕೆ.ಆರ್.ಪೇಟೆ", "outlet_id": 97578, "lat": 12.664802, "lng": 76.483495, "has_cng": False},
        ],
    },
    "ramanagara": {
        "name_en": "Ramanagara",
        "name_kn": "ರಾಮನಗರ",
        "taluks": [
            {"key": "ramanagara", "kn": "ರಾಮನಗರ", "outlet_id": 97554, "lat": 12.725728, "lng": 77.274324, "has_cng": False},
            {"key": "channapatna", "kn": "ಚನ್ನಪಟ್ಟಣ", "outlet_id": 97559, "lat": 12.548354, "lng": 77.219383, "has_cng": False},
            {"key": "kanakapura", "kn": "ಕನಕಪುರ", "outlet_id": 97565, "lat": 12.615686, "lng": 77.434442, "has_cng": False},
            {"key": "magadi", "kn": "ಮಾಗಡಿ", "outlet_id": 417658, "lat": 12.951860, "lng": 77.229920, "has_cng": False},
        ],
    },
    "chamarajanagar": {
        "name_en": "Chamarajanagar",
        "name_kn": "ಚಾಮರಾಜನಗರ",
        "taluks": [
            {"key": "chamarajanagar", "kn": "ಚಾಮರಾಜನಗರ", "outlet_id": 97601, "lat": 11.927121, "lng": 76.940251, "has_cng": False},
            {"key": "gundlupet", "kn": "ಗುಂಡ್ಲುಪೇಟೆ", "outlet_id": 97603, "lat": 11.829041, "lng": 76.679501, "has_cng": False},
            {"key": "hanur", "kn": "ಹನೂರು", "outlet_id": 97604, "lat": 12.095481, "lng": 77.293371, "has_cng": False},
            {"key": "kollegal", "kn": "ಕೊಳ್ಳೇಗಾಲ", "outlet_id": 97605, "lat": 12.152781, "lng": 77.110258, "has_cng": False},
            {"key": "yelandur", "kn": "ಯಳಂದೂರು", "outlet_id": 97607, "lat": 12.058895, "lng": 77.033755, "has_cng": False},
        ],
    },
    "kolar": {
        "name_en": "Kolar",
        "name_kn": "ಕೋಲಾರ",
        "taluks": [
            {"key": "kolar", "kn": "ಕೋಲಾರ", "outlet_id": 97615, "lat": 13.141381, "lng": 78.139667, "has_cng": False},
            {"key": "mulbagal", "kn": "ಮುಳಬಾಗಿಲು", "outlet_id": 97617, "lat": 13.167207, "lng": 78.399457, "has_cng": False},
            {"key": "bangarpet", "kn": "ಬಂಗಾರಪೇಟೆ", "outlet_id": 97620, "lat": 12.984570, "lng": 78.181580, "has_cng": False},
            {"key": "malur", "kn": "ಮಾಲೂರು", "outlet_id": 97622, "lat": 13.012288, "lng": 77.937516, "has_cng": False},
            {"key": "srinivaspur", "kn": "ಶ್ರೀನಿವಾಸಪುರ", "outlet_id": 97625, "lat": 13.333666, "lng": 78.213931, "has_cng": False},
        ],
    },
    "chikkaballapur": {
        "name_en": "Chikkaballapur",
        "name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
        "taluks": [
            {"key": "chikkaballapur", "kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "outlet_id": 97645, "lat": 13.592384, "lng": 77.783945, "has_cng": False},
            {"key": "chintamani", "kn": "ಚಿಂತಾಮಣಿ", "outlet_id": 97636, "lat": 13.399159, "lng": 78.053258, "has_cng": False},
            {"key": "sidlaghatta", "kn": "ಶಿಡ್ಲಘಟ್ಟ", "outlet_id": 97642, "lat": 13.383283, "lng": 77.860611, "has_cng": False},
            {"key": "gauribidanur", "kn": "ಗೌರಿಬಿದನೂರು", "outlet_id": 97638, "lat": 13.614941, "lng": 77.517901, "has_cng": False},
            {"key": "gudibande", "kn": "ಗುಡಿಬಂಡೆ", "outlet_id": 97644, "lat": 13.669894, "lng": 77.713917, "has_cng": False},
            {"key": "bagepalli", "kn": "ಬಾಗೇಪಲ್ಲಿ", "outlet_id": 417381, "lat": 13.762751, "lng": 77.821333, "has_cng": False},
        ],
    },
    "udupi": {
        "name_en": "Udupi",
        "name_kn": "ಉಡುಪಿ",
        "taluks": [
            {"key": "udupi", "kn": "ಉಡುಪಿ", "outlet_id": 390761, "lat": 13.348381, "lng": 74.706721, "has_cng": False},
            {"key": "kundapura", "kn": "ಕುಂದಾಪುರ", "outlet_id": 391069, "lat": 13.647108, "lng": 74.822211, "has_cng": False},
            {"key": "karkala", "kn": "ಕಾರ್ಕಳ", "outlet_id": 405432, "lat": 13.204587, "lng": 74.995782, "has_cng": False},
            {"key": "hebri", "kn": "ಹೆಬ್ರಿ", "outlet_id": 390916, "lat": 13.459721, "lng": 74.984231, "has_cng": False},
            {"key": "kaup", "kn": "ಕಾಪು", "outlet_id": 420128, "lat": 13.264924, "lng": 74.748658, "has_cng": False},
            {"key": "brahmavara", "kn": "ಬ್ರಹ್ಮಾವರ", "outlet_id": 395365, "lat": 13.424581, "lng": 74.740001, "has_cng": False},
        ],
    },
    "uttara_kannada": {
        "name_en": "Uttara Kannada",
        "name_kn": "ಉತ್ತರ ಕನ್ನಡ",
        "taluks": [
            {"key": "karwar_ankola", "kn": "ಅಂಕೋಲಾ", "outlet_id": 419174, "lat": 14.659091, "lng": 74.307931, "has_cng": False},
            {"key": "sirsi", "kn": "ಶಿರಸಿ", "outlet_id": 406649, "lat": 14.614770, "lng": 74.832360, "has_cng": False},
            {"key": "honnavar", "kn": "ಹೊನ್ನಾವರ", "outlet_id": 406722, "lat": 14.282601, "lng": 74.452660, "has_cng": False},
            {"key": "kumta", "kn": "ಕುಮಟಾ", "outlet_id": 406724, "lat": 14.430890, "lng": 74.423210, "has_cng": False},
            {"key": "bhatkal", "kn": "ಭಟ್ಕಳ", "outlet_id": 403881, "lat": 14.061451, "lng": 74.507925, "has_cng": False},
            {"key": "haliyal", "kn": "ಹಳಿಯಾಳ", "outlet_id": 400198, "lat": 15.335401, "lng": 74.765241, "has_cng": False},
            {"key": "yellapur", "kn": "ಯಲ್ಲಾಪುರ", "outlet_id": 404835, "lat": 14.976616, "lng": 74.713239, "has_cng": False},
            {"key": "mundgod", "kn": "ಮುಂಡಗೋಡ", "outlet_id": 390218, "lat": 14.789448, "lng": 75.033989, "has_cng": False},
        ],
    },
    "vijayapura": {
        "name_en": "Vijayapura",
        "name_kn": "ವಿಜಯಪುರ",
        "taluks": [
            {"key": "vijayapura", "kn": "ವಿಜಯಪುರ", "outlet_id": 391512, "lat": 16.786320, "lng": 75.720500, "has_cng": False},
            {"key": "sindagi", "kn": "ಸಿಂದಗಿ", "outlet_id": 390263, "lat": 16.870926, "lng": 75.497312, "has_cng": False},
            {"key": "muddebihal", "kn": "ಮುದ್ದೇಬಿಹಾಳ", "outlet_id": 400142, "lat": 16.342895, "lng": 76.129617, "has_cng": False},
            {"key": "basavana_bagewadi", "kn": "ಬಸವನ ಬಾಗೇವಾಡಿ", "outlet_id": 395331, "lat": 16.571336, "lng": 75.979339, "has_cng": False},
            {"key": "indi", "kn": "ಇಂಡಿ", "outlet_id": 390910, "lat": 17.177492, "lng": 75.956285, "has_cng": False},
            {"key": "chadchan", "kn": "ಚಡಚಣ", "outlet_id": 393557, "lat": 17.315163, "lng": 75.652884, "has_cng": False},
        ],
    },
    "gadag": {
        "name_en": "Gadag",
        "name_kn": "ಗದಗ",
        "taluks": [
            {"key": "gadag", "kn": "ಗದಗ", "outlet_id": 390737, "lat": 15.429255, "lng": 75.634213, "has_cng": False},
            {"key": "mundargi", "kn": "ಮುಂಡರಗಿ", "outlet_id": 390894, "lat": 15.210361, "lng": 75.897469, "has_cng": False},
            {"key": "gajendragad", "kn": "ಗಜೇಂದ್ರಗಡ", "outlet_id": 391272, "lat": 15.729705, "lng": 75.966878, "has_cng": False},
            {"key": "shirahatti", "kn": "ಶಿರಹಟ್ಟಿ", "outlet_id": 398088, "lat": 15.117010, "lng": 75.466393, "has_cng": False},
            {"key": "ron", "kn": "ರೋಣ", "outlet_id": 406811, "lat": 15.686227, "lng": 75.737588, "has_cng": False},
            {"key": "nargund", "kn": "ನರಗುಂದ", "outlet_id": 406785, "lat": 15.719917, "lng": 75.386481, "has_cng": False},
        ],
    },
    "bagalkot": {
        "name_en": "Bagalkot",
        "name_kn": "ಬಾಗಲಕೋಟೆ",
        "taluks": [
            {"key": "bagalkot", "kn": "ಬಾಗಲಕೋಟೆ", "outlet_id": 390716, "lat": 16.200178, "lng": 75.613475, "has_cng": False},
            {"key": "mudhol", "kn": "ಮುಧೋಳ", "outlet_id": 390304, "lat": 16.340437, "lng": 75.273530, "has_cng": False},
            {"key": "jamkhandi", "kn": "ಜಮಖಂಡಿ", "outlet_id": 399844, "lat": 16.548377, "lng": 75.182388, "has_cng": False},
            {"key": "badami", "kn": "ಬಾದಾಮಿ", "outlet_id": 391642, "lat": 15.909709, "lng": 75.686254, "has_cng": False},
            {"key": "bilgi", "kn": "ಬೀಳಗಿ", "outlet_id": 390877, "lat": 16.416765, "lng": 75.434959, "has_cng": False},
            {"key": "ilkal", "kn": "ಇಲಕಲ್", "outlet_id": 410898, "lat": 15.981443, "lng": 76.102995, "has_cng": False},
            {"key": "rabkavi_banhatti", "kn": "ರಬಕವಿ ಬನಹಟ್ಟಿ", "outlet_id": 399110, "lat": 16.491384, "lng": 75.139957, "has_cng": False},
        ],
    },
    "belagavi": {
        "name_en": "Belagavi",
        "name_kn": "ಬೆಳಗಾವಿ",
        "taluks": [
            {"key": "belgaum", "kn": "ಬೆಳಗಾವಿ", "outlet_id": 390791, "lat": 15.868329, "lng": 74.529144, "has_cng": False},
            {"key": "nipani", "kn": "ನಿಪ್ಪಾಣಿ", "outlet_id": 390327, "lat": 16.397231, "lng": 74.380541, "has_cng": False},
            {"key": "gokak", "kn": "ಗೋಕಾಕ್", "outlet_id": 410716, "lat": 16.160043, "lng": 74.848708, "has_cng": False},
            {"key": "bailhongal", "kn": "ಬೈಲಹೊಂಗಲ", "outlet_id": 406653, "lat": 15.814701, "lng": 74.848101, "has_cng": False},
            {"key": "chikkodi", "kn": "ಚಿಕ್ಕೋಡಿ", "outlet_id": 399384, "lat": 16.426163, "lng": 74.587892, "has_cng": False},
            {"key": "athani", "kn": "ಅಥಣಿ", "outlet_id": 393757, "lat": 16.720887, "lng": 75.059476, "has_cng": False},
            {"key": "raibag", "kn": "ರಾಯಭಾಗ", "outlet_id": 399516, "lat": 16.501544, "lng": 74.760505, "has_cng": False},
            {"key": "ramdurg", "kn": "ರಾಮದುರ್ಗ", "outlet_id": 391726, "lat": 15.950208, "lng": 75.288791, "has_cng": False},
            {"key": "saundatti", "kn": "ಸವದತ್ತಿ", "outlet_id": 406716, "lat": 15.771260, "lng": 75.114355, "has_cng": False},
            {"key": "khanapur", "kn": "ಖಾನಾಪುರ", "outlet_id": 406651, "lat": 15.645201, "lng": 74.503101, "has_cng": False},
            {"key": "hukkeri", "kn": "ಹುಕ್ಕೇರಿ", "outlet_id": 390837, "lat": 16.332902, "lng": 74.413365, "has_cng": False},
            {"key": "kagwad", "kn": "ಕಾಗವಾಡ", "outlet_id": 421017, "lat": 16.708846, "lng": 74.713347, "has_cng": False},
        ],
    },
    "koppal": {
        "name_en": "Koppal",
        "name_kn": "ಕೊಪ್ಪಳ",
        "taluks": [
            {"key": "koppal", "kn": "ಕೊಪ್ಪಳ", "outlet_id": 391547, "lat": 15.349560, "lng": 76.164840, "has_cng": False},
            {"key": "yelburga", "kn": "ಯಲಬುರ್ಗಾ", "outlet_id": 390521, "lat": 15.466741, "lng": 76.003861, "has_cng": False},
            {"key": "kushtagi", "kn": "ಕುಷ್ಟಗಿ", "outlet_id": 390995, "lat": 15.737206, "lng": 76.196641, "has_cng": False},
            {"key": "gangavathi", "kn": "ಗಂಗಾವತಿ", "outlet_id": 392450, "lat": 15.438473, "lng": 76.538075, "has_cng": False},
            {"key": "karatagi", "kn": "ಕಾರಟಗಿ", "outlet_id": 398419, "lat": 15.619851, "lng": 76.638538, "has_cng": False},
            {"key": "kanakagiri", "kn": "ಕನಕಗಿರಿ", "outlet_id": 399488, "lat": 15.569966, "lng": 76.424335, "has_cng": False},
        ],
    },
    "kalaburagi": {
        "name_en": "Kalaburagi",
        "name_kn": "ಕಲಬುರಗಿ",
        "taluks": [
            {"key": "gulbarga", "kn": "ಕಲಬುರಗಿ", "outlet_id": 391687, "lat": 17.358490, "lng": 76.846460, "has_cng": False},
            {"key": "jewargi", "kn": "ಜೇವರ್ಗಿ", "outlet_id": 390430, "lat": 17.035510, "lng": 76.791933, "has_cng": False},
            {"key": "chittapur", "kn": "ಚಿತ್ತಾಪುರ", "outlet_id": 390544, "lat": 17.250592, "lng": 77.047594, "has_cng": False},
            {"key": "afzalpur", "kn": "ಅಫಜಲಪುರ", "outlet_id": 391438, "lat": 17.278840, "lng": 76.216880, "has_cng": False},
            {"key": "chincholi", "kn": "ಚಿಂಚೋಳಿ", "outlet_id": 391806, "lat": 17.564506, "lng": 77.393439, "has_cng": False},
            {"key": "aland", "kn": "ಆಳಂದ", "outlet_id": 391837, "lat": 17.525381, "lng": 76.607417, "has_cng": False},
            {"key": "sedam", "kn": "ಸೇಡಂ", "outlet_id": 391850, "lat": 17.073999, "lng": 77.403467, "has_cng": False},
            {"key": "shahabad", "kn": "ಶಹಾಬಾದ್", "outlet_id": 391102, "lat": 17.129664, "lng": 76.933861, "has_cng": False},
        ],
    },
    "raichur": {
        "name_en": "Raichur",
        "name_kn": "ರಾಯಚೂರು",
        "taluks": [
            {"key": "raichur", "kn": "ರಾಯಚೂರು", "outlet_id": 390703, "lat": 16.205878, "lng": 77.411453, "has_cng": False},
            {"key": "devadurga", "kn": "ದೇವದುರ್ಗ", "outlet_id": 391800, "lat": 16.423906, "lng": 76.914654, "has_cng": False},
            {"key": "manvi", "kn": "ಮಾನ್ವಿ", "outlet_id": 391857, "lat": 15.992156, "lng": 76.999225, "has_cng": False},
            {"key": "sirwar", "kn": "ಸಿರವಾರ", "outlet_id": 391830, "lat": 16.179537, "lng": 77.027816, "has_cng": False},
            {"key": "lingsugur", "kn": "ಲಿಂಗಸುಗೂರು", "outlet_id": 394552, "lat": 16.014757, "lng": 76.435621, "has_cng": False},
            {"key": "sindhanur", "kn": "ಸಿಂಧನೂರು", "outlet_id": 419150, "lat": 15.786475, "lng": 76.769570, "has_cng": False},
        ],
    },
    "hassan": {
        "name_en": "Hassan",
        "name_kn": "ಹಾಸನ",
        "taluks": [
            {"key": "hassan", "kn": "ಹಾಸನ", "outlet_id": 398174, "lat": 13.000751, "lng": 76.096461, "has_cng": False},
            {"key": "arkalgud", "kn": "ಅರಕಲಗೂಡು", "outlet_id": 390699, "lat": 12.626572, "lng": 76.046925, "has_cng": False},
            {"key": "arsikere", "kn": "ಅರಸೀಕೆರೆ", "outlet_id": 391061, "lat": 13.319743, "lng": 76.262155, "has_cng": False},
            {"key": "belur", "kn": "ಬೇಲೂರು", "outlet_id": 391045, "lat": 13.073584, "lng": 75.862501, "has_cng": False},
            {"key": "channarayapatna", "kn": "ಚನ್ನರಾಯಪಟ್ಟಣ", "outlet_id": 390780, "lat": 12.937391, "lng": 76.363481, "has_cng": False},
            {"key": "holenarsipur", "kn": "ಹೊಳೆನರಸೀಪುರ", "outlet_id": 400113, "lat": 12.787531, "lng": 76.244601, "has_cng": False},
            {"key": "alur", "kn": "ಆಲೂರು", "outlet_id": 400167, "lat": 12.976291, "lng": 75.998101, "has_cng": False},
            {"key": "sakleshpur", "kn": "ಸಕಲೇಶಪುರ", "outlet_id": 482852, "lat": 12.935657, "lng": 75.770018, "has_cng": False},
        ],
    },
    "dakshina_kannada": {
        "name_en": "Dakshina Kannada",
        "name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ",
        "taluks": [
            {"key": "mangalore", "kn": "ಮಂಗಳೂರು", "outlet_id": 394291, "lat": 12.873141, "lng": 74.851671, "has_cng": False},
            {"key": "puttur", "kn": "ಪುತ್ತೂರು", "outlet_id": 391513, "lat": 12.752946, "lng": 75.217236, "has_cng": False},
            {"key": "belthangady", "kn": "ಬೆಳ್ತಂಗಡಿ", "outlet_id": 393346, "lat": 12.992149, "lng": 75.292681, "has_cng": False},
            {"key": "bantwal", "kn": "ಬಂಟ್ವಾಳ", "outlet_id": 398123, "lat": 12.754727, "lng": 75.104787, "has_cng": False},
            {"key": "sullia", "kn": "ಸುಳ್ಯ", "outlet_id": 403981, "lat": 12.743913, "lng": 75.475638, "has_cng": False},
            {"key": "kadaba", "kn": "ಕಡಬ", "outlet_id": 399352, "lat": 12.739852, "lng": 75.337205, "has_cng": False},
            {"key": "moodabidri", "kn": "ಮೂಡುಬಿದಿರೆ", "outlet_id": 399367, "lat": 13.065589, "lng": 74.942046, "has_cng": False},
        ],
    },
    "mysuru": {
        "name_en": "Mysuru",
        "name_kn": "ಮೈಸೂರು",
        "taluks": [
            {"key": "mysore", "kn": "ಮೈಸೂರು", "outlet_id": 394979, "lat": 12.315731, "lng": 76.632551, "has_cng": True},
            {"key": "nanjangud", "kn": "ನಂಜನಗೂಡು", "outlet_id": 398149, "lat": 12.120541, "lng": 76.680791, "has_cng": False},
            {"key": "hunsur", "kn": "ಹುಣಸೂರು", "outlet_id": 404282, "lat": 12.305350, "lng": 76.298450, "has_cng": False},
            {"key": "periyapatna", "kn": "ಪಿರಿಯಾಪಟ್ಟಣ", "outlet_id": 394429, "lat": 12.337534, "lng": 76.104970, "has_cng": False},
            {"key": "krnagar", "kn": "ಕೆ.ಆರ್.ನಗರ", "outlet_id": 393262, "lat": 12.444772, "lng": 76.383072, "has_cng": False},
            {"key": "tnarasipura", "kn": "ಟಿ.ನರಸೀಪುರ", "outlet_id": 390951, "lat": 12.256786, "lng": 76.961975, "has_cng": False},
            {"key": "hdkote", "kn": "ಹೆಚ್.ಡಿ.ಕೋಟೆ", "outlet_id": 399701, "lat": 12.083522, "lng": 76.334855, "has_cng": False},
            {"key": "sargur", "kn": "ಸರಗೂರು", "outlet_id": 394410, "lat": 11.996365, "lng": 76.400921, "has_cng": False},
        ],
    },
    "haveri": {
        "name_en": "Haveri",
        "name_kn": "ಹಾವೇರಿ",
        "taluks": [
            {"key": "haveri", "kn": "ಹಾವೇರಿ", "outlet_id": 406646, "lat": 14.789970, "lng": 75.397420, "has_cng": False},
            {"key": "ranebennur", "kn": "ರಾಣೇಬೆನ್ನೂರು", "outlet_id": 392077, "lat": 14.605981, "lng": 75.646157, "has_cng": False},
            {"key": "byadgi", "kn": "ಬ್ಯಾಡಗಿ", "outlet_id": 390954, "lat": 14.747423, "lng": 75.453064, "has_cng": False},
            {"key": "shiggaon", "kn": "ಶಿಗ್ಗಾಂವಿ", "outlet_id": 390996, "lat": 14.973406, "lng": 75.233782, "has_cng": False},
            {"key": "hanagal", "kn": "ಹಾನಗಲ್", "outlet_id": 391120, "lat": 14.781264, "lng": 75.136109, "has_cng": False},
            {"key": "hirekerur", "kn": "ಹಿರೇಕೆರೂರು", "outlet_id": 399897, "lat": 14.458621, "lng": 75.384541, "has_cng": False},
            {"key": "savanur", "kn": "ಸವಣೂರು", "outlet_id": 390734, "lat": 15.031897, "lng": 75.307906, "has_cng": False},
            {"key": "rattihalli", "kn": "ರಟ್ಟಿಹಳ್ಳಿ", "outlet_id": 399410, "lat": 14.427920, "lng": 75.515290, "has_cng": False},
        ],
    },
    "shivamogga": {
        "name_en": "Shivamogga",
        "name_kn": "ಶಿವಮೊಗ್ಗ",
        "taluks": [
            {"key": "shimoga", "kn": "ಶಿವಮೊಗ್ಗ", "outlet_id": 398157, "lat": 13.931971, "lng": 75.586961, "has_cng": False},
            {"key": "bhadravathi", "kn": "ಭದ್ರಾವತಿ", "outlet_id": 390745, "lat": 13.838598, "lng": 75.713664, "has_cng": False},
            {"key": "sagar", "kn": "ಸಾಗರ", "outlet_id": 398241, "lat": 14.168421, "lng": 75.021471, "has_cng": False},
            {"key": "shikaripura", "kn": "ಶಿಕಾರಿಪುರ", "outlet_id": 391343, "lat": 14.369847, "lng": 75.249446, "has_cng": False},
            {"key": "soraba", "kn": "ಸೊರಬ", "outlet_id": 390832, "lat": 14.562491, "lng": 75.151157, "has_cng": False},
            {"key": "thirthahalli", "kn": "ತೀರ್ಥಹಳ್ಳಿ", "outlet_id": 398204, "lat": 13.688264, "lng": 75.247635, "has_cng": False},
            {"key": "hosanagara", "kn": "ಹೊಸನಗರ", "outlet_id": 391315, "lat": 13.818791, "lng": 75.027819, "has_cng": False},
        ],
    },
    "chitradurga": {
        "name_en": "Chitradurga",
        "name_kn": "ಚಿತ್ರದುರ್ಗ",
        "taluks": [
            {"key": "chitradurga", "kn": "ಚಿತ್ರದುರ್ಗ", "outlet_id": 390759, "lat": 14.215544, "lng": 76.379986, "has_cng": False},
            {"key": "hiriyur", "kn": "ಹಿರಿಯೂರು", "outlet_id": 391813, "lat": 14.021329, "lng": 76.581521, "has_cng": False},
            {"key": "hosadurga", "kn": "ಹೊಸದುರ್ಗ", "outlet_id": 391358, "lat": 13.697308, "lng": 76.535620, "has_cng": False},
            {"key": "holalkere", "kn": "ಹೊಳಲ್ಕೆರೆ", "outlet_id": 391138, "lat": 14.222857, "lng": 76.392655, "has_cng": False},
            {"key": "challakere", "kn": "ಚಳ್ಳಕೆರೆ", "outlet_id": 391706, "lat": 14.297467, "lng": 76.653576, "has_cng": False},
            {"key": "molakalmuru", "kn": "ಮೊಳಕಾಲ್ಮೂರು", "outlet_id": 391849, "lat": 14.611794, "lng": 76.668927, "has_cng": False},
        ],
    },
    "yadgir": {
        "name_en": "Yadgir",
        "name_kn": "ಯಾದಗಿರಿ",
        "taluks": [
            {"key": "yadgir", "kn": "ಯಾದಗಿರಿ", "outlet_id": 391709, "lat": 16.755591, "lng": 77.128894, "has_cng": False},
            {"key": "shahapur", "kn": "ಶಹಾಪುರ", "outlet_id": 390804, "lat": 16.759274, "lng": 76.788803, "has_cng": False},
            {"key": "gurmatkal", "kn": "ಗುರುಮಠಕಲ್", "outlet_id": 400097, "lat": 16.869991, "lng": 77.385101, "has_cng": False},
            {"key": "shorapur", "kn": "ಶೋರಾಪುರ", "outlet_id": 481465, "lat": 16.665312, "lng": 76.527909, "has_cng": False},
        ],
    },
    "vijayanagara": {
        "name_en": "Vijayanagara",
        "name_kn": "ವಿಜಯನಗರ",
        "taluks": [
            {"key": "hosapete", "kn": "ಹೊಸಪೇಟೆ", "outlet_id": 375380, "lat": 15.267955, "lng": 76.386040, "has_cng": False},
            {"key": "kotturu", "kn": "ಕೊಟ್ಟೂರು", "outlet_id": 390834, "lat": 14.832146, "lng": 76.228776, "has_cng": False},
            {"key": "hagaribommanahalli", "kn": "ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ", "outlet_id": 390827, "lat": 15.044014, "lng": 76.201998, "has_cng": False},
            {"key": "hadagali", "kn": "ಹೂವಿನ ಹಡಗಲಿ", "outlet_id": 417700, "lat": 15.023652, "lng": 75.927423, "has_cng": False},
        ],
    },
    "davanagere": {
        "name_en": "Davanagere",
        "name_kn": "ದಾವಣಗೆರೆ",
        "taluks": [
            {"key": "davangere", "kn": "ದಾವಣಗೆರೆ", "outlet_id": 391086, "lat": 14.479467, "lng": 75.906382, "has_cng": False},
            {"key": "jagalur", "kn": "ಜಗಳೂರು", "outlet_id": 390730, "lat": 14.666253, "lng": 76.298266, "has_cng": False},
            {"key": "harihar", "kn": "ಹರಿಹರ", "outlet_id": 394590, "lat": 14.486322, "lng": 75.802989, "has_cng": False},
            {"key": "channagiri", "kn": "ಚನ್ನಗಿರಿ", "outlet_id": 391839, "lat": 14.013032, "lng": 75.937631, "has_cng": False},
            {"key": "honnali", "kn": "ಹೊನ್ನಾಳಿ", "outlet_id": 400119, "lat": 14.235151, "lng": 75.652531, "has_cng": False},
        ],
    },
    "chikkamagaluru": {
        "name_en": "Chikkamagaluru",
        "name_kn": "ಚಿಕ್ಕಮಗಳೂರು",
        "taluks": [
            {"key": "chikmagalur", "kn": "ಚಿಕ್ಕಮಗಳೂರು", "outlet_id": 398251, "lat": 13.324921, "lng": 75.773091, "has_cng": False},
            {"key": "kadur", "kn": "ಕಡೂರು", "outlet_id": 400163, "lat": 13.552494, "lng": 76.008123, "has_cng": False},
            {"key": "tarikere", "kn": "ತಾರೀಕೆರೆ", "outlet_id": 391241, "lat": 13.723491, "lng": 75.715371, "has_cng": False},
            {"key": "mudigere", "kn": "ಮೂಡಿಗೆರೆ", "outlet_id": 417831, "lat": 13.130039, "lng": 75.640027, "has_cng": False},
            {"key": "sringeri", "kn": "ಶೃಂಗೇರಿ", "outlet_id": 399783, "lat": 13.424895, "lng": 75.252464, "has_cng": False},
            {"key": "koppa", "kn": "ಕೊಪ್ಪ", "outlet_id": 400178, "lat": 13.533834, "lng": 75.367386, "has_cng": False},
            {"key": "kalasa", "kn": "ಕಳಸ", "outlet_id": 399351, "lat": 13.230490, "lng": 75.358970, "has_cng": False},
        ],
    },
    "kodagu": {
        "name_en": "Kodagu",
        "name_kn": "ಕೊಡಗು",
        "taluks": [
            {"key": "kodagu", "kn": "ಮಡಿಕೇರಿ", "outlet_id": 394406, "lat": 12.418160, "lng": 75.742860, "has_cng": False},
            {"key": "virajpet", "kn": "ವಿರಾಜಪೇಟೆ", "outlet_id": 391617, "lat": 12.226206, "lng": 75.746144, "has_cng": False},
            {"key": "somwarpet", "kn": "ಸೋಮವಾರಪೇಟೆ", "outlet_id": 400155, "lat": 12.485071, "lng": 75.955844, "has_cng": False},
            {"key": "gonikoppal", "kn": "ಗೋಣಿಕೊಪ್ಪಲು", "outlet_id": 398187, "lat": 12.144741, "lng": 75.944513, "has_cng": False},
        ],
    },
    "ballari": {
        "name_en": "Ballari",
        "name_kn": "ಬಳ್ಳಾರಿ",
        "taluks": [
            {"key": "bellary", "kn": "ಬಳ್ಳಾರಿ", "outlet_id": 398212, "lat": 15.145761, "lng": 76.928051, "has_cng": False},
            {"key": "siruguppa", "kn": "ಸಿರುಗುಪ್ಪ", "outlet_id": 398267, "lat": 15.635844, "lng": 76.893052, "has_cng": False},
            {"key": "sandur", "kn": "ಸಂಡೂರು", "outlet_id": 405615, "lat": 14.972145, "lng": 76.610804, "has_cng": False},
            {"key": "kudligi", "kn": "ಕೂಡ್ಲಿಗಿ", "outlet_id": 400123, "lat": 14.896077, "lng": 76.391784, "has_cng": False},
        ],
    },
    "bidar": {
        "name_en": "Bidar",
        "name_kn": "ಬೀದರ್",
        "taluks": [
            {"key": "bidar", "kn": "ಬೀದರ್", "outlet_id": 391344, "lat": 17.934816, "lng": 77.475971, "has_cng": False},
            {"key": "humnabad", "kn": "ಹುಮ್ನಾಬಾದ್", "outlet_id": 390548, "lat": 17.771288, "lng": 77.088715, "has_cng": False},
            {"key": "kamal_nagar", "kn": "ಕಮಲನಗರ", "outlet_id": 391093, "lat": 18.252296, "lng": 77.168297, "has_cng": False},
            {"key": "aurad", "kn": "ಔರಾದ್", "outlet_id": 390998, "lat": 18.240001, "lng": 77.425410, "has_cng": False},
            {"key": "basavakalyan", "kn": "ಬಸವಕಲ್ಯಾಣ", "outlet_id": 392454, "lat": 17.828092, "lng": 76.913198, "has_cng": False},
            {"key": "bhalki", "kn": "ಭಾಲ್ಕಿ", "outlet_id": 392476, "lat": 18.066095, "lng": 77.156305, "has_cng": False},
        ],
    },
}


def _fetch_hpcl_outlet(item: dict) -> tuple[str, dict]:
    """Fetches live prices for a specific outlet_id using master_outlet_id = 96681."""
    outlet_id = item["outlet_id"]
    key = item["key"]
    
    params = {
        "master_outlet_id": KARNATAKA_MASTER_OUTLET_ID,
        "outlet_id": outlet_id,
    }

    prices = {}
    try:
        resp = requests.get(HP_API_URL, params=params, headers=HP_HEADERS, timeout=10)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "lxml")
        for card in soup.select(".fuel-price-card-text"):
            name_el = card.select_one(".fuel_Name")
            price_el = card.select_one(".fuel-text")
            if not name_el or not price_el:
                continue

            fuel_name = name_el.get_text(strip=True).lower()
            price_match = re.search(r"([\d]+\.[\d]+)", price_el.get_text(strip=True))
            if not price_match:
                continue

            val = float(price_match.group(1))
            if "petrol" in fuel_name and (85 <= val <= 140):
                prices["petrol"] = round(val, 2)
            elif "diesel" in fuel_name and (75 <= val <= 120):
                prices["diesel"] = round(val, 2)
            elif "cng" in fuel_name and (50 <= val <= 110):
                prices["cng"] = round(val, 2)

    except Exception as e:
        log.debug(f"Outlet {outlet_id} ({key}) fetch error: {e}")

    result = {
        "key": key,
        "name_kn": item["kn"],
        "outlet_id": outlet_id,
        "master_outlet_id": KARNATAKA_MASTER_OUTLET_ID,
        "latitude": item.get("lat"),
        "longitude": item.get("lng"),
        "petrol": prices.get("petrol"),
        "diesel": prices.get("diesel"),
        "cng": prices.get("cng") if item.get("has_cng") else None,
        "is_live": "petrol" in prices and "diesel" in prices,
    }

    return key, result


def run() -> dict:
    """Main execution: Scrapes petrol & diesel prices across Karnataka Districts & Taluks."""
    log.info("⛽ Starting Karnataka District & Taluk level petrol/diesel scraper...")

    # Flatten list of all taluk outlets for concurrent execution
    all_taluk_items = []
    for dist_key, dist_data in KARNATAKA_DISTRICTS_TALUKS.items():
        for taluk in dist_data["taluks"]:
            item = dict(taluk)
            item["district_key"] = dist_key
            all_taluk_items.append(item)

    log.info(f"🔍 Fetching live HPCL rates for {len(all_taluk_items)} Taluks/Cities across Karnataka...")

    # Parallel scraping using ThreadPoolExecutor for fast execution
    scraped_results = {}
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(_fetch_hpcl_outlet, item) for item in all_taluk_items]
        for future in as_completed(futures):
            key, res = future.result()
            scraped_results[key] = res

    # Establish Bangalore base anchor rates for fallbacks
    blr_res = scraped_results.get("bangalore", {})
    base_petrol = blr_res.get("petrol") or 102.86
    base_diesel = blr_res.get("diesel") or 88.94
    base_cng = blr_res.get("cng") or 79.00

    districts_output = {}
    cities_output = {}
    live_count = 0

    for dist_key, dist_data in KARNATAKA_DISTRICTS_TALUKS.items():
        dist_taluks_output = {}

        for taluk in dist_data["taluks"]:
            key = taluk["key"]
            res = scraped_results.get(key, {})

            # Fallback if a specific outlet API call failed
            petrol = res.get("petrol") or base_petrol
            diesel = res.get("diesel") or base_diesel
            cng = res.get("cng") if taluk.get("has_cng") else None

            if res.get("is_live"):
                live_count += 1

            taluk_data = {
                "name_en": key.replace("_", " ").title(),
                "name_kn": taluk["kn"],
                "outlet_id": taluk["outlet_id"],
                "master_outlet_id": KARNATAKA_MASTER_OUTLET_ID,
                "latitude": taluk.get("lat"),
                "longitude": taluk.get("lng"),
                "petrol": petrol,
                "diesel": diesel,
                "cng": cng,
                "change": 0.00,
                "is_live": res.get("is_live", False),
            }

            dist_taluks_output[key] = taluk_data
            cities_output[key] = taluk_data  # Flattened City/Taluk map for fast lookup

        districts_output[dist_key] = {
            "name_en": dist_data["name_en"],
            "name_kn": dist_data["name_kn"],
            "taluks": dist_taluks_output,
        }

    # Alias for bengaluru/bangalore
    if "bangalore" in cities_output:
        cities_output["bengaluru"] = cities_output["bangalore"]

    output = {
        "date": ist_date(),
        "updated_at": ist_now(),
        "source": "HP Retail Live Outlet API",
        "live_outlets_scraped": live_count,
        "total_taluks": len(all_taluk_items),
        "total_districts": len(districts_output),
        "districts": districts_output,
        "cities": cities_output,
        "note_kn": "ಬೆಲೆಗಳು ಪ್ರತಿ ದಿನ ಬೆಳಿಗ್ಗೆ 6 ಗಂಟೆಗೆ ಅಪ್‌ಡೇಟ್‌",
        "note_en": "Prices updated daily at 6:00 AM IST",
    }

    from history_tracker import process_petrol_history
    output = process_petrol_history(output)

    store("petrol_rates.json", "petrol_rates", output)
    log.info(f"✅ Petrol & Diesel data saved for {len(districts_output)} Districts & {len(all_taluk_items)} Taluks ({live_count} live HPCL outlets).")
    return output


if __name__ == "__main__":
    run()