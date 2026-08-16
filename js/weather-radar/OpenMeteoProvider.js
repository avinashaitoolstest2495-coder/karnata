/**
 * OpenMeteoProvider.js
 * Live Weather Data Provider using Open-Meteo API (100% Free, Real-Time, Direct Client Fetch)
 */

const WMO_WEATHER_CODES = {
  0:  { kn: "ಶುಭ ಹವಾಮಾನ ☀️",          en: "Clear sky",          icon: "☀️" },
  1:  { kn: "ಹೆಚ್ಚಾಗಿ ಶುಭ 🌤️",          en: "Mainly clear",       icon: "🌤️" },
  2:  { kn: "ಭಾಗಶಃ ಮೋಡ ⛅",           en: "Partly cloudy",      icon: "⛅" },
  3:  { kn: "ಮೋಡ ☁️",                  en: "Overcast",           icon: "☁️" },
  45: { kn: "ಮಂಜು 🌫️",                 en: "Fog",                icon: "🌫️" },
  48: { kn: "ಐಸ್ ಮಂಜು 🌫️",             en: "Icy fog",            icon: "🌫️" },
  51: { kn: "ತುಂತುರು ಮಳೆ 🌦️",          en: "Light drizzle",      icon: "🌦️" },
  53: { kn: "ಮಧ್ಯಮ ತುಂತುರು 🌦️",        en: "Moderate drizzle",   icon: "🌦️" },
  55: { kn: "ಭಾರೀ ತುಂತುರು 🌧️",         en: "Heavy drizzle",      icon: "🌧️" },
  61: { kn: "ಹಗುರ ಮಳೆ 🌧️",             en: "Slight rain",        icon: "🌧️" },
  63: { kn: "ಮಧ್ಯಮ ಮಳೆ 🌧️",            en: "Moderate rain",      icon: "🌧️" },
  65: { kn: "ಭಾರೀ ಮಳೆ 🌧️",             en: "Heavy rain",         icon: "🌧️" },
  80: { kn: "ಮಳೆಯ ಸಾಧ್ಯತೆ 🌦️",         en: "Rain showers",       icon: "🌦️" },
  81: { kn: "ಮಳೆ ಸಾಧ್ಯ 🌧️",             en: "Rain showers",       icon: "🌧️" },
  82: { kn: "ಭಾರೀ ಮಳೆ ⚠️ 🌧️",          en: "Heavy rain showers", icon: "🌧️" },
  95: { kn: "ಗುಡುಗು ಮಳೆ ⛈️",           en: "Thunderstorm",       icon: "⛈️" },
  96: { kn: "ಆಲಿಕಲ್ಲು ⛈️",              en: "Thunderstorm + hail",icon: "⛈️" },
  99: { kn: "ತೀವ್ರ ಗುಡುಗು ⚠️⛈️",       en: "Heavy thunderstorm", icon: "⛈️" }
};

class OpenMeteoProvider {
  static liveCityCache = {};

