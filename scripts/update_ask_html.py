with open("ask.html", "r", encoding="utf-8") as f:
    html = f.read().replace("\r\n", "\n")

# 1. Upgrade JSON-LD and Meta tags in ask.html
old_ld = """  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "askKARNATA AI — ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ಎಐ ಸಹಾಯಕ | Karnata.in",
    "applicationCategory": "UtilityApplication",
    "operatingSystem": "All",
    "url": "https://karnata.in/ask.html",
    "description": "askKARNATA AI — ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ ಸಹಾಯಕ. SIR ಮತದಾರರ ಪಟ್ಟಿ, ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು, ಬಂಗಾರ ದರ, ಹವಾಮಾನ, APMC ಧಾರಣೆ.",
    "browserRequirements": "Requires JavaScript. Requires HTML5."
  }
  </script>"""

new_ld = """  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "WebApplication",
        "name": "askKARNATA AI Studio — ಕರ್ನಾಟಕ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಅರ್ಹತೆ & ಸಮಗ್ರ ಎಐ ಸಹಾಯಕ | Karnata.in",
        "applicationCategory": "PublicServiceApplication",
        "operatingSystem": "All",
        "inLanguage": ["kn", "en"],
        "url": "https://karnata.in/ask",
        "description": "askKARNATA AI Studio — ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ಕನ್ನಡ ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ ಸಹಾಯಕ. 885+ ರಾಜ್ಯ ಮತ್ತು ಕೇಂದ್ರ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ವೈಯಕ್ತಿಕ ಅರ್ಹತಾ ಪರೀಕ್ಷಕ (What schemes apply for me), ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026 (SIR Final Roll), 5 ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು, ಬಂಗಾರ ದರ, ಹವಾಮಾನ, ಮತ್ತು APMC ಧಾರಣೆ.",
        "featureList": [
          "Interactive 9-Question Citizen Scheme Eligibility Finder in Kannada (885+ Schemes)",
          "8-Question Per-Scheme Eligibility Verification with Direct Official Portal Links",
          "Karnataka SIR Final Voter List 2026 & Electoral Roll Guidance",
          "Live 13 Major Dams Water Levels, 31 District Weather & 174 APMC Market Prices"
        ],
        "browserRequirements": "Requires JavaScript. Requires HTML5."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "askKARNATA AI ನಲ್ಲಿ ನನಗೆ ಯಾವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಸಿಗುತ್ತವೆ ಎಂದು ಹೇಗೆ ಕೇಳುವುದು? (How to check what government schemes apply to me in Ask Studio?)",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "askKARNATA AI Studio (karnata.in/ask) ದಲ್ಲಿ 'ನನಗೆ ಯಾವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಸಿಗುತ್ತವೆ?' ಅಥವಾ 'What schemes apply for me?' ಎಂದು ಕೇಳಿದರೆ, ತಕ್ಷಣವೇ 9 ಪ್ರಶ್ನೆಗಳ ಕನ್ನಡ ಅರ್ಹತಾ ಫಾರ್ಮ್ ತೆರೆಯುತ್ತದೆ. ನಿಮ್ಮ ವಯಸ್ಸು, ಲಿಂಗ, ವೃತ್ತಿ (ರೈತ/ವಿದ್ಯಾರ್ಥಿ/ಮಹಿಳೆ/ಕಾರ್ಮಿಕ/ಉದ್ಯಮಿ), ಜಾತಿ ವರ್ಗ ಮತ್ತು ಬಿಪಿಎಲ್ ಕಾರ್ಡ್ ವಿವರ ಆಯ್ಕೆ ಮಾಡಿದ ತಕ್ಷಣ 885+ ಯೋಜನೆಗಳಲ್ಲಿ ನಿಮಗೆ ಸಿಗುವ ಯೋಜನೆಗಳ ಪಟ್ಟಿ ಮತ್ತು ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್ ಲಿಂಕ್ ಸಿಗುತ್ತದೆ."
            }
          }
        ]
      }
    ]
  }
  </script>"""

if old_ld in html:
    html = html.replace(old_ld, new_ld, 1)

