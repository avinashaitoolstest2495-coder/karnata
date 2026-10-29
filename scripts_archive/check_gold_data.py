# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
import json, base64

SECRET_KEY = "NK_SECURE_KEY_2026_KARNATA"

def decrypt_payload(encoded_str):
    raw_bytes = base64.b64decode(encoded_str)
    key_bytes = SECRET_KEY.encode('utf-8')
    decrypted = bytearray()
    for i, b in enumerate(raw_bytes):
        decrypted.append(b ^ key_bytes[i % len(key_bytes)])
    return json.loads(decrypted.decode('utf-8'))

with open("data/gold_rates.json", "r", encoding="utf-8") as f:
    d = json.load(f)
    print("=== data/gold_rates.json ===")
    print("date:", d.get("date"))
    print("last_updated:", d.get("last_updated"))
    print("baseGold:", d.get("baseGold"))
    print("yesterdayGold:", d.get("yesterdayGold"))
    print("baseSilver:", d.get("baseSilver"))

with open("data/history/gold_history.json", "r", encoding="utf-8") as f:
    h = json.load(f)
    if "payload" in h:
        dec = decrypt_payload(h["payload"])
        print("\n=== data/history/gold_history.json (decrypted sample) ===")
        print("keys:", list(dec.keys()) if isinstance(dec, dict) else type(dec))
        if isinstance(dec, list):
            print("latest 3:", dec[-3:])
        elif isinstance(dec, dict):
            for k in list(dec.keys())[:3]:
                print(k, dec[k])
