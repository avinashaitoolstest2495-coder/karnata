import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('_worker.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'captcha id and value are required' in l.lower():
        for j in range(max(0, i-40), min(len(lines), i+30)):
            print(f"{j+1}: {lines[j]}", end='')
        break
