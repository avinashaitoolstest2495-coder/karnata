import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ai-jyothishya.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'planets-tbody' in l and i > 700:
        for j in range(max(0, i-5), min(len(lines), i+15)):
            print(f"{j+1}: {lines[j]}", end='')
        break
