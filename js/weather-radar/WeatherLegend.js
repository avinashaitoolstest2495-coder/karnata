/**
 * WeatherLegend.js
 * Dynamic Legend Scale for Weather Radar, Temperature, Wind & Cloud Cover Layers
 */

class WeatherLegend {
  constructor(containerEl) {
    this.container = containerEl;
    this.activeLayer = "precipitation";
    this.render();
  }

  setLayer(layerId) {
    this.activeLayer = layerId;
    this.render();
  }

  render() {
    if (!this.container) return;

    let title = "Precipitation Radar";
    let sub = "RainViewer Satellite";
    let gradient = "linear-gradient(to right, #86EFAC 0%, #22C55E 20%, #EAB308 45%, #F97316 65%, #EF4444 85%, #A855F7 100%)";
    let labels = [
      { text: "Light", color: "#22C55E" },
      { text: "Moderate", color: "#EAB308" },
      { text: "Heavy", color: "#F97316" },
      { text: "Severe", color: "#EF4444" }
    ];

    if (this.activeLayer === "temperature") {
      title = "Live Temperature (°C)";
      sub = "Real-Time Telemetry";
      gradient = "linear-gradient(to right, #3B82F6 0%, #06B6D4 30%, #10B981 55%, #F59E0B 80%, #EF4444 100%)";
      labels = [
        { text: "< 18°C Cool", color: "#3B82F6" },
        { text: "18-24°C Mild", color: "#10B981" },
        { text: "25-30°C Warm", color: "#F59E0B" },
        { text: "> 30°C Hot", color: "#EF4444" }
      ];
    } else if (this.activeLayer === "wind") {
      title = "Wind Speed (km/h)";
      sub = "Live Anemometer Stream";
      gradient = "linear-gradient(to right, #93C5FD 0%, #3B82F6 40%, #1D4ED8 75%, #4338CA 100%)";
      labels = [
        { text: "Light (0-10)", color: "#93C5FD" },
        { text: "Moderate (10-25)", color: "#3B82F6" },
        { text: "Strong (>25)", color: "#4338CA" }
      ];
    } else if (this.activeLayer === "cloud") {
      title = "Cloud Cover (%)";
      sub = "Infrared Satellite";
      gradient = "linear-gradient(to right, #E2E8F0 0%, #94A3B8 50%, #475569 100%)";
      labels = [
        { text: "Clear (0-20%)", color: "#64748B" },
        { text: "Partly (20-60%)", color: "#475569" },
        { text: "Overcast (60-100%)", color: "#1E293B" }
      ];
    }

    this.container.innerHTML = `
      <div class="msn-legend-card">
        <div class="msn-legend-header">
          <span class="msn-legend-title">${title}</span>
          <span class="msn-legend-sub">${sub}</span>
        </div>
        <div class="msn-legend-gradient" style="background: ${gradient};"></div>
        <div class="msn-legend-labels">
          ${labels.map(l => `<span style="color:${l.color};">${l.text}</span>`).join('')}
        </div>
      </div>
    `;
  }
}

if (typeof window !== "undefined") {
  window.WeatherLegend = WeatherLegend;
}
