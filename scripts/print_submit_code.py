import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('karnataka-sir-voter-roll.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1420, 1445):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')