# 2. Add CSS for Interactive Eligibility Wizard & 8-Question Scheme Checker inside Ask Studio chat bubbles
interactive_css = """
    /* INTERACTIVE SCHEME ELIGIBILITY WIZARD & 8-QUESTION CHECKER IN ASK STUDIO */
    .ask-wiz-card {
      margin-top: 16px;
      background: linear-gradient(145deg, #131824 0%, #171f2e 100%);
      border: 1.5px solid rgba(52, 211, 153, 0.35);
      border-radius: 16px;
      padding: 18px;
      box-shadow: 0 10px 28px rgba(0, 0, 0, 0.35);
    }
    .ask-wiz-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      flex-wrap: wrap;
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }
    .ask-wiz-title {
      font-size: 16px;
      font-weight: 800;
      color: #34D399;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .ask-wiz-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 10px;
    }
    .ask-wiz-field {
      background: rgba(11, 12, 16, 0.65);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 10px;
      padding: 9px 11px;
    }
    .ask-wiz-field label {
      display: block;
      font-size: 12px;
      font-weight: 700;
      color: #94A3B8;
      margin-bottom: 5px;
    }
    .ask-wiz-field select {
      width: 100%;
      background: #1E212D;
      color: #F8FAFC;
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 8px;
      padding: 7px 9px;
      font-family: var(--font-kn), var(--font-en), sans-serif;
      font-size: 13.5px;
      font-weight: 600;
      outline: none;
    }
    .ask-wiz-btn {
      margin-top: 14px;
      width: 100%;
      background: linear-gradient(135deg, #059669, #16A34A);
      color: #FFFFFF;
      border: none;
      border-radius: 11px;
      padding: 11px 16px;
      font-family: var(--font-kn), var(--font-en), sans-serif;
      font-size: 14.5px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 6px 18px rgba(22, 163, 74, 0.35);
      transition: transform 0.15s ease;
    }
    .ask-wiz-btn:hover {
      transform: translateY(-1px);
    }
    .ask-wiz-results {
      margin-top: 14px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .ask-scheme-mini {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-left: 4px solid #34D399;
      border-radius: 12px;
      padding: 12px 14px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .ask-scheme-mini-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      flex-wrap: wrap;
    }
    .ask-scheme-mini-title {
      font-size: 15px;
      font-weight: 800;
      color: #F8FAFC;
    }
    .ask-scheme-mini-pts {
      margin: 4px 0 4px 16px;
      font-size: 13.5px;
      color: #CBD5E1;
      line-height: 1.55;
    }
    .ask-scheme-mini-actions {
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      margin-top: 4px;
    }
    .btn-mini-q {
      background: rgba(52, 211, 153, 0.15);
      border: 1px solid #34D399;
      color: #6EE7B7;
      padding: 5px 11px;
      border-radius: 8px;
      font-family: var(--font-kn), var(--font-en), sans-serif;
      font-size: 12.5px;
      font-weight: 800;
      cursor: pointer;
    }
    .btn-mini-q:hover {
      background: #10B981;
      color: #FFFFFF;
    }
    .btn-mini-web {
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid #38BDF8;
      color: #BAE6FD;
      padding: 5px 11px;
      border-radius: 8px;
      font-size: 12.5px;
      font-weight: 800;
      text-decoration: none;
    }
    .ask-q8-box {
      margin-top: 14px;
      background: #121620;
      border: 1.5px solid rgba(56, 189, 248, 0.35);
      border-radius: 14px;
      padding: 15px;
    }
    .ask-q8-item {
      padding: 10px 12px;
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.07);
      margin-bottom: 8px;
    }
    .ask-q8-cat {
      font-size: 11.5px;
      font-weight: 800;
      color: #38BDF8;
      margin-bottom: 3px;
    }
    .ask-q8-prompt {
      font-size: 13.5px;
      font-weight: 700;
      color: #F8FAFC;
      margin-bottom: 8px;
      line-height: 1.45;
    }
    .ask-q8-btns {
      display: flex;
      gap: 8px;
    }
    .ask-q8-btn {
      flex: 1;
      padding: 6px 10px;
      border-radius: 8px;
      border: 1px solid rgba(255, 255, 255, 0.16);
      background: #1E212D;
      color: #CBD5E1;
      font-family: var(--font-kn), var(--font-en), sans-serif;
      font-size: 13px;
      font-weight: 800;
      cursor: pointer;
    }
    .ask-q8-btn.yes.active {
      background: #059669;
      border-color: #34D399;
      color: #FFFFFF;
    }
    .ask-q8-btn.no.active {
      background: #E11D48;
      border-color: #FDA4AF;
      color: #FFFFFF;
    }
    .ask-q8-verdict {
      margin-top: 10px;
      padding: 12px 14px;
      border-radius: 10px;
      font-size: 14px;
      font-weight: 800;
      display: none;
    }
"""

if ".ask-wiz-card" not in html:
    html = html.replace("    @keyframes fadeIn {", interactive_css + "\n    @keyframes fadeIn {", 1)

# 3. Add Top Bar Scheme Checker link and Hero Chips/Prompts for Scheme Eligibility
old_top_actions = """    <div class="top-actions">
      <button class="btn-clean" onclick="resetChat()">+ ಹೊಸ ಚಾಟ್</button>
      <a href="/" class="btn-clean">🏠 ಮುಖಪುಟ</a>
    </div>"""

