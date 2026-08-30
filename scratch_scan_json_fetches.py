import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
js_files = [f for f in os.listdir('.') if f.endswith('.js')]
all_files = html_files + js_files

fetches = {}
for hf in all_files:
    try:
        with open(hf, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        found = re.findall(r'[\'\"`]([^\'\"`]+\.json)[\'\"`]', c)
        if found:
            fetches[hf] = list(set(found))
    except Exception as e:
        pass

print("=== JSON FILES REFERENCED IN HTML & JS ===")
missing_files = set()
for hf, jsons in sorted(fetches.items()):
    print(f"\n{hf}:")
    for j in jsons:
        # Strip query params like ?v=123
        j_base = j.split('?')[0].lstrip('./')
        p1 = j_base
        p2 = os.path.join('data', j_base)
        p3 = os.path.join('data', os.path.basename(j_base))
        
        exists = False
        actual_path = None
        for p in [p1, p2, p3]:
            if os.path.exists(p) and os.path.isfile(p):
                exists = True
                actual_path = p
                break
        
        if exists:
            size = os.path.getsize(actual_path)
            print(f"   [OK] {j} -> found at {actual_path} ({size} bytes)")
        else:
            print(f"   [MISSING] {j} -> NOT FOUND ANYWHERE!")
            missing_files.add(j_base)

print("\n=== SUMMARY OF MISSING JSON FILES ===")
for m in sorted(missing_files):
    print(f" - {m}")
