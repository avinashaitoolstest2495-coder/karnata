"""
Karnata — generate_district_pages.py
Generates all 30 Karnataka district pages automatically.
Each page is SEO-optimised with:
  - Unique meta title/description per district
  - Local MLA/MP/DC/SP data
  - Nearest dam info
  - Local APMC markets
  - District weather
  - Local government schemes info
  - Schema.org structured data

Run: python generate_district_pages.py
Output: ../districts/*.html  (30 files)
"""

import json
from pathlib import Path

OUT = Path("../districts")
OUT.mkdir(exist_ok=True)

# ─── Complete Karnataka district data ────────────────────────
DISTRICTS = [
    {
        "key": "bengaluru-urban",
        "name_kn": "ಬೆಂಗಳೂರು ನಗರ",
        "name_en": "Bengaluru Urban",
        "hq_kn": "ಬೆಂಗಳೂರು",
        "hq_en": "Bengaluru",
        "region": "South Karnataka",
        "population": "1,27,65,000",
        "area_km2": "2,190",
        "taluks_kn": ["ಬೆಂಗಳೂರು ಉತ್ತರ", "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ", "ಬೆಂಗಳೂರು ಪೂರ್ವ", "ಅನೇಕಲ್", "ಯಲಹಂಕ"],
        "taluks_en": ["Bengaluru North", "Bengaluru South", "Bengaluru East", "Anekal", "Yelahanka"],
        "assembly_seats": 28,
        "lok_sabha": "Bengaluru North, Bengaluru Central, Bengaluru South",
        "dc_name": "ಶ್ರೀ ಜಗದೀಶ್ (IAS)",
        "sp_name": "ಶ್ರೀ ರಮೇಶ್ (IPS)",
        "dc_phone": "080-22353822",
        "sp_phone": "080-22942222",
        "nearest_dam": "KRS ಅಣೆಕಟ್ಟು (ಮಂಡ್ಯ)",
        "apmc_markets": ["ಬೆಂಗಳೂರು", "ಕೃಷ್ಣರಾಜಪೇಟೆ"],
        "famous_for_kn": "ಸಿಲಿಕಾನ್ ವ್ಯಾಲಿ, ತಂತ್ರಜ್ಞಾನ ಕೇಂದ್ರ, ಸರ್ಕಾರಿ ರಾಜಧಾನಿ",
        "famous_for_en": "Silicon Valley of India, IT Hub, State Capital",
        "pin_codes": ["560001", "560002", "560003", "560038"],
        "key_mlas": ["ಡಾ. ಕೆ. ಸುಧಾಕರ್ (ಚಿಕ್ಕಬಳ್ಳಾಪುರ)", "ಎಸ್.ಆರ್. ವಿಶ್ವನಾಥ್ (ಯಲಹಂಕ)"],
        "lat": 12.9716, "lon": 77.5946,
        "seo_keywords": "Bengaluru Urban district, ಬೆಂಗಳೂರು ಜಿಲ್ಲೆ, Bangalore MLA list, BBMP ward, Bengaluru DC SP contact",
    },
    {
        "key": "bengaluru-rural",
        "name_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ",
        "name_en": "Bengaluru Rural",
        "hq_kn": "ದೇವನಹಳ್ಳಿ",
        "hq_en": "Devanahalli",
        "region": "South Karnataka",
        "population": "9,87,257",
        "area_km2": "2,259",
        "taluks_kn": ["ದೇವನಹಳ್ಳಿ", "ದೊಡ್ಡಬಳ್ಳಾಪುರ", "ಹೊಸಕೋಟೆ", "ನೆಲಮಂಗಲ"],
        "taluks_en": ["Devanahalli", "Doddaballapur", "Hoskote", "Nelamangala"],
        "assembly_seats": 4,
        "lok_sabha": "Bengaluru Rural",
        "dc_name": "ಶ್ರೀ ಆನಂದ್ (IAS)",
        "sp_name": "ಶ್ರೀ ಸಿದ್ಧಾರ್ಥ (IPS)",
        "dc_phone": "080-27734000",
        "sp_phone": "080-27734100",
        "nearest_dam": "ತಿಪ್ಪಗೊಂಡನಹಳ್ಳಿ ಜಲಾಶಯ",
        "apmc_markets": ["ದೊಡ್ಡಬಳ್ಳಾಪುರ", "ದೇವನಹಳ್ಳಿ"],
        "famous_for_kn": "ಕೆಂಪೇಗೌಡ ಅಂತರಾಷ್ಟ್ರೀಯ ವಿಮಾನ ನಿಲ್ದಾಣ, ಬ್ಯಾಡ್ಮಿಂಟನ್ ಆಟ",
        "famous_for_en": "Kempegowda International Airport, Silk weaving",
        "pin_codes": ["562110", "561203", "562114"],
        "key_mlas": ["ಎಂ.ಟಿ.ಬಿ. ನಾಗರಾಜ್ (ಹೊಸಕೋಟೆ)"],
        "lat": 13.0072, "lon": 77.5673,
        "seo_keywords": "Bengaluru Rural district, ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ, Devanahalli MLA, airport district Karnataka",
    },
    {
        "key": "mysuru",
        "name_kn": "ಮೈಸೂರು",
        "name_en": "Mysuru",
        "hq_kn": "ಮೈಸೂರು",
        "hq_en": "Mysuru",
        "region": "South Karnataka",
        "population": "30,01,127",
        "area_km2": "6,854",
        "taluks_kn": ["ಮೈಸೂರು", "ನಂಜನಗೂಡು", "ಹುಣಸೂರು", "ಎಚ್.ಡಿ. ಕೋಟೆ", "ಕೆ.ಆರ್. ನಗರ", "ಪಿರಿಯಾಪಟ್ಟಣ", "ತಿ.ನರಸೀಪುರ"],
        "taluks_en": ["Mysuru", "Nanjangud", "Hunsur", "H.D. Kote", "K.R. Nagar", "Periyapatna", "T. Narsipur"],
        "assembly_seats": 11,
        "lok_sabha": "Mysuru-Kodagu",
        "dc_name": "ಶ್ರೀ ಕೃಷ್ಣ (IAS)",
        "sp_name": "ಶ್ರೀ ಅಭಿಷೇಕ್ (IPS)",
        "dc_phone": "0821-2438400",
        "sp_phone": "0821-2444000",
        "nearest_dam": "KRS ಅಣೆಕಟ್ಟು, ಕಬಿನಿ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ಮೈಸೂರು", "ನಂಜನಗೂಡು"],
        "famous_for_kn": "ದಸರಾ ಹಬ್ಬ, ಅರಮನೆ, ಸಾಂಸ್ಕೃತಿಕ ನಗರ",
        "famous_for_en": "Dasara festival, Mysore Palace, Cultural capital",
        "pin_codes": ["570001", "570002", "571301"],
        "key_mlas": ["ತನ್ವೀರ್ ಸೇಠ್ (ಮೈಸೂರು)", "ಎಸ್.ಎ. ರಾಮದಾಸ್ (ನಂಜನಗೂಡು)"],
        "lat": 12.2958, "lon": 76.6394,
        "seo_keywords": "Mysuru district, ಮೈಸೂರು ಜಿಲ್ಲೆ, Mysore MLA DC SP, Kabini dam Mysuru, Mysore APMC",
    },
    {
        "key": "mandya",
        "name_kn": "ಮಂಡ್ಯ",
        "name_en": "Mandya",
        "hq_kn": "ಮಂಡ್ಯ",
        "hq_en": "Mandya",
        "region": "South Karnataka",
        "population": "19,13,552",
        "area_km2": "4,961",
        "taluks_kn": ["ಮಂಡ್ಯ", "ಮದ್ದೂರು", "ಮಳವಳ್ಳಿ", "ಕೆ.ಆರ್. ಪೇಟೆ", "ಪಾಂಡವಪುರ", "ಶ್ರೀರಂಗಪಟ್ಟಣ", "ನಾಗಮಂಗಲ"],
        "taluks_en": ["Mandya", "Maddur", "Malavalli", "K.R. Pete", "Pandavapura", "Srirangapatna", "Nagamangala"],
        "assembly_seats": 7,
        "lok_sabha": "Mandya",
        "dc_name": "ಶ್ರೀ ವೆಂಕಟೇಶ್ (IAS)",
        "sp_name": "ಶ್ರೀ ಮಲ್ಲಿಕಾರ್ಜುನ (IPS)",
        "dc_phone": "08232-222003",
        "sp_phone": "08232-222007",
        "nearest_dam": "KRS ಅಣೆಕಟ್ಟು (ಕೃಷ್ಣರಾಜ ಸಾಗರ)",
        "apmc_markets": ["ಮಂಡ್ಯ", "ಮದ್ದೂರು", "ಕೆ.ಆರ್. ಪೇಟೆ"],
        "famous_for_kn": "ಸಕ್ಕರೆ ಕಾರ್ಖಾನೆ, ಭತ್ತ, KRS ಅಣೆಕಟ್ಟು",
        "famous_for_en": "Sugar mills, Paddy farming, KRS Dam",
        "pin_codes": ["571401", "571402", "571422"],
        "key_mlas": ["ರವಿ ಗಣಿಗ (ಮಂಡ್ಯ)"],
        "lat": 12.5220, "lon": 76.8951,
        "seo_keywords": "Mandya district, ಮಂಡ್ಯ ಜಿಲ್ಲೆ, KRS dam level today, Mandya MLA, sugar Karnataka",
    },
    {
        "key": "hassan",
        "name_kn": "ಹಾಸನ",
        "name_en": "Hassan",
        "hq_kn": "ಹಾಸನ",
        "hq_en": "Hassan",
        "region": "South Karnataka",
        "population": "17,76,221",
        "area_km2": "6,814",
        "taluks_kn": ["ಹಾಸನ", "ಅರಕಲಗೂಡು", "ಅರಸೀಕೆರೆ", "ಬೇಲೂರು", "ಚನ್ನರಾಯಪಟ್ಟಣ", "ಹೊಳೆನರಸೀಪುರ", "ಸಕಲೇಶಪುರ", "ಆಲೂರು"],
        "taluks_en": ["Hassan", "Arakalagudu", "Arsikere", "Belur", "Channarayapatna", "Holenarasipura", "Sakleshpur", "Alur"],
        "assembly_seats": 8,
        "lok_sabha": "Hassan",
        "dc_name": "ಶ್ರೀ ರೋಹಿಣಿ (IAS)",
        "sp_name": "ಶ್ರೀ ಹರೀಶ್ (IPS)",
        "dc_phone": "08172-268011",
        "sp_phone": "08172-268016",
        "nearest_dam": "ಹೇಮಾವತಿ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ಹಾಸನ", "ಅರಸೀಕೆರೆ", "ಚನ್ನರಾಯಪಟ್ಟಣ"],
        "famous_for_kn": "ಬೇಲೂರು-ಹಳೇಬೀಡು ದೇವಾಲಯ, ಕಾಫಿ, ಅಡಿಕೆ",
        "famous_for_en": "Belur-Halebidu temples, Coffee, Arecanut",
        "pin_codes": ["573201", "573202", "573103"],
        "key_mlas": ["ಎಚ್.ಡಿ. ರೇವಣ್ಣ (ಹೊಳೆನರಸೀಪುರ)"],
        "lat": 13.0068, "lon": 76.1003,
        "seo_keywords": "Hassan district, ಹಾಸನ ಜಿಲ್ಲೆ, Hemavathi dam level, Hassan MLA DC, Belur temple",
    },
    {
        "key": "kodagu",
        "name_kn": "ಕೊಡಗು",
        "name_en": "Kodagu",
        "hq_kn": "ಮಡಿಕೇರಿ",
        "hq_en": "Madikeri",
        "region": "South Karnataka",
        "population": "5,54,762",
        "area_km2": "4,102",
        "taluks_kn": ["ಮಡಿಕೇರಿ", "ವಿರಾಜಪೇಟೆ", "ಸೋಮವಾರಪೇಟೆ"],
        "taluks_en": ["Madikeri", "Virajpet", "Somwarpet"],
        "assembly_seats": 2,
        "lok_sabha": "Mysuru-Kodagu",
        "dc_name": "ಶ್ರೀ ಅಮ್ಲಾನ್ (IAS)",
        "sp_name": "ಶ್ರೀ ಕಾರ್ತಿಕ್ (IPS)",
        "dc_phone": "08272-225005",
        "sp_phone": "08272-225010",
        "nearest_dam": "ಹಾರಂಗಿ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ಮಡಿಕೇರಿ", "ವಿರಾಜಪೇಟೆ"],
        "famous_for_kn": "ಕಾಫಿ, ಮಸಾಲೆ, ಮಳೆಕಾಡು, ಕೊಡವ ಜನರು",
        "famous_for_en": "Coffee, Spices, Rainforest, Coorg tourism",
        "pin_codes": ["571201", "571212", "571232"],
        "key_mlas": ["ಅಪ್ಪಚ್ಚು ರಂಜನ್ (ಮಡಿಕೇರಿ)"],
        "lat": 12.3375, "lon": 75.8069,
        "seo_keywords": "Kodagu district, ಕೊಡಗು ಜಿಲ್ಲೆ, Madikeri MLA, Harangi dam, Coorg coffee",
    },
    {
        "key": "dakshina-kannada",
        "name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ",
        "name_en": "Dakshina Kannada",
        "hq_kn": "ಮಂಗಳೂರು",
        "hq_en": "Mangaluru",
        "region": "Coastal Karnataka",
        "population": "20,83,625",
        "area_km2": "4,560",
        "taluks_kn": ["ಮಂಗಳೂರು", "ಬಂಟ್ವಾಳ", "ಬೆಳ್ತಂಗಡಿ", "ಕಡಬ", "ಪುತ್ತೂರು", "ಸುಳ್ಯ"],
        "taluks_en": ["Mangaluru", "Bantwal", "Belthangady", "Kadaba", "Puttur", "Sullia"],
        "assembly_seats": 8,
        "lok_sabha": "Dakshina Kannada",
        "dc_name": "ಶ್ರೀ ಮುಲ್ಲೈ ಮುಹಿಲನ್ (IAS)",
        "sp_name": "ಶ್ರೀ ಯತೀಶ್ (IPS)",
        "dc_phone": "0824-2220038",
        "sp_phone": "0824-2220100",
        "nearest_dam": "ಸೂಪ ಅಣೆಕಟ್ಟು, ವಾರಾಹಿ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ಮಂಗಳೂರು", "ಪುತ್ತೂರು"],
        "famous_for_kn": "ಮಂಗಳೂರಿನ ಬಂದರು, ತಾಳ ತೆಂಗಿನ ತೋಟ, ಉಡುಪಿ ಅಡಿಗೆ",
        "famous_for_en": "Mangalore port, Cashew, Udupi cuisine, Tulu culture",
        "pin_codes": ["575001", "575002", "574211"],
        "key_mlas": ["ಯು.ಟಿ. ಖಾದರ್ (ಮಂಗಳೂರು)"],
        "lat": 12.8438, "lon": 74.9919,
        "seo_keywords": "Dakshina Kannada district, ದಕ್ಷಿಣ ಕನ್ನಡ ಜಿಲ್ಲೆ, Mangaluru MLA DC, DK district Karnataka",
    },
    {
        "key": "udupi",
        "name_kn": "ಉಡುಪಿ",
        "name_en": "Udupi",
        "hq_kn": "ಉಡುಪಿ",
        "hq_en": "Udupi",
        "region": "Coastal Karnataka",
        "population": "11,77,361",
        "area_km2": "3,598",
        "taluks_kn": ["ಉಡುಪಿ", "ಕಾರ್ಕಳ", "ಕುಂದಾಪುರ"],
        "taluks_en": ["Udupi", "Karkala", "Kundapura"],
        "assembly_seats": 5,
        "lok_sabha": "Udupi-Chikkamagaluru",
        "dc_name": "ಶ್ರೀ ವಿದ್ಯಾಕುಮಾರಿ (IAS)",
        "sp_name": "ಶ್ರೀ ಅಕ್ಷಯ್ (IPS)",
        "dc_phone": "0820-2524636",
        "sp_phone": "0820-2524700",
        "nearest_dam": "ವಾರಾಹಿ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ಉಡುಪಿ", "ಕುಂದಾಪುರ"],
        "famous_for_kn": "ಕೃಷ್ಣ ಮಠ, ಯಕ್ಷಗಾನ, ಸಮುದ್ರ ತೀರ",
        "famous_for_en": "Udupi Krishna Temple, Yakshagana, Coastal tourism",
        "pin_codes": ["576101", "576201", "576111"],
        "key_mlas": ["ಯತ್ನಾಳ್ (ಉಡುಪಿ)"],
        "lat": 13.3409, "lon": 74.7421,
        "seo_keywords": "Udupi district, ಉಡುಪಿ ಜಿಲ್ಲೆ, Udupi MLA DC SP, Krishna temple, coastal Karnataka",
    },
    {
        "key": "shivamogga",
        "name_kn": "ಶಿವಮೊಗ್ಗ",
        "name_en": "Shivamogga",
        "hq_kn": "ಶಿವಮೊಗ್ಗ",
        "hq_en": "Shivamogga",
        "region": "Central Karnataka",
        "population": "17,52,753",
        "area_km2": "8,477",
        "taluks_kn": ["ಶಿವಮೊಗ್ಗ", "ಭದ್ರಾವತಿ", "ತೀರ್ಥಹಳ್ಳಿ", "ಸಾಗರ", "ಸೊರಬ", "ಶಿಕಾರಿಪುರ", "ಹೊಸನಗರ"],
        "taluks_en": ["Shivamogga", "Bhadravathi", "Thirthahalli", "Sagar", "Soraba", "Shikaripura", "Hosanagara"],
        "assembly_seats": 7,
        "lok_sabha": "Shivamogga",
        "dc_name": "ಶ್ರೀ ಕುಮಾರ್ (IAS)",
        "sp_name": "ಶ್ರೀ ಯಶಸ್ (IPS)",
        "dc_phone": "08182-222013",
        "sp_phone": "08182-222020",
        "nearest_dam": "ಲಿಂಗನಮಕ್ಕಿ ಅಣೆಕಟ್ಟು, ಭದ್ರಾ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ಶಿವಮೊಗ್ಗ", "ಸಾಗರ", "ಭದ್ರಾವತಿ"],
        "famous_for_kn": "ಕ್ರಾಂತಿವೀರ ಸಂಗೊಳ್ಳಿ ರಾಯಣ್ಣ, ಅಡಿಕೆ, ಲಿಂಗನಮಕ್ಕಿ ಜಲಪಾತ",
        "famous_for_en": "Jog Falls, Bhadra wildlife sanctuary, Areca nut",
        "pin_codes": ["577201", "577202", "577301"],
        "key_mlas": ["ಬಿ.ಎಸ್. ಯಡಿಯೂರಪ್ಪ (ಶಿಕಾರಿಪುರ)"],
        "lat": 13.9299, "lon": 75.5681,
        "seo_keywords": "Shivamogga district, ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆ, Linganamakki dam, Jog Falls, Shivamogga MLA DC",
    },
    {
        "key": "chikkamagaluru",
        "name_kn": "ಚಿಕ್ಕಮಗಳೂರು",
        "name_en": "Chikkamagaluru",
        "hq_kn": "ಚಿಕ್ಕಮಗಳೂರು",
        "hq_en": "Chikkamagaluru",
        "region": "Central Karnataka",
        "population": "11,37,753",
        "area_km2": "7,201",
        "taluks_kn": ["ಚಿಕ್ಕಮಗಳೂರು", "ಮೂಡಿಗೆರೆ", "ಕಡೂರು", "ಶೃಂಗೇರಿ", "ತರೀಕೆರೆ", "ಆಲೂರು", "ನರಸಿಂಹರಾಜಪುರ"],
        "taluks_en": ["Chikkamagaluru", "Mudigere", "Kadur", "Sringeri", "Tarikere", "Alur", "N.R. Pura"],
        "assembly_seats": 5,
        "lok_sabha": "Udupi-Chikkamagaluru",
        "dc_name": "ಶ್ರೀ ವರ್ಷಾ (IAS)",
        "sp_name": "ಶ್ರೀ ಪ್ರದೀಪ್ (IPS)",
        "dc_phone": "08262-222001",
        "sp_phone": "08262-222010",
        "nearest_dam": "ಭದ್ರಾ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ಚಿಕ್ಕಮಗಳೂರು", "ಕಡೂರು"],
        "famous_for_kn": "ಕಾಫಿ ತೋಟ, ಮುಳ್ಳಯ್ಯನ ಗಿರಿ, ಕಾಡು",
        "famous_for_en": "Coffee estates, Mullayanagiri trek, Bhadra wildlife",
        "pin_codes": ["577101", "577132", "577201"],
        "key_mlas": ["ಸಿ.ಟಿ. ರವಿ (ಚಿಕ್ಕಮಗಳೂರು)"],
        "lat": 13.3153, "lon": 75.7754,
        "seo_keywords": "Chikkamagaluru district, ಚಿಕ್ಕಮಗಳೂರು ಜಿಲ್ಲೆ, Bhadra dam level, coffee Karnataka, Chikkamagaluru MLA",
    },
    {
        "key": "tumakuru",
        "name_kn": "ತುಮಕೂರು",
        "name_en": "Tumakuru",
        "hq_kn": "ತುಮಕೂರು",
        "hq_en": "Tumakuru",
        "region": "South Karnataka",
        "population": "26,81,449",
        "area_km2": "10,597",
        "taluks_kn": ["ತುಮಕೂರು", "ತಿಪಟೂರು", "ಚಿಕ್ಕನಾಯಕನಹಳ್ಳಿ", "ಕುಣಿಗಲ್", "ಮಧುಗಿರಿ", "ಪಾವಗಡ", "ಶಿರಾ", "ಸಿರಾ", "ಕೊರಟಗೆರೆ", "ತುರುವೇಕೆರೆ"],
        "taluks_en": ["Tumakuru", "Tiptur", "Chikkanayakanhalli", "Kunigal", "Madhugiri", "Pavagada", "Shira", "Sira", "Koratagere", "Turuvekere"],
        "assembly_seats": 11,
        "lok_sabha": "Tumakuru",
        "dc_name": "ಶ್ರೀ ಶ್ರೀನಿವಾಸ್ (IAS)",
        "sp_name": "ಶ್ರೀ ಚಂದ್ರಶೇಖರ್ (IPS)",
        "dc_phone": "0816-2277237",
        "sp_phone": "0816-2277300",
        "nearest_dam": "ಗೊರೂರು ಜಲಾಶಯ",
        "apmc_markets": ["ತುಮಕೂರು", "ತಿಪಟೂರು"],
        "famous_for_kn": "ತೆಂಗಿನಕಾಯಿ, ರೇಷ್ಮೆ, ಪಾವಗಡ ಸೌರ ಶಕ್ತಿ ಪಾರ್ಕ್",
        "famous_for_en": "Coconut, Silk, Pavagada Solar Park (world's largest)",
        "pin_codes": ["572101", "572102", "572201"],
        "key_mlas": ["ಎಂ.ಟಿ.ಬಿ. ನಾಗರಾಜ್ (ತುಮಕೂರು)"],
        "lat": 13.3379, "lon": 77.1173,
        "seo_keywords": "Tumakuru district, ತುಮಕೂರು ಜಿಲ್ಲೆ, Tumkur MLA DC SP, Pavagada solar, coconut Karnataka",
    },
    {
        "key": "chitradurga",
        "name_kn": "ಚಿತ್ರದುರ್ಗ",
        "name_en": "Chitradurga",
        "hq_kn": "ಚಿತ್ರದುರ್ಗ",
        "hq_en": "Chitradurga",
        "region": "Central Karnataka",
        "population": "16,60,378",
        "area_km2": "8,440",
        "taluks_kn": ["ಚಿತ್ರದುರ್ಗ", "ಹಿರಿಯೂರು", "ಹೊಸದುರ್ಗ", "ಮೊಳಕಾಲ್ಮೂರು", "ಹೊಳಲ್ಕೆರೆ", "ಚಳ್ಳಕೆರೆ"],
        "taluks_en": ["Chitradurga", "Hiriyur", "Hosadurga", "Molakalmuru", "Holalkere", "Challakere"],
        "assembly_seats": 6,
        "lok_sabha": "Chitradurga",
        "dc_name": "ಶ್ರೀ ಮಹಾಂತೇಶ (IAS)",
        "sp_name": "ಶ್ರೀ ರವಿಶಂಕರ್ (IPS)",
        "dc_phone": "08194-222225",
        "sp_phone": "08194-222010",
        "nearest_dam": "ವಾಣಿ ವಿಲಾಸ ಸಾಗರ",
        "apmc_markets": ["ಚಿತ್ರದುರ್ಗ", "ಹಿರಿಯೂರು"],
        "famous_for_kn": "ಒನಕೆ ಓಬವ್ವ ಕಿಂಡಿ, ಕೋಟೆ, ಸಾಂಸ್ಕೃತಿಕ ಇತಿಹಾಸ",
        "famous_for_en": "Chitradurga Fort, Onake Obavva, Historical significance",
        "pin_codes": ["577501", "577502", "577526"],
        "key_mlas": ["ಎ. ಮಂಜು (ಚಿತ್ರದುರ್ಗ)"],
        "lat": 14.2226, "lon": 76.3984,
        "seo_keywords": "Chitradurga district, ಚಿತ್ರದುರ್ಗ ಜಿಲ್ಲೆ, Chitradurga fort, Chitradurga MLA DC SP",
    },
    {
        "key": "davanagere",
        "name_kn": "ದಾವಣಗೆರೆ",
        "name_en": "Davanagere",
        "hq_kn": "ದಾವಣಗೆರೆ",
        "hq_en": "Davanagere",
        "region": "Central Karnataka",
        "population": "19,46,905",
        "area_km2": "5,924",
        "taluks_kn": ["ದಾವಣಗೆರೆ", "ಹರಪನಹಳ್ಳಿ", "ಜಗಳೂರು", "ಚನ್ನಗಿರಿ", "ಹೊನ್ನಾಳಿ", "ನ್ಯಾಮತಿ"],
        "taluks_en": ["Davanagere", "Harapanahalli", "Jagalur", "Channagiri", "Honnali", "Nyamati"],
        "assembly_seats": 6,
        "lok_sabha": "Davanagere",
        "dc_name": "ಶ್ರೀ ಮಹಮ್ಮದ್ ಅಜ್ಹರ್ (IAS)",
        "sp_name": "ಶ್ರೀ ಹನುಮಂತ (IPS)",
        "dc_phone": "08192-231610",
        "sp_phone": "08192-231800",
        "nearest_dam": "ಭದ್ರಾ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ದಾವಣಗೆರೆ", "ಹರಪನಹಳ್ಳಿ"],
        "famous_for_kn": "ಬ್ಯಾಣ ಮಸಾಲೆ ಬನ್ಸ್, ಹತ್ತಿ ನಗರ, ವಸ್ತ್ರ ಉದ್ಯಮ",
        "famous_for_en": "Davanagere Benne Dosa, Cotton textile industry",
        "pin_codes": ["577001", "577002", "577512"],
        "key_mlas": ["ಎಸ್.ಎ. ರವೀಂದ್ರ (ದಾವಣಗೆರೆ)"],
        "lat": 14.4644, "lon": 75.9218,
        "seo_keywords": "Davanagere district, ದಾವಣಗೆರೆ ಜಿಲ್ಲೆ, Davanagere MLA DC SP, cotton Karnataka",
    },
    {
        "key": "belagavi",
        "name_kn": "ಬೆಳಗಾವಿ",
        "name_en": "Belagavi",
        "hq_kn": "ಬೆಳಗಾವಿ",
        "hq_en": "Belagavi",
        "region": "North Karnataka",
        "population": "48,09,290",
        "area_km2": "13,415",
        "taluks_kn": ["ಬೆಳಗಾವಿ", "ಗೋಕಾಕ", "ಚಿಕ್ಕೋಡಿ", "ಬೈಲಹೊಂಗಲ", "ರಾಯಬಾಗ", "ಅಥಣಿ", "ರಾಮದುರ್ಗ", "ಮೂಡಲಗಿ", "ಸವದತ್ತಿ", "ಖಾನಾಪುರ", "ಕಿತ್ತೂರು", "ಹುಕ್ಕೇರಿ"],
        "taluks_en": ["Belagavi", "Gokak", "Chikodi", "Bailhongal", "Raybag", "Athani", "Ramdurg", "Mudalgi", "Savadatti", "Khanapur", "Kittur", "Hukkeri"],
        "assembly_seats": 18,
        "lok_sabha": "Belagavi",
        "dc_name": "ಶ್ರೀ ಮಹಮ್ಮದ್ ರೋಷನ್ (IAS)",
        "sp_name": "ಶ್ರೀ ಶ್ರೀಧರ (IPS)",
        "dc_phone": "0831-2401005",
        "sp_phone": "0831-2401100",
        "nearest_dam": "ಮಲಪ್ರಭಾ, ಘಟಪ್ರಭಾ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ಬೆಳಗಾವಿ", "ಗೋಕಾಕ", "ಚಿಕ್ಕೋಡಿ"],
        "famous_for_kn": "ಕಿತ್ತೂರು ಚೆನ್ನಮ್ಮ, ಕಬ್ಬು, ಉತ್ತರ ಕರ್ನಾಟಕ ವಾಣಿಜ್ಯ ಕೇಂದ್ರ",
        "famous_for_en": "Kittur Chennamma, Sugarcane, Commercial hub of North Karnataka",
        "pin_codes": ["590001", "590002", "591302"],
        "key_mlas": ["ಅಭಯ ಪಾಟೀಲ (ಬೆಳಗಾವಿ ಉತ್ತರ)"],
        "lat": 15.8497, "lon": 74.4977,
        "seo_keywords": "Belagavi district, ಬೆಳಗಾವಿ ಜಿಲ್ಲೆ, Belgaum MLA DC SP, Malaprabha dam, North Karnataka",
    },
    {
        "key": "dharwad",
        "name_kn": "ಧಾರವಾಡ",
        "name_en": "Dharwad",
        "hq_kn": "ಧಾರವಾಡ",
        "hq_en": "Dharwad",
        "region": "North Karnataka",
        "population": "18,46,993",
        "area_km2": "4,260",
        "taluks_kn": ["ಧಾರವಾಡ", "ಹುಬ್ಬಳ್ಳಿ", "ಕಲಘಟಗಿ", "ನವಲಗುಂದ", "ಕುಂದಗೋಳ", "ಅಣ್ಣಿಗೇರಿ"],
        "taluks_en": ["Dharwad", "Hubli", "Kalghatgi", "Navalgund", "Kundagol", "Annigeri"],
        "assembly_seats": 8,
        "lok_sabha": "Dharwad",
        "dc_name": "ಶ್ರೀ ಗುರುದತ್ (IAS)",
        "sp_name": "ಶ್ರೀ ಥಾಕೂರ ರಾಮ್ (IPS)",
        "dc_phone": "0836-2447906",
        "sp_phone": "0836-2447700",
        "nearest_dam": "ನವಿಲು ತೀರ್ಥ",
        "apmc_markets": ["ಹುಬ್ಬಳ್ಳಿ", "ಧಾರವಾಡ"],
        "famous_for_kn": "ಧಾರವಾಡ ಪೇಡ, ಹಿಂದೂಸ್ಥಾನಿ ಸಂಗೀತ, IIT ಧಾರವಾಡ",
        "famous_for_en": "Dharwad Peda (sweet), Hindustani music, IIT Dharwad",
        "pin_codes": ["580001", "580002", "580023"],
        "key_mlas": ["ಪ್ರಹ್ಲಾದ ಜೋಶಿ (ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ ಕೇಂದ್ರ)"],
        "lat": 15.4589, "lon": 75.0078,
        "seo_keywords": "Dharwad district, ಧಾರವಾಡ ಜಿಲ್ಲೆ, Hubli Dharwad MLA, IIT Dharwad, Dharwad peda",
    },
    {
        "key": "gadag",
        "name_kn": "ಗದಗ",
        "name_en": "Gadag",
        "hq_kn": "ಗದಗ-ಬೆಟಗೇರಿ",
        "hq_en": "Gadag-Betageri",
        "region": "North Karnataka",
        "population": "10,65,235",
        "area_km2": "4,656",
        "taluks_kn": ["ಗದಗ", "ರೋಣ", "ಮುಂಡರಗಿ", "ನರಗುಂದ", "ಶಿರಹಟ್ಟಿ"],
        "taluks_en": ["Gadag", "Ron", "Mundargi", "Nargund", "Shirhatti"],
        "assembly_seats": 5,
        "lok_sabha": "Dharwad",
        "dc_name": "ಶ್ರೀ ಮಹಮ್ಮದ್ ರೋಷಾನ್ (IAS)",
        "sp_name": "ಶ್ರೀ ಆಕಾಶ್ (IPS)",
        "dc_phone": "08372-236036",
        "sp_phone": "08372-236100",
        "nearest_dam": "ಮಲಪ್ರಭಾ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ಗದಗ", "ರೋಣ"],
        "famous_for_kn": "ತ್ರಿಕೂಟೇಶ್ವರ ದೇವಾಲಯ, ಅಕ್ಕಿ, ಗೋವಿನಜೋಳ",
        "famous_for_en": "Trikuteshwara Temple, Cotton weaving, Jowar cultivation",
        "pin_codes": ["582101", "582102", "582201"],
        "key_mlas": ["ಹೆಚ್.ಕೆ. ಪಾಟೀಲ (ಗದಗ)"],
        "lat": 15.4167, "lon": 75.6167,
        "seo_keywords": "Gadag district, ಗದಗ ಜಿಲ್ಲೆ, Gadag MLA DC SP, North Karnataka district",
    },
    {
        "key": "haveri",
        "name_kn": "ಹಾವೇರಿ",
        "name_en": "Haveri",
        "hq_kn": "ಹಾವೇರಿ",
        "hq_en": "Haveri",
        "region": "North Karnataka",
        "population": "15,98,094",
        "area_km2": "4,823",
        "taluks_kn": ["ಹಾವೇರಿ", "ರಾಣೆಬೆನ್ನೂರ", "ಹಂಸಬಾವಿ", "ಶಿಗ್ಗಾಂವ", "ಬ್ಯಾಡಗಿ", "ಸವಣೂರ"],
        "taluks_en": ["Haveri", "Ranebennur", "Hamsabavi", "Shiggaon", "Byadagi", "Savanur"],
        "assembly_seats": 6,
        "lok_sabha": "Haveri",
        "dc_name": "ಶ್ರೀ ರಾಘವೇಂದ್ರ (IAS)",
        "sp_name": "ಶ್ರೀ ಗೋಪಿ (IPS)",
        "dc_phone": "08375-235027",
        "sp_phone": "08375-235100",
        "nearest_dam": "ಕಿಮ್ಮನ ಪ್ರಭ",
        "apmc_markets": ["ಹಾವೇರಿ", "ರಾಣೆಬೆನ್ನೂರ", "ಬ್ಯಾಡಗಿ"],
        "famous_for_kn": "ಬ್ಯಾಡಗಿ ಖಾರ, ಹತ್ತಿ, ಮೆಣಸಿನಕಾಯಿ ಮಾರುಕಟ್ಟೆ",
        "famous_for_en": "Byadagi Chilli (world famous), Cotton, Kadlekalu",
        "pin_codes": ["581110", "581201", "581306"],
        "key_mlas": ["ಶ್ರೀ ನೇಹರು ಒಳೇಕಾರ (ಹಾವೇರಿ)"],
        "lat": 14.7957, "lon": 75.3998,
        "seo_keywords": "Haveri district, ಹಾವೇರಿ ಜಿಲ್ಲೆ, Haveri MLA DC, Byadagi chilli market Karnataka",
    },
    {
        "key": "uttara-kannada",
        "name_kn": "ಉತ್ತರ ಕನ್ನಡ",
        "name_en": "Uttara Kannada",
        "hq_kn": "ಕಾರವಾರ",
        "hq_en": "Karwar",
        "region": "Coastal Karnataka",
        "population": "14,37,169",
        "area_km2": "10,291",
        "taluks_kn": ["ಕಾರವಾರ", "ಸಿದ್ದಾಪುರ", "ಶಿರಸಿ", "ಹಳಿಯಾಳ", "ಸುಪ", "ಅಂಕೋಲ", "ಕುಮಟ", "ಭಟ್ಕಳ", "ಯಲ್ಲಾಪುರ", "ಮುಂಡಗೋಡ", "ಜೋಯಿಡ"],
        "taluks_en": ["Karwar", "Siddapur", "Sirsi", "Haliyal", "Supa", "Ankola", "Kumta", "Bhatkal", "Yellapur", "Mundgod", "Joida"],
        "assembly_seats": 6,
        "lok_sabha": "Uttara Kannada",
        "dc_name": "ಶ್ರೀ ಲಕ್ಷ್ಮೀ ಪ್ರಿಯಾ (IAS)",
        "sp_name": "ಶ್ರೀ ಉಲ್ಲಾಸ್ (IPS)",
        "dc_phone": "08382-226001",
        "sp_phone": "08382-226100",
        "nearest_dam": "ಸೂಪ ಅಣೆಕಟ್ಟು (ಕಾಳಿ ನದಿ)",
        "apmc_markets": ["ಕಾರವಾರ", "ಶಿರಸಿ"],
        "famous_for_kn": "ಅರೇಬಿಯನ್ ಸಮುದ್ರ ತೀರ, ನವ್ಯ ಅರಣ್ಯ, ಸ್ವರ್ಣ ನದಿ",
        "famous_for_en": "Arabian Sea coast, Western Ghats, Naval base Karwar",
        "pin_codes": ["581301", "581401", "581315"],
        "key_mlas": ["ಅರ್ ವಿ ದೇಶಪಾಂಡೆ (ಶಿರಸಿ)"],
        "lat": 14.7941, "lon": 74.6561,
        "seo_keywords": "Uttara Kannada district, ಉತ್ತರ ಕನ್ನಡ ಜಿಲ್ಲೆ, Karwar MLA DC, Supa dam, coastal Karnataka",
    },
    {
        "key": "bagalkote",
        "name_kn": "ಬಾಗಲಕೋಟೆ",
        "name_en": "Bagalkote",
        "hq_kn": "ಬಾಗಲಕೋಟೆ",
        "hq_en": "Bagalkote",
        "region": "North Karnataka",
        "population": "18,90,826",
        "area_km2": "6,575",
        "taluks_kn": ["ಬಾಗಲಕೋಟೆ", "ಬೀಳಗಿ", "ಮುಧೋಳ", "ಜಮಖಂಡಿ", "ಹುನಗುಂದ", "ಬಾದಾಮಿ"],
        "taluks_en": ["Bagalkote", "Bilagi", "Mudhol", "Jamkhandi", "Hungund", "Badami"],
        "assembly_seats": 6,
        "lok_sabha": "Bagalkote",
        "dc_name": "ಶ್ರೀ ಸ್ಯಾಮ್ (IAS)",
        "sp_name": "ಶ್ರೀ ಸಿದ್ಧಲಿಂಗ (IPS)",
        "dc_phone": "08354-232007",
        "sp_phone": "08354-232100",
        "nearest_dam": "ಆಲಮಟ್ಟಿ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ಬಾಗಲಕೋಟೆ", "ಜಮಖಂಡಿ"],
        "famous_for_kn": "ಬಾದಾಮಿ ಗುಹಾ ದೇವಾಲಯ, ದ್ರಾಕ್ಷಿ, ದಾಳಿಂಬೆ",
        "famous_for_en": "Badami cave temples, Grapes, Pomegranate, Almatti dam",
        "pin_codes": ["587101", "587102", "587201"],
        "key_mlas": ["ವೀರಣ್ಣ ಚರಂತಿಮಠ (ಬಾಗಲಕೋಟೆ)"],
        "lat": 16.1831, "lon": 75.6965,
        "seo_keywords": "Bagalkote district, ಬಾಗಲಕೋಟೆ ಜಿಲ್ಲೆ, Almatti dam level, Badami caves, Bagalkote MLA",
    },
    {
        "key": "vijayapura",
        "name_kn": "ವಿಜಯಪುರ",
        "name_en": "Vijayapura",
        "hq_kn": "ವಿಜಯಪುರ",
        "hq_en": "Vijayapura",
        "region": "North Karnataka",
        "population": "21,75,102",
        "area_km2": "10,494",
        "taluks_kn": ["ವಿಜಯಪುರ", "ಸಿಂದಗಿ", "ಮುದ್ದೇಬಿಹಾಳ", "ಇಂಡಿ", "ಬಸವನ ಬಾಗೇವಾಡಿ", "ತಾಳಿಕೋಟ"],
        "taluks_en": ["Vijayapura", "Sindagi", "Muddebihal", "Indi", "Basavana Bagewadi", "Talikota"],
        "assembly_seats": 7,
        "lok_sabha": "Bijapur",
        "dc_name": "ಶ್ರೀ ಹಾಜ್ ಪ್ರಮೀಳಾ (IAS)",
        "sp_name": "ಶ್ರೀ ರಾಹುಲ್ (IPS)",
        "dc_phone": "08352-252000",
        "sp_phone": "08352-252100",
        "nearest_dam": "ಆಲಮಟ್ಟಿ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ವಿಜಯಪುರ", "ಇಂಡಿ"],
        "famous_for_kn": "ಗೋಲ್ ಗುಮ್ಮಟ, ಒಂಟೆ-ಗೋಪು, ಮಸ್ತ್ ನಿರ್ಮಾಣ ಕಲೆ",
        "famous_for_en": "Gol Gumbaz, Adil Shah dynasty, Pomegranate farming",
        "pin_codes": ["586101", "586102", "586201"],
        "key_mlas": ["ಬಸನಗೌಡ ಪಾಟೀಲ ಯತ್ನಾಳ (ವಿಜಯಪುರ)"],
        "lat": 16.8302, "lon": 75.7100,
        "seo_keywords": "Vijayapura district Bijapur, ವಿಜಯಪುರ ಜಿಲ್ಲೆ, Gol Gumbaz, Vijayapura MLA DC SP",
    },
    {
        "key": "kalaburagi",
        "name_kn": "ಕಲಬುರಗಿ",
        "name_en": "Kalaburagi",
        "hq_kn": "ಕಲಬುರಗಿ",
        "hq_en": "Kalaburagi",
        "region": "Hyderabad-Karnataka",
        "population": "27,23,156",
        "area_km2": "16,224",
        "taluks_kn": ["ಕಲಬುರಗಿ", "ಅಳಂದ", "ಅಫ್ಜಲ್ಪುರ", "ಚಿಂಚೋಳಿ", "ಚಿತ್ತಾಪುರ", "ಜೇವರ್ಗಿ", "ಸೇಡಂ", "ಯಾದಗಿರ"],
        "taluks_en": ["Kalaburagi", "Aland", "Afzalpur", "Chincholi", "Chittapur", "Jevargi", "Sedam", "Yadgir"],
        "assembly_seats": 8,
        "lok_sabha": "Kalaburagi",
        "dc_name": "ಶ್ರೀ ಫೌಜಿಯಾ ತರನ್ನುಮ್ (IAS)",
        "sp_name": "ಶ್ರೀ ಇಶಾನ್ (IPS)",
        "dc_phone": "08472-272003",
        "sp_phone": "08472-272100",
        "nearest_dam": "ಭೀಮಾ ನದಿ ಯೋಜನೆ",
        "apmc_markets": ["ಕಲಬುರಗಿ", "ಸೇಡಂ"],
        "famous_for_kn": "ತೊಗರಿ ಬೆಳೆ, ಕಲ್ಯಾಣ ಕರ್ನಾಟಕ, ಐತಿಹಾಸಿಕ ಕೋಟೆ",
        "famous_for_en": "Tur dal farming, Gulbarga fort, Kalyana Karnataka region",
        "pin_codes": ["585101", "585102", "585201"],
        "key_mlas": ["ಅಲ್ಲಮಪ್ರಭು ಪಾಟೀಲ (ಕಲಬುರಗಿ)"],
        "lat": 17.3297, "lon": 76.8343,
        "seo_keywords": "Kalaburagi Gulbarga district, ಕಲಬುರಗಿ ಜಿಲ್ಲೆ, Gulbarga MLA DC SP, toor dal Karnataka",
    },
    {
        "key": "yadgir",
        "name_kn": "ಯಾದಗಿರಿ",
        "name_en": "Yadgir",
        "hq_kn": "ಯಾದಗಿರಿ",
        "hq_en": "Yadgir",
        "region": "Hyderabad-Karnataka",
        "population": "11,72,985",
        "area_km2": "5,517",
        "taluks_kn": ["ಯಾದಗಿರಿ", "ಶಹಾಪುರ", "ಸುರಪುರ"],
        "taluks_en": ["Yadgir", "Shahapur", "Shorapur"],
        "assembly_seats": 3,
        "lok_sabha": "Yadgir",
        "dc_name": "ಶ್ರೀ ರಾಜೇಶ್ (IAS)",
        "sp_name": "ಶ್ರೀ ಮಂಜುನಾಥ (IPS)",
        "dc_phone": "08473-252036",
        "sp_phone": "08473-252100",
        "nearest_dam": "ನಾರಾಯಣಪುರ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ಯಾದಗಿರಿ", "ಶಹಾಪುರ"],
        "famous_for_kn": "ಮಾವು, ತೊಗರಿ, ಶ್ರೀಶೈಲ ಪ್ರವಾಸ ರಸ್ತೆ",
        "famous_for_en": "Mango, Tur dal, Narayanapura dam",
        "pin_codes": ["585201", "585236", "585214"],
        "key_mlas": ["ವೆಂಕಟ ರೆಡ್ಡಿ (ಶಹಾಪುರ)"],
        "lat": 16.7620, "lon": 77.1382,
        "seo_keywords": "Yadgir district, ಯಾದಗಿರಿ ಜಿಲ್ಲೆ, Narayanapura dam, Yadgir MLA DC SP",
    },
    {
        "key": "raichur",
        "name_kn": "ರಾಯಚೂರು",
        "name_en": "Raichur",
        "hq_kn": "ರಾಯಚೂರು",
        "hq_en": "Raichur",
        "region": "Hyderabad-Karnataka",
        "population": "19,28,812",
        "area_km2": "8,442",
        "taluks_kn": ["ರಾಯಚೂರು", "ದೇವದುರ್ಗ", "ಮಾನ್ವಿ", "ಲಿಂಗಸ್ಗೂರ", "ಸಿಂಧನೂರ"],
        "taluks_en": ["Raichur", "Devadurga", "Manvi", "Lingasur", "Sindhanur"],
        "assembly_seats": 7,
        "lok_sabha": "Raichur",
        "dc_name": "ಶ್ರೀ ಡಾ. ಕೆ.ವಿ. ರಾಜೇಂದ್ರ (IAS)",
        "sp_name": "ಶ್ರೀ ಕೋರ್ ಸಿದ್ಧ (IPS)",
        "dc_phone": "08532-222203",
        "sp_phone": "08532-222400",
        "nearest_dam": "ತುಂಗಭದ್ರ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ರಾಯಚೂರು", "ಸಿಂಧನೂರ"],
        "famous_for_kn": "ಭತ್ತ, ತೊಗರಿ, ರಾಯಚೂರು ಕೋಟೆ, ಕೃಷ್ಣ ನದಿ",
        "famous_for_en": "Rice, Tur dal, Raichur fort, Krishna-Tungabhadra doab",
        "pin_codes": ["584101", "584102", "584128"],
        "key_mlas": ["ಬಸವರಾಜ ದಡ್ಡಲ (ರಾಯಚೂರು)"],
        "lat": 16.2120, "lon": 77.3439,
        "seo_keywords": "Raichur district, ರಾಯಚೂರು ಜಿಲ್ಲೆ, Raichur MLA DC SP, Tungabhadra dam Raichur",
    },
    {
        "key": "koppal",
        "name_kn": "ಕೊಪ್ಪಳ",
        "name_en": "Koppal",
        "hq_kn": "ಕೊಪ್ಪಳ",
        "hq_en": "Koppal",
        "region": "North Karnataka",
        "population": "13,91,236",
        "area_km2": "5,591",
        "taluks_kn": ["ಕೊಪ್ಪಳ", "ಗಂಗಾವತಿ", "ಕುಷ್ಟಗಿ", "ಯಲಬುರ್ಗ"],
        "taluks_en": ["Koppal", "Gangavathi", "Kushtagi", "Yalabura"],
        "assembly_seats": 4,
        "lok_sabha": "Koppal",
        "dc_name": "ಶ್ರೀ ದೇಬಿ ಪ್ರಸಾದ್ (IAS)",
        "sp_name": "ಶ್ರೀ ಗೋಪಾಲ (IPS)",
        "dc_phone": "08539-220001",
        "sp_phone": "08539-220100",
        "nearest_dam": "ತುಂಗಭದ್ರ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ಗಂಗಾವತಿ", "ಕೊಪ್ಪಳ"],
        "famous_for_kn": "ಕ್ರಾಂತಿ ವೀರ ಸಂಗೊಳ್ಳಿ ರಾಯಣ್ಣ ಜನ್ಮಭೂಮಿ, ಅಕ್ಕಿ",
        "famous_for_en": "Sangollirayanna birthplace, Rice, Pampa Sarovar",
        "pin_codes": ["583231", "583227", "583201"],
        "key_mlas": ["ರಾಘವೇಂದ್ರ ಹಿಟ್ನಾಳ (ಕೊಪ್ಪಳ)"],
        "lat": 15.3474, "lon": 76.1547,
        "seo_keywords": "Koppal district, ಕೊಪ್ಪಳ ಜಿಲ್ಲೆ, Koppal MLA DC SP, Gangavathi APMC rice",
    },
    {
        "key": "ballari",
        "name_kn": "ಬಳ್ಳಾರಿ",
        "name_en": "Ballari",
        "hq_kn": "ಬಳ್ಳಾರಿ",
        "hq_en": "Ballari",
        "region": "North Karnataka",
        "population": "28,32,280",
        "area_km2": "8,419",
        "taluks_kn": ["ಬಳ್ಳಾರಿ", "ಹೊಸಪೇಟೆ", "ಸಂಡೂರು", "ಸಿರಗುಪ್ಪ", "ಹಡಗಲಿ", "ಕೂಡ್ಲಿಗಿ"],
        "taluks_en": ["Ballari", "Hosapete", "Sandur", "Siruguppa", "Hadagali", "Kudligi"],
        "assembly_seats": 8,
        "lok_sabha": "Ballari",
        "dc_name": "ಶ್ರೀ ಪವನ್ ಕುಮಾರ್ (IAS)",
        "sp_name": "ಶ್ರೀ ಕ್ಯಾಪ್ಟನ್ ರಾಹುಲ್ (IPS)",
        "dc_phone": "08392-277000",
        "sp_phone": "08392-277100",
        "nearest_dam": "ತುಂಗಭದ್ರ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ಬಳ್ಳಾರಿ", "ಹೊಸಪೇಟೆ"],
        "famous_for_kn": "ಕಬ್ಬಿಣ ಅದಿರು, ವಿಜಯನಗರ ಸಾಮ್ರಾಜ್ಯ, ಹಂಪಿ",
        "famous_for_en": "Iron ore mining, Hampi (UNESCO), Vijayanagara empire",
        "pin_codes": ["583101", "583201", "583104"],
        "key_mlas": ["ಬಿ. ನಾಗೇಂದ್ರ (ಹೊಸಪೇಟೆ)"],
        "lat": 15.1394, "lon": 76.9214,
        "seo_keywords": "Ballari district, ಬಳ್ಳಾರಿ ಜಿಲ್ಲೆ, Hampi Karnataka, Ballari MLA DC SP, Tungabhadra dam",
    },
    {
        "key": "vijayanagara",
        "name_kn": "ವಿಜಯನಗರ",
        "name_en": "Vijayanagara",
        "hq_kn": "ಹೊಸಪೇಟೆ",
        "hq_en": "Hosapete",
        "region": "North Karnataka",
        "population": "13,21,000",
        "area_km2": "5,104",
        "taluks_kn": ["ಹೊಸಪೇಟೆ", "ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ", "ಹೂವಿನಹಡಗಲಿ", "ಕೂಡ್ಲಿಗಿ"],
        "taluks_en": ["Hosapete", "Hagari Bommanahalli", "Hoovina Hadagali", "Kudligi"],
        "assembly_seats": 4,
        "lok_sabha": "Ballari",
        "dc_name": "ಶ್ರೀ ಎ.ಟಿ. ರಮೇಶ್ (IAS)",
        "sp_name": "ಶ್ರೀ ಮಲ್ಲಿಕಾರ್ಜುನ (IPS)",
        "dc_phone": "08394-241001",
        "sp_phone": "08394-241100",
        "nearest_dam": "ತುಂಗಭದ್ರ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ಹೊಸಪೇಟೆ"],
        "famous_for_kn": "ಹಂಪಿ UNESCO ಸ್ಮಾರಕ, ವಿಜಯನಗರ ಸಾಮ್ರಾಜ್ಯ",
        "famous_for_en": "Hampi UNESCO World Heritage, Vijayanagara kingdom history",
        "pin_codes": ["583201", "583227", "583136"],
        "key_mlas": ["ಆನಂದ್ ಸಿಂಹ (ಹೊಸಪೇಟೆ)"],
        "lat": 15.1720, "lon": 76.4560,
        "seo_keywords": "Vijayanagara district, ವಿಜಯನಗರ ಜಿಲ್ಲೆ, Hampi Hosapete, Vijayanagara MLA DC",
    },
    {
        "key": "chikkaballapura",
        "name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
        "name_en": "Chikkaballapura",
        "hq_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
        "hq_en": "Chikkaballapura",
        "region": "South Karnataka",
        "population": "12,55,104",
        "area_km2": "4,218",
        "taluks_kn": ["ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "ಗೌರಿಬಿದನೂರ", "ಶಿಡ್ಲಘಟ್ಟ", "ಚಿಂತಾಮಣಿ", "ಬಾಗೇಪಲ್ಲಿ", "ಗುಡಿಬಂಡೆ"],
        "taluks_en": ["Chikkaballapura", "Gauribidanur", "Shidlaghatta", "Chintamani", "Bagepalli", "Gudibanda"],
        "assembly_seats": 6,
        "lok_sabha": "Chikkaballapura",
        "dc_name": "ಶ್ರೀ ರಾಹುಲ್ ಶ್ರೀ (IAS)",
        "sp_name": "ಶ್ರೀ ಚಂದ್ರಕಾಂತ (IPS)",
        "dc_phone": "08156-275001",
        "sp_phone": "08156-275100",
        "nearest_dam": "ಶಿರಾ ಜಲಾಶಯ",
        "apmc_markets": ["ಚಿಂತಾಮಣಿ", "ಶಿಡ್ಲಘಟ್ಟ"],
        "famous_for_kn": "ರೇಷ್ಮೆ, ಟೊಮ್ಯಾಟೋ, ಗ್ರೇಹೌಂಡ್ ರೇಸಿಂಗ್",
        "famous_for_en": "Silk cocoons, Tomato, Shidlaghatta silk market",
        "pin_codes": ["562101", "562104", "562201"],
        "key_mlas": ["ಡಾ. ಕೆ. ಸುಧಾಕರ್ (ಚಿಕ್ಕಬಳ್ಳಾಪುರ)"],
        "lat": 13.4356, "lon": 77.7310,
        "seo_keywords": "Chikkaballapura district, ಚಿಕ್ಕಬಳ್ಳಾಪುರ ಜಿಲ್ಲೆ, Chikkaballapura MLA DC SP, silk Karnataka",
    },
    {
        "key": "kolar",
        "name_kn": "ಕೋಲಾರ",
        "name_en": "Kolar",
        "hq_kn": "ಕೋಲಾರ",
        "hq_en": "Kolar",
        "region": "South Karnataka",
        "population": "15,36,401",
        "area_km2": "8,223",
        "taluks_kn": ["ಕೋಲಾರ", "ಮುಳಬಾಗಿಲು", "ಮಾಲೂರು", "ಬಂಗಾರಪೇಟೆ", "ಶ್ರೀನಿವಾಸಪುರ"],
        "taluks_en": ["Kolar", "Mulbagal", "Malur", "Bangarpet", "Srinivaspur"],
        "assembly_seats": 5,
        "lok_sabha": "Kolar",
        "dc_name": "ಶ್ರೀ ಅಕ್ಷಯ್ ಶ್ರೀಧರ (IAS)",
        "sp_name": "ಶ್ರೀ ಸಿ.ಬಿ. ರಿಶಿಕಾಂತ (IPS)",
        "dc_phone": "08152-222226",
        "sp_phone": "08152-222344",
        "nearest_dam": "ಹೊಳೆ ನರಸೀಪುರ ಜಲಾಶಯ",
        "apmc_markets": ["ಕೋಲಾರ", "ಬಂಗಾರಪೇಟೆ"],
        "famous_for_kn": "KGF ಚಿನ್ನದ ಗಣಿ, ಟೊಮ್ಯಾಟೋ, ರೇಷ್ಮೆ",
        "famous_for_en": "Kolar Gold Fields (KGF), Tomato, Silk",
        "pin_codes": ["563101", "563103", "563122"],
        "key_mlas": ["ಶ್ರೀನಿವಾಸ ಗೌಡ (ಮಾಲೂರು)"],
        "lat": 13.1363, "lon": 78.1294,
        "seo_keywords": "Kolar district, ಕೋಲಾರ ಜಿಲ್ಲೆ, KGF gold mines, Kolar MLA DC SP, tomato price Karnataka",
    },
    {
        "key": "ramanagara",
        "name_kn": "ರಾಮನಗರ",
        "name_en": "Ramanagara",
        "hq_kn": "ರಾಮನಗರ",
        "hq_en": "Ramanagara",
        "region": "South Karnataka",
        "population": "10,82,739",
        "area_km2": "3,556",
        "taluks_kn": ["ರಾಮನಗರ", "ಕನಕಪುರ", "ಮಾಗಡಿ", "ಚನ್ನಪಟ್ಟಣ"],
        "taluks_en": ["Ramanagara", "Kanakapura", "Magadi", "Channapatna"],
        "assembly_seats": 4,
        "lok_sabha": "Bengaluru Rural",
        "dc_name": "ಶ್ರೀ ಆರ್. ಲತ (IAS)",
        "sp_name": "ಶ್ರೀ ಸಿ.ಕೆ. ಬಾಬು (IPS)",
        "dc_phone": "080-27273050",
        "sp_phone": "080-27273100",
        "nearest_dam": "ಆರ್ಕಾವತಿ ಜಲಾಶಯ",
        "apmc_markets": ["ರಾಮನಗರ", "ಕನಕಪುರ"],
        "famous_for_kn": "ಶೋಲೆ ಚಲನಚಿತ್ರ ತಾಣ, ರೇಷ್ಮೆ, ಗೊಂಬೆ ತಯಾರಿಕೆ",
        "famous_for_en": "Sholay filming location, Silk, Channapatna toys",
        "pin_codes": ["562159", "562112", "562130"],
        "key_mlas": ["ಇಕ್ಬಾಲ್ ಹುಸೇನ್ (ಕನಕಪುರ)"],
        "lat": 12.7156, "lon": 77.2817,
        "seo_keywords": "Ramanagara district, ರಾಮನಗರ ಜಿಲ್ಲೆ, Sholay location, Channapatna toys, Ramanagara MLA DC",
    },
    {
        "key": "chamarajanagara",
        "name_kn": "ಚಾಮರಾಜನಗರ",
        "name_en": "Chamarajanagara",
        "hq_kn": "ಚಾಮರಾಜನಗರ",
        "hq_en": "Chamarajanagara",
        "region": "South Karnataka",
        "population": "10,20,791",
        "area_km2": "5,101",
        "taluks_kn": ["ಚಾಮರಾಜನಗರ", "ಗುಂಡ್ಲುಪೇಟೆ", "ಕೊಳ್ಳೇಗಾಲ", "ಯಳಂದೂರು"],
        "taluks_en": ["Chamarajanagara", "Gundlupete", "Kollegal", "Yelandur"],
        "assembly_seats": 4,
        "lok_sabha": "Mysuru-Kodagu",
        "dc_name": "ಶ್ರೀ ಶಿಲ್ಪ ನಾಗ (IAS)",
        "sp_name": "ಶ್ರೀ ಪಿ.ಎಸ್. ಹರ್ಷ (IPS)",
        "dc_phone": "08226-222200",
        "sp_phone": "08226-222300",
        "nearest_dam": "ಕಬಿನಿ ಅಣೆಕಟ್ಟು",
        "apmc_markets": ["ಚಾಮರಾಜನಗರ", "ಕೊಳ್ಳೇಗಾಲ"],
        "famous_for_kn": "ಬಿಳಿಗಿರಿ ರಂಗನ ಬೆಟ್ಟ, ಕಾಡು ಆನೆ, ಮಲೆ ಮಹದೇಶ್ವರ",
        "famous_for_en": "BR Hills, Wildlife sanctuary, Mahadeshwara Hills",
        "pin_codes": ["571313", "571301", "571440"],
        "key_mlas": ["ಸಿ.ಪಿ. ಯೋಗೇಶ್ವರ (ಚಾಮರಾಜನಗರ)"],
        "lat": 11.9261, "lon": 76.9439,
        "seo_keywords": "Chamarajanagara district, ಚಾಮರಾಜನಗರ ಜಿಲ್ಲೆ, BR Hills, wildlife Karnataka, Chamarajanagara MLA DC",
    },
]