new_top_actions = """    <div class="top-actions">
      <a href="/scheme-checker" class="btn-clean" style="border-color:rgba(52,211,153,0.4);color:#6EE7B7;">🎯 ಯೋಜನೆ ಅರ್ಹತೆ (885+)</a>
      <button class="btn-clean" onclick="resetChat()">+ ಹೊಸ ಚಾಟ್</button>
      <a href="/" class="btn-clean">🏠 ಮುಖಪುಟ</a>
    </div>"""

if old_top_actions in html:
    html = html.replace(old_top_actions, new_top_actions, 1)

old_chips = """        <!-- CATEGORY CHIPS -->
        <div class="chips-row">
          <button class="chip" onclick="askPreset('SIR ಎಂದರೇನು? ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯಲ್ಲಿ ಹೆಸರು ಹೇಗೆ ಪರಿಶೀಲಿಸುವುದು?')">🗳️ SIR ಮತದಾರರ ಪಟ್ಟಿ</button>
          <button class="chip" onclick="askPreset('ಗೃಹಲಕ್ಷ್ಮಿ ಮತ್ತು ಗೃಹಜ್ಯೋತಿ ಯೋಜನೆಗಳ ನಿಯಮಗಳು ಮತ್ತು ಅರ್ಹತೆ ಏನು?')">🌸 ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು</button>"""

new_chips = """        <!-- CATEGORY CHIPS -->
        <div class="chips-row">
          <button class="chip" style="border-color:rgba(52,211,153,0.5);color:#6EE7B7;" onclick="askPreset('ನನಗೆ ಯಾವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಸಿಗುತ್ತವೆ? ನನ್ನ ಅರ್ಹತೆ ಪರೀಕ್ಷಿಸಿ')">🎯 ನನಗೆ ಯಾವ ಯೋಜನೆ ಸಿಗುತ್ತದೆ? (885+)</button>
          <button class="chip" onclick="askPreset('SIR ಎಂದರೇನು? ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿಯಲ್ಲಿ ಹೆಸರು ಹೇಗೆ ಪರಿಶೀಲಿಸುವುದು?')">🗳️ ಅಂತಿಮ ಮತದಾರರ ಪಟ್ಟಿ 2026</button>
          <button class="chip" onclick="askPreset('ಗೃಹಲಕ್ಷ್ಮಿ ಮತ್ತು ಗೃಹಜ್ಯೋತಿ ಯೋಜನೆಗಳ ನಿಯಮಗಳು ಮತ್ತು ಅರ್ಹತೆ ಏನು?')">🌸 ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು</button>"""

if old_chips in html:
    html = html.replace(old_chips, new_chips, 1)

old_prompts = """        <!-- SUGGESTED PROMPTS -->
        <div class="prompts-list">
          <div class="prompt-card" onclick="askPreset('SIR ಎಂದರೇನು? ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯಲ್ಲಿ ಹೆಸರು ಹೇಗೆ ಪರಿಶೀಲಿಸುವುದು?')">"""

new_prompts = """        <!-- SUGGESTED PROMPTS -->
        <div class="prompts-list">
          <div class="prompt-card" style="border-color:rgba(52,211,153,0.4);background:rgba(16,185,129,0.08);" onclick="askPreset('ನನಗೆ ಯಾವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಸಿಗುತ್ತವೆ? ನನ್ನ ಅರ್ಹತೆ ಪರೀಕ್ಷಿಸಿ (What schemes apply for me?)')">
            <span>🎯 ನನಗೆ ಯಾವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಸಿಗುತ್ತವೆ? (885+ ರಾಜ್ಯ ಮತ್ತು ಕೇಂದ್ರ ಯೋಜನೆಗಳ ಅರ್ಹತೆ ಪರೀಕ್ಷಿಸಿ)</span>
            <span class="prompt-arrow">→</span>
          </div>
          <div class="prompt-card" onclick="askPreset('ರೈತ ಸಿರಿ ಯೋಜನೆ ಮತ್ತು ಕೃಷಿ ಭಾಗ್ಯ ಯೋಜನೆಗೆ ಅರ್ಹತೆ ಏನು?')">
            <span>🌾 ರೈತ ಸಿರಿ ಯೋಜನೆ ಮತ್ತು ಕೃಷಿ ಭಾಗ್ಯ ಯೋಜನೆಗೆ ಅರ್ಹತೆ ಏನು?</span>
            <span class="prompt-arrow">→</span>
          </div>
          <div class="prompt-card" onclick="askPreset('SIR ಎಂದರೇನು? ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯಲ್ಲಿ ಹೆಸರು ಹೇಗೆ ಪರಿಶೀಲಿಸುವುದು?')">"""

if old_prompts in html:
    html = html.replace(old_prompts, new_prompts, 1)

# 4. Update script version & submitQuery logic in ask.html to prioritize rich client scheme engine + render interactive wizard & 8-question checker
html = html.replace(
    '<script src="/ask-ai-engine.js?v=20260826_2350"></script>',
    '<script src="/ask-ai-engine.js?v=20261029_1200"></script>',
    1,
)

