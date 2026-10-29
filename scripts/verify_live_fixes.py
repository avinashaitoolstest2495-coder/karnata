import urllib.request, json, re, sys

sys.stdout.reconfigure(encoding='utf-8')

print("1. Testing live captcha API:")
cap_url = 'https://karnata.in/api/voter-search?action=captcha'
try:
    req = urllib.request.Request(cap_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        cap_data = json.loads(resp.read().decode('utf-8'))
        print("   success:", cap_data.get('success'))
        print("   captchaId:", cap_data.get('captchaId'))
        print("   has captchaImg:", 'captchaImg' in cap_data)
        if 'captchaImg' in cap_data:
            print("   captchaImg starts with:", cap_data['captchaImg'][:35])
except Exception as e:
    print("   Error:", e)

print("\n2. Testing live voter roll page HTML:")
v_url = 'https://karnata.in/karnataka-sir-voter-roll/'
try:
    req = urllib.request.Request(v_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        v_html = resp.read().decode('utf-8')
        print("   Has captchaImg fallback in script:", "d.captchaImg || d.captchaSvg" in v_html)
        print("   Has data URI prefixing:", "data:image/jpeg;base64," in v_html)
except Exception as e:
    print("   Error:", e)

print("\n3. Testing live dam levels page HTML:")
d_url = 'https://karnata.in/dam-levels'
try:
    req = urllib.request.Request(d_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        d_html = resp.read().decode('utf-8')
        print("   Has data-loader.js in head:", "<script src=\"/data-loader.js\"></script>\n</head>" in d_html)
        print("   Has 04-09-2026 update date:", "04-09-2026" in d_html)
        print("   Has 80% average:", '<div class="sum-val" id="sum-avg">80%</div>' in d_html)
        print("   Has KRS 60.5% in HTML:", "60.5%" in d_html)
        print("   Has Almatti 99.8% in HTML:", "99.8%" in d_html)
        print("   Has Harangi 97.7% in HTML:", "97.7%" in d_html)
        print("   Has Tungabhadra 89.6% in HTML:", "89.6%" in d_html)
except Exception as e:
    print("   Error:", e)

print("\n4. Testing live dam JSON endpoint:")
dj_url = 'https://karnata.in/data/dam_levels.json'
try:
    req = urllib.request.Request(dj_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=10) as resp:
        dj_data = json.loads(resp.read().decode('utf-8'))
        print("   Has root-level dams:", 'dams' in dj_data)
        if 'dams' in dj_data:
            print("   Live dams count:", len(dj_data['dams']))
            print("   KRS in JSON:", dj_data['dams'].get('krs', {}).get('storage_pct'))
except Exception as e:
    print("   Error:", e)

