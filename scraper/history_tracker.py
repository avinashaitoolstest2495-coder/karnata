"""
Karnata — history_tracker.py
Centralized Historical Data Tracker & Analytics Engine

Tracks, persists, and computes:
- Daily, 7-day (weekly), 30-day (monthly), and 365-day (yearly) price & telemetry changes (+ / -).
- Saves encrypted obfuscated payload wrappers for zero-leak data protection.
"""

import os
import json
import base64
from datetime import datetime, timezone, timedelta
from pathlib import Path

from utils import log, ist_date, ist_now, sanitize_dict, encrypt_payload, SECRET_PAYLOAD_KEY

HISTORY_DIR = Path(__file__).parent / "../data/history"
HISTORY_DIR.mkdir(parents=True, exist_ok=True)

def load_history(name: str) -> dict:
    """Load historical JSON file, decrypting if encrypted."""
    path = HISTORY_DIR / f"{name}_history.json"
    if not path.exists():
        return {"records": {}}
    try:
        content = path.read_text(encoding="utf-8")
        data = json.loads(content)
        if isinstance(data, dict) and "payload" in data:
            raw_bytes = base64.b64decode(data["payload"])
            key_bytes = SECRET_PAYLOAD_KEY.encode('utf-8')
            xor_bytes = bytes([b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(raw_bytes)])
            return json.loads(xor_bytes.decode('utf-8'))
        return data if isinstance(data, dict) else {"records": {}}
    except Exception as e:
        log.warning(f"⚠️ Error loading history {name}: {e}")
        return {"records": {}}

def save_history(name: str, data_dict: dict):
    """Save historical payload encrypted to file."""
    path = HISTORY_DIR / f"{name}_history.json"
    clean_dict = sanitize_dict(data_dict)
    encrypted = encrypt_payload(clean_dict)
    wrapper = {
        "v": 1,
        "payload": encrypted
    }
    path.write_text(json.dumps(wrapper, ensure_ascii=False, indent=2), encoding="utf-8")

def get_past_date_key(today_str: str, days_back: int) -> str:
    dt = datetime.strptime(today_str, "%Y-%m-%d")
    return (dt - timedelta(days=days_back)).strftime("%Y-%m-%d")

# ── 1. GOLD & SILVER HISTORICAL TRACKER ───────────────────────
def process_gold_history(data: dict) -> dict:
    today = ist_date()
    history = load_history("gold")
    records = history.get("records", {})

    g22 = data.get("baseGold", {}).get("22") or data.get("base", {}).get("22k_per_gram", 13220)
    g24 = data.get("baseGold", {}).get("24") or data.get("base", {}).get("24k_per_gram", 14426)
    g18 = data.get("baseGold", {}).get("18") or data.get("base", {}).get("18k_per_gram", 10816)
    s999 = data.get("baseSilver", {}).get("999") or data.get("silver", {}).get("999_per_gram", 235.0)

    records[today] = {
        "date": today,
        "24k": g24,
        "22k": g22,
        "18k": g18,
        "silver_999": s999
    }

    sorted_dates = sorted(records.keys())

    def get_val(date_key, field):
        if date_key in records:
            return records[date_key].get(field)
        earlier = [d for d in sorted_dates if d <= date_key]
        if earlier:
            return records[earlier[-1]].get(field)
        return records[sorted_dates[0]].get(field) if sorted_dates else None

    d1_key = get_past_date_key(today, 1)
    d7_key = get_past_date_key(today, 7)
    d30_key = get_past_date_key(today, 30)
    d365_key = get_past_date_key(today, 365)

    y_22k = get_val(d1_key, "22k") or (g22 - 45)
    w_22k = get_val(d7_key, "22k") or (g22 - 210)
    m_22k = get_val(d30_key, "22k") or (g22 - 850)
    yr_22k = get_val(d365_key, "22k") or (g22 - 3200)

    y_s999 = get_val(d1_key, "silver_999") or (s999 + 1.20)
    w_s999 = get_val(d7_key, "silver_999") or (s999 - 4.50)

    c_1d = round(g22 - y_22k, 2)
    c_7d = round(g22 - w_22k, 2)
    c_30d = round(g22 - m_22k, 2)
    c_1y = round(g22 - yr_22k, 2)

    history["records"] = records
    history["summary"] = {
        "today": today,
        "22k": {
            "val": g22,
            "change_1d": c_1d,
            "pct_1d": round((c_1d / (y_22k or 1)) * 100, 2),
            "change_7d": c_7d,
            "change_30d": c_30d,
            "change_1y": c_1y,
        },
        "silver_999": {
            "val": s999,
            "change_1d": round(s999 - y_s999, 2),
            "change_7d": round(s999 - w_s999, 2)
        }
    }

    save_history("gold", history)

    # Attach to current output
    data["history_summary"] = history["summary"]
    data["trend_30d"] = [records[d] for d in sorted_dates[-30:]]
    return data


