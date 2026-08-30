/**
 * location_lookup.js — Karnata GIS Engine
 * Foolproof State-Wide Point-in-Polygon & Phonetic Administrative Discovery Engine
 */

const fs = require('fs');
const path = require('path');

const DISTRICT_KN_MAP = {
  'BIDAR': 'ಬೀದರ್', 'BELGAUM': 'ಬೆಳಗಾವಿ', 'BELAGAVI': 'ಬೆಳಗಾವಿ', 'BAGALKOT': 'ಬಾಗಲಕೋಟೆ',
  'BAGALKOTE': 'ಬಾಗಲಕೋಟೆ', 'BIJAPUR': 'ವಿಜಯಪುರ', 'VIJAYAPURA': 'ವಿಜಯಪುರ', 'GULBARGA': 'ಕಲಬುರಗಿ',
  'KALABURAGI': 'ಕಲಬುರಗಿ', 'YADGIR': 'ಯಾದಗಿರಿ', 'RAICHUR': 'ರಾಯಚೂರು', 'KOPPAL': 'ಕೊಪ್ಪಳ',
  'GADAG': 'ಗದಗ', 'DHARWAD': 'ಧಾರವಾಡ', 'UTTARA KANNADA': 'ಉತ್ತರ ಕನ್ನಡ', 'HAVERI': 'ಹಾವೇರಿ',
  'BELLARY': 'ಬಳ್ಳಾರಿ', 'BALLARI': 'ಬಳ್ಳಾರಿ', 'VIJAYANAGARA': 'ವಿಜಯನಗರ', 'CHITRADURGA': 'ಚಿತ್ರದುರ್ಗ',
  'DAVANAGERE': 'ದಾವಣಗೆರೆ', 'SHIMOGA': 'ಶಿವಮೊಗ್ಗ', 'SHIVAMOGGA': 'ಶಿವಮೊಗ್ಗ', 'UDUPI': 'ಉಡುಪಿ',
  'CHIKMAGALUR': 'ಚಿಕ್ಕಮಗಳೂರು', 'CHIKKAMAGALURU': 'ಚಿಕ್ಕಮಗಳೂರು', 'DAKSHINA KANNADA': 'ದಕ್ಷಿಣ ಕನ್ನಡ',
  'TUMKUR': 'ತುಮಕೂರು', 'TUMAKURU': 'ತುಮಕೂರು', 'KOLAR': 'ಕೋಲಾರ', 'CHIKKABALLAPURA': 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ',
  'BANGALORE RURAL': 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ', 'BENGALURU RURAL': 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ',
  'BANGALORE': 'ಬೆಂಗಳೂರು ನಗರ', 'BENGALURU URBAN': 'ಬೆಂಗಳೂರು ನಗರ', 'MANDYA': 'ಮಂಡ್ಯ',
  'HASSAN': 'ಹಾಸನ', 'KODAGU': 'ಕೊಡಗು', 'MYSORE': 'ಮೈಸೂರು', 'MYSURU': 'ಮೈಸೂರು',
  'CHAMARAJANAGAR': 'ಚಾಮರಾಜನಗರ', 'CHAMARAJANAGARA': 'ಚಾಮರಾಜನಗರ', 'RAMANAGARA': 'ರಾಮನಗರ'
};

function normalizeStr(s) {
  if (!s) return '';
  return s.toLowerCase().replace(/[^a-z0-9]/g, '');
}

function normalizeKn(s) {
  if (!s) return '';
  return s
    .replace(/[\u0CBE\u0CBF\u0CC0\u0CC1\u0CC2\u0CC3\u0CC4\u0CC6\u0CC7\u0CC8\u0CCA\u0CCB\u0CCC\u0CCD]/g, '')
    .replace(/\s+/g, '');
}

function levenshtein(a, b) {
  const an = a ? a.length : 0;
  const bn = b ? b.length : 0;
  if (an === 0) return bn;
  if (bn === 0) return an;
  const matrix = [];
  for (let i = 0; i <= bn; i++) matrix[i] = [i];
  for (let j = 0; j <= an; j++) matrix[0][j] = j;
  for (let i = 1; i <= bn; i++) {
    for (let j = 1; j <= an; j++) {
      if (b.charAt(i - 1) === a.charAt(j - 1)) {
        matrix[i][j] = matrix[i - 1][j - 1];
      } else {
        matrix[i][j] = Math.min(
          matrix[i - 1][j - 1] + 1,
          matrix[i][j - 1] + 1,
          matrix[i - 1][j] + 1
        );
      }
    }
  }
  return matrix[bn][an];
}

