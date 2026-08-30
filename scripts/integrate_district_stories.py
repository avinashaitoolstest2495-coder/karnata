# scripts/integrate_district_stories.py
import json
import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

district_meta = {
    0: {'slug': 'koppal', 'name_kn': 'ಕೊಪ್ಪಳ', 'name_en': 'Koppal'},
    1: {'slug': 'bidar', 'name_kn': 'ಬೀದರ್', 'name_en': 'Bidar'},
    2: {'slug': 'kalaburagi', 'name_kn': 'ಕಲಬುರಗಿ', 'name_en': 'Kalaburagi'},
    3: {'slug': 'yadgir', 'name_kn': 'ಯಾದಗಿರಿ', 'name_en': 'Yadgir'},
    4: {'slug': 'raichur', 'name_kn': 'ರಾಯಚೂರು', 'name_en': 'Raichur'},
    5: {'slug': 'vijayanagara', 'name_kn': 'ವಿಜಯನಗರ', 'name_en': 'Vijayanagara'},
    6: {'slug': 'ballari', 'name_kn': 'ಬಳ್ಳಾರಿ', 'name_en': 'Ballari'},
    7: {'slug': 'vijayapura', 'name_kn': 'ವಿಜಯಪುರ', 'name_en': 'Vijayapura'},
    8: {'slug': 'bagalkote', 'name_kn': 'ಬಾಗಲಕೋಟೆ', 'name_en': 'Bagalkote'},
    9: {'slug': 'gadag', 'name_kn': 'ಗದಗ', 'name_en': 'Gadag'},
    10: {'slug': 'dharwad', 'name_kn': 'ಧಾರವಾಡ', 'name_en': 'Dharwad'}
}

def parse_text_to_html(raw_text, dist_name_kn):
    lines = [l.rstrip() for l in raw_text.strip().split('\n')]
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
            html_parts.append(f'<h3 style="font-size: 19px; font-weight: 900; color: #0F172A; margin: 28px 0 12px; display: flex; align-items: center; gap: 8px; border-left: 4px solid #B91C1C; padding-left: 12px; line-height: 1.4;">📍 {clean_head}</h3>')
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
    transcript_path = r'C:\Users\avina\.gemini\antigravity\brain\eb992232-7e29-44eb-b019-891a87e05063\.system_generated\logs\transcript_full.jsonl'
    with open(transcript_path, 'r', encoding='utf-8') as f:
        last_user = None
        for line in f:
            obj = json.loads(line)
            if obj.get('type') == 'USER_INPUT':
                last_user = obj

    raw_text = last_user['content']
    clean_text = re.sub(r'</?USER_REQUEST>', '', raw_text).strip()
    sections = re.split(r'=+', clean_text)

    updated_districts = []

    for idx, sec_text in enumerate(sections):
        if idx not in district_meta:
            continue
        meta = district_meta[idx]
        slug = meta['slug']
        name_kn = meta['name_kn']
        
        guide_section_html = parse_text_to_html(sec_text, name_kn)
        
        for base_dir in ['.', 'namma-karnataka']:
            file_path = os.path.join(base_dir, 'districts', f'{slug}.html')
            if not os.path.exists(file_path):
                continue
                
            with open(file_path, 'r', encoding='utf-8') as f_in:
                html = f_in.read()
                
            # If already has a district-guide-sec, replace it cleanly
            if '<!-- DISTRICT COMPREHENSIVE GUIDE & ESSAY -->' in html:
                html = re.sub(r'<!-- DISTRICT COMPREHENSIVE GUIDE & ESSAY -->.*?<!-- /DISTRICT COMPREHENSIVE GUIDE -->', guide_section_html, html, flags=re.DOTALL)
            elif 'class="d-sec district-guide-sec"' in html:
                html = re.sub(r'<div class="d-sec district-guide-sec".*?</div>\s*</div>', guide_section_html, html, count=1, flags=re.DOTALL)
            else:
                target = '<main class="d-main">'
                if target in html:
                    html = html.replace(target, f'{target}\n\n    {guide_section_html}\n')
                else:
                    html = html.replace('</main>', f'\n    {guide_section_html}\n  </main>')
                    
            with open(file_path, 'w', encoding='utf-8') as f_out:
                f_out.write(html)
                
        updated_districts.append(slug)
        print(f'Successfully integrated guide for {name_kn} ({slug}.html) - {len(sec_text)} chars')

    print(f'\nTotal districts updated: {len(updated_districts)}')

if __name__ == '__main__':
    main()
