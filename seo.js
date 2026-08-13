/**
 * Karnata — seo.js
 * Shared SEO + GEO (Generative Engine Optimization) module.
 *
 * What this does:
 *  1. Injects correct Schema.org JSON-LD per page (WebApplication,
 *     FAQPage, Dataset, BreadcrumbList, Organization)
 *  2. Updates Open Graph / Twitter card meta tags
 *  3. Sets canonical URL
 *  4. Injects live data into FAQ answers so AI engines get real numbers
 *     (e.g. "ಇಂದು 22K ಚಿನ್ನ ಬೆಲೆ ₹7,320/g — karnata.in")
 *
 * Why Schema.org matters for GEO:
 *  Google AI Overviews, ChatGPT Search, Perplexity all parse structured
 *  data to extract facts. A FAQPage schema with the correct answer to
 *  "KRS dam level today" makes it far more likely an AI cites us.
 *  Source: Google Search Central documentation (June 2026).
 *
 * Include in every HTML page:
 *   <script src="/seo.js"></script>
 */

const NKSeo = (() => {

  const SITE_NAME  = 'Karnata — Universe Of Karnataka';
  const SITE_URL   = 'https://karnata.in';
  const LOGO_URL   = 'https://karnata.in/icons/icon-512.png';

  // ─── Detect current page ────────────────────────────────
  function currentPage() {
    const path = window.location.pathname;
    if (path.includes('gold-rate'))        return 'gold';
    if (path.includes('dam-level'))        return 'dam';
    if (path.includes('civic-finder'))     return 'civic';
    if (path.includes('emi-calculator'))   return 'emi';
    if (path.includes('salary-calc'))      return 'salary';
    if (path.includes('more-tools'))       return 'tools';
    if (path.includes('weather'))          return 'weather';
    if (path.includes('news-explainer'))   return 'news';
    if (path.includes('status-checker'))   return 'status';
    if (path.includes('kannada-typing'))   return 'typing';
    if (path.includes('districts/'))       return 'district';
    return 'home';
  }

  // ─── Inject JSON-LD schema ──────────────────────────────
  function injectSchema(schema) {
    const existing = document.getElementById('nk-schema');
    if (existing) existing.remove();
    const script = document.createElement('script');
    script.type = 'application/ld+json';
    script.id   = 'nk-schema';
    script.textContent = JSON.stringify(schema);
    document.head.appendChild(script);
  }

  // ─── Organization schema (every page) ──────────────────
  function orgSchema() {
    return {
      '@context': 'https://schema.org',
      '@type': 'Organization',
      name: 'Karnata',
      alternateName: 'ಕರ್ನಾಟ',
      url: SITE_URL,
      logo: LOGO_URL,
      description: 'ಕರ್ನಾಟಕದ ಕನ್ನಡಿಗರಿಗಾಗಿ ಲೈವ್ ಮಾಹಿತಿ — ಚಿನ್ನ ಬೆಲೆ, ಅಣೆಕಟ್ಟು, MLA, ಹವಾಮಾನ, APMC',
      inLanguage: 'kn',
      areaServed: { '@type': 'State', name: 'Karnataka', containedIn: 'India' },
      sameAs: [`${SITE_URL}`],
    };
  }

  // ─── WebSite schema with Sitelinks Searchbox ───────────
  function websiteSchema() {
    return {
      '@context': 'https://schema.org',
      '@type': 'WebSite',
      name: SITE_NAME,
      url: SITE_URL,
      inLanguage: 'kn',
      potentialAction: {
        '@type': 'SearchAction',
        target: { '@type': 'EntryPoint', urlTemplate: `${SITE_URL}/civic-finder.html?q={search_term_string}` },
        'query-input': 'required name=search_term_string',
      },
    };
  }

  // ─── Gold rate page schema ──────────────────────────────
  function goldSchema(liveData) {
    const price22k = liveData?.base?.['22k_per_gram'] || '—';
    const price24k = liveData?.base?.['24k_per_gram'] || '—';
    const silver   = liveData?.silver?.['999_per_gram'] || '—';
    const date     = liveData?.date || new Date().toISOString().split('T')[0];

    return [
      {
        '@context': 'https://schema.org',
        '@type': 'Dataset',
        name: 'Karnataka Gold Silver Rates Today',
        alternateName: 'ಕರ್ನಾಟಕ ಚಿನ್ನ ಬೆಳ್ಳಿ ಬೆಲೆ ಇಂದು',
        description: `Today's gold and silver rates in Karnataka. 22K gold: ₹${price22k}/gram, 24K gold: ₹${price24k}/gram, Silver: ₹${silver}/gram. Updated daily from IBJA.`,
        url: `${SITE_URL}/gold-rate.html`,
        temporalCoverage: date,
        spatialCoverage: { '@type': 'State', name: 'Karnataka' },
        creator: { '@type': 'Organization', name: 'Karnata' },
        sources: ['IBJA — India Bullion and Jewellers Association'],
        inLanguage: 'kn',
        isAccessibleForFree: true,
      },
      {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        mainEntity: [
          {
            '@type': 'Question',
            name: 'ಇಂದು ಬೆಂಗಳೂರಿನಲ್ಲಿ 22K ಚಿನ್ನ ಬೆಲೆ ಎಷ್ಟು?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: `ಇಂದು (${date}) ಬೆಂಗಳೂರಿನಲ್ಲಿ 22K ಚಿನ್ನ ಬೆಲೆ ₹${price22k} ಪ್ರತಿ ಗ್ರಾಂ. ಮೂಲ: IBJA (India Bullion and Jewellers Association). Karnata ಪ್ರತಿ ದಿನ ಬೆಳಿಗ್ಗೆ 7 ಗಂಟೆಗೆ ನವೀಕರಿಸುತ್ತದೆ.`,
            },
          },
          {
            '@type': 'Question',
            name: 'Today gold rate in Karnataka 22K and 24K?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: `Today (${date}) gold rate in Karnataka: 22K gold is ₹${price22k} per gram, 24K gold is ₹${price24k} per gram. Silver is ₹${silver} per gram. Source: IBJA rates updated daily at 7 AM IST on Karnata.`,
            },
          },
          {
            '@type': 'Question',
            name: 'KRS dam ಅಣೆಕಟ್ಟು ನೀರಿನ ಮಟ್ಟ ಇಂದು ಎಷ್ಟು?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'KRS ಅಣೆಕಟ್ಟು ಮಟ್ಟ Karnata ನ dam-levels ಪುಟದಲ್ಲಿ ಪ್ರತಿ ದಿನ KSNDMC ಮತ್ತು Karnataka Water Resources Dept ನಿಂದ ನವೀಕರಿಸಲಾಗುತ್ತದೆ.',
            },
          },
          {
            '@type': 'Question',
            name: 'ಚಿನ್ನ ಬೆಲೆ ಪ್ರತಿ ದಿನ ಬದಲಾಗುತ್ತದೆಯೇ?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'ಹೌದು. IBJA (India Bullion and Jewellers Association) ಪ್ರತಿ ದಿನ ಬೆಳಿಗ್ಗೆ ದರ ನಿಗದಿಪಡಿಸುತ್ತದೆ. ಅಂತರರಾಷ್ಟ್ರೀಯ ಮಾರುಕಟ್ಟೆ, ರೂಪಾಯಿ-ಡಾಲರ್ ವಿನಿಮಯ ದರ, ಬೇಡಿಕೆ ಮೇಲೆ ಅವಲಂಬಿತ.',
            },
          },
          {
            '@type': 'Question',
            name: '22K vs 24K gold — ಯಾವ ಚಿನ್ನ ಒಳ್ಳೆಯದು?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: '24K ಶುದ್ಧ ಚಿನ್ನ (99.9%) — ಹೂಡಿಕೆಗೆ ಒಳ್ಳೆಯದು. 22K ಆಭರಣ ಚಿನ್ನ (91.6%) — ಗಟ್ಟಿ ಮತ್ತು ಆಭರಣಕ್ಕೆ ಸೂಕ್ತ. ಹೆಚ್ಚಿನ ಅಂಗಡಿಗಳಲ್ಲಿ 22K ಆಭರಣ ಮಾರಾಟ ಆಗುತ್ತದೆ.',
            },
          },
        ],
      },
    ];
  }

  // ─── Dam levels page schema ─────────────────────────────
  function damSchema(liveData) {
    const krs  = liveData?.dams?.krs;
    const date = liveData?.date || new Date().toISOString().split('T')[0];
    const krsPct = krs?.storage_pct || '—';

    return [
      {
        '@context': 'https://schema.org',
        '@type': 'Dataset',
        name: 'Karnataka Dam Water Levels Today',
        alternateName: 'ಕರ್ನಾಟಕ ಅಣೆಕಟ್ಟು ನೀರಿನ ಮಟ್ಟ ಇಂದು',
        description: `Live water levels for Karnataka dams including KRS, Kabini, Hemavathi, Tungabhadra. KRS dam today: ${krsPct}%. Source: Karnataka Water Resources Dept API.`,
        url: `${SITE_URL}/dam-levels.html`,
        temporalCoverage: date,
        spatialCoverage: { '@type': 'State', name: 'Karnataka' },
        creator: { '@type': 'Organization', name: 'Karnata' },
        isAccessibleForFree: true,
      },
      {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        mainEntity: [
          {
            '@type': 'Question',
            name: 'KRS dam water level today 2025',
            acceptedAnswer: {
              '@type': 'Answer',
              text: `KRS (Krishna Raja Sagara) dam water level today (${date}) is ${krsPct}% full. Maximum capacity: 49.5 TMC. Live data updated daily at 8 AM IST from Karnataka Water Resources Department. Check karnata.in/dam-levels.html for current level.`,
            },
          },
          {
            '@type': 'Question',
            name: 'ಇಂದು KRS ಅಣೆಕಟ್ಟು ನೀರಿನ ಮಟ್ಟ ಎಷ್ಟು?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: `ಇಂದು (${date}) KRS ಕೃಷ್ಣರಾಜ ಸಾಗರ ಅಣೆಕಟ್ಟು ${krsPct}% ತುಂಬಿದೆ. ಮಾಹಿತಿ: Karnataka Water Resources Dept. Karnata ಪ್ರತಿ ದಿನ 8 ಗಂಟೆಗೆ ನವೀಕರಿಸುತ್ತದೆ.`,
            },
          },
          {
            '@type': 'Question',
            name: 'Karnataka dam levels during monsoon 2025',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'Karnataka has 13 major dams including KRS, Kabini, Harangi, Hemavathi (Cauvery basin), Tungabhadra, Almatti (Krishna basin), Linganamakki, Supa (Sharavathi basin). Karnata tracks all dam levels daily from Karnataka Water Resources Dept API.',
            },
          },
          {
            '@type': 'Question',
            name: 'KRS ಅಣೆಕಟ್ಟು ಗರಿಷ್ಠ ಸಂಗ್ರಹ ಸಾಮರ್ಥ್ಯ ಎಷ್ಟು?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'KRS ಅಣೆಕಟ್ಟು (ಕೃಷ್ಣರಾಜ ಸಾಗರ) ಗರಿಷ್ಠ ಸಾಮರ್ಥ್ಯ 49.5 TMC. ಗರಿಷ್ಠ ಮಟ್ಟ 124.80 ಅಡಿ. ಮಂಡ್ಯ ಜಿಲ್ಲೆ, ಕಾವೇರಿ ನದಿ ಮೇಲೆ ನಿರ್ಮಿಸಲಾಗಿದೆ.',
            },
          },
        ],
      },
    ];
  }

  // ─── Civic finder page schema ───────────────────────────
  function civicSchema() {
    return {
      '@context': 'https://schema.org',
      '@type': 'FAQPage',
      mainEntity: [
        {
          '@type': 'Question',
          name: 'Who is the MLA of Gangavathi Karnataka?',
          acceptedAnswer: {
            '@type': 'Answer',
            text: 'Gangavathi is a taluk in Koppal district, Karnataka. The MLA for Gangavathi constituency can be found on Karnata civic finder tool at karnata.in/civic-finder.html — enter your village or ward name to get your current MLA, MP, DC, and SP details.',
          },
        },
        {
          '@type': 'Question',
          name: 'ನನ್ನ MLA ಯಾರು ಎಂದು ಹೇಗೆ ತಿಳಿಯಬೇಕು Karnataka?',
          acceptedAnswer: {
            '@type': 'Answer',
            text: 'Karnata civic finder ಉಪಕರಣದಲ್ಲಿ ನಿಮ್ಮ ಊರು ಅಥವಾ ವಾರ್ಡ್ ಹೆಸರು ಟೈಪ್ ಮಾಡಿ. ತಕ್ಷಣ ನಿಮ್ಮ MLA, MP, DC, SP ಮಾಹಿತಿ ಮತ್ತು ಸಂಪರ್ಕ ನಂಬರ್ ಸಿಗುತ್ತದೆ. karnata.in/civic-finder.html',
          },
        },
        {
          '@type': 'Question',
          name: 'How many assembly seats in Karnataka?',
          acceptedAnswer: {
            '@type': 'Answer',
            text: 'Karnataka has 224 assembly constituencies (Vidhan Sabha seats) and 28 Lok Sabha (parliament) seats across 31 districts. Each district has multiple MLAs. Find your MLA by entering your village name at karnata.in/civic-finder.html.',
          },
        },
        {
          '@type': 'Question',
          name: 'DC ಮತ್ತು SP ಸಂಪರ್ಕ ನಂಬರ್ ಕರ್ನಾಟಕ',
          acceptedAnswer: {
            '@type': 'Answer',
            text: 'Karnata ನ district pages ನಲ್ಲಿ ಎಲ್ಲ 31 ಜಿಲ್ಲೆಗಳ Deputy Commissioner (DC) ಮತ್ತು Superintendent of Police (SP) ಸಂಪರ್ಕ ನಂಬರ್ ಲಭ್ಯವಿದೆ. karnata.in/districts/ ನಲ್ಲಿ ನಿಮ್ಮ ಜಿಲ್ಲೆ ಆಯ್ಕೆ ಮಾಡಿ.',
          },
        },
      ],
    };
  }

  // ─── EMI Calculator schema ──────────────────────────────
  function emiSchema() {
    return [
      {
        '@context': 'https://schema.org',
        '@type': 'WebApplication',
        name: 'EMI Calculator Karnataka — ಕನ್ನಡ',
        alternateName: 'ಇಎಂಐ ಕ್ಯಾಲ್ಕುಲೇಟರ್',
        url: `${SITE_URL}/emi-calculator.html`,
        applicationCategory: 'FinanceApplication',
        inLanguage: 'kn',
        description: 'Free EMI calculator in Kannada for home loan, car loan, personal loan, education loan, gold loan. Calculate monthly EMI, total interest, amortization schedule.',
        offers: { '@type': 'Offer', price: '0', priceCurrency: 'INR' },
        featureList: ['Home Loan EMI', 'Car Loan EMI', 'Personal Loan EMI', 'Gold Loan EMI', 'Amortization Table'],
      },
      {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        mainEntity: [
          {
            '@type': 'Question',
            name: '₹50 ಲಕ್ಷ ಹೋಮ್ ಲೋನ್ 20 ವರ್ಷಕ್ಕೆ EMI ಎಷ್ಟು?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: '₹50 ಲಕ್ಷ ಹೋಮ್ ಲೋನ್, 8.5% ಬಡ್ಡಿ, 20 ವರ್ಷ (240 ತಿಂಗಳು) — EMI ಅಂದಾಜು ₹43,391/ತಿಂಗಳು. ಒಟ್ಟು ಬಡ್ಡಿ ₹54.14 ಲಕ್ಷ. Karnata EMI calculator ನಲ್ಲಿ ನಿಮ್ಮ ನಿಖರ EMI ಲೆಕ್ಕ ಹಾಕಿ.',
            },
          },
          {
            '@type': 'Question',
            name: 'How to calculate home loan EMI in Kannada?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'Use Karnata free EMI calculator at karnata.in/emi-calculator.html. Enter loan amount, interest rate, and tenure. The calculator shows monthly EMI, total interest payable, and a complete amortization schedule in Kannada.',
            },
          },
          {
            '@type': 'Question',
            name: 'SBI home loan interest rate 2025 Karnataka',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'SBI home loan interest rates for 2025 start from 8.50% p.a. for loans up to ₹30 lakhs. Rates vary based on CIBIL score and loan amount. Calculate your EMI at karnata.in/emi-calculator.html with current bank rates.',
            },
          },
        ],
      },
    ];
  }

  // ─── Salary Calculator schema ───────────────────────────
  function salarySchema() {
    return [
      {
        '@context': 'https://schema.org',
        '@type': 'WebApplication',
        name: 'Salary Calculator Karnataka 2025 — ಸಂಬಳ ಕ್ಯಾಲ್ಕುಲೇಟರ್',
        url: `${SITE_URL}/salary-calculator.html`,
        applicationCategory: 'FinanceApplication',
        inLanguage: 'kn',
        description: 'Karnataka take-home salary calculator 2025. Calculate in-hand salary after PF, TDS, ESI, professional tax. New vs old tax regime comparison in Kannada.',
        offers: { '@type': 'Offer', price: '0', priceCurrency: 'INR' },
      },
      {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        mainEntity: [
          {
            '@type': 'Question',
            name: '₹6 ಲಕ್ಷ CTC ಗೆ ಕೈಗೆ ಬರುವ ಸಂಬಳ ಎಷ್ಟು?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: '₹6,00,000 CTC ಗೆ ಅಂದಾಜು ₹45,000-48,000 ಪ್ರತಿ ತಿಂಗಳು ಕೈಗೆ ಬರುತ್ತದೆ (New Tax Regime, PF ಕಡಿತದ ನಂತರ). ₹7 ಲಕ್ಷ ವರೆಗೆ New Regime ನಲ್ಲಿ TDS ಶೂನ್ಯ. ನಿಮ್ಮ ನಿಖರ ಸಂಬಳ Karnata ನಲ್ಲಿ ಲೆಕ್ಕ ಹಾಕಿ.',
            },
          },
          {
            '@type': 'Question',
            name: 'New tax regime vs old tax regime 2025 which is better?',
            acceptedAnswer: {
              '@type': 'Answer',
              text: 'For income up to ₹7 lakh: New regime is better (zero tax via 87A rebate). For income above ₹7 lakh with 80C, HRA, 80D deductions: Compare both. Use Karnata salary calculator at karnata.in/salary-calculator.html to compare both regimes instantly.',
            },
          },
        ],
      },
    ];
  }

  // ─── Weather page schema ────────────────────────────────
  function weatherSchema() {
    return {
      '@context': 'https://schema.org',
      '@type': 'FAQPage',
      mainEntity: [
        {
          '@type': 'Question',
          name: 'Karnataka weather forecast today 2025',
          acceptedAnswer: {
            '@type': 'Answer',
            text: 'Karnata provides live weather forecasts for all 31 Karnataka districts using Open-Meteo API data (updated hourly). Includes 7-day forecast, rain probability, IMD alerts, and AQI for major cities. Visit karnata.in/weather.html for your district.',
          },
        },
        {
          '@type': 'Question',
          name: 'ಕರ್ನಾಟಕ ಮಳೆ ಎಚ್ಚರಿಕೆ ಇಂದು',
          acceptedAnswer: {
            '@type': 'Answer',
            text: 'Karnata ಮಳೆ ಎಚ್ಚರಿಕೆ IMD ಮತ್ತು Open-Meteo ಡೇಟಾ ಆಧಾರದ ಮೇಲೆ ನೀಡಲಾಗುತ್ತದೆ. 80%ಕ್ಕಿಂತ ಹೆಚ್ಚು ಮಳೆ ಸಾಧ್ಯತೆ ಇದ್ದರೆ ಕೆಂಪು ಎಚ್ಚರಿಕೆ. Push notification ಚಾಲು ಮಾಡಿದರೆ ಮಳೆ ಮೊದಲೇ ತಿಳಿಯುತ್ತದೆ.',
          },
        },
      ],
    };
  }

  // ─── Update Open Graph meta tags with live data ─────────
  function updateOGMeta({ title, description, url, imageAlt } = {}) {
    const setMeta = (prop, val) => {
      if (!val) return;
      let el = document.querySelector(`meta[property="${prop}"]`) ||
               document.querySelector(`meta[name="${prop}"]`);
      if (!el) { el = document.createElement('meta'); el.setAttribute('property', prop); document.head.appendChild(el); }
      el.setAttribute('content', val);
    };
    if (title)       setMeta('og:title', title);
    if (description) setMeta('og:description', description);
    if (url)         setMeta('og:url', `${SITE_URL}${url}`);
    setMeta('og:image', LOGO_URL);
    setMeta('og:image:alt', imageAlt || 'Karnata Karnataka');
    setMeta('og:site_name', SITE_NAME);
    setMeta('og:locale', 'kn_IN');
    setMeta('twitter:card', 'summary');
    setMeta('twitter:site', '@karnatain');
  }

  // ─── Set canonical URL ──────────────────────────────────
  function setCanonical(path) {
    let el = document.querySelector('link[rel="canonical"]');
    if (!el) { el = document.createElement('link'); el.rel = 'canonical'; document.head.appendChild(el); }
    el.href = `${SITE_URL}${path || window.location.pathname}`;
  }

  // ─── Main init ──────────────────────────────────────────
  async function init() {
    const page = currentPage();
    setCanonical();

    // Load live data for schema population where relevant
    let liveGold = null, liveDams = null;
    try {
      const [g, d] = await Promise.allSettled([
        fetch('/data/gold_rates.json').then(r => r.json()),
        fetch('/data/dam_levels.json').then(r => r.json()),
      ]);
      if (g.status === 'fulfilled') liveGold = g.value;
      if (d.status === 'fulfilled') liveDams = d.value;
    } catch(e) {}

    // Inject page-specific schema
    let schemas = [];
    switch (page) {
      case 'home':
        schemas = homeSchema();
        updateOGMeta({ title: 'Karnata — ಕರ್ನಾಟಕ ಲೈವ್ ಮಾಹಿತಿ | Karnata.in', url: '/' });
        break;
      case 'gold':
        schemas = [orgSchema(), ...goldSchema(liveGold)];
        updateOGMeta({
          title: `ಇಂದಿನ ಚಿನ್ನ ಬೆಲೆ — Today Karnataka Gold Rate ₹${liveGold?.base?.['22k_per_gram'] || '—'}/g | Karnata.in`,
          description: `ಇಂದು ಕರ್ನಾಟಕ ಚಿನ್ನ ಬೆಲೆ 22K: ₹${liveGold?.base?.['22k_per_gram'] || '—'}/g, 24K: ₹${liveGold?.base?.['24k_per_gram'] || '—'}/g. Karnataka Gold Rate Today.`,
          url: '/gold-rate.html',
        });
        injectSchema([breadcrumbSchema([{name:'ಮುಖಪುಟ',url:'/'},{name:'ಚಿನ್ನ ಬೆಲೆ',url:'/gold-rate.html'}]), ...schemas]);
        return;
      case 'petrol':
        schemas = [orgSchema(), websiteSchema()];
        updateOGMeta({
          title: 'ಇಂದಿನ ಪೆಟ್ರೋಲ್ ಡೀಸೆಲ್ ಬೆಲೆ — Today Karnataka Petrol Diesel Price | Karnata.in',
          description: 'ಕರ್ನಾಟಕ ಪೆಟ್ರೋಲ್ ಡೀಸೆಲ್ ಬೆಲೆ. Today petrol and diesel price in Bangalore, Mysore, Hubli. Live IOCL rates Karnataka.',
          url: '/petrol-price.html'
        });
        injectSchema([breadcrumbSchema([{name:'ಮುಖಪುಟ',url:'/'},{name:'ಪೆಟ್ರೋಲ್ ಬೆಲೆ',url:'/petrol-price.html'}]), ...schemas]);
        return;
      case 'dam':
        schemas = [orgSchema(), ...damSchema(liveDams)];
        updateOGMeta({
          title: `ಅಣೆಕಟ್ಟು ಮಟ್ಟ ಇಂದು — Karnataka Dam Water Levels Today | Karnata.in`,
          description: `ಕರ್ನಾಟಕ 13 ಅಣೆಕಟ್ಟುಗಳ ನೀರಿನ ಮಟ್ಟ ಇಂದು. KRS, Kabini, Almatti dam levels today. KSNDMC ಮಾಹಿತಿ.`,
          url: '/dam-levels.html',
        });
        injectSchema([breadcrumbSchema([{name:'ಮುಖಪುಟ',url:'/'},{name:'ಅಣೆಕಟ್ಟು ಮಟ್ಟ',url:'/dam-levels.html'}]), ...schemas]);
        return;
      case 'apmc':
        schemas = [orgSchema(), websiteSchema()];
        updateOGMeta({
          title: 'APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ — Karnataka APMC Mandi Rates Today | Karnata.in',
          description: 'ಕರ್ನಾಟಕ APMC ಮಾರುಕಟ್ಟೆ ಧಾರಣೆ. Today agricultural commodity prices across Karnataka APMC mandis.',
          url: '/apmc-prices.html'
        });
        injectSchema([breadcrumbSchema([{name:'ಮುಖಪುಟ',url:'/'},{name:'APMC ಧಾರಣೆ',url:'/apmc-prices.html'}]), ...schemas]);
        return;
      case 'civic':
        schemas = [orgSchema(), civicSchema()];
        updateOGMeta({ title: 'MLA MP DC SP ಹುಡುಕಿ — Karnataka Civic Representatives Finder | Karnata.in', url: '/civic-finder.html' });
        break;
      case 'emi':
        schemas = [orgSchema(), ...emiSchema()];
        updateOGMeta({ title: 'EMI ಕ್ಯಾಲ್ಕುಲೇಟರ್ — Karnataka Home Car Personal Loan EMI | Karnata.in', url: '/emi-calculator.html' });
        break;
      case 'sip':
        schemas = [orgSchema(), websiteSchema()];
        updateOGMeta({ title: 'SIP ಕ್ಯಾಲ್ಕುಲೇಟರ್ — Karnataka Mutual Fund SIP Growth Calculator | Karnata.in', url: '/sip-calculator.html' });
        break;
      case 'salary':
        schemas = [orgSchema(), ...salarySchema()];
        updateOGMeta({ title: 'ಸಂಬಳ ಕ್ಯಾಲ್ಕುಲೇಟರ್ 2026 — Take Home Salary Calculator Karnataka | Karnata.in', url: '/salary-calculator.html' });
        break;
      case 'scheme':
        schemas = [orgSchema(), websiteSchema()];
        updateOGMeta({ title: 'ಸರ್ಕಾರಿ ಯೋಜನೆ ಅರ್ಹತೆ — Karnataka Government Schemes Eligibility 2026 | Karnata.in', url: '/scheme-checker.html' });
        break;
      case 'weather':
        schemas = [orgSchema(), weatherSchema()];
        updateOGMeta({ title: 'ಕರ್ನಾಟಕ ಹವಾಮಾನ ಇಂದು — Karnataka Weather Forecast & Rain Alerts | Karnata.in', url: '/weather.html' });
        break;
      default:
        schemas = [orgSchema(), websiteSchema()];
    }

    injectSchema(schemas.length === 1 ? schemas[0] : schemas);
  }

  return { init, breadcrumbSchema, injectSchema };

})();

// Auto-init when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', NKSeo.init);
} else {
  NKSeo.init();
}
