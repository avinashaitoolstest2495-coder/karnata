/**
 * Karnata — /api/schemes
 * Government Schemes Eligibility Matching API
 * Cloudflare Pages Function
 */

const CACHE_TTL = 3600; // 1 hour

export async function onRequest(context) {
  const { request, env } = context;

  // Handle CORS
  if (request.method === 'OPTIONS') {
    return new Response(null, {
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
      }
    });
  }

  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Content-Type': 'application/json',
  };

  try {
    // Determine base URL dynamically depending on the deployment environment
    const url = new URL(request.url);
    const origin = url.origin;

    // Fetch the JSON from the same deployment
    const dataResponse = await fetch(`${origin}/data/government_schemes.json`);
    if (!dataResponse.ok) {
        throw new Error(`Failed to load scheme data: ${dataResponse.status}`);
    }
    
    const data = await dataResponse.json();
    const schemes = data.schemes || [];

    if (request.method === 'GET') {
      const searchParams = url.searchParams;
      const query = searchParams.get('search')?.toLowerCase() || '';

      let filteredSchemes = schemes;
      if (query) {
        filteredSchemes = schemes.filter(s => 
          (s.scheme_name_en && s.scheme_name_en.toLowerCase().includes(query)) ||
          (s.scheme_name_kn && s.scheme_name_kn.includes(query)) ||
          (s.tags && s.tags.includes(query))
        );
      }

      return new Response(JSON.stringify({
        last_updated: data.last_updated,
        total: filteredSchemes.length,
        schemes: filteredSchemes
      }), {
        headers: {
          ...corsHeaders,
          'Cache-Control': `public, max-age=${CACHE_TTL}`,
        }
      });
    }

    if (request.method === 'POST') {
      const body = await request.json();
      const { age, gender, income, category, occupation, residence } = body;

      const eligible = [];
      const possible = [];

      schemes.forEach(scheme => {
        let isEligible = true;
        let needsSpecialCheck = false;

        // Age check
        if (scheme.min_age !== null && age < scheme.min_age) isEligible = false;
        if (scheme.max_age !== null && age > scheme.max_age) isEligible = false;

        // Income check
        if (scheme.income_max !== null && income > scheme.income_max) isEligible = false;

        // Gender check
        if (scheme.gender && !scheme.gender.includes('all') && !scheme.gender.includes(gender)) {
            isEligible = false;
        }

        // Category check
        if (scheme.categories && !scheme.categories.includes('all') && !scheme.categories.includes(category)) {
            isEligible = false;
        }

        // Occupation check
        if (scheme.occupations && !scheme.occupations.includes('all') && !scheme.occupations.includes(occupation)) {
            isEligible = false;
        }

        // Residence check
        if (scheme.residence_type !== 'any' && scheme.residence_type !== residence) {
            isEligible = false;
        }

        // Special criteria
        if (scheme.special_criteria && scheme.special_criteria.length > 0) {
            needsSpecialCheck = true;
        }

        if (isEligible) {
          if (needsSpecialCheck) {
            possible.push({ ...scheme, reason: "ಹೆಚ್ಚುವರಿ ಪರಿಶೀಲನೆ ಅಗತ್ಯ (Special criteria applies)" });
          } else {
            eligible.push(scheme);
          }
        }
      });

      return new Response(JSON.stringify({
        eligible_count: eligible.length,
        possible_count: possible.length,
        eligible,
        possible
      }), {
        headers: {
          ...corsHeaders,
          'Cache-Control': `public, max-age=${CACHE_TTL}`,
        }
      });
    }

    return new Response(JSON.stringify({ error: 'Method not allowed' }), {
      status: 405,
      headers: corsHeaders
    });

  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: corsHeaders
    });
  }
}
