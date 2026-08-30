/**
 * Ask Karnata AI — Verified D1 FAQ Matcher
 * Performs token overlap and semantic keyword matching against certified Karnataka FAQs.
 */

export async function matchFAQ(normalizedQ, intent, env) {
  if (!env || !env.DB || !normalizedQ) return null;

  try {
    // 1. Exact or Prefix Search in ai_faq
    const exactMatch = await env.DB.prepare(
      'SELECT question, answer, category, source_url, action_label, action_url, keywords FROM ai_faq WHERE normalized_question LIKE ? LIMIT 1'
    ).bind(`%${normalizedQ}%`).first();

    if (exactMatch) {
      return formatFAQResponse(exactMatch, 'Exact FAQ Match');
    }

    // 2. Keyword Token Overlap Search
    const tokens = normalizedQ.split(' ').filter(t => t.length > 2);
    if (tokens.length === 0) return null;

    // Build SQL condition
    const conditions = tokens.map(() => '(normalized_question LIKE ? OR keywords LIKE ?)').join(' OR ');
    const params = [];
    tokens.forEach(t => {
      params.push(`%${t}%`);
      params.push(`%${t}%`);
    });

    const rows = await env.DB.prepare(
      `SELECT question, answer, category, source_url, action_label, action_url, keywords FROM ai_faq WHERE ${conditions} LIMIT 5`
    ).bind(...params).all();

    if (rows && rows.results && rows.results.length > 0) {
      // Score best candidate by keyword overlap
      let bestRow = null;
      let highestScore = 0;

      for (const row of rows.results) {
        let score = 0;
        const rowText = (row.normalized_question + ' ' + (row.keywords || '')).toLowerCase();
        for (const t of tokens) {
          if (rowText.includes(t)) score += 1;
        }
        if (score > highestScore) {
          highestScore = score;
          bestRow = row;
        }
      }

      // If at least 2 tokens match or >= 50% match
      if (bestRow && (highestScore >= 2 || highestScore >= tokens.length * 0.5)) {
        return formatFAQResponse(bestRow, 'Verified Knowledge FAQ');
      }
    }
  } catch (err) {
    console.warn('[D1 FAQ Match Warning]:', err);
  }

  return null;
}

function formatFAQResponse(faqRow, matchType) {
  const cards = [];
  if (faqRow.action_label && faqRow.action_url) {
    cards.push({
      title: faqRow.action_label,
      url: faqRow.action_url,
      icon: '🔎'
    });
  }

  const sources = [];
  if (faqRow.source_url) {
    sources.push({
      name: faqRow.category === 'SIR' ? 'Election Commission of India' : 'Government of Karnataka',
      url: faqRow.source_url
    });
  }

  return {
    answer: faqRow.answer,
    cards,
    sources,
    provider: `Karnata Certified FAQ (${matchType})`,
    faqHit: true
  };
}
