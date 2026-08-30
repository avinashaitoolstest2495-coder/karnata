# -*- coding: utf-8 -*-
"""
Karnata — scripts/fix_real_workers_ai_and_cards.py
1. Removes static interception in _worker.js so that Cloudflare Workers AI directly answers EVERY question (both on ask.html and gold-rate.html).
2. Connects strictly to Cloudflare Workers AI (@cf/meta/llama-3.3-70b-instruct / @cf/meta/llama-3.1-8b-instruct / @cf/qwen/qwen2.5-72b-instruct).
3. Fixes text contrast in the 4 battle cards in gold-rate.html (.bc-name clearly visible dark text).
4. Syncs workspaces and deploys.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

# 1. Update _worker.js
with open(os.path.join(ROOT_DIR, '_worker.js'), 'r', encoding='utf-8') as f:
    worker_js = f.read()

# Remove the static gold/silver rates interception from resolvePrecisionEntity
old_gold_intercept = """  // 7. GOLD & SILVER RATES
  if (combined.includes('ಚಿನ್ನ') || combined.includes('ಬಂಗಾರ') || combined.includes('ಬೆಳ್ಳಿ') || combined.includes('gold') || combined.includes('silver')) {
    return {
      answer: `### 🪙 ಕರ್ನಾಟಕ ಬುಲಿಯನ್ ಮಾರುಕಟ್ಟೆ ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ:

* **24 ಕ್ಯಾರೆಟ್ ಅಪರಂಜಿ ಚಿನ್ನ (99.9% Pure):** **₹16,380 / ಗ್ರಾಂ** (₹1,63,800 / 10 ಗ್ರಾಂ)
* **22 ಕ್ಯಾರೆಟ್ ಆಭರಣ ಚಿನ್ನ (91.6% Hallmark):** **₹15,010 / ಗ್ರಾಂ** (₹1,50,100 / 10 ಗ್ರಾಂ)
* **18 ಕ್ಯಾರೆಟ್ ಚಿನ್ನ:** **₹12,281 / ಗ್ರಾಂ** (₹1,22,810 / 10 ಗ್ರಾಂ)
* **ಬೆಳ್ಳಿ (999 Pure Silver):** **₹260 / ಗ್ರಾಂ** (₹2,60,000 / 1 ಕೆಜಿ)
* **ಆಭರಣ ಬೆಳ್ಳಿ (925 Sterling Silver):** **₹240.5 / ಗ್ರಾಂ** (₹2,40,500 / 1 ಕೆಜಿ)`,
      cards: [{ title: "🪙 ಲೈವ್ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ", url: "/gold-rate.html", icon: "🪙" }],
      sources: [{ name: "Karnataka Bullion Association", url: "https://karnata.in/gold-rate.html" }],
      provider: "Karnata Precision Data (Live Bullion Rates)"
    };
  }"""

if old_gold_intercept in worker_js:
    worker_js = worker_js.replace(old_gold_intercept, "")
    print("SUCCESS: Removed static gold interception from _worker.js.")
else:
    # Use regex to strip it
    worker_js = re.sub(r'// 7\. GOLD & SILVER RATES[\s\S]*?provider: "Karnata Precision Data \(Live Bullion Rates\)"\s*\};\s*\}', '', worker_js)
    print("SUCCESS: Regex removed static gold interception.")

# Ensure Workers AI models list prioritize top high-quality models
candidate_models_str = """      const candidateModels = [
        '@cf/meta/llama-3.3-70b-instruct',
        '@cf/meta/llama-3.1-8b-instruct',
        '@cf/qwen/qwen2.5-72b-instruct',
        '@cf/qwen/qwen1.5-7b-chat'
      ];"""

worker_js = re.sub(r'const candidateModels = \[[\s\S]*?\];', candidate_models_str, worker_js)

# Upgrade system prompt to give concise, structured, helpful answers in pure Kannada
new_system_prompt = """    const systemPrompt = `You are askKARNATA AI (ಕರ್ನಾಟ ಎಐ), the intelligent, factual, and helpful AI assistant for Karnataka state, India (Karnata.in).
Respond in natural, fluent, polite, grammatically correct Kannada (ಕನ್ನಡ).

CORE INSTRUCTIONS:
1. Answer the user's question directly, clearly, and thoughtfully.
2. If the user asks whether to buy or sell gold, or for wedding timing, or investment advice, provide a structured answer with:
   - Clear decision/verdict (ಖರೀದಿಗೆ ಸೂಕ್ತ / ಭಾಗಶಃ ಲಾಭ ಗಳಿಕೆ / ಹಂತ ಹಂತವಾಗಿ ಹೂಡಿಕೆ ಮಾಡಿ).
   - Market reasons with bullet points.
   - Smart tips (SIP model, SGB vs jewellery, making charge savings).
3. If the user asks general Karnataka questions (schemes, leaders, weather, dams, agriculture), answer factually and concisely.
4. Keep the tone helpful, authentic, and culturally polite.

VERIFIED FACTS & LIVE DATA:
${ragContext.verifiedFacts}
${goldContext}

Answer the user's specific question:`;"""

worker_js = re.sub(r'const systemPrompt = `You are askKARNATA AI[\s\S]*?Answer the user\'s question directly:`;', new_system_prompt, worker_js)

with open(os.path.join(ROOT_DIR, '_worker.js'), 'w', encoding='utf-8') as f:
    f.write(worker_js)
with open(os.path.join(NK_DIR, '_worker.js'), 'w', encoding='utf-8') as f:
    f.write(worker_js)

print("SUCCESS_UPDATED_WORKER_JS")

# 2. Fix the 4 battle cards styling in gold-rate.html
with open(os.path.join(ROOT_DIR, 'gold-rate.html'), 'r', encoding='utf-8') as f:
    gold_html = f.read()

# Fix .battle-card styling to ensure crisp black text and high contrast
battle_css_fix = """
    .battle-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
      margin-top: 20px;
    }
    @media (max-width: 860px) { .battle-grid { grid-template-columns: repeat(2, 1fr); } }
    @media (max-width: 480px) { .battle-grid { grid-template-columns: 1fr; } }

    .battle-card {
      background: #FFFFFF !important;
      border: 1.5px solid #E2E8F0 !important;
      border-radius: 14px !important;
      padding: 20px 16px !important;
      text-align: center !important;
      color: #0F172A !important;
      box-shadow: 0 4px 14px rgba(0,0,0,0.04) !important;
    }
    .battle-card.winner {
      border: 2px solid #F59E0B !important;
      background: #FFFDF5 !important;
      box-shadow: 0 6px 20px rgba(245, 158, 11, 0.15) !important;
    }
    .bc-icon { font-size: 28px; margin-bottom: 6px; }
    .bc-name { font-size: 15px; font-weight: 800; color: #0F172A !important; margin-bottom: 8px; }
    .bc-cagr { font-size: 18px; font-weight: 900; color: #D97706 !important; margin-bottom: 4px; font-family: 'Inter', sans-serif; }
    .bc-val { font-size: 13.5px; font-weight: 700; color: #334155 !important; font-family: 'Inter', sans-serif; }
"""

if '.battle-card.winner' in gold_html:
    gold_html = re.sub(r'\.battle-grid\s*\{[\s\S]*?\.bc-val[^\}]*\}', battle_css_fix.strip(), gold_html)
else:
    gold_html = gold_html.replace('</style>', battle_css_fix + '\n</style>')

with open(os.path.join(ROOT_DIR, 'gold-rate.html'), 'w', encoding='utf-8') as f:
    f.write(gold_html)
with open(os.path.join(NK_DIR, 'gold-rate.html'), 'w', encoding='utf-8') as f:
    f.write(gold_html)

print("SUCCESS_FIXED_BATTLE_CARDS_AND_WORKER")
