import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('gba-central.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'wardtablebody' in line.lower():
        for j in range(max(0, i-5), min(len(lines), i+10)):
            print(f"{j+1}: {lines[j]}", end='')
        break
