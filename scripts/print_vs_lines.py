import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('functions/api/voter-search.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(75, 115):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end='')
