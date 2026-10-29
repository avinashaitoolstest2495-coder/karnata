import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scraper/cloudflare_worker.js', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.splitlines():
    if 'captcha' in line.lower() or 'voter' in line.lower():
        print(line.strip()[:140])
