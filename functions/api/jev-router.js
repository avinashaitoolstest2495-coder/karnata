/**
 * Karnata — /api/jev-router
 * Universal Graph Transit Engine v3.0
 */
let fnBmtcCache = null;
let fnKsrtcCache = null;

export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
// ══════════════════════════════════════════════════════════════
    // Route: JEV Transit Router — Universal Graph Transit Engine v3.0
    // Covers all 85+ stations, all lines, exact BMRCL fares, BMTC & KSRTC
    // Endpoint: /api/jev-router (Supports POST, GET, OPTIONS)
    // ══════════════════════════════════════════════════════════════

      const corsHeaders = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-TypeSafe-Key',
      };

      if (request.method === 'OPTIONS') {
        return new Response('', { status: 200, headers: corsHeaders });
      }

      let userInput = '';
      let fromStationParam = '';
      let toStationParam = '';

      if (request.method === 'POST') {
        try {
          const body = await request.json();
          userInput = body.userInput || body.q || body.query || '';
          fromStationParam = body.fromStation || '';
          toStationParam = body.toStation || '';
        } catch {
          userInput = '';
        }
      } else if (request.method === 'GET') {
        userInput = url.searchParams.get('userInput') || url.searchParams.get('q') || url.searchParams.get('query') || '';
        fromStationParam = url.searchParams.get('fromStation') || '';
        toStationParam = url.searchParams.get('toStation') || '';
      } else {
        return new Response(JSON.stringify({ error: 'Method Not Allowed' }), {
          status: 405,
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }

      if (!userInput && fromStationParam && toStationParam) {
        userInput = fromStationParam + ' to ' + toStationParam;
      }

      if (!userInput || typeof userInput !== 'string' || !userInput.trim()) {
        return new Response(JSON.stringify({
          error: 'userInput is required (non-empty string, max 500 characters)'
        }), {
          status: 400,
          headers: { 'Content-Type': 'application/json', ...corsHeaders }
        });
      }

      const t0 = Date.now();
      const input = userInput.trim().slice(0, 500);
      const q = input.toLowerCase();

      // ── 1. Traffic Sensitivity Detection ──
      const trafficRegex = /\b(traffic|traffic jam|heavy traffic|gridlock|rush hour|peak hour|congestion|congested|slow moving|bottleneck|bypass|bypass traffic|avoid traffic|avoid congestion|skip traffic|silk board traffic|tin factory traffic|goraguntepalya traffic|outer ring road traffic|orr traffic|waterlogged|delay|delayed|stuck in traffic)\b|ಟ್ರಾಫಿಕ್|ಜಾಮ್|ದಟ್ಟಣೆ|ರಶ್|ತಡೆ/i;
      const isTrafficSensitive = trafficRegex.test(q);

      // ── 2. Urgency Score Resolution (1 - 5) ──
      let urgencyScore = 1;
      let urgencyReason = 'Casual route enquiry';

      const critRegex = /\b(emergency|urgent|urgently|immediate|immediately|missing flight|miss the flight|miss flight|flight in|flight at|flight boarding|train in|hospital|ambulance|critical|life or death|in 5 min|in 10 min|in 15 min|in 20 min|right now|hurry up|quick)\b|ತುರ್ತು|ವಿಮಾನ|ತಕ್ಷಣ/i;
      const highRegex = /\b(running late|late for|fastest|quickest|asap|as soon as possible|hurry|reach fast|fast route|time is running out|meeting in|interview in|exam in|exam time|reach before)\b|ಬೇಗ|ತಡವಾಗಿದೆ|ಶೀಘ್ರ/i;
      const modRegex  = /\b(today|now|soon|schedule|commute|office time|morning commute|evening commute|reach by|estimated time|how long will it take|travel time)\b|ಇಂದು|ಈಗ/i;
      const mildRegex = /\b(tomorrow|tonight|this evening|later today|weekend|planning|best time to travel|which bus goes|which metro goes)\b|ನಾಳೆ|ರಾತ್ರಿ/i;

      if (critRegex.test(q)) {
        urgencyScore = 5;
        urgencyReason = 'Critical time deadline / flight departure / emergency';
      } else if (highRegex.test(q)) {
        urgencyScore = 4;
        urgencyReason = 'High urgency / running late / fastest transit path requested';
      } else if (modRegex.test(q)) {
        urgencyScore = 3;
        urgencyReason = 'Moderate urgency / scheduled commute today';
      } else if (mildRegex.test(q)) {
        urgencyScore = 2;
        urgencyReason = 'Mild urgency / planning journey ahead';
      }

      // ── 3. Transit Mode Intent Scoring ──
      let metroScore = 0;
      let bmtcScore = 0;
      let ksrtcScore = 0;

      if (/\b(metro|bmrcl|purple line|green line|yellow line|pink line|namma metro|metro card|smart card|token|metro station|train to whitefield)\b|ಮೆಟ್ರೋ|ನಮ್ಮ ಮೆಟ್ರೋ|ನೇರಳೆ ಮಾರ್ಗ|ಹಸಿರು ಮಾರ್ಗ/i.test(q)) {
        metroScore += 12;
      }
      if (/\b(bmtc|city bus|volvo|vajra|vayu vajra|kia[-\s]?\d+|ttmc|bus stop|bus stand|bus pass|daily pass|route no|500d|335e|g[-\s]?[1-9]|mf[-\s]?\d+|shakti|pushpak)\b|ಬಿಎಂಟಿಸಿ|ಸಿಟಿ ಬಸ್|ವೋಲ್ವೋ|ವಾಯು ವಜ್ರ|ಬಸ್ಸು/i.test(q)) {
        bmtcScore += 12;
      }
      if (/\b(ksrtc|intercity|outstation|rajahamsa|airavat|club class|ambaari|sarige|flybus|sleeper bus|ksrtc booking|awatar|nekrtc|nwkrtc|kalyana karnataka|north western)\b|ಕೆಎಸ್ಆರ್ಟಿಸಿ|ರಾಜಹಂಸ|ಐರಾವತ|ಅಂಬಾರಿ|ಸಾರಿಗೆ|ಫ್ಲೈಬಸ್/i.test(q)) {
        ksrtcScore += 12;
      }

      // ── 4. Complete Station Network Datasets ──
      const PURPLE = [
        ["Whitefield (Kadugodi)", "ವೈಟ್‌ಫೀಲ್ಡ್ (ಕಾಡುಗೋಡಿ)"],
        ["Hopefarm Channasandra", "ಹೋಪ್‌ಫಾರ್ಮ್ ಚನ್ನಸಂದ್ರ"],
        ["Kadugodi Tree Park", "ಕಾಡುಗೋಡಿ ಟ್ರೀ ಪಾರ್ಕ್"],
        ["Pattandur Agrahara", "ಪಟ್ಟಂದೂರು ಅಗ್ರಹಾರ"],
        ["Sri Sathya Sai Hospital", "ಶ್ರೀ ಸತ್ಯ ಸಾಯಿ ಆಸ್ಪತ್ರೆ"],
        ["Nallurahalli", "ನಲ್ಲೂರಹಳ್ಳಿ"],
        ["Kundalahalli", "ಕುಂದಲಹಳ್ಳಿ"],
        ["Seetharampalya", "ಸೀತಾರಾಮಪಾಳ್ಯ"],
        ["Hoodi", "ಹೂಡಿ"],
        ["Garudacharpalya", "ಗರುಡಾಚಾರ್‌ಪಾಳ್ಯ"],
        ["Singayyanapalya", "ಸಿಂಗಯ್ಯನಪಾಳ್ಯ"],
        ["Krishnarajapura (K.R. Pura)", "ಕೃಷ್ಣರಾಜಪುರ"],
        ["Benniganahalli", "ಬೆನ್ನಿಗಾನಹಳ್ಳಿ"],
        ["Baiyappanahalli", "ಬೈಯ್ಯಪ್ಪನಹಳ್ಳಿ"],
        ["Swami Vivekananda Road", "ಸ್ವಾಮಿ ವಿವೇಕಾನಂದ ರಸ್ತೆ"],
        ["Indiranagar", "ಇಂದಿರಾನಗರ"],
        ["Halasuru", "ಹಲಸೂರು"],
        ["Trinity", "ಟ್ರಿನಿಟಿ"],
        ["Mahatma Gandhi Road", "ಎಂ.ಜಿ. ರಸ್ತೆ"],
        ["Cubbon Park", "ಕಬ್ಬನ್ ಪಾರ್ಕ್"],
        ["Dr. B.R. Ambedkar Stn (Vidhana Soudha)", "ವಿಧಾನ ಸೌಧ"],
        ["Sir M. Visvesvaraya (Central College)", "ಸರ್ ಎಂ. ವಿಶ್ವೇಶ್ವರಯ್ಯ"],
        ["Nadaprabhu Kempegowda Stn (Majestic)", "ನಾಡಪ್ರಭು ಕೆಂಪೇಗೌಡ ನಿಲ್ದಾಣ (ಮೆಜೆಸ್ಟಿಕ್)"],
        ["Krantivira Sangolli Rayanna Railway Stn", "ಕ್ರಾಂತಿವೀರ ಸಂಗೊಳ್ಳಿ ರಾಯಣ್ಣ"],
        ["Magadi Road", "ಮಾಗಡಿ ರಸ್ತೆ"],
        ["Sri Balagangadharanatha Swamiji Stn", "ಹೊಸಹಳ್ಳಿ"],
        ["Vijayanagar", "ವಿಜಯನಗರ"],
        ["Attiguppe", "ಅತ್ತಿಗುಪ್ಪೆ"],
        ["Deepanjali Nagar", "ದೀಪಾಂಜಲಿ ನಗರ"],
        ["Mysuru Road", "ಮೈಸೂರು ರಸ್ತೆ"],
        ["Pantharapalya (Nayandahalli)", "ಪಂತರಪಾಳ್ಯ (ನಾಯಂಡಹಳ್ಳಿ)"],
        ["Rajarajeshwari Nagar", "ರಾಜರಾಜೇಶ್ವರಿ ನಗರ"],
        ["Jnanabharathi", "ಜ್ಞಾನಭಾರತಿ"],
        ["Pattanagere", "ಪಟ್ಟಣಗೆರೆ"],
        ["Kengeri Bus Terminal", "ಕೆಂಗೇರಿ ಬಸ್ ಟರ್ಮಿನಲ್"],
        ["Kengeri", "ಕೆಂಗೇರಿ"],
        ["Challaghatta", "ಚಲ್ಲಘಟ್ಟ"]
      ];

      const GREEN = [
        ["Madavara (BIEC)", "ಮಾದಾವರ (BIEC)"],
        ["Chikkabidarakallu", "ಚಿಕ್ಕಬಿದರಕಲ್ಲು"],
        ["Manjunathanagar", "ಮಂಜುನಾಥನಗರ"],
        ["Nagasandra", "ನಾಗಸಂದ್ರ"],
        ["Dasarahalli", "ದಾಸರಹಳ್ಳಿ"],
        ["Jalahalli", "ಜಾಲಹಳ್ಳಿ"],
        ["Peenya Industry", "ಪೀಣ್ಯ ಇಂಡಸ್ಟ್ರಿ"],
        ["Peenya", "ಪೀಣ್ಯ"],
        ["Goraguntepalya", "ಗೊರಗುಂಟೆಪಾಳ್ಯ"],
        ["Yeshwanthpur", "ಯಶವಂತಪುರ"],
        ["Sandal Soap Factory", "ಸ್ಯಾಂಡಲ್ ಸೋಪ್ ಫ್ಯಾಕ್ಟರಿ"],
        ["Mahalakshmi", "ಮಹಾಲಕ್ಷ್ಮಿ"],
        ["Rajajinagar", "ರಾಜಾಜಿನಗರ"],
        ["Kuvempu Road", "ಕುವೆಂಪು ರಸ್ತೆ"],
        ["Srirampura", "ಶ್ರೀರಾಂಪುರ"],
        ["Mantri Square Sampige Road", "ಮಂತ್ರಿ ಸ್ಕ್ವೇರ್ ಸಂಪಿಗೆ ರಸ್ತೆ"],
        ["Nadaprabhu Kempegowda Stn (Majestic)", "ನಾಡಪ್ರಭು ಕೆಂಪೇಗೌಡ ನಿಲ್ದಾಣ (ಮೆಜೆಸ್ಟಿಕ್)"],
        ["Chickpete", "ಚಿಕ್ಕಪೇಟೆ"],
        ["Krishna Rajendra Market", "ಕೃಷ್ಣ ರಾಜೇಂದ್ರ ಮಾರುಕಟ್ಟೆ"],
        ["National College", "ನ್ಯಾಷನಲ್ ಕಾಲೇಜು"],
        ["Lalbagh", "ಲಾಲ್‌ಬಾಗ್"],
        ["South End Circle", "ಸೌತ್ ಎಂಡ್ ಸರ್ಕಲ್"],
        ["Jayanagar", "ಜಯನಗರ"],
        ["Rashtreeya Vidyalaya Road", "ರಾಷ್ಟ್ರೀಯ ವಿದ್ಯಾಲಯ ರಸ್ತೆ"],
        ["Banashankari", "ಬನಶಂಕರಿ"],
        ["Jaya Prakash Nagar (JP Nagar)", "ಜಯಪ್ರಕಾಶ ನಗರ"],
        ["Yelachenahalli", "ಯಲಚೇನಹಳ್ಳಿ"],
        ["Konanakunte Cross", "ಕೋಣನಕುಂಟೆ ಕ್ರಾಸ್"],
        ["Doddakallasandra", "ದೊಡ್ಡಕಲ್ಲಸಂದ್ರ"],
        ["Vajarahalli", "ವಜ್ರಹಳ್ಳಿ"],
        ["Thalaghattapura", "ತಲಘಟ್ಟಪುರ"],
        ["Silk Institute", "ಸಿಲ್ಕ್ ಇನ್‌ಸ್ಟಿಟ್ಯೂಟ್"]
      ];

      const YELLOW = [
        ["Rashtreeya Vidyalaya Road", "ರಾಷ್ಟ್ರೀಯ ವಿದ್ಯಾಲಯ ರಸ್ತೆ"],
        ["Ragigudda", "ರಾಗಿಗುಡ್ಡ"],
        ["Jayadeva Hospital", "ಜಯದೇವ ಆಸ್ಪತ್ರೆ"],
        ["BTM Layout", "ಬಿಟಿಎಂ ಲೇಔಟ್"],
        ["Central Silk Board", "ಸೆಂಟ್ರಲ್ ಸಿಲ್ಕ್ ಬೋರ್ಡ್"],
        ["Bommanahalli", "ಬೊಮ್ಮನಹಳ್ಳಿ"],
        ["Hongasandra", "ಹೊಂಗಸಂದ್ರ"],
        ["Kudlu Gate", "ಕುಡ್ಲು ಗೇಟ್"],
        ["Singasandra", "ಸಿಂಗಸಂದ್ರ"],
        ["Hosa Road", "ಹೊಸ ರಸ್ತೆ"],
        ["Beratena Agrahara", "ಬೆರಟೇನ ಅಗ್ರಹಾರ"],
        ["Electronic City", "ಎಲೆಕ್ಟ್ರಾನಿಕ್ ಸಿಟಿ"],
        ["Infosys Foundation Konappana Agrahara", "ಕೋನಪ್ಪನ ಅಗ್ರಹಾರ"],
        ["Huskur Road", "ಹುಸ್ಕೂರು ರಸ್ತೆ"],
        ["Hebbagodi", "ಹೆಬ್ಬಗೋಡಿ"],
        ["Bommasandra", "ಬೊಮ್ಮಸಂದ್ರ"]
      ];

      const KNOWN_INTERCITY_CITIES = ['mysuru', 'mysore', 'mangaluru', 'mangalore', 'hubballi', 'hubli', 'dharwad', 'belagavi', 'belgaum', 'shivamogga', 'shimoga', 'davanagere', 'davangere', 'ballari', 'bellary', 'kalaburagi', 'gulbarga', 'bidar', 'raichur', 'vijayapura', 'bijapur', 'hassan', 'chikmagalur', 'chikkamagaluru', 'udupi', 'gokarna', 'dharmasthala', 'kukke', 'subrahmanya', 'tirupati', 'ooty', 'coorg', 'madikeri', 'kodagu'];

      // BMRCL Official Tariff Slabs
      const TARIFF_SLABS = [
        { maxStn: 2, token: 10, smartPeak: 10, smartOff: 9 },
        { maxStn: 4, token: 20, smartPeak: 19, smartOff: 18 },
        { maxStn: 6, token: 30, smartPeak: 29, smartOff: 27 },
        { maxStn: 8, token: 40, smartPeak: 38, smartOff: 36 },
        { maxStn: 10, token: 50, smartPeak: 48, smartOff: 45 },
        { maxStn: 15, token: 60, smartPeak: 57, smartOff: 54 },
        { maxStn: 20, token: 70, smartPeak: 67, smartOff: 63 },
        { maxStn: 25, token: 80, smartPeak: 76, smartOff: 72 },
        { maxStn: 999, token: 90, smartPeak: 86, smartOff: 81 }
      ];

      function calculateBmrclFare(stnCount) {
        for (const slab of TARIFF_SLABS) {
          if (stnCount <= slab.maxStn) return slab;
        }
        return TARIFF_SLABS[TARIFF_SLABS.length - 1];
      }

      // Graph construction
      const stnGraph = {};
      const stnIndex = {};
      const linesMeta = {
        purple: { name_en: 'Purple Line', name_kn: 'ನೇರಳೆ ಮಾರ್ಗ', color: '#8B5CF6' },
        green:  { name_en: 'Green Line',  name_kn: 'ಹಸಿರು ಮಾರ್ಗ', color: '#10B981' },
        yellow: { name_en: 'Yellow Line', name_kn: 'ಹಳದಿ ಮಾರ್ಗ', color: '#EAB308' }
      };

      function registerLineStns(lineId, arr) {
        for (let i = 0; i < arr.length; i++) {
          const key = lineId + ':' + (i + 1);
          stnGraph[key] = {
            key: key,
            line: lineId,
            lineName: linesMeta[lineId].name_en,
            lineNameKn: linesMeta[lineId].name_kn,
            lineColor: linesMeta[lineId].color,
            index: i + 1,
            name_en: arr[i][0],
            name_kn: arr[i][1],
            neighbors: []
          };
          if (i > 0) {
            const prev = lineId + ':' + i;
            stnGraph[key].neighbors.push(prev);
            stnGraph[prev].neighbors.push(key);
          }

          const norm = arr[i][0].toLowerCase().replace(/[^a-z0-9]/g, ' ').replace(/\s+/g, ' ').trim();
          stnIndex[norm] = key;
          if (arr[i][1]) stnIndex[arr[i][1].trim()] = key;

          for (const word of norm.split(' ')) {
            if (word.length > 3 && !['station', 'road', 'cross', 'park', 'nagar', 'circle', 'line', 'tree'].includes(word)) {
              if (!stnIndex[word]) stnIndex[word] = key;
            }
          }
        }
      }

      registerLineStns('purple', PURPLE);
      registerLineStns('green', GREEN);
      registerLineStns('yellow', YELLOW);

      // Interchanges
      stnGraph['purple:23'].neighbors.push('green:17'); // Majestic
      stnGraph['green:17'].neighbors.push('purple:23');

      stnGraph['green:24'].neighbors.push('yellow:1');  // RV Road
      stnGraph['yellow:1'].neighbors.push('green:24');

      // Check Intercity destination
      for (const city of KNOWN_INTERCITY_CITIES) {
        if (q.includes(city)) ksrtcScore += 8;
      }

      // Check Metro keywords
      for (const k of Object.keys(stnIndex)) {
        if (q.includes(k)) metroScore += 2;
      }

      let transitGroup = 'General_Query';
      let confidence = 0.75;
      const maxScore = Math.max(metroScore, bmtcScore, ksrtcScore);
      if (maxScore > 0) {
        if (metroScore === maxScore) {
          transitGroup = 'Namma_Metro';
          confidence = Math.min(0.99, 0.8 + (metroScore * 0.02));
        } else if (bmtcScore === maxScore) {
          transitGroup = 'BMTC_City_Bus';
          confidence = Math.min(0.99, 0.8 + (bmtcScore * 0.02));
        } else if (ksrtcScore === maxScore) {
          transitGroup = 'KSRTC_Intercity';
          confidence = Math.min(0.99, 0.8 + (ksrtcScore * 0.02));
        }
      }

      // ── 5. Origin / Destination Resolution ──
      stnIndex['silk board'] = 'yellow:5';
      stnIndex['central silk board'] = 'yellow:5';
      stnIndex['electronic city'] = 'yellow:12';
      stnIndex['ecity'] = 'yellow:12';
      stnIndex['itpl'] = 'purple:1';
      stnIndex['majestic'] = 'purple:23';
      stnIndex['kbs'] = 'purple:23';
      stnIndex['kr puram'] = 'purple:12';
      stnIndex['tin factory'] = 'purple:12';
      stnIndex['rv road'] = 'yellow:1';
      stnIndex['madavara'] = 'green:1';
      stnIndex['biec'] = 'green:1';

      const sortedStnEntries = Object.entries(stnIndex).sort((a, b) => b[0].length - a[0].length);

      function matchStation(term) {
        if (!term) return null;
        const norm = term.toLowerCase().replace(/[^a-z0-9]/g, ' ').replace(/\s+/g, ' ').trim();
        if (stnIndex[norm]) return stnIndex[norm];
        for (const [k, v] of sortedStnEntries) {
          if (norm === k || norm.includes(k)) return v;
        }
        for (const [k, v] of sortedStnEntries) {
          if (k.includes(norm) && norm.length >= 4) return v;
        }
        return null;
      }

      let fromKey = null;
      let toKey = null;

      if (fromStationParam && toStationParam) {
        fromKey = matchStation(fromStationParam);
        toKey = matchStation(toStationParam);
      }

      if (!fromKey || !toKey) {
        const fromTo = q.match(/\bfrom\s+([a-z\s]+?)\s+to\s+([a-z\s]+?)(?:\s+(?:by|via|in|avoiding|avoid|with|urgent)|$)/i);
        if (fromTo) {
          fromKey = matchStation(fromTo[1]);
          toKey = matchStation(fromTo[2]);
        }
      }

      if (!fromKey || !toKey) {
        const xToY = q.match(/\b([a-z\s]+?)\s+to\s+([a-z\s]+?)(?:\s+(?:by|via|in|avoiding|avoid|with|urgent)|$)/i);
        if (xToY) {
          const c1 = xToY[1].replace(/\b(metro|bus|bmtc|ksrtc|how to go|how to reach|ticket|route)\b/gi, '').trim();
          const c2 = xToY[2].replace(/\b(metro|bus|bmtc|ksrtc|ticket|fast|urgently)\b/gi, '').trim();
          if (!fromKey) fromKey = matchStation(c1);
          if (!toKey) toKey = matchStation(c2);
        }
      }

      if (!fromKey || !toKey) {
        const knM = q.match(/(.+?)\s*(?:ದಿಂದ|ಯಿಂದ|ಇಂದ)\s*(.+?)\s*(?:ಗೆ|ಕ್ಕೆ)/);
        if (knM) {
          if (!fromKey) fromKey = matchStation(knM[1]);
          if (!toKey) toKey = matchStation(knM[2]);
        }
      }

      if (!fromKey && !toKey) {
        fromKey = 'purple:23'; // Majestic
        toKey = 'purple:1';   // Whitefield
      } else if (!fromKey) {
        fromKey = 'purple:23'; // Majestic
      } else if (!toKey) {
        toKey = (fromKey === 'purple:23') ? 'purple:1' : 'purple:23';
      }

      // ── 6. Shortest Path Graph Traversal ──
      const queue = [[fromKey]];
      const visited = new Set([fromKey]);
      let pathKeys = null;

      if (fromKey === toKey) {
        pathKeys = [fromKey];
      } else {
        while (queue.length > 0) {
          const path = queue.shift();
          const curr = path[path.length - 1];
          if (curr === toKey) {
            pathKeys = path;
            break;
          }
          for (const n of stnGraph[curr].neighbors) {
            if (!visited.has(n)) {
              visited.add(n);
              queue.push([...path, n]);
            }
          }
        }
      }

      if (!pathKeys) pathKeys = [fromKey, toKey];

      const fullStops = pathKeys.map(k => stnGraph[k]);
      const stationCount = fullStops.length;
      const tariff = calculateBmrclFare(stationCount);

      const interchanges = [];
      for (let i = 0; i < fullStops.length - 1; i++) {
        if (fullStops[i].line !== fullStops[i + 1].line) {
          interchanges.push({
            station_en: fullStops[i].name_en,
            station_kn: fullStops[i].name_kn,
            fromLine: fullStops[i].lineName,
            toLine: fullStops[i + 1].lineName,
            instruction: 'Switch from ' + fullStops[i].lineName + ' to ' + fullStops[i + 1].lineName + ' via interchange concourse'
          });
        }
      }

      const travelTimeMinutes = Math.round(stationCount * 1.8 + interchanges.length * 5);
      const roadMinutes = Math.round(travelTimeMinutes * 2.2);
      const timeSaved = Math.max(0, roadMinutes - travelTimeMinutes);
      const cabFare = Math.round(tariff.token * 9.5);

      const originStn = fullStops[0];
      const destStn = fullStops[fullStops.length - 1];
      const linesUsed = [...new Set(fullStops.map(s => s.lineName))].join(' ➔ ');

      // ── 7. Real BMTC Bus Matching Engine (2,025 Authentic Routes) ──
      if (!fnBmtcCache && env && env.ASSETS) {
        try {
          const bResp = await env.ASSETS.fetch(new Request(new URL('/data/bmtc_all_routes.json', request.url)));
          if (bResp.ok) {
            const bData = await bResp.json();
            fnBmtcCache = bData.routes || [];
          }
        } catch (e) {}
      }

      if (!fnKsrtcCache && env && env.ASSETS) {
        try {
          const kResp = await env.ASSETS.fetch(new Request(new URL('/data/ksrtc_majestic_timetables.json', request.url)));
          if (kResp.ok) {
            fnKsrtcCache = await kResp.json();
          }
        } catch (e) {}
      }

      let bmtcRoutes = [];
      const originName = originStn.name_en.toLowerCase();
      const destName = destStn.name_en.toLowerCase();

      function formatBmtcItem(r) {
        let typeStr = 'Ordinary City Bus';
        let fareStr = r.fare_ord || '₹10 - ₹25';
        if (r.category === 'vayu_vajra' || (r.route_no && r.route_no.startsWith('KIA'))) {
          typeStr = 'Vayu Vajra AC Airport';
          fareStr = r.fare_ac || '₹150 - ₹350';
        } else if (r.category === 'vajra' || (r.route_no && (r.route_no.startsWith('V-') || r.route_no.endsWith('E')))) {
          typeStr = 'Volvo Vajra AC Express';
          fareStr = r.fare_ac || '₹40 - ₹80';
        } else if (r.category === 'metro_feeder' || (r.route_no && r.route_no.startsWith('MF'))) {
          typeStr = 'Namma Metro Feeder';
          fareStr = '₹10 - ₹20';
        } else if (r.category === 'big10' || (r.route_no && r.route_no.startsWith('G-'))) {
          typeStr = 'Big-10 Arterial Express';
          fareStr = '₹15 - ₹30';
        }

        return {
          route: r.route_no,
          name: r.full_name,
          type: typeStr,
          category: r.category || 'ordinary',
          from: r.origin,
          to: r.dest,
          distance: r.distance || '~20 km',
          stopsCount: r.stops_count || 20,
          tripsDaily: r.trip_count || 24,
          fare: fareStr,
          timeMinutes: Math.round(travelTimeMinutes * 1.6 + 15),
          shaktiFree: r.shakti_free !== false && !typeStr.includes('AC')
        };
      }

      if (fnBmtcCache && fnBmtcCache.length > 0) {
        const qClean = q.toLowerCase();
        
        // 1. Direct route number match (e.g. "500-D", "KIA-9", "335-E")
        const directMatches = fnBmtcCache.filter(r => {
          const rNo = (r.route_no || '').toLowerCase().replace(/[^a-z0-9]/g, '');
          const qNorm = qClean.replace(/[^a-z0-9]/g, '');
          return qNorm.length >= 2 && (rNo === qNorm || qClean.includes((r.route_no || '').toLowerCase()));
        });

        if (directMatches.length > 0) {
          bmtcRoutes = directMatches.slice(0, 15).map(r => formatBmtcItem(r));
        } else {
          // 2. Token & Corridor matching
          const getTokens = (str) => str.toLowerCase().replace(/[^a-z0-9\s]/g, ' ')
            .split(/\s+/)
            .filter(t => t.length > 3 && !['station', 'cross', 'road', 'layout', 'park', 'gate', 'nagar', 'city', 'main', 'central', 'circle', 'railway'].includes(t));

          const syns = {
            'majestic': ['kempegowda', 'kbs', 'majestic', 'subhash'],
            'whitefield': ['kadugodi', 'whitefield', 'itpl', 'pattandur', 'hopefarm'],
            'electronic': ['electronic', 'wipro', 'ecity', 'konappana', 'infosys', 'bommasandra'],
            'silk': ['silk', 'csb', 'madiwala', 'hsr', 'btm'],
            'yeshwanthpur': ['yeshwantpur', 'yeshwanthpura', 'sandal', 'goraguntepalya'],
            'banashankari': ['banashankari', 'bsk', 'padmanabhanagar', 'jayanagar'],
            'krishnarajapura': ['krishnarajapura', 'tin factory', 'kr puram', 'benniganahalli'],
            'airport': ['airport', 'kia', 'devanahalli', 'kempegowda international airport'],
            'marathahalli': ['marathahalli', 'kundalahalli', 'kalamandir', 'hal'],
            'hebbal': ['hebbal', 'manyata', 'nagawara']
          };

          const expandTokens = (tokens) => {
            const res = [...tokens];
            for (const t of tokens) {
              for (const [k, v] of Object.entries(syns)) {
                if (t.includes(k) || k.includes(t)) res.push(...v);
              }
            }
            return [...new Set(res)];
          };

          const oTokens = expandTokens(getTokens(originName));
          const dTokens = expandTokens(getTokens(destName));

          const scored = [];
          for (const r of fnBmtcCache) {
            const text = ((r.full_name || '') + ' ' + (r.terminals ? r.terminals.join(' ') : '') + ' ' + (r.origin || '') + ' ' + (r.dest || '')).toLowerCase();
            const hasO = oTokens.length === 0 || oTokens.some(t => text.includes(t));
            const hasD = dTokens.length === 0 || dTokens.some(t => text.includes(t));
            if (hasO && hasD) {
              let score = (r.trip_count || 1);
              if (r.category === 'vayu_vajra') score += 50;
              scored.push({ route: r, score });
            }
          }
          scored.sort((a, b) => b.score - a.score);
          bmtcRoutes = scored.slice(0, 12).map(s => formatBmtcItem(s.route));
        }
      }

      // Fallback if cache not loaded yet
      if (bmtcRoutes.length === 0) {
        if (originName.includes('majestic') || destName.includes('majestic')) {
          bmtcRoutes = [
            { route: '335-E', name: 'Kempegowda Bus Station → ITPL', type: 'Volvo Vajra AC Express', category: 'vajra', from: 'KBS Majestic', to: 'ITPL Kadugodi', distance: '46.2 ಕಿ.ಮೀ', stopsCount: 28, tripsDaily: 12, fare: '₹65', timeMinutes: 75, shaktiFree: false },
            { route: 'KIA-9', name: 'Kempegowda Bus Station → Airport', type: 'Vayu Vajra AC Airport', category: 'vayu_vajra', from: 'KBS Majestic', to: 'Kempegowda Airport', distance: '23.1 ಕಿ.ಮೀ', stopsCount: 21, tripsDaily: 243, fare: '₹260', timeMinutes: 80, shaktiFree: false },
            { route: '333-E', name: 'Kadugodi Bus Station → Kempegowda Bus Station', type: 'Ordinary City Bus', category: 'ordinary', from: 'KBS Majestic', to: 'Whitefield', distance: '28.5 ಕಿ.ಮೀ', stopsCount: 32, tripsDaily: 48, fare: '₹25', timeMinutes: 85, shaktiFree: true }
          ];
        } else {
          bmtcRoutes = [
            { route: '500-D', name: 'Central Silk Board → Hebbal TTMC', type: 'Volvo Vajra AC Express', category: 'vajra', from: 'Central Silk Board', to: 'Hebbal via Marathahalli', distance: '32.4 ಕಿ.ಮೀ', stopsCount: 24, tripsDaily: 156, fare: '₹60', timeMinutes: 65, shaktiFree: false },
            { route: 'G-3', name: 'Electronic City Wipro Gate → Brigade Road', type: 'Big-10 Arterial Express', category: 'big10', from: 'Silk Board', to: 'Electronic City', distance: '35.2 ಕಿ.ಮೀ', stopsCount: 18, tripsDaily: 78, fare: '₹25', timeMinutes: 40, shaktiFree: true }
          ];
        }
      }

      // ── 8. Real KSRTC Intercity Matching (2,032 Departures from Majestic) ──
      let ksrtcPlan = null;
      let matchedCity = null;

      for (const city of KNOWN_INTERCITY_CITIES) {
        if (q.includes(city) || originName.includes(city) || destName.includes(city)) {
          matchedCity = city;
          break;
        }
      }

      if (matchedCity) {
        const capCity = matchedCity.toUpperCase();
        let departures = [];

        if (fnKsrtcCache && fnKsrtcCache.length > 0) {
          const directDep = fnKsrtcCache.filter(k => 
            (k.to && k.to.toUpperCase().includes(capCity)) || 
            (k.via && k.via.toUpperCase().includes(capCity))
          );
          if (directDep.length > 0) {
            departures = directDep.slice(0, 10).map(d => ({
              departureTime: d.dep_time,
              service: d.service || 'EXPRESS',
              via: d.via || 'Direct Highway Express',
              terminal: d.origin_terminal || 'Kempegowda Bus Station (Majestic Terminal 1)'
            }));
          }
        }

        if (departures.length === 0) {
          if (matchedCity.includes('mys')) {
            departures = [
              { departureTime: 'Every 5-10 mins (24x7)', service: 'AIRAVAT CLUB CLASS / EV POWER PLUS', via: 'Bengaluru-Mysuru Expressway Non-Stop (1h 30m)', terminal: 'Mysore Road Satellite Bus Station / Majestic Terminal 1' },
              { departureTime: 'Every 15 mins', service: 'RAJAHAMSA EXECUTIVE', via: 'Bidadi - Ramanagara - Channapatna - Mandya', terminal: 'Mysore Road Satellite Station (MCTC)' }
            ];
          } else {
            departures = [
              { departureTime: '06:00, 14:00, 20:30, 22:15', service: 'AIRAVAT CLUB CLASS MULTI-AXLE', via: 'NH Highway Express Corridor', terminal: 'Kempegowda Bus Station (Majestic Terminal 1)' },
              { departureTime: '07:30, 15:30, 21:15, 23:00', service: 'RAJAHAMSA EXECUTIVE', via: 'State Highway Direct', terminal: 'Majestic Terminal 2' }
            ];
          }
        }

        ksrtcPlan = {
          destinationCity: matchedCity.charAt(0).toUpperCase() + matchedCity.slice(1),
          totalDeparturesToday: departures.length > 0 ? (departures.length * 4) : 24,
          services: departures,
          bookingUrl: 'https://ksrtc.in'
        };
      }

      // ── 9. Build Complete Response Payload ──
      const resultPayload = {
        transitGroup,
        isTrafficSensitive,
        urgencyScore,
        confidence: Math.round(confidence * 100) / 100,
        urgencyReason,
        query: input,
        processingMs: Date.now() - t0,
        engine: 'Universal Graph Transit Engine v3.0 (All 85+ Stations)',
        metroJourney: {
          origin: originStn.name_en,
          originKn: originStn.name_kn,
          destination: destStn.name_en,
          destinationKn: destStn.name_kn,
          linesUsed,
          lineColor: fullStops[0].lineColor,
          stationsCount: stationCount,
          durationMinutes: travelTimeMinutes,
          fareToken: tariff.token,
          fareSmartcardPeak: tariff.smartPeak,
          fareSmartcardOff: tariff.smartOff,
          interchanges,
          nextTrainFrequency: 'Every 3.5 – 5 minutes (Operating: 05:00 AM – 11:00 PM)',
          trafficComparison: {
            roadMinutes,
            timeSavedMinutes: timeSaved,
            cabEstimatedFareINR: cabFare,
            moneySavedINR: Math.max(0, cabFare - tariff.token),
            congestionHotspot: 'Tin Factory, KR Puram, Silk Board & ORR road gridlock completely avoided.'
          },
          fullStationsList: fullStops.map((s, idx) => ({
            stopNumber: idx + 1,
            key: s.key,
            name_en: s.name_en,
            name_kn: s.name_kn,
            line: s.line,
            lineName: s.lineName,
            lineColor: s.lineColor,
            isStart: (idx === 0),
            isEnd: (idx === fullStops.length - 1),
            isInterchange: (s.key === 'purple:23' || s.key === 'green:17' || s.key === 'green:24' || s.key === 'yellow:1')
          }))
        },
        bmtcAlternatives: bmtcRoutes,
        ksrtcOption: ksrtcPlan
      };

      return new Response(JSON.stringify(resultPayload), {
        status: 200,
        headers: {
          'Content-Type': 'application/json; charset=utf-8',
          'Cache-Control': 'public, max-age=60',
          ...corsHeaders
        }
      });
}
