import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('sip-calculator.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if 'table-body' in l.lower() or 'rendersip' in l.lower() or 'growth-table' in l.lower() or 'calculatesip' in l.lower() or 'function calculate' in l.lower():
        print(f"{i+1}: {l.strip()[:100]}")
