"""
Official IMD Karnataka District Vector Map Builder.
Converts the official IMD MC Bengaluru GeoJSON (data/gis/imd_karnataka_districts.geojson)
into precision SVG vector paths with accurate Kannada district labels.
"""

import json
import math
import sys
from pathlib import Path
from shapely.geometry import shape

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parent.parent

IMD_MAP_DIST_INFO = {
    'BAGALKOT': ('bagalkote', 'ಬಾಗಲಕೋಟೆ', 'Bagalkote', 'ಬಾಗಲಕೋಟೆ'),
    'BALLARI': ('ballari', 'ಬಳ್ಳಾರಿ', 'Ballari', 'ಬಳ್ಳಾರಿ'),
    'BELAGAVI': ('belagavi', 'ಬೆಳಗಾವಿ', 'Belagavi', 'ಬೆಳಗಾವಿ'),
    'BENGALURU RURAL': ('bengaluru_rural', 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ', 'Bengaluru Rural', 'ಬೆಂ.ಗ್ರಾಮಾಂತರ'),
    'BENGALURU URBAN': ('bengaluru_urban', 'ಬೆಂಗಳೂರು ನಗರ', 'Bengaluru Urban', 'ಬೆಂಗಳೂರು'),
    'BIDAR': ('bidar', 'ಬೀದರ್', 'Bidar', 'ಬೀದರ್'),
    'CHAMARAJANAGAR': ('chamarajanagara', 'ಚಾಮರಾಜನಗರ', 'Chamarajanagar', 'ಚಾಮರಾಜನಗರ'),
    'CHIK BALLAPUR': ('chikkaballapura', 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', 'Chikkaballapura', 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ'),
    'CHIKKAMAGALURU': ('chikkamagaluru', 'ಚಿಕ್ಕಮಗಳೂರು', 'Chikkamagaluru', 'ಚಿಕ್ಕಮಗಳೂರು'),
    'CHITRADURGA': ('chitradurga', 'ಚಿತ್ರದುರ್ಗ', 'Chitradurga', 'ಚಿತ್ರದುರ್ಗ'),
    'DAKSHINA  KANNADA': ('dakshina_kannada', 'ದಕ್ಷಿಣ ಕನ್ನಡ', 'Dakshina Kannada', 'ಮಂಗಳೂರು'),
    'DAVANGERE': ('davanagere', 'ದಾವಣಗೆರೆ', 'Davanagere', 'ದಾವಣಗೆರೆ'),
    'DHARWAD': ('dharwad', 'ಧಾರವಾಡ', 'Dharwad', 'ಧಾರವಾಡ'),
    'GADAG': ('gadag', 'ಗದಗ', 'Gadag', 'ಗದಗ'),
    'HASSAN': ('hassan', 'ಹಾಸನ', 'Hassan', 'ಹಾಸನ'),
    'HAVERI': ('haveri', 'ಹಾವೇರಿ', 'Haveri', 'ಹಾವೇರಿ'),
    'KALABURAGI': ('kalaburagi', 'ಕಲಬುರಗಿ', 'Kalaburagi', 'ಕಲಬುರಗಿ'),
    'KODAGU': ('kodagu', 'ಕೊಡಗು', 'Kodagu', 'ಕೊಡಗು'),
    'KOLAR': ('kolar', 'ಕೋಲಾರ', 'Kolar', 'ಕೋಲಾರ'),
    'KOPPAL': ('koppal', 'ಕೊಪ್ಪಳ', 'Koppal', 'ಕೊಪ್ಪಳ'),
    'MANDYA': ('mandya', 'ಮಂಡ್ಯ', 'Mandya', 'ಮಂಡ್ಯ'),
    'MYSURU': ('mysuru', 'ಮೈಸೂರು', 'Mysuru', 'ಮೈಸೂರು'),
    'RAICHUR': ('raichur', 'ರಾಯಚೂರು', 'Raichur', 'ರಾಯಚೂರು'),
    'RAMANAGARAM': ('ramanagara', 'ರಾಮನಗರ', 'Ramanagara', 'ರಾಮನಗರ'),
    'SHIVAMOGGA': ('shivamogga', 'ಶಿವಮೊಗ್ಗ', 'Shivamogga', 'ಶಿವಮೊಗ್ಗ'),
    'TUMAKURU': ('tumakuru', 'ತುಮಕೂರು', 'Tumakuru', 'ತುಮಕೂರು'),
    'UDUPI': ('udupi', 'ಉಡುಪಿ', 'Udupi', 'ಉಡುಪಿ'),
    'UTTARA  KANNADA': ('uttara_kannada', 'ಉತ್ತರ ಕನ್ನಡ', 'Uttara Kannada', 'ಕಾರವಾರ'),
    'VIJAYAPURA': ('vijayapura', 'ವಿಜಯಪುರ', 'Vijayapura', 'ವಿಜಯಪುರ'),
    'VIJAYANAGARA': ('vijayanagara', 'ವಿಜಯನಗರ', 'Vijayanagara', 'ವಿಜಯನಗರ'),
    'YADGIR': ('yadgir', 'ಯಾದಗಿರಿ', 'Yadgir', 'ಯಾದಗಿರಿ')
}

def build_precision_map():
    geojson_path = ROOT_DIR / "data" / "gis" / "imd_karnataka_districts.geojson"
    if not geojson_path.exists():
        raise FileNotFoundError(f"IMD GeoJSON not found at {geojson_path}")

    with open(geojson_path, "r", encoding="utf-8") as f:
        geo = json.load(f)

    min_lon, min_lat, max_lon, max_lat = 180, 90, -180, -90
    geoms = {}
    for feat in geo['features']:
        dname = feat['properties']['DISTRICT']
        g = shape(feat['geometry'])
        geoms[dname] = g
        b = g.bounds
        min_lon = min(min_lon, b[0])
        min_lat = min(min_lat, b[1])
        max_lon = max(max_lon, b[2])
        max_lat = max(max_lat, b[3])

    view_w = 880
    view_h = 1200
    pad = 20
    usable_w = view_w - 2 * pad
    usable_h = view_h - 2 * pad

    mid_lat = (min_lat + max_lat) / 2.0
    cos_lat = math.cos(math.radians(mid_lat))

    geo_w = (max_lon - min_lon) * cos_lat
    geo_h = max_lat - min_lat

    scale = min(usable_w / geo_w, usable_h / geo_h)
    offset_x = pad + (usable_w - geo_w * scale) / 2.0
    offset_y = pad + (usable_h - geo_h * scale) / 2.0

    def project(lon, lat):
        x = offset_x + (lon - min_lon) * cos_lat * scale
        y = offset_y + (max_lat - lat) * scale
        return round(x, 1), round(y, 1)

    def geom_to_path(g):
        parts = []
        polys = [g] if g.geom_type == 'Polygon' else list(g.geoms)
        for p in polys:
            coords = list(p.exterior.coords)
            if len(coords) < 3: continue
            pts = [project(lon, lat) for lon, lat in coords]
            parts.append('M ' + ' L '.join(f'{x} {y}' for x, y in pts) + ' Z')
            for interior in p.interiors:
                icoords = list(interior.coords)
                if len(icoords) < 3: continue
                ipts = [project(lon, lat) for lon, lat in icoords]
                parts.append('M ' + ' L '.join(f'{x} {y}' for x, y in ipts) + ' Z')
        return ' '.join(parts)

    LABEL_OFFSETS = {
        'bengaluru_urban': (0, -4),
        'bengaluru_rural': (30, -25),
        'ramanagara': (-10, 8),
        'kolar': (12, 0),
        'chikkaballapura': (12, -8),
        'tumakuru': (8, 0),
        'chamarajanagara': (12, 10),
        'dakshina_kannada': (5, 5),
        'udupi': (-5, 0),
        'uttara_kannada': (8, 0),
        'vijayanagara': (-5, 0)
    }

    districts_list = []
    for dname, g in geoms.items():
        info = IMD_MAP_DIST_INFO.get(dname)
        if not info:
            continue
        dist_id, dist_kn, dist_en, short_label = info
        path_d = geom_to_path(g)
        rep = g.representative_point()
        cx, cy = project(rep.x, rep.y)
        
        ox, oy = LABEL_OFFSETS.get(dist_id, (0, 0))
        cx += ox
        cy += oy
        
        districts_list.append({
            'imd_name': dname,
            'id': dist_id,
            'name_kn': dist_kn,
            'name_en': dist_en,
            'short_label': short_label,
            'path_d': path_d,
            'cx': round(cx, 1),
            'cy': round(cy, 1)
        })

    out_json = {
        'viewBox': f'0 0 {view_w} {view_h}',
        'districts': districts_list
    }

    target_paths = [
        ROOT_DIR / "data" / "gis" / "karnataka_districts_precision.json",
        ROOT_DIR / "namma-karnataka" / "data" / "gis" / "karnataka_districts_precision.json"
    ]
    for tp in target_paths:
        tp.parent.mkdir(parents=True, exist_ok=True)
        with open(tp, "w", encoding="utf-8") as f:
            json.dump(out_json, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated {len(districts_list)} districts from IMD shapefile!")

if __name__ == "__main__":
    build_precision_map()
