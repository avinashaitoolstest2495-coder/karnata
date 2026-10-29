import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('gram-panchayat.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix resultsCountText
text = re.sub(
    r'<div id="resultsCountText"[^>]*>[\s\S]*?</div>',
    '<div id="resultsCountText" style="font-size:15px; font-weight:800; color:#475569;">ಒಟ್ಟು 5,935 ಗ್ರಾಮ ಪಂಚಾಯಿತಿಗಳು</div>',
    text
)

# Find where gp-card is
matches = [m.start() for m in re.finditer(r'<div class="gp-card">', text)]
print("Indices of gp-card:", len(matches))
print("First match:", matches[0], "Last match:", matches[-1])

with open('gram-panchayat.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated resultsCountText successfully.")
