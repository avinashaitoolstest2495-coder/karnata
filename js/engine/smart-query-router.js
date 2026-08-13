/**
 * Karnata Smart Data Engine — Query Router
 * Rule-based, lightweight, zero-LLM intent classification and entity extractor.
 */

(function(exports) {
  const Resolver = typeof window !== 'undefined' && window.KarnataEntityResolver 
    ? window.KarnataEntityResolver 
    : require('./entity-resolver.js');

  function routeQuery(query) {
    const norm = Resolver.normalizeText(query);
    const districts = Resolver.resolveDistricts(norm);
    const primaryDistrict = districts.length > 0 ? districts[0] : null;
    const dam = Resolver.resolveDam(norm);
    const year = Resolver.extractYear(norm);

    const isExplicitComparison = norm.includes('ಹೋಲಿಸಿ') || norm.includes('ಹೋಲಿಕೆ') || norm.includes('compare') || norm.includes('vs') || norm.includes('difference');

    const isMultiData = (norm.includes('ರೈತರು') || norm.includes('ರೈತ') || norm.includes('ಗಮನಿಸಬೇಕಾದ') || norm.includes('ವಿಷಯಗಳು') || norm.includes('summary') || norm.includes('ಒಟ್ಟು ವಿವರ') || norm.includes('ಮಾಹಿತಿ')) && primaryDistrict;

    if (isMultiData && !norm.includes(' weather') && !norm.includes('apmc') && !norm.includes('mla') && !norm.includes('ಚುನಾವಣೆ')) {
      return {
        intent: 'MULTI_DATA',
        query,
        district: primaryDistrict,
        districts,
        dam,
        year
      };
    }

    if (isExplicitComparison) {
      return {
        intent: 'COMPARISON',
        query,
        comparisonType: norm.includes('petrol') || norm.includes('ಪೆಟ್ರೋಲ್') ? 'PETROL' : 'WEATHER',
        districts,
        dam,
        year
      };
    }

    // Gold / Silver Intent
    if (norm.includes('ಚಿನ್ನ') || norm.includes('gold') || norm.includes('22k') || norm.includes('24k') || norm.includes('18k') || norm.includes('ಬೆಳ್ಳಿ') || norm.includes('silver')) {
      return {
        intent: 'GOLD',
        query,
        district: primaryDistrict,
        targetMetal: norm.includes('ಬೆಳ್ಳಿ') || norm.includes('silver') ? 'silver' : norm.includes('24k') ? '24k' : norm.includes('18k') ? '18k' : '22k',
        isHistorical: norm.includes('30') || norm.includes('7') || norm.includes('trend') || norm.includes('ಹಿನ್ನಲೆ') || norm.includes('ಇತಿಹಾಸ') || norm.includes('days') || norm.includes('ದಿನ')
      };
    }

    // Petrol / Fuel Intent
    if (norm.includes('ಪೆಟ್ರೋಲ್') || norm.includes('petrol') || norm.includes('ಡೀಸೆಲ್') || norm.includes('diesel') || norm.includes('cng') || norm.includes('ಇಂಧನ') || norm.includes('fuel')) {
      return {
        intent: 'PETROL',
        query,
        targetFuel: norm.includes('diesel') || norm.includes('ಡೀಸೆಲ್') ? 'diesel' : 'petrol',
        district: primaryDistrict
      };
    }

    // Dam Intent
    if (dam || norm.includes('ಅಣೆಕಟ್ಟು') || norm.includes('dam') || norm.includes('ನೀರು') || norm.includes('ನೀರಿನ') || norm.includes('ಮಟ್ಟ') || norm.includes('storage') || norm.includes('tmc') || norm.includes('inflow') || norm.includes('outflow')) {
      return {
        intent: 'DAM',
        query,
        dam: dam || { key: 'krs', matched_alias: 'krs' },
        subType: norm.includes('inflow') ? 'inflow' : norm.includes('outflow') ? 'outflow' : norm.includes('percentage') || norm.includes('ಶೇಕಡಾ') ? 'percentage' : 'full',
        district: primaryDistrict
      };
    }

    // MLA or Election Intent with Year
    if (year) {
      return {
        intent: 'ELECTION',
        query,
        year,
        district: primaryDistrict
      };
    }

    // MP Intent
    if (/\bmp\b/i.test(norm) || norm.includes('ಸಂಸದ') || norm.includes('ಲೋಕಸಭೆ') || norm.includes('mp of')) {
      return {
        intent: 'MP',
        query,
        district: primaryDistrict
      };
    }

    // MLA Intent
    if (norm.includes('mla') || norm.includes('ಶಾಸಕ') || norm.includes('ಶಾಸಕರು') || norm.includes('ವಿಧಾನಸಭೆ')) {
      return {
        intent: 'MLA',
        query,
        district: primaryDistrict,
        year: year || null,
        isGenericPrompt: !primaryDistrict && (norm.includes('ನನ್ನ') || norm.includes('ನನ್ನ ಕ್ಷೇತ್ರದ') || norm.trim() === 'mla' || norm.trim() === 'ಶಾಸಕರು' || norm.trim() === 'ಶಾಸಕ' || norm.includes('constituency mla'))
      };
    }

    // Election Result / Winner Intent
    if (year || norm.includes('게ದ್ದರು') || norm.includes('ಗೆದ್ದಿದ್ದರು') || norm.includes('winner') || norm.includes('ಚುನಾವಣೆ') || norm.includes('election') || norm.includes('ವೋಟ್') || norm.includes('ಮತಗಳ') || norm.includes('margin') || norm.includes('historical election')) {
      return {
        intent: 'ELECTION',
        query,
        year: year || 2018,
        district: primaryDistrict
      };
    }

    // APMC Intent
    if (norm.includes('apmc') || norm.includes('ಮಾರುಕಟ್ಟೆ') || norm.includes('ಬೆಳೆ') || norm.includes('ತರಕಾರಿ') || norm.includes('ಸೊಪ್ಪು') || norm.includes('ಅಕ್ಕಿ') || norm.includes('ರಾಗಿ') || norm.includes('ಗೋಧಿ') || norm.includes('ಬೆಲ್ಲ') || norm.includes('ತೆಂಗಿನಕಾಯಿ') || norm.includes('ಟೊಮ್ಯಾಟೊ') || norm.includes('tomato') || norm.includes('commodity')) {
      return {
        intent: 'APMC',
        query,
        crop: norm.includes('ಟೊಮ್ಯಾಟೊ') || norm.includes('tomato') ? 'tomato' : null,
        district: primaryDistrict
      };
    }

    // Government Schemes Intent
    if (norm.includes('scheme') || norm.includes('ಯೋಜನೆ') || norm.includes('ಗ್ಯಾರಂಟಿ') || norm.includes('ರೈತರಿಗೆ ಯಾವ') || norm.includes('ವಿದ್ಯಾರ್ಥಿ ಯೋಜನೆ')) {
      return {
        intent: 'SCHEME',
        query,
        targetCat: norm.includes('ರೈತ') || norm.includes('farmer') ? 'farmers' : norm.includes('ವಿದ್ಯಾರ್ಥಿ') || norm.includes('student') ? 'students' : norm.includes('ಮಹಿಳೆ') || norm.includes('women') ? 'women' : 'all'
      };
    }

    // Weather Intent
    if (norm.includes('weather') || norm.includes('ಮಳೆ') || norm.includes('ಹವಾಮಾನ') || norm.includes('ಉಷ್ಣಾಂಶ') || norm.includes('temp') || norm.includes('temperature') || norm.includes('rain') || norm.includes('rainfall')) {
      return {
        intent: 'WEATHER',
        query,
        district: primaryDistrict
      };
    }

    // District List / Summary Intent
    if (norm.includes('ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿ') || norm.includes('ಜಿಲ್ಲೆಗಳ') || norm.includes('districts') || norm.includes('ಜಿಲ್ಲೆಗಳು') || norm.includes('ಕರ್ನಾಟಕದ ಜಿಲ್ಲೆ')) {
      return {
        intent: 'DISTRICTS',
        query
      };
    }

    if (norm.includes('calculator') || norm.includes('emi') || norm.includes('sip') || norm.includes('salary') || norm.includes('ಸಂಬಳ')) {
      return { intent: 'CALCULATOR', query };
    }

    if (norm.includes('news') || norm.includes('ಸುದ್ದಿ')) {
      return { intent: 'NEWS', query, district: primaryDistrict };
    }

    // Fallbacks
    if (dam) return { intent: 'DAM', query, dam, district: primaryDistrict };
    if (primaryDistrict) return { intent: 'MULTI_DATA', query, district: primaryDistrict };

    return {
      intent: 'UNKNOWN',
      query
    };
  }

  const Router = {
    routeQuery
  };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = Router;
  } else {
    exports.KarnataQueryRouter = Router;
  }
})(typeof window !== 'undefined' ? window : globalThis);
