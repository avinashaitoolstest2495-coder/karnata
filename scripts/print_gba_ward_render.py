import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('gba.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(850, 915):
    print(f"{i+1}: {lines[i]}", end='')
