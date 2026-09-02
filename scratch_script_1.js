






    // ══════════════════════════════════════════════════════════════════════






    // FETCH LIVE IMD BENGALURU DISTRICT NOWCAST & WARNINGS






    // ══════════════════════════════════════════════════════════════════════






        async function loadImdNowcastWarnings() {

  const container = document.getElementById('imdNowcastContainer');

  const timeElem = document.getElementById('imdNowcastUpdateTime');

  if (!container) return;



  let districts = {};

  let updated_at = null;



  try {

    const res = await fetch('/api/weather/nowcast?t=' + Date.now(), { cache: 'no-store' });

    if (res.ok) {

      const data = await res.json();

      districts = data.districts || {};

      updated_at = data.updated_at;

    }

  } catch(e) {

    console.warn('Nowcast API fetch notice:', e);

  }



  // Direct client fallback to data-loader

  if (!Object.keys(districts).length) {

    try {

      if (typeof NK !== 'undefined' && NK.fetch) {

        const rawW = await NK.fetch('weather', 'weather.json');

        if (rawW && rawW.imd_warnings) {

          districts = rawW.imd_warnings;

          updated_at = rawW.updated_at;

        }

      }

    } catch(err) {}

  }



  if (timeElem && updated_at) {

    timeElem.textContent = 'IMD BENGALURU UPDATE: ' + new Date(updated_at).toLocaleTimeString('kn-IN', { hour: '2-digit', minute: '2-digit' });

  }



  const keys = Object.keys(districts);

  if (!keys.length) {

    container.innerHTML = `<div style="text-align:center; padding:24px; color:#64748B; grid-column:1/-1;">ಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳಲ್ಲಿ ಪ್ರಸ್ತುತ ಹವಾಮಾನ ಸ್ಥಿರವಾಗಿದೆ (ಹಸಿರು ವಲಯ - ಸುರಕ್ಷಿತ).</div>`;

    return;

  }



  container.innerHTML = keys.map(k => {

    const d = districts[k];

    let cardBg = '#FFFFFF';

    let cardBorder = '#E2E8F0';

    let badgeBg = '#DCFCE7';

    let badgeColor = '#166534';

    let titleColor = '#0F172A';

    let infoBoxBg = '#F8FAFC';

    let infoBorder = '#10B981';

    let infoTextColor = '#334155';



    const lvl = (d.alert_level || d.level || 'GREEN').toUpperCase();

    if (lvl === 'RED') {

      cardBg = '#FEF2F2'; cardBorder = '#EF4444'; badgeBg = '#DC2626'; badgeColor = '#FFFFFF'; titleColor = '#991B1B'; infoBoxBg = '#FFFFFF'; infoBorder = '#DC2626'; infoTextColor = '#7F1D1D';

    } else if (lvl === 'ORANGE') {

      cardBg = '#FFF7ED'; cardBorder = '#F97316'; badgeBg = '#EA580C'; badgeColor = '#FFFFFF'; titleColor = '#9A3412'; infoBoxBg = '#FFFFFF'; infoBorder = '#EA580C'; infoTextColor = '#7C2D12';

    } else if (lvl === 'YELLOW') {

      cardBg = '#FEFCE8'; cardBorder = '#EAB308'; badgeBg = '#CA8A04'; badgeColor = '#FFFFFF'; titleColor = '#854D0E'; infoBoxBg = '#FFFFFF'; infoBorder = '#CA8A04'; infoTextColor = '#713F12';

    }



    return `

      <div style="background:${cardBg}; border:1.5px solid ${cardBorder}; border-radius:16px; padding:16px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 4px 12px rgba(0,0,0,0.03);">

        <div>

          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">

            <div>

              <strong style="font-size:16px; font-weight:900; color:${titleColor}; display:block;">${d.district_kn || d.kn || d.district_en}</strong>

              <span style="font-size:11px; font-weight:700; color:#64748B;">${d.district_en || ''}</span>

            </div>

            <span style="background:${badgeBg}; color:${badgeColor}; font-size:11px; font-weight:900; padding:3px 10px; border-radius:12px;">${d.icon || '🌧️'} ${d.alert_level_kn || d.alert_level || 'ಮುನ್ನೆಚ್ಚರಿಕೆ'}</span>

          </div>

          <div style="background:${infoBoxBg}; border-left:3.5px solid ${infoBorder}; padding:10px 12px; border-radius:8px; margin-bottom:10px;">

            <div style="font-size:13px; font-weight:900; color:${titleColor}; margin-bottom:4px;">${d.hazard_kn || 'ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ'}</div>

            <div style="font-size:12px; color:${infoTextColor}; line-height:1.45;">${d.warning_info || 'ಯಾವುದೇ ಗಂಭೀರ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ ಇಲ್ಲ (ಸುರಕ್ಷಿತ)'}</div>

          </div>

        </div>

        <div style="font-size:11px; color:#64748B; font-weight:700; border-top:1px solid ${cardBorder}; padding-top:8px; display:flex; justify-content:space-between; align-items:center;">

          <span>🏛️ ${d.source || 'IMD ಬೆಂಗಳೂರು'}</span>

          <a href="https://mausam.imd.gov.in/imd_latest/contents/districtwisewarnings_mc.php?id=13" target="_blank" style="color:#0284C7; font-weight:800; text-decoration:none;">ಬುಲೆಟಿನ್ ↗</a>

        </div>

      </div>

    `;

  }).join('');

}



if (document.readyState === 'loading') {

  document.addEventListener('DOMContentLoaded', loadWeatherData);

} else {

  loadWeatherData();

}



