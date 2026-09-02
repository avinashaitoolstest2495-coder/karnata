/**
 * Karnata.in — Autonomous Real-Time Geo & District Push Notification Engine
 * 1. Automatically detects user's exact district via HTML5 Geolocation (Haversine 31 districts).
 * 2. Fetches active IMD weather alerts (Yellow, Orange, Red alerts).
 * 3. Dispatches native system push notifications strictly targeted to respective districts.
 * 4. Includes instant testWeatherNotification() helper for user/developer verification.
 */

(function() {
  const STORAGE_KEY_DISTRICT = 'karnata_user_district_key';
  const STORAGE_KEY_SUB_ID = 'karnata_push_sub_id';
  const STORAGE_KEY_SEEN_PUSHES = 'karnata_seen_push_ids';

  // Exact 31 Karnataka Districts with Official District Headquarter Coordinates
  const KARNATAKA_31_DISTRICTS = [
    { key: "bengaluru_urban", name_kn: "ಬೆಂಗಳೂರು ನಗರ", lat: 12.9716, lon: 77.5946 },
    { key: "bengaluru_rural", name_kn: "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", lat: 13.0072, lon: 77.5673 },
    { key: "mysuru", name_kn: "ಮೈಸೂರು", lat: 12.2958, lon: 76.6394 },
    { key: "mandya", name_kn: "ಮಂಡ್ಯ", lat: 12.5220, lon: 76.8951 },
    { key: "hassan", name_kn: "ಹಾಸನ", lat: 13.0068, lon: 76.1003 },
    { key: "kodagu", name_kn: "ಕೊಡಗು", lat: 12.3375, lon: 75.8069 },
    { key: "dakshina_kannada", name_kn: "ದಕ್ಷಿಣ ಕನ್ನಡ (ಮಂಗಳೂರು)", lat: 12.8438, lon: 74.9919 },
    { key: "udupi", name_kn: "ಉಡುಪಿ", lat: 13.3409, lon: 74.7421 },
    { key: "uttara_kannada", name_kn: "ಉತ್ತರ ಕನ್ನಡ (ಕಾರವಾರ)", lat: 14.7941, lon: 74.6561 },
    { key: "shivamogga", name_kn: "ಶಿವಮೊಗ್ಗ", lat: 13.9299, lon: 75.5681 },
    { key: "chikkamagaluru", name_kn: "ಚಿಕ್ಕಮಗಳೂರು", lat: 13.3153, lon: 75.7754 },
    { key: "tumakuru", name_kn: "ತುಮಕೂರು", lat: 13.3379, lon: 77.1173 },
    { key: "chitradurga", name_kn: "ಚಿತ್ರದುರ್ಗ", lat: 14.2226, lon: 76.3984 },
    { key: "davanagere", name_kn: "ದಾವಣಗೆರೆ", lat: 14.4644, lon: 75.9218 },
    { key: "belagavi", name_kn: "ಬೆಳಗಾವಿ", lat: 15.8497, lon: 74.4977 },
    { key: "dharwad", name_kn: "ಧಾರವಾಡ / ಹುಬ್ಬಳ್ಳಿ", lat: 15.4589, lon: 75.0078 },
    { key: "gadag", name_kn: "ಗದಗ", lat: 15.4167, lon: 75.6167 },
    { key: "haveri", name_kn: "ಹಾವೇರಿ", lat: 14.7957, lon: 75.3998 },
    { key: "bagalkote", name_kn: "ಬಾಗಲಕೋಟೆ", lat: 16.1831, lon: 75.6965 },
    { key: "vijayapura", name_kn: "ವಿಜಯಪುರ", lat: 16.8302, lon: 75.7100 },
    { key: "kalaburagi", name_kn: "ಕಲಬುರಗಿ", lat: 17.3297, lon: 76.8343 },
    { key: "yadgir", name_kn: "ಯಾದಗಿರಿ", lat: 16.7620, lon: 77.1382 },
    { key: "raichur", name_kn: "ರಾಯಚೂರು", lat: 16.2120, lon: 77.3439 },
    { key: "koppal", name_kn: "ಕೊಪ್ಪಳ", lat: 15.3474, lon: 76.1547 },
    { key: "ballari", name_kn: "ಬಳ್ಳಾರಿ", lat: 15.1394, lon: 76.9214 },
    { key: "vijayanagara", name_kn: "ವಿಜಯನಗರ", lat: 15.1720, lon: 76.4560 },
    { key: "chikkaballapura", name_kn: "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", lat: 13.4356, lon: 77.7310 },
    { key: "kolar", name_kn: "ಕೋಲಾರ", lat: 13.1363, lon: 78.1294 },
    { key: "ramanagara", name_kn: "ರಾಮನಗರ", lat: 12.7156, lon: 77.2817 },
    { key: "chamarajanagara", name_kn: "ಚಾಮರಾಜನಗರ", lat: 11.9261, lon: 76.9439 },
    { key: "bidar", name_kn: "ಬೀದರ್", lat: 17.9104, lon: 77.5199 }
  ];

  // Register Service Worker
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js').then((reg) => {
      console.log('✅ Karnata SW Ready:', reg.scope);
    }).catch((err) => {
      console.warn('⚠️ SW Register notice:', err);
    });
  }

  // Haversine formula to find nearest Karnataka district HQ
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
    // Metro Bengaluru bounding box check
    if (userLat >= 12.75 && userLat <= 13.25 && userLon >= 77.30 && userLon <= 77.85) {
      return KARNATAKA_31_DISTRICTS.find(d => d.key === 'bengaluru_urban') || KARNATAKA_31_DISTRICTS[0];
    }
    let nearest = KARNATAKA_31_DISTRICTS[0];
    let minDist = Infinity;
    for (const d of KARNATAKA_31_DISTRICTS) {
      const dist = getDistance(userLat, userLon, d.lat, d.lon);
      if (dist < minDist) {
        minDist = dist;
        nearest = d;
      }
    }
    return nearest;
  }

  function getUserDistrict() {
    return localStorage.getItem(STORAGE_KEY_DISTRICT) || 'bengaluru_urban';
  }

  function getSeenPushes() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY_SEEN_PUSHES) || '[]');
    } catch(e) { return []; }
  }

  function addSeenPush(id) {
    const list = getSeenPushes();
    if (!list.includes(id)) {
      list.push(id);
      if (list.length > 50) list.shift();
      localStorage.setItem(STORAGE_KEY_SEEN_PUSHES, JSON.stringify(list));
    }
  }

  // Auto-detect Geo-Location
  function detectUserGeoLocation() {
    if ('geolocation' in navigator) {
      navigator.geolocation.getCurrentPosition(
        (pos) => {
          const nearest = findNearestDistrict(pos.coords.latitude, pos.coords.longitude);
          const prevDist = localStorage.getItem(STORAGE_KEY_DISTRICT);
          localStorage.setItem(STORAGE_KEY_DISTRICT, nearest.key);
          console.log('📍 Geo-Location Detected District:', nearest.name_kn, `(${nearest.key})`);
          if (prevDist !== nearest.key) {
            checkLiveDistrictPushFeed();
          }
        },
        (err) => {
          console.warn('Geolocation notice:', err.message);
        },
        { timeout: 8000, maximumAge: 3600000 }
      );
    }
  }

  // Check live district push feed (Edge API with static data fallback)
  async function checkLiveDistrictPushFeed() {
    const userDist = getUserDistrict();
    let feed = [];

    // 1. Try Cloudflare Worker API
    try {
      const res = await fetch(`/api/push/feed?district=${userDist}&t=${Date.now()}`, { cache: 'no-store' });
      if (res.ok) {
        const data = await res.json();
        feed = data.feed || [];
      }
    } catch(e) {}

    // 2. Fallback to direct static JSON feed
    if (!feed.length) {
      try {
        const staticRes = await fetch(`/data/live_push_feed.json?t=${Date.now()}`, { cache: 'no-store' });
        if (staticRes.ok) {
          const staticData = await staticRes.json();
          const allAlerts = staticData.feed || [];
          feed = allAlerts.filter(item => item.target_district === 'all' || item.target_district === userDist);
        }
      } catch(e) {}
    }

    if (!feed.length) return;

    const seenList = getSeenPushes();

    for (const item of feed) {
      const matchesDistrict = (item.target_district === 'all' || item.target_district === userDist);

      if (matchesDistrict && !seenList.includes(item.id)) {
        addSeenPush(item.id);
        dispatchNotification(item, userDist);
      }
    }
  }

  // Dispatch native notification or in-page toast
  function dispatchNotification(item, userDist) {
    if ('Notification' in window && Notification.permission === 'granted') {
      const vibratePattern = item.alert_level === 'red'
        ? [300, 100, 300, 100, 300]
        : (item.alert_level === 'orange' ? [200, 100, 200] : [150, 100, 150]);

      if ('serviceWorker' in navigator && navigator.serviceWorker.ready) {
        navigator.serviceWorker.ready.then(reg => {
          reg.showNotification(item.title, {
            body: item.body,
            icon: item.icon || 'https://karnata.in/assets/icons/icon-512x512.png',
            badge: item.badge || 'https://karnata.in/assets/icons/icon-192x192.png',
            data: { url: item.url || `https://karnata.in/weather?district=${userDist}` },
            vibrate: vibratePattern,
            tag: item.id
          });
        });
      } else {
        new Notification(item.title, {
          body: item.body,
          icon: item.icon || 'https://karnata.in/assets/icons/icon-512x512.png',
          tag: item.id
        });
      }
    } else if ('Notification' in window && Notification.permission !== 'denied') {
      showInPagePushBanner(item, userDist);
    }
  }

  // Non-intrusive alert toast for user's district or statewide gold alerts
  function showInPagePushBanner(item, userDist) {
    let b = document.getElementById('karnata-live-district-alert-toast');
    if (!b) {
      b = document.createElement('div');
      b.id = 'karnata-live-district-alert-toast';
      b.style.cssText = 'position:fixed; bottom:24px; right:20px; max-width:380px; width:90%; background:#0F172A; color:#FFF; border-radius:18px; padding:18px; z-index:9999999; box-shadow:0 20px 40px rgba(0,0,0,0.5); font-family:system-ui,-apple-system,sans-serif; animation:slideIn 0.3s ease;';
      document.body.appendChild(b);
    }

    const isGold = (item.topic === 'gold_rate_alert' || (item.id && item.id.startsWith('GOLD-')));

    let badgeColor = '#CA8A04';
    let badgeText = '🟡 ಹಳದಿ ನಿಗಾ';
    let actionBtnText = 'ಹವಾಮಾನ ವೀಕ್ಷಿಸಿ ➔';
    let actionUrl = item.url || `/weather?district=${userDist}`;
    let toastBorder = '2px solid #0284C7';

    if (isGold) {
      toastBorder = '2px solid #F59E0B';
      actionBtnText = 'ಇಂದಿನ ದರ & ಲೆಕ್ಕ ನೋಡಿ ➔';
      actionUrl = item.url || '/gold-rate';
      if (item.alert_level === 'gold_drop') {
        badgeColor = '#16A34A';
        badgeText = '🪙 ದರ ಇಳಿಕೆ (10 AM Live)';
      } else if (item.alert_level === 'gold_surge') {
        badgeColor = '#D97706';
        badgeText = '👑 ದರ ಜಿಗಿತ (10 AM Live)';
      } else {
        badgeColor = '#B45309';
        badgeText = '🪙 ಲೈವ್ ದರ (10 AM Live)';
      }
    } else {
      badgeColor = item.alert_level === 'red' ? '#DC2626' : (item.alert_level === 'orange' ? '#EA580C' : '#CA8A04');
      badgeText = item.alert_level === 'red' ? '🔴 ರೆಡ್ ಅಲರ್ಟ್' : (item.alert_level === 'orange' ? '🟠 ಆರೆಂಜ್ ಅಲರ್ಟ್' : '🟡 ಹಳದಿ ನಿಗಾ');
    }

    b.style.border = toastBorder;

    b.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px;">
        <div style="font-size:11.5px; font-weight:800; background:${badgeColor}; color:#FFF; padding:3px 9px; border-radius:6px;">${badgeText}</div>
        <button onclick="this.parentElement.parentElement.style.display='none'" style="background:none; border:none; color:#94A3B8; font-size:18px; cursor:pointer; padding:0 4px;">✕</button>
      </div>
      <strong style="display:block; font-size:14.5px; font-weight:800; color:#F8FAFC; margin-bottom:5px;">${item.title}</strong>
      <p style="font-size:12.5px; color:#CBD5E1; line-height:1.45; margin-bottom:14px;">${item.body}</p>
      <div style="display:flex; gap:8px;">
        <a href="${actionUrl}" style="flex:1; background:${isGold ? '#D97706' : '#0284C7'}; color:#FFF; text-align:center; padding:9px; border-radius:10px; font-size:12.5px; font-weight:800; text-decoration:none;">${actionBtnText}</a>
        <button onclick="window.karnataRequestPushPermission()" style="background:#16A34A; color:#FFF; border:none; padding:9px 14px; border-radius:10px; font-size:12.5px; font-weight:800; cursor:pointer;">🔔 ಆನ್ ಮಾಡಿ</button>
      </div>
    `;
    b.style.display = 'block';
  }

  // Global helper for user click on "ಆನ್ ಮಾಡಿ"
  window.karnataRequestPushPermission = async function() {
    if ('Notification' in window) {
      try {
        const perm = await Notification.requestPermission();
        if (perm === 'granted') {
          console.log('✅ Push notification permission granted!');
          const toast = document.getElementById('karnata-live-district-alert-toast');
          if (toast) toast.style.display = 'none';
          checkLiveDistrictPushFeed();
        }
      } catch(e) {}
    }
  };

  // ══════════════════════════════════════════════════════════════════════════════
  // ⚡ INSTANT TEST GOLD NOTIFICATION HELPER (For User / Developer Verification)
  // Usage in browser console:
  //   testGoldNotification('drop')   // Test Gold price drop notification
  //   testGoldNotification('surge')  // Test Gold price surge notification
  // ══════════════════════════════════════════════════════════════════════════════
  window.testGoldNotification = function(action = 'drop') {
    const isDrop = action !== 'surge';
    const testItem = {
      id: 'TEST-GOLD-' + (isDrop ? 'DROP' : 'SURGE') + '-' + Date.now(),
      alert_level: isDrop ? 'gold_drop' : 'gold_surge',
      target_district: 'all',
      target_district_kn: 'ಕರ್ನಾಟಕ ರಾಜ್ಯಾದ್ಯಂತ',
      title: isDrop 
        ? '🪙 ಇಂದಿನ ಚಿನ್ನದ ದರದಲ್ಲಿ ಭಾರಿ ಇಳಿಕೆ! ₹398 ಕುಸಿತ — ಖರೀದಿಗೆ ಸುವರ್ಣಾವಕಾಶ?' 
        : '👑 ಇಂದಿನ ಚಿನ್ನದ ದರದಲ್ಲಿ ಭಾರಿ ಜಿಗಿತ! 24K ₹15,207, 22K ₹13,935ಕ್ಕೆ ಏರಿಕೆ',
      body: isDrop
        ? '10 AM ಲೈವ್ ಅಪ್ಡೇಟ್: 24K ಚಿನ್ನ ಗ್ರಾಂಗೆ ₹398 ಇಳಿಕೆಯಾಗಿ ₹15,207 ಆಗಿದೆ! 22K ಆಭರಣ ಬಂಗಾರ ₹13,935 (1 ಪವನ್‌ಗೆ ₹2,920 ಉಳಿತಾಯ). ನಿಮ್ಮ ಜಿಲ್ಲೆಯ ದರ ನೋಡಿ ➔'
        : '10 AM ಲೈವ್ ಅಪ್ಡೇಟ್: ಇಂದು ಬುಲಿಯನ್ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಗ್ರಾಂಗೆ ₹250 ಏರಿಕೆ ಕಂಡಿದೆ. 8 ಗ್ರಾಂ (1 ಪವನ್) ಬೆಲೆ ₹1,11,480. ಇಂದಿನ ಲೈವ್ ದರ ಮತ್ತು ಟ್ರೆಂಡ್ ವಿಶ್ಲೇಷಿಸಿ ➔',
      url: 'https://karnata.in/gold-rate',
      icon: 'https://karnata.in/assets/icons/icon-512x512.png',
      badge: 'https://karnata.in/assets/icons/icon-192x192.png',
      topic: 'gold_rate_alert',
      created_at: new Date().toISOString()
    };
    dispatchNotification(testItem, getUserDistrict());
  };

  // ══════════════════════════════════════════════════════════════════════════════
  // ⚡ INSTANT TEST WEATHER NOTIFICATION HELPER
  // ══════════════════════════════════════════════════════════════════════════════
  window.testWeatherNotification = async function(level = 'yellow', distKey = null) {
    const dKey = distKey || getUserDistrict();
    const dObj = KARNATAKA_31_DISTRICTS.find(d => d.key === dKey) || KARNATAKA_31_DISTRICTS[0];
    const dKn = dObj.name_kn;
    const lvl = (level || 'yellow').toLowerCase();

    let testAlert = {
      id: 'TEST-WEATHER-' + lvl.toUpperCase() + '-' + Date.now(),
      alert_level: lvl,
      target_district: dKey,
      target_district_kn: dKn,
      url: `https://karnata.in/weather?district=${dKey}`
    };

    if (lvl === 'red') {
      testAlert.title = `🚨 ${dKn} ಕಟ್ಟೆಚ್ಚರ: ಅತಿ ಭಾರೀ ಮಳೆ & ಬಿರುಗಾಳಿ! (Red Alert)`;
      testAlert.body = `ಅಧಿಕೃತ ಮುನ್ನೆಚ್ಚರಿಕೆ 🌊: ${dKn} ಸುತ್ತಮುತ್ತ ಪ್ರವಾಹ ಹಾಗೂ ತೀವ್ರ ಬಿರುಗಾಳಿ ಸಹಿತ ಅತಿ ಭಾರೀ ಮಳೆ ಸಂಭವ! ಅನಗತ್ಯ ಪ್ರಯಾಣ ತಪ್ಪಿಸಿ, ಸುರಕ್ಷಿತ ಕಟ್ಟಡಗಳಲ್ಲಿರಿ ➔`;
    } else if (lvl === 'orange') {
      testAlert.title = `⛈️ ${dKn}: ಬಿರುಸಿನ ಮಳೆ & ಗುಡುಗು ಮುನ್ನೆಚ್ಚರಿಕೆ! (Orange Alert)`;
      testAlert.body = `IMD ಲೈವ್ ಎಚ್ಚರಿಕೆ ⚡: ${dKn} ಜಿಲ್ಲೆಯಾದ್ಯಂತ ಮುಂದಿನ ಕೆಲ ಗಂಟೆಗಳಲ್ಲಿ ಬಿರುಗಾಳಿ ಸಹಿತ ಧಾರಾಕಾರ ಮಳೆ ಸಾಧ್ಯತೆ! ಮರದ ಕೆಳಗೆ ಆಶ್ರಯ ಪಡೆಯಬೇಡಿ ➔`;
    } else {
      testAlert.title = `🌦️ ${dKn}: ಜಿಟಿಜಿಟಿ ಮಳೆ ಸಂಭವ! ಹೊರಡುವ ಮುನ್ನ ಗಮನಿಸಿ`;
      testAlert.body = `ಲೈವ್ ನೌಕಾಸ್ಟ್ 🌧️: ${dKn} ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಮುಂದಿನ 2-3 ಗಂಟೆಗಳಲ್ಲಿ ಹಗುರ ತುಂತುರು ಮಳೆ ಸಾಧ್ಯತೆ. ಹೊರಡುವಾಗ ಛತ್ರಿ ಜತೆಗಿರಲಿ! ಲೈವ್ ರೇಡಾರ್ ನೋಡಿ ➔`;
    }

    console.log('⚡ Triggering Test Weather Notification:', testAlert);
    dispatchNotification(testAlert, dKey);
  };

  // URL test parameter listener (e.g. ?test_push=1, ?test_alert=red, ?test_gold=drop, ?test_gold=surge)
  try {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('test_push') || urlParams.has('test_alert')) {
      const lvl = urlParams.get('test_alert') || 'yellow';
      setTimeout(() => {
        window.testWeatherNotification(lvl);
      }, 1500);
    }
    if (urlParams.has('test_gold')) {
      const gAction = urlParams.get('test_gold') || 'drop';
      setTimeout(() => {
        window.testGoldNotification(gAction);
      }, 1200);
    }
  } catch(e) {}

  // Initialize
  document.addEventListener('DOMContentLoaded', () => {
    detectUserGeoLocation();
    setTimeout(checkLiveDistrictPushFeed, 2000);
    // Periodic check every 30 seconds
    setInterval(checkLiveDistrictPushFeed, 30000);
  });
})();
