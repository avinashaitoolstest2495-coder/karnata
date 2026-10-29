import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('apmc-prices.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, line in enumerate(lines):
    if '<tbody' in line.lower() or '10-' in line.lower() or '10 ವರ್ಷ' in line or '10 year' in line.lower() or 'historical' in line.lower():
        print(f"{i+1}: {line.strip()[:140]}")
