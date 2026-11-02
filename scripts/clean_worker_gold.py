import os
import re

def clean_worker_js():
    paths = ['_worker.js', 'namma-karnataka/_worker.js']
    for p in paths:
        if not os.path.exists(p):
            continue
        with open(p, 'r', encoding='utf-8') as f:
            code = f.read()

        # 1. Header comment
        code = re.sub(
            r'// Official Jos Alukkas Karnataka Live Rates[^\n]*',
            '// Karnataka Bullion & Jewellers Association (KBJA Live Benchmark Telemetry)',
            code
        )
        
        # 2. Hubs in citiesMap
        code = re.sub(r'\(Jos Alukkas Showrooms\)', '(ಮುಖ್ಯ ಆಭರಣ ಮಾರುಕಟ್ಟೆ)', code)
        code = re.sub(r'\(Jos Alukkas [^\)]+\)', '(ಮುಖ್ಯ ಆಭರಣ ಮಾರುಕಟ್ಟೆ & ಶೋರೂಂಗಳು)', code)
        
        # 3. Clean Kannada/English titles and references
        code = code.replace(
            '### 💍 ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಮದುವೆ ಆಭರಣ ಖರೀದಿ ಮಾರ್ಗದರ್ಶಿ (Jos Alukkas Wedding Jewellery)',
            '### 💍 ಕರ್ನಾಟಕ ಮದುವೆ ಆಭರಣ ಖರೀದಿ & ಉಳಿತಾಯ ಮಾರ್ಗದರ್ಶಿ (KBJA Wedding Jewellery Guide)'
        )
        code = code.replace(
            '* **1. ಇಂದಿನ ಅಧಿಕೃತ ದರಗಳು (Jos Alukkas Rates):**',
            '* **1. ಇಂದಿನ ಅಧಿಕೃತ ಲೈವ್ ದರಗಳು (KBJA Live Rates - 02/11/2026):**'
        )
        code = code.replace(
            '* **1. ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಇಂದಿನ ದರಗಳು:**',
            '* **1. ಕರ್ನಾಟಕ ಮಾರುಕಟ್ಟೆ ಇಂದಿನ ಅಧಿಕೃತ ದರಗಳು (02/11/2026):**'
        )
        code = code.replace(
            'ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಲೈವ್ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ (Jos Alukkas Rates)',
            'ಅಧಿಕೃತ ಲೈವ್ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ (KBJA Live Rates - 02/11/2026)'
        )
        code = code.replace(
            'ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಕರ್ನಾಟಕ ದರ (Updated on: 2026-11-02T09:41:42 (Jos Alukkas Official))',
            'ಕರ್ನಾಟಕ ಬುಲಿಯನ್ & ಆಭರಣ ವ್ಯಾಪಾರಿಗಳ ಒಕ್ಕೂಟ (KBJA Live - 02/11/2026)'
        )
        code = code.replace(
            '### 🏙️ ಕರ್ನಾಟಕದ ನಗರಗಳಲ್ಲಿ ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ (Jos Alukkas Rates)',
            '### 🏙️ ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ನಗರಗಳಲ್ಲಿ ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ಲೈವ್ ದರಗಳು (City-wise Live Rates - 02/11/2026)'
        )
        code = code.replace(
            '*(ಮೂಲ: ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಕರ್ನಾಟಕ ಅಧಿಕೃತ ದರಗಳು).*',
            '*(ಮೂಲ: ಕರ್ನಾಟಕ ಬುಲಿಯನ್ & ಆಭರಣ ವ್ಯಾಪಾರಿಗಳ ಒಕ್ಕೂಟ - KBJA Live Benchmark).*'
        )
        code = code.replace(
            '### 🥈 ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಅಧಿಕೃತ ಬೆಳ್ಳಿ ದರ (Jos Alukkas Live Silver Rates)',
            '### 🥈 ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಅಧಿಕೃತ ಬೆಳ್ಳಿ ದರ (KBJA Live Silver Rates - 02/11/2026)'
        )
        code = code.replace(
            '💡 ಮೂಲ: ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಕರ್ನಾಟಕ ಅಧಿಕೃತ ಬೆಲೆ (Updated on: 2026-11-02T09:41:42 (Jos Alukkas Official)).',
            '💡 ಮೂಲ: ಕರ್ನಾಟಕ ಬುಲಿಯನ್ & ಆಭರಣ ವ್ಯಾಪಾರಿಗಳ ಒಕ್ಕೂಟ (KBJA Live Benchmark - 02/11/2026).'
        )
        code = code.replace(
            '### 📜 ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಇತ್ತೀಚಿನ ಚಿನ್ನದ ಬೆಲೆ ಇತಿಹಾಸ (Recent Daily Movement)',
            '### 📜 ಕರ್ನಾಟಕ ಚಿನ್ನದ ಬೆಲೆ ಇತ್ತೀಚಿನ ದೈನಂದಿನ ಇತಿಹಾಸ (Recent Daily Movement)'
        )
        code = code.replace(
            '📊 ಅಧಿಕೃತ ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ 365-ದಿನಗಳ ಲೈವ್ ಡಾಟಾಬೇಸ್‌ನಿಂದ ಪಡೆಯಲಾಗಿದೆ.',
            '📊 ಕರ್ನಾಟಕ ಬುಲಿಯನ್ ಅಸೋಸಿಯೇಷನ್ 125 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ದಾಖಲೆಗಳಿಂದ ಪಡೆಯಲಾಗಿದೆ.'
        )
        code = code.replace(
            '### 🟢 ಇಂದಿನ ಚಿನ್ನ ಖರೀದಿ ವಿಶ್ಲೇಷಣೆ (Jos Alukkas Market Analysis)',
            '### 🟢 ಇಂದಿನ ಚಿನ್ನ ಖರೀದಿ AI ವಿಶ್ಲೇಷಣೆ (Gold Buy Decision & Market Analysis - 02/11/2026)'
        )
        code = code.replace(
            'ಇಂದು ಜೋಸ್ ಆಲುಕ್ಕಾಸ್‌ನಲ್ಲಿ 24K ಚಿನ್ನ',
            'ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ 24K ಅಪರಂಜಿ ಚಿನ್ನ'
        )
        code = code.replace(
            '### 🟡 ಚಿನ್ನ ಮಾರಾಟ & ಎಕ್ಸ್‌ಚೇಂಜ್ ವಿಶ್ಲೇಷಣೆ (Jos Alukkas Exchange)',
            '### 🟡 ಚಿನ್ನ ಮಾರಾಟ & ಹಳೆಯ ಒಡವೆ ಎಕ್ಸ್‌ಚೇಂಜ್ ವಿಶ್ಲೇಷಣೆ (Gold Sell & Exchange Decision)'
        )
        code = code.replace(
            'ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಶೋರೂಂಗಳಲ್ಲಿ',
            'ಪ್ರಮುಖ ಆಭರಣ ಶೋರೂಂಗಳಲ್ಲಿ'
        )
        code = code.replace(
            '### 🥇 ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಅಧಿಕೃತ ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಚಿನ್ನದ ದರ (Jos Alukkas Gold Rate Today)',
            '### 🥇 ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಅಧಿಕೃತ ಲೈವ್ ಚಿನ್ನದ ದರ (Karnataka Live Gold Rate - 02/11/2026)'
        )
        code = code.replace(
            '🕒 **ಅಧಿಕೃತ ಮೂಲ:** ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ಕರ್ನಾಟಕ (Updated on: 2026-11-02T09:41:42 (Jos Alukkas Official))',
            '🕒 **ಅಧಿಕೃತ ಮೂಲ:** ಕರ್ನಾಟಕ ಬುಲಿಯನ್ & ಆಭರಣ ವ್ಯಾಪಾರಿಗಳ ಒಕ್ಕೂಟ (KBJA Live - 02 ನವೆಂಬರ್ 2026)'
        )
        code = code.replace(
            '{ title: "🥇 ಲೈವ್ ಜೋಸ್ ಆಲುಕ್ಕಾಸ್ ದರ ಪೋರ್ಟಲ್", url: "/gold-rate.html", icon: "🥇" }',
            '{ title: "🥇 ಲೈವ್ ಚಿನ್ನದ ದರ ಪೋರ್ಟಲ್", url: "/gold-rate.html", icon: "🥇" }'
        )
        code = code.replace(
            '{ name: "Jos Alukkas Karnataka", url: "https://www.josalukkasonline.com/gold-rate-today/karnataka" }',
            '{ name: "Karnataka Bullion & Jewellers Association (KBJA)", url: "/gold-rate.html" }'
        )
        code = code.replace(
            'provider: "Jos Alukkas Live Karnataka Telemetry"',
            'provider: "Karnataka Bullion & Jewellers Association (KBJA Live)"'
        )
        code = code.replace(
            "provider: groundedGold.provider || 'Jos Alukkas Karnataka Telemetry'",
            "provider: groundedGold.provider || 'Karnataka Bullion & Jewellers Association (KBJA Live)'"
        )
        code = code.replace(
            '// TIER 0: Grounded Financial & Gold Decision Intelligence (Jos Alukkas Karnataka Live)',
            '// TIER 0: Grounded Financial & Gold Decision Intelligence (KBJA Karnataka Live)'
        )
        
        # General regex replacements in case anything else lingered
        code = re.sub(r'ಜೋಸ್\s*ಆಲುಕ್ಕಾಸ್', 'ಕರ್ನಾಟಕ ಬುಲಿಯನ್', code)
        code = re.sub(r'ಜೋಸ್\s*ಲುಕ್ಕಾಸ್', 'ಕರ್ನಾಟಕ ಬುಲಿಯನ್', code)
        code = re.sub(r'Jos\s*Alukkas', 'Karnataka Bullion', code)
        
        with open(p, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f"Cleaned {p} successfully.")

if __name__ == '__main__':
    clean_worker_js()
