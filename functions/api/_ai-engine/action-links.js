/**
 * Ask Karnata AI — Smart Action Links & Official Citations Generator
 */

export function generateSmartActionLinks(normalizedQ, intent) {
  const q = (normalizedQ || '').toLowerCase();
  const links = [];

  // 1. SIR & Voter Guide
  if (intent === 'SIR' || intent === 'VOTER' || q.includes('sir') || q.includes('ಮತದಾರ') || q.includes('voter')) {
    links.push({ title: "🔎 SIR Draft Roll ಹುಡುಕಿ", url: "/karnataka-sir-voter-roll.html", icon: "🗳️" });
  }

  // 2. Guarantee Schemes
  if (intent === 'GOVERNMENT_SCHEME' || q.includes('ಗ್ಯಾರಂಟಿ') || q.includes('ಗೃಹಲಕ್ಷ್ಮಿ') || q.includes('ಗೃಹಜ್ಯೋತಿ') || q.includes('ಯುವನಿಧಿ')) {
    links.push({ title: "📜 ಸರ್ಕಾರದ 5 ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು", url: "/guarantee-schemes.html", icon: "🌸" });
  }

  // 3. APMC & Mandi Rates
  if (intent === 'APMC_CROPS' || q.includes('apmc') || q.includes('ಬೆಳೆ') || q.includes('ಧಾರಣೆ') || q.includes('ಮಾರುಕಟ್ಟೆ')) {
    links.push({ title: "🌾 APMC ಮಾರುಕಟ್ಟೆ ಕೃಷಿ ದರಗಳು", url: "/apmc-prices.html", icon: "🌾" });
  }

  // 4. Gold & Fuel Rates
  if (intent === 'GOLD_SILVER' || q.includes('ಚಿನ್ನ') || q.includes('gold')) {
    links.push({ title: "🥇 ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ", url: "/gold-rate.html", icon: "🥇" });
  }
  if (intent === 'PETROL_DIESEL' || q.includes('ಪೆಟ್ರೋಲ್') || q.includes('diesel')) {
    links.push({ title: "⛽ ಇಂದಿನ ಪೆಟ್ರೋಲ್ & ಡೀಸೆಲ್ ದರ", url: "/petrol-price.html", icon: "⛽" });
  }

  // 5. Dams & Water Storage
  if (intent === 'DAM_WATER' || q.includes('dam') || q.includes('ಜಲಾಶಯ') || q.includes('krs') || q.includes('ತುಂಗಭದ್ರಾ')) {
    links.push({ title: "💧 13 ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ಮಟ್ಟ", url: "/dam-levels.html", icon: "💧" });
  }

  // 6. Officers & Administration
  if (intent === 'OFFICERS' || q.includes('ಅಧಿಕಾರಿ') || q.includes('dc') || q.includes('sp') || q.includes('ತಹಶೀಲ್ದಾರ್')) {
    links.push({ title: "👥 ಅಧಿಕಾರಿಗಳ ಡೈರೆಕ್ಟರಿ & ವರ್ಗಾವಣೆ", url: "/officers.html", icon: "👥" });
  }

  // 7. Representatives & Districts
  if (intent === 'MLAS_MPS' || q.includes('ಶಾಸಕ') || q.includes('ಸಂಸದ') || q.includes('ಕ್ಷೇತ್ರ')) {
    links.push({ title: "🏛️ 224 ಶಾಸಕರು & 28 ಸಂಸದರು", url: "/mla-mp.html", icon: "🏛️" });
  }

  if (intent === 'DISTRICT_TOURISM' || q.includes('ಜಿಲ್ಲೆ') || q.includes('district')) {
    links.push({ title: "🗺️ ಕರ್ನಾಟಕದ 31 ಜಿಲ್ಲೆಗಳ ದರ್ಶನ", url: "/districts.html", icon: "🗺️" });
  }

  // Default fallback links
  if (links.length === 0) {
    links.push({ title: "🔎 SIR Draft Roll ಪರಿಶೀಲಿಸಿ", url: "/karnataka-sir-voter-roll.html", icon: "🗳️" });
    links.push({ title: "📜 ಸರ್ಕಾರದ 5 ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು", url: "/guarantee-schemes.html", icon: "🌸" });
  }

  const seen = new Set();
  const deduped = [];
  for (const l of links) {
    if (!seen.has(l.url)) {
      seen.add(l.url);
      deduped.push(l);
    }
  }
  return deduped.slice(0, 3);
}

export function generateOfficialSources(intent) {
  const sources = [];

  if (intent === 'SIR' || intent === 'VOTER') {
    sources.push({
      name: "Election Commission of India (ECI)",
      url: "https://voters.eci.gov.in"
    });
    sources.push({
      name: "Chief Electoral Officer (CEO Karnataka)",
      url: "https://ceokarnataka.kar.nic.in"
    });
    sources.push({
      name: "Karnata.in SIR Knowledge Desk",
      url: "https://karnata.in/karnataka-sir-voter-roll.html"
    });
  } else if (intent === 'GOVERNMENT_SCHEME') {
    sources.push({
      name: "Seva Sindhu Karnataka",
      url: "https://sevasindhugs.karnataka.gov.in"
    });
    sources.push({
      name: "Karnataka State Portal",
      url: "https://karnataka.gov.in"
    });
  } else if (intent === 'APMC_CROPS') {
    sources.push({
      name: "Karnataka State Agricultural Marketing Board (KSAMB)",
      url: "https://krishimaratavahini.kar.nic.in"
    });
  } else {
    sources.push({
      name: "Government of Karnataka Official Portal",
      url: "https://karnataka.gov.in"
    });
    sources.push({
      name: "Karnata.in State Information Hub",
      url: "https://karnata.in"
    });
  }

  return sources;
}
