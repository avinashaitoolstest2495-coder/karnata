import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('_worker.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'export default' in l or 'addEventListener' in l or 'async fetch(' in l:
        print(f"{i+1}: {l.strip()[:140]}")
