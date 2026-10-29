import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data-loader.js', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.splitlines()[50:]:
    if 'window.' in line or 'export' in line or 'dams' in line:
        print(line[:140])
