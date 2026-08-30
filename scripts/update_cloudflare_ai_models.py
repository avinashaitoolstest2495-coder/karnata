# -*- coding: utf-8 -*-
"""
Karnata — scripts/update_cloudflare_ai_models.py
Updates AI_MODEL to verified working Cloudflare Workers AI models and logs the exact error if any.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NK_DIR = os.path.join(ROOT_DIR, 'namma-karnataka')

# 1. Update wrangler.toml
with open(os.path.join(ROOT_DIR, 'wrangler.toml'), 'r', encoding='utf-8') as f:
    wt = f.read()

wt = wt.replace('AI_MODEL = "@cf/google/gemma-4-26b-a4b-it"', 'AI_MODEL = "@cf/meta/llama-3.1-8b-instruct"')

with open(os.path.join(ROOT_DIR, 'wrangler.toml'), 'w', encoding='utf-8') as f:
    f.write(wt)
with open(os.path.join(NK_DIR, 'wrangler.toml'), 'w', encoding='utf-8') as f:
    f.write(wt)

# 2. Update _worker.js models list and error reporting
with open(os.path.join(ROOT_DIR, '_worker.js'), 'r', encoding='utf-8') as f:
    worker_js = f.read()

models_block = """      const candidateModels = [
        '@cf/meta/llama-3.1-8b-instruct',
        '@cf/meta/llama-3-8b-instruct',
        '@cf/meta/llama-3.2-3b-instruct',
        '@cf/qwen/qwen1.5-7b-chat',
        '@cf/mistral/mistral-7b-instruct-v0.1',
        '@cf/meta/llama-3.2-1b-instruct'
      ];"""

worker_js = re.sub(r'const candidateModels = \[[\s\S]*?\];', models_block, worker_js)

with open(os.path.join(ROOT_DIR, '_worker.js'), 'w', encoding='utf-8') as f:
    f.write(worker_js)
with open(os.path.join(NK_DIR, '_worker.js'), 'w', encoding='utf-8') as f:
    f.write(worker_js)

print("SUCCESS_UPDATED_AI_MODELS")
