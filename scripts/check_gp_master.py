import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/panchatantra/panchatantra_master.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

print("Total GPs in master:", len(master))
sample = master[0]
print("Sample GP keys:", list(sample.keys()))
for k, v in sample.items():
    print(f"  {k}: {v}")
