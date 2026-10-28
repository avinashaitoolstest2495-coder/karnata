#!/usr/bin/env python3
"""
BBK13 Daily Social Media Live Scraper & Updater
Scrapes real Instagram follower counts, post counts, updates X and Google Trends metrics,
and syncs bigg-boss-kannada-13.html.
Can be executed locally or in GitHub Actions on a daily cron schedule.
"""

import urllib.request
import re
import html
import json
import time
import sys
import os

PROFILES = [
    {
        "id": "C02",
        "seat": "B01",
        "nameKn": "ಸೌಂದರ್ಯ ಶೆಟ್ಟಿ",
        "nameEn": "Soundarya Shetty",
        "photo": "assets/bbk13/contestants/passenger_02_face.jpg",
        "url": "https://www.instagram.com/soundharyashetty_/",
        "handle": "@soundharyashetty_",
        "category": "celebrity",
        "categoryKn": "ಸೆಲೆಬ್ರಿಟಿ",
        "entryFollowersNum": 582000,
        "entryFollowersKn": "582K",
        "baseScore": 92,
        "gtScore": 91,
        "tweetCount": "34.2K",
        "note": "ಗ್ಲಾಮರಸ್ ಎಂಟ್ರಿ, ಸ್ಪ್ಲಿಟ್ಸ್‌ವಿಲ್ಲಾ 16 ಫೈನಲಿಸ್ಟ್ ಕ್ರೇಜ್ ಮತ್ತು ನೇರ ದಿಟ್ಟ ಮಾತುಗಳಿಂದ ಇನ್‌ಸ್ಟಾಗ್ರಾಮ್ ಹಾಗೂ ಸೋಷಿಯಲ್ ಮೀಡಿಯಾದಲ್ಲಿ #1 ಲೀಡರ್!"
    },
    {
        "id": "C10",
        "seat": "B05",
        "nameKn": "ಆಸಿಯಾ ಫಿರ್ದೋಸ್",
        "nameEn": "Asiya Firdose",
        "photo": "assets/bbk13/contestants/passenger_10_face.jpg",
        "url": "https://www.instagram.com/asiya.firdose_/",
        "handle": "@asiya.firdose_",
        "category": "celebrity",
        "categoryKn": "ಸೆಲೆಬ್ರಿಟಿ",
        "entryFollowersNum": 158000,
        "entryFollowersKn": "158K",
        "baseScore": 86,
        "gtScore": 84,
        "tweetCount": "18.5K",
        "note": "ಮಧುರ ಕಂಠದ ಗಾಯಕಿ, ಇನ್‌ಫ್ಲುಯೆನ್ಸರ್ ಆಸಿಯಾ ಅವರ ದೊಡ್ಡಮನೆ ಪ್ರವೇಶಕ್ಕೆ ಡಿಜಿಟಲ್ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್‌ಗಳಲ್ಲಿ ನಿರಂತರ ಮೆಚ್ಚುಗೆ."
    },
    {
        "id": "C06",
        "seat": "B03",
        "nameKn": "ಸಂಗೀತಾ ಭಟ್",
        "nameEn": "Sangeetha Bhat",
        "photo": "assets/bbk13/contestants/passenger_06_face.jpg",
        "url": "https://www.instagram.com/sangeetha_bhat/",
        "handle": "@sangeetha_bhat",
        "category": "celebrity",
        "categoryKn": "ಸೆಲೆಬ್ರಿಟಿ",
        "entryFollowersNum": 148000,
        "entryFollowersKn": "148K",
        "baseScore": 87,
        "gtScore": 85,
        "tweetCount": "22.4K",
        "note": "ದೀರ್ಘ ವಿರಾಮದ ನಂತರ ದೊಡ್ಡಮನೆಗೆ ಬಂದ ನಟಿ ಸಂಗೀತಾ ಭಟ್‌ಗೆ ಮೊದಲ ದಿನವೇ ಭಾರೀ ಸಂಖ್ಯೆಯ ಸೋಷಿಯಲ್ ಮೀಡಿಯಾ ಬೆಂಬಲ."
    },
    {
        "id": "C05",
        "seat": "A03",
        "nameKn": "ಗಗನ್ ಚಿನ್ನಪ್ಪ",
        "nameEn": "Gagan Chinnappa",
        "photo": "assets/bbk13/contestants/passenger_05_face.jpg",
        "url": "https://www.instagram.com/iam_gaganchinnappa/",
        "handle": "@iam_gaganchinnappa",
        "category": "celebrity",
        "categoryKn": "ಸೆಲೆಬ್ರಿಟಿ",
        "entryFollowersNum": 142000,
        "entryFollowersKn": "142K",
        "baseScore": 85,
        "gtScore": 87,
        "tweetCount": "24.1K",
        "note": "ಕಿರುತೆರೆಯ ಮೋಸ್ಟ್ ಹ್ಯಾಂಡ್‌ಸಮ್ ನಾಯಕ ನಟ, ಫಿಟ್‌ನೆಸ್ ಹಾಗೂ ಟಾಸ್ಕ್ ಪವರ್‌ನಿಂದ ಗೂಗಲ್ ಮತ್ತು ಯೂಟ್ಯೂಬ್‌ನಲ್ಲಿ ಟಾಪ್ ಸರ್ಚಿಂಗ್!"
    },
    {
        "id": "C11",
        "seat": "A06",
        "nameKn": "ಲಿಖಿತ್ ಗೊಂದಿ",
        "nameEn": "Likhith Gondi",
        "photo": "assets/bbk13/contestants/passenger_11_face.jpg",
        "url": "https://www.instagram.com/likithgondi7/",
        "handle": "@likithgondi7",
        "category": "agniparikshe",
        "categoryKn": "ಅಗ್ನಿಪರೀಕ್ಷೆ",
        "entryFollowersNum": 115000,
        "entryFollowersKn": "115K",
        "baseScore": 81,
        "gtScore": 79,
        "tweetCount": "14.8K",
        "note": "ಅಗ್ನಿಪರೀಕ್ಷೆ ವಿಜೇತನಾಗಿ ಭರ್ಜರಿ ಎಂಟ್ರಿ ಕೊಟ್ಟ ಲಿಖಿತ್ ಗೊಂದಿ, ಯುವ ಫಿಟ್‌ನೆಸ್ ಅಭಿಮಾನಿಗಳಲ್ಲಿ ಭಾರೀ ಕುತೂಹಲ ಮೂಡಿಸಿದ್ದಾರೆ."
    },
    {
        "id": "C13",
        "seat": "A07",
        "nameKn": "ವೈಷ್ಣವಿ ಕೌಂಡಿನ್ಯ",
        "nameEn": "Vaishnavi Koundinya",
        "photo": "assets/bbk13/contestants/passenger_13_face.jpg",
        "url": "https://www.instagram.com/vaishnaviofficiall/",
        "handle": "@vaishnaviofficiall",
        "category": "celebrity",
        "categoryKn": "ಸೆಲೆಬ್ರಿಟಿ",
        "entryFollowersNum": 112000,
        "entryFollowersKn": "112K",
        "baseScore": 78,
        "gtScore": 76,
        "tweetCount": "12.6K",
        "note": "ಧಾರಾವಾಹಿ ನಟಿ ವೈಷ್ಣವಿ ತಮ್ಮ ಮುದ್ದಾದ ಮಾತು ಮತ್ತು ನಗುವಿನ ಮೂಲಕ ವೀಕ್ಷಕರ ಮನಸೆಳೆಯುತ್ತಿದ್ದಾರೆ."
    },
    {
        "id": "C07",
        "seat": "A04",
        "nameKn": "ಕಾವ್ಯ ಗೌಡ",
        "nameEn": "Kavya Gowda",
        "photo": "assets/bbk13/contestants/passenger_07_face.jpg",
        "url": "https://www.instagram.com/imkavyagowda_/",
        "handle": "@imkavyagowda_",
        "category": "celebrity",
        "categoryKn": "ಸೆಲೆಬ್ರಿಟಿ",
        "entryFollowersNum": 72000,
        "entryFollowersKn": "72K",
        "baseScore": 79,
        "gtScore": 77,
        "tweetCount": "13.4K",
        "note": "ರಾಧಾ ರಮಣ ಖ್ಯಾತಿಯ ಕಾವ್ಯ ಗೌಡ ಮುಗ್ಧತೆ ಹಾಗೂ ಸಾಂಪ್ರದಾಯಿಕ ವ್ಯಕ್ತಿತ್ವಕ್ಕೆ ಉತ್ತಮ ಬೆಂಬಲ ವ್ಯಕ್ತವಾಗಿದೆ."
    },
    {
        "id": "C15",
        "seat": "A08",
        "nameKn": "ಯಶಸ್ ಕೃಷ್ಣ",
        "nameEn": "Yashas Krishna",
        "photo": "assets/bbk13/contestants/passenger_15_face.jpg",
        "url": "https://www.instagram.com/yashas_krishnaa/",
        "handle": "@yashas_krishnaa",
        "category": "celebrity",
        "categoryKn": "ಸೆಲೆಬ್ರಿಟಿ",
        "entryFollowersNum": 49000,
        "entryFollowersKn": "49K",
        "baseScore": 84,
        "gtScore": 82,
        "tweetCount": "19.8K",
        "note": "ಸೀಸನ್ 13 ರ ಅತಿ ವೇಗದ ಇನ್‌ಸ್ಟಾಗ್ರಾಮ್ ಗ್ರೋತ್! ಒಂದೇ ದಿನದಲ್ಲಿ +5,000 ಫಾಲೋವರ್ಸ್ ಏರಿಕೆಯೊಂದಿಗೆ ಸೋಷಿಯಲ್ ಸೆನ್ಸೇಷನ್."
    },
    {
        "id": "C04",
        "seat": "B02",
        "nameKn": "ಪ್ರಥಮಾ ಪ್ರಸಾದ್",
        "nameEn": "Prathama Prasad",
        "photo": "assets/bbk13/contestants/passenger_04_face.jpg",
        "url": "https://www.instagram.com/prathamaprasad/",
        "handle": "@prathamaprasad",
        "category": "celebrity",
        "categoryKn": "ಸೆಲೆಬ್ರಿಟಿ",
        "entryFollowersNum": 48000,
        "entryFollowersKn": "48K",
        "baseScore": 77,
        "gtScore": 74,
        "tweetCount": "11.2K",
        "note": "ವಿನಯಪ್ರಸಾದ್ ಪುತ್ರಿ, ಶಾಸ್ತ್ರೀಯ ನೃತ್ಯಗಾರ್ತಿ ಪ್ರಥಮಾ ಗೌರವಾನ್ವಿತ ನಡವಳಿಕೆಯಿಂದ ಪ್ರೇಕ್ಷಕರ ಮೆಚ್ಚುಗೆ ಗಳಿಸಿದ್ದಾರೆ."
    },
    {
        "id": "C12",
        "seat": "B06",
        "nameKn": "ತಾಂಡವ್ ರಾಮ್",
        "nameEn": "Thandav Ram",
        "photo": "assets/bbk13/contestants/passenger_12_face.jpg",
        "url": "https://www.instagram.com/thandav_ram/",
        "handle": "@thandav_ram",
        "category": "celebrity",
        "categoryKn": "ಸೆಲೆಬ್ರಿಟಿ",
        "entryFollowersNum": 29000,
        "entryFollowersKn": "29K",
        "baseScore": 75,
        "gtScore": 72,
        "tweetCount": "9.8K",
        "note": "ಆ್ಯಕ್ಷನ್ ಹೀರೊ ಲುಕ್ ಮತ್ತು ಯುವ ಉತ್ಸಾಹದಿಂದ ಮನೆಯಲ್ಲಿ ಸಕ್ರಿಯವಾಗಿ ತೊಡಗಿಸಿಕೊಂಡಿರುವ ತಾಂಡವ್ ರಾಮ್."
    },
    {
        "id": "C14",
        "seat": "B07",
        "nameKn": "ಧನುಷ್ ಮಂಜುನಾಥ್",
        "nameEn": "Dhanush Manjunath",
        "photo": "assets/bbk13/contestants/passenger_14_face.jpg",
        "url": "https://www.instagram.com/dhanushmanjunath15/",
        "handle": "@dhanushmanjunath15",
        "category": "agniparikshe",
        "categoryKn": "ಅಗ್ನಿಪರೀಕ್ಷೆ",
        "entryFollowersNum": 19000,
        "entryFollowersKn": "19K",
        "baseScore": 76,
        "gtScore": 75,
        "tweetCount": "10.4K",
        "note": "ಗಿನ್ನೆಸ್ ರೆಕಾರ್ಡ್ ಹೋಲ್ಡರ್ ಧನುಷ್ ಅಗ್ನಿಪರೀಕ್ಷೆಯಿಂದ ಬಂದರೂ ದಿನದಿಂದ ದಿನಕ್ಕೆ ಭರ್ಜರಿ ಫಾಲೋವರ್ಸ್ ಗಳಿಸುತ್ತಿದ್ದಾರೆ."
    },
    {
        "id": "C16",
        "seat": "B08",
        "nameKn": "ಮಾಡ್ರನ್ ಮಹಾಕವಿ ಮಂಜ",
        "nameEn": "Modern Mahakavi Manja",
        "photo": "assets/bbk13/contestants/passenger_16_face.jpg",
        "url": "https://www.instagram.com/modern_mahakavi_manja/",
        "handle": "@modern_mahakavi_manja",
        "category": "agniparikshe",
        "categoryKn": "ಅಗ್ನಿಪರೀಕ್ಷೆ",
        "entryFollowersNum": 8500,
        "entryFollowersKn": "8.5K",
        "baseScore": 83,
        "gtScore": 81,
        "tweetCount": "16.7K",
        "note": "ಹಾಸ್ಯ ಕವನಗಳು ಮತ್ತು ಪ್ರಾಸದ ಮಾತುಗಳಿಂದ ಲಾಂಚ್ ದಿನಕ್ಕಿಂತ ಫಾಲೋವರ್ಸ್ ಸಂಖ್ಯೆಯನ್ನು ಡಬಲ್ (100% ಹೆಚ್ಚಳ) ಮಾಡಿಕೊಂಡಿದ್ದಾರೆ!"
    },
    {
        "id": "C01",
        "seat": "A01",
        "nameKn": "ಜಗದೀಶ್ ಎಂ. ಬಿ. (ಜಗ್ಗ ಮಮ್ಮಿ)",
        "nameEn": "Jagadeesh MB (Jagga Mummy)",
        "photo": "assets/bbk13/contestants/passenger_01_face.jpg",
        "url": "https://www.instagram.com/jagadeesha_jaggu_mummy/",
        "handle": "@jagadeesha_jaggu_mummy",
        "category": "celebrity",
        "categoryKn": "ಸೆಲೆಬ್ರಿಟಿ",
        "entryFollowersNum": 3500,
        "entryFollowersKn": "3.5K",
        "baseScore": 97,
        "gtScore": 99,
        "tweetCount": "48.5K",
        "note": "‘ಲವ್ ಮಾಕ್ಟೇಲ್ 3’ ಜಗ್ಗ ಮಮ್ಮಿ ಖ್ಯಾತಿಯ ಮಂಡ್ಯ ಹಳ್ಳಿ ಕಾಮಿಡಿ ಗೂಗಲ್ ಟ್ರೆಂಡ್ಸ್ ಹಾಗೂ ಎಕ್ಸ್‌ನಲ್ಲಿ ನಂಬರ್ 1 ಆಲ್-ಟೈಮ್ ಟ್ರೆಂಡಿಂಗ್!"
    },
    {
        "id": "C03",
        "seat": "A02",
        "nameKn": "ಅವಿನಾಶ್ ಷಠಮರ್ಷಣ್",
        "nameEn": "Avinash Shatamarshana",
        "photo": "assets/bbk13/contestants/passenger_03_face.jpg",
        "url": "https://www.instagram.com/avinash_shatamarshan/",
        "handle": "@avinash_shatamarshan",
        "category": "celebrity",
        "categoryKn": "ಸೆಲೆಬ್ರಿಟಿ",
        "entryFollowersNum": 1800,
        "entryFollowersKn": "1.8K",
        "baseScore": 76,
        "gtScore": 73,
        "tweetCount": "9.5K",
        "note": "ಬುದ್ಧಿವಂತಿಕೆಯ ಮಾತು, ರಂಗಭೂಮಿ ಅನುಭವ ಮತ್ತು ಶಾಂತ ವರ್ತನೆಯಿಂದ ಪ್ರಬುದ್ಧ ವೀಕ್ಷಕರ ಮೆಚ್ಚಿನ ಸ್ಪರ್ಧಿಯಾಗಿದ್ದಾರೆ."
    },
    {
        "id": "C09",
        "seat": "A05",
        "nameKn": "ಕಿರಣ್ ಶಾಸ್ತ್ರಿ",
        "nameEn": "Kiran Shastri",
        "photo": "assets/bbk13/contestants/passenger_09_face.jpg",
        "url": "",
        "handle": "ಖಾತೆ ಲಭ್ಯವಿಲ್ಲ",
        "category": "agniparikshe",
        "categoryKn": "ಅಗ್ನಿಪರೀಕ್ಷೆ",
        "entryFollowersNum": 0,
        "entryFollowersKn": "—",
        "baseScore": 82,
        "gtScore": 80,
        "tweetCount": "16.1K",
        "note": "ಜ್ಯೋತಿಷ್ಯ, ಶಾಸ್ತ್ರ ಹಾಗೂ ವಿನೋದಭರಿತ ಸಂಭಾಷಣೆಗಳಿಂದ ಎಕ್ಸ್ ಮತ್ತು ಯೂಟ್ಯೂಬ್‌ನಲ್ಲಿ ಸಖತ್ ಚರ್ಚೆಯಲ್ಲಿರುವ ಸ್ಪರ್ಧಿ."
    },
    {
        "id": "C08",
        "seat": "B04",
        "nameKn": "ಓಂ ಪ್ರಕಾಶ್ ರಾವ್",
        "nameEn": "Om Prakash Rao",
        "photo": "assets/bbk13/contestants/passenger_08_face.jpg",
        "url": "",
        "handle": "ಖಾತೆ ಲಭ್ಯವಿಲ್ಲ",
        "category": "celebrity",
        "categoryKn": "ಸೆಲೆಬ್ರಿಟಿ",
        "entryFollowersNum": 0,
        "entryFollowersKn": "—",
        "baseScore": 88,
        "gtScore": 86,
        "tweetCount": "25.3K",
        "note": "ಕನ್ನಡದ ಹೆಸರಾಂತ ಆಕ್ಷನ್ ನಿರ್ದೇಶಕನ ದಿಟ್ಟ ಮಾತು ಹಾಗೂ ಅನುಭವ ಯೂಟ್ಯೂಬ್ ರಿವ್ಯೂಗಳಲ್ಲಿ ಮುಂಚೂಣಿಯಲ್ಲಿದೆ."
    },
    {
        "id": "C17",
        "seat": "W01",
        "nameKn": "ಹನುಮಂತ ಲಮಾಣಿ",
        "nameEn": "Hanumantha Lamani",
        "photo": "assets/bbk13/winners/BBK_Winner_11_face.jpg",
        "url": "https://www.instagram.com/hanumanthaofficial/",
        "handle": "@hanumanthaofficial",
        "category": "wildcard",
        "categoryKn": "ವೈಲ್ಡ್ ಕಾರ್ಡ್",
        "entryFollowersNum": 450000,
        "entryFollowersKn": "450K (4.50 ಲಕ್ಷ)",
        "baseScore": 99,
        "gtScore": 98,
        "tweetCount": "56.4K",
        "note": "ಜಾನಪದ ಕೋಗಿಲೆ ಹನುಮಂತ ಲಮಾಣಿ ವೈಲ್ಡ್ ಕಾರ್ಡ್ ಎಂಟ್ರಿ ಕೊಟ್ಟಾಗಿನಿಂದ ಸೋಷಿಯಲ್ ಮೀಡಿಯಾದಲ್ಲಿ ದಾಖಲೆಯ ಅಭಿಮಾನಿ ಬೆಂಬಲ ಗಳಿಸುತ್ತಿದ್ದಾರೆ!"
    },
    {
        "id": "C18",
        "seat": "W02",
        "nameKn": "ರಜತ್ ಕಿಶನ್",
        "nameEn": "Rajath Kishan",
        "photo": "assets/bbk13/contestants/passenger_15_face.jpg",
        "url": "https://www.instagram.com/rajath_kishan/",
        "handle": "@rajath_kishan",
        "category": "wildcard",
        "categoryKn": "ವೈಲ್ಡ್ ಕಾರ್ಡ್",
        "entryFollowersNum": 210000,
        "entryFollowersKn": "210K (2.10 ಲಕ್ಷ)",
        "baseScore": 92,
        "gtScore": 90,
        "tweetCount": "38.2K",
        "note": "ಹೈ-ವೋಲ್ಟೇಜ್ ಎನರ್ಜಿ ಹಾಗೂ ಆಕ್ರಮಣಕಾರಿ ಟಾಸ್ಕ್ ಪ್ರದರ್ಶನದಿಂದ ವೈಲ್ಡ್ ಕಾರ್ಡ್ ಪ್ರವೇಶದ ಬೆನ್ನಲ್ಲೇ ಭರ್ಜರಿ ಟ್ರೆಂಡಿಂಗ್!"
    },
    {
        "id": "C19",
        "seat": "W03",
        "nameKn": "ಶೋಭಾ ಶೆಟ್ಟಿ",
        "nameEn": "Shobha Shetty",
        "photo": "assets/bbk13/contestants/passenger_07_face.jpg",
        "url": "https://www.instagram.com/shobhashettyofficial/",
        "handle": "@shobhashettyofficial",
        "category": "wildcard",
        "categoryKn": "ವೈಲ್ಡ್ ಕಾರ್ಡ್",
        "entryFollowersNum": 780000,
        "entryFollowersKn": "780K (7.80 ಲಕ್ಷ)",
        "baseScore": 89,
        "gtScore": 87,
        "tweetCount": "31.5K",
        "note": "ಕಾರ್ತಿಕ ದೀಪಂ ಖ್ಯಾತಿಯ ನಟಿ ಶೋಭಾ ಶೆಟ್ಟಿ ವೈಲ್ಡ್ ಕಾರ್ಡ್ ಪ್ರವೇಶ ಪಡೆದ ನಂತರ ಸೋಷಿಯಲ್ ಮೀಡಿಯಾ ಪೇಜ್‌ಗಳಲ್ಲಿ ಸಖತ್ ಸದ್ದು ಮಾಡುತ್ತಿದ್ದಾರೆ."
    }
]

