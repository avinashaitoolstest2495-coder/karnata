import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('dam-levels.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(900, 925):
    print(f"{i+1}: {lines[i]}", end='')
