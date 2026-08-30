import os
import json
import base64
from pathlib import Path
import sys

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "scripts"))

# Read official pure KRAMA dataset
target_json = ROOT_DIR / "data" / "apmc_prices.json"
if target_json.exists():
    with open(target_json, "r", encoding="utf-8") as f:
        d = json.load(f)
    items = d.get("items", [])
else:
    from scrape_full_krama_live_pure import run_pure_krama_scraper
    items = run_pure_krama_scraper()

SECRET_KEY = "NK_SECURE_KEY_2026_KARNATA"

def xor_encrypt(data_str, key):
    res = bytearray()
    for i, ch in enumerate(data_str.encode('utf-8')):
        res.append(ch ^ ord(key[i % len(key)]))
    return base64.b64encode(res).decode('ascii')

payload_str = json.dumps(items, ensure_ascii=False)
encrypted_payload = xor_encrypt(payload_str, SECRET_KEY)

output_data = {
    "date": "2026-08-28",
    "updated_at": "2026-08-28T08:00:00+05:30",
    "total_records": len(items),
    "total_mandis": len(set(d.get("market", "") for d in items if isinstance(d, dict))),
    "source": "Official KRAMA (krama.karnataka.gov.in)",
    "v": 2,
    "payload": encrypted_payload,
    "items": items
}

with open(target_json, "w", encoding="utf-8") as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"SUCCESS: data/apmc_prices.json updated with {len(items)} pure KRAMA records.")