old_submit_block = """      // 2. Fetch from Cloudflare Edge API /api/ask-ai (with instant client fallback)
      let answerText = '';
      let cards = [];
      let sources = [];
      let providerName = 'Karnata Intelligence';

      try {
        const res = await fetch('/api/ask-ai', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt: text })
        });
        if (res.ok) {
          const data = await res.json();
          if (data && data.answer) {
            answerText = data.answer;
            cards = data.cards || [];
            sources = data.sources || [];
            providerName = data.provider || 'Karnata Intelligence';
          }
        }
      } catch (e) {
        console.warn('[Ask API Network Error, trying client engine]:', e);
      }

      // 3. Client engine fallback if API failed or offline
      if (!answerText && window.AskKARNATAEngine) {
        const clientRes = window.AskKARNATAEngine.query(text);
        if (clientRes && clientRes.text) {
          answerText = clientRes.text;
          cards = clientRes.cards || [];
          providerName = 'Karnata Client Dataset';
        }
      }

      const aiContentEl = msgGroup.querySelector('.ai-body');
      const badgeEl = msgGroup.querySelector('.ai-source-badge');

      if (answerText) {
        if (badgeEl) badgeEl.textContent = providerName;
        let html = parseMarkdown(answerText);

        // Smart Action Buttons
        if (cards && cards.length > 0) {
          html += `
            <div class="links-box">
              ${cards.map(c => `<a href="${c.url}" class="action-btn-pill">${c.icon || '🔎'} ${c.title}</a>`).join('')}
            </div>
          `;
        }

        // Official Source Citations
        if (sources && sources.length > 0) {
          html += `
            <div class="sources-box">
              <span>🏛️ ಅಧಿಕೃತ ಮೂಲ:</span>
              ${sources.map(s => `<a href="${s.url}" target="_blank" rel="noopener noreferrer" class="source-link">🔗 ${s.name}</a>`).join(' · ')}
            </div>
          `;
        }

        aiContentEl.innerHTML = html;
        saveHistoryToStorage(text, answerText, cards, sources);"""

new_submit_block = """      // 2. Check Client Knowledge Engine First (885+ Schemes, Interactive Eligibility Wizard, Dams, APMC, Gold, Weather)
      let answerText = '';
      let cards = [];
      let sources = [];
      let providerName = 'Karnata Intelligence';
      let clientRes = null;

      if (window.AskKARNATAEngine) {
        clientRes = window.AskKARNATAEngine.query(text);
        if (clientRes && clientRes.text && !clientRes.isFallback && (clientRes.showEligibilityWizard || clientRes.schemeInteractiveSlug)) {
          answerText = clientRes.text;
          cards = clientRes.cards || [];
          sources = clientRes.sources || [];
          providerName = '885+ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಅರ್ಹತಾ ಎಂಜಿನ್';
        }
      }

      // 3. Fetch from Cloudflare Edge API /api/ask-ai if not already answered by Scheme Engine
      if (!answerText) {
        try {
          const res = await fetch('/api/ask-ai', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt: text })
          });
          if (res.ok) {
            const data = await res.json();
            if (data && data.answer) {
              answerText = data.answer;
              cards = data.cards || [];
              sources = data.sources || [];
              providerName = data.provider || 'Karnata Intelligence';
            }
          }
        } catch (e) {
          console.warn('[Ask API Network Error, trying client engine]:', e);
        }
      }

      // 4. Client engine fallback if API failed or offline
      if (!answerText && clientRes && clientRes.text) {
        answerText = clientRes.text;
        cards = clientRes.cards || [];
        sources = clientRes.sources || [];
        providerName = 'Karnata Client Dataset';
      }

      const aiContentEl = msgGroup.querySelector('.ai-body');
      const badgeEl = msgGroup.querySelector('.ai-source-badge');

      if (answerText) {
        if (badgeEl) badgeEl.textContent = providerName;
        let html = parseMarkdown(answerText);

        // Interactive 9-Question Citizen Eligibility Wizard inside Ask Studio
        const wizUid = 'wiz_' + Date.now();
        if (clientRes && clientRes.showEligibilityWizard) {
          const prof = clientRes.initialProfile || {};
          html += buildAskStudioWizardHTML(wizUid, prof);
        }

        // Interactive 8-Question Single Scheme Eligibility Checklist inside Ask Studio
        if (clientRes && clientRes.schemeInteractiveSlug) {
          html += buildAskStudioSchemeQ8HTML(clientRes.schemeInteractiveSlug, 'q8_' + Date.now());
        }

        // Smart Action Buttons
        if (cards && cards.length > 0) {
          html += `
            <div class="links-box">
              ${cards.map(c => `<a href="${c.url}" ${c.url.startsWith('http') ? 'target="_blank" rel="noopener noreferrer"' : ''} class="action-btn-pill">${c.icon || '🔎'} ${c.title}</a>`).join('')}
            </div>
          `;
        }

        // Official Source Citations
        if (sources && sources.length > 0) {
          html += `
            <div class="sources-box">
              <span>🏛️ ಅಧಿಕೃತ ಮೂಲ:</span>
              ${sources.map(s => `<a href="${s.url}" target="_blank" rel="noopener noreferrer" class="source-link">🔗 ${s.name}</a>`).join(' · ')}
            </div>
          `;
        }

        aiContentEl.innerHTML = html;
        if (clientRes && clientRes.showEligibilityWizard) {
          runAskStudioWizardSearch(wizUid);
        }
        saveHistoryToStorage(text, answerText, cards, sources);"""

