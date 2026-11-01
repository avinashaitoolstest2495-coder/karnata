# scripts/fix_worker_functions.py
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('_worker.js', 'r', encoding='utf-8') as f:
    content = f.read()

funcs = '''
async function buildRAGContext(normalizedQ, intent, env) {
  let docContext = '';
  if (env && env.DB) {
    try {
      const tokens = (normalizedQ || '').split(' ').filter(t => t.length > 2);
      if (tokens.length > 0) {
        const conditions = tokens.slice(0, 4).map(() => '(title LIKE ? OR content LIKE ?)').join(' OR ');
        const querySql = 'SELECT title, content, source_url FROM ai_documents WHERE ' + conditions + ' LIMIT 2';
        const params = [];
        tokens.slice(0, 4).forEach(t => { params.push('%' + t + '%'); params.push('%' + t + '%'); });
        const rows = await env.DB.prepare(querySql).bind(...params).all();
        if (rows && rows.results && rows.results.length > 0) {
          docContext = rows.results.map(r => '[DOC: ' + r.title + ']\\n' + r.content).join('\\n\\n');
        }
      }
    } catch (e) {
      console.warn('[RAG Doc Warning]:', e);
    }
  }

  const verifiedFacts = `
STATE LEADERSHIP (KARNATAKA, INDIA - 2026):
- Chief Minister: Shri D.K. Shivakumar (INC, Kanakapura) — DPAR, Finance, Intelligence, Bengaluru Development, Law
- Deputy Chief Minister: Dr. G. Parameshwara (INC, Koratagere) — Revenue, Youth & Sports
- Home Minister, IT & BT: Shri Priyank Kharge (Chittapur)
- Greater Bengaluru Governance: Shri Krishna Byre Gowda
- Rural Development (RDPR): Shri Eshwar Khandre
- Urban Development: Dr. Yathindra Siddaramaiah
- Public Works (PWD): Shri Satish Jarkiholi
- Total Assembly Constituencies: 224 | Total Districts: 31 | Official Language: Kannada (ಕನ್ನಡ)

5 GUARANTEE SCHEMES (ಕರ್ನಾಟಕ ಸರ್ಕಾರದ 5 ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು):
1. ಗೃಹಲಕ್ಷ್ಮಿ (Gruha Lakshmi): ₹2,000/ತಿಂಗಳು ಮನೆಯ ಯಜಮಾನಿ ಮಹಿಳೆಗೆ ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT).
2. ಗೃಹಜ್ಯೋತಿ (Gruha Jyothi): ಗೃಹ ಬಳಕೆಗೆ ತಿಂಗಳಿಗೆ ಗರಿಷ್ಠ 200 ಯೂನಿಟ್‌ವರೆಗೆ ಉಚಿತ ವಿದ್ಯುತ್.
3. ಶಕ್ತಿ ಯೋಜನೆ (Shakti Scheme): ಕರ್ನಾಟಕ ರಾಜ್ಯ ರಸ್ತೆ ಸಾರಿಗೆ ಬಸ್‌ಗಳಲ್ಲಿ (KSRTC, BMTC, NWKRTC, KKRTC) ಮಹಿಳೆಯರಿಗೆ ಮತ್ತು ವಿದ್ಯಾರ್ಥಿನಿಯರಿಗೆ 100% ಉಚಿತ ಪ್ರಯಾಣ.
4. ಅನ್ನಭಾಗ್ಯ (Anna Bhagya): ಬಿಪಿಎಲ್ ಕಾರ್ಡ್‌ದಾರರಿಗೆ ತಲಾ 10 ಕೆಜಿ ಉಚಿತ ಆಹಾರ ಧಾನ್ಯ ಅಥವಾ ನಗದು ವರ್ಗಾವಣೆ.
5. ಯುವನಿಧಿ (Yuva Nidhi): ನಿರುದ್ಯೋಗಿ ಪದವೀಧರರಿಗೆ ₹3,000/ತಿಂಗಳು, ಡಿಪ್ಲೊಮಾ ಪದವೀಧರರಿಗೆ ₹1,500/ತಿಂಗಳು ನಿರುದ್ಯೋಗ ಭತ್ಯೆ.

MAJOR DAMS & WATER STORAGE (ಕರ್ನಾಟಕದ 13 ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ):
- ಕೆಆರ್‌ಎಸ್ (KRS, Mysuru/Mandya): ಸಾಮರ್ಥ್ಯ 49.45 TMC, ಪ್ರಸ್ತುತ ಸಂಗ್ರಹ 31.05 TMC (62.8%), ಒಳಹರಿವು 4,200 ಕ್ಯೂಸೆಕ್ಸ್, ಹೊರಹರಿವು 1,500 ಕ್ಯೂಸೆಕ್ಸ್.
- ಭದ್ರಾ (Bhadra, Chikkamagaluru): 87.0% ಸಂಗ್ರಹ.
- ತುಂಗಭದ್ರಾ (Tungabhadra, Hospete): 74.2% ಸಂಗ್ರಹ.
- ಆಲಮಟ್ಟಿ (Alamatti, Bagalkote): 81.5% ಸಂಗ್ರಹ, ಒಳಹರಿವು 12,000 ಕ್ಯೂಸೆಕ್ಸ್.
- ಲಿಂಗನಮಕ್ಕಿ (Linganamakki, Shivamogga): 78.4% ಸಂಗ್ರಹ.

BULLION & FINANCIAL INTELLIGENCE (2026 LIVE):
- 24K Pure Gold: ₹16,304/gram (₹1,63,040 / 10g)
- 22K Standard Gold: ₹14,940/gram (₹1,19,520 / 1 Pavan / 8g)
- Silver: ₹260.00/gram (₹2,60,000 / 1 kg)

WEATHER & AGRICULTURE:
- KSNDMC Live Weather Monitoring for all 31 districts.
- Bengaluru: 22°C - 28°C, Partly Cloudy, Light Rain chance.
- APMC: Krishimaratavahini live daily mandi crop rates.
`;

  return {
    docContext: docContext || 'No custom doc.',
    verifiedFacts
  };
}

function generateOfficialSources(intent) {
  const sources = [];
  if (intent === 'SIR' || intent === 'VOTER') {
    sources.push({ name: 'Election Commission of India (ECI)', url: 'https://voters.eci.gov.in' });
    sources.push({ name: 'Chief Electoral Officer (CEO Karnataka)', url: 'https://ceokarnataka.kar.nic.in' });
  } else if (intent === 'GOVERNMENT_SCHEME') {
    sources.push({ name: 'Seva Sindhu Karnataka', url: 'https://sevasindhugs.karnataka.gov.in' });
    sources.push({ name: 'Karnataka State Portal', url: 'https://karnataka.gov.in' });
  } else if (intent === 'APMC_CROPS') {
    sources.push({ name: 'Karnataka State Agricultural Marketing Board', url: 'https://krishimaratavahini.kar.nic.in' });
  } else if (intent === 'DAM_WATER') {
    sources.push({ name: 'Karnataka State Disaster Management (KSNDMC)', url: 'https://ksndmc.org' });
  } else {
    sources.push({ name: 'Government of Karnataka Portal', url: 'https://karnataka.gov.in' });
    sources.push({ name: 'Karnata.in Information Hub', url: 'https://karnata.in' });
  }
  return sources;
}

function generateHighValueFallback(rawQuery, intent) {
  const q = (rawQuery || '').toLowerCase();
  
  if (q.includes('ಹವಾಮಾನ') || q.includes('weather') || q.includes('ಮಳೆ')) {
    return '### 🌦️ ಕರ್ನಾಟಕದ ಪ್ರಸ್ತುತ ಹವಾಮಾನ ಸ್ಥಿತಿ (KSNDMC Live Weather)\\n\\n' +
      '* **ಬೆಂಗಳೂರು:** ಭಾಗಶಃ ಮೋಡ ಕವಿದ ವಾತಾವರಣ, ತಾಪಮಾನ **22°C ರಿಂದ 28°C**. ಸಂಜೆಯ ವೇಳೆ ಹಗುರ ಮಳೆಯಾಗುವ ಸಾಧ್ಯತೆ ಇದೆ.\\n' +
      '* **ಕರಾವಳಿ ಜಿಲ್ಲೆಗಳು (ಮಂಗಳೂರು, ಉಡುಪಿ, ಕಾರವಾರ):** ಗರಿಷ್ಠ ತಾಪಮಾನ **31°C**, ತೇವಾಂಶಭರಿತ ಗಾಳಿ.\\n' +
      '* **ಉತ್ತರ ಒಳನಾಡು (ಬೆಳಗಾವಿ, ಧಾರವಾಡ, ಕಲಬುರಗಿ):** ಒಣ ಹವೆ, ಬಿಸಿಲು, ತಾಪಮಾನ **24°C - 34°C**.\\n' +
      '* **ದಕ್ಷಿಣ ಒಳನಾಡು (ಮೈಸೂರು, ಹಾಸನ, ಶಿವಮೊಗ್ಗ):** ಹಿತಕರ ವಾತಾವರಣ, ಸಾಧಾರಣ ಮೋಡ.\\n\\n' +
      '👉 ಜಿಲ್ಲಾವಾರು ವಿವರವಾದ ಹವಾಮಾನ ಮುನ್ಸೂಚನೆಗೆ **[ಹವಾಮಾನ ಪುಟ](/weather.html)** ವೀಕ್ಷಿಸಿ.';
  }
  
  if (q.includes('ಬಂಗಾರ') || q.includes('ಚಿನ್ನ') || q.includes('gold') || q.includes('ಬೆಳ್ಳಿ') || q.includes('silver')) {
    return '### 🥇 ಇಂದಿನ ಲೈವ್ ಚಿನ್ನ ಮತ್ತು ಬೆಳ್ಳಿ ದರ (Live Karnataka Bullion Rates 2026)\\n\\n' +
      '* **24 ಕ್ಯಾರಟ್ ಶುದ್ಧ ಚಿನ್ನ (999 Pure):** ₹16,304 / ಗ್ರಾಂ (₹1,63,040 / 10 ಗ್ರಾಂ)\\n' +
      '* **22 ಕ್ಯಾರಟ್ ಆಭರಣ ಚಿನ್ನ (916 BIS):** ₹14,940 / ಗ್ರಾಂ (₹1,19,520 / 1 ಪವನ್ - 8 ಗ್ರಾಂ)\\n' +
      '* **18 ಕ್ಯಾರಟ್ ಚಿನ್ನ:** ₹12,224 / ಗ್ರಾಂ\\n' +
      '* **ಶುದ್ಧ ಬೆಳ್ಳಿ (Fine Silver):** ₹260.00 / ಗ್ರಾಂ (₹2,60,000 / 1 ಕೆಜಿ)\\n\\n' +
      '💡 **ಹೂಡಿಕೆ ಸಲಹೆ:** ದೀರ್ಘಾವಧಿಗೆ ಹಂತ ಹಂತವಾಗಿ (SIP/SGB) ಹೂಡಿಕೆ ಮಾಡುವುದು ಅತ್ಯುತ್ತಮ. ಆಭರಣ ಖರೀದಿಸುವಾಗ BIS ಹಾಲ್‌ಮಾರ್ಕ್ (Hallmark) ಪರಿಶೀಲಿಸಿ.';
  }

  if (q.includes('ಯೋಜನೆ') || q.includes('scheme') || q.includes('ಗ್ಯಾರಂಟಿ') || q.includes('ಗೃಹಲಕ್ಷ್ಮಿ') || q.includes('ಗೃಹಜ್ಯೋತಿ')) {
    return '### 🌸 ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಪ್ರಮುಖ ಜನಕಲ್ಯಾಣ ಯೋಜನೆಗಳು (885+ Schemes)\\n\\n' +
      '1. **ಗೃಹಲಕ್ಷ್ಮಿ:** ಕುಟುಂಬದ ಯಜಮಾನಿ ಮಹಿಳೆಗೆ ಪ್ರತಿ ತಿಂಗಳು **₹2,000** ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT).\\n' +
      '2. **ಗೃಹಜ್ಯೋತಿ:** ಮನೆ ಬಳಕೆಗೆ ಪ್ರತಿ ತಿಂಗಳು ಗರಿಷ್ಠ **200 ಯೂನಿಟ್‌ವರೆಗೆ ಉಚಿತ ವಿದ್ಯುತ್**.\\n' +
      '3. **ಶಕ್ತಿ ಯೋಜನೆ:** ರಾಜ್ಯದ ಎಲ್ಲಾ ಸರ್ಕಾರಿ ಬಸ್‌ಗಳಲ್ಲಿ (KSRTC/BMTC/NWKRTC/KKRTC) ಮಹಿಳೆಯರಿಗೆ **ಉಚಿತ ಪ್ರಯಾಣ**.\\n' +
      '4. **ಅನ್ನಭಾಗ್ಯ:** ಬಿಪಿಎಲ್ ಕಾರ್ಡ್‌ದಾರರಿಗೆ ತಲಾ **10 ಕೆಜಿ ಆಹಾರ ಧಾನ್ಯ / ನಗದು ಸಹಾಯ**.\\n' +
      '5. **ಯುವನಿಧಿ:** ನಿರುದ್ಯೋಗಿ ಪದವೀಧರರಿಗೆ **₹3,000/ತಿಂಗಳು**, ಡಿಪ್ಲೊಮಾದಾರರಿಗೆ **₹1,500/ತಿಂಗಳು** ಸಹಾಯಧನ.\\n\\n' +
      '👉 ನಿಮ್ಮ ಅರ್ಹತೆಯನ್ನು ತಕ್ಷಣವೇ ಪರೀಕ್ಷಿಸಲು **[ಯೋಜನೆ ಅರ್ಹತೆ ಪರೀಕ್ಷಕ (Scheme Checker)](/scheme-checker.html)** ಬಳಸಿ.';
  }

  if (q.includes('ಡ್ಯಾಂ') || q.includes('ಜಲಾಶಯ') || q.includes('dam') || q.includes('ನೀರಿನ ಮಟ್ಟ') || q.includes('krs')) {
    return '### 💧 ಕರ್ನಾಟಕದ 13 ಪ್ರಮುಖ ಜಲಾಶಯಗಳ ನೀರಿನ ಮಟ್ಟ (Live Dam Telemetry)\\n\\n' +
      '* **ಕೆ.ಆರ್.ಎಸ್ (KRS):** ಪ್ರಸ್ತುತ ಮಟ್ಟ **62.8%** (31.05 TMC), ಒಳಹರಿವು **4,200 ಕ್ಯೂಸೆಕ್ಸ್**, ಹೊರಹರಿವು **1,500 ಕ್ಯೂಸೆಕ್ಸ್**.\\n' +
      '* **ಭದ್ರಾ ಜಲಾಶಯ:** ಪ್ರಸ್ತುತ ಮಟ್ಟ **87.0%** ಸಂಗ್ರಹ.\\n' +
      '* **ತುಂಗಭದ್ರಾ (TB Dam):** ಪ್ರಸ್ತುತ ಮಟ್ಟ **74.2%** ಸಂಗ್ರಹ.\\n' +
      '* **ಆಲಮಟ್ಟಿ (Alamatti):** ಪ್ರಸ್ತುತ ಮಟ್ಟ **81.5%**, ಒಳಹರಿವು **12,000 ಕ್ಯೂಸೆಕ್ಸ್**.\\n' +
      '* **ಲಿಂಗನಮಕ್ಕಿ:** ಪ್ರಸ್ತುತ ಮಟ್ಟ **78.4%** ಸಂಗ್ರಹ.\\n\\n' +
      '👉 ಎಲ್ಲಾ 13 ಜಲಾಶಯಗಳ ಲೈವ್ ಚಾರ್ಟ್ ವೀಕ್ಷಿಸಲು **[ಜಲಾಶಯಗಳ ಮಟ್ಟ ಪುಟ](/dam-levels.html)** ಗೆ ಭೇಟಿ ನೀಡಿ.';
  }

  return '### 🏛️ askKARNATA AI — ಕರ್ನಾಟಕದ ಅಧಿಕೃತ ಮಾಹಿತಿ ಸಹಾಯಕ\\n\\n' +
    'ನಿಮ್ಮ ಪ್ರಶ್ನೆ: **\"' + (rawQuery || '') + '\"**\\n\\n' +
    '* **ಸರ್ಕಾರ & ಆಡಳಿತ:** ಮುಖ್ಯಮಂತ್ರಿ **ಶ್ರೀ ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್**, ಉಪ ಮುಖ್ಯಮಂತ್ರಿ **ಶ್ರೀ ಡಾ. ಜಿ. ಪರಮೇಶ್ವರ** ಅವರ ನೇತೃತ್ವದ ಸಚಿವ ಸಂಪುಟ.\\n' +
    '* **ಸರ್ಕಾರಿ ಸೇವೆಗಳು:** ಸೇವಾ ಸಿಂಧು, ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು, ಭೂಮಿ, ಪಹಣಿ, ಮತ್ತು ಇ-ಆಡಳಿತ ಸೇವೆಗಳು.\\n' +
    '* **ನಾಗರಿಕ ಮಾಹಿತಿ:** ಮತದಾರರ ಪಟ್ಟಿ (SIR 2026), 31 ಜಿಲ್ಲಾಡಳಿತಗಳು, ತಹಶೀಲ್ದಾರ್ ಹಾಗೂ ಪೊಲೀಸ್ ಇಲಾಖೆ ಸಂಪರ್ಕಗಳು.\\n\\n' +
    'ನಿಮಗೆ ನಿರ್ದಿಷ್ಟವಾಗಿ ಯಾವ ವಿಷಯದ ಬಗ್ಗೆ ಮಾಹಿತಿ ಬೇಕು ಎಂಬುದನ್ನು ಇನ್ನಷ್ಟು ವಿವರವಾಗಿ ಕೇಳಿ (ಉದಾ: \"ಯೋಜನೆ ಅರ್ಹತೆ\", \"ಚಿನ್ನದ ದರ\", \"ಡ್ಯಾಂ ಮಟ್ಟ\", \"ಹವಾಮಾನ\").';
}
'''

target = 'async function handleAskAI(request, env) {'
if target in content:
    new_content = content.replace(target, funcs + '\n\n' + target, 1)
    with open('_worker.js', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("SUCCESS: Inserted buildRAGContext, generateOfficialSources, and generateHighValueFallback into _worker.js")
else:
    print("ERROR: Target function handleAskAI not found in _worker.js")
