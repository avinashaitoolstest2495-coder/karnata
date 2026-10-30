/**
 * Cloudflare Pages API: /api/posters
 * Real-Time Kannada Poster Upload, Retrieval & Deletion
 * Backed by Cloudflare KV (NK_DATA) for global edge sync across all devices, PCs, and phones.
 */

export async function onRequest(context) {
  const { request, env } = context;

  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, DELETE, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0'
  };

  if (request.method === 'OPTIONS') {
    return new Response(null, { headers: corsHeaders });
  }

  const kv = env?.NK_DATA || env?.TRANSFERS_KV || null;
  const KV_POSTERS_KEY = 'karnata_community_posters_v1';

  // ── GET: Return all community-uploaded posters from KV ──
  if (request.method === 'GET') {
    let posters = [];
    if (kv) {
      try {
        const raw = await kv.get(KV_POSTERS_KEY);
        if (raw) {
          posters = JSON.parse(raw);
        }
      } catch (err) {
        console.error('KV Posters GET error:', err);
      }
    }

    return new Response(JSON.stringify({
      success: true,
      count: posters.length,
      posters: posters
    }), {
      headers: {
        'Content-Type': 'application/json; charset=utf-8',
        ...corsHeaders
      }
    });
  }

  // ── POST: Upload new poster from any PC / mobile ──
  if (request.method === 'POST') {
    try {
      const payload = await request.json();

      if (!payload.imageData && !payload.imageUrl) {
        return new Response(JSON.stringify({
          success: false,
          error: 'Image data or image URL is required'
        }), {
          status: 400,
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }

      // Generate unique poster ID
      const posterId = 'custom-' + Date.now() + '-' + Math.random().toString(36).substring(2, 7);

      const newPoster = {
        id: posterId,
        category: payload.category || 'rajyotsava',
        catLabel: payload.catLabel || '🎨 ಪೋಸ್ಟರ್',
        header: payload.header || '',
        quote: payload.quote || 'ಸಿರಿಗನ್ನಡಂ ಗೆಲ್ಗೆ, ಸಿರಿಗನ್ನಡಂ ಬಾಳ್ಗೆ!',
        author: payload.author || (payload.uploaderName ? `— ${payload.uploaderName}` : '— ಕನ್ನಡಿಗ'),
        bgType: 'image',
        bgImage: payload.imageData || payload.imageUrl,
        aspect: payload.aspect || '4:5',
        uploaderName: payload.uploaderName || '',
        created_at: new Date().toISOString()
      };

      let existingPosters = [];
      if (kv) {
        try {
          const raw = await kv.get(KV_POSTERS_KEY);
          if (raw) existingPosters = JSON.parse(raw);
        } catch (e) {}

        // Add to top of list (keep up to 100 recent community posters)
        existingPosters.unshift(newPoster);
        if (existingPosters.length > 100) {
          existingPosters = existingPosters.slice(0, 100);
        }

        try {
          await kv.put(KV_POSTERS_KEY, JSON.stringify(existingPosters));
        } catch (err) {
          console.error('KV Posters PUT error:', err);
          return new Response(JSON.stringify({
            success: false,
            error: 'KV Storage write failed: ' + (err.message || 'unknown error')
          }), { status: 500, headers: corsHeaders });
        }
      }

      return new Response(JSON.stringify({
        success: true,
        message: 'Poster uploaded and published live successfully across all devices!',
        poster: newPoster
      }), {
        headers: {
          'Content-Type': 'application/json; charset=utf-8',
          ...corsHeaders
        }
      });
    } catch (err) {
      return new Response(JSON.stringify({
        success: false,
        error: err.message || 'Failed to process upload'
      }), {
        status: 500,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }
  }

  // ── DELETE: Remove a poster by ID ──
  if (request.method === 'DELETE') {
    try {
      const url = new URL(request.url);
      const id = url.searchParams.get('id');
      if (!id || !kv) {
        return new Response(JSON.stringify({ success: false, error: 'ID is required' }), {
          status: 400,
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }

      let posters = [];
      const raw = await kv.get(KV_POSTERS_KEY);
      if (raw) posters = JSON.parse(raw);
      const updated = posters.filter(p => p.id !== id);
      await kv.put(KV_POSTERS_KEY, JSON.stringify(updated));

      return new Response(JSON.stringify({ success: true, count: updated.length }), {
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    } catch (err) {
      return new Response(JSON.stringify({ success: false, error: err.message }), {
        status: 500,
        headers: { 'Content-Type': 'application/json', ...corsHeaders }
      });
    }
  }

  return new Response(JSON.stringify({ error: 'Method not allowed' }), {
    status: 405,
    headers: corsHeaders
  });
}
