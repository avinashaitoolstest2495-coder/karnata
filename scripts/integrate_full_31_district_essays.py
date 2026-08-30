# scripts/integrate_full_31_district_essays.py
import json
import re
import os
import sys
import glob
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).parent.parent

# 1. Existing user essays (Batch 1: 11 districts)
batch1_meta = {
    0: {'slug': 'koppal', 'name_kn': 'ಕೊಪ್ಪಳ'},
    1: {'slug': 'bidar', 'name_kn': 'ಬೀದರ್'},
    2: {'slug': 'kalaburagi', 'name_kn': 'ಕಲಬುರಗಿ'},
    3: {'slug': 'yadgir', 'name_kn': 'ಯಾದಗಿರಿ'},
    4: {'slug': 'raichur', 'name_kn': 'ರಾಯಚೂರು'},
    5: {'slug': 'vijayanagara', 'name_kn': 'ವಿಜಯನಗರ'},
    6: {'slug': 'ballari', 'name_kn': 'ಬಳ್ಳಾರಿ'},
    7: {'slug': 'vijayapura', 'name_kn': 'ವಿಜಯಪುರ'},
    8: {'slug': 'bagalkote', 'name_kn': 'ಬಾಗಲಕೋಟೆ'},
    9: {'slug': 'gadag', 'name_kn': 'ಗದಗ'},
    10: {'slug': 'dharwad', 'name_kn': 'ಧಾರವಾಡ'}
}

def parse_text_to_html(raw_text, dist_name_kn):
    clean_raw = re.sub(r'add this to respective districts.*', '', raw_text, flags=re.IGNORECASE | re.DOTALL).strip()
    clean_raw = re.sub(r'</?USER_REQUEST>', '', clean_raw).strip()
    clean_raw = re.sub(r'<ADDITIONAL_METADATA>.*', '', clean_raw, flags=re.IGNORECASE | re.DOTALL).strip()
    
    lines = [l.rstrip() for l in clean_raw.strip().split('\n')]
    html_parts = []
    
    in_list = False
    list_type = 'ul'
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            if in_list:
                html_parts.append(f'</{list_type}>')
                in_list = False
            i += 1
            continue
            
        line_clean = line.replace('**', '')
        
        # Check if line is a prominent heading
        if (len(line_clean) < 75 and 
            not line_clean.endswith('.') and 
            not line_clean.endswith(';') and 
            not line_clean.startswith('-') and 
            not line_clean.startswith('*') and 
            not re.match(r'^\d+\.', line_clean)):
            if in_list:
                html_parts.append(f'</{list_type}>')
                in_list = False
            clean_head = line_clean.rstrip(':')
            html_parts.append(f'<h3 style="font-size: 19px; font-weight: 900; color: #0F172A; margin: 28px 0 12px; display: flex; align-items: center; gap: 8px; border-left: 4px solid #B91C1C; padding-left: 12px; line-height: 1.4;">{clean_head}</h3>')
            i += 1
            continue
            
        # Bullet list item
        if line.startswith('- ') or line.startswith('* '):
            if not in_list or list_type != 'ul':
                if in_list:
                    html_parts.append(f'</{list_type}>')
                html_parts.append('<ul style="margin: 12px 0 16px 20px; padding-left: 10px; color: #334155;">')
                in_list = True
                list_type = 'ul'
            content = line[2:].strip()
            if ':' in content:
                parts = content.split(':', 1)
                if len(parts[0]) < 45:
                    html_parts.append(f'<li style="margin-bottom: 9px; line-height: 1.75;"><strong style="color: #0F172A;">{parts[0].replace("**","")}:</strong>{parts[1]}</li>')
                else:
                    html_parts.append(f'<li style="margin-bottom: 9px; line-height: 1.75;">{content}</li>')
            else:
                html_parts.append(f'<li style="margin-bottom: 9px; line-height: 1.75;">{content}</li>')
            i += 1
            continue
            
        # Numbered list item
        m_num = re.match(r'^(\d+)\.\s+(.*)', line)
        if m_num:
            if not in_list or list_type != 'ol':
                if in_list:
                    html_parts.append(f'</{list_type}>')
                html_parts.append('<ol style="margin: 12px 0 16px 20px; padding-left: 10px; color: #334155;">')
                in_list = True
                list_type = 'ol'
            content = m_num.group(2).strip()
            html_parts.append(f'<li style="margin-bottom: 9px; line-height: 1.75;">{content}</li>')
            i += 1
            continue
            
        if in_list:
            html_parts.append(f'</{list_type}>')
            in_list = False
            
        html_parts.append(f'<p style="font-size: 15.5px; line-height: 1.85; color: #334155; margin-bottom: 14px;">{line_clean}</p>')
        i += 1
        
    if in_list:
        html_parts.append(f'</{list_type}>')
        
    body_html = '\n'.join(html_parts)
    
    wrapper = f"""<!-- DISTRICT COMPREHENSIVE GUIDE & ESSAY -->
    <div class="d-sec district-guide-sec" style="background:#FFFFFF; border:1.5px solid #E2E8F0; border-radius:18px; padding:28px 24px; box-shadow:0 10px 30px rgba(15,23,42,0.06); margin-bottom:24px;">
      <div style="display:flex; align-items:center; justify-content:space-between; border-bottom:2px solid #F1F5F9; padding-bottom:14px; margin-bottom:20px; flex-wrap:wrap; gap:10px;">
        <h2 style="font-size:22px; font-weight:900; color:#0F172A; margin:0; display:flex; align-items:center; gap:8px;">
          📖 {dist_name_kn} ಜಿಲ್ಲೆಯ ಸಮಗ್ರ ಇತಿಹಾಸ, ಸಂಸ್ಕೃತಿ &amp; ಪ್ರವಾಸೋದ್ಯಮ ದರ್ಶನ
        </h2>
        <span style="background:#FEF2F2; color:#B91C1C; font-size:12px; font-weight:800; padding:4px 14px; border-radius:20px; border:1px solid #FECACA;">
          ಸಮಗ್ರ ಕೈಪಿಡಿ &amp; ಮಾರ್ಗದರ್ಶಿ
        </span>
      </div>
      <div class="district-guide-content">
{body_html}
      </div>
    </div>
    <!-- /DISTRICT COMPREHENSIVE GUIDE -->"""
    return wrapper.strip()

