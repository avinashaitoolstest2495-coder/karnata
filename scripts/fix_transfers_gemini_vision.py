# -*- coding: utf-8 -*-
"""
Karnata — scripts/fix_transfers_gemini_vision.py
Fixes Google Gemini Vision AI OCR in admin-transfers.html and admin/transfers.html
by correcting inlineData / mimeType payload schema and supported model endpoints.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ══════════════════════════════════════════════════════════════════════════════
# 1. READ admin-transfers.html
# ══════════════════════════════════════════════════════════════════════════════
src_file = os.path.join(ROOT_DIR, 'admin-transfers.html')
with open(src_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Update Model Selector in HTML
model_select_html = """        <select id="gemini-model-select" onchange="localStorage.setItem('karnata_gemini_model', this.value)">
          <option value="gemini-2.0-flash" selected>⚡ Gemini 2.0 Flash (ಅತ್ಯಂತ ವೇಗ & ನಿಖರ)</option>
          <option value="gemini-1.5-flash">🚀 Gemini 1.5 Flash (ಸ್ಥಿರ ಮಾದರಿ)</option>
          <option value="gemini-1.5-pro">🧠 Gemini 1.5 Pro (ಡೀಪ್ ಅನಾಲಿಸಿಸ್)</option>
          <option value="gemini-2.0-flash-lite">💡 Gemini 2.0 Flash Lite</option>
        </select>"""

content = re.sub(
    r'<select id="gemini-model-select"[\s\S]*?</select>',
    model_select_html,
    content
)

# Replace callGeminiVisionWithFallback and handleBulkFiles with 100% robust Google AI Studio implementation
robust_js = """    async function callGeminiVisionWithFallback(apiKey, selectedModel, mimeType, base64Data, prompt) {
      const candidateModels = [
        selectedModel || 'gemini-2.0-flash',
        'gemini-2.0-flash',
        'gemini-1.5-flash',
        'gemini-1.5-flash-latest',
        'gemini-1.5-pro',
        'gemini-2.0-flash-lite'
      ];
      const uniqueModels = [...new Set(candidateModels)];

      let lastError = null;

      for (let model of uniqueModels) {
        try {
          const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${apiKey}`;
          
          const payload = {
            contents: [{
              parts: [
                { text: prompt },
                {
                  inlineData: {
                    mimeType: mimeType || 'image/jpeg',
                    data: base64Data
                  }
                }
              ]
            }],
            generationConfig: {
              temperature: 0.1,
              maxOutputTokens: 4096
            }
          };

          const res = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
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
            console.warn(`Model ${model} returned: ${lastError}. Trying fallback model...`);
          }
        } catch (e) {
          lastError = e.message;
          console.warn(`Error on ${model}: ${lastError}`);
        }
      }

      throw new Error(lastError || 'Gemini Vision AI ಕರೆ ವಿಫಲವಾಗಿದೆ. API Key ಪರೀಕ್ಷಿಸಿ.');
    }

    async function handleBulkFiles(e) {
      const files = Array.from(e.target.files);
      if (!files.length) return;

      const apiKey = (document.getElementById('gemini-key-input').value || localStorage.getItem('karnata_gemini_key') || '').trim();
      if (!apiKey) {
        alert('⚠️ ದಯವಿಟ್ಟು ಮೊದಲು ಮೇಲಿರುವ "Gemini API Key" ಬಾಕ್ಸ್‌ನಲ್ಲಿ ನಿಮ್ಮ Google AI Studio ಕೀ ನಮೂದಿಸಿ "💾 ಕೀ ಸೇವ್ ಮಾಡಿ" ಕ್ಲಿಕ್ ಮಾಡಿ.');
        document.getElementById('gemini-key-input').focus();
        return;
      }

      const selectedModel = document.getElementById('gemini-model-select').value || 'gemini-2.0-flash';
      const queueContainer = document.getElementById('queue-container');
      const ocrStatus = document.getElementById('ocr-status');
      const statusText = document.getElementById('ocr-status-text');
      const progressText = document.getElementById('ocr-progress-text');

      queueContainer.innerHTML = '';
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
          const mimeType = file.type || (file.name.endsWith('.png') ? 'image/png' : 'image/jpeg');
          const rawBase64 = base64DataUrl.includes(',') ? base64DataUrl.split(',')[1] : base64DataUrl;

          const prompt = `You are an expert Karnataka Government DPAR Official Gazette & Transfer Order Specialist.
Extract every government officer transfer from this official notification photo/document.
Return strictly a JSON array of objects with this schema:
[
  {
    "order_no": "ಆದೇಶ ಸಂಖ್ಯೆ (e.g. ಸಿಆಸುಇ 112 ಆಸೇವ 2026 or e-DPAR 279 SAS 2026)",
    "date": "ದಿನಾಂಕ (DD-MM-YYYY)",
    "cadre": "IAS | IPS | KAS | Tahsildar",
    "officer_name_kn": "ಅಧಿಕಾರಿಯ ಹೆಸರು ಮತ್ತು ಶ್ರೇಣಿ ಶುದ್ಧ ಕನ್ನಡದಲ್ಲಿ",
    "officer_name_en": "Officer Name in English",
    "previous_posting": "ಹಿಂದಿನ ಹುದ್ದೆ",
    "new_posting": "ವರ್ಗಾಯಿಸಲಾದ ನೂತನ ಹುದ್ದೆ",
    "district_key": "bengaluru_urban | mysuru | belagavi | tumakuru | kalaburagi | dharwad | shivamogga | mangaluru",
    "summary_kn": "ಸ್ಪಷ್ಟ ಹಾಗೂ ಅಧಿಕೃತ ಕನ್ನಡ ಪತ್ರಿಕಾ ಸಾರಾಂಶ"
  }
]
Output strictly raw JSON without markdown formatting.`;

          const parsed = await callGeminiVisionWithFallback(apiKey, selectedModel, mimeType, rawBase64, prompt);

          const statusElem = document.getElementById(`st-${i}`);
          if (statusElem) {
            statusElem.innerHTML = '✅ ಯಶಸ್ವಿ';
            statusElem.style.color = 'var(--accent-green)';
          }

          if (Array.isArray(parsed)) {
            parsed.forEach(p => extractedTransfers.push(p));
          } else if (typeof parsed === 'object') {
            extractedTransfers.push(parsed);
          }
        } catch (err) {
          console.error(err);
          const statusElem = document.getElementById(`st-${i}`);
          if (statusElem) {
            statusElem.innerHTML = '❌ ದೋಷ';
            statusElem.style.color = 'var(--accent-red)';
          }
          alert(`ಚಿತ್ರ ವಿಶ್ಲೇಷಣೆಯಲ್ಲಿ ದೋಷ: ${err.message}\\nದಯವಿಟ್ಟು Google AI Studio API Key ಸರಿಯಾಗಿದೆಯೇ ಪರೀಕ್ಷಿಸಿ.`);
        }
      }

      ocrStatus.style.display = 'none';
      renderExtractedCards();
    }"""

content = re.sub(
    r'async function callGeminiVisionWithFallback[\s\S]*?renderExtractedCards\(\);\s*\}',
    robust_js,
    content
)

# ══════════════════════════════════════════════════════════════════════════════
# 2. SAVE TO ALL TRANSFER DESTINATIONS
# ══════════════════════════════════════════════════════════════════════════════
destinations = [
    os.path.join(ROOT_DIR, 'admin-transfers.html'),
    os.path.join(ROOT_DIR, 'admin', 'transfers.html'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'admin-transfers.html'),
    os.path.join(ROOT_DIR, 'namma-karnataka', 'admin', 'transfers.html')
]

for d in destinations:
    os.makedirs(os.path.dirname(d), exist_ok=True)
    with open(d, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed Gemini Vision OCR in {d}")

print("SUCCESS_GEMINI_VISION_OCR_FIXED")
