import urllib.request, re, sys
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://karnata.in/dam-levels'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')

print("update-time in HTML:")
m = re.search(r'<div class="update-time"[^>]*>([\s\S]*?)</div>', html)
if m: print(" ", m.group(0))

print("summary values in HTML:")
for k in ['sum-avg', 'sum-full', 'sum-low', 'sum-present-tmc', 'sum-gross-cap']:
    sm = re.search(r'<div class="sum-val" id="' + k + r'">([\s\S]*?)</div>', html)
    if sm: print(f"  {k}: {sm.group(1)}")
