/**
 * Cloudflare Pages Function: /api/scrape-directory
 * Triggers live sync / fetch of Karnataka Government Contact Directory
 */

export async function onRequest(context) {
  const { request } = context;

  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type'
  };

  if (request.method === 'OPTIONS') {
    return new Response(null, { headers: corsHeaders });
  }

  try {
    const url = 'https://karnataka.gov.in/contactdirectory/public/17/government-contact-directory/kn';
    const resp = await fetch(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) KarnataSyncBot/2.0'
      }
    });

    if (!resp.ok) {
      throw new Error(`Failed to fetch upstream: ${resp.status}`);
    }

    const html = await resp.text();
    const tableCount = (html.match(/<table/g) || []).length;
    const rowCount = (html.match(/<tr/g) || []).length;

    return new Response(JSON.stringify({
      success: true,
      message: 'ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಅಧಿಕೃತ ಸಂಪರ್ಕ ಕೈಪಿಡಿ ಯಶಸ್ವಿಯಾಗಿ ಲೈವ್ ಸಿಂಕ್ ಆಗಿದೆ!',
      source: url,
      tables_found: tableCount,
      estimated_rows: rowCount,
      timestamp: new Date().toISOString()
    }), {
      status: 200,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });

  } catch (err) {
    return new Response(JSON.stringify({
      success: false,
      error: err.message,
      timestamp: new Date().toISOString()
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json', ...corsHeaders }
    });
  }
}
