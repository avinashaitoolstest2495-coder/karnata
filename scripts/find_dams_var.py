import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dam-levels.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, l in enumerate(lines):
    if 'const dams =' in l or 'let dams =' in l or 'var dams =' in l:
        print(f"{i+1}: {l.strip()[:140]}")
