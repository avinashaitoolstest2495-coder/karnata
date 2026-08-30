/**
 * WeatherRadarProvider.js
 * Weather Provider Abstraction Layer for Karnata Website (MSN Weather Architecture)
 * Default Provider: RainViewer Public API (v2.0)
 */

const WEATHER_PROVIDER_CONFIG = {
  activeProvider: "rainviewer", // "rainviewer" | "imd" (future provider)
  rainviewer: {
    apiUrl: "https://api.rainviewer.com/public/weather-maps.json",
    defaultColorScheme: 2, // 2 = Universal Blue/Green/Yellow/Red
    smooth: 1,
    snow: 1,
    tileSize: 256
  }
};

class WeatherRadarProvider {
  constructor(config = WEATHER_PROVIDER_CONFIG) {
    this.config = config;
    this.host = "https://tilecache.rainviewer.com";
    this.frames = [];
    this.latestFrameIndex = -1;
    this.lastFetched = null;
  }

  /**
   * Fetch live radar metadata from provider
   * @returns {Promise<Array>} Array of frame objects [{ time, path, timeStr, isNowcast }, ...]
   */
  async fetchRadarFrames() {
    return await this.fetchRadarMetadata();
  }

  async fetchRadarMetadata() {
    try {
      const response = await fetch(this.config.rainviewer.apiUrl, { cache: "no-cache" });
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      
      this.host = data.host || "https://tilecache.rainviewer.com";
      const pastFrames = data.radar?.past || [];
      const nowcastFrames = data.radar?.nowcast || [];

      // Combine past & nowcast frames
      const combined = [
        ...pastFrames.map(f => ({ ...f, isNowcast: false })),
        ...nowcastFrames.map(f => ({ ...f, isNowcast: true }))
      ];

      // Format frame objects
      this.frames = combined.map((f, idx) => {
        const dateObj = new Date(f.time * 1000);
        const isLatestPast = !f.isNowcast && (idx === pastFrames.length - 1);
        return {
          time: f.time,
          path: f.path || `/v2/radar/${f.time}`,
          date: dateObj,
          timeStr: this.formatTimeIST(dateObj),
          isNowcast: f.isNowcast,
          isLatestPast: isLatestPast
        };
      });

      this.latestFrameIndex = pastFrames.length > 0 ? pastFrames.length - 1 : this.frames.length - 1;
      this.lastFetched = new Date();
      return this.frames;
    } catch (error) {
      console.warn("[WeatherRadarProvider] Metadata fetch failed:", error);
      throw error;
    }
  }

  /**
   * Construct tile URL dynamically based on RainViewer API spec
   * {host}{path}/{tileSize}/{z}/{x}/{y}/{colorScheme}/{smooth}_{snow}.png
   */
  getTileUrl(path, z, x, y) {
    const { tileSize, defaultColorScheme, smooth, snow } = this.config.rainviewer;
    return `${this.host}${path}/${tileSize}/${z}/${x}/${y}/${defaultColorScheme}/${smooth}_${snow}.png`;
  }

  /**
   * Format timestamp in India Standard Time (IST)
   */
  formatTimeIST(dateObj) {
    try {
      return dateObj.toLocaleTimeString("en-IN", {
        timeZone: "Asia/Kolkata",
        hour: "numeric",
        minute: "2-digit",
        hour12: true
      });
    } catch (e) {
      return dateObj.toTimeString().substring(0, 5);
    }
  }

  getFrames() {
    return this.frames;
  }

  getLatestPastIndex() {
    return this.latestFrameIndex;
  }
}

if (typeof window !== "undefined") {
  window.WeatherRadarProvider = WeatherRadarProvider;
  window.WEATHER_PROVIDER_CONFIG = WEATHER_PROVIDER_CONFIG;
}
