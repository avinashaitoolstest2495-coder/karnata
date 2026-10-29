import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('petrol-price.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if 'hero-petrol' in l or 'hero-diesel' in l or 'hero-detected-loc' in l:
        print(f"{i+1}: {l.strip()[:140]}")
