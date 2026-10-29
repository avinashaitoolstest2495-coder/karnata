import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('karnataka-sir-voter-roll.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1390, 1420):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')
