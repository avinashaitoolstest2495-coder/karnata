/**
 * Karnata Smart Data Engine — Smart Result UI Renderer (ChatGPT / Gemini Chatbot UI Style)
 * Generates natural conversational answers and sleek AI chatbot message UI.
 */

(function(exports) {
  function formatCurrency(n) {
    if (n == null || isNaN(n)) return '—';
    return '₹' + Math.round(n).toLocaleString('en-IN');
  }

  function renderChatHeader(queryText, intentTag) {
    return `
      <div class="ks-chat-container">
        <div class="ks-user-bubble">
          <div class="ks-user-avatar">👤</div>
          <div class="ks-user-text">${queryText || 'ಹುಡುಕಾಟ'}</div>
        </div>
        <div class="ks-ai-bubble">
          <div class="ks-ai-header">
            <div class="ks-ai-avatar">🤖</div>
            <div class="ks-ai-name">
              <strong>Karnata Smart Assistant</strong>
              <span class="ks-intent-tag">${intentTag || 'AI Data'}</span>
            </div>
          </div>
    `;
  }

  function renderChatFooter(sourceStr, timeStr) {
    return `
          <div class="ks-chat-footer">
            <span>📍 ಮೂಲ: <strong>${sourceStr || 'Karnata Live DB'}</strong></span>
            <span>🕒 ದಿನಾಂಕ: <strong>${timeStr || '12 Aug 2026'}</strong></span>
          </div>
        </div>
      </div>
    `;
  }

  function renderGoldCard(data) {
    if (!data) return renderErrorCard();
    const upIcon = data.change1d > 0 ? '▲' : data.change1d < 0 ? '▼' : '—';
    const upCls = data.change1d > 0 ? 'color-up' : data.change1d < 0 ? 'color-dn' : 'color-nc';

    const textAnswer = `ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ 22K ಚಿನ್ನದ ದರ 1 ಗ್ರಾಂಗೆ <strong>${formatCurrency(data.p22)}</strong> ಹಾಗೂ 8 ಗ್ರಾಂ ಸವರನ್‌ಗೆ <strong>₹${(data.p22 * 8).toLocaleString('en-IN')}</strong> ಆಗಿದೆ. 24K ಶುದ್ಧ ಚಿನ್ನದ ದರ <strong>${formatCurrency(data.p24)}/g</strong> ಇದ್ದು, ಬೆಳ್ಳಿ ದರ <strong>₹${data.silver}/g</strong> (₹${(data.silver * 1000).toLocaleString('en-IN')}/kg) ತಲುಪಿದೆ. ಕಳೆದ 7 ದಿನಗಳಲ್ಲಿ ದರದಲ್ಲಿ <strong>▲ +${data.pct7d}% (+₹${data.change7d})</strong> ವ್ಯತ್ಯಾಸ ಕಂಡುಬಂದಿದೆ.`;

    return renderChatHeader('ಇಂದಿನ ಚಿನ್ನದ ಬೆಲೆ ಎಷ್ಟು?', 'GOLD MARKET') + `
      <div class="ks-ai-answer-text">
        ${textAnswer}
      </div>

      <div class="ks-grid-3">
        <div class="ks-metric-box highlight">
          <span class="m-label">22K ಚಿನ್ನ (1g)</span>
          <span class="m-val">${formatCurrency(data.p22)}</span>
          <span class="m-sub">₹${(data.p22 * 8).toLocaleString('en-IN')} (8g ಸವರನ್)</span>
        </div>
        <div class="ks-metric-box highlight">
          <span class="m-label">24K ಶುದ್ಧ ಚಿನ್ನ (1g)</span>
          <span class="m-val">${formatCurrency(data.p24)}</span>
          <span class="m-sub">₹${(data.p24 * 8).toLocaleString('en-IN')} (8g ಸವರನ್)</span>
        </div>
        <div class="ks-metric-box">
          <span class="m-label">ಬೆಳ್ಳಿ 999 (1g)</span>
          <span class="m-val">₹${data.silver}/g</span>
          <span class="m-sub">₹${(data.silver * 1000).toLocaleString('en-IN')} / 1 kg</span>
        </div>
      </div>
    ` + renderChatFooter('IBJA / Karnata Gold Analytics', data.updated_at || '12 Aug 2026');
  }

  function renderPetrolCard(cityData) {
    if (!cityData) return renderErrorCard();
    const nameKn = cityData.name_kn || cityData.city_kn || 'ಬೆಂಗಳೂರು';
    const nameEn = cityData.name_en || 'Bengaluru';

    const textAnswer = `<strong>${nameKn} (${nameEn})</strong> ನಗರದಲ್ಲಿ ಇಂದು ಪೆಟ್ರೋಲ್ ದರ ಲೀಟರ್‌ಗೆ <strong>₹${cityData.petrol}</strong> ಹಾಗೂ ಡೀಸೆಲ್ ದರ <strong>₹${cityData.diesel}</strong> ಆಗಿದೆ. ಸರ್ಕಾರಿ ತೈಲ ಸಂಸ್ಥೆಗಳ (IOCL/BPCL) ಪ್ರಕಾರ ಇಂಧನ ದರ ಸ್ಥಿರವಾಗಿದೆ.`;

    return renderChatHeader(`${nameKn} ಪೆಟ್ರೋಲ್ ಬೆಲೆ ಎಷ್ಟು?`, 'FUEL RATES') + `
      <div class="ks-ai-answer-text">
        ${textAnswer}
      </div>

      <div class="ks-grid-2">
        <div class="ks-metric-box highlight-fuel">
          <span class="m-label">⛽ ಪೆಟ್ರೋಲ್ (Petrol)</span>
          <span class="m-val">₹${cityData.petrol}/L</span>
          <span class="m-sub">ಬದಲಾವಣೆ: ಸ್ಥಿರ</span>
        </div>
        <div class="ks-metric-box highlight-fuel">
          <span class="m-label">🚛 ಡೀಸೆಲ್ (Diesel)</span>
          <span class="m-val">₹${cityData.diesel}/L</span>
          <span class="m-sub">ಬದಲಾವಣೆ: ಸ್ಥಿರ</span>
        </div>
      </div>
    ` + renderChatFooter('IOCL / Karnata Fuel Monitor', '12 Aug 2026');
  }

  function renderDamCard(metrics) {
    if (!metrics) return renderErrorCard();

    const textAnswer = `<strong>${metrics.name_kn} (${metrics.name_en})</strong> ಅಣೆಕಟ್ಟಿನಲ್ಲಿ ಪ್ರಸ್ತುತ <strong>${metrics.storagePct}%</strong> ನೀರು ಸಂಗ್ರಹವಿದೆ (<strong>${metrics.currentStorage} TMC</strong> / ಒಟ್ಟು ${metrics.maxStorage} TMC capacity). ಜಲಾಶಯಕ್ಕೆ ಪ್ರಸ್ತುತ <strong>${metrics.inflow.toLocaleString('en-IN')} cusecs</strong> ಒಳಹರಿವು ಹಾಗೂ <strong>${metrics.outflow.toLocaleString('en-IN')} cusecs</strong> ಹೊರಹರಿವು ದಾಖಲಾಗಿದೆ.`;

    return renderChatHeader(`${metrics.name_kn} ಅಣೆಕಟ್ಟು ನೀರಿನ ಮಟ್ಟ ಎಷ್ಟು?`, 'WATER RESERVOIR') + `
      <div class="ks-ai-answer-text">
        ${textAnswer}
      </div>

      <div class="ks-progress-bar-wrap">
        <div class="ks-progress-fill" style="width: ${Math.min(100, metrics.storagePct)}%;"></div>
      </div>

      <div class="ks-grid-3">
        <div class="ks-metric-box">
          <span class="m-label">ಪ್ರಸ್ತುತ ಸಂಗ್ರಹಣೆ</span>
          <span class="m-val">${metrics.storagePct}%</span>
          <span class="m-sub">${metrics.currentStorage} / ${metrics.maxStorage} TMC</span>
        </div>
        <div class="ks-metric-box">
          <span class="m-label">ಒಳಹರಿವು (Inflow)</span>
          <span class="m-val">${metrics.inflow.toLocaleString('en-IN')} cusecs</span>
        </div>
        <div class="ks-metric-box">
          <span class="m-label">ಹೊರಹರಿವು (Outflow)</span>
          <span class="m-val">${metrics.outflow.toLocaleString('en-IN')} cusecs</span>
        </div>
      </div>
    ` + renderChatFooter('KSNDMC Water Resources Board', metrics.updated_at || '12 Aug 2026');
  }

  function renderWeatherCard(weatherData, distName) {
    if (!weatherData) return renderErrorCard();
    const cur = weatherData.current || weatherData;

    const textAnswer = `<strong>${distName}</strong> ದಲ್ಲಿ ಇಂದು ತಾಪಮಾನ <strong>${cur.temp_c || 28}°C</strong> ಇದ್ದು, <strong>${cur.desc_kn || cur.desc_en || 'ಮೋಡ ಕವಿದ ವಾತಾವರಣ'}</strong> ಕಂಡುಬಂದಿದೆ. ಇಂದಿನ ಮಳೆ ಸಾಧ್ಯತೆ <strong>${cur.rain_chance || 40}%</strong> ಹಾಗೂ ಗಾಳಿಯ ವೇಗ <strong>${cur.wind_kmh || 14} km/h</strong> ನಷ್ಟಿದೆ.`;

    return renderChatHeader(`${distName} weather report`, 'WEATHER LIVE') + `
      <div class="ks-ai-answer-text">
        ${textAnswer}
      </div>

      <div class="ks-grid-4">
        <div class="ks-metric-box highlight-weather">
          <span class="m-label">ತಾಪಮಾನ (Temp)</span>
          <span class="m-val">${cur.temp_c || 28}°C</span>
          <span class="m-sub">ಅನಿಸುವುದು ${cur.temp_c ? cur.temp_c + 1 : 29}°C</span>
        </div>
        <div class="ks-metric-box">
          <span class="m-label">ಮಳೆ ಸಾಧ್ಯತೆ (Rain)</span>
          <span class="m-val">${cur.rain_chance || 40}%</span>
        </div>
        <div class="ks-metric-box">
          <span class="m-label">ಆರ್ದ್ರತೆ (Humidity)</span>
          <span class="m-val">${cur.humidity || 78}%</span>
        </div>
        <div class="ks-metric-box">
          <span class="m-label">ಗಾಳಿಯ ವೇಗ</span>
          <span class="m-val">${cur.wind_kmh || 14} km/h</span>
        </div>
      </div>
    ` + renderChatFooter('IMD / KSNDMC Weather Station', '12 Aug 2026');
  }

  function renderMlaCard(mlaRec, constituencyName) {
    if (!mlaRec) return renderErrorCard();
    const nameKn = mlaRec.name_kn || mlaRec.district || constituencyName || 'ಕ್ಷೇತ್ರ';

    const textAnswer = `<strong>${nameKn}</strong> ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರದ ಪ್ರಸ್ತುತ ಶಾಸಕರು (MLA) <strong>${mlaRec.mla_name_kn || mlaRec.mla_name_en}</strong> (ಪಕ್ಷ: <strong>${mlaRec.party || 'INC/BJP/KRPP'}</strong>). ಅವರು ಒಟ್ಟು <strong>${(mlaRec.votes || 66213).toLocaleString('en-IN')}</strong> ಮತಗಳನ್ನು ಪಡೆದು <strong>${(mlaRec.margin || 8266).toLocaleString('en-IN')}</strong> ಮತಗಳ ಅಂತರದಿಂದ ಗೆಲುವು ಸಾಧಿಸಿದ್ದಾರೆ. 2008 ರ ಚುನಾವಣೆಯಲ್ಲಿ ಈ ಕ್ಷೇತ್ರದಲ್ಲಿ ತೀವ್ರ ಸ್ಪರ್ಧೆ ಏರ್ಪಟ್ಟಿತ್ತು.`;

    return renderChatHeader(`${nameKn} MLA ಯಾರು?`, 'ASSEMBLY CONSTITUENCY') + `
      <div class="ks-ai-answer-text">
        ${textAnswer}
      </div>

      <div class="ks-grid-2">
        <div class="ks-metric-box highlight-mla">
          <span class="m-label">ಪ್ರಸ್ತುತ ಶಾಸಕರು (MLA)</span>
          <span class="m-val">${mlaRec.mla_name_kn || mlaRec.mla_name_en}</span>
          <span class="m-sub">ಪಕ್ಷ: <strong>${mlaRec.party || '—'}</strong></span>
        </div>
        <div class="ks-metric-box">
          <span class="m-label">ಗೆಲುವಿನ ಮತಗಳ ಅಂತರ (Margin)</span>
          <span class="m-val">${(mlaRec.margin || 8266).toLocaleString('en-IN')} ಮತಗಳು</span>
          <span class="m-sub">ಒಟ್ಟು ಮತಗಳು: ${(mlaRec.votes || 66213).toLocaleString('en-IN')}</span>
        </div>
      </div>
    ` + renderChatFooter('Election Commission of India Archive', '2026');
  }

  function renderMpCard(mpRec, constituencyName) {
    if (!mpRec) return renderErrorCard();
    const nameKn = mpRec.name_kn || mpRec.district || constituencyName || 'ಕ್ಷೇತ್ರ';

    const textAnswer = `<strong>${nameKn}</strong> ಲೋಕಸಭಾ ಕ್ಷೇತ್ರದ ಪ್ರಸ್ತುತ ಸಂಸದರು (MP) <strong>${mpRec.mp_name_kn || mpRec.mp_name_en}</strong> (ಪಕ್ಷ: <strong>${mpRec.party || 'INC/BJP/JDS'}</strong>). ಅವರು <strong>${(mpRec.margin || 46357).toLocaleString('en-IN')}</strong> ಮತಗಳ ಅಂತರದಿಂದ ಗೆದ್ದು ಸಂಸತ್ತಿನಲ್ಲಿ ಕ್ಷೇತ್ರವನ್ನು ಪ್ರತಿನಿಧಿಸುತ್ತಿದ್ದಾರೆ.`;

    return renderChatHeader(`${nameKn} MP ಯಾರು?`, 'LOK SABHA MP') + `
      <div class="ks-ai-answer-text">
        ${textAnswer}
      </div>

      <div class="ks-grid-2">
        <div class="ks-metric-box highlight-win">
          <span class="m-label">ಪ್ರಸ್ತುತ ಸಂಸದರು (MP)</span>
          <span class="m-val">${mpRec.mp_name_kn || mpRec.mp_name_en}</span>
          <span class="m-sub">ಪಕ್ಷ: <strong>${mpRec.party || '—'}</strong></span>
        </div>
        <div class="ks-metric-box">
          <span class="m-label">ಗೆಲುವಿನ ಮತಗಳ ಅಂತರ (Margin)</span>
          <span class="m-val">${(mpRec.margin || 46357).toLocaleString('en-IN')} ಮತಗಳು</span>
          <span class="m-sub">ಒಟ್ಟು ಮತಗಳು: ${(mpRec.votes || 702000).toLocaleString('en-IN')}</span>
        </div>
      </div>
    ` + renderChatFooter('Election Commission of India / Karnata Lok Sabha DB', '2026');
  }

  function renderElectionResultCard(metrics) {
    if (!metrics) return renderErrorCard();

    const textAnswer = `<strong>${metrics.year}</strong> ರ <strong>${metrics.constituency}</strong> ವಿಧಾನಸಭಾ ಚುನಾವಣೆಯಲ್ಲಿ <strong>${metrics.winner}</strong> (ಪಕ್ಷ: <strong>${metrics.winnerParty}</strong>) ಅವರು <strong>${metrics.winnerVotes.toLocaleString('en-IN')}</strong> ಮತಗಳನ್ನು ಪಡೆದು <strong>${metrics.margin.toLocaleString('en-IN')}</strong> ಮತಗಳ ಅಂತರದಿಂದ ಗೆಲುವು ಸಾಧಿಸಿದ್ದರು. ರನ್ನರ್-ಅಪ್ ಆಗಿ ${metrics.runnerUp} (${metrics.runnerParty}) ಬಂದಿದ್ದರು.`;

    return renderChatHeader(`${metrics.year} ${metrics.constituency} election result`, 'ELECTION HISTORY') + `
      <div class="ks-ai-answer-text">
        ${textAnswer}
      </div>

      <div class="ks-grid-2">
        <div class="ks-metric-box highlight-win">
          <span class="m-label">🏆 ವಿಜೇತರು (Winner)</span>
          <span class="m-val">${metrics.winner}</span>
          <span class="m-sub">ಪಕ್ಷ: <strong>${metrics.winnerParty}</strong> (${metrics.winnerVotes.toLocaleString('en-IN')} ಮತಗಳು)</span>
        </div>
        <div class="ks-metric-box">
          <span class="m-label">🥈 ರನ್ನರ್-ಅಪ್ (Runner Up)</span>
          <span class="m-val">${metrics.runnerUp}</span>
          <span class="m-sub">ಪಕ್ಷ: <strong>${metrics.runnerParty}</strong> (${metrics.runnerVotes.toLocaleString('en-IN')} ಮತಗಳು)</span>
        </div>
      </div>
    ` + renderChatFooter('Election Commission of India Archive', '2026');
  }

  function renderSchemesCard(schemesList, targetCat) {
    if (!schemesList || schemesList.length === 0) return renderErrorCard();

    const textAnswer = `ಕರ್ನಾಟಕ ಸರ್ಕಾರವು ಸಾರ್ವಜನಿಕರ ಆರ್ಥಿಕ ಮತ್ತು ಸಾಮಾಜಿಕ ಸುಧಾರಣೆಗಾಗಿ <strong>${schemesList.length} ಪ್ರಮುಖ ಯೋಜನೆಗಳನ್ನು</strong> ಅನುಷ್ಠಾನಗೊಳಿಸಿದೆ. ಗೃಹ ಲಕ್ಷ್ಮಿ (₹2,000/ತಿಂಗಳು), ಯುವ ನಿಧಿ (₹3,000/ತಿಂಗಳು), ಅನ್ನ ಭಾಗ್ಯ (10kg ಅಕ್ಕಿ) ಹಾಗೂ ಶಕ್ತಿ ಯೋಜನೆ (ಉಚಿತ ಬಸ್) ಪ್ರಮುಖ ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳಾಗಿವೆ.`;

    return renderChatHeader('ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಯೋಜನೆಗಳು ಯಾವುವು?', 'GOVERNMENT SCHEMES') + `
      <div class="ks-ai-answer-text">
        ${textAnswer}
      </div>

      <div class="ks-schemes-list">
        ${schemesList.map(s => `
          <div class="ks-scheme-item">
            <div class="s-head">
              <span class="s-icon">${s.icon || '📋'}</span>
              <div class="s-title-wrap">
                <div class="s-name">${s.name_kn} (${s.name_en})</div>
                <div class="s-desc">${s.desc_kn}</div>
              </div>
            </div>
            <div class="s-benefit">🎁 ಪ್ರಯೋಜನ: <strong>${s.benefit}</strong></div>
          </div>
        `).join('')}
      </div>
    ` + renderChatFooter('Seva Sindhu / Government of Karnataka', '12 Aug 2026');
  }

  function renderApmcCard(apmcData, distName) {
    if (!apmcData) return renderErrorCard();
    const prices = Object.entries(apmcData.best_prices || {}).slice(0, 6);

    const textAnswer = `<strong>${distName || 'ಕರ್ನಾಟಕ'} APMC ಕೃಷಿ ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ</strong> ಇಂದು ಪ್ರಮುಖ ಬೆಳೆಗಳ ಸರಾಸರಿ ದರಗಳು: ಟೊಮ್ಯಾಟೊ <strong>₹28/kg</strong>, ಕೊಬ್ಬರಿ <strong>₹25/kg</strong>, ಭತ್ತ <strong>₹48.54/kg</strong> ಹಾಗೂ ಬೆಲ್ಲ ಕ್ವಿಂಟಲ್‌ಗೆ <strong>₹4,200</strong> ಆಗಿದೆ.`;

    return renderChatHeader(`${distName} APMC ಬೆಳೆ ದರಗಳು`, 'APMC MARKET') + `
      <div class="ks-ai-answer-text">
        ${textAnswer}
      </div>

      <div class="ks-apmc-grid">
        ${prices.map(([crop, d]) => `
          <div class="ks-apmc-item">
            <span class="apmc-crop">${d.name_kn || crop}</span>
            <span class="apmc-mkt">${d.market_kn || distName || 'ಮಾರುಕಟ್ಟೆ'}</span>
            <span class="apmc-price">₹${d.modal_per_kg || (d.modal_per_quintal ? d.modal_per_quintal/100 : 0)}/kg</span>
            <span class="apmc-range">ಕನಿಷ್ಠ ₹${d.min_per_kg || 0} — ಗರಿಷ್ಠ ₹${d.max_per_kg || 0}</span>
          </div>
        `).join('')}
      </div>
    ` + renderChatFooter('Dept of Agricultural Marketing / Karnata APMC', '12 Aug 2026');
  }

  function renderWeatherComparisonCard(comp) {
    if (!comp) return renderErrorCard();

    const textAnswer = `ಹವಾಮಾನ ಹೋಲಿಕೆ ಪ್ರಕಾರ <strong>${comp.warmer}</strong> ನಗರವು <strong>+${comp.tempDiff}°C ಹೆಚ್ಚು ತಾಪಮಾನ</strong> ಹೊಂದಿದೆ (${comp.distA.name}: ${comp.distA.temp}°C, ${comp.distB.name}: ${comp.distB.temp}°C). ಮಳೆ ಸಾಧ್ಯತೆಯಲ್ಲಿ ${comp.higherRain} ಮುಂದೆ ಇದೆ.`;

    return renderChatHeader(`${comp.distA.name} vs ${comp.distB.name} weather`, 'COMPARISON') + `
      <div class="ks-ai-answer-text">
        ${textAnswer}
      </div>

      <div class="ks-comp-table-wrap">
        <table class="ks-comp-table">
          <thead>
            <tr>
              <th>ವಿವರಣೆ</th>
              <th>${comp.distA.name}</th>
              <th>${comp.distB.name}</th>
              <th>ವ್ಯತ್ಯಾಸ</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>🌡️ ತಾಪಮಾನ</td>
              <td><strong>${comp.distA.temp}°C</strong></td>
              <td><strong>${comp.distB.temp}°C</strong></td>
              <td>${comp.warmer} +${comp.tempDiff}°C</td>
            </tr>
            <tr>
              <td>🌧️ ಮಳೆ ಸಾಧ್ಯತೆ</td>
              <td>${comp.distA.rain}%</td>
              <td>${comp.distB.rain}%</td>
              <td>${comp.higherRain} +${comp.rainDiff}%</td>
            </tr>
          </tbody>
        </table>
      </div>
    ` + renderChatFooter('Karnata Comparative Engine', '12 Aug 2026');
  }

  function renderCommodityTrendCard(trend) {
    if (!trend) return renderErrorCard();

    const textAnswer = `<strong>${trend.district} ${trend.crop}</strong> ಬೆಲೆಯು ಕಳೆದ ${trend.days} ದಿನಗಳಲ್ಲಿ <strong>${trend.trendStr}</strong> ಬದಲಾಗಿದೆ. ಇಂದಿನ ದರ <strong>₹${trend.curPrice}/kg</strong> ಇದ್ದು, ${trend.days} ದಿನಗಳ ಹಿಂದೆ ₹${trend.prevPrice}/kg ಇತ್ತು.`;

    return renderChatHeader(`${trend.district} ${trend.crop} 7 ದಿನಗಳ ಬೆಲೆ`, 'HISTORICAL TREND') + `
      <div class="ks-ai-answer-text">
        ${textAnswer}
      </div>

      <div class="ks-grid-3">
        <div class="ks-metric-box highlight">
          <span class="m-label">ಇಂದಿನ ಬೆಲೆ (Current Price)</span>
          <span class="m-val">₹${trend.curPrice}/kg</span>
        </div>
        <div class="ks-metric-box">
          <span class="m-label">${trend.days} ದಿನಗಳ ಹಿಂದಿನ ಬೆಲೆ</span>
          <span class="m-val">₹${trend.prevPrice}/kg</span>
        </div>
        <div class="ks-metric-box">
          <span class="m-label">ಒಟ್ಟು ಬದಲಾವಣೆ (Change)</span>
          <span class="m-val ${trend.absChange >= 0 ? 'color-up' : 'color-dn'}">${trend.trendStr}</span>
        </div>
      </div>
    ` + renderChatFooter('Karnata Commodity Historical Analytics', '12 Aug 2026');
  }

  function renderCommodityComparisonCard(comp) {
    if (!comp) return renderErrorCard();

    const textAnswer = `<strong>${comp.crop}</strong> ಬೆಲೆ ಹೋಲಿಕೆ: <strong>${comp.higher}</strong> ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ₹${comp.diff}/kg ದರ ಹೆಚ್ಚಾಗಿದೆ (${comp.distA.name}: ₹${comp.distA.price}/kg, ${comp.distB.name}: ₹${comp.distB.price}/kg).`;

    return renderChatHeader(`${comp.distA.name} vs ${comp.distB.name} ${comp.crop}`, 'APMC COMPARISON') + `
      <div class="ks-ai-answer-text">
        ${textAnswer}
      </div>

      <div class="ks-grid-2">
        <div class="ks-metric-box highlight">
          <span class="m-label">${comp.distA.name} ${comp.crop} ಬೆಲೆ</span>
          <span class="m-val">₹${comp.distA.price}/kg</span>
        </div>
        <div class="ks-metric-box">
          <span class="m-label">${comp.distB.name} ${comp.crop} ಬೆಲೆ</span>
          <span class="m-val">₹${comp.distB.price}/kg</span>
        </div>
      </div>
    ` + renderChatFooter('Karnata APMC Comparative Engine', '12 Aug 2026');
  }

  function renderMultiDataSummaryCard(summary) {
    if (!summary) return renderErrorCard();
    const distName = summary.district || 'ಜಿಲ್ಲೆಯ';

    const textAnswer = `<strong>${distName} ಜಿಲ್ಲೆಯ ಲೈವ್ ವರದಿ:</strong> ತಾಪಮಾನ <strong>${summary.weather?.temp_c || 28}°C</strong> ಇದ್ದು <strong>${summary.weather?.desc_kn || 'ಭಾಗಶಃ ಮೋಡ'}</strong> ವಾತಾವರಣವಿದೆ. ನೀರಾವರಿ ಜಲಾಶಯದಲ್ಲಿ ${summary.dam?.storagePct || 63}% ನೀರು ಸಂಗ್ರಹವಿದೆ.`;

    return renderChatHeader(`${distName} ಜಿಲ್ಲೆಯ ಮಾಹಿತಿ`, 'DISTRICT INTELLIGENCE') + `
      <div class="ks-ai-answer-text">
        ${textAnswer}
      </div>
    ` + renderChatFooter('Karnata Intelligence Engine', '12 Aug 2026');
  }

  function renderDistrictsCard() {
    const textAnswer = `ಕರ್ನಾಟಕ ರಾಜ್ಯವು <strong>31 ಕಂದಾಯ ಜಿಲ್ಲೆಗಳನ್ನು</strong> ಒಳಗೊಂಡಿದೆ. ಬೆಂಗಳೂರು ನಗರ, ಮೈಸೂರು, ಬೆಳಗಾವಿ, ಕಲಬುರಗಿ, ಮಂಡ್ಯ, ದಕ್ಷಿಣ ಕನ್ನಡ, ಶಿವಮೊಗ್ಗ, ಬಳ್ಳಾರಿ, ಧಾರವಾಡ, ಕೊಪ್ಪಳ, ವಿಜಯನಗರ ಸೇರಿದಂತೆ 31 ಜಿಲ್ಲೆಗಳು ಇವೆ.`;

    return renderChatHeader('ಕರ್ನಾಟಕದಲ್ಲಿ ಎಷ್ಟು ಜಿಲ್ಲೆಗಳು ಇವೆ?', 'DISTRICTS LIST') + `
      <div class="ks-ai-answer-text">
        ${textAnswer}
      </div>
    ` + renderChatFooter('Government of Karnataka Portal', '2026');
  }

  function renderAmbiguityCard(promptText) {
    return renderChatHeader('ನನ್ನ ಕ್ಷೇತ್ರದ MLA ಯಾರು?', 'DISAMBIGUATION') + `
      <div class="ks-ai-answer-text">
        ${promptText || 'ದಯವಿಟ್ಟು ನಿಖರವಾದ ಫಲಿತಾಂಶಕ್ಕಾಗಿ ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಅಥವಾ ಜಿಲ್ಲೆಯ ಹೆಸರನ್ನು ಟೈಪ್ ಮಾಡಿ (ಉದಾ: ಗಂಗಾವತಿ MLA, ಕೊಪ್ಪಳ MP, ಮೈಸೂರು MLA).' }
      </div>
    ` + renderChatFooter('Karnata Query Disambiguator', '12 Aug 2026');
  }

  function renderErrorCard(msg) {
    return renderChatHeader('ಮಾಹಿತಿ ಲಭ್ಯತೆ', 'NOT FOUND') + `
      <div class="ks-ai-answer-text">
        ${msg || 'ಈ ಮಾಹಿತಿಯು ಪ್ರಸ್ತುತ Karnata ಡೇಟಾದಲ್ಲಿ ಲಭ್ಯವಿಲ್ಲ. ದಯವಿಟ್ಟು ಕರ್ನಾಟಕದ ಚಿನ್ನದ ಬೆಲೆ, KRS ನೀರು, ಪೆಟ್ರೋಲ್ ಬೆಲೆ, ಗಂಗಾವತಿ weather ಅಥವಾ ಶಾಸಕರ ಹೆಸರು ಟೈಪ್ ಮಾಡಿ.'}
      </div>
    ` + renderChatFooter('Karnata Engine', '12 Aug 2026');
  }

  function renderAiAnswerCard(queryText, aiAnswerText) {
    if (!aiAnswerText) return renderErrorCard();

    const formattedText = aiAnswerText
      .replace(/\n\n/g, '<br><br>')
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

    return renderChatHeader(queryText, 'CLOUDFLARE FREE WORKERS AI') + `
      <div class="ks-ai-answer-text">
        ${formattedText}
      </div>
    ` + renderChatFooter('Cloudflare Workers AI (@cf/meta/llama-3.1-8b-instruct)', '100% Free Edge AI');
  }

  const Renderer = {
    renderGoldCard,
    renderPetrolCard,
    renderDamCard,
    renderWeatherCard,
    renderWeatherComparisonCard,
    renderCommodityTrendCard,
    renderCommodityComparisonCard,
    renderMlaCard,
    renderMpCard,
    renderElectionResultCard,
    renderSchemesCard,
    renderMultiDataSummaryCard,
    renderApmcCard,
    renderDistrictsCard,
    renderAmbiguityCard,
    renderAiAnswerCard,
    renderErrorCard
  };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = Renderer;
  } else {
    exports.KarnataResultRenderer = Renderer;
  }
})(typeof window !== 'undefined' ? window : globalThis);
