/**
 * GET /api/gis/lookup?lat={lat}&lng={lng}
 * Cloudflare Pages Function for Spatial Administrative Resolution
 */

import { LocationLookupEngine } from '../../../lib/gis/location_lookup.js';

export async function onRequestGet(context) {
  const { searchParams } = new URL(context.request.url);
  const lat = searchParams.get('lat');
  const lng = searchParams.get('lng');

  if (!lat || !lng) {
    return new Response(JSON.stringify({
      success: false,
      error: 'ಅಕ್ಷಾಂಶ (lat) ಮತ್ತು ರೇಖಾಂಶ (lng) ಅಗತ್ಯವಿದೆ (lat and lng required)'
    }), {
      status: 400,
      headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' }
    });
  }

  try {
    const engine = new LocationLookupEngine();
    const result = engine.lookup(lat, lng);

    return new Response(JSON.stringify(result), {
      status: result.success ? 200 : 404,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'public, max-age=3600'
      }
    });
  } catch (err) {
    return new Response(JSON.stringify({
      success: false,
      error: err.message
    }), {
      status: 500,
      headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' }
    });
  }
}
