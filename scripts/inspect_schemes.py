import json, sys
sys.stdout.reconfigure(encoding='utf-8')
with open('data/government_schemes.json', encoding='utf-8') as f:
    d = json.load(f)
schemes = d.get('schemes', [])
print(f"Total schemes: {len(schemes)}")
for i, s in enumerate(schemes):
    print(f"{i+1:02d}. [{s.get('scheme_type','?'):13s}] {s.get('id',''):35s} | {s.get('scheme_name_en','')}")
