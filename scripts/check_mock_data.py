import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scraper/generate_mock_data.py', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.splitlines():
    if 'krs' in line.lower() or 'dam' in line.lower() or '34' in line:
        print(line.strip()[:140])