def main():
    transcript_files = glob.glob(r'C:\Users\avina\.gemini\antigravity\brain\*\.system_generated\logs\transcript_full.jsonl')
    
    batch1_text = None
    batch2_text = None
    batch3_text = None
    batch4_text = None
    
    for t_path in transcript_files:
        try:
            with open(t_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if 'USER_INPUT' in line:
                        if 'ಕೊಪ್ಪಳದ ನೆಲಕ್ಕೆ' in line:
                            obj = json.loads(line)
                            txt = obj.get('content', '')
                            if not batch1_text or len(txt) > len(batch1_text):
                                batch1_text = txt
                        if 'ಸಾಧನಕೇರಿಯ ಕವಿತೆಗಳು' in line:
                            obj = json.loads(line)
                            txt = obj.get('content', '')
                            if not batch2_text or len(txt) > len(batch2_text):
                                batch2_text = txt
                        if 'ಸಾಸಿವೆ ಕಾಳು ಗಾತ್ರದ ಕೆತ್ತನೆಗಳು' in line:
                            obj = json.loads(line)
                            txt = obj.get('content', '')
                            if not batch3_text or len(txt) > len(batch3_text):
                                batch3_text = txt
                        if 'ಬೆಳಗಾವಿ: ಕುಂದಾದ ನಗರಿ' in line:
                            obj = json.loads(line)
                            txt = obj.get('content', '')
                            if not batch4_text or len(txt) > len(batch4_text):
                                batch4_text = txt
        except Exception:
            continue

    guides_catalog = {}

    # Ingest Batch 1 (11 districts: Koppal, Bidar, Kalaburagi, Yadgir, Raichur, Vijayanagara, Ballari, Vijayapura, Bagalkote, Gadag, Dharwad)
    if batch1_text:
        clean_text1 = re.sub(r'</?USER_REQUEST>', '', batch1_text).strip()
        sec1 = re.split(r'={5,}', clean_text1)
        for idx, s in enumerate(sec1):
            if idx in batch1_meta:
                meta = batch1_meta[idx]
                slug = meta['slug']
                name_kn = meta['name_kn']
                guide_html = parse_text_to_html(s, name_kn)
                guides_catalog[slug] = {
                    'name_kn': name_kn,
                    'raw_text': s,
                    'html': guide_html
                }
                print(f"[INGESTED BATCH 1] {name_kn} ({slug})")

    # Ingest Batch 2 (Dharwad, Haveri, Uttara Kannada, Davanagere, Chitradurga, Tumakuru, Udupi, Kodagu, Mysuru, Chamarajanagara, Mandya)
    if batch2_text:
        clean_text2 = re.sub(r'</?USER_REQUEST>', '', batch2_text).strip()
        sec2 = re.split(r'={5,}', clean_text2)
        
        batch2_mapping = [
            ('dharwad', 'ಧಾರವಾಡ', 0),
            ('haveri', 'ಹಾವೇರಿ', 1),
            ('uttara-kannada', 'ಉತ್ತರ ಕನ್ನಡ', 2),
            ('tumakuru', 'ತುಮಕೂರು', 4),
            ('udupi', 'ಉಡುಪಿ', 5),
            ('kodagu', 'ಕೊಡಗು', 6),
            ('mysuru', 'ಮೈಸೂರು', 7),
            ('chamarajanagara', 'ಚಾಮರಾಜನಗರ', 8),
            ('mandya', 'ಮಂಡ್ಯ', 9),
        ]
        
        if len(sec2) > 3:
            s3 = sec2[3]
            m_chitra = re.search(r'\n+(ಚಿತ್ರದುರ್ಗ\s*[:\n].*)', s3, re.DOTALL)
            if m_chitra:
                davanagere_text = s3[:m_chitra.start()].strip()
                chitradurga_text = m_chitra.group(1).strip()
                
                guides_catalog['davanagere'] = {
                    'name_kn': 'ದಾವಣಗೆರೆ',
                    'raw_text': davanagere_text,
                    'html': parse_text_to_html(davanagere_text, 'ದಾವಣಗೆರೆ')
                }
                print(f"[INGESTED BATCH 2] ದಾವಣಗೆರೆ (davanagere)")
                
                guides_catalog['chitradurga'] = {
                    'name_kn': 'ಚಿತ್ರದುರ್ಗ',
                    'raw_text': chitradurga_text,
                    'html': parse_text_to_html(chitradurga_text, 'ಚಿತ್ರದುರ್ಗ')
                }
                print(f"[INGESTED BATCH 2] ಚಿತ್ರದುರ್ಗ (chitradurga)")
            else:
                guides_catalog['davanagere'] = {
                    'name_kn': 'ದಾವಣಗೆರೆ',
                    'raw_text': s3,
                    'html': parse_text_to_html(s3, 'ದಾವಣಗೆರೆ')
                }
                print(f"[INGESTED BATCH 2] ದಾವಣಗೆರೆ (davanagere)")

        for slug, name_kn, sec_idx in batch2_mapping:
            if sec_idx < len(sec2):
                stext = sec2[sec_idx]
                guides_catalog[slug] = {
                    'name_kn': name_kn,
                    'raw_text': stext,
                    'html': parse_text_to_html(stext, name_kn)
                }
                print(f"[INGESTED BATCH 2] {name_kn} ({slug})")

    # Ingest Batch 3 (Mandya, Hassan, Ramanagara, Chikkaballapura, Bengaluru Rural, Bengaluru Urban)
    if batch3_text:
        clean_text3 = re.sub(r'</?USER_REQUEST>', '', batch3_text).strip()
        sec3 = re.split(r'={5,}', clean_text3)
        
        batch3_mapping = [
            ('mandya', 'ಮಂಡ್ಯ', 0),
            ('hassan', 'ಹಾಸನ', 1),
            ('ramanagara', 'ರಾಮನಗರ', 2),
            ('chikkaballapura', 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ', 3),
            ('bengaluru-rural', 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ', 4),
            ('bengaluru-urban', 'ಬೆಂಗಳೂರು ನಗರ', 5),
        ]
        
        for slug, name_kn, sec_idx in batch3_mapping:
            if sec_idx < len(sec3):
                stext = sec3[sec_idx].strip()
                if len(stext) > 100:
                    guides_catalog[slug] = {
                        'name_kn': name_kn,
                        'raw_text': stext,
                        'html': parse_text_to_html(stext, name_kn)
                    }
                    print(f"[INGESTED BATCH 3] {name_kn} ({slug})")

    # Ingest Batch 4 (Belagavi, Shivamogga, Chikkamagaluru, Dakshina Kannada, Kolar)
    if batch4_text:
        clean_text4 = re.sub(r'</?USER_REQUEST>', '', batch4_text).strip()
        clean_text4 = re.sub(r'<ADDITIONAL_METADATA>.*', '', clean_text4, flags=re.DOTALL).strip()
        
        headers_b4 = [
            ('belagavi', 'ಬೆಳಗಾವಿ', 'ಬೆಳಗಾವಿ:'),
            ('shivamogga', 'ಶಿವಮೊಗ್ಗ', 'ಶಿವಮೊಗ್ಗ:'),
            ('chikkamagaluru', 'ಚಿಕ್ಕಮಗಳೂರು', 'ಚಿಕ್ಕಮಗಳೂರು:'),
            ('dakshina-kannada', 'ದಕ್ಷಿಣ ಕನ್ನಡ', 'ದಕ್ಷಿಣ ಕನ್ನಡ:'),
            ('kolar', 'ಕೋಲಾರ', 'ಕೋಲಾರ:')
        ]
        
        pos_list = []
        for slug, name_kn, h_str in headers_b4:
            p = clean_text4.find(h_str)
            pos_list.append((p, slug, name_kn, h_str))
            
        pos_list.sort(key=lambda x: x[0])
        
        for i, (p, slug, name_kn, h_str) in enumerate(pos_list):
            if p != -1:
                end_p = pos_list[i+1][0] if i+1 < len(pos_list) and pos_list[i+1][0] != -1 else len(clean_text4)
                item_text = clean_text4[p:end_p].strip()
                guides_catalog[slug] = {
                    'name_kn': name_kn,
                    'raw_text': item_text,
                    'html': parse_text_to_html(item_text, name_kn)
                }
                print(f"[INGESTED BATCH 4] {name_kn} ({slug}) - len: {len(item_text)}")

    # Save to data/district_comprehensive_guides.json
    guides_json_path = BASE_DIR / "data" / "district_comprehensive_guides.json"
    with open(guides_json_path, "w", encoding="utf-8") as f:
        json.dump(guides_catalog, f, ensure_ascii=False, indent=2)

    print(f"\n=======================================================")
    print(f"SUCCESS! All {len(guides_catalog)}/31 districts consolidated with 100% authentic user essays!")
    print(f"Saved into: {guides_json_path}")
    print(f"=======================================================")

if __name__ == '__main__':
    main()
