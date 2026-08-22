"""
Karnata — dam_scraper.py
Uses the working Karnataka Water Resources API:
POST https://water.karnataka.gov.in/CommonXyZABC.aspx/GetReservoirLocs
Returns GeoJSON with all Karnataka reservoirs and live water levels.
"""

import json
import requests
from utils import store, log, ist_now, ist_date, telegram_alert

API_URL = "https://water.karnataka.gov.in/CommonXyZABC.aspx/GetReservoirLocs"
API_HEADERS = {
    "Content-Type": "application/json; charset=utf-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "https://water.karnataka.gov.in",
    "Referer": "https://water.karnataka.gov.in/ReservoirPublic",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
}

# Map API reservoir names → our canonical keys used in dam-levels.html
RESERVOIR_NAME_MAP = {
    "krishna raja sagara": "krs",
    "k.r.sagara": "krs",
    "k.r. sagara": "krs",
    "krs": "krs",
    "kabini": "kabini",
    "harangi": "harangi",
    "hemavathi": "hemavathi",
    "hemavathy": "hemavathi",
    "tungabhadra": "tungabhadra",
    "linganamakki": "linganamakki",
    "linganamakkey": "linganamakki",
    "almatti": "almatti",
    "narayanapura": "narayanapura",
    "malaprabha": "malaprabha",
    "ghataprabha": "ghataprabha",
    "hidkal": "ghataprabha",
    "bhadra": "bhadra",
    "supa": "supa",
    "varahi": "varahi",
    "vanivilasa": "vanivilasa",
    "vanivilasa sagar": "vanivilasa",
    "vanivilasasagar": "vanivilasa",
    "gayathri": "gayathri",
}

# Total design storage capacity (TMC) for Karnataka reservoirs
DESIGN_CAPACITIES = {
    "almatti": 123.081,
    "krs": 49.452,
    "tungabhadra": 105.788,
    "linganamakki": 151.750,
    "supa": 147.540,
    "bhadra": 71.535,
    "hemavathi": 37.103,
    "kabini": 19.520,
    "harangi": 8.500,
    "ghataprabha": 51.000,
    "malaprabha": 37.730,
    "narayanapura": 33.313,
    "vanivilasa": 30.000,
    "gayathri": 0.980,
}

