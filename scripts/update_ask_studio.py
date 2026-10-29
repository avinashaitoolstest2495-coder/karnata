import re

with open("ask-ai-engine.js", "r", encoding="utf-8") as f:
    code = f.read().replace("\r\n", "\n")

# 1. Add all_schemes to db if not already present
if "all_schemes: null" not in code:
    code = code.replace(
        "    dams: null,\n    petrol: null\n  };",
        "    dams: null,\n    petrol: null,\n    all_schemes: null\n  };",
        1,
    )

# 2. Load myscheme_karnataka_all.json in loadAllDatasets
if "myscheme_karnataka_all.json" not in code:
    old_promise = """      const [rGold, rWeather, rNews, rLocalNews, rCmsNews, rApmc, rMp, rDams, rPetrol, rConst] = await Promise.all([
        fetch(`/data/gold_rates.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/weather.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/news_articles.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/local_news.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/cms_articles.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/apmc_prices.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/mp_authentic_history.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/dam_levels.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/petrol_rates.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/constituencies.json?v=${ts}`).then(r => r.json()).catch(() => null)
      ]);"""
    new_promise = """      const [rGold, rWeather, rNews, rLocalNews, rCmsNews, rApmc, rMp, rDams, rPetrol, rConst, rSchemes] = await Promise.all([
        fetch(`/data/gold_rates.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/weather.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/news_articles.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/local_news.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/cms_articles.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/apmc_prices.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/mp_authentic_history.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/dam_levels.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/petrol_rates.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/constituencies.json?v=${ts}`).then(r => r.json()).catch(() => null),
        fetch(`/data/myscheme_karnataka_all.json?v=${ts}`).then(r => r.json()).catch(() => null)
      ]);"""
    assert old_promise in code, "old_promise not found"
    code = code.replace(old_promise, new_promise, 1)
    code = code.replace(
        "      db.mp_history = rMp;\n",
        "      db.mp_history = rMp;\n      db.all_schemes = (rSchemes && Array.isArray(rSchemes.schemes)) ? rSchemes.schemes : [];\n",
        1,
    )

# 3. Route scheme & eligibility queries at top of query(userQuery)
if "answerSchemeEligibilityQuery(q)" not in code:
    old_query_head = """  function query(userQuery) {
    const q = (userQuery || '').toLowerCase().trim();
    if (!q) return null;"""
    new_query_head = """  function query(userQuery) {
    const q = (userQuery || '').toLowerCase().trim();
    if (!q) return null;

    // 0. 885+ GOVERNMENT SCHEMES & PERSONALIZED ELIGIBILITY CHECKER
    const schemeAns = answerSchemeEligibilityQuery(q);
    if (schemeAns) return schemeAns;"""
    assert old_query_head in code, "old_query_head not found"
    code = code.replace(old_query_head, new_query_head, 1)

