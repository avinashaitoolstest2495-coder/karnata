import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('UPDATE_AND_DEPLOY.bat', 'r', encoding='utf-8') as f:
    print("=== UPDATE_AND_DEPLOY.bat ===")
    print(f.read())

with open('scripts/run_all_and_deploy.py', 'r', encoding='utf-8') as f:
    print("=== scripts/run_all_and_deploy.py ===")
    print(f.read()[:1000])
