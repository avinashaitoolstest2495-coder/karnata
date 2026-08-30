# -*- coding: utf-8 -*-
import json, os

chunks = [
    r'C:\Users\avina\.gemini\antigravity\brain\eb992232-7e29-44eb-b019-891a87e05063\.system_generated\logs\chunks\transcript_full\00000135.jsonl',
    r'C:\Users\avina\.gemini\antigravity\brain\eb992232-7e29-44eb-b019-891a87e05063\.system_generated\logs\chunks\transcript_full\00000136.jsonl',
    r'C:\Users\avina\.gemini\antigravity\brain\eb992232-7e29-44eb-b019-891a87e05063\.system_generated\logs\chunks\transcript_full\00000137.jsonl',
    r'C:\Users\avina\.gemini\antigravity\brain\eb992232-7e29-44eb-b019-891a87e05063\.system_generated\logs\chunks\transcript_full\00000138.jsonl',
]

snippets = []
for c in chunks:
    with open(c, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if 'File Path: `file:///c:/Users/avina/Downloads/karnata-site-with-cms/gold-rate.html`' in line:
                try:
                    obj = json.loads(line)
                    content = obj.get('content', '')
                    snippets.append((c, content))
                except: pass

print('Total snippets found:', len(snippets))
for idx, (c, snip) in enumerate(snippets):
    print(f'Snippet {idx} from {os.path.basename(c)}: {len(snip)} chars')
    with open(f'gold_snip_{idx}.txt', 'w', encoding='utf-8') as out:
        out.write(snip)
