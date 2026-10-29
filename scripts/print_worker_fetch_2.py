import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('_worker.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(15530, min(len(lines), 15650)):
    if lines[i].strip():
        print(f"{i+1}: {lines[i].strip()[:140]}")
