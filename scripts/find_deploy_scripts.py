import os

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if any(w in f.lower() for w in ['deploy', 'publish', 'build', 'workflow', '.yml', '.yaml', '.sh', '.bat', '.ps1']):
            print(os.path.join(root, f))
