# -*- coding: utf-8 -*-
import glob, json, os

chunks = sorted(glob.glob(r'C:\Users\avina\.gemini\antigravity\brain\eb992232-7e29-44eb-b019-891a87e05063\.system_generated\logs\chunks\transcript_full\*.jsonl'), reverse=True)
print('Total chunks:', len(chunks))

found = []
for c in chunks:
    try:
        with open(c, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if 'TargetFile' in line and 'gold-rate.html' in line:
                    try:
                        obj = json.loads(line)
                        for tc in obj.get('tool_calls', []):
                            args = tc.get('args', {})
                            if 'gold-rate.html' in args.get('TargetFile', ''):
                                code = args.get('CodeContent', '')
                                if len(code) > 20000:
                                    found.append((c, code))
                    except Exception as e:
                        pass
    except Exception as e:
        pass

print('Total matching code writes found:', len(found))
if found:
    found.sort(key=lambda x: len(x[1]), reverse=True)
    best_chunk, best_code = found[0]
    print(f'Best match from {best_chunk} with length {len(best_code)}')
    with open('perfect_yesterday_gold.html', 'w', encoding='utf-8') as out:
        out.write(best_code)
    print("SUCCESS: Wrote perfect_yesterday_gold.html")
else:
    print("No code write found directly. Searching for file viewing chunks...")
    for c in chunks:
        try:
            with open(c, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    if 'File Path: `file:///c:/Users/avina/Downloads/karnata-site-with-cms/gold-rate.html`' in line:
                        print('Found view_file output in chunk:', c)
        except: pass
