# scripts/extract_jos_alukkas.py
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\avina\.gemini\antigravity\brain\7d9e2577-cb7a-4642-8e15-991f9a7acb8f\.system_generated\steps\905\content.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('"initialGoldRateData":')
if idx != -1:
    end_idx = text.find('</script>', idx)
    chunk = text[idx:end_idx]
    
    # Extract initialGoldRateData
    m_rate = re.search(r'"initialGoldRateData":\s*(\{.*?\})\s*,\s*"initialStats":', chunk)
    if m_rate:
        rate_json = json.loads(m_rate.group(1))
        print("Rate JSON:", rate_json)
        
    # Extract List under initialStats
    m_list = re.search(r'"List":\s*(\[\{.*?\}\])\s*,\s*"Graph22KT":', chunk, re.DOTALL)
    if m_list:
        list_json = json.loads(m_list.group(1))
        print("List count:", len(list_json))
        day_entries = list_json[0]
        print("Keys in entry:", day_entries.keys())
        p24 = day_entries.get('24KT', [])
        p22 = day_entries.get('22KT', [])
        p18 = day_entries.get('18KT', [])
        print(f"24KT entries: {len(p24)}, latest: {p24[-1]}")
        print(f"22KT entries: {len(p22)}, latest: {p22[-1]}")
        print(f"18KT entries: {len(p18)}, latest: {p18[-1]}")
else:
    print("Not found initialGoldRateData")
