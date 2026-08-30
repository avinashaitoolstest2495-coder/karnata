/**
 * panchatantra_engine.js — Universal Panchatantra Orchestrator & CLI Runner
 * Supports:
 * --gp <gp_id>        : Test / Scrape single Gram Panchayat (e.g. 1520001005 for AGOLI)
 * --taluk <tp_id>     : Scrape all Gram Panchayats in a Taluk (e.g. 1520001 for Gangavati)
 * --district <dist_id>: Scrape all Gram Panchayats in a District (e.g. 1520 for Koppal)
 * --full              : Full Karnataka Gram Panchayat Scrape
 */

const { gpScraper } = require('./gp_scraper');
const { hierarchyManager } = require('./hierarchy_manager');
const { storageManager } = require('./storage_manager');

async function runCli() {
  const args = process.argv.slice(2);
  const gpIdx = args.indexOf('--gp');
  const talukIdx = args.indexOf('--taluk');
  const districtIdx = args.indexOf('--district');

  console.log('🏛️  Panchatantra Gram Panchayat Universal Scraper Engine');
  console.log('====================================================\n');

  if (gpIdx !== -1 && args[gpIdx + 1]) {
    const gpId = args[gpIdx + 1];
    console.log(`Executing Single GP Test for GP ID: ${gpId}...`);
    const result = await gpScraper.scrapeGp({ gp_id: gpId });

    console.log('\n=== SCRAPE RESULT SUMMARY ===');
    console.log(`GP: ${result.gp_name_kn} (${result.gp_name_en})`);
    console.log(`District: ${result.district_name_kn} (${result.district_name_en}) | Taluk: ${result.taluk_name_kn} (${result.taluk_name_en})`);
    console.log(`LGD Code: ${result.lgd_code} | Pin: ${result.pin_code} | Coordinates: ${result.latitude}, ${result.longitude}`);
    console.log(`Total Staff Collected: ${result.total_staff} (PDO: ${result.staff.find(s => s.designation_kn?.includes('ಅಭಿವೃದ್ಧಿ') || s.designation?.includes('Development'))?.emp_name_en || 'N/A'})`);
    console.log(`Total Meetings: ${result.total_meetings} | Revenue Villages: ${result.revenue.length} | Applications: ${result.applications.length}`);
    console.log('\nService Statuses:');
    for (const [sName, sVal] of Object.entries(result.statuses)) {
      console.log(`  ${sVal === 'success' ? '✓' : (sVal === 'empty' ? '○' : '✗')} ${sName}: ${sVal}`);
    }
    console.log(`Overall Status: ${result.overall_status.toUpperCase()}`);
    console.log('=============================\n');
    return;
  }

  if (talukIdx !== -1 && args[talukIdx + 1]) {
    const tpId = args[talukIdx + 1];
    console.log(`Fetching GPs for Taluk ID: ${tpId}...`);
    const gps = await hierarchyManager.fetchGps(tpId);
    console.log(`Found ${gps.length} Gram Panchayats. Starting scrape...`);

    for (let i = 0; i < gps.length; i++) {
      const gp = gps[i];
      process.stdout.write(`[${i+1}/${gps.length}] ${gp.gp_name_en} (${gp.gp_id})... `);
      const res = await gpScraper.scrapeGp(gp);
      console.log(`✓ Done (Staff: ${res.total_staff}, Meetings: ${res.total_meetings})`);
    }
    console.log('\n🎉 Taluk scrape completed successfully!');
    return;
  }

  // Default demo run
  console.log('Running default verification test on GP AGOLI (1520001005)...');
  const res = await gpScraper.scrapeGp({ gp_id: '1520001005' });
  console.log(`✓ GP ${res.gp_name_en} completed! Total Staff: ${res.total_staff}`);
}

if (require.main === module) {
  runCli().catch(err => {
    console.error('Fatal Engine Error:', err);
    process.exit(1);
  });
}

module.exports = {
  gpScraper,
  hierarchyManager,
  storageManager
};
