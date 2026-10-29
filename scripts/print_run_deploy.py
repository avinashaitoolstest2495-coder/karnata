import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/run_all_and_deploy.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(150, min(len(lines), 230)):
    print(f"{i+1}: {lines[i]}", end='')
