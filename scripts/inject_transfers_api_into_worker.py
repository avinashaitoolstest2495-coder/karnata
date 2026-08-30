# -*- coding: utf-8 -*-
"""
Karnata — scripts/inject_transfers_api_into_worker.py
Injects /api/transfers & /api/publish-transfers into _worker.js with Cloudflare KV sync
so all devices and browsers globally see updated transfers instantly.
"""

import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
worker_path = os.path.join(ROOT_DIR, '_worker.js')

with open(worker_path, 'r', encoding='utf-8') as f:
    worker_code = f.read()

transfers_worker_handler = """    // Route: Global Real-Time Edge API for Karnataka Transfers & Alerts
    if (url.pathname === '/api/transfers' || url.pathname === '/api/transfers/' || url.pathname === '/api/publish-transfers') {
      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
        'Content-Type': 'application/json; charset=utf-8'
      };

      if (request.method === 'OPTIONS') {
        return new Response(null, { headers: corsHeaders });
      }

      const kv = env && (env.NK_DATA || env.TRANSFERS_KV);

      // POST: Save newly extracted/published transfers into Cloudflare KV Edge
      if (request.method === 'POST') {
        try {
          const body = await request.json();
          const incomingTransfers = Array.isArray(body.transfers) ? body.transfers : (body.transfers ? [body.transfers] : []);

          let existingKvTransfers = [];
          if (kv) {
            try {
              const rawKv = await kv.get('karnata_live_transfers');
              if (rawKv) existingKvTransfers = JSON.parse(rawKv);
            } catch (e) {}
          }

          // Combine with deduplication
          const seen = new Set();
          const merged = [];

          for (let t of [...incomingTransfers, ...existingKvTransfers]) {
            const key = t.id || (t.order_no + '_' + (t.officer_name_kn || t.officer_name_en));
            if (!seen.has(key)) {
              seen.add(key);
              merged.push(t);
            }
          }

          if (kv) {
            await kv.put('karnata_live_transfers', JSON.stringify(merged));
          }

          return new Response(JSON.stringify({
            success: true,
            message: `Successfully saved ${incomingTransfers.length} transfers globally to Cloudflare Edge.`,
            count: merged.length,
            transfers: merged
          }), { headers: corsHeaders });
        } catch (pErr) {
          return new Response(JSON.stringify({ error: pErr.message }), { status: 500, headers: corsHeaders });
        }
      }

      // GET: Serve all transfers merged with live KV published transfers
      let baseTransfers = [];
      try {
        const staticResp = await env.ASSETS.fetch(new Request(new URL('/data/recent_transfers.json', request.url)));
        if (staticResp.ok) {
          const d = await staticResp.json();
          baseTransfers = d.transfers || [];
        }
      } catch (e) {}

      let kvTransfers = [];
      if (kv) {
        try {
          const rawKv = await kv.get('karnata_live_transfers');
          if (rawKv) kvTransfers = JSON.parse(rawKv);
        } catch (e) {}
      }

      const seen = new Set();
      const merged = [];

      for (let t of [...kvTransfers, ...baseTransfers]) {
        const key = t.id || (t.order_no + '_' + (t.officer_name_kn || t.officer_name_en));
        if (!seen.has(key)) {
          seen.add(key);
          merged.push(t);
        }
      }

      return new Response(JSON.stringify({
        success: true,
        count: merged.length,
        updated_at: new Date().toISOString(),
        transfers: merged
      }), { headers: corsHeaders });
    }
"""

if "url.pathname === '/api/transfers'" not in worker_code:
    worker_code = worker_code.replace(
        "    // Route: Officers Directory Admin API (GET & POST)",
        transfers_worker_handler + "\n    // Route: Officers Directory Admin API (GET & POST)"
    )
    with open(worker_path, 'w', encoding='utf-8') as f:
        f.write(worker_code)
    
    with open(os.path.join(ROOT_DIR, 'namma-karnataka', '_worker.js'), 'w', encoding='utf-8') as f:
        f.write(worker_code)
    print("Injected /api/transfers into _worker.js")

print("SUCCESS_TRANSFERS_API_DEPLOYED")
