import json

# Load representatives catalog
with open('data/gis/representatives_catalog.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

# Kannada transliteration mappings for Rajya Sabha members
rs_kn_names = {
    "Mallikarjun Kharge": "ಮಲ್ಲಿಕಾರ್ಜುನ ಖರ್ಗೆ",
    "Mansoor Ali Khan": "ಮನ್ಸೂರ್ ಅಲಿ ಖಾನ್",
    "Pawan Khera": "ಪವನ್ ಖೇರಾ",
    "Syed Naseer Hussain": "ಸೈಯದ್ ನಾಸೀರ್ ಹುಸೇನ್",
    "Ajay Maken": "ಅಜಯ್ ಮಾಕೆನ್",
    "G. C. Chandrasekhar": "ಜಿ. ಸಿ. ಚಂದ್ರಶೇಖರ್",
    "Jairam Ramesh": "ಜೈರಾಮ್ ರಮೇಶ್",
    "M. Nagaraja": "ಎಂ. ನಾಗರಾಜ",
    "Narayana Bhandage": "ನಾರಾಯಣ ಭಾಂಡಗೆ",
    "Nirmala Sitharaman": "ನಿರ್ಮಲಾ ಸೀತಾರಾಮನ್",
    "Lehar Singh Siroya": "ಲೆಹರ್ ಸಿಂಗ್ ಸಿರೋಯಾ",
    "Jaggesh": "ಜಗ್ಗೇಶ್"
}

for k, v in catalog.get('rajya_sabha', {}).items():
    en_name = v.get('name_en', '')
    v['name_kn'] = rs_kn_names.get(en_name, en_name)
    v['mp_kn'] = v['name_kn']

# Kannada category names for MLCs
for k, v in catalog.get('mlcs', {}).items():
    cat = v.get('category', '')
    if 'ವಿಧಾನಸಭೆ' in cat or 'MLAs' in cat:
        v['category_clean'] = 'ವಿಧಾನಸಭೆ ಚುನಾಯಿತ'
    elif 'ಸ್ಥಳೀಯ' in cat or 'Local' in cat:
        v['category_clean'] = 'ಸ್ಥಳೀಯ ಸಂಸ್ಥೆ'
    elif 'ಪದವೀಧರ' in cat or 'Graduates' in cat:
        v['category_clean'] = 'ಪದವೀಧರ ಕ್ಷೇತ್ರ'
    elif 'ಶಿಕ್ಷಕರ' in cat or 'Teachers' in cat:
        v['category_clean'] = 'ಶಿಕ್ಷಕರ ಕ್ಷೇತ್ರ'
    elif 'ನಾಮನಿರ್ದೇಶನ' in cat or 'Nominated' in cat:
        v['category_clean'] = 'ನಾಮನಿರ್ದೇಶನ'
    else:
        v['category_clean'] = 'ವಿಧಾನ ಪರಿಷತ್'

with open('data/gis/representatives_catalog.json', 'w', encoding='utf-8') as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

print("SUCCESS_ENRICHED_CATALOG")
