/**
 * Karnata.in — Precision District Government Order (GO) Alert Engine
 * Rules:
 * 1. ONLY fresh Government Orders (GO / ಅಧಿಸೂಚನೆ) published within the last 72 hours qualify.
 * 2. Matches user's specific district (GPS / IP / selected district) — no spam from other districts.
 * 3. Shows clean localized notification card and triggers browser push alert once.
 */

(function(window) {
  const STORAGE_SEEN_KEY = 'karnata_seen_go_orders_v3';
  const DISTRICT_KEY = 'karnata_user_district';

  const DISTRICT_NAMES_KN = {
    koppal: "ಕೊಪ್ಪಳ", mysuru: "ಮೈಸೂರು", bengaluru_urban: "ಬೆಂಗಳೂರು",
    tumakuru: "ತುಮಕೂರು", haveri: "ಹಾವೇರಿ", yadgir: "ಯಾದಗಿರಿ",
    belagavi: "ಬೆಳಗಾವಿ", kalaburagi: "ಕಲಬುರಗಿ", dakshina_kannada: "ದಕ್ಷಿಣ ಕನ್ನಡ",
    vijayapura: "ವಿಜಯಪುರ", dharwad: "ಧಾರವಾಡ", shivamogga: "ಶಿವಮೊಗ್ಗ",
    udupi: "ಉಡುಪಿ", ballari: "ಬಳ್ಳಾರಿ", vijayanagara: "ವಿಜಯನಗರ",
    bagalkote: "ಬಾಗಲಕೋಟೆ", bidar: "ಬೀದರ್", raichur: "ರಾಯಚೂರು",
    gadag: "ಗದಗ", uttara_kannada: "ಉತ್ತರ ಕನ್ನಡ", chikkamagaluru: "ಚಿಕ್ಕಮಗಳೂರು",
    hassan: "ಹಾಸನ", mandya: "ಮಂಡ್ಯ", chamarajanagar: "ಚಾಮರಾಜನಗರ",
    chitradurga: "ಚಿತ್ರದುರ್ಗ", davanagere: "ದಾವಣಗೆರೆ", kolar: "ಕೋಲಾರ",
    chikkaballapura: "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", ramanagara: "ರಾಮನಗರ", kodagu: "ಕೊಡಗು"
  };

  function parseDateToTimestamp(dateStr) {
    if (!dateStr) return 0;
    const parts = dateStr.trim().split(/[\.\-\/]/);
    if (parts.length === 3) {
      // Check if DD-MM-YYYY or YYYY-MM-DD
      if (parts[0].length === 4) {
        return new Date(parts[0], parts[1] - 1, parts[2]).getTime();
      } else {
        return new Date(parts[2], parts[1] - 1, parts[0]).getTime();
      }
    }
    return 0;
  }

  function isRecentGO(dateStr) {
    if (!dateStr) return false;
    const ts = parseDateToTimestamp(dateStr);
    if (!ts) return false;
    const now = Date.now();
    // Valid within last 3 days (3 * 24 * 60 * 60 * 1000 = 259,200,000 ms)
    // Or future/same day
    const diff = now - ts;
    return diff <= 259200000 && diff >= -86400000;
  }

  function getUserDistrict() {
    if (typeof localStorage === 'undefined') return 'bengaluru_urban';
    const saved = localStorage.getItem(DISTRICT_KEY) || localStorage.getItem('nk_s3') || localStorage.getItem('user_district');
    if (!saved) return 'bengaluru_urban';
    try {
      if (saved.startsWith('{')) {
        const obj = JSON.parse(saved);
        return (obj.district || obj.key || 'bengaluru_urban').toLowerCase().replace('-', '_');
      }
      return saved.toLowerCase().replace('-', '_');
    } catch(e) {
      return 'bengaluru_urban';
    }
  }

  function getSeenOrders() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_SEEN_KEY) || '[]');
    } catch(e) {
      return [];
    }
  }

  function markOrderSeen(orderId) {
    const seen = getSeenOrders();
    if (!seen.includes(orderId)) {
      seen.push(orderId);
      localStorage.setItem(STORAGE_SEEN_KEY, JSON.stringify(seen));
    }
  }

  function showDistrictToast(transfer) {
    const toast = document.getElementById('toast-alert') || document.getElementById('toast-notification');
    const msgEl = document.getElementById('toast-msg');
    if (!toast || !msgEl) return;

    const distName = DISTRICT_NAMES_KN[transfer.district_key] || transfer.district_kn || "ಕರ್ನಾಟಕ";

    msgEl.innerHTML = `
      <div style="font-weight:800; font-size:13.5px; color:#1D4ED8; margin-bottom:4px; display:flex; align-items:center; gap:6px;">
        <span>🔔</span> <span>${distName} ಜಿಲ್ಲಾ ನೂತನ ವರ್ಗಾವಣೆ ಆದೇಶ (GO Alert):</span>
      </div>
      <div style="font-weight:700; font-size:15px; color:#0F172A; margin-bottom:4px;">
        ${transfer.officer_name_kn || 'ಅಧಿಕಾರಿ ವರ್ಗಾವಣೆ'}
      </div>
      <div style="font-size:13px; color:#475569; line-height:1.45;">
        ${transfer.previous_posting && transfer.new_posting ? `<span style="color:#64748B;">${transfer.previous_posting}</span> ➔ <strong style="color:#059669;">${transfer.new_posting}</strong>` : (transfer.summary_kn || '')}
      </div>
      <div style="margin-top:10px; display:flex; justify-content:space-between; align-items:center; border-top:1px dashed #E2E8F0; padding-top:6px;">
        <span style="font-size:11.5px; color:#64748B;">📅 ${transfer.date || 'ಇಂದು'} | ಆದೇಶ: ${transfer.order_no || 'DPAR'}</span>
        <a href="/officers.html?tab=transfers" style="color:#2563EB; font-size:12px; font-weight:800; text-decoration:none;">ಆದೇಶ ಪರಿಶೀಲಿಸಿ →</a>
      </div>
    `;
    toast.style.display = 'block';

    // Auto dismiss after 10 seconds
    setTimeout(() => {
      if (toast) toast.style.display = 'none';
    }, 10000);
  }

  function triggerBrowserNotification(transfer) {
    if (typeof Notification !== 'undefined') {
      if (Notification.permission === 'granted') {
        const distName = DISTRICT_NAMES_KN[transfer.district_key] || transfer.district_kn || "ಕರ್ನಾಟಕ";
        try {
          new Notification(`🔔 ${distName} ಜಿಲ್ಲಾ ನೂತನ ವರ್ಗಾವಣೆ ಆದೇಶ`, {
            body: `${transfer.officer_name_kn}: ${transfer.new_posting || transfer.summary_kn}`,
            icon: '/favicon.ico'
          });
        } catch(e) {}
      } else if (Notification.permission !== 'denied') {
        Notification.requestPermission();
      }
    }
  }

  function checkTransferAlerts(transfersList) {
    if (!transfersList || transfersList.length === 0) return;
    const userDist = getUserDistrict();
    const seen = getSeenOrders();

    // STRICT FILTER:
    // 1. Must be a recently published GO (within last 72 hours or flagged as is_new_go_alert)
    // 2. Must match the user's specific district (or be a top statewide breaking GO)
    // 3. Must NOT have been seen before on this device
    const targetTransfer = transfersList.find(t => {
      const isFresh = t.is_new_go_alert || isRecentGO(t.date);
      const isDistrictMatch = (t.district_key === userDist) || (t.summary_kn && t.summary_kn.includes(DISTRICT_NAMES_KN[userDist]));
      const isUnseen = !seen.includes(t.id);
      return isFresh && isDistrictMatch && isUnseen;
    });

    if (targetTransfer) {
      showDistrictToast(targetTransfer);
      triggerBrowserNotification(targetTransfer);
      markOrderSeen(targetTransfer.id);
    }
  }

  // Ask for browser notification permission on user engagement
  document.addEventListener('click', function reqPerm() {
    if (typeof Notification !== 'undefined' && Notification.permission === 'default') {
      Notification.requestPermission();
    }
    document.removeEventListener('click', reqPerm);
  }, { once: true });

  window.DistrictNotificationEngine = {
    getUserDistrict,
    checkTransferAlerts
  };
})(window);
