import sys, json
sys.stdout.reconfigure(encoding='utf-8')
with open('gba.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('const BWSSB_EMBEDDED_DATA =')
if start != -1:
    end = text.find(';\n', start)
    js_obj = text[start + len('const BWSSB_EMBEDDED_DATA ='):end].strip()
    data = json.loads(js_obj)
    print("Divisions:", list(data.get('divisions', {}).keys()))
    c1 = data.get('divisions', {}).get('Central_1', {})
    print("Central_1 EE:", c1.get('ee'))
    print("Central_1 Subdivisions:", list(c1.get('subdivisions', {}).keys()))
    sub1 = list(c1.get('subdivisions', {}).values())[0] if c1.get('subdivisions') else {}
    print("Subdivision 1 AEE:", sub1.get('name'), sub1.get('aee'))
    print("Stations:", sub1.get('stations', [])[:2])
