import re
import subprocess

for fn in ['admin/index.html', 'admin/articles.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        html = f.read()
    scripts = re.findall(r'<script(?:\s+[^>]*)?>([\s\S]*?)</script>', html)
    for i, s in enumerate(scripts):
        clean_name = fn.replace('/', '_').replace('.', '_')
        sfname = f'scratch_{clean_name}_{i}.js'
        with open(sfname, 'w', encoding='utf-8') as sf:
            sf.write(s)
        try:
            subprocess.run(['node', '-c', sfname], check=True, capture_output=True, text=True)
            print(f"[OK] {fn} script #{i} syntax valid")
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] {fn} script #{i} syntax error:\n{e.stderr}")
