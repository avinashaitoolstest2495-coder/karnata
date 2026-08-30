# -*- coding: utf-8 -*-
"""
Karnata — scripts/optimize_active_pages_seo.py
Optimizes SEO, AI GEO, Multilingual Kannada Metadata, OpenGraph, and Schema.org
for ONLY the ACTIVE primary pages of Karnata.in.
Also generates a pristine sitemap.xml with only active pages.
"""

import os
import re
import json
from bs4 import BeautifulSoup

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Strict list of ACTIVE pages
ACTIVE_PAGES_META = {
    'index.html': {
        'url': 'https://karnata.in/',
        'priority': '1.0',
        'title': 'ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ | Karnataka Live News, Weather, Gold, Dam & Governance Portal — Karnata.in',
        'desc': 'ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ: ಇಂದಿನ ಹವಾಮಾನ, 27 ಮಳೆ ನಕ್ಷತ್ರಗಳು, ಚಿನ್ನ-ಬೆಳ್ಳಿ ದರ, ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ, APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ, ಸಚಿವರು ಮತ್ತು ಸರ್ಕಾರಿ ವರ್ಗಾವಣೆ ಆದೇಶಗಳು.',
        'keywords': 'ಕರ್ನಾಟಕ ಲೈವ್, ಕರ್ನಾಟಕ ಮಾಹಿತಿ, ಕರ್ನಾಟಕ ಹವಾಮಾನ, ಇಂದಿನ ಚಿನ್ನದ ದರ, ಕರ್ನಾಟಕ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ, APMC ದರಗಳು, ಕರ್ನಾಟಕ ಸಚಿವರು, Karnataka news, Karnataka weather, Gold rate Karnataka, Dam levels Karnataka, Karnata.in',
        'schema_type': 'WebSite',
        'geo_place': 'Bengaluru, Karnataka, India'
    },
    'weather.html': {
        'url': 'https://karnata.in/weather',
        'priority': '0.95',
        'title': 'ಕರ್ನಾಟಕ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ & 27 ಮಳೆ ನಕ್ಷತ್ರಗಳು | Karnataka Live Weather, KSNDMC Telemetry, IMD Nowcast — Karnata.in',
        'desc': 'ಕರ್ನಾಟಕ 31 ಜಿಲ್ಲೆಗಳ ಲೈವ್ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ, KSNDMC ರಿಯಲ್-ಟೈಮ್ ಮಳೆ ಟೆಲಿಮೆಟ್ರಿ, IMD ನೌಕಾಸ್ಟ್ ಎಚ್ಚರಿಕೆಗಳು, 27 ಮಳೆ ನಕ್ಷತ್ರಗಳು ಮತ್ತು ಕೃಷಿ ಮಳೆ ವಿಜ್ಞಾನ ಮಾರ್ಗದರ್ಶಿ.',
        'keywords': 'ಕರ್ನಾಟಕ ಹವಾಮಾನ, ಮಳೆ ನಕ್ಷತ್ರಗಳು, KSNDMC ಮಳೆ ವಿವರ, IMD ಬೆಂಗಳೂರು ನೌಕಾಸ್ಟ್, ಜಿಲ್ಲಾವಾರು ಹವಾಮಾನ, Karnataka weather forecast, Rain nakshatras, KSNDMC telemetry, IMD nowcast Bengaluru',
        'schema_type': 'WeatherForecast',
        'geo_place': 'Karnataka, India'
    },
    'gold-rate.html': {
        'url': 'https://karnata.in/gold-rate',
        'priority': '0.90',
        'title': 'ಕರ್ನಾಟಕ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಲೈವ್ ದರ ಇಂದು | Today Gold Rate in Karnataka (22K, 24K, 18K), Silver Price — Karnata.in',
        'desc': 'ಕರ್ನಾಟಕದ ಇಂದಿನ ಚಿನ್ನ ಮತ್ತು ಬೆಳ್ಳಿ ಲೈವ್ ದರ: 22 ಕ್ಯಾರೆಟ್ ಆಭರಣ ಚಿನ್ನ, 24 ಕ್ಯಾರೆಟ್ ಶುದ್ಧ ಚಿನ್ನ, 18 ಕ್ಯಾರೆಟ್ ಮತ್ತು ಬೆಳ್ಳಿ ಬೆಲೆ, ಜಿಎಸ್‌ಟಿ ಲೆಕ್ಕಾಚಾರ ಹಾಗೂ AI ಸಲಹೆಗಾರ.',
        'keywords': 'ಕರ್ನಾಟಕ ಚಿನ್ನದ ದರ, ಇಂದಿನ ಚಿನ್ನದ ಬೆಲೆ, 22 ಕ್ಯಾರೆಟ್ ಚಿನ್ನ, 24 ಕ್ಯಾರೆಟ್ ಚಿನ್ನ, ಬೆಳ್ಳಿ ದರ ಇಂದು, Gold rate Karnataka today, 22k gold price Bengaluru, Silver rate Karnataka, Karnata gold rate',
        'schema_type': 'FinancialProduct',
        'geo_place': 'Bengaluru, Karnataka, India'
    },
    'dam-levels.html': {
        'url': 'https://karnata.in/dam-levels',
        'priority': '0.90',
        'title': 'ಕರ್ನಾಟಕ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ ಇಂದು | Karnataka Dam Water Levels Live (KRS, Almatti, Kabini, Bhadra) — Karnata.in',
        'desc': 'ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ಲೈವ್ ನೀರಿನ ಮಟ್ಟ: ಕೆಆರ್‌ಎಸ್, ಆಲಮಟ್ಟಿ, ಕಬಿನಿ, ಲಿಂಗನಮಕ್ಕಿ, ಭದ್ರಾ, ತುಂಗಭದ್ರಾ ಅಣೆಕಟ್ಟುಗಳ ಒಳಹರಿವು, ಹೊರಹರಿವು ಮತ್ತು ಸಂಗ್ರಹ ಸಾಮರ್ಥ್ಯ.',
        'keywords': 'ಕರ್ನಾಟಕ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ, ಕೆಆರ್‌ಎಸ್ ಡ್ಯಾಂ ಲೈವ್, ಆಲಮಟ್ಟಿ ಡ್ಯಾಂ ನೀರಿನ ಮಟ್ಟ, ಕಬಿನಿ ಡ್ಯಾಂ, Karnataka dam levels today, KRS water level, Almatti dam storage, Karnataka reservoir live water status',
        'schema_type': 'GovernmentService',
        'geo_place': 'Karnataka, India'
    },
    'apmc-prices.html': {
        'url': 'https://karnata.in/apmc-prices',
        'priority': '0.85',
        'title': 'ಕರ್ನಾಟಕ APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ ಇಂದು | Karnataka APMC Mandi Commodity Rates Today — Karnata.in',
        'desc': 'ಕರ್ನಾಟಕದ ಎಲ್ಲಾ APMC ಮಾರುಕಟ್ಟೆಗಳ ದೈನಂದಿನ ಕೃಷಿ ಉತ್ಪನ್ನಗಳ ಲೈವ್ ದರ: ಅಡಿಕೆ, ಈರುಳ್ಳಿ, ಟೊಮೆಟೊ, ಮೆಕ್ಕೆಜೋಳ, ತೊಗರಿ, ಹತ್ತಿ ಮತ್ತು ರಾಗಿ ಇಂದಿನ ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು.',
        'keywords': 'ಕರ್ನಾಟಕ APMC ದರಗಳು, ಇಂದಿನ ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ, ಅಡಿಕೆ ಧಾರಣೆ ಇಂದು, ಈರುಳ್ಳಿ ರೇಟ್, APMC mandi rates Karnataka, Today market price Karnataka, Arecanut price today',
        'schema_type': 'GovernmentService',
        'geo_place': 'Karnataka, India'
    },
    'cabinet-ministers.html': {
        'url': 'https://karnata.in/cabinet-ministers',
        'priority': '0.85',
        'title': 'ಕರ್ನಾಟಕ ಸಚಿವ ಸಂಪುಟ 2026 | Karnataka Cabinet Ministers List & Portfolios — Karnata.in',
        'desc': 'ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಮುಖ್ಯಮಂತ್ರಿ, ಉಪ ಮುಖ್ಯಮಂತ್ರಿ ಮತ್ತು ಸಂಪುಟ ಸಚಿವರ ಸಂಪೂರ್ಣ ಪಟ್ಟಿ, ಖಾತೆಗಳ ವಿವರ ಮತ್ತು ಸಂಪರ್ಕ ಮಾಹಿತಿ.',
        'keywords': 'ಕರ್ನಾಟಕ ಸಚಿವರು, ಕರ್ನಾಟಕ ಸಚಿವ ಸಂಪುಟ, ಮುಖ್ಯಮಂತ್ರಿ, ಕರ್ನಾಟಕ ಮಂತ್ರಿಗಳ ಪಟ್ಟಿ, Karnataka cabinet ministers list, Karnataka government ministers, CM Siddaramaiah, DCM DK Shivakumar',
        'schema_type': 'GovernmentOrganization',
        'geo_place': 'Vidhana Soudha, Bengaluru, Karnataka, India'
    },
    'officers.html': {
        'url': 'https://karnata.in/officers',
        'priority': '0.85',
        'title': 'ಕರ್ನಾಟಕ IAS, IPS ಅಧಿಕಾರಿಗಳ ವರ್ಗಾವಣೆ & ಡೈರೆಕ್ಟರಿ | Karnataka Senior Officers Directory & Transfers — Karnata.in',
        'desc': 'ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಹಿರಿಯ ಐಎಎಸ್ (IAS), ಐಪಿಎಸ್ (IPS), ಐಎಫ್‌ಎಸ್ (IFS) ಅಧಿಕಾರಿಗಳ ಸಂಪೂರ್ಣ ಡೈರೆಕ್ಟರಿ ಮತ್ತು ಇತ್ತೀಚಿನ ವರ್ಗಾವಣೆ ಆದೇಶಗಳ ಅಧಿಕೃತ ಮಾಹಿತಿ.',
        'keywords': 'ಕರ್ನಾಟಕ ಅಧಿಕಾರಿಗಳ ವರ್ಗಾವಣೆ, IAS ಅಧಿಕಾರಿಗಳ ಪಟ್ಟಿ, IPS ಅಧಿಕಾರಿಗಳು ಕರ್ನಾಟಕ, Karnataka IAS officers directory, Karnataka IPS transfers, Karnataka government orders, Officers directory',
        'schema_type': 'GovernmentService',
        'geo_place': 'Bengaluru, Karnataka, India'
    },
    'karnataka-stories.html': {
        'url': 'https://karnata.in/karnataka-stories',
        'priority': '0.85',
        'title': 'ಕರ್ನಾಟಕ ವಿಶೇಷ ಲೇಖನಗಳು & ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು | Karnataka News, Schemes & In-Depth Guides — Karnata.in',
        'desc': 'ಕರ್ನಾಟಕದ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು, ಕೃಷಿ, ಇತಿಹಾಸ, ಸಂಸ್ಕೃತಿ, ತಂತ್ರಜ್ಞಾನ ಮತ್ತು ಆಡಳಿತ ಸುಧಾರಣೆಗಳ ಕುರಿತಾದ ಸಮಗ್ರ ವಿಶೇಷ ಲೇಖನಗಳು ಮತ್ತು ಮಾರ್ಗದರ್ಶಿಗಳು.',
        'keywords': 'ಕರ್ನಾಟಕ ಲೇಖನಗಳು, ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು, ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆ, ಭೂಮಿ ಆರ್‌ಟಿಸಿ, ಕರ್ನಾಟಕ ಇತಿಹಾಸ, Karnataka government schemes, Gruha Lakshmi, Bhoomi RTC, Karnataka news analysis',
        'schema_type': 'CollectionPage',
        'geo_place': 'Karnataka, India'
    },
    'article/gruha-lakshmi-status-check-2026.html': {
        'url': 'https://karnata.in/article/gruha-lakshmi-status-check-2026',
        'priority': '0.90',
        'title': 'ಗೃಹಲಕ್ಷ್ಮಿ ₹2000 ಹಣ ಜಮೆ ಸ್ಟೇಟಸ್ ಚೆಕ್ 2026 | Gruha Lakshmi DBT Status Check Online Guide — Karnata.in',
        'desc': 'ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆಯ ₹2000 ಮಾಸಿಕ ಹಣ ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾಗಿದೆಯೇ ಎಂದು ಮೊಬೈಲ್‌ನಲ್ಲೇ ಡಿಬಿಟಿ (DBT) ಸ್ಟೇಟಸ್ ಚೆಕ್ ಮಾಡುವ ಸುಲಭ ಅಧಿಕೃತ ವಿಧಾನ.',
        'keywords': 'ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆ ಸ್ಟೇಟಸ್, ಗೃಹಲಕ್ಷ್ಮಿ ಹಣ ಚೆಕ್, ಗೃಹಲಕ್ಷ್ಮಿ ₹2000 DBT, Gruha Lakshmi status check online, Gruha Lakshmi DBT payment status, Karnataka guarantee schemes',
        'schema_type': 'Article',
        'geo_place': 'Karnataka, India'
    },
    'article/karnataka-bhoomi-rtc-pahani-online.html': {
        'url': 'https://karnata.in/article/karnataka-bhoomi-rtc-pahani-online',
        'priority': '0.90',
        'title': 'ಕರ್ನಾಟಕ ಭೂಮಿ RTC ಪಹಣಿ ಆನ್‌ಲೈನ್ ಡೌನ್‌ಲೋಡ್ | Karnataka Bhoomi RTC Pahani Online Viewing Guide — Karnata.in',
        'desc': 'ಕರ್ನಾಟಕ ಭೂಮಿ ಪೋರ್ಟಲ್ ಮೂಲಕ ಮೊಬೈಲ್‌ನಲ್ಲೇ ನಿಮ್ಮ ಜಮೀನಿನ ಆರ್‌ಟಿಸಿ (RTC / ಪಹಣಿ) ಮತ್ತು ಮ್ಯುಟೇಶನ್ ಸ್ಟೇಟಸ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡುವ ಹಂತ-ಹಂತದ ಸಮಗ್ರ ಮಾಹಿತಿ.',
        'keywords': 'ಭೂಮಿ ಆರ್‌ಟಿಸಿ ಪಹಣಿ, RTC ಡೌನ್‌ಲೋಡ್ ಆನ್‌ಲೈನ್, ಕರ್ನಾಟಕ ಪಹಣಿ ಚೆಕ್, Bhoomi RTC online Karnataka, Pahani download online, Bhoomi mutation status Karnataka',
        'schema_type': 'Article',
        'geo_place': 'Karnataka, India'
    },
    'article/karnataka-dam-water-storage-analysis.html': {
        'url': 'https://karnata.in/article/karnataka-dam-water-storage-analysis',
        'priority': '0.85',
        'title': 'ಕರ್ನಾಟಕ ಜಲಾಶಯಗಳ ನೀರಿನ ಸಂಗ್ರಹ ಸಮಗ್ರ ವಿಶ್ಲೇಷಣೆ | Karnataka Dam Storage Analysis & Monsoon Inflow — Karnata.in',
        'desc': 'ಕರ್ನಾಟಕದ 12 ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ, ಕಾವೇರಿ ಮತ್ತು ಕೃಷ್ಣಾ ಕೊಳ್ಳದ ಒಳಹರಿವು ಹಾಗೂ ಕೃಷಿ-ಕುಡಿಯುವ ನೀರಿನ ಲಭ್ಯತೆಯ ವಿಶ್ಲೇಷಣಾ ವರದಿ.',
        'keywords': 'ಜಲಾಶಯಗಳ ನೀರಿನ ಸಂಗ್ರಹ, ಕಾವೇರಿ ಕೊಳ್ಳದ ಡ್ಯಾಂಗಳು, ಕೃಷ್ಣಾ ಕೊಳ್ಳ, Karnataka dam storage analysis, Cauvery basin dams, Krishna basin reservoir levels',
        'schema_type': 'Article',
        'geo_place': 'Karnataka, India'
    },
    'article/karnataka-gba-5-corporations-guide.html': {
        'url': 'https://karnata.in/article/karnataka-gba-5-corporations-guide',
        'priority': '0.85',
        'title': 'ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಪ್ರಾಧಿಕಾರ (GBA) 5 ಮಹಾನಗರ ಪಾಲಿಕೆಗಳ ರಚನೆ | Greater Bengaluru Authority 5 Corporations Guide — Karnata.in',
        'desc': 'ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಆಡಳಿತ ಮಸೂದೆ: ಬಿಬಿಎಂಪಿಯ 5 ಹೊಸ ಮಹಾನಗರ ಪಾಲಿಕೆಗಳ ವಿಭಜನೆ, ವಲಯಗಳು, ತೆರಿಗೆ ಮತ್ತು ನಾಗರಿಕ ಸೇವೆಗಳ ಸಮಗ್ರ ಮಾರ್ಗದರ್ಶಿ.',
        'keywords': 'ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಪ್ರಾಧಿಕಾರ, GBA 5 ಪಾಲಿಕೆಗಳು, ಬಿಬಿಎಂಪಿ ವಿಭಜನೆ, Greater Bengaluru Authority, GBA 5 corporations, BBMP restructuring, Bengaluru civic administration',
        'schema_type': 'Article',
        'geo_place': 'Bengaluru, Karnataka, India'
    },
    'article/panchatantra-village-budget-grants.html': {
        'url': 'https://karnata.in/article/panchatantra-village-budget-grants',
        'priority': '0.85',
        'title': 'ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ಬಜೆಟ್ & ಪಂಚತಂತ್ರ ಅನುದಾನ ಚೆಕ್ | Panchatantra Gram Panchayat Budget & Grants Guide — Karnata.in',
        'desc': 'ನಿಮ್ಮ ಗ್ರಾಮ ಪಂಚಾಯಿತಿಗೆ ಸರ್ಕಾರದಿಂದ ಬಿಡುಗಡೆಯಾದ ಅನುದಾನ ಮತ್ತು ಅಭಿವೃದ್ಧಿ ಕಾಮಗಾರಿಗಳ ಲೆಕ್ಕ ಪರಿಶೀಲಿಸಲು ಪಂಚತಂತ್ರ ಪೋರ್ಟಲ್ ಬಳಸುವ ವಿಧಾನ.',
        'keywords': 'ಪಂಚತಂತ್ರ ಅನುದಾನ, ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ಬಜೆಟ್, ಪಂಚಾಯತ್ ಅಭಿವೃದ್ಧಿ ಕಾಮಗಾರಿ, Panchatantra gram panchayat budget, Karnataka village grants, RDPR Karnataka',
        'schema_type': 'Article',
        'geo_place': 'Karnataka, India'
    },
    'mla-mp.html': {
        'url': 'https://karnata.in/mla-mp',
        'priority': '0.80',
        'title': 'ಕರ್ನಾಟಕ 224 ಶಾಸಕರು & 28 ಸಂಸದರ ಸಂಪೂರ್ಣ ವಿವರ | Karnataka MLAs & MPs Directory — Karnata.in',
        'desc': 'ಕರ್ನಾಟಕದ ಎಲ್ಲಾ 224 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಶಾಸಕರು ಮತ್ತು 28 ಲೋಕಸಭಾ ಕ್ಷೇತ್ರಗಳ ಸಂಸದರ ಪಕ್ಷ, ಕ್ಷೇತ್ರ, ಫೋನ್ ನಂಬರ್ ಮತ್ತು ಸಂಪರ್ಕ ವಿವರ.',
        'keywords': 'ಕರ್ನಾಟಕ ಶಾಸಕರು, ಕರ್ನಾಟಕ ಸಂಸದರು, 224 ಶಾಸಕರ ಪಟ್ಟಿ, Karnataka MLAs list, Karnataka MPs list, Karnataka legislative assembly directory',
        'schema_type': 'GovernmentOrganization',
        'geo_place': 'Karnataka, India'
    },
    'gba.html': {
        'url': 'https://karnata.in/gba',
        'priority': '0.80',
        'title': 'ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಪ್ರಾಧಿಕಾರ (GBA) ಅಧಿಕೃತ ಮಾಹಿತಿ | Greater Bengaluru Authority Portal — Karnata.in',
        'desc': 'ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಆಡಳಿತ ಪ್ರಾಧಿಕಾರದ 5 ಮಹಾನಗರ ಪಾಲಿಕೆಗಳ ನಕ್ಷೆ, ವಲಯಗಳು, ವಾರ್ಡ್‌ಗಳು ಮತ್ತು ನಾಗರಿಕ ಸೌಲಭ್ಯಗಳ ಮಾಹಿತಿ ಕೇಂದ್ರ.',
        'keywords': 'ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು, GBA ಪೋರ್ಟಲ್, ಬೆಂಗಳೂರು ಆಡಳಿತ, Greater Bengaluru Authority, GBA Bengaluru, Bangalore civic portal',
        'schema_type': 'GovernmentOrganization',
        'geo_place': 'Bengaluru, Karnataka, India'
    },
    'petrol-price.html': {
        'url': 'https://karnata.in/petrol-price',
        'priority': '0.80',
        'title': 'ಕರ್ನಾಟಕ ಪೆಟ್ರೋಲ್ & ಡೀಸೆಲ್ ದರ ಇಂದು | Today Petrol & Diesel Price in Karnataka — Karnata.in',
        'desc': 'ಕರ್ನಾಟಕ 31 ಜಿಲ್ಲೆಗಳ ಇಂದಿನ ಪೆಟ್ರೋಲ್, ಡೀಸೆಲ್ ಮತ್ತು ಸಿಎನ್‌ಜಿ (CNG) ಲೈವ್ ದರಗಳು ಹಾಗೂ ಇಂಧನ ಬೆಲೆ ಏರಿಳಿತದ ಇತಿಹಾಸ.',
        'keywords': 'ಕರ್ನಾಟಕ ಪೆಟ್ರೋಲ್ ದರ ಇಂದು, ಡೀಸೆಲ್ ಬೆಲೆ ಕರ್ನಾಟಕ, Petrol price Karnataka today, Diesel price Bengaluru, CNG rate Karnataka',
        'schema_type': 'Product',
        'geo_place': 'Karnataka, India'
    },
    'karnataka-elections.html': {
        'url': 'https://karnata.in/karnataka-elections',
        'priority': '0.80',
        'title': 'ಕರ್ನಾಟಕ ಚುನಾವಣೆ ಮಾಹಿತಿ & ಫಲಿತಾಂಶಗಳು | Karnataka Election Hub — Karnata.in',
        'desc': 'ಕರ್ನಾಟಕ ವಿಧಾನಸಭಾ, ಲೋಕಸಭಾ ಮತ್ತು ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳ ಚುನಾವಣೆ ಮಾಹಿತಿ, ಮತದಾರರ ನೋಂದಣಿ ಹಾಗೂ ಕ್ಷೇತ್ರವಾರು ಫಲಿತಾಂಶಗಳ ವಿಶ್ಲೇಷಣೆ.',
        'keywords': 'ಕರ್ನಾಟಕ ಚುನಾವಣೆ, ಮತದಾರರ ಪಟ್ಟಿ, ವಿಧಾನಸಭಾ ಚುನಾವಣೆ, Karnataka election results, Karnataka assembly election, Voter registration Karnataka',
        'schema_type': 'GovernmentService',
        'geo_place': 'Karnataka, India'
    },
    'karnataka-sir-voter-roll.html': {
        'url': 'https://karnata.in/karnataka-sir-voter-roll',
        'priority': '0.80',
        'title': 'ಕರ್ನಾಟಕ ಮತದಾರರ ಪಟ್ಟಿ ಆನ್‌ಲೈನ್ ಪರಿಶೀಲನೆ | Karnataka Electoral Roll & Voter ID Search — Karnata.in',
        'desc': 'ನಿಮ್ಮ ಮತದಾರರ ಗುರುತಿನ ಚೀಟಿ (Voter ID) ಮತ್ತು ಮತಗಟ್ಟೆ ವಿವರವನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಸರಳವಾಗಿ ಹುಡುಕಿ ಪರಿಶೀಲಿಸುವ ವಿಧಾನ.',
        'keywords': 'ಮತದಾರರ ಪಟ್ಟಿ ಕರ್ನಾಟಕ, ವೋಟರ್ ಐಡಿ ಚೆಕ್, Karnataka voter list online, Voter ID search Karnataka, CEO Karnataka electoral roll',
        'schema_type': 'GovernmentService',
        'geo_place': 'Karnataka, India'
    },
    'ai-jyothishya.html': {
        'url': 'https://karnata.in/ai-jyothishya',
        'priority': '0.75',
        'title': 'ಕನ್ನಡ AI ಜ್ಯೋತಿಷ್ಯ & ಜಾತಕ ವಿಶ್ಲೇಷಣೆ | Kannada AI Astrology & Daily Horoscope — Karnata.in',
        'desc': 'ನಿಮ್ಮ ರಾಶಿ ಭವಿಷ್ಯ, ಜನ್ಮ ಕುಂಡಲಿ, ನಕ್ಷತ್ರ ಫಲ ಮತ್ತು ವಾಸ್ತು ಸಲಹೆಗಳನ್ನು ಶುದ್ಧ ಕನ್ನಡದಲ್ಲಿ ಪಡೆಯುವ ಆಧುನಿಕ AI ಜ್ಯೋತಿಷ್ಯ ಸಹಾಯಕ.',
        'keywords': 'ಕನ್ನಡ ಜ್ಯೋತಿಷ್ಯ, ಇಂದಿನ ರಾಶಿ ಭವಿಷ್ಯ, AI ಜ್ಯೋತಿಷ್ಯ, Kannada astrology, Daily horoscope Kannada, Rashi bhavishya today',
        'schema_type': 'WebApplication',
        'geo_place': 'Karnataka, India'
    },
    'kannada-typing.html': {
        'url': 'https://karnata.in/kannada-typing',
        'priority': '0.75',
        'title': 'ಕನ್ನಡ ಟೈಪಿಂಗ್ & ನುಡಿ ಯುನಿಕೋಡ್ ಕನ್ವರ್ಟರ್ | Easy Kannada Typing Online Tool — Karnata.in',
        'desc': 'ಇಂಗ್ಲಿಷ್ ಅಕ್ಷರಗಳಲ್ಲಿ ಟೈಪ್ ಮಾಡಿ ನೇರವಾಗಿ ಶುದ್ಧ ಕನ್ನಡ ಲಿಪಿಗೆ ಪರಿವರ್ತಿಸುವ ಸುಲಭ ಆನ್‌ಲೈನ್ ಕನ್ನಡ ಟೈಪಿಂಗ್ ಮತ್ತು ನುಡಿ ಯುನಿಕೋಡ್ ಟೂಲ್.',
        'keywords': 'ಕನ್ನಡ ಟೈಪಿಂಗ್, ಇಂಗ್ಲಿಷ್ ಟು ಕನ್ನಡ, ನುಡಿ ಯುನಿಕೋಡ್, Kannada typing online, English to Kannada converter, Nudi to Unicode',
        'schema_type': 'WebApplication',
        'geo_place': 'Karnataka, India'
    },
    'emi-calculator.html': {
        'url': 'https://karnata.in/emi-calculator',
        'priority': '0.70',
        'title': 'ಗೃಹ & ವಾಹನ ಸಾಲ EMI ಕ್ಯಾಲ್ಕುಲೇಟರ್ | Home & Car Loan EMI Calculator Kannada — Karnata.in',
        'desc': 'ಗೃಹ ಸಾಲ, ವಾಹನ ಸಾಲ ಮತ್ತು ವೈಯಕ್ತಿಕ ಸಾಲದ ಮಾಸಿಕ ಇಎಂಐ (EMI) ಮತ್ತು ಬಡ್ಡಿಯನ್ನು ನಿಖರವಾಗಿ ಲೆಕ್ಕಹಾಕುವ ಕನ್ನಡ ಕ್ಯಾಲ್ಕುಲೇಟರ್.',
        'keywords': 'ಇಎಂಐ ಕ್ಯಾಲ್ಕುಲೇಟರ್, ಗೃಹ ಸಾಲ ಇಎಂಐ, EMI calculator Kannada, Home loan EMI calculator, Car loan calculator Karnataka',
        'schema_type': 'WebApplication',
        'geo_place': 'Karnataka, India'
    },
    'sip-calculator.html': {
        'url': 'https://karnata.in/sip-calculator',
        'priority': '0.70',
        'title': 'ಮ್ಯೂಚುಯಲ್ ಫಂಡ್ SIP ಕ್ಯಾಲ್ಕುಲೇಟರ್ | Mutual Fund SIP & Wealth Calculator — Karnata.in',
        'desc': 'ನಿಮ್ಮ ಮಾಸಿಕ ಮ್ಯೂಚುಯಲ್ ಫಂಡ್ ಹೂಡಿಕೆಯ ದೀರ್ಘಾವಧಿ ಲಾಭ ಮತ್ತು ಸಂಪತ್ತನ್ನು ಲೆಕ್ಕಹಾಕುವ ಕನ್ನಡ SIP ಕ್ಯಾಲ್ಕುಲೇಟರ್.',
        'keywords': 'ಎಸ್ಐಪಿ ಕ್ಯಾಲ್ಕುಲೇಟರ್, ಮ್ಯೂಚುಯಲ್ ಫಂಡ್ ಹೂಡಿಕೆ, SIP calculator Kannada, Mutual fund returns calculator',
        'schema_type': 'WebApplication',
        'geo_place': 'Karnataka, India'
    },
    'salary-calculator.html': {
        'url': 'https://karnata.in/salary-calculator',
        'priority': '0.70',
        'title': 'ಕರ್ನಾಟಕ ವೇತನ & ತೆರಿಗೆ ಕ್ಯಾಲ್ಕುಲೇಟರ್ | Take-Home Salary & Income Tax Calculator — Karnata.in',
        'desc': 'ಕರ್ನಾಟಕ ಸರ್ಕಾರಿ ಮತ್ತು ಖಾಸಗಿ ಉದ್ಯೋಗಿಗಳ ಸಿಟಿಸಿ (CTC), ಪಿಎಫ್ (PF), ಇಎಸ್‌ಐ ಮತ್ತು ಆದಾಯ ತೆರಿಗೆ ಕಡಿತದ ನಂತರದ ನಿವ್ವಳ ವೇತನ ಲೆಕ್ಕಾಚಾರ.',
        'keywords': 'ಸಂಬಳ ಕ್ಯಾಲ್ಕುಲೇಟರ್, ಆದಾಯ ತೆರಿಗೆ ಲೆಕ್ಕ, Salary calculator Kannada, In-hand salary calculator Karnataka, Income tax calculator',
        'schema_type': 'WebApplication',
        'geo_place': 'Karnataka, India'
    },
    'ask.html': {
        'url': 'https://karnata.in/ask',
        'priority': '0.85',
        'title': 'askKARNATA AI — ಕರ್ನಾಟಕದ ಅಧಿಕೃತ AI ಪ್ರಶ್ನೋತ್ತರ ಸಹಾಯಕ | AI Assistant for Karnataka — Karnata.in',
        'desc': 'ಕರ್ನಾಟಕದ ಆಡಳಿತ, ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು, ಹವಾಮಾನ, ಪ್ರವಾಸೋದ್ಯಮ, ಸಂಸ್ಕೃತಿ ಮತ್ತು ಇತಿಹಾಸದ ಬಗ್ಗೆ ನಿಮ್ಮ ಯಾವುದೇ ಪ್ರಶ್ನೆಗೆ ಕನ್ನಡದಲ್ಲೇ ಉತ್ತರಿಸುವ AI ಅಸಿಸ್ಟೆಂಟ್.',
        'keywords': 'askKARNATA AI, ಕನ್ನಡ AI, ಕರ್ನಾಟಕ ಪ್ರಶ್ನೋತ್ತರ, Kannada AI chatbot, Karnataka government AI assistant, askKARNATA',
        'schema_type': 'WebApplication',
        'geo_place': 'Karnataka, India'
    },
    'about.html': {
        'url': 'https://karnata.in/about',
        'priority': '0.60',
        'title': 'ನಮ್ಮ ಬಗ್ಗೆ | About Us — Karnata.in (ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ)',
        'desc': 'Karnata.in ಕರ್ನಾಟಕದ ನಾಗರಿಕರಿಗೆ ನಿಖರವಾದ, ಅಧಿಕೃತ ಮತ್ತು ನೈಜ-ಸಮಯದ ಸಾರ್ವಜನಿಕ ಮಾಹಿತಿ, ಹವಾಮಾನ, ಜಲಾಶಯಗಳು, ಕೃಷಿ ಮತ್ತು ಆಡಳಿತ ವಿವರಗಳನ್ನು ಒದಗಿಸುವ ಸ್ವತಂತ್ರ ವೇದಿಕೆಯಾಗಿದೆ.',
        'keywords': 'ನಮ್ಮ ಬಗ್ಗೆ, Karnata.in ಬಗ್ಗೆ, About Karnata.in, Karnataka citizen information portal',
        'schema_type': 'AboutPage',
        'geo_place': 'Bengaluru, Karnataka, India'
    },
    'contact.html': {
        'url': 'https://karnata.in/contact',
        'priority': '0.60',
        'title': 'ಸಂಪರ್ಕಿಸಿ | Contact Us — Karnata.in',
        'desc': 'Karnata.in ತಂಡವನ್ನು ಸಂಪರ್ಕಿಸಿ: ಪ್ರತಿಕ್ರಿಯೆಗಳು, ತಿದ್ದುಪಡಿಗಳು, ಜಾಹೀರಾತು ಮತ್ತು ಸಹಯೋಗಕ್ಕಾಗಿ ನಮ್ಮ ಇಮೇಲ್ ಅಥವಾ ಫಾರ್ಮ್ ಮೂಲಕ ಸಂಪರ್ಕಿಸಬಹುದು.',
        'keywords': 'ಸಂಪರ್ಕಿಸಿ, Karnata.in ಸಂಪರ್ಕ, Contact Karnata.in, Feedback Karnataka portal',
        'schema_type': 'ContactPage',
        'geo_place': 'Bengaluru, Karnataka, India'
    },
    'privacy-policy.html': {
        'url': 'https://karnata.in/privacy-policy',
        'priority': '0.50',
        'title': 'ಗೌಪ್ಯತಾ ನೀತಿ | Privacy Policy — Karnata.in',
        'desc': 'Karnata.in ಪೋರ್ಟಲ್‌ನ ಬಳಕೆದಾರರ ಗೌಪ್ಯತಾ ನೀತಿ ಮತ್ತು ಡೇಟಾ ಸಂರಕ್ಷಣಾ ನಿಯಮಾವಳಿಗಳ ಅಧಿಕೃತ ವಿವರ.',
        'keywords': 'ಗೌಪ್ಯತಾ ನೀತಿ, Privacy policy Karnata.in',
        'schema_type': 'WebPage',
        'geo_place': 'Karnataka, India'
    },
    'terms.html': {
        'url': 'https://karnata.in/terms',
        'priority': '0.50',
        'title': 'ನಿಯಮಗಳು ಮತ್ತು ಷರತ್ತುಗಳು | Terms & Conditions — Karnata.in',
        'desc': 'Karnata.in ಪೋರ್ಟಲ್ ಬಳಕೆದಾರರ ಸೇವಾ ನಿಯಮಗಳು, ಹಕ್ಕುಗಳು ಮತ್ತು ಷರತ್ತುಗಳ ಸಂಪೂರ್ಣ ಮಾಹಿತಿ.',
        'keywords': 'ನಿಯಮಗಳು ಮತ್ತು ಷರತ್ತುಗಳು, Terms and conditions Karnata.in',
        'schema_type': 'WebPage',
        'geo_place': 'Karnataka, India'
    },
    'disclaimer.html': {
        'url': 'https://karnata.in/disclaimer',
        'priority': '0.50',
        'title': 'ಹಕ್ಕುತ್ಯಾಗ | Disclaimer — Karnata.in',
        'desc': 'Karnata.in ನಲ್ಲಿ ಪ್ರಕಟವಾಗುವ ಹವಾಮಾನ, ಜಲಾಶಯಗಳು, ಮಾರುಕಟ್ಟೆ ದರಗಳು ಮತ್ತು ಸರ್ಕಾರಿ ಆದೇಶಗಳ ದತ್ತಾಂಶ ಹಕ್ಕುತ್ಯಾಗ ವಿವರಣೆ.',
        'keywords': 'ಹಕ್ಕುತ್ಯಾಗ, Disclaimer Karnata.in',
        'schema_type': 'WebPage',
        'geo_place': 'Karnataka, India'
    }
}

