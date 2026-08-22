/**
 * Cloudflare Pages Function: /api/transfers
 * Global Real-Time Edge API for Karnataka Transfers & Alerts
 * Backed by Cloudflare KV (NK_DATA) for 100% Global Edge Persistence across all browsers.
 */

export async function onRequest(context) {
  const { request, env } = context;

  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0'
  };

  if (request.method === 'OPTIONS') {
    return new Response(null, { headers: corsHeaders });
  }

  const origin = new URL(request.url).origin;
  const kv = env?.NK_DATA || env?.TRANSFERS_KV || null;

  // GET: Serve all transfers merged with live KV published transfers
  if (request.method === 'GET') {
    let baseTransfers = [];
    try {
      const res = await fetch(`${origin}/data/recent_transfers.json?v=${Date.now()}`);
      if (res.ok) {
        const d = await res.json();
        baseTransfers = d.transfers || [];
      }
    } catch (e) {}

    // Read persistently stored live transfers from Cloudflare KV
    let kvTransfers = [];
    if (kv) {
      try {
        const rawKv = await kv.get('karnata_live_transfers');
        if (rawKv) {
          kvTransfers = JSON.parse(rawKv);
        }
      } catch (e) {
        console.error('KV Read Error:', e);
      }
    }

    // Merge: KV live transfers on top, then base file transfers
    const seen = new Set();
    const merged = [];

    for (let t of [...kvTransfers, ...baseTransfers]) {
      const key = t.id || (t.order_no + t.officer_name_kn);
      if (!seen.has(key)) {
        seen.add(key);
        merged.push(t);
      }
    }

    return new Response(JSON.stringify({
      status: 'success',
      total_transfers: merged.length,
      kv_live_count: kvTransfers.length,
      updated_at: new Date().toISOString(),
      transfers: merged
    }), {
      headers: {
        'Content-Type': 'application/json; charset=utf-8',
        ...corsHeaders
      }
    });
  }

  // POST: Publish new live transfer directly into Cloudflare KV
  if (request.method === 'POST') {
    try {
      const body = await request.json().catch(() => ({}));
      const newItems = Array.isArray(body.transfers) ? body.transfers : (body ? [body] : []);

      if (!newItems.length) {
        return new Response(JSON.stringify({ error: 'No transfers provided' }), {
          status: 400,
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }

      const formatted = newItems.map((item, idx) => ({
        id: item.id || `LIVE-TRF-${Date.now()}-${idx}`,
        cadre: item.cadre || 'KAS',
        cadre_badge: item.cadre === 'IAS' ? '🏛️ IAS' : (item.cadre === 'IPS' ? '👮 IPS' : '📜 KAS'),
        date: item.date || new Date().toISOString().slice(0, 10).split('-').reverse().join('-'),
        order_no: item.order_no || 'ಸಿಆಸುಇ ಅಧಿಸೂಚನೆ 2026',
        officer_name_kn: item.officer_name_kn || 'ಅಧಿಕಾರಿಯ ಹೆಸರು',
        officer_name_en: item.officer_name_en || item.officer_name_kn || 'Officer Name',
        previous_posting: item.previous_posting || '',
        new_posting: item.new_posting || '',
        district_key: item.district_key || 'bengaluru_urban',
        summary_kn: item.summary_kn || `${item.officer_name_kn} ರವರ ವರ್ಗಾವಣೆ ಆದೇಶ.`,
        summary_en: item.summary_en || `${item.officer_name_en || item.officer_name_kn} transfer order.`,
        is_live_alert: true,
        is_new_go_alert: true,
        source: 'Cloudflare KV Live Publish',
        source_label: '⚡ Live Alert: ನೂತನ ವರ್ಗಾವಣೆ'
      }));

      // Persist permanently in Cloudflare KV
      if (kv) {
        try {
          const rawKv = await kv.get('karnata_live_transfers');
          const existing = rawKv ? JSON.parse(rawKv) : [];
          
          // Deduplicate
          const seenIds = new Set();
          const combined = [];
          for (let it of [...formatted, ...existing]) {
            const k = it.id || (it.order_no + it.officer_name_kn);
            if (!seenIds.has(k)) {
              seenIds.add(k);
              combined.push(it);
            }
          }

          await kv.put('karnata_live_transfers', JSON.stringify(combined));
          console.log(`✅ Stored ${combined.length} transfers in Cloudflare KV (NK_DATA)`);
        } catch (e) {
          console.error('KV Write Error:', e);
        }
      }

      // Trigger instant Google Search Engine & IndexNow indexing ping
      try {
        await fetch(`${origin}/api/ping-search-engines?url=${encodeURIComponent('https://karnata.in/officers.html')}`);
      } catch (e) {}

      return new Response(JSON.stringify({
        success: true,
        count: formatted.length,
        transfers: formatted,
        message: `${formatted.length} ವರ್ಗಾವಣೆ ಆದೇಶಗಳನ್ನು Cloudflare KV ಗೆ ಯಶಸ್ವಿಯಾಗಿ ಸೇವ್ ಮಾಡಲಾಗಿದೆ!`
      }), {
        headers: {
          'Content-Type': 'application/json; charset=utf-8',
          ...corsHeaders
        }
      });
    } catch (err) {
      return new Response(JSON.stringify({ error: err.message }), {
        status: 500,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }
  }
}
