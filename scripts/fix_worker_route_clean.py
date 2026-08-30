# -*- coding: utf-8 -*-
"""
Karnata — scripts/fix_worker_route_clean.py
Cleans up _worker.js and places /api/gold-ai properly inside export default { async fetch(request, env, ctx) { ... } }
"""

with open("_worker.js", "r", encoding="utf-8") as f:
    text = f.read()

# Remove the incorrectly placed top-level block
import re
text = re.sub(r'// ═+\s*// GOLD & COMMODITY REAL-TIME LLM INTELLIGENCE ENDPOINT[\s\S]*?return new Response\(JSON\.stringify\(\{\s*success: false,\s*fallback: true,\s*message: \'Using client-side neural gold model\'\s*\}\), \{ headers: corsHeaders \}\);\s*\}', '', text)

# Now find export default { async fetch(request, env, ctx) {
route_code = """
    // Route: Gold & Commodity LLM AI
    if (url.pathname === '/api/gold-ai') {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Content-Type': 'application/json'
      };

      if (request.method === 'OPTIONS') {
        return new Response(null, { headers: corsHeaders });
      }

      let query = '';
      if (request.method === 'POST') {
        try {
          const body = await request.json();
          query = (body.prompt || body.question || '').trim();
        } catch (e) {}
      } else {
        query = (url.searchParams.get('q') || url.searchParams.get('prompt') || '').trim();
      }

      if (!query) {
        return new Response(JSON.stringify({ error: 'Prompt is required' }), { status: 400, headers: corsHeaders });
      }

      const goldSystemPrompt = `You are the Karnataka Gold & Commodity Market Intelligence AI Expert on Karnata.in.
Current Spot Rates: 24K Gold: ₹16,304/gram, 22K Gold: ₹14,940/gram (₹1,19,520/pavan), 999 Silver: ₹260.00/gram.
10-Year Historical CAGR: +18.9% (2016: ₹2,862/g -> 2026: ₹16,304/g).
Seasonality: August-Sept is Pre-Festive Dip (Best accumulation window). Diwali/Dhanteras brings 3.5%-6% price surge. Ugadi/Akshaya Tritiya brings 3%-5% surge.
Answer the user question thoroughly and respectfully in clean, structured, natural Kannada (ಕನ್ನಡ) with markdown bold headings and bullet points. Include realistic price projection numbers and clear buying/selling strategy.`;

      if (env && env.AI) {
        const candidateModels = [
          '@cf/meta/llama-3.1-8b-instruct',
          '@cf/qwen/qwen1.5-7b-chat',
          '@cf/mistral/mistral-7b-instruct-v0.1'
        ];

        for (const m of candidateModels) {
          try {
            const aiResp = await env.AI.run(m, {
              messages: [
                { role: 'system', content: goldSystemPrompt },
                { role: 'user', content: query }
              ],
              max_tokens: 700,
              temperature: 0.3
            });

            const textResp = aiResp ? (aiResp.response || aiResp.text || (aiResp.choices && aiResp.choices[0] && aiResp.choices[0].message && aiResp.choices[0].message.content)) : null;
            if (textResp && textResp.length > 30) {
              return new Response(JSON.stringify({
                success: true,
                answer: textResp,
                model: m,
                source: 'Cloudflare Workers AI (LLM)'
              }), { headers: corsHeaders });
            }
          } catch (mErr) {
            console.warn(`[Gold AI] Model ${m} error:`, mErr.message);
          }
        }
      }

      return new Response(JSON.stringify({
        success: false,
        fallback: true,
        message: 'Using client-side neural gold model'
      }), { headers: corsHeaders });
    }
"""

pos_fetch = text.find('async fetch(request, env, ctx) {')
if pos_fetch != -1:
    pos_url = text.find('const url = new URL(request.url);', pos_fetch)
    if pos_url != -1:
        insert_idx = pos_url + len('const url = new URL(request.url);')
        text = text[:insert_idx] + route_code + text[insert_idx:]

with open("_worker.js", "w", encoding="utf-8") as f:
    f.write(text)

with open("namma-karnataka/_worker.js", "w", encoding="utf-8") as f:
    f.write(text)

print("SUCCESS_CLEANED_WORKER_ROUTER")
