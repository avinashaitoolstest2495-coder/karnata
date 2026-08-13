/**
 * WeatherTimeline.js
 * MSN-style Interactive Animation Timeline for Weather Radar Map
 */

class WeatherTimeline {
  constructor(options = {}) {
    this.container = options.container;
    this.playBtn = options.playBtn;
    this.prevBtn = options.prevBtn;
    this.nextBtn = options.nextBtn;
    this.slider = options.slider;
    this.timeDisplay = options.timeDisplay;
    this.ticksContainer = options.ticksContainer;
    this.onFrameChange = options.onFrameChange;

    this.frames = [];
    this.currentIndex = 0;
    this.isPlaying = false;
    this.timer = null;
    this.speed = 600; // ms per frame

    this.bindEvents();
  }

  setFrames(frames, initialIndex) {
    this.frames = frames || [];
    if (this.frames.length === 0) return;

    this.currentIndex = (initialIndex !== undefined && initialIndex >= 0 && initialIndex < this.frames.length)
      ? initialIndex
      : this.frames.length - 1;

    if (this.slider) {
      this.slider.min = 0;
      this.slider.max = this.frames.length - 1;
      this.slider.value = this.currentIndex;
    }

    this.renderTicks();
    this.updateUI();
  }

  bindEvents() {
    if (this.playBtn) {
      this.playBtn.addEventListener("click", () => this.togglePlay());
    }

    if (this.prevBtn) {
      this.prevBtn.addEventListener("click", () => {
        this.pause();
        this.step(-1);
      });
    }

    if (this.nextBtn) {
      this.nextBtn.addEventListener("click", () => {
        this.pause();
        this.step(1);
      });
    }

    if (this.slider) {
      this.slider.addEventListener("input", (e) => {
        this.pause();
        this.goToFrame(parseInt(e.target.value, 10));
      });
    }
  }

  renderTicks() {
    if (!this.ticksContainer || this.frames.length === 0) return;
    
    const step = Math.max(1, Math.floor(this.frames.length / 5));
    let tickHtml = "";

    this.frames.forEach((f, idx) => {
      if (idx % step === 0 || idx === this.frames.length - 1 || f.isLatestPast) {
        const label = f.isLatestPast ? "NOW" : f.timeStr;
        const isNowClass = f.isLatestPast ? "wt-tick-now" : "";
        tickHtml += `<span class="wt-tick ${isNowClass}" data-idx="${idx}">${label}</span>`;
      }
    });

    this.ticksContainer.innerHTML = tickHtml;
  }

  togglePlay() {
    if (this.isPlaying) {
      this.pause();
    } else {
      this.play();
    }
  }

  play() {
    if (this.isPlaying || this.frames.length === 0) return;
    this.isPlaying = true;
    if (this.playBtn) {
      this.playBtn.innerHTML = `<svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>`;
      this.playBtn.setAttribute("aria-label", "Pause Radar Animation");
    }

    this.timer = setInterval(() => {
      this.step(1);
    }, this.speed);
  }

  pause() {
    if (!this.isPlaying) return;
    this.isPlaying = false;
    if (this.timer) {
      clearInterval(this.timer);
      this.timer = null;
    }
    if (this.playBtn) {
      this.playBtn.innerHTML = `<svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>`;
      this.playBtn.setAttribute("aria-label", "Play Radar Animation");
    }
  }

  step(direction) {
    if (this.frames.length === 0) return;
    let nextIdx = this.currentIndex + direction;

    if (nextIdx >= this.frames.length) {
      nextIdx = 0; // Loop back
    } else if (nextIdx < 0) {
      nextIdx = this.frames.length - 1;
    }

    this.goToFrame(nextIdx);
  }

  goToFrame(index) {
    if (index < 0 || index >= this.frames.length) return;
    this.currentIndex = index;
    this.updateUI();

    if (typeof this.onFrameChange === "function") {
      this.onFrameChange(this.frames[this.currentIndex], this.currentIndex);
    }
  }

  updateUI() {
    if (this.slider) {
      this.slider.value = this.currentIndex;
    }

    const currentFrame = this.frames[this.currentIndex];
    if (currentFrame && this.timeDisplay) {
      const tag = currentFrame.isLatestPast
        ? `<span class="wt-now-tag">NOW</span>`
        : (currentFrame.isNowcast ? `<span class="wt-fc-tag">FORECAST</span>` : "");

      this.timeDisplay.innerHTML = `${tag} <span class="wt-time-txt">${currentFrame.timeStr} IST</span>`;
    }
  }

  getCurrentFrame() {
    return this.frames[this.currentIndex];
  }
}

if (typeof window !== "undefined") {
  window.WeatherTimeline = WeatherTimeline;
}
