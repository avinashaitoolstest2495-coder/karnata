/**
 * Karnata Smart Data Engine — Session Context & Follow-Up Resolver
 * Lightweight deterministic session memory without AI.
 */

(function(exports) {
  const Resolver = typeof window !== 'undefined' && window.KarnataEntityResolver 
    ? window.KarnataEntityResolver 
    : require('./entity-resolver.js');

  const sessionState = {
    district: null,
    commodity: null,
    dam: null,
    constituency: null,
    lastIntent: null,
    lastQuery: null
  };

  function updateContext(query, routeResult) {
    if (!routeResult) return;
    if (routeResult.district) sessionState.district = routeResult.district;
    if (routeResult.crop) sessionState.commodity = routeResult.crop;
    if (routeResult.dam) sessionState.dam = routeResult.dam;
    if (routeResult.intent) sessionState.lastIntent = routeResult.intent;
    sessionState.lastQuery = query;

    if (typeof sessionStorage !== 'undefined') {
      try { sessionStorage.setItem('nk_session_context', JSON.stringify(sessionState)); } catch(e) {}
    }
  }

  function getStoredContext() {
    if (typeof sessionStorage !== 'undefined') {
      try {
        const stored = JSON.parse(sessionStorage.getItem('nk_session_context') || '{}');
        if (stored.district) sessionState.district = stored.district;
        if (stored.commodity) sessionState.commodity = stored.commodity;
        if (stored.dam) sessionState.dam = stored.dam;
      } catch(e) {}
    }
    return sessionState;
  }

  function resolveFollowUp(query) {
    getStoredContext();
    const norm = Resolver.normalizeText(query);

    const is7Day = norm.includes('7 ದಿನ') || norm.includes('7 days') || norm.includes('7 day') || norm.includes('ಕಳೆದ 7') || norm.includes('7d');
    const is30Day = norm.includes('30 ದಿನ') || norm.includes('30 days') || norm.includes('30 day') || norm.includes('ಕಳೆದ 30') || norm.includes('30d');
    const isComp = norm.includes('ಹೋಲಿಸಿ') || norm.includes('ಹೋಲಿಕೆ') || norm.includes('compare') || norm.includes('vs');

    if (is7Day || is30Day) {
      return {
        isFollowUp: true,
        type: 'HISTORICAL',
        days: is30Day ? 30 : 7,
        district: sessionState.district || { key: 'mandya', name_en: 'Mandya' },
        commodity: sessionState.commodity || 'tomato'
      };
    }

    if (isComp) {
      const targetDist = Resolver.resolveDistrict(norm);
      return {
        isFollowUp: true,
        type: 'COMPARISON',
        distA: sessionState.district || { key: 'mandya', name_en: 'Mandya' },
        distB: targetDist || { key: 'mysuru', name_en: 'Mysuru' },
        commodity: sessionState.commodity || 'tomato',
        dam: sessionState.dam
      };
    }

    return null;
  }

  const SessionContext = {
    sessionState,
    updateContext,
    resolveFollowUp
  };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = SessionContext;
  } else {
    exports.KarnataSessionContext = SessionContext;
  }
})(typeof window !== 'undefined' ? window : globalThis);
