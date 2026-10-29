import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('karnataka-sir-voter-roll.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, l in enumerate(lines):
    if 'captcha' in l.lower():
        print(f"{i+1}: {l.strip()[:140]}")
