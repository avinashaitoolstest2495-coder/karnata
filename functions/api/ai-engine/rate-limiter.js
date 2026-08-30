/**
 * Ask Karnata AI — Rate Limiting, Abuse Prevention & Free-Tier Budget Protection
 */

// In-memory sliding window cache for burst rate limiting
const inMemoryRateMap = new Map();

/**
 * Check if the request exceeds rate limits or daily AI caps
 */
export async function checkRateLimitAndSecurity(request, env, normalizedQ) {
  const clientIP = request.headers.get('CF-Connecting-IP') || 
                   request.headers.get('x-real-ip') || 
                   'anonymous';

  const now = Date.now();

  // 1. IP Burst Rate Limiting: Max 20 requests per minute per IP
  const windowMs = 60 * 1000;
  const ipData = inMemoryRateMap.get(clientIP) || { count: 0, firstReq: now };

  if (now - ipData.firstReq > windowMs) {
    ipData.count = 1;
    ipData.firstReq = now;
  } else {
    ipData.count += 1;
  }
  inMemoryRateMap.set(clientIP, ipData);

  if (ipData.count > 25) {
    return {
      allowed: false,
      reason: 'RATE_LIMIT_EXCEEDED',
      message: 'ಕ್ಷಮಿಸಿ, ಹೆಚ್ಚಿನ ಸಂಖ್ಯೆಯ ವಿನಂತಿಗಳು ಬಂದಿವೆ. ದಯವಿಟ್ಟು 1 ನಿಮಿಷದ ನಂತರ ಪ್ರಯತ್ನಿಸಿ.'
    };
  }

  // 2. Input Payload Length Limit (Max 1500 chars)
  const maxLen = parseInt(env.AI_MAX_INPUT_LENGTH || '1500', 10);
  if (normalizedQ.length > maxLen) {
    return {
      allowed: false,
      reason: 'PAYLOAD_TOO_LARGE',
      message: 'ಪ್ರಶ್ನೆಯು ನಿಗದಿಪಡಿಸಿದ ಮಿತಿಗಿಂತ ಹೆಚ್ಚಾಗಿದೆ. ದಯವಿಟ್ಟು ಚಿಕ್ಕದಾದ ಪ್ರಶ್ನೆ ಕೇಳಿ.'
    };
  }

  // 3. Prompt Injection Shield
  if (
    normalizedQ.includes('ignore previous') || 
    normalizedQ.includes('system prompt') || 
    normalizedQ.includes('api key') || 
    normalizedQ.includes('database password')
  ) {
    return {
      allowed: false,
      reason: 'INJECTION_DETECTED',
      message: 'ಕ್ಷಮಿಸಿ, ಸುರಕ್ಷತಾ ಕಾರಣಗಳಿಂದ ಈ ರೀತಿಯ ವಿನಂತಿಗಳನ್ನು ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಲು ಸಾಧ್ಯವಿಲ್ಲ. ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ಮಾಹಿತಿಯ ಕುರಿತು ಕೇಳಿ.'
    };
  }

  return { allowed: true };
}

/**
 * Check if the daily AI limit has been reached
 */
export async function checkDailyAIBudget(env) {
  if (!env || !env.NK_DATA) return true; // allow if KV is not bound

  const todayStr = new Date().toISOString().slice(0, 10);
  const key = `ai_daily_count_${todayStr}`;
  const dailyLimit = parseInt(env.AI_DAILY_LIMIT || '1000', 10);

  try {
    const rawVal = await env.NK_DATA.get(key);
    const count = rawVal ? parseInt(rawVal, 10) : 0;
    if (count >= dailyLimit) {
      return false; // budget exceeded
    }
    // Increment count with 2-day TTL
    await env.NK_DATA.put(key, (count + 1).toString(), { expirationTtl: 172800 });
    return true;
  } catch (err) {
    console.warn('[Daily AI Budget Check Warning]:', err);
    return true; // fail open to avoid downtime
  }
}
