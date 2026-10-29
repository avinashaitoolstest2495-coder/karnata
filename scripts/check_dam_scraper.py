import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scraper/dam_scraper.py', 'r', encoding='utf-8') as f:
    print(f.read()[:2000])
