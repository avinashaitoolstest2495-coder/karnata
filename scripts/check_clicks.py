import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'onclick=["\'][^"\']*location\.href\s*=\s*[\'"]([^\'"]+)[\'"][^"\']*["\']', text)
for m in matches:
    print('onclick location.href ->', m)