# ══════════════════════════════════════════════════════════════════════════════
# 1. OPTIMIZE METADATA ON EACH ACTIVE PAGE
# ══════════════════════════════════════════════════════════════════════════════
for rel_path, meta in ACTIVE_PAGES_META.items():
    file_path = os.path.join(ROOT_DIR, rel_path)
    if not os.path.exists(file_path):
        print(f"Skipping non-existent: {rel_path}")
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update <html lang="kn">
    html = re.sub(r'<html(?:\s+[^>]*)?>', '<html lang="kn">', html, count=1)

    # Clean existing title
    html = re.sub(r'<title>[\s\S]*?</title>', f'<title>{meta["title"]}</title>', html, count=1)

    # Standard SEO Head Block
    seo_head_block = f"""  <meta name="description" content="{meta['desc']}" />
  <meta name="keywords" content="{meta['keywords']}" />
  <link rel="canonical" href="{meta['url']}" />

  <!-- AI GEO & Search Engine Directives -->
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
  <meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large" />
  <meta name="bingbot" content="index, follow, max-snippet:-1, max-image-preview:large" />

  <!-- Regional Geo Tags (Karnataka, India) -->
  <meta name="geo.region" content="IN-KA" />
  <meta name="geo.placename" content="{meta['geo_place']}" />
  <meta name="geo.position" content="12.9716;77.5946" />
  <meta name="ICBM" content="12.9716, 77.5946" />

  <!-- Open Graph & Social Meta -->
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{meta['title']}" />
  <meta property="og:description" content="{meta['desc']}" />
  <meta property="og:url" content="{meta['url']}" />
  <meta property="og:site_name" content="ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ ಕೇಂದ್ರ — Karnata.in" />
  <meta property="og:locale" content="kn_IN" />
  <meta property="og:locale:alternate" content="en_IN" />
  <meta property="og:image" content="https://karnata.in/assets/images/og-karnata-preview.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{meta['title']}" />
  <meta name="twitter:description" content="{meta['desc']}" />
  <meta name="twitter:image" content="https://karnata.in/assets/images/og-karnata-preview.png" />"""

    # Replace meta description & canonical if already present or inject after <title>
    # Remove existing duplicates
    for tag_name in ['description', 'keywords', 'robots', 'googlebot', 'bingbot', 'geo.region', 'geo.placename', 'geo.position', 'ICBM']:
        html = re.sub(rf'<meta\s+name=["\']?{tag_name}["\']?[^>]*>\s*', '', html, flags=re.I)
    for prop_name in ['og:type', 'og:title', 'og:description', 'og:url', 'og:site_name', 'og:locale', 'og:locale:alternate', 'og:image', 'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image']:
        html = re.sub(rf'<meta\s+property=["\']?{prop_name}["\']?[^>]*>\s*', '', html, flags=re.I)
        html = re.sub(rf'<meta\s+name=["\']?{prop_name}["\']?[^>]*>\s*', '', html, flags=re.I)
    html = re.sub(r'<link\s+rel=["\']?canonical["\']?[^>]*>\s*', '', html, flags=re.I)

    # Inject cleaned SEO block right after <title>
    html = html.replace(f'<title>{meta["title"]}</title>', f'<title>{meta["title"]}</title>\n{seo_head_block}')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    # Sync with namma-karnataka copy
    namma_file = os.path.join(ROOT_DIR, 'namma-karnataka', rel_path)
    os.makedirs(os.path.dirname(namma_file), exist_ok=True)
    with open(namma_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"[OPTIMIZED] {rel_path}")

