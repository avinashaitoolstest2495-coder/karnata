# -*- coding: utf-8 -*-
import json, os

chunks = [
    r'C:\Users\avina\.gemini\antigravity\brain\eb992232-7e29-44eb-b019-891a87e05063\.system_generated\logs\chunks\transcript_full\00000102.jsonl',
    r'C:\Users\avina\.gemini\antigravity\brain\eb992232-7e29-44eb-b019-891a87e05063\.system_generated\logs\chunks\transcript_full\00000103.jsonl',
    r'C:\Users\avina\.gemini\antigravity\brain\eb992232-7e29-44eb-b019-891a87e05063\.system_generated\logs\chunks\transcript_full\00000104.jsonl',
]

for c in chunks:
    with open(c, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if 'TargetFile' in line and 'scripts/' in line:
                try:
                    obj = json.loads(line)
                    for tc in obj.get('tool_calls', []):
                        args = tc.get('args', {})
                        tf = args.get('TargetFile', '')
                        cc = args.get('CodeContent', '')
                        print(f"TargetFile: {tf} | size: {len(cc)}")
                        with open(os.path.basename(tf), 'w', encoding='utf-8') as out:
                            out.write(cc)
                except: pass