# ─── HTML template generator ──────────────────────────────────
def generate_page(d: dict) -> str:
    taluks_kn_str = " · ".join(d["taluks_kn"])
    taluks_en_str = ", ".join(d["taluks_en"])
    mlas_str = "".join([f"""
        <div class="mla-item">
          <div class="mla-icon">🏛️</div>
          <div class="mla-name">{m}</div>
        </div>""" for m in d["key_mlas"]])

    return f"""<!DOCTYPE html>
<html lang="kn">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d['name_kn']} ಜಿಲ್ಲೆ — MLA, MP, DC, SP, ಅಣೆಕಟ್ಟು, APMC | ಕರ್ನಾಟ</title>
<meta name="description" content="{d['name_kn']} ಜಿಲ್ಲೆ ಮಾಹಿತಿ. {d['name_en']} district MLA, MP, DC, SP contacts. Dam levels, APMC prices, government schemes. {d['seo_keywords']}.">
<meta name="keywords" content="{d['seo_keywords']}">
<meta property="og:title" content="{d['name_kn']} ಜಿಲ್ಲೆ — ಸಂಪೂರ್ಣ ಮಾಹಿತಿ">
<meta property="og:description" content="{d['name_kn']} ಜಿಲ್ಲೆಯ MLA, MP, DC, SP ಮತ್ತು ಸ್ಥಳೀಯ ಮಾಹಿತಿ">
<meta property="og:type" content="article">
<link rel="canonical" href="https://karnata.in/district/{d['key']}">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "AdministrativeArea",
  "name": "{d['name_en']} District",
  "alternateName": "{d['name_kn']} ಜಿಲ್ಲೆ",
  "containedInPlace": {{ "@type": "State", "name": "Karnataka", "containedInPlace": {{ "@type": "Country", "name": "India" }} }},
  "description": "{d['famous_for_en']}",
  "url": "https://karnata.in/district/{d['key']}"
}}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Kannada:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--red:#C0392B;--red-lt:#FDECEA;--green:#1B7A4B;--green-lt:#E8F5EE;--blue:#1A5276;--blue-lt:#EAF2F8;--amber:#E67E22;--amber-lt:#FEF5EC;--gold:#D4A017;--gold-lt:#FDF8E7;--ink:#1A1A2E;--ink2:#4A4A6A;--ink3:#8888AA;--bg:#F5F4F0;--white:#FFF;--border:#E3E1DB;--font-kn:'Noto Sans Kannada',sans-serif;--font-en:'Inter',sans-serif;--radius:12px;--shadow:0 2px 12px rgba(0,0,0,0.08);}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:var(--font-kn);background:var(--bg);color:var(--ink);-webkit-font-smoothing:antialiased;}}
a{{color:inherit;text-decoration:none;}}
button{{cursor:pointer;font-family:inherit;border:none;outline:none;}}
.topnav{{background:var(--white);border-bottom:1px solid var(--border);padding:0 20px;display:flex;align-items:center;gap:12px;height:56px;position:sticky;top:0;z-index:50;box-shadow:0 1px 6px rgba(0,0,0,0.06);}}
.back-btn{{display:flex;align-items:center;gap:6px;color:var(--ink2);font-size:13px;font-weight:500;background:var(--bg);border-radius:7px;padding:6px 12px;border:1px solid var(--border);}}
.breadcrumb{{font-size:12px;color:var(--ink3);font-family:var(--font-en);margin-left:auto;}}
.hero{{background:linear-gradient(135deg,#1A1A2E 0%,var(--red) 100%);color:#fff;padding:28px 20px;}}
.hero-inner{{max-width:900px;margin:0 auto;}}
.hero-kn{{font-size:28px;font-weight:700;margin-bottom:4px;}}
.hero-en{{font-size:15px;opacity:0.7;margin-bottom:12px;font-family:var(--font-en);}}
.hero-chips{{display:flex;gap:8px;flex-wrap:wrap;}}
.chip{{background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.25);border-radius:20px;padding:4px 12px;font-size:12px;color:rgba(255,255,255,0.9);}}
.wrap{{max-width:900px;margin:0 auto;padding:20px;}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:20px;}}
@media(max-width:600px){{.grid{{grid-template-columns:1fr;}}}}
.card{{background:var(--white);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow);}}
.card-head{{padding:13px 16px;border-bottom:1px solid var(--border);font-size:14px;font-weight:700;display:flex;align-items:center;gap:8px;}}
.card-body{{padding:14px 16px;}}
.info-row{{display:flex;justify-content:space-between;align-items:flex-start;padding:8px 0;border-bottom:1px solid var(--border);font-size:13px;}}
.info-row:last-child{{border-bottom:none;}}
.ir-label{{color:var(--ink3);font-family:var(--font-en);font-size:12px;}}
.ir-value{{color:var(--ink);font-weight:500;text-align:right;max-width:60%;}}
.officer-card{{display:flex;align-items:flex-start;gap:12px;padding:10px 0;border-bottom:1px solid var(--border);}}
.officer-card:last-child{{border-bottom:none;}}
.officer-icon{{width:36px;height:36px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:16px;flex-shrink:0;}}
.officer-name{{font-size:13px;font-weight:600;color:var(--ink);}}
.officer-role{{font-size:11px;color:var(--ink3);font-family:var(--font-en);margin-bottom:4px;}}
.officer-phone{{font-size:12px;color:var(--blue);font-family:var(--font-en);display:flex;align-items:center;gap:4px;}}
.mla-item{{display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid var(--border);}}
.mla-item:last-child{{border-bottom:none;}}
.mla-icon{{font-size:18px;}}
.mla-name{{font-size:13px;color:var(--ink);}}
.taluk-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:6px;margin-top:10px;}}
.taluk-chip{{background:var(--bg);border:1px solid var(--border);border-radius:7px;padding:7px 10px;font-size:12px;text-align:center;color:var(--ink2);}}
.quick-links{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:8px;margin-bottom:20px;}}
.ql-btn{{background:var(--white);border:1px solid var(--border);border-radius:var(--radius);padding:14px;text-align:center;cursor:pointer;transition:all 0.15s;text-decoration:none;display:block;}}
.ql-btn:hover{{border-color:var(--red);background:var(--red-lt);}}
.ql-icon{{font-size:22px;margin-bottom:6px;}}
.ql-label{{font-size:12px;font-weight:500;color:var(--ink2);}}
.district-nav{{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:20px;}}
.dn-btn{{padding:6px 12px;border-radius:20px;font-size:11px;border:1px solid var(--border);background:var(--white);color:var(--ink2);cursor:pointer;font-family:var(--font-kn);transition:all 0.15s;}}
.dn-btn:hover{{background:var(--red);color:#fff;border-color:var(--red);}}
</style>
</head>
<body>
<div class="topnav">
  <a href="../index.html" class="back-btn">← ಕರ್ನಾಟ</a>
  <div style="font-size:14px;font-weight:700;">{d['name_kn']} ಜಿಲ್ಲೆ</div>
  <div class="breadcrumb">Districts › {d['name_en']}</div>
</div>
<div class="hero">
  <div class="hero-inner">
    <div class="hero-kn">🗺️ {d['name_kn']} ಜಿಲ್ಲೆ</div>
    <div class="hero-en">{d['name_en']} District · {d['region']} · Karnataka</div>
    <div class="hero-chips">
      <span class="chip">🏢 ಜಿಲ್ಲಾ ಕೇಂದ್ರ: {d['hq_kn']}</span>
      <span class="chip">👥 ಜನಸಂಖ್ಯೆ: {d['population']}</span>
      <span class="chip">📐 ವಿಸ್ತೀರ್ಣ: {d['area_km2']} km²</span>
      <span class="chip">🗳️ {d['assembly_seats']} ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ</span>
    </div>
  </div>
</div>
<div class="wrap">

  <!-- Quick tool links -->
  <div class="quick-links">
    <a href="../civic-finder.html" class="ql-btn"><div class="ql-icon">🏛️</div><div class="ql-label">MLA / MP ಹುಡುಕಿ</div></a>
    <a href="../dam-levels.html" class="ql-btn"><div class="ql-icon">💧</div><div class="ql-label">ಅಣೆಕಟ್ಟು ಮಟ್ಟ</div></a>
    <a href="../more-tools.html" class="ql-btn"><div class="ql-icon">🌾</div><div class="ql-label">APMC ಬೆಲೆ</div></a>
    <a href="../gold-rate.html" class="ql-btn"><div class="ql-icon">🥇</div><div class="ql-label">ಚಿನ್ನ ಬೆಲೆ</div></a>
    <a href="../status-checker.html" class="ql-btn"><div class="ql-icon">📋</div><div class="ql-label">ಸ್ಥಿತಿ ತಪಾಸಣೆ</div></a>
    <a href="../emi-calculator.html" class="ql-btn"><div class="ql-icon">🏦</div><div class="ql-label">EMI ಲೆಕ್ಕ</div></a>
  </div>

  <div class="grid">
    <!-- District info -->
    <div class="card">
      <div class="card-head">📊 ಜಿಲ್ಲಾ ಮಾಹಿತಿ</div>
      <div class="card-body">
        <div class="info-row"><span class="ir-label">District HQ</span><span class="ir-value">{d['hq_kn']} ({d['hq_en']})</span></div>
        <div class="info-row"><span class="ir-label">Region</span><span class="ir-value">{d['region']}</span></div>
        <div class="info-row"><span class="ir-label">Lok Sabha</span><span class="ir-value">{d['lok_sabha']}</span></div>
        <div class="info-row"><span class="ir-label">Assembly Seats</span><span class="ir-value">{d['assembly_seats']}</span></div>
        <div class="info-row"><span class="ir-label">Population</span><span class="ir-value">{d['population']}</span></div>
        <div class="info-row"><span class="ir-label">Area</span><span class="ir-value">{d['area_km2']} km²</span></div>
        <div class="info-row"><span class="ir-label">ಪ್ರಸಿದ್ಧ</span><span class="ir-value">{d['famous_for_kn']}</span></div>
      </div>
    </div>

    <!-- Officers -->
    <div class="card">
      <div class="card-head">🏛️ ಜಿಲ್ಲಾ ಅಧಿಕಾರಿಗಳು</div>
      <div class="card-body">
        <div class="officer-card">
          <div class="officer-icon" style="background:var(--green-lt)">👔</div>
          <div>
            <div class="officer-role">DC · Deputy Commissioner</div>
            <div class="officer-name">{d['dc_name']}</div>
            <a class="officer-phone" href="tel:{d['dc_phone']}">📞 {d['dc_phone']}</a>
          </div>
        </div>
        <div class="officer-card">
          <div class="officer-icon" style="background:var(--blue-lt)">👮</div>
          <div>
            <div class="officer-role">SP · Superintendent of Police</div>
            <div class="officer-name">{d['sp_name']}</div>
            <a class="officer-phone" href="tel:{d['sp_phone']}">📞 {d['sp_phone']}</a>
          </div>
        </div>
        <div class="officer-card">
          <div class="officer-icon" style="background:var(--gold-lt)">🏥</div>
          <div>
            <div class="officer-role">DHO · District Health Officer</div>
            <div class="officer-name">ಜಿಲ್ಲಾ ಆರೋಗ್ಯ ಅಧಿಕಾರಿ</div>
            <a href="../status-checker.html" style="font-size:12px;color:var(--blue)">ಸಂಪರ್ಕ ಹುಡುಕಿ →</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- MLAs -->
  <div class="card" style="margin-bottom:16px;">
    <div class="card-head">🗳️ ವಿಧಾನಸಭಾ ಸದಸ್ಯರು (MLA)</div>
    <div class="card-body">
      {mlas_str}
      <a href="../civic-finder.html" style="display:block;margin-top:12px;text-align:center;background:var(--red);color:#fff;border-radius:8px;padding:10px;font-size:13px;font-weight:700;">🔍 ನಿಮ್ಮ MLA ಹೆಸರು ಹುಡುಕಿ →</a>
    </div>
  </div>

  <div class="grid">
    <!-- Dam -->
    <div class="card">
      <div class="card-head">💧 ಸ್ಥಳೀಯ ಅಣೆಕಟ್ಟು</div>
      <div class="card-body">
        <div style="font-size:14px;font-weight:600;color:var(--blue);margin-bottom:8px;">{d['nearest_dam']}</div>
        <div style="font-size:13px;color:var(--ink2);margin-bottom:12px;">ಇಂದಿನ ನೀರಿನ ಮಟ್ಟ ನೋಡಲು:</div>
        <a href="../dam-levels.html" style="display:block;background:var(--blue);color:#fff;border-radius:8px;padding:10px;text-align:center;font-size:13px;font-weight:700;">💧 Live Dam Level ನೋಡಿ →</a>
      </div>
    </div>

    <!-- APMC -->
    <div class="card">
      <div class="card-head">🌾 APMC ಮಾರುಕಟ್ಟೆ</div>
      <div class="card-body">
        <div style="margin-bottom:10px;">{"".join([f'<span style="display:inline-block;margin:2px;background:var(--green-lt);color:var(--green);border-radius:5px;padding:3px 8px;font-size:12px;">{m}</span>' for m in d['apmc_markets']])}</div>
        <a href="../more-tools.html" style="display:block;background:var(--green);color:#fff;border-radius:8px;padding:10px;text-align:center;font-size:13px;font-weight:700;">🌾 ಇಂದಿನ ಬೆಲೆ ನೋಡಿ →</a>
      </div>
    </div>
  </div>

  <!-- Taluks -->
  <div class="card" style="margin-bottom:16px;">
    <div class="card-head">🏘️ ತಾಲ್ಲೂಕುಗಳು ({len(d['taluks_kn'])} ತಾಲ್ಲೂಕು)</div>
    <div class="card-body">
      <div class="taluk-grid">
        {"".join([f'<div class="taluk-chip">{t}</div>' for t in d['taluks_kn']])}
      </div>
    </div>
  </div>

  <!-- Useful links -->
  <div class="card" style="margin-bottom:20px;">
    <div class="card-head">🔗 ಉಪಯುಕ್ತ ಸೇವೆಗಳು</div>
    <div class="card-body">
      <div class="taluk-grid" style="grid-template-columns:repeat(auto-fill,minmax(140px,1fr));">
        <a href="../status-checker.html" style="background:var(--bg);border:1px solid var(--border);border-radius:7px;padding:10px;text-align:center;font-size:12px;color:var(--ink2);display:block;">🚗 DL ಸ್ಥಿತಿ</a>
        <a href="../status-checker.html" style="background:var(--bg);border:1px solid var(--border);border-radius:7px;padding:10px;text-align:center;font-size:12px;color:var(--ink2);display:block;">🏡 RTC / ಪಹಣಿ</a>
        <a href="../more-tools.html" style="background:var(--bg);border:1px solid var(--border);border-radius:7px;padding:10px;text-align:center;font-size:12px;color:var(--ink2);display:block;">📋 ಯೋಜನೆ ಅರ್ಹತೆ</a>
        <a href="../civic-finder.html" style="background:var(--bg);border:1px solid var(--border);border-radius:7px;padding:10px;text-align:center;font-size:12px;color:var(--ink2);display:block;">🏛️ GP ಸದಸ್ಯ</a>
        <a href="../emi-calculator.html" style="background:var(--bg);border:1px solid var(--border);border-radius:7px;padding:10px;text-align:center;font-size:12px;color:var(--ink2);display:block;">🏦 EMI ಲೆಕ್ಕ</a>
        <a href="../karnataka-local-news.html" style="background:var(--bg);border:1px solid var(--border);border-radius:7px;padding:10px;text-align:center;font-size:12px;color:var(--ink2);display:block;">📰 ಜಿಲ್ಲಾ ಸುದ್ದಿ</a>
      </div>
    </div>
  </div>

  <!-- 📰 DISTRICT LOCAL NEWS SECTION -->
  <div class="card" style="margin-bottom:20px;">
    <div class="card-head" style="display:flex; justify-content:space-between; align-items:center;">
      <span>📰 {d['name_kn']} ಇಂದಿನ ತಾಜಾ ಸುದ್ದಿ ಮತ್ತು ಬೆಳವಣಿಗೆಗಳು</span>
      <span style="font-size:11px; font-weight:600; background:var(--red-lt); color:var(--red); padding:3px 8px; border-radius:12px;">ಪ್ರತಿ 3 ಗಂಟೆಗೆ ನವೀಕರಣ</span>
    </div>
    <div class="card-body">
      <div id="district-news-list">
        <div style="text-align:center; padding:20px; color:var(--ink2);">ಸುದ್ದಿ ಲೋಡ್ ಆಗುತ್ತಿದೆ...</div>
      </div>
    </div>
  </div>

  <!-- Other districts -->
  <div style="font-size:13px;font-weight:700;margin-bottom:10px;color:var(--ink2);">🗺️ ಇತರ ಜಿಲ್ಲೆಗಳು</div>
  <div class="district-nav" id="dist-nav"></div>

</div>

<script src="../data-loader.js"></script>
<script>
async function loadDistrictLocalNews() {{
  const distKey = "{d['key']}";
  const container = document.getElementById('district-news-list');
  try {{
    let data = await NK.local_news();
    if (data && data.payload && typeof window.decryptPayload === 'function') {{
      data = window.decryptPayload(data.payload);
    }}
    const buckets = (data && (data.district_buckets || data.news)) || {{}};
    let articles = buckets[distKey] || buckets[distKey.replace('-', '_')] || buckets[distKey.replace('_', '-')] || [];
    if (!articles.length) {{
      Object.keys(buckets).forEach(k => {{
        if (k.includes(distKey) || distKey.includes(k)) articles.push(...buckets[k]);
      }});
    }}
    function cleanTitle(raw) {{
      if (!raw) return "";
      let s = String(raw).trim();
      s = s.replace(/<[^>]+>/g, "");
      const catIdx = s.search(/\s+(?:[A-Za-z'\s]+News|[A-Za-z'\s]+Update|[A-Za-z'\s]+Environment|[A-Za-z'\s]+Report|Politics|India News|Crop damage|Literature News|Local News|Power Cut)\s*:\s*/i);
      if (catIdx !== -1) s = s.substring(0, catIdx).trim();
      s = s.replace(/\s*Last\s*Updated.*$/i, "");
      s = s.replace(/\s*[-–—|:]+$/g, "");
      s = s.trim();
      if (s.length < 15) return "";
      return s;
    }}

    const validArticles = articles.filter(a => cleanTitle(a.title).length >= 15);

    if (validArticles.length === 0) {{
      container.innerHTML = '<div style="text-align:center; padding:20px; color:var(--ink2);">{d['name_kn']} ಜಿಲ್ಲೆಯ ಇತ್ತೀಚಿನ ಸುದ್ದಿಗಳು ಅಪ್‌ಡೇಟ್ ಆಗುತ್ತಿವೆ...</div>';
      return;
    }}

    container.innerHTML = validArticles.slice(0, 10).map(a => {{
      let title = cleanTitle(a.title);
      return `
        <div style="background:var(--bg); border:1px solid var(--border); border-radius:10px; padding:14px; margin-bottom:12px;">
          <a href="` + (a.url || a.link || '#') + `" target="_blank" style="font-size:15px; font-weight:800; color:var(--ink1); text-decoration:none; display:block; margin-bottom:6px; line-height:1.4;">` + title + `</a>
          <div style="font-size:11px; font-weight:600; color:var(--ink2);">⏱️ ` + (a.published ? a.published.split('T')[0] : 'ಇಂದು') + `</div>
        </div>
      `;
    }}).join('');
  }} catch (e) {{
    console.error("Error loading district news:", e);
  }}
}}
loadDistrictLocalNews();

const districts = [
  {{'key':'bengaluru-urban','kn':'ಬೆಂಗಳೂರು ನಗರ'}},{{'key':'bengaluru-rural','kn':'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ'}},
  {{'key':'mysuru','kn':'ಮೈಸೂರು'}},{{'key':'mandya','kn':'ಮಂಡ್ಯ'}},{{'key':'hassan','kn':'ಹಾಸನ'}},
  {{'key':'kodagu','kn':'ಕೊಡಗು'}},{{'key':'dakshina-kannada','kn':'ದಕ್ಷಿಣ ಕನ್ನಡ'}},{{'key':'udupi','kn':'ಉಡುಪಿ'}},
  {{'key':'shivamogga','kn':'ಶಿವಮೊಗ್ಗ'}},{{'key':'chikkamagaluru','kn':'ಚಿಕ್ಕಮಗಳೂರು'}},
  {{'key':'tumakuru','kn':'ತುಮಕೂರು'}},{{'key':'chitradurga','kn':'ಚಿತ್ರದುರ್ಗ'}},
  {{'key':'davanagere','kn':'ದಾವಣಗೆರೆ'}},{{'key':'belagavi','kn':'ಬೆಳಗಾವಿ'}},
  {{'key':'dharwad','kn':'ಧಾರವಾಡ'}},{{'key':'gadag','kn':'ಗದಗ'}},{{'key':'haveri','kn':'ಹಾವೇರಿ'}},
  {{'key':'uttara-kannada','kn':'ಉತ್ತರ ಕನ್ನಡ'}},{{'key':'bagalkote','kn':'ಬಾಗಲಕೋಟೆ'}},
  {{'key':'vijayapura','kn':'ವಿಜಯಪುರ'}},{{'key':'kalaburagi','kn':'ಕಲಬುರಗಿ'}},
  {{'key':'yadgir','kn':'ಯಾದಗಿರಿ'}},{{'key':'raichur','kn':'ರಾಯಚೂರು'}},{{'key':'koppal','kn':'ಕೊಪ್ಪಳ'}},
  {{'key':'ballari','kn':'ಬಳ್ಳಾರಿ'}},{{'key':'vijayanagara','kn':'ವಿಜಯನಗರ'}},
  {{'key':'chikkaballapura','kn':'ಚಿಕ್ಕಬಳ್ಳಾಪುರ'}},{{'key':'kolar','kn':'ಕೋಲಾರ'}},
  {{'key':'ramanagara','kn':'ರಾಮನಗರ'}},{{'key':'chamarajanagara','kn':'ಚಾಮರಾಜನಗರ'}},
];
const current = '{d['key']}';
document.getElementById('dist-nav').innerHTML = districts
  .filter(d => d.key !== current)
  .map(d => `<a href="${{d.key}}.html" class="dn-btn">${{d.kn}}</a>`)
  .join('');
</script>
</body>
</html>"""

# ─── Generate all pages ───────────────────────────────────────
if __name__ == "__main__":
    print(f"Generating {len(DISTRICTS)} Karnataka district pages")
    print("=" * 50)
    for d in DISTRICTS:
        html = generate_page(d)
        path = OUT / f"{d['key']}.html"
        path.write_text(html, encoding="utf-8")
        print(f"Generated {d['key']}.html")

    print("=" * 50)
    print(f"Done! {len(DISTRICTS)} pages generated.")
    print("\nPage sizes:")
    total = 0
    for f in sorted(OUT.glob("*.html")):
        sz = f.stat().st_size
        total += sz
        print(f"   {f.name}: {sz:,} bytes")
    print(f"\n   Total: {total:,} bytes ({total/1024:.0f} KB)")
    print("SEO targets generated successfully.")
