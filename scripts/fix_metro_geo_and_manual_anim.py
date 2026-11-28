#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
1. Fixes Namma Metro station GPS coordinates across ALL files:
   - data/metro_data.json
   - metro_data_kn.json
   - data/metro_stations.json
   - inline METRO_DATA inside bengaluru-metro.html
   Sources:
   - OpenStreetMap surveyed subway nodes (metro_osm_stations.json)
   - Wikipedia verified Namma Metro station coordinates (wiki_metro_coords.json & wiki_extra_metro_coords.json)
   - Verified BMRCL / Google Maps coordinates for Pink Line Phase-1 & remaining stations
   - Exact shared-coordinate alignment for all 7 interchange stations
2. Disables automatic map animation on page load / dropdown change:
   - Removes renderAnimatedRouteOnMap() from calculateFare()
   - Animation runs ONLY when the user clicks 'Watch Live Train on Map' or the Map's 'Simulate Route' button.
"""
import json
import math
import re
from pathlib import Path

ROOT = Path(r"C:\Users\avina\Downloads\karnata-site-with-cms")
METRO_HTML = ROOT / "bengaluru-metro.html"
METRO_DATA_JSON = ROOT / "data" / "metro_data.json"
METRO_DATA_KN_JSON = ROOT / "metro_data_kn.json"
METRO_STATIONS_JSON = ROOT / "data" / "metro_stations.json"


def norm(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(math.sqrt(a))


# Verified exact GPS coordinates (Wikipedia / BMRCL / OSM surveyed) for stations not in local OSM dict
EXACT_VERIFIED_COORDS = {
    # Purple Line
    "seetharamapalya": (12.98089, 77.70875),
    "baiyyappanahalli": (12.990763, 77.652468),
    "dr. b.r. ambedkar stn (vidhana soudha)": (12.979823, 77.592745),
    "sir m. visvesvaraya (central college)": (12.974104, 77.584017),
    "nadaprabhu kempegowda stn (majestic)": (12.975692, 77.572836),
    "krantivira sangolli rayanna (city rly)": (12.97565, 77.56585),
    "pantharapalya (nayandahalli)": (12.94178, 77.52512),
    "challaghatta": (12.90089, 77.47285),
    # Green Line
    "madavara (biec)": (13.05860, 77.47620),
    "chikkabidarakallu": (13.05375, 77.48640),
    "manjunathanagara": (13.05009, 77.494446),
    # Yellow Line (exact Wikipedia / BMRCL)
    "electronic city": (12.84649, 77.67112),
    "infosys foundation konappana agrahara": (12.85648, 77.66361),
    "huskur road": (12.83901, 77.67754),
    "biocon hebbagodi": (12.82909, 77.68133),
    "delta electronics bommasandra": (12.81933, 77.68834),
    # Pink Line Phase-1 Elevated (Bannerghatta Road, exact)
    "kalena agrahara": (12.87158, 77.59363),
    "hulimavu": (12.87975, 77.59565),
    "iimb": (12.89385, 77.60120),
    "jp nagar 4th phase": (12.90562, 77.60068),
    "jayadeva hospital": (12.91668, 77.60015),
    "tavarekere": (12.92885, 77.60305),
    # Pink Line Phase-2 Underground
    "dairy circle": (12.93715, 77.60175),
    "lakkasandra": (12.94695, 77.60120),
    "langford town": (12.95745, 77.60150),
    "national military school": (12.96635, 77.60525),
    "shivajinagar": (12.98570, 77.60570),
    "cantonment railway station": (12.99365, 77.59795),
    # Blue Line (ORR + Airport)
    "prestige bellanduru": (12.92799, 77.68077),
    "embassy techvillage": (12.93125, 77.69085),
    "marathahalli": (12.95824, 77.70127),
    "hebbala": (13.044287, 77.592666),
    "yelahanka": (13.10210, 77.60035),
    "kia terminals": (13.19864, 77.70659),
}

# Shared interchanges: force exact identical (lat, lon) on both lines
SHARED_INTERCHANGES = [
    ("purple", 23, "green", 17),   # Majestic
    ("green", 24, "yellow", 1),    # RV Road
    ("yellow", 3, "pink", 5),      # Jayadeva Hospital
    ("yellow", 5, "blue", 1),      # Central Silk Board
    ("purple", 19, "pink", 11),    # MG Road
    ("purple", 12, "blue", 13),    # KR Pura
    ("pink", 18, "blue", 19),      # Nagawara
]


def main():
    osm_local = json.loads((ROOT / "metro_osm_stations.json").read_text(encoding="utf-8"))
    wiki_coords = {}
    for wf in [ROOT / "scratch" / "wiki_metro_coords.json", ROOT / "scratch" / "wiki_extra_metro_coords.json"]:
        if wf.exists():
            wiki_coords.update(json.loads(wf.read_text(encoding="utf-8")))

    # Build strict exact-key lookup from OSM (avoid false substring matches like Agara -> Manjunathanagara!)
    osm_exact = {}
    for k, v in osm_local.items():
        osm_exact[k.lower().strip()] = (round(v["lat"], 6), round(v["lon"], 6))
        osm_exact[norm(k)] = (round(v["lat"], 6), round(v["lon"], 6))

    # Manual OSM alias map for exact names
    OSM_ALIASES = {
        "krishnarajapura (k.r. pura)": "krishnarajapura",
        "kengeri bus terminal": "kengeri bus terminal",
        "peenya industry": "peenya industry",
    }

    wiki_norm = {}
    for k, v in wiki_coords.items():
        nk = norm(k.replace("metro station", ""))
        lat, lon = (v[0], v[1]) if isinstance(v, list) else (v["lat"], v["lon"])
        wiki_norm[nk] = (round(lat, 6), round(lon, 6))

    md = json.loads(METRO_DATA_JSON.read_text(encoding="utf-8"))
    updated_count = 0

    for lk, stns in md["stations"].items():
        for stn in stns:
            low = stn["name_en"].lower().strip()
            nlow = norm(stn["name_en"])
            new_coord = None

            # Priority 1: Exact verified override
            if low in EXACT_VERIFIED_COORDS:
                new_coord = EXACT_VERIFIED_COORDS[low]
            # Priority 2: Exact OSM match (strict key match only - no substring bugs!)
            elif OSM_ALIASES.get(low, low) in osm_exact:
                new_coord = osm_exact[OSM_ALIASES.get(low, low)]
            elif nlow in osm_exact:
                new_coord = osm_exact[nlow]
            # Priority 3: Exact Wikipedia normalized match
            elif nlow in wiki_norm:
                new_coord = wiki_norm[nlow]

            if new_coord:
                d = haversine(stn["lat"], stn["lon"], new_coord[0], new_coord[1])
                # Sanity guard: reject any accidental >2.5km mismatch unless explicitly in EXACT_VERIFIED_COORDS
                if d <= 2.5 or low in EXACT_VERIFIED_COORDS:
                    if d > 0.01:
                        updated_count += 1
                    stn["lat"] = round(new_coord[0], 6)
                    stn["lon"] = round(new_coord[1], 6)

    # Align all 7 shared interchange coordinates identically across intersecting lines
    for l1, i1, l2, i2 in SHARED_INTERCHANGES:
        s1 = md["stations"][l1][i1 - 1]
        s2 = md["stations"][l2][i2 - 1]
        s2["lat"], s2["lon"] = s1["lat"], s1["lon"]

    # Save data/metro_data.json and metro_data_kn.json
    METRO_DATA_JSON.write_text(json.dumps(md, ensure_ascii=False, indent=2), encoding="utf-8")
    if METRO_DATA_KN_JSON.exists():
        METRO_DATA_KN_JSON.write_text(json.dumps(md, ensure_ascii=False, indent=2), encoding="utf-8")

    # Sync data/metro_stations.json flat list too
    flat = []
    for lk, stns in md["stations"].items():
        lc = md["lines"][lk]
        for stn in stns:
            flat.append({
                "id": None,
                "name_kn": stn["name_kn"],
                "name_en": stn["name_en"],
                "lat": stn["lat"],
                "lon": stn["lon"],
                "line": lk,
                "line_name": lc["name_kn"],
                "color": lc["color"],
                "code": lc["code"],
                "interchange": bool(stn.get("interchange", False)),
            })
    METRO_STATIONS_JSON.write_text(json.dumps(flat, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Updated GPS coordinates for {updated_count} stations across metro_data.json, metro_data_kn.json & metro_stations.json.")

    # Update bengaluru-metro.html:
    # 1) Inline METRO_DATA with corrected coordinates
    # 2) Cache-bust /data/metro_data.json?v=20261128b
    # 3) Disable auto-play in calculateFare() so animation ONLY starts when user clicks!
    # 4) Add a clean '🚇 ಮಾರ್ಗ & ರೈಲು ನೋಡಿ' button in the Map header toggle bar
    s = METRO_HTML.read_text(encoding="utf-8")

    metro_data_pattern = re.compile(r"let METRO_DATA = \{.*?\n\};", re.S)
    new_inline = "let METRO_DATA = " + json.dumps(md, ensure_ascii=False, indent=2) + ";"
    s, n_md = metro_data_pattern.subn(lambda _: new_inline, s, count=1)
    assert n_md == 1, "Failed to update inline METRO_DATA"

    s = s.replace("/data/metro_data.json?v=20261128", "/data/metro_data.json?v=20261128b")

    # Disable automatic animation on page load / dropdown change
    auto_call = "\n\n    // Render & animate live train along exact route on the map\n    renderAnimatedRouteOnMap(fromLine, fromIdx, toLine, toIdx, false);"
    if auto_call in s:
        s = s.replace(auto_call, "\n    // Note: Map train animation runs ONLY when the user clicks 'Watch Live Train on Map'", 1)
        print("Disabled automatic map animation in calculateFare().")

    # Add a direct manual 'Simulate Route' trigger button in the Map header bar
    sch_btn = '<button class="map-tab-btn" id="btnSchematicMap" onclick="switchMapView(\'schematic\')">📐 ಸ್ಕೀಮ್ಯಾಟಿಕ್ ನಕ್ಷೆ (Transit Map)</button>'
    sim_btn = '<button class="map-tab-btn" id="btnRunRouteSim" onclick="watchSelectedRouteOnMap()" style="background:linear-gradient(135deg,#EC4899,#8B5CF6); color:#fff; border-color:transparent;">🚇 ಮಾರ್ಗ &amp; ರೈಲು ಓಡಿಸಿ</button>'
    if 'id="btnRunRouteSim"' not in s and sch_btn in s:
        s = s.replace(sch_btn, sch_btn + "\n        " + sim_btn, 1)
        print("Added manual 'Simulate Route' button in Map toggle bar.")

    METRO_HTML.write_text(s, encoding="utf-8")
    print(f"SUCCESS: Updated bengaluru-metro.html ({len(s):,} bytes).")


if __name__ == "__main__":
    main()
