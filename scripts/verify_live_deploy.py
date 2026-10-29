import urllib.request

urls = [
    'https://karnata.pages.dev/sitemap.xml',
    'https://karnata.pages.dev/petrol-price',
    'https://karnata.pages.dev/gram-panchayat',
    'https://karnata.pages.dev/dam-levels',
    'https://karnata.pages.dev/nanna-sthala'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read().decode('utf-8')
            print(f"HTTP {resp.status} - {u} (length: {len(data)})")
            if 'petrol-price' in u:
                print("  Petrol 110.89:", "110.89" in data)
                print("  31 districts:", "31 ಜಿಲ್ಲೆಗಳು" in data)
                print("  Dharwad:", "ಧಾರವಾಡ" in data)
            elif 'dam-levels' in u:
                print("  KRS 62.8%:", "62.8%" in data)
                print("  Bhadra 87.0%:", "87.0%" in data)
            elif 'gram-panchayat' in u:
                print("  Pre-rendered GP cards:", "gp-card" in data)
            elif 'nanna-sthala' in u:
                print("  Vidhana Soudha default:", "ವಿಧಾನಸೌಧ, ಬೆಂಗಳೂರು" in data)
    except Exception as e:
        print(f"Error checking {u}: {e}")
