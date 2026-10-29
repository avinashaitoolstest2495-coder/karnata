import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/panchatantra/panchatantra_master.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

gps = master['gram_panchayats']
for k, v in gps[0].items():
    print(f"  {k}: {v}")
