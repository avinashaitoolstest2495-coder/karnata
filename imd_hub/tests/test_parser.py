"""
test_parser.py
Unit tests for IMD Karnataka Weather Scraper & Validator using mocked HTML.
Does NOT make live network requests.
"""

import pytest
from app.scraper.imd_parser import parse_karnataka_index, parse_city_forecast_page
from app.scraper.validator import validate_observation, parse_float

MOCK_INDEX_HTML = """
<html>
<body>
<table>
  <tr><td>Bangalore</td><td><a href="citywxnew.php?id=43295">FORECAST</a></td></tr>
  <tr><td>Mysore</td><td><a href="citywxnew.php?id=43291">FORECAST</a></td></tr>
  <tr><td>Belgaum</td><td><a href="citywxnew.php?id=43161">FORECAST</a></td></tr>
</table>
</body>
</html>
"""

MOCK_CITY_HTML = """
<html>
<body>
<div>Local Weather Report For: Bengaluru-City</div>
<div>Dated :Aug 11, 2026</div>

<table>
  <tr><th colspan="2">Past 24 Hours Weather Data</th></tr>
  <tr><td>Maximum Temp(oC)</td><td>30.2</td></tr>
  <tr><td>Departure from Normal(oC)</td><td>2.2</td></tr>
  <tr><td>Minimum Temp (oC)</td><td>21.2</td></tr>
  <tr><td>Departure from Normal(oC)</td><td>1.1</td></tr>
  <tr><td>24 Hours Rainfall (mm)</td><td>NIL</td></tr>
  <tr><td>R.H. at 0830 hrs (%)</td><td>83</td></tr>
  <tr><td>R.H. at 1730 hrs (%)</td><td>93</td></tr>
</table>

<table>
  <tr><th colspan="4">7 DAY'S FORECAST</th></tr>
  <tr><td>11/08/2026</td><td>21.0</td><td>30.0</td><td>Generally cloudy sky with Light rain</td></tr>
  <tr><td>12/08/2026</td><td>20.0</td><td>29.5</td><td>Partly cloudy sky</td></tr>
</table>
</body>
</html>
"""

def test_parse_karnataka_index():
    locations = parse_karnataka_index(MOCK_INDEX_HTML)
    assert len(locations) == 3
    assert locations[0]["location_name"] == "Bangalore"
    assert locations[0]["imd_city_id"] == "43295"

def test_parse_city_forecast_page():
    parsed = parse_city_forecast_page(MOCK_CITY_HTML)
    assert parsed["city_name"] == "Bengaluru-City"
    obs = parsed["observation"]
    assert obs["max_temp"] == "30.2"
    assert obs["rainfall_24h"] == "NIL"
    assert len(parsed["forecasts"]) == 2

def test_nil_rainfall_validation():
    raw_obs = {"max_temp": "30.2", "min_temp": "21.2", "rainfall_24h": "NIL", "rh_0830": "83"}
    norm, errors = validate_observation(raw_obs)
    assert norm["rainfall_24h"] is None  # MUST be NULL, not 0
    assert norm["max_temp"] == 30.2
    assert norm["rh_0830"] == 83
    assert len(errors) == 0

def test_invalid_temperature_validation():
    raw_obs = {"max_temp": "75.0", "min_temp": "20.0", "rainfall_24h": "5.0"}
    norm, errors = validate_observation(raw_obs)
    assert norm["max_temp"] is None  # Invalid temp > 60 discarded
    assert len(errors) == 1

def test_suspicious_temp_check():
    raw_obs = {"max_temp": "18.0", "min_temp": "25.0"}  # Max < Min
    norm, errors = validate_observation(raw_obs)
    assert len(errors) == 1
    assert "Suspicious temp check failed" in errors[0]
