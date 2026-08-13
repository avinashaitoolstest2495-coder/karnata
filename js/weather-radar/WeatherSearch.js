/**
 * WeatherSearch.js
 * Comprehensive Karnataka City & Taluk Location Search Dataset for Weather Radar Map
 */

const KARNATAKA_CITIES_SEARCH = [
  // Major District HQ Cities
  { name_kn: "ಬೆಂಗಳೂರು", name_en: "Bengaluru", lat: 12.9716, lon: 77.5946, district: "Bengaluru Urban" },
  { name_kn: "ಮೈಸೂರು", name_en: "Mysuru", lat: 12.2958, lon: 76.6394, district: "Mysuru" },
  { name_kn: "ಮಂಗಳೂರು", name_en: "Mangaluru", lat: 12.8438, lon: 74.9919, district: "Dakshina Kannada" },
  { name_kn: "ಹುಬ್ಬಳ್ಳಿ", name_en: "Hubballi", lat: 15.3647, lon: 75.1240, district: "Dharwad" },
  { name_kn: "ಧಾರವಾಡ", name_en: "Dharwad", lat: 15.4589, lon: 75.0078, district: "Dharwad" },
  { name_kn: "ಬೆಳಗಾವಿ", name_en: "Belagavi", lat: 15.8497, lon: 74.4977, district: "Belagavi" },
  { name_kn: "ಶಿವಮೊಗ್ಗ", name_en: "Shivamogga", lat: 13.9299, lon: 75.5681, district: "Shivamogga" },
  { name_kn: "ತುಮಕೂರು", name_en: "Tumakuru", lat: 13.3379, lon: 77.1173, district: "Tumakuru" },
  { name_kn: "ಕಲಬುರಗಿ", name_en: "Kalaburagi", lat: 17.3297, lon: 76.8343, district: "Kalaburagi" },
  { name_kn: "ಬಳ್ಳಾರಿ", name_en: "Ballari", lat: 15.1394, lon: 76.9214, district: "Ballari" },
  { name_kn: "ವಿಜಯಪುರ", name_en: "Vijayapura", lat: 16.8302, lon: 75.7100, district: "Vijayapura" },
  { name_kn: "ದಾವಣಗೆರೆ", name_en: "Davangere", lat: 14.4644, lon: 75.9218, district: "Davangere" },
  { name_kn: "ಹಾಸನ", name_en: "Hassan", lat: 13.0068, lon: 76.1003, district: "Hassan" },
  { name_kn: "ಮಂಡ್ಯ", name_en: "Mandya", lat: 12.5220, lon: 76.8951, district: "Mandya" },
  { name_kn: "ಉಡುಪಿ", name_en: "Udupi", lat: 13.3409, lon: 74.7421, district: "Udupi" },
  { name_kn: "ರಾಯಚೂರು", name_en: "Raichur", lat: 16.2120, lon: 77.3439, district: "Raichur" },
  { name_kn: "ಕೋಲಾರ", name_en: "Kolar", lat: 13.1363, lon: 78.1294, district: "Kolar" },
  { name_kn: "ಚಿಕ್ಕಮಗಳೂರು", name_en: "Chikkamagaluru", lat: 13.3153, lon: 75.7754, district: "Chikkamagaluru" },
  { name_kn: "ಕೊಡಗು (ಮಡಿಕೇರಿ)", name_en: "Madikeri", lat: 12.4244, lon: 75.7382, district: "Kodagu" },
  { name_kn: "ಕಾರವಾರ", name_en: "Karwar", lat: 14.7941, lon: 74.6561, district: "Uttara Kannada" },
  { name_kn: "ಚಿತ್ರದುರ್ಗ", name_en: "Chitradurga", lat: 14.2226, lon: 76.3984, district: "Chitradurga" },
  { name_kn: "ಬಾಗಲಕೋಟೆ", name_en: "Bagalkote", lat: 16.1831, lon: 75.6965, district: "Bagalkote" },
  { name_kn: "ಯಾದಗಿರಿ", name_en: "Yadgir", lat: 16.7620, lon: 77.1382, district: "Yadgir" },
  { name_kn: "ಕೊಪ್ಪಳ", name_en: "Koppal", lat: 15.3474, lon: 76.1547, district: "Koppal" },
  { name_kn: "ವಿಜಯನಗರ (ಹೊಸಪೇಟೆ)", name_en: "Hospet", lat: 15.2689, lon: 76.3909, district: "Vijayanagara" },
  { name_kn: "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", name_en: "Chikkaballapura", lat: 13.4356, lon: 77.7310, district: "Chikkaballapura" },
  { name_kn: "ರಾಮನಗರ", name_en: "Ramanagara", lat: 12.7156, lon: 77.2817, district: "Ramanagara" },
  { name_kn: "ಚಾಮರಾಜನಗರ", name_en: "Chamarajanagara", lat: 11.9261, lon: 76.9439, district: "Chamarajanagara" },
  { name_kn: "ಬೀದರ್", name_en: "Bidar", lat: 17.9104, lon: 77.5199, district: "Bidar" },

  // Key Taluk Towns & Cities (Koppal, Gangavathi, Sindhanur, etc.)
  { name_kn: "ಗಂಗಾವತಿ", name_en: "Gangavathi", lat: 15.4326, lon: 76.5306, district: "Koppal" },
  { name_kn: "ಸಿಂಧನೂರು", name_en: "Sindhanur", lat: 15.7770, lon: 76.7592, district: "Raichur" },
  { name_kn: "ಯಲಬುರ್ಗಾ", name_en: "Yelbarga", lat: 15.6322, lon: 76.0124, district: "Koppal" },
  { name_kn: "ಕುಷ್ಟಗಿ", name_en: "Kushtagi", lat: 15.7590, lon: 76.1960, district: "Koppal" },
  { name_kn: "ಗೋಕಾಕ", name_en: "Gokak", lat: 16.1681, lon: 74.8322, district: "Belagavi" },
  { name_kn: "ರಾಣೇಬೆನ್ನೂರು", name_en: "Ranebennur", lat: 14.6238, lon: 75.6218, district: "Haveri" },
  { name_kn: "ಹಾವೇರಿ", name_en: "Haveri", lat: 14.7954, lon: 75.3992, district: "Haveri" },
  { name_kn: "ಶಿರಸಿ", name_en: "Sirsi", lat: 14.6194, lon: 74.8354, district: "Uttara Kannada" },
  { name_kn: "ಸಾಗರ", name_en: "Sagara", lat: 14.1670, lon: 75.0298, district: "Shivamogga" },
  { name_kn: "ಭದ್ರಾವತಿ", name_en: "Bhadravati", lat: 13.8409, lon: 75.7037, district: "Shivamogga" },
  { name_kn: "ಚಿಂತಾಮಣಿ", name_en: "Chintamani", lat: 13.4014, lon: 78.0583, district: "Chikkaballapura" },
  { name_kn: "ತಿಪಟೂರು", name_en: "Tiptur", lat: 13.2625, lon: 76.4770, district: "Tumakuru" },
  { name_kn: "ನಂಜನಗೂಡು", name_en: "Nanjangud", lat: 12.1190, lon: 76.6806, district: "Mysuru" },
  { name_kn: "ಕುಂದಾಪುರ", name_en: "Kundapura", lat: 13.6268, lon: 74.6914, district: "Udupi" },
  { name_kn: "ಪುತ್ತೂರು", name_en: "Puttur", lat: 12.7667, lon: 75.2000, district: "Dakshina Kannada" },
  { name_kn: "ಭಟ್ಕಳ", name_en: "Bhatkal", lat: 13.9782, lon: 74.5504, district: "Uttara Kannada" },
  { name_kn: "ದಾಂಡೇಲಿ", name_en: "Dandeli", lat: 15.2443, lon: 74.6186, district: "Uttara Kannada" },
  { name_kn: "ಕುಮಟಾ", name_en: "Kumta", lat: 14.4263, lon: 74.4069, district: "Uttara Kannada" }
];

