import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('gba.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, line in enumerate(lines):
    if 'wardtablebody' in line.lower() or 'renderwards' in line.lower() or 'corporationwards' in line.lower():
        print(f"{i+1}: {line.strip()[:140]}")
