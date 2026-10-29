import sys, json
sys.stdout.reconfigure(encoding='utf-8')
with open('gba.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const BWSSB_EMBEDDED_DATA =')
if start != -1:
    end = text.find(';\n', start)
    js_obj = text[start + len('const BWSSB_EMBEDDED_DATA ='):end].strip()
    data = json.loads(js_obj)
    print(json.dumps(data.get('divisions', {}).get('Central_1'), indent=2, ensure_ascii=False))
