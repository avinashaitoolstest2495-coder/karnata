import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('dam-levels.html', 'r', encoding='utf-8') as f:
    text = f.read()

for k in ['krs', 'bhadra', 'malaprabha']:
    m = re.search(r'<tr data-dam-key="' + k + r'">([\s\S]*?)</tr>', text)
    if m:
        print(f"=== {k} ===")
        for line in m.group(0).splitlines():
            if 'tbl-storage-cell' in line or 'tbl-flow-cell' in line:
                print(" ", line.strip())
