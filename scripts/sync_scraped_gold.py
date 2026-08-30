import json

# 1. Update morning_bulletin.json
for p in ['data/morning_bulletin.json', 'namma-karnataka/data/morning_bulletin.json']:
    with open(p, 'r', encoding='utf-8') as f:
        mb = json.load(f)
    mb['summary'] = 'ಚಿನ್ನ ₹15010/g · ಬೆಳ್ಳಿ ₹260.0/g | ಪೆಟ್ರೋಲ್ ₹102.86 | ಕೆಆರ್‌ಎಸ್ 61.7% | ಹವಾಮಾನ 20°C'
    if 'sections' in mb and 'gold_silver' in mb['sections']:
        gs = mb['sections']['gold_silver']
        gs['gold_22k'] = 15010
        gs['gold_24k'] = 16375
        gs['silver_999'] = 260.0
        gs['gold_display'] = '22K ಚಿನ್ನ: ₹15010/g · 24K: ₹16375/g'
        gs['silver_display'] = 'ಬೆಳ್ಳಿ ದರ: ₹260.0/g (100g: ₹26,000)'
        gs['display'] = '22K: ₹15010/g · 24K: ₹16375/g · ಬೆಳ್ಳಿ: ₹260.0/g'
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(mb, f, ensure_ascii=False, indent=2)

# 2. Update gold-rate.html
with open('gold-rate.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('const DEFAULT_GOLD = { 24: 8890, 22: 8150, 18: 6668 };', 'const DEFAULT_GOLD = { 24: 16375, 22: 15010, 18: 12281 };')
c = c.replace('const DEFAULT_YESTERDAY_GOLD = { 24: 8840, 22: 8105, 18: 6631 };', 'const DEFAULT_YESTERDAY_GOLD = { 24: 16223, 22: 14870, 18: 12167 };')
c = c.replace('const DEFAULT_SILVER = { 999: 104.50, 925: 96.65 };', 'const DEFAULT_SILVER = { 999: 260.00, 925: 240.50 };')
c = c.replace('const DEFAULT_YESTERDAY_SILVER = { 999: 104.00, 925: 96.20 };', 'const DEFAULT_YESTERDAY_SILVER = { 999: 260.00, 925: 240.50 };')

c = c.replace('id="gold22-price">₹8,150<', 'id="gold22-price">₹15,010<')
c = c.replace('id="gold24-price">₹8,890<', 'id="gold24-price">₹16,375<')
c = c.replace('id="silver-price">₹104.50<', 'id="silver-price">₹260.00<')
c = c.replace('id="gold18-price">₹6,668<', 'id="gold18-price">₹12,281<')

with open('gold-rate.html', 'w', encoding='utf-8') as f:
    f.write(c)

# 3. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    h = f.read()

h = h.replace('₹8,150', '₹15,010')
h = h.replace('₹104.50', '₹260.00')
h = h.replace('₹8,150/g', '₹15,010/g')
h = h.replace('₹104.50/g', '₹260.00/g')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(h)

print('Updated all files with live scraped Jos Alukkas & Bullion prices!')
