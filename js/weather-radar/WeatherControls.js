/**
 * WeatherControls.js
 * Map Controls & Layer Selector for Karnataka Weather Radar
 */

class WeatherControls {
  constructor(options = {}) {
    this.container = options.container;
    this.statusContainer = options.statusContainer;
    this.weatherMap = options.weatherMap;
    this.onLayerChange = options.onLayerChange;
    this.activeLayer = "precipitation";

    this.layers = [
      { id: "precipitation", label: "🌧 Radar", icon: "🌧", available: true },
      { id: "temperature", label: "🌡 Temperature", icon: "🌡", available: true },
      { id: "wind", label: "💨 Wind", icon: "💨", available: true },
      { id: "cloud", label: "☁ Cloud Cover", icon: "☁", available: true }
    ];

    this.render();
  }

  render() {
    if (this.container) {
      const html = `
        <div class="msn-control-pill">
          <div class="wc-layer-dropdown">
            <button class="msn-pill-btn wc-layer-btn" id="wc-active-layer-btn">
              <span>🌧 Radar</span>
              <span class="wc-arrow">▼</span>
            </button>
            <div class="wc-layer-menu" id="wc-layer-menu">
              ${this.layers.map(l => `
                <button class="wc-layer-item ${l.id === this.activeLayer ? 'active' : ''}" data-id="${l.id}">
                  <span>${l.label}</span>
                </button>
              `).join('')}
            </div>
          </div>

          <span class="msn-pill-divider"></span>

          <button class="msn-pill-btn" id="wc-zoom-out-btn" title="Zoom Out">−</button>
          <button class="msn-pill-btn" id="wc-zoom-in-btn" title="Zoom In">+</button>

          <span class="msn-pill-divider"></span>

          <button class="msn-pill-btn" id="wc-fullscreen-btn" title="Toggle Fullscreen">⛶</button>
        </div>
      `;
      this.container.innerHTML = html;
      this.bindEvents();
    }

    this.setStatus("live", "Updated " + this.getFormattedCurrentTime());
  }

  bindEvents() {
    const layerBtn = document.getElementById("wc-active-layer-btn");
    const layerMenu = document.getElementById("wc-layer-menu");
    const zoomInBtn = document.getElementById("wc-zoom-in-btn");
    const zoomOutBtn = document.getElementById("wc-zoom-out-btn");
    const fsBtn = document.getElementById("wc-fullscreen-btn");

    if (layerBtn && layerMenu) {
      layerBtn.addEventListener("click", (e) => {
        e.stopPropagation();
        layerMenu.classList.toggle("show");
      });

      document.addEventListener("click", () => layerMenu.classList.remove("show"));

      layerMenu.querySelectorAll(".wc-layer-item").forEach(item => {
        item.addEventListener("click", (e) => {
          e.stopPropagation();
          const layerId = item.dataset.id;
          const layerObj = this.layers.find(l => l.id === layerId);

          this.activeLayer = layerId;
          layerMenu.querySelectorAll(".wc-layer-item").forEach(i => i.classList.remove("active"));
          item.classList.add("active");
          layerBtn.querySelector("span").textContent = layerObj.label;
          layerMenu.classList.remove("show");

          if (typeof this.onLayerChange === "function") {
            this.onLayerChange(layerId);
          }
        });
      });
    }

    if (zoomInBtn) {
      zoomInBtn.addEventListener("click", () => {
        if (this.weatherMap) this.weatherMap.zoomIn();
      });
    }

    if (zoomOutBtn) {
      zoomOutBtn.addEventListener("click", () => {
        if (this.weatherMap) this.weatherMap.zoomOut();
      });
    }

    if (fsBtn) {
      fsBtn.addEventListener("click", () => {
        const card = document.querySelector(".weather-map-card");
        if (card) {
          if (!document.fullscreenElement) {
            card.requestFullscreen?.() || card.webkitRequestFullscreen?.();
          } else {
            document.exitFullscreen?.() || document.webkitExitFullscreen?.();
          }
        }
      });
    }
  }

  setStatus(state, message) {
    if (!this.statusContainer) return;

    let dotColor = "#10B981"; // green
    let text = message || "Live Radar";

    if (state === "updating") {
      dotColor = "#F59E0B"; // amber
      text = "Updating radar...";
    } else if (state === "error") {
      dotColor = "#EF4444"; // red
      text = "Live radar temporarily unavailable";
    }

    this.statusContainer.innerHTML = `
      <span class="wc-status-dot" style="background:${dotColor}"></span>
      <span class="wc-status-txt">${text}</span>
    `;
  }

  getFormattedCurrentTime() {
    try {
      return new Date().toLocaleTimeString("en-IN", {
        timeZone: "Asia/Kolkata",
        hour: "numeric",
        minute: "2-digit",
        hour12: true
      }) + " IST";
    } catch (e) {
      return "IST";
    }
  }
}

if (typeof window !== "undefined") {
  window.WeatherControls = WeatherControls;
}
