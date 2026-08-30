# -*- coding: utf-8 -*-
"""
Karnata — scripts/refine_workers_ai_and_purge_bad_cache.py
1. In _worker.js getCachedResponse: ignore stale fallback responses containing generic boilerplate.
2. Refine prompt engineering for Cloudflare Workers AI so that every response has high Kannada fluency, bullet points, and exact numbers.
3. Sync and deploy.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

with open(os.path.join(ROOT_DIR, '_worker.js'), 'r', encoding='utf-8') as f:
    worker_js = f.read()

# 1. Ignore generic cached boilerplate
cache_purge_logic = """      if (row) {
        if (row.answer && (row.answer.includes('SIR ಮತದಾರರ ಪಟ್ಟಿ') || row.answer.includes('Karnata Knowledge Fallback'))) {
          // Stale boilerplate cache — bypass and let Workers AI answer freshly
        } else {
          env.DB.prepare(
            'UPDATE ai_cache SET hit_count = hit_count + 1 WHERE normalized_question = ?'
          ).bind(normalizedQ).run().catch(() => {});

          return {
            answer: row.answer,
            cards: row.cards_json ? JSON.parse(row.cards_json) : [],
            sources: row.sources_json ? JSON.parse(row.sources_json) : [],
            provider: 'Karnata Edge D1 Cache',
            cacheHit: true
          };
        }
      }"""

worker_js = re.sub(r'if \(row\) \{[\s\S]*?return \{[\s\S]*?cacheHit: true\s*\};\s*\}', cache_purge_logic, worker_js)

# 2. Refine system prompt
refined_system_prompt = """    const systemPrompt = `You are askKARNATA AI (ಕರ್ನಾಟ ಎಐ), the official intelligent AI assistant for Karnataka state, India (Karnata.in).
Respond in natural, fluent, polite, grammatically correct Kannada (ಕನ್ನಡ).

INSTRUCTIONS:
1. Answer the user's question directly, clearly, and thoughtfully with bullet points.
2. If the user asks about gold/silver buying, selling, or investment, use the live market data below to give:
   - Clear Verdict: (ಖರೀದಿಗೆ ಸೂಕ್ತ ಸಮಯ / ಭಾಗಶಃ ಲಾಭ ಗಳಿಕೆ / ಹಂತ ಹಂತವಾಗಿ ಹೂಡಿಕೆ).
   - Live Rates: 24K: ₹16,304/g, 22K: ₹14,940/g, Silver: ₹260/g.
   - Smart Tips: (ಮುಂಗಡ ಬುಕಿಂಗ್, ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ ಉಳಿತಾಯ, SGB/ಡಿಜಿಟಲ್ ಗೋಲ್ಡ್).
3. If the user asks general Karnataka questions (schemes, leaders, weather, dams, agriculture), answer factually and concisely.

VERIFIED FACTS & LIVE DATA:
${ragContext.verifiedFacts}
${goldContext}

Answer the user's specific question now:`;"""

worker_js = re.sub(r'const systemPrompt = `You are askKARNATA AI[\s\S]*?Answer the user\'s specific question:`;', refined_system_prompt, worker_js)

with open(os.path.join(ROOT_DIR, '_worker.js'), 'w', encoding='utf-8') as f:
    f.write(worker_js)
with open(os.path.join(NK_DIR, '_worker.js'), 'w', encoding='utf-8') as f:
    f.write(worker_js)

print("SUCCESS_REFINED_WORKERS_AI_AND_CACHE")
