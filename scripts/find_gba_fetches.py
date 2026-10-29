import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('gba.html', 'r', encoding='utf-8') as f:
    for line in f:
        if 'fetch(' in line:
            print(line.strip()[:140])
