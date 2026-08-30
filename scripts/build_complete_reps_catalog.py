import json
from bs4 import BeautifulSoup
import re

# 1. Parse Rajya Sabha Data
f_rs = r'C:\Users\avina\.gemini\antigravity\brain\eb992232-7e29-44eb-b019-891a87e05063\.system_generated\steps\2680\content.md'
with open(f_rs, 'r', encoding='utf-8') as f:
    soup_rs = BeautifulSoup(f.read(), 'html.parser')

rs_list = {}
for t in soup_rs.find_all('table'):
    rows = t.find_all('tr')
    if len(rows) >= 12:
        for idx, r in enumerate(rows[1:13]):
            cols = [c.get_text(strip=True) for c in r.find_all(['th', 'td'])]
            if len(cols) >= 5:
                num = idx + 1
                name = cols[1]
                party = cols[3] if len(cols) > 3 and cols[3] in ['INC', 'BJP', 'JD(S)', 'JDS'] else (cols[2] if cols[2] in ['INC', 'BJP', 'JD(S)', 'JDS'] else 'INC')
                term_start = cols[-2]
                term_end = cols[-1]
                
                party_kn = 'ಕಾಂಗ್ರೆಸ್' if party == 'INC' else ('ಬಿಜೆಪಿ' if party == 'BJP' else ('ಜೆಡಿಎಸ್' if 'JD' in party else party))
                
                rs_list[str(num)] = {
                    "code": num,
                    "name_en": name,
                    "name_kn": name,
                    "mp_en": name,
                    "mp_kn": name,
                    "party_en": party,
                    "party_kn": party_kn,
                    "district_en": "Karnataka (Rajya Sabha)",
                    "district_kn": "ಕರ್ನಾಟಕ (ರಾಜ್ಯಸಭೆ)",
                    "category": "Rajya Sabha",
                    "term": f"{term_start} to {term_end}",
                    "type": "rs"
                }
        if len(rs_list) == 12:
            break

print(f"Parsed {len(rs_list)} Rajya Sabha Members")

# 2. Parse MLC Data
f_mlc = r'C:\Users\avina\.gemini\antigravity\brain\eb992232-7e29-44eb-b019-891a87e05063\.system_generated\steps\2678\content.md'
with open(f_mlc, 'r', encoding='utf-8') as f:
    soup_mlc = BeautifulSoup(f.read(), 'html.parser')

tables_mlc = soup_mlc.find_all('table')
mlc_cats = [
    ('ವಿಧಾನಸಭೆಯಿಂದ ಚುನಾಯಿತ (Elected by MLAs)', tables_mlc[1]),
    ('ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳಿಂದ ಚುನಾಯಿತ (Local Authorities)', tables_mlc[2]),
    ('ಪದವೀಧರ ಕ್ಷೇತ್ರ (Graduates)', tables_mlc[3]),
    ('ಶಿಕ್ಷಕರ ಕ್ಷೇತ್ರ (Teachers)', tables_mlc[4]),
    ('ನಾಮನಿರ್ದೇಶನ (Nominated)', tables_mlc[5]),
]

mlc_list = {}
mlc_counter = 1

for cat_label, tbl in mlc_cats:
    rows = tbl.find_all('tr')[1:]
    for r in rows:
        cols = [c.get_text(strip=True) for c in r.find_all(['th', 'td'])]
        if len(cols) >= 3:
            # typical columns: [#, Member, Party, Term start, Term end] or [Constituency, Member, Party, ...]
            name = cols[1] if cols[0].isdigit() or cols[0].startswith('1') or cols[0].startswith('2') else (cols[1] if len(cols) > 1 else cols[0])
            const_name = cols[0] if not cols[0].isdigit() else (cat_label.split('(')[0].strip())
            party = 'INC'
            for c in cols:
                if c in ['INC', 'BJP', 'JD(S)', 'JDS', 'Ind.', 'Independent', 'IND']:
                    party = 'IND' if 'Ind' in c else c
                    break
                elif 'Congress' in c or 'INC' in c: party = 'INC'; break
                elif 'Bharatiya' in c or 'BJP' in c: party = 'BJP'; break
                elif 'Janata' in c or 'JD' in c: party = 'JD(S)'; break

            party_kn = 'ಕಾಂಗ್ರೆಸ್' if party == 'INC' else ('ಬಿಜೆಪಿ' if party == 'BJP' else ('ಜೆಡಿಎಸ್' if 'JD' in party else 'ಪಕ್ಷೇತರ'))
            
            mlc_list[str(mlc_counter)] = {
                "code": mlc_counter,
                "ac_name_en": const_name,
                "ac_name_kn": const_name,
                "name_en": name,
                "name_kn": name,
                "mla_name_en": name,
                "mla_name_kn": name,
                "party_en": party,
                "party_kn": party_kn,
                "district_en": "Karnataka (MLC)",
                "district_kn": "ಕರ್ನಾಟಕ ವಿಧಾನ ಪರಿಷತ್",
                "category": cat_label.split('(')[0].strip(),
                "constituency_type": cat_label,
                "type": "mlc"
            }
            mlc_counter += 1

print(f"Parsed {len(mlc_list)} MLCs")

# Load existing reps_catalog or district_representatives_catalog.json
catalog_path = 'data/district_representatives_catalog.json'
if not os.path.exists(catalog_path):
    catalog_path = 'data/reps_catalog.json'

with open(catalog_path, 'r', encoding='utf-8') as f:
    master_catalog = json.load(f)

master_catalog['mlcs'] = mlc_list
master_catalog['rajya_sabha'] = rs_list

with open('data/district_representatives_catalog.json', 'w', encoding='utf-8') as f:
    json.dump(master_catalog, f, ensure_ascii=False, indent=2)

print("SUCCESS_SAVED_REPRESENTATIVES_CATALOG")
