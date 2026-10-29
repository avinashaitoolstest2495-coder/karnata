import glob, re, os
targets = ['/districts.html', 'districts/index.html', 'districts.html']
found = []
for p in glob.glob('*.html') + glob.glob('districts/*.html') + glob.glob('article/*.html') + glob.glob('dam-levels/*.html'):
    c = open(p, 'r', encoding='utf-8', errors='ignore').read()
    for t in targets:
        if f'href="{t}"' in c or f"href='{t}'" in c:
            found.append((p, t))
print(f'Remaining legacy links: {len(found)}')
for f, t in found:
    print(' ', f, t)
