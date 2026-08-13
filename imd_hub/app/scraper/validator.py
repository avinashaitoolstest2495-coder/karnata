"""
validator.py
Data Quality & Type Normalization Engine for IMD Scraper
"""
import re
from typing import Optional, Any

def parse_float(val: Any) -> Optional[float]:
    if val is None:
        return None
    s = str(val).strip().upper()
    if not s or s in ("NIL", "NA", "N/A", "-", "--", "BLANK", "NULL", "NONE"):
        return None
    # Remove degree symbol or extraneous text
    cleaned = re.sub(r"[^\d\.\-]", "", s)
    if not cleaned or cleaned == "-":
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None

def parse_int(val: Any) -> Optional[int]:
    if val is None:
        return None
    s = str(val).strip().upper()
    if not s or s in ("NIL", "NA", "N/A", "-", "--", "BLANK", "NULL", "NONE"):
        return None
    cleaned = re.sub(r"[^\d\-]", "", s)
    if not cleaned or cleaned == "-":
        return None
    try:
        return int(cleaned)
    except ValueError:
        return None

def validate_observation(data: dict) -> tuple[dict, list[str]]:
    """
    Validates and normalizes parsed observation dict.
    Returns (normalized_dict, list_of_errors_or_warnings)
    """
    errors = []
    norm = {}

    # Temperature Validation (-10°C to 60°C)
    max_temp = parse_float(data.get("max_temp"))
    if max_temp is not None:
        if not (-10.0 <= max_temp <= 60.0):
            errors.append(f"Invalid max_temp: {max_temp}°C (out of range -10 to 60)")
            max_temp = None
    norm["max_temp"] = max_temp

    min_temp = parse_float(data.get("min_temp"))
    if min_temp is not None:
        if not (-10.0 <= min_temp <= 60.0):
            errors.append(f"Invalid min_temp: {min_temp}°C (out of range -10 to 60)")
            min_temp = None
    norm["min_temp"] = min_temp

    # Suspicious temp check: max_temp < min_temp
    if max_temp is not None and min_temp is not None and max_temp < min_temp:
        errors.append(f"Suspicious temp check failed: max_temp ({max_temp}) < min_temp ({min_temp})")

    norm["max_temp_departure"] = parse_float(data.get("max_temp_departure"))
    norm["min_temp_departure"] = parse_float(data.get("min_temp_departure"))

    # Rainfall Validation (>= 0)
    rainfall = parse_float(data.get("rainfall_24h"))
    if rainfall is not None:
        if rainfall < 0:
            errors.append(f"Invalid negative rainfall: {rainfall} mm")
            rainfall = None
    norm["rainfall_24h"] = rainfall

    # Humidity Validation (0 to 100%)
    rh_0830 = parse_int(data.get("rh_0830"))
    if rh_0830 is not None and not (0 <= rh_0830 <= 100):
        errors.append(f"Invalid rh_0830: {rh_0830}%")
        rh_0830 = None
    norm["rh_0830"] = rh_0830

    rh_1730 = parse_int(data.get("rh_1730"))
    if rh_1730 is not None and not (0 <= rh_1730 <= 100):
        errors.append(f"Invalid rh_1730: {rh_1730}%")
        rh_1730 = None
    norm["rh_1730"] = rh_1730

    norm["sunset"] = str(data.get("sunset")).strip() if data.get("sunset") else None
    norm["sunrise_tomorrow"] = str(data.get("sunrise_tomorrow")).strip() if data.get("sunrise_tomorrow") else None
    norm["moonset"] = str(data.get("moonset")).strip() if data.get("moonset") else None
    norm["moonrise"] = str(data.get("moonrise")).strip() if data.get("moonrise") else None

    return norm, errors