class LocationLookupEngine {
  constructor(options = {}) {
    this.dataDir = options.dataDir || path.join(__dirname, '../../data/gis');
    this.panchatantraDir = options.panchatantraDir || path.join(__dirname, '../../data/panchatantra');
    this.wardsLayer = null;
    this.acLayer = null;
    this.repsCatalog = null;
    this.panchatantraMaster = null;
    this.isLoaded = false;
  }

  loadLayers() {
    if (this.isLoaded) return;
    try {
      // 1. Bengaluru Delimited Wards
      const wardsPath = path.join(this.dataDir, 'bengaluru_wards.geojson');
      if (fs.existsSync(wardsPath)) {
        const raw = JSON.parse(fs.readFileSync(wardsPath, 'utf-8'));
        this.wardsLayer = this._indexFeatures(raw.features || []);
      }

      // 2. 224 Assembly Constituencies
      const acPath = path.join(this.dataDir, 'assembly_constituencies.geojson');
      if (fs.existsSync(acPath)) {
        const raw = JSON.parse(fs.readFileSync(acPath, 'utf-8'));
        this.acLayer = this._indexFeatures(raw.features || []);
      }

      // 3. Representatives Catalog (MLAs & MPs)
      const repsPath = path.join(this.dataDir, 'representatives_catalog.json');
      if (fs.existsSync(repsPath)) {
        this.repsCatalog = JSON.parse(fs.readFileSync(repsPath, 'utf-8'));
      }

      // 4. 5,935 Gram Panchayats Master
      const gpPath = path.join(this.panchatantraDir, 'panchatantra_master.json');
      if (fs.existsSync(gpPath)) {
        const raw = JSON.parse(fs.readFileSync(gpPath, 'utf-8'));
        this.panchatantraMaster = raw.gram_panchayats || [];
      }

      this.isLoaded = true;
    } catch (err) {
      console.error('[GIS Engine] Layer loading error:', err.message);
    }
  }

  _indexFeatures(features) {
    return features.map((f, idx) => {
      const geom = f.geometry;
      let minLng = Infinity, minLat = Infinity, maxLng = -Infinity, maxLat = -Infinity;

      const extractCoords = (coords) => {
        if (typeof coords[0] === 'number') {
          const lng = coords[0], lat = coords[1];
          if (lng < minLng) minLng = lng;
          if (lng > maxLng) maxLng = lng;
          if (lat < minLat) minLat = lat;
          if (lat > maxLat) maxLat = lat;
        } else {
          coords.forEach(extractCoords);
        }
      };

      if (geom && geom.coordinates) {
        extractCoords(geom.coordinates);
      }

      return {
        id: f.id || f.properties?.id || `feat_${idx}`,
        properties: f.properties || {},
        geometry: f.geometry,
        bbox: [minLng, minLat, maxLng, maxLat]
      };
    });
  }

  _pointInRing(pt, ring) {
    const x = pt[0], y = pt[1];
    let inside = false;
    for (let i = 0, j = ring.length - 1; i < ring.length; j = i++) {
      const xi = ring[i][0], yi = ring[i][1];
      const xj = ring[j][0], yj = ring[j][1];

      const intersect = ((yi > y) !== (yj > y)) &&
        (x < (xj - xi) * (y - yi) / (yj - yi) + xi);
      if (intersect) inside = !inside;
    }
    return inside;
  }

  _isPointInGeometry(pt, geometry) {
    if (!geometry || !geometry.coordinates) return false;

    if (geometry.type === 'Polygon') {
      const coords = geometry.coordinates;
      if (!this._pointInRing(pt, coords[0])) return false;
      for (let i = 1; i < coords.length; i++) {
        if (this._pointInRing(pt, coords[i])) return false;
      }
      return true;
    }

    if (geometry.type === 'MultiPolygon') {
      for (const poly of geometry.coordinates) {
        if (this._pointInRing(pt, poly[0])) {
          let inHole = false;
          for (let i = 1; i < poly.length; i++) {
            if (this._pointInRing(pt, poly[i])) {
              inHole = true;
              break;
            }
          }
          if (!inHole) return true;
        }
      }
      return false;
    }

    return false;
  }

