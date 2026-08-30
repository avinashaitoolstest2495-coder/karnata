/**
 * Ask Karnata AI — Multi-Tier Aggressive Cache Manager
 * Resolves exact & normalized queries from D1 (ai_cache) & KV with zero AI latency.
 */

export async function getCachedResponse(normalizedQ, env) {
  if (!normalizedQ) return null;

  // 1. Try Cloudflare KV Fast In-Memory Cache if available
  if (env && env.NK_DATA) {
    try {
      const kvKey = `ai_cache:${normalizedQ.slice(0, 80)}`;
      const kvCached = await env.NK_DATA.get(kvKey, 'json');
      if (kvCached) {
        return {
          answer: kvCached.answer,
          cards: kvCached.cards || [],
          sources: kvCached.sources || [],
          provider: 'Karnata High-Speed Edge Cache (KV)',
          cacheHit: true
        };
      }
    } catch (e) {}
  }

  // 2. Try Cloudflare D1 Cache
  if (env && env.DB) {
    try {
      const nowUnix = Math.floor(Date.now() / 1000);
      const row = await env.DB.prepare(
        'SELECT answer, sources_json, cards_json, hit_count FROM ai_cache WHERE normalized_question = ? AND expires_at > ? LIMIT 1'
      ).bind(normalizedQ, nowUnix).first();

      if (row) {
        // Increment hit counter asynchronously
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
    } catch (dbErr) {
      console.warn('[D1 Cache Lookup Warning]:', dbErr);
    }
  }

  return null;
}

export async function saveResponseToCache(normalizedQ, answer, cards, sources, env) {
  if (!normalizedQ || !answer) return;

  const ttlSeconds = parseInt(env.AI_CACHE_TTL || '86400', 10);
  const expiresAt = Math.floor(Date.now() / 1000) + ttlSeconds;

  // 1. Save to KV
  if (env && env.NK_DATA) {
    try {
      const kvKey = `ai_cache:${normalizedQ.slice(0, 80)}`;
      await env.NK_DATA.put(kvKey, JSON.stringify({
        answer,
        cards,
        sources,
        created: Date.now()
      }), { expirationTtl: ttlSeconds });
    } catch (e) {}
  }

  // 2. Save to D1
  if (env && env.DB) {
    try {
      const cacheId = 'cache_' + Math.random().toString(36).substring(2, 10);
      await env.DB.prepare(
        `INSERT INTO ai_cache (id, normalized_question, answer, sources_json, cards_json, expires_at)
         VALUES (?, ?, ?, ?, ?, ?)
         ON CONFLICT(normalized_question) DO UPDATE SET 
           answer = excluded.answer,
           sources_json = excluded.sources_json,
           cards_json = excluded.cards_json,
           hit_count = hit_count + 1,
           expires_at = excluded.expires_at`
      ).bind(
        cacheId,
        normalizedQ,
        answer,
        JSON.stringify(sources || []),
        JSON.stringify(cards || []),
        expiresAt
      ).run();
    } catch (dbErr) {
      console.warn('[D1 Cache Write Warning]:', dbErr);
    }
  }
}
