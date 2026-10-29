import os, sys, re
sys.stdout.reconfigure(encoding='utf-8')

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root or 'scratch' in root:
        continue
    for f in sorted(files):
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            # check for empty tbody: <tbody[^>]*>\s*</tbody>
            empty_tbs = re.findall(r'<tbody[^>]*>\s*</tbody>', content)
            if empty_tbs:
                print(f"Empty tbody found in: {path} ({len(empty_tbs)} instances)")
