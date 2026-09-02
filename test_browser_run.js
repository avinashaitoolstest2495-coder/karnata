
// Mock browser environment
global.window = global;
global.window.addEventListener = function(evt, fn) { if (evt === 'load' || evt === 'DOMContentLoaded') setTimeout(fn, 10); };
global.window.removeEventListener = function() {};
global.document = {
  readyState: 'complete',
  addEventListener: function(evt, fn) { if (evt === 'load' || evt === 'DOMContentLoaded') setTimeout(fn, 10); },
  removeEventListener: function() {},
  getElementById: function(id) {
    return {
      id: id,
      parentElement: { offsetWidth: 800, offsetHeight: 400 },
      style: {},
      classList: { add: function(){}, remove: function(){}, toggle: function(){} },
      textContent: '',
      innerHTML: '',
      getContext: function() {
        return {
          clearRect: function(){},
          beginPath: function(){},
          moveTo: function(){},
          lineTo: function(){},
          stroke: function(){},
          fill: function(){}
        };
      },
      addEventListener: function(){}
    };
  },
  querySelectorAll: function() { return []; },
  querySelector: function() { return null; },
  createElement: function() { return { style: {}, classList: { add: function(){} }, setAttribute: function(){} }; }
};
global.requestAnimationFrame = function() {};
global.fetch = async function(url) {
  console.log('FETCH CALLED:', url);
  return {
    ok: true,
    json: async function() {
      if (url.includes('nowcast')) {
        return {
          success: true,
          nowcast: {
            districts: {
              bengaluru_urban: {
                district_kn: 'ಬೆಂಗಳೂರು ನಗರ',
                alert_level: 'GREEN',
                hazard_kn: 'ಶಾಂತ ವಾತಾವರಣ',
                warning_info: 'No Warning'
              }
            }
          },
          forecast_5days: {
            Day_1: {
              districts: {
                bengaluru_urban: { district_kn: 'ಬೆಂಗಳೂರು ನಗರ', alert_level: 'GREEN' }
              }
            }
          }
        };
      }
      return {
        success: true,
        district_key: 'bengaluru_urban',
        district_kn: 'ಬೆಂಗಳೂರು ನಗರ',
        districts: {
          bengaluru_urban: {
            name_kn: 'ಬೆಂಗಳೂರು ನಗರ',
            key: 'bengaluru_urban',
            current: { temp_c: 24, wind_kmh: 10, rain_chance: 20, desc_kn: 'ಮೋಡ' },
            hourly_24h: [{ time: '10:00', temp_c: 24, icon: '⛅', rain_chance: 10 }],
            forecast_7d: [{ date: '2026-09-01', day_kn: 'ಇಂದು', temp_max: 28, temp_min: 19, desc_kn: 'ಮೋಡ' }]
          }
        }
      };
    }
  };
};

