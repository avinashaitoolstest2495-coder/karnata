import os

def update_worker_live_rates():
    paths = ['_worker.js', 'namma-karnataka/_worker.js']
    for p in paths:
        if not os.path.exists(p):
            continue
        with open(p, 'r', encoding='utf-8') as f:
            code = f.read()

        # Update top constants in generateGroundedGoldAnswer
        old_top = """  // Karnataka Bullion & Jewellers Association (KBJA Live Benchmark Telemetry)
  const g24 = 13893;      // 24K Pure per gram (₹13,893)
  const g22 = 12730;      // 22K Jewellery per gram (₹12,730)
  const g18 = 10420;      // 18K Diamond Jewellery per gram (₹10,420)
  const g14 = 8201;       // 14K Gold per gram (₹8,201)
  const pt950 = 7090;    // PT950 Platinum per gram (₹7,090)
  const sil = 265.00;     // Silver 999 per gram (₹265.00)
  const sil925 = 245.00;  // Silver 925 per gram (₹245.00)
  const gsr = 52.4;       // Gold-to-Silver Ratio"""

        new_top = """  // Karnataka Bullion & Jewellers Association (KBJA Live Benchmark Telemetry)
  const g24 = 13942;      // 24K Pure per gram (₹13,942)
  const g22 = 12775;      // 22K Jewellery per gram (₹12,775)
  const g18 = 10455;      // 18K Diamond Jewellery per gram (₹10,455)
  const g14 = 8230;       // 14K Gold per gram (₹8,230)
  const pt950 = 7090;    // PT950 Platinum per gram (₹7,090)
  const sil = 264.86;     // Silver 999 per gram (₹264.86)
  const sil925 = 245.00;  // Silver 925 per gram (₹245.00)
  const gsr = 52.6;       // Gold-to-Silver Ratio"""

        code = code.replace(old_top, new_top)

        # Update general live query section (lines 216-248)
        old_general_answer = """    return {
      answer: `### 🥇 ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಅಧಿಕೃತ ಕರ್ನಾಟಕ ಬುಲಿಯನ್ ಚಿನ್ನದ ದರ (Karnataka Bullion Gold Rate Today)

* **24 ಕ್ಯಾರಟ್ ಶುದ್ಧ ಅಪರಂಜಿ ಚಿನ್ನ (24K Gold / Gram):**
  * **1 ಗ್ರಾಂ:** **₹13,893** *(ನಿನ್ನೆ: ₹14,231 | ಬದಲಾವಣೆ: -₹338 🔴 (ಇಳಿಕೆ))*
  * **10 ಗ್ರಾಂ:** **₹138,930**
  * **100 ಗ್ರಾಂ:** **₹1,389,300**

* **22 ಕ್ಯಾರಟ್ ಆಭರಣ ಚಿನ್ನ (22K Gold / Gram):**
  * **1 ಗ್ರಾಂ:** **₹12,730** *(ನಿನ್ನೆ: ₹13,040 | ಬದಲಾವಣೆ: -₹310 🔴 (ಇಳಿಕೆ))*
  * **1 ಪವನ್ (8 ಗ್ರಾಂ):** **₹101,840**
  * **10 ಗ್ರಾಂ:** **₹127,300**

* **18 ಕ್ಯಾರಟ್ ಚಿನ್ನ (18K Gold / Gram):**
  * **1 ಗ್ರಾಂ:** **₹10,420** *(ನಿನ್ನೆ: ₹10,670 | ಬದಲಾವಣೆ: -₹250 🔴 (ಇಳಿಕೆ))*
  * **10 ಗ್ರಾಂ:** **₹104,200**

* **14 ಕ್ಯಾರಟ್ ಚಿನ್ನ (14K Gold):** **₹8,201 / ಗ್ರಾಂ**
* **ಪ್ಲಾಟಿನಂ (PT950 Platinum):** **₹7,090 / ಗ್ರಾಂ**
* **ಶುದ್ಧ ಬೆಳ್ಳಿ (Silver 999):** **₹265.00 / ಗ್ರಾಂ** (₹265,000 / 1 ಕೆಜಿ)

---
🕒 **ಅಧಿಕೃತ ಮೂಲ:** ಕರ್ನಾಟಕ ಬುಲಿಯನ್ ಕರ್ನಾಟಕ (Updated on: 31-10-26, 9:40:55 AM (Karnataka Bullion Live))
💡 **ಬಿಲ್ ಸೂತ್ರ:** ಆಭರಣ ಮೊತ್ತ = (ತೂಕ × ₹12,730) + ಮೇಕಿಂಗ್ ಶುಲ್ಕ + 3% GST + ₹45 BIS ಹಾಲ್‌ಮಾರ್ಕ್ ಶುಲ್ಕ.`,"""

        new_general_answer = """    return {
      answer: `### 🥇 ಇಂದು ಕರ್ನಾಟಕದಲ್ಲಿ ಅಧಿಕೃತ ಲೈವ್ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರಗಳು (KBJA Live Rates - 02/11/2026)

* **24 ಕ್ಯಾರಟ್ ಶುದ್ಧ ಅಪರಂಜಿ ಚಿನ್ನ (24K Gold / Gram):**
  * **1 ಗ್ರಾಂ:** **₹13,942** *(ನಿನ್ನೆ: ₹13,893 | ಬದಲಾವಣೆ: +₹49 🟢 (ಏರಿಕೆ))*
  * **10 ಗ್ರಾಂ:** **₹139,420**
  * **100 ಗ್ರಾಂ:** **₹1,394,200**

* **22 ಕ್ಯಾರಟ್ ಆಭರಣ ಚಿನ್ನ (22K Gold / Gram):**
  * **1 ಗ್ರಾಂ:** **₹12,775** *(ನಿನ್ನೆ: ₹12,730 | ಬದಲಾವಣೆ: +₹45 🟢 (ಏರಿಕೆ))*
  * **1 ಪವನ್ (8 ಗ್ರಾಂ):** **₹102,200**
  * **10 ಗ್ರಾಂ:** **₹127,750**

* **18 ಕ್ಯಾರಟ್ ಚಿನ್ನ (18K Gold / Gram):**
  * **1 ಗ್ರಾಂ:** **₹10,455** *(ನಿನ್ನೆ: ₹10,418 | ಬದಲಾವಣೆ: +₹37 🟢 (ಏರಿಕೆ))*
  * **10 ಗ್ರಾಂ:** **₹104,550**

* **14 ಕ್ಯಾರಟ್ ಚಿನ್ನ (14K Gold):** **₹8,230 / ಗ್ರಾಂ**
* **ಪ್ಲಾಟಿನಂ (PT950 Platinum):** **₹7,090 / ಗ್ರಾಂ**
* **ಶುದ್ಧ ಬೆಳ್ಳಿ (Silver 999):** **₹264.86 / ಗ್ರಾಂ** (₹264,860 / 1 ಕೆಜಿ)

---
🕒 **ಅಧಿಕೃತ ಮೂಲ:** ಕರ್ನಾಟಕ ಬುಲಿಯನ್ & ಆಭರಣ ವ್ಯಾಪಾರಿಗಳ ಒಕ್ಕೂಟ (KBJA Live Benchmark - 02 ನವೆಂಬರ್ 2026)
💡 **ಬಿಲ್ ಸೂತ್ರ:** ಆಭರಣ ಮೊತ್ತ = (ತೂಕ × ₹12,775) + ಮೇಕಿಂಗ್ ಶುಲ್ಕ + 3% GST + ₹45 BIS ಹಾಲ್‌ಮಾರ್ಕ್ ಶುಲ್ಕ.`,"""

        code = code.replace(old_general_answer, new_general_answer)

        # Update city map prices to 13942 / 12775
        city_diffs = {
            'bengaluru': 0, 'bangalore': 0,
            'mysuru': 0, 'mysore': 0,
            'mangaluru': 0, 'mangalore': 0,
            'hubballi': 3, 'hubli': 3, 'dharwad': 3,
            'belagavi': -2, 'belgaum': -2,
            'kalaburagi': 6, 'gulbarga': 6,
            'davanagere': 3, 'shivamogga': 2, 'shimoga': 2,
            'tumakuru': 0, 'tumkur': 0,
            'hassan': 1, 'udupi': 0,
            'ballari': 4, 'bellary': 4,
            'vijayapura': 3, 'bijapur': 3,
            'bidar': 6, 'raichur': 5
        }
        for ck, diff in city_diffs.items():
            g24_c = 13942 + diff
            g22_c = round(g24_c * (22/24))
            g18_c = round(g24_c * (18/24))
            # replace in city line
            import re
            pattern = re.compile(rf"('{ck}':\s*\{{[^}}]*\}})", re.IGNORECASE)
            def repl(m):
                s = m.group(1)
                s = re.sub(r'g24:\s*\d+', f'g24: {g24_c}', s)
                s = re.sub(r'g22:\s*\d+', f'g22: {g22_c}', s)
                s = re.sub(r'g18:\s*\d+', f'g18: {g18_c}', s)
                s = re.sub(r'sil:\s*[\d\.]+', 'sil: 264.86', s)
                s = re.sub(r'\(Karnataka Bullion [^\)]+\)', '(ಮುಖ್ಯ ಆಭರಣ ಮಾರುಕಟ್ಟೆ)', s)
                return s
            code = pattern.sub(repl, code)

        with open(p, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f"Updated live rates in {p} successfully.")

if __name__ == '__main__':
    update_worker_live_rates()
