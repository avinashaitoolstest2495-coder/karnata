import requests, json
import urllib3
urllib3.disable_warnings()

url = 'https://mausam.imd.gov.in/imd_latest/contents/districtwisewarnings_mc.php?id=13'
res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, verify=False, timeout=12)
areas_idx = res.text.find('"areas": [')
if areas_idx != -1:
    end_idx = res.text.find(']', areas_idx)
    raw_areas = json.loads(res.text[areas_idx+9:end_idx+1])
    
    all_31_karnataka = [
        ("bengaluru_urban", ["BENGALURU URBAN", "BANGALORE URBAN", "BENGALURU", "BANGALORE"]),
        ("bengaluru_rural", ["BENGALURU RURAL", "BANGALORE RURAL"]),
        ("mysuru", ["MYSURU", "MYSORE"]),
        ("mandya", ["MANDYA"]),
        ("hassan", ["HASSAN"]),
        ("kodagu", ["KODAGU", "COORG"]),
        ("dakshina_kannada", ["DAKSHINA KANNADA", "SOUTH KANARA", "MANGALORE", "MANGALURU"]),
        ("udupi", ["UDUPI"]),
        ("uttara_kannada", ["UTTARA KANNADA", "NORTH KANARA", "KARWAR"]),
        ("shivamogga", ["SHIVAMOGGA", "SHIMOGA"]),
        ("chikkamagaluru", ["CHIKKAMAGALURU", "CHIKMAGALUR", "CHIKMAGALURU"]),
        ("tumakuru", ["TUMAKURU", "TUMKUR"]),
        ("chitradurga", ["CHITRADURGA"]),
        ("davanagere", ["DAVANAGERE", "DAVANGERE"]),
        ("belagavi", ["BELAGAVI", "BELGAUM"]),
        ("dharwad", ["DHARWAD", "HUBLI"]),
        ("gadag", ["GADAG"]),
        ("haveri", ["HAVERI"]),
        ("bagalkote", ["BAGALKOTE", "BAGALKOT"]),
        ("vijayapura", ["VIJAYAPURA", "BIJAPUR"]),
        ("kalaburagi", ["KALABURAGI", "GULBARGA"]),
        ("yadgir", ["YADGIR", "YADAGIRI"]),
        ("raichur", ["RAICHUR"]),
        ("koppal", ["KOPPAL"]),
        ("ballari", ["BALLARI", "BELLARY"]),
        ("vijayanagara", ["VIJAYANAGARA", "HOSAPETE", "HOSPET"]),
        ("chikkaballapura", ["CHIKKABALLAPURA", "CHIKKABALLAPUR", "CHIKBALLAPUR"]),
        ("kolar", ["KOLAR"]),
        ("ramanagara", ["RAMANAGARA", "RAMANAGARAM", "RAMANAGAR"]),
        ("chamarajanagar", ["CHAMARAJANAGAR", "CHAMARAJANAGARA", "CHAMRAJNAGAR"]),
        ("bidar", ["BIDAR"])
    ]

    found_map = {}
    for a in raw_areas:
        title = (a.get('title') or '').upper().strip()
        found_map[title] = a

    matched = []
    missing = []
    for key, aliases in all_31_karnataka:
        found_match = None
        for al in aliases:
            for ft, item in found_map.items():
                if al == ft or al in ft or ft in al:
                    found_match = (key, ft, item.get('color'))
                    break
            if found_match: break
        
        if found_match:
            matched.append(found_match)
        else:
            missing.append(key)

    print(f"Total matched: {len(matched)} / {len(all_31_karnataka)}")
    for m in matched:
        print(f"  OK: {m[0]} -> {m[1]} ({m[2]})")
    if missing:
        print("  MISSING:", missing)
        # Search all titles for missing keys
        for miss in missing:
            print(f"Possible matches for {miss}:", [t for t in found_map if miss[:4].upper() in t])
