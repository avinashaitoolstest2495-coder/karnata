/**
 * Karnata — Automatic 1-Time Notification & Location Permission Manager
 * Requests Notification & Location permission ONCE on first site visit.
 * Auto-detects user's district and enables background rain notifications.
 */

(function () {
  const KARNATAKA_HQ_COORDS = [
    { key: 'bengaluru_urban', name: 'ಬೆಂಗಳೂರು ನಗರ', lat: 12.9716, lon: 77.5946 },
    { key: 'bengaluru_rural', name: 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ', lat: 13.0072, lon: 77.5673 },
    { key: 'mysuru', name: 'ಮೈಸೂರು', lat: 12.2958, lon: 76.6394 },
    { key: 'mandya', name: 'ಮಂಡ್ಯ', lat: 12.5220, lon: 76.8951 },
    { key: 'hassan', name: 'ಹಾಸನ', lat: 13.0068, lon: 76.1003 },
    { key: 'kodagu', name: 'ಕೊಡಗು', lat: 12.3375, lon: 75.8069 },
    { key: 'dakshina_kannada', name: 'ದಕ್ಷಿಣ ಕನ್ನಡ', lat: 12.8438, lon: 74.9919 },
    { key: 'udupi', name: 'ಉಡುಪಿ', lat: 13.3409, lon: 74.7421 },
    { key: 'shivamogga', name: 'ಶಿವಮೊಗ್ಗ', lat: 13.9299, lon: 75.5681 },
    { key: 'chikkamagaluru', name: 'ಚಿಕ್ಕಮಗಳೂರು', lat: 13.3153, lon: 75.7754 },
    { key: 'tumakuru', name: 'ತುಮಕೂರು', lat: 13.3379, lon: 77.1173 },
    { key: 'chitradurga', name: 'ಚಿತ್ರದುರ್ಗ', lat: 14.2226, lon: 76.3984 },
    { key: 'davanagere', name: 'ದಾವಣಗೆರೆ', lat: 14.4644, lon: 75.9218 },
    { key: 'belagavi', name: 'ಬೆಳಗಾವಿ', lat: 15.8497, lon: 74.4977 },
    { key: 'dharwad', name: 'ಧಾರವಾಡ', lat: 15.4589, lon: 75.0078 },
    { key: 'gadag', name: 'ಗದಗ', lat: 15.4167, lon: 75.6167 },
    { key: 'haveri', name: 'ಹಾವೇರಿ', lat: 14.7957, lon: 75.3998 },
    { key: 'uttara_kannada', name: 'ಉತ್ತರ ಕನ್ನಡ', lat: 14.7941, lon: 74.6561 },
    { key: 'bagalkote', name: 'ಬಾಗಲಕೋಟೆ', lat: 16.1831, lon: 75.6965 },
    { key: 'vijayapura', name: 'ವಿಜಯಪುರ', lat: 16.8302, lon: 75.7100 },
    { key: 'kalaburagi', name: 'ಕಲಬುರಗಿ', lat: 17.3297, lon: 76.8343 },
    { key: 'yadgir', name: 'ಯಾದಗಿರಿ', lat: 16.7620, lon: 77.1382 },
    { key: 'raichur', name: 'ರಾಯಚೂರು', lat: 16.2120, lon: 77.3439 },
    { key: 'koppal', name: 'ಕೊಪ್ಪಳ', lat: 15.3474, lon: 76.1547 },
    { key: 'ballari', name: 'ಬಳ್ಳಾರಿ', lat: 15.1394, lon: 76.9214 },
    { key: 'vijayanagara', name: 'ವಿಜಯನಗರ', lat: 15.1720, lon: 76.4560 },
    { key: 'chikkaballapura', name: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', lat: 13.4356, lon: 77.7310 },
    { key: 'kolar', name: 'ಕೋಲಾರ', lat: 13.1363, lon: 78.1294 },
    { key: 'ramanagara', name: 'ರಾಮನಗರ', lat: 12.7156, lon: 77.2817 },
    { key: 'chamarajanagara', name: 'ಚಾಮರಾಜನಗರ', lat: 11.9261, lon: 76.9439 },
  ];

  // Register Service Worker for Web Push
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js').then((reg) => {
      console.log('✅ Karnata SW Registered:', reg.scope);
    }).catch((err) => {
      console.warn('⚠️ SW Register error:', err);
    });
  }

  function getDistance(lat1, lon1, lat2, lon2) {
    const R = 6371;
    const dLat = (lat2 - lat1) * Math.PI / 180;
    const dLon = (lon2 - lon1) * Math.PI / 180;
    const a = Math.sin(dLat/2) * Math.sin(dLat/2) +
              Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
              Math.sin(dLon/2) * Math.sin(dLon/2);
    return R * (2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)));
  }

  function findNearestDistrict(userLat, userLon) {
    // Metropolitan Bengaluru bounding box check -> return Bengaluru Urban
    if (userLat >= 12.75 && userLat <= 13.25 && userLon >= 77.30 && userLon <= 77.85) {
      return KARNATAKA_HQ_COORDS.find(d => d.key === 'bengaluru_urban') || KARNATAKA_HQ_COORDS[0];
    }
    let nearest = KARNATAKA_HQ_COORDS[0];
    let minDist = Infinity;
    for (const d of KARNATAKA_HQ_COORDS) {
      const dist = getDistance(userLat, userLon, d.lat, d.lon);
      if (dist < minDist) {
        minDist = dist;
        nearest = d;
      }
    }
    return nearest;
  }

  async function requestOneTimePermissions() {
    const alreadyAsked = localStorage.getItem('karnata_perm_asked_v2');
    if (alreadyAsked) return;

    localStorage.setItem('karnata_perm_asked_v2', 'true');

    // 1. Request Notification Permission
    if ('Notification' in window && Notification.permission !== 'granted' && Notification.permission !== 'denied') {
      try {
        const perm = await Notification.requestPermission();
        if (perm === 'granted') {
          console.log('✅ Notification permission granted');
        }
      } catch (e) {}
    }

    // 2. Request Location Permission & Detect District
    if ('geolocation' in navigator) {
      navigator.geolocation.getCurrentPosition(
        (pos) => {
          const nearest = findNearestDistrict(pos.coords.latitude, pos.coords.longitude);
          localStorage.setItem('karnata_user_district', nearest.key);
          console.log('📍 Location detected nearest district:', nearest.name, nearest.key);
          if (window.selectDistrict && typeof window.selectDistrict === 'function') {
            window.selectDistrict(nearest.key);
          }
        },
        (err) => {
          console.warn('Location permission denied or unavailable:', err.message);
        },
        { timeout: 8000 }
      );
    }
  }

  document.addEventListener('DOMContentLoaded', () => {
    // Run 1-time permission request
    setTimeout(requestOneTimePermissions, 1000);
  });
})();
