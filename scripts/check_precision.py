import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('functions/precision_data.js', 'r', encoding='utf-8') as f:
    text = f.read()

for l in text.splitlines():
    if 'krs' in l.lower() or '34' in l or 'storage_pct' in l:
        print(l[:140])
