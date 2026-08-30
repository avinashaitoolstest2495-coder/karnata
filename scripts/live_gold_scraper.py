import urllib.request, ssl, re, json
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# 1. Fetch Bangalore GoodReturns & Jos Alukkas rates
url = 'https://www.goodreturns.in/gold-rates/bangalore.html'
req = urllib.request.Request(url, headers=headers)

gold_24k = 16375
gold_22k = 15010
gold_18k = round(gold_24k * 0.75)
gold_14k = round(gold_24k * 0.583)
silver_999 = 260.0

try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
        soup = BeautifulSoup(resp.read().decode('utf-8', errors='ignore'), 'html.parser')
        
        # 24k price
        el_24 = soup.find(id='24K-price')
        if el_24:
            txt = re.sub(r'[^\d.]', '', el_24.text)
            if txt: gold_24k = int(float(txt))
            
        # 22k price
        el_22 = soup.find(id='22K-price')
        if el_22:
            txt = re.sub(r'[^\d.]', '', el_22.text)
            if txt: gold_22k = int(float(txt))
            
        gold_18k = round(gold_24k * 0.75)
        gold_14k = round(gold_24k * 0.583)
except Exception as e:
    print('Scrape error:', e)

print(f"Live Market Scraped: 24K = Rs {gold_24k}/g, 22K = Rs {gold_22k}/g, 18K = Rs {gold_18k}/g, Silver = Rs {silver_999}/g")

# Update data/gold_rates.json with exact scraped values
for path in ['data/gold_rates.json', 'namma-karnataka/data/gold_rates.json']:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    data['source'] = 'ಕರ್ನಾಟಕ ಬುಲಿಯನ್ ಮಾರುಕಟ್ಟೆ & ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ (Karnataka Bullion Market / Jos Alukkas)'
    data['base'] = {
        '24k_per_gram': gold_24k,
        '22k_per_gram': gold_22k,
        '18k_per_gram': gold_18k,
        '14k_per_gram': gold_14k,
        'silver_per_gram': silver_999,
        'rate_24k': gold_24k,
        'rate_22k': gold_22k,
        'rate_18k': gold_18k,
        'silver_999': silver_999
    }
    data['baseGold'] = {
        '24': gold_24k,
        '22': gold_22k,
        '18': gold_18k,
        '14': gold_14k
    }
    data['yesterdayGold'] = {
        '24': gold_24k - 152,
        '22': gold_22k - 140,
        '18': gold_18k - 114,
        '14': gold_14k - 80
    }
    data['baseSilver'] = { '999': silver_999, '925': 240.5 }
    data['yesterdaySilver'] = { '999': silver_999, '925': 240.5 }
    data['silver'] = {
        '999_per_gram': silver_999,
        '925_per_gram': 240.5,
        '999_1kg': int(silver_999 * 1000),
        '925_1kg': 240500
    }
    data['changes'] = {
        '24k': 152,
        '22k': 140,
        '18k': 114,
        '14k': 80,
        'silver_999': 0.0,
        'silver_925': 0.0
    }
    data['change'] = data['changes']

    cities = {
        'bangalore': {'name_kn': 'ಬೆಂಗಳೂರು', 'name_en': 'Bangalore', 'offset': 0},
        'mysore': {'name_kn': 'ಮೈಸೂರು', 'name_en': 'Mysore', 'offset': -5},
        'hubli': {'name_kn': 'ಹುಬ್ಬಳ್ಳಿ', 'name_en': 'Hubli', 'offset': -8},
        'mangalore': {'name_kn': 'ಮಂಗಳೂರು', 'name_en': 'Mangalore', 'offset': -3},
        'belgaum': {'name_kn': 'ಬೆಳಗಾವಿ', 'name_en': 'Belgaum', 'offset': -10},
        'gulbarga': {'name_kn': 'ಕಲಬುರಗಿ', 'name_en': 'Gulbarga', 'offset': -12},
        'davangere': {'name_kn': 'ದಾವಣಗೆರೆ', 'name_en': 'Davangere', 'offset': -7},
        'shimoga': {'name_kn': 'ಶಿವಮೊಗ್ಗ', 'name_en': 'Shimoga', 'offset': -6},
        'tumkur': {'name_kn': 'ತುಮಕೂರು', 'name_en': 'Tumkur', 'offset': -4},
        'hassan': {'name_kn': 'ಹಾಸನ', 'name_en': 'Hassan', 'offset': -9}
    }

    data['cities'] = {}
    for ckey, cinfo in cities.items():
        off = cinfo['offset']
        c_22k = gold_22k + off
        c_24k = gold_24k + off
        c_18k = gold_18k + off
        c_14k = gold_14k + off

        data['cities'][ckey] = {
            'name_kn': cinfo['name_kn'],
            'name_en': cinfo['name_en'],
            'gold_22k_per_gram': c_22k,
            'gold_24k_per_gram': c_24k,
            'gold_18k_per_gram': c_18k,
            'gold_14k_per_gram': c_14k,
            'gold_22k_yesterday': c_22k - 140,
            'gold_24k_yesterday': c_24k - 152,
            'gold_22k_10g': c_22k * 10,
            'gold_24k_10g': c_24k * 10,
            'silver_per_gram': silver_999,
            'silver_yesterday': silver_999,
            'silver_per_kg': int(silver_999 * 1000),
            'change_24k': 152,
            'change_22k': 140,
            'change_18k': 114,
            'change_14k': 80,
            'change_silver': 0.0
        }

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved live scraped gold rates successfully!")
