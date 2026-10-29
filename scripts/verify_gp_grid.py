import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('gram-panchayat.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<div class="grid" id="gpGrid">([\s\S]*?)</div>\s*<!-- Pagination -->', text)
if m:
    cards = re.findall(r'<div class="gp-card">', m.group(1))
    print("Cards inside #gpGrid:", len(cards))
    print("resultsCountText:", "ಒಟ್ಟು 5,935 ಗ್ರಾಮ ಪಂಚಾಯಿತಿಗಳು" in text)
