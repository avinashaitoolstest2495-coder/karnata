import os
import glob
import json

index_path = os.path.join('data', 'sir_voter_rolls', 'index.json')
with open(index_path, 'r', encoding='utf-8') as f:
    idx = json.load(f)

print('Index Status: OK')
print(f"Districts: {len(idx['districts'])}")
print(f"Constituencies: {len(idx['constituencies'])}")

files = glob.glob(os.path.join('data', 'sir_voter_rolls', 'ac_*.json'))
print(f"Total AC files: {len(files)}")

corrupted = 0
total_parts = 0
for file in files:
    try:
        with open(file, 'r', encoding='utf-8') as f:
            d = json.load(f)
            total_parts += len(d.get('parts', []))
    except Exception as e:
        print(f"Corrupted file {file}: {e}")
        corrupted += 1

print(f"Verification Results: {len(files)} files checked. Corrupted: {corrupted}. Total verified parts: {total_parts}")
