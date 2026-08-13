"""
imd_parser.py
Resilient BeautifulSoup Parser for IMD Karnataka Main Page & City Forecast Pages
"""

import re
from urllib.parse import urljoin, parse_qs, urlparse
from bs4 import BeautifulSoup

def parse_karnataka_index(html: str, base_url: str = "https://internal.imd.gov.in/power/SRLDC/Karnatak.html") -> list[dict]:
    """
    Parses Karnataka source page to discover location names & forecast URLs.
    Returns list of dicts: [{location_name, normalized_name, source_url, forecast_url, imd_city_id}, ...]
    """
    soup = BeautifulSoup(html, "html.parser")
    locations = []
    seen_combos = set()

    for a in soup.find_all("a"):
        href = a.get("href")
        if not href or "citywxnew.php" not in href:
            continue

        full_url = urljoin(base_url, href.strip())

        parsed_url = urlparse(full_url)
        query = parse_qs(parsed_url.query)
        city_id = query.get("id", [None])[0]

        loc_name = ""

        # Strategy A: Walk up to parent <li> structure (IMD Menu Bar)
        parent_li = a.find_parent("li")
        if parent_li:
            outer_li = parent_li.find_parent("li") or parent_li
            spans = [s.text.strip() for s in outer_li.find_all("span") if s.text.strip() and s.text.strip().upper() not in ("FORECAST", "FORECSAT", "")]
            if spans:
                loc_name = spans[0]

        # Strategy B: Fallback to parent <tr> / <td> cells
        if not loc_name or loc_name.upper() in ("FORECAST", "FORECSAT"):
            parent_tr = a.find_parent("tr")
            if parent_tr:
                cells = [td.text.strip() for td in parent_tr.find_all(["td", "th"])]
                filtered = [c for c in cells if c.upper() not in ("FORECAST", "FORECSAT", "CLICK HERE", "LINK", "DETAILS", "")]
                if filtered:
                    loc_name = filtered[0]

        if not loc_name or loc_name.upper() in ("FORECAST", "FORECSAT"):
            loc_name = f"IMD City {city_id or 'Unknown'}"

        loc_name = re.sub(r"[\s\:\-\_]+", " ", loc_name).strip().title()
        normalized_name = re.sub(r"[^\w\s]", "", loc_name).strip().lower().replace(" ", "_")

        combo_key = (normalized_name, full_url)
        if combo_key not in seen_combos:
            seen_combos.add(combo_key)
            locations.append({
                "location_name": loc_name,
                "normalized_name": normalized_name,
                "source_url": base_url,
                "forecast_url": full_url,
                "imd_city_id": city_id
            })

    return locations

def parse_city_forecast_page(html: str, source_url: str = "") -> dict:
    """
    Parses individual IMD city forecast page (e.g. citywxnew.php?id=43295).
    """
    soup = BeautifulSoup(html, "html.parser")
    result = {
        "city_name": None,
        "dated": None,
        "observation": {},
        "forecasts": [],
        "warnings": []
    }

    text_content = soup.get_text()
    loc_match = re.search(r"Local Weather Report (?:and Forecast )?For\s*:\s*([^\n\r]+)", text_content, re.IGNORECASE)
    if loc_match:
        result["city_name"] = loc_match.group(1).strip()

    date_match = re.search(r"Dated\s*:\s*([^\n\r]+)", text_content, re.IGNORECASE)
    if date_match:
        result["dated"] = date_match.group(1).strip()

    obs = {}
    
    # Target Table 1 (Past 24 Hours Weather Data)
    for table in soup.find_all("table"):
        table_text = table.get_text()
        if "Past 24 Hours" in table_text or "Maximum Temp" in table_text:
            rows = table.find_all("tr")
            for tr in rows:
                tds = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
                if not tds:
                    continue
                
                label = tds[0] if len(tds) > 0 else ""
                val = tds[1] if len(tds) > 1 else ""

                if "Maximum Temp" in label and "Departure" not in label:
                    obs["max_temp"] = val
                elif "Departure from Normal" in label and "max_temp" in obs and "max_temp_departure" not in obs:
                    obs["max_temp_departure"] = val
                elif "Minimum Temp" in label and "Departure" not in label:
                    obs["min_temp"] = val
                elif "Departure from Normal" in label and "min_temp" in obs and "min_temp_departure" not in obs:
                    obs["min_temp_departure"] = val
                elif "24 Hours Rainfall" in label:
                    obs["rainfall_24h"] = val
                elif "R.H. at 0830" in label:
                    obs["rh_0830"] = val
                elif "R.H. at 1730" in label:
                    obs["rh_1730"] = val
                elif "Sunset" in label:
                    obs["sunset"] = val
                elif "Sunrise" in label:
                    obs["sunrise_tomorrow"] = val
                elif "Moonset" in label:
                    obs["moonset"] = val
                elif "Moonrise" in label:
                    obs["moonrise"] = val

    result["observation"] = obs

    # Target Table 2 (7 Day's Forecast)
    forecasts = []
    for table in soup.find_all("table"):
        table_text = table.get_text()
        if "7 Day's Forecast" in table_text or "7 DAY" in table_text.upper():
            rows = table.find_all("tr")
            for tr in rows:
                tds = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
                if len(tds) >= 4:
                    date_str = tds[0]
                    # Filter out header rows
                    if date_str.upper() not in ("DATE", "DATE/TIME", "DATETIME") and not date_str.startswith("7 Day"):
                        if not any(k in date_str for k in ["Maximum", "Minimum", "Departure", "Rainfall", "R.H.", "Sunset", "Sunrise", "Moonset", "Moonrise"]):
                            forecasts.append({
                                "date": date_str,
                                "min_temp": tds[1],
                                "max_temp": tds[2],
                                "weather": tds[3],
                                "warning": tds[4] if len(tds) > 4 else None
                            })

    result["forecasts"] = forecasts
    return result