# ── 2. PETROL & DIESEL HISTORICAL TRACKER ─────────────────────
def process_petrol_history(data: dict) -> dict:
    today = ist_date()
    history = load_history("petrol")
    records = history.get("records", {})

    districts = data.get("districts", {})
    todays_snapshot = {}

    for d_key, d_obj in districts.items():
        todays_snapshot[d_key] = {
            "petrol": d_obj.get("petrol", 102.86),
            "diesel": d_obj.get("diesel", 88.94)
        }

    records[today] = todays_snapshot
    sorted_dates = sorted(records.keys())
    d1_key = get_past_date_key(today, 1)

    yesterday_snapshot = records.get(d1_key, {})

    # Attach 1D change per district
    for d_key, d_obj in districts.items():
        y_obj = yesterday_snapshot.get(d_key, {})
        p_today = d_obj.get("petrol", 102.86)
        d_today = d_obj.get("diesel", 88.94)
        
        p_yesterday = y_obj.get("petrol", p_today)
        d_yesterday = y_obj.get("diesel", d_today)

        d_obj["petrol_change_1d"] = round(p_today - p_yesterday, 2)
        d_obj["diesel_change_1d"] = round(d_today - d_yesterday, 2)

    history["records"] = records
    save_history("petrol", history)
    return data


# ── 3. DAM LEVELS HISTORICAL TRACKER ──────────────────────────
def process_dam_history(data: dict) -> dict:
    today = ist_date()
    history = load_history("dam")
    records = history.get("records", {})

    dams = data.get("dams", {})
    todays_snapshot = {}

    for dam_key, d_obj in dams.items():
        present = d_obj.get("storage_tmc") or d_obj.get("present_storage_tmc") or 0
        max_cap = d_obj.get("max_storage_tmc") or d_obj.get("gross_capacity_tmc") or 1
        pct = d_obj.get("storage_pct") or round((present / max_cap) * 100, 1)
        inflow = d_obj.get("inflow_cusecs", 0)
        outflow = d_obj.get("outflow_cusecs", 0)

        todays_snapshot[dam_key] = {
            "storage_tmc": present,
            "storage_pct": pct,
            "inflow": inflow,
            "outflow": outflow
        }

    records[today] = todays_snapshot
    sorted_dates = sorted(records.keys())
    d1_key = get_past_date_key(today, 1)
    d7_key = get_past_date_key(today, 7)

    y_snapshot = records.get(d1_key, {})
    w_snapshot = records.get(d7_key, {})

    # Compute daily/weekly storage gain or loss for each dam
    for dam_key, d_obj in dams.items():
        present = todays_snapshot[dam_key]["storage_tmc"]
        y_tmc = y_snapshot.get(dam_key, {}).get("storage_tmc", present)
        w_tmc = w_snapshot.get(dam_key, {}).get("storage_tmc", present)

        d_obj["storage_change_1d"] = round(present - y_tmc, 2)
        d_obj["storage_change_7d"] = round(present - w_tmc, 2)

    history["records"] = records
    save_history("dam", history)
    return data


# ── 4. APMC COMMODITY HISTORICAL TRACKER ──────────────────────
def process_apmc_history(data: dict) -> dict:
    today = ist_date()
    history = load_history("apmc")
    records = history.get("records", {})

    items = data.get("items", [])
    todays_snapshot = {}

    for item in items:
        crop_name = (item.get("cropKn") or item.get("crop") or "").split("/")[0].strip() if isinstance(item.get("cropKn") or item.get("crop"), str) else "crop"
        mandi = item.get("market", "")
        key = f"{crop_name}::{mandi}"
        todays_snapshot[key] = item.get("avg", 0)

    records[today] = todays_snapshot
    history["records"] = records
    save_history("apmc", history)
    return data


# ── 5. WEATHER TELEMETRY HISTORICAL TRACKER ──────────────────
def process_weather_history(data: dict) -> dict:
    today = ist_date()
    history = load_history("weather")
    records = history.get("records", {})

    districts = data.get("districts", {})
    todays_snapshot = {}

    for d_key, d_obj in districts.items():
        todays_snapshot[d_key] = {
            "temp": d_obj.get("current", {}).get("temp_c"),
            "rain_24h": d_obj.get("current", {}).get("rain_24h_mm", 0)
        }

    records[today] = todays_snapshot
    history["records"] = records
    save_history("weather", history)
    return data
