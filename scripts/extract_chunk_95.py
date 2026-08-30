# -*- coding: utf-8 -*-
import json, os

chunk_95 = r'C:\Users\avina\.gemini\antigravity\brain\eb992232-7e29-44eb-b019-891a87e05063\.system_generated\logs\chunks\transcript_full\00000095.jsonl'

with open(chunk_95, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        if 'TargetFile' in line and 'scripts/' in line:
            try:
                obj = json.loads(line)
                for tc in obj.get('tool_calls', []):
                    args = tc.get('args', {})
                    tf = args.get('TargetFile', '')
                    cc = args.get('CodeContent', '')
                    print(f"Found script in chunk 95: {tf} | size: {len(cc)}")
                    with open('script_from_chunk_95.py', 'w', encoding='utf-8') as out:
                        out.write(cc)
            except: pass
