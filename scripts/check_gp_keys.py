import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/panchatantra/panchatantra_master.json', 'r', encoding='utf-8') as f:
    master = json.load(f)

print("Master keys:", list(master.keys()))
for k in master:
    val = master[k]
    print(k, "type:", type(val), "len:", len(val) if hasattr(val, '__len__') else val)
