import json, re, sys
sys.stdout.reconfigure(encoding="utf-8")

with open("data/myscheme_raw_harvest.json", "r", encoding="utf-8") as f:
    ms = json.load(f)
with open("data/government_schemes.json", "r", encoding="utf-8") as f:
    cs = json.load(f)["schemes"]

def norm(s):
    return re.sub(r'[^a-z0-9]', '', (s or '').lower())

ms_by_norm = {norm(s["name_en"]): s for s in ms}
for c in cs:
    t = c.get("scheme_name_en") or ""
    n = norm(t)
    if n in ms_by_norm:
        print("EXACT:", t, "==", ms_by_norm[n]["name_en"])
