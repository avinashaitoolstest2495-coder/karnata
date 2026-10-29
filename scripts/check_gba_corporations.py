import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for name in ['gba-central.html', 'gba-east.html', 'gba-north.html', 'gba-south.html', 'gba-west.html']:
    with open(name, 'r', encoding='utf-8') as f:
        c = f.read()
    m = re.findall(r'<tbody[^>]*>\s*</tbody>', c)
    print(f"{name}: empty tbody count = {len(m)}")
    # Find which tbody is empty
    for tm in re.finditer(r'<tbody([^>]*)>\s*</tbody>', c):
        print(f"  Empty tbody attrs: {tm.group(1)}")