# 4. Add Scheme Eligibility Engine functions before return { init: loadAllDatasets, query: query }
scheme_engine_js = r"""
  // --- 0. 885+ GOVERNMENT SCHEMES & INTERACTIVE ELIGIBILITY ENGINE ---
  function getOfficialSchemeWebsite(s) {
    if (!s) return 'https://sevasindhu.karnataka.gov.in';
    if (s.apply_link && s.apply_link.startsWith('http') && !s.apply_link.includes('myscheme.gov.in')) {
      return s.apply_link;
    }
    const min = ((s.ministry_en || '') + ' ' + (s.categories || []).join(' ')).toLowerCase();
    if (s.level === 'State') {
      if (min.includes('agriculture') || min.includes('horticulture')) return 'https://raitamitra.karnataka.gov.in';
      if (min.includes('education') || s.isStudent) return 'https://ssp.postmatric.karnataka.gov.in';
      if (min.includes('labour') || min.includes('construction')) return 'https://karbwwb.karnataka.gov.in';
      if (min.includes('finance') || s.slug === 'iss') return 'https://ksfc.karnataka.gov.in';
      if (min.includes('housing')) return 'https://ashraya.karnataka.gov.in';
      return 'https://sevasindhu.karnataka.gov.in';
    } else {
      if (min.includes('agriculture') || min.includes('farmers')) return 'https://agricoop.gov.in';
      if (min.includes('science') || min.includes('technology')) return 'https://onlinedst.gov.in';
      if (min.includes('msme') || min.includes('entrepreneur')) return 'https://msme.gov.in';
      if (min.includes('education') || s.isStudent) return 'https://scholarships.gov.in';
      if (min.includes('labour')) return 'https://eshram.gov.in';
      if (min.includes('social justice')) return 'https://socialjustice.gov.in';
      if (min.includes('women')) return 'https://wcd.nic.in';
      if (min.includes('health')) return 'https://pmjay.gov.in';
      return 'https://www.india.gov.in/my-government/schemes';
    }
  }

  function getSchemeBySlug(slug) {
    const schemes = db.all_schemes || [];
    return schemes.find(s => s.slug === slug || s.id === slug || s.curated_id === slug) || null;
  }

  function buildSchemeQuestions(s) {
    if (!s) return [];
    const questions = [];
    const cats = (s.categories || []).join(' ').toLowerCase();
    const minText = ((s.ministry_en || '') + ' ' + (s.ministry_kn || '')).toLowerCase();
    const fullDescKn = (s.description_kn || s.benefits_kn || s.description_en || '').trim();

    const isAgri = cats.includes('agriculture') || minText.includes('agriculture') || minText.includes('ಕೃಷಿ') || minText.includes('ತೋಟಗಾರಿಕೆ') || (s.occupations || []).includes('Farmer');
    const isEdu = cats.includes('education') || s.isStudent || (s.occupations || []).includes('Student');
    const isBiz = cats.includes('business') || minText.includes('msme') || minText.includes('ಕೈಗಾರಿಕೆ') || minText.includes('finance');
    const isLabour = cats.includes('skills') || minText.includes('labour') || minText.includes('ಕಾರ್ಮಿಕ');
    const isWomen = cats.includes('women') || ((s.genders || []).includes('Female') && !(s.genders || []).includes('Male'));
    const isHousing = cats.includes('housing') || minText.includes('ವಸತಿ');

    // Q1: Residency
    questions.push({
      id: 'q1',
      category: '1. ವಾಸಸ್ಥಳ ಅರ್ಹತೆ (Residency)',
      prompt: s.level === 'State'
        ? 'ನೀವು ಕರ್ನಾಟಕ ರಾಜ್ಯದ ಖಾಯಂ ನಿವಾಸಿಯಾಗಿದ್ದು ಆಧಾರ್ / ವಾಸಸ್ಥಳ ಪ್ರಮಾಣಪತ್ರ ಹೊಂದಿದ್ದೀರಾ?'
        : 'ನೀವು ಭಾರತದ ಪ್ರಜೆಯಾಗಿದ್ದು ಪ್ರಸ್ತುತ ಕರ್ನಾಟಕದಲ್ಲಿ ವಾಸಿಸುತ್ತಿದ್ದೀರಾ?',
      expected: 'Yes'
    });

    // Q2: Age
    const ab = s.ageBrackets || [];
    let agePrompt = 'ಅರ್ಜಿದಾರರು ಈ ಯೋಜನೆಗೆ ನಿಗದಿಪಡಿಸಿದ ವಯೋಮಿತಿ ಮಾನದಂಡವನ್ನು ಪೂರೈಸುತ್ತಾರೆಯೇ?';
    if (ab.length > 0 && ab.length < 10) {
      const minA = Math.min(...ab);
      const maxA = Math.max(...ab);
      agePrompt = minA >= 60
        ? 'ಅರ್ಜಿದಾರರ ವಯಸ್ಸು 60 ವರ್ಷ ಅಥವಾ ಅದಕ್ಕಿಂತ ಹೆಚ್ಚಿದೆಯೇ (ಹಿರಿಯ ನಾಗರಿಕರು)?'
        : `ಅರ್ಜಿದಾರರ ವಯಸ್ಸು ${minA === 0 ? '1' : minA} ರಿಂದ ${maxA + 9} ವರ್ಷಗಳ ವ್ಯಾಪ್ತಿಯಲ್ಲಿದೆಯೇ?`;
    } else if (isEdu) {
      agePrompt = 'ಅರ್ಜಿದಾರರು ಪ್ರಸ್ತುತ ಶಾಲೆ/ಕಾಲೇಜು/ವಿಶ್ವವಿದ್ಯಾಲಯದಲ್ಲಿ ವ್ಯಾಸಂಗ ಮಾಡುತ್ತಿರುವ ವಿದ್ಯಾರ್ಥಿ ವಯೋಮಿತಿಯಲ್ಲಿದ್ದಾರೆಯೇ?';
    } else if (isBiz || isLabour) {
      agePrompt = 'ಅರ್ಜಿದಾರರು 18 ವರ್ಷ ಪೂರೈಸಿದ ವಯಸ್ಕ ನಾಗರಿಕರಾಗಿದ್ದಾರೆಯೇ?';
    }
    questions.push({
      id: 'q2',
      category: '2. ವಯೋಮಿತಿ ಅರ್ಹತೆ (Age Criteria)',
      prompt: agePrompt,
      expected: 'Yes'
    });

    // Q3: Occupation / Target Group
    let occPrompt = 'ನೀವು ಈ ಯೋಜನೆಯ ಉದ್ದೇಶಿತ ಫಲಾನುಭವಿ ವರ್ಗಕ್ಕೆ ಸೇರಿದವರಾಗಿದ್ದೀರಾ?';
    if (isAgri) occPrompt = 'ನೀವು ಕೃಷಿ ಭೂಮಿ ಹೊಂದಿರುವ ರೈತರಾಗಿದ್ದು, FRUITS ಗುರುತಿನ ಸಂಖ್ಯೆ (FID) ಮತ್ತು ಪಹಣಿ (RTC) ಹೊಂದಿದ್ದೀರಾ?';
    else if (isEdu) occPrompt = 'ನೀವು ಸರ್ಕಾರದಿಂದ ಮಾನ್ಯತೆ ಪಡೆದ ಶಿಕ್ಷಣ ಸಂಸ್ಥೆಯಲ್ಲಿ ವ್ಯಾಸಂಗ ಮಾಡುತ್ತಿದ್ದು, ಹಿಂದಿನ ಪರೀಕ್ಷೆಯಲ್ಲಿ ಉತ್ತೀರ್ಣರಾಗಿದ್ದೀರಾ?';
    else if (isWomen) occPrompt = 'ಅರ್ಜಿದಾರರು ಮಹಿಳೆ / ಹೆಣ್ಣುಮಗುವಾಗಿದ್ದು, ಈ ಯೋಜನೆಯ ಕುಟುಂಬ ಮಾನದಂಡವನ್ನು ಪೂರೈಸುತ್ತಾರೆಯೇ?';
    else if (isBiz) occPrompt = 'ನೀವು ಹೊಸ ಉದ್ಯಮ/ವ್ಯಾಪಾರ ಪ್ರಾರಂಭಿಸಲು ಅಥವಾ ಅಸ್ತಿತ್ವದಲ್ಲಿರುವ ಘಟಕವನ್ನು ವಿಸ್ತರಿಸಲು ಅಧಿಕೃತ ಯೋಜನೆ ಹೊಂದಿದ್ದೀರಾ?';
    else if (isLabour) occPrompt = 'ನೀವು ಕಟ್ಟಡ ಕಾರ್ಮಿಕರು, ಕುಶಲಕರ್ಮಿಗಳು, ನೇಕಾರರು ಅಥವಾ ಅಸಂಘಟಿತ ವಲಯದ ಕಾರ್ಮಿಕರಾಗಿ ನೋಂದಾಯಿಸಿಕೊಂಡಿದ್ದೀರಾ?';
    else if (isHousing) occPrompt = 'ನಿಮ್ಮ ಕುಟುಂಬಕ್ಕೆ ಸ್ವಂತ ಪಕ್ಕಾ ಮನೆ ಇಲ್ಲದೇ ವಸತಿ ಸಹಾಯಧನಕ್ಕಾಗಿ ಅರ್ಜಿ ಸಲ್ಲಿಸುತ್ತಿದ್ದೀರಾ?';
    questions.push({
      id: 'q3',
      category: '3. ವೃತ್ತಿ / ಫಲಾನುಭವಿ ವರ್ಗ (Beneficiary Category)',
      prompt: occPrompt,
      expected: 'Yes'
    });

    // Q4 & Q5: Specific Scheme Eligibility Points
    const eligLines = [];
    if (Array.isArray(s.eligibility_text_kn)) {
      s.eligibility_text_kn.forEach(x => { if (x && x.length > 8) eligLines.push(x); });
    } else if (typeof s.eligibility_text_kn === 'string' && s.eligibility_text_kn.trim()) {
      s.eligibility_text_kn.split(/\n|•|(?<=[.।])\s+/).forEach(x => {
        const clean = x.trim();
        if (clean.length > 8) eligLines.push(clean);
      });
    }
    if (eligLines.length === 0 && fullDescKn) {
      fullDescKn.split(/(?<=[.।])\s+/).forEach(x => {
        const clean = x.trim();
        if (clean.length > 10) eligLines.push(clean);
      });
    }

    questions.push({
      id: 'q4',
      category: '4. ಯೋಜನೆಯ ವಿಶೇಷ ನಿಯಮ 1 (Scheme Condition 1)',
      prompt: eligLines[0]
        ? `ನೀವು ಈ ಅರ್ಹತಾ ನಿಯಮವನ್ನು ಪೂರೈಸುತ್ತೀರಾ: "${eligLines[0]}"?`
        : 'ನೀವು ಈ ಯೋಜನೆಯ ಇಲಾಖಾ ಮಾರ್ಗಸೂಚಿಯ ಮೊದಲನೇ ಮುಖ್ಯ ಷರತ್ತನ್ನು ಪೂರೈಸುತ್ತೀರಾ?',
      expected: 'Yes'
    });

    questions.push({
      id: 'q5',
      category: '5. ಯೋಜನೆಯ ವಿಶೇಷ ನಿಯಮ 2 (Scheme Condition 2)',
      prompt: eligLines[1]
        ? `ನೀವು ಈ ನಿಯಮವನ್ನೂ ಪೂರೈಸುತ್ತೀರಾ: "${eligLines[1]}"?`
        : 'ಅರ್ಜಿದಾರರು ಸಂಬಂಧಪಟ್ಟ ಇಲಾಖೆಯ ನೋಂದಣಿ ಮತ್ತು ಕನಿಷ್ಠ ಅರ್ಹತಾ ಮಾನದಂಡವನ್ನು ಹೊಂದಿದ್ದಾರೆಯೇ?',
      expected: 'Yes'
    });

    // Q6: Caste & Income / BPL
    const castes = (s.castes || []).filter(x => x !== 'All');
    let incomePrompt = 'ನಿಮ್ಮ ಕುಟುಂಬದ ವಾರ್ಷಿಕ ಆದಾಯ ಮತ್ತು ವರ್ಗವು ಈ ಯೋಜನೆಯ ಮಿತಿಯೊಳಗಿದೆಯೇ?';
    if (s.isBpl && castes.length > 0) {
      incomePrompt = `ನೀವು ${castes.join(' / ')} ವರ್ಗಕ್ಕೆ ಸೇರಿದ್ದು, BPL / ಅಂತ್ಯೋದಯ ಪಡಿತರ ಚೀಟಿ ಹೊಂದಿದ್ದೀರಾ?`;
    } else if (s.isBpl) {
      incomePrompt = 'ನಿಮ್ಮ ಕುಟುಂಬವು BPL (ಬಡತನ ರೇಖೆಗಿಂತ ಕೆಳಗಿನ) ಅಥವಾ ಅಂತ್ಯೋದಯ ಪಡಿತರ ಚೀಟಿ ಹೊಂದಿದೆಯೇ?';
    } else if (castes.length > 0) {
      incomePrompt = `ನೀವು ${castes.join(' / ')} ಸಮುದಾಯಕ್ಕೆ ಸೇರಿದ್ದು, ಅಧಿಕೃತ ಜಾತಿ ಪ್ರಮಾಣಪತ್ರ (RD ಸಂಖ್ಯೆ) ಹೊಂದಿದ್ದೀರಾ?`;
    }
    questions.push({
      id: 'q6',
      category: '6. ಜಾತಿ ಮತ್ತು ಆದಾಯ / ಪಡಿತರ ಚೀಟಿ (Caste & Income)',
      prompt: incomePrompt,
      expected: 'Yes'
    });

    // Q7: Non-duplication & Exclusion Check
    questions.push({
      id: 'q7',
      category: '7. ಅನರ್ಹತೆ ಮತ್ತು ದ್ವಿಗುಣ ಸೌಲಭ್ಯ ಪರಿಶೀಲನೆ (Exclusion Check)',
      prompt: 'ನೀವು ಇದೇ ಉದ್ದೇಶಕ್ಕಾಗಿ ರಾಜ್ಯ ಅಥವಾ ಕೇಂದ್ರ ಸರ್ಕಾರದ ಬೇರೆ ಯಾವುದೇ ಯೋಜನೆಯಡಿ ಈಗಾಗಲೇ ದ್ವಿಗುಣ ಸಹಾಯಧನ ಪಡೆದಿಲ್ಲ ತಾನೇ (ಮತ್ತು ಅನರ್ಹತೆ ವ್ಯಾಪ್ತಿಗೆ ಬರುವುದಿಲ್ಲ ತಾನೇ)?',
      expected: 'Yes'
    });

    // Q8: Documents & Aadhaar DBT Bank Account
    questions.push({
      id: 'q8',
      category: '8. ದಾಖಲೆಗಳು ಮತ್ತು ಆಧಾರ್-ಬ್ಯಾಂಕ್ ಜೋಡಣೆ (Documents & DBT)',
      prompt: 'ನಿಮ್ಮ ಬಳಿ ಆಧಾರ್ ಕಾರ್ಡ್, ಆಧಾರ್ ಜೋಡಣೆಯಾದ ಬ್ಯಾಂಕ್ ಖಾತೆ (NPCI DBT Active), ಹಾಗೂ ಕಂದಾಯ ಇಲಾಖೆಯ ಜಾತಿ/ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ ಸಿದ್ಧವಿದೆಯೇ?',
      expected: 'Yes'
    });

    return questions;
  }

  function findEligibleSchemes(profile = {}) {
    const schemes = db.all_schemes || [];
    const age = profile.age !== undefined && profile.age !== '' ? parseInt(profile.age, 10) : null;
    const gender = profile.gender || '';
    const role = profile.role || '';
    const caste = profile.caste || '';
    const bpl = profile.bpl || 'no';
    const residence = profile.residence || '';
    const special = profile.special || '';
    const level = profile.level || 'all';

    let matched = schemes.filter(s => {
      if (level !== 'all' && s.level !== level) return false;

      if (gender) {
        const g = s.genders || [];
        if (g.length > 0 && !g.includes('All') && !g.includes(gender)) return false;
      }

      if (age !== null && !isNaN(age)) {
        const ab = s.ageBrackets || [];
        if (ab.length > 0 && !ab.includes(age)) return false;
      }

      if (caste) {
        const c = s.castes || [];
        if (c.length > 0 && !c.includes('All') && !c.includes(caste)) return false;
      }

      if (residence) {
        const r = s.residences || [];
        if (r.length > 0 && !r.includes('Both') && !r.includes(residence)) return false;
      }

      if (bpl === 'no' && s.isBpl) {
        return false;
      }

      if (role === 'farmer') {
        const isAg = (s.categories || []).includes('Agriculture,Rural & Environment') || (s.occupations || []).includes('Farmer');
        if (!isAg && !s.is_guarantee) return false;
      } else if (role === 'student') {
        const isSt = s.isStudent || (s.categories || []).includes('Education & Learning') || (s.occupations || []).includes('Student');
        if (!isSt) return false;
      } else if (role === 'woman') {
        const isW = (s.categories || []).includes('Women and Child') || (s.genders || []).includes('Female') || s.is_guarantee;
        if (!isW) return false;
      } else if (role === 'business') {
        const isBz = (s.categories || []).includes('Business & Entrepreneurship') || (s.categories || []).includes('Banking,Financial Services and Insurance');
        if (!isBz) return false;
      } else if (role === 'worker') {
        const isWk = (s.categories || []).includes('Skills & Employment') || (s.occupations || []).some(o => o.includes('Worker') || o.includes('Artisan') || o.includes('Karamchari'));
        if (!isWk) return false;
      } else if (role === 'unemployed') {
        const isUn = (s.employmentStatuses || []).includes('Unemployed') || (s.categories || []).includes('Skills & Employment') || s.slug === 'yuva-nidhi';
        if (!isUn) return false;
      } else if (role === 'senior') {
        const ab = s.ageBrackets || [];
        if (ab.length > 0 && !ab.includes(60)) return false;
      }

      if (special === 'disability' && !s.disability) return false;
      if (special === 'minority' && !s.minority) return false;
      if (special === 'widow' && !(s.maritalStatuses || []).includes('Widowed')) return false;
      if (special === 'exservice' && !(s.occupations || []).includes('Ex Servicemen')) return false;

      return true;
    });

    matched.sort((a, b) => {
      const ga = a.is_guarantee ? 0 : 1;
      const gb = b.is_guarantee ? 0 : 1;
      if (ga !== gb) return ga - gb;
      const sa = a.level === 'State' ? 0 : 1;
      const sb = b.level === 'State' ? 0 : 1;
      if (sa !== sb) return sa - sb;
      return (a.priority ?? 4) - (b.priority ?? 4);
    });

    return matched;
  }

  function answerSchemeEligibilityQuery(q) {
    const schemes = db.all_schemes || [];
    if (!schemes || schemes.length === 0) return null;

    // 1. Check if user is asking about a specific scheme by name or slug
    const isGeneralDiscovery = (
      q.includes('ನನಗೆ ಯಾವ') ||
      q.includes('ಯಾವ ಯೋಜನೆಗಳು ಸಿಗುತ್ತವೆ') ||
      q.includes('ಯಾವ ಯೋಜನೆ ಸಿಗುತ್ತದೆ') ||
      q.includes('what schemes') ||
      q.includes('which schemes') ||
      q.includes('schemes apply for me') ||
      q.includes('schemes for me') ||
      q.includes('am i eligible') ||
      q.includes('ಅರ್ಹತೆ ಪರೀಕ್ಷಿ') ||
      q.includes('885')
    );

    if (!isGeneralDiscovery) {
      let bestMatch = null;
      let bestScore = 0;

      for (const s of schemes) {
        const nameKn = (s.name_kn || '').toLowerCase();
        const nameEn = (s.name_en || '').toLowerCase();
        const slug = (s.slug || '').toLowerCase();
        let score = 0;

        if (slug.length > 3 && q === slug) score = 100;
        else if (nameKn.length > 4 && q.includes(nameKn.split('(')[0].trim())) score = 90;
        else if (nameEn.length > 5 && q.includes(nameEn.split('(')[0].trim())) score = 85;
        else {
          // Check strong keywords for curated/popular schemes
          const knClean = nameKn.replace(/ಯೋಜನೆ|ಸ್ಕೀಮ್|ಕರ್ನಾಟಕ/g, '').trim();
          if (knClean.length >= 4 && q.includes(knClean)) score = 75;
        }

        if (score > bestScore) {
          bestScore = score;
          bestMatch = s;
        }
      }

      if (bestMatch && bestScore >= 75) {
        const officialUrl = getOfficialSchemeWebsite(bestMatch);
        const qs = buildSchemeQuestions(bestMatch);
        const lvlLabel = bestMatch.level === 'State' ? '🏛️ ಕರ್ನಾಟಕ ರಾಜ್ಯ ಸರ್ಕಾರದ ಯೋಜನೆ' : '🇮🇳 ಕೇಂದ್ರ ಸರ್ಕಾರದ ಯೋಜನೆ';
        const desc = bestMatch.description_kn || bestMatch.description_en || '';
        const ben = bestMatch.benefits_kn || bestMatch.benefits_en || desc;
        const applyHow = bestMatch.how_to_apply_kn || bestMatch.how_to_apply_en || 'ಅಧಿಕೃತ ಇಲಾಖಾ ಪೋರ್ಟಲ್ ಅಥವಾ ಸೇವಾ ಸಿಂಧು ಮೂಲಕ ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.';

        const qListMd = qs.map((item, idx) => `${idx + 1}. **${item.category}:** ${item.prompt}`).join('\n');

        const md = `### 🎯 ${bestMatch.name_kn} (${bestMatch.name_en})

* **ಮಟ್ಟ & ಇಲಾಖೆ:** ${lvlLabel} • **${bestMatch.ministry_kn || bestMatch.ministry_en}**
* **ಯೋಜನೆಯ ವಿವರ:** ${desc}
* **ಪ್ರಮುಖ ಸೌಲಭ್ಯಗಳು:** ${ben}
* **ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ವಿಧಾನ:** ${applyHow}
* **ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್:** [${officialUrl}](${officialUrl})

---

#### ✅ ಈ ಯೋಜನೆಗೆ ನಿಮ್ಮ ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಲು 8 ಪ್ರಶ್ನೆಗಳು (8-Point Eligibility Checklist):
${qListMd}

💡 *ಕೆಳಗಿನ ಸಂವಾದಾತ್ಮಕ ಅರ್ಹತಾ ಪರೀಕ್ಷಕದಲ್ಲಿ **ಹೌದು / ಇಲ್ಲ** ಆಯ್ಕೆ ಮಾಡಿ ತಕ್ಷಣ ನಿಮ್ಮ ಅರ್ಹತೆ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ!*`;

        return {
          text: md,
          schemeInteractiveSlug: bestMatch.slug,
          cards: [
            { title: "🌐 ಅಧಿಕೃತ ಯೋಜನೆಯ ವೆಬ್‌ಸೈಟ್ ತೆರೆಯಿರಿ", url: officialUrl, icon: "🔗" },
            { title: "📋 ಎಲ್ಲಾ 885+ ಯೋಜನೆಗಳ ಪೋರ್ಟಲ್", url: `/scheme-checker?id=${encodeURIComponent(bestMatch.slug)}`, icon: "🏛️" }
          ],
          sources: [
            { name: bestMatch.ministry_kn || bestMatch.ministry_en || "Official Department Portal", url: officialUrl }
          ]
        };
      }
    }

    // 2. Check if query is a general scheme discovery / persona eligibility question
    const schemeKeywords = [
      'ಯೋಜನೆ', 'ಸ್ಕೀಮ್', 'scheme', 'schemes', 'ಅರ್ಹತೆ', 'eligible', 'eligibility',
      'ವಿದ್ಯಾರ್ಥಿವೇತನ', 'scholarship', 'ಸಬ್ಸಿಡಿ', 'subsidy', 'ಸಹಾಯಧನ', 'ಪಿಂಚಣಿ', 'pension',
      'ರೈತ ಸಿರಿ', 'ಕೃಷಿ ಭಾಗ್ಯ', 'ವಿದ್ಯಾಸಿರಿ', 'ರೈತ ಶಕ್ತಿ', 'ಮುದ್ರಾ', 'ಪಿಎಂ ಕಿಸಾನ್', 'pm kisan',
      'ನನಗೆ ಯಾವ', 'ರೈತರಿಗೆ', 'ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ', 'ಮಹಿಳೆಯರಿಗೆ', 'ಕಾರ್ಮಿಕರಿಗೆ', 'ವಿಕಲಚೇತನರಿಗೆ'
    ];
    const hasSchemeIntent = isGeneralDiscovery || schemeKeywords.some(k => q.includes(k));
    if (!hasSchemeIntent) return null;

    // Detect initial persona from user query
    const initProfile = {
      age: '',
      gender: '',
      role: '',
      caste: '',
      bpl: 'yes',
      residence: '',
      special: '',
      level: 'all'
    };

    if (q.includes('ರೈತ') || q.includes('ಕೃಷಿ') || q.includes('farmer') || q.includes('agriculture')) initProfile.role = 'farmer';
    else if (q.includes('ವಿದ್ಯಾರ್ಥಿ') || q.includes('student') || q.includes('scholarship') || q.includes('ವಿದ್ಯಾರ್ಥಿವೇತನ')) initProfile.role = 'student';
    else if (q.includes('ಮಹಿಳೆ') || q.includes('ಮಹಿಳಾ') || q.includes('women') || q.includes('woman') || q.includes('ಗೃಹಿಣಿ')) { initProfile.role = 'woman'; initProfile.gender = 'Female'; }
    else if (q.includes('ಉದ್ಯಮ') || q.includes('ವ್ಯಾಪಾರ') || q.includes('ಸಾಲ') || q.includes('business') || q.includes('loan') || q.includes('msme')) initProfile.role = 'business';
    else if (q.includes('ಕಾರ್ಮಿಕ') || q.includes('worker') || q.includes('labour') || q.includes('ಕುಶಲಕರ್ಮಿ')) initProfile.role = 'worker';
    else if (q.includes('ನಿರುದ್ಯೋಗ') || q.includes('unemployed') || q.includes('ಯುವ')) initProfile.role = 'unemployed';
    else if (q.includes('ಹಿರಿಯ') || q.includes('senior') || q.includes('60')) { initProfile.role = 'senior'; initProfile.age = '60'; }

    if (q.includes('ವಿಕಲಚೇತನ') || q.includes('ಅಂಗವಿಕಲ') || q.includes('disabled') || q.includes('disability')) initProfile.special = 'disability';
    else if (q.includes('ಅಲ್ಪಸಂಖ್ಯಾತ') || q.includes('minority')) initProfile.special = 'minority';
    else if (q.includes('ವಿಧವ') || q.includes('widow')) initProfile.special = 'widow';

    if (q.includes('sc') || q.includes('ಪರಿಶಿಷ್ಟ ಜಾತಿ')) initProfile.caste = 'Scheduled Caste (SC)';
    else if (q.includes('st') || q.includes('ಪರಿಶಿಷ್ಟ ಪಂಗಡ')) initProfile.caste = 'Scheduled Tribe (ST)';
    else if (q.includes('obc') || q.includes('ಹಿಂದುಳಿದ')) initProfile.caste = 'Other Backward Class (OBC)';

    const matched = findEligibleSchemes(initProfile);
    const stateCnt = matched.filter(s => s.level === 'State').length;
    const centralCnt = matched.filter(s => s.level === 'Central').length;
    const topSlice = matched.slice(0, 8);

    const topListMd = topSlice.map((s, idx) => {
      const site = getOfficialSchemeWebsite(s);
      const badge = s.level === 'State' ? '🏛️ ರಾಜ್ಯ' : '🇮🇳 ಕೇಂದ್ರ';
      const shortBen = (s.benefits_kn || s.description_kn || s.description_en || '').split(/(?<=[.।])\s+/)[0];
      return `${idx + 1}. **${s.name_kn}** (${badge}) — ${shortBen} [🌐 ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್](${site})`;
    }).join('\n');

    const md = `### 🎯 ನಿಮಗೆ ಅನ್ವಯಿಸುವ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಅರ್ಹತಾ ಮಾರ್ಗದರ್ಶಿ (${matched.length} ಯೋಜನೆಗಳು ಲಭ್ಯವಿವೆ)

* **ಒಟ್ಟು ಹೊಂದಿಕೆಯಾದ ಯೋಜನೆಗಳು:** **${matched.length} ಯೋಜನೆಗಳು** (🏛️ ಕರ್ನಾಟಕ ರಾಜ್ಯ: **${stateCnt}** | 🇮🇳 ಕೇಂದ್ರ ಸರ್ಕಾರ: **${centralCnt}**)
* **ಪಾಯಿಂಟ್ಸ್ ವಿವರ:** ಕೆಳಗಿನ ಸಂವಾದಾತ್ಮಕ **9-ಪ್ರಶ್ನೆಗಳ ಅರ್ಹತಾ ಪರೀಕ್ಷಕ (Interactive Citizen Eligibility Finder)** ನಲ್ಲಿ ನಿಮ್ಮ ವಯಸ್ಸು, ಲಿಂಗ, ವೃತ್ತಿ, ಜಾತಿ ವರ್ಗ, ಮತ್ತು ಪಡಿತರ ಚೀಟಿ ಆಯ್ಕೆ ಮಾಡಿದರೆ ತಕ್ಷಣವೇ ನಿಮಗೆ ಸಿಗುವ ನಿಖರ ಯೋಜನೆಗಳ ಪಟ್ಟಿ ಮತ್ತು ಪ್ರತಿ ಯೋಜನೆಯ **8 ಅರ್ಹತಾ ಪ್ರಶ್ನೆಗಳ ಪರೀಕ್ಷಕ** ಇಲ್ಲಿಯೇ ತೆರೆಯುತ್ತದೆ!

---

#### 🌟 ಪ್ರಮುಖ ಶಿಫಾರಸು ಯೋಜನೆಗಳು (Top Recommended Schemes):
${topListMd}`;

    return {
      text: md,
      showEligibilityWizard: true,
      initialProfile: initProfile,
      cards: [
        { title: "🎯 ಪೂರ್ಣ 885+ ಯೋಜನೆಗಳ ಅರ್ಹತಾ ಪೋರ್ಟಲ್ ತೆರೆಯಿರಿ", url: "/scheme-checker?wizard=1", icon: "🏛️" },
        { title: "🌐 ಸೇವಾ ಸಿಂಧು ಅಧಿಕೃತ ಪೋರ್ಟಲ್", url: "https://sevasindhu.karnataka.gov.in", icon: "🔗" }
      ],
      sources: [
        { name: "ಸೇವಾ ಸಿಂಧು (Seva Sindhu Karnataka)", url: "https://sevasindhu.karnataka.gov.in" },
        { name: "ರೈತ ಮಿತ್ರ (Raita Mitra)", url: "https://raitamitra.karnataka.gov.in" },
        { name: "ರಾಜ್ಯ ವಿದ್ಯಾರ್ಥಿವೇತನ ಪೋರ್ಟಲ್ (SSP)", url: "https://ssp.postmatric.karnataka.gov.in" }
      ]
    };
  }
"""

old_return = """  return {
    init: loadAllDatasets,
    query: query
  };"""

new_return = scheme_engine_js + """
  return {
    init: loadAllDatasets,
    query: query,
    findEligibleSchemes: findEligibleSchemes,
    buildSchemeQuestions: buildSchemeQuestions,
    getOfficialSchemeWebsite: getOfficialSchemeWebsite,
    getSchemeBySlug: getSchemeBySlug,
    getAllSchemes: function() { return db.all_schemes || []; }
  };"""

if "findEligibleSchemes: findEligibleSchemes" not in code:
    assert old_return in code, "old_return not found"
    code = code.replace(old_return, new_return, 1)

with open("ask-ai-engine.js", "w", encoding="utf-8") as f:
    f.write(code)

print("Successfully upgraded ask-ai-engine.js with 885+ schemes and 8-question eligibility engine!")
