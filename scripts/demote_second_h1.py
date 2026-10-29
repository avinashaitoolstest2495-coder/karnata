import re, sys
sys.stdout.reconfigure(encoding='utf-8')

pages = [
    'gold-rate.html', 'ai-jyothishya.html', 'apmc-prices.html',
    'dam-levels.html', 'emi-calculator.html', 'kannada-typing.html',
    'salary-calculator.html', 'sip-calculator.html'
]

pattern = re.compile(r'(<article[^>]*>[\s\S]*?<header[^>]*>[\s\S]*?)<h1(\s+style=\"[^\"]*\")>([\s\S]*?)</h1>', re.I)

for p in pages:
    c = open(p, 'r', encoding='utf-8').read()
    
    # Replace second H1 with H2 in the article header
    def repl(m):
        return f'{m.group(1)}<h2{m.group(2)}>{m.group(3)}</h2>'

    new_c, count = pattern.subn(repl, c, count=1)
    if count == 1:
        open(p, 'w', encoding='utf-8').write(new_c)
        print(f'Successfully demoted second H1 to H2 on {p}')
    else:
        # Fallback: specific string replacement
        target = '<h1 style=\"font-size: 28px; color: #0f172a; margin-bottom: 12px; font-weight: 700;\">'
        rep = '<h2 style=\"font-size: 28px; color: #0f172a; margin-bottom: 12px; font-weight: 700;\">'
        if target in c:
            idx = c.find(target)
            idx_end = c.find('</h1>', idx)
            new_c = c[:idx] + rep + c[idx+len(target):idx_end] + '</h2>' + c[idx_end+5:]
            open(p, 'w', encoding='utf-8').write(new_c)
            print(f'Demoted via fallback on {p}')
        else:
            print(f'Could not find second H1 on {p}')

# Add H1 to index.html if missing
idx_c = open('index.html', 'r', encoding='utf-8').read()
if '<h1' not in idx_c:
    old_logo = '<span class=\"mh-logo-kn\">ಕರ್ನಾಟ</span>'
    new_logo = '<h1 class=\"mh-logo-kn\" style=\"margin:0; padding:0; display:inline;\">ಕರ್ನಾಟ</h1>'
    if old_logo in idx_c:
        idx_c = idx_c.replace(old_logo, new_logo, 1)
        open('index.html', 'w', encoding='utf-8').write(idx_c)
        print('Added H1 to index.html masthead')