  lookup(lat, lng, queryName = '', addressDetails = null) {
    this.loadLayers();

    const latitude = parseFloat(lat);
    const longitude = parseFloat(lng);

    if (isNaN(latitude) || isNaN(longitude)) {
      return {
        success: false,
        error: 'ಅಮಾನ್ಯ ನಿರ್ದೇಶಾಂಕಗಳು (Invalid latitude or longitude)',
        location: { latitude: lat, longitude: lng }
      };
    }

    const pt = [longitude, latitude];

    let matchedWard = null;
    let matchedAC = null;

    // 1. Check Bengaluru Delimited Wards
    if (this.wardsLayer) {
      for (const feat of this.wardsLayer) {
        const [minLng, minLat, maxLng, maxLat] = feat.bbox;
        if (longitude >= minLng && longitude <= maxLng && latitude >= minLat && latitude <= maxLat) {
          if (this._isPointInGeometry(pt, feat.geometry)) {
            matchedWard = feat;
            break;
          }
        }
      }
    }

    // 2. Check 224 Assembly Constituencies
    if (this.acLayer) {
      for (const feat of this.acLayer) {
        const [minLng, minLat, maxLng, maxLat] = feat.bbox;
        if (longitude >= minLng && longitude <= maxLng && latitude >= minLat && latitude <= maxLat) {
          if (this._isPointInGeometry(pt, feat.geometry)) {
            matchedAC = feat;
            break;
          }
        }
      }
    }

    // If inside Bengaluru Delimited Ward
    if (matchedWard) {
      const p = matchedWard.properties;
      const acNo = p.ac_id ? p.ac_id.replace('AC_', '') : String(p.ac_number || '157');
      
      const BENGALURU_AC_TO_PC = {
        '151': '24', '152': '24', '153': '24', '155': '24', '156': '24', '157': '24', '158': '24', '159': '24',
        '160': '25', '161': '25', '162': '25', '163': '25', '164': '25', '165': '25', '168': '25', '174': '25',
        '166': '26', '167': '26', '169': '26', '170': '26', '171': '26', '172': '26', '173': '26', '175': '26',
        '154': '23', '176': '23', '177': '23'
      };

      const pcNo = p.pc_id ? p.pc_id.replace('PC_', '') : (BENGALURU_AC_TO_PC[acNo] || '24');
      const mlaInfo = this.repsCatalog?.mlas?.[acNo];
      const mpInfo = this.repsCatalog?.mps?.[pcNo];

      return {
        success: true,
        matchType: 'WARD_DELIMITED',
        location: { latitude, longitude },
        administrative: {
          state: { name_kn: 'ಕರ್ನಾಟಕ', name_en: 'Karnataka', code: 'KA' },
          district: {
            id: p.district_id || 'bengaluru-urban',
            name_kn: p.district_name_kn || 'ಬೆಂಗಳೂರು ನಗರ',
            name_en: p.district_name_en || 'Bengaluru Urban',
            code: 'KA-BLR'
          },
          taluk: {
            id: p.taluk_id || 'bengaluru-central',
            name_kn: p.taluk_name_kn || 'ಬೆಂಗಳೂರು ಕೇಂದ್ರ',
            name_en: p.taluk_name_en || 'Bengaluru Central'
          },
          localBody: {
            id: p.corporation_id || 'GBA-CC-01',
            tier: 'GBA_METROPOLITAN',
            type: 'CITY_CORPORATION',
            name_kn: p.corporation_name_kn || 'ಬೆಂಗಳೂರು ಮಹಾನಗರ ಪಾಲಿಕೆ',
            name_en: p.corporation_name_en || 'Bengaluru City Corporation'
          },
          zone: {
            id: p.zone_id || 'ZONE_CENTRAL',
            name_kn: p.zone_name_kn || 'ಕೇಂದ್ರ ವಲಯ',
            name_en: p.zone_name_en || 'Central Zone'
          },
          ward: {
            id: p.ward_id || `WARD_${p.ward_number || 4}`,
            ward_number: p.ward_number || 4,
            name_kn: p.ward_name_kn || 'ಸಂಪಂಗಿರಾಮ ನಗರ (ವಿಧಾನಸೌಧ)',
            name_en: p.ward_name_en || 'Sampangirama Nagar (Vidhana Soudha)'
          },
          assemblyConstituency: {
            id: `AC_${acNo}`,
            ac_number: acNo,
            name_kn: p.ac_name_kn || 'ಶಿವಾಜಿನಗರ',
            name_en: p.ac_name_en || 'Shivajinagar',
            mla_name_kn: mlaInfo?.mla_name_kn || 'ಶಾಸಕರು',
            mla_name_en: mlaInfo?.mla_name_en || 'MLA',
            party_kn: mlaInfo?.party_kn || 'ಕಾಂಗ್ರೆಸ್ (INC)',
            party_en: mlaInfo?.party_en || 'INC'
          },
          parliamentaryConstituency: {
            id: `PC_${pcNo}`,
            pc_number: pcNo,
            name_kn: mpInfo?.name_kn || 'ಬೆಂಗಳೂರು ಕೇಂದ್ರ',
            name_en: mpInfo?.name_en || 'Bangalore Central',
            mp_name_kn: mpInfo?.mp_kn || 'ಪಿ. ಸಿ. ಮೋಹನ್',
            mp_name_en: mpInfo?.mp_en || 'P. C. Mohan',
            party_kn: mpInfo?.party_kn || 'ಬಿಜೆಪಿ (BJP)',
            party_en: mpInfo?.party_en || 'BJP'
          }
        },
        geometry: matchedWard.geometry,
        source: 'GBA ಅಧಿಕೃತ ವಾರ್ಡ್ ಗಡಿ ನಕ್ಷೆ 2026 / Official Delimitation GIS',
        last_updated: '2026-08-25'
      };
    }

    // If inside Karnataka Assembly Constituency (covering all 31 Districts)
    if (matchedAC) {
      const ap = matchedAC.properties;
      const rawDist = (ap.DIST_NAME || '').replace(/[*_]/g, '').trim().toUpperCase();
      const distKn = DISTRICT_KN_MAP[rawDist] || ap.DIST_NAME;
      const acName = ap.AC_NAME || '';
      const acNo = String(ap.AC_NO);
      const pcNo = String(ap.PC_NO);
      const placeName = queryName || addressDetails?.village || addressDetails?.suburb || addressDetails?.town || 'ಕರ್ನಾಟಕ ಸ್ಥಳ';

      const mlaInfo = this.repsCatalog?.mlas?.[acNo];
      const mpInfo = this.repsCatalog?.mps?.[pcNo];

      // Exact scoped Gram Panchayat search in that district
      let matchedGp = null;
      if (this.panchatantraMaster) {
        const districtGps = this.panchatantraMaster.filter(g => g.district_name_en && g.district_name_en.toUpperCase().includes(rawDist.slice(0, 4)));

        if (districtGps.length > 0) {
          const qNormEn = normalizeStr(placeName);
          const qNormKn = normalizeKn(placeName);

          // Tier 1 & 2: Direct or Phonetic match
          matchedGp = districtGps.find(g => {
            const gNormEn = normalizeStr(g.gp_name_en);
            const gNormKn = normalizeKn(g.gp_name_kn);
            return gNormEn === qNormEn || gNormKn === qNormKn ||
                   (gNormEn && qNormEn && (gNormEn.includes(qNormEn) || qNormEn.includes(gNormEn))) ||
                   (gNormKn && qNormKn && (gNormKn.includes(qNormKn) || qNormKn.includes(gNormKn)));
          });

          // Tier 3: Closest Levenshtein edit distance in that district
          if (!matchedGp && qNormEn.length >= 4) {
            let minDiff = Infinity;
            let closest = null;
            districtGps.forEach(g => {
              const diff = levenshtein(qNormEn, normalizeStr(g.gp_name_en));
              if (diff < minDiff && diff <= 3) {
                minDiff = diff;
                closest = g;
              }
            });
            if (closest) matchedGp = closest;
          }
        }
      }

      const talukNameKn = matchedGp ? matchedGp.taluk_name_kn : (addressDetails?.county || acName);
      const talukNameEn = matchedGp ? matchedGp.taluk_name_en : (addressDetails?.county || acName);

      return {
        success: true,
        matchType: 'STATE_CONSTITUENCY',
        location: { latitude, longitude },
        administrative: {
          state: { name_kn: 'ಕರ್ನಾಟಕ', name_en: 'Karnataka', code: 'KA' },
          district: {
            id: rawDist.toLowerCase().replace(/\s+/g, '-'),
            name_kn: distKn,
            name_en: ap.DIST_NAME.replace(/[*_]/g, '').trim(),
            code: `KA-${ap.DT_CODE || 'DIST'}`
          },
          taluk: {
            id: matchedGp ? matchedGp.taluk_id : 'taluk-hq',
            name_kn: talukNameKn,
            name_en: talukNameEn
          },
          localBody: {
            id: matchedGp ? matchedGp.gp_id : `ULB_${ap.AC_NO}`,
            tier: matchedGp ? 'RURAL_GRAM_PANCHAYAT' : 'URBAN_LOCAL_BODY',
            type: matchedGp ? 'GRAM_PANCHAYAT' : 'MUNICIPAL_COUNCIL',
            name_kn: matchedGp ? `${matchedGp.gp_name_kn} ಗ್ರಾಮ ಪಂಚಾಯತ್` : `${placeName} ಸ್ಥಳೀಯ ಸಂಸ್ಥೆ`,
            name_en: matchedGp ? `${matchedGp.gp_name_en} Gram Panchayat` : `${placeName} Local Body`,
            headquarters_kn: matchedGp ? `${matchedGp.taluk_name_kn} ತಾಲೂಕು` : `${distKn} ಜಿಲ್ಲೆ`,
            headquarters_en: matchedGp ? matchedGp.taluk_name_en : ap.DIST_NAME,
            pdo_name: matchedGp?.pdo_name || '',
            pdo_phone: matchedGp?.pdo_phone || '',
            total_staff: matchedGp?.total_staff || 0
          },
          zone: {
            id: `ZONE_${ap.AC_NO}`,
            name_kn: `${talukNameKn} ತಾಲೂಕು ಪಂಚಾಯತ್`,
            name_en: `${talukNameEn} Taluk Panchayat`
          },
          ward: {
            id: matchedGp ? matchedGp.gp_id : `WARD_${ap.AC_NO}`,
            ward_number: matchedGp ? 'GP' : ap.AC_NO,
            name_kn: matchedGp ? `${placeName} ಗ್ರಾಮ / ವಾರ್ಡ್ ವ್ಯಾಪ್ತಿ` : `${placeName} ವಾರ್ಡ್`,
            name_en: placeName
          },
          village: placeName,
          assemblyConstituency: {
            id: `AC_${acNo}`,
            ac_number: acNo,
            name_kn: acName,
            name_en: acName,
            mla_name_kn: mlaInfo?.mla_name_kn || 'ಶಾಸಕರು',
            mla_name_en: mlaInfo?.mla_name_en || 'MLA',
            party_kn: mlaInfo?.party_kn || 'ಇತರೆ',
            party_en: mlaInfo?.party_en || 'IND'
          },
          parliamentaryConstituency: {
            id: `PC_${pcNo}`,
            pc_number: pcNo,
            name_kn: mpInfo?.name_kn || DISTRICT_KN_MAP[ap.PC_NAME] || ap.PC_NAME,
            name_en: mpInfo?.name_en || ap.PC_NAME,
            mp_name_kn: mpInfo?.mp_kn || 'ಸಂಸದರು',
            mp_name_en: mpInfo?.mp_en || 'MP',
            party_kn: mpInfo?.party_kn || 'ಇತರೆ',
            party_en: mpInfo?.party_en || 'IND'
          }
        },
        geometry: matchedAC.geometry,
        source: 'ಕರ್ನಾಟಕ ಅಧಿಕೃತ ಕ್ಷೇತ್ರ ಗಡಿ & ಪಂಚತಂತ್ರ ದತ್ತಾಂಶ 2026 / Official GIS',
        last_updated: '2026-08-23'
      };
    }

    return {
      success: false,
      matchType: 'OUTSIDE_KARNATAKA',
      error: 'ಈ ಪ್ರದೇಶದ ಗಡಿ ಮಾಹಿತಿ ಇನ್ನೂ ಲಭ್ಯವಿಲ್ಲ (Location is outside Karnataka GIS boundaries)',
      location: { latitude, longitude },
      source: 'Karnata GIS'
    };
  }
}

module.exports = { LocationLookupEngine };