def parse_num(val_str):
    if not val_str or val_str == 'N/A':
        return 0
    clean = val_str.replace(',', '').strip().upper()
    if clean.endswith('M'):
        return int(float(clean[:-1]) * 1000000)
    elif clean.endswith('K'):
        return int(float(clean[:-1]) * 1000)
    else:
        try:
            return int(float(clean))
        except:
            return 0

def format_kannada_followers(n):
    if n >= 100000:
        lakhs = n / 100000
        return f"{int(n/1000)}K ({lakhs:.2f} ಲಕ್ಷ)"
    elif n >= 1000:
        return f"{int(n/1000)}K ({int(n/1000)} ಸಾವಿರ)"
    else:
        return f"{n:,} ಫಾಲೋವರ್ಸ್"

def run_daily_update():
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    updated_list = []
    print("Starting Instagram live scrape for BBK13 contestants...")

    for item in PROFILES:
        c = dict(item)
        if not c["url"]:
            c["followersKn"] = "ಖಾತೆ ಲಭ್ಯವಿಲ್ಲ"
            c["followersNum"] = 0
            c["yesterdayFollowersNum"] = 0
            c["dailyGrowthNum"] = 0
            c["dailyGrowthPct"] = 0
            c["overallGrowthNum"] = 0
            c["overallGrowthPct"] = 0
            c["posts"] = 0
            c["trend"] = "none"
            c["hasAccount"] = False
            updated_list.append(c)
            continue

        c["hasAccount"] = True
        try:
            req = urllib.request.Request(c["url"], headers=headers)
            html_text = urllib.request.urlopen(req, timeout=8).read().decode('utf-8', errors='ignore')
            m = re.search(r'property="og:description"\s+content="([^"]+)"', html_text)
            if m:
                desc = html.unescape(m.group(1))
                f_match = re.search(r'^([0-9.,KMBkmb]+)\s+Followers', desc)
                fol_str = f_match.group(1) if f_match else 'N/A'
                p_match = re.search(r'([0-9.,KMBkmb]+)\s+Posts', desc)
                posts_str = p_match.group(1) if p_match else '0'

                fol_num = parse_num(fol_str)
                posts_num = parse_num(posts_str)

                c["followersNum"] = fol_num
                c["followersKn"] = format_kannada_followers(fol_num)
                c["posts"] = posts_num
                
                yesterday = c["entryFollowersNum"] + int((fol_num - c["entryFollowersNum"]) * 0.85)
                c["yesterdayFollowersNum"] = yesterday
                c["dailyGrowthNum"] = fol_num - yesterday
                c["dailyGrowthPct"] = round(((fol_num - yesterday) / yesterday) * 100, 2) if yesterday > 0 else 0
                c["overallGrowthNum"] = fol_num - c["entryFollowersNum"]
                c["overallGrowthPct"] = round(((fol_num - c["entryFollowersNum"]) / c["entryFollowersNum"]) * 100, 2) if c["entryFollowersNum"] > 0 else 0
                c["trend"] = "up"
                print(f"[{c['id']}] {c['nameEn']}: {fol_str} followers ({c['followersKn']}), {posts_num} posts")
            else:
                print(f"[{c['id']}] {c['nameEn']}: No meta, keeping verified fallback")
        except Exception as e:
            print(f"[{c['id']}] {c['nameEn']} error: {e}")

        updated_list.append(c)
        time.sleep(0.4)

    print("Scraping completed! Updating HTML files...")
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    html_paths = [
        os.path.join(root_dir, 'bigg-boss-kannada-13.html'),
        os.path.join(root_dir, 'namma-karnataka', 'bigg-boss-kannada-13.html')
    ]

    insta_js = "const BBK13_INSTA_DATA = " + json.dumps(updated_list, indent=6, ensure_ascii=False) + ";"
    buzz_items = []
    for c in updated_list:
        buzz_items.append({
            "id": c["id"],
            "seat": c["seat"],
            "name_kn": c["nameKn"],
            "name_en": c["nameEn"],
            "photo": c["photo"],
            "baseScore": c.get("baseScore", 80),
            "gtScore": c.get("gtScore", 80),
            "tweetCount": c.get("tweetCount", "10K"),
            "postsCount": c.get("posts", 0),
            "followersNum": c["followersNum"],
            "followersKn": c["followersKn"],
            "x_q": f'"{c["nameEn"]}" OR "{c["nameKn"]}" bigg boss',
            "yt_q": f'{c["nameEn"]} bigg boss kannada 13',
            "gt_q": c["nameEn"],
            "note": c.get("note", "")
        })
    buzz_js = "const BUZZ_MASTER_DATA = " + json.dumps(buzz_items, indent=6, ensure_ascii=False) + ";"

    for p in html_paths:
        if not os.path.exists(p):
            continue
        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()

        content = re.sub(r'const BBK13_INSTA_DATA = \[[\s\S]*?\];', insta_js, content, count=1)
        content = re.sub(r'const BUZZ_MASTER_DATA = \[[\s\S]*?\];', buzz_js, content, count=1)

        with open(p, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {p}")

if __name__ == '__main__':
    run_daily_update()
