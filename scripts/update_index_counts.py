import os
import glob
import json

data_dir = os.path.join('data', 'sir_voter_rolls')
index_file = os.path.join(data_dir, 'index.json')

with open(index_file, 'r', encoding='utf-8') as f:
    idx = json.load(f)

ac_files = glob.glob(os.path.join(data_dir, 'ac_*.json'))
print(f"Total AC files found: {len(ac_files)}")

total_parts = 0
for fpath in sorted(ac_files):
    with open(fpath, 'r', encoding='utf-8') as f:
        ac_data = json.load(f)
        total_parts += len(ac_data.get('parts', []))

idx['total_verified_parts'] = total_parts
with open(index_file, 'w', encoding='utf-8') as f:
    json.dump(idx, f, ensure_ascii=False, indent=2)

print(f"Updated index.json! Total verified parts across Karnataka: {total_parts}")
