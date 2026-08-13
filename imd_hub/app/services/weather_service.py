"""
weather_service.py
Query Helper & Data Aggregator Service for Public & Admin REST APIs
"""

import datetime
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.database.models import IMDLocation, WeatherObservation, WeatherForecast, ScrapeRun, ScrapeError
from app.services.translation_service import get_kannada_city_name, get_kannada_weather_desc

def get_all_karnataka_weather(db: Session) -> dict:
    locations = db.query(IMDLocation).filter(IMDLocation.active == True).all()
    
    last_run = db.query(ScrapeRun).order_by(desc(ScrapeRun.started_at)).first()
    updated_at_str = last_run.completed_at.isoformat() if last_run and last_run.completed_at else datetime.datetime.utcnow().isoformat()

    results = []
    for loc in locations:
        latest_obs = db.query(WeatherObservation).filter(
            WeatherObservation.location_id == loc.id
        ).order_by(desc(WeatherObservation.scraped_at)).first()

        latest_fc = db.query(WeatherForecast).filter(
            WeatherForecast.location_id == loc.id
        ).order_by(desc(WeatherForecast.scraped_at)).first()

        weather_desc_en = latest_fc.weather_description if latest_fc else "Partly cloudy sky"

        results.append({
            "id": loc.id,
            "name_en": loc.location_name,
            "name_kn": get_kannada_city_name(loc.location_name),
            "normalized_name": loc.normalized_name,
            "max_temp": latest_obs.max_temp if latest_obs else (latest_fc.max_temp if latest_fc else None),
            "min_temp": latest_obs.min_temp if latest_obs else (latest_fc.min_temp if latest_fc else None),
            "rainfall_24h": latest_obs.rainfall_24h if latest_obs else None,
            "humidity": {
                "0830": latest_obs.rh_0830 if latest_obs else None,
                "1730": latest_obs.rh_1730 if latest_obs else None
            },
            "weather_condition_en": weather_desc_en,
            "weather_condition_kn": get_kannada_weather_desc(weather_desc_en),
            "sunset": latest_obs.sunset if latest_obs else None,
            "sunrise_tomorrow": latest_obs.sunrise_tomorrow if latest_obs else None,
            "last_fetched": latest_obs.scraped_at.isoformat() if latest_obs else None,
            "source": "India Meteorological Department (IMD)",
            "source_url": loc.forecast_url
        })

    return {
        "status": "success",
        "updated_at": updated_at_str,
        "source": "India Meteorological Department (IMD)",
        "source_url": "https://internal.imd.gov.in/power/SRLDC/Karnatak.html",
        "locations_count": len(results),
        "locations": results
    }

def get_city_weather_details(db: Session, city_norm: str) -> dict:
    loc = db.query(IMDLocation).filter(IMDLocation.normalized_name == city_norm.lower()).first()
    if not loc:
        return {"status": "error", "message": f"City '{city_norm}' not found"}

    latest_obs = db.query(WeatherObservation).filter(
        WeatherObservation.location_id == loc.id
    ).order_by(desc(WeatherObservation.scraped_at)).first()

    forecast_records = db.query(WeatherForecast).filter(
        WeatherForecast.location_id == loc.id
    ).order_by(desc(WeatherForecast.scraped_at), WeatherForecast.forecast_date).limit(7).all()

    forecasts_list = []
    for fc in forecast_records:
        forecasts_list.append({
            "date": fc.forecast_date.isoformat(),
            "min_temp": fc.min_temp,
            "max_temp": fc.max_temp,
            "weather_en": fc.weather_description,
            "weather_kn": get_kannada_weather_desc(fc.weather_description),
            "warning": fc.warning
        })

    return {
        "status": "success",
        "name_en": loc.location_name,
        "name_kn": get_kannada_city_name(loc.location_name),
        "normalized_name": loc.normalized_name,
        "updated_at": latest_obs.scraped_at.isoformat() if latest_obs else None,
        "source": "India Meteorological Department (IMD)",
        "source_url": loc.forecast_url,
        "latest_observation": {
            "max_temp": latest_obs.max_temp if latest_obs else None,
            "max_temp_departure": latest_obs.max_temp_departure if latest_obs else None,
            "min_temp": latest_obs.min_temp if latest_obs else None,
            "min_temp_departure": latest_obs.min_temp_departure if latest_obs else None,
            "rainfall_24h": latest_obs.rainfall_24h if latest_obs else None,
            "rh_0830": latest_obs.rh_0830 if latest_obs else None,
            "rh_1730": latest_obs.rh_1730 if latest_obs else None,
            "sunset": latest_obs.sunset if latest_obs else None,
            "sunrise_tomorrow": latest_obs.sunrise_tomorrow if latest_obs else None,
            "moonset": latest_obs.moonset if latest_obs else None,
            "moonrise": latest_obs.moonrise if latest_obs else None
        },
        "forecast_7_days": forecasts_list
    }

def get_city_history(db: Session, city_norm: str, days: int = 7) -> dict:
    loc = db.query(IMDLocation).filter(IMDLocation.normalized_name == city_norm.lower()).first()
    if not loc:
        return {"status": "error", "message": f"City '{city_norm}' not found"}

    cutoff_date = datetime.date.today() - datetime.timedelta(days=days)

    observations = db.query(WeatherObservation).filter(
        WeatherObservation.location_id == loc.id,
        WeatherObservation.observation_date >= cutoff_date
    ).order_by(desc(WeatherObservation.observation_date)).all()

    history_list = []
    for obs in observations:
        history_list.append({
            "date": obs.observation_date.isoformat(),
            "scraped_at": obs.scraped_at.isoformat(),
            "max_temp": obs.max_temp,
            "min_temp": obs.min_temp,
            "rainfall_24h": obs.rainfall_24h,
            "rh_0830": obs.rh_0830,
            "rh_1730": obs.rh_1730
        })

    return {
        "status": "success",
        "name_en": loc.location_name,
        "name_kn": get_kannada_city_name(loc.location_name),
        "days": days,
        "history_count": len(history_list),
        "history": history_list
    }
