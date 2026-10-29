import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ai-jyothishya.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if '<table class="planets-table">' in l:
        for j in range(max(0, i-5), min(len(lines), i+30)):
            print(f"{j+1}: {lines[j]}", end='')
        break
