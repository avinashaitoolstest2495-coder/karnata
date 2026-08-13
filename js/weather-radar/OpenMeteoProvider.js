/**
 * OpenMeteoProvider.js
 * Live Weather Data Provider using Open-Meteo API (100% Free, Real-Time, No API Key)
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
  static async fetchLiveWeather(lat, lon) {
    try {
      const url = `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m&hourly=temperature_2m,precipitation_probability,weather_code&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Asia%2FKolkata`;
      const res = await fetch(url);
      if (!res.ok) throw new Error(`Open-Meteo HTTP ${res.status}`);
      const data = await res.json();
      
      const current = data.current || {};
      const codeInfo = WMO_WEATHER_CODES[current.weather_code] || { kn: "ಸಾಮಾನ್ಯ ⛅", en: "Partly Cloudy", icon: "⛅" };

      return {
        temp_c: Math.round(current.temperature_2m ?? 24),
        feels_like: Math.round(current.apparent_temperature ?? current.temperature_2m ?? 24),
        humidity: current.relative_humidity_2m ?? 80,
        wind_kmh: Math.round(current.wind_speed_10m ?? 10),
        precipitation_mm: current.precipitation ?? 0.0,
        weather_code: current.weather_code,
        desc_kn: codeInfo.kn,
        desc_en: codeInfo.en,
        icon: codeInfo.icon,
        daily_max: data.daily?.temperature_2m_max || [],
        daily_min: data.daily?.temperature_2m_min || []
      };
    } catch (e) {
      console.warn("[OpenMeteoProvider] Fetch failed, using fallback:", e);
      return null;
    }
  }
}

if (typeof window !== "undefined") {
  window.OpenMeteoProvider = OpenMeteoProvider;
  window.WMO_WEATHER_CODES = WMO_WEATHER_CODES;
}
