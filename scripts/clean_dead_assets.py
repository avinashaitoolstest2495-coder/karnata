for p in ['cabinet-ministers.html', 'former-cms.html', 'karnataka.html']:
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    if '<link rel="stylesheet" href="/css/nav-styles.css">\n' in c:
        c = c.replace('<link rel="stylesheet" href="/css/nav-styles.css">\n', '')
    elif '<link rel="stylesheet" href="/css/nav-styles.css">' in c:
        c = c.replace('<link rel="stylesheet" href="/css/nav-styles.css">', '')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'Removed dead nav-styles.css link from {p}')

# Add /aqi redirect in _redirects
with open('_redirects', 'r', encoding='utf-8') as f:
    r_text = f.read()
if '/aqi' not in r_text:
    r_text += '\n/aqi                        /weather                          301\n'
    with open('_redirects', 'w', encoding='utf-8') as f:
        f.write(r_text)
    print('Added /aqi -> /weather 301 redirect in _redirects')

