import sys

with open(r'c:\Users\avina\Downloads\karnata-site-with-cms\nav-component.js', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

idx1 = text.find('<div class="nk-nav">')
idx2 = text.find('`;', idx1)
print(f"idx1={idx1}, idx2={idx2}")
if idx1 != -1 and idx2 != -1:
    print(text[idx1:idx2])
