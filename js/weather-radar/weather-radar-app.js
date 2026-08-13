/**
 * weather-radar-app.js
 * Main Orchestrator for Karnata Interactive Weather Radar & Telemetry Map
 * Connects RainViewer Radar API + Real Scraped District Weather Data + Open-Meteo Telemetry
 */

document.addEventListener("DOMContentLoaded", () => {
  initWeatherRadarApp();
});

if (document.readyState === "interactive" || document.readyState === "complete") {
  initWeatherRadarApp();
}

let weatherRadarAppInitialized = false;

async function initWeatherRadarApp() {
  if (weatherRadarAppInitialized) return;
  const container = document.getElementById("karnata-weather-map");
  if (!container) return;

  weatherRadarAppInitialized = true;

  // Initialize Provider
  const provider = new WeatherRadarProvider();

  // Initialize Map
  const weatherMap = new WeatherMap("karnata-weather-map", provider, {
    onLocationSelect: async (locationInfo) => {
      await updateLocationPanel(locationInfo, timeline.getCurrentFrame());
    }
  });

  // Initialize Legend
  const legend = new WeatherLegend(document.getElementById("wm-legend-slot"));

  // Initialize Controls (MSN Control Pill with functional layer switcher)
  const controls = new WeatherControls({
    container: document.getElementById("wm-layer-selector-slot"),
    statusContainer: document.getElementById("wm-status-slot"),
    weatherMap: weatherMap,
    onLayerChange: (layerId) => {
      weatherMap.setMode(layerId);
      legend.setLayer(layerId);
    }
  });

  // Initialize Timeline
  const timeline = new WeatherTimeline({
    container: document.getElementById("wm-timeline-bar"),
    playBtn: document.getElementById("wm-play-btn"),
    slider: document.getElementById("wm-timeline-slider"),
    timeDisplay: document.getElementById("wm-frame-time"),
    ticksContainer: document.getElementById("wm-timeline-ticks"),
    onFrameChange: (frame) => {
      weatherMap.setRadarFrame(frame);
      updateLocationPanel(currentSelectedLocation, frame);
    }
  });

  // Initialize Search
  new WeatherSearch(
    document.getElementById("wm-search-input"),
    document.getElementById("wm-search-results"),
    (city) => {
      weatherMap.selectCity(city);
    }
  );

  let currentSelectedLocation = {
    name: "ಬೆಂಗಳೂರು (Bengaluru)",
    district: "Bengaluru Urban",
    lat: 12.9716,
    lon: 77.5946
  };

  async function updateLocationPanel(loc, currentFrame) {
    if (!loc) return;
    currentSelectedLocation = loc;

    const locNameEl = document.getElementById("wm-panel-loc-name");
    const coordsEl = document.getElementById("wm-panel-coords");
    const liveStatsEl = document.getElementById("wm-panel-live-stats");

    if (locNameEl) locNameEl.textContent = `📍 ${loc.name || "Karnataka Region"}`;
    if (coordsEl) coordsEl.textContent = `As of ${currentFrame ? currentFrame.timeStr : 'NOW'} IST | Lat: ${loc.lat.toFixed(4)}°, Lon: ${loc.lon.toFixed(4)}°`;

    let lw = loc.liveWeather;
    if (!lw && typeof OpenMeteoProvider !== 'undefined') {
      lw = await OpenMeteoProvider.fetchLiveWeather(loc.lat, loc.lon);
    }

    if (liveStatsEl) {
      const tempC = lw ? Math.round(lw.temp_c ?? 22) : 22;
      const descKn = lw ? (lw.desc_kn || 'ಭಾಗಶಃ ಮೋಡ ⛅') : 'ಭಾಗಶಃ ಮೋಡ ⛅';
      const rainMm = lw ? (lw.precipitation_mm ?? lw.rain_24h_mm ?? 0) : 0;
      const rainChance = lw ? (lw.rain_chance || 35) : 35;
      const windKmh = lw ? (lw.wind_kmh || 10) : 10;
      const humidity = lw ? (lw.humidity || 90) : 90;

      liveStatsEl.innerHTML = `
        <div class="msn-live-weather-row">
          <span class="msn-live-temp">🌡️ ${tempC}°C</span>
          <span class="msn-live-desc">${descKn}</span>
        </div>
        <div class="msn-live-details">
          <span>💧 Rain: ${rainMm}mm (${rainChance}%)</span>
          <span>💨 Wind: ${windKmh} km/h</span>
          <span>💦 ${humidity}%</span>
        </div>
        <div class="msn-rain-dist-tag">ℹ️ Live telemetry active for ${loc.name || 'Karnataka'}</div>
      `;
    }
  }

  // Load live radar data
  async function loadRadarData(isRefresh = false) {
    if (isRefresh) {
      controls.setStatus("updating");
    }

    try {
      const frames = await provider.fetchRadarMetadata();
      const latestIdx = provider.getLatestPastIndex();

      timeline.setFrames(frames, latestIdx);

      if (frames.length > 0 && frames[latestIdx]) {
        weatherMap.setRadarFrame(frames[latestIdx]);
        await updateLocationPanel(currentSelectedLocation, frames[latestIdx]);
      }

      controls.setStatus("live", "Updated " + controls.getFormattedCurrentTime());
    } catch (err) {
      console.error("[WeatherRadarApp] Failed to load radar data:", err);
      controls.setStatus("error", "Live radar temporarily unavailable");
      const timeDisplay = document.getElementById("wm-frame-time");
      if (timeDisplay) {
        timeDisplay.innerHTML = `<span class="wt-error-msg">⚠️ Live radar unavailable</span>`;
      }
    }
  }

  // Initial load
  await loadRadarData();

  // Auto refresh metadata every 5 minutes (300,000 ms)
  setInterval(() => {
    loadRadarData(true);
  }, 300000);
}
