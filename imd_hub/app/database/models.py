import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Date, ForeignKey, UniqueConstraint, Text
from sqlalchemy.orm import relationship
from .database import Base

class IMDLocation(Base):
    __tablename__ = "imd_locations"

    id = Column(Integer, primary_key=True, index=True)
    location_name = Column(String(100), nullable=False)
    normalized_name = Column(String(100), nullable=False, index=True)
    source_url = Column(String(500), nullable=False)
    forecast_url = Column(String(500), nullable=False)
    imd_city_id = Column(String(50), nullable=True, index=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    observations = relationship("WeatherObservation", back_populates="location")
    forecasts = relationship("WeatherForecast", back_populates="location")

class WeatherObservation(Base):
    __tablename__ = "weather_observations"

    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("imd_locations.id"), nullable=False, index=True)
    observation_date = Column(Date, nullable=False, index=True)
    scraped_at = Column(DateTime(timezone=True), nullable=False, index=True)

    max_temp = Column(Float, nullable=True)
    max_temp_departure = Column(Float, nullable=True)
    min_temp = Column(Float, nullable=True)
    min_temp_departure = Column(Float, nullable=True)

    rainfall_24h = Column(Float, nullable=True)

    rh_0830 = Column(Integer, nullable=True)
    rh_1730 = Column(Integer, nullable=True)

    sunset = Column(String(20), nullable=True)
    sunrise_tomorrow = Column(String(20), nullable=True)
    moonset = Column(String(20), nullable=True)
    moonrise = Column(String(20), nullable=True)

    source_url = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    location = relationship("IMDLocation", back_populates="observations")

    __table_args__ = (
        UniqueConstraint('location_id', 'observation_date', 'scraped_at', name='_loc_obs_scraped_uc'),
    )

class WeatherForecast(Base):
    __tablename__ = "weather_forecasts"

    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("imd_locations.id"), nullable=False, index=True)
    scraped_at = Column(DateTime(timezone=True), nullable=False, index=True)
    forecast_date = Column(Date, nullable=False, index=True)

    min_temp = Column(Float, nullable=True)
    max_temp = Column(Float, nullable=True)
    weather_description = Column(String(255), nullable=True)
    warning = Column(String(255), nullable=True)

    source_url = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    location = relationship("IMDLocation", back_populates="forecasts")

class ScrapeRun(Base):
    __tablename__ = "scrape_runs"

    id = Column(Integer, primary_key=True, index=True)
    started_at = Column(DateTime(timezone=True), nullable=False)
    completed_at = Column(DateTime(timezone=True), nullable=True)

    locations_found = Column(Integer, default=0)
    locations_success = Column(Integer, default=0)
    locations_failed = Column(Integer, default=0)

    status = Column(String(50), default="RUNNING") # RUNNING | SUCCESS | FAILED
    error_message = Column(Text, nullable=True)

class ScrapeError(Base):
    __tablename__ = "scrape_errors"

    id = Column(Integer, primary_key=True, index=True)
    scrape_run_id = Column(Integer, ForeignKey("scrape_runs.id"), nullable=True)
    location_id = Column(Integer, ForeignKey("imd_locations.id"), nullable=True)
    url = Column(String(500), nullable=True)
    error_type = Column(String(100), nullable=True)
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
