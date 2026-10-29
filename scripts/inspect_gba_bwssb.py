import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('gba.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("--- LINES 560-630 ---")
for i in range(560, 635):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')
