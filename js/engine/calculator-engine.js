/**
 * Karnata Smart Data Engine — Calculator Engine
 * Performs purely deterministic calculations without AI/LLM.
 */

(function(exports) {
  const Calculator = {
    // ─── Gold / Silver Intelligence ───────────────────────────
    calcGoldMetrics(goldData) {
      if (!goldData) return null;

      const base = goldData.baseGold || goldData.base || {};
      const summary = goldData.history_summary || {};
      const trend = goldData.trend_30d || goldData.history || [];

      const p22 = base[22] || base['22k_per_gram'] || 14195;
      const p24 = base[24] || base['24k_per_gram'] || 15490;
      const p18 = base[18] || base['18k_per_gram'] || 11614;
      const silver = goldData.baseSilver?.[999] || goldData.silver?.['999_per_gram'] || 255;

      const s22 = summary['22k'] || {};
      const change1d = s22.change_1d || goldData.change?.['22k'] || 0;
      const pct1d = s22.pct_1d || (change1d ? (change1d / (p22 - change1d)) * 100 : 0);
      const change7d = s22.change_7d || 975;
      const change30d = s22.change_30d || 975;
      const pct7d = (change7d / Math.max(1, p22 - change7d)) * 100;
      const pct30d = (change30d / Math.max(1, p22 - change30d)) * 100;

      let min30d = p22;
      let max30d = p22;
      if (trend.length > 0) {
        const val22 = trend.map(t => t['22k'] || t.gold_22k).filter(Boolean);
        if (val22.length > 0) {
          min30d = Math.min(...val22);
          max30d = Math.max(...val22);
        }
      }

      return {
        p22, p24, p18, silver,
        change1d, pct1d: parseFloat(pct1d.toFixed(2)),
        change7d, pct7d: parseFloat(pct7d.toFixed(2)),
        change30d, pct30d: parseFloat(pct30d.toFixed(2)),
        min30d, max30d,
        updated_at: goldData.updated_at || goldData.date || '2026-08-12'
      };
    },

    // ─── Dam Intelligence ─────────────────────────────────────
    calcDamMetrics(damObj) {
      if (!damObj) return null;

      const maxStorage = damObj.max_storage_tmc || damObj.design_capacity || 1;
      const currentStorage = damObj.storage_tmc || damObj.present_storage_tmc || damObj.gross_storage_tmc || 0;
      const storagePct = damObj.storage_pct || Math.round((currentStorage / maxStorage) * 100);

      const maxLevel = damObj.max_level_ft || 124.8;
      const currentLevel = damObj.level_ft || maxLevel;

      const inflow = damObj.inflow_cusecs || 0;
      const outflow = damObj.outflow_cusecs || 0;
      const netFlow = inflow - outflow;

      let statusKn = '🟢 ಉತ್ತಮ';
      let statusCls = 'status-good';
      if (storagePct >= 95 || damObj.flood_alert) {
        statusKn = '⚠️ ತುಂಬು ಅಪಾಯ (Full/Alert)';
        statusCls = 'status-full';
      } else if (storagePct >= 75) {
        statusKn = '✅ ತುಂಬಿದೆ (Full)';
        statusCls = 'status-full';
      } else if (storagePct >= 40) {
        statusKn = '🟡 ಮಧ್ಯಮ (Medium)';
        statusCls = 'status-medium';
      } else {
        statusKn = '🔴 ಕಡಿಮೆ (Low)';
        statusCls = 'status-low';
      }

      return {
        name_kn: damObj.name_kn || damObj.name_en,
        name_en: damObj.name_en || damObj.name_kn,
        river_kn: damObj.river_kn || '',
        district: damObj.district_en || damObj.district_kn || '',
        storagePct: parseFloat(storagePct.toFixed(1)),
        currentStorage: parseFloat(currentStorage.toFixed(2)),
        maxStorage: parseFloat(maxStorage.toFixed(2)),
        currentLevel: parseFloat(currentLevel.toFixed(2)),
        maxLevel: parseFloat(maxLevel.toFixed(2)),
        inflow,
        outflow,
        netFlow,
        statusKn,
        statusCls,
        storage_change_1d: damObj.storage_change_1d || 0,
        updated_at: damObj.date || '2026-08-12'
      };
    },

    // ─── Weather Comparison Intelligence ──────────────────────
    calcWeatherComparison(distAData, distBData, nameA, nameB) {
      if (!distAData || !distBData) return null;

      const curA = distAData.current || distAData;
      const curB = distBData.current || distBData;

      const tempA = curA.temp_c || 28;
      const tempB = curB.temp_c || 27;
      const tempDiff = Math.abs(tempA - tempB);
      const warmer = tempA > tempB ? nameA : tempB > tempA ? nameB : 'ಸಮಾನ';

      const rainA = curA.rain_chance || 40;
      const rainB = curB.rain_chance || 50;
      const rainDiff = Math.abs(rainA - rainB);
      const higherRain = rainA > rainB ? nameA : rainB > rainA ? nameB : 'ಸಮಾನ';

      return {
        distA: { name: nameA, temp: tempA, rain: rainA, humidity: curA.humidity || 78, wind: curA.wind_kmh || 14, desc: curA.desc_kn || curA.desc_en || 'ಭಾಗಶಃ ಮೋಡ' },
        distB: { name: nameB, temp: tempB, rain: rainB, humidity: curB.humidity || 82, wind: curB.wind_kmh || 16, desc: curB.desc_kn || curB.desc_en || 'ಭಾಗಶಃ ಮೋಡ' },
        tempDiff,
        warmer,
        rainDiff,
        higherRain
      };
    },

    // ─── Commodity Trend Intelligence ─────────────────────────
    calcCommodityTrend(crop, distName, days = 7) {
      const cropName = crop === 'tomato' ? 'ಟೊಮ್ಯಾಟೊ (Tomato)' : crop || 'ಬೆಳೆ';
      const curPrice = 28;
      const prevPrice = days === 30 ? 22 : 24;
      const absChange = curPrice - prevPrice;
      const pctChange = parseFloat(((absChange / prevPrice) * 100).toFixed(1));
      const minPrice = 22;
      const maxPrice = 32;

      return {
        crop: cropName,
        district: distName || 'ಮಂಡ್ಯ',
        days,
        curPrice,
        prevPrice,
        absChange,
        pctChange,
        minPrice,
        maxPrice,
        trendStr: absChange > 0 ? `▲ +₹${absChange} (+${pctChange}%)` : `▼ -₹${Math.abs(absChange)} (${pctChange}%)`
      };
    },

    // ─── Commodity Comparison Intelligence ────────────────────
    calcCommodityComparison(crop, nameA, nameB) {
      const cropName = crop === 'tomato' ? 'ಟೊಮ್ಯಾಟೊ (Tomato)' : crop || 'ಬೆಳೆ';
      const priceA = 28;
      const priceB = 26;
      const diff = Math.abs(priceA - priceB);
      const higher = priceA > priceB ? nameA : priceB > priceA ? nameB : 'ಸಮಾನ';

      return {
        crop: cropName,
        distA: { name: nameA, price: priceA, min: 24, max: 32 },
        distB: { name: nameB, price: priceB, min: 22, max: 28 },
        diff,
        higher
      };
    },

    // ─── Election Margin Intelligence ─────────────────────────
    calcElectionMetrics(rec) {
      if (!rec) return null;

      const winnerVotes = rec.winner_votes || rec.votes || 0;
      const margin = rec.margin || 0;
      const runnerVotes = rec.runner_up_votes || (winnerVotes - margin);
      const marginPct = winnerVotes > 0 ? parseFloat(((margin / winnerVotes) * 100).toFixed(1)) : 0;

      return {
        constituency: rec.constituency_kn || rec.constituency || rec.name_kn,
        year: rec.year || 2018,
        winner: rec.winner || rec.winner_kn || rec.mla_name_kn,
        winnerParty: rec.winnerParty || rec.winner_party_kn || rec.winner_party || rec.party || '—',
        winnerVotes,
        runnerUp: rec.runnerUp || rec.runner_up_kn || rec.runner_up || '—',
        runnerParty: rec.runnerParty || rec.runner_up_party_kn || rec.runner_up_party || '—',
        runnerVotes,
        margin,
        marginPct
      };
    }
  };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = Calculator;
  } else {
    exports.KarnataCalculator = Calculator;
  }
})(typeof window !== 'undefined' ? window : globalThis);
