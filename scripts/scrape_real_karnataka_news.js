const https = require('https');
const fs = require('fs');
const path = require('path');

/**
 * Karnata Live Real-Time Multi-District News Scraper
 * Scrapes real live news articles for all 31 districts of Karnataka using Google News & TV9 Kannada RSS.
 */

const DISTRICTS_MAPPING = [
  { key: 'bengaluru-urban', search_en: 'Bengaluru Urban news', search_kn: 'ಬೆಂಗಳೂರು ಸುದ್ದಿ' },
  { key: 'bengaluru-rural', search_en: 'Bengaluru Rural news', search_kn: 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ ಸುದ್ದಿ' },
  { key: 'mysuru', search_en: 'Mysuru news', search_kn: 'ಮೈಸೂರು ಸುದ್ದಿ' },
  { key: 'mandya', search_en: 'Mandya news', search_kn: 'ಮಂಡ್ಯ ಸುದ್ದಿ' },
  { key: 'belagavi', search_en: 'Belagavi news', search_kn: 'ಬೆಳಗಾವಿ ಸುದ್ದಿ' },
  { key: 'kalaburagi', search_en: 'Kalaburagi news', search_kn: 'ಕಲಬುರಗಿ ಸುದ್ದಿ' },
  { key: 'dakshina-kannada', search_en: 'Mangaluru Dakshina Kannada news', search_kn: 'ದಕ್ಷಿಣ ಕನ್ನಡ ಮಂಗಳೂರು ಸುದ್ದಿ' },
  { key: 'shivamogga', search_en: 'Shivamogga news', search_kn: 'ಶಿವಮೊಗ್ಗ ಸುದ್ದಿ' },
  { key: 'ballari', search_en: 'Ballari news', search_kn: 'ಬಳ್ಳಾರಿ ಸುದ್ದಿ' },
  { key: 'dharwad', search_en: 'Dharwad Hubballi news', search_kn: 'ಧಾರವಾಡ ಹುಬ್ಬಳ್ಳಿ ಸುದ್ದಿ' },
  { key: 'hassan', search_en: 'Hassan news', search_kn: 'ಹಾಸನ ಸುದ್ದಿ' },
  { key: 'tumakuru', search_en: 'Tumakuru news', search_kn: 'ತುಮಕೂರು ಸುದ್ದಿ' },
  { key: 'udupi', search_en: 'Udupi news', search_kn: 'ಉಡುಪಿ ಸುದ್ದಿ' },
  { key: 'kodagu', search_en: 'Kodagu Coorg news', search_kn: 'ಕೊಡಗು ಮಡಿಕೇರಿ ಸುದ್ದಿ' },
  { key: 'bagalkote', search_en: 'Bagalkote news', search_kn: 'ಬಾಗಲಕೋಟೆ ಸುದ್ದಿ' },
  { key: 'chamarajanagara', search_en: 'Chamarajanagara news', search_kn: 'ಚಾಮರಾಜನಗರ ಸುದ್ದಿ' },
  { key: 'chikkaballapura', search_en: 'Chikkaballapura news', search_kn: 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ ಸುದ್ದಿ' },
  { key: 'chikkamagaluru', search_en: 'Chikkamagaluru news', search_kn: 'ಚಿಕ್ಕಮಗಳೂರು ಸುದ್ದಿ' },
  { key: 'chitradurga', search_en: 'Chitradurga news', search_kn: 'ಚಿತ್ರದುರ್ಗ ಸುದ್ದಿ' },
  { key: 'davanagere', search_en: 'Davanagere news', search_kn: 'ದಾವಣಗೆರೆ ಸುದ್ದಿ' },
  { key: 'gadag', search_en: 'Gadag news', search_kn: 'ಗದಗ ಸುದ್ದಿ' },
  { key: 'haveri', search_en: 'Haveri news', search_kn: 'ಹಾವೇರಿ ಸುದ್ದಿ' },
  { key: 'kolar', search_en: 'Kolar news', search_kn: 'ಕೋಲಾರ ಸುದ್ದಿ' },
  { key: 'koppal', search_en: 'Koppal news', search_kn: 'ಕೊಪ್ಪಳ ಸುದ್ದಿ' },
  { key: 'raichur', search_en: 'Raichur news', search_kn: 'ರಾಯಚೂರು ಸುದ್ದಿ' },
  { key: 'ramanagara', search_en: 'Ramanagara Channapatna news', search_kn: 'ರಾಮನಗರ ಸುದ್ದಿ' },
  { key: 'uttara-kannada', search_en: 'Uttara Kannada Karwar news', search_kn: 'ಉತ್ತರ ಕನ್ನಡ ಕಾರವಾರ ಸುದ್ದಿ' },
  { key: 'vijayanagara', search_en: 'Vijayanagara Hosapete news', search_kn: 'ವಿಜಯನಗರ ಹೊಸಪೇಟೆ ಸುದ್ದಿ' },
  { key: 'vijayapura', search_en: 'Vijayapura news', search_kn: 'ವಿಜಯಪುರ ಸುದ್ದಿ' },
  { key: 'yadgir', search_en: 'Yadgir news', search_kn: 'ಯಾದಗಿರಿ ಸುದ್ದಿ' },
  { key: 'bidar', search_en: 'Bidar news', search_kn: 'ಬೀದರ್ ಸುದ್ದಿ' }
];

function fetchHttps(url) {
  return new Promise((resolve, reject) => {
    const req = https.get(url, { headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' } }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => resolve(data));
    });
    req.on('error', err => reject(err));
    req.setTimeout(10000, () => { req.destroy(); reject(new Error('Timeout')); });
  });
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
      let sourceName = srcMatch ? srcMatch[1].trim() : 'Live News';

      // Clean up title source suffix if present (e.g., "Title - Source")
      const titleParts = rawTitle.split(' - ');
      let headline = rawTitle;
      if (titleParts.length > 1) {
        sourceName = titleParts[titleParts.length - 1];
        headline = titleParts.slice(0, titleParts.length - 1).join(' - ');
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
  console.log('STARTING REAL LIVE NEWS SCRAPER FOR ALL 31 KARNATAKA DISTRICTS');
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
  const allArticlesList = existingData.articles || [];

  for (const dist of DISTRICTS_MAPPING) {
    console.log(`Scraping real live news for: ${dist.key} ...`);
    const articles = scrapedDataByDistrict[dist.key] || [];
    const seenTitles = new Set(articles.map(a => (a.title || a.headline || '').trim().toLowerCase()));

    // Query 1: Google News Kannada Search
    try {
      const qUrlKn = `https://news.google.com/rss/search?q=${encodeURIComponent(dist.search_kn)}&hl=kn&gl=IN&ceid=IN:kn`;
      const xmlKn = await fetchHttps(qUrlKn);
      const itemsKn = parseXmlItems(xmlKn);
      itemsKn.slice(0, 5).forEach(it => {
        const tKey = (it.title || '').trim().toLowerCase();
        if (tKey && !seenTitles.has(tKey)) {
          articles.unshift({ ...it, district: dist.key, category: 'ಸ್ಥಳೀಯ ಸುದ್ದಿ' });
          seenTitles.add(tKey);
        }
      });
    } catch (e) {
      console.warn(`[Scraper Warning] KN news fetch failed for ${dist.key}:`, e.message);
    }

    // Query 2: Google News English Search
    try {
      const qUrlEn = `https://news.google.com/rss/search?q=${encodeURIComponent(dist.search_en)}&hl=en-IN&gl=IN&ceid=IN:en`;
      const xmlEn = await fetchHttps(qUrlEn);
      const itemsEn = parseXmlItems(xmlEn);
      itemsEn.slice(0, 5).forEach(it => {
        const tKey = (it.title || '').trim().toLowerCase();
        if (tKey && !seenTitles.has(tKey)) {
          articles.push({ ...it, district: dist.key, category: 'Real Live News (EN)' });
          seenTitles.add(tKey);
        }
      });
    } catch (e) {
      console.warn(`[Scraper Warning] EN news fetch failed for ${dist.key}:`, e.message);
    }

    // Delay slightly to prevent rate limit
    await new Promise(r => setTimeout(r, 150));

    scrapedDataByDistrict[dist.key] = articles.slice(0, 25);
    console.log(`  -> Total ${scrapedDataByDistrict[dist.key].length} live articles for ${dist.key}`);
  }

  const updatedFlatArticles = [];
  Object.values(scrapedDataByDistrict).forEach(arr => {
    if (Array.isArray(arr)) updatedFlatArticles.push(...arr);
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
  console.log(`SUCCESSFULLY SCRAPED ${updatedFlatArticles.length} REAL LIVE ARTICLES ACROSS ALL 31 DISTRICTS!`);
  console.log('Saved to data/local_news.json');
  console.log('===========================================================');
}

scrapeAllDistrictsNews();
