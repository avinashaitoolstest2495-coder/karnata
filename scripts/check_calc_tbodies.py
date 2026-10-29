import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for f in ['ai-jyothishya.html', 'emi-calculator.html', 'sip-calculator.html']:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    for m in re.finditer(r'<table[^>]*>[\s\S]*?<tbody([^>]*)>\s*</tbody>[\s\S]*?</table>', c):
        print(f"File: {f}")
        print("Table snippet:", m.group(0)[:300])
