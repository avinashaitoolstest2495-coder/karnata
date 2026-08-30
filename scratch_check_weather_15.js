
    // ══════════════════════════════════════════════════════════════════════
    // FETCH LIVE IMD BENGALURU DISTRICT NOWCAST & WARNINGS
    // ══════════════════════════════════════════════════════════════════════
    async function loadImdNowcastWarnings() {
      const container = document.getElementById('imdNowcastContainer');
      const timeElem = document.getElementById('imdNowcastUpdateTime');
      if (!container) return;

      try {
        const res = await fetch('/api/weather/nowcast?t=' + Date.now(), { cache: 'no-store' });
        if (res.ok) {
          const data = await res.json();
          const districts = data.districts || {};
          const keys = Object.keys(districts);
          
          if (timeElem && data.updated_at) {
            timeElem.textContent = '⏱️ IMD ನವೀಕರಣ: ' + new Date(data.updated_at).toLocaleTimeString('kn-IN', { hour: '2-digit', minute: '2-digit' });
          }

          if (!keys.length) {
            container.innerHTML = `<div style="text-align:center; padding:20px; color:#94A3B8; grid-column:1/-1;">ಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಹವಾಮಾನ ಸ್ಥಿರವಾಗಿದೆ (ಹಸಿರು ವಲಯ).</div>`;
            return;
          }

          container.innerHTML = keys.map(k => {
            const d = districts[k];
            let badgeBg = '#065F46';
            let badgeColor = '#A7F3D0';
            let cardBorder = '#047857';

            if (d.alert_level === 'RED') {
              badgeBg = '#991B1B'; badgeColor = '#FEE2E2'; cardBorder = '#EF4444';
            } else if (d.alert_level === 'ORANGE') {
              badgeBg = '#9A3412'; badgeColor = '#FFEDD5'; cardBorder = '#F97316';
            } else if (d.alert_level === 'YELLOW') {
              badgeBg = '#854D0E'; badgeColor = '#FEF9C3'; cardBorder = '#EAB308';
            }

            return `
              <div style="background:rgba(15,23,42,0.7); border:1.5px solid ${cardBorder}; border-radius:14px; padding:14px; display:flex; flex-direction:column; justify-content:space-between;">
                <div>
                  <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                    <strong style="font-size:16px; color:#FFF;">${d.district_kn}</strong>
                    <span style="font-size:11px; font-weight:800; background:${badgeBg}; color:${badgeColor}; padding:3px 8px; border-radius:6px;">
                      ${d.severity_icon} ${d.alert_level_kn}
                    </span>
                  </div>
                  <p style="font-size:12.5px; color:#CBD5E1; line-height:1.45; margin:0 0 10px;">
                    ${d.warning_info}
                  </p>
                </div>
                <div style="font-size:11px; color:#64748B; border-top:1px solid rgba(255,255,255,0.1); padding-top:6px;">
                  🏛️ IMD ಬೆಂಗಳೂರು ಮುನ್ಸೂಚನೆ
                </div>
              </div>
            `;
          }).join('');
        }
      } catch(e) {
        console.warn('IMD Nowcast load notice:', e);
      }
    }

    document.addEventListener('DOMContentLoaded', loadImdNowcastWarnings);