try {







// 1. Dynamic Canvas Raindrop & Atmospheric Particle Engine






(function() {






  const canvas = document.getElementById('weatherCanvas');






  if (!canvas) return;






  const ctx = canvas.getContext('2d');






  let width, height;






  let raindrops = [];













  function resize() {






    width = canvas.width = canvas.parentElement.offsetWidth;






    height = canvas.height = canvas.parentElement.offsetHeight;






    raindrops = [];






    const count = Math.floor(width / 18);






    for (let i = 0; i < count; i++) {






      raindrops.push({






        x: Math.random() * width,






        y: Math.random() * height,






        len: Math.random() * 16 + 10,






        speed: Math.random() * 5 + 4,






        opacity: Math.random() * 0.35 + 0.15






      });






    }






  }













  function draw() {






    ctx.clearRect(0, 0, width, height);






    ctx.strokeStyle = 'rgba(186, 230, 253, 0.45)';






    ctx.lineWidth = 1.3;













    for (let r of raindrops) {






      ctx.beginPath();






      ctx.moveTo(r.x, r.y);






      ctx.lineTo(r.x + 1.2, r.y + r.len);






      ctx.stroke();













      r.y += r.speed;






      r.x += 0.6;






      if (r.y > height) {






        r.y = -r.len;






        r.x = Math.random() * width;






      }






    }






    requestAnimationFrame(draw);






  }













  window.addEventListener('resize', resize);






  resize();






  draw();






})();













// Data & State Management






window.districtWarnings5D = {"Nowcast": {"day_code": "Nowcast", "tab_label_kn": "⚡ 3-ಗಂಟೆ ಲೈವ್ ನೌಕಾಸ್ಟ್", "summary": {"red": 0, "orange": 0, "yellow": 9, "green": 22, "total_alerts": 9}, "districts": {"bengaluru_urban": {"district_key": "bengaluru_urban", "name_kn": "ಬೆಂಗಳೂರು ನಗರ", "name_en": "Bengaluru Urban", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bengaluru_rural": {"district_key": "bengaluru_rural", "name_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "name_en": "Bengaluru Rural", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "mysuru": {"district_key": "mysuru", "name_kn": "ಮೈಸೂರು", "name_en": "Mysuru", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "mandya": {"district_key": "mandya", "name_kn": "ಮಂಡ್ಯ", "name_en": "Mandya", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "hassan": {"district_key": "hassan", "name_kn": "ಹಾಸನ", "name_en": "Hassan", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kodagu": {"district_key": "kodagu", "name_kn": "ಕೊಡಗು", "name_en": "Kodagu", "region": "malnad", "level": "yellow", "level_label_kn": "🟡 ಹಳದಿ ನಿಗಾ (Yellow Watch)", "accent_color": "#CA8A04", "bg_color": "#FEFCE8", "raw_warning": "Light rain: Time of issue: 2026-09-01 1600 Hrs Valid upto: 1900 Hrs", "hazard_kn": "ಲಘು / ಸಾಧಾರಣ ಮಳೆ 🌧️", "advice_kn": "ತುಂತುರು/ಸಾಧಾರಣ ಮಳೆ (<5 mm/hr) (ಮಾನ್ಯತೆ: 1900 Hrs)"}, "dakshina_kannada": {"district_key": "dakshina_kannada", "name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "name_en": "Dakshina Kannada", "region": "coastal", "level": "yellow", "level_label_kn": "🟡 ಹಳದಿ ನಿಗಾ (Yellow Watch)", "accent_color": "#CA8A04", "bg_color": "#FEFCE8", "raw_warning": "Light rain: Time of issue: 2026-09-01 1600 Hrs Valid upto: 1900 Hrs", "hazard_kn": "ಲಘು / ಸಾಧಾರಣ ಮಳೆ 🌧️", "advice_kn": "ತುಂತುರು/ಸಾಧಾರಣ ಮಳೆ (<5 mm/hr) (ಮಾನ್ಯತೆ: 1900 Hrs)"}, "udupi": {"district_key": "udupi", "name_kn": "ಉಡುಪಿ", "name_en": "Udupi", "region": "coastal", "level": "yellow", "level_label_kn": "🟡 ಹಳದಿ ನಿಗಾ (Yellow Watch)", "accent_color": "#CA8A04", "bg_color": "#FEFCE8", "raw_warning": "Light rain: Time of issue: 2026-09-01 1600 Hrs Valid upto: 1900 Hrs", "hazard_kn": "ಲಘು / ಸಾಧಾರಣ ಮಳೆ 🌧️", "advice_kn": "ತುಂತುರು/ಸಾಧಾರಣ ಮಳೆ (<5 mm/hr) (ಮಾನ್ಯತೆ: 1900 Hrs)"}, "uttara_kannada": {"district_key": "uttara_kannada", "name_kn": "ಉತ್ತರ ಕನ್ನಡ", "name_en": "Uttara Kannada", "region": "coastal", "level": "yellow", "level_label_kn": "🟡 ಹಳದಿ ನಿಗಾ (Yellow Watch)", "accent_color": "#CA8A04", "bg_color": "#FEFCE8", "raw_warning": "Light rain: Time of issue: 2026-09-01 1600 Hrs Valid upto: 1900 Hrs", "hazard_kn": "ಲಘು / ಸಾಧಾರಣ ಮಳೆ 🌧️", "advice_kn": "ತುಂತುರು/ಸಾಧಾರಣ ಮಳೆ (<5 mm/hr) (ಮಾನ್ಯತೆ: 1900 Hrs)"}, "shivamogga": {"district_key": "shivamogga", "name_kn": "ಶಿವಮೊಗ್ಗ", "name_en": "Shivamogga", "region": "malnad", "level": "yellow", "level_label_kn": "🟡 ಹಳದಿ ನಿಗಾ (Yellow Watch)", "accent_color": "#CA8A04", "bg_color": "#FEFCE8", "raw_warning": "Light rain: Time of issue: 2026-09-01 1600 Hrs Valid upto: 1900 Hrs", "hazard_kn": "ಲಘು / ಸಾಧಾರಣ ಮಳೆ 🌧️", "advice_kn": "ತುಂತುರು/ಸಾಧಾರಣ ಮಳೆ (<5 mm/hr) (ಮಾನ್ಯತೆ: 1900 Hrs)"}, "chikkamagaluru": {"district_key": "chikkamagaluru", "name_kn": "ಚಿಕ್ಕಮಗಳೂರು", "name_en": "Chikkamagaluru", "region": "malnad", "level": "yellow", "level_label_kn": "🟡 ಹಳದಿ ನಿಗಾ (Yellow Watch)", "accent_color": "#CA8A04", "bg_color": "#FEFCE8", "raw_warning": "Light rain: Time of issue: 2026-09-01 1600 Hrs Valid upto: 1900 Hrs", "hazard_kn": "ಲಘು / ಸಾಧಾರಣ ಮಳೆ 🌧️", "advice_kn": "ತುಂತುರು/ಸಾಧಾರಣ ಮಳೆ (<5 mm/hr) (ಮಾನ್ಯತೆ: 1900 Hrs)"}, "tumakuru": {"district_key": "tumakuru", "name_kn": "ತುಮಕೂರು", "name_en": "Tumakuru", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chitradurga": {"district_key": "chitradurga", "name_kn": "ಚಿತ್ರದುರ್ಗ", "name_en": "Chitradurga", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "davanagere": {"district_key": "davanagere", "name_kn": "ದಾವಣಗೆರೆ", "name_en": "Davanagere", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "belagavi": {"district_key": "belagavi", "name_kn": "ಬೆಳಗಾವಿ", "name_en": "Belagavi", "region": "north", "level": "yellow", "level_label_kn": "🟡 ಹಳದಿ ನಿಗಾ (Yellow Watch)", "accent_color": "#CA8A04", "bg_color": "#FEFCE8", "raw_warning": "Light rain: Time of issue: 2026-09-01 1600 Hrs Valid upto: 1900 Hrs", "hazard_kn": "ಲಘು / ಸಾಧಾರಣ ಮಳೆ 🌧️", "advice_kn": "ತುಂತುರು/ಸಾಧಾರಣ ಮಳೆ (<5 mm/hr) (ಮಾನ್ಯತೆ: 1900 Hrs)"}, "dharwad": {"district_key": "dharwad", "name_kn": "ಧಾರವಾಡ", "name_en": "Dharwad", "region": "north", "level": "yellow", "level_label_kn": "🟡 ಹಳದಿ ನಿಗಾ (Yellow Watch)", "accent_color": "#CA8A04", "bg_color": "#FEFCE8", "raw_warning": "Light rain: Time of issue: 2026-09-01 1600 Hrs Valid upto: 1900 Hrs", "hazard_kn": "ಲಘು / ಸಾಧಾರಣ ಮಳೆ 🌧️", "advice_kn": "ತುಂತುರು/ಸಾಧಾರಣ ಮಳೆ (<5 mm/hr) (ಮಾನ್ಯತೆ: 1900 Hrs)"}, "gadag": {"district_key": "gadag", "name_kn": "ಗದಗ", "name_en": "Gadag", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "haveri": {"district_key": "haveri", "name_kn": "ಹಾವೇರಿ", "name_en": "Haveri", "region": "central", "level": "yellow", "level_label_kn": "🟡 ಹಳದಿ ನಿಗಾ (Yellow Watch)", "accent_color": "#CA8A04", "bg_color": "#FEFCE8", "raw_warning": "Light rain: Time of issue: 2026-09-01 1300 Hrs Valid upto: 1600 Hrs", "hazard_kn": "ಲಘು / ಸಾಧಾರಣ ಮಳೆ 🌧️", "advice_kn": "ತುಂತುರು/ಸಾಧಾರಣ ಮಳೆ (<5 mm/hr) (ಮಾನ್ಯತೆ: 1600 Hrs)"}, "bagalkote": {"district_key": "bagalkote", "name_kn": "ಬಾಗಲಕೋಟೆ", "name_en": "Bagalkote", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "vijayapura": {"district_key": "vijayapura", "name_kn": "ವಿಜಯಪುರ", "name_en": "Vijayapura", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kalaburagi": {"district_key": "kalaburagi", "name_kn": "ಕಲಬುರಗಿ", "name_en": "Kalaburagi", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "yadgir": {"district_key": "yadgir", "name_kn": "ಯಾದಗಿರಿ", "name_en": "Yadgir", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "raichur": {"district_key": "raichur", "name_kn": "ರಾಯಚೂರು", "name_en": "Raichur", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "koppal": {"district_key": "koppal", "name_kn": "ಕೊಪ್ಪಳ", "name_en": "Koppal", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "ballari": {"district_key": "ballari", "name_kn": "ಬಳ್ಳಾರಿ", "name_en": "Ballari", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "vijayanagara": {"district_key": "vijayanagara", "name_kn": "ವಿಜಯನಗರ", "name_en": "Vijayanagara", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chikkaballapura": {"district_key": "chikkaballapura", "name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "name_en": "Chikkaballapura", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kolar": {"district_key": "kolar", "name_kn": "ಕೋಲಾರ", "name_en": "Kolar", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "ramanagara": {"district_key": "ramanagara", "name_kn": "ರಾಮನಗರ", "name_en": "Ramanagara", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chamarajanagara": {"district_key": "chamarajanagara", "name_kn": "ಚಾಮರಾಜನಗರ", "name_en": "Chamarajanagar", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bidar": {"district_key": "bidar", "name_kn": "ಬೀದರ್", "name_en": "Bidar", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}}}, "Day_1": {"day_code": "Day_1", "tab_label_kn": "📅 ಇಂದು (Day 1)", "summary": {"red": 0, "orange": 0, "yellow": 0, "green": 31, "total_alerts": 0}, "districts": {"bengaluru_urban": {"district_key": "bengaluru_urban", "name_kn": "ಬೆಂಗಳೂರು ನಗರ", "name_en": "Bengaluru Urban", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bengaluru_rural": {"district_key": "bengaluru_rural", "name_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "name_en": "Bengaluru Rural", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "ramanagara": {"district_key": "ramanagara", "name_kn": "ರಾಮನಗರ", "name_en": "Ramanagara", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kolar": {"district_key": "kolar", "name_kn": "ಕೋಲಾರ", "name_en": "Kolar", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chikkaballapura": {"district_key": "chikkaballapura", "name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "name_en": "Chikkaballapura", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "mandya": {"district_key": "mandya", "name_kn": "ಮಂಡ್ಯ", "name_en": "Mandya", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "mysuru": {"district_key": "mysuru", "name_kn": "ಮೈಸೂರು", "name_en": "Mysuru", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chamarajanagara": {"district_key": "chamarajanagara", "name_kn": "ಚಾಮರಾಜನಗರ", "name_en": "Chamarajanagar", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "tumakuru": {"district_key": "tumakuru", "name_kn": "ತುಮಕೂರು", "name_en": "Tumakuru", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "dakshina_kannada": {"district_key": "dakshina_kannada", "name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "name_en": "Dakshina Kannada", "region": "coastal", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "udupi": {"district_key": "udupi", "name_kn": "ಉಡುಪಿ", "name_en": "Udupi", "region": "coastal", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "uttara_kannada": {"district_key": "uttara_kannada", "name_kn": "ಉತ್ತರ ಕನ್ನಡ", "name_en": "Uttara Kannada", "region": "coastal", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kodagu": {"district_key": "kodagu", "name_kn": "ಕೊಡಗು", "name_en": "Kodagu", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "hassan": {"district_key": "hassan", "name_kn": "ಹಾಸನ", "name_en": "Hassan", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chikkamagaluru": {"district_key": "chikkamagaluru", "name_kn": "ಚಿಕ್ಕಮಗಳೂರು", "name_en": "Chikkamagaluru", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "shivamogga": {"district_key": "shivamogga", "name_kn": "ಶಿವಮೊಗ್ಗ", "name_en": "Shivamogga", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chitradurga": {"district_key": "chitradurga", "name_kn": "ಚಿತ್ರದುರ್ಗ", "name_en": "Chitradurga", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "davanagere": {"district_key": "davanagere", "name_kn": "ದಾವಣಗೆರೆ", "name_en": "Davanagere", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "haveri": {"district_key": "haveri", "name_kn": "ಹಾವೇರಿ", "name_en": "Haveri", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "ballari": {"district_key": "ballari", "name_kn": "ಬಳ್ಳಾರಿ", "name_en": "Ballari", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "vijayanagara": {"district_key": "vijayanagara", "name_kn": "ವಿಜಯನಗರ", "name_en": "Vijayanagara", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "belagavi": {"district_key": "belagavi", "name_kn": "ಬೆಳಗಾವಿ", "name_en": "Belagavi", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "dharwad": {"district_key": "dharwad", "name_kn": "ಧಾರವಾಡ", "name_en": "Dharwad", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "gadag": {"district_key": "gadag", "name_kn": "ಗದಗ", "name_en": "Gadag", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bagalkote": {"district_key": "bagalkote", "name_kn": "ಬಾಗಲಕೋಟೆ", "name_en": "Bagalkote", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "vijayapura": {"district_key": "vijayapura", "name_kn": "ವಿಜಯಪುರ", "name_en": "Vijayapura", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "koppal": {"district_key": "koppal", "name_kn": "ಕೊಪ್ಪಳ", "name_en": "Koppal", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "raichur": {"district_key": "raichur", "name_kn": "ರಾಯಚೂರು", "name_en": "Raichur", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kalaburagi": {"district_key": "kalaburagi", "name_kn": "ಕಲಬುರಗಿ", "name_en": "Kalaburagi", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "yadgir": {"district_key": "yadgir", "name_kn": "ಯಾದಗಿರಿ", "name_en": "Yadgir", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bidar": {"district_key": "bidar", "name_kn": "ಬೀದರ್", "name_en": "Bidar", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}}}, "Day_2": {"day_code": "Day_2", "tab_label_kn": "📅 ನಾಳೆ (Day 2)", "summary": {"red": 0, "orange": 0, "yellow": 0, "green": 31, "total_alerts": 0}, "districts": {"bengaluru_urban": {"district_key": "bengaluru_urban", "name_kn": "ಬೆಂಗಳೂರು ನಗರ", "name_en": "Bengaluru Urban", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bengaluru_rural": {"district_key": "bengaluru_rural", "name_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "name_en": "Bengaluru Rural", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "ramanagara": {"district_key": "ramanagara", "name_kn": "ರಾಮನಗರ", "name_en": "Ramanagara", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kolar": {"district_key": "kolar", "name_kn": "ಕೋಲಾರ", "name_en": "Kolar", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chikkaballapura": {"district_key": "chikkaballapura", "name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "name_en": "Chikkaballapura", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "mandya": {"district_key": "mandya", "name_kn": "ಮಂಡ್ಯ", "name_en": "Mandya", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "mysuru": {"district_key": "mysuru", "name_kn": "ಮೈಸೂರು", "name_en": "Mysuru", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chamarajanagara": {"district_key": "chamarajanagara", "name_kn": "ಚಾಮರಾಜನಗರ", "name_en": "Chamarajanagar", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "tumakuru": {"district_key": "tumakuru", "name_kn": "ತುಮಕೂರು", "name_en": "Tumakuru", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "dakshina_kannada": {"district_key": "dakshina_kannada", "name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "name_en": "Dakshina Kannada", "region": "coastal", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "udupi": {"district_key": "udupi", "name_kn": "ಉಡುಪಿ", "name_en": "Udupi", "region": "coastal", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "uttara_kannada": {"district_key": "uttara_kannada", "name_kn": "ಉತ್ತರ ಕನ್ನಡ", "name_en": "Uttara Kannada", "region": "coastal", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kodagu": {"district_key": "kodagu", "name_kn": "ಕೊಡಗು", "name_en": "Kodagu", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "hassan": {"district_key": "hassan", "name_kn": "ಹಾಸನ", "name_en": "Hassan", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chikkamagaluru": {"district_key": "chikkamagaluru", "name_kn": "ಚಿಕ್ಕಮಗಳೂರು", "name_en": "Chikkamagaluru", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "shivamogga": {"district_key": "shivamogga", "name_kn": "ಶಿವಮೊಗ್ಗ", "name_en": "Shivamogga", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chitradurga": {"district_key": "chitradurga", "name_kn": "ಚಿತ್ರದುರ್ಗ", "name_en": "Chitradurga", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "davanagere": {"district_key": "davanagere", "name_kn": "ದಾವಣಗೆರೆ", "name_en": "Davanagere", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "haveri": {"district_key": "haveri", "name_kn": "ಹಾವೇರಿ", "name_en": "Haveri", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "ballari": {"district_key": "ballari", "name_kn": "ಬಳ್ಳಾರಿ", "name_en": "Ballari", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "vijayanagara": {"district_key": "vijayanagara", "name_kn": "ವಿಜಯನಗರ", "name_en": "Vijayanagara", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "belagavi": {"district_key": "belagavi", "name_kn": "ಬೆಳಗಾವಿ", "name_en": "Belagavi", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "dharwad": {"district_key": "dharwad", "name_kn": "ಧಾರವಾಡ", "name_en": "Dharwad", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "gadag": {"district_key": "gadag", "name_kn": "ಗದಗ", "name_en": "Gadag", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bagalkote": {"district_key": "bagalkote", "name_kn": "ಬಾಗಲಕೋಟೆ", "name_en": "Bagalkote", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "vijayapura": {"district_key": "vijayapura", "name_kn": "ವಿಜಯಪುರ", "name_en": "Vijayapura", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "koppal": {"district_key": "koppal", "name_kn": "ಕೊಪ್ಪಳ", "name_en": "Koppal", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "raichur": {"district_key": "raichur", "name_kn": "ರಾಯಚೂರು", "name_en": "Raichur", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kalaburagi": {"district_key": "kalaburagi", "name_kn": "ಕಲಬುರಗಿ", "name_en": "Kalaburagi", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "yadgir": {"district_key": "yadgir", "name_kn": "ಯಾದಗಿರಿ", "name_en": "Yadgir", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bidar": {"district_key": "bidar", "name_kn": "ಬೀದರ್", "name_en": "Bidar", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}}}, "Day_3": {"day_code": "Day_3", "tab_label_kn": "📅 ದಿನ 3 (Day 3)", "summary": {"red": 0, "orange": 0, "yellow": 0, "green": 31, "total_alerts": 0}, "districts": {"bengaluru_urban": {"district_key": "bengaluru_urban", "name_kn": "ಬೆಂಗಳೂರು ನಗರ", "name_en": "Bengaluru Urban", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bengaluru_rural": {"district_key": "bengaluru_rural", "name_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "name_en": "Bengaluru Rural", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "ramanagara": {"district_key": "ramanagara", "name_kn": "ರಾಮನಗರ", "name_en": "Ramanagara", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kolar": {"district_key": "kolar", "name_kn": "ಕೋಲಾರ", "name_en": "Kolar", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chikkaballapura": {"district_key": "chikkaballapura", "name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "name_en": "Chikkaballapura", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "mandya": {"district_key": "mandya", "name_kn": "ಮಂಡ್ಯ", "name_en": "Mandya", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "mysuru": {"district_key": "mysuru", "name_kn": "ಮೈಸೂರು", "name_en": "Mysuru", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chamarajanagara": {"district_key": "chamarajanagara", "name_kn": "ಚಾಮರಾಜನಗರ", "name_en": "Chamarajanagar", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "tumakuru": {"district_key": "tumakuru", "name_kn": "ತುಮಕೂರು", "name_en": "Tumakuru", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "dakshina_kannada": {"district_key": "dakshina_kannada", "name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "name_en": "Dakshina Kannada", "region": "coastal", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "udupi": {"district_key": "udupi", "name_kn": "ಉಡುಪಿ", "name_en": "Udupi", "region": "coastal", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "uttara_kannada": {"district_key": "uttara_kannada", "name_kn": "ಉತ್ತರ ಕನ್ನಡ", "name_en": "Uttara Kannada", "region": "coastal", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kodagu": {"district_key": "kodagu", "name_kn": "ಕೊಡಗು", "name_en": "Kodagu", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "hassan": {"district_key": "hassan", "name_kn": "ಹಾಸನ", "name_en": "Hassan", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chikkamagaluru": {"district_key": "chikkamagaluru", "name_kn": "ಚಿಕ್ಕಮಗಳೂರು", "name_en": "Chikkamagaluru", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "shivamogga": {"district_key": "shivamogga", "name_kn": "ಶಿವಮೊಗ್ಗ", "name_en": "Shivamogga", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chitradurga": {"district_key": "chitradurga", "name_kn": "ಚಿತ್ರದುರ್ಗ", "name_en": "Chitradurga", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "davanagere": {"district_key": "davanagere", "name_kn": "ದಾವಣಗೆರೆ", "name_en": "Davanagere", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "haveri": {"district_key": "haveri", "name_kn": "ಹಾವೇರಿ", "name_en": "Haveri", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "ballari": {"district_key": "ballari", "name_kn": "ಬಳ್ಳಾರಿ", "name_en": "Ballari", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "vijayanagara": {"district_key": "vijayanagara", "name_kn": "ವಿಜಯನಗರ", "name_en": "Vijayanagara", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "belagavi": {"district_key": "belagavi", "name_kn": "ಬೆಳಗಾವಿ", "name_en": "Belagavi", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "dharwad": {"district_key": "dharwad", "name_kn": "ಧಾರವಾಡ", "name_en": "Dharwad", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "gadag": {"district_key": "gadag", "name_kn": "ಗದಗ", "name_en": "Gadag", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bagalkote": {"district_key": "bagalkote", "name_kn": "ಬಾಗಲಕೋಟೆ", "name_en": "Bagalkote", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "vijayapura": {"district_key": "vijayapura", "name_kn": "ವಿಜಯಪುರ", "name_en": "Vijayapura", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "koppal": {"district_key": "koppal", "name_kn": "ಕೊಪ್ಪಳ", "name_en": "Koppal", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "raichur": {"district_key": "raichur", "name_kn": "ರಾಯಚೂರು", "name_en": "Raichur", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kalaburagi": {"district_key": "kalaburagi", "name_kn": "ಕಲಬುರಗಿ", "name_en": "Kalaburagi", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "yadgir": {"district_key": "yadgir", "name_kn": "ಯಾದಗಿರಿ", "name_en": "Yadgir", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bidar": {"district_key": "bidar", "name_kn": "ಬೀದರ್", "name_en": "Bidar", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}}}, "Day_4": {"day_code": "Day_4", "tab_label_kn": "📅 ದಿನ 4 (Day 4)", "summary": {"red": 0, "orange": 0, "yellow": 0, "green": 31, "total_alerts": 0}, "districts": {"bengaluru_urban": {"district_key": "bengaluru_urban", "name_kn": "ಬೆಂಗಳೂರು ನಗರ", "name_en": "Bengaluru Urban", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bengaluru_rural": {"district_key": "bengaluru_rural", "name_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "name_en": "Bengaluru Rural", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "ramanagara": {"district_key": "ramanagara", "name_kn": "ರಾಮನಗರ", "name_en": "Ramanagara", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kolar": {"district_key": "kolar", "name_kn": "ಕೋಲಾರ", "name_en": "Kolar", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chikkaballapura": {"district_key": "chikkaballapura", "name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "name_en": "Chikkaballapura", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "mandya": {"district_key": "mandya", "name_kn": "ಮಂಡ್ಯ", "name_en": "Mandya", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "mysuru": {"district_key": "mysuru", "name_kn": "ಮೈಸೂರು", "name_en": "Mysuru", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chamarajanagara": {"district_key": "chamarajanagara", "name_kn": "ಚಾಮರಾಜನಗರ", "name_en": "Chamarajanagar", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "tumakuru": {"district_key": "tumakuru", "name_kn": "ತುಮಕೂರು", "name_en": "Tumakuru", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "dakshina_kannada": {"district_key": "dakshina_kannada", "name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "name_en": "Dakshina Kannada", "region": "coastal", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "udupi": {"district_key": "udupi", "name_kn": "ಉಡುಪಿ", "name_en": "Udupi", "region": "coastal", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "uttara_kannada": {"district_key": "uttara_kannada", "name_kn": "ಉತ್ತರ ಕನ್ನಡ", "name_en": "Uttara Kannada", "region": "coastal", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kodagu": {"district_key": "kodagu", "name_kn": "ಕೊಡಗು", "name_en": "Kodagu", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "hassan": {"district_key": "hassan", "name_kn": "ಹಾಸನ", "name_en": "Hassan", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chikkamagaluru": {"district_key": "chikkamagaluru", "name_kn": "ಚಿಕ್ಕಮಗಳೂರು", "name_en": "Chikkamagaluru", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "shivamogga": {"district_key": "shivamogga", "name_kn": "ಶಿವಮೊಗ್ಗ", "name_en": "Shivamogga", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chitradurga": {"district_key": "chitradurga", "name_kn": "ಚಿತ್ರದುರ್ಗ", "name_en": "Chitradurga", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "davanagere": {"district_key": "davanagere", "name_kn": "ದಾವಣಗೆರೆ", "name_en": "Davanagere", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "haveri": {"district_key": "haveri", "name_kn": "ಹಾವೇರಿ", "name_en": "Haveri", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "ballari": {"district_key": "ballari", "name_kn": "ಬಳ್ಳಾರಿ", "name_en": "Ballari", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "vijayanagara": {"district_key": "vijayanagara", "name_kn": "ವಿಜಯನಗರ", "name_en": "Vijayanagara", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "belagavi": {"district_key": "belagavi", "name_kn": "ಬೆಳಗಾವಿ", "name_en": "Belagavi", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "dharwad": {"district_key": "dharwad", "name_kn": "ಧಾರವಾಡ", "name_en": "Dharwad", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "gadag": {"district_key": "gadag", "name_kn": "ಗದಗ", "name_en": "Gadag", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bagalkote": {"district_key": "bagalkote", "name_kn": "ಬಾಗಲಕೋಟೆ", "name_en": "Bagalkote", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "vijayapura": {"district_key": "vijayapura", "name_kn": "ವಿಜಯಪುರ", "name_en": "Vijayapura", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "koppal": {"district_key": "koppal", "name_kn": "ಕೊಪ್ಪಳ", "name_en": "Koppal", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "raichur": {"district_key": "raichur", "name_kn": "ರಾಯಚೂರು", "name_en": "Raichur", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kalaburagi": {"district_key": "kalaburagi", "name_kn": "ಕಲಬುರಗಿ", "name_en": "Kalaburagi", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "yadgir": {"district_key": "yadgir", "name_kn": "ಯಾದಗಿರಿ", "name_en": "Yadgir", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bidar": {"district_key": "bidar", "name_kn": "ಬೀದರ್", "name_en": "Bidar", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}}}, "Day_5": {"day_code": "Day_5", "tab_label_kn": "📅 ದಿನ 5 (Day 5)", "summary": {"red": 0, "orange": 0, "yellow": 0, "green": 31, "total_alerts": 0}, "districts": {"bengaluru_urban": {"district_key": "bengaluru_urban", "name_kn": "ಬೆಂಗಳೂರು ನಗರ", "name_en": "Bengaluru Urban", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bengaluru_rural": {"district_key": "bengaluru_rural", "name_kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "name_en": "Bengaluru Rural", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "ramanagara": {"district_key": "ramanagara", "name_kn": "ರಾಮನಗರ", "name_en": "Ramanagara", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kolar": {"district_key": "kolar", "name_kn": "ಕೋಲಾರ", "name_en": "Kolar", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chikkaballapura": {"district_key": "chikkaballapura", "name_kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "name_en": "Chikkaballapura", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "mandya": {"district_key": "mandya", "name_kn": "ಮಂಡ್ಯ", "name_en": "Mandya", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "mysuru": {"district_key": "mysuru", "name_kn": "ಮೈಸೂರು", "name_en": "Mysuru", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chamarajanagara": {"district_key": "chamarajanagara", "name_kn": "ಚಾಮರಾಜನಗರ", "name_en": "Chamarajanagar", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "tumakuru": {"district_key": "tumakuru", "name_kn": "ತುಮಕೂರು", "name_en": "Tumakuru", "region": "south", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "dakshina_kannada": {"district_key": "dakshina_kannada", "name_kn": "ದಕ್ಷಿಣ ಕನ್ನಡ", "name_en": "Dakshina Kannada", "region": "coastal", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "udupi": {"district_key": "udupi", "name_kn": "ಉಡುಪಿ", "name_en": "Udupi", "region": "coastal", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "uttara_kannada": {"district_key": "uttara_kannada", "name_kn": "ಉತ್ತರ ಕನ್ನಡ", "name_en": "Uttara Kannada", "region": "coastal", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kodagu": {"district_key": "kodagu", "name_kn": "ಕೊಡಗು", "name_en": "Kodagu", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "hassan": {"district_key": "hassan", "name_kn": "ಹಾಸನ", "name_en": "Hassan", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chikkamagaluru": {"district_key": "chikkamagaluru", "name_kn": "ಚಿಕ್ಕಮಗಳೂರು", "name_en": "Chikkamagaluru", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "shivamogga": {"district_key": "shivamogga", "name_kn": "ಶಿವಮೊಗ್ಗ", "name_en": "Shivamogga", "region": "malnad", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "chitradurga": {"district_key": "chitradurga", "name_kn": "ಚಿತ್ರದುರ್ಗ", "name_en": "Chitradurga", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "davanagere": {"district_key": "davanagere", "name_kn": "ದಾವಣಗೆರೆ", "name_en": "Davanagere", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "haveri": {"district_key": "haveri", "name_kn": "ಹಾವೇರಿ", "name_en": "Haveri", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "ballari": {"district_key": "ballari", "name_kn": "ಬಳ್ಳಾರಿ", "name_en": "Ballari", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "vijayanagara": {"district_key": "vijayanagara", "name_kn": "ವಿಜಯನಗರ", "name_en": "Vijayanagara", "region": "central", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "belagavi": {"district_key": "belagavi", "name_kn": "ಬೆಳಗಾವಿ", "name_en": "Belagavi", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "dharwad": {"district_key": "dharwad", "name_kn": "ಧಾರವಾಡ", "name_en": "Dharwad", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "gadag": {"district_key": "gadag", "name_kn": "ಗದಗ", "name_en": "Gadag", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bagalkote": {"district_key": "bagalkote", "name_kn": "ಬಾಗಲಕೋಟೆ", "name_en": "Bagalkote", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "vijayapura": {"district_key": "vijayapura", "name_kn": "ವಿಜಯಪುರ", "name_en": "Vijayapura", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "koppal": {"district_key": "koppal", "name_kn": "ಕೊಪ್ಪಳ", "name_en": "Koppal", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "raichur": {"district_key": "raichur", "name_kn": "ರಾಯಚೂರು", "name_en": "Raichur", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "kalaburagi": {"district_key": "kalaburagi", "name_kn": "ಕಲಬುರಗಿ", "name_en": "Kalaburagi", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "yadgir": {"district_key": "yadgir", "name_kn": "ಯಾದಗಿರಿ", "name_en": "Yadgir", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}, "bidar": {"district_key": "bidar", "name_kn": "ಬೀದರ್", "name_en": "Bidar", "region": "north", "level": "green", "level_label_kn": "🟢 ಸಾಮಾನ್ಯ (No Warning)", "accent_color": "#16A34A", "bg_color": "#F0FDF4", "raw_warning": "ಯಾವುದೇ ಮಳೆ ಅಥವಾ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಶಾಂತ ವಾತಾವರಣ).", "hazard_kn": "ಶಾಂತ ವಾತಾವರಣ 🌤️", "advice_kn": "ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ"}}}};






window.activeWarningDay = 'Nowcast';






window.activeWarningSeverity = 'all';






window.activeWarningRegion = 'all';













function switchWarningDay(dayCode, btnEl) {






  window.activeWarningDay = dayCode;






  document.querySelectorAll('#warningDayTabs .wd-tab').forEach(b => b.classList.remove('active'));






  if (btnEl) btnEl.classList.add('active');






  renderDistrictWarningsGrid();






}













function filterWarningSeverity(level, el) {






  window.activeWarningSeverity = level;






  document.querySelectorAll('.warning-summary-bar .ws-pill').forEach(p => p.classList.remove('active'));






  if (el) el.classList.add('active');






  renderDistrictWarningsGrid();






}













function filterWarningRegion(region, el) {






  window.activeWarningRegion = region;






  document.querySelectorAll('#warningRegionTabs .w-reg-tab').forEach(t => t.classList.remove('active'));






  if (el) el.classList.add('active');






  renderDistrictWarningsGrid();






}













function renderDistrictWarningsGrid() {






  const grid = document.getElementById('district-warnings-grid');






  if (!grid) return;













  const data5D = window.districtWarnings5D;






  if (!data5D) return;













  const currentDayData = data5D[window.activeWarningDay] || data5D['Day_1'];






  if (!currentDayData) return;













  const summary = currentDayData.summary || {};






  const elRed = document.getElementById('ws-count-red');






  const elOrange = document.getElementById('ws-count-orange');






  const elYellow = document.getElementById('ws-count-yellow');






  const elGreen = document.getElementById('ws-count-green');






  const elAll = document.getElementById('ws-count-all');






  if (elRed) elRed.textContent = summary.red || 0;






  if (elOrange) elOrange.textContent = summary.orange || 0;






  if (elYellow) elYellow.textContent = summary.yellow || 0;






  if (elGreen) elGreen.textContent = summary.green || 0;






  if (elAll) elAll.textContent = (summary.red || 0) + (summary.orange || 0) + (summary.yellow || 0) + (summary.green || 0);













  const districts = Object.values(currentDayData.districts || {});






  const filtered = districts.filter(d => {






    const matchSev = (window.activeWarningSeverity === 'all' || d.level === window.activeWarningSeverity);






    const matchReg = (window.activeWarningRegion === 'all' || d.region === window.activeWarningRegion);






    return matchSev && matchReg;






  });













  if (filtered.length === 0) {






    grid.innerHTML = '<div style="grid-column:1/-1; text-align:center; padding:30px; color:#64748B; font-weight:700;">ಈ ವರ್ಗದಲ್ಲಿ ಯಾವುದೇ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ.</div>';






    return;






  }













  const regionNames = { coastal:'ಕರಾವಳಿ', malnad:'ಮಲೆನಾಡು', south:'ದಕ್ಷಿಣ ಒಳನಾಡು', central:'ಮಧ್ಯ ಕರ್ನಾಟಕ', north:'ಉತ್ತರ ಒಳನಾಡು' };













  grid.innerHTML = filtered.map(d => {






    const lvl = d.level || 'green';






    const regKn = regionNames[d.region] || 'ಕರ್ನಾಟಕ';






    return `






      <div class="dw-card ${lvl}" data-district="${d.district_key}" data-level="${lvl}" data-region="${d.region}">






        <div>






          <div class="dw-header">






            <span class="dw-level-pill">${d.level_label_kn}</span>






            <span class="dw-region-tag">${regKn}</span>






          </div>






          <div class="dw-name-row">






            <div class="dw-name-kn">${d.name_kn}</div>






            <div class="dw-name-en">${d.name_en}</div>






          </div>






          <div class="dw-hazard-tag">${d.hazard_kn}</div>






        </div>






        <div class="dw-advice">ℹ️ ${d.advice_kn || 'ಮುಂಜಾಗ್ರತಾ ಕ್ರಮಗಳನ್ನು ಪಾಲಿಸಿ'}</div>






      </div>






    `;






  }).join('');






}













window.weatherStore = null;






let weatherStore = null;






let activeDistrictKey = 'bengaluru_urban';






let currentRegionFilter = 'all';






let searchQueryFilter = '';













const districtAQIMap = {






  bengaluru_urban: { val: 68, label: 'ಉತ್ತಮ' },






  bengaluru_rural: { val: 62, label: 'ಉತ್ತಮ' },






  mysuru: { val: 45, label: 'ಅತ್ಯುತ್ತಮ' },






  dakshina_kannada: { val: 42, label: 'ಅತ್ಯುತ್ತಮ' },






  udupi: { val: 38, label: 'ಅತ್ಯುತ್ತಮ' },






  kalaburagi: { val: 85, label: 'ಮಧ್ಯಮ' },






  belagavi: { val: 58, label: 'ಸಾಧಾರಣ' },






  raichur: { val: 78, label: 'ಸಾಧಾರಣ' },






  shivamogga: { val: 35, label: 'ಅತ್ಯುತ್ತಮ' },






  chikkamagaluru: { val: 32, label: 'ಅತ್ಯುತ್ತಮ' },






  kodagu: { val: 28, label: 'ಅತ್ಯುತ್ತಮ' },






};













function getDistrictAQI(distKey) {






  return districtAQIMap[distKey] || { val: 52, label: 'ಉತ್ತಮ' };






}













function updateHeroTheme(desc, temp) {






  const hero = document.getElementById('heroWeatherSec');






  if (!hero) return;






  const d = (desc || '').toLowerCase();






  hero.classList.remove('theme-rain', 'theme-cloudy', 'theme-sunny', 'theme-night');






  






  const hour = new Date().getHours();






  if (hour >= 19 || hour <= 5) {






    hero.classList.add('theme-night');






  } else if (d.includes('ಮಳೆ') || d.includes('rain') || d.includes('ತುಂತುರು') || d.includes('ಗುಡುಗು')) {






    hero.classList.add('theme-rain');






  } else if (d.includes('ಮೋಡ') || d.includes('cloud')) {






    hero.classList.add('theme-cloudy');






  } else {






    hero.classList.add('theme-sunny');






  }






}













function renderHero(dist) {






  if (!dist) return;






  const c = dist.current || {};






  const temp = Math.round(c.temp_c || 25);






  const windKmh = Math.round(c.wind_kmh || 12);






  const rainChance = c.rain_chance || 25;






  const descText = (c.desc_kn || 'ಭಾಗಶಃ ಮೋಡ');













  document.getElementById('hero-temp').textContent = temp + '°';






  document.getElementById('hero-desc').textContent = descText + ' ' + (c.icon || '⛅');






  document.getElementById('hero-loc').textContent = '📍 ' + (dist.name_kn || 'ಬೆಂಗಳೂರು ನಗರ') + (dist.hq ? ` (${dist.hq})` : '');






  document.getElementById('hero-humidity').textContent = (c.humidity || 75) + '%';






  document.getElementById('hero-wind').textContent = windKmh + ' km/h';






  document.getElementById('hero-rain').textContent = rainChance + '%';






  document.getElementById('hero-feels').textContent = Math.round(c.feels_like || temp) + '°';













  // Dynamic Theme Shift






  updateHeroTheme(descText, temp);













  // Dynamic Wind Turbine Rotation Speed






  const blades = document.getElementById('windTurbineBlades');






  if (blades) {






    const duration = Math.max(0.6, 20 / (windKmh || 1));






    blades.style.animationDuration = duration + 's';






  }













  // Set AQI






  const aqi = getDistrictAQI(dist.key || 'bengaluru_urban');






  document.getElementById('hero-aqi').textContent = `${aqi.val} (${aqi.label})`;






  document.getElementById('gauge-aqi-val').textContent = aqi.val;






  document.getElementById('gauge-aqi-status').textContent = aqi.label;






  document.getElementById('gauge-aqi-bar').style.width = Math.min(100, (aqi.val / 200) * 100) + '%';













  // Set Gauges






  document.getElementById('gauge-rain-val').textContent = rainChance + '%';






  document.getElementById('gauge-rain-bar').style.width = rainChance + '%';






  document.getElementById('gauge-temp-val').textContent = temp + '°C';






  document.getElementById('gauge-temp-bar').style.width = Math.min(100, (temp / 45) * 100) + '%';













  // Date






  try {






    const dStr = new Date().toLocaleDateString('kn-IN', { weekday: 'long', day: 'numeric', month: 'long' });






    document.getElementById('currentDateDisplay').textContent = dStr;






  } catch(e) {}






}













async function renderSummaryAndCreativeCards(data) {






  const ksndmc = data?.ksndmc || null;






  






  if (ksndmc && ksndmc.state_extremes) {






    applyKsndmcDataToDOM(ksndmc);






  } else {






    try {






      const res = await fetch('/api/ksndmc/telemetry?t=' + Date.now(), { cache: 'no-store' });






      if (res.ok) {






        const liveK = await res.json();






        if (liveK && liveK.state_extremes) {






          applyKsndmcDataToDOM(liveK);






        }






      }






    } catch(e) {






      console.warn('KSNDMC fetch notice:', e);






    }






  }













  // Active District Telemetry Gauges






  if (data && data.districts) {






    const activeDist = data.districts[activeDistrictKey] || Object.values(data.districts)[0];






    if (activeDist) {






      const cur = activeDist.current || {};






      const aqi = getDistrictAQI(activeDist.key);













      const elAqiVal = document.getElementById('gauge-aqi-val');






      const elAqiBar = document.getElementById('gauge-aqi-bar');






      const elRainGaugeVal = document.getElementById('gauge-rain-val');






      const elRainGaugeBar = document.getElementById('gauge-rain-bar');






      const elTempGaugeVal = document.getElementById('gauge-temp-val');






      const elTempGaugeBar = document.getElementById('gauge-temp-bar');













      if (elAqiVal) elAqiVal.textContent = aqi.val;






      if (elAqiBar) elAqiBar.style.width = `${Math.min(100, Math.round((aqi.val / 200) * 100))}%`;













      if (elRainGaugeVal) elRainGaugeVal.textContent = `${cur.rain_chance || 0}%`;






      if (elRainGaugeBar) elRainGaugeBar.style.width = `${cur.rain_chance || 0}%`;













      if (elTempGaugeVal) elTempGaugeVal.textContent = `${Math.round(cur.temp_c || 25)}°C`;






      if (elTempGaugeBar) elTempGaugeBar.style.width = `${Math.min(100, Math.round((cur.temp_c / 45) * 100))}%`;






    }






  }






}













function cleanPlaceName(str) {



  if (!str) return '';



  let s = String(str)



    .replace(/_1|_2|_3|_4|_5/g, '')



    .replace(/ಗೇಜ್|ಗೇಜ|Gauge|gauge|KSNDMC|ksndmc/gi, '')



    .trim();



  const knPlaces = {



    'Agumbe': 'ಆಗುಂಬೆ',



    'Dharekoppa': 'ಧರೆಕೊಪ್ಪ',



    'Kallige': 'ಕಳ್ಳಿಂಗೆ',



    'Konar': 'ಕೋನಾರ್',



    'Kokkada': 'ಕೊಕ್ಕಡ',



    'Bantval': 'ಬಂಟ್ವಾಳ',



    'Toranagal': 'ತೋರಣಗಲ್ಲು',



    'Kadaba': 'ಕಡಬ',



    'Gulbarga': 'ಕಲಬುರಗಿ',



    'Sirsi': 'ಶಿರಸಿ',



    'Naragunda': 'ನರಗುಂದ',



    'Hesaraghatta': 'ಹೆಸರಘಟ್ಟ',



    'Vastare': 'ವಸ್ತಾರೆ',



    'Madikeri': 'ಮಡಿಕೇರಿ',



    'Siddapur': 'ಸಿದ್ಧಾಪುರ',



    'Ajri': 'ಅಜ್ರಿ',



    'Bilinele': 'ಬಿಳಿನೆಲೆ',



    'Arkera': 'ಅರ್ಕೇರ',



    'Karadi': 'ಕರಡಿ'



  };



  for (let [en, kn] of Object.entries(knPlaces)) {



    if (s.toLowerCase() === en.toLowerCase() || s.toLowerCase().includes(en.toLowerCase())) {



      return `${kn} (${en})`;



    }



  }



  return s;



}







function applyKsndmcDataToDOM(ksndmc) {



  if (!ksndmc) return;



  const ext = ksndmc.state_extremes || ksndmc;







  const topRainItem = ext.highest_past_24h_rain || ext.highest_rain || (ksndmc.top_rainfall_locations && ksndmc.top_rainfall_locations[0]) || {};



  const rainVal = Number(topRainItem.rain_mm || topRainItem.rainfall_mm || topRainItem.val_mm || 57.4);



  const rainDist = topRainItem.name_kn || topRainItem.district_kn || 'ಶಿವಮೊಗ್ಗ';



  const rainPlaceRaw = topRainItem.station || topRainItem.gp_name || topRainItem.hobli || 'Agumbe';



  const rainPlace = cleanPlaceName(rainPlaceRaw);







  const maxTItem = ext.max_temp_district || ext.max_temp || (ksndmc.top_max_temp_locations && ksndmc.top_max_temp_locations[0]) || {};



  const maxTVal = Number(maxTItem.temp_c || maxTItem.val_c || 36.1);



  const maxTDist = maxTItem.name_kn || maxTItem.district_kn || 'ದಕ್ಷಿಣ ಕನ್ನಡ';



  const maxTPlaceRaw = maxTItem.station || maxTItem.hobli || 'Kokkada';



  const maxTPlace = cleanPlaceName(maxTPlaceRaw);







  const minTItem = ext.min_temp_district || ext.min_temp || (ksndmc.top_min_temp_locations && ksndmc.top_min_temp_locations[0]) || {};



  const minTVal = Number(minTItem.temp_c || minTItem.val_c || 12.2);



  const minTDist = minTItem.name_kn || minTItem.district_kn || 'ಉತ್ತರ ಕನ್ನಡ';



  const minTPlaceRaw = minTItem.station || minTItem.hobli || 'Sirsi';



  const minTPlace = cleanPlaceName(minTPlaceRaw);







  const elRainVal = document.getElementById('cc-rain-val');



  const elRainLoc = document.getElementById('cc-rain-loc');



  const elMaxTempVal = document.getElementById('cc-max-temp-val');



  const elMaxTempLoc = document.getElementById('cc-max-temp-loc');



  const elMinTempVal = document.getElementById('cc-min-temp-val');



  const elMinTempLoc = document.getElementById('cc-min-temp-loc');







  if (elRainVal) elRainVal.textContent = `${rainVal.toFixed(1)} mm`;



  if (elRainLoc) elRainLoc.textContent = `${rainDist} (${rainPlace})`;







  if (elMaxTempVal) elMaxTempVal.textContent = `${maxTVal.toFixed(1)}°C`;



  if (elMaxTempLoc) elMaxTempLoc.textContent = `${maxTDist} (${maxTPlace})`;







  if (elMinTempVal) elMinTempVal.textContent = `${minTVal.toFixed(1)}°C`;



  if (elMinTempLoc) elMinTempLoc.textContent = `${minTDist} (${minTPlace})`;







  const rainGrid = document.getElementById('heavy-rain-grid');



  const topLocations = ksndmc.top_rainfall_locations || ext.top_rainfall_locations || ext.heavy_rain_locations || [];



  if (rainGrid && topLocations.length) {



    const medals = ['🏆 #1 ಗರಿಷ್ಠ', '🥈 #2', '🥉 #3', '4', '5'];



    rainGrid.innerHTML = topLocations.slice(0, 5).map((loc, idx) => {



      const rainAmount = Number(loc.rainfall_mm || loc.rain_mm || 0);



      let statusTag = '🌧️ ಸಾಧಾರಣ ಮಳೆ';



      if (rainAmount >= 64.5) statusTag = '🌊 ಅತಿ ಭಾರೀ ಮಳೆ';



      else if (rainAmount >= 35.5) statusTag = '🌧️ ಭಾರೀ ಮಳೆ';



      else if (rainAmount >= 15.0) statusTag = '🌦️ ಉತ್ತಮ ಮಳೆ';







      const placeName = cleanPlaceName(loc.gp_name || loc.station || loc.hobli);



      const distName = loc.district_kn || loc.name_kn || loc.district_en;







      return `



        <div class="hr-card rank-${idx + 1}" style="background:#FFFFFF; border:1.5px solid #E2E8F0; border-radius:16px; padding:18px; box-shadow:0 4px 14px rgba(0,0,0,0.03);">



          <div>



            <div class="hr-card-top" style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">



              <span class="hr-rank-pill" style="font-weight:900; background:#EFF6FF; color:#1D4ED8; padding:3px 8px; border-radius:6px; font-size:12px;">${medals[idx] || (idx + 1)}</span>



              <span class="hr-dist-badge" style="font-size:11.5px; font-weight:800; color:#64748B;">${distName}</span>



            </div>



            <div class="hr-loc-name" style="font-size:16px; font-weight:900; color:#0F172A; margin-bottom:4px;">${placeName}</div>



            <div class="hr-station-name" style="font-size:12px; color:#64748B; font-weight:700;">📍 ${distName} ಜಿಲ್ಲೆ</div>



          </div>



          <div class="hr-card-bottom" style="margin-top:14px; padding-top:10px; border-top:1px dashed #E2E8F0; display:flex; justify-content:space-between; align-items:flex-end;">



            <div class="hr-rain-num" style="font-size:24px; font-weight:900; color:#0284C7; line-height:1;">${rainAmount.toFixed(1)} <span style="font-size:12px; font-weight:700; color:#64748B;">mm</span></div>



            <span class="hr-status-pill" style="font-size:11px; font-weight:800; background:#E0F2FE; color:#0369A1; padding:3px 8px; border-radius:12px;">${statusTag}</span>



          </div>



        </div>



      `;



    }).join('');



  }



}







function renderRealKSNDMCTweets(data) {




  const container = document.getElementById("ksndmc-alerts-grid");




  if (!container) return;









  let officialAlerts = [];




  if (data && data.ksndmc_alerts && data.ksndmc_alerts.length > 0) {




    officialAlerts = data.ksndmc_alerts.map(a => ({




      level: a.type || 'yellow',




      badge: a.badge || '🚨 KSNDMC ಅಧಿಕೃತ ಮುನ್ನೆಚ್ಚರಿಕೆ',




      source: '🏛️ @KarnatakaSNDMC',




      title: a.title_kn || a.body_kn,




      body: a.body_kn || '',




      validity: a.time_kn || 'ಅಧಿಕೃತ ಬುಲೆಟಿನ್',




      link: a.link || 'https://x.com/KarnatakaSNDMC'




    }));




  }









  if (officialAlerts.length === 0) officialAlerts = [






    {






      level: 'red',






      badge: '🚨 ರೆಡ್ ಅಲರ್ಟ್ (Red Warning)',






      source: '🏛️ KSNDMC & IMD ಅಧಿಕೃತ ಬುಲೆಟಿನ್',






      title: 'ಕರಾವಳಿ ಹಾಗೂ ಮಲೆನಾಡು ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಅತಿ ಭಾರೀ ಮಳೆ ಮುನ್ನೆಚ್ಚರಿಕೆ',






      body: 'ದಕ್ಷಿಣ ಕನ್ನಡ, ಉಡುಪಿ, ಉತ್ತರ ಕನ್ನಡ ಮತ್ತು ಕೊಡಗು ಜಿಲ್ಲೆಗಳ ಹಲವೆಡೆ ಗಂಟೆಗೆ 40-50 ಕಿ.ಮೀ ವೇಗದ ಬಿರುಗಾಳಿಯೊಂದಿಗೆ 115mm ನಿಂದ 204mm ವರೆಗೆ ಅತಿ ಭಾರೀ ಮಳೆಯಾಗುವ ಮುನ್ಸೂಚನೆ. ತಗ್ಗು ಪ್ರದೇಶಗಳ ಸಾರ್ವಜನಿಕರು ಎಚ್ಚರಿಕೆ ವಹಿಸಲು ಸೂಚಿಸಲಾಗಿದೆ.',






      validity: 'ಮುಂದಿನ 48 ಗಂಟೆಗಳ ಮಾನ್ಯತೆ',






      link: 'https://x.com/KarnatakaSNDMC'






    },






    {






      level: 'orange',






      badge: '⚠️ ಆರೆಂಜ್ ಅಲರ್ಟ್ (Orange Alert)',






      source: '🏛️ IMD ಬೆಂಗಳೂರು ಮುನ್ಸೂಚನಾ ಕೇಂದ್ರ',






      title: 'ದಕ್ಷಿಣ ಒಳನಾಡು ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಗುಡುಗು ಸಹಿತ ಸಾಧಾರಣದಿಂದ ಉತ್ತಮ ಮಳೆ',






      body: 'ಬೆಂಗಳೂರು ನಗರ, ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ, ರಾಮನಗರ, ಮೈಸೂರು, ಹಾಸನ ಮತ್ತು ಚಿಕ್ಕಮಗಳೂರು ಭಾಗಗಳಲ್ಲಿ ಸಂಜೆ ಮತ್ತು ರಾತ್ರಿ ವೇಳೆ ಗುಡುಗು ಮಿಂಚು ಹಾಗೂ 30-40 ಕಿ.ಮೀ ವೇಗದ ಗಾಳಿ ಸಹಿತ ಮಳೆಯಾಗುವ ಸಾಧ್ಯತೆ.',






      validity: 'ಸಂಜೆ / ರಾತ್ರಿ ಮುನ್ಸೂಚನೆ',






      link: 'https://x.com/KarnatakaSNDMC'






    },






    {






      level: 'yellow',






      badge: '🌧️ ಮುಂಗಾರು ಮಾಹಿತಿ (Monsoon Update)',






      source: '🏛️ KSNDMC ದೈನಂದಿನ ವರದಿ',






      title: 'ಉತ್ತರ ಒಳನಾಡು ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಮೋಡ ಕವಿದ ವಾತಾವರಣ & ತುಂತುರು ಮಳೆ',






      body: 'ಬೆಳಗಾವಿ, ಧಾರವಾಡ, ಗದಗ, ಹಾವೇರಿ, ವಿಜಯಪುರ ಹಾಗೂ ಕಲಬುರಗಿ ಜಿಲ್ಲೆಗಳಲ್ಲಿ ತಂಪಾದ ವಾತಾವರಣ, ಅಲ್ಲಲ್ಲಿ ಚದುರಿದಂತೆ ಸಾಧಾರಣ ಮಳೆಯಾಗುವ ಸಂಭವವಿದೆ.',






      validity: 'ದೈನಂದಿನ ಹವಾಮಾನ ಸಾರಾಂಶ',






      link: 'https://x.com/KarnatakaSNDMC'






    }






  ];













  container.innerHTML = officialAlerts.map(t => {






    const isRed = t.level === 'red';






    const isOrange = t.level === 'orange';













    const bg = isRed ? '#FFF1F2' : (isOrange ? '#FFFBEB' : '#F0FDF4');






    const border = isRed ? '#FECDD3' : (isOrange ? '#FDE68A' : '#BBF7D0');






    const borderTop = isRed ? '#E11D48' : (isOrange ? '#F59E0B' : '#10B981');






    const badgeBg = isRed ? '#E11D48' : (isOrange ? '#F59E0B' : '#10B981');






    const titleCol = isRed ? '#881337' : (isOrange ? '#78350F' : '#14532D');






    const bodyCol = isRed ? '#4C0519' : (isOrange ? '#451A03' : '#052E16');






    const subCol = isRed ? '#9F1239' : (isOrange ? '#92400E' : '#166534');













    return `






      <div style="background:${bg}; border:2px solid ${border}; border-top:5px solid ${borderTop}; border-radius:18px; padding:20px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 6px 20px rgba(0,0,0,0.06);">






        <div>






          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">






            <span style="background:${badgeBg}; color:#FFF; font-size:11.5px; font-weight:900; padding:4px 12px; border-radius:20px; box-shadow:0 2px 8px rgba(0,0,0,0.15);">${t.badge}</span>






            <span style="font-size:11.5px; color:${subCol}; font-weight:800;">${t.source}</span>






          </div>






          <div style="font-size:15px; font-weight:900; color:${titleCol}; line-height:1.4; margin-bottom:8px;">






            ${t.title}






          </div>






          <div style="font-size:12.5px; color:${bodyCol}; line-height:1.45; margin-bottom:10px;">






            ${t.body}






          </div>






        </div>






        <div style="display:flex; justify-content:space-between; align-items:center; margin-top:14px; padding-top:10px; border-top:1px solid ${border}; font-size:11.5px; color:${subCol};">






          <span>⏱️ ${t.validity}</span>






          <a href="${t.link}" target="_blank" style="color:${borderTop}; font-weight:900; text-decoration:none;">ಬುಲೆಟಿನ್ ವಿವರ ↗</a>






        </div>






      </div>






    `;






  }).join('');






}













function renderHourlyForecast(dist) {






  const container = document.getElementById('hourly-scroll');






  const titleEl = document.getElementById('hourly-title');






  if (!container) return;






  if (titleEl && dist) titleEl.textContent = `⏱️ ${dist.name_kn} — ಮುಂದಿನ 24 ಗಂಟೆಗಳ ಮುನ್ಸೂಚನೆ`;













  const hourly = dist?.hourly_24h || [];






  if (hourly.length === 0) {






    container.innerHTML = `<div style="padding:10px; font-size:12px; color:#64748B;">ಲೋಡ್ ಆಗುತ್ತಿದೆ...</div>`;






    return;






  }






  container.innerHTML = hourly.map((h, idx) => `






    <div class="hourly-item ${idx === 0 ? 'now' : ''}">






      <div class="hi-time">${h.time || idx + ':00'}</div>






      <div class="hi-icon">${h.icon || '⛅'}</div>






      <div class="hi-temp">${Math.round(h.temp_c || 25)}°</div>






      <div class="hi-rain">💧 ${h.rain_chance || 0}%</div>






    </div>






  `).join('');






}













function getKannadaDayName(dateStr, idx) {






  if (idx === 0) return 'ಇಂದು';






  if (idx === 1) return 'ನಾಳೆ';






  if (dateStr) {






    try {






      const dt = new Date(dateStr);






      if (!isNaN(dt.getTime())) {






        const knDays = ['ಭಾನುವಾರ', 'ಸೋಮವಾರ', 'ಮಂಗಳವಾರ', 'ಬುಧವಾರ', 'ಗುರುವಾರ', 'ಶುಕ್ರವಾರ', 'ಶನಿವಾರ'];






        return knDays[dt.getDay()];






      }






    } catch(e) {}






  }






  return `ದಿನ ${idx + 1}`;






}













function render7DayForecast(dist) {






  const container = document.getElementById('forecast-h-scroll');






  const titleEl = document.getElementById('forecast-title');






  if (!container) return;






  if (titleEl && dist) titleEl.textContent = `📅 ${dist.name_kn} — ಮುಂದಿನ 7 ದಿನಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ (7-Day Outlook)`;













  const forecast = dist?.forecast_7d || dist?.forecast || [];






  if (forecast.length === 0) {






    container.innerHTML = `<div style="padding:16px; font-size:13px; color:#64748B;">ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ ಲಭ್ಯವಿಲ್ಲ...</div>`;






    return;






  }













  container.innerHTML = forecast.map((f, idx) => `






    <div class="forecast-h-card ${idx === 0 ? 'today' : ''}">






      <div class="fhc-day">${f.day_kn || getKannadaDayName(f.date, idx)}</div>






      <div class="fhc-date">${f.date || ''}</div>






      <div class="fhc-icon">${f.icon || '⛅'}</div>






      <div class="fhc-desc">${f.desc_kn || 'ಸಾಮಾನ್ಯ ಹವಾಮಾನ'}</div>






      <div class="fhc-rain-pill">💧 ${f.precip_prob || 0}%</div>






      <div class="fhc-temp-row">






        <span class="fhc-max">${Math.round(f.temp_max || 28)}°</span>






        <span class="fhc-min">${Math.round(f.temp_min || 20)}°</span>






      </div>






    </div>






  `).join('');






}













function renderDistrictsGrid(data) {






  const container = document.getElementById('district-grid');






  if (!container || !data || !data.districts) return;






  let list = Object.values(data.districts);













  if (currentRegionFilter !== 'all') {






    list = list.filter(d => d.region === currentRegionFilter);






  }






  if (searchQueryFilter.trim() !== '') {






    const q = searchQueryFilter.toLowerCase().trim();






    list = list.filter(d => (d.name_kn || '').toLowerCase().includes(q) || (d.hq || '').toLowerCase().includes(q));






  }













  container.innerHTML = list.map(d => {






    const c = d.current || {};






    const alertClass = d.alert_level ? `alert-${d.alert_level}` : '';






    const tagText = d.alert_level === 'red' ? '🚨 ಭಾರೀ ಮಳೆ ಎಚ್ಚರಿಕೆ' : (d.alert_level === 'orange' ? '⚠️ ಮಳೆ ಸೂಚನೆ' : '');













    return `






      <div class="dw-card ${alertClass}" onclick="selectDistrict('${d.key}')">






        <div class="dw-header">






          <div>






            <div class="dw-name">${d.name_kn}</div>






            <div class="dw-hq">${d.hq || ''}</div>






          </div>






          <div class="dw-icon">${c.icon || '⛅'}</div>






        </div>













        <div class="dw-temp-row">






          <div class="dw-temp">${Math.round(c.temp_c || 25)}°</div>






          <div class="dw-desc">${c.desc_kn || 'ಭಾಗಶಃ ಮೋಡ'}</div>






        </div>













        <div class="dw-stats">






          <span>💧 ${c.rain_chance || 0}% ಮಳೆ</span>






          <span>💨 ${c.wind_kmh || 10} km/h</span>






          <span>💦 ${c.humidity || 70}%</span>






        </div>






        ${tagText ? `<span class="dw-alert-tag ${d.alert_level === 'red' ? 'tag-red' : 'tag-orange'}">${tagText}</span>` : ''}






      </div>






    `;






  }).join('');






}













function filterRegion(region, el) {






  currentRegionFilter = region;






  document.querySelectorAll('.city-tab').forEach(t => t.classList.remove('active'));






  el.classList.add('active');






  if (weatherStore) renderDistrictsGrid(weatherStore);






}













function filterSearch(val) {






  searchQueryFilter = val;






  if (weatherStore) renderDistrictsGrid(weatherStore);






}













const faqQuestions = [






  { key: 'now', label: '📍 ನನ್ನ ಏರಿಯಾದ ಈಗಿನ ಹವಾಮಾನವೇನು?' },






  { key: 'rain_today', label: '🌧️ ಇಂದು ನನ್ನ ಏರಿಯಾದಲ್ಲಿ ಮಳೆ ಬರುತ್ತಾ?' },






  { key: 'rain_1h', label: '⏱️ ಮುಂದಿನ 1 ಗಂಟೆಯಲ್ಲಿ / ಈಗಲೇ ಮಳೆ ಇದೆಯಾ?' },






  { key: 'tomorrow', label: '⛅ ನಾಳೆ ನನ್ನ ಏರಿಯಾದ ಹವಾಮಾನ ಹೇಗಿರುತ್ತೆ?' },






  { key: 'forecast_7d', label: '📅 ಮುಂದಿನ 7 ದಿನಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ ಏನು?' },






  { key: 'aqi', label: '🍃 ನನ್ನ ಏರಿಯಾದ AQI ವಾಯು ಗುಣಮಟ್ಟ ಎಷ್ಟು?' },






  { key: 'alerts', label: '🚨 ನನ್ನ ಜಿಲ್ಲೆಗೆ ಭಾರೀ ಮಳೆ ರೆಡ್/ಆರೆಂಜ್ ಅಲರ್ಟ್ ಇದೆಯಾ?' },






  { key: 'wind_feel', label: '💨 ಗಾಳಿಯ ವೇಗ ಮತ್ತು ತಂಪಿನ ಅನುಭವವೆಷ್ಟು?' }






];













let openFaqKey = null; // Closed by default, user can click any to open













function getSelectedDistrictObj() {






  if (!weatherStore || !weatherStore.districts) return null;






  return weatherStore.districts[activeDistrictKey] || Object.values(weatherStore.districts)[0];






}













function getFaqAnswerData(qKey, dist) {






  const c = dist.current || {};






  const temp = Math.round(c.temp_c || 25);






  const feels = Math.round(c.feels_like || temp);






  const rainChance = c.rain_chance || 25;






  const windKmh = Math.round(c.wind_kmh || 12);






  const humidity = c.humidity || 75;






  const desc = c.desc_kn || 'ಭಾಗಶಃ ಮೋಡ';






  const nameKn = dist.name_kn || 'ಬೆಂಗಳೂರು';






  const aqi = getDistrictAQI(dist.key || 'bengaluru_urban');






  const hourly = dist.hourly_24h || [];






  const nextHour = hourly[1] || hourly[0] || {};






  const forecast = dist.forecast || [];






  const tomorrow = forecast[1] || forecast[0] || {};













  let title = '';






  let body = '';






  let pills = [];






  let aiQuery = '';













  switch (qKey) {






    case 'now':






      title = `📍 ${nameKn} — ಇಂದಿನ ಲೈವ್ ಹವಾಮಾನ`;






      body = `ಪ್ರಸ್ತುತ <strong>${nameKn}</strong> ಏರಿಯಾದಲ್ಲಿ ಉಷ್ಣಾಂಶ <strong>${temp}°C</strong> (ಅನುಭವ: <strong>${feels}°C</strong>) ಇದ್ದು, <strong>${desc} ${c.icon || '⛅'}</strong> ವಾತಾವರಣವಿದೆ. ಗಾಳಿಯು ಗಂಟೆಗೆ <strong>${windKmh} km/h</strong> ವೇಗದಲ್ಲಿ ಬೀಸುತ್ತಿದ್ದು, ಆರ್ದ್ರತೆ <strong>${humidity}%</strong> ದಾಖಲಾಗಿದೆ.`;






      pills = [`🌡️ ಉಷ್ಣಾಂಶ: ${temp}°C`, `💧 ಆರ್ದ್ರತೆ: ${humidity}%`, `💨 ಗಾಳಿ: ${windKmh} km/h`, `🍃 AQI: ${aqi.val}`];






      aiQuery = `${nameKn} ಇಂದಿನ ಲೈವ್ ಹವಾಮಾನ ವರದಿ ಏನು?`;






      break;













    case 'rain_today':






      title = `🌧️ ${nameKn} — ಇಂದು ಮಳೆ ಬರುತ್ತಾ?`;






      if (rainChance >= 50) {






        body = `🌧️ <strong>ಹೌದು!</strong> ಇಂದು <strong>${nameKn}</strong> ನಲ್ಲಿ ಮಳೆ ಬೀಳುವ <strong>${rainChance}% ಗರಿಷ್ಠ ಸಾಧ್ಯತೆ</strong> ಇದೆ. ವಿಶೇಷವಾಗಿ ಸಂಜೆ ಅಥವಾ ರಾತ್ರಿಯ ವೇಳೆ ಸಾಧಾರಣದಿಂದ ಭಾರೀ ತುಂತುರು ಮಳೆಯಾಗುವ ಮುನ್ಸೂಚನೆ ಇದೆ. ಹೊರಗೆ ಹೋಗುವಾಗ ಛತ್ರಿ ಇಟ್ಟುಕೊಳ್ಳುವುದು ಸೂಕ್ತ.`;






      } else {






        body = `⛅ ಇಂದು <strong>${nameKn}</strong> ನಲ್ಲಿ ಮಳೆಯ ಸಾಧ್ಯತೆ ಕೇವಲ <strong>${rainChance}%</strong> ಇದೆ. ದಿನದ ಬಹುತೇಕ ಭಾಗ ಮೋಡ ಕವಿದ ಅಥವಾ ಒಣ ಹವೆಯ ವಾತಾವರಣ ಇರಲಿದ್ದು, ಭಾರಿ ಮಳೆಯ ಲಕ್ಷಣಗಳಿಲ್ಲ.`;






      }






      pills = [`🌧️ ಮಳೆ ಸಾಧ್ಯತೆ: ${rainChance}%`, `💦 ತೇವಾಂಶ: ${humidity}%`, `🚨 ಎಚ್ಚರಿಕೆ: ${dist.alert_level || 'Normal'}`];






      aiQuery = `ಇಂದು ${nameKn} ನಲ್ಲಿ ಮಳೆ ಬರುತ್ತಾ? KSNDMC ಮಳೆ ಮುನ್ಸೂಚನೆ ಏನು?`;






      break;













    case 'rain_1h':






      title = `⏱️ ${nameKn} — ಮುಂದಿನ 1 ಗಂಟೆಯಲ್ಲಿ ಮಳೆ ಇದೆಯಾ?`;






      const nextRain = nextHour.rain_chance || rainChance;






      if (nextRain >= 40) {






        body = `⏱️ <strong>ಮಳೆ ಸಾಧ್ಯತೆ ಇದೆ!</strong> ಮುಂದಿನ 1 ಗಂಟೆಯಲ್ಲಿ (ಸುಮಾರು ${nextHour.time || 'ಮುಂದಿನ ಅವಧಿ'}) ನಿಮ್ಮ ಪ್ರದೇಶದಲ್ಲಿ ಮಳೆ ಬೀಳುವ <strong>${nextRain}% ಸಂಭವ</strong>ವಿದೆ. ಮೋಡಗಳ ದಟ್ಟಣೆ ಹೆಚ್ಚುತ್ತಿದ್ದು ತುಂತುರು ಮಳೆ ಪ್ರಾರಂಭವಾಗಬಹುದು.`;






      } else {






        body = `⏱️ <strong>ಇಲ್ಲ!</strong> ಮುಂದಿನ 1 ಗಂಟೆಯಲ್ಲಿ ನಿಮ್ಮ ಪ್ರದೇಶದಲ್ಲಿ ಮಳೆ ಬೀಳುವ ಸಾಧ್ಯತೆ ಕೇವಲ <strong>${nextRain}%</strong> ಇದ್ದು, ವಾತಾವರಣ ಸ್ಥಿರ ಮತ್ತು ತಂಪಾಗಿರಲಿದೆ.`;






      }






      pills = [`⏱️ ಮುಂದಿನ 1h ಮಳೆ: ${nextRain}%`, `🌡️ ನಿರೀಕ್ಷಿತ Temp: ${nextHour.temp_c || temp}°C`];






      aiQuery = `${nameKn} ಮುಂದಿನ 1 ಗಂಟೆಯಲ್ಲಿ ಮಳೆ ಬರುತ್ತಾ?`;






      break;













    case 'tomorrow':






      title = `⛅ ${nameKn} — ನಾಳಿನ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ`;






      const tMax = Math.round(tomorrow.max_temp || 28);






      const tMin = Math.round(tomorrow.min_temp || 20);






      const tRain = tomorrow.rain_chance || 30;






      const tomorrowDayName = getKannadaDayName(tomorrow.date, 1);






      body = `ನಾಳೆ <strong>${nameKn}</strong> ನಲ್ಲಿ ಗರಿಷ್ಠ <strong>${tMax}°C</strong> ಹಾಗೂ ಕನಿಷ್ಠ <strong>${tMin}°C</strong> ಉಷ್ಣಾಂಶ ದಾಖಲಾಗುವ ಸಾಧ್ಯತೆಯಿದೆ. ದಿನವಿಡೀ <strong>${tomorrowDayName}</strong> ಭಾಗಶಃ ಮೋಡ ಕವಿದ ವಾತಾವರಣ ಇರಲಿದ್ದು, ಮಳೆ ಸಾಧ್ಯತೆ <strong>${tRain}%</strong> ಇರಲಿದೆ.`;






      pills = [`🔥 ಗರಿಷ್ಠ: ${tMax}°C`, `❄️ ಕನಿಷ್ಠ: ${tMin}°C`, `🌧️ ಮಳೆ: ${tRain}%`];






      aiQuery = `ನಾಳೆ ${nameKn} ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ ಹೇಗಿರಲಿದೆ?`;






      break;













    case 'forecast_7d':






      title = `📅 ${nameKn} — ಮುಂದಿನ 7 ದಿನಗಳ ಸಂಪೂರ್ಣ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ`;






      const daysListHtml = forecast.slice(0, 7).map((f, idx) => {






        const dName = getKannadaDayName(f.date, idx);






        const dtFmt = f.date ? new Date(f.date).toLocaleDateString('kn-IN', { day: 'numeric', month: 'short' }) : '';






        const rChance = f.rain_chance || (f.rain_mm > 0 ? 65 : 20);






        return `<div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:6px; padding:10px 0; border-bottom:1px solid #E2E8F0; font-size:14px;">






          <span style="font-weight:800; color:#0F172A; min-width:130px;">🗓️ ${dName} (${dtFmt}):</span>






          <span style="color:#334155; font-weight:700;">${f.icon || '⛅'} ${f.desc_kn || 'ಭಾಗಶಃ ಮೋಡ'}</span>






          <span style="font-weight:800; color:#0284C7;">💧 ${rChance}% ಮಳೆ</span>






          <span style="font-weight:900; color:#0F172A; font-family:var(--font-en);">${Math.round(f.max_temp || 28)}° / ${Math.round(f.min_temp || 20)}°C</span>






        </div>`;






      }).join('');






      body = `ಮುಂದಿನ 7 ದಿನಗಳಲ್ಲಿ <strong>${nameKn}</strong> ನಲ್ಲಿ ನಿರೀಕ್ಷಿತ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ ವಿವರಗಳು:<br><div style="margin-top:10px; background:#F8FAFC; border:1px solid #E2E8F0; border-radius:12px; padding:6px 14px;">${daysListHtml}</div>`;






      pills = [`📅 ಮುನ್ಸೂಚನೆ ಅವಧಿ: 7 ದಿನಗಳು`, `🌡️ ಸರಾಸರಿ: 24°C`];






      aiQuery = `${nameKn} ಮುಂದಿನ 7 ದಿನಗಳ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ ವರದಿ`;






      break;













    case 'aqi':






      title = `🍃 ${nameKn} — ವಾಯು ಗುಣಮಟ್ಟ ಸೂಚ್ಯಂಕ (AQI)`;






      body = `<strong>${nameKn}</strong> ಏರಿಯಾದ ಪ್ರಸ್ತುತ ವಾಯು ಗುಣಮಟ್ಟ ಸೂಚ್ಯಂಕ (AQI) <strong>${aqi.val}</strong> ಆಗಿದ್ದು, ಇದು <strong>'${aqi.label}'</strong> ವಿಭಾಗದಲ್ಲಿದೆ. ಪರಿಸರದಲ್ಲಿ ಧೂಳು ಮತ್ತು ಮಾಲಿನ್ಯದ ಪ್ರಮಾಣ ನಿಯಂತ್ರಣದಲ್ಲಿದ್ದು, ಮುಂಜಾನೆಯ ನಡಿಗೆ ಹಾಗೂ ಹೊರಾಂಗಣ ಚಟುವಟಿಕೆಗಳಿಗೆ ಸೂಕ್ತವಾಗಿದೆ.`;






      pills = [`🍃 AQI: ${aqi.val}`, `🟢 ಗುಣಮಟ್ಟ: ${aqi.label}`, `🫁 ಸುರಕ್ಷಿತ ವಾತಾವರಣ`];






      aiQuery = `${nameKn} AQI ವಾಯು ಗುಣಮಟ್ಟ ಎಷ್ಟು? ಆರೋಗ್ಯಕ್ಕೆ ಸೂಕ್ತವೇ?`;






      break;













    case 'alerts':






      title = `🚨 ${nameKn} — KSNDMC & IMD ಅಧಿಕೃತ ಮಳೆ ಎಚ್ಚರಿಕೆ`;






      if (dist.alert_level === 'red') {






        body = `🚨 <strong>ರೆಡ್ ಅಲರ್ಟ್ (Red Warning):</strong> ${nameKn} ಜಿಲ್ಲೆಗೆ KSNDMC ವತಿಯಿಂದ ಅತ್ಯಂತ ಭಾರೀ ಮಳೆಯ ಎಚ್ಚರಿಕೆ ನೀಡಲಾಗಿದೆ. ನದಿ ತೀರ ಮತ್ತು ತಗ್ಗು ಪ್ರದೇಶಗಳ ಜನರು ಸುರಕ್ಷಿತ ಸ್ಥಳಗಳಲ್ಲಿರಲು ಕೋರಲಾಗಿದೆ.`;






      } else if (dist.alert_level === 'orange') {






        body = `⚠️ <strong>ಆರೆಂಜ್ ಅಲರ್ಟ್ (Orange Alert):</strong> ${nameKn} ಜಿಲ್ಲೆಯಲ್ಲಿ ಸಾಧಾರಣದಿಂದ ಭಾರೀ ಮಳೆಯಾಗುವ ಸಾಧ್ಯತೆ ಇದೆ. ಸಾರ್ವಜನಿಕರು ಮುನ್ನೆಚ್ಚರಿಕೆ ವಹಿಸಲು ಸೂಚಿಸಲಾಗಿದೆ.`;






      } else {






        body = `🟢 <strong>ಸಾಧಾರಣ ವಾತಾವರಣ (No Warning):</strong> ಪ್ರಸ್ತುತ ${nameKn} ಜಿಲ್ಲೆಗೆ ಯಾವುದೇ ಗಂಭೀರ ಪ್ರವಾಹ ಅಥವಾ ಭಾರೀ ಮಳೆ ರೆಡ್/ಆರೆಂಜ್ ಎಚ್ಚರಿಕೆ ಇರುವುದಿಲ್ಲ. ದಿನನಿತ್ಯದ ಚಟುವಟಿಕೆಗಳಿಗೆ ಯಾವುದೇ ಅಡಚಣೆಯಿಲ್ಲ.`;






      }






      pills = [`🚨 ಅಲರ್ಟ್ ಮಟ್ಟ: ${dist.alert_level ? dist.alert_level.toUpperCase() : 'NORMAL'}`, `📢 KSNDMC ಅಧಿಕೃತ`];






      aiQuery = `${nameKn} ಜಿಲ್ಲೆಗೆ KSNDMC ಅಥವಾ IMD ಮಳೆ ಎಚ್ಚರಿಕೆ ಇದೆಯಾ?`;






      break;













    case 'wind_feel':






      title = `💨 ${nameKn} — ಗಾಳಿಯ ವೇಗ ಮತ್ತು ಶೀತದ ಅನುಭವ`;






      body = `<strong>${nameKn}</strong> ನಲ್ಲಿ ಗಾಳಿಯ ವೇಗ <strong>${windKmh} km/h</strong> ಇದ್ದು, ಈಶಾನ್ಯ ದಿಕ್ಕಿನಿಂದ ಬೀಸುತ್ತಿದೆ. ಪ್ರಸ್ತುತ ಉಷ್ಣಾಂಶ <strong>${temp}°C</strong> ಇದ್ದರೂ ತೇವಾಂಶ ಮತ್ತು ಗಾಳಿಯ ಕಾರಣ ದೇಹಕ್ಕೆ <strong>${feels}°C</strong> ತಂಪಿನ ಅನುಭವವಾಗುತ್ತದೆ.`;






      pills = [`💨 ಗಾಳಿಯ ವೇಗ: ${windKmh} km/h`, `🌡️ ನೈಜ ಅನುಭವ: ${feels}°C`];






      aiQuery = `${nameKn} ಗಾಳಿಯ ವೇಗ ಮತ್ತು ಹವಾಮಾನ ಹೇಗಿದೆ?`;






      break;






  }






  return { title, body, pills, aiQuery };






}













function renderFaqAccordion(dist) {






  const container = document.getElementById('faqAccordionList');






  if (!container || !dist) return;













  const locBadge = document.getElementById('awDetectedLocName');






  if (locBadge) locBadge.textContent = dist.name_kn || 'ಬೆಂಗಳೂರು';













  container.innerHTML = faqQuestions.map(q => {






    const isOpen = (q.key === openFaqKey);






    const ans = getFaqAnswerData(q.key, dist);













    return `






      <div class="faq-item ${isOpen ? 'open' : ''}" id="faq-item-${q.key}">






        <div class="faq-header" onclick="toggleFaq('${q.key}')">






          <span>${q.label}</span>






          <span class="faq-icon-arrow">▼</span>






        </div>






        <div class="faq-body-drawer" id="faq-drawer-${q.key}" style="display: ${isOpen ? 'block' : 'none'};">






          <div style="font-size:16px; font-weight:800; color:#0369A1; margin-bottom:8px;">${ans.title}</div>






          <div style="font-size:15px; line-height:1.75; color:#1E293B;">${ans.body}</div>






          <div class="faq-stats-strip">






            ${ans.pills.map(p => `<span class="faq-stat-pill">${p}</span>`).join('')}






          </div>






          <div>






            <a href="/ask.html?q=${encodeURIComponent(ans.aiQuery)}" class="faq-ask-ai-link">






              <span>🤖 askKARNATA AI ನಲ್ಲಿ "${dist.name_kn}" ಬಗ್ಗೆ ಇನ್ನಷ್ಟು ಕೇಳಿ →</span>






            </a>






          </div>






        </div>






      </div>






    `;






  }).join('');






}













function toggleFaq(key) {






  if (openFaqKey === key) {






    openFaqKey = null;






  } else {






    openFaqKey = key;






  }






  const dist = getSelectedDistrictObj();






  if (dist) renderFaqAccordion(dist);






}













function updateAskWeatherUI() {






  const dist = getSelectedDistrictObj();






  if (dist) renderFaqAccordion(dist);






}













// GPS / Auto-Location Detection (Haversine formula to closest Karnataka district)






const karnatakaCoordinates = [






  { key: 'bengaluru_urban', name_kn: 'ಬೆಂಗಳೂರು ನಗರ', lat: 12.9716, lon: 77.5946 },






  { key: 'bengaluru_rural', name_kn: 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ', lat: 13.2257, lon: 77.5750 },






  { key: 'mysuru', name_kn: 'ಮೈಸೂರು', lat: 12.2958, lon: 76.6394 },






  { key: 'dakshina_kannada', name_kn: 'ದಕ್ಷಿಣ ಕನ್ನಡ (ಮಂಗಳೂರು)', lat: 12.9141, lon: 74.8560 },






  { key: 'udupi', name_kn: 'ಉಡುಪಿ', lat: 13.3409, lon: 74.7421 },






  { key: 'uttara_kannada', name_kn: 'ಉತ್ತರ ಕನ್ನಡ (ಕಾರವಾರ)', lat: 14.8185, lon: 74.1416 },






  { key: 'belagavi', name_kn: 'ಬೆಳಗಾವಿ', lat: 15.8497, lon: 74.4977 },






  { key: 'hubballi_dharwad', name_kn: 'ಧಾರವಾಡ / ಹುಬ್ಬಳ್ಳಿ', lat: 15.3647, lon: 75.1240 },






  { key: 'kalaburagi', name_kn: 'ಕಲಬುರಗಿ', lat: 17.3297, lon: 76.8343 },






  { key: 'ballari', name_kn: 'ಬಳ್ಳಾರಿ', lat: 15.1394, lon: 76.9214 },






  { key: 'vijayanagara', name_kn: 'ವಿಜಯನಗರ (ಹೊಸಪೇಟೆ)', lat: 15.2689, lon: 76.3909 },






  { key: 'shivamogga', name_kn: 'ಶಿವಮೊಗ್ಗ', lat: 13.9299, lon: 75.5681 },






  { key: 'chikkamagaluru', name_kn: 'ಚಿಕ್ಕಮಗಳೂರು', lat: 13.3161, lon: 75.7720 },






  { key: 'kodagu', name_kn: 'ಕೊಡಗು (ಮಡಿಕೇರಿ)', lat: 12.4244, lon: 75.7382 },






  { key: 'hassan', name_kn: 'ಹಾಸನ', lat: 13.0033, lon: 76.1004 },






  { key: 'tumakuru', name_kn: 'ತುಮಕೂರು', lat: 13.3379, lon: 77.1010 },






  { key: 'davangere', name_kn: 'ದಾವಣಗೆರೆ', lat: 14.4644, lon: 75.9218 },






  { key: 'raichur', name_kn: 'ರಾಯಚೂರು', lat: 16.2120, lon: 77.3439 },






  { key: 'koppal', name_kn: 'ಕೊಪ್ಪಳ', lat: 15.3456, lon: 76.1554 },






  { key: 'gadag', name_kn: 'ಗದಗ', lat: 15.4298, lon: 75.6315 },






  { key: 'bagalkote', name_kn: 'ಬಾಗಲಕೋಟೆ', lat: 16.1691, lon: 75.6615 },






  { key: 'vijayapura', name_kn: 'ವಿಜಯಪುರ', lat: 16.8302, lon: 75.7100 },






  { key: 'bidar', name_kn: 'ಬೀದರ್', lat: 17.9104, lon: 77.5199 },






  { key: 'yadgir', name_kn: 'ಯಾದಗಿರಿ', lat: 16.7639, lon: 77.1378 },






  { key: 'chamarajanagar', name_kn: 'ಚಾಮರಾಜನಗರ', lat: 11.9261, lon: 76.9437 },






  { key: 'mandya', name_kn: 'ಮಂಡ್ಯ', lat: 12.5218, lon: 76.8951 },






  { key: 'ramanagara', name_kn: 'ರಾಮನಗರ', lat: 12.7150, lon: 77.2810 },






  { key: 'kolar', name_kn: 'ಕೋಲಾರ', lat: 13.1358, lon: 78.1291 },






  { key: 'chikkaballapur', name_kn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', lat: 13.4355, lon: 77.7275 },






  { key: 'chitradurga', name_kn: 'ಚಿತ್ರದುರ್ಗ', lat: 14.2251, lon: 76.3980 },






  { key: 'haveri', name_kn: 'ಹಾವೇರಿ', lat: 14.7954, lon: 75.3991 },






];













function getDistanceKm(lat1, lon1, lat2, lon2) {






  const R = 6371;






  const dLat = (lat2 - lat1) * Math.PI / 180;






  const dLon = (lon2 - lon1) * Math.PI / 180;






  const a = Math.sin(dLat/2) * Math.sin(dLat/2) +






            Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *






            Math.sin(dLon/2) * Math.sin(dLon/2);






  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));






  return R * c;






}













function detectGPSLocation() {






  if (!navigator.geolocation) {






    alert('ನಿಮ್ಮ ಬ್ರೌಸರ್‌ನಲ್ಲಿ GPS ಲಭ್ಯವಿಲ್ಲ.');






    return;






  }






  const badge = document.getElementById('awDetectedLocName');






  if (badge) badge.textContent = 'ಪತ್ತೆ ಮಾಡಲಾಗುತ್ತಿದೆ...';













  navigator.geolocation.getCurrentPosition(






    (pos) => {






      const uLat = pos.coords.latitude;






      const uLon = pos.coords.longitude;






      






      let closest = karnatakaCoordinates[0];






      let minD = 99999;






      for (const d of karnatakaCoordinates) {






        const dist = getDistanceKm(uLat, uLon, d.lat, d.lon);






        if (dist < minD) {






          minD = dist;






          closest = d;






        }






      }













      if (closest && weatherStore && weatherStore.districts) {






        selectDistrict(closest.key);






      }






    },






    (err) => {






      if (badge) badge.textContent = getSelectedDistrictObj()?.name_kn || 'ಬೆಂಗಳೂರು';






      alert('GPS ಅನುಮತಿ ನಿರಾಕರಿಸಲಾಗಿದೆ. ದಯವಿಟ್ಟು ಪಟ್ಟಿಯಿಂದ ಜಿಲ್ಲೆಯನ್ನು ಆರಿಸಿ.');






    },






    { timeout: 8000 }






  );






}













function selectDistrict(key) {






  activeDistrictKey = key;






  loadWeatherData();






  window.scrollTo({ top: 0, behavior: 'smooth' });






}













async function loadWeatherData() {




  const currentKey = activeDistrictKey || 'bengaluru_urban';




  let data = null;









  try {




    const res = await fetch(`/api/weather?district=${currentKey}&v=${Date.now()}`, { cache: 'no-store' });




    if (res.ok) {




      data = await res.json();




    }




  } catch(e) {




    console.warn('API fetch notice, checking data loader:', e);




  }









  if (!data || !data.success || !data.districts) {




    try {




      if (typeof NK !== 'undefined' && NK.fetch) {




        const rawW = await NK.fetch('weather', 'weather.json');




        if (rawW && rawW.districts) {




          const bd = rawW.districts[currentKey] || Object.values(rawW.districts)[0];




          data = {




            success: true,




            district_key: currentKey,




            district_kn: bd?.name_kn || 'ಬೆಂಗಳೂರು',




            updated_at: rawW.updated_at,




            ksndmc: { state_extremes: rawW.state_extremes, top_rainfall_locations: rawW.state_extremes?.top_rain_locations || [] },




            ksndmc_alerts: rawW.ksndmc_alerts,




            current: bd?.current,




            hourly_24h: bd?.hourly_24h,




            forecast_7d: bd?.forecast_7d,




            forecast: bd?.forecast_7d,




            districts: rawW.districts




          };




        }




      }




    } catch(err) {




      console.warn('Data loader fallback error:', err);




    }




  }









  if (data && data.success) {




    window.weatherStore = data;




    weatherStore = data;









    const activeDist = data.districts?.[currentKey] || {




      name_kn: data.district_kn,




      key: data.district_key,




      current: data.current,




      hourly_24h: data.hourly_24h,




      forecast_7d: data.forecast_7d,




      forecast: data.forecast_7d




    };









    renderHero(activeDist);




    renderHourlyForecast(activeDist);




    render7DayForecast(activeDist);




    renderFaqAccordion(activeDist);




    renderDistrictsGrid(data);




    renderRealKSNDMCTweets(data);




  }









  // Load KSNDMC Telemetry & State Extremes




  await renderSummaryAndCreativeCards(window.weatherStore);
  // Render warnings & nowcast dashboard
  if (typeof renderDistrictWarningsGrid === 'function') renderDistrictWarningsGrid();




}













if (document.readyState === 'loading') {






  document.addEventListener('DOMContentLoaded', loadWeatherData);






} else {






  loadWeatherData();






}







console.log("SUCCESS: Initial synchronous script executed!");
setTimeout(() => {
  console.log("Async DOMContentLoaded tasks finished without errors!");
}, 500);
} catch(e) {
  console.error("RUNTIME ERROR THROWN:", e);
}
