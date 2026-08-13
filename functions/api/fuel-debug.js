/**
 * Cloudflare Pages Function: /functions/api/fuel-debug.js
 * Open https://karnata.pages.dev/api/fuel-debug in your browser to see the raw live API response
 * Shows exactly what indianapi.in returns + confirms your key is working
 */

const BASE_URL = 'https://fuel.indianapi.in';

export async function onRequest(context) {
  const { env } = context;
  const apiKey = env.INDIAN_API_KEY;

  const h = { 'Content-Type': 'application/json' };

  if (!apiKey) {
    return new Response(JSON.stringify({
      status: 'ERROR',
      message: 'INDIAN_API_KEY not set in Cloudflare environment variables',
    }, null, 2), { headers: h });
  }

  const headers = { 'x-api-key': apiKey };

  try {
    // Fetch cities list, live petrol (city), and 10-day history all at once
    const [citiesRes, petrolRes, histRes] = await Promise.all([
      fetch(`${BASE_URL}/cities`, { headers }),
      fetch(`${BASE_URL}/live_fuel_price?fuel_type=petrol&location_type=city`, { headers }),
      fetch(`${BASE_URL}/historical_fuel_price?fuel_type=petrol&location_type=city&location=Bangalore&n=10`, { headers }),
    ]);

    const cities   = await citiesRes.json();
    const petrol   = await petrolRes.json();
    const history  = await histRes.json();

    // Filter to Karnataka-related cities
    const kaCities = Array.isArray(petrol)
      ? petrol.filter(c => {
          const name = (c.city || c.name || '').toLowerCase();
          return ['bangalore','mysore','hubli','mangalore','belgaum','davangere','tumkur',
            'gulbarga','shimoga','bellary','hassan','bidar','raichur','udupi','mandya',
            'kolar','chitradurga','gadag','haveri','koppal','bagalkot','karwar',
            'ramanagara','chikballapur','chikmagalur','chamarajanagar','yadgir']
            .some(k => name.includes(k));
        })
      : [];

    return new Response(JSON.stringify({
      status: 'SUCCESS',
      api_key_set: true,
      timestamp: new Date().toISOString(),
      endpoints_used: [
        `${BASE_URL}/cities`,
        `${BASE_URL}/live_fuel_price?fuel_type=petrol&location_type=city`,
        `${BASE_URL}/historical_fuel_price?fuel_type=petrol&location_type=city&location=Bangalore&n=10`,
      ],
      total_cities_from_api: Array.isArray(cities) ? cities.length : 'N/A',
      all_city_names_sample: Array.isArray(cities) ? cities.slice(0, 20) : cities,
      karnataka_cities_found: kaCities.length,
      karnataka_petrol_prices: kaCities,
      bangalore_10day_history: history,
      raw_petrol_sample_first_5: Array.isArray(petrol) ? petrol.slice(0, 5) : petrol,
    }, null, 2), { headers: h });

  } catch (err) {
    return new Response(JSON.stringify({
      status: 'ERROR',
      message: err.message,
    }, null, 2), { status: 500, headers: h });
  }
}
