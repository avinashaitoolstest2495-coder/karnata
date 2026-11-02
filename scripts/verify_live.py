import sys, urllib.request, re, json

sys.stdout.reconfigure(encoding='utf-8')
url = 'https://karnata.pages.dev/gold-rate.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)
html = resp.read().decode('utf-8')

m = re.search(r'const GOLD_HIST_FULL = (\[[\s\S]*?\]);', html)
hist = json.loads(m.group(1))
print('Live page total history:', len(hist))
print('Live page last date:', hist[-1]['date'])
rev = list(reversed(hist))
print('Live page 7-day dates:', [x['date'] for x in rev[:7]])
print('Creative chart canvas in live page:', 'id="histCreativeChart"' in html)
print('Chart container in live page:', 'id="hist-chart-wrapper"' in html)
