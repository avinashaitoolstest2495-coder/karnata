import re
import subprocess

for fn in ['admin/index.html', 'admin-transfers.html', 'cms/admin.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    scripts = re.findall(r'<script(?:\s+[^>]*)?>([\s\S]*?)</script>', c)
    for i, s in enumerate(scripts):
        if 'application/ld+json' in s or not s.strip():
            continue
        clean_fn = fn.replace('/', '_').replace('.', '_')
        sfname = f'scratch_{clean_fn}_{i}.js'
        with open(sfname, 'w', encoding='utf-8') as sf:
            sf.write(s)
        try:
            subprocess.run(['node', '-c', sfname], check=True, capture_output=True, text=True)
            print(f"[OK] {fn} script #{i} syntax valid")
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] {fn} script #{i} syntax error:\n{e.stderr}")
