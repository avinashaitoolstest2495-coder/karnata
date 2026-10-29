import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('gram-panchayat.html', 'r', encoding='utf-8') as f:
    text = f.read()

cards = re.findall(r'<div class="gp-card">', text)
print("Total gp-card elements:", len(cards))
print("Loading placeholder still present?", "ಕರ್ನಾಟಕ ಗ್ರಾಮ ಪಂಚಾಯತ್ ದತ್ತಾಂಶ ಲೋಡ್ ಆಗುತ್ತಿದೆ" in text)
print("Results count text:", "ಒಟ್ಟು 5,935 ಗ್ರಾಮ ಪಂಚಾಯಿತಿಗಳು" in text)
print("Pagination visible?", '<div class="pagination-bar" id="paginationBar" style="display:flex;">' in text)