  static async fetchLiveWeather(lat, lon) {
    try {
      const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,precipitation_probability,weather_code&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=Asia%2FKolkata`;
      const res = await fetch(url);
      if (!res.ok) throw new Error(`Open-Meteo HTTP ${res.status}`);
      const data = await res.json();
      
      const current = data.current || {};
      const codeInfo = WMO_WEATHER_CODES[current.weather_code] || { kn: "ಭಾಗಶಃ ಮೋಡ ⛅", en: "Partly Cloudy", icon: "⛅" };

      // Extract next 24 hours of hourly data
      const hourlyList = [];
      if (data.hourly && data.hourly.time) {
        const times = data.hourly.time;
        const temps = data.hourly.temperature_2m || [];
        const rains = data.hourly.precipitation_probability || [];
        const codes = data.hourly.weather_code || [];
        
        // Find current hour index matching local time
        const now = new Date();
        const localYear = now.getFullYear();
        const localMonth = String(now.getMonth() + 1).padStart(2, '0');
        const localDate = String(now.getDate()).padStart(2, '0');
        const localHour = String(now.getHours()).padStart(2, '0');
        const currentLocalHourStr = `${localYear}-${localMonth}-${localDate}T${localHour}`;
        let startIdx = times.findIndex(t => t.startsWith(currentLocalHourStr));
        if (startIdx === -1) {
          const nowTs = Date.now();
          startIdx = times.findIndex(t => new Date(t).getTime() >= nowTs - 3600000);
          if (startIdx === -1) startIdx = 0;
        }

        for (let i = startIdx; i < Math.min(startIdx + 24, times.length); i++) {
          const dt = new Date(times[i]);
          const hTime = dt.toLocaleTimeString('kn-IN', { hour: '2-digit', minute: '2-digit' });
          const wCode = codes[i] || 2;
          const wInfo = WMO_WEATHER_CODES[wCode] || { kn: "ಮೋಡ", icon: "⛅" };
          hourlyList.push({
            time: hTime,
            temp_c: Math.round(temps[i] ?? current.temperature_2m ?? 24),
            rain_chance: rains[i] ?? 0,
            icon: wInfo.icon,
            desc_kn: wInfo.kn
          });
        }
      }

      // Extract 7 days daily data
      const dailyList = [];
      if (data.daily && data.daily.time) {
        const dTimes = data.daily.time;
        const dMax = data.daily.temperature_2m_max || [];
        const dMin = data.daily.temperature_2m_min || [];
        const dRain = data.daily.precipitation_probability_max || [];
        const dCodes = data.daily.weather_code || [];
        
        for (let i = 0; i < Math.min(7, dTimes.length); i++) {
          const wCode = dCodes[i] || 2;
          const wInfo = WMO_WEATHER_CODES[wCode] || { kn: "ಭಾಗಶಃ ಮೋಡ", icon: "⛅" };
          dailyList.push({
            date: dTimes[i],
            max_temp: Math.round(dMax[i] ?? 30),
            min_temp: Math.round(dMin[i] ?? 20),
            rain_chance: dRain[i] ?? 0,
            icon: wInfo.icon,
            desc_kn: wInfo.kn
          });
        }
      }

      return {
        temp_c: Math.round(current.temperature_2m ?? 24),
        feels_like: Math.round(current.apparent_temperature ?? current.temperature_2m ?? 24),
        humidity: Math.round(current.relative_humidity_2m ?? 80),
        wind_kmh: Math.round(current.wind_speed_10m ?? 10),
        precipitation_mm: current.precipitation ?? 0.0,
        weather_code: current.weather_code,
        desc_kn: codeInfo.kn,
        desc_en: codeInfo.en,
        icon: codeInfo.icon,
        hourly_24h: hourlyList,
        forecast: dailyList
      };
    } catch (e) {
      console.warn("[OpenMeteoProvider] Fetch failed, using fallback:", e);
      return null;
    }
  }

  static async fetchBatchCitiesWeather(cities) {
    if (!cities || !cities.length) return {};
    try {
      const lats = cities.map(c => c.lat.toFixed(4)).join(',');
      const lons = cities.map(c => c.lon.toFixed(4)).join(',');
      const url = `https://api.open-meteo.com/v1/forecast?latitude=${lats}&longitude=${lons}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m&timezone=Asia%2FKolkata`;
      
      const res = await fetch(url);
      if (!res.ok) throw new Error(`Open-Meteo batch HTTP ${res.status}`);
      const list = await res.json();
      
      const results = {};
      const dataArray = Array.isArray(list) ? list : [list];

      dataArray.forEach((item, idx) => {
        const city = cities[idx];
        if (!city) return;
        const current = item.current || {};
        const codeInfo = WMO_WEATHER_CODES[current.weather_code] || { kn: "ಭಾಗಶಃ ಮೋಡ ⛅", icon: "⛅" };

        const wObj = {
          temp_c: Math.round(current.temperature_2m ?? 24),
          humidity: Math.round(current.relative_humidity_2m ?? 80),
          wind_kmh: Math.round(current.wind_speed_10m ?? 10),
          precipitation_mm: current.precipitation ?? 0,
          desc_kn: codeInfo.kn,
          icon: codeInfo.icon,
          weather_code: current.weather_code
        };

        results[city.name_en] = wObj;
        results[city.district] = wObj;
        OpenMeteoProvider.liveCityCache[city.name_en] = wObj;
      });

      return results;
    } catch (e) {
      console.warn("[OpenMeteoProvider] Batch fetch failed:", e);
      return {};
    }
  }
}

if (typeof window !== "undefined") {
  window.OpenMeteoProvider = OpenMeteoProvider;
  window.WMO_WEATHER_CODES = WMO_WEATHER_CODES;
}
