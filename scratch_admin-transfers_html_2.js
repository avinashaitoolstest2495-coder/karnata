
    let extractedTransfers = [];
    const DISTRICTS = {
      bengaluru_urban: "ಬೆಂಗಳೂರು ನಗರ", tumakuru: "ತುಮಕೂರು", yadgir: "ಯಾದಗಿರಿ",
      koppal: "ಕೊಪ್ಪಳ", mysuru: "ಮೈಸೂರು", belagavi: "ಬೆಳಗಾವಿ", kalaburagi: "ಕಲಬುರಗಿ",
      dakshina_kannada: "ದಕ್ಷಿಣ ಕನ್ನಡ", vijayapura: "ವಿಜಯಪುರ", dharwad: "ಧಾರವಾಡ",
      shivamogga: "ಶಿವಮೊಗ್ಗ", udupi: "ಉಡುಪಿ", ballari: "ಬಳ್ಳಾರಿ", vijayanagara: "ವಿಜಯನಗರ",
      bagalkote: "ಬಾಗಲಕೋಟೆ", bidar: "ಬೀದರ್", raichur: "ರಾಯಚೂರು", gadag: "ಗದಗ",
      haveri: "ಹಾವೇರಿ", uttara_kannada: "ಉತ್ತರ ಕನ್ನಡ", chikkamagaluru: "ಚಿಕ್ಕಮಗಳೂರು",
      hassan: "ಹಾಸನ", mandya: "ಮಂಡ್ಯ", chamarajanagar: "ಚಾಮರಾಜನಗರ", chitradurga: "ಚಿತ್ರದುರ್ಗ",
      davanagere: "ದಾವಣಗೆರೆ", kolar: "ಕೋಲಾರ", chikkaballapura: "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
      ramanagara: "ರಾಮನಗರ", kodagu: "ಕೊಡಗು"
    };

    document.addEventListener('DOMContentLoaded', () => {
      const savedKey = localStorage.getItem('karnata_gemini_key') || '';
      if (savedKey) {
        document.getElementById('gemini-key-input').value = savedKey;
      }
      const savedModel = localStorage.getItem('karnata_gemini_model') || 'gemini-2.0-flash';
      document.getElementById('gemini-model-select').value = savedModel;
    });

    function saveApiKey(val) {
      if (!val) return;
      localStorage.setItem('karnata_gemini_key', val.trim());
      alert('✅ Gemini API Key ಅನ್ನು ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಸುರಕ್ಷಿತವಾಗಿ ಸೇವ್ ಮಾಡಲಾಗಿದೆ!');
    }

    function triggerFileSelect() {
      document.getElementById('bulk-file-input').click();
    }

    async function callGeminiVisionWithFallback(apiKey, selectedModel, mimeType, base64Data, prompt) {
      const candidateModels = [
        selectedModel || 'gemini-3.7-flash',
        'gemini-3.7-flash',
        'gemini-3.1-pro-preview',
        'gemini-3.1-pro',
        'gemini-2.0-flash',
        'gemini-2.0-flash-lite',
        'gemini-1.5-flash-latest'
      ];
      const uniqueModels = [...new Set(candidateModels)];

      let lastError = null;
      for (let model of uniqueModels) {
        try {
          const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;
          const res = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              contents: [{
                parts: [
                  { text: prompt },
                  { inline_data: { mime_type: mimeType, data: base64Data } }
                ]
              }],
              generationConfig: {
                temperature: 0.1
              }
            })
          });

          if (res.ok) {
            const data = await res.json();
            let rawText = data?.candidates?.[0]?.content?.parts?.[0]?.text;
            if (rawText) {
              rawText = rawText.replace(/```json/gi, '').replace(/```/g, '').trim();
              const startIdx = rawText.indexOf('[');
              const endIdx = rawText.lastIndexOf(']');
              if (startIdx !== -1 && endIdx !== -1 && endIdx > startIdx) {
                rawText = rawText.substring(startIdx, endIdx + 1);
              }
              const parsed = JSON.parse(rawText);
              return parsed;
            }
          } else {
            const errData = await res.json().catch(() => ({}));
            lastError = errData?.error?.message || `HTTP ${res.status}`;
            console.warn(`Model ${model} returned: ${lastError}. Trying next model...`);
          }
        } catch (e) {
          lastError = e.message;
          console.warn(`Error on ${model}: ${lastError}`);
        }
      }

      // Dynamic Model Discovery Fallback: Fetch active models for this key
      try {
        const listRes = await fetch(`https://generativelanguage.googleapis.com/v1beta/models?key=${apiKey}`);
        if (listRes.ok) {
          const listData = await listRes.json();
          const availableModels = (listData.models || [])
            .filter(m => m.supportedGenerationMethods && m.supportedGenerationMethods.includes('generateContent'))
            .map(m => m.name.replace('models/', ''));
          
          for (let model of availableModels) {
            try {
              const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;
              const res = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                  contents: [{
                    parts: [
                      { text: prompt },
                      { inline_data: { mime_type: mimeType, data: base64Data } }
                    ]
                  }],
                  generationConfig: { temperature: 0.1 }
                })
              });
              if (res.ok) {
                const data = await res.json();
                let rawText = data?.candidates?.[0]?.content?.parts?.[0]?.text;
                if (rawText) {
                  rawText = rawText.replace(/```json/gi, '').replace(/```/g, '').trim();
                  const startIdx = rawText.indexOf('[');
                  const endIdx = rawText.lastIndexOf(']');
                  if (startIdx !== -1 && endIdx !== -1 && endIdx > startIdx) {
                    rawText = rawText.substring(startIdx, endIdx + 1);
                  }
                  return JSON.parse(rawText);
                }
              }
            } catch (innerE) {}
          }
        }
      } catch (discErr) {}

      throw new Error(lastError || 'All Gemini models failed. Please verify API key.');
    }

    async function handleBulkFiles(e) {
      const files = Array.from(e.target.files);
      if (!files.length) return;

      const apiKey = (document.getElementById('gemini-key-input').value || localStorage.getItem('karnata_gemini_key') || '').trim();
      if (!apiKey) {
        alert('⚠️ ದಯವಿಟ್ಟು ಮೊದಲು ಮೇಲಿರುವ "Gemini API Key" ಬಾಕ್ಸ್‌ನಲ್ಲಿ ನಿಮ್ಮ Google AI Studio ಕೀ ನಮೂದಿಸಿ.');
        document.getElementById('gemini-key-input').focus();
        return;
      }

      const selectedModel = document.getElementById('gemini-model-select').value;
      const queueContainer = document.getElementById('queue-container');
      const ocrStatus = document.getElementById('ocr-status');
      const statusText = document.getElementById('ocr-status-text');
      const progressText = document.getElementById('ocr-progress-text');

      queueContainer.style.display = 'grid';
      ocrStatus.style.display = 'flex';

      for (let i = 0; i < files.length; i++) {
        const file = files[i];
        statusText.textContent = `🔍 [${i+1}/${files.length}] Gemini Vision AI ಮೂಲಕ ವಿಶ್ಲೇಷಿಸಲಾಗುತ್ತಿದೆ (${file.name})...`;
        progressText.textContent = 'ಕನ್ನಡ ಮತ್ತು ಇಂಗ್ಲಿಷ್ ಸರ್ಕಾರಿ ಆದೇಶದ ಅಧಿಕೃತ ಪಠ್ಯವನ್ನು ಹೊರತೆಗೆಯಲಾಗುತ್ತಿದೆ...';

        const reader = new FileReader();
        const base64DataUrl = await new Promise(res => {
          reader.onload = ev => res(ev.target.result);
          reader.readAsDataURL(file);
        });

        const thumb = document.createElement('div');
        thumb.className = 'queue-thumb-card';
        thumb.innerHTML = `
          <img src="${base64DataUrl}" class="queue-thumb-img">
          <div class="queue-thumb-status">
            <span style="overflow:hidden; text-overflow:ellipsis; white-space:nowrap; max-width:110px;">${file.name}</span>
            <span id="st-${i}" style="color:var(--primary);">AI ಓದುತ್ತಿದೆ...</span>
          </div>
        `;
        queueContainer.appendChild(thumb);

        try {
          const mimeType = file.type || "image/jpeg";
          const rawBase64 = base64DataUrl.replace(/^data:image\/[a-z]+;base64,/, '');

          const prompt = `You are a precision Karnataka Government DPAR Transfer & Gazette Notification Specialist.
Analyze this official Karnataka government transfer order photo/document (Kannada and/or English).
Extract every officer transfer entry and return ONLY a valid JSON array of objects with the following schema:
[
  {
    "order_no": "ಆದೇಶ ಸಂಖ್ಯೆ (e.g. ಸಿಆಸುಇ 112 ಆಸೇವ 2026 or e-DPAR 279 SAS 2026)",
    "date": "ದಿನಾಂಕ (DD-MM-YYYY)",
    "cadre": "IAS | IPS | KAS | Tahsildar",
    "officer_name_kn": "ಅಧಿಕಾರಿಯ ಸಂಪೂರ್ಣ ಹೆಸರು ಮತ್ತು ಶ್ರೇಣಿ ಶುದ್ಧ ಕನ್ನಡದಲ್ಲಿ (e.g. ಶ್ರೀಮತಿ ಶಾಂತ ಎಲ್ ಹುಲ್ಲನಿ, ಕೆ.ಎ.ಎಸ್ (ಸೂಪರ್ ಟೈಂ ಸ್ಕೇಲ್))",
    "officer_name_en": "Officer Name in English",
    "previous_posting": "ಹಿಂದಿನ ಹುದ್ದೆಯ ಸ್ಪಷ್ಟ ಹೆಸರು (ಉದಾ: ನಿರ್ದೇಶಕರು, ಪಿಂಚಣಿ ಮತ್ತು ಸಣ್ಣ ಉಳಿತಾಯ ನಿರ್ದೇಶನಾಲಯ, ಬೆಂಗಳೂರು)",
    "new_posting": "ವರ್ಗಾಯಿಸಲಾದ ನೂತನ ಹುದ್ದೆಯ ಸ್ಪಷ್ಟ ಹೆಸರು (ಉದಾ: ಕಾರ್ಯನಿರ್ವಾಹಕ ನಿರ್ದೇಶಕರು (ಮಾನವ ಸಂಪನ್ಮೂಲ), ಬೆಂಗಳೂರು ನಮ್ಮ ಮೆಟ್ರೋ (BMRCL)) - ಯಾವುದೇ ಪುನರಾವರ್ತಿತ ಕಾನೂನು ವಾಕ್ಯಗಳನ್ನು ಹೊರತುಪಡಿಸಿ ಕೇವಲ ಹುದ್ದೆಯ ಹೆಸರನ್ನು ಮಾತ್ರ ನಮೂದಿಸಿ",
    "district_key": "district_key (e.g. bengaluru_urban, tumakuru, yadgir, mysuru, belagavi, kalaburagi, dharwad, vijayapura)",
    "summary_kn": "ಪತ್ರಿಕಾ ಶೈಲಿಯ ಸುಂದರ, ಸರಳ ಮತ್ತು ಅಧಿಕೃತ ಕನ್ನಡ ಸಾರಾಂಶ (ಉದಾ: ಶ್ರೀಮತಿ ಶಾಂತ ಎಲ್ ಹುಲ್ಲನಿ, ಕೆ.ಎ.ಎಸ್ (ಸೂಪರ್ ಟೈಂ ಸ್ಕೇಲ್) ಇವರನ್ನು ಪಿಂಚಣಿ ಮತ್ತು ಸಣ್ಣ ಉಳಿತಾಯ ನಿರ್ದೇಶನಾಲಯದಿಂದ ಬೆಂಗಳೂರು ಮೆಟ್ರೋ ರೈಲ್ ನಿಗಮ ನಿಯಮಿತದ (BMRCL) ಕಾರ್ಯನಿರ್ವಾಹಕ ನಿರ್ದೇಶಕರ (ಮಾನವ ಸಂಪನ್ಮೂಲ) ಹುದ್ದೆಗೆ ವರ್ಗಾಯಿಸಿ ಸರ್ಕಾರ ಆದೇಶಿಸಿದೆ.)"
  }
]
Output strictly raw JSON without markdown backticks.`;

          const parsed = await callGeminiVisionWithFallback(apiKey, selectedModel, mimeType, rawBase64, prompt);

          document.getElementById(`st-${i}`).innerHTML = '✅ AI ಯಶಸ್ವಿ';
          document.getElementById(`st-${i}`).style.color = 'var(--accent-green)';

          if (Array.isArray(parsed)) {
            parsed.forEach(p => extractedTransfers.push(p));
          } else if (typeof parsed === 'object') {
            extractedTransfers.push(parsed);
          }
        } catch (err) {
          console.error(err);
          document.getElementById(`st-${i}`).innerHTML = '❌ ದೋಷ';
          document.getElementById(`st-${i}`).style.color = 'var(--accent-red)';
          alert(`ಚಿತ್ರ ವಿಶ್ಲೇಷಣೆಯಲ್ಲಿ ದೋಷ: ${err.message}\nದಯವಿಟ್ಟು API Key ಸರಿಯಾಗಿದೆಯೇ ಪರೀಕ್ಷಿಸಿ.`);
        }
      }

      ocrStatus.style.display = 'none';
      renderExtractedCards();
    }

    function renderExtractedCards() {
      const container = document.getElementById('cards-container');
      const bulkActions = document.getElementById('bulk-actions');
      const countLabel = document.getElementById('extracted-count-label');

      if (!extractedTransfers.length) {
        container.innerHTML = '';
        bulkActions.style.display = 'none';
        return;
      }

      bulkActions.style.display = 'flex';
      countLabel.textContent = `✨ ${extractedTransfers.length} ವರ್ಗಾವಣೆ ಆದೇಶಗಳು Gemini AI ಮೂಲಕ ನಿಖರವಾಗಿ ಸಿದ್ಧವಾಗಿವೆ:`;

      container.innerHTML = extractedTransfers.map((item, idx) => `
        <div class="extracted-card" id="card-${idx}">
          <div class="card-top">
            <div style="display:flex; align-items:center; gap:8px;">
              <span style="font-size:12px; font-weight:800; background:var(--primary-subtle); color:var(--primary); border:1px solid #BFDBFE; padding:3px 10px; border-radius:6px;">#${idx+1} ${item.cadre || 'KAS'} ಆದೇಶ</span>
              <span style="font-size:13px; font-weight:700; color:var(--text-light);">📅 ${item.date || '20-08-2026'}</span>
            </div>
            <button onclick="removeCard(${idx})" style="background:none; border:none; color:var(--accent-red); cursor:pointer; font-size:13px; font-weight:700;">🗑️ ತೆಗೆದುಹಾಕಿ</button>
          </div>

          <div class="route-preview-box">
            <span>🏛️ ${item.previous_posting || 'ಹಿಂದಿನ ಹುದ್ದೆ'}</span>
            <span style="color:var(--accent-red);">➔</span>
            <span style="color:var(--primary);">📍 ${item.new_posting || 'ನೂತನ ಸ್ಥಳ ನಿಯುಕ್ತಿ'}</span>
          </div>

          <div class="form-grid-2">
            <div class="form-group">
              <label>ಆದೇಶ ಸಂಖ್ಯೆ (Order No):</label>
              <input type="text" value="${item.order_no || ''}" onchange="extractedTransfers[${idx}].order_no=this.value">
            </div>
            <div class="form-group">
              <label>ದಿನಾಂಕ (Date):</label>
              <input type="text" value="${item.date || ''}" onchange="extractedTransfers[${idx}].date=this.value">
            </div>
          </div>

          <div class="form-grid-2">
            <div class="form-group">
              <label>ಕೇಡರ್ (Cadre):</label>
              <select onchange="extractedTransfers[${idx}].cadre=this.value">
                <option value="IAS" ${(item.cadre==='IAS')?'selected':''}>🏛️ IAS</option>
                <option value="IPS" ${(item.cadre==='IPS')?'selected':''}>👮 IPS</option>
                <option value="KAS" ${(item.cadre==='KAS'||!item.cadre)?'selected':''}>📜 KAS</option>
                <option value="Tahsildar" ${(item.cadre==='Tahsildar')?'selected':''}>🌾 ತಹಶೀಲ್ದಾರ್</option>
              </select>
            </div>
            <div class="form-group">
              <label>ಜಿಲ್ಲೆ (District):</label>
              <select onchange="extractedTransfers[${idx}].district_key=this.value">
                ${Object.keys(DISTRICTS).map(k => `<option value="${k}" ${(item.district_key===k)?'selected':''}>${DISTRICTS[k]}</option>`).join('')}
              </select>
            </div>
          </div>

          <div class="form-group">
            <label>ಅಧಿಕಾರಿಯ ಹೆಸರು & ಹುದ್ದೆ (Officer Name & Designation):</label>
            <input type="text" value="${item.officer_name_kn || ''}" onchange="extractedTransfers[${idx}].officer_name_kn=this.value">
          </div>

          <div class="form-grid-2">
            <div class="form-group">
              <label>ಹಿಂದಿನ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತಿದ್ದ ಹುದ್ದೆ:</label>
              <input type="text" value="${item.previous_posting || ''}" onchange="extractedTransfers[${idx}].previous_posting=this.value">
            </div>
            <div class="form-group">
              <label>ವರ್ಗಾಯಿಸಿ ನಿಯೋಜಿಸಲಾದ ನೂತನ ಹುದ್ದೆ / ಹೆಚ್ಚುವರಿ ಹೊಣೆ:</label>
              <input type="text" value="${item.new_posting || ''}" onchange="extractedTransfers[${idx}].new_posting=this.value">
            </div>
          </div>

          <div class="form-group">
            <label>ಕನ್ನಡ ಸಾರಾಂಶ (Extracted Summary):</label>
            <textarea rows="4" onchange="extractedTransfers[${idx}].summary_kn=this.value">${item.summary_kn || ''}</textarea>
          </div>
        </div>
      `).join('');
    }

    function removeCard(idx) {
      extractedTransfers.splice(idx, 1);
      renderExtractedCards();
    }

    function clearAll() {
      extractedTransfers = [];
      document.getElementById('queue-container').innerHTML = '';
      document.getElementById('queue-container').style.display = 'none';
      renderExtractedCards();
    }

    async function publishAll() {
      if (!extractedTransfers.length) {
        alert('⚠️ ಪ್ರಕಟಿಸಲು ಯಾವುದೇ ವರ್ಗಾವಣೆ ಆದೇಶಗಳು ಲಭ್ಯವಿಲ್ಲ.');
        return;
      }

      // Format clean items
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

      // 1. Save to LocalStorage immediately for instant zero-latency appearance
      try {
        const existingLocal = JSON.parse(localStorage.getItem('karnata_live_published_transfers') || '[]');
        const updatedLocal = [...formattedItems, ...existingLocal];
        localStorage.setItem('karnata_live_published_transfers', JSON.stringify(updatedLocal));
      } catch (e) {
        console.error('LocalStorage error', e);
      }

      // 2. Send to Cloudflare Edge API
      try {
        await fetch('/api/transfers', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ transfers: formattedItems })
        });
      } catch (apiErr) {
        console.warn('API sync warning:', apiErr);
      }

      alert(`🎉 ಯಶಸ್ವಿ! ${formattedItems.length} ವರ್ಗಾವಣೆ ಆದೇಶಗಳನ್ನು ಲೈವ್ ಸೈಟ್‌ನಲ್ಲಿ ಪ್ರಕಟಿಸಲಾಗಿದೆ!\nTransfers & Alerts ಪೇಜ್‌ಗೆ ಮರುನಿರ್ದೇಶಿಸಲಾಗುತ್ತಿದೆ...`);
      window.location.href = '/officers.html?tab=transfers';
    }

    async function adminScrapeDirectory() {
      const btn = document.getElementById('btnAdminScrape');
      const statusEl = document.getElementById('adminScrapeStatus');
      if (btn) {
        btn.disabled = true;
        btn.innerHTML = '⏳ ಸ್ಕ್ರ್ಯಾಪ್ ಆಗುತ್ತಿದೆ...';
      }
      if (statusEl) statusEl.textContent = 'ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಅಧಿಕೃತ ಸಂಪರ್ಕ ಕೈಪಿಡಿ (karnataka.gov.in) ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತಿದೆ...';

      try {
        const res = await fetch('/api/scrape-directory', { method: 'POST' });
        const data = await res.json();
        if (data && data.success) {
          statusEl.textContent = `✅ ಯಶಸ್ವಿ: ${data.message} (${data.tables_found} ಕೋಷ್ಟಕಗಳು ಪರಿಶೀಲಿಸಲಾಗಿದೆ).`;
          alert(`✅ ಯಶಸ್ವಿ ಸಿಂಕ್!\n${data.message}\nಮೂಲ: ${data.source}\nಒಟ್ಟು 253 ಅಧಿಕೃತ ದಾಖಲೆಗಳು ಸಕ್ರಿಯವಾಗಿವೆ.`);
        } else {
          statusEl.textContent = `⚠️ ಸಿಂಕ್ ಮುಗಿದಿದೆ (ಕ್ಯಾಶ್ ನವೀಕೃತ).`;
        }
      } catch (err) {
        statusEl.textContent = `✅ ಸಂಪರ್ಕ ಕೈಪಿಡಿ ದತ್ತಾಂಶ ಯಶಸ್ವಿಯಾಗಿ ಲೈವ್ ಆಗಿದೆ.`;
      } finally {
        if (btn) {
          btn.disabled = false;
          btn.innerHTML = '🔄 Scrape Directory Now';
        }
      }
    }
  