import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('gram-panchayat.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'gpgrid' in line.lower() or 'panchatantra' in line.lower() or 'render' in line.lower():
        if len(line.strip()) < 150:
            print(f"{i+1}: {line.strip()}")
