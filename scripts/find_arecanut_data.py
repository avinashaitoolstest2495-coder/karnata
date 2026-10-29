import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

with open('apmc-prices.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract arecanut from CROP_ANALYZER_DB
m = re.search(r'const CROP_ANALYZER_DB = ({[\s\S]*?});\s*let currentCropData', text)
if not m:
    print("Could not find CROP_ANALYZER_DB with exact regex, looking for arecanut block")
    start = text.find('"arecanut": {')
    if start != -1:
        end = text.find('},\n    "coconut":', start)
        areca_str = text[start + len('"arecanut": {'):end]
        print("Found arecanut block snippet:")
        print(areca_str[:400])
else:
    print("Regex matched CROP_ANALYZER_DB")
