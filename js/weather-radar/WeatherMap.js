/**
 * WeatherMap.js
 * Interactive Leaflet Map Manager for Karnataka Weather Radar
 * Features: Karnataka State Boundary Highlight, Live Cursor Hover Detection (Koppal, Gangavathi, etc.), High-Contrast Basemap
 */

class WeatherMap {
  constructor(containerId, provider, options = {}) {
    this.containerId = containerId;
    this.provider = provider;
    this.options = options;

    this.map = null;
    this.activeRadarLayer = null;
    this.cityMarkersGroup = null;
    this.boundaryLayer = null;
    this.hoverTooltip = null;
    this.selectedMarker = null;
    this.currentZoom = 7;
    this.activeMode = "precipitation";
    this.lastHoveredCity = null;
    this.onLocationSelect = options.onLocationSelect;

    // Default center: Karnataka, India
    this.defaultCenter = [15.3173, 75.7139];
    this.defaultZoom = 7;

    this.initMap();
  }

  initMap() {
    const container = document.getElementById(this.containerId);
    if (!container) return;

    // Initialize Leaflet map
    this.map = L.map(this.containerId, {
      center: this.defaultCenter,
      zoom: this.defaultZoom,
      minZoom: 5,
      maxZoom: 13,
      zoomControl: false,
      attributionControl: true
    });

    // High-Contrast CartoDB Voyager Basemap
    L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
      maxZoom: 18,
      subdomains: 'abcd',
      attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="https://carto.com/">CARTO</a> | Radar by <a href="https://www.rainviewer.com/">RainViewer</a>'
    }).addTo(this.map);

    // Highlight Karnataka State Boundary
    this.loadKarnatakaBoundary();

    // Layer group for Karnataka city badges
    this.cityMarkersGroup = L.layerGroup().addTo(this.map);

    // Populate city weather badges
    this.renderCityBadges();
    window.addEventListener('weatherDataLoaded', () => {
      this.renderCityBadges();
    });

    // Listen to zoom changes
    this.map.on('zoomend', () => {
      this.currentZoom = this.map.getZoom();
      this.renderCityBadges();
    });

    // Cursor Hover Handler (Mousemove detection across Karnataka)
    let hoverTimer = null;
    this.map.on('mousemove', (e) => {
      if (hoverTimer) clearTimeout(hoverTimer);
      hoverTimer = setTimeout(() => {
        this.handleMapHover(e.latlng.lat, e.latlng.lng);
      }, 50);
    });

    // Initial selected city pin (Bengaluru)
    this.selectCity({
      name_kn: "ಬೆಂಗಳೂರು",
      name_en: "Bengaluru",
      district: "Bengaluru Urban",
      lat: 12.9716,
      lon: 77.5946
    }, false);

    setTimeout(() => {
      if (this.map) this.map.invalidateSize();
    }, 300);

    // Map click handler
    this.map.on('click', (e) => {
      this.handleMapClick(e.latlng.lat, e.latlng.lng);
    });
  }

  async loadKarnatakaBoundary() {
    try {
      const res = await fetch('/data/karnataka_boundary.json');
      if (!res.ok) return;
      const data = await res.json();

      this.boundaryLayer = L.geoJSON(data, {
        style: {
          color: '#0284C7',
          weight: 2.5,
          opacity: 0.9,
          fillColor: '#0284C7',
          fillOpacity: 0.05
        }
      }).addTo(this.map);
    } catch (e) {
      console.warn("[WeatherMap] Boundary load warning:", e);
    }
  }

  /**
   * Double-buffered smooth radar frame rendering
   */
  setRadarFrame(frame) {
    if (!this.map || !frame || !this.provider || this.activeMode !== "precipitation") return;

    const tileUrl = this.provider.getTileUrl(frame.path, '{z}', '{x}', '{y}');

    const newLayer = L.tileLayer(tileUrl, {
      opacity: 0.85,
      zIndex: 500,
      tileSize: 256,
      maxZoom: 18
    });

    newLayer.addTo(this.map);

    newLayer.on('load', () => {
      if (this.activeRadarLayer && this.map.hasLayer(this.activeRadarLayer)) {
        this.map.removeLayer(this.activeRadarLayer);
      }
      this.activeRadarLayer = newLayer;
    });

    setTimeout(() => {
      if (this.activeRadarLayer !== newLayer && this.map.hasLayer(newLayer)) {
        if (this.activeRadarLayer && this.map.hasLayer(this.activeRadarLayer)) {
          this.map.removeLayer(this.activeRadarLayer);
        }
        this.activeRadarLayer = newLayer;
      }
    }, 1200);
  }

  renderCityBadges() {
    this.cityMarkersGroup.clearLayers();
    if (typeof KARNATAKA_CITIES_SEARCH === 'undefined') return;

    const topCityNames = ["Bengaluru", "Mysuru", "Mangaluru", "Hubballi", "Belagavi", "Kalaburagi", "Shivamogga", "Davangere", "Ballari", "Vijayapura", "Koppal", "Gangavathi"];
    
    const displayList = this.currentZoom < 8
      ? KARNATAKA_CITIES_SEARCH.filter(c => topCityNames.includes(c.name_en))
      : KARNATAKA_CITIES_SEARCH;

    displayList.forEach(city => {
      const liveW = this.getLiveWeatherForCity(city);

      let badgeVal = "24°C";
      let icon = "🌡️";
      let tempColor = "#0284C7";

      if (this.activeMode === "temperature") {
        const tempC = liveW ? Math.round(liveW.temp_c || 24) : 24;
        badgeVal = `${tempC}°C`;
        icon = "🌡️";
        tempColor = tempC > 28 ? "#EF4444" : (tempC > 24 ? "#F59E0B" : "#0284C7");
      } else if (this.activeMode === "wind") {
        const windKmh = liveW ? Math.round(liveW.wind_kmh || 12) : 12;
        badgeVal = `${windKmh} km/h`;
        icon = "💨";
        tempColor = "#2563EB";
      } else if (this.activeMode === "cloud") {
        const humidity = liveW ? Math.round(liveW.humidity || 80) : 80;
        badgeVal = `${humidity}% Cloud`;
        icon = "☁️";
        tempColor = "#475569";
      } else {
        const tempC = liveW ? Math.round(liveW.temp_c || 24) : 24;
        badgeVal = `${tempC}°C`;
        icon = "🌡️";
      }

      const badgeHtml = `
        <div class="wm-city-badge">
          <span class="wm-cb-name">${city.name_kn}</span>
          <span class="wm-cb-temp" style="color:${tempColor};">${icon} ${badgeVal}</span>
        </div>
      `;

      const markerIcon = L.divIcon({
        className: 'wm-city-badge-wrapper',
        html: badgeHtml,
        iconSize: [120, 28],
        iconAnchor: [60, 14]
      });

      const marker = L.marker([city.lat, city.lon], { icon: markerIcon });

      // Mouseover hover on marker
      marker.on('mouseover', (e) => {
        L.DomEvent.stopPropagation(e);
        this.selectCity(city, false);
      });

      marker.on('click', (e) => {
        L.DomEvent.stopPropagation(e);
        this.selectCity(city, true);
      });

      this.cityMarkersGroup.addLayer(marker);
    });
  }

  async handleMapHover(lat, lon) {
    if (typeof KARNATAKA_CITIES_SEARCH === 'undefined') return;

    let closestCity = null;
    let minDiff = 0.45; // ~45 km radius threshold

    KARNATAKA_CITIES_SEARCH.forEach(c => {
      const diff = Math.hypot(c.lat - lat, c.lon - lon);
      if (diff < minDiff) {
        minDiff = diff;
        closestCity = c;
      }
    });

    if (closestCity && closestCity.name_en !== this.lastHoveredCity) {
      this.lastHoveredCity = closestCity.name_en;
      await this.selectCity(closestCity, false);
    }
  }

  async selectCity(city, doFly = true) {
    if (!this.map || !city) return;

    if (doFly) {
      this.map.flyTo([city.lat, city.lon], 9, { duration: 1.2 });
    }

    if (this.selectedMarker) {
      this.map.removeLayer(this.selectedMarker);
    }

    this.selectedMarker = L.marker([city.lat, city.lon], {
      icon: L.divIcon({
        className: 'wm-selected-pin-wrapper',
        html: `
          <div class="wm-pin-pulse"></div>
          <div class="wm-pin-core"></div>
        `,
        iconSize: [30, 30],
        iconAnchor: [15, 15]
      })
    }).addTo(this.map);

    let liveWeather = this.getLiveWeatherForCity(city);
    if (!liveWeather && typeof OpenMeteoProvider !== 'undefined') {
      liveWeather = await OpenMeteoProvider.fetchLiveWeather(city.lat, city.lon);
    }

    if (typeof this.onLocationSelect === 'function') {
      this.onLocationSelect({
        name: `${city.name_kn} (${city.name_en})`,
        district: city.district,
        lat: city.lat,
        lon: city.lon,
        liveWeather: liveWeather
      });
    }
  }

  async handleMapClick(lat, lon) {
    const roundLat = parseFloat(lat.toFixed(4));
    const roundLon = parseFloat(lon.toFixed(4));

    let closestCity = null;
    let closestName = `Location (${roundLat}, ${roundLon})`;
    let minDiff = 0.5;

    if (typeof KARNATAKA_CITIES_SEARCH !== 'undefined') {
      KARNATAKA_CITIES_SEARCH.forEach(c => {
        const diff = Math.hypot(c.lat - roundLat, c.lon - roundLon);
        if (diff < minDiff) {
          minDiff = diff;
          closestCity = c;
          closestName = `${c.name_kn} (${c.name_en})`;
        }
      });
    }

    if (this.selectedMarker) {
      this.map.removeLayer(this.selectedMarker);
    }

    this.selectedMarker = L.marker([roundLat, roundLon], {
      icon: L.divIcon({
        className: 'wm-selected-pin-wrapper',
        html: `
          <div class="wm-pin-pulse"></div>
          <div class="wm-pin-core"></div>
        `,
        iconSize: [30, 30],
        iconAnchor: [15, 15]
      })
    }).addTo(this.map);

    let liveWeather = closestCity ? this.getLiveWeatherForCity(closestCity) : null;
    if (!liveWeather && typeof OpenMeteoProvider !== 'undefined') {
      liveWeather = await OpenMeteoProvider.fetchLiveWeather(roundLat, roundLon);
    }

    if (typeof this.onLocationSelect === 'function') {
      this.onLocationSelect({
        name: closestName,
        district: closestCity ? closestCity.district : "Karnataka",
        lat: roundLat,
        lon: roundLon,
        liveWeather: liveWeather
      });
    }
  }

    getLiveWeatherForCity(city) {
    const store = window.weatherStore || (typeof weatherStore !== 'undefined' ? weatherStore : null);
    if (!store || !store.districts) return null;

    const distKey = (city.district || '').toLowerCase().replace(/ /g, '_');
    const distObj = store.districts[distKey] ||
      Object.values(store.districts).find(d =>
        (d.hq || '').toLowerCase() === (city.name_en || '').toLowerCase() ||
        (d.name_kn || '').includes(city.name_kn) ||
        (city.name_kn || '').includes(d.name_kn)
      );

    return distObj ? distObj.current : null;
  }

  setMode(mode) {
    this.activeMode = mode;
    this.renderCityBadges();

    if (mode !== "precipitation" && this.activeRadarLayer && this.map.hasLayer(this.activeRadarLayer)) {
      this.map.removeLayer(this.activeRadarLayer);
    }
  }

  zoomIn() {
    if (this.map) this.map.zoomIn();
  }

  zoomOut() {
    if (this.map) this.map.zoomOut();
  }

  resetView() {
    if (this.map) {
      this.map.flyTo(this.defaultCenter, this.defaultZoom);
    }
  }
}

if (typeof window !== "undefined") {
  window.WeatherMap = WeatherMap;
}
