import os

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith(('.js', '.ts', '.py')):
            p = os.path.join(root, f)
            try:
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    c = fp.read()
                    if 'captcha' in c.lower() and ('required' in c.lower() or 'value' in c.lower() or 'search' in c.lower()):
                        for line in c.splitlines():
                            if 'required' in line.lower() and 'captcha' in line.lower():
                                print(f"{p}: {line.strip()}")
            except:
                pass
