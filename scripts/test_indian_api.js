/**
 * Test Script: Verify indianapi.in API response for Karnataka districts
 * Usage: node scripts/test_indian_api.js YOUR_API_KEY
 *
 * This will show you exactly what data the API returns so you can confirm it's live.
 */

const API_KEY = process.argv[2] || process.env.INDIAN_API_KEY;
const BASE    = 'https://fuel.indianapi.in';

if (!API_KEY) {
  console.error('❌ Please pass your API key: node scripts/test_indian_api.js YOUR_KEY');
  process.exit(1);
}

const headers = { 'x-api-key': API_KEY };

async function run() {
  console.log('='.repeat(60));
  console.log('🔑 Testing IndianAPI.in Fuel Price API');
  console.log('='.repeat(60));

  // 1. List all available cities
  console.log('\n📍 Step 1: Fetching city list...');
  const citiesRes = await fetch(`${BASE}/cities`, { headers });
  const cities = await citiesRes.json();
  console.log(`   Total cities: ${Array.isArray(cities) ? cities.length : 'N/A'}`);
  const kaCities = Array.isArray(cities) ? cities.filter(c =>
    ['Bangalore','Mysore','Hubli','Mangalore','Belgaum','Davangere','Tumkur',
     'Gulbarga','Shimoga','Bellary','Hassan','Bidar','Raichur','Udupi','Mandya',
     'Kolar','Chitradurga','Gadag','Haveri','Koppal','Bagalkot','Karwar',
     'Ramanagara','Chikballapur','Chikmagalur','Chamarajanagar','Yadgir'].some(
      k => (c.name || c.value || '').toLowerCase().includes(k.toLowerCase())
    )
  ) : [];
  console.log(`   Karnataka cities found: ${kaCities.length}`);
  kaCities.forEach(c => console.log(`     - ${c.name || c.value}`));

  // 2. Live petrol prices for all states
  console.log('\n⛽ Step 2: Fetching live PETROL prices (state level)...');
  const petrolRes = await fetch(`${BASE}/live_fuel_price?fuel_type=petrol&location_type=state`, { headers });
  const petrolData = await petrolRes.json();
  const kaState = Array.isArray(petrolData) ? petrolData.find(d =>
    (d.city || d.name || '').toLowerCase().includes('karnatak')
  ) : null;
  console.log(`   Karnataka petrol: ${kaState ? JSON.stringify(kaState) : 'Not found in response'}`);
  console.log(`   Sample (first 3):`, JSON.stringify(Array.isArray(petrolData) ? petrolData.slice(0,3) : petrolData, null, 2));

  // 3. Live diesel prices for Karnataka state
  console.log('\n🛢️  Step 3: Fetching live DIESEL prices (state level)...');
  const dieselRes = await fetch(`${BASE}/live_fuel_price?fuel_type=diesel&location_type=state`, { headers });
  const dieselData = await dieselRes.json();
  const kaDiesel = Array.isArray(dieselData) ? dieselData.find(d =>
    (d.city || d.name || '').toLowerCase().includes('karnatak')
  ) : null;
  console.log(`   Karnataka diesel: ${kaDiesel ? JSON.stringify(kaDiesel) : 'Not found'}`);

  // 4. Live prices at city level for Bangalore
  console.log('\n🏙️  Step 4: Fetching live PETROL price for Bangalore (city level)...');
  const bangRes = await fetch(`${BASE}/live_fuel_price?fuel_type=petrol&location_type=city`, { headers });
  const bangData = await bangRes.json();
  const bangCity = Array.isArray(bangData) ? bangData.find(d =>
    (d.city || d.name || '').toLowerCase().includes('bangal')
  ) : null;
  console.log(`   Bangalore petrol: ${bangCity ? JSON.stringify(bangCity) : 'Not found'}`);
  console.log(`   Sample cities (first 5):`, JSON.stringify(Array.isArray(bangData) ? bangData.slice(0,5) : bangData, null, 2));

  // 5. Historical petrol data for Bangalore (last 10 days as test)
  console.log('\n📊 Step 5: Fetching HISTORICAL petrol for Bangalore (last 10 days)...');
  const histRes = await fetch(
    `${BASE}/historical_fuel_price?fuel_type=petrol&location_type=city&location=Bangalore&n=10`,
    { headers }
  );
  const histData = await histRes.json();
  console.log(`   Historical data (petrol, Bangalore, 10 days):`);
  console.log(JSON.stringify(histData, null, 2));

  // 6. Historical diesel data for Bangalore
  console.log('\n📊 Step 6: Fetching HISTORICAL diesel for Bangalore (last 10 days)...');
  const histDRes = await fetch(
    `${BASE}/historical_fuel_price?fuel_type=diesel&location_type=city&location=Bangalore&n=10`,
    { headers }
  );
  const histDData = await histDRes.json();
  console.log(`   Historical data (diesel, Bangalore, 10 days):`);
  console.log(JSON.stringify(histDData, null, 2));

  console.log('\n' + '='.repeat(60));
  console.log('✅ Test complete! Review above output to confirm live data.');
  console.log('='.repeat(60));
}

run().catch(e => {
  console.error('❌ Test failed:', e.message);
  process.exit(1);
});