# Kannada names + metadata keyed by our canonical key
DAM_META = {
    "krs":          {"name_kn": "K.R.Sagara Dam (ಕೃಷ್ಣರಾಜ ಸಾಗರ)", "river_kn": "ಕಾವೇರಿ",   "district_en": "Mandya",         "basin": "cauvery"},
    "kabini":       {"name_kn": "ಕಬಿನಿ ಅಣೆಕಟ್ಟು",               "river_kn": "ಕಬಿನಿ",    "district_en": "H.D. Kote",      "basin": "cauvery"},
    "harangi":      {"name_kn": "ಹಾರಂಗಿ ಅಣೆಕಟ್ಟು",              "river_kn": "ಹಾರಂಗಿ",   "district_en": "Kodagu",         "basin": "cauvery"},
    "hemavathi":    {"name_kn": "ಹೇಮಾವತಿ ಅಣೆಕಟ್ಟು",             "river_kn": "ಹೇಮಾವತಿ",  "district_en": "Hassan",         "basin": "cauvery"},
    "tungabhadra":  {"name_kn": "ತುಂಗಭದ್ರ ಅಣೆಕಟ್ಟು",            "river_kn": "ತುಂಗಭದ್ರ", "district_en": "Vijayanagara",   "basin": "krishna"},
    "linganamakki": {"name_kn": "ಲಿಂಗನಮಕ್ಕಿ ಅಣೆಕಟ್ಟು",          "river_kn": "ಶರಾವತಿ",   "district_en": "Shivamogga",     "basin": "sharavathi"},
    "almatti":      {"name_kn": "ಆಲಮಟ್ಟಿ ಅಣೆಕಟ್ಟು",              "river_kn": "ಕೃಷ್ಣ",    "district_en": "Vijayapura",     "basin": "krishna"},
    "narayanapura": {"name_kn": "ನಾರಾಯಣಪುರ ಅಣೆಕಟ್ಟು",           "river_kn": "ಕೃಷ್ಣ",    "district_en": "Yadgir",         "basin": "krishna"},
    "malaprabha":   {"name_kn": "ಮಲಪ್ರಭಾ ಅಣೆಕಟ್ಟು",              "river_kn": "ಮಲಪ್ರಭಾ",  "district_en": "Belagavi",       "basin": "krishna"},
    "ghataprabha":  {"name_kn": "ಘಟಪ್ರಭಾ (ಹಿಡ್ಕಲ್) ಅಣೆಕಟ್ಟು",    "river_kn": "ಘಟಪ್ರಭಾ",  "district_en": "Belagavi",       "basin": "krishna"},
    "bhadra":       {"name_kn": "ಭದ್ರಾ ಅಣೆಕಟ್ಟು",                "river_kn": "ಭದ್ರಾ",    "district_en": "Chikkamagaluru", "basin": "krishna"},
    "supa":         {"name_kn": "ಸೂಪ ಅಣೆಕಟ್ಟು",                  "river_kn": "ಕಾಳಿ",     "district_en": "Uttara Kannada", "basin": "sharavathi"},
    "varahi":       {"name_kn": "ವಾರಾಹಿ ಅಣೆಕಟ್ಟು",               "river_kn": "ವಾರಾಹಿ",   "district_en": "Udupi",          "basin": "sharavathi"},
    "vanivilasa":   {"name_kn": "ವಾಣಿವಿಲಾಸ ಸಾಗರ",               "river_kn": "ವೇದಾವತಿ",  "district_en": "Chitradurga",    "basin": "krishna"},
    "gayathri":     {"name_kn": "ಗಾಯತ್ರಿ ಜಲಾಶಯ",                "river_kn": "ಸುವರ್ಣಮುಖಿ","district_en": "Chitradurga",   "basin": "krishna"},
}


def fetch_api() -> list[dict] | None:
    """Call the Karnataka Water Resources API via direct or Indian proxy routing."""
    try:
        from utils import indian_fetch
        resp = indian_fetch(API_URL, method="POST", headers=API_HEADERS, timeout=12)
        if resp and resp.status_code == 200:
            geo = json.loads(resp.json()["d"])
            features = geo.get("features", [])
            log.info(f"✅ Water API: {len(features)} reservoirs received")
            return [f["properties"] for f in features]
    except Exception as e:
        log.error(f"❌ Water API error: {e}")
    return None


def match_key(reservoir_name: str) -> str | None:
    """Match API ReservoirName to our canonical key (case-insensitive)."""
    name_lower = reservoir_name.lower().strip()
    for pattern, key in RESERVOIR_NAME_MAP.items():
        if pattern in name_lower or name_lower in pattern:
            return key
    return None


def safe_float(val, default=0.0) -> float:
    try:
        return float(val) if val not in (None, "", "N/A") else default
    except (ValueError, TypeError):
        return default


