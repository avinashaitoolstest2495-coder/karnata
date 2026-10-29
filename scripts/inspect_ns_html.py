import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('nanna-sthala.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(480, 540):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')