class WeatherSearch {
  constructor(inputEl, resultsEl, onSelectCallback) {
    this.inputEl = inputEl;
    this.resultsEl = resultsEl;
    this.onSelect = onSelectCallback;
    this.hideResults();
    this.init();
  }

  init() {
    if (!this.inputEl || !this.resultsEl) return;

    this.inputEl.addEventListener("input", (e) => this.handleInput(e.target.value));
    
    document.addEventListener("click", (e) => {
      if (!this.inputEl.contains(e.target) && !this.resultsEl.contains(e.target)) {
        this.hideResults();
      }
    });
  }

  handleInput(val) {
    const q = (val || "").trim().toLowerCase();
    if (!q) {
      this.hideResults();
      return;
    }

    const matches = KARNATAKA_CITIES_SEARCH.filter(c =>
      c.name_en.toLowerCase().includes(q) ||
      c.name_kn.toLowerCase().includes(q) ||
      c.district.toLowerCase().includes(q)
    ).slice(0, 7);

    if (matches.length === 0) {
      this.resultsEl.innerHTML = `<div class="ws-no-result">No matching city found</div>`;
      this.showResults();
      return;
    }

    this.resultsEl.innerHTML = matches.map(c => `
      <div class="ws-item">
        <span class="ws-item-kn">${c.name_kn}</span>
        <span class="ws-item-en">${c.name_en} (${c.district})</span>
      </div>
    `).join('');

    this.resultsEl.querySelectorAll('.ws-item').forEach((item, idx) => {
      item.addEventListener('click', () => {
        const city = matches[idx];
        this.inputEl.value = `${city.name_kn} (${city.name_en})`;
        this.hideResults();
        if (typeof this.onSelect === 'function') {
          this.onSelect(city);
        }
      });
    });

    this.showResults();
  }

  showResults() {
    if (this.resultsEl) this.resultsEl.style.display = "block";
  }

  hideResults() {
    if (this.resultsEl) this.resultsEl.style.display = "none";
  }
}

if (typeof window !== "undefined") {
  window.KARNATAKA_CITIES_SEARCH = KARNATAKA_CITIES_SEARCH;
  window.WeatherSearch = WeatherSearch;
}
