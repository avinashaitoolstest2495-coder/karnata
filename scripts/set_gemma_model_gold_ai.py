# -*- coding: utf-8 -*-
"""
Karnata — scripts/set_gemma_model_gold_ai.py
Sets @cf/google/gemma-4-26b-a4b-it as the primary AI model for /api/gold-ai and /api/ask-ai,
with robust Kannada-first prompt engineering and flawless fallback.
"""

with open("_worker.js", "r", encoding="utf-8") as f:
    worker_code = f.read()

# Update /api/gold-ai candidate models to prioritize @cf/google/gemma-4-26b-a4b-it
worker_code = worker_code.replace(
    """        const candidateModels = [
          '@cf/meta/llama-3.1-8b-instruct',
          '@cf/qwen/qwen1.5-7b-chat',
          '@cf/mistral/mistral-7b-instruct-v0.1'
        ];""",
    """        const candidateModels = [
          env.AI_MODEL || '@cf/google/gemma-4-26b-a4b-it',
          '@cf/google/gemma-4-26b-a4b-it',
          '@cf/meta/llama-3.1-8b-instruct',
          '@cf/google/gemma-7b-it-lora',
          '@cf/qwen/qwen1.5-7b-chat'
        ];"""
)

# Enhance system prompt for Gemma to ensure high quality pure Kannada
old_prompt = """const goldSystemPrompt = `You are the Karnataka Gold & Commodity Market Intelligence AI Expert on Karnata.in.
Current Spot Rates: 24K Gold: ₹16,304/gram, 22K Gold: ₹14,940/gram (₹1,19,520/pavan), 999 Silver: ₹260.00/gram.
10-Year Historical CAGR: +18.9% (2016: ₹2,862/g -> 2026: ₹16,304/g).
Seasonality: August-Sept is Pre-Festive Dip (Best accumulation window). Diwali/Dhanteras brings 3.5%-6% price surge. Ugadi/Akshaya Tritiya brings 3%-5% surge.
Answer the user question thoroughly and respectfully in clean, structured, natural Kannada (ಕನ್ನಡ) with markdown bold headings and bullet points. Include realistic price projection numbers and clear buying/selling strategy.`;"""

new_prompt = """const goldSystemPrompt = `ನೀವು Karnata.in ನ ಅಧಿಕೃತ ಕರ್ನಾಟಕ ಚಿನ್ನ & ಕಮಾಡಿಟಿ ಮಾರುಕಟ್ಟೆ AI ವಿಶ್ಲೇಷಕರು.
ಇಂದಿನ ದರಗಳು: 24K ಅಪರಂಜಿ ಚಿನ್ನ: ₹16,304/ಗ್ರಾಂ (₹1,63,040/10g), 22K ಆಭರಣ ಬಂಗಾರ: ₹14,940/ಗ್ರಾಂ (₹1,19,520/1 ಪವನ್), 999 ಶುದ್ಧ ಬೆಳ್ಳಿ: ₹260.00/ಗ್ರಾಂ.
10-ವರ್ಷಗಳ CAGR: +18.9% (2016 ರಲ್ಲಿ ₹2,862/ಗ್ರಾಂ ಇದ್ದದ್ದು ಇಂದು ₹16,304).
ಮುನ್ಸೂಚನೆ: 2027 ಕ್ಕೆ ₹18,500 - ₹19,800/ಗ್ರಾಂ, 2030 ಕ್ಕೆ ₹24,000 - ₹27,000/ಗ್ರಾಂ.
ಸೀಸನ್: ದೀಪಾವಳಿ & ಧಂತೇರಸ್‌ಗೆ 3.5% - 6% ಏರಿಕೆ, ಯುಗಾದಿ & ಅಕ್ಷಯ ತೃತೀಯಕ್ಕೆ 3% - 5% ಏರಿಕೆ.
ಬಳಕೆದಾರರ ಪ್ರಶ್ನೆಗೆ ಕೇವಲ ಶುದ್ಧ, ಸುಲಲಿತ ಮತ್ತು ಸ್ಪಷ್ಟ ಕನ್ನಡದಲ್ಲಿ (Pure Kannada only) 3 ಪ್ರಮುಖ ವಿಭಾಗಗಳಲ್ಲಿ (1. ಐತಿಹಾಸಿಕ ವಿಶ್ಲೇಷಣೆ, 2. ನಿಖರ ಬೆಲೆ ಮುನ್ಸೂಚನೆ, 3. ಸ್ಮಾರ್ಟ್ ತಂತ್ರ) ಬೋಲ್ಡ್ ಹೆಡಿಂಗ್ಸ್ ಹಾಗೂ ಬುಲೆಟ್ ಪಾಯಿಂಟ್‌ಗಳೊಂದಿಗೆ ಉತ್ತರಿಸಿ. ಯಾವುದೇ ಇಂಗ್ಲಿಷ್ ಅನುವಾದ ಅಥವಾ ಅಸ್ಪಷ್ಟ ಪದಗಳನ್ನು ಬಳಸಬೇಡಿ.`;"""

worker_code = worker_code.replace(old_prompt, new_prompt)

with open("_worker.js", "w", encoding="utf-8") as f:
    f.write(worker_code)

with open("namma-karnataka/_worker.js", "w", encoding="utf-8") as f:
    f.write(worker_code)

print("SUCCESS_CONFIGURED_GEMMA_MODEL")
