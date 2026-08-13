/**
 * Karnata Smart Data Engine — Multi-Data Engine
 * Combines weather, APMC, dam, and news datasets into structured multi-topic responses.
 */

(function(exports) {
  const DataProvider = typeof window !== 'undefined' && window.KarnataDataProvider 
    ? window.KarnataDataProvider 
    : require('./data-provider.js');

  const Calculator = typeof window !== 'undefined' && window.KarnataCalculator 
    ? window.KarnataCalculator 
    : require('./calculator-engine.js');

  async function getMultiDataSummary(districtObj) {
    const distKey = districtObj ? districtObj.key : 'mandya';
    const distNameEn = districtObj ? districtObj.name_en : 'Mandya';
    const distNameKn = distKey === 'mandya' ? 'ಮಂಡ್ಯ' : distKey === 'mysuru' ? 'ಮೈಸೂರು' : distKey === 'bengaluru' ? 'ಬೆಂಗಳೂರು' : distNameEn;

    const [weatherData, apmcData, damData, newsData] = await Promise.all([
      DataProvider.getWeatherData(),
      DataProvider.getApmcData(),
      DataProvider.getDamData(),
      DataProvider.getLocalNewsData()
    ]);

    // 1. Weather
    const distWeather = weatherData?.districts?.[distKey] || weatherData?.districts?.[distKey.replace(/_/g, '-')] || {};
    const curWeather = distWeather.current || { temp_c: 28, desc_kn: 'ಭಾಗಶಃ ಮೋಡ', rain_chance: 40 };

    // 2. APMC
    let apmcItems = [];
    if (apmcData && apmcData.items) {
      apmcItems = apmcData.items.filter(i => {
        const mkt = (i.market_en || i.market_kn || '').toLowerCase();
        return mkt.includes(distKey) || mkt.includes(distNameEn.toLowerCase());
      });
    }
    if (apmcItems.length === 0 && apmcData?.best_prices) {
      apmcItems = Object.values(apmcData.best_prices).slice(0, 4);
    }

    // 3. Relevant Dam
    let damKey = 'krs';
    if (distKey === 'vijayapura' || distKey === 'bagalkote') damKey = 'almatti';
    else if (distKey === 'shivamogga') damKey = 'bhadra';
    else if (distKey === 'ballari' || distKey === 'vijayanagara') damKey = 'tungabhadra';
    else if (distKey === 'hassan') damKey = 'hemavathi';

    const damObj = damData?.dams?.[damKey] || damData?.dams?.['k.r.sagara_dam'] || Object.values(damData?.dams || {})[0];
    const damMetrics = Calculator.calcDamMetrics(damObj);

    // 4. Local News
    let newsItems = [];
    if (newsData && Array.isArray(newsData.news)) {
      newsItems = newsData.news.filter(n => {
        const txt = ((n.title_kn || '') + ' ' + (n.title || '') + ' ' + (n.district || '')).toLowerCase();
        return txt.includes(distKey) || txt.includes(distNameEn.toLowerCase());
      }).slice(0, 3);

      if (newsItems.length === 0) {
        newsItems = newsData.news.slice(0, 3);
      }
    } else if (newsData && Array.isArray(newsData.articles)) {
      newsItems = newsData.articles.slice(0, 3);
    }

    return {
      district: distNameKn,
      districtEn: distNameEn,
      weather: curWeather,
      apmc: apmcItems.slice(0, 4),
      dam: damMetrics,
      news: newsItems,
      timestamp: new Date().toLocaleTimeString('kn-IN', { hour: '2-digit', minute: '2-digit' })
    };
  }

  const MultiDataEngine = {
    getMultiDataSummary
  };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = MultiDataEngine;
  } else {
    exports.KarnataMultiDataEngine = MultiDataEngine;
  }
})(typeof window !== 'undefined' ? window : globalThis);
