# -*- coding: utf-8 -*-
import glob
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

total_mlas = 0
total_mps = 0
files = sorted(glob.glob('districts/*.html'))

print(f"{'District':20} | {'MPs':3} | {'MLAs':4} | {'MP Name & Party':35} | Sample MLAs")
print("-" * 90)

for f in files:
    if 'index.html' in f:
        continue
    slug = f.replace('\\', '/').split('/')[-1].replace('.html', '')
    c = open(f, encoding='utf-8').read()
    
    # Extract MP
    mp_names = re.findall(r'<div style="font-size:18px; font-weight:900; color:#0F172A; line-height:1.3; margin-bottom:3px;">([^<]+)</div>', c)
    mp_parties = re.findall(r'🗳️ ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ:[\s\S]*?<span class="d-party-tag [^"]*">([^<]+)</span>', c)
    
    # Extract MLAs
    mla_names = re.findall(r'<div style="font-size:17.5px; font-weight:900; color:#0F172A; line-height:1.3; margin-bottom:3px;">([^<]+)</div>', c)
    mla_consts = re.findall(r'🏛️\s*([^\n<]+)[\s\S]*?class="d-party-tag', c)
    
    total_mlas += len(mla_names)
    total_mps += len(mp_names)
    
    mp_desc = f"{mp_names[0]} ({mp_parties[0]})" if mp_names and mp_parties else (mp_names[0] if mp_names else "None")
    sample_mlas = ", ".join(mla_names[:3])
    print(f"{slug:20} | {len(mp_names):3} | {len(mla_names):4} | {mp_desc:35} | {sample_mlas}")

print("-" * 90)
print(f"TOTAL: {len(files)-1} Districts | Total MPs: {total_mps} | Total MLAs: {total_mlas}")