def build_dam_record(props: dict, key: str) -> dict:
    """Convert raw API properties into our standardised dam record."""
    meta = DAM_META.get(key, {})

    api_design_cap = safe_float(props.get("StorageCapacity_AsPerDesign"))
    known_design_cap = DESIGN_CAPACITIES.get(key, 0.0)
    max_cap = api_design_cap if api_design_cap > 0 else (known_design_cap if known_design_cap > 0 else 50.0)

    gross_storage = safe_float(props.get("TMC_GrossCapacity"))
    live_storage  = safe_float(props.get("TMC_Live_Above_Cill"))

    # Present storage in TMC
    present_storage = gross_storage if gross_storage > 0 else live_storage

    # Calculate actual percentage full
    pct = round((present_storage / max_cap) * 100, 1) if max_cap > 0 else safe_float(props.get("PercentFull"), 0)
    pct = max(0.0, min(100.0, pct))   # clamp to 0-100

    if pct >= 95:  status_kn = "⚠️ ತುಂಬು ಅಪಾಯ"
    elif pct >= 75: status_kn = "✅ ತುಂಬಿದೆ"
    elif pct >= 50: status_kn = "🟢 ಉತ್ತಮ"
    elif pct >= 30: status_kn = "🟡 ಮಧ್ಯಮ"
    else:           status_kn = "🔴 ಕಡಿಮೆ"

    return {
        "id":              key,
        "key":             key,
        **meta,
        "reservoir_id":    props.get("ReservoirID", ""),
        "name_en":         props.get("ReservoirName", key),
        "date":            props.get("Date", ist_date()),
        "storage_pct":     round(pct, 1),
        "level_ft":        safe_float(props.get("Reservior_Level")),   # sic — API typo
        "design_capacity": round(max_cap, 3),
        "max_storage_tmc": round(max_cap, 3),
        "gross_storage_tmc": round(gross_storage, 3),
        "live_storage_tmc":  round(live_storage, 3),
        "storage_tmc":     round(present_storage, 3),
        "present_storage_tmc": round(present_storage, 3),
        "inflow_cusecs":   safe_float(props.get("Flow_Inflow")),
        "outflow_cusecs":  safe_float(props.get("Flow_OutFlow")),
        "lat":             safe_float(props.get("Lat")),
        "lon":             safe_float(props.get("Long")),
        "status_kn":       status_kn,
        "flood_alert":     pct >= 95,
        "is_live":         True,
    }


# The strictly allowed 13 major dams with dedicated detail pages
ALLOWED_DAMS = [
    "almatti", "krs", "hemavathi", "kabini", "harangi", "bhadra",
    "tungabhadra", "linganamakki", "ghataprabha", "malaprabha",
    "narayanapura", "supa", "vanivilasa"
]

FALLBACK_DAMS = {
    "krs":          {"pct": 46.7, "present": 23.08, "inflow": 32048, "outflow": 1450, "level": 108.45},
    "kabini":       {"pct": 95.4, "present": 18.61, "inflow": 31746, "outflow": 27000, "level": 2282.5},
    "harangi":      {"pct": 92.1, "present": 7.83,  "inflow": 11645, "outflow": 10750, "level": 2857.0},
    "hemavathi":    {"pct": 75.5, "present": 28.02, "inflow": 12856, "outflow": 500,   "level": 2911.75},
    "tungabhadra":  {"pct": 41.8, "present": 44.19, "inflow": 40705, "outflow": 0,     "level": 1618.2},
    "linganamakki": {"pct": 78.0, "present": 118.3, "inflow": 28500, "outflow": 1200,  "level": 1805.4},
    "almatti":      {"pct": 91.0, "present": 111.97,"inflow": 125855,"outflow": 128350,"level": 1702.5},
    "narayanapura": {"pct": 88.5, "present": 29.49, "inflow": 128954,"outflow": 123364,"level": 1612.3},
    "malaprabha":   {"pct": 45.2, "present": 17.06, "inflow": 11449, "outflow": 1000,  "level": 2068.5},
    "ghataprabha":  {"pct": 75.3, "present": 38.42, "inflow": 20806, "outflow": 0,     "level": 2155.9},
    "bhadra":       {"pct": 64.7, "present": 46.25, "inflow": 36103, "outflow": 100,   "level": 2145.8},
    "supa":         {"pct": 70.0, "present": 103.28,"inflow": 18400, "outflow": 500,   "level": 1820.0},
    "vanivilasa":   {"pct": 77.9, "present": 23.38, "inflow": 0,     "outflow": 0,     "level": 2131.6},
}

