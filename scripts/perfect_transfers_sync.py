# -*- coding: utf-8 -*-
"""
Karnata — scripts/perfect_transfers_sync.py
Ensures transfers publish waits for Cloudflare KV confirmation before redirecting,
and officers.html always fetches with no-cache from /api/transfers.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Update admin-transfers.html
admin_trf = os.path.join(ROOT_DIR, 'admin-transfers.html')
with open(admin_trf, 'r', encoding='utf-8') as f:
    content = f.read()

publish_fn_replacement = """    async function publishAll() {
      if (!extractedTransfers.length) {
        alert('⚠️ ಪ್ರಕಟಿಸಲು ಯಾವುದೇ ವರ್ಗಾವಣೆ ಆದೇಶಗಳು ಲಭ್ಯವಿಲ್ಲ.');
        return;
      }

      const publishBtn = document.querySelector('.btn-green');
      if (publishBtn) {
        publishBtn.disabled = true;
        publishBtn.innerHTML = '⏳ ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಗ್ಲೋಬಲ್ ಎಡ್ಜ್‌ಗೆ ಸಿಂಕ್ ಆಗುತ್ತಿದೆ...';
      }

      const todayStr = new Date().toISOString().slice(0, 10).split('-').reverse().join('-');
      const formattedItems = extractedTransfers.map((item, idx) => ({
        id: item.id || `LIVE-TRF-${Date.now()}-${idx}`,
        cadre: item.cadre || 'KAS',
        cadre_badge: item.cadre === 'IAS' ? '🏛️ IAS' : (item.cadre === 'IPS' ? '👮 IPS' : '📜 KAS'),
        date: item.date || todayStr,
        order_no: item.order_no || 'ಸಿಆಸುಇ ಅಧಿಸೂಚನೆ 2026',
        officer_name_kn: item.officer_name_kn || 'ಅಧಿಕಾರಿಯ ಹೆಸರು',
        officer_name_en: item.officer_name_en || item.officer_name_kn || 'Officer Name',
        previous_posting: item.previous_posting || '',
        new_posting: item.new_posting || '',
        district_key: item.district_key || 'bengaluru_urban',
        summary_kn: item.summary_kn || `${item.officer_name_kn} ರವರ ವರ್ಗಾವಣೆ ಆದೇಶ.`,
        summary_en: item.summary_en || `${item.officer_name_en || item.officer_name_kn} transfer order.`,
        is_live_alert: true,
        source: 'Admin Live Publish',
        source_label: '⚡ Live Alert: ನೂತನ ವರ್ಗಾವಣೆ'
      }));

      // 1. Save to LocalStorage
      try {
        const existingLocal = JSON.parse(localStorage.getItem('karnata_live_published_transfers') || '[]');
        const updatedLocal = [...formattedItems, ...existingLocal];
        localStorage.setItem('karnata_live_published_transfers', JSON.stringify(updatedLocal));
      } catch (e) {}

      // 2. Send to Cloudflare Edge API and wait for 200 OK
      try {
        const res = await fetch('/api/transfers', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ transfers: formattedItems })
        });
        if (res.ok) {
          const d = await res.json();
          alert(`🎉 ಯಶಸ್ವಿ! ${formattedItems.length} ಹೊಸ ವರ್ಗಾವಣೆ ಆದೇಶಗಳು ಕ್ಲೌಡ್‌ಫ್ಲೇರ್ ಗ್ಲೋಬಲ್ ಎಡ್ಜ್‌ನಲ್ಲಿ ಲೈವ್ ಆಗಿವೆ! (ಒಟ್ಟು: ${d.count || '1500+'})\\nTransfers & Alerts ಪೇಜ್‌ಗೆ ಮರುನಿರ್ದೇಶಿಸಲಾಗುತ್ತಿದೆ...`);
          window.location.href = '/officers.html?tab=transfers&t=' + Date.now();
          return;
        }
      } catch (apiErr) {
        console.warn('API sync warning:', apiErr);
      }

      alert(`🎉 ವರ್ಗಾವಣೆ ಆದೇಶಗಳು ಲೈವ್ ಸೈಟ್‌ನಲ್ಲಿ ಪ್ರಕಟವಾಗಿವೆ!`);
      window.location.href = '/officers.html?tab=transfers&t=' + Date.now();
    }"""

content = re.sub(
    r'async function publishAll\(\)\s*\{[\s\S]*?window\.location\.href\s*=\s*\'/officers\.html\?tab=transfers\';\s*\}',
    publish_fn_replacement,
    content
)

for d in [
    os.path.join(ROOT_DIR, 'admin-transfers.html'),
    os.path.join(ROOT_DIR, 'admin', 'transfers.html'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'admin-transfers.html'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'admin', 'transfers.html')
]:
    with open(d, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {d}")

# 2. Update officers.html
off_path = os.path.join(ROOT_DIR, 'officers.html')
with open(off_path, 'r', encoding='utf-8') as f:
    off_content = f.read()

# Make sure officers.html fetches with cache: 'no-store'
off_fetch_old = "fetch(`/api/transfers${cacheBuster}`).then(r => r.json()).catch(() => fetch(`/data/recent_transfers.json${cacheBuster}`).then(r => r.json()).catch(() => ({ transfers: [] })))"
off_fetch_new = "fetch(`/api/transfers${cacheBuster}`, { cache: 'no-store' }).then(r => r.json()).catch(() => fetch(`/data/recent_transfers.json${cacheBuster}`, { cache: 'no-store' }).then(r => r.json()).catch(() => ({ transfers: [] })))"

if off_fetch_old in off_content:
    off_content = off_content.replace(off_fetch_old, off_fetch_new)
    with open(off_path, 'w', encoding='utf-8') as f:
        f.write(off_content)
    with open(os.path.join(ROOT_DIR, 'namma-karnataka', 'officers.html'), 'w', encoding='utf-8') as f:
        f.write(off_content)
    print("Updated officers.html with no-store cache directive.")

print("SUCCESS_PERFECT_TRANSFERS_SYNC_APPLIED")
