import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/run_all_and_deploy.py', 'r', encoding='utf-8') as f:
    text = f.read()

# print the deployment step specifically
idx = text.find('deploy')
while idx != -1:
    print("--- DEPLOY MENTION ---")
    print(text[max(0, idx-100):min(len(text), idx+400)])
    idx = text.find('deploy', idx+200)
