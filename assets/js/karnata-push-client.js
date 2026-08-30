/**
 * Karnata.in — Autonomous Real-Time Geo & District Push Notification Listener
 * Automatically detects user district, subscribes, and pops native notification
 * the instant a transfer, weather alert, or article is published.
 */

(function() {
  const STORAGE_KEY_DISTRICT = 'karnata_user_district_key';
  const STORAGE_KEY_SUB_ID = 'karnata_push_sub_id';
  const STORAGE_KEY_SEEN_PUSHES = 'karnata_seen_push_ids';

  const KARNATAKA_DISTRICTS = {
    "bengaluru_urban": "ಬೆಂಗಳೂರು ನಗರ",
    "bengaluru_rural": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ",
    "mysuru": "ಮೈಸೂರು",
    "belagavi": "ಬೆಳಗಾವಿ",
    "dharwad": "ಧಾರವಾಡ / ಹುಬ್ಬಳ್ಳಿ",
    "dakshina_kannada": "ದಕ್ಷಿಣ ಕನ್ನಡ (ಮಂಗಳೂರು)",
    "kalaburagi": "ಕಲಬುರಗಿ",
    "tumakuru": "ತುಮಕೂರು",
    "shivamogga": "ಶಿವಮೊಗ್ಗ",
    "ballari": "ಬಳ್ಳಾರಿ",
    "vijayanagara": "ವಿಜಯನಗರ",
    "vijayapura": "ವಿಜಯಪುರ",
    "bagalkote": "ಬಾಗಲಕೋಟೆ",
    "bidar": "ಬೀದರ್",
    "raichur": "ರಾಯಚೂರು",
    "koppal": "ಕೊಪ್ಪಳ",
    "gadag": "ಗದಗ",
    "haveri": "ಹಾವೇರಿ",
    "uttara_kannada": "ಉತ್ತರ ಕನ್ನಡ (ಕಾರವಾರ)",
    "udupi": "ಉಡುಪಿ",
    "chikkamagaluru": "ಚಿಕ್ಕಮಗಳೂರು",
    "hassan": "ಹಾಸನ",
    "mandya": "ಮಂಡ್ಯ",
    "chamarajanagar": "ಚಾಮರಾಜನಗರ",
    "chitradurga": "ಚಿತ್ರದುರ್ಗ",
    "davanagere": "ದಾವಣಗೆರೆ",
    "kolar": "ಕೋಲಾರ",
    "chikkaballapura": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
    "ramanagara": "ರಾಮನಗರ",
    "kodagu": "ಕೊಡಗು (ಮಡಿಕೇರಿ)",
    "yadgir": "ಯಾದಗಿರಿ"
  };

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

  // Register subscription with Cloudflare
  async function syncSubscriptionWithEdge(distKey) {
    let subId = localStorage.getItem(STORAGE_KEY_SUB_ID);
    if (!subId) {
      subId = 'SUB-' + Math.random().toString(36).substring(2, 9);
      localStorage.setItem(STORAGE_KEY_SUB_ID, subId);
    }
    const dist = distKey || getUserDistrict();
    try {
      await fetch('/api/push/subscribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          subscriber_id: subId,
          district: dist,
          district_kn: KARNATAKA_DISTRICTS[dist] || dist,
          topics: ['transfers', 'weather', 'fuel_gold', 'apmc', 'breaking']
        })
      });
    } catch(e) {}
  }

  // Autonomous Real-Time Feed Checker
  async function checkLiveDistrictPushFeed() {
    const dist = getUserDistrict();
    try {
      const res = await fetch(`/api/push/feed?district=${dist}&t=${Date.now()}`, { cache: 'no-store' });
      if (res.ok) {
        const data = await res.json();
        const feed = data.feed || [];
        if (!feed.length) return;

        const seenList = getSeenPushes();

        for (let item of feed) {
          if (!seenList.includes(item.id)) {
            addSeenPush(item.id);

            // Pop native notification if allowed
            if (Notification.permission === 'granted') {
              if ('serviceWorker' in navigator) {
                const reg = await navigator.serviceWorker.ready;
                reg.showNotification(item.title, {
                  body: item.body,
                  icon: item.icon || 'https://karnata.in/assets/icons/icon-512x512.png',
                  badge: item.badge || 'https://karnata.in/assets/icons/icon-192x192.png',
                  data: { url: item.url || 'https://karnata.in/officers?tab=transfers' },
                  vibrate: [200, 100, 200],
                  tag: item.id
                });
              } else {
                new Notification(item.title, { body: item.body, icon: item.icon });
              }
            } else if (Notification.permission !== 'denied') {
              // Auto request permission on user interest
              showInPagePushBanner(item);
            }
          }
        }
      }
    } catch(e) {}
  }

  function showInPagePushBanner(item) {
    let b = document.getElementById('karnata-live-district-alert-toast');
    if (!b) {
      b = document.createElement('div');
      b.id = 'karnata-live-district-alert-toast';
      b.style.cssText = 'position:fixed; top:20px; right:20px; max-width:380px; width:90%; background:#0F172A; color:#FFF; border:1px solid #334155; border-radius:16px; padding:16px; z-index:9999999; box-shadow:0 20px 40px rgba(0,0,0,0.5); font-family:system-ui,sans-serif; animation:slideIn 0.3s ease;';
      document.body.appendChild(b);
    }
    b.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
        <div style="font-size:11px; font-weight:800; background:#E11D48; color:#FFF; padding:2px 8px; border-radius:4px;">🚨 ಲೈವ್ ಅಲರ್ಟ್</div>
        <button onclick="this.parentElement.parentElement.style.display='none'" style="background:none; border:none; color:#94A3B8; font-size:16px; cursor:pointer;">✕</button>
      </div>
      <strong style="display:block; font-size:14.5px; color:#F8FAFC; margin-bottom:4px;">${item.title}</strong>
      <p style="font-size:12.5px; color:#CBD5E1; line-height:1.4; margin-bottom:12px;">${item.body}</p>
      <div style="display:flex; gap:8px;">
        <a href="${item.url}" style="flex:1; background:#2563EB; color:#FFF; text-align:center; padding:8px; border-radius:8px; font-size:12.5px; font-weight:700; text-decoration:none;">ವೀಕ್ಷಿಸಿ ➔</a>
        <button onclick="window.karnataRequestPushPermission()" style="background:#059669; color:#FFF; border:none; padding:8px 12px; border-radius:8px; font-size:12.5px; font-weight:700; cursor:pointer;">🔔 ಆನ್ ಮಾಡಿ</button>
      </div>
    `;
  }

  // Auto-detect Geo-Location if permitted
  function autoDetectGeo() {
    if (navigator.geolocation && !localStorage.getItem(STORAGE_KEY_DISTRICT)) {
      navigator.geolocation.getCurrentPosition(pos => {
        const lat = pos.coords.latitude;
        const lon = pos.coords.longitude;
        let matched = 'bengaluru_urban';
        if (lat > 15.5 && lon < 75.0) matched = 'belagavi';
        else if (lat > 15.0 && lon > 74.8 && lon < 75.6) matched = 'dharwad';
        else if (lat < 12.6 && lon > 76.2 && lon < 77.0) matched = 'mysuru';
        else if (lat > 17.0) matched = 'kalaburagi';
        else if (lat > 12.8 && lat < 13.5 && lon < 75.2) matched = 'dakshina_kannada';

        localStorage.setItem(STORAGE_KEY_DISTRICT, matched);
        syncSubscriptionWithEdge(matched);
      }, () => {
        syncSubscriptionWithEdge('bengaluru_urban');
      });
    } else {
      syncSubscriptionWithEdge(getUserDistrict());
    }
  }

  // Setup Real-time Reactive Listener
  document.addEventListener('DOMContentLoaded', () => {
    autoDetectGeo();
    // Fast Polling loop (every 15s for true real-time automatic triggers)
    setInterval(checkLiveDistrictPushFeed, 15000);
    setTimeout(checkLiveDistrictPushFeed, 1500);
  });
})();
