import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('emi-calculator.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if 'input' in l.lower() or 'amort' in l.lower() or 'calcemi' in l.lower():
        if len(l.strip()) < 120:
            print(f"{i+1}: {l.strip()}")
