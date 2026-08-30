# -*- coding: utf-8 -*-
"""
Karnata — scripts/fix_gemini_2026_models.py
Updates Google Gemini Vision AI in admin-transfers.html and admin/transfers.html
to use official 2026 models (gemini-3.5-flash-lite, gemini-3.5-flash, gemini-2.5-flash)
with automated dynamic model discovery.
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
          <option value="gemini-3.5-flash-lite" selected>⚡ Gemini 3.5 Flash Lite (ಅತ್ಯಂತ ವೇಗ & ಶಿಫಾರಸು)</option>
          <option value="gemini-3.5-flash">🚀 Gemini 3.5 Flash</option>
          <option value="gemini-2.5-flash">⚡ Gemini 2.5 Flash</option>
          <option value="gemini-2.5-pro">🧠 Gemini 2.5 Pro</option>
          <option value="gemini-1.5-flash">💡 Gemini 1.5 Flash</option>
        </select>"""

content = re.sub(
    r'<select id="gemini-model-select"[\s\S]*?</select>',
    model_select_html,
    content
)

# 2026 Robust Model Caller with Dynamic Discovery
robust_2026_js = """    async function callGeminiVisionWithFallback(apiKey, selectedModel, mimeType, base64Data, prompt) {
      // Prioritize 2026 Google Generative AI Models
      const candidateModels = [
        selectedModel || 'gemini-3.5-flash-lite',
        'gemini-3.5-flash-lite',
        'gemini-3.5-flash',
        'gemini-2.5-flash',
        'gemini-2.5-pro',
        'gemini-1.5-flash',
        'gemini-1.5-pro'
      ];
      const uniqueModels = [...new Set(candidateModels)];

      let lastError = null;

      // 1. Try static list of current 2026 models
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
            console.warn(`Model ${model} returned: ${lastError}. Trying next...`);
          }
        } catch (e) {
          lastError = e.message;
          console.warn(`Error on ${model}: ${lastError}`);
        }
      }

      // 2. Dynamic Discovery Fallback: Fetch available models directly from Google AI Studio for this key
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
                      { inlineData: { mimeType: mimeType || 'image/jpeg', data: base64Data } }
                    ]
                  }],
                  generationConfig: { temperature: 0.1, maxOutputTokens: 4096 }
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

      throw new Error(lastError || 'Gemini Vision AI ಕರೆ ವಿಫಲವಾಗಿದೆ. API Key ಪರೀಕ್ಷಿಸಿ.');
    }"""

content = re.sub(
    r'async function callGeminiVisionWithFallback[\s\S]*?throw new Error\(lastError \|\| [^;]+\);\s*\}',
    robust_2026_js,
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
    print(f"Updated 2026 Gemini Vision AI in {d}")

print("SUCCESS_GEMINI_2026_MODELS_DEPLOYED")
