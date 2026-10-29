import os, re, sys
sys.stdout.reconfigure(encoding='utf-8')

for p in ['karnataka-sir-voter-roll.html', 'karnataka-sir-voter-roll/index.html']:
    if not os.path.exists(p): continue
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Remove unstyled duplicate article block
    c = re.sub(r'\s*<!-- COMPREHENSIVE KARNATAKA SIR 2026 ELECTORAL ROLL & CITIZEN RIGHTS MANUAL ARTICLE -->[\s\S]*?<!-- Legal Notice -->', '\n\n    <!-- Legal Notice -->', c)
    
    # Demote sir-title h1 to h2
    c = re.sub(r'<h1 class=\"sir-title\">([\s\S]*?)</h1>', r'<h2 class=\"sir-title\">\1</h2>', c)
    
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Cleaned', p)
