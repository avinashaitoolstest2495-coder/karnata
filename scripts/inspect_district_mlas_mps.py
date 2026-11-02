# -*- coding: utf-8 -*-
import sys
import glob
import re
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

files = sorted(glob.glob('districts/*.html'))
print(f"Total district html files: {len(files)}")

district_reps = {}

for f in files:
    if 'index.html' in f:
        continue
    slug = f.replace('\\', '/').split('/')[-1].replace('.html', '')
    html = open(f, encoding='utf-8').read()
    
    # Extract MP
    mp_sec = re.findall(r'<!-- 2\. REPRESENTATIVES: MPS & MLAS -->([\s\S]*?)<!-- 3\.', html)
    if not mp_sec:
        mp_sec = re.findall(r'ಲೋಕಸಭಾ ಸಂಸದರು([\s\S]*?)ಶಾಸಕರು', html)

    # Find rep cards
    cards = re.findall(r'<div class="d-big-rep-card"[^>]*>([\s\S]*?)</div>\s*</div>\s*</div>', html)
    # also check img tags in file
    mp_imgs = re.findall(r'/assets/images/mps/[^"]+', html)
    mla_imgs = re.findall(r'/assets/images/mlas/[^"]+', html)
    
    district_reps[slug] = {
        "mp_imgs": len(mp_imgs),
        "mla_imgs": len(mla_imgs),
        "total_cards": len(cards)
    }

print("Sample districts representative image counts:")
for k in list(district_reps.keys())[:10]:
    print(f"  {k:18} -> MP imgs: {district_reps[k]['mp_imgs']}, MLA imgs: {district_reps[k]['mla_imgs']}")