# ══════════════════════════════════════════════════════════════════════════════
# 2. GENERATE PRISTINE sitemap.xml CONTAINING ONLY ACTIVE PAGES
# ══════════════════════════════════════════════════════════════════════════════
sitemap_lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

for rel_path, meta in ACTIVE_PAGES_META.items():
    sitemap_lines.append('  <url>')
    sitemap_lines.append(f'    <loc>{meta["url"]}</loc>')
    sitemap_lines.append('    <lastmod>2026-08-29</lastmod>')
    sitemap_lines.append('    <changefreq>daily</changefreq>')
    sitemap_lines.append(f'    <priority>{meta["priority"]}</priority>')
    sitemap_lines.append('  </url>')

sitemap_lines.append('</urlset>')
sitemap_content = '\n'.join(sitemap_lines) + '\n'

with open(os.path.join(ROOT_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap_content)
with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print(f"Generated pristine sitemap.xml with {len(ACTIVE_PAGES_META)} active pages.")

# ══════════════════════════════════════════════════════════════════════════════
# 3. UPDATE robots.txt
# ══════════════════════════════════════════════════════════════════════════════
robots_content = """# Karnata.in Robots.txt for Search Engines & AI Crawlers (GEO / AI SEO)

User-agent: *
Allow: /
Disallow: /scratch/
Disallow: /api/
Disallow: /admin/
Disallow: /admin-articles
Disallow: /admin-transfers
Disallow: /cms/
Disallow: /studio/
Disallow: /imd_hub/
Disallow: /officers-admin
Disallow: /push-admin

# AI Search Engines & Crawlers
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Anthropic-ai
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Applebot-Extended
Allow: /

Sitemap: https://karnata.in/sitemap.xml
"""

with open(os.path.join(ROOT_DIR, 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write(robots_content)
with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write(robots_content)

print("Updated robots.txt")
print("SUCCESS_SEO_AND_GEO_OPTIMIZATION_COMPLETE")
