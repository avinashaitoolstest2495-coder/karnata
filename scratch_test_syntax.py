import re
import subprocess

for fn in ['index.html', 'karnataka-stories.html', 'article.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        text = f.read()
    scripts = re.findall(r'<script(?:\s+[^>]*)?>([\s\S]*?)</script>', text)
    for i, s in enumerate(scripts):
        if 'application/ld+json' in s or not s.strip():
            continue
        sfname = f'scratch_syntax_{fn.replace(".", "_")}_{i}.js'
        with open(sfname, 'w', encoding='utf-8') as sf:
            sf.write(s)
        try:
            res = subprocess.run(['node', '-c', sfname], capture_output=True, text=True, check=True)
            print(f"[OK] {fn} script #{i} syntax valid")
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] {fn} script #{i} syntax error:\n{e.stderr}")
