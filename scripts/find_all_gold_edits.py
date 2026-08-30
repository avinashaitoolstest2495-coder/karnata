# -*- coding: utf-8 -*-
import json, os, glob

all_chunks = sorted(glob.glob(r'C:\Users\avina\.gemini\antigravity\brain\eb992232-7e29-44eb-b019-891a87e05063\.system_generated\logs\chunks\transcript_full\*.jsonl'))

found_writes = []
for c in all_chunks:
    with open(c, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if 'gold-rate.html' in line and 'ReplacementContent' in line:
                try:
                    obj = json.loads(line)
                    for tc in obj.get('tool_calls', []):
                        args = tc.get('args', {})
                        rc = args.get('ReplacementContent', '')
                        if len(rc) > 5000:
                            found_writes.append((c, args.get('Description', ''), len(rc), rc))
                except: pass
            if 'gold-rate.html' in line and 'CodeContent' in line:
                try:
                    obj = json.loads(line)
                    for tc in obj.get('tool_calls', []):
                        args = tc.get('args', {})
                        cc = args.get('CodeContent', '')
                        if len(cc) > 5000:
                            found_writes.append((c, args.get('Description', ''), len(cc), cc))
                except: pass

print(f"Total edits/writes found: {len(found_writes)}")
for idx, (c, desc, sz, content) in enumerate(found_writes):
    print(f"{idx}: {os.path.basename(c)} | {desc} | {sz} bytes")
    with open(f'gold_edit_{idx}.html', 'w', encoding='utf-8') as out:
        out.write(content)
