# scripts/parse_jos_alukkas_data.py
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\avina\.gemini\antigravity\brain\7d9e2577-cb7a-4642-8e15-991f9a7acb8f\.system_generated\steps\905\content.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('initialGoldRateData')
end_idx = text.find('</script>', idx)
chunk = text[idx-2:end_idx]

# Unescape JSON string
cleaned = chunk.encode().decode('unicode_escape')

# Extract initialGoldRateData
m_rate = re.search(r'"initialGoldRateData":\s*(\{.*?\})\s*,\s*"initialStats":', cleaned)
if m_rate:
    rate_info = json.loads(m_rate.group(1))
    print("=== JOS ALUKKAS TODAY'S LIVE RATES ===")
    print("24K Rate:", rate_info['R24KT'])
    print("22K Rate:", rate_info['R22KT'])
    print("18K Rate:", rate_info['R18KT'])
    print("14K Rate:", rate_info.get('R14KT'))
    print("PT950 Platinum:", rate_info.get('PT950'))
    print("Silver 925:", rate_info.get('RS925'))
    print("Last Updated:", rate_info.get('LastUpdated'))

# Extract List from initialStats
m_list = re.search(r'"List":\s*(\[\{.*?\}\])\s*,\s*"Graph22KT":', cleaned, re.DOTALL)
if m_list:
    list_info = json.loads(m_list.group(1))[0]
    p24 = list_info['24KT']
    p22 = list_info['22KT']
    p18 = list_info['18KT']
    print("\n=== RECENT JOS ALUKKAS DAILY ENTRIES ===")
    for item in p24[-10:]:
        print(f"Date: {item['Date']} | 24K: ₹{item['Price']} | Diff: {item['Difference']}")
