import glob, re, sys
sys.stdout.reconfigure(encoding='utf-8')

all_html = glob.glob('*.html') + glob.glob('districts/*.html') + glob.glob('article/*.html') + glob.glob('dam-levels/*.html')

updated_files = []
for p in all_html:
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    
    pattern = re.compile(r'href=[\"\x27](/?districts(\.html|/index\.html))[\"\x27]')
    matches = pattern.findall(c)
    if matches:
        new_c = pattern.sub('href="/districts"', c)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(new_c)
        updated_files.append((p, len(matches)))

print(f'Standardized links to /districts across {len(updated_files)} files:')
for p, cnt in updated_files:
    print(f'  {p}: {cnt} links updated')
