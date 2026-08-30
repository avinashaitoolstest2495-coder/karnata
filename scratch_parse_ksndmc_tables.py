from bs4 import BeautifulSoup
import json

with open('scratch_ksndmc_804.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table')
print(f"Total tables found: {len(tables)}")
for idx, tbl in enumerate(tables):
    rows = tbl.find_all('tr')
    print(f"\n--- TABLE #{idx} (Rows: {len(rows)}) ---")
    for r in rows[:6]:
        cells = [c.get_text(strip=True) for c in r.find_all(['th', 'td'])]
        print("  ", " | ".join(cells[:8]))

# Look for carousel or slider items
carousel_items = soup.find_all(class_=lambda x: x and 'carousel-item' in x)
print(f"\nCarousel items: {len(carousel_items)}")
for c in carousel_items:
    print("Carousel Text:", c.get_text(" ", strip=True))