assert old_submit_block in html, "old_submit_block not found"
html = html.replace(old_submit_block, new_submit_block, 1)

# 5. Add helper functions for the Ask Studio Interactive Wizard & 8-Question Scheme Checker
ask_wizard_helpers = r"""
    function buildAskStudioWizardHTML(uid, prof = {}) {
      return `
        <div class="ask-wiz-card" id="${uid}">
          <div class="ask-wiz-head">
            <div class="ask-wiz-title">🎯 ನನಗೆ ಯಾವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಸಿಗುತ್ತವೆ? — 9 ಪ್ರಶ್ನೆಗಳ ಅರ್ಹತಾ ಪರೀಕ್ಷಕ</div>
            <span style="font-size:12px;color:#94A3B8;">885+ ರಾಜ್ಯ & ಕೇಂದ್ರ ಯೋಜನೆಗಳು</span>
          </div>
          <div class="ask-wiz-grid">
            <div class="ask-wiz-field">
              <label>1. ನಿಮ್ಮ ವಯಸ್ಸು (Age Group)</label>
              <select id="${uid}_age">
                <option value="">ಎಲ್ಲಾ ವಯಸ್ಸು (All Ages)</option>
                <option value="0" ${prof.age === '0' ? 'selected' : ''}>0 – 10 ವರ್ಷ (ಮಕ್ಕಳು)</option>
                <option value="10" ${prof.age === '10' ? 'selected' : ''}>11 – 20 ವರ್ಷ (ವಿದ್ಯಾರ್ಥಿ/ಯುವ)</option>
                <option value="20" ${prof.age === '20' ? 'selected' : ''}>21 – 30 ವರ್ಷ (ಯುವಜನತೆ)</option>
                <option value="30" ${prof.age === '30' ? 'selected' : ''}>31 – 40 ವರ್ಷ</option>
                <option value="40" ${prof.age === '40' ? 'selected' : ''}>41 – 50 ವರ್ಷ</option>
                <option value="50" ${prof.age === '50' ? 'selected' : ''}>51 – 60 ವರ್ಷ</option>
                <option value="60" ${prof.age === '60' ? 'selected' : ''}>60+ ವರ್ಷ (ಹಿರಿಯ ನಾಗರಿಕರು)</option>
              </select>
            </div>
            <div class="ask-wiz-field">
              <label>2. ಲಿಂಗ (Gender)</label>
              <select id="${uid}_gender">
                <option value="">ಎಲ್ಲಾ (All)</option>
                <option value="Female" ${prof.gender === 'Female' ? 'selected' : ''}>👩 ಮಹಿಳೆ (Female)</option>
                <option value="Male" ${prof.gender === 'Male' ? 'selected' : ''}>👨 ಪುರುಷ (Male)</option>
                <option value="Transgender" ${prof.gender === 'Transgender' ? 'selected' : ''}>🏳️‍⚧️ ತೃತೀಯ ಲಿಂಗಿ</option>
              </select>
            </div>
            <div class="ask-wiz-field">
              <label>3. ನಿಮ್ಮ ವೃತ್ತಿ / ಪಾತ್ರ (Occupation)</label>
              <select id="${uid}_role">
                <option value="">ಎಲ್ಲಾ ವರ್ಗ (All Citizens)</option>
                <option value="farmer" ${prof.role === 'farmer' ? 'selected' : ''}>🌾 ರೈತ / ಕೃಷಿಕ (Farmer)</option>
                <option value="student" ${prof.role === 'student' ? 'selected' : ''}>🎓 ವಿದ್ಯಾರ್ಥಿ (Student)</option>
                <option value="woman" ${prof.role === 'woman' ? 'selected' : ''}>👩 ಗೃಹಿಣಿ / ಮಹಿಳಾ ಸಬಲೀಕರಣ</option>
                <option value="business" ${prof.role === 'business' ? 'selected' : ''}>💼 ಸ್ವಯಂ ಉದ್ಯೋಗ / ವ್ಯಾಪಾರ / ಸಾಲ</option>
                <option value="worker" ${prof.role === 'worker' ? 'selected' : ''}>👷 ಕಟ್ಟಡ / ಕುಶಲಕರ್ಮಿ / ಕಾರ್ಮಿಕ</option>
                <option value="unemployed" ${prof.role === 'unemployed' ? 'selected' : ''}>🔍 ಉದ್ಯೋಗಾಂಕ್ಷಿ / ನಿರುದ್ಯೋಗಿ</option>
                <option value="senior" ${prof.role === 'senior' ? 'selected' : ''}>👴 ಹಿರಿಯ ನಾಗರಿಕರು (Senior Citizen)</option>
              </select>
            </div>
            <div class="ask-wiz-field">
              <label>4. ಜಾತಿ ವರ್ಗ (Caste Category)</label>
              <select id="${uid}_caste">
                <option value="">ಎಲ್ಲಾ ವರ್ಗ (All)</option>
                <option value="Other Backward Class (OBC)" ${prof.caste === 'Other Backward Class (OBC)' ? 'selected' : ''}>ಹಿಂದುಳಿದ ವರ್ಗ (OBC)</option>
                <option value="Scheduled Caste (SC)" ${prof.caste === 'Scheduled Caste (SC)' ? 'selected' : ''}>ಪರಿಶಿಷ್ಟ ಜಾತಿ (SC)</option>
                <option value="Scheduled Tribe (ST)" ${prof.caste === 'Scheduled Tribe (ST)' ? 'selected' : ''}>ಪರಿಶಿಷ್ಟ ಪಂಗಡ (ST)</option>
                <option value="General" ${prof.caste === 'General' ? 'selected' : ''}>ಸಾಮಾನ್ಯ ವರ್ಗ (General)</option>
              </select>
            </div>
            <div class="ask-wiz-field">
              <label>5. ಪಡಿತರ ಚೀಟಿ (Ration Card)</label>
              <select id="${uid}_bpl">
                <option value="yes" ${prof.bpl !== 'no' ? 'selected' : ''}>BPL / ಅಂತ್ಯೋದಯ ಕಾರ್ಡ್ ಹೊಂದಿದ್ದೇನೆ</option>
                <option value="no" ${prof.bpl === 'no' ? 'selected' : ''}>APL / ಯಾವುದೇ ಕಾರ್ಡ್</option>
              </select>
            </div>
            <div class="ask-wiz-field">
              <label>6. ವಾಸಸ್ಥಳ ಪ್ರದೇಶ (Residence)</label>
              <select id="${uid}_res">
                <option value="">ಗ್ರಾಮೀಣ ಮತ್ತು ನಗರ (Both)</option>
                <option value="Rural" ${prof.residence === 'Rural' ? 'selected' : ''}>🌾 ಗ್ರಾಮೀಣ ಪ್ರದೇಶ (Rural)</option>
                <option value="Urban" ${prof.residence === 'Urban' ? 'selected' : ''}>🏙️ ನಗರ ಪ್ರದೇಶ (Urban)</option>
              </select>
            </div>
            <div class="ask-wiz-field">
              <label>7. ವಿಶೇಷ ವರ್ಗ (Special Category)</label>
              <select id="${uid}_special">
                <option value="">ಯಾವುದೂ ಇಲ್ಲ (None)</option>
                <option value="disability" ${prof.special === 'disability' ? 'selected' : ''}>♿ ವಿಕಲಚೇತನರು (PwD)</option>
                <option value="minority" ${prof.special === 'minority' ? 'selected' : ''}>🕌 ಅಲ್ಪಸಂಖ್ಯಾತರು (Minority)</option>
                <option value="widow" ${prof.special === 'widow' ? 'selected' : ''}>👩 ವಿಧವಾ ಮಹಿಳೆ (Widowed)</option>
                <option value="exservice" ${prof.special === 'exservice' ? 'selected' : ''}>🎖️ ಮಾಜಿ ಸೈನಿಕರು (Ex-Servicemen)</option>
              </select>
            </div>
            <div class="ask-wiz-field">
              <label>8. ಸರ್ಕಾರದ ಆಯ್ಕೆ (Govt Level)</label>
              <select id="${uid}_level">
                <option value="all">🏛️ + 🇮🇳 ರಾಜ್ಯ & ಕೇಂದ್ರ ಎರಡೂ</option>
                <option value="State">🏛️ ಕರ್ನಾಟಕ ರಾಜ್ಯ ಯೋಜನೆಗಳು ಮಾತ್ರ</option>
                <option value="Central">🇮🇳 ಕೇಂದ್ರ ಸರ್ಕಾರದ ಯೋಜನೆಗಳು ಮಾತ್ರ</option>
              </select>
            </div>
          </div>
          <button type="button" class="ask-wiz-btn" onclick="runAskStudioWizardSearch('${uid}')">
            🎯 ನನಗೆ ಸಿಗುವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳನ್ನು ತೋರಿಸಿ (Find My Eligible Schemes)
          </button>
          <div class="ask-wiz-results" id="${uid}_results"></div>
        </div>
      `;
    }

    function runAskStudioWizardSearch(uid) {
      if (!window.AskKARNATAEngine || !window.AskKARNATAEngine.findEligibleSchemes) return;
      const profile = {
        age: document.getElementById(uid + '_age')?.value || '',
        gender: document.getElementById(uid + '_gender')?.value || '',
        role: document.getElementById(uid + '_role')?.value || '',
        caste: document.getElementById(uid + '_caste')?.value || '',
        bpl: document.getElementById(uid + '_bpl')?.value || 'yes',
        residence: document.getElementById(uid + '_res')?.value || '',
        special: document.getElementById(uid + '_special')?.value || '',
        level: document.getElementById(uid + '_level')?.value || 'all'
      };
      const matched = window.AskKARNATAEngine.findEligibleSchemes(profile);
      const resBox = document.getElementById(uid + '_results');
      if (!resBox) return;

      const stateCnt = matched.filter(s => s.level === 'State').length;
      const centralCnt = matched.filter(s => s.level === 'Central').length;
      const top = matched.slice(0, 10);

      let html = `
        <div style="padding:10px 12px;border-radius:10px;background:rgba(52,211,153,0.12);border:1px solid rgba(52,211,153,0.35);color:#A7F3D0;font-size:13.5px;font-weight:800;">
          🎉 ನಿಮ್ಮ ವಿವರಕ್ಕೆ ಒಟ್ಟು <strong>${matched.length} ಯೋಜನೆಗಳು</strong> ಹೊಂದಿಕೆಯಾಗಿವೆ! (🏛️ ರಾಜ್ಯ: ${stateCnt} • 🇮🇳 ಕೇಂದ್ರ: ${centralCnt})
        </div>
      `;

      top.forEach((s, idx) => {
        const site = window.AskKARNATAEngine.getOfficialSchemeWebsite(s);
        const badge = s.level === 'State' ? '🏛️ ಕರ್ನಾಟಕ ರಾಜ್ಯ' : '🇮🇳 ಕೇಂದ್ರ ಸರ್ಕಾರ';
        const ben = (s.benefits_kn || s.description_kn || s.description_en || '').split(/(?<=[.।])\s+/).slice(0, 2).join(' ');
        const qBoxId = `${uid}_q8_${idx}`;
        html += `
          <div class="ask-scheme-mini">
            <div class="ask-scheme-mini-top">
              <div class="ask-scheme-mini-title">${idx + 1}. ${escapeHtml(s.name_kn || s.name_en)}</div>
              <span style="font-size:11.5px;font-weight:800;color:#6EE7B7;">${badge}</span>
            </div>
            <ul class="ask-scheme-mini-pts">
              <li>${escapeHtml(ben)}</li>
              <li>ಇಲಾಖೆ: ${escapeHtml(s.ministry_kn || s.ministry_en || '')}</li>
            </ul>
            <div class="ask-scheme-mini-actions">
              <button type="button" class="btn-mini-q" onclick="toggleInlineSchemeQ8('${s.slug}', '${qBoxId}')">✅ 8 ಪ್ರಶ್ನೆಗಳ ಅರ್ಹತೆ ಪರೀಕ್ಷಿಸಿ</button>
              <a href="${site}" target="_blank" rel="noopener noreferrer" class="btn-mini-web">🌐 ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್ ↗</a>
              <a href="/scheme-checker?id=${encodeURIComponent(s.slug)}" class="btn-mini-web" style="border-color:rgba(255,255,255,0.2);color:#CBD5E1;">📄 ಪೂರ್ಣ ವಿವರ</a>
            </div>
            <div id="${qBoxId}"></div>
          </div>
        `;
      });

      if (matched.length > 10) {
        html += `
          <a href="/scheme-checker?wizard=1" class="action-btn-pill" style="justify-content:center;text-align:center;">
            📋 ಉಳಿದ ಎಲ್ಲಾ ${matched.length} ಅರ್ಹ ಯೋಜನೆಗಳನ್ನು ಯೋಜನೆಗಳ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನೋಡಿ →
          </a>
        `;
      }

      resBox.innerHTML = html;
    }

    function toggleInlineSchemeQ8(slug, containerId) {
      const box = document.getElementById(containerId);
      if (!box) return;
      if (box.innerHTML.trim() !== '') {
        box.innerHTML = '';
        return;
      }
      box.innerHTML = buildAskStudioSchemeQ8HTML(slug, containerId + '_inner');
    }

    const ASK_Q8_STATE = {};

    function buildAskStudioSchemeQ8HTML(slug, qid) {
      if (!window.AskKARNATAEngine || !window.AskKARNATAEngine.getSchemeBySlug) return '';
      const s = window.AskKARNATAEngine.getSchemeBySlug(slug);
      if (!s) return '';
      const questions = window.AskKARNATAEngine.buildSchemeQuestions(s);
      const site = window.AskKARNATAEngine.getOfficialSchemeWebsite(s);
      ASK_Q8_STATE[qid] = { total: questions.length, answers: {}, site: site, name: s.name_kn || s.name_en };

      const qItems = questions.map((q, i) => `
        <div class="ask-q8-item">
          <div class="ask-q8-cat">${escapeHtml(q.category)}</div>
          <div class="ask-q8-prompt">${escapeHtml(q.prompt)}</div>
          <div class="ask-q8-btns">
            <button type="button" class="ask-q8-btn yes" id="${qid}_y_${i}" onclick="answerAskStudioQ8('${qid}', ${i}, 'Yes', '${q.expected}')">👍 ಹೌದು (Yes)</button>
            <button type="button" class="ask-q8-btn no" id="${qid}_n_${i}" onclick="answerAskStudioQ8('${qid}', ${i}, 'No', '${q.expected}')">👎 ಇಲ್ಲ (No)</button>
          </div>
        </div>
      `).join('');

      return `
        <div class="ask-q8-box" id="${qid}">
          <div style="font-size:14.5px;font-weight:800;color:#38BDF8;margin-bottom:10px;">
            ✅ ${escapeHtml(s.name_kn || s.name_en)} — 8 ಪ್ರಶ್ನೆಗಳ ವೈಯಕ್ತಿಕ ಅರ್ಹತಾ ಪರೀಕ್ಷೆ
          </div>
          ${qItems}
          <div class="ask-q8-verdict" id="${qid}_verdict"></div>
        </div>
      `;
    }

    function answerAskStudioQ8(qid, idx, val, expected) {
      const st = ASK_Q8_STATE[qid];
      if (!st) return;
      st.answers[idx] = (val === expected);
      const yBtn = document.getElementById(`${qid}_y_${idx}`);
      const nBtn = document.getElementById(`${qid}_n_${idx}`);
      if (yBtn) yBtn.classList.toggle('active', val === 'Yes');
      if (nBtn) nBtn.classList.toggle('active', val === 'No');

      const answeredCount = Object.keys(st.answers).length;
      const failedCount = Object.values(st.answers).filter(v => v === false).length;
      const verdictEl = document.getElementById(`${qid}_verdict`);
      if (!verdictEl) return;

      verdictEl.style.display = 'block';
      if (failedCount > 0) {
        verdictEl.style.background = 'rgba(225, 29, 72, 0.15)';
        verdictEl.style.border = '1px solid #F43F5E';
        verdictEl.style.color = '#FECDD3';
        verdictEl.innerHTML = `⚠️ ನೀವು ಆಯ್ಕೆ ಮಾಡಿದ ಉತ್ತರಗಳ ಪ್ರಕಾರ ಈ ಯೋಜನೆಯ ಕೆಲವು ಮಾನದಂಡಗಳು ಹೊಂದಿಕೆಯಾಗುತ್ತಿಲ್ಲ (${answeredCount}/${st.total} ಪರಿಶೀಲಿಸಲಾಗಿದೆ).`;
      } else if (answeredCount === st.total) {
        verdictEl.style.background = 'rgba(16, 185, 129, 0.18)';
        verdictEl.style.border = '1px solid #34D399';
        verdictEl.style.color = '#A7F3D0';
        verdictEl.innerHTML = `🎉 ಅಭಿನಂದನೆಗಳು! ಎಲ್ಲಾ ${st.total} ಅರ್ಹತಾ ಮಾನದಂಡಗಳನ್ನು ನೀವು ಪೂರೈಸಿದ್ದೀರಿ! <br><a href="${st.site}" target="_blank" rel="noopener noreferrer" style="display:inline-block;margin-top:8px;padding:7px 14px;background:#10B981;color:#fff;border-radius:8px;text-decoration:none;font-weight:800;">🌐 ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ (${st.site}) ↗</a>`;
      } else {
        verdictEl.style.background = 'rgba(56, 189, 248, 0.12)';
        verdictEl.style.border = '1px solid #38BDF8';
        verdictEl.style.color = '#BAE6FD';
        verdictEl.innerHTML = `⏳ ${answeredCount} / ${st.total} ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸಲಾಗಿದೆ — ಫಲಿತಾಂಶಕ್ಕಾಗಿ ಉಳಿದ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸಿ.`;
      }
    }
"""

if "function buildAskStudioWizardHTML" not in html:
    html = html.replace("    function escapeHtml(str) {", ask_wizard_helpers + "\n    function escapeHtml(str) {", 1)

with open("ask.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully upgraded ask.html with interactive 9-question Citizen Eligibility Wizard & 8-question scheme verifier!")
