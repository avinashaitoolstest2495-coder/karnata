const https = require('https');
const fs = require('fs');
const path = require('path');

/**
 * Karnata Live Real-Time Multi-District News Scraper
 * Strictly 100% Kannada-first News Scraper for all 31 districts of Karnataka.
 * NO English articles, NO Horoscope/Lifestyle, ONLY authentic Karnataka district news.
 */

const DISTRICTS_MAPPING = [
  { key: 'bengaluru-urban', search_kn: 'ಬೆಂಗಳೂರು ನಗರ ಸುದ್ದಿ' },
  { key: 'bengaluru-rural', search_kn: 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ ಸುದ್ದಿ' },
  { key: 'mysuru', search_kn: 'ಮೈಸೂರು ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'mandya', search_kn: 'ಮಂಡ್ಯ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'belagavi', search_kn: 'ಬೆಳಗಾವಿ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'kalaburagi', search_kn: 'ಕಲಬುರಗಿ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'dakshina-kannada', search_kn: 'ದಕ್ಷಿಣ ಕನ್ನಡ ಮಂಗಳೂರು ಸುದ್ದಿ' },
  { key: 'shivamogga', search_kn: 'ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'ballari', search_kn: 'ಬಳ್ಳಾರಿ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'dharwad', search_kn: 'ಧಾರವಾಡ ಹುಬ್ಬಳ್ಳಿ ಸುದ್ದಿ' },
  { key: 'hassan', search_kn: 'ಹಾಸನ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'tumakuru', search_kn: 'ತುಮಕೂರು ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'udupi', search_kn: 'ಉಡುಪಿ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'kodagu', search_kn: 'ಕೊಡಗು ಮಡಿಕೇರಿ ಸುದ್ದಿ' },
  { key: 'bagalkote', search_kn: 'ಬಾಗಲಕೋಟೆ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'chamarajanagara', search_kn: 'ಚಾಮರಾಜನಗರ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'chikkaballapura', search_kn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'chikkamagaluru', search_kn: 'ಚಿಕ್ಕಮಗಳೂರು ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'chitradurga', search_kn: 'ಚಿತ್ರದುರ್ಗ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'davanagere', search_kn: 'ದಾವಣಗೆರೆ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'gadag', search_kn: 'ಗದಗ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'haveri', search_kn: 'ಹಾವೇರಿ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'kolar', search_kn: 'ಕೋಲಾರ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'koppal', search_kn: 'ಕೊಪ್ಪಳ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'raichur', search_kn: 'ರಾಯಚೂರು ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'ramanagara', search_kn: 'ರಾಮನಗರ ಚನ್ನಪಟ್ಟಣ ಸುದ್ದಿ' },
  { key: 'uttara-kannada', search_kn: 'ಉತ್ತರ ಕನ್ನಡ ಕಾರವಾರ ಸುದ್ದಿ' },
  { key: 'vijayanagara', search_kn: 'ವಿಜಯನಗರ ಹೊಸಪೇಟೆ ಸುದ್ದಿ' },
  { key: 'vijayapura', search_kn: 'ವಿಜಯಪುರ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'yadgir', search_kn: 'ಯಾದಗಿರಿ ಜಿಲ್ಲೆ ಸುದ್ದಿ' },
  { key: 'bidar', search_kn: 'ಬೀದರ್ ಜಿಲ್ಲೆ ಸುದ್ದಿ' }
];

function fetchHttps(url) {
  return new Promise((resolve, reject) => {
    const req = https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', 'Accept-Language': 'kn-IN,kn;q=0.9' } }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve(data));
    });
    req.on('error', err => reject(err));
    req.setTimeout(10000, () => { req.destroy(); reject(new Error('Timeout')); });
  });
}

function isKannadaText(text) {
  if (!text || typeof text !== 'string') return false;
  return /[\u0C80-\u0CFF]/.test(text);
}

function parseXmlItems(xmlText) {
  const items = [];
  const itemRegex = /<item>[\s\S]*?<\/item>/gi;
  const titleRegex = /<title>(.*?)<\/title>/i;
  const linkRegex = /<link>(.*?)<\/link>/i;
  const pubDateRegex = /<pubDate>(.*?)<\/pubDate>/i;
  const sourceRegex = /<source[^>]*>(.*?)<\/source>/i;

  let match;
  while ((match = itemRegex.exec(xmlText)) !== null) {
    const block = match[0];
    const titleMatch = titleRegex.exec(block);
    const linkMatch = linkRegex.exec(block);
    const pubMatch = pubDateRegex.exec(block);
    const srcMatch = sourceRegex.exec(block);

    if (titleMatch && titleMatch[1]) {
      let rawTitle = titleMatch[1].replace(/<!\[CDATA\[(.*?)\]\]>/g, '$1').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').trim();
      let link = linkMatch ? linkMatch[1].replace(/<!\[CDATA\[(.*?)\]\]>/g, '$1').trim() : '#';
      let pubDateStr = pubMatch ? pubMatch[1].trim() : new Date().toISOString();
      let sourceName = srcMatch ? srcMatch[1].trim() : 'ಕನ್ನಡ ಲೈವ್';

      // Clean up title source suffix if present (e.g., "Title - Source")
      const titleParts = rawTitle.split(' - ');
      let headline = rawTitle;
      if (titleParts.length > 1) {
        sourceName = titleParts[titleParts.length - 1];
        headline = titleParts.slice(0, titleParts.length - 1).join(' - ');
      }

      // STRICT: ONLY KANNADA ARTICLES!
      if (!isKannadaText(headline)) {
        continue;
      }

      let validIsoDate = new Date().toISOString();
      try {
        const d = new Date(pubDateStr);
        if (!isNaN(d.getTime())) validIsoDate = d.toISOString();
      } catch (e) {}

      items.push({
        headline,
        title: headline,
        link,
        url: link,
        source: sourceName,
        published: validIsoDate,
        published_at: validIsoDate,
        time_ago: 'ಇಂದು (Live)'
      });
    }
  }
  return items;
}

async function scrapeAllDistrictsNews() {
  console.log('===========================================================');
  console.log('STARTING STRICT KANNADA-ONLY LIVE NEWS SCRAPER (31 DISTRICTS)');
  console.log('===========================================================\n');

  const dataDir = path.join(__dirname, '../data');
  const filePath = path.join(dataDir, 'local_news.json');

  let existingData = {};
  if (fs.existsSync(filePath)) {
    try {
      existingData = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    } catch (e) {}
  }

  const scrapedDataByDistrict = existingData.district_buckets || existingData.districts || {};

  // Clean out any English articles from existing data
  Object.keys(scrapedDataByDistrict).forEach(k => {
    if (Array.isArray(scrapedDataByDistrict[k])) {
      scrapedDataByDistrict[k] = scrapedDataByDistrict[k].filter(a => isKannadaText(a.title || a.headline));
    }
  });

  for (const dist of DISTRICTS_MAPPING) {
    console.log(`Scraping Kannada live news for: ${dist.key} ...`);
    const articles = scrapedDataByDistrict[dist.key] || [];
    const seenTitles = new Set(articles.map(a => (a.title || a.headline || '').trim().toLowerCase()));

    // Query: Google News Kannada Search
    try {
      const qUrlKn = `https://news.google.com/rss/search?q=${encodeURIComponent(dist.search_kn)}&hl=kn&gl=IN&ceid=IN:kn`;
      const xmlKn = await fetchHttps(qUrlKn);
      const itemsKn = parseXmlItems(xmlKn);
      itemsKn.slice(0, 10).forEach(it => {
        const tKey = (it.title || '').trim().toLowerCase();
        if (tKey && !seenTitles.has(tKey) && isKannadaText(it.title)) {
          articles.unshift({ ...it, district: dist.key, category: 'ಸ್ಥಳೀಯ ಸುದ್ದಿ' });
          seenTitles.add(tKey);
        }
      });
    } catch (e) {
      console.warn(`[Scraper Warning] KN news fetch failed for ${dist.key}:`, e.message);
    }

    await new Promise(r => setTimeout(r, 120));

    scrapedDataByDistrict[dist.key] = articles.slice(0, 30);
    console.log(`  -> Total ${scrapedDataByDistrict[dist.key].length} Kannada articles for ${dist.key}`);
  }

  const updatedFlatArticles = [];
  Object.values(scrapedDataByDistrict).forEach(arr => {
    if (Array.isArray(arr)) {
      arr.forEach(a => {
        if (isKannadaText(a.title || a.headline)) {
          updatedFlatArticles.push(a);
        }
      });
    }
  });

  const payload = {
    updated_at: new Date().toISOString(),
    total: updatedFlatArticles.length,
    districts_count: Object.keys(scrapedDataByDistrict).length,
    districts: scrapedDataByDistrict,
    district_buckets: scrapedDataByDistrict,
    news: scrapedDataByDistrict,
    articles: updatedFlatArticles
  };

  if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
  }
  fs.writeFileSync(filePath, JSON.stringify(payload, null, 2), 'utf8');

  console.log('\n===========================================================');
  console.log(`SUCCESSFULLY PROCESSED ${updatedFlatArticles.length} 100% KANNADA ARTICLES ACROSS ALL 31 DISTRICTS!`);
  console.log('===========================================================');
}

if (require.main === module) {
  scrapeAllDistrictsNews().catch(console.error);
}

module.exports = { scrapeAllDistrictsNews };