def run() -> dict:
    log.info("💧 Starting dam levels scraper (Karnataka Water API)...")

    api_records = fetch_api()
    dams = {}

    if api_records:
        for props in api_records:
            name = props.get("ReservoirName", "")
            key  = match_key(name)
            if key and key in ALLOWED_DAMS:
                dams[key] = build_dam_record(props, key)
                log.info(f"  {dams[key]['name_kn']}: {dams[key]['storage_pct']}% | "
                         f"{dams[key]['storage_tmc']}/{dams[key]['max_storage_tmc']} TMC | "
                         f"in={dams[key]['inflow_cusecs']} out={dams[key]['outflow_cusecs']}")

    # Fill any missing dam from the strictly allowed 13 list using existing live cache first
    from utils import load_json
    existing_dam_data = load_json("dam_levels.json", {}).get("dams", {})

    for key in ALLOWED_DAMS:
        if key not in dams:
            if key in existing_dam_data and existing_dam_data[key].get("storage_pct"):
                dams[key] = dict(existing_dam_data[key])
                dams[key]["date"] = ist_date()
                log.info(f"  📌 Sticky Cache Preserved for {key}: {dams[key]['storage_pct']}%")
            else:
                meta = DAM_META.get(key, {})
                fb   = FALLBACK_DAMS.get(key, {})
                cap  = DESIGN_CAPACITIES.get(key, 50.0)
                pct  = fb.get("pct", 70.0)
                present = fb.get("present", round(pct * cap / 100, 2))
                dams[key] = {
                    "id":            key,
                    "key":           key,
                    **meta,
                    "storage_pct":   pct,
                    "storage_tmc":   present,
                    "present_storage_tmc": present,
                    "max_storage_tmc": cap,
                    "design_capacity": cap,
                    "inflow_cusecs": fb.get("inflow", 0),
                    "outflow_cusecs":fb.get("outflow", 0),
                    "level_ft":      fb.get("level", 0),
                    "date":          ist_date(),
                    "is_live":       False,
                    "flood_alert":   pct >= 95,
                    "status_kn":     "✅ ತುಂಬಿದೆ" if pct >= 75 else ("🟢 ಉತ್ತಮ" if pct >= 50 else ("🟡 ಮಧ್ಯಮ" if pct >= 30 else "🔴 ಕಡಿಮೆ")),
                }

    log.info(f"✅ Strictly 13 major reservoirs included in output")

    # Summary
    pcts   = [d["storage_pct"] for d in dams.values()]
    tmc    = sum(d.get("storage_tmc",0) for d in dams.values())
    cap    = sum(d.get("max_storage_tmc",0) for d in dams.values())
    alerts = [k for k, d in dams.items() if d.get("flood_alert")]

    if alerts:
        telegram_alert(f"🚨 ಪ್ರವಾಹ ಎಚ್ಚರಿಕೆ: {', '.join(alerts)} — 95%ಕ್ಕಿಂತ ಹೆಚ್ಚು ತುಂಬಿದೆ")

    output = {
        "date":       ist_date(),
        "updated_at": ist_now(),
        "source":     "Karnataka Water Resources Dept API",
        "source_url": "https://water.karnataka.gov.in/ReservoirPublic",
        "update_schedule": "9:00 AM and 12:00 PM daily",
        "is_live":    any(d.get("is_live") for d in dams.values()),
        "summary": {
            "avg_pct":           round(sum(pcts)/len(pcts), 1) if pcts else 0,
            "full_count":        sum(1 for p in pcts if p >= 75),
            "low_count":         sum(1 for p in pcts if p < 30),
            "total_storage_tmc": round(tmc, 1),
            "total_capacity_tmc":round(cap, 1),
            "overall_pct":       round(tmc/cap*100, 1) if cap else 0,
            "flood_alerts":      alerts,
            "total_reservoirs":  len(dams),
        },
        "dams":     dams,
        "note_kn":  "ಮಾಹಿತಿ Karnataka Water Resources Dept ನಿಂದ — ಬೆಳಿಗ್ಗೆ 9:00 ಮತ್ತು ಮಧ್ಯಾಹ್ನ 12:00 ಗಂಟೆಗೆ ನವೀಕರಣ",
    }

    from history_tracker import process_dam_history
    output = process_dam_history(output)

    store("dam_levels.json", "dam_levels", output)
    log.info(f"✅ Dams saved: {len(dams)} reservoirs | avg={output['summary']['avg_pct']}% | "
             f"total={round(tmc,1)}/{round(cap,1)} TMC")
    return output


if __name__ == "__main__":
    run()
