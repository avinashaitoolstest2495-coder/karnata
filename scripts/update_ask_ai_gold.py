import os
import re

def update_ask_ai_engine():
    paths = ['ask-ai-engine.js', 'namma-karnataka/ask-ai-engine.js']
    for p in paths:
        if not os.path.exists(p):
            continue
        with open(p, 'r', encoding='utf-8') as f:
            code = f.read()

        # Update answerGoldQuery initialization
        old_init = """    const goldData = db.gold || {};
    const baseGold = goldData.baseGold || { 24: 13942, 22: 12775, 18: 10455, 14: 8230 };
    const yesterdayGold = goldData.yesterdayGold || { 24: 13893, 22: 12730, 18: 10418, 14: 8415 };
    const baseSilver = goldData.baseSilver || { 999: 264.86, 925: 245.00 };
    const yesterdaySilver = goldData.yesterdaySilver || { 999: 258.50, 925: 239.00 };
    const changes = goldData.changes || { '24k': -1, '22k': -1, 'silver_999': -0.10 };
    const yearlyList = goldData.yearly_1901_2026 || [];

    const r24k_1g = baseGold[24] || 15496;
    const r22k_1g = baseGold[22] || 14204;
    const r18k_1g = baseGold[18] || 11622;
    const r14k_1g = baseGold[14] || 9050;
    const rSilver_1g = baseSilver[999] || 244.90;
    const rSilver925_1g = baseSilver[925] || 226.53;

    const y24k_1g = yesterdayGold[24] || 15497;
    const y22k_1g = yesterdayGold[22] || 14205;
    const ySilver_1g = yesterdaySilver[999] || 245.00;"""

        new_init = """    const goldData = db.gold || {};
    const baseGold = goldData.baseGold || { '24': 13942, '22': 12775, '18': 10455, '14': 8230 };
    const yesterdayGold = goldData.yesterdayGold || { '24': 13893, '22': 12730, '18': 10418, '14': 8415 };
    const baseSilver = goldData.baseSilver || { '999': 264.86, '925': 245.00 };
    const yesterdaySilver = goldData.yesterdaySilver || { '999': 263.97, '925': 244.18 };
    const changes = goldData.changes || { '24k': 49, '22k': 45, '18k': 37, 'silver_999': 0.89, 'silver_925': 0.82 };
    const yearlyList = goldData.yearly_1901_2026 || [];

    const r24k_1g = baseGold['24'] || baseGold[24] || 13942;
    const r22k_1g = baseGold['22'] || baseGold[22] || 12775;
    const r18k_1g = baseGold['18'] || baseGold[18] || 10455;
    const r14k_1g = baseGold['14'] || baseGold[14] || 8230;
    const rSilver_1g = baseSilver['999'] || baseSilver[999] || 264.86;
    const rSilver925_1g = baseSilver['925'] || baseSilver[925] || 245.00;

    const y24k_1g = yesterdayGold['24'] || yesterdayGold[24] || 13893;
    const y22k_1g = yesterdayGold['22'] || yesterdayGold[22] || 12730;
    const ySilver_1g = yesterdaySilver['999'] || yesterdaySilver[999] || 263.97;"""

        if old_init in code:
            code = code.replace(old_init, new_init)
        else:
            # Fallback regex replacement
            code = re.sub(
                r'const r24k_1g = baseGold\[24\] \|\| \d+;',
                "const r24k_1g = baseGold['24'] || baseGold[24] || 13942;",
                code
            )
            code = re.sub(
                r'const r22k_1g = baseGold\[22\] \|\| \d+;',
                "const r22k_1g = baseGold['22'] || baseGold[22] || 12775;",
                code
            )
            code = re.sub(
                r'const r18k_1g = baseGold\[18\] \|\| \d+;',
                "const r18k_1g = baseGold['18'] || baseGold[18] || 10455;",
                code
            )
            code = re.sub(
                r'const rSilver_1g = baseSilver\[999\] \|\| [\d\.]+;',
                "const rSilver_1g = baseSilver['999'] || baseSilver[999] || 264.86;",
                code
            )

        # Update markdown live rates title to include today's date
        old_md_title = "### 💰 ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಸಜೀವ ಚಿನ್ನ ಹಾಗೂ ಬೆಳ್ಳಿ ದರಗಳು (Live Gold & Silver Rates)"
        new_md_title = "### 💰 ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಸಜೀವ ಚಿನ್ನ ಹಾಗೂ ಬೆಳ್ಳಿ ದರಗಳು (Live Gold & Silver Rates - 02/11/2026)"
        code = code.replace(old_md_title, new_md_title)

        with open(p, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f"Updated {p} successfully.")

if __name__ == '__main__':
    update_ask_ai_engine()
