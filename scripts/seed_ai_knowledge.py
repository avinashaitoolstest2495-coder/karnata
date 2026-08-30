"""
Karnata — seed_ai_knowledge.py
Seeds 120+ comprehensive verified FAQs, SIR guides, Guarantee scheme policies,
land records, civic services, and knowledge documents into Cloudflare D1 (karnata-ai-db).
"""

import json
import os
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).parent.parent
MIGRATIONS_DIR = BASE_DIR / "migrations"

FAQS = [
    # =========================================================================
    # 1. SIR & ELECTORAL ROLL / VOTER SERVICES (ECI & CEO KARNATAKA)
    # =========================================================================
    {
        "id": "faq_sir_001",
        "question": "SIR ಎಂದರೇನು? ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯಲ್ಲಿ ಹೆಸರು ಹೇಗೆ ಪರಿಶೀಲಿಸುವುದು?",
        "normalized_question": "sir ಎಂದರೇನು ಕರಡು ಮತದಾರರ ಪಟ್ಟಿ ಹೆಸರು ಹೇಗೆ ಪರಿಶೀಲಿಸುವುದು what is sir check draft roll",
        "answer": """### 🗳️ SIR (Special Summary Revision) ಮತ್ತು ಕರಡು ಮತದಾರರ ಪಟ್ಟಿ ಪರಿಶೀಲನೆ

**SIR (ವಿಶೇಷ ಸಂಕ್ಷಿಪ್ತ ಪರಿಷ್ಕರಣೆ / Special Summary Revision)** ಎಂಬುದು ಭಾರತೀಯ ಚುನಾವಣಾ ಆಯೋಗ (ECI) ಪ್ರತಿವರ್ಷ ಸಾರ್ವತ್ರಿಕವಾಗಿ ನಡೆಸುವ ಶಾಸನಬದ್ಧ ಮತದಾರರ ಪಟ್ಟಿ ಪರಿಷ್ಕರಣಾ ಪ್ರಕ್ರಿಯೆಯಾಗಿದೆ.

---

### 📋 ಕರಡು ಪಟ್ಟಿಯಲ್ಲಿ (Draft Roll) ಹೆಸರು ಪರಿಶೀಲಿಸುವ ಹಂತಗಳು:
1. **ಕ್ಷೇತ್ರ ಆಯ್ಕೆಮಾಡಿ:** ನಿಮ್ಮ ಜಿಲ್ಲೆ ಹಾಗೂ 224 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳಲ್ಲಿ ನಿಮ್ಮ ಕ್ಷೇತ್ರವನ್ನು ಗುರುತಿಸಿ.
2. **Part Number (ಭಾಗ ಸಂಖ್ಯೆ) ಪತ್ತೆಹಚ್ಚಿ:** ನಿಮ್ಮ ಹಳ್ಳಿ ಅಥವಾ ಬಡಾವಣೆಯ ಮತಗಟ್ಟೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ Part Number ಆಯ್ಕೆಮಾಡಿ.
3. **Draft Roll PDF ತೆರೆಯಿರಿ:** ಆಯೋಗವು ಪ್ರಕಟಿಸಿದ ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ.
4. **ಹೆಸರು / EPIC ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ:** ನಿಮ್ಮ ವೋಟರ್ ಐಡಿ ಸಂಖ್ಯೆ (EPIC No.) ಅಥವಾ ಪೂರ್ಣ ಹೆಸರನ್ನು ಹುಡುಕಿ (Ctrl+F ಬಳಸಿ).

---

### ⚠️ ಕರಡು ಪಟ್ಟಿಯಲ್ಲಿ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ತಿದ್ದುಪಡಿ ಬೇಕಿದ್ದರೆ:
* **ಹೊಸ ಮತದಾರರ ನೋಂದಣಿ (18+ ವರ್ಷ):** [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6** ಸಲ್ಲಿಸಿ.
* **ವಿಳಾಸ / ಹೆಸರು / ಭಾವಚಿತ್ರ ತಿದ್ದುಪಡಿ:** **Form 8** ಮೂಲಕ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.
* **ಆಕ್ಷೇಪಣೆ / ಹೆಸರು ತೆಗೆದುಹಾಕಲು:** **Form 7** ಸಲ್ಲಿಸಿ.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [ceokarnataka.kar.nic.in](https://ceokarnataka.kar.nic.in) | **ಸಹಾಯವಾಣಿ:** 1950""",
        "category": "SIR",
        "language": "kn",
        "source_url": "https://ceokarnataka.kar.nic.in",
        "keywords": "sir, eci, summary revision, draft roll, ಕರಡು, ಮತದಾರ, ಪರಿಷ್ಕರಣೆ, ಹೆಸರು, ಪರಿಶೀಲಿಸುವುದು, voter list",
        "action_label": "🔎 SIR Draft Roll ಪರಿಶೀಲಿಸಿ",
        "action_url": "/karnataka-sir-voter-roll.html"
    },
    {
        "id": "faq_sir_002",
        "question": "ಹೊಸದಾಗಿ ವೋಟರ್ ಐಡಿಗೆ (Form 6) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "ಹೊಸ ವೋಟರ್ ಐಡಿ ಅರ್ಜಿ form 6 apply new voter id registration online",
        "answer": """### 📝 ಹೊಸ ಮತದಾರರ ಗುರುತಿನ ಚೀಟಿ ನೋಂದಣಿ (Form 6)

18 ವರ್ಷ ತುಂಬಿದ ಅಥವಾ ಅರ್ಹತಾ ದಿನಾಂಕಕ್ಕೆ 18 ವರ್ಷ ಪೂರೈಸಲಿರುವ ಪ್ರತಿಯೊಬ್ಬ ಭಾರತೀಯ ನಾಗರಿಕರು ಮತದಾರರ ಪಟ್ಟಿಗೆ ಹೆಸರು ಸೇರಿಸಲು **Form 6** ಸಲ್ಲಿಸಬೇಕು.

---

### 📌 ಅರ್ಹತೆ & ಅಗತ್ಯ ದಾಖಲೆಗಳು:
* **ವಯಸ್ಸಿನ ಪುರಾವೆ:** ಆಧಾರ್ ಕಾರ್ಡ್ / ಜನನ ಪ್ರಮಾಣಪತ್ರ / SSLC ಅಂಕಪಟ್ಟಿ / ಪಾಸ್‌ಪೋರ್ಟ್ / ಪ್ಯಾನ್ ಕಾರ್ಡ್.
* **ವಿಳಾಸದ ಪುರಾವೆ:** ವಿದ್ಯುತ್ ಬಿಲ್ / ನೀರಿನ ಬಿಲ್ / ಗ್ಯಾಸ್ ಕನೆಕ್ಷನ್ ಬಿಲ್ / ಆಧಾರ್ ಕಾರ್ಡ್ / ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್.
* **ಭಾವಚಿತ್ರ:** ಇತ್ತೀಚಿನ ಪಾಸ್‌ಪೋರ್ಟ್ ಸೈಜ್ ಭಾವಚಿತ್ರ (ಗರಿಷ್ಠ 2 MB, JPG/JPEG).

---

### 🚀 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಕೆಯ ಹಂತಗಳು:
1. [voters.eci.gov.in](https://voters.eci.gov.in) ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ ಅಥವಾ **ECI Voter Helpline App** ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ.
2. ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಹಾಗೂ OTP ನಮೂದಿಸಿ ಖಾತೆ ತೆರೆಯಿರಿ.
3. **Forms** ವಿಭಾಗದಲ್ಲಿ **Form 6 (Register as a New Elector)** ಆಯ್ಕೆಮಾಡಿ.
4. ವೈಯಕ್ತಿಕ ವಿವರ, ವಿಳಾಸ, ಕುಟುಂಬದ ಸದಸ್ಯರ EPIC ಸಂಖ್ಯೆ ಹಾಗೂ ದಾಖಲೆಗಳನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
5. ಡಿಕ್ಲರೇಶನ್ ಒಪ್ಪಿ ಸಬ್ಮಿಟ್ ಮಾಡಿ. ಸಲ್ಲಿಕೆಯ ನಂತರ ದೊರೆಯುವ **Reference Number (Ack No)** ಸುರಕ್ಷಿತವಾಗಿಟ್ಟುಕೊಳ್ಳಿ.
6. ಬೂತ್ ಮಟ್ಟದ ಅಧಿಕಾರಿ (BLO) ಸ್ಥಳ ಪರಿಶೀಲನೆ ನಡೆಸಿದ 15-30 ದಿನಗಳಲ್ಲಿ ನಿಮ್ಮ EPIC ರಚನೆಯಾಗುತ್ತದೆ.

💡 **ಸಲಹೆ:** ನಿಮ್ಮ ನೋಂದಾಯಿತ ಮೊಬೈಲ್ ಮೂಲಕವೇ e-EPIC ಡಿಜಿಟಲ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.""",
        "category": "SIR",
        "language": "kn",
        "source_url": "https://voters.eci.gov.in",
        "keywords": "form 6, new voter id, apply voter card, ಹೊಸ ಮತದಾರರ ಗುರುತಿನ ಚೀಟಿ, ನೋಂದಣಿ",
        "action_label": "🌐 Form 6 ಅರ್ಜಿ ಸಲ್ಲಿಸಿ",
        "action_url": "https://voters.eci.gov.in"
    },
    {
        "id": "faq_sir_003",
        "question": "ವೋಟರ್ ಐಡಿಯಲ್ಲಿ ವಿಳಾಸ ಬದಲಾವಣೆ, ಹೆಸರು ತಿದ್ದುಪಡಿ (Form 8) ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "ವೋಟರ್ ಐಡಿ ಹೆಸರು ವಿಳಾಸ ತಿದ್ದುಪಡಿ form 8 correction voter id shifting address update",
        "answer": """### 🛠️ ವೋಟರ್ ಐಡಿ ತಿದ್ದುಪಡಿ ಮತ್ತು ಸ್ಥಳಾಂತರ ಪ್ರಕ್ರಿಯೆ (Form 8)

ಮತದಾರರ ಪಟ್ಟಿಯಲ್ಲಿ ಹೆಸರು, ವಿಳಾಸ, ಹುಟ್ಟಿದ ದಿನಾಂಕ, ಲಿಂಗ, ಸಂಬಂಧಿಕರ ಹೆಸರು, ಫೋಟೋ ತಿದ್ದುಪಡಿ ಅಥವಾ ಬೇರೆ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಕ್ಕೆ ಸ್ಥಳಾಂತರವಾಗಿದ್ದರೆ **Form 8** ಸಲ್ಲಿಸಬೇಕು.

---

### 📋 Form 8 ನಲ್ಲಿ ಲಭ್ಯವಿರುವ 4 ಮುಖ್ಯ ಆಯ್ಕೆಗಳು:
1. **Shifting of Residence:** ಒಂದೇ ಕ್ಷೇತ್ರದೊಳಗೆ ಅಥವಾ ಬೇರೆ ಕ್ಷೇತ್ರಕ್ಕೆ ವಿಳಾಸ ಬದಲಾವಣೆ.
2. **Correction of Entries:** ಹೆಸರು, ವಯಸ್ಸು, ಲಿಂಗ, ಸಂಬಂಧದ ವಿವರ, ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಅಥವಾ ಫೋಟೋ ತಿದ್ದುಪಡಿ.
3. **Issue of Replacement EPIC:** ಹಳೆಯ ಕಾರ್ಡ್ ಹಾಳಾಗಿದ್ದರೆ/ಕಳೆದುಹೋದರೆ ಹೊಸ PVC ಕಾರ್ಡ್ ಕೋರಿಕೆ.
4. **Request for marking as PwD:** ವಿಶೇಷ ಚೇತನ ಮತದಾರರ ಗುರುತು ನಮೂದು.

---

### 💻 ತಿದ್ದುಪಡಿ ಮಾಡುವ ವಿಧಾನ:
1. [voters.eci.gov.in](https://voters.eci.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ ಲಾಗಿನ್ ಆಗಿ.
2. **Form 8** ಆಯ್ಕೆಮಾಡಿ ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ನಮೂದಿಸಿ.
3. ತಿದ್ದುಪಡಿ ಮಾಡಬೇಕಾದ ಕ್ಷೇತ್ರವನ್ನು (ಉದಾ: Address ಅಥವಾ Name) ಟಿಕ್ ಮಾಡಿ.
4. ಸೂಕ್ತ ಅಧಿಕೃತ ಪೂರಕ ದಾಖಲೆಯನ್ನು (ಆಧಾರ್/ವಿದ್ಯುತ್ ಬಿಲ್/ಗೆಜೆಟ್ ನೋಟಿಫಿಕೇಶನ್) ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ಸಬ್ಮಿಟ್ ಮಾಡಿ.""",
        "category": "SIR",
        "language": "kn",
        "source_url": "https://voters.eci.gov.in",
        "keywords": "form 8, voter id correction, address change, name correction, ತಿದ್ದುಪಡಿ, ವಿಳಾಸ ಬದಲಾವಣೆ",
        "action_label": "✏️ Form 8 ತಿದ್ದುಪಡಿ ಮಾಡಿ",
        "action_url": "https://voters.eci.gov.in"
    },
    {
        "id": "faq_sir_004",
        "question": "ಡಿಜಿಟಲ್ ವೋಟರ್ ಐಡಿ (e-EPIC) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "e-epic download digital voter card online pdf ವೋಟರ್ ಕಾರ್ಡ್ ಡೌನ್‌ಲೋಡ್",
        "answer": """### 📱 ಅಧಿಕೃತ e-EPIC (ಡಿಜಿಟಲ್ ಮತದಾರರ ಚೀಟಿ) ಡೌನ್‌ಲೋಡ್

e-EPIC ಎಂಬುದು ಭಾರತೀಯ ಚುನಾವಣಾ ಆಯೋಗವು ಅಧಿಕೃತವಾಗಿ ನೀಡುವ ಸುರಕ್ಷಿತ PDF ಆವೃತ್ತಿಯ ಮತದಾರರ ಗುರುತಿನ ಚೀಟಿಯಾಗಿದ್ದು, ಭೌತಿಕ ಕಾರ್ಡ್‌ನಷ್ಟೇ ಸಂಪೂರ್ಣ ಕಾನೂನು ಮಾನ್ಯತೆ ಹೊಂದಿದೆ.

---

### 📥 e-EPIC ಡೌನ್‌ಲೋಡ್ ಮಾಡುವ ವಿಧಾನ:
1. **ವೆಬ್‌ಸೈಟ್ ಪ್ರವೇಶಿಸಿ:** [voters.eci.gov.in](https://voters.eci.gov.in)
2. ಮುಖಪುಟದಲ್ಲಿರುವ **'E-EPIC Download'** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ **EPIC ಸಂಖ್ಯೆ** ಅಥವಾ Form 6 **Reference No.** ನಮೂದಿಸಿ, ರಾಜ್ಯವನ್ನು **'Karnataka'** ಎಂದು ಆಯ್ಕೆಮಾಡಿ.
4. ನಿಮ್ಮ ನೋಂದಾಯಿತ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಗೆ 6 ಅಂಕಿಗಳ **OTP** ರವಾನೆಯಾಗುತ್ತದೆ.
5. OTP ನಮೂದಿಸಿ ದೃಢೀಕರಿಸಿ **'Download e-EPIC'** ಕ್ಲಿಕ್ ಮಾಡಿ.

💡 **ಗಮನಿಸಿ:** ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆಗೆ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಲಿಂಕ್ ಆಗಿರದಿದ್ದರೆ, ಮೊದಲು **Form 8** ಸಲ್ಲಿಸಿ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಅಪ್‌ಡೇಟ್ ಮಾಡಿಕೊಳ್ಳಬೇಕು.""",
        "category": "SIR",
        "language": "kn",
        "source_url": "https://voters.eci.gov.in",
        "keywords": "e-epic, digital voter id, download epic, ವೋಟರ್ ಕಾರ್ಡ್ ಡೌನ್‌ಲೋಡ್, ಇ ಎಪಿಕ್",
        "action_label": "📥 e-EPIC ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ",
        "action_url": "https://voters.eci.gov.in"
    },
    {
        "id": "faq_sir_005",
        "question": "ನನ್ನ ಮತಗಟ್ಟೆ (Polling Booth) ಮತ್ತು BLO ಅಧಿಕಾರಿಯ ವಿವರ ಪತ್ತೆಹಚ್ಚುವುದು ಹೇಗೆ?",
        "normalized_question": "find my blo booth polling station ಮತಗಟ್ಟೆ ಅಧಿಕಾರಿ ವಿವರ",
        "answer": """### 📍 ನಿಮ್ಮ ಮತಗಟ್ಟೆ ಮತ್ತು BLO (Booth Level Officer) ಮಾಹಿತಿ ಪಡೆಯುವುದು

ಪ್ರತಿ ಮತಗಟ್ಟೆ ವ್ಯಾಪ್ತಿಗೆ ಸ್ಥಳೀಯ ಮತದಾರರ ಪಟ್ಟಿ ಉಸ್ತುವಾರಿಗಾಗಿ ಒಬ್ಬ ಸರ್ಕಾರಿ ಅಧಿಕಾರಿಯನ್ನು (BLO) ನಿಯೋಜಿಸಲಾಗಿರುತ್ತದೆ.

---

### 🔍 BLO ಹಾಗೂ ಮತಗಟ್ಟೆ ತಿಳಿಯುವ 3 ಸುಲಭ ವಿಧಾನಗಳು:
1. **ಆನ್‌ಲೈನ್ ಪೋರ್ಟಲ್:** [electoralsearch.eci.gov.in](https://electoralsearch.eci.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ನಮೂದಿಸಿ 'Know Your Polling Officer' ಕ್ಲಿಕ್ ಮಾಡಿ.
2. **ECI Voter Helpline App:** ಆ್ಯಪ್‌ನಲ್ಲಿ 'Know Your BLO/ERO' ವಿಭಾಗಕ್ಕೆ ಹೋಗಿ EPIC ಹಾಕಿ.
3. **SMS ಸೌಲಭ್ಯ:** ನಿಮ್ಮ ಮೊಬೈಲ್‌ನಿಂದ `ECIBLO <ಸ್ಪೇಸ್> <EPIC ಸಂಖ್ಯೆ>` ಎಂದು ಟೈಪ್ ಮಾಡಿ **1950** ಸಂಖ್ಯೆಗೆ ಕಳುಹಿಸಿ.

ಇಲ್ಲಿ ನಿಮ್ಮ ಮತಗಟ್ಟೆಯ ಹೆಸರು, ಕೊಠಡಿ ಸಂಖ್ಯೆ, BLO ಹೆಸರು ಹಾಗೂ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಲಭ್ಯವಾಗುತ್ತದೆ.""",
        "category": "SIR",
        "language": "kn",
        "source_url": "https://electoralsearch.eci.gov.in",
        "keywords": "blo contact, polling booth, voting center, ಬಿಎಲ್ಒ, ಮತಗಟ್ಟೆ",
        "action_label": "🔍 BLO ವಿವರ ಹುಡುಕಿ",
        "action_url": "https://electoralsearch.eci.gov.in"
    },
    {
        "id": "faq_sir_006",
        "question": "ಮೃತಪಟ್ಟವರ ಅಥವಾ ಶಾಶ್ವತ ಸ್ಥಳಾಂತರಗೊಂಡವರ ಹೆಸರು ಮತದಾರರ ಪಟ್ಟಿಯಿಂದ ರದ್ದುಪಡಿಸುವುದು ಹೇಗೆ (Form 7)?",
        "normalized_question": "ಮತದಾರರ ಪಟ್ಟಿ ಹೆಸರು ತೆಗೆದುಹಾಕುವುದು form 7 deletion dead voter shifting objection",
        "answer": """### ❌ ಮತದಾರರ ಪಟ್ಟಿಯಿಂದ ಹೆಸರು ರದ್ದುಗೊಳಿಸುವ ಪ್ರಕ್ರಿಯೆ (Form 7)

ಮೃತ ವ್ಯಕ್ತಿಗಳ, ನಕಲಿ ನೋಂದಣಿಗಳ ಅಥವಾ ಶಾಶ್ವತವಾಗಿ ಬೇರೆಡೆಗೆ ಸ್ಥಳಾಂತರಗೊಂಡ ವ್ಯಕ್ತಿಗಳ ಹೆಸರನ್ನು ಮತದಾರರ ಪಟ್ಟಿಯಿಂದ ತೆಗೆದುಹಾಕಲು **Form 7 (Application for Objection for Proposed Inclusion / Deletion)** ಸಲ್ಲಿಸಬೇಕು.

---

### 📋 ಅಗತ್ಯವಿರುವ ವಿವರಗಳು:
* ರದ್ದುಪಡಿಸಬೇಕಾದ ವ್ಯಕ್ತಿಯ ಹೆಸರು ಮತ್ತು EPIC ಸಂಖ್ಯೆ.
* ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಮತ್ತು ಬೂತ್ ಸಂಖ್ಯೆ (Part Number).
* **ಮರಣದ ಸಂದರ್ಭದಲ್ಲಿ:** ಪುರಸಭೆ/ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ನೀಡಿದ ಅಧಿಕೃತ **ಮರಣ ಪ್ರಮಾಣಪತ್ರ (Death Certificate)** ಸಂಖ್ಯೆ.

---

### 💻 ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಹಂತಗಳು:
1. [voters.eci.gov.in](https://voters.eci.gov.in) ಗೆ ಲಾಗಿನ್ ಆಗಿ **Form 7** ಆಯ್ಕೆಮಾಡಿ.
2. ಅರ್ಜಿದಾರರ ವಿವರ ಹಾಗೂ ಆಕ್ಷೇಪಣೆಗೆ ಒಳಗಾದ ವ್ಯಕ್ತಿಯ ವಿವರಗಳನ್ನು ಭರ್ತಿಮಾಡಿ.
3. ಮರಣ ಪ್ರಮಾಣಪತ್ರವನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ಸಬ್ಮಿಟ್ ಮಾಡಿ. ಸ್ಥಳೀಯ BLO ಪರಿಶೀಲನೆ ನಡೆಸಿ ಹೆಸರು ರದ್ದುಪಡಿಸುತ್ತಾರೆ.""",
        "category": "SIR",
        "language": "kn",
        "source_url": "https://voters.eci.gov.in",
        "keywords": "form 7, delete voter, dead voter deletion, ಹೆಸರು ತೆಗೆಯುವುದು, ಮೃತ ಮತದಾರ",
        "action_label": "📄 Form 7 ವಿವರ ನೋಡಿ",
        "action_url": "https://voters.eci.gov.in"
    },

    # =========================================================================
    # 2. KARNATAKA 5 GUARANTEE SCHEMES
    # =========================================================================
    {
        "id": "faq_sch_007",
        "question": "ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆ: ₹2,000 DBT ಸ್ಥಿತಿ ನೋಡುವುದು ಹೇಗೆ? ಹಣ ಬಾರದಿದ್ದರೆ ಪರಿಹಾರವೇನು?",
        "normalized_question": "ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆ ಯಾರು ಅರ್ಹರು dbt ಸ್ಥಿತಿ gruha lakshmi scheme amount eligibility bank aadhaar",
        "answer": """### 🌸 ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆ (Gruha Lakshmi Scheme) — ₹2,000 ಮಾಸಿಕ ನೆರವು

ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಮಹತ್ವಾಕಾಂಕ್ಷಿ ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆಯಡಿ ಕುಟುಂಬದ ಯಜಮಾನಿ ಮಹಿಳೆಗೆ ಪ್ರತಿ ತಿಂಗಳು **₹2,000** ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT) ಮೂಲಕ ನೀಡಲಾಗುತ್ತದೆ.

---

### 📌 ಅರ್ಹತೆಯ ಮಾನದಂಡಗಳು:
1. ರೇಷನ್ ಕಾರ್ಡ್‌ನಲ್ಲಿ (BPL, APL, Antyodaya) ಮಹಿಳೆ **ಕುಟುಂಬದ ಯಜಮಾನಿ (Head of Family)** ಎಂದು ನಮೂದಾಗಿರಬೇಕು.
2. ಮಹಿಳೆ ಅಥವಾ ಆಕೆಯ ಪತಿ ಆದಾಯ ತೆರಿಗೆ (Income Tax) ಅಥವಾ GST ಪಾವತಿದಾರರಾಗಿರಬಾರದು.
3. ಮಹಿಳೆಯ ಆಧಾರ್ ಸಂಖ್ಯೆಯು ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ **Aadhaar NPCI Seeding** ಆಗಿರಬೇಕು.

---

### 🔍 DBT ಹಣ ಜಮೆಯಾಗದಿರಲು ಮುಖ್ಯ ಕಾರಣಗಳು & ಪರಿಹಾರ:
* **NPCI Seeding ದೋಷ:** ಬ್ಯಾಂಕ್ ಶಾಖೆಗೆ ಭೇಟಿ ನೀಡಿ *Aadhaar Mandate / DBT Consent Form* ಸಲ್ಲಿಸಿ ಖಾತೆಗೆ ಸೀಡಿಂಗ್ ಮಾಡಿಸಿ.
* **e-KYC ಬಾಕಿ:** ನಿಮ್ಮ ಗ್ರಾಮ ಒನ್ ಅಥವಾ ಕರ್ನಾಟಕ ಒನ್ ಕೇಂದ್ರಗಳಲ್ಲಿ ರೇಷನ್ ಕಾರ್ಡ್ e-KYC ಪೂರ್ಣಗೊಳಿಸಿ.
* **ಹಣ ಬಂದಿರುವ ಸ್ಥಿತಿ ತಿಳಿಯಲು:** Google Play Store ನಿಂದ ಅಧಿಕೃತ **'DBT Karnataka'** ಆ್ಯಪ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ ನಿಮ್ಮ ಆಧಾರ್ ಸಂಖ್ಯೆ ಹಾಕಿ ತಿಂಗಳಾವಾರು ಪಾವತಿ ವಿವರಗಳನ್ನು ನೇರವಾಗಿ ಪರಿಶೀಲಿಸಿ.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [sevasindhugs.karnataka.gov.in](https://sevasindhugs.karnataka.gov.in) | **ಸಹಾಯವಾಣಿ:** 1902""",
        "category": "SCHEME",
        "language": "kn",
        "source_url": "https://sevasindhugs.karnataka.gov.in",
        "keywords": "gruha lakshmi, 2000 dbt, ಗೃಹಲಕ್ಷ್ಮಿ, ಯಜಮಾನಿ ಮಹಿಳೆ, ಗ್ಯಾರಂಟಿ ಯೋಜನೆ, ಅರ್ಹರು, dbt, npci",
        "action_label": "📜 ಗೃಹಲಕ್ಷ್ಮಿ ವಿವರ ನೋಡಿ",
        "action_url": "/guarantee-schemes.html"
    },
    {
        "id": "faq_sch_008",
        "question": "ಗೃಹಜ್ಯೋತಿ ಯೋಜನೆ: 200 ಯೂನಿಟ್ ಉಚಿತ ವಿದ್ಯುತ್ ಲೆಕ್ಕಾಚಾರ ಹೇಗೆ? ಶೂನ್ಯ ಬಿಲ್ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "ಗೃಹಜ್ಯೋತಿ 200 ಯೂನಿಟ್ ಲೆಕ್ಕಾಚಾರ gruha jyothi calculation 200 units free electricity zero bill",
        "answer": """### ⚡ ಗೃಹಜ್ಯೋತಿ ಯೋಜನೆ (Gruha Jyothi Scheme) — ಉಚಿತ ವಿದ್ಯುತ್ ನಿಯಮಗಳು

ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಮನೆಬಳಕೆಯ ಗ್ರಾಹಕರಿಗೆ ಮಾಸಿಕ ಗರಿಷ್ಠ **200 ಯೂನಿಟ್‌ವರೆಗೆ** ಉಚಿತ ವಿದ್ಯುತ್ ಒದಗಿಸಲಾಗುತ್ತದೆ.

---

### 📊 ಉಚಿತ ಯೂನಿಟ್ ಲೆಕ್ಕಾಚಾರದ ಅಧಿಕೃತ ಸೂತ್ರ:
* **ವಾರ್ಷಿಕ ಸರಾಸರಿ ಬಳಕೆ (Average Consumption):** ಹಿಂದಿನ 12 ತಿಂಗಳ (ಹಿಂದಿನ ವರ್ಷದ ಜುಲೈನಿಂದ ಜೂನ್‌ವರೆಗೆ) ಒಟ್ಟು ಬಳಕೆಯ ಸರಾಸರಿ ಯೂನಿಟ್ ಲೆಕ್ಕಹಾಕಲಾಗುತ್ತದೆ.
* **10% ಹೆಚ್ಚುವರಿ ಅರ್ಹತೆ (Entitled Units):** ವಾರ್ಷಿಕ ಸರಾಸರಿ ಯೂನಿಟ್‌ಗೆ 10% ಹೆಚ್ಚುವರಿ ಯೂನಿಟ್ ಸೇರಿಸಲಾಗುತ್ತದೆ (ಗರಿಷ್ಠ ಮಿತಿ 200 ಯೂನಿಟ್‌ಗಳು).

---

### 💡 ಬಿಲ್ಲಿಂಗ್ ನಿಯಮಗಳು:
1. **ಶೂನ್ಯ ಬಿಲ್ (Zero Bill):** ನಿಮ್ಮ ಮಾಸಿಕ ಬಳಕೆ ನಿಮ್ಮ 'ಅರ್ಹತಾ ಯೂನಿಟ್' ಅಥವಾ 200 ಯೂನಿಟ್‌ಗಿಂತ ಕಡಿಮೆಯಿದ್ದರೆ ವಿದ್ಯುತ್ ಬಿಲ್ ₹0 (Zero) ಬರುತ್ತದೆ.
2. **ಭಾಗಶಃ ಬಿಲ್:** ಅರ್ಹತಾ ಮಿತಿಗಿಂತ ಹೆಚ್ಚಿದ್ದು ಆದರೆ 200 ಯೂನಿಟ್‌ಗಿಂತ ಒಳಗಿದ್ದರೆ ಹೆಚ್ಚುವರಿ ಯೂನಿಟ್‌ಗೆ ಮಾತ್ರ ಬಿಲ್ ಕಟ್ಟಬೇಕು.
3. **ಪೂರ್ಣ ಬಿಲ್:** ಮಾಸಿಕ ಬಳಕೆ 200 ಯೂನಿಟ್‌ ಮೀರಿದರೆ ಆ ತಿಂಗಳ ಸಂಪೂರ್ಣ ಬಿಲ್ ಗ್ರಾಹಕರೇ ಪಾವತಿಸಬೇಕು.

🔗 **ಅರ್ಜಿ ಸಲ್ಲಿಕೆ:** ಸೇವಾ ಸಿಂಧು ಪೋರ್ಟಲ್ ಅಥವಾ ವಿದ್ಯುತ್ ಸರಬರಾಜು ಕಂಪನಿಗಳ (BESCOM, HESCOM, GESCOM, MESCOM, CESC) ಪೋರ್ಟಲ್.""",
        "category": "SCHEME",
        "language": "kn",
        "source_url": "https://sevasindhugs.karnataka.gov.in",
        "keywords": "gruha jyothi, free power calculation, 200 units, ಗೃಹಜ್ಯೋತಿ, ಉಚಿತ ವಿದ್ಯುತ್, zero bill",
        "action_label": "⚡ ಗೃಹಜ್ಯೋತಿ ವಿವರ ನೋಡಿ",
        "action_url": "/guarantee-schemes.html"
    },
    {
        "id": "faq_sch_009",
        "question": "ಬಾಡಿಗೆ ಮನೆಯಲ್ಲಿರುವವರು ಗೃಹಜ್ಯೋತಿ ಯೋಜನೆಗೆ ನೋಂದಾಯಿಸಿಕೊಳ್ಳುವುದು ಹೇಗೆ?",
        "normalized_question": "ಬಾಡಿಗೆದಾರರಿಗೆ ಗೃಹಜ್ಯೋತಿ gruha jyothi tenant rental agreement apply seva sindhu",
        "answer": """### 🏠 ಬಾಡಿಗೆದಾರರಿಗೆ ಗೃಹಜ್ಯೋತಿ ಯೋಜನೆಯ ನೋಂದಣಿ ಪ್ರಕ್ರಿಯೆ

ಸ್ವಂತ ಮನೆಯಲ್ಲದ ಬಾಡಿಗೆದಾರರೂ ಸಹ ಗೃಹಜ್ಯೋತಿ 200 ಯೂನಿಟ್ ಉಚಿತ ವಿದ್ಯುತ್ ಸೌಲಭ್ಯ ಪಡೆಯಲು ಅರ್ಹರಾಗಿದ್ದಾರೆ.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
1. ಬಾಡಿಗೆದಾರರ ಆಧಾರ್ ಕಾರ್ಡ್.
2. ಮೀಟರ್‌ನ ವಿದ್ಯುತ್ ಬಿಲ್ (Consumer ID / Account ID).
3. ಮಾನ್ಯತೆ ಇರುವ ಬಾಡಿಗೆ ಕರಾರು ಒಪ್ಪಂದ (Rental Agreement / Lease Agreement) ಅಥವಾ ಅದೇ ವಿಳಾಸವಿರುವ ಮತದಾರರ ಗುರುತಿನ ಚೀಟಿ / ಗ್ಯಾಸ್ ಬಿಲ್.

---

### 💻 ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ವಿಧಾನ:
1. [sevasindhugs.karnataka.gov.in](https://sevasindhugs.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ.
2. ಎಸ್ಕಾಂ ಹೆಸರು ಮತ್ತು Account ID ನಮೂದಿಸಿ.
3. ಗ್ರಾಹಕರ ವಿಧದಲ್ಲಿ **'Tenant (ಬಾಡಿಗೆದಾರ)'** ಎಂದು ಆಯ್ಕೆಮಾಡಿ.
4. ಬಾಡಿಗೆದಾರರ ಆಧಾರ್ ಸಂಖ್ಯೆ ಹಾಕಿ OTP ಮೂಲಕ ಇ-ಸಹಿ ಮಾಡಿ ಸಲ್ಲಿಸಿ.

💡 **ಗಮನಿಸಿ:** ಒಂದು ಆಧಾರ್ ಸಂಖ್ಯೆಗೆ ಕೇವಲ ಒಂದು ವಿದ್ಯುತ್ ಮೀಟರ್ ಸಂಪರ್ಕಕ್ಕೆ ಮಾತ್ರ ಗೃಹಜ್ಯೋತಿ ಸೌಲಭ್ಯ ಲಭ್ಯವಿರುತ್ತದೆ.""",
        "category": "SCHEME",
        "language": "kn",
        "source_url": "https://sevasindhugs.karnataka.gov.in",
        "keywords": "gruha jyothi tenant, rental agreement, ಬಾಡಿಗೆದಾರರು, ಗೃಹಜ್ಯೋತಿ, ಬಾಡಿಗೆ ಮನೆ",
        "action_label": "⚡ ಗೃಹಜ್ಯೋತಿ ಪೋರ್ಟಲ್",
        "action_url": "https://sevasindhugs.karnataka.gov.in"
    },
    {
        "id": "faq_sch_010",
        "question": "ಶಕ್ತಿ ಯೋಜನೆಯಡಿ ಮಹಿಳೆಯರು ಯಾವ ಕೆಎಸ್‌ಆರ್‌ಟಿಸಿ/ಬಿಎಂಟಿಸಿ ಬಸ್‌ಗಳಲ್ಲಿ ಉಚಿತವಾಗಿ ಪ್ರಯಾಣಿಸಬಹುದು?",
        "normalized_question": "ಶಕ್ತಿ ಯೋಜನೆ ಉಚಿತ ಬಸ್ ಯಾವ ಬಸ್ shakti scheme free bus allowed bus types smart card",
        "answer": """### 🚌 ಶಕ್ತಿ ಯೋಜನೆ (Shakti Scheme) — ಮಹಿಳೆಯರಿಗೆ ಉಚಿತ ಬಸ್ ಪ್ರಯಾಣ

ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಮಹಿಳೆಯರು ಹಾಗೂ ಲಿಂಗತ್ವ ಅಲ್ಪಸಂಖ್ಯಾತರು ರಾಜ್ಯದೊಳಗೆ ಸಾರಿಗೆ ನಿಗಮಗಳ ಬಸ್‌ಗಳಲ್ಲಿ ಉಚಿತವಾಗಿ ಪ್ರಯಾಣಿಸಬಹುದು.

---

### ✅ ಉಚಿತ ಪ್ರಯಾಣ ಲಭ್ಯವಿರುವ ಬಸ್‌ಗಳು:
* **KSRTC, NWKRTC, KKRTC:** ನಗರ (City), ಸಾಮಾನ್ಯ (Ordinary) ಮತ್ತು ವೇಗದೂತ (Express) ಬಸ್‌ಗಳು.
* **BMTC (ಬೆಂಗಳೂರು):** ಎಲ್ಲಾ ಸಾಮಾನ್ಯ ನೀಲಿ/ಹಸಿರು ಸಿಟಿ ಬಸ್‌ಗಳು.

---

### ❌ ಉಚಿತವಲ್ಲದ ಪ್ರೀಮಿಯಂ ಬಸ್‌ಗಳು:
* ರಾಜಹಂಸ (Rajahamsa), ನಾನ್‌-ಎಸಿ ಸ್ಲೀಪರ್, ಐರಾವತ (Airavat), ಐರಾವತ ಕ್ಲಬ್ ಕ್ಲಾಸ್, ಇವಿ ಪವರ್ ಪ್ಲಸ್ (EV Power Plus), ಅಂಬಾರಿ ಉತ್ಸವ, ಫ್ಲೈಬಸ್, ವಜ್ರ (Vajra AC) ಮತ್ತು ವಾಯುವಜ್ರ (Airport AC).
* ಕರ್ನಾಟಕದ ಗಡಿಯಾಚೆಗಿನ ಅಂತರರಾಜ್ಯ ಪ್ರಯಾಣ (Inter-state travel).

---

### 🎫 ಪ್ರಯಾಣ ನಿಯಮ:
ಮಹಿಳೆಯರು ತಮ್ಮ ಕರ್ನಾಟಕ ವಿಳಾಸವಿರುವ ಅಧಿಕೃತ ಸರ್ಕಾರದ ಗುರುತಿನ ಚೀಟಿ (ಆಧಾರ್ ಕಾರ್ಡ್, ವೋಟರ್ ಐಡಿ, ಚಾಲನಾ ಪರವಾನಗಿ) ತೋರಿಸಿ ನಿರ್ವಾಹಕರಿಂದ **ಶೂನ್ಯ ದರದ ಟಿಕೆಟ್ (Zero Fare Ticket)** ಪಡೆದುಕೊಳ್ಳಬೇಕು.""",
        "category": "SCHEME",
        "language": "kn",
        "source_url": "https://ksrtc.in",
        "keywords": "shakti scheme, free bus travel women, ksrtc bmtc, ಶಕ್ತಿ ಯೋಜನೆ, ಉಚಿತ ಬಸ್, ಝೀರೋ ಟಿಕೆಟ್",
        "action_label": "🚌 ಶಕ್ತಿ ಯೋಜನೆ ನಿಯಮಗಳು",
        "action_url": "/guarantee-schemes.html"
    },
    {
        "id": "faq_sch_011",
        "question": "ಅನ್ನಭಾಗ್ಯ ಯೋಜನೆಯಡಿ ಅಕ್ಕಿ ಮತ್ತು ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT) ನಿಯಮಗಳು ಯಾವುವು?",
        "normalized_question": "ಅನ್ನಭಾಗ್ಯ ಅಕ್ಕಿ ಹಣ dbt anna bhagya 5kg rice 170 cash bpl phh aay",
        "answer": """### 🍚 ಅನ್ನಭಾಗ್ಯ ಯೋಜನೆ (Anna Bhagya Scheme) ವಿವರ

ರಾಜ್ಯದ ಬಡ ಕುಟುಂಬಗಳ ಆಹಾರ ಭದ್ರತೆಗಾಗಿ BPL ಮತ್ತು ಅಂತ್ಯೋದಯ (AAY) ಕಾರ್ಡ್‌ದಾರರಿಗೆ ತಲಾ **10 ಕೆಜಿ ಆಹಾರ ಧಾನ್ಯ** ಒದಗಿಸಲಾಗುತ್ತದೆ.

---

### 🌾 ಧಾನ್ಯ ಮತ್ತು ನಗದು ಹಂಚಿಕೆಯ ಸೂತ್ರ:
1. **ಕೇಂದ್ರ ಸರ್ಕಾರದ ಪಾಲು (PMGKAY):** ಪ್ರತಿ ಸದಸ್ಯರಿಗೆ **5 ಕೆಜಿ ಉಚಿತ ಅಕ್ಕಿ**.
2. **ರಾಜ್ಯ ಸರ್ಕಾರದ ಪಾಲು:** ಹೆಚ್ಚುವರಿ 5 ಕೆಜಿ ಅಕ್ಕಿ ಲಭ್ಯವಾಗುವವರೆಗೆ ಪ್ರತಿ ಕೆಜಿಗೆ **₹34 ರಂತೆ ಒಟ್ಟು ₹170** ನಗದನ್ನು ಕುಟುಂಬದ ಮುಖ್ಯಸ್ಥರ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT) ಮಾಡಲಾಗುತ್ತದೆ.

---

### 📌 ಅರ್ಹತೆ & ಷರತ್ತುಗಳು:
* ಕುಟುಂಬವು ಸಕ್ರಿಯ BPL (Priority Household) ಅಥವಾ ಅಂತ್ಯೋದಯ (AAY) ಕಾರ್ಡ್ ಹೊಂದಿರಬೇಕು.
* ಪಡಿತರ ಚೀಟಿಯ ಎಲ್ಲಾ ಸದಸ್ಯರ ಆಧಾರ್ e-KYC ಪೂರ್ಣಗೊಂಡಿರಬೇಕು.
* ಕುಟುಂಬದ ಯಜಮಾನಿಯ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ NPCI Aadhaar Mapping ಕಡ್ಡಾಯ.

🔗 **ಆಹಾರ ಇಲಾಖೆ ಪೋರ್ಟಲ್:** [ahara.kar.nic.in](https://ahara.kar.nic.in)""",
        "category": "SCHEME",
        "language": "kn",
        "source_url": "https://ahara.kar.nic.in",
        "keywords": "anna bhagya, 10kg rice, 170 cash dbt, bpl ration, ಅನ್ನಭಾಗ್ಯ, ನಗದು ವರ್ಗಾವಣೆ, ಆಹಾರ ಇಲಾಖೆ",
        "action_label": "🍚 ಆಹಾರ ಇಲಾಖೆ ಪೋರ್ಟಲ್",
        "action_url": "https://ahara.kar.nic.in"
    },
    {
        "id": "faq_sch_012",
        "question": "ಯುವನಿಧಿ (Yuva Nidhi) ನಿರುದ್ಯೋಗ ಭತ್ಯೆ ಯೋಜನೆ: ಯಾರು ಅರ್ಹರು? ಮಾಸಿಕ ಭತ್ಯೆ ಎಷ್ಟು?",
        "normalized_question": "ಯುವನಿಧಿ ಅರ್ಹತೆ ಹಣ yuva nidhi eligibility graduate diploma stipend 3000 1500",
        "answer": """### 🎓 ಯುವನಿಧಿ ಯೋಜನೆ (Yuva Nidhi Scheme) — ಯುವಜನರಿಗೆ ಆರ್ಥಿಕ ನೆರವು

ವ್ಯಾಸಂಗ ಮುಗಿಸಿ ಉದ್ಯೋಗ ಹುಡುಕುತ್ತಿರುವ ಯುವ ಪದವೀಧರರು ಮತ್ತು ಡಿಪ್ಲೋಮಾ ತೇರ್ಗಡೆಯಾದವರಿಗೆ ಆರ್ಥಿಕ ಸ್ಥಿರತೆ ನೀಡಲು ಮಾಸಿಕ ನಿರುದ್ಯೋಗ ಭತ್ಯೆ ನೀಡಲಾಗುತ್ತದೆ.

---

### 💰 ಮಾಸಿಕ ಭತ್ಯೆಯ ವಿವರ:
* **ಪದವೀಧರರಿಗೆ (Degree / Engineering / Medical / Arts / Science / Commerce):** ಪ್ರತಿ ತಿಂಗಳು **₹3,000**.
* **ಡಿಪ್ಲೋಮಾ ಹೊಂದಿದವರಿಗೆ (Diploma Holders):** ಪ್ರತಿ ತಿಂಗಳು **₹1,500**.

---

### 📌 ಅರ್ಹತೆಯ ಮಾನದಂಡಗಳು:
1. ಕರ್ನಾಟಕದಲ್ಲಿ ಕನಿಷ್ಠ 6 ವರ್ಷಗಳ ಕಾಲ ವ್ಯಾಸಂಗ ಮಾಡಿರಬೇಕು.
2. ಪರೀಕ್ಷಾ ಫಲಿತಾಂಶ ಪ್ರಕಟವಾಗಿ 180 ದಿನಗಳು (6 ತಿಂಗಳು) ಕಳೆದರೂ ಯಾವುದೇ ಉದ್ಯೋಗ (ಖಾಸಗಿ/ಸರ್ಕಾರಿ) ಸಿಗದಿರಬೇಕು.
3. ಉನ್ನತ ಶಿಕ್ಷಣಕ್ಕೆ (Higher Education - Post Graduation) ನೋಂದಾಯಿಸಿಕೊಂಡಿರಬಾರದು.
4. ಗರಿಷ್ಠ **2 ವರ್ಷಗಳ ಅವಧಿಗೆ** ಅಥವಾ ಉದ್ಯೋಗ ದೊರೆಯುವವರೆಗೆ (ಯಾವುದು ಮೊದಲೋ ಅದು) ಈ ಭತ್ಯೆ ಜಮೆಯಾಗುತ್ತದೆ.

---

### 📝 ಮಾಸಿಕ ಸ್ವಯಂ ಘೋಷಣೆ (Monthly Self Declaration):
ಪ್ರತಿ ತಿಂಗಳು 25 ನೇ ತಾರೀಖಿನೊಳಗೆ ಸೇವಾ ಸಿಂಧು ಪೋರ್ಟಲ್‌ನಲ್ಲಿ *"ನನಗೆ ಯಾವುದೇ ಉದ್ಯೋಗ ಸಿಕ್ಕಿಲ್ಲ"* ಎಂದು OTP ಮೂಲಕ ದೃಢೀಕರಿಸುವುದು ಕಡ್ಡಾಯ.""",
        "category": "SCHEME",
        "language": "kn",
        "source_url": "https://sevasindhugs.karnataka.gov.in",
        "keywords": "yuva nidhi, 3000 degree stipend, 1500 diploma, ಯುವನಿಧಿ, ನಿರುದ್ಯೋಗ ಭತ್ಯೆ, ಸೇವಾ ಸಿಂಧು",
        "action_label": "🎓 ಯುವನಿಧಿ ಪೋರ್ಟಲ್",
        "action_url": "https://sevasindhugs.karnataka.gov.in"
    },

    # =========================================================================
    # 3. REVENUE, BHOOMI, RTC, MOJINI & PROPERTY REGISTRATION
    # =========================================================================
    {
        "id": "faq_rev_013",
        "question": "ಭೂಮಿ (Bhoomi) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಡಿಜಿಟಲ್ ಪಹಣಿ (RTC) ಡೌನ್‌ಲೋಡ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "bhoomi rtc download pahani online ಪಹಣಿ ಡೌನ್‌ಲೋಡ್ ಭೂಮಿ ಸರ್ವೆ ನಂಬರ್",
        "answer": """### 🌾 ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪಹಣಿ / RTC (Record of Rights, Tenancy and Crops) ಡೌನ್‌ಲೋಡ್

ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಕಂದಾಯ ಇಲಾಖೆಯ ಅಧಿಕೃತ **ಭೂಮಿ (Bhoomi)** ಪೋರ್ಟಲ್ ಮೂಲಕ ನಿಮ್ಮ ಜಮೀನಿನ ನೈಜ ಪಹಣಿ ವೀಕ್ಷಿಸಬಹುದು ಮತ್ತು ಡೌನ್‌ಲೋಡ್ ಮಾಡಬಹುದು.

---

### 💻 ಹಂತ-ಹಂತದ ವಿಧಾನ:
1. **ಭೂಮಿ ವೆಬ್‌ಸೈಟ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [bhoomi.karnataka.gov.in](https://bhoomi.karnataka.gov.in)
2. ಮುಖಪುಟದಲ್ಲಿ **'View RTC Information'** ಅಥವಾ **'RTC Wallet'** ಕ್ಲಿಕ್ ಮಾಡಿ.
3. ನಿಮ್ಮ **ಜಿಲ್ಲೆ (District), ತಾಲೂಕು (Taluk), ಹೋಬಳಿ (Hobli), ಗ್ರಾಮ (Village)** ಆಯ್ಕೆಮಾಡಿ.
4. ನಿಮ್ಮ ಜಮೀನಿನ **ಸರ್ವೆ ನಂಬರ್ (Survey No)** ಹಾಕಿ 'Go' ಕ್ಲಿಕ್ ಮಾಡಿ.
5. ಸರ್ನೋಕ್ (Surnoc), ಹಿಸ್ಸಾ (Hissa) ಮತ್ತು ಅವಧಿ (Period) ಆರಿಸಿ **'Fetch Details'** ಒತ್ತಿರಿ.
6. **View RTC:** ಉಚಿತವಾಗಿ ಪರದೆಯ ಮೇಲೆ ಪಹಣಿ ವೀಕ್ಷಿಸಿ.
7. **ಡಿಜಿಟಲ್ ಸಹಿ ಇರುವ RTC:** ₹15 ಆನ್‌ಲೈನ್ ಶುಲ್ಕ ಪಾವತಿಸಿ ಕಂದಾಯ ಇಲಾಖೆಯ ಅಧಿಕೃತ ಡಿಜಿಟಲ್ ಸಹಿ ಇರುವ ವಾಟರ್‌ಮಾರ್ಕ್ ಪಹಣಿ PDF ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಿ.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://bhoomi.karnataka.gov.in",
        "keywords": "bhoomi rtc, download pahani, survey number, hissa, ಪಹಣಿ, ಭೂಮಿ, ಲ್ಯಾಂಡ್ ರೆಕಾರ್ಡ್",
        "action_label": "🌾 ಭೂಮಿ ಪೋರ್ಟಲ್ ಪ್ರವೇಶಿಸಿ",
        "action_url": "https://bhoomi.karnataka.gov.in"
    },
    {
        "id": "faq_rev_014",
        "question": "ಮ್ಯುಟೇಶನ್ (Mutation Extract / MR) ಎಂದರೇನು? ಅದರ ಆನ್‌ಲೈನ್ ಸ್ಥಿತಿ ನೋಡುವುದು ಹೇಗೆ?",
        "normalized_question": "mutation status bhoomi mr extract ಮ್ಯುಟೇಶನ್ ಸ್ಥಿತಿ ಖಾತಾ ಬದಲಾವಣೆ ವಾರಸುದಾರಿಕೆ",
        "answer": """### 📜 ಮ್ಯುಟೇಶನ್ (Mutation Extract) ಮತ್ತು ಖಾತೆ ಬದಲಾವಣೆ

ಜಮೀನು ಮಾರಾಟವಾದಾಗ, ದಾನ ನೀಡಿದಾಗ, ವಿಭಾಗ ಪತ್ರವಾದಾಗ ಅಥವಾ ಮಾಲೀಕರು ಮೃತಪಟ್ಟು ವಾರಸುದಾರರಿಗೆ ವರ್ಗಾವಣೆಯಾದಾಗ ಕಂದಾಯ ದಾಖಲೆಯಲ್ಲಿ ಮಾಲೀಕತ್ವ ಬದಲಾಯಿಸುವ ಅಧಿಕೃತ ಪ್ರಕ್ರಿಯೆಯನ್ನು **ಮ್ಯುಟೇಶನ್ (ಹಕ್ಕು ಬದಲಾವಣೆ)** ಎನ್ನಲಾಗುತ್ತದೆ.

---

### 🔍 ಮ್ಯುಟೇಶನ್ ಸ್ಥಿತಿ (MR Status) ಟ್ರ್ಯಾಕ್ ಮಾಡುವ ವಿಧಾನ:
1. [bhoomi.karnataka.gov.in](https://bhoomi.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ **'Mutation Status'** ಆಯ್ಕೆಮಾಡಿ.
2. ನಿಮ್ಮ ಜಿಲ್ಲೆ, ತಾಲೂಕು, ಹೋಬಳಿ, ಗ್ರಾಮ ಮತ್ತು ಸರ್ವೆ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ.
3. ಅಥವಾ ಉಪನೋಂದಣಾಧಿಕಾರಿ ಕಚೇರಿಯಲ್ಲಿ ನೋಂದಣಿಯಾದ ನಂತರ ಸಿಕ್ಕ **MR Number** ಹಾಕಿ.
4. **ಹಂತಗಳ ಪರಿಶೀಲನೆ:**
   - ನೋಟಿಸ್ ಜಾರಿ (Form 9, 10 & 12 Notice period - 30 days).
   - ಗ್ರಾಮ ಆಡಳಿತಾಧಿಕಾರಿ (VA) ಪರಿಶೀಲನೆ.
   - ಕಂದಾಯ ನಿರೀಕ್ಷಕರ (RI) ಅನುಮೋದನೆ ಮತ್ತು ತಹಶೀಲ್ದಾರ್ ಡಿಜಿಟಲ್ ಸಹಿ.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://bhoomi.karnataka.gov.in",
        "keywords": "mutation status, mr register, bhoomi mutation, ಮ್ಯುಟೇಶನ್, ಖಾತೆ ಬದಲಾವಣೆ, ವಾರಸುದಾರಿಕೆ",
        "action_label": "📜 ಮ್ಯುಟೇಶನ್ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಿ",
        "action_url": "https://bhoomi.karnataka.gov.in"
    },
    {
        "id": "faq_rev_015",
        "question": "ಕಾವೇರಿ 2.0 (Kaveri 2.0) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಋಣಭಾರ ಪ್ರಮಾಣಪತ್ರ (EC) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "kaveri 2.0 encumbrance certificate ec download online ಋಣಭಾರ ಪ್ರಮಾಣ ಪತ್ರ ಈಸಿ",
        "answer": """### 🏛️ ಕಾವೇರಿ 2.0 (Kaveri 2.0) ನಲ್ಲಿ ಆನ್‌ಲೈನ್ EC (Encumbrance Certificate)

ಯಾವುದೇ ಸ್ಥಿರಾಸ್ತಿಯ ಮೇಲೆ ಬ್ಯಾಂಕ್ ಸಾಲ, ಅಡಮಾನ, ಕೋರ್ಟ್ ತಡೆಯಾಜ್ಞೆ ಅಥವಾ ಹಿಂದಿನ ಮಾರಾಟ ವಹಿವಾಟುಗಳು ಇವೆಯೇ ಎಂದು ತಿಳಿಯಲು **EC (ಋಣಭಾರ ಪ್ರಮಾಣಪತ್ರ)** ಅತ್ಯಗತ್ಯ.

---

### 💻 ಆನ್‌ಲೈನ್ EC ಪಡೆಯುವ ವಿಧಾನ:
1. **ಕಾವೇರಿ 2.0 ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [kaveri.karnataka.gov.in](https://kaveri.karnataka.gov.in)
2. ನಾಗರಿಕ ಲಾಗಿನ್ (Citizen Login) ಮೂಲಕ ಸೈನ್ ಇನ್ ಆಗಿ.
3. **'Online EC'** ಸೇವೆ ಆಯ್ಕೆಮಾಡಿ.
4. ಆಸ್ತಿಯ ವಿವರ (ಜಿಲ್ಲೆ, ಉಪನೋಂದಣಾಧಿಕಾರಿ ಕಚೇರಿ, ಸರ್ವೆ ನಂಬರ್ / ನಿವೇಶನ ಸಂಖ್ಯೆ, ಮತ್ತು ಹುಡುಕಾಟದ ಅವಧಿ ಉದಾ: 15 ಅಥವಾ 30 ವರ್ಷ) ನಮೂದಿಸಿ.
5. ಶುಲ್ಕ ಪಾವತಿಸಿ (Search Fee).
6. ಸಬ್-ರಿಜಿಸ್ಟ್ರಾರ್ ಅವರ ಡಿಜಿಟಲ್ ಸಹಿ ಇರುವ **Form 15 (ವಹಿವಾಟು ಇದ್ದರೆ)** ಅಥವಾ **Form 16 (Nil Encumbrance Certificate)** ತಕ್ಷಣ ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://kaveri.karnataka.gov.in",
        "keywords": "kaveri 2.0, encumbrance certificate, ec download, stamp duty, ಕಾವೇರಿ 2.0, ಈಸಿ, ಋಣಭಾರ",
        "action_label": "🏛️ ಕಾವೇರಿ 2.0 ಪೋರ್ಟಲ್",
        "action_url": "https://kaveri.karnataka.gov.in"
    },
    {
        "id": "faq_rev_016",
        "question": "ದಿಶಾಂಕ್ (Dishank) ಆ್ಯಪ್ ಮತ್ತು ಮೋಜಿನಿ (Mojini) ಮೂಲಕ ಸರ್ವೆ ನಂಬರ್ ಮತ್ತು ಗಡಿ ತಿಳಿಯುವುದು ಹೇಗೆ?",
        "normalized_question": "dishank app mojini survey number boundary 11e sketch ದಿಶಾಂಕ್ ಆ್ಯಪ್ ಮೋಜಿನಿ ನಕ್ಷೆ",
        "answer": """### 🗺️ ದಿಶಾಂಕ್ (Dishank) ಮತ್ತು ಮೋಜಿನಿ (Mojini) ತಂತ್ರಜ್ಞಾನಗಳು

ಕರ್ನಾಟಕ ಕಂದಾಯ ಇಲಾಖೆಯು ಭೂಮಾಪನ ಮತ್ತು ಗಡಿ ವಿವಾದಗಳನ್ನು ತಡೆಯಲು ಅಭಿವೃದ್ಧಿಪಡಿಸಿರುವ ಎರಡು ಅತ್ಯಾಧುನಿಕ ಡಿಜಿಟಲ್ ಸಾಧನಗಳು:

---

### 📱 1. ದಿಶಾಂಕ್ ಆ್ಯಪ್ (Dishank App):
* ನೀವು ಯಾವುದೇ ಜಮೀನಿನಲ್ಲಿ ನಿಂತು ಆ್ಯಪ್ ಆನ್ ಮಾಡಿದರೆ ನಿಮ್ಮ ಫೋನಿನ ಜಿಪಿಎಸ್ (GPS) ಲೊಕೇಶನ್ ಆಧರಿಸಿ ಆ ಜಾಗದ **ನೈಜ ಸರ್ವೆ ನಂಬರ್**, ಹಿಸ್ಸಾ ಮತ್ತು ಗ್ರಾಮದ ನಕ್ಷೆಯನ್ನು ಪರದೆಯ ಮೇಲೆ ಲೈವ್ ಆಗಿ ತೋರಿಸುತ್ತದೆ.
* ಆ ಜಮೀನು ರಾಜಕಾಲುವೆ, ಅರಣ್ಯ ಪ್ರದೇಶ, ಗೋಮಾಳ ಅಥವಾ ಸರ್ಕಾರಿ ಜಾಗವೇ ಎಂಬುದನ್ನು ಖರೀದಿಸುವ ಮುನ್ನವೇ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಬಹುದು.

---

### 📐 2. ಮೋಜಿನಿ ಪೋರ್ಟಲ್ (Mojini):
* ಜಮೀನಿನ ವಿಭಜನೆ (11E ಸ್ಕೆಚ್), ತತ್ಕಾಲ್ ಪೋಡಿ, ಹದ್ದುಬಸ್ತು ಮತ್ತು ಅಲೈನ್ಮೆಂಟ್ ನಕ್ಷೆಗಳ ಅರ್ಜಿ ಸಲ್ಲಿಕೆ ಹಾಗೂ ಸ್ಟೇಟಸ್ ತಿಳಿಯಲು [mojini.karnataka.gov.in](https://mojini.karnataka.gov.in) ಬಳಸಲಾಗುತ್ತದೆ.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://mojini.karnataka.gov.in",
        "keywords": "dishank app, mojini survey, 11e sketch, podi, ದಿಶಾಂಕ್, ಮೋಜಿನಿ, ಸರ್ವೆ ನಂಬರ್",
        "action_label": "🗺️ ಮೋಜಿನಿ ಪೋರ್ಟಲ್",
        "action_url": "https://mojini.karnataka.gov.in"
    },

    # =========================================================================
    # 4. CITIZEN CERTIFICATES & WELFARE (NADAKACHERI / SEVA SINDHU)
    # =========================================================================
    {
        "id": "faq_cert_017",
        "question": "ನಾಡಕಚೇರಿಯಲ್ಲಿ ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ (Caste & Income Certificate) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "nadakacheri caste income certificate online apply ಜಾತಿ ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರ rd number",
        "answer": """### 📑 ನಾಡಕಚೇರಿ (Nadakacheri / Atalji Janasnehi Kendra) ಸೇವೆಗಳು

ಶೈಕ್ಷಣಿಕ ವಿದ್ಯಾರ್ಥಿವೇತನಗಳು, ಶಾಲಾ ಪ್ರವೇಶ, ಸರ್ಕಾರಿ ಉದ್ಯೋಗ ಹಾಗೂ ಸಬ್ಸಿಡಿ ಯೋಜನೆಗಳಿಗೆ ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ ಅತ್ಯಗತ್ಯ.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
* ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ರೇಷನ್ ಕಾರ್ಡ್.
* ಶಾಲಾ ವರ್ಗಾವಣೆ ಪ್ರಮಾಣಪತ್ರ (TC / Study Certificate) - ಜಾತಿ ನಮೂದಾಗಿರಬೇಕು.
* ಸ್ವಯಂ ಘೋಷಣಾ ಪತ್ರ ಮತ್ತು ಆದಾಯದ ಪುರಾವೆ (ವೇತನ ಚೀಟಿ / ಪಹಣಿ).

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಕೆಯ ವಿಧಾನ:
1. [nadakacheri.karnataka.gov.in](https://nadakacheri.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಮೂಲಕ ಲಾಗಿನ್ ಆಗಿ.
2. **'Online Application' -> 'Caste / Income Certificate'** ಆಯ್ಕೆಮಾಡಿ.
3. ಪ್ರವರ್ಗ (Category 1, 2A, 2B, 3A, 3B, SC, ST) ಆಯ್ಕೆಮಾಡಿ ಕುಟುಂಬದ ವಿವರ ಭರ್ತಿ ಮಾಡಿ.
4. ₹40 ಆನ್‌ಲೈನ್ ಸೇವಾ ಶುಲ್ಕ ಪಾವತಿಸಿ.
5. ಗ್ರಾಮ ಆಡಳಿತಾಧಿಕಾರಿ (VA) ಮತ್ತು ಕಂದಾಯ ನಿರೀಕ್ಷಕರು (RI) ಸ್ಥಳ ತನಿಖೆ ನಡೆಸಿ ಅನುಮೋದಿಸಿದ ನಂತರ ನಿಮ್ಮ **RD Number** ಬಳಸಿ ಡಿಜಿಟಲ್ ಸಹಿಯುಳ್ಳ ಸರ್ಟಿಫಿಕೇಟ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.""",
        "category": "CERTIFICATES",
        "language": "kn",
        "source_url": "https://nadakacheri.karnataka.gov.in",
        "keywords": "caste income certificate, nadakacheri rd number, ಜಾತಿ ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರ, ನಾಡಕಚೇರಿ, ಆರ್‌ಡಿ ನಂಬರ್",
        "action_label": "📑 ನಾಡಕಚೇರಿ ಪೋರ್ಟಲ್",
        "action_url": "https://nadakacheri.karnataka.gov.in"
    },
    {
        "id": "faq_cert_018",
        "question": "ಸಂಧ್ಯಾ ಸುರಕ್ಷಾ ಮತ್ತು ವೃದ್ಧಾಪ್ಯ ವೇತನಕ್ಕೆ ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ನಿಯಮಗಳೇನು?",
        "normalized_question": "sandhya suraksha old age pension monthly amount ಸಂಧ್ಯಾ ಸುರಕ್ಷಾ ಮಾಸಾಶನ ವೃದ್ಧಾಪ್ಯ ವೇತನ",
        "answer": """### 👵 ಸಂಧ್ಯಾ ಸುರಕ್ಷಾ ಯೋಜನೆ (Sandhya Suraksha Scheme)

ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಸಾಮಾಜಿಕ ಭದ್ರತಾ ಯೋಜನೆಯಡಿ ನಿರ್ಗತಿಕ ಮತ್ತು ಬಡ ಹಿರಿಯ ನಾಗರಿಕರಿಗೆ ಮಾಸಿಕ ಪಿಂಚಣಿ ನೀಡಲಾಗುತ್ತದೆ.

---

### 📌 ಅರ್ಹತೆ & ನೆರವು:
* **ವಯಸ್ಸು:** 65 ವರ್ಷ ಮತ್ತು ಅದಕ್ಕಿಂತ ಮೇಲ್ಪಟ್ಟ ಹಿರಿಯ ನಾಗರಿಕರು.
* **ಮಾಸಿಕ ಪಿಂಚಣಿ:** ಪ್ರತಿ ತಿಂಗಳು **₹1,200** ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT).
* **ಆದಾಯ ಮಿತಿ:** ಫಲಾನುಭವಿ ಹಾಗೂ ಅವರ ಸಂಗಾತಿಯ ಒಟ್ಟು ವಾರ್ಷಿಕ ಆದಾಯ ₹32,000 ಮೀರಬಾರದು.
* ಯಾವುದೇ ಸಾರ್ವಜನಿಕ ಅಥವಾ ಖಾಸಗಿ ಸಂಸ್ಥೆಯಿಂದ ಬೇರೆ ಯಾವುದೇ ಪಿಂಚಣಿ ಪಡೆಯುತ್ತಿರಬಾರದು.

---

### 📝 ಅರ್ಜಿ ಸಲ್ಲಿಕೆ:
ಗ್ರಾಮ ಒನ್, ಕರ್ನಾಟಕ ಒನ್ ಅಥವಾ ನಾಡಕಚೇರಿ ಕೇಂದ್ರಗಳಲ್ಲಿ ವಯಸ್ಸಿನ ದಾಖಲೆ (ಆಧಾರ್/ವೋಟರ್ ಐಡಿ), ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರದೊಂದಿಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು.""",
        "category": "WELFARE",
        "language": "kn",
        "source_url": "https://nadakacheri.karnataka.gov.in",
        "keywords": "sandhya suraksha, senior citizen pension, ವೃದ್ಧಾಪ್ಯ ವೇತನ, ಸಂಧ್ಯಾ ಸುರಕ್ಷಾ, ಮಾಸಾಶನ",
        "action_label": "👵 ನಾಡಕಚೇರಿ ಪಿಂಚಣಿ ಸೇವೆ",
        "action_url": "https://nadakacheri.karnataka.gov.in"
    },

    # =========================================================================
    # 5. STATE ADMINISTRATION, LEADERSHIP & CONSTITUENCIES
    # =========================================================================
    {
        "id": "faq_adm_019",
        "question": "ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಪ್ರಸ್ತುತ ಮುಖ್ಯಮಂತ್ರಿ, ಸಚಿವ ಸಂಪುಟ ಮತ್ತು ಸಾಂವಿಧಾನಿಕ ನಾಯಕರು ಯಾರು?",
        "normalized_question": "ಕರ್ನಾಟಕ ಮುಖ್ಯಮಂತ್ರಿ ಸಂಪುಟ ನಾಯಕರು ಯಾರು cm of karnataka leadership cabinet",
        "answer": """### 🏛️ ಕರ್ನಾಟಕ ರಾಜ್ಯ ಕಾರ್ಯಾಂಗ & ಆಡಳಿತ ನಾಯಕತ್ವ

* **ಮುಖ್ಯಮಂತ್ರಿ:** **ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್ (D.K. Shivakumar)** (ಕನಕಪುರ ಕ್ಷೇತ್ರ - INC)
* **ಉಪಮುಖ್ಯಮಂತ್ರಿ:** **ಡಾ. ಜಿ. ಪರಮೇಶ್ವರ್ (Dr. G. Parameshwara)** (ಕೊರಟಗೆರೆ ಕ್ಷೇತ್ರ - INC)
* **ರಾಜ್ಯಪಾಲರು:** **ಥಾವರ್‌ಚಂದ್ ಗೆಹ್ಲೋಟ್ (Thaawarchand Gehlot)**
* **ಮುಖ್ಯ ಕಾರ್ಯದರ್ಶಿ (Chief Secretary):** **ಡಾ. ಶಾಲಿನಿ ರಜನೀಶ್, IAS**
* **ವಿಧಾನಸಭಾ ಸಂಖ್ಯಾಬಲ:** ಒಟ್ಟು 224 ಚುನಾಯಿತ ಸದಸ್ಯರು.
* **ಲೋಕಸಭಾ ಕ್ಷೇತ್ರಗಳು:** 28 ಸಂಸದರು.""",
        "category": "ADMIN",
        "language": "kn",
        "source_url": "https://karnataka.gov.in",
        "keywords": "cm, chief minister, dks, parameshwara, ಮುಖ್ಯಮಂತ್ರಿ, ಆಡಳಿತ, ಸಚಿವ ಸಂಪುಟ, cabinet",
        "action_label": "👥 ಅಧಿಕಾರಿಗಳು & ಸಂಪುಟ ನೋಡಿ",
        "action_url": "/officers.html"
    },
    {
        "id": "faq_adm_020",
        "question": "ಕರ್ನಾಟಕದ 4 ಕಂದಾಯ ವಿಭಾಗಗಳು ಮತ್ತು 31 ಜಿಲ್ಲೆಗಳ ವಿನ್ಯಾಸವೇನು?",
        "normalized_question": "karnataka 4 revenue divisions 31 districts list ಕರ್ನಾಟಕ ಕಂದಾಯ ವಿಭಾಗಗಳು ಜಿಲ್ಲೆಗಳು",
        "answer": """### 🗺️ ಕರ್ನಾಟಕದ ಕಂದಾಯ ವಿಭಾಗಗಳು (Revenue Divisions) ಮತ್ತು 31 ಜಿಲ್ಲೆಗಳು:

ಆಡಳಿತಾತ್ಮಕ ಅನುಕೂಲಕ್ಕಾಗಿ ಕರ್ನಾಟಕವನ್ನು 4 ಪ್ರಮುಖ ವಿಭಾಗಗಳಾಗಿ ವಿಂಗಡಿಸಲಾಗಿದೆ:

---

1. **ಬೆಂಗಳೂರು ವಿಭಾಗ (Bengaluru Division - 9 ಜಿಲ್ಲೆಗಳು):**
   - ಬೆಂಗಳೂರು ನಗರ, ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ, ರಾಮನಗರ, ಕೋಲಾರ, ಚಿಕ್ಕಬಳ್ಳಾಪುರ, ತುಮಕೂರು, ಶಿವಮೊಗ್ಗ, ಚಿತ್ರದುರ್ಗ, ದಾವಣಗೆರೆ.
2. **ಮೈಸೂರು ವಿಭಾಗ (Mysuru Division - 8 ಜಿಲ್ಲೆಗಳು):**
   - ಮೈಸೂರು, ಮಂಡ್ಯ, ಹಾಸನ, ಚಿಕ್ಕಮಗಳೂರು, ದಕ್ಷಿಣ ಕನ್ನಡ, ಉಡುಪಿ, ಕೊಡಗು, ಚಾಮರಾಜನಗರ.
3. **ಬೆಳಗಾವಿ ವಿಭಾಗ (Belagavi Division - 7 ಜಿಲ್ಲೆಗಳು):**
   - ಬೆಳಗಾವಿ, ಧಾರವಾಡ, ವಿಜಯಪುರ, ಬಾಗಲಕೋಟೆ, ಗದಗ, ಹಾವೇರಿ, ಉತ್ತರ ಕನ್ನಡ.
4. **ಕಲಬುರಗಿ ವಿಭಾಗ (Kalaburagi Division - 7 ಜಿಲ್ಲೆಗಳು):**
   - ಕಲಬುರಗಿ, ಬೀದರ್, ರಾಯಚೂರು, ಕೊಪ್ಪಳ, ಬಳ್ಳಾರಿ, ಯಾದಗಿರಿ, ವಿಜಯನಗರ (ರಾಜ್ಯದ 31ನೇ ನೂತನ ಜಿಲ್ಲೆ).""",
        "category": "ADMIN",
        "language": "kn",
        "source_url": "https://karnataka.gov.in",
        "keywords": "31 districts, revenue divisions, bengaluru, mysuru, belagavi, kalaburagi, ಕಂದಾಯ ವಿಭಾಗ",
        "action_label": "🗺️ 31 ಜಿಲ್ಲೆಗಳ ಮ್ಯಾಟ್ರಿಕ್ಸ್",
        "action_url": "/districts.html"
    },

    # =========================================================================
    # 6. SCHOLARSHIPS (SSP) & HIGHER EDUCATION
    # =========================================================================
    {
        "id": "faq_edu_021",
        "question": "SSP (State Scholarship Portal) ಪೋಸ್ಟ್-ಮೆಟ್ರಿಕ್ ವಿದ್ಯಾರ್ಥಿವೇತನಕ್ಕೆ ಅರ್ಜಿ ಸಲ್ಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "ssp scholarship karnataka post matric apply e-attestation ಎಸ್ಎಸ್ಪಿ ವಿದ್ಯಾರ್ಥಿವೇತನ",
        "answer": """### 🎓 SSP (State Scholarship Portal) ಪೋಸ್ಟ್-ಮೆಟ್ರಿಕ್ ವಿದ್ಯಾರ್ಥಿವೇತನ

ಕರ್ನಾಟಕದ ಎಸ್‌ಸಿ, ಎಸ್‌ಟಿ, ಹಿಂದುಳಿದ ವರ್ಗಗಳು (OBC), ಅಲ್ಪಸಂಖ್ಯಾತ ಮತ್ತು ಬ್ರಾಹ್ಮಣ ಅಭಿವೃದ್ಧಿ ಮಂಡಳಿಯ ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ SSP ಏಕೀಕೃತ ಪೋರ್ಟಲ್ ಆಗಿದೆ.

---

### 📋 ಅಗತ್ಯ ವಿವರ & ದಾಖಲೆಗಳು:
* ವಿದ್ಯಾರ್ಥಿ ಮತ್ತು ಪೋಷಕರ ಆಧಾರ್ ಸಂಖ್ಯೆ.
* ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರದ **RD Number**.
* ಕಾಲೇಜು ಪ್ರವೇಶ ನೋಂದಣಿ ಸಂಖ್ಯೆ (Student University Reg No) ಮತ್ತು ಶುಲ್ಕ ರಶೀದಿ.
* ಹಾಸ್ಟೆಲ್ ವಿವರಗಳು (ಸರ್ಕಾರಿ ಅಥವಾ ಅನುಮೋದಿತ ಖಾಸಗಿ ಹಾಸ್ಟೆಲ್).
* ಆಧಾರ್ ಸೀಡೆಡ್ ಬ್ಯಾಂಕ್ ಖಾತೆ (NPCI Active Bank Account).

---

### 💻 ಅರ್ಜಿ ಹಂತಗಳು:
1. [ssp.postmatric.karnataka.gov.in](https://ssp.postmatric.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ Student ID ರಚಿಸಿ.
2. ಇ-ದೃಢೀಕರಣ (e-Attestation): ಶುಲ್ಕ ರಶೀದಿ ಮತ್ತು ಅಂಕಪಟ್ಟಿಗಳನ್ನು ನಿಮ್ಮ ಕಾಲೇಜಿನ ಇ-ಅಟೆಸ್ಟೇಶನ್ ಅಧಿಕಾರಿಯಿಂದ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ದೃಢೀಕರಿಸಿ.
3. ಕಾಲೇಜು ಮತ್ತು ಕೋರ್ಸ್ ಆಯ್ಕೆಮಾಡಿ ಸಬ್ಮಿಟ್ ಮಾಡಿ.""",
        "category": "EDUCATION",
        "language": "kn",
        "source_url": "https://ssp.postmatric.karnataka.gov.in",
        "keywords": "ssp scholarship, post matric scholarship, e-attestation, ಎಸ್ಎಸ್ಪಿ ವಿದ್ಯಾರ್ಥಿವೇತನ, ಇ-ಅಟೆಸ್ಟೇಷನ್",
        "action_label": "🎓 SSP ಪೋರ್ಟಲ್",
        "action_url": "https://ssp.postmatric.karnataka.gov.in"
    },

    # =========================================================================
    # 7. CIVIC & UTILITIES (BBMP, BESCOM, BWSSB, TRANSIT, HEALTH)
    # =========================================================================
    {
        "id": "faq_civ_022",
        "question": "ಬೆಂಗಳೂರಿನಲ್ಲಿ BBMP ಇ-ಖಾತಾ ಮತ್ತು ಆಸ್ತಿ ತೆರಿಗೆ (Property Tax) ಪಾವತಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "bbmp e khata download online property tax a khata b khata ಬಿಬಿಎಂಪಿ ಇ-ಖಾತಾ ಆಸ್ತಿ ತೆರಿಗೆ",
        "answer": """### 🏢 BBMP ಇ-ಖಾತಾ (e-Aasthi) ಮತ್ತು ಆಸ್ತಿ ತೆರಿಗೆ ಪಾವತಿ

ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಮಹಾನಗರ ವ್ಯಾಪ್ತಿಯ ಆಸ್ತಿಗಳ ನಿರ್ವಹಣೆಗೆ ಬಿಬಿಎಂಪಿ ಇ-ಖಾತಾ ಕಡ್ಡಾಯವಾಗಿದೆ.

---

### 📜 ಇ-ಖಾತಾ (e-Aasthi) ಡೌನ್‌ಲೋಡ್:
* [bbmpeaasthi.karnataka.gov.in](https://bbmpeaasthi.karnataka.gov.in) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನಿಮ್ಮ 10 ಅಂಕಿಗಳ Property PID ಸಂಖ್ಯೆ ನಮೂದಿಸಿ ಡಿಜಿಟಲ್ ಇ-ಖಾತಾ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.

---

### 💳 ಆಸ್ತಿ ತೆರಿಗೆ ಪಾವತಿ ವಿಧಾನ:
1. [bbmptax.karnataka.gov.in](https://bbmptax.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ.
2. SAS Base Application Number ಅಥವಾ PID ನಮೂದಿಸಿ 'Fetch' ಕ್ಲಿಕ್ ಮಾಡಿ.
3. ಬಾಕಿ ತೆರಿಗೆ ವಿವರ ಪರಿಶೀಲಿಸಿ UPI, ನೆಟ್ ಬ್ಯಾಂಕಿಂಗ್ ಅಥವಾ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ ಮೂಲಕ ಪಾವತಿಸಿ ತಕ್ಷಣ ಅಧಿಕೃತ ರಶೀದಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಿ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bbmptax.karnataka.gov.in",
        "keywords": "bbmp e khata, bbmp property tax, a khata, b khata, ಬೆಂಗಳೂರು ಆಸ್ತಿ ತೆರಿಗೆ, ಇ-ಖಾತಾ",
        "action_label": "🏢 BBMP ಆಸ್ತಿ ಪೋರ್ಟಲ್",
        "action_url": "https://bbmptax.karnataka.gov.in"
    },
    {
        "id": "faq_civ_023",
        "question": "ಬೆಸ್ಕಾಂ (BESCOM) ವಿದ್ಯುತ್ ಬಿಲ್ ಪಾವತಿ ಮತ್ತು ತುರ್ತು ದೂರು ಸಹಾಯವಾಣಿ ಯಾವುದು?",
        "normalized_question": "bescom bill payment power cut complaint 1912 ಬೆಸ್ಕಾಂ ವಿದ್ಯುತ್ ಬಿಲ್ ದೂರು",
        "answer": """### 💡 ಬೆಸ್ಕಾಂ (BESCOM) ವಿದ್ಯುತ್ ಸೇವೆಗಳು & 24/7 ಸಹಾಯವಾಣಿ

* **ತುರ್ತು ವಿದ್ಯುತ್ ದೂರು ಸಂಖ್ಯೆ:** **1912** (ಟೋಲ್-ಫ್ರೀ / ವಿದ್ಯುತ್ ಕಡಿತ, ಟ್ರಾನ್ಸ್‌ಫಾರ್ಮರ್ ಸಮಸ್ಯೆ, ತುರ್ತು ಅಪಾಯಗಳಿಗೆ).
* **WhatsApp ದೂರು ಸಂಖ್ಯೆ:** 9483191212 / 9483191222.
* **ಆನ್‌ಲೈನ್ ಬಿಲ್ ಪಾವತಿ:** [bescom.karnataka.gov.in](https://bescom.karnataka.gov.in) ಅಥವಾ **BESCOM Mithra App** ನಲ್ಲಿ ನಿಮ್ಮ 10 ಅಂಕಿಗಳ Account ID ನಮೂದಿಸಿ ಪಾವತಿಸಬಹುದು.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bescom.karnataka.gov.in",
        "keywords": "bescom 1912, electricity bill online, power complaint, ಬೆಸ್ಕಾಂ ಬಿಲ್, ವಿದ್ಯುತ್ ದೂರು",
        "action_label": "💡 ಬೆಸ್ಕಾಂ ಪೋರ್ಟಲ್",
        "action_url": "https://bescom.karnataka.gov.in"
    },
    {
        "id": "faq_civ_024",
        "question": "ಆಯುಷ್ಮಾನ್ ಭಾರತ್ - ಆರೋಗ್ಯ ಕರ್ನಾಟಕ (AB-ArK) ಯೋಜನೆಯಡಿ ಉಚಿತ ಚಿಕಿತ್ಸೆ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "ayushman bharat arogya karnataka free treatment ಆಯುಷ್ಮಾನ್ ಭಾರತ್ ಆರೋಗ್ಯ ಕರ್ನಾಟಕ",
        "answer": """### 🏥 ಆಯುಷ್ಮಾನ್ ಭಾರತ್ - ಆರೋಗ್ಯ ಕರ್ನಾಟಕ (AB-ArK) ಆರೋಗ್ಯ ಭದ್ರತೆ

ರಾಜ್ಯದ ಪ್ರತಿಯೊಬ್ಬ ನಾಗರಿಕರಿಗೂ ಗುಣಮಟ್ಟದ ಚಿಕಿತ್ಸೆ ಒದಗಿಸುವ ಸಾರ್ವತ್ರಿಕ ಆರೋಗ್ಯ ಯೋಜನೆ.

---

### 💰 ಚಿಕಿತ್ಸಾ ಮಿತಿ:
* **BPL / ಅಂತ್ಯೋದಯ ಕಾರ್ಡ್‌ದಾರರು:** ವರ್ಷಕ್ಕೆ ಪ್ರತಿ ಕುಟುಂಬಕ್ಕೆ ಗರಿಷ್ಠ **₹5 ಲಕ್ಷದವರೆಗೆ** ಸಂಪೂರ್ಣ ಉಚಿತ ಚಿಕಿತ್ಸೆ.
* **APL ಕಾರ್ಡ್‌ದಾರರು:** ಪ್ಯಾಕೇಜ್ ದರದ **30% ರಿಯಾಯಿತಿ** (ವರ್ಷಕ್ಕೆ ಗರಿಷ್ಠ ₹1.50 ಲಕ್ಷ).

---

### 🏥 ಚಿಕಿತ್ಸೆ ಪಡೆಯುವ ವಿಧಾನ:
1. ಸಾಮಾನ್ಯ ಚಿಕಿತ್ಸೆಗಳಿಗೆ ನೇರವಾಗಿ ತಾಲೂಕು ಅಥವಾ ಜಿಲ್ಲಾ ಸರ್ಕಾರಿ ಆಸ್ಪತ್ರೆಗೆ ಭೇಟಿ ನೀಡಿ.
2. ಸರ್ಕಾರಿ ಆಸ್ಪತ್ರೆಯಲ್ಲಿ ಲಭ್ಯವಿಲ್ಲದ ಸೂಪರ್ ಸ್ಪೆಷಾಲಿಟಿ ಚಿಕಿತ್ಸೆಗಳಿಗೆ ವೈದ್ಯರಿಂದ **ರೆಫರಲ್ ಪತ್ರ (Referral Letter)** ಪಡೆದು ಎಂಪ್ಯಾನೆಲ್ ಆದ ಖಾಸಗಿ ಆಸ್ಪತ್ರೆಗಳಿಗೆ ಹೋಗಬಹುದು.
3. ತುರ್ತು ಅಪಘಾತ ಮತ್ತು ಜೀವನ್ಮರಣ ಸ್ಥಿತಿಯಲ್ಲಿ ರೆಫರಲ್ ಇಲ್ಲದೆಯೇ ನೇರವಾಗಿ ಖಾಸಗಿ ಆಸ್ಪತ್ರೆಗೆ ದಾಖಲಾಗಬಹುದು.""",
        "category": "HEALTH",
        "language": "kn",
        "source_url": "https://arogya.karnataka.gov.in",
        "keywords": "arogya karnataka, ayushman bharat ark, 5 lakh free hospital, ಆರೋಗ್ಯ ಕರ್ನಾಟಕ, ಉಚಿತ ಚಿಕಿತ್ಸೆ",
        "action_label": "🏥 ಆರೋಗ್ಯ ಕರ್ನಾಟಕ ವಿವರ",
        "action_url": "https://arogya.karnataka.gov.in"
    },
    {
        "id": "faq_civ_025",
        "question": "ಫ್ರೂಟ್ಸ್ (FRUITS) ಪೋರ್ಟಲ್ ಎಂದರೇನು? ರೈತರ FID ನಂಬರ್ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "fruits portal fid number farmer registration ಫ್ರೂಟ್ಸ್ ತಂತ್ರಾಂಶ ಎಫ್ಐಡಿ ಕೃಷಿ ಸಾಲ",
        "answer": """### 👨‍🌾 FRUITS (Farmer Registration & Unified Beneficiary Information System)

ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಕೃಷಿ, ತೋಟಗಾರಿಕೆ, ರೇಷ್ಮೆ ಮತ್ತು ಪಶುಸಂಗೋಪನಾ ಇಲಾಖೆಗಳ ಸೌಲಭ್ಯಗಳನ್ನು ಒಂದೇ ಸೂರಿನಡಿ ತರಲು ಅಭಿವೃದ್ಧಿಪಡಿಸಲಾದ ತಂತ್ರಾಂಶ.

---

### 📌 FID (Farmer Identification Number) ಮಹತ್ವ:
* ಪ್ರತಿ ರೈತ ಕುಟುಂಬಕ್ಕೆ ನೀಡಲಾಗುವ ವಿಶಿಷ್ಟ ಗುರುತಿನ ಸಂಖ್ಯೆಯೇ **FID**.
* ಬೆಳೆ ವಿಮೆ ಪರಿಹಾರ, ಕಿಸಾನ್ ಸಮ್ಮಾನ್ ನಿಧಿ, ಬಿತ್ತನೆ ಬೀಜ/ರಸಗೊಬ್ಬರ ಸಬ್ಸಿಡಿ, ಟ್ರ್ಯಾಕ್ಟರ್ ಸಹಾಯಧನ ಮತ್ತು ಶೂನ್ಯ ಬಡ್ಡಿ ಸಾಲ ಪಡೆಯಲು FID ಕಡ್ಡಾಯ.

---

### 📝 FID ಪಡೆಯುವ ವಿಧಾನ:
1. ಹತ್ತಿರದ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ (RSK) ಅಥವಾ ಗ್ರಾಮ ಪಂಚಾಯಿತಿಗೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಮೀನಿನ ಪಹಣಿ (RTC), ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ಸಲ್ಲಿಸಿ ತಕ್ಷಣ FID ರಚಿಸಿಕೊಳ್ಳಿ.
3. ಆನ್‌ಲೈನ್ ಸ್ಥಿತಿ ಪರಿಶೀಲನೆ: [fruits.karnataka.gov.in](https://fruits.karnataka.gov.in)""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://fruits.karnataka.gov.in",
        "keywords": "fruits portal, fid number, farmer id, ಬೆಳೆ ಸಾಲ, ಸಬ್ಸಿಡಿ, ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ",
        "action_label": "🌾 FRUITS ಪೋರ್ಟಲ್",
        "action_url": "https://fruits.karnataka.gov.in"
    },
    {
        "id": "faq_civ_026",
        "question": "ಪರಿಹಾರ (Parihara) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಬೆಳೆ ಹಾನಿ ಮತ್ತು ಬರ ಪರಿಹಾರ ಚೆಕ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "parihara crop loss drought compensation check online ಪರಿಹಾರ ಬೆಳೆ ಹಾನಿ ಹಣ",
        "answer": """### 🌾 ಪರಿಹಾರ (Parihara) ಪೋರ್ಟಲ್ — ಬೆಳೆ ಹಾನಿ ಪರಿಹಾರ ಟ್ರ್ಯಾಕಿಂಗ್

ಅತಿವೃಷ್ಟಿ, ಅನಾವೃಷ್ಟಿ ಅಥವಾ ಬರಗಾಲದಿಂದ ಹಾನಿಗೊಳಗಾದ ಬೆಳೆಗಳಿಗೆ ರಾಜ್ಯ ಮತ್ತು ಎನ್‌ಡಿಆರ್‌ಎಫ್ (NDRF) ನಿಧಿಯಿಂದ ನೇರವಾಗಿ ರೈತರ ಖಾತೆಗೆ DBT ಜಮೆ ಮಾಡಲಾಗುತ್ತದೆ.

---

### 🔍 ಪರಿಹಾರ ಹಣ ಚೆಕ್ ಮಾಡುವ ವಿಧಾನ:
1. **ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [parihara.karnataka.gov.in](https://parihara.karnataka.gov.in)
2. **'Parihara Payment Status'** ಆಯ್ಕೆಮಾಡಿ.
3. ವರ್ಷ ಮತ್ತು ಋತು (Kharif / Rabi) ಆಯ್ಕೆಮಾಡಿ.
4. ರೈತರ **ಆಧಾರ್ ಸಂಖ್ಯೆ** ಅಥವಾ **FID ಸಂಖ್ಯೆ** ಅಥವಾ **ಸರ್ವೆ ನಂಬರ್** ನಮೂದಿಸಿ 'Fetch Details' ಕ್ಲಿಕ್ ಮಾಡಿ.
5. ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾದ ಮೊತ್ತ, ದಿನಾಂಕ ಮತ್ತು UTR ನಂಬರ್ ಪರದೆಯ ಮೇಲೆ ಲಭ್ಯವಾಗುತ್ತದೆ.""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://parihara.karnataka.gov.in",
        "keywords": "parihara status, crop loss dbt, drought compensation, ಪರಿಹಾರ ಬೆಳೆ ಹಾನಿ, ಬರ ಪರಿಹಾರ",
        "action_label": "🌾 ಪರಿಹಾರ ಸ್ಥಿತಿ ನೋಡಿ",
        "action_url": "https://parihara.karnataka.gov.in"
    },
    {
        "id": "faq_civ_027",
        "question": "ಕರ್ನಾಟಕ ಪೊಲೀಸ್ ತುರ್ತು ಸಹಾಯವಾಣಿ 112 ಮತ್ತು KSP App ನ ಪ್ರಯೋಜನಗಳೇನು?",
        "normalized_question": "karnataka police emergency 112 ksp app e-lost complaint ಪೊಲೀಸ್ ಸಹಾಯವಾಣಿ",
        "answer": """### 👮 ಕರ್ನಾಟಕ ಪೊಲೀಸ್ (KSP) ತುರ್ತು ಸೇವೆಗಳು & ನಾಗರಿಕ ಸೌಲಭ್ಯಗಳು

* **ತುರ್ತು ಸಹಾಯವಾಣಿ: 112 (Emergency Response Support System):** ಪೊಲೀಸ್, ಅಗ್ನಿಶಾಮಕ ಮತ್ತು ಆಂಬ್ಯುಲೆನ್ಸ್ ಮೂರೂ ಸೇವೆಗಳಿಗೆ ಒಂದೇ ತುರ್ತು ಸಂಖ್ಯೆ. ಕರೆ ಮಾಡಿದ 15 ನಿಮಿಷಗಳಲ್ಲಿ ಹೊಯ್ಸಳ/ಪೊಲೀಸ್ ವಾಹನ ಸ್ಥಳಕ್ಕೆ ತಲುಪುತ್ತದೆ.
* **KSP Citizen Mobile App:**
  - **E-Lost Report:** ಮೊಬೈಲ್, ಪಾಸ್‌ಪೋರ್ಟ್, ದಾಖಲೆಗಳು ಕಳೆದುಹೋದರೆ ಠಾಣೆಗೆ ಹೋಗದೆ ಮೊಬೈಲ್‌ನಲ್ಲೇ ಡಿಜಿಟಲ್ ಪ್ರಮಾಣಪತ್ರ ಪಡೆಯಬಹುದು.
  - **FIR Status:** ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಎಫ್‌ಐಆರ್ ಪ್ರತಿಯನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.
  - **ಹಿರಿಯ ನಾಗರಿಕರ ರಕ್ಷಣೆ:** ಹಿರಿಯ ನಾಗರಿಕರು ತುರ್ತು ರಕ್ಷಣೆಗಾಗಿ ನೋಂದಾಯಿಸಿಕೊಳ್ಳಬಹುದು.""",
        "category": "POLICE",
        "language": "kn",
        "source_url": "https://ksp.karnataka.gov.in",
        "keywords": "ksp app, 112 emergency, e lost app, ಕರ್ನಾಟಕ ಪೊಲೀಸ್, ತುರ್ತು ಸಹಾಯವಾಣಿ",
        "action_label": "👮 ಪೊಲೀಸ್ ಪೋರ್ಟಲ್",
        "action_url": "https://ksp.karnataka.gov.in"
    }
]

# =============================================================================
# 8. COMPLETE 31 DISTRICTS COMPREHENSIVE ADMINISTRATIVE MATRIX (62 FAQs)
# Generates 2 deeply detailed FAQs for every single district in Karnataka:
#   - Administrative Hub, Subdivisions, Taluks, DC/SP governance, Economy
#   - SIR Draft Roll, Assembly Constituencies (224 mapping) & Polling Station checks
# =============================================================================

DISTRICTS_FULL_DATA = [
    ("bengaluru_urban", "ಬೆಂಗಳೂರು ನಗರ", "Bengaluru Urban", "ಬೆಂಗಳೂರು ಉತ್ತರ, ಬೆಂಗಳೂರು ದಕ್ಷಿಣ, ಬೆಂಗಳೂರು ಪೂರ್ವ, ಆನೇಕಲ್, ಯಲಹಂಕ", 28, "ಮಾಹಿತಿ ತಂತ್ರಜ್ಞಾನ, ಜೈವಿಕ ತಂತ್ರಜ್ಞಾನ, ಕೈಗಾರಿಕೆ ಹಾಗೂ ವಾಣಿಜ್ಯ"),
    ("bengaluru_rural", "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ", "Bengaluru Rural", "ದೇವನಹಳ್ಳಿ, ನೆಲಮಂಗಲ, ದೊಡ್ಡಬಳ್ಳಾಪುರ, ಹೊಸಕೋಟೆ", 4, "ರೇಷ್ಮೆ, ಕೃಷಿ, ಕೈಗಾರಿಕಾ ಕಾರಿಡಾರ್ ಹಾಗೂ ಕೆಂಪೇಗೌಡ ಅಂತಾರಾಷ್ಟ್ರೀಯ ವಿಮಾನ ನಿಲ್ದಾಣ"),
    ("ramanagara", "ರಾಮನಗರ", "Ramanagara", "ರಾಮನಗರ, ಕನಕಪುರ, ಚನ್ನಪಟ್ಟಣ, ಮಾಗಡಿ", 4, "ರೇಷ್ಮೆ ಮಾರುಕಟ್ಟೆ (ಸಿಲ್ಕ್ ಸಿಟಿ), ಚನ್ನಪಟ್ಟಣದ ಮರದ ಬೊಂಬೆಗಳು ಮತ್ತು ಕೃಷಿ"),
    ("kolar", "ಕೋಲಾರ", "Kolar", "ಕೋಲಾರ, ಬಂಗಾರಪೇಟೆ, ಮಾಲೂರು, ಮುಳಬಾಗಿಲು, ಶ್ರೀನಿವಾಸಪುರ", 6, "ಮಾವು ಬೆಳೆ, ಚಿನ್ನದ ಗಣಿ ಇತಿಹಾಸ, ಹಾಲು ಉತ್ಪಾದನೆ ಮತ್ತು ರೇಷ್ಮೆ"),
    ("chikkaballapur", "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", "Chikkaballapur", "ಚಿಕ್ಕಬಳ್ಳಾಪುರ, ಬಾಗೇಪಲ್ಲಿ, ಗೌರಿಬಿದನೂರು, ಚಿಂತಾಮಣಿ, ಶಿಡ್ಲಘಟ್ಟ, ಗುಡಿಬಂಡೆ", 5, "ದ್ರಾಕ್ಷಿ ಬೆಳೆ, ನಂದಿಬೆಟ್ಟ ಪ್ರವಾಸೋದ್ಯಮ ಮತ್ತು ರೇಷ್ಮೆ ಕೃಷಿ"),
    ("tumakuru", "ತುಮಕೂರು", "Tumakuru", "ತುಮಕೂರು, ಕುಣಿಗಲ್, ಗುಬ್ಬಿ, ತಿಪಟೂರು, ಚಿಕ್ಕನಾಯಕನಹಳ್ಳಿ, ಶಿರಾ, ಪಾವಗಡ, ಮಧುಗಿರಿ, ಕೊರಟಗೆರೆ, ತುರುವೇಕೆರೆ", 11, "ತೆಂಗು ಉತ್ಪಾದನೆ (ಕಲ್ಪತರು ನಾಡು), ಪಾವಗಡ ಸೋಲಾರ್ ಪಾರ್ಕ್, ಕೈಗಾರಿಕೆಗಳು"),
    ("shivamogga", "ಶಿವಮೊಗ್ಗ", "Shivamogga", "ಶಿವಮೊಗ್ಗ, ಭದ್ರಾವತಿ, ತೀರ್ಥಹಳ್ಳಿ, ಸಾಗರ, ಶಿಕಾರಿಪುರ, ಸೊರಬ, ಹೊಸನಗರ", 7, "ಅಡಿಕೆ ಬೆಳೆ, ಜೋಗ ಜಲಪಾತ, ಮಲೆನಾಡಿನ ನಿಸರ್ಗ ಸಂಪತ್ತು ಮತ್ತು ಕಬ್ಬಿಣ ಕೈಗಾರಿಕೆ"),
    ("chitradurga", "ಚಿತ್ರದುರ್ಗ", "Chitradurga", "ಚಿತ್ರದುರ್ಗ, ಚಳ್ಳಕೆರೆ, ಹಿರಿಯೂರು, ಹೊಳಲ್ಕೆರೆ, ಹೊಸದುರ್ಗ, ಮೊಳಕಾಲ್ಮುರು", 6, "ಏಳು ಸುತ್ತಿನ ಕೋಟೆ, ಸೈನ್ಸ್ ಸಿಟಿ (ಚಳ್ಳಕೆರೆ), ಸಿರಿಧಾನ್ಯ ಮತ್ತು ಪವನ ಶಕ್ತಿ"),
    ("davanagere", "ದಾವಣಗೆರೆ", "Davanagere", "ದಾವಣಗೆರೆ, ಹರಿಹರ, ಜಗಳೂರು, ಚನ್ನಗಿರಿ, ಹೊನ್ನಾಳಿ, ನ್ಯಾಮತಿ", 7, "ಬೆಣ್ಣೆ ದೋಸೆ, ಜವಳಿ ಕೈಗಾರಿಕೆ (ಮ್ಯಾಂಚೆಸ್ಟರ್), ಅಡಿಕೆ ಮತ್ತು ಮೆಕ್ಕೆಜೋಳ"),
    ("mysuru", "ಮೈಸೂರು", "Mysuru", "ಮೈಸೂರು, ನಂಜನಗೂಡು, ಹುಣಸೂರು, ಪಿರಿಯಾಪಟ್ಟಣ, ಕೆ.ಆರ್.ನಗರ, ಹೆಚ್.ಡಿ.ಕೋಟೆ, ಸರಗೂರು, ಟಿ.ನರಸೀಪುರ", 11, "ಸಾಂಸ್ಕೃತಿಕ ರಾಜಧಾನಿ, ಅರಮನೆ, ಪ್ರವಾಸೋದ್ಯಮ, ಮೈಸೂರು ಪಾಕ್ ಮತ್ತು ರೇಷ್ಮೆ"),
    ("mandya", "ಮಂಡ್ಯ", "Mandya", "ಮಂಡ್ಯ, ಮದ್ದೂರು, ಮಳವಳ್ಳಿ, ಪಾಂಡವಪುರ, ಶ್ರೀರಂಗಪಟ್ಟಣ, ಕೃಷ್ಣರಾಜಪೇಟೆ, ನಾಗಮಂಗಲ", 7, "ಸಕ್ಕರೆ ನಾಡು, ಕಾವೇರಿ ನೀರಾವರಿ ಕೃಷಿ, ಬೆಲ್ಲ ಮತ್ತು ಭತ್ತ"),
    ("hassan", "ಹಾಸನ", "Hassan", "ಹಾಸನ, ಅರಸೀಕೆರೆ, ಚನ್ನರಾಯಪಟ್ಟಣ, ಹೊಳೆನರಸೀಪುರ, ಸಕಲೇಶಪುರ, ಆಲೂರು, ಅರಕಲಗೂಡು, ಬೇಲೂರು", 7, "ಶಿಲ್ಪಕಲೆ (ಬೇಲೂರು-ಹಳೇಬೀಡು), ಹಾಸನಾಂಬೆ ದೇವಾಲಯ, ಕಾಫಿ ಮತ್ತು ಏಲಕ್ಕಿ"),
    ("chikkamagaluru", "ಚಿಕ್ಕಮಗಳೂರು", "Chikkamagaluru", "ಚಿಕ್ಕಮಗಳೂರು, ಕಡೂರು, ತರೀಕೆರೆ, ಮೂಡಿಗೆರೆ, ಕೊಪ್ಪ, ಶೃಂಗೇರಿ, ನರಸಿಂಹರಾಜಪುರ, ಅಜ್ಜಂಪುರ", 5, "ಕಾಫಿಯ ತವರು, ಮುಳ್ಳಯ್ಯನಗಿರಿ, ಶೃಂಗೇರಿ ಶಾರದಾಂಬೆ ಮತ್ತು ಮಲೆನಾಡು ಪ್ರವಾಸೋದ್ಯಮ"),
    ("dakshina_kannada", "ದಕ್ಷಿಣ ಕನ್ನಡ", "Dakshina Kannada", "ಮಂಗಳೂರು, ಬಂಟ್ವಾಳ, ಪುತ್ತೂರು, ಬೆಳ್ತಂಗಡಿ, ಸುಳ್ಯ, ಕಡಬ, ಮೂಡುಬಿದಿರೆ", 8, "ನವ ಮಂಗಳೂರು ಬಂದರು, ಬ್ಯಾಂಕಿಂಗ್ ರಾಜಧಾನಿ, ಕರಾವಳಿ ಶಿಕ್ಷಣ ಹಬ್ ಮತ್ತು ಗೋಡಂಬಿ"),
    ("udupi", "ಉಡುಪಿ", "Udupi", "ಉಡುಪಿ, ಕುಂದಾಪುರ, ಕಾರ್ಕಳ, ಬೈಂದೂರು, ಬ್ರಹ್ಮಾವರ, ಕಾಪು, ಹೆಬ್ರಿ", 5, "ಶ್ರೀಕೃಷ್ಣ ಮಠ, ಕರಾವಳಿ ಪ್ರವಾಸೋದ್ಯಮ, ಮೀನುಗಾರಿಕೆ ಮತ್ತು ಉನ್ನತ ಶಿಕ್ಷಣ"),
    ("kodagu", "ಕೊಡಗು", "Kodagu", "ಮಡಿಕೇರಿ, ವಿರಾಜಪೇಟೆ, ಸೋಮವಾರಪೇಟೆ, ಪೊನ್ನಂಪೇಟೆ, ಕುಶಾಲನಗರ", 2, "ಭಾರತದ ಸ್ಕಾಟ್‌ಲ್ಯಾಂಡ್, ಕಾಫಿ ಎಸ್ಟೇಟ್, ಕಿತ್ತಳೆ, ಏಲಕ್ಕಿ ಮತ್ತು ಯೋಧರ ನಾಡು"),
    ("chamarajanagar", "ಚಾಮರಾಜನಗರ", "Chamarajanagar", "ಚಾಮರಾಜನಗರ, ಗುಂಡ್ಲುಪೇಟೆ, ಕೊಳ್ಳೇಗಾಲ, ಹನೂರು, ಯಳಂದೂರು", 4, "ಬಂಡೀಪುರ ಹುಲಿ ಸಂರಕ್ಷಿತಾರಣ್ಯ, ಮಲೆ ಮಹದೇಶ್ವರ ಬೆಟ್ಟ, ರೇಷ್ಮೆ ಮತ್ತು ಅರಣ್ಯ ಉತ್ಪನ್ನಗಳು"),
    ("belagavi", "ಬೆಳಗಾವಿ", "Belagavi", "ಬೆಳಗಾವಿ, ಗೋಕಾಕ್, ಚಿಕ್ಕೋಡಿ, ಅಥಣಿ, ಬೈಲಹೊಂಗಲ, ಹುಕ್ಕೇರಿ, ರಾಮದುರ್ಗ, ಸವದತ್ತಿ, ಖಾನಾಪುರ, ರಾಯಬಾಗ, ನಿಪ್ಪಾಣಿ, ಮೂಡಲಗಿ, ಕಾಗವಾಡ, ಕಿತ್ತೂರು", 18, "ಸುವರ್ಣ ಸೌಧ, ಕುಂದಾ ಸಿಹಿ, ಕಬ್ಬು ಮತ್ತು ಸಕ್ಕರೆ ಕಾರ್ಖಾನೆಗಳು, ಗಡಿ ವಾಣಿಜ್ಯ"),
    ("dharwad", "ಧಾರವಾಡ", "Dharwad", "ಧಾರವಾಡ, ಹುಬ್ಬಳ್ಳಿ ನಗರ, ಹುಬ್ಬಳ್ಳಿ ಗ್ರಾಮೀಣ, ಕುಂದಗೋಳ, ನವಲಗುಂದ, ಕಲಘಟಗಿ, ಅಣ್ಣಿಗೇರಿ, ಅಳ್ನಾವರ", 7, "ವಿದ್ಯಾನಗರಿ, ಧಾರವಾಡ ಪೇಡ, ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ ಸ್ಮಾರ್ಟ್ ಸಿಟಿ ಮತ್ತು ಹೈಕೋರ್ಟ್ ಪೀಠ"),
    ("vijayapura", "ವಿಜಯಪುರ", "Vijayapura", "ವಿಜಯಪುರ, ಇಂಡಿ, ಮುದ್ದೇಬಿಹಾಳ, ಬಸವನ ಬಾಗೇವಾಡಿ, ಸಿಂದಗಿ, ತಾಳಿಕೋಟೆ, ಚಡಚಣ, ತಿಕೋಟಾ, ಬಬಲೇಶ್ವರ, ದೇವರಹಿಪ್ಪರಗಿ, ಕೊಲ್ಹಾರ, ಆಲಮೇಲ", 8, "ಗೋಳಗುಮ್ಮಟ, ಐತಿಹಾಸಿಕ ಸ್ಮಾರಕಗಳು, ದ್ರಾಕ್ಷಿ ಮತ್ತು ನಿಂಬೆ ಬೆಳೆ"),
    ("bagalkote", "ಬಾಗಲಕೋಟೆ", "Bagalkote", "ಬಾಗಲಕೋಟೆ, ಬಾದಾಮಿ, ಜಮಖಂಡಿ, ಮುಧೋಳ, ಹುನಗುಂದ, ಬೀಳಗಿ, ರಬಕವಿ ಬನಹಟ್ಟಿ, ಇಳಕಲ್, ಗುಳೇದಗುಡ್ಡ", 7, "ಇಳಕಲ್ ಸೀರೆ, ಬಾದಾಮಿ ಗುಹಾಂತರ ದೇವಾಲಯಗಳು, ಪಟ್ಟದಕಲ್ಲು ಮತ್ತು ಕಬ್ಬು"),
    ("gadag", "ಗದಗ", "Gadag", "ಗದಗ, ರೋಣ, ಶಿರಹಟ್ಟಿ, ನರಗುಂದ, ಮುಂಡರಗಿ, ಗಜೇಂದ್ರಗಡ, ಲಕ್ಷ್ಮೇಶ್ವರ", 4, "ಮುದ್ರಣ ನಗರಿ, ಸಹಕಾರಿ ಚಳವಳಿಯ ತವರು, ಕಪ್ಪತಗುಡ್ಡ ಮತ್ತು ಪವನ ವಿದ್ಯುತ್"),
    ("haveri", "ಹಾವೇರಿ", "Haveri", "ಹಾವೇರಿ, ರಾಣೆಬೆನ್ನೂರು, ಬ್ಯಾಡಗಿ, ಹಿರೇಕೆರೂರು, ಹಾನಗಲ್, ಸವಣೂರು, ಶಿಗ್ಗಾಂವಿ, ರಟ್ಟಿಹಳ್ಳಿ", 6, "ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ, ಏಲಕ್ಕಿ ಹಾರ, ಕನಕದಾಸರ ತವರು (ಕಾಗಿನೆಲೆ) ಮತ್ತು ಬೀಜೋತ್ಪಾದನೆ"),
    ("uttara_kannada", "ಉತ್ತರ ಕನ್ನಡ", "Uttara Kannada", "ಕಾರವಾರ, ಅಂಕೋಲಾ, ಕುಮಟಾ, ಹೊನ್ನಾವರ, ಭಟ್ಕಳ, ಶಿರಸಿ, ಸಿದ್ದಾಪುರ, ಯಲ್ಲಾಪುರ, ಹಳಿಯಾಳ, ಜೋಯಿಡಾ, ಮುಂಡಗೋಡ, ದಾಂಡೇಲಿ", 6, "ಐಎನ್‌ಎಸ್ ಕದಂಬ ನೌಕಾನೆಲೆ, ದಾಂಡೇಲಿ ಅರಣ್ಯ, ಗೋಕರ್ಣ ಪ್ರವಾಸೋದ್ಯಮ ಮತ್ತು ಅಡಿಕೆ"),
    ("kalaburagi", "ಕಲಬುರಗಿ", "Kalaburagi", "ಕಲಬುರಗಿ, ಆಳಂದ, ಅಫಜಲಪುರ, ಜೇವರ್ಗಿ, ಸೇಡಂ, ಚಿತ್ತಾಪುರ, ಚಿಂಚೋಳಿ, ಕಾಳಗಿ, ಕಮಲಾಪುರ, ಶಹಾಬಾದ್, ಯಡ್ರಾಮಿ", 9, "ತೊಗರಿ ಕಣಜ, ಸಿಮೆಂಟ್ ಕೈಗಾರಿಕೆಗಳು, ಗುಲಬರ್ಗಾ ಕೋಟೆ ಮತ್ತು ಹೈಕೋರ್ಟ್ ಪೀಠ"),
    ("bidar", "ಬೀದರ್", "Bidar", "ಬೀದರ್, ಬಸವಕಲ್ಯಾಣ, ಭಾಲ್ಕಿ, ಹುಮ್ನಾಬಾದ್, ಔರಾದ್, ಕಮಲನಗರ, ಚಿಟಗುಪ್ಪ, ಹುಲಸೂರು", 6, "ಬಿದ್ರಿ ಕಲೆ, ಗುರು ನಾನಕ್ ಝೀರಾ, ಅನುಭವ ಮಂಟಪ (ಬಸವಕಲ್ಯಾಣ) ಮತ್ತು ಐತಿಹಾಸಿಕ ಕೋಟೆ"),
    ("raichur", "ರಾಯಚೂರು", "Raichur", "ರಾಯಚೂರು, ಮಾನ್ವಿ, ಸಿಂಧನೂರು, ದೇವದುರ್ಗ, ಲಿಂಗಸುಗೂರು, ಮಸ್ಕಿ, ಸಿರವಾರ", 7, "ಶಾಖೋತ್ಪನ್ನ ವಿದ್ಯುತ್ ಸ್ಥಾವರ (RTPS), ಸೋನಾ ಮಸೂರಿ ಭತ್ತ ಮತ್ತು ಹತ್ತಿ ಬೆಳೆ"),
    ("koppal", "ಕೊಪ್ಪಳ", "Koppal", "ಕೊಪ್ಪಳ, ಗಂಗಾವತಿ, ಕುಷ್ಟಗಿ, ಯಲಬುರ್ಗಾ, ಕನಕಗಿರಿ, ಕಾರಟಗಿ, ಕುಕನೂರು", 5, "ಕಿನ್ನಾಳ ಕರಕುಶಲ ಕಲೆ, ಭತ್ತದ ಕಣಜ (ಗಂಗಾವತಿ), ಅಂಜನಾದ್ರಿ ಬೆಟ್ಟ ಮತ್ತು ಆನೆಗೊಂದಿ"),
    ("ballari", "ಬಳ್ಳಾರಿ", "Ballari", "ಬಳ್ಳಾರಿ, ಸಿರುಗುಪ್ಪ, ಸಂಡೂರು, ಕುರುಗೋಡು, ಕಂಪ್ಲಿ", 5, "ಉಕ್ಕು ಕೈಗಾರಿಕೆ (ಜಿಂದಾಲ್), ಕಬ್ಬಿಣದ ಅದಿರು, ಜೀನ್ಸ್ ವಸ್ತ್ರೋದ್ಯಮ ಮತ್ತು ಬಳ್ಳಾರಿ ಕೋಟೆ"),
    ("yadgir", "ಯಾದಗಿರಿ", "Yadgir", "ಯಾದಗಿರಿ, ಶಹಾಪುರ, ಸುರಪುರ, ಗುರುಮಿಠಕಲ್, ವಡಗೇರಾ, ಹುಣಸಗಿ", 4, "ಬೋನಾಳ ಪಕ್ಷಿಧಾಮ, ತೊಗರಿ ಮತ್ತು ಭತ್ತದ ಕೃಷಿ, ಕೃಷ್ಣಾ ನದಿ ಕಣಿವೆ ಯೋಜನೆಗಳು"),
    ("vijayanagara", "ವಿಜಯನಗರ", "Vijayanagara", "ಹೊಸಪೇಟೆ, ಹರಪನಹಳ್ಳಿ, ಹೂವಿನಹಡಗಲಿ, ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ, ಕೊಟ್ಟೂರು, ಕೂಡ್ಲಿಗಿ", 5, "ಹಂಪಿ ವಿಶ್ವ ಪರಂಪರೆ ತಾಣ, ತುಂಗಭದ್ರಾ ಜಲಾಶಯ (ಹೊಸಪೇಟೆ) ಮತ್ತು ಕೈಗಾರಿಕೆಗಳು")
]

counter = 28
for code, name_kn, name_en, taluks, mla_count, econ in DISTRICTS_FULL_DATA:
    # 1. District Administrative Master FAQ
    FAQS.append({
        "id": f"faq_dist_{counter:03d}",
        "question": f"{name_kn} ({name_en}) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?",
        "normalized_question": f"{name_kn} {name_en} ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla",
        "answer": f"""### 🏛️ {name_kn} ({name_en}) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** {name_kn}
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** {mla_count} ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** {taluks}.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** {econ}.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.""",
        "category": "DISTRICTS",
        "language": "kn",
        "source_url": f"https://{code.replace('_', '')}.nic.in",
        "keywords": f"{name_kn}, {name_en}, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats",
        "action_label": f"🏛️ {name_kn} ಜಿಲ್ಲಾ ಪುಟ",
        "action_url": f"/districts/{code}.html"
    })
    counter += 1

    # 2. District SIR & Electoral Roll FAQ
    FAQS.append({
        "id": f"faq_dist_sir_{counter:03d}",
        "question": f"{name_kn} ಜಿಲ್ಲೆಯ {mla_count} ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": f"{name_kn} {name_en} sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth",
        "answer": f"""### 🗳️ {name_kn} ({name_en}) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

{name_kn} ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **{mla_count} ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **'{name_kn}'** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.""",
        "category": "SIR",
        "language": "kn",
        "source_url": "https://ceokarnataka.kar.nic.in",
        "keywords": f"{name_kn}, {name_en}, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, {mla_count} mla",
        "action_label": f"🔎 {name_kn} Draft Roll ನೋಡಿ",
        "action_url": "/karnataka-sir-voter-roll.html"
    })
    counter += 1

# =============================================================================
# KNOWLEDGE DOCUMENTS (MASTER GUIDES FOR RAG & DEEP SEARCH)
# =============================================================================

DOCUMENTS = [
    {
        "id": "doc_sir_overview",
        "title": "Karnataka SIR Electoral Roll Complete Guide & Methodology",
        "content": """ಕರ್ನಾಟಕ ವಿಶೇಷ ಸಂಕ್ಷಿಪ್ತ ಪರಿಷ್ಕರಣೆ (SIR) ಪ್ರಕ್ರಿಯೆಯು ಭಾರತೀಯ ಚುನಾವಣಾ ಆಯೋಗದ (ECI) ಕಟ್ಟುನಿಟ್ಟಾದ ಮಾರ್ಗಸೂಚಿಗಳ ಅಡಿಯಲ್ಲಿ ನಡೆಯುತ್ತದೆ.
ರಾಜ್ಯದ 31 ಜಿಲ್ಲೆಗಳ 224 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ವ್ಯಾಪ್ತಿಯಲ್ಲಿರುವ ಸುಮಾರು 5.4 ಕೋಟಿ ಮತದಾರರ ಮಾಹಿತಿಯನ್ನು ನಿರಂತರವಾಗಿ ನವೀಕರಿಸಲಾಗುತ್ತದೆ.
ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ತಾಲೂಕು ಕಚೇರಿಗಳು, ಮತಗಟ್ಟೆಗಳು ಹಾಗೂ ceokarnataka.kar.nic.in ಮತ್ತು karnata.in ಪೋರ್ಟಲ್‌ಗಳಲ್ಲಿ ಪ್ರಕಟಿಸಲಾಗುತ್ತದೆ.
ಪ್ರತಿ ಮತಗಟ್ಟೆಗೆ ಒಬ್ಬ ಬೂತ್ ಮಟ್ಟದ ಅಧಿಕಾರಿಯನ್ನು (BLO) ನೇಮಿಸಲಾಗಿದ್ದು, ಫಾರ್ಮ್ 6, 7, 8 ಅರ್ಜಿಗಳನ್ನು ಆನ್‌ಲೈನ್ ಮತ್ತು ಆಫ್‌ಲೈನ್‌ನಲ್ಲಿ ಸ್ವೀಕರಿಸಲಾಗುತ್ತದೆ.
ಮತದಾರರ ಸಹಾಯವಾಣಿ 1950 ಮೂಲಕ ಸಾರ್ವಜನಿಕರು ಯಾವುದೇ ದೂರುಗಳನ್ನು ದಾಖಲಿಸಬಹುದು.""",
        "url": "/karnataka-sir-voter-roll.html",
        "category": "SIR",
        "source_type": "official_eci",
        "source_url": "https://ceokarnataka.kar.nic.in",
        "keywords": "sir, electoral roll, draft roll, voter list, eci, blo, form 6, form 8"
    },
    {
        "id": "doc_schemes_overview",
        "title": "Karnataka 5 Guarantee Welfare Schemes Master Guide",
        "content": """ಕರ್ನಾಟಕ ಸರ್ಕಾರದ 5 ಪ್ರಮುಖ ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳ ನಿಯಮಾವಳಿ ಮತ್ತು ಅನುಷ್ಠಾನ:
1. ಗೃಹಲಕ್ಷ್ಮಿ: ಕುಟುಂಬದ ಯಜಮಾನಿ ಮಹಿಳೆಗೆ ಪ್ರತಿ ತಿಂಗಳು ₹2,000 ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT). ತೆರಿಗೆ ಪಾವತಿದಾರರಲ್ಲದ ಕುಟುಂಬಗಳಿಗೆ ಸೌಲಭ್ಯ.
2. ಗೃಹಜ್ಯೋತಿ: ಗೃಹಬಳಕೆಯ ಪ್ರತಿ ಮನೆಗೆ ಮಾಸಿಕ 200 ಯೂನಿಟ್‌ವರೆಗೆ ಉಚಿತ ವಿದ್ಯುತ್. ವಾರ್ಷಿಕ ಸರಾಸರಿ ಬಳಕೆ + 10% ಹೆಚ್ಚುವರಿ ಯೂನಿಟ್ ಸೂತ್ರ.
3. ಶಕ್ತಿ ಯೋಜನೆ: ರಾಜ್ಯದ ನಾಲ್ಕೂ ಸಾರಿಗೆ ನಿಗಮಗಳ (KSRTC, BMTC, NWKRTC, KKRTC) ಸಾಮಾನ್ಯ ಮತ್ತು ಎಕ್ಸ್‌ಪ್ರೆಸ್ ಬಸ್‌ಗಳಲ್ಲಿ ಮಹಿಳೆಯರಿಗೆ ಸಂಪೂರ್ಣ ಉಚಿತ ಪ್ರಯಾಣ.
4. ಅನ್ನಭಾಗ್ಯ: BPL ಮತ್ತು ಅಂತ್ಯೋದಯ ಕಾರ್ಡ್‌ನ ಪ್ರತಿ ಸದಸ್ಯರಿಗೆ 10 ಕೆಜಿ ಆಹಾರ ಧಾನ್ಯ (5 ಕೆಜಿ ಅಕ್ಕಿ + 5 ಕೆಜಿಗೆ ತಲಾ ₹34 ರಂತೆ ₹170 DBT ನಗದು).
5. ಯುವನಿಧಿ: ಪದವೀಧರರಿಗೆ ₹3,000 ಮತ್ತು ಡಿಪ್ಲೋಮಾದಾರರಿಗೆ ₹1,500 ಮಾಸಿಕ ನಿರುದ್ಯೋಗ ಭತ್ಯೆ (ಗರಿಷ್ಠ 2 ವರ್ಷಗಳವರೆಗೆ).""",
        "url": "/guarantee-schemes.html",
        "category": "SCHEMES",
        "source_type": "official_gov",
        "source_url": "https://sevasindhugs.karnataka.gov.in",
        "keywords": "guarantee schemes, gruha lakshmi, gruha jyothi, shakti, anna bhagya, yuva nidhi"
    },
    {
        "id": "doc_land_revenue_overview",
        "title": "Karnataka Digital Land Records & Property Registration Guide",
        "content": """ಕರ್ನಾಟಕ ಕಂದಾಯ ಇಲಾಖೆಯ ಡಿಜಿಟಲ್ ಪೋರ್ಟಲ್‌ಗಳು ಮತ್ತು ಸೇವೆಗಳು:
1. ಭೂಮಿ (Bhoomi): ಪಹಣಿ (RTC), ಮ್ಯುಟೇಶನ್ ರೆಜಿಸ್ಟರ್ (MR Extract), ಕಂದಾಯ ನಕ್ಷೆಗಳು ಮತ್ತು ಇ-ಕನ್ವರ್ಶನ್ ಸೇವೆಗಳು.
2. ಕಾವೇರಿ 2.0 (Kaveri 2.0): ಆನ್‌ಲೈನ್ ಆಸ್ತಿ ನೋಂದಣಿ, ಮುದ್ರಾಂಕ ಶುಲ್ಕ ಲೆಕ್ಕಾಚಾರ, ಅಪಾಯಿಂಟ್‌ಮೆಂಟ್ ಸ್ಲಾಟ್ ಬುಕಿಂಗ್ ಮತ್ತು ಆನ್‌ಲೈನ್ ಋಣಭಾರ ಪ್ರಮಾಣಪತ್ರ (EC).
3. ಮೋಜಿನಿ (Mojini): ಭೂ ಅಳತೆ, 11E ಸ್ಕೆಚ್, ತತ್ಕಾಲ್ ಪೋಡಿ ಮತ್ತು ಸರ್ವೆ ಅರ್ಜಿಗಳ ಲೈವ್ ಟ್ರ್ಯಾಕಿಂಗ್.
4. ದಿಶಾಂಕ್ (Dishank): ಜಿಪಿಎಸ್ ಆಧಾರಿತ ನೈಜ ಸರ್ವೆ ನಂಬರ್ ಮತ್ತು ಜಮೀನಿನ ಸ್ವರೂಪ ತಿಳಿಸುವ ಮೊಬೈಲ್ ಆ್ಯಪ್.""",
        "url": "/revenue-services.html",
        "category": "REVENUE",
        "source_type": "official_gov",
        "source_url": "https://bhoomi.karnataka.gov.in",
        "keywords": "bhoomi, kaveri 2.0, mojini, dishank, land records, rtc, mutation, ec"
    },
    {
        "id": "doc_districts_overview",
        "title": "Karnataka 31 Districts Administrative & Assembly Matrix",
        "content": """ಕರ್ನಾಟಕ ರಾಜ್ಯವು 4 ಕಂದಾಯ ವಿಭಾಗಗಳು (ಬೆಂಗಳೂರು, ಮೈಸೂರು, ಬೆಳಗಾವಿ, ಕಲಬುರಗಿ) ಮತ್ತು 31 ಜಿಲ್ಲೆಗಳನ್ನು ಒಳಗೊಂಡಿದೆ.
ರಾಜ್ಯದಲ್ಲಿ ಒಟ್ಟು 224 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು ಹಾಗೂ 28 ಲೋಕಸಭಾ ಕ್ಷೇತ್ರಗಳಿವೆ.
ಪ್ರತಿ ಜಿಲ್ಲೆಯ ಆಡಳಿತವನ್ನು ಜಿಲ್ಲಾಧಿಕಾರಿ (DC), ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ (SP) ಹಾಗೂ ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ (CEO) ಮುನ್ನಡೆಸುತ್ತಾರೆ.
ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರರು ಕಂದಾಯ ಮತ್ತು ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತಾರೆ.""",
        "url": "/districts.html",
        "category": "DISTRICTS",
        "source_type": "official_gov",
        "source_url": "https://karnataka.gov.in",
        "keywords": "31 districts, dc, sp, tahsildar, taluk, mla, mp, karnataka, revenue divisions"
    }
]

# =========================================================================
# 9. ADVANCED CITIZEN SERVICES, TRANSPORT, SCHEMES & WELFARE (121+)
# =========================================================================

ADDITIONAL_EXPANSION_FAQS = [
    {
        "id": "faq_sakala_121",
        "question": "ಸಕಾಲ (Sakala) ಕಾಯ್ದೆ ಎಂದರೇನು? ನಿಗದಿತ ಅವಧಿಯಲ್ಲಿ ಸರ್ಕಾರಿ ಸೇವೆ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "sakala services karnataka guarantee of services act track gsc number ಸಕಾಲ ಸೇವೆಗಳು",
        "answer": """### ⏱️ ಕರ್ನಾಟಕ ಸಕಾಲ ಸೇವೆಗಳ ಕಾಯ್ದೆ (Sakala Services Guarantee Act)

ಕರ್ನಾಟಕ ನಾಗರಿಕ ಸೇವೆಗಳ ಖಾತರಿ ಅಧಿನಿಯಮ (ಸಕಾಲ) ಅಡಿಯಲ್ಲಿ ರಾಜ್ಯ ಸರ್ಕಾರದ 1,100 ಕ್ಕೂ ಹೆಚ್ಚು ನಾಗರಿಕ ಸೇವೆಗಳನ್ನು ನಿಗದಿತ ಕಾಲಮಿತಿಯೊಳಗೆ (Time-bound Delivery) ಪಡೆಯುವುದು ಪ್ರತಿಯೊಬ್ಬ ನಾಗರಿಕನ ಹಕ್ಕಾಗಿದೆ.

---

### 📌 ಸಕಾಲದ ಪ್ರಮುಖ ವೈಶಿಷ್ಟ್ಯಗಳು:
* **GSC ಸಂಖ್ಯೆ (Guarantee of Services Citizen Number):** ನೀವು ಯಾವುದೇ ಸರ್ಕಾರಿ ಕಚೇರಿ, ನಾಡಕಚೇರಿ ಅಥವಾ ಸೇವಾ ಸಿಂಧು ಕೇಂದ್ರದಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿದಾಗ 15 ಅಂಕಿಗಳ ಅನನ್ಯ **GSC ಸಂಖ್ಯೆ** ನೀಡಲಾಗುತ್ತದೆ.
* **ಕಾಲಮಿತಿ ಮೀರಿದರೆ ಪರಿಹಾರ:** ನಿಗದಿತ ದಿನಾಂಕದೊಳಗೆ ಸೇವೆ ಸಿಗದಿದ್ದರೆ, ಸಂಬಂಧಪಟ್ಟ ತಪ್ಪಿತಸ್ಥ ಅಧಿಕಾರಿಗೆ ದಿನಕ್ಕೆ **₹20 ರಂತೆ ಗರಿಷ್ಠ ₹500 ವರೆಗೆ ದಂಡ** ವಿಧಿಸಲಾಗುತ್ತದೆ ಹಾಗೂ ಆ ಮೊತ್ತವನ್ನು ಅರ್ಜಿದಾರರಿಗೆ ಪರಿಹಾರವಾಗಿ ನೀಡಲಾಗುತ್ತದೆ.

---

### 🔍 ಸಕಾಲ ಅರ್ಜಿ ಸ್ಥಿತಿ (Status) ಟ್ರ್ಯಾಕ್ ಮಾಡುವ ವಿಧಾನ:
1. [sakala.kar.nic.in](https://sakala.kar.nic.in) ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ.
2. ಮುಖಪುಟದಲ್ಲಿ ನಿಮ್ಮ **GSC Number** ನಮೂದಿಸಿ 'Track' ಕ್ಲಿಕ್ ಮಾಡಿ.
3. ಸೇವೆ ವಿಳಂಬವಾದರೆ ಪೋರ್ಟಲ್‌ನಲ್ಲಿಯೇ **1st Appeal (ಮೊದಲ ಮೇಲ್ಮನವಿ)** ಅಥವಾ **2nd Appeal** ಸಲ್ಲಿಸಬಹುದು.

🔗 **ಸಕಾಲ ಸಹಾಯವಾಣಿ:** 080-44554455 (ಬೆಳಗ್ಗೆ 8:00 ರಿಂದ ರಾತ್ರಿ 8:00 ರವರೆಗೆ)""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://sakala.kar.nic.in",
        "keywords": "sakala, gsc number, guarantee of services, ಸಕಾಲ, ಸೇವಾ ಖಾತರಿ, ಅರ್ಜಿ ಟ್ರ್ಯಾಕಿಂಗ್",
        "action_label": "⏱️ ಸಕಾಲ ಪೋರ್ಟಲ್",
        "action_url": "https://sakala.kar.nic.in"
    },
    {
        "id": "faq_pass_122",
        "question": "KSRTC ಮತ್ತು BMTC ವಿದ್ಯಾರ್ಥಿ ಬಸ್ ಪಾಸ್‌ಗೆ (Student Bus Pass) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "student bus pass online apply bmtc ksrtc seva sindhu ವಿದ್ಯಾರ್ಥಿ ಬಸ್ ಪಾಸ್",
        "answer": """### 🚌 ವಿದ್ಯಾರ್ಥಿ ರಿಯಾಯಿತಿ ದರದ ಬಸ್ ಪಾಸ್ (Student Bus Pass) ಪ್ರಕ್ರಿಯೆ

ಶಾಲಾ-ಕಾಲೇಜು ಮತ್ತು ವಿಶ್ವವಿದ್ಯಾಲಯಗಳ ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಕೆಎಸ್‌ಆರ್‌ಟಿಸಿ ಮತ್ತು ಬಿಎಂಟಿಸಿ ವತಿಯಿಂದ ಸೇವಾ ಸಿಂಧು ಪೋರ್ಟಲ್ ಮೂಲಕ ಡಿಜಿಟಲ್ ಸ್ಮಾರ್ಟ್ ಬಸ್ ಪಾಸ್ ವಿತರಿಸಲಾಗುತ್ತದೆ.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
* ವಿದ್ಯಾರ್ಥಿಯ ಆಧಾರ್ ಕಾರ್ಡ್.
* ಶಾಲಾ/ಕಾಲೇಜಿನ ಪ್ರವೇಶ ರಶೀದಿ (Fee Receipt) ಮತ್ತು ಕಾಲೇಜು ಗುರುತಿನ ಚೀಟಿ (ID Card).
* ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರದ RD ನಂಬರ್ (SC/ST ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಉಚಿತ ಪಾಸ್ ಸೌಲಭ್ಯಕ್ಕಾಗಿ).
* ಭಾವಚಿತ್ರ (ಪಾಸ್‌ಪೋರ್ಟ್ ಅಳತೆ).

---

### 🚀 ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಹಂತಗಳು:
1. [sevasindhu.karnataka.gov.in](https://sevasindhu.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ **'Student Bus Pass'** ಲಿಂಕ್ ಆಯ್ಕೆಮಾಡಿ.
2. ಶಿಕ್ಷಣ ಸಂಸ್ಥೆಯ ವಿವರ, ವ್ಯಾಸಂಗ ಮಾಡುವ ಕೋರ್ಸ್ ಹಾಗೂ ಪ್ರಯಾಣದ ಪ್ರಾರಂಭ-ಅಂತಿಮ ನಿಲ್ದಾಣಗಳನ್ನು (Route) ಆಯ್ಕೆಮಾಡಿ.
3. ಸಂಬಂಧಪಟ್ಟ ಶಾಲಾ/ಕಾಲೇಜು ಪ್ರಾಂಶುಪಾಲರು ತಮ್ಮ ಲಾಗಿನ್‌ನಲ್ಲಿ ಅರ್ಜಿಯನ್ನು ಆನ್‌ಲೈನ್ ಅನುಮೋದನೆ (Approve) ಮಾಡುತ್ತಾರೆ.
4. ಅನುಮೋದನೆಗೊಂಡ SMS ಬಂದ ನಂತರ, ಹತ್ತಿರದ KSRTC ಬಸ್ ನಿಲ್ದಾಣ ಅಥವಾ BMTC ಪಾಸಿಂಗ್ ಕೌಂಟರ್‌ಗೆ ತೆರಳಿ ಸ್ಮಾರ್ಟ್ ಕಾರ್ಡ್ ಪಡೆದುಕೊಳ್ಳಿ.""",
        "category": "TRANSIT",
        "language": "kn",
        "source_url": "https://sevasindhu.karnataka.gov.in",
        "keywords": "student bus pass, bmtc smart card, ksrtc student pass, ವಿದ್ಯಾರ್ಥಿ ಬಸ್ ಪಾಸ್, ಸೇವಾ ಸಿಂಧು",
        "action_label": "🚌 ಬಸ್ ಪಾಸ್ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ",
        "action_url": "https://sevasindhu.karnataka.gov.in"
    },
    {
        "id": "faq_dl_123",
        "question": "ಪರಿವಾಹನ್ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಲರ್ನರ್ ಲೈಸೆನ್ಸ್ (LLR) ಮತ್ತು ಡ್ರೈವಿಂಗ್ ಲೈಸೆನ್ಸ್ (DL) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "parivahan sarathi karnataka apply llr driving license dl online ಲರ್ನರ್ ಲೈಸೆನ್ಸ್ ಚಾಲನಾ ಪರವಾನಗಿ",
        "answer": """### 🚗 ಸಾರಥಿ ಪರಿವಾಹನ್ (Parivahan Sarathi) — ಚಾಲನಾ ಪರವಾನಗಿ ಪ್ರಕ್ರಿಯೆ

ಕರ್ನಾಟಕದಲ್ಲಿ ಕಾಗದರಹಿತ (Paperless Faceless) ವ್ಯವಸ್ಥೆಯ ಮೂಲಕ ಮನೆಯಲ್ಲೇ ಕುಳಿತು LLR ಪರೀಕ್ಷೆ ಬರೆಯಬಹುದು.

---

### 📝 1. ಲರ್ನರ್ಸ್ ಲೈಸೆನ್ಸ್ (LLR Online):
1. [parivahan.gov.in](https://parivahan.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ **'Karnataka'** ರಾಜ್ಯ ಆಯ್ಕೆಮಾಡಿ.
2. **'Apply for Learner License (LL)'** ಕ್ಲಿಕ್ ಮಾಡಿ ಆಧಾರ್ ದೃಢೀಕರಣ (Aadhaar Authentication) ಆಯ್ಕೆಮಾಡಿ.
3. ರಸ್ತೆ ಸುರಕ್ಷತಾ ವೀಡಿಯೊ (Road Safety Tutorial) ವೀಕ್ಷಿಸಿದ ನಂತರ ಆನ್‌ಲೈನ್‌ನಲ್ಲೇ 20 ಪ್ರಶ್ನೆಗಳ MCQ ಪರೀಕ್ಷೆ ಬರೆಯಿರಿ.
4. ಉತ್ತೀರ್ಣರಾದ ತಕ್ಷಣ ಡಿಜಿಟಲ್ ಸಹಿಯುಳ್ಳ LLR PDF ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.

---

### 🏍️ 2. ಕಾಯಂ ಡ್ರೈವಿಂಗ್ ಲೈಸೆನ್ಸ್ (Permanent DL):
* LLR ಪಡೆದ 30 ದಿನಗಳ ನಂತರ ಮತ್ತು 6 ತಿಂಗಳ ಒಳಗಾಗಿ **'Apply for Driving License'** ಆಯ್ಕೆಮಾಡಿ RTO ಟ್ರ್ಯಾಕ್ ಟೆಸ್ಟ್‌ಗೆ ಸ್ಲಾಟ್ ಬುಕ್ ಮಾಡಿ.
* RTO ಟ್ರ್ಯಾಕ್‌ನಲ್ಲಿ ವಾಹನ ಚಾಲನಾ ಪರೀಕ್ಷೆ ಉತ್ತೀರ್ಣರಾದ ನಂತರ ಸ್ಮಾರ್ಟ್ ಕಾರ್ಡ್ DL ನಿಮ್ಮ ಮನೆ ವಿಳಾಸಕ್ಕೆ ಸ್ಪೀಡ್ ಪೋಸ್ಟ್ ಮೂಲಕ ಬರುತ್ತದೆ.""",
        "category": "TRANSPORT",
        "language": "kn",
        "source_url": "https://parivahan.gov.in",
        "keywords": "parivahan karnataka, llr online exam, driving licence slot, ಲರ್ನರ್ ಲೈಸೆನ್ಸ್, ಡಿಎಲ್ ಬುಕಿಂಗ್",
        "action_label": "🚗 ಪರಿವಾಹನ್ ಪೋರ್ಟಲ್",
        "action_url": "https://parivahan.gov.in"
    },
    {
        "id": "faq_rera_124",
        "question": "K-RERA (ಕರ್ನಾಟಕ ರೇರಾ) ದಲ್ಲಿ ಫ್ಲಾಟ್/ಬಡಾವಣೆ ನೋಂದಣಿ ಪರಿಶೀಲಿಸುವುದು ಮತ್ತು ಬಿಲ್ಡರ್ ವಿರುದ್ಧ ದೂರು ನೀಡುವುದು ಹೇಗೆ?",
        "normalized_question": "k rera karnataka real estate project search builder complaint ಕರ್ನಾಟಕ ರೇರಾ ದೂರು",
        "answer": """### 🏢 ಕೆ-ರೇರಾ (K-RERA - Karnataka Real Estate Regulatory Authority)

ಬೆಂಗಳೂರು ಹಾಗೂ ಕರ್ನಾಟಕದಾದ್ಯಂತ ಅಪಾರ್ಟ್‌ಮೆಂಟ್, ವಿಲ್ಲಾ ಅಥವಾ ನಿವೇಶನ ಖರೀದಿಸುವ ಮುನ್ನ ಆ ಪ್ರಾಜೆಕ್ಟ್ RERA ಅನುಮೋದನೆ ಹೊಂದಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸುವುದು ಕಾನೂನುಬದ್ಧ ಸುರಕ್ಷತೆಗೆ ಕಡ್ಡಾಯ.

---

### 🔍 1. RERA ನೋಂದಾಯಿತ ಪ್ರಾಜೆಕ್ಟ್ ಪರಿಶೀಲನೆ:
* [rera.karnataka.gov.in](https://rera.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ **'Project Status'** ಆಯ್ಕೆಮಾಡಿ.
* ಬಿಲ್ಡರ್ ಹೆಸರು ಅಥವಾ RERA ನೋಂದಣಿ ಸಂಖ್ಯೆ (ಉದಾ: PRM/KA/RERA/...) ಹಾಕಿ.
* ಇಲ್ಲಿ ಅನುಮೋದಿತ ನಕ್ಷೆಗಳು, ಬ್ಯಾಂಕ್ ಖಾತೆ ವಿವರಗಳು ಹಾಗೂ ಕಾಮಗಾರಿ ಮುಕ್ತಾಯ ದಿನಾಂಕ (Completion Date) ತಿಳಿಯಬಹುದು.

---

### ⚖️ 2. ಬಿಲ್ಡರ್ ವಿರುದ್ಧ ಆನ್‌ಲೈನ್ ದೂರು ಸಲ್ಲಿಕೆ (Form N / Form M):
* ಫ್ಲಾಟ್ ಹಸ್ತಾಂತರ ವಿಳಂಬವಾದರೆ, ಕಳಪೆ ಗುಣಮಟ್ಟದ ನಿರ್ಮಾಣವಿದ್ದರೆ ಅಥವಾ ಸೌಲಭ್ಯಗಳ ಕೊರತೆಯಿದ್ದರೆ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ₹1,000 ಶುಲ್ಕ ಪಾವತಿಸಿ ಆನ್‌ಲೈನ್ ದೂರು ಸಲ್ಲಿಸಬಹುದು. ರೇರಾ ಪ್ರಾಧಿಕಾರವು ತ್ವರಿತ ವಿಚಾರಣೆ ನಡೆಸಿ ಬಡ್ಡಿ ಸಮೇತ ಪರಿಹಾರ ಕೊಡಿಸುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://rera.karnataka.gov.in",
        "keywords": "k rera, rera registered project, file rera complaint, ರೇರಾ ನೋಂದಣಿ, ಬಿಲ್ಡರ್ ದೂರು",
        "action_label": "🏢 K-RERA ಪೋರ್ಟಲ್",
        "action_url": "https://rera.karnataka.gov.in"
    },
    {
        "id": "faq_ggram_125",
        "question": "ಗ್ರಾಮ ಒನ್ (Grama One) ಮತ್ತು ಕರ್ನಾಟಕ ಒನ್ ಕೇಂದ್ರಗಳಲ್ಲಿ ಯಾವೆಲ್ಲಾ ಸೇವೆಗಳು ಸಿಗುತ್ತವೆ?",
        "normalized_question": "grama one karnataka one services list center locator ಗ್ರಾಮ ಒನ್ ಕೇಂದ್ರ ಸೇವೆಗಳು",
        "answer": """### 🏛️ ಗ್ರಾಮ ಒನ್ (Grama One) & ಕರ್ನಾಟಕ ಒನ್ ಸಿಟಿಜನ್ ಸರ್ವಿಸ್ ಸೆಂಟರ್ಸ್

ಗ್ರಾಮೀಣ ಮತ್ತು ನಗರ ಪ್ರದೇಶದ ನಾಗರಿಕರು ಸರ್ಕಾರಿ ಕಚೇರಿಗಳಿಗೆ ಅಲೆದಾಡುವುದನ್ನು ತಪ್ಪಿಸಲು ಒಂದೇ ಸೂರಿನಡಿ 800 ಕ್ಕೂ ಹೆಚ್ಚು ಸರ್ಕಾರಿ-ಖಾಸಗಿ ಸೇವೆಗಳನ್ನು ಒದಗಿಸಲಾಗುತ್ತದೆ.

---

### 📋 ಲಭ್ಯವಿರುವ ಪ್ರಮುಖ ಸೇವೆಗಳು:
1. **ಕಂದಾಯ ಇಲಾಖೆ:** ಜಾತಿ, ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ, ವಾಸಸ್ಥಳ ದೃಢೀಕರಣ, ಭೂಮಿ ಪಹಣಿ (RTC), ಮ್ಯುಟೇಶನ್ ಪ್ರತಿ.
2. **ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳು:** ಗೃಹಲಕ್ಷ್ಮಿ, ಗೃಹಜ್ಯೋತಿ, ಯುವನಿಧಿ ನೋಂದಣಿ ಮತ್ತು e-KYC.
3. **ಆಹಾರ ಇಲಾಖೆ:** ಹೊಸ ರೇಷನ್ ಕಾರ್ಡ್ ಅರ್ಜಿ, ಸದಸ್ಯರ ಹೆಸರು ಸೇರ್ಪಡೆ/ತೆಗೆದುಹಾಕುವಿಕೆ, ವಿಳಾಸ ತಿದ್ದುಪಡಿ.
4. **ಯುಟಿಲಿಟಿ ಬಿಲ್‌ಗಳು:** ಬೆಸ್ಕಾಂ/ಎಸ್ಕಾಂ ವಿದ್ಯುತ್ ಬಿಲ್, ನೀರಿನ ಬಿಲ್, ಮೊಬೈಲ್ ರೀಚಾರ್ಜ್, ಆಸ್ತಿ ತೆರಿಗೆ.
5. **ಸಾರಿಗೆ & ಪೊಲೀಸ್:** ಸೇವಾ ಸಿಂಧು ಬಸ್ ಪಾಸ್, KSP ಪೊಲೀಸ್ ವೆರಿಫಿಕೇಶನ್ ಸರ್ಟಿಫಿಕೇಟ್ (PCC).

🔗 **ನಿಮ್ಮ ಸಮೀಪದ ಕೇಂದ್ರ ತಿಳಿಯಲು:** [karnatakaone.gov.in](https://karnatakaone.gov.in) | [gramaone.karnataka.gov.in](https://gramaone.karnataka.gov.in)""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://gramaone.karnataka.gov.in",
        "keywords": "grama one, karnataka one, citizen services, ಗ್ರಾಮ ಒನ್, ಸೇವಾ ಸಿಂಧು ಕೇಂದ್ರ",
        "action_label": "🏛️ ಗ್ರಾಮ ಒನ್ ವಿವರ",
        "action_url": "https://gramaone.karnataka.gov.in"
    },
    {
        "id": "faq_bhuaadhaar_126",
        "question": "ಭೂ-ಆಧಾರ್ (Bhu-Aadhaar / ULPIN) ಎಂದರೇನು? ಜಮೀನಿಗೆ 14 ಅಂಕಿಗಳ ಅನನ್ಯ ಕೋಡ್ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "bhu aadhaar ulpin unique land parcel identification karnataka ಭೂ ಆಧಾರ್ ಸಂಖ್ಯೆ",
        "answer": """### 🌐 ಭೂ-ಆಧಾರ್ (Bhu-Aadhaar / ULPIN - Unique Land Parcel Identification Number)

ಭೂ-ಆಧಾರ್ ಎಂಬುದು ಕಂದಾಯ ಇಲಾಖೆಯು ಪ್ರತಿ ಕೃಷಿ ಮತ್ತು ಕೃಷಿಯೇತರ ಜಮೀನಿನ ಭೂ-ಖಂಡಕ್ಕೆ ನೀಡುವ **14 ಅಂಕಿಗಳ ಅನನ್ಯ ಜಿಯೋ-ರೆಫರೆನ್ಸ್ ಆಲ್ಫಾ-ನ್ಯೂಮರಿಕ್ ಗುರುತಿನ ಸಂಖ್ಯೆಯಾಗಿದೆ**.

---

### 🎯 ಭೂ-ಆಧಾರ್‌ನ ಮುಖ್ಯ ಅನುಕೂಲಗಳು:
* **ನಕಲಿ ನೋಂದಣಿಗೆ ಬ್ರೇಕ್:** ಜಮೀನಿನ ಅಕ್ಷಾಂಶ-ರೇಖಾಂಶ (Longitude & Latitude) ಆಧರಿಸಿ ನೀಡುವುದರಿಂದ ಒಂದೇ ಜಮೀನನ್ನು ಇಬ್ಬರಿಗೆ ಮಾರಾಟ ಮಾಡಲು ಸಾಧ್ಯವಿಲ್ಲ.
* **ಸರ್ವೆ ನಕ್ಷೆ ಲಿಂಕ್:** ಜಮೀನಿನ ನೈಜ ಗಡಿಗಳು ಮತ್ತು ಮೋಜಿನಿ ನಕ್ಷೆಯು ನೇರವಾಗಿ ಡಿಜಿಟಲ್ ರೂಪದಲ್ಲಿ ಲಿಂಕ್ ಆಗಿರುತ್ತದೆ.
* **ಬ್ಯಾಂಕ್ ಸಾಲ & ಪರಿಹಾರ:** ಬೆಳೆ ಸಾಲ, ಬರ ಪರಿಹಾರ ಮತ್ತು ಭೂಸ್ವಾಧೀನ ಪರಿಹಾರಗಳು ಯಾವುದೇ ಲೋಪವಿಲ್ಲದೆ ನೇರವಾಗಿ ನೈಜ ಮಾಲೀಕರ ಖಾತೆಗೆ ತಲುಪಲು ಇದು ನೆರವಾಗುತ್ತದೆ.

💡 ನಿಮ್ಮ ಭೂಮಿಯ ಪಹಣಿ (RTC) ಯಲ್ಲಿ ಇತ್ತೀಚಿನ ನವೀಕರಣದೊಂದಿಗೆ ULPIN ಮುದ್ರಿತವಾಗಿರುತ್ತದೆ.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://bhoomi.karnataka.gov.in",
        "keywords": "bhu aadhaar, ulpin karnataka, geo referenced land parcel, ಭೂ ಆಧಾರ್, ಭೂಮಿ ಕೋಡ್",
        "action_label": "🌾 ಭೂಮಿ ಪೋರ್ಟಲ್",
        "action_url": "https://bhoomi.karnataka.gov.in"
    },
    {
        "id": "faq_milk_127",
        "question": "ಕ್ಷೀರಧಾರೆ / ಹಾಲಿನ ಪ್ರೋತ್ಸಾಹಧನ (₹5 Milk Subsidy) ರೈತರ ಖಾತೆಗೆ ಜಮೆಯಾಗುವುದು ಹೇಗೆ?",
        "normalized_question": "milk producer subsidy 5 rs kmf dbt nandini ksheera ksheeradhare ಹಾಲಿನ ಪ್ರೋತ್ಸಾಹಧನ",
        "answer": """### 🥛 ಹಾಲು ಉತ್ಪಾದಕರಿಗೆ ₹5 ಪ್ರೋತ್ಸಾಹಧನ ಯೋಜನೆ (Ksheeradhare Scheme)

ಕರ್ನಾಟಕ ಸಹಕಾರಿ ಹಾಲು ಮಹಾಮಂಡಳಿ (KMF - ನಂದಿನಿ) ವ್ಯಾಪ್ತಿಯ ಹಾಲು ಉತ್ಪಾದಕರ ಸಹಕಾರ ಸಂಘಗಳಿಗೆ (MPCS) ಹಾಲು ಪೂರೈಸುವ ರೈತರಿಗೆ ಸರ್ಕಾರ ಪ್ರತಿ ಲೀಟರ್ ಹಾಲಿಗೆ **₹5 ಪ್ರೋತ್ಸಾಹಧನ** ನೀಡುತ್ತದೆ.

---

### 📌 ಹಣ ಜಮೆಯಾಗಲು ಅಗತ್ಯವಿರುವ ಷರತ್ತುಗಳು:
1. ಹಾಲು ಉತ್ಪಾದಕ ರೈತರು ಸ್ಥಳೀಯ ಪ್ರಾಥಮಿಕ ಹಾಲು ಉತ್ಪಾದಕರ ಸಹಕಾರ ಸಂಘದಲ್ಲಿ (ಡೈರಿ) ನೋಂದಾಯಿತ ಸದಸ್ಯರಾಗಿರಬೇಕು.
2. ರೈತರ **FRUITS FID ಸಂಖ್ಯೆ** ಮತ್ತು ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಆಧಾರ್ ಲಿಂಕ್ (NPCI Seeding) ಕಡ್ಡಾಯ.
3. ಪ್ರತಿ ತಿಂಗಳು ಡೈರಿಯಿಂದ ಸ್ವೀಕರಿಸಲಾದ ಹಾಲಿನ ಪ್ರಮಾಣ (ಕ್ವಾಂಟಿಟಿ), ಜಿಡ್ಡಿನಾಂಶ (Fat) ಮತ್ತು ಎಸ್‌ಎನ್‌ಎಫ್ (SNF) ಆಧಾರದ ಮೇಲೆ ಪ್ರೋತ್ಸಾಹಧನದ ಮೊತ್ತವನ್ನು ನೇರವಾಗಿ ರೈತರ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ DBT ಮಾಡಲಾಗುತ್ತದೆ.

🔗 **ಪರಿಶೀಲನಾ ಪೋರ್ಟಲ್:** [ahvs.karnataka.gov.in](https://ahvs.karnataka.gov.in)""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://ahvs.karnataka.gov.in",
        "keywords": "milk subsidy 5 rupees, kmf nandini dbt, ksheeradhare, ಹಾಲಿನ ಪ್ರೋತ್ಸಾಹಧನ, ಕೆಎಂಎಫ್",
        "action_label": "🥛 ಪಶುಸಂಗೋಪನಾ ಇಲಾಖೆ",
        "action_url": "https://ahvs.karnataka.gov.in"
    },
    {
        "id": "faq_kass_128",
        "question": "ಕರ್ನಾಟಕ ಆರೋಗ್ಯ ಸಂಜೀವಿನಿ ಯೋಜನೆ (KASS) ಎಂದರೇನು? ಸರ್ಕಾರಿ ನೌಕರರಿಗೆ ಇದರ ಸೌಲಭ್ಯಗಳೇನು?",
        "normalized_question": "kass karnataka arogya sanjeevini scheme government employees cashless ಆರೋಗ್ಯ ಸಂಜೀವಿನಿ",
        "answer": """### 🏥 ಕರ್ನಾಟಕ ಆರೋಗ್ಯ ಸಂಜೀವಿನಿ ಯೋಜನೆ (KASS)

ಕರ್ನಾಟಕ ರಾಜ್ಯ ಸರ್ಕಾರಿ ನೌಕರರು ಹಾಗೂ ಅವರ ಅವಲಂಬಿತ ಕುಟುಂಬ ಸದಸ್ಯರಿಗೆ ಸಂಪೂರ್ಣ **ನಗದುರಹಿತ (Cashless Medical Treatment)** ವೈದ್ಯಕೀಯ ಚಿಕಿತ್ಸೆ ಒದಗಿಸುವ ಸಮಗ್ರ ಯೋಜನೆ.

---

### 🌟 ಯೋಜನೆಯ ಪ್ರಮುಖ ಲಾಭಗಳು:
* **ನಗದುರಹಿತ ಸೌಲಭ್ಯ:** ಎಂಪ್ಯಾನೆಲ್ ಆಗಿರುವ ಯಾವುದೇ ನೆಟ್‌ವರ್ಕ್ ಆಸ್ಪತ್ರೆಗಳಲ್ಲಿ ನೌಕರರು ಜೇಬಿನಿಂದ ಹಣ ಪಾವತಿಸದೆ ನೇರವಾಗಿ ಗ್ರೀನ್ ಕಾರ್ಡ್ / KASS ಐಡಿ ತೋರಿಸಿ ಚಿಕಿತ್ಸೆ ಪಡೆಯಬಹುದು.
* **ಒಳಗೊಂಡಿರುವ ಚಿಕಿತ್ಸೆಗಳು:** ಪ್ರಮುಖ ಶಸ್ತ್ರಚಿಕಿತ್ಸೆಗಳು, ಹೃದ್ರೋಗ, ಕ್ಯಾನ್ಸರ್, ಮೂತ್ರಪಿಂಡ ಕಸಿ, ತುರ್ತು ಅಪಘಾತ ಚಿಕಿತ್ಸೆ ಸೇರಿದಂತೆ ವ್ಯಾಪಕ ವೈದ್ಯಕೀಯ ಪ್ಯಾಕೇಜ್‌ಗಳು.
* **ಅರ್ಹರು:** ರಾಜ್ಯ ಸರ್ಕಾರದ ಕಾಯಂ ನೌಕರರು, ಪಿಂಚಣಿದಾರರು ಮತ್ತು ಅವರ ಅವಲಂಬಿತ ಪತ್ನಿ/ಪತಿ, ಮಕ್ಕಳು ಮತ್ತು ಪೋಷಕರು.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [kass.karnataka.gov.in](https://kass.karnataka.gov.in)""",
        "category": "HEALTH",
        "language": "kn",
        "source_url": "https://kass.karnataka.gov.in",
        "keywords": "kass scheme, arogya sanjeevini, govt employees cashless health, ಆರೋಗ್ಯ ಸಂಜೀವಿನಿ",
        "action_label": "🏥 KASS ಪೋರ್ಟಲ್",
        "action_url": "https://kass.karnataka.gov.in"
    },
    {
        "id": "faq_solar_129",
        "question": "ಬೆಸ್ಕಾಂ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ರೂಫ್‌ಟಾಪ್ ಸೋಲಾರ್ (PM Surya Ghar / Net Metering) ಸಬ್ಸಿಡಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "bescom rooftop solar subsidy pm surya ghar net metering ಬೆಸ್ಕಾಂ ಸೋಲಾರ್ ಸಬ್ಸಿಡಿ",
        "answer": """### ☀️ ರೂಫ್‌ಟಾಪ್ ಸೋಲಾರ್ ಮತ್ತು PM ಸೂರ್ಯ ಘರ್ ಮುಫ್ತ್ ಬಿಜ್ಲಿ ಯೋಜನೆ

ಮನೆಯ ಛಾವಣಿಯ ಮೇಲೆ ಸೌರ ವಿದ್ಯುತ್ ಫಲಕ (Solar Rooftop) ಅಳವಡಿಸಿ ಉಚಿತ ವಿದ್ಯುತ್ ಪಡೆಯುವ ಜೊತೆಗೆ ಹೆಚ್ಚುವರಿ ವಿದ್ಯುತ್ತನ್ನು ಬೆಸ್ಕಾಂಗೆ ಮಾರಿ ಆದಾಯ ಗಳಿಸಬಹುದು.

---

### 💰 ಸಬ್ಸಿಡಿ ವಿವರ (PM Surya Ghar):
* **1 kW ಸಾಮರ್ಥ್ಯ:** ₹30,000 ಸಬ್ಸಿಡಿ.
* **2 kW ಸಾಮರ್ಥ್ಯ:** ₹60,000 ಸಬ್ಸಿಡಿ.
* **3 kW ಮತ್ತು ಅದಕ್ಕಿಂತ ಹೆಚ್ಚು:** ಗರಿಷ್ಠ **₹78,000 ಕೇಂದ್ರ ಸರ್ಕಾರದ ನೇರ ಸಬ್ಸಿಡಿ**.

---

### 🔌 ನೆಟ್ ಮೀಟರಿಂಗ್ (Net Metering) ಪ್ರಕ್ರಿಯೆ:
1. [pmsuryaghar.gov.in](https://pmsuryaghar.gov.in) ನಲ್ಲಿ ನೋಂದಾಯಿಸಿ ನಿಮ್ಮ ಎಸ್ಕಾಂ Consumer Account ID ನೀಡಿ.
2. ಬೆಸ್ಕಾಂ ಅನುಮೋದಿತ ವೆಂಡರ್ ಮೂಲಕ ಸೋಲಾರ್ ಪ್ಯಾನಲ್ ಅಳವಡಿಸಿ.
3. ಬೆಸ್ಕಾಂ ಅಧಿಕಾರಿಗಳು ಬೈ-ಡೈರೆಕ್ಷನಲ್ ನೆಟ್ ಮೀಟರ್ ಅಳವಡಿಸಿದ ನಂತರ ಸಬ್ಸಿಡಿ ಹಣ ನೇರವಾಗಿ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bescom.karnataka.gov.in",
        "keywords": "bescom solar, pm surya ghar subsidy, net metering rooftop, ಬೆಸ್ಕಾಂ ಸೋಲಾರ್, ಸೂರ್ಯ ಘರ್",
        "action_label": "☀️ ಸೂರ್ಯ ಘರ್ ಪೋರ್ಟಲ್",
        "action_url": "https://pmsuryaghar.gov.in"
    },
    {
        "id": "faq_cmrf_130",
        "question": "ಮುಖ್ಯಮಂತ್ರಿಗಳ ಪರಿಹಾರ ನಿಧಿ (CMRF) ಯಿಂದ ವೈದ್ಯಕೀಯ ಚಿಕಿತ್ಸಾ ಧನಸಹಾಯ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "cmrf karnataka apply cm relief fund medical financial assistance ಮುಖ್ಯಮಂತ್ರಿಗಳ ಪರಿಹಾರ ನಿಧಿ",
        "answer": """### 🏛️ ಮುಖ್ಯಮಂತ್ರಿಗಳ ಪರಿಹಾರ ನಿಧಿ (Chief Minister's Relief Fund - CMRF)

ಮಾರಣಾಂತಿಕ ಕಾಯಿಲೆಗಳಿಂದ ಬಳಲುತ್ತಿರುವ ಬಡ ರೋಗಿಗಳಿಗೆ ಚಿಕಿತ್ಸಾ ವೆಚ್ಚ ಭರಿಸಲು ಮುಖ್ಯಮಂತ್ರಿಗಳ ಪರಿಹಾರ ನಿಧಿಯಿಂದ ಆರ್ಥಿಕ ನೆರವು ನೀಡಲಾಗುತ್ತದೆ.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
* ಆಸ್ಪತ್ರೆಯ ಮೂಲ ಅಂದಾಜು ವೆಚ್ಚದ ಪತ್ರ (Original Estimated Medical Bill with Seal & Signature).
* ರೋಗಿಯ ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು BPL ರೇಷನ್ ಕಾರ್ಡ್ ಪ್ರತಿ.
* ಡಿಸ್ಚಾರ್ಜ್ ಸಮ್ಮರಿ (ಚಿಕಿತ್ಸೆ ಪಡೆದಿದ್ದರೆ) ಹಾಗೂ ಆಸ್ಪತ್ರೆಯ ಬ್ಯಾಂಕ್ ಖಾತೆ ವಿವರ (Bank IFSC / Account Number).
* ಸ್ಥಳೀಯ ಶಾಸಕರ (MLA) ಶಿಫಾರಸು ಪತ್ರ.

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಕೆ:
1. [cmrf.karnataka.gov.in](https://cmrf.karnataka.gov.in) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ದಾಖಲೆಗಳನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
2. ಪರಿಶೀಲನೆಯ ನಂತರ ಪರಿಹಾರ ಮೊತ್ತವು ನೇರವಾಗಿ ರೋಗಿ ಚಿಕಿತ್ಸೆ ಪಡೆಯುತ್ತಿರುವ ಆಸ್ಪತ್ರೆಯ ಖಾತೆಗೆ ಅಥವಾ ರೋಗಿಯ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ವರ್ಗಾವಣೆಯಾಗುತ್ತದೆ.""",
        "category": "HEALTH",
        "language": "kn",
        "source_url": "https://cmrf.karnataka.gov.in",
        "keywords": "cmrf karnataka, cm relief fund medical, ಮುಖ್ಯಮಂತ್ರಿ ಪರಿಹಾರ ನಿಧಿ, ಚಿಕಿತ್ಸಾ ಧನಸಹಾಯ",
        "action_label": "🏛️ CMRF ಪೋರ್ಟಲ್",
        "action_url": "https://cmrf.karnataka.gov.in"
    },
    {
        "id": "faq_kpsc_131",
        "question": "KPSC (ಕರ್ನಾಟಕ ಲೋಕಸೇವಾ ಆಯೋಗ) ಒನ್ ಟೈಮ್ ರಿಜಿಸ್ಟ್ರೇಷನ್ (OTR) ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "kpsc one time registration otr profile apply kpsc hall ticket ಕೆಪಿಎಸ್ಸಿ ಒಟಿಆರ್ ನೋಂದಣಿ",
        "answer": """### 📚 KPSC ಒನ್ ಟೈಮ್ ರಿಜಿಸ್ಟ್ರೇಷನ್ (One Time Registration - OTR)

ಕರ್ನಾಟಕ ಲೋಕಸೇವಾ ಆಯೋಗವು ನಡೆಸುವ KAS, FDA, SDA, ಗ್ರೂಪ್ ಸಿ ಮತ್ತು ಇಂಜಿನಿಯರಿಂಗ್ ಹುದ್ದೆಗಳಿಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಲು OTR ಪ್ರೊಫೈಲ್ ಕಡ್ಡಾಯ.

---

### 📝 OTR ನೋಂದಣಿ ಹಂತಗಳು:
1. **ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [kpsc.kar.nic.in](https://kpsc.kar.nic.in)
2. **'One Time Registration (OTR)'** ಲಿಂಕ್ ಕ್ಲಿಕ್ ಮಾಡಿ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಹಾಗೂ ಇಮೇಲ್ ಮೂಲಕ ಸೈನ್ ಅಪ್ ಆಗಿ.
3. ಆಧಾರ್ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ ಇ-ಕೆವೈಸಿ ಪೂರ್ಣಗೊಳಿಸಿ.
4. ಎಸ್‌ಎಸ್‌ಎಲ್‌ಸಿ, ಪಿಯುಸಿ, ಪದವಿ ಅಂಕಪಟ್ಟಿಗಳು, ಕನ್ನಡ ಮಾಧ್ಯಮ, ಗ್ರಾಮೀಣ ಮೀಸಲಾತಿ ಮತ್ತು ಜಾತಿ ಪ್ರಮಾಣಪತ್ರದ RD ಸಂಖ್ಯೆ ನಮೂದಿಸಿ.
5. ಭಾವಚಿತ್ರ ಹಾಗೂ ಸಹಿ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ಪ್ರೊಫೈಲ್ ಲಾಕ್ ಮಾಡಿ.

💡 ಒಮ್ಮೆ OTR ಸೃಷ್ಟಿಸಿದರೆ ಯಾವುದೇ ಹೊಸ ಅಧಿಸೂಚನೆ ಪ್ರಕಟವಾದಾಗ ಕೇವಲ ಒಂದೇ ಕ್ಲಿಕ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಶುಲ್ಕ ಕಟ್ಟಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು.""",
        "category": "EDUCATION",
        "language": "kn",
        "source_url": "https://kpsc.kar.nic.in",
        "keywords": "kpsc otr, kpsc login, kpsc kas application, ಕೆಪಿಎಸ್ಸಿ, ಒಟಿಆರ್ ನೋಂದಣಿ, ಸರ್ಕಾರಿ ಉದ್ಯೋಗ",
        "action_label": "📚 KPSC ಪೋರ್ಟಲ್",
        "action_url": "https://kpsc.kar.nic.in"
    },
    {
        "id": "faq_sindhutva_132",
        "question": "ಸಿಂಧುತ್ವ ಪ್ರಮಾಣಪತ್ರ (Caste Validity / Sindhutva Certificate) ಎಂದರೇನು? ಸರ್ಕಾರಿ ಕೆಲಸಕ್ಕೆ ಇದು ಏಕೆ ಕಡ್ಡಾಯ?",
        "normalized_question": "sindhutva caste validity certificate verification dcre karnataka ಸಿಂಧುತ್ವ ಪ್ರಮಾಣ ಪತ್ರ",
        "answer": """### 📑 ಜಾತಿ ಸಿಂಧುತ್ವ ಪ್ರಮಾಣಪತ್ರ (Caste Validity / Sindhutva)

ಸರ್ಕಾರಿ ಉದ್ಯೋಗಕ್ಕೆ ನೇಮಕಾತಿ ಹೊಂದಿದಾಗ ಅಥವಾ ವೃತ್ತಿಪರ ಕೋರ್ಸ್‌ಗಳ (ವೈದ್ಯಕೀಯ/ಇಂಜಿನಿಯರಿಂಗ್) ಮೀಸಲಾತಿ ಪ್ರವೇಶದ ಸಂದರ್ಭದಲ್ಲಿ ನೈಜ ಜಾತಿಯನ್ನು ದೃಢೀಕರಿಸಲು ಜಿಲ್ಲಾ ಜಾತಿ ಪರಿಶೀಲನಾ ಸಮಿತಿಯು ನೀಡುವ ಪ್ರಮಾಣಪತ್ರವೇ **ಸಿಂಧುತ್ವ**.

---

### 🏛️ ಪರಿಶೀಲನಾ ಪ್ರಾಧಿಕಾರ:
* ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ (DC) ಅಧ್ಯಕ್ಷತೆಯ **ಜಿಲ್ಲಾ ಸಿಂಧುತ್ವ ಸಮಿತಿ (District Caste Verification Committee)** ಈ ಪ್ರಮಾಣಪತ್ರವನ್ನು ಪರಿಶೀಲಿಸಿ ನೀಡುತ್ತದೆ.

---

### 📋 ಅಗತ್ಯವಿರುವ ಪುರಾವೆಗಳು:
1. ಅಭ್ಯರ್ಥಿ, ಪೋಷಕರು ಮತ್ತು ರಕ್ತಸಂಬಂಧಿಗಳ ಪ್ರಾಥಮಿಕ ಶಾಲಾ ದಾಖಲಾತಿ ಪ್ರತಿ (School Admission Register Excerpt - ನಮೂದಾಗಿರುವ ಜಾತಿಯೊಂದಿಗೆ).
2. ವಂಶವೃಕ್ಷ ಪ್ರಮಾಣಪತ್ರ (Genealogy Tree Certificate).
3. ತಹಶೀಲ್ದಾರ್ ನೀಡಿದ ಜಾತಿ ಪ್ರಮಾಣಪತ್ರ (Caste Certificate).
4. ಅಗತ್ಯಬಿದ್ದರೆ ನಾಗರಿಕ ಹಕ್ಕು ಜಾರಿ ನಿರ್ದೇಶನಾಲಯ (DCRE) ಸ್ಥಳೀಯ ವಿಚಾರಣೆ ನಡೆಸಿ ವರದಿ ನೀಡುತ್ತದೆ.""",
        "category": "CERTIFICATES",
        "language": "kn",
        "source_url": "https://sw.karnataka.gov.in",
        "keywords": "sindhutva certificate, caste validity, dcre verification, ಸಿಂಧುತ್ವ ಪ್ರಮಾಣಪತ್ರ, ಜಾತಿ ಸಿಂಧುತ್ವ",
        "action_label": "📑 ಸಮಾಜ ಕಲ್ಯಾಣ ಇಲಾಖೆ",
        "action_url": "https://sw.karnataka.gov.in"
    },
    {
        "id": "faq_arivu_133",
        "question": "ಅಲ್ಪಸಂಖ್ಯಾತರ 'ಅರಿವು' (Arivu) ಶೈಕ್ಷಣಿಕ ಸಾಲ ಯೋಜನೆಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "kmdc arivu education loan minorities cet neet loan ಅರಿವು ಶೈಕ್ಷಣಿಕ ಸಾಲ ಯೋಜನೆ",
        "answer": """### 🎓 ಕೆಎಂಡಿಸಿ 'ಅರಿವು' ಶೈಕ್ಷಣಿಕ ಸಾಲ ಯೋಜನೆ (KMDC Arivu Scheme)

ಕರ್ನಾಟಕ ಅಲ್ಪಸಂಖ್ಯಾತರ ಅಭಿವೃದ್ಧಿ ನಿಗಮದ (KMDC) ವತಿಯಿಂದ ಮುಸ್ಲಿಂ, ಕ್ರಿಶ್ಚಿಯನ್, ಜೈನ, ಬೌದ್ಧ, ಸಿಖ್ ಮತ್ತು ಪಾರ್ಸಿ ಸಮುದಾಯದ ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಉನ್ನತ ಶಿಕ್ಷಣಕ್ಕಾಗಿ ರಿಯಾಯಿತಿ ಬಡ್ಡಿದರದಲ್ಲಿ ಶೈಕ್ಷಣಿಕ ಸಾಲ ನೀಡಲಾಗುತ್ತದೆ.

---

### 💰 ಸಾಲದ ವಿವರ & ಮೊತ್ತ:
* **ವೃತ್ತಿಪರ ಕೋರ್ಸ್‌ಗಳು (MBBS, BDS, B.Tech/BE, B.Arch, MBA, MCA ಇತ್ಯಾದಿ):** ವಾರ್ಷಿಕ ಗರಿಷ್ಠ **₹50,000 ದಿಂದ ₹5 ಲಕ್ಷದವರೆಗೆ** ನೇರವಾಗಿ KEA / ಕಾಲೇಜು ಖಾತೆಗೆ ವರ್ಗಾವಣೆ.
* **ಬಡ್ಡಿದರ:** ಕೇವಲ **2% ವಾರ್ಷಿಕ ಸೇವಾ ಶುಲ್ಕ (Service Charge)**.

---

### 📌 ಅರ್ಹತೆ:
1. ಕರ್ನಾಟಕ ಪರೀಕ್ಷಾ ಪ್ರಾಧಿಕಾರದ (KEA / CET / NEET) ಮುಖಾಂತರ ಸೀಟು ಪಡೆದಿರಬೇಕು.
2. ಕುಟುಂಬದ ವಾರ್ಷಿಕ ಆದಾಯ ₹4.50 ಲಕ್ಷಕ್ಕಿಂತ ಒಳಗಿರಬೇಕು.

🔗 **ಅರ್ಜಿ ಸಲ್ಲಿಕೆ:** [kmdconline.karnataka.gov.in](https://kmdconline.karnataka.gov.in)""",
        "category": "EDUCATION",
        "language": "kn",
        "source_url": "https://kmdconline.karnataka.gov.in",
        "keywords": "arivu scheme, kmdc education loan, cet neet minority loan, ಅರಿವು ಸಾಲ ಯೋಜನೆ, ಅಲ್ಪಸಂಖ್ಯಾತರ ಕಲ್ಯಾಣ",
        "action_label": "🎓 KMDC ಪೋರ್ಟಲ್",
        "action_url": "https://kmdconline.karnataka.gov.in"
    },
    {
        "id": "faq_landpur_134",
        "question": "ಅಂಬೇಡ್ಕರ್ ನಿಗಮದ 'ಭೂ ಒಡೆತನ ಯೋಜನೆ' (Land Purchase Scheme) ಯಡಿ ಕೃಷಿ ಭೂಮಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "ambedkar corporation land purchase scheme sc st farmers ಭೂ ಒಡೆತನ ಯೋಜನೆ ದಲಿತ ಕೃಷಿ ಭೂಮಿ",
        "answer": """### 🌾 ಡಾ. ಬಿ.ಆರ್. ಅಂಬೇಡ್ಕರ್ ಅಭಿವೃದ್ಧಿ ನಿಗಮದ 'ಭೂ ಒಡೆತನ ಯೋಜನೆ'

ಭೂಹೀನ ಪರಿಶಿಷ್ಟ ಜಾತಿ (SC) ಮತ್ತು ಪರಿಶಿಷ್ಟ ಪಂಗಡದ (ST) ಕೃಷಿ ಕಾರ್ಮಿಕ ಕುಟುಂಬಗಳಿಗೆ ಸ್ವಂತ ಜಮೀನಿನ ಒಡೆತನ ಕಲ್ಪಿಸಲು ಸರ್ಕಾರವೇ ಕೃಷಿ ಜಮೀನು ಖರೀದಿಸಿ ಫಲಾನುಭವಿಗಳ ಹೆಸರಿಗೆ ನೋಂದಾಯಿಸಿಕೊಡುತ್ತದೆ.

---

### 📌 ಪ್ರಮುಖ ಸೌಲಭ್ಯಗಳು:
* ನಿಗಮದ ವತಿಯಿಂದ ಕನಿಷ್ಠ **2 ಎಕರೆ ಖುಷ್ಕಿ (Dry Land)** ಅಥವಾ **1 ಎಕರೆ ನೀರಾವರಿ (Wet Land)** ಜಮೀನನ್ನು ಖರೀದಿಸಿ ಮಹಿಳೆಯ ಹೆಸರಿಗೆ ಸಂಪೂರ್ಣ ಮಾಲೀಕತ್ವ ನೀಡಲಾಗುತ್ತದೆ.
* ಇದರಲ್ಲಿ **50% ಸಬ್ಸಿಡಿ (ಸಹಾಯಧನ)** ಮತ್ತು ಉಳಿದ 50% ಮೊತ್ತ ದೀರ್ಘಾವಧಿಯ ಸಾಲದ ರೂಪದಲ್ಲಿರುತ್ತದೆ.

---

### 📋 ಅರ್ಹತೆ:
1. ಅರ್ಜಿದಾರರು ಪರಿಶಿಷ್ಟ ಜಾತಿ/ಪಂಗಡಕ್ಕೆ ಸೇರಿದವರಾಗಿರಬೇಕು ಮತ್ತು ಕುಟುಂಬದಲ್ಲಿ ಯಾರಿಗೂ ಸ್ವಂತ ಕೃಷಿ ಭೂಮಿ ಇರಬಾರದು.
2. ಕೃಷಿ ಕೂಲಿ ಕಾರ್ಮಿಕರಾಗಿರಬೇಕು.
3. ವಾರ್ಷಿಕ ಕುಟುಂಬದ ಆದಾಯ ಗ್ರಾಮೀಣ ಪ್ರದೇಶದಲ್ಲಿ ₹1.50 ಲಕ್ಷ ಮೀರಬಾರದು.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [adcl.karnataka.gov.in](https://adcl.karnataka.gov.in)""",
        "category": "WELFARE",
        "language": "kn",
        "source_url": "https://adcl.karnataka.gov.in",
        "keywords": "land purchase scheme, ambedkar nigama, sc st land ownership, ಭೂ ಒಡೆತನ ಯೋಜನೆ, ಅಂಬೇಡ್ಕರ್ ನಿಗಮ",
        "action_label": "🌾 ಅಂಬೇಡ್ಕರ್ ನಿಗಮ ವಿವರ",
        "action_url": "https://adcl.karnataka.gov.in"
    },
    {
        "id": "faq_lokad_135",
        "question": "ಲೋಕ ಅದಾಲತ್ (National Lok Adalat) ನಲ್ಲಿ ಬಾಕಿ ಇರುವ ಕೋರ್ಟ್ ಕೇಸ್ ಮತ್ತು ಟ್ರಾಫಿಕ್ ಫೈನ್ ಇತ್ಯರ್ಥಪಡಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "lok adalat karnataka traffic fine discount compound case settle ಲೋಕ ಅದಾಲತ್ ಸಂಧಾನ",
        "answer": """### ⚖️ ರಾಷ್ಟ್ರೀಯ ಲೋಕ ಅದಾಲತ್ (Karnataka State Legal Services Authority - KSLSA)

ಕೋರ್ಟ್ ಶುಲ್ಕವಿಲ್ಲದೆ, ಯಾವುದೇ ವಕೀಲರ ಶುಲ್ಕದ ಹೊರೆಯಿಲ್ಲದೆ ಪರಸ್ಪರ ಮಾತುಕತೆ ಮತ್ತು ಸಂಧಾನದ ಮೂಲಕ ಸಿವಿಲ್, ಕೌಟುಂಬಿಕ, ಬ್ಯಾಂಕ್ ಸಾಲ ಹಾಗೂ ರಾಜಿ ಮಾಡಿಕೊಳ್ಳಬಹುದಾದ ಕ್ರಿಮಿನಲ್ ಪ್ರಕರಣಗಳನ್ನು ಇತ್ಯರ್ಥಪಡಿಸುವ ನ್ಯಾಯಾಲಯ ಪದ್ಧತಿ.

---

### 🌟 ಲೋಕ ಅದಾಲತ್‌ನ ಪ್ರಮುಖ ಲಾಭಗಳು:
* **ಅಂತಿಮ ತೀರ್ಪು (No Appeal):** ಲೋಕ ಅದಾಲತ್‌ನಲ್ಲಿ ಹೊರಡಿಸಲಾದ ಆದೇಶವು ಸಿವಿಲ್ ಕೋರ್ಟ್ ಡಿಗ್ರಿಗೆ ಸಮಾನವಾಗಿದ್ದು, ಇದರ ವಿರುದ್ಧ ಬೇರೆ ಯಾವ ಕೋರ್ಟ್‌ನಲ್ಲೂ ಮೇಲ್ಮನವಿಗೆ ಅವಕಾಶವಿಲ್ಲದೆ ಶಾಶ್ವತ ಮುಕ್ತಿ ಸಿಗುತ್ತದೆ.
* **ಕೋರ್ಟ್ ಫೀ ಮರುಪಾವತಿ:** ನ್ಯಾಯಾಲಯದಲ್ಲಿದ್ದ ಕೇಸ್ ಲೋಕ ಅದಾಲತ್‌ನಲ್ಲಿ ಇತ್ಯರ್ಥವಾದರೆ ಈ ಹಿಂದೆ ಪಾವತಿಸಿದ್ದ ಕೋರ್ಟ್ ಶುಲ್ಕವನ್ನು ಸಂಪೂರ್ಣ ವಾಪಸ್ ನೀಡಲಾಗುತ್ತದೆ.
* **ಟ್ರಾಫಿಕ್ ಚಲನ್ ರಿಯಾಯಿತಿ:** ಸರ್ಕಾರ ವಿಶೇಷ ಆದೇಶ ಹೊರಡಿಸಿದ ಸಂದರ್ಭಗಳಲ್ಲಿ ಬಾಕಿ ಟ್ರಾಫಿಕ್ ಫೈನ್‌ಗಳಿಗೆ 50% ವರೆಗೆ ರಿಯಾಯಿತಿ ಸೌಲಭ್ಯ ಸಿಗುತ್ತದೆ.

🔗 **ಸಂಪರ್ಕ:** [kslsa.kar.nic.in](https://kslsa.kar.nic.in) | ಟೋಲ್-ಫ್ರೀ ಲೀಗಲ್ ಹೆಲ್ಪ್‌ಲೈನ್: **15100**""",
        "category": "LEGAL",
        "language": "kn",
        "source_url": "https://kslsa.kar.nic.in",
        "keywords": "lok adalat karnataka, kslsa, traffic challan settlement, dispute compromise, ಲೋಕ ಅದಾಲತ್, ರಾಜಿ ಸಂಧಾನ",
        "action_label": "⚖️ KSLSA ಪೋರ್ಟಲ್",
        "action_url": "https://kslsa.kar.nic.in"
    }
]

# =========================================================================
# 10. EXPANSION BATCH 2: HOUSING, RURAL E-SWATHU, AGRICULTURE & SOCIAL WELFARE
# =========================================================================

ADDITIONAL_EXPANSION_FAQS_BATCH_2 = [
    {
        "id": "faq_eswathu_136",
        "question": "ಇ-ಸ್ವತ್ತು (E-Swathu) ಎಂದರೇನು? ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ವ್ಯಾಪ್ತಿಯ ನಮೂನೆ 9 ಮತ್ತು 11 (Form 9 & 11) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "e swathu form 9 form 11 gram panchayat property search ಇ-ಸ್ವತ್ತು ನಮೂನೆ 9 ನಮೂನೆ 11",
        "answer": """### 🏡 ಇ-ಸ್ವತ್ತು (E-Swathu) — ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ಆಸ್ತಿ ದಾಖಲೆಗಳು

ಗ್ರಾಮೀಣ ಪ್ರದೇಶಗಳಲ್ಲಿ ಆಸ್ತಿಗಳ ನಕಲಿ ನೋಂದಣಿ ತಡೆಯಲು ಹಾಗೂ ಅಧಿಕೃತ ಮಾಲೀಕತ್ವ ನೀಡಲು ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಇಲಾಖೆಯು (RDPR) **ಇ-ಸ್ವತ್ತು ತಂತ್ರಾಂಶ**ವನ್ನು ಕಡ್ಡಾಯಗೊಳಿಸಿದೆ.

---

### 📜 ನಮೂನೆ 9 ಮತ್ತು ನಮೂನೆ 11 ರ ವ್ಯತ್ಯಾಸ:
* **ನಮೂನೆ 9 (Form 9):** ಗ್ರಾಮಠಾಣಾ (ಗ್ರಾಮದ ವಸತಿ ಪ್ರದೇಶ) ವ್ಯಾಪ್ತಿಯಲ್ಲಿರುವ ಅಥವಾ ನಗರಾಭಿವೃದ್ಧಿ ಪ್ರಾಧಿಕಾರದಿಂದ ಅನುಮೋದನೆ ಪಡೆದ ಭೂ-ಪರಿವರ್ತಿತ (DC Converted) ನಿವೇಶನಗಳಿಗೆ ನೀಡುವ ಅಧಿಕೃತ ದಾಖಲೆ.
* **ನಮೂನೆ 11 (Form 11):** ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಆಸ್ತಿ ತೆರಿಗೆ ನಿಗದಿಪಡಿಸಲು ನೀಡುವ ಆಸ್ತಿ ನೋಂದಣಿ ಪುಸ್ತಕದ ಸಾರಾಂಶ (Property Tax Register Extract).

---

### 💻 ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಇ-ಸ್ವತ್ತು ಪರಿಶೀಲಿಸುವ ವಿಧಾನ:
1. [e-swathu.kar.nic.in](https://e-swathu.kar.nic.in) ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ.
2. **'Search Property' (ಆಸ್ತಿ ಹುಡುಕು)** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ಜಿಲ್ಲೆ, ತಾಲೂಕು, ಗ್ರಾಮ ಪಂಚಾಯಿತಿ, ಗ್ರಾಮ ಮತ್ತು ಆಸ್ತಿ ಸಂಖ್ಯೆ (Property ID) ನಮೂದಿಸಿ.
4. ಪಂಚಾಯಿತಿ ಅಭಿವೃದ್ಧಿ ಅಧಿಕಾರಿ (PDO) ಡಿಜಿಟಲ್ ಸಹಿ ಮಾಡಿರುವ ನಮೂನೆ 9/11 PDF ಅನ್ನು ತಕ್ಷಣ ವೀಕ್ಷಿಸಬಹುದು ಅಥವಾ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.

⚠️ ಉಪನೋಂದಣಾಧಿಕಾರಿ ಕಚೇರಿಯಲ್ಲಿ ಗ್ರಾಮೀಣ ಆಸ್ತಿ ನೋಂದಣಿ ಮಾಡಲು ಡಿಜಿಟಲ್ ಇ-ಸ್ವತ್ತು ಕಡ್ಡಾಯ.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://e-swathu.kar.nic.in",
        "keywords": "e swathu, form 9, form 11, gram panchayat property, ಇ-ಸ್ವತ್ತು, ನಮೂನೆ 9, ನಮೂನೆ 11, ಪಿಡಿಒ",
        "action_label": "🏡 ಇ-ಸ್ವತ್ತು ಪೋರ್ಟಲ್",
        "action_url": "https://e-swathu.kar.nic.in"
    },
    {
        "id": "faq_ganga_137",
        "question": "ಗಂಗಾ ಕಲ್ಯಾಣ ಯೋಜನೆ (Ganga Kalyana Scheme) ಯಡಿ ಉಚಿತ ಬೋರ್‌ವೆಲ್ ಮತ್ತು ಪಂಪ್‌ಸೆಟ್ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "ganga kalyana scheme free borewell irrigation subsidy sc st obc minority ಗಂಗಾ ಕಲ್ಯಾಣ ಯೋಜನೆ",
        "answer": """### 🌾 ಗಂಗಾ ಕಲ್ಯಾಣ ಯೋಜನೆ (Ganga Kalyana Irrigation Scheme)

ಸಣ್ಣ ಮತ್ತು ಅತಿ ಸಣ್ಣ ಹಿಂದುಳಿದ ವರ್ಗ, ಪರಿಶಿಷ್ಟ ಜಾತಿ, ಪರಿಶಿಷ್ಟ ಪಂಗಡ ಹಾಗೂ ಅಲ್ಪಸಂಖ್ಯಾತ ರೈತರಿಗೆ ನೀರಾವರಿ ಸೌಲಭ್ಯ ಒದಗಿಸಲು ಸರ್ಕಾರವೇ ಉಚಿತವಾಗಿ ಕೊಳವೆಬಾವಿ (Borewell) ಕೊರೆಸಿ, ಪಂಪ್‌ಸೆಟ್ ಮತ್ತು ವಿದ್ಯುದ್ದೀಕರಣ ಒದಗಿಸುವ ಯೋಜನೆ.

---

### 📌 ಅರ್ಹತೆಯ ಮಾನದಂಡಗಳು:
1. ಅರ್ಜಿದಾರರು ಸಣ್ಣ ಅಥವಾ ಅತಿ ಸಣ್ಣ ರೈತರಾಗಿರಬೇಕು (ಕನಿಷ್ಠ 1 ಎಕರೆಯಿಂದ ಗರಿಷ್ಠ 5 ಎಕರೆ ಕೃಷಿ ಜಮೀನು).
2. ಯಾವುದೇ ನೀರಾವರಿ ಸೌಲಭ್ಯವಿರದ ಒಣಭೂಮಿ (ಖುಷ್ಕಿ ಜಮೀನು) ಹೊಂದಿರಬೇಕು.
3. ಕುಟುಂಬದ ವಾರ್ಷಿಕ ಆದಾಯ ಗ್ರಾಮೀಣ ಪ್ರದೇಶದಲ್ಲಿ ₹98,000 ಮತ್ತು ನಗರ ಪ್ರದೇಶದಲ್ಲಿ ₹1.20 ಲಕ್ಷ ಮೀರಿರಬಾರದು.
4. ಒಂದೇ ಕುಟುಂಬದಲ್ಲಿ ಈ ಹಿಂದೆ ಗಂಗಾ ಕಲ್ಯಾಣ ಸೌಲಭ್ಯ ಪಡೆದಿರಬಾರದು.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು & ಅರ್ಜಿ ಸಲ್ಲಿಕೆ:
* ಜಮೀನಿನ ಪಹಣಿ (RTC), ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ (RD Number).
* ಸಣ್ಣ/ಅತಿ ಸಣ್ಣ ರೈತರ ದೃಢೀಕರಣ ಪತ್ರ (ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿಯಿಂದ).
* ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್.
* [sevasindhu.karnataka.gov.in](https://sevasindhu.karnataka.gov.in) ಅಥವಾ ಆಯಾ ಅಭಿವೃದ್ಧಿ ನಿಗಮಗಳ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ (D. Devaraj Urs, Ambedkar, KMDC) ಅರ್ಜಿ ಸಲ್ಲಿಸಬೇಕು.""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://sevasindhu.karnataka.gov.in",
        "keywords": "ganga kalyana, free borewell, irrigation subsidy, ಗಂಗಾ ಕಲ್ಯಾಣ, ಉಚಿತ ಬೋರ್‌ವೆಲ್, ನೀರಾವರಿ",
        "action_label": "🌾 ಸೇವಾ ಸಿಂಧು ಪೋರ್ಟಲ್",
        "action_url": "https://sevasindhu.karnataka.gov.in"
    },
    {
        "id": "faq_ashraya_138",
        "question": "ಆಶ್ರಯ / ಬಸವ ವಸತಿ ಯೋಜನೆ ಮತ್ತು ಡಾ. ಬಿ.ಆರ್. ಅಂಬೇಡ್ಕರ್ ನಿವಾಸ ಯೋಜನೆಯಡಿ ಉಚಿತ ಮನೆ ಸಹಾಯಧನ ಎಷ್ಟು?",
        "normalized_question": "basava vasati yojana ashraya scheme rgrhcl free housing subsidy ಬಸವ ವಸತಿ ಯೋಜನೆ ಆಶ್ರಯ",
        "answer": """### 🏠 ರಾಜೀವ್ ಗಾಂಧಿ ಗ್ರಾಮೀಣ ವಸತಿ ನಿಗಮ (RGRHCL) — ಬಸವ ವಸತಿ & ಆಶ್ರಯ ಯೋಜನೆಗಳು

ಸ್ವಂತ ನಿವೇಶನ ಹೊಂದಿರುವ ಆದರೆ ಪಕ್ಕಾ ಮನೆ ಇಲ್ಲದ ಬಡ ಗ್ರಾಮೀಣ ಮತ್ತು ನಗರ ಕುಟುಂಬಗಳಿಗೆ ಮನೆ ನಿರ್ಮಿಸಿಕೊಳ್ಳಲು ಸರ್ಕಾರ ಹಂತ-ಹಂತವಾಗಿ ನೇರ ಸಹಾಯಧನ ನೀಡುತ್ತದೆ.

---

### 💰 ಸರ್ಕಾರದ ಸಹಾಯಧನ ಮೊತ್ತ:
* **ಸಾಮಾನ್ಯ & ಹಿಂದುಳಿದ ವರ್ಗಗಳು (ಬಸವ ವಸತಿ ಯೋಜನೆ):** ₹1.20 ಲಕ್ಷದಿಂದ ₹1.50 ಲಕ್ಷದವರೆಗೆ ನೇರ ನಗದು ಸಹಾಯಧನ.
* **SC / ST ಫಲಾನುಭವಿಗಳು (ಡಾ. ಬಿ.ಆರ್. ಅಂಬೇಡ್ಕರ್ ನಿವಾಸ ಯೋಜನೆ):** ಗ್ರಾಮೀಣ ಪ್ರದೇಶದಲ್ಲಿ **₹1.75 ಲಕ್ಷ**, ನಗರ ಪ್ರದೇಶದಲ್ಲಿ **₹2.00 ಲಕ್ಷ**.
* ಇದರ ಜೊತೆಗೆ ಮಹಾತ್ಮ ಗಾಂಧಿ ಉದ್ಯೋಗ ಖಾತರಿ (MGNREGA) ಅಡಿಯಲ್ಲಿ 90 ದಿನಗಳ ಕೂಲಿ ಹಣ (ಸುಮಾರು ₹27,000+) ಮತ್ತು ಶೌಚಾಲಯ ನಿರ್ಮಾಣಕ್ಕೆ ₹12,000 ಹೆಚ್ಚುವರಿ ಅನುದಾನ ಸಿಗುತ್ತದೆ.

---

### 📱 ಜಿಪಿಎಸ್ ಹಂತಗಳು & ಹಣ ಜಮೆ (Ashraya App):
ಮನೆಯ ಅಡಿಪಾಯ (Foundation), ಲಿಂಟಲ್ (Lintel), ಛಾವಣಿ (Roofing) ಮತ್ತು ಪೂರ್ಣಗೊಂಡ (Completed) 4 ಹಂತಗಳಲ್ಲಿ ಜಿಪಿಎಸ್ ಫೋಟೋ ತೆಗೆದ ನಂತರ ನೇರವಾಗಿ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ DBT ಆಗುತ್ತದೆ.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [ashraya.karnataka.gov.in](https://ashraya.karnataka.gov.in)""",
        "category": "WELFARE",
        "language": "kn",
        "source_url": "https://ashraya.karnataka.gov.in",
        "keywords": "basava vasati, ashraya scheme, rgrhcl housing subsidy, ಬಸವ ವಸತಿ ಯೋಜನೆ, ಉಚಿತ ಮನೆ, ಆಶ್ರಯ",
        "action_label": "🏠 ಆಶ್ರಯ ಪೋರ್ಟಲ್",
        "action_url": "https://ashraya.karnataka.gov.in"
    },
    {
        "id": "faq_marr_139",
        "question": "ಕಾವೇರಿ 2.0 ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಆನ್‌ಲೈನ್ ವಿವಾಹ ನೋಂದಣಿ (Marriage Registration) ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "marriage registration online kaveri 2.0 sub registrar certificate ವಿವಾಹ ನೋಂದಣಿ ಕಾವೇರಿ",
        "answer": """### 💍 ಕಾವೇರಿ 2.0 ಮೂಲಕ ಆನ್‌ಲೈನ್ ವಿವಾಹ ನೋಂದಣಿ (Hindu Marriage Act / Special Marriage Act)

ಕರ್ನಾಟಕದಲ್ಲಿ ಸಬ್-ರಿಜಿಸ್ಟ್ರಾರ್ ಕಚೇರಿಗೆ ಅಲೆದಾಡದೆ ಕಾವೇರಿ 2.0 ಮೂಲಕ ಆನ್‌ಲೈನ್‌ನಲ್ಲೇ ಮದುವೆ ನೋಂದಣಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ಸ್ಲಾಟ್ ಬುಕ್ ಮಾಡಬಹುದು.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
1. ವಧು ಮತ್ತು ವರನ ವಯಸ್ಸಿನ ಪುರಾವೆ (SSLC ಅಂಕಪಟ್ಟಿ / ಪಾಸ್‌ಪೋರ್ಟ್ / ಜನನ ಪ್ರಮಾಣಪತ್ರ - ವರನಿಗೆ 21 ವರ್ಷ, ವಧುವಿಗೆ 18 ವರ್ಷ ತುಂಬಿರಬೇಕು).
2. ವಧು-ವರರ ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ವಾಸಸ್ಥಳದ ಪುರಾವೆ.
3. ಮದುವೆ ಆಮಂತ್ರಣ ಪತ್ರಿಕೆ (Marriage Invitation Card) ಮತ್ತು ಮದುವೆ ಮಂಟಪದ ರಶೀದಿ / ಫೋಟೋ.
4. ಮೂವರು (3) ಸಾಕ್ಷಿದಾರರ ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ವಿಳಾಸ ದಾಖಲೆ.

---

### 🚀 ಪ್ರಕ್ರಿಯೆ:
1. [kaveri.karnataka.gov.in](https://kaveri.karnataka.gov.in) ಗೆ ಲಾಗಿನ್ ಆಗಿ **'Marriage Registration'** ಆಯ್ಕೆಮಾಡಿ.
2. ವಧು-ವರ ಹಾಗೂ ಸಾಕ್ಷಿದಾರರ ವಿವರ ನಮೂದಿಸಿ ದಾಖಲೆಗಳನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
3. ಆನ್‌ಲೈನ್ ಶುಲ್ಕ ಪಾವತಿಸಿ ಸಬ್-ರಿಜಿಸ್ಟ್ರಾರ್ ಕಚೇರಿ ಭೇಟಿಗೆ ದಿನಾಂಕ ಹಾಗೂ ಸಮಯದ ಸ್ಲಾಟ್ ಆಯ್ಕೆಮಾಡಿ.
4. ನಿಗದಿತ ದಿನದಂದು ಕಚೇರಿಗೆ ತೆರಳಿ ಬಯೋಮೆಟ್ರಿಕ್ ಹೆಬ್ಬೆಟ್ಟಿನ ಗುರುತು ನೀಡಿದ ತಕ್ಷಣ ಡಿಜಿಟಲ್ ವಿವಾಹ ಪ್ರಮಾಣಪತ್ರ ಸಿಗುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://kaveri.karnataka.gov.in",
        "keywords": "marriage registration, kaveri 2.0 marriage certificate, ವಿವಾಹ ನೋಂದಣಿ, ಮದುವೆ ಪ್ರಮಾಣಪತ್ರ",
        "action_label": "💍 ಕಾವೇರಿ 2.0 ಪೋರ್ಟಲ್",
        "action_url": "https://kaveri.karnataka.gov.in"
    },
    {
        "id": "faq_meter_140",
        "question": "ಬೆಸ್ಕಾಂ / ಎಸ್ಕಾಂಗಳಲ್ಲಿ ವಿದ್ಯುತ್ ಮೀಟರ್ ಹೆಸರು ವರ್ಗಾವಣೆ (Name Transfer) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "bescom meter name transfer change of ownership online ಬೆಸ್ಕಾಂ ಮೀಟರ್ ಹೆಸರು ಬದಲಾವಣೆ",
        "answer": """### ⚡ ವಿದ್ಯುತ್ ಮೀಟರ್ ಮಾಲೀಕತ್ವ ವರ್ಗಾವಣೆ (Electricity Meter Name Transfer)

ಮನೆ ಅಥವಾ ವಾಣಿಜ್ಯ ಮಳಿಗೆ ಖರೀದಿಸಿದಾಗ ಹಳೆಯ ಮಾಲೀಕರ ಹೆಸರಿನಲ್ಲಿರುವ ವಿದ್ಯುತ್ ಸಂಪರ್ಕವನ್ನು (Account ID) ನಿಮ್ಮ ಹೆಸರಿಗೆ ಬದಲಾಯಿಸಿಕೊಳ್ಳುವ ಸುಲಭ ವಿಧಾನ:

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
* ನೋಂದಾಯಿತ ಕ್ರಯಪತ್ರ (Registered Sale Deed) ಅಥವಾ ಇತ್ತೀಚಿನ ಕಂದಾಯ ಇ-ಖಾತಾ ಪ್ರತಿ.
* ಇತ್ತೀಚಿನ ವಿದ್ಯುತ್ ಬಿಲ್ ಪಾವತಿ ರಶೀದಿ (ಯಾವುದೇ ಬಾಕಿ ಇರಬಾರದು).
* ಹೊಸ ಮಾಲೀಕರ ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ಫೋಟೋ.
* ಹಳೆಯ ಮಾಲೀಕರಿಂದ ನಿರಾಕ್ಷೇಪಣಾ ಪತ್ರ (NOC) ಅಥವಾ ಮರಣ ಹೊಂದಿದ್ದರೆ ಮರಣ ಪ್ರಮಾಣಪತ್ರ & ವಾರಸುದಾರಿಕೆ ದಾಖಲೆ.

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಕೆ:
1. ನಿಮ್ಮ ಎಸ್ಕಾಂ (BESCOM, HESCOM, MESCOM, GESCOM, CESC) ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್‌ಗೆ ಲಾಗಿನ್ ಆಗಿ.
2. **'Change of Name / Transfer of Installation'** ಸೇವೆ ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಗದಿತ ವರ್ಗಾವಣೆ ಶುಲ್ಕವನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪಾವತಿಸಿ ದಾಖಲೆ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
4. ಸೆಕ್ಷನ್ ಆಫೀಸರ್ ಪರಿಶೀಲಿಸಿದ 7 ದಿನಗಳಲ್ಲಿ ಹೊಸ ಬಿಲ್ ನಿಮ್ಮ ಹೆಸರಿನಲ್ಲೇ ಮುದ್ರಿತವಾಗುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bescom.karnataka.gov.in",
        "keywords": "bescom name transfer, meter ownership change, escom meter transfer, ಮೀಟರ್ ಹೆಸರು ವರ್ಗಾವಣೆ",
        "action_label": "⚡ ಬೆಸ್ಕಾಂ ಸೇವೆಗಳು",
        "action_url": "https://bescom.karnataka.gov.in"
    },
    {
        "id": "faq_panchatantra_141",
        "question": "ಪಂಚತಂತ್ರ 2.0 (Panchatantra 2.0) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ಸೇವೆಗಳಿಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "panchatantra 2.0 gram panchayat citizen services building permission trade license ಪಂಚತಂತ್ರ 2.0",
        "answer": """### 🏛️ ಪಂಚತಂತ್ರ 2.0 (Panchatantra 2.0) — ಗ್ರಾಮ ಪಂಚಾಯತ್ ಆನ್‌ಲೈನ್ ಪೋರ್ಟಲ್

ಗ್ರಾಮೀಣ ಭಾಗದ ಸಾರ್ವಜನಿಕರಿಗೆ ಪಂಚಾಯಿತಿ ಕಚೇರಿಗೆ ಹೋಗದೆ ಮನೆಯಲ್ಲೇ ಡಿಜಿಟಲ್ ಸೇವೆಗಳನ್ನು ಒದಗಿಸಲು ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಇಲಾಖೆಯು ಪಂಚತಂತ್ರ 2.0 ಜಾರಿಗೆ ತಂದಿದೆ.

---

### 📋 ಲಭ್ಯವಿರುವ ಪ್ರಮುಖ ಆನ್‌ಲೈನ್ ಸೇವೆಗಳು:
1. **ಕಟ್ಟಡ ನಿರ್ಮಾಣ ಪರವಾನಗಿ (Building Construction Permission):** ಗ್ರಾಮೀಣ ನಿವೇಶನಗಳಲ್ಲಿ ಮನೆ ನಿರ್ಮಿಸಲು ಅನುಮೋದನೆ.
2. **ಕುಡಿಯುವ ನೀರಿನ ಸಂಪರ್ಕ (Drinking Water Tap Connection):** ಹೊಸ ಪೈಪ್‌ಲೈನ್ ಸಂಪರ್ಕಕ್ಕೆ ಅರ್ಜಿ.
3. **ವಾಣಿಜ್ಯ ಪರವಾನಗಿ (Trade License):** ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಅಂಗಡಿ, ಕಾರ್ಖಾನೆ ತೆರೆಯಲು ಲೈಸೆನ್ಸ್.
4. **ರಸ್ತೆ ಅಗೆಯುವಿಕೆ ಅನುಮತಿ & ನಿರಾಕ್ಷೇಪಣಾ ಪತ್ರ (NOC):** ವಿದ್ಯುತ್ ಅಥವಾ ದೂರವಾಣಿ ಸಂಪರ್ಕಕ್ಕೆ NOC.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [panchatantra.karnataka.gov.in](https://panchatantra.karnataka.gov.in)""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://panchatantra.karnataka.gov.in",
        "keywords": "panchatantra 2.0, gram panchayat services, building permission, ಪಂಚತಂತ್ರ 2.0, ಗ್ರಾಮ ಪಂಚಾಯತ್ ಸೇವೆ",
        "action_label": "🏛️ ಪಂಚತಂತ್ರ ಪೋರ್ಟಲ್",
        "action_url": "https://panchatantra.karnataka.gov.in"
    },
    {
        "id": "faq_janaspandana_142",
        "question": "ಮುಖ್ಯಮಂತ್ರಿಗಳ ಜನಸ್ಪಂದನ (Janaspandana / IPGRS) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ದೂರು ದಾಖಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "janaspandana cm grievance portal ipgrs karnataka complaint status ಜನಸ್ಪಂದನ ದೂರು",
        "answer": """### 📢 ಜನಸ್ಪಂದನ (Janaspandana - IPGRS) — ಮುಖ್ಯಮಂತ್ರಿಗಳ ಸಾರ್ವಜನಿಕ ಕುಂದುಕೊರತೆ ನಿವಾರಣಾ ಪೋರ್ಟಲ್

ಸರ್ಕಾರಿ ಕಚೇರಿಗಳಲ್ಲಿ ಕೆಲಸ ವಿಳಂಬವಾದರೆ, ಅಧಿಕಾರಿಗಳು ಸ್ಪಂದಿಸದಿದ್ದರೆ ಅಥವಾ ಯಾವುದೇ ಯೋಜನೆಗಳ ಲೋಪವಿದ್ದರೆ ನೇರವಾಗಿ ಮುಖ್ಯಮಂತ್ರಿಗಳ ಸಚಿವಾಲಯಕ್ಕೆ ದೂರು ಸಲ್ಲಿಸುವ ವ್ಯವಸ್ಥೆ.

---

### 📱 ದೂರು ದಾಖಲಿಸುವ 3 ಮಾರ್ಗಗಳು:
1. **ಟೋಲ್-ಫ್ರೀ ಕಾಲ್ ಸೆಂಟರ್:** **1902** ಸಂಖ್ಯೆಗೆ ಕರೆ ಮಾಡಿ ನಿಮ್ಮ ದೂರು ದಾಖಲಿಸಬಹುದು.
2. **ಆನ್‌ಲೈನ್ ಪೋರ್ಟಲ್:** [janaspandana.karnataka.gov.in](https://janaspandana.karnataka.gov.in) ನಲ್ಲಿ ಆಧಾರ್ ಒಟಿಪಿ ಮೂಲಕ ಲಾಗಿನ್ ಆಗಿ ದೂರು ಮತ್ತು ದಾಖಲೆ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
3. **ನೇರ ಜನಸ್ಪಂದನ ಸಮಾವೇಶ:** ಜಿಲ್ಲಾ ಮಟ್ಟದಲ್ಲಿ ಜಿಲ್ಲಾ ಉಸ್ತುವಾರಿ ಸಚಿವರು ಮತ್ತು ಬೆಂಗಳೂರಿನಲ್ಲಿ ಮುಖ್ಯಮಂತ್ರಿಗಳು ನಡೆಸುವ ಜನಸ್ಪಂದನದಲ್ಲಿ ಲಿಖಿತ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು.

💡 ದೂರು ದಾಖಲಾದ ತಕ್ಷಣ SMS ಮೂಲಕ **Grievance ID** ಬರುತ್ತದೆ. 30 ದಿನಗಳೊಳಗೆ ಸಂಬಂಧಪಟ್ಟ ಜಿಲ್ಲಾಧಿಕಾರಿ/ಇಲಾಖಾ ಮುಖ್ಯಸ್ಥರು ಕ್ರಮ ಕೈಗೊಂಡು ವರದಿ ನೀಡಬೇಕು.""",
        "category": "ADMIN",
        "language": "kn",
        "source_url": "https://janaspandana.karnataka.gov.in",
        "keywords": "janaspandana, 1902 helpline, cm grievance, ipgrs, ಜನಸ್ಪಂದನ, ಮುಖ್ಯಮಂತ್ರಿ ದೂರು ಪೋರ್ಟಲ್",
        "action_label": "📢 ಜನಸ್ಪಂದನ ಪೋರ್ಟಲ್",
        "action_url": "https://janaspandana.karnataka.gov.in"
    },
    {
        "id": "faq_udid_143",
        "question": "ವಿಶೇಷ ಚೇತನರ ವಿಶಿಷ್ಟ ಗುರುತಿನ ಚೀಟಿ (UDID Card) ಮತ್ತು ಮಾಸಿಕ ಪಿಂಚಣಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "udid card unique disability identity card monthly pension karnataka ವಿಕಲಚೇತನರ ಪಿಂಚಣಿ ಯುಡಿಐಡಿ",
        "answer": """### ♿ ವಿಶೇಷ ಚೇತನರ UDID ಕಾರ್ಡ್ ಮತ್ತು ಮಾಸಿಕ ಪಿಂಚಣಿ ಸೌಲಭ್ಯ

ಭಾರತ ಸರ್ಕಾರದ ಸಾಮಾಜಿಕ ನ್ಯಾಯ ಮತ್ತು ಸಬಲೀಕರಣ ಸಚಿವಾಲಯವು ವಿಶೇಷ ಚೇತನರಿಗೆ ರಾಷ್ಟ್ರವ್ಯಾಪಿ ಮಾನ್ಯತೆ ಇರುವ **UDID (Unique Disability ID) ಕಾರ್ಡ್** ನೀಡುತ್ತದೆ.

---

### 💰 ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಮಾಸಿಕ ಪಿಂಚಣಿ ಮೊತ್ತ:
* **40% ರಿಂದ 74% ಅಂಗವಿಕಲತೆ ಹೊಂದಿರುವವರಿಗೆ:** ತಿಂಗಳಿಗೆ **₹1,400**.
* **75% ಮತ್ತು ಅದಕ್ಕಿಂತ ಹೆಚ್ಚಿನ ತೀವ್ರ ಅಂಗವಿಕಲತೆ ಹೊಂದಿರುವವರಿಗೆ:** ತಿಂಗಳಿಗೆ **₹2,000**.

---

### 📋 UDID ಕಾರ್ಡ್ ಪಡೆಯುವ ವಿಧಾನ:
1. [swavlambancard.gov.in](https://swavlambancard.gov.in) ನಲ್ಲಿ ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.
2. ನಿಮ್ಮ ಜಿಲ್ಲಾ ಸರ್ಕಾರಿ ಆಸ್ಪತ್ರೆಯ ವೈದ್ಯಕೀಯ ಮಂಡಳಿಯ (Medical Board) ಮುಂದೆ ಹಾಜರಾಗಿ ಅಂಗವಿಕಲತೆ ಶೇಕಡಾವಾರು ಪರೀಕ್ಷಿಸಿಕೊಳ್ಳಿ.
3. ಪ್ರಮಾಣೀಕರಣ ಪೂರ್ಣಗೊಂಡ ನಂತರ ಕ್ಯೂಆರ್ ಕೋಡ್ ಮತ್ತು ಬ್ರೈಲ್ ಲಿಪಿ ಹೊಂದಿರುವ ಸ್ಮಾರ್ಟ್ ಕಾರ್ಡ್ ಮನೆ ವಿಳಾಸಕ್ಕೆ ಬರುತ್ತದೆ.""",
        "category": "WELFARE",
        "language": "kn",
        "source_url": "https://swavlambancard.gov.in",
        "keywords": "udid card, disability pension karnataka, swavlamban card, ವಿಶೇಷ ಚೇತನರ ಪಿಂಚಣಿ, ಯುಡಿಐಡಿ ಕಾರ್ಡ್",
        "action_label": "♿ UDID ಪೋರ್ಟಲ್",
        "action_url": "https://swavlambancard.gov.in"
    },
    {
        "id": "faq_pcc_144",
        "question": "ಪೊಲೀಸ್ ಕ್ಲಿಯರೆನ್ಸ್ ಪ್ರಮಾಣಪತ್ರ (Police Verification Certificate / PVC) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "police verification certificate pvc pcc ksp karnataka police online ಪೊಲೀಸ್ ಪರಿಶೀಲನಾ ಪ್ರಮಾಣ ಪತ್ರ",
        "answer": """### 👮 ಪೊಲೀಸ್ ಪರಿಶೀಲನಾ ಪ್ರಮಾಣಪತ್ರ (Police Verification Certificate - PVC / PCC)

ಖಾಸಗಿ ಕಂಪನಿಗಳ ಉದ್ಯೋಗ, ವಿದೇಶಿ ವೀಸಾ, ಪಾಸ್‌ಪೋರ್ಟ್, ಭದ್ರತಾ ಏಜೆನ್ಸಿ ಕೆಲಸ ಅಥವಾ ಸರ್ಕಾರಿ ಗುತ್ತಿಗೆದಾರರ ಪರವಾನಗಿಗಾಗಿ ಯಾವುದೇ ಅಪರಾಧ ಹಿನ್ನೆಲೆ ಇಲ್ಲವೆಂದು ಸಾಬೀತುಪಡಿಸಲು PVC ಅಗತ್ಯ.

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಕೆ:
1. **ಕರ್ನಾಟಕ ಪೊಲೀಸ್ ಪೋರ್ಟಲ್:** [ksp.karnataka.gov.in](https://ksp.karnataka.gov.in) ಅಥವಾ **Seva Sindhu** ಗೆ ಭೇಟಿ ನೀಡಿ.
2. **'Police Verification Services'** ಆಯ್ಕೆಮಾಡಿ (ಉದ್ಯೋಗಕ್ಕಾಗಿ ಅಥವಾ ಪಾಸ್‌ಪೋರ್ಟ್‌ಗಾಗಿ).
3. ಆಧಾರ್ ಕಾರ್ಡ್, ಪ್ರಸ್ತುತ ವಿಳಾಸದ ಪುರಾವೆ ಮತ್ತು ಭಾವಚಿತ್ರ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
4. ನಿಗದಿತ ಸರ್ಕಾರಿ ಶುಲ್ಕ (ಸಾಮಾನ್ಯ ನಾಗರಿಕರಿಗೆ ₹250, ಕಂಪನಿಗಳಿಗೆ ₹500) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪಾವತಿಸಿ.
5. ಸ್ಥಳೀಯ ಠಾಣೆಯ ಪೊಲೀಸ್ ಸಿಬ್ಬಂದಿ ಭೌತಿಕ ಸ್ಥಳ ಪರಿಶೀಲನೆ ನಡೆಸಿದ 10-15 ದಿನಗಳಲ್ಲಿ ಡಿಜಿಟಲ್ ಸಹಿಯುಳ್ಳ PVC ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.""",
        "category": "POLICE",
        "language": "kn",
        "source_url": "https://ksp.karnataka.gov.in",
        "keywords": "police verification certificate, pvc pcc online, ksp verification, ಪೊಲೀಸ್ ವೆರಿಫಿಕೇಷನ್ ಸರ್ಟಿಫಿಕೇಟ್",
        "action_label": "👮 ಪೊಲೀಸ್ ಸೇವೆಗಳು",
        "action_url": "https://ksp.karnataka.gov.in"
    },
    {
        "id": "faq_kusum_145",
        "question": "ಪಿಎಂ ಕುಸುಮ್ (PM-KUSUM) ಯೋಜನೆಯಡಿ ಸೌರ ಕೃಷಿ ಪಂಪ್‌ಸೆಟ್‌ಗೆ (Solar Pump Set) ಸಬ್ಸಿಡಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "pm kusum solar pump subsidy karnataka breda farmers ಸೋಲಾರ್ ಪಂಪ್ ಸೆಟ್ ಸಬ್ಸಿಡಿ",
        "answer": """### ☀️ ಪಿಎಂ ಕುಸುಮ್ (PM-KUSUM Component-B) ಸೌರ ಪಂಪ್‌ಸೆಟ್ ಯೋಜನೆ

ವಿದ್ಯುತ್ ಸಂಪರ್ಕವಿಲ್ಲದ ಅಥವಾ ಡೀಸೆಲ್ ಪಂಪ್‌ಸೆಟ್ ಬಳಸುತ್ತಿರುವ ರೈತರಿಗೆ ಹಗಲು ಹೊತ್ತಿನಲ್ಲೇ ನಿರಂತರ ಕೃಷಿ ನೀರಾವರಿಗಾಗಿ ಸೌರಶಕ್ತಿ ಚಾಲಿತ ಪಂಪ್‌ಸೆಟ್‌ಗಳನ್ನು ಭಾರಿ ಸಬ್ಸಿಡಿಯೊಂದಿಗೆ ಅಳವಡಿಸಲಾಗುತ್ತದೆ.

---

### 💰 ಸಬ್ಸಿಡಿ ರಚನೆ:
* **ಕೇಂದ್ರ ಸರ್ಕಾರದ ಪಾಲು:** 30% ಸಬ್ಸಿಡಿ.
* **ರಾಜ್ಯ ಸರ್ಕಾರದ ಪಾಲು (KREDL / ಇಂಧನ ಇಲಾಖೆ):** 50% ಸಬ್ಸಿಡಿ (SC/ST ರೈತರಿಗೆ 80% ವರೆಗೆ).
* **ರೈತರ ಪಾಲು:** ಕೇವಲ **20% ಮೊತ್ತ** ಮಾತ್ರ (ಬ್ಯಾಂಕ್ ಸಾಲ ಸೌಲಭ್ಯವೂ ಲಭ್ಯ).

---

### 📌 ಅರ್ಹತೆ & ಅರ್ಜಿ:
* ಜಮೀನಿನ ಪಹಣಿ (RTC), ಕೊಳವೆಬಾವಿ/ಬಾವಿ ಮೂಲದ ದೃಢೀಕರಣ ಮತ್ತು ಆಧಾರ್ ಕಾರ್ಡ್ ಹೊಂದಿರಬೇಕು.
* [kredlinfo.in](https://kredlinfo.in) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಅಧಿಸೂಚನೆ ಪ್ರಕಟವಾದಾಗ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಬೇಕು.""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://kredlinfo.in",
        "keywords": "pm kusum karnataka, solar pump subsidy, kredl solar irrigation, ಸೋಲಾರ್ ಪಂಪ್ ಸೆಟ್, ಕೃಷಿ ಸೌರ ವಿದ್ಯುತ್",
        "action_label": "☀️ KREDL ಪೋರ್ಟಲ್",
        "action_url": "https://kredlinfo.in"
    },
    {
        "id": "faq_elevate_146",
        "question": "ಕರ್ನಾಟಕ ಸ್ಟಾರ್ಟಪ್ ಎಲಿವೇಟ್ (Elevate Idea2POC) ಅನುದಾನಕ್ಕೆ ನವೋದ್ಯಮಗಳು ಅರ್ಜಿ ಸಲ್ಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "startup karnataka elevate 100 grant seed fund idea2poc ಎಲಿವೇಟ್ ಸ್ಟಾರ್ಟಪ್ ಅನುದಾನ",
        "answer": """### 🚀 ಸ್ಟಾರ್ಟಪ್ ಕರ್ನಾಟಕ 'ಎಲಿವೇಟ್' (Elevate 100 / Idea2POC) ಅನುದಾನ

ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಐಟಿ, ಬಿಟಿ ಮತ್ತು ವಿಜ್ಞಾನ ತಂತ್ರಜ್ಞಾನ ಇಲಾಖೆಯು ನವೀನ ಆಲೋಚನೆ ಮತ್ತು ತಂತ್ರಜ್ಞಾನ ಹೊಂದಿರುವ ಅರ್ಹ ಆರಂಭಿಕ ಹಂತದ ಸ್ಟಾರ್ಟಪ್‌ಗಳಿಗೆ ಯಾವುದೇ ಈಕ್ವಿಟಿ (Equity) ಪಡೆಯದೆ ನೀಡುವ ಅನುದಾನ.

---

### 💰 ಸೌಲಭ್ಯ & ಆರ್ಥಿಕ ನೆರವು:
* ಆಯ್ಕೆಯಾದ ಪ್ರತಿ ಸ್ಟಾರ್ಟಪ್‌ಗೆ **₹50 ಲಕ್ಷದವರೆಗೆ ನೇರ ಸೀಡ್ ಫಂಡಿಂಗ್ (Non-dilutive Grant)** ನೀಡಲಾಗುತ್ತದೆ.
* ಸರ್ಕಾರಿ ಇನ್‌ಕ್ಯುಬೇಟರ್‌ಗಳು, ಮಾರ್ಗದರ್ಶನ (Mentorship), ಪೇಟೆಂಟ್ ನೆರವು ಹಾಗೂ ಜಾಗತಿಕ ಹೂಡಿಕೆದಾರರ ಸಮಾವೇಶಗಳಲ್ಲಿ ಉಚಿತ ಮಳಿಗೆ ಸೌಲಭ್ಯ.

---

### 📌 ಅರ್ಹತಾ ಮಾನದಂಡಗಳು:
1. ಕಂಪನಿಯು ಪ್ರೈವೇಟ್ ಲಿಮಿಟೆಡ್ ಅಥವಾ ಎಲ್‌ಎಲ್‌ಪಿ ಆಗಿ ನೋಂದಣಿಯಾಗಿರಬೇಕು ಮತ್ತು ಕೇಂದ್ರದ DPIIT ಮಾನ್ಯತೆ ಹೊಂದಿರಬೇಕು.
2. ಕಂಪನಿಯ ಕಚೇರಿ ಅಥವಾ ಪ್ರಮುಖ ಆರ್&ಡಿ (R&D) ಘಟಕ ಕರ್ನಾಟಕದಲ್ಲೇ ಇರಬೇಕು.
3. ಮಹಿಳಾ ಉದ್ಯಮಿಗಳು ಮತ್ತು ಗ್ರಾಮೀಣ ಸ್ಟಾರ್ಟಪ್‌ಗಳಿಗೆ 'Elevate Womxn' ಮತ್ತು 'Elevate Kalyana Karnataka' ವಿಶೇಷ ವಿಭಾಗಗಳಿವೆ.

🔗 **ಅರ್ಜಿ ಸಲ್ಲಿಕೆ:** [startup.karnataka.gov.in](https://startup.karnataka.gov.in)""",
        "category": "INDUSTRY",
        "language": "kn",
        "source_url": "https://startup.karnataka.gov.in",
        "keywords": "startup karnataka, elevate 100, idea2poc grant, ಸ್ಟಾರ್ಟಪ್ ಕರ್ನಾಟಕ, ಎಲಿವೇಟ್ ಅನುದಾನ, ಸೀಡ್ ಫಂಡ್",
        "action_label": "🚀 ಸ್ಟಾರ್ಟಪ್ ಪೋರ್ಟಲ್",
        "action_url": "https://startup.karnataka.gov.in"
    },
    {
        "id": "faq_varuna_147",
        "question": "ವರುಣ ಮಿತ್ರ (Varuna Mitra) ರೈತರ ಹವಾಮಾನ ಸಹಾಯವಾಣಿ ಮತ್ತು ಮಳೆ ಮುನ್ಸೂಚನೆ ಮಾಹಿತಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "varuna mitra karnataka weather forecast rainfall helpline ksndmc ವರುಣ ಮಿತ್ರ ಮಳೆ ಮಾಹಿತಿ",
        "answer": """### 🌧️ ವರುಣ ಮಿತ್ರ (Varuna Mitra) — ಕರ್ನಾಟಕ ನೈಸರ್ಗಿಕ ವಿಕೋಪ ಉಸ್ತುವಾರಿ ಕೇಂದ್ರ (KSNDMC)

ರೈತರು ಬಿತ್ತನೆ, ಕೊಯ್ಲು ಮತ್ತು ಕೀಟನಾಶಕ ಸಿಂಪಡಣೆಗೆ ಅನುಕೂಲವಾಗುವಂತೆ ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ಮಟ್ಟದ ನೈಜ ಸಮಯದ ಮಳೆ ಮತ್ತು ಹವಾಮಾನ ಮುನ್ಸೂಚನೆ ನೀಡುವ ಅತ್ಯಾಧುನಿಕ ಸೌಲಭ್ಯ.

---

### 📞 24/7 ರೈತ ಸಹಾಯವಾಣಿ ಸಂಖ್ಯೆ:
* **ವರುಣ ಮಿತ್ರ ಸಹಾಯವಾಣಿ: 9243345433**
* ಈ ಸಂಖ್ಯೆಗೆ ಕರೆ ಮಾಡಿ ನಿಮ್ಮ ಜಿಲ್ಲೆ ಮತ್ತು ತಾಲೂಕು ತಿಳಿಸಿದರೆ ಮುಂದಿನ 3 ದಿನಗಳ ಮಳೆ ಸಾಧ್ಯತೆ, ತಾಪಮಾನ, ಗಾಳಿಯ ವೇಗ ಮತ್ತು ತೇವಾಂಶದ ನಿಖರ ಮಾಹಿತಿ ಲಭ್ಯವಾಗುತ್ತದೆ.
* ಬರ, ಚಂಡಮಾರುತ ಮತ್ತು ಅತಿವೃಷ್ಟಿ ಎಚ್ಚರಿಕೆಗಳನ್ನು ಮುಂಚಿತವಾಗಿಯೇ ಪಡೆಯಬಹುದು.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [ksndmc.karnataka.gov.in](https://ksndmc.karnataka.gov.in)""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://ksndmc.karnataka.gov.in",
        "keywords": "varuna mitra, ksndmc weather helpline, rainfall forecast, ವರುಣ ಮಿತ್ರ, ಮಳೆ ಮುನ್ಸೂಚನೆ, ಹವಾಮಾನ ಮಾಹಿತಿ",
        "action_label": "🌧️ KSNDMC ಪೋರ್ಟಲ್",
        "action_url": "https://ksndmc.karnataka.gov.in"
    },
    {
        "id": "faq_digi_148",
        "question": "ಡಿಜಿಲಾಕರ್ (DigiLocker) ನಲ್ಲಿ ಕರ್ನಾಟಕ SSLC, PUC ಅಂಕಪಟ್ಟಿ ಮತ್ತು ವಾಹನ ದಾಖಲೆಗಳನ್ನು ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "digilocker karnataka sslc puc marks card driving licence rc ಡಿಜಿಲಾಕರ್ ಅಂಕಪಟ್ಟಿ",
        "answer": """### 📱 ಡಿಜಿಲಾಕರ್ (DigiLocker) — ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಅಧಿಕೃತ ಡಿಜಿಟಲ್ ದಾಖಲೆಗಳು

ಭಾರತ ಸರ್ಕಾರದ ಡಿಜಿಟಲ್ ಇಂಡಿಯಾ ಉಪಕ್ರಮದಡಿ ಕರ್ನಾಟಕ ಶಾಲಾ ಪರೀಕ್ಷೆ ಮತ್ತು ಮೌಲ್ಯನಿರ್ಣಯ ಮಂಡಳಿ (KSEAB) ಹಾಗೂ ಸಾರಿಗೆ ಇಲಾಖೆಯ ದಾಖಲೆಗಳನ್ನು ಕಾನೂನುಬದ್ಧವಾಗಿ ಸಂಗ್ರಹಿಸಬಹುದು.

---

### 📜 ಲಭ್ಯವಿರುವ ಕರ್ನಾಟಕದ ಪ್ರಮುಖ ದಾಖಲೆಗಳು:
1. **SSLC (10th) & 2nd PUC ಅಂಕಪಟ್ಟಿಗಳು:** ನಿಮ್ಮ ನೋಂದಣಿ ಸಂಖ್ಯೆ (Register No) ಮತ್ತು ಉತ್ತೀರ್ಣರಾದ ವರ್ಷ ಹಾಕಿ ಡಿಜಿಟಲ್ ಸಹಿಯುಳ್ಳ ಅಂಕಪಟ್ಟಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.
2. **ಡ್ರೈವಿಂಗ್ ಲೈಸೆನ್ಸ್ (DL) & ವಾಹನ RC:** ಸಾರಿಗೆ ಇಲಾಖೆಯ ಅಧಿಕೃತ ಡಿಜಿಟಲ್ ದಾಖಲೆಗಳು (ಟ್ರಾಫಿಕ್ ಪೊಲೀಸರಿಗೆ ತೋರಿಸಲು ಸಂಪೂರ್ಣ ಮಾನ್ಯತೆ ಇದೆ).
3. **ರೇಷನ್ ಕಾರ್ಡ್ & ಜಾತಿ ಪ್ರಮಾಣಪತ್ರ:** ಆಹಾರ ಮತ್ತು ಕಂದಾಯ ಇಲಾಖೆಯ ಪ್ರಮಾಣಪತ್ರಗಳು.

🔗 **ವೆಬ್‌ಸೈಟ್:** [digilocker.gov.in](https://digilocker.gov.in) ಅಥವಾ ಮೊಬೈಲ್ ಆ್ಯಪ್ ಬಳಸಿ.""",
        "category": "EDUCATION",
        "language": "kn",
        "source_url": "https://digilocker.gov.in",
        "keywords": "digilocker karnataka, sslc marks card download, puc marks card, ಡಿಜಿಲಾಕರ್, ಅಂಕಪಟ್ಟಿ ಡೌನ್‌ಲೋಡ್",
        "action_label": "📱 ಡಿಜಿಲಾಕರ್ ಪೋರ್ಟಲ್",
        "action_url": "https://digilocker.gov.in"
    },
    {
        "id": "faq_devaraj_149",
        "question": "ಡಿ. ದೇವರಾಜ ಅರಸು ವಿದೇಶ ವ್ಯಾಸಂಗ ವಿದ್ಯಾರ್ಥಿವೇತನಕ್ಕೆ (Foreign Studies Scholarship) ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮಾನದಂಡಗಳೇನು?",
        "normalized_question": "devaraj urs foreign studies scholarship obc students devraj devraj urs ವಿದೇಶ ವ್ಯಾಸಂಗ ವಿದ್ಯಾರ್ಥಿವೇತನ",
        "answer": """### ✈️ ಡಿ. ದೇವರಾಜ ಅರಸು ವಿದೇಶ ವ್ಯಾಸಂಗ ವಿದ್ಯಾರ್ಥಿವೇತನ (D. Devaraj Urs Foreign Studies Scholarship)

ಹಿಂದುಳಿದ ವರ್ಗಗಳ ಕಲ್ಯಾಣ ಇಲಾಖೆಯ (BCWD) ವತಿಯಿಂದ ಜಾಗತಿಕ ಖ್ಯಾತಿಯ ವಿದೇಶಿ ವಿಶ್ವವಿದ್ಯಾಲಯಗಳಲ್ಲಿ ಉನ್ನತ ವ್ಯಾಸಂಗ (Master's, Ph.D, Post-Doctoral) ಮಾಡುವ ಹಿಂದುಳಿದ ವರ್ಗಗಳ ಪ್ರತಿಭಾವಂತ ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಆರ್ಥಿಕ ನೆರವು ನೀಡಲಾಗುತ್ತದೆ.

---

### 💰 ಆರ್ಥಿಕ ನೆರವಿನ ಮೊತ್ತ:
* ಗರಿಷ್ಠ **₹20 ಲಕ್ಷದವರೆಗೆ ಬಡ್ಡಿರಹಿತ ಆರ್ಥಿಕ ಅನುದಾನ (Grant-in-aid)** (ಕೋರ್ಸ್ ಶುಲ್ಕ, ವೀಸಾ, ವಿಮಾನ ಟಿಕೆಟ್ ಮತ್ತು ಜೀವನ ವೆಚ್ಚಕ್ಕಾಗಿ).

---

### 📌 ಅರ್ಹತೆಯ ಮಾನದಂಡಗಳು:
1. ವಿದ್ಯಾರ್ಥಿಯು ಹಿಂದುಳಿದ ವರ್ಗಗಳ ಪ್ರವರ್ಗ-1, 2A, 2B, 3A, 3B ಗೆ ಸೇರಿರಬೇಕು.
2. QS / Times Higher Education ಜಾಗತಿಕ ರ‍್ಯಾಂಕಿಂಗ್‌ನಲ್ಲಿ ಮೊದಲ 500 ರೊಳಗಿನ ವಿದೇಶಿ ವಿಶ್ವವಿದ್ಯಾಲಯದಲ್ಲಿ ಪ್ರವೇಶ (Offer of Admission) ಪಡೆದಿರಬೇಕು.
3. ಪದವಿಯಲ್ಲಿ ಕನಿಷ್ಠ 60% ಅಂಕಗಳನ್ನು ಹೊಂದಿರಬೇಕು.
4. ಕುಟುಂಬದ ಒಟ್ಟು ವಾರ್ಷಿಕ ಆದಾಯ ಮಿತಿ ₹8.00 ಲಕ್ಷ ಮೀರಿರಬಾರದು.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [bcwd.karnataka.gov.in](https://bcwd.karnataka.gov.in)""",
        "category": "EDUCATION",
        "language": "kn",
        "source_url": "https://bcwd.karnataka.gov.in",
        "keywords": "devaraj urs foreign scholarship, bcwd study abroad, obc master degree abroad, ದೇವರಾಜ ಅರಸು ವಿದೇಶ ವ್ಯಾಸಂಗ",
        "action_label": "✈️ BCWD ಪೋರ್ಟಲ್",
        "action_url": "https://bcwd.karnataka.gov.in"
    },
    {
        "id": "faq_mathru_150",
        "question": "ಮಾತೃಪೂರ್ಣ ಮತ್ತು ಪ್ರಧಾನಮಂತ್ರಿ ಮಾತೃ ವಂದನಾ (PMMVY) ಯೋಜನೆಯಡಿ ಗರ್ಭಿಣಿಯರಿಗೆ ಸಿಗುವ ಸೌಲಭ್ಯಗಳೇನು?",
        "normalized_question": "pmmvy mathru poorna pregnant women 5000 financial assistance ಮಾತೃಪೂರ್ಣ ಮಾತೃವಂದನಾ ಯೋಜನೆ",
        "answer": """### 🤱 ಮಾತೃಪೂರ್ಣ & ಪ್ರಧಾನಮಂತ್ರಿ ಮಾತೃ ವಂದನಾ ಯೋಜನೆ (PMMVY)

ತಾಯಿ ಮತ್ತು ನವಜಾತ ಶಿಶುವಿನ ಅಪೌಷ್ಟಿಕತೆ ಹೋಗಲಾಡಿಸಲು ಮಹಿಳಾ ಮತ್ತು ಮಕ್ಕಳ ಅಭಿವೃದ್ಧಿ ಇಲಾಖೆಯು ಜಾರಿಗೊಳಿಸಿರುವ ಪ್ರಮುಖ ಕಲ್ಯಾಣ ಯೋಜನೆಗಳು.

---

### 🍲 1. ಮಾತೃಪೂರ್ಣ ಯೋಜನೆ (Mathru Poorna):
* ಅಂಗನವಾಡಿ ಕೇಂದ್ರಗಳ ಮೂಲಕ ಗರ್ಭಿಣಿಯರು ಮತ್ತು ಬಾಣಂತಿಯರಿಗೆ ಪ್ರತಿದಿನ ಒಂದು ಪೌಷ್ಟಿಕ ಬಿಸಿಯೂಟ (ಅನ್ನ, ಸಾಂಬಾರು, ಮೊಟ್ಟೆ/ಹಾಲು, ತರಕಾರಿ, ಶೇಂಗಾ ಚಿಕ್ಕಿ ಮತ್ತು ಕಬ್ಬಿಣಾಂಶದ ಪೂರಕಗಳು) ಸಂಪೂರ್ಣ ಉಚಿತವಾಗಿ ನೀಡಲಾಗುತ್ತದೆ.

---

### 💰 2. ಪ್ರಧಾನಮಂತ್ರಿ ಮಾತೃ ವಂದನಾ ಯೋಜನೆ (PMMVY):
* ಮೊದಲ ಮಗುವಿನ ಜನನಕ್ಕೆ **₹5,000** ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT) 2 ಕಂತುಗಳಲ್ಲಿ ಜಮೆಯಾಗುತ್ತದೆ.
* ಎರಡನೇ ಮಗು ಹೆಣ್ಣು ಮಗುವಾದರೆ ಹೆಚ್ಚುವರಿಯಾಗಿ **₹6,000** ಏಕಗಂಟಿನ ಆರ್ಥಿಕ ನೆರವು ಸಿಗುತ್ತದೆ.

📝 ನೋಂದಣಿಗೆ ಸಮೀಪದ ಅಂಗನವಾಡಿ ಕಾರ್ಯಕರ್ತೆ ಅಥವಾ ಆಶಾ ಕಾರ್ಯಕರ್ತೆಯನ್ನು ಭೇಟಿ ಮಾಡಿ ತಾಯಿ ಕಾರ್ಡ್ (MCP Card) ಮತ್ತು ಆಧಾರ್ ವಿವರ ಸಲ್ಲಿಸಿ.""",
        "category": "HEALTH",
        "language": "kn",
        "source_url": "https://wcd.karnataka.gov.in",
        "keywords": "pmmvy karnataka, mathru poorna scheme, pregnant women 5000 dbt, ಮಾತೃಪೂರ್ಣ, ಮಾತೃವಂದನಾ, ಅಂಗನವಾಡಿ",
        "action_label": "🤱 ಮಹಿಳಾ & ಮಕ್ಕಳ ಕಲ್ಯಾಣ",
        "action_url": "https://wcd.karnataka.gov.in"
    }
]

# =========================================================================
# 11. EXPANSION BATCH 3: CIVIL REGISTRATION, CYBER SECURITY, HIGHER EDUCATION,
#     CROP INSURANCE & HOUSING BOARD SERVICES (151 - 166)
# =========================================================================

ADDITIONAL_EXPANSION_FAQS_BATCH_3 = [
    {
        "id": "faq_ejanma_151",
        "question": "ಇ-ಜನ್ಮ (e-JanMa) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಜನನ ಮತ್ತು ಮರಣ ಪ್ರಮಾಣಪತ್ರ (Birth & Death Certificate) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "ejanma karnataka birth certificate death certificate download verify ಇ-ಜನ್ಮ ಜನನ ಮರಣ ಪ್ರಮಾಣಪತ್ರ",
        "answer": """### 👶 ಇ-ಜನ್ಮ (e-JanMa) — ಜನನ ಮತ್ತು ಮರಣ ನೋಂದಣಿ ತಂತ್ರಾಂಶ

ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಅರ್ಥ ಮತ್ತು ಸಾಂಖ್ಯಿಕ ನಿರ್ದೇಶನಾಲಯವು ರಾಜ್ಯದ ಎಲ್ಲಾ ಆಸ್ಪತ್ರೆಗಳು, ಮಹಾನಗರ ಪಾಲಿಕೆಗಳು ಮತ್ತು ಗ್ರಾಮ ಪಂಚಾಯಿತಿಗಳ ಜನನ-ಮರಣ ನೋಂದಣಿಯನ್ನು **e-JanMa** ಮೂಲಕ ಡಿಜಿಟಲೀಕರಣಗೊಳಿಸಿದೆ.

---

### 🔍 ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಜನನ/ಮರಣ ಪ್ರಮಾಣಪತ್ರ ಪರಿಶೀಲಿಸುವ ವಿಧಾನ:
1. **ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [ejanma.karnataka.gov.in](https://ejanma.karnataka.gov.in)
2. **'Birth / Death Verification'** ಮೆನು ಆಯ್ಕೆಮಾಡಿ.
3. ಮಗು ಹುಟ್ಟಿದ / ವ್ಯಕ್ತಿ ಮೃತಪಟ್ಟ **ದಿನಾಂಕ (Date of Event)**, ಲಿಂಗ (Gender) ಮತ್ತು ತಾಯಿ/ತಂದೆಯ ಹೆಸರು ಅಥವಾ ನೋಂದಣಿ ಸಂಖ್ಯೆ (Registration No.) ನಮೂದಿಸಿ.
4. ಪರದೆಯ ಮೇಲೆ ನೋಂದಣಿ ವಿವರಗಳು ಮತ್ತು ಕಂದಾಯ ಇಲಾಖೆಯ ಅಧಿಕೃತ ಡಿಜಿಟಲ್ ರೆಕಾರ್ಡ್ ಕಾಣಿಸುತ್ತದೆ.

---

### 📋 ಪ್ರಮಾಣಪತ್ರ ಪಡೆಯುವ ಹಂತಗಳು:
* **ಆಸ್ಪತ್ರೆಯಲ್ಲಿ ಜನನವಾದರೆ:** ಆಸ್ಪತ್ರೆಯ ಅಧಿಕೃತ ನೋಂದಣಿ ಸಂಖ್ಯೆ (Registration Unit Number) ಪಡೆದು ಹತ್ತಿರದ ಕರ್ನಾಟಕ ಒನ್, ಬೆಂಗಳೂರು ಒನ್ ಅಥವಾ ಗ್ರಾಮ ಒನ್ ಕೇಂದ್ರಗಳಲ್ಲಿ ₹5 ಪಾವತಿಸಿ ಡಿಜಿಟಲ್ ಸಹಿಯುಳ್ಳ ಪ್ರಿಂಟ್ ಪಡೆಯಬಹುದು.
* **ಮನೆಯಲ್ಲಿ ಜನನ/ಮರಣವಾದರೆ:** 21 ದಿನಗಳ ಒಳಗಾಗಿ ಸ್ಥಳೀಯ ಗ್ರಾಮ ಆಡಳಿತಾಧಿಕಾರಿ (VA) ಅಥವಾ ಪುರಸಭೆ ಆರೋಗ್ಯಾಧಿಕಾರಿಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ನೋಂದಾಯಿಸಬೇಕು.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [ejanma.karnataka.gov.in](https://ejanma.karnataka.gov.in)""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://ejanma.karnataka.gov.in",
        "keywords": "ejanma, birth certificate download, death certificate karnataka, ಇ-ಜನ್ಮ, ಜನನ ಪ್ರಮಾಣಪತ್ರ, ಮರಣ ಪ್ರಮಾಣಪತ್ರ",
        "action_label": "👶 e-JanMa ಪೋರ್ಟಲ್",
        "action_url": "https://ejanma.karnataka.gov.in"
    },
    {
        "id": "faq_cyber_152",
        "question": "ಆನ್‌ಲೈನ್ ಹಣಕಾಸು ವಂಚನೆ ಅಥವಾ ಸೈಬರ್ ಅಪರಾಧವಾದರೆ 1930 ಸಹಾಯವಾಣಿಗೆ ದೂರು ನೀಡುವುದು ಹೇಗೆ?",
        "normalized_question": "cyber crime helpline 1930 financial fraud complaint portal ksp ಸೈಬರ್ ಕ್ರೈಮ್ ದೂರು ಹಣ ವಂಚನೆ",
        "answer": """### 🛡️ ಸೈಬರ್ ಅಪರಾಧ & ಆನ್‌ಲೈನ್ ಆರ್ಥಿಕ ವಂಚನೆ ತಡೆ ಸಹಾಯವಾಣಿ (1930)

UPI, ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್, ಬ್ಯಾಂಕ್ ಒಟಿಪಿ, ನಕಲಿ ಲಿಂಕ್ ಅಥವಾ ಡಿಜಿಟಲ್ ಅರೆಸ್ಟ್ ಹೆಸರಿನಲ್ಲಿ ಆನ್‌ಲೈನ್ ಹಣ ಕಳೆದುಕೊಂಡರೆ ತಕ್ಷಣ ಕ್ರಮ ಕೈಗೊಳ್ಳಲು ಕೇಂದ್ರ ಗೃಹ ಸಚಿವಾಲಯ ಹಾಗೂ ಕರ್ನಾಟಕ ಸಿಐಡಿ ಸೈಬರ್ ವಿಭಾಗವು **1930** ತುರ್ತು ಸಹಾಯವಾಣಿ ರೂಪಿಸಿದೆ.

---

### ⏱️ ಗೋಲ್ಡನ್ ಅವರ್ (Golden Hour) ಮಹತ್ವ:
* ವಂಚನೆ ನಡೆದ **ಮೊದಲ 1 ರಿಂದ 2 ಗಂಟೆಗಳ ಒಳಗಾಗಿ (Golden Hour)** 1930 ಗೆ ಕರೆ ಮಾಡಿದರೆ, ವಂಚಕರು ನಿಮ್ಮ ಹಣವನ್ನು ಬೇರೆ ಖಾತೆಗೆ ಅಥವಾ ಎಟಿಎಂ ಮೂಲಕ ಡ್ರಾ ಮಾಡದಂತೆ ಬ್ಯಾಂಕ್‌ಗಳ ಮೂಲಕ ತಕ್ಷಣ ಆ ಹಣವನ್ನು **ಹೋಲ್ಡ್ (Lien / Freeze)** ಮಾಡಲಾಗುತ್ತದೆ.

---

### 📋 ದೂರು ನೀಡುವ ವಿಧಾನ:
1. **ತುರ್ತು ಕರೆ:** ತಕ್ಷಣ **1930** ಸಂಖ್ಯೆಗೆ ಕರೆ ಮಾಡಿ ವಂಚನೆ ನಡೆದ ಬ್ಯಾಂಕ್ ಖಾತೆ, ಯುಪಿಐ ಐಡಿ (UPI ID), ಕಡಿತವಾದ ಮೊತ್ತ ಮತ್ತು ಬಂದಿರುವ SMS ಟ್ರಾನ್ಸಾಕ್ಷನ್ ರೆಫರೆನ್ಸ್ ನಂಬರ್ ನೀಡಿ.
2. **ಆನ್‌ಲೈನ್ ದೂರು ಸಲ್ಲಿಕೆ:** ಅಧಿಕೃತ ಪೋರ್ಟಲ್ [cybercrime.gov.in](https://cybercrime.gov.in) ನಲ್ಲಿ 24 ಗಂಟೆಯೊಳಗೆ ದೂರಿನ ಪೂರ್ಣ ವಿವರ ಮತ್ತು ಸ್ಕ್ರೀನ್‌ಶಾಟ್‌ಗಳನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ Acknowledgement ಸಂಖ್ಯೆ ಪಡೆಯಿರಿ.

💡 ಯಾವುದೇ ಕಾರಣಕ್ಕೂ ಅಪರಿಚಿತರಿಗೆ OTP, AnyDesk / TeamViewer ಆ್ಯಪ್ ಆಕ್ಸೆಸ್ ನೀಡಬೇಡಿ.""",
        "category": "POLICE",
        "language": "kn",
        "source_url": "https://cybercrime.gov.in",
        "keywords": "1930 cyber helpline, cyber crime complaint, financial fraud freeze money, ಸೈಬರ್ ವಂಚನೆ, 1930 ದೂರು",
        "action_label": "🛡️ ಸೈಬರ್ ಕ್ರೈಮ್ ಪೋರ್ಟಲ್",
        "action_url": "https://cybercrime.gov.in"
    },
    {
        "id": "faq_samrakshane_153",
        "question": "ಸಂರಕ್ಷಣೆ (Samrakshane) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಪ್ರಧಾನಮಂತ್ರಿ ಫಸಲ್ ಬಿಮಾ ಬೆಳೆ ವಿಮೆ ಸ್ಥಿತಿ ನೋಡುವುದು ಹೇಗೆ?",
        "normalized_question": "samrakshane crop insurance status pmfby karnataka ಬೆಳೆ ವಿಮೆ ಪರಿಹಾರ ಸಂರಕ್ಷಣೆ",
        "answer": """### 🌾 ಸಂರಕ್ಷಣೆ (Samrakshane) — ಕರ್ನಾಟಕ ಬೆಳೆ ವಿಮಾ ಪೋರ್ಟಲ್ (PMFBY)

ಪ್ರಕೃತಿ ವಿಕೋಪ, ಪ್ರವಾಹ, ಕೀಟಬಾಧೆ ಅಥವಾ ಬರಗಾಲದಿಂದ ಹಾನಿಗೊಳಗಾದ ಬೆಳೆಗಳಿಗೆ ಪ್ರಧಾನಮಂತ್ರಿ ಫಸಲ್ ಬಿಮಾ ಯೋಜನೆಯಡಿ ವಿಮಾ ಪರಿಹಾರವನ್ನು ನೇರವಾಗಿ ರೈತರ ಖಾತೆಗೆ ಜಮೆ ಮಾಡಲಾಗುತ್ತದೆ.

---

### 🔍 ಬೆಳೆ ವಿಮೆ ಸ್ಟೇಟಸ್ ಪರಿಶೀಲಿಸುವ ವಿಧಾನ:
1. [samrakshane.karnataka.gov.in](https://samrakshane.karnataka.gov.in) ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ.
2. ವರ್ಷ ಮತ್ತು ಋತು (Kharif / Rabi / Summer) ಆಯ್ಕೆಮಾಡಿ.
3. **'Check Status'** ವಿಭಾಗದಲ್ಲಿ ನಿಮ್ಮ **Proposal Number** ಅಥವಾ **ರೈತರ ಆಧಾರ್ ಸಂಖ್ಯೆ** ಅಥವಾ **FID ಸಂಖ್ಯೆ** ನಮೂದಿಸಿ.
4. ಬ್ಯಾಂಕ್‌ನಿಂದ ಪ್ರೀಮಿಯಂ ಡೆಬಿಟ್ ಆಗಿರುವ ವಿವರ, ವಿಮಾ ಕಂಪನಿಯ ಅನುಮೋದನೆ ಮತ್ತು ಪರಿಹಾರ ಮಂಜೂರಾದ ಮೊತ್ತದ ವಿವರಗಳು ಕಾಣಿಸುತ್ತವೆ.

---

### ⚠️ ಬೆಳೆ ಹಾನಿಯಾದಾಗ ದೂರು ನೀಡಲು:
ಸ್ಥಳೀಯ ಬೆಳೆ ಹಾನಿಯಾದರೆ (Localized Calamity) ಹಾನಿ ಸಂಭವಿಸಿದ **72 ಗಂಟೆಗಳ ಒಳಗಾಗಿ** 'Crop Insurance App' ಮೂಲಕ ಜಿಪಿಎಸ್ ಫೋಟೋ ಅಪ್‌ಲೋಡ್ ಮಾಡಬೇಕು ಅಥವಾ 1800-180-1551 ಟೋಲ್-ಫ್ರೀ ಸಂಖ್ಯೆಗೆ ಕರೆ ಮಾಡಬೇಕು.""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://samrakshane.karnataka.gov.in",
        "keywords": "samrakshane portal, pmfby karnataka, crop insurance status, ಸಂರಕ್ಷಣೆ, ಬೆಳೆ ವಿಮೆ ಪರಿಹಾರ",
        "action_label": "🌾 ಸಂರಕ್ಷಣೆ ಪೋರ್ಟಲ್",
        "action_url": "https://samrakshane.karnataka.gov.in"
    },
    {
        "id": "faq_kea_154",
        "question": "KEA (ಕರ್ನಾಟಕ ಪರೀಕ್ಷಾ ಪ್ರಾಧಿಕಾರ) CET ಕೌನ್ಸಿಲಿಂಗ್ ದಾಖಲೆ ಪರಿಶೀಲನೆಗೆ (Document Verification) ಯಾವ ದಾಖಲೆಗಳು ಬೇಕು?",
        "normalized_question": "kea cet document verification eligibility clause study certificate 7 years ಕೆಇಎ ದಾಖಲೆ ಪರಿಶೀಲನೆ",
        "answer": """### 🎓 KEA (Karnataka Examinations Authority) — KCET ದಾಖಲೆ ಪರಿಶೀಲನಾ ಮಾರ್ಗಸೂಚಿ

ಇಂಜಿನಿಯರಿಂಗ್, ವೈದ್ಯಕೀಯ (NEET), ಕೃಷಿ, ಪಶುವೈದ್ಯಕೀಯ ಮತ್ತು ವಾಸ್ತುಶಿಲ್ಪ ಸೀಟು ಹಂಚಿಕೆಗೆ ಕೆಇಎ ನಡೆಸುವ ದಾಖಲೆ ಪರಿಶೀಲನೆ ಕಡ್ಡಾಯ.

---

### 📋 ಪರಿಶೀಲನೆಗೆ ಕಡ್ಡಾಯವಾಗಿ ಬೇಕಾದ ಮೂಲ ದಾಖಲೆಗಳು (Originals + 2 ಸೆಟ್ ಜೆರಾಕ್ಸ್):
1. **KCET Application Form & Admission Ticket (Hall Ticket).**
2. **SSLC (10th) & 2nd PUC Marks Cards.**
3. **7 ವರ್ಷಗಳ ವ್ಯಾಸಂಗ ಪ್ರಮಾಣಪತ್ರ (Study Certificate):** ಕರ್ನಾಟಕದಲ್ಲಿ 1 ರಿಂದ 12 ನೇ ತರಗತಿವರೆಗೆ ಕನಿಷ್ಠ 7 ವರ್ಷ ಓದಿರುವುದಕ್ಕೆ ಕ್ಷೇತ್ರ ಶಿಕ್ಷಣಾಧಿಕಾರಿಗಳ (BEO / DDPU) ಮೇಲುಸಹಿ (Counter Signature) ಹೊಂದಿರಬೇಕು (ಕ್ಲಾಸ್-A ಅರ್ಹತೆಗೆ).
4. **ಗ್ರಾಮೀಣ ಮೀಸಲಾತಿ ಪ್ರಮಾಣಪತ್ರ (Rural Certificate):** 1 ರಿಂದ 10 ನೇ ತರಗತಿವರೆಗೆ ಗ್ರಾಮೀಣ ಪ್ರದೇಶದಲ್ಲಿ ಓದಿದ್ದರೆ (BEO ಸಹಿ ಕಡ್ಡಾಯ).
5. **ಕನ್ನಡ ಮಾಧ್ಯಮ ಪ್ರಮಾಣಪತ್ರ (Kannada Medium Certificate):** 1 ರಿಂದ 10 ನೇ ತರಗತಿವರೆಗೆ ಕನ್ನಡ ಮಾಧ್ಯಮದಲ್ಲಿ ವ್ಯಾಸಂಗ ಮಾಡಿದ್ದರೆ.
6. **ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ:** ಚಾಲ್ತಿಯಲ್ಲಿರುವ RD Number ಹೊಂದಿರುವ ತಹಶೀಲ್ದಾರ್ ಪ್ರಮಾಣಪತ್ರ.

ದಾಖಲೆ ಪರಿಶೀಲನೆ ಪೂರ್ಣಗೊಂಡ ನಂತರ ಕೆಇಎ **'Verification Slip'** ಮತ್ತು **'Secret Key'** ನೀಡುತ್ತದೆ. ಇದನ್ನು ಬಳಸಿಯೇ ಆಪ್ಷನ್ ಎಂಟ್ರಿ (Option Entry) ಮಾಡಬೇಕು.""",
        "category": "EDUCATION",
        "language": "kn",
        "source_url": "https://cetonline.karnataka.gov.in",
        "keywords": "kea cet verification, study certificate beo signature, secret key option entry, ಕೆಇಎ ದಾಖಲೆ ಪರಿಶೀಲನೆ",
        "action_label": "🎓 KEA ಅಧಿಕೃತ ಪೋರ್ಟಲ್",
        "action_url": "https://cetonline.karnataka.gov.in"
    },
    {
        "id": "faq_farmloan_155",
        "question": "ಸಹಕಾರಿ ಬ್ಯಾಂಕ್‌ಗಳಲ್ಲಿ ₹3 ಲಕ್ಷ ಮತ್ತು ₹5 ಲಕ್ಷ ಶೂನ್ಯ ಬಡ್ಡಿ ಕೃಷಿ ಸಾಲ (Zero Percent Interest Crop Loan) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "zero interest crop loan cooperative bank dcc bank karnataka ಶೂನ್ಯ ಬಡ್ಡಿ ಕೃಷಿ ಸಾಲ ಡಿಸಿಸಿ ಬ್ಯಾಂಕ್",
        "answer": """### 🌾 ಪ್ರಾಥಮಿಕ ಕೃಷಿ ಪತ್ತಿನ ಸಹಕಾರ ಸಂಘಗಳ (PACS / DCC Bank) ಶೂನ್ಯ ಬಡ್ಡಿ ಬೆಳೆ ಸಾಲ

ಕರ್ನಾಟಕ ಸರ್ಕಾರವು ರೈತರ ಕೃಷಿ ಚಟುವಟಿಕೆಗಳಿಗೆ ಉತ್ತೇಜನ ನೀಡಲು ಸಹಕಾರಿ ಬ್ಯಾಂಕ್‌ಗಳ ಮೂಲಕ ಶೂನ್ಯ ಬಡ್ಡಿದರದಲ್ಲಿ ಅಲ್ಪಾವಧಿ ಬೆಳೆ ಸಾಲ ಒದಗಿಸುತ್ತದೆ.

---

### 💰 ಸಾಲದ ಮಿತಿ & ಸಬ್ಸಿಡಿ ನಿಯಮಗಳು:
* **₹3.00 ಲಕ್ಷದವರೆಗೆ:** **0% ಬಡ್ಡಿದರ (ಸಂಪೂರ್ಣ ಶೂನ್ಯ ಬಡ್ಡಿ)** ಅಲ್ಪಾವಧಿ ಕೃಷಿ ಬೆಳೆ ಸಾಲ.
* **₹3.00 ಲಕ್ಷದಿಂದ ₹5.00 ಲಕ್ಷದವರೆಗೆ:** ಕೇವಲ **3% ರಿಯಾಯಿತಿ ಬಡ್ಡಿದರದಲ್ಲಿ** ಕೃಷಿ ಸಾಲ.
* **ಷರತ್ತು:** ಸಾಲ ಪಡೆದ ದಿನದಿಂದ **12 ತಿಂಗಳ (1 ವರ್ಷ) ಒಳಗಾಗಿ** ಸಾಲವನ್ನು ಮರುಪಾವತಿಸಿದರೆ ಮಾತ್ರ ಸರ್ಕಾರದ ಬಡ್ಡಿ ಸಹಾಯಧನ (Interest Subvention) ಅನ್ವಯವಾಗುತ್ತದೆ.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
1. ಪ್ರಸ್ತುತ ಸಾಲಿನ ಜಮೀನಿನ ಪಹಣಿ (RTC) ಮತ್ತು ಮ್ಯುಟೇಶನ್ ಪ್ರತಿ.
2. ರೈತರ **FRUITS FID ಕಾರ್ಡ್** ಮತ್ತು ಆಧಾರ್ ಕಾರ್ಡ್.
3. ಸ್ಥಳೀಯ ಪ್ರಾಥಮಿಕ ಕೃಷಿ ಪತ್ತಿನ ಸಹಕಾರ ಸಂಘದ (ಡಿಸಿಸಿ ಬ್ಯಾಂಕ್ ಶಾಖೆ) ಸದಸ್ಯತ್ವ ಷೇರು.

🔗 **ಅಧಿಕೃತ ಇಲಾಖೆ:** [sahakara.kar.gov.in](https://sahakara.kar.gov.in)""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://sahakara.kar.gov.in",
        "keywords": "zero percent farm loan, dcc bank crop loan, sahakara nigama, ಶೂನ್ಯ ಬಡ್ಡಿ ಸಾಲ, ಕೃಷಿ ಬೆಳೆ ಸಾಲ",
        "action_label": "🌾 ಸಹಕಾರ ಇಲಾಖೆ ವಿವರ",
        "action_url": "https://sahakara.kar.gov.in"
    },
    {
        "id": "faq_podi_156",
        "question": "ಪೋಡಿ ಮುಕ್ತ ಗ್ರಾಮ ಅಭಿಯಾನ (Podi Muktha Grama) ಮತ್ತು ತತ್ಕಾಲ್ ಪೋಡಿ (Tatkal Podi) ಅರ್ಜಿ ಸಲ್ಲಿಕೆ ಹೇಗೆ?",
        "normalized_question": "tatkal podi online mojini joint land survey separation ಪೋಡಿ ಮುಕ್ತ ಗ್ರಾಮ ತತ್ಕಾಲ್ ಪೋಡಿ",
        "answer": """### 📐 ಪೋಡಿ ಮುಕ್ತ ಗ್ರಾಮ & ತತ್ಕಾಲ್ ಪೋಡಿ (Land Parcel Division)

ಒಂದೇ ಸರ್ವೆ ನಂಬರ್‌ನಲ್ಲಿ ಜಂಟಿಯಾಗಿರುವ (Joint Ownership / Hissa) ಜಮೀನುಗಳನ್ನು ಪ್ರತ್ಯೇಕಿಸಿ, ಪ್ರತಿ ಮಾಲೀಕರಿಗೂ ಪ್ರತ್ಯೇಕ ಸರ್ವೆ ನಂಬರ್ ಮತ್ತು ಸ್ವತಂತ್ರ ಪಹಣಿ (Individual RTC) ನೀಡುವ ಪ್ರಕ್ರಿಯೆಯೇ **ಪೋಡಿ**.

---

### 🚀 ತತ್ಕಾಲ್ ಪೋಡಿ (Tatkal Podi) ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ವಿಧಾನ:
1. [mojini.karnataka.gov.in](https://mojini.karnataka.gov.in) ಅಥವಾ ಗ್ರಾಮ ಒನ್ ಕೇಂದ್ರಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಮೀನಿನ 11E ಸ್ಕೆಚ್, ಕ್ರಯಪತ್ರ/ವಿಭಾಗಪತ್ರ ಮತ್ತು ಮೂಲ ಪಹಣಿ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
3. ನಿಗದಿತ ಸರ್ಕಾರಿ ಸರ್ವೆ ಶುಲ್ಕವನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪಾವತಿಸಿ.
4. ಸರ್ಕಾರಿ ಭೂಮಾಪಕರು (Government Surveyor) ಸ್ಥಳಕ್ಕೆ ಭೇಟಿ ನೀಡಿ ಜಿಪಿಎಸ್ ಗಡಿ ಗುರುತಿಸಿ, ಹೊಸ ಹಿಸ್ಸಾ ನಂಬರ್ ನೀಡಿ ತಹಶೀಲ್ದಾರ್ ಅನುಮೋದನೆಗೆ ಕಳುಹಿಸುತ್ತಾರೆ.
5. ಪ್ರಕ್ರಿಯೆ ಮುಗಿದ ನಂತರ ಪ್ರತ್ಯೇಕ ಸ್ವತಂತ್ರ ಪಹಣಿ (RTC) ರಚನೆಯಾಗುತ್ತದೆ.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://mojini.karnataka.gov.in",
        "keywords": "tatkal podi, podi muktha grama, mojini land division, ಪೋಡಿ ಮುಕ್ತ ಗ್ರಾಮ, ತತ್ಕಾಲ್ ಪೋಡಿ, ಹಿಸ್ಸಾ",
        "action_label": "📐 ಮೋಜಿನಿ ಪೋರ್ಟಲ್",
        "action_url": "https://mojini.karnataka.gov.in"
    },
    {
        "id": "faq_khb_157",
        "question": "ಕರ್ನಾಟಕ ಗೃಹ ಮಂಡಳಿ (KHB) ಮತ್ತು BDA ನಿವೇಶನಗಳ ಇ-ಹರಾಜು (e-Auction) ಮತ್ತು ಆನ್‌ಲೈನ್ ಹಂಚಿಕೆ ಪ್ರಕ್ರಿಯೆ ಏನು?",
        "normalized_question": "khb karnataka housing board bda site allotment e auction online ಬಿಡಿಎ ನಿವೇಶನ ಹಂಚಿಕೆ",
        "answer": """### 🏢 ಕರ್ನಾಟಕ ಗೃಹ ಮಂಡಳಿ (KHB) & BDA ನಿವೇಶನ ಹಂಚಿಕೆ

ಬೆಂಗಳೂರು ಅಭಿವೃದ್ಧಿ ಪ್ರಾಧಿಕಾರ (BDA) ಮತ್ತು ಕರ್ನಾಟಕ ಗೃಹ ಮಂಡಳಿಯು (KHB) ರಾಜ್ಯದ ಪ್ರಮುಖ ನಗರಗಳಲ್ಲಿ ವಸತಿ ನಿವೇಶನಗಳು (Sites), ಮನೆಗಳು ಮತ್ತು ವಾಣಿಜ್ಯ ಮಳಿಗೆಗಳನ್ನು ಸಾರ್ವಜನಿಕರಿಗೆ ಹಂಚಿಕೆ ಮಾಡುತ್ತದೆ.

---

### 💻 ಇ-ಹರಾಜು (e-Auction) ನಲ್ಲಿ ಭಾಗವಹಿಸುವ ವಿಧಾನ:
1. **ಇ-ಪ್ರೊಕ್ಯೂರ್‌ಮೆಂಟ್ / ಹರಾಜು ಪೋರ್ಟಲ್:** [kppp.karnataka.gov.in](https://kppp.karnataka.gov.in) ಅಥವಾ [khb.karnataka.gov.in](https://khb.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ.
2. ಆಧಾರ್ ಇ-ಕೆವೈಸಿ ಮೂಲಕ ನೋಂದಾಯಿಸಿ ಬಯಸಿದ ಲೇಔಟ್‌ನ ನಿವೇಶನ ಸಂಖ್ಯೆ (Site / Plot No) ಆಯ್ಕೆಮಾಡಿ.
3. ಇಎಂಡಿ (Earnest Money Deposit - EMD) ಠೇವಣಿ ಮೊತ್ತವನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪಾವತಿಸಿ.
4. ಲೈವ್ ಬಿಡ್ಡಿಂಗ್ ದಿನದಂದು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಹೆಚ್ಚಿನ ಮೊತ್ತದ ಬಿಡ್ ಸಲ್ಲಿಸಿ.
5. ಅತಿ ಹೆಚ್ಚು ಮೊತ್ತ ನಮೂದಿಸಿದ ಬಿಡ್ಡರ್‌ಗೆ ಪ್ರಾಧಿಕಾರವು Allotment Letter ನೀಡುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://khb.karnataka.gov.in",
        "keywords": "khb site allotment, bda e auction, karnataka housing board, ಬಿಡಿಎ ಸೈಟು ಹಂಚಿಕೆ, ಕೆಹೆಚ್‌ಬಿ",
        "action_label": "🏢 KHB ಪೋರ್ಟಲ್",
        "action_url": "https://khb.karnataka.gov.in"
    },
    {
        "id": "faq_estamp_158",
        "question": "ಆನ್‌ಲೈನ್ ಇ-ಸ್ಟ್ಯಾಂಪ್ ಪೇಪರ್ (e-Stamp Paper) ಪಡೆಯುವುದು ಹೇಗೆ? ಸಿಂಧುತ್ವ ಪರಿಶೀಲನೆ ಹೇಗೆ?",
        "normalized_question": "e stamp paper online download stock holding karnataka validity ಇ-ಸ್ಟ್ಯಾಂಪ್ ಪೇಪರ್",
        "answer": """### 📜 ಇ-ಸ್ಟ್ಯಾಂಪ್ ಪೇಪರ್ (e-Stamp Paper) — ಸ್ಟಾಕ್ ಹೋಲ್ಡಿಂಗ್ (SHCIL) & ಕಾವೇರಿ 2.0

ಬಾಡಿಗೆ ಒಪ್ಪಂದ, ಅಫಿಡವಿಟ್, ಒಪ್ಪಂದ ಪತ್ರ ಮತ್ತು ಸಾಲದ ಪತ್ರಗಳಿಗೆ ಭೌತಿಕ ಸ್ಟ್ಯಾಂಪ್ ಪೇಪರ್ ಬದಲಿಗೆ ನಕಲು ಮಾಡಲಾಗದ ಭದ್ರತಾ ವೈಶಿಷ್ಟ್ಯವುಳ್ಳ ಡಿಜಿಟಲ್ ಇ-ಸ್ಟ್ಯಾಂಪ್ ಬಳಸಲಾಗುತ್ತದೆ.

---

### 💻 ಆನ್‌ಲೈನ್ ಇ-ಸ್ಟ್ಯಾಂಪ್ ಪಡೆಯುವ ವಿಧಾನ:
1. [shcilestamp.com](https://www.shcilestamp.com) ಅಥವಾ [kaveri.karnataka.gov.in](https://kaveri.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ.
2. ರಾಜ್ಯವನ್ನು **'Karnataka'** ಎಂದು ಆಯ್ಕೆಮಾಡಿ.
3. First Party (ನೀಡುವವರು) ಮತ್ತು Second Party (ಪಡೆಯುವವರು) ಹೆಸರು, ಮತ್ತು ಉದ್ದೇಶ (Description of Document) ನಮೂದಿಸಿ.
4. ನಿಗದಿತ ಮುದ್ರಾಂಕ ಶುಲ್ಕ (ಉದಾ: ₹20, ₹50, ₹100, ₹500) ಪಾವತಿಸಿ ಇ-ಸ್ಟ್ಯಾಂಪ್ ಸರ್ಟಿಫಿಕೇಟ್ ಪ್ರಿಂಟ್ ತೆಗೆದುಕೊಳ್ಳಿ.

---

### 🔍 ಇ-ಸ್ಟ್ಯಾಂಪ್ ಅಸಲಿಯುಕ್ತತೆ ಪರಿಶೀಲನೆ:
* ಪ್ರಮಾಣಪತ್ರದ ಮೇಲಿರುವ 16 ಅಂಕಿಗಳ **Certificate Number** ಅನ್ನು SHCIL ವೆಬ್‌ಸೈಟ್‌ನಲ್ಲಿ 'Verify e-Stamp' ಆಯ್ಕೆಯಲ್ಲಿ ಹಾಕಿ ಅಥವಾ ಕ್ಯೂಆರ್ ಕೋಡ್ ಸ್ಕ್ಯಾನ್ ಮಾಡಿ ಅದು ಅಸಲಿಯೇ ಅಥವಾ ನಕಲಿಯೇ ಎಂದು ತಿಳಿಯಬಹುದು.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://kaveri.karnataka.gov.in",
        "keywords": "e stamp paper, shcilestamp karnataka, verify estamp, ಇ-ಸ್ಟ್ಯಾಂಪ್ ಪೇಪರ್, ಬಾಡಿಗೆ ಒಪ್ಪಂದ ಸ್ಟ್ಯಾಂಪ್",
        "action_label": "📜 e-Stamp ಪೋರ್ಟಲ್",
        "action_url": "https://kaveri.karnataka.gov.in"
    },
    {
        "id": "faq_labourkit_159",
        "question": "ಕಟ್ಟಡ ಕಾರ್ಮಿಕರಿಗೆ ಉಚಿತ ಟೂಲ್‌ಕಿಟ್, ಬಸ್ ಪಾಸ್ ಮತ್ತು ಹೆರಿಗೆ ಧನಸಹಾಯ (KBOCWWB) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "karnataka labour board maternity benefit free bus pass tool kit ಲೇಬರ್ ಬೋರ್ಡ್ ಸೌಲಭ್ಯಗಳು",
        "answer": """### 👷 ಕರ್ನಾಟಕ ಕಟ್ಟಡ ಮತ್ತು ಇತರೆ ನಿರ್ಮಾಣ ಕಾರ್ಮಿಕರ ಕಲ್ಯಾಣ ಮಂಡಳಿ (KBOCWWB)

ನೋಂದಾಯಿತ ಕಟ್ಟಡ ಮತ್ತು ನಿರ್ಮಾಣ ಕಾರ್ಮಿಕರಿಗೆ ಹಾಗೂ ಅವರ ಕುಟುಂಬಕ್ಕೆ ಸಾಮಾಜಿಕ ಭದ್ರತಾ ಸೌಲಭ್ಯಗಳು ಲಭ್ಯವಿವೆ.

---

### 🛠️ ಪ್ರಮುಖ ಕಲ್ಯಾಣ ಸೌಲಭ್ಯಗಳು:
1. **ವೃತ್ತಿಪರ ಟೂಲ್‌ಕಿಟ್ (Free Tool Kit):** ಮೇಸ್ತ್ರಿ, ಪ್ಲಂಬರ್, ಎಲೆಕ್ಟ್ರಿಷಿಯನ್, ಬಡಗಿ, ಪೇಂಟರ್ ಮತ್ತು ಬಾರ್ ಬೆಂಡಿಂಗ್ ವೃತ್ತಿಯ ಕಾರ್ಮಿಕರಿಗೆ ಉಚಿತ ಸುಧಾರಿತ ಟೂಲ್‌ಕಿಟ್ ವಿತರಣೆ.
2. **ತಾಯಿ ಮಗು ಸಹಾಯಧನ (Maternity Assistance):** ಮಹಿಳಾ ಕಾರ್ಮಿಕರಿಗೆ ಹೆರಿಗೆ ಸಮಯದಲ್ಲಿ **₹30,000** ನೇರ ಆರ್ಥಿಕ ನೆರವು.
3. **ಉಚಿತ ಬಸ್ ಪಾಸ್:** ಕೆಲಸದ ಸ್ಥಳಕ್ಕೆ ಪ್ರಯಾಣಿಸಲು KSRTC / BMTC ವಾರ್ಷಿಕ ಉಚಿತ ಬಸ್ ಪಾಸ್.
4. **ವಿದ್ಯಾರ್ಥಿವೇತನ:** ಕಾರ್ಮಿಕರ ಮಕ್ಕಳಿಗೆ 1 ನೇ ತರಗತಿಯಿಂದ ಸ್ನಾತಕೋತ್ತರ/ಇಂಜಿನಿಯರಿಂಗ್/ವೈದ್ಯಕೀಯ ವ್ಯಾಸಂಗಕ್ಕೆ ₹2,000 ದಿಂದ ₹50,000 ವರೆಗೆ ಶೈಕ್ಷಣಿಕ ಧನಸಹಾಯ.

🔗 **ಅರ್ಜಿ ಸಲ್ಲಿಕೆ:** ಸೇವಾ ಸಿಂಧು ಅಥವಾ [kbocwwb.karnataka.gov.in](https://kbocwwb.karnataka.gov.in)""",
        "category": "LABOUR",
        "language": "kn",
        "source_url": "https://kbocwwb.karnataka.gov.in",
        "keywords": "karnataka labour board, construction worker benefits, maternity assistance, ಲೇಬರ್ ಕಾರ್ಡ್ ಟೂಲ್ ಕಿಟ್",
        "action_label": "👷 ಕಾರ್ಮಿಕ ಕಲ್ಯಾಣ ಪೋರ್ಟಲ್",
        "action_url": "https://kbocwwb.karnataka.gov.in"
    },
    {
        "id": "faq_elder_160",
        "question": "ಹಿರಿಯ ನಾಗರಿಕರ ಎಲ್ಡರ್‌ಲೈನ್ (Elderline 14567) ಸಹಾಯವಾಣಿ ಮತ್ತು ಸೌಲಭ್ಯಗಳೇನು?",
        "normalized_question": "elderline 14567 senior citizen helpline karnataka card ಹಿರಿಯ ನಾಗರಿಕರ ಸಹಾಯವಾಣಿ",
        "answer": """### 👵 ರಾಷ್ಟ್ರೀಯ ಹಿರಿಯ ನಾಗರಿಕರ ಸಹಾಯವಾಣಿ — ಎಲ್ಡರ್‌ಲೈನ್ (Elderline 14567)

60 ವರ್ಷ ಮತ್ತು ಅದಕ್ಕಿಂತ ಮೇಲ್ಪಟ್ಟ ಹಿರಿಯ ನಾಗರಿಕರ ರಕ್ಷಣೆ, ಕಾನೂನು ನೆರವು, ವೃದ್ಧಾಶ್ರಮ ಮಾಹಿತಿ ಮತ್ತು ಕೌಟುಂಬಿಕ ದೌರ್ಜನ್ಯ ತಡೆಯಲು ಮೀಸಲಾದ ಟೋಲ್-ಫ್ರೀ ಸಹಾಯವಾಣಿ.

---

### 📞 ಒದಗಿಸುವ ಸೇವೆಗಳು (ಟೋಲ್-ಫ್ರೀ: 14567):
* **ಕಾನೂನು ಸಲಹೆ:** ಮಕ್ಕಳಿಂದ ಆಸ್ತಿ ಕಸಿದುಕೊಂಡು ನಿರ್ಲಕ್ಷಿಸಿದರೆ *ಹಿರಿಯ ನಾಗರಿಕರ ಪೋಷಣೆ ಮತ್ತು ರಕ್ಷಣೆ ಕಾಯ್ದೆ-2007* ರ ಅಡಿಯಲ್ಲಿ ತಕ್ಷಣ ಆಸ್ತಿ ರದ್ದುಪಡಿಸಿ ವಾಪಸ್ ಕೊಡಿಸಲು ಸಹಾಯಕ ಆಯುಕ್ತರ (AC Court) ಮುಂದೆ ದೂರು ದಾಖಲಿಸಲು ನೆರವು.
* **ರಕ್ಷಣೆ & ಪುನರ್ವಸತಿ:** ರಸ್ತೆಯಲ್ಲಿ ಅನಾಥರಾಗಿರುವ ವೃದ್ಧರನ್ನು ರಕ್ಷಿಸಿ ಸರ್ಕಾರಿ ವೃದ್ಧಾಶ್ರಮಗಳಿಗೆ ಸೇರಿಸುವುದು.
* **ಮಾನಸಿಕ ಸಮಾಲೋಚನೆ:** ಒಂಟಿತನ ಮತ್ತು ಆತಂಕ ನಿವಾರಣೆಗೆ ಕೌನ್ಸಿಲಿಂಗ್.

💡 ಹಿರಿಯ ನಾಗರಿಕರ ಗುರುತಿನ ಚೀಟಿ (Senior Citizen ID Card) ಗಾಗಿ ಸೇವಾ ಸಿಂಧು ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು.""",
        "category": "WELFARE",
        "language": "kn",
        "source_url": "https://welfare.karnataka.gov.in",
        "keywords": "elderline 14567, senior citizen id card, maintenance act 2007, ಹಿರಿಯ ನಾಗರಿಕರ ಸಹಾಯವಾಣಿ, ಎಲ್ಡರ್ ಲೈನ್",
        "action_label": "👵 ಹಿರಿಯ ನಾಗರಿಕರ ಕಲ್ಯಾಣ",
        "action_url": "https://welfare.karnataka.gov.in"
    },
    {
        "id": "faq_svanidhi_161",
        "question": "ಬೀದಿ ಬದಿ ವ್ಯಾಪಾರಿಗಳಿಗೆ ಪಿಎಂ ಸ್ವನಿಧಿ (PM SVANidhi) ಯೋಜನೆಯಡಿ ₹10,000 ದಿಂದ ₹50,000 ಸಾಲ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "pm svanidhi street vendor loan karnataka bbmp subsidy ಬೀದಿ ಬದಿ ವ್ಯಾಪಾರಿ ಸಾಲ ಸ್ವನಿಧಿ",
        "answer": """### 🛒 ಪಿಎಂ ಸ್ವನಿಧಿ ಯೋಜನೆ (PM SVANidhi Scheme) — ಬೀದಿ ಬದಿ ವ್ಯಾಪಾರಿಗಳ ಸಾಲ ಸೌಲಭ್ಯ

ನಗರ ಮತ್ತು ಪಟ್ಟಣ ಪ್ರದೇಶಗಳ ಸಣ್ಣ ಬೀದಿ ಬದಿ ವ್ಯಾಪಾರಿಗಳಿಗೆ ಯಾವುದೇ ಶ್ಯೂರಿಟಿ ಇಲ್ಲದೆ ಕಡಿಮೆ ಬಡ್ಡಿದರದಲ್ಲಿ ಕಾರ್ಯನಿರತ ಬಂಡವಾಳ ಸಾಲ (Working Capital Loan) ನೀಡಲಾಗುತ್ತದೆ.

---

### 💰 3 ಹಂತಗಳ ಸಾಲದ ವಿವರ:
1. **ಮೊದಲ ಹಂತ:** **₹10,000** ಸಾಲ (1 ವರ್ಷದ ಮರುಪಾವತಿ ಅವಧಿ).
2. **ಎರಡನೇ ಹಂತ:** ಮೊದಲ ಸಾಲ ಸರಿಯಾಗಿ ತೀರಿಸಿದರೆ **₹20,000** ವರೆಗೆ ಸಾಲ.
3. **ಮೂರನೇ ಹಂತ:** ಎರಡನೇ ಸಾಲ ತೀರಿಸಿದ ನಂತರ **₹50,000** ಸಾಲ.

---

### 🌟 ಬಡ್ಡಿ ಸಬ್ಸಿಡಿ & ಕ್ಯಾಶ್‌ಬ್ಯಾಕ್:
* ಸಕಾಲದಲ್ಲಿ ಸಾಲ ಮರುಪಾವತಿಸಿದರೆ **7% ವಾರ್ಷಿಕ ಬಡ್ಡಿ ಸಹಾಯಧನ (Interest Subsidy)** ನೇರವಾಗಿ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ.
* ಡಿಜಿಟಲ್ ವ್ಯಾಪಾರ (QR Code ಪಾವತಿ) ಮಾಡಿದರೆ ವರ್ಷಕ್ಕೆ ಗರಿಷ್ಠ ₹1,200 ವರೆಗೆ ಕ್ಯಾಶ್‌ಬ್ಯಾಕ್ ಸಿಗುತ್ತದೆ.

📝 **ಅರ್ಜಿ ಸಲ್ಲಿಕೆ:** ನಗರ ಸ್ಥಳೀಯ ಸಂಸ್ಥೆ (ULB/BBMP) ನೀಡಿದ Vendor ID Card ನೊಂದಿಗೆ [pmsvanidhi.mohua.gov.in](https://pmsvanidhi.mohua.gov.in) ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.""",
        "category": "WELFARE",
        "language": "kn",
        "source_url": "https://pmsvanidhi.mohua.gov.in",
        "keywords": "pm svanidhi karnataka, street vendor loan, bbmp vendor card, ಪಿಎಂ ಸ್ವನಿಧಿ ಸಾಲ, ಬೀದಿ ಬದಿ ವ್ಯಾಪಾರಿ",
        "action_label": "🛒 PM SVANidhi ಪೋರ್ಟಲ್",
        "action_url": "https://pmsvanidhi.mohua.gov.in"
    },
    {
        "id": "faq_tree_162",
        "question": "ಸ್ವಂತ ಜಮೀನಿನಲ್ಲಿ ಒಣಗಿದ ಅಥವಾ ಅಪಾಯಕಾರಿ ಮರ ಕಡಿಯಲು ಅರಣ್ಯ ಇಲಾಖೆ (Forest Dept) ಅನುಮತಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "tree felling permission online karnataka forest department ಮರ ಕಡಿಯಲು ಅನುಮತಿ ಅರಣ್ಯ ಇಲಾಖೆ",
        "answer": """### 🌳 ಮರ ಕಡಿಯುವ ಆನ್‌ಲೈನ್ ಪರವಾನಗಿ (Tree Felling Permission)

ಕರ್ನಾಟಕ ಮರ ಸಂರಕ್ಷಣಾ ಕಾಯ್ದೆಯನ್ವಯ (Karnataka Preservation of Trees Act) ಸ್ವಂತ ಜಮೀನು, ಮನೆ ಆವರಣ ಅಥವಾ ಕಾಫಿ ಎಸ್ಟೇಟ್‌ಗಳಲ್ಲಿರುವ ಮರಗಳನ್ನು ಕಡಿಯಲು ಅರಣ್ಯ ಇಲಾಖೆಯ ಪೂರ್ವಾನುಮತಿ ಕಡ್ಡಾಯ.

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಪ್ರಕ್ರಿಯೆ:
1. [aranya.karnataka.gov.in](https://aranya.karnataka.gov.in) ಅಥವಾ **Seva Sindhu** ಗೆ ಭೇಟಿ ನೀಡಿ.
2. **'Tree Felling Permission'** ಆಯ್ಕೆಮಾಡಿ.
3. ಜಮೀನಿನ ಪಹಣಿ (RTC), ವಿಳಾಸದ ಪುರಾವೆ ಹಾಗೂ ಕಡಿಯಬೇಕಾದ ಮರದ ಜಾತಿ, ಸುತ್ತಳತೆ ಮತ್ತು ಕಾರಣವನ್ನು (ಮನೆ ನಿರ್ಮಾಣ/ಅಪಾಯಕಾರಿ ಮರ) ನಮೂದಿಸಿ.
4. ಮರದ ಫೋಟೋ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.
5. ಉಪ ಅರಣ್ಯ ಸಂರಕ್ಷಣಾಧಿಕಾರಿ (DCF) ಅಥವಾ ವಲಯ ಅರಣ್ಯಾಧಿಕಾರಿ (RFO) ಸ್ಥಳ ಪರಿಶೀಲನೆ ನಡೆಸಿ 30 ದಿನಗಳೊಳಗೆ ಅಧಿಕೃತ ಕಡಿಯುವ ಆದೇಶ ಮತ್ತು ಟ್ರಾನ್ಸಿಟ್ ಪಾಸ್ (Transit Permit) ನೀಡುತ್ತಾರೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://aranya.karnataka.gov.in",
        "keywords": "tree felling permission, karnataka forest rfo, timber transit permit, ಮರ ಕಡಿಯಲು ಅನುಮತಿ, ಅರಣ್ಯ ಇಲಾಖೆ",
        "action_label": "🌳 ಅರಣ್ಯ ಇಲಾಖೆ ಪೋರ್ಟಲ್",
        "action_url": "https://aranya.karnataka.gov.in"
    },
    {
        "id": "faq_msme_163",
        "question": "ಕರ್ನಾಟಕ ಸಿಂಗಲ್ ವಿಂಡೋ (K-Swagath) ನಲ್ಲಿ ಹೊಸ ಕೈಗಾರಿಕೆ/ಉದ್ಯಮ ಸ್ಥಾಪನೆಗೆ ಅನುಮೋದನೆ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "k swagath karnataka single window clearance invest karnataka msme ಕೆ-ಸ್ವಾಗತ್ ಏಕಗವಾಕ್ಷಿ ಕೈಗಾರಿಕೆ",
        "answer": """### 🏭 ಕೆ-ಸ್ವಾಗತ್ (K-Swagath) — ಏಕಗವಾಕ್ಷಿ ಕೈಗಾರಿಕಾ ಅನುಮೋದನಾ ಪೋರ್ಟಲ್

ರಾಜ್ಯದಲ್ಲಿ ಸೂಕ್ಷ್ಮ, ಸಣ್ಣ, ಮಧ್ಯಮ ಮತ್ತು ಬೃಹತ್ ಕೈಗಾರಿಕೆಗಳನ್ನು ಸ್ಥಾಪಿಸಲು ವಿವಿಧ ಇಲಾಖೆಗಳ (KIADB, KSPCB, BESCOM, Fire Dept, Urban Planning) 40 ಕ್ಕೂ ಹೆಚ್ಚು ಪರವಾನಗಿಗಳನ್ನು ಒಂದೇ ಅರ್ಜಿಯ ಮೂಲಕ ನೀಡುವ ವ್ಯವಸ್ಥೆ.

---

### 🌟 ಪ್ರಮುಖ ಸೌಲಭ್ಯಗಳು:
* **ಸಂಯುಕ್ತ ಅರ್ಜಿ ನಮೂನೆ (CAF - Combined Application Form):** ಪ್ರತ್ಯೇಕ ಕಚೇರಿಗಳಿಗೆ ಅಲೆಯದೆ ಒಂದೇ ಅರ್ಜಿಯಲ್ಲಿ ಎಲ್ಲಾ ಇಲಾಖಾ ನಿರಾಕ್ಷೇಪಣಾ ಪತ್ರಗಳಿಗೆ (NOC) ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು.
* **ಕಾಲಮಿತಿ ಅನುಮೋದನೆ:** ನಿಗದಿತ ದಿನಗಳಲ್ಲಿ (15 ರಿಂದ 30 ದಿನಗಳು) ಅನುಮೋದನೆ ಸಿಗದಿದ್ದರೆ ಅದನ್ನು 'ಡೀಮ್ಡ್ ಅಪ್ರೂವಲ್ (Deemed Approval)' ಎಂದು ಪರಿಗಣಿಸಲಾಗುತ್ತದೆ.
* **ಕೈಗಾರಿಕಾ ಸಬ್ಸಿಡಿ:** ವಿದ್ಯುತ್ ತೆರಿಗೆ ವಿನಾಯಿತಿ, ಸ್ಟ್ಯಾಂಪ್ ಡ್ಯೂಟಿ ವಿನಾಯಿತಿ ಮತ್ತು ಬಂಡವಾಳ ಹೂಡಿಕೆ ಸಹಾಯಧನ ಪಡೆಯಲು ನೆರವು.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [ebiz.karnataka.gov.in](https://ebiz.karnataka.gov.in) | [investkarnataka.co.in](https://investkarnataka.co.in)""",
        "category": "INDUSTRY",
        "language": "kn",
        "source_url": "https://investkarnataka.co.in",
        "keywords": "k swagath, invest karnataka single window, kiadb allotment, ಕೈಗಾರಿಕಾ ಏಕಗವಾಕ್ಷಿ, ಉದ್ಯಮ ಸ್ಥಾಪನೆ",
        "action_label": "🏭 ಕೆ-ಸ್ವಾಗತ್ ಪೋರ್ಟಲ್",
        "action_url": "https://investkarnataka.co.in"
    },
    {
        "id": "faq_bhagya_164",
        "question": "ಭಾಗ್ಯಲಕ್ಷ್ಮಿ ಯೋಜನೆ (Bhagyalakshmi Scheme) ಯ ಮುಕ್ತಾಯ ಹಣ (Maturity Amount) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "bhagyalakshmi scheme maturity bond sukanya samriddhi wcd karnataka ಭಾಗ್ಯಲಕ್ಷ್ಮಿ ಯೋಜನೆ ಬಾಂಡ್",
        "answer": """### 🌸 ಭಾಗ್ಯಲಕ್ಷ್ಮಿ ಯೋಜನೆ — ಹೆಣ್ಣು ಮಕ್ಕಳ ಆರ್ಥಿಕ ಭದ್ರತೆ

ಬಿಪಿಎಲ್ ಕುಟುಂಬಗಳಲ್ಲಿ ಜನಿಸಿದ ಹೆಣ್ಣು ಮಕ್ಕಳ ಭವಿಷ್ಯ, ಶಿಕ್ಷಣ ಮತ್ತು ಬಾಲ್ಯವಿವಾಹ ತಡೆಗಟ್ಟಲು ಸರ್ಕಾರ ನೀಡುವ ಬಾಂಡ್ ಭದ್ರತಾ ಯೋಜನೆ.

---

### 💰 ಮೆಚ್ಯೂರಿಟಿ ನಿಯಮಗಳು & ಹಣ ವಿತರಣೆ:
* ಹೆಣ್ಣು ಮಗುವಿಗೆ **18 ವರ್ಷ ತುಂಬಿದ ನಂತರ** ಹಾಗೂ ಆಕೆ 10 ನೇ ತರಗತಿ ಉತ್ತೀರ್ಣಳಾಗಿರಬೇಕು ಮತ್ತು 18 ವರ್ಷದವರೆಗೆ ಅವಿವಾಹಿತಳಾಗಿರಬೇಕು.
* ಮೆಚ್ಯೂರಿಟಿ ಅವಧಿ ಪೂರ್ಣಗೊಂಡಾಗ ಎಲ್‌ಐಸಿ (LIC) / ಅಂಚೆ ಇಲಾಖೆಯಿಂದ ಮುಕ್ತಾಯ ಮೊತ್ತವು ಫಲಾನುಭವಿ ಹೆಣ್ಣು ಮಗಳ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
1. ಮೂಲ ಭಾಗ್ಯಲಕ್ಷ್ಮಿ ಬಾಂಡ್ ಪ್ರಮಾಣಪತ್ರ (Original Bond Certificate).
2. ಹೆಣ್ಣು ಮಗಳ 10th Marks Card ಮತ್ತು ಆಧಾರ್ ಕಾರ್ಡ್.
3. ಹೆಣ್ಣು ಮಗಳ ಸ್ವಂತ ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ಪ್ರತಿ.
4. ಅವಿವಾಹಿತ ದೃಢೀಕರಣ ಪತ್ರ.
ಅರ್ಜಿಯನ್ನು ಸ್ಥಳೀಯ ಅಂಗನವಾಡಿ ಕಾರ್ಯಕರ್ತೆ ಅಥವಾ ತಾಲೂಕು ಸಿಡಿಪಿಒ (CDPO) ಕಚೇರಿಗೆ ಸಲ್ಲಿಸಬೇಕು.""",
        "category": "WELFARE",
        "language": "kn",
        "source_url": "https://wcd.karnataka.gov.in",
        "keywords": "bhagyalakshmi scheme, maturity bond claim, sukanya samriddhi, ಭಾಗ್ಯಲಕ್ಷ್ಮಿ ಬಾಂಡ್ ಹಣ, ಸಿಡಿಪಿಒ",
        "action_label": "🌸 ಮಹಿಳಾ & ಮಕ್ಕಳ ಅಭಿವೃದ್ಧಿ",
        "action_url": "https://wcd.karnataka.gov.in"
    },
    {
        "id": "faq_poll_165",
        "question": "ಕರ್ನಾಟಕ ರಾಜ್ಯ ಮಾಲಿನ್ಯ ನಿಯಂತ್ರಣ ಮಂಡಳಿ (KSPCB) ಯಿಂದ CTE ಮತ್ತು CTO ಪರವಾನಗಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "kspcb consent to establish cte consent to operate cto karnataka ಮಾಲಿನ್ಯ ನಿಯಂತ್ರಣ ಮಂಡಳಿ",
        "answer": """### 🏭 KSPCB (Karnataka State Pollution Control Board) ಅನುಮತಿಗಳು

ಕಾರ್ಖಾನೆ, ಹೋಟೆಲ್, ಆಸ್ಪತ್ರೆ, ವಸತಿ ಸಮುಚ್ಚಯ ಅಥವಾ ಗಣಿಗಾರಿಕೆ ಪ್ರಾರಂಭಿಸುವ ಮುನ್ನ ಪರಿಸರ ಮಾಲಿನ್ಯ ನಿಯಂತ್ರಣ ಕಾಯ್ದೆಯನ್ವಯ ಮಂಡಳಿಯ ಒಪ್ಪಿಗೆ ಪಡೆಯುವುದು ಕಾನೂನುಬದ್ಧವಾಗಿ ಕಡ್ಡಾಯ.

---

### 📜 2 ಹಂತಗಳ ಅನುಮೋದನೆ:
1. **Consent to Establish (CTE):** ಪ್ರಾಜೆಕ್ಟ್ ಕಾಮಗಾರಿ ಅಥವಾ ಕಟ್ಟಡ ನಿರ್ಮಾಣ ಪ್ರಾರಂಭಿಸುವ ಮುನ್ನ ಪಡೆಯುವ ಅನುಮೋದನೆ.
2. **Consent to Operate (CTO):** ಘಟಕದ ನಿರ್ಮಾಣ ಪೂರ್ಣಗೊಂಡು ಉತ್ಪಾದನೆ ಅಥವಾ ಕಾರ್ಯಾಚರಣೆ ಆರಂಭಿಸುವ ಮುನ್ನ ಪಡೆಯುವ ಅಂತಿಮ ಲೈಸೆನ್ಸ್.

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ (XGN Portal):
* [kspcb.karnataka.gov.in](https://kspcb.karnataka.gov.in) ನಲ್ಲಿರುವ **XGN (Extended Green Node)** ವ್ಯವಸ್ಥೆಯ ಮೂಲಕ ಆನ್‌ಲೈನ್‌ನಲ್ಲೇ ತ್ಯಾಜ್ಯ ನೀರು ಸಂಸ್ಕರಣಾ ಘಟಕ (STP/ETP), ಗಾಳಿಯ ಮಾಲಿನ್ಯ ನಿಯಂತ್ರಣ ಉಪಕರಣಗಳ ನಕ್ಷೆ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ನಿಗದಿತ ಶುಲ್ಕ ಪಾವತಿಸಿ ಡಿಜಿಟಲ್ ಪ್ರಮಾಣಪತ್ರ ಪಡೆಯಬಹುದು.""",
        "category": "INDUSTRY",
        "language": "kn",
        "source_url": "https://kspcb.karnataka.gov.in",
        "keywords": "kspcb cte cto, pollution control consent, xgn portal, ಮಾಲಿನ್ಯ ನಿಯಂತ್ರಣ ಮಂಡಳಿ, ಸಿಟಿಒ",
        "action_label": "🏭 KSPCB ಪೋರ್ಟಲ್",
        "action_url": "https://kspcb.karnataka.gov.in"
    },
    {
        "id": "faq_brahmin_166",
        "question": "ಕರ್ನಾಟಕ ಬ್ರಾಹ್ಮಣ ಅಭಿವೃದ್ಧಿ ಮಂಡಳಿಯ (KSBDB) ಅರುಂಧತಿ, ಮೈತ್ರೇಯಿ ಮತ್ತು ವಸಿಷ್ಠ ಸಾಲ ಯೋಜನೆಗಳು ಯಾವುವು?",
        "normalized_question": "brahmin development board arundhati maitreyi vasistha scheme ksbdb ಬ್ರಾಹ್ಮಣ ಅಭಿವೃದ್ಧಿ ಮಂಡಳಿ",
        "answer": """### 🏛️ ಕರ್ನಾಟಕ ರಾಜ್ಯ ಬ್ರಾಹ್ಮಣ ಅಭಿವೃದ್ಧಿ ಮಂಡಳಿ (KSBDB) ಕಲ್ಯಾಣ ಯೋಜನೆಗಳು

ಆರ್ಥಿಕವಾಗಿ ಹಿಂದುಳಿದ ಬ್ರಾಹ್ಮಣ ಸಮುದಾಯದ (EWS) ಬಡ ಕುಟುಂಬಗಳಿಗೆ ವಿವಿಧ ಆರ್ಥಿಕ ಸೌಲಭ್ಯಗಳನ್ನು ಒದಗಿಸಲಾಗುತ್ತದೆ.

---

### 🌟 ಪ್ರಮುಖ ಯೋಜನೆಗಳ ವಿವರ:
1. **ಅರುಂಧತಿ ಯೋಜನೆ (Arundhati Scheme):** ಆರ್ಥಿಕವಾಗಿ ಹಿಂದುಳಿದ ಅರ್ಚಕರು ಮತ್ತು ಬಡ ಅರ್ಹ ಬ್ರಾಹ್ಮಣ ವಧುವಿನ ವಿವಾಹಕ್ಕೆ **₹25,000** ಆರ್ಥಿಕ ಸಹಾಯಧನ.
2. **ಮೈತ್ರೇಯಿ ಯೋಜನೆ (Maitreyi Scheme):** ಆರ್ಥಿಕವಾಗಿ ಹಿಂದುಳಿದ ಬ್ರಾಹ್ಮಣ ಅರ್ಚಕರು/ಪುರೋಹಿತರನ್ನು ವಿವಾಹವಾಗುವ ಯುವತಿಯರ ಹೆಸರಿನಲ್ಲಿ **₹3.00 ಲಕ್ಷ ಠೇವಣಿ (Bond)** ಬಾಂಡ್ ಸೌಲಭ್ಯ.
3. **ವಸಿಷ್ಠ ಸ್ವಯಂ ಉದ್ಯೋಗ ಯೋಜನೆ:** ಸಣ್ಣ ವ್ಯಾಪಾರ, ಕೃಷಿ ಪೂರಕ ಉದ್ದೇಶಗಳಿಗೆ ಗರಿಷ್ಠ ₹2 ಲಕ್ಷದವರೆಗೆ (20% ಸಬ್ಸಿಡಿ ಹಾಗೂ 4% ಬಡ್ಡಿದರದಲ್ಲಿ) ಸಾಲ ಸೌಲಭ್ಯ.
4. **ಸಾಂದೀಪನಿ ಶಿಷ್ಯವೇತನ:** ಪಿಯುಸಿ, ಪದವಿ ಹಾಗೂ ಸ್ನಾತಕೋತ್ತರ ಬಡ ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ವಾರ್ಷಿಕ ವಿದ್ಯಾರ್ಥಿವೇತನ.

🔗 **ಅರ್ಜಿ ಸಲ್ಲಿಕೆ:** [ksbdb.karnataka.gov.in](https://ksbdb.karnataka.gov.in)""",
        "category": "WELFARE",
        "language": "kn",
        "source_url": "https://ksbdb.karnataka.gov.in",
        "keywords": "ksbdb schemes, arundhati maitreyi scheme, brahmin development board, ಬ್ರಾಹ್ಮಣ ಅಭಿವೃದ್ಧಿ ಮಂಡಳಿ, ಅರುಂಧತಿ ಯೋಜನೆ",
        "action_label": "🏛️ KSBDB ಪೋರ್ಟಲ್",
        "action_url": "https://ksbdb.karnataka.gov.in"
    }
]

# =========================================================================
# 12. EXPANSION BATCH 4: REVENUE COURTS, RTI, TRANSPORT (HSRP),
#     DBT TROUBLESHOOTING, E-COURTS & ALLIED AGRICULTURE (167 - 184)
# =========================================================================

ADDITIONAL_EXPANSION_FAQS_BATCH_4 = [
    {
        "id": "faq_rccms_167",
        "question": "ಆರ್‌ಸಿಸಿಎಂಎಸ್ (RCCMS) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ತಹಶೀಲ್ದಾರ್/ಡಿಸಿ ಕಂದಾಯ ನ್ಯಾಯಾಲಯ ಕೇಸ್ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "rccms karnataka revenue court case monitoring system order copy ಆರ್‌ಸಿಸಿಎಂಎಸ್ ಕಂದಾಯ ಕೇಸ್",
        "answer": """### ⚖️ ಆರ್‌ಸಿಸಿಎಂಎಸ್ (Revenue Court Case Monitoring System - RCCMS)

ಕರ್ನಾಟಕದ ತಹಶೀಲ್ದಾರ್ (Tahsildar), ಸಹಾಯಕ ಆಯುಕ್ತರು (AC) ಮತ್ತು ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ (DC) ಕಂದಾಯ ನ್ಯಾಯಾಲಯಗಳಲ್ಲಿ ದಾಖಲಾಗಿರುವ ಭೂ ವಿವಾದ, ಖಾತೆ ತಕರಾರು ಮತ್ತು ಪಹಣಿ ತಿದ್ದುಪಡಿ ಕೇಸ್‌ಗಳನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಟ್ರ್ಯಾಕ್ ಮಾಡುವ ತಂತ್ರಾಂಶ.

---

### 🔍 ಕಂದಾಯ ಕೋರ್ಟ್ ಕೇಸ್ ಮತ್ತು ಆದೇಶ ಪ್ರತಿ (Order Copy) ಪಡೆಯುವ ವಿಧಾನ:
1. **ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [rccms.karnataka.gov.in](https://rccms.karnataka.gov.in)
2. **'Case Status' (ಪ್ರಕರಣದ ಸ್ಥಿತಿ)** ಮೆನು ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ **ಜಿಲ್ಲೆ, ತಾಲೂಕು, ನ್ಯಾಯಾಲಯದ ವಿಧ (DC / AC / Tahsildar Court)** ಆಯ್ಕೆಮಾಡಿ.
4. **ಪ್ರಕರಣ ಸಂಖ್ಯೆ (Case Number)** ಅಥವಾ ಜಮೀನಿನ **ಸರ್ವೆ ಸಂಖ್ಯೆ (Survey Number)** ಅಥವಾ ಪಕ್ಷಗಾರರ ಹೆಸರು (Party Name) ನಮೂದಿಸಿ.
5. ವಿಚಾರಣೆಯ ಮುಂದಿನ ದಿನಾಂಕ (Next Hearing Date), ನಡಾವಳಿಗಳು (Proceedings) ಮತ್ತು ಅಂತಿಮ ತೀರ್ಪಿನ ಆದೇಶ ಪ್ರತಿ (Judgment Copy PDF) ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.

💡 ಯಾವುದೇ ಕೃಷಿ ಜಮೀನು ಖರೀದಿಸುವ ಮುನ್ನ ಆ ಸರ್ವೆ ನಂಬರ್ ಮೇಲೆ ಕಂದಾಯ ಕೋರ್ಟ್‌ನಲ್ಲಿ ತಡೆಯಾಜ್ಞೆ (Stay Order) ಅಥವಾ ಕೇಸ್ ಬಾಕಿ ಇದೆಯೇ ಎಂದು ಪರೀಕ್ಷಿಸಲು RCCMS ಅತ್ಯಗತ್ಯ.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://rccms.karnataka.gov.in",
        "keywords": "rccms karnataka, revenue court case status, dc ac court order copy, ಕಂದಾಯ ನ್ಯಾಯಾಲಯ, ಆರ್‌ಸಿಸಿಎಂಎಸ್, ಸರ್ವೆ ನಂಬರ್ ಕೇಸ್",
        "action_label": "⚖️ RCCMS ಪೋರ್ಟಲ್",
        "action_url": "https://rccms.karnataka.gov.in"
    },
    {
        "id": "faq_rti_168",
        "question": "ಆನ್‌ಲೈನ್ ಮಾಹಿತಿ ಹಕ್ಕು ಕಾಯ್ದೆ (RTI Online Karnataka) ಮೂಲಕ ಸರ್ಕಾರಿ ದಾಖಲೆ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "rti online karnataka portal apply first appeal mahithi hakku ಮಾಹಿತಿ ಹಕ್ಕು ಆನ್‌ಲೈನ್ ಅರ್ಜಿ",
        "answer": """### 📑 ಕರ್ನಾಟಕ ಆನ್‌ಲೈನ್ ಮಾಹಿತಿ ಹಕ್ಕು (RTI Online Karnataka)

ಮಾಹಿತಿ ಹಕ್ಕು ಅಧಿನಿಯಮ 2005 ರ ಅಡಿಯಲ್ಲಿ ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಯಾವುದೇ ಇಲಾಖೆ, ನಿಗಮ, ಮಂಡಳಿ ಅಥವಾ ಪ್ರಾಧಿಕಾರಗಳಿಂದ ಸಾರ್ವಜನಿಕ ದಾಖಲೆ ಮತ್ತು ಮಾಹಿತಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲೇ ಪಡೆಯಬಹುದು.

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಕೆಯ ಹಂತಗಳು:
1. **ಆರ್‌ಟಿಐ ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [rtionline.karnataka.gov.in](https://rtionline.karnataka.gov.in)
2. **'Submit Request'** ಕ್ಲಿಕ್ ಮಾಡಿ ನಿಬಂಧನೆಗಳನ್ನು ಒಪ್ಪಿಕೊಳ್ಳಿ.
3. ಮಾಹಿತಿ ಪಡೆಯಬೇಕಾದ ಸಾರ್ವಜನಿಕ ಪ್ರಾಧಿಕಾರವನ್ನು (Public Authority / Department) ಆಯ್ಕೆಮಾಡಿ.
4. ಅರ್ಜಿದಾರರ ಹೆಸರು, ವಿಳಾಸ ಮತ್ತು ಸಂಪರ್ಕ ವಿವರಗಳನ್ನು ನಮೂದಿಸಿ.
5. ಕೇಳಬಯಸಿದ ಮಾಹಿತಿಯನ್ನು ಗರಿಷ್ಠ 3,000 ಅಕ್ಷರಗಳಲ್ಲಿ ಸ್ಪಷ್ಟವಾಗಿ ಟೈಪ್ ಮಾಡಿ (ಅಗತ್ಯವಿದ್ದರೆ ಪೂರಕ PDF ಲಗತ್ತಿಸಿ).
6. **₹10 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಶುಲ್ಕ** ಪಾವತಿಸಿ (BPL ಕಾರ್ಡ್‌ದಾರರಿಗೆ ಸಂಪೂರ್ಣ ಉಚಿತ).
7. ಸಲ್ಲಿಕೆಯ ನಂತರ ಬರುವ **RTI Registration Number** ಇಟ್ಟುಕೊಳ್ಳಿ.

---

### ⏱️ ಕಾಲಮಿತಿ & ಮೇಲ್ಮನವಿ (First Appeal):
* ಸಾರ್ವಜನಿಕ ಮಾಹಿತಿ ಅಧಿಕಾರಿ (PIO) **30 ದಿನಗಳ ಒಳಗಾಗಿ** ಮಾಹಿತಿ ನೀಡಬೇಕು.
* ಮಾಹಿತಿ ಸಿಗದಿದ್ದರೆ ಅದೇ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ **'Submit First Appeal'** ಮೂಲಕ ಮೊದಲ ಮೇಲ್ಮನವಿ ಸಲ್ಲಿಸಬಹುದು.""",
        "category": "ADMIN",
        "language": "kn",
        "source_url": "https://rtionline.karnataka.gov.in",
        "keywords": "rti online karnataka, right to information act, rti first appeal, ಮಾಹಿತಿ ಹಕ್ಕು ಅರ್ಜಿ, ಆರ್‌ಟಿಐ",
        "action_label": "📑 RTI ಪೋರ್ಟಲ್",
        "action_url": "https://rtionline.karnataka.gov.in"
    },
    {
        "id": "faq_hsrp_169",
        "question": "ಹಳೆಯ ವಾಹನಗಳಿಗೆ ಹೈ ಸೆಕ್ಯುರಿಟಿ ರಿಜಿಸ್ಟ್ರೇಷನ್ ಪ್ಲೇಟ್ (HSRP Number Plate) ಆನ್‌ಲೈನ್ ಬುಕಿಂಗ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "hsrp number plate online booking karnataka siam book my hsrp ಹೆಚ್‌ಎಸ್‌ಆರ್‌ಪಿ ನಂಬರ್ ಪ್ಲೇಟ್",
        "answer": """### 🚗 ಅತಿ ಸುರಕ್ಷಿತ ನೋಂದಣಿ ಫಲಕ (HSRP - High Security Registration Plate)

ಕರ್ನಾಟಕದಲ್ಲಿ ಏಪ್ರಿಲ್ 1, 2019 ಕ್ಕಿಂತ ಮೊದಲು ನೋಂದಣಿಯಾಗಿರುವ ಎಲ್ಲಾ ಹಳೆಯ ವಾಹನಗಳಿಗೆ (ದ್ವಿಚಕ್ರ, ಕಾರು, ಲಾರಿ, ಬಸ್, ಟ್ರ್ಯಾಕ್ಟರ್) HSRP ನಂಬರ್ ಪ್ಲೇಟ್ ಅಳವಡಿಸುವುದು ಕಡ್ಡಾಯವಾಗಿದೆ.

---

### 🚀 ಆನ್‌ಲೈನ್ HSRP ಬುಕಿಂಗ್ ಮಾಡುವ ಅಧಿಕೃತ ಹಂತಗಳು:
1. [transport.karnataka.gov.in](https://transport.karnataka.gov.in) ಅಥವಾ [siam.in](https://www.siam.in) / [bookmyhsrp.com](https://bookmyhsrp.com) ಗೆ ಭೇಟಿ ನೀಡಿ.
2. ವಾಹನ ತಯಾರಕ ಕಂಪನಿ (Vehicle Maker - ಉದಾ: Hero, Honda, Maruti, Hyundai) ಆಯ್ಕೆಮಾಡಿ.
3. ವಾಹನದ ನೋಂದಣಿ ಸಂಖ್ಯೆ (Vehicle Reg No), ಚಾಸಿಸ್ ನಂಬರ್ (ಕೊನೆಯ 5 ಅಂಕಿ) ಮತ್ತು ಇಂಜಿನ್ ನಂಬರ್ (ಕೊನೆಯ 5 ಅಂಕಿ) ನಮೂದಿಸಿ.
4. ನಿಮ್ಮ ಹತ್ತಿರದ ಅಧಿಕೃತ ಡೀಲರ್ (Showroom) ಮತ್ತು ಅಳವಡಿಕೆಯ ದಿನಾಂಕ/ಸಮಯದ ಸ್ಲಾಟ್ ಆಯ್ಕೆಮಾಡಿ.
5. ಆನ್‌ಲೈನ್ ಶುಲ್ಕ ಪಾವತಿಸಿ ರಶೀದಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ.
6. ನಿಗದಿತ ದಿನದಂದು ವಾಹನ ತೆಗೆದುಕೊಂಡು ಹೋಗಿ ಲೇಸರ್ ಕೋಡೆಡ್ HSRP ನಂಬರ್ ಪ್ಲೇಟ್ ಹಾಗೂ ಕಲರ್ ಸ್ಟಿಕ್ಕರ್ ಅಳವಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ನಕಲಿ ವೆಬ್‌ಸೈಟ್‌ಗಳ ಬಗ್ಗೆ ಎಚ್ಚರವಿರಲಿ. ಕೇವಲ SIAM ಅಥವಾ ಸಾರಿಗೆ ಇಲಾಖೆಯ ಅಧಿಕೃತ ಪೋರ್ಟಲ್ ಮೂಲಕವೇ ಬುಕ್ ಮಾಡಿ.""",
        "category": "TRANSPORT",
        "language": "kn",
        "source_url": "https://transport.karnataka.gov.in",
        "keywords": "hsrp number plate booking, bookmyhsrp siam, hsrp karnataka deadline, ಹೆಚ್‌ಎಸ್‌ಆರ್‌ಪಿ ನಂಬರ್ ಪ್ಲೇಟ್, ಸಾರಿಗೆ ಇಲಾಖೆ",
        "action_label": "🚗 HSRP ಬುಕಿಂಗ್ ಪೋರ್ಟಲ್",
        "action_url": "https://transport.karnataka.gov.in"
    },
    {
        "id": "faq_ration_split_170",
        "question": "ರೇಷನ್ ಕಾರ್ಡ್ ವಿಭಜನೆ (Separation) ಮತ್ತು ಹೊಸ ಸದಸ್ಯರ ಹೆಸರು ಸೇರ್ಪಡೆ/ತೆಗೆದುಹಾಕುವುದು ಹೇಗೆ?",
        "normalized_question": "ration card member add delete card splitting ahara karnataka ರೇಷನ್ ಕಾರ್ಡ್ ವಿಭಜನೆ ಹೆಸರು ಸೇರ್ಪಡೆ",
        "answer": """### 🛒 ರೇಷನ್ ಕಾರ್ಡ್ ತಿದ್ದುಪಡಿ & ಸದಸ್ಯರ ಬದಲಾವಣೆ (Ahara Portal)

ಮದುವೆಯಾದಾಗ ಹೊಸ ಕುಟುಂಬಕ್ಕೆ ಪ್ರತ್ಯೇಕ ರೇಷನ್ ಕಾರ್ಡ್ ಮಾಡಿಸಲು ಅಥವಾ ನವಜಾತ ಶಿಶುವಿನ ಹೆಸರು ಸೇರಿಸಲು ಆಹಾರ ಇಲಾಖೆಯ ಪೋರ್ಟಲ್ ಬಳಸಬಹುದು.

---

### 👶 1. ಹೊಸ ಸದಸ್ಯರ / ಮಕ್ಕಳ ಹೆಸರು ಸೇರ್ಪಡೆ:
* ಮಗುವಿನ ಜನನ ಪ್ರಮಾಣಪತ್ರ (Birth Certificate) ಮತ್ತು ಆಧಾರ್ ಕಾರ್ಡ್ ಅಗತ್ಯ.
* ಗ್ರಾಮ ಒನ್ / ಕರ್ನಾಟಕ ಒನ್ ಅಥವಾ ಆಹಾರ ಇಲಾಖೆಯ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ 'Add Member' ಆಯ್ಕೆಮಾಡಿ ಆಧಾರ್ e-KYC ಮೂಲಕ ತಕ್ಷಣ ಸೇರಿಸಬಹುದು.

---

### ✂️ 2. ರೇಷನ್ ಕಾರ್ಡ್ ವಿಭಜನೆ (Card Splitting):
* ಪೋಷಕರ ರೇಷನ್ ಕಾರ್ಡ್‌ನಿಂದ ಮದುವೆಯಾದ ದಂಪತಿಯ ಹೆಸರನ್ನು ಮೊದಲು 'Surrender / Deletion of Name' ಮೂಲಕ ತೆಗೆದುಹಾಕಬೇಕು.
* ರದ್ದಾದ ನಂತರ ಸಿಗುವ ಡಿಲಿಶನ್ ಸರ್ಟಿಫಿಕೇಟ್ (Deletion Certificate) ಬಳಸಿ ಹೊಸ ರೇಷನ್ ಕಾರ್ಡ್‌ಗೆ (New Ration Card) ಅರ್ಜಿ ಸಲ್ಲಿಸಬೇಕು.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [ahara.kar.nic.in](https://ahara.kar.nic.in)""",
        "category": "FOOD",
        "language": "kn",
        "source_url": "https://ahara.kar.nic.in",
        "keywords": "ration card modification, add member ration card, split ration card, ರೇಷನ್ ಕಾರ್ಡ್ ತಿದ್ದುಪಡಿ, ಹೆಸರು ಸೇರ್ಪಡೆ",
        "action_label": "🛒 ಆಹಾರ ಇಲಾಖೆ ಪೋರ್ಟಲ್",
        "action_url": "https://ahara.kar.nic.in"
    },
    {
        "id": "faq_dbt_error_171",
        "question": "DBT Karnataka ಆ್ಯಪ್‌ನಲ್ಲಿ ಬ್ಯಾಂಕ್ ಸೀಡಿಂಗ್ ಫೇಲ್ (NPCI Inactive) ದೋಷ ಬಂದರೆ ಸರಿಪಡಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "dbt karnataka app bank seeding failed npci inactive error solution ಡಿಬಿಟಿ ಹಣ ಬಂದಿಲ್ಲ ಬ್ಯಾಂಕ್ ಸೀಡಿಂಗ್",
        "answer": """### 💳 DBT Karnataka ಬ್ಯಾಂಕ್ ಸೀಡಿಂಗ್ ದೋಷ ಪರಿಹಾರ (NPCI Seeding Troubleshooting)

ಗೃಹಲಕ್ಷ್ಮಿ, ಅನ್ನಭಾಗ್ಯ ಅಥವಾ ವಿದ್ಯಾರ್ಥಿವೇತನದ ಹಣ ಖಾತೆಗೆ ಜಮೆಯಾಗದೆ 'NPCI Inactive' ಅಥವಾ 'Aadhaar Not Mapped' ಎಂದು ತೋರಿಸಿದರೆ ಈ ಕೆಳಗಿನ ಕ್ರಮಗಳನ್ನು ಅನುಸರಿಸಿ:

---

### 🔧 ಹಂತ-ಹಂತದ ಪರಿಹಾರ:
1. **ಬ್ಯಾಂಕ್ ಶಾಖೆಗೆ ಭೇಟಿ ನೀಡಿ:** ನಿಮ್ಮ ಮುಖ್ಯ ಬ್ಯಾಂಕ್ ಶಾಖೆಗೆ ತೆರಳಿ **'NPCI / DBT Aadhaar Seeding Form'** ಭರ್ತಿ ಮಾಡಿ ನೀಡಿ (ಕೇವಲ ಆಧಾರ್ ಲಿಂಕ್ ಸಾಲದು, DBT ಮ್ಯಾಪಿಂಗ್ ಸಕ್ರಿಯವಾಗಿರಬೇಕು).
2. **ಇಂಡಿಯಾ ಪೋಸ್ಟ್ ಪೇಮೆಂಟ್ಸ್ ಬ್ಯಾಂಕ್ (IPPB Account):** ಸರ್ಕಾರಿ ಯೋಜನೆಗಳ ಹಣ ತ್ವರಿತವಾಗಿ ಜಮೆಯಾಗಲು ಹತ್ತಿರದ ಅಂಚೆ ಕಚೇರಿಯಲ್ಲಿ ಕೇವಲ 10 ನಿಮಿಷಗಳಲ್ಲಿ ಬಯೋಮೆಟ್ರಿಕ್ ಮೂಲಕ **IPPB ಖಾತೆ** ತೆರೆಯಿರಿ (ಇದು ಸ್ವಯಂಚಾಲಿತವಾಗಿ NPCI ಸೀಡ್ ಆಗಿರುತ್ತದೆ).
3. **ಸೀಡಿಂಗ್ ಸ್ಥಿತಿ ಪರೀಕ್ಷಿಸಿ:** [resident.uidai.gov.in](https://resident.uidai.gov.in) ಅಥವಾ DBT Karnataka App ನಲ್ಲಿ 'Check Bank Seeding Status' ಕ್ಲಿಕ್ ಮಾಡಿ 'Active' ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.""",
        "category": "SCHEME",
        "language": "kn",
        "source_url": "https://sevasindhugs.karnataka.gov.in",
        "keywords": "dbt app npci error, bank seeding failed, ippb dbt account, ಡಿಬಿಟಿ ಬ್ಯಾಂಕ್ ಸೀಡಿಂಗ್, ಎನ್‌ಪಿಸಿಐ ದೋಷ",
        "action_label": "📱 DBT ಆ್ಯಪ್ ಪರಿಶೀಲನೆ",
        "action_url": "https://sevasindhugs.karnataka.gov.in"
    },
    {
        "id": "faq_kidwai_172",
        "question": "ಕಿದ್ವಾಯಿ ಕ್ಯಾನ್ಸರ್ ಸಂಸ್ಥೆಯಲ್ಲಿ (Kidwai KMIO) ಉಚಿತ ಹಾಗೂ ರಿಯಾಯಿತಿ ದರದ ಚಿಕಿತ್ಸೆ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "kidwai cancer hospital bangalore bpl free cancer treatment sast ಕಿದ್ವಾಯಿ ಕ್ಯಾನ್ಸರ್ ಆಸ್ಪತ್ರೆ ಉಚಿತ ಚಿಕಿತ್ಸೆ",
        "answer": """### 🏥 ಕಿದ್ವಾಯಿ ಸ್ಮಾರಕ ಕ್ಯಾನ್ಸರ್ ಸಂಸ್ಥೆ (KMIO Bengaluru) ಚಿಕಿತ್ಸಾ ಸೌಲಭ್ಯಗಳು

ಬೆಂಗಳೂರಿನ ಕಿದ್ವಾಯಿ ಸಂಸ್ಥೆಯು ದಕ್ಷಿಣ ಭಾರತದ ಪ್ರಮುಖ ಕ್ಯಾನ್ಸರ್ ಸಂಶೋಧನೆ ಮತ್ತು ಸೂಪರ್ ಸ್ಪೆಷಾಲಿಟಿ ಆಸ್ಪತ್ರೆಯಾಗಿದೆ.

---

### 💰 ರಿಯಾಯಿತಿ & ಉಚಿತ ಚಿಕಿತ್ಸಾ ಯೋಜನೆಗಳು:
* **BPL ಕಾರ್ಡ್‌ದಾರರಿಗೆ:** ಆಯುಷ್ಮಾನ್ ಭಾರತ್ - ಆರೋಗ್ಯ ಕರ್ನಾಟಕ (AB-ArK) ಹಾಗೂ ಸುವರ್ಣ ಆರೋಗ್ಯ ಸುರಕ್ಷಾ ಟ್ರಸ್ಟ್ (SAST) ಅಡಿಯಲ್ಲಿ ಕೀಮೋಥೆರಪಿ, ರೇಡಿಯೋಥೆರಪಿ, ಮತ್ತು ಸರ್ಜರಿಗಳು ಸಂಪೂರ್ಣ ಉಚಿತ.
* **ಮುಖ್ಯಮಂತ್ರಿಗಳ ಪರಿಹಾರ ನಿಧಿ (CMRF):** ದುಬಾರಿ ಕ್ಯಾನ್ಸರ್ ಔಷಧಿಗಳಿಗೆ ಹೆಚ್ಚುವರಿ ಧನಸಹಾಯ ಲಭ್ಯ.
* **ಧರ್ಮಾರ್ಥ ವಿಭಾಗ:** ನಿರ್ಗತಿಕ ರೋಗಿಗಳಿಗೆ ಆಸ್ಪತ್ರೆಯ ಬಡ ರೋಗಿಗಳ ಕಲ್ಯಾಣ ನಿಧಿಯಿಂದ (Poor Patients Fund) ಉಚಿತ ಔಷಧಿ ಮತ್ತು ಊಟ-ವಸತಿ ಸೌಲಭ್ಯ.

📝 ದಾಖಲಾಗಲು ರೋಗಿಯ ಆಧಾರ್ ಕಾರ್ಡ್, BPL ರೇಷನ್ ಕಾರ್ಡ್ ಮತ್ತು ಸ್ಥಳೀಯ ಸರ್ಕಾರಿ ಆಸ್ಪತ್ರೆಯ ರೆಫರಲ್ ಪತ್ರ ಅಗತ್ಯ.""",
        "category": "HEALTH",
        "language": "kn",
        "source_url": "https://kmio.karnataka.gov.in",
        "keywords": "kidwai cancer hospital, kmio free chemo radiation, cancer bpl scheme, ಕಿದ್ವಾಯಿ ಕ್ಯಾನ್ಸರ್ ಚಿಕಿತ್ಸೆ, ಉಚಿತ ಕೀಮೋ",
        "action_label": "🏥 ಕಿದ್ವಾಯಿ ಪೋರ್ಟಲ್",
        "action_url": "https://kmio.karnataka.gov.in"
    },
    {
        "id": "faq_police_ncr_173",
        "question": "ಕರ್ನಾಟಕ ಪೊಲೀಸರಲ್ಲಿ ಎನ್‌ಸಿಆರ್ (NCR) ಮತ್ತು ಎಫ್‌ಐಆರ್ (FIR) ನಡುವಿನ ವ್ಯತ್ಯಾಸವೇನು? ಆನ್‌ಲೈನ್ ಕಾಪಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "ncr vs fir difference karnataka police download fir copy online ಎನ್‌ಸಿಆರ್ ಮತ್ತು ಎಫ್‌ಐಆರ್ ವ್ಯತ್ಯಾಸ",
        "answer": """### 👮 ಎನ್‌ಸಿಆರ್ (NCR) vs ಎಫ್‌ಐಆರ್ (FIR) — ಕಾನೂನು ಮಾರ್ಗದರ್ಶಿ

* **FIR (First Information Report - ಪ್ರಥಮ ವರ್ತಮಾನ ವರದಿ):** ಕೊಲೆ, ದರೋಡೆ, ಅತ್ಯಾಚಾರ, ಕಳ್ಳತನ, ಗಂಭೀರ ಹಲ್ಲೆಯಂತಹ ಗಂಭೀರ ಅಪರಾಧಗಳಾದಾಗ (Cognizable Offence) ದಾಖಲಾಗುತ್ತದೆ. ಪೊಲೀಸರು ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಅನುಮತಿಯಿಲ್ಲದೆ ತನಿಖೆ ಮತ್ತು ಬಂಧನ ಮಾಡಬಹುದು.
* **NCR (Non-Cognizable Report - ಅಸಂಜ್ಞೇಯ ಅಪರಾಧ ವರದಿ):** ಸಣ್ಣ ಗಲಾಟೆ, ಬೈಗುಳ, ದಾಖಲೆ ಅಥವಾ ಮೊಬೈಲ್ ಕಳೆದುಹೋದ ಪ್ರಕರಣಗಳಲ್ಲಿ ಎನ್‌ಸಿಆರ್ ನೀಡಲಾಗುತ್ತದೆ. ನ್ಯಾಯಾಲಯದ ಆದೇಶವಿಲ್ಲದೆ ಪೊಲೀಸರು ನೇರವಾಗಿ ತನಿಖೆ ಮಾಡುವಂತಿಲ್ಲ.

---

### 📥 ಆನ್‌ಲೈನ್ FIR / NCR ಪ್ರತಿ ಪಡೆಯುವ ವಿಧಾನ:
1. [ksp.karnataka.gov.in](https://ksp.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ.
2. **'FIR Search'** ಆಯ್ಕೆಮಾಡಿ ಜಿಲ್ಲೆ, ಪೊಲೀಸ್ ಠಾಣೆ ಮತ್ತು ವರ್ಷ ನಮೂದಿಸಿ.
3. FIR ಸಂಖ್ಯೆ ಹಾಕಿ ಅಧಿಕೃತ ಡಿಜಿಟಲ್ ಪ್ರತಿಯನ್ನು ಉಚಿತವಾಗಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.""",
        "category": "POLICE",
        "language": "kn",
        "source_url": "https://ksp.karnataka.gov.in",
        "keywords": "ncr vs fir, ksp fir search, download fir online, ಎನ್‌ಸಿಆರ್ ಎಫ್‌ಐಆರ್ ವ್ಯತ್ಯಾಸ, ಪೊಲೀಸ್ ಎಫ್‌ಐಆರ್ ಡೌನ್‌ಲೋಡ್",
        "action_label": "👮 KSP FIR ಶೋಧನೆ",
        "action_url": "https://ksp.karnataka.gov.in"
    },
    {
        "id": "faq_ecourts_174",
        "question": "ಇ-ಕೋರ್ಟ್ಸ್ (e-Courts) ನಲ್ಲಿ ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ ಮತ್ತು ಜಿಲ್ಲಾ ಕೋರ್ಟ್ ಕೇಸ್ ಸ್ಥಿತಿ (CNR Number) ನೋಡುವುದು ಹೇಗೆ?",
        "normalized_question": "ecourts services karnataka high court district court cnr number case status ಇ-ಕೋರ್ಟ್ಸ್ ಕೇಸ್ ಸ್ಥಿತಿ",
        "answer": """### ⚖️ ಇ-ಕೋರ್ಟ್ಸ್ ಸೇವೆಗಳು (e-Courts Services) — ನ್ಯಾಯಾಲಯ ಪ್ರಕರಣಗಳ ಲೈವ್ ಟ್ರ್ಯಾಕಿಂಗ್

ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ ಹಾಗೂ ಎಲ್ಲಾ ಜಿಲ್ಲಾ ಮತ್ತು ತಾಲೂಕು ಸಿವಿಲ್/ಕ್ರಿಮಿನಲ್ ನ್ಯಾಯಾಲಯಗಳ ಕಲಾಪ ವಿವರಗಳನ್ನು ಮನೆಯಲ್ಲೇ ಕುಳಿತು ಮೊಬೈಲ್‌ನಲ್ಲೇ ತಿಳಿಯಬಹುದು.

---

### 🔍 16 ಅಂಕಿಗಳ CNR ಸಂಖ್ಯೆ ಮೂಲಕ ಹುಡುಕಾಟ:
1. **ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [ecourts.gov.in](https://ecourts.gov.in) ಅಥವಾ **eCourts Services App** ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ.
2. ನಿಮ್ಮ ವಕೀಲರು ನೀಡಿರುವ 16 ಅಂಕಿಗಳ **CNR Number** ನಮೂದಿಸಿ 'Search' ಕ್ಲಿಕ್ ಮಾಡಿ.
3. **ಲಭ್ಯವಾಗುವ ಮಾಹಿತಿ:**
   - ಪ್ರಕರಣದ ಹಿಂದಿನ ದಿನಾಂಕದ ನಡಾವಳಿಗಳು (Daily Orders).
   - ಮುಂದಿನ ವಿಚಾರಣೆ ದಿನಾಂಕ ಮತ್ತು ಕೋರ್ಟ್ ಹಾಲ್ ಸಂಖ್ಯೆ (Next Hearing Date).
   - ಅಂತಿಮ ತೀರ್ಪಿನ ಸಹಿಯುಳ್ಳ PDF ಪ್ರತಿ (Final Judgment Copy).

💡 CNR ಸಂಖ್ಯೆ ಇಲ್ಲದಿದ್ದರೆ, ಜಿಲ್ಲೆ, ಕೋರ್ಟ್ ಸಂಕೀರ್ಣ, ಕೇಸ್ ಪ್ರಕಾರ (OS / CC / PCR) ಮತ್ತು ವರ್ಷ ಹಾಕಿ ಹುಡುಕಬಹುದು.""",
        "category": "LEGAL",
        "language": "kn",
        "source_url": "https://ecourts.gov.in",
        "keywords": "ecourts karnataka, cnr number case status, high court orders download, ಇ-ಕೋರ್ಟ್ಸ್ ಕೇಸ್ ಮಾಹಿತಿ, ಸಿಎನ್‌ಆರ್ ನಂಬರ್",
        "action_label": "⚖️ e-Courts ಪೋರ್ಟಲ್",
        "action_url": "https://ecourts.gov.in"
    },
    {
        "id": "faq_matsya_175",
        "question": "ಮತ್ಸ್ಯ ಸಿರಿ ಮತ್ತು ಮೀನುಗಾರರಿಗೆ ಕರಮುಕ್ತ ಡೀಸೆಲ್/ಸೀಮೆಎಣ್ಣೆ ಸಬ್ಸಿಡಿ (Fisheries Subsidy) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "matsya siri karnataka fisheries diesel kerosene subsidy kcc loan ಮತ್ಸ್ಯ ಸಿರಿ ಮೀನುಗಾರರ ಸಬ್ಸಿಡಿ",
        "answer": """### 🐟 ಕರ್ನಾಟಕ ಮತ್ಸ್ಯ ಸಿರಿ ಮತ್ತು ಮೀನುಗಾರರ ಕಲ್ಯಾಣ ಯೋಜನೆಗಳು

ಕರಾವಳಿ ಮತ್ತು ಒಳನಾಡು ಮೀನುಗಾರರಿಗೆ ಮೀನುಗಾರಿಕೆ ಇಲಾಖೆಯ ವತಿಯಿಂದ ವ್ಯಾಪಕ ಆರ್ಥಿಕ ಉತ್ತೇಜನ ನೀಡಲಾಗುತ್ತದೆ.

---

### 🚢 ಪ್ರಮುಖ ಸಬ್ಸಿಡಿ ವಿವರಗಳು:
* **ಕರಮುಕ್ತ ಡೀಸೆಲ್ (Tax-Free Diesel):** ಯಾಂತ್ರೀಕೃತ ಮೀನುಗಾರಿಕಾ ದೋಣಿಗಳಿಗೆ ವಾರ್ಷಿಕ ನಿಗದಿತ ಕೋಟಾದಲ್ಲಿ ಮಾರಾಟ ತೆರಿಗೆ ರಹಿತ (Sales Tax Free) ಡೀಸೆಲ್ ನೇರ ವಿತರಣೆ.
* **ಸೀಮೆಎಣ್ಣೆ ಸಹಾಯಧನ:** ಸಾಂಪ್ರದಾಯಿಕ ನಾಡದೋಣಿಗಳಿಗೆ (OBM Boats) ರಿಯಾಯಿತಿ ದರದ ಸೀಮೆಎಣ್ಣೆ ವಿತರಣೆ.
* **ಮೀನುಗಾರರ ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ (KCC):** ಮೀನುಗಾರಿಕೆ ಬಂಡವಾಳಕ್ಕಾಗಿ ₹2.00 ಲಕ್ಷದವರೆಗೆ **ಶೂನ್ಯ ಬಡ್ಡಿದರದಲ್ಲಿ** ಅಲ್ಪಾವಧಿ ಸಾಲ.
* **ಮತ್ಸ್ಯ ವಿಕಾಸ ಯೋಜನೆ:** ಐಸ್‌ಬಾಕ್ಸ್ ಹೊಂದಿರುವ ದ್ವಿಚಕ್ರ/ತ್ರಿಚಕ್ರ ವಾಹನ ಖರೀದಿಗೆ 40% ರಿಂದ 60% ಸಬ್ಸಿಡಿ.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [fisheries.karnataka.gov.in](https://fisheries.karnataka.gov.in)""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://fisheries.karnataka.gov.in",
        "keywords": "matsya siri, fisheries diesel subsidy karnataka, kcc loan fishermen, ಮತ್ಸ್ಯ ಸಿರಿ, ಮೀನುಗಾರರ ಡೀಸೆಲ್ ಸಬ್ಸಿಡಿ",
        "action_label": "🐟 ಮೀನುಗಾರಿಕೆ ಇಲಾಖೆ",
        "action_url": "https://fisheries.karnataka.gov.in"
    },
    {
        "id": "faq_silk_176",
        "question": "ರೇಷ್ಮೆ ಇಲಾಖೆಯಿಂದ ಹಿಪ್ಪುನೇರಳೆ ಕೃಷಿ, ಹನಿ ನೀರಾವರಿ ಮತ್ತು ರೇಷ್ಮೆ ಗೂಡಿಗೆ ಪ್ರೋತ್ಸಾಹಧನ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "sericulture subsidy cocoon incentive drip irrigation reshme ilakhe ರೇಷ್ಮೆ ಗೂಡು ಪ್ರೋತ್ಸಾಹಧನ ಹಿಪ್ಪುನೇರಳೆ",
        "answer": """### 🐛 ರೇಷ್ಮೆ ಕೃಷಿ ಇಲಾಖೆ (Department of Sericulture) ಸಹಾಯಧನ ಯೋಜನೆಗಳು

ರೇಷ್ಮೆ ಬೆಳೆಗಾರರಿಗೆ ಹಿಪ್ಪುನೇರಳೆ ತೋಟ ನಿರ್ಮಾಣದಿಂದ ಹಿಡಿದು ಗೂಡು ಮಾರುಕಟ್ಟೆಯವರೆಗೆ ವಿವಿಧ ಹಂತಗಳಲ್ಲಿ ಸರ್ಕಾರ ಸಬ್ಸಿಡಿ ಒದಗಿಸುತ್ತದೆ.

---

### 💰 ಲಭ್ಯವಿರುವ ಸಬ್ಸಿಡಿಗಳು:
1. **ಹಿಪ್ಪುನೇರಳೆ ತೋಟ ಮತ್ತು ಹನಿ ನೀರಾವರಿ:** ಹೊಸ ಹಿಪ್ಪುನೇರಳೆ ನಾಟಿಗೆ ಹಾಗೂ ಹನಿ ನೀರಾವರಿ ಅಳವಡಿಕೆಗೆ 75% ರಿಂದ 90% ವರೆಗೆ ಸಹಾಯಧನ.
2. **ರೇಷ್ಮೆ ಹುಳು ಸಾಕಾಣಿಕೆ ಮನೆ (Rearing Shed):** ಸುಧಾರಿತ ರೇಷ್ಮೆ ಶೆಡ್ ನಿರ್ಮಾಣಕ್ಕೆ ಸಾಮಾನ್ಯ ವರ್ಗಕ್ಕೆ ₹2.50 ಲಕ್ಷ, SC/ST ರೈತರಿಗೆ ₹4.00 ಲಕ್ಷದವರೆಗೆ ಅನುದಾನ.
3. **ಗೂಡು ಪ್ರೋತ್ಸಾಹಧನ (Cocoon Incentive DBT):** ಸರ್ಕಾರಿ ರೇಷ್ಮೆ ಮಾರುಕಟ್ಟೆಗಳಲ್ಲಿ (ರಾಮನಗರ, ಶಿಡ್ಲಘಟ್ಟ ಇತ್ಯಾದಿ) ಮಾರಾಟವಾಗುವ ದ್ವಿತಳಿ (Bivoltine) ಗೂಡಿಗೆ ಪ್ರತಿ ಕೆಜಿಗೆ ಹೆಚ್ಚುವರಿ ಸರ್ಕಾರದ ಪ್ರೋತ್ಸಾಹಧನ ರೈತರ ಖಾತೆಗೆ DBT ಆಗುತ್ತದೆ.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [sericulture.karnataka.gov.in](https://sericulture.karnataka.gov.in)""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://sericulture.karnataka.gov.in",
        "keywords": "sericulture subsidy karnataka, cocoon incentive dbt, bivoltine silk shed subsidy, ರೇಷ್ಮೆ ಇಲಾಖೆ, ಗೂಡು ಪ್ರೋತ್ಸಾಹಧನ",
        "action_label": "🐛 ರೇಷ್ಮೆ ಇಲಾಖೆ ಪೋರ್ಟಲ್",
        "action_url": "https://sericulture.karnataka.gov.in"
    },
    {
        "id": "faq_fire_noc_177",
        "question": "ಅಗ್ನಿಶಾಮಕ ಇಲಾಖೆಯಿಂದ ಕಟ್ಟಡಗಳಿಗೆ ಅಗ್ನಿ ಸುರಕ್ಷತಾ ಎನ್‌ಒಸಿ (Fire Safety NOC) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "fire safety noc ksfes karnataka building clearance online ಅಗ್ನಿಶಾಮಕ ಇಲಾಖೆ ಎನ್‌ಒಸಿ",
        "answer": """### 🚒 ಕರ್ನಾಟಕ ರಾಜ್ಯ ಅಗ್ನಿಶಾಮಕ ಮತ್ತು ತುರ್ತು ಸೇವೆಗಳು (KSFES Fire NOC)

15 ಮೀಟರ್‌ಗಿಂತ ಎತ್ತರದ ಬಹುಮಹಡಿ ಕಟ್ಟಡಗಳು, ವಾಣಿಜ್ಯ ಸಂಕೀರ್ಣಗಳು, ಶಾಲೆ-ಕಾಲೇಜುಗಳು, ಆಸ್ಪತ್ರೆಗಳು ಮತ್ತು ಕೈಗಾರಿಕೆಗಳಿಗೆ ಅಗ್ನಿ ಸುರಕ್ಷತಾ ಪ್ರಮಾಣಪತ್ರ ಕಡ್ಡಾಯ.

---

### 📜 2 ಹಂತಗಳ ಅಗ್ನಿಶಾಮಕ ಪ್ರಮಾಣಪತ್ರಗಳು:
1. **Fire CC (Construction Clearance):** ಕಟ್ಟಡ ನಕ್ಷೆ ಮಂಜೂರಾತಿ ಸಮಯದಲ್ಲಿ ಸುರಕ್ಷತಾ ಮಾರ್ಗಗಳು ಮತ್ತು ಅಗ್ನಿಶಾಮಕ ಸಲಕರಣೆಗಳ ನೀಲನಕ್ಷೆಗೆ ನೀಡುವ ಆರಂಭಿಕ ಎನ್‌ಒಸಿ.
2. **Final Fire NOC (Clearance Certificate):** ಕಟ್ಟಡ ಪೂರ್ಣಗೊಂಡ ನಂತರ ಸ್ಪ್ರಿಂಕ್ಲರ್, ಫೈರ್ ಅಲಾರಂ, ಹೈಡ್ರಂಟ್ ಪೈಪ್‌ಗಳನ್ನು ಪರೀಕ್ಷಿಸಿ ನೀಡುವ ಅಂತಿಮ ಕಾರ್ಯಾಚರಣಾ ಪ್ರಮಾಣಪತ್ರ (ಇದನ್ನು ಪ್ರತಿ 2 ವರ್ಷಕ್ಕೊಮ್ಮೆ ನವೀಕರಿಸಬೇಕು).

🔗 **ಆನ್‌ಲೈನ್ ಅರ್ಜಿ:** [ksfes.karnataka.gov.in](https://ksfes.karnataka.gov.in)""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://ksfes.karnataka.gov.in",
        "keywords": "fire noc karnataka, ksfes building clearance, fire safety certificate, ಅಗ್ನಿಶಾಮಕ ಎನ್‌ಒಸಿ, ಕಟ್ಟಡ ಸುರಕ್ಷತೆ",
        "action_label": "🚒 KSFES ಪೋರ್ಟಲ್",
        "action_url": "https://ksfes.karnataka.gov.in"
    },
    {
        "id": "faq_sheep_178",
        "question": "ಅಮೃತ ಸ್ವಾಭಿಮಾನಿ ಕುರಿ-ಮೇಕೆ ಸಾಕಾಣಿಕೆ ಯೋಜನೆ ಮತ್ತು ಆಕಸ್ಮಿಕ ಕುರಿ ಸಾವು ಪರಿಹಾರ (₹5,000) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "amrutha swarojgara sheep goat rearing subsidy 5000 compensation ಅನುಗ್ರಹ ಕುರಿ ಪರಿಹಾರ",
        "answer": """### 🐑 ಕರ್ನಾಟಕ ಕುರಿ ಮತ್ತು ಉಣ್ಣೆ ಅಭಿವೃದ್ಧಿ ನಿಗಮ (KASWDC) — ಕಲ್ಯಾಣ ಯೋಜನೆಗಳು

ಕುರಿ ಮತ್ತು ಮೇಕೆ ಸಾಕಾಣಿಕೆದಾರರಿಗೆ ಆರ್ಥಿಕ ರಕ್ಷಣೆ ಮತ್ತು ಸ್ವಯಂ ಉದ್ಯೋಗ ಕಲ್ಪಿಸಲು ಸರ್ಕಾರ ಜಾರಿಗೊಳಿಸಿರುವ ಪ್ರಮುಖ ಯೋಜನೆಗಳು.

---

### 🌟 ಪ್ರಮುಖ ಸೌಲಭ್ಯಗಳು:
1. **ಅಮೃತ ಸ್ವಾಭಿಮಾನಿ ಕುರಿ ಘಟಕ ಯೋಜನೆ:** 20 ಕುರಿ + 1 ಟಗರು ಘಟಕ ಸ್ಥಾಪನೆಗೆ ₹1.75 ಲಕ್ಷ ವೆಚ್ಚದಲ್ಲಿ **50% ಸರ್ಕಾರದ ಸಹಾಯಧನ (ಸಬ್ಸಿಡಿ)**.
2. **ಅನುಗ್ರಹ ಯೋಜನೆ (ಕುರಿ-ಮೇಕೆ ಆಕಸ್ಮಿಕ ಸಾವು ಪರಿಹಾರ):** ಕಾಯಿಲೆ, ಸಿಡಿಲು ಅಥವಾ ಅಪಘಾತದಿಂದ ಕುರಿ/ಮೇಕೆ ಸಾವನ್ನಪ್ಪಿದರೆ 6 ತಿಂಗಳು ಮೇಲ್ಪಟ್ಟ ಕುರಿಗೆ **₹5,000** ಹಾಗೂ 3-6 ತಿಂಗಳ ಮರಿಗೆ **₹3,500** ಪರಿಹಾರ ಧನ.

📝 ಕುರಿ ಸಾವನ್ನಪ್ಪಿದ 24 ಗಂಟೆಯೊಳಗೆ ಸ್ಥಳೀಯ ಸರ್ಕಾರಿ ಪಶುವೈದ್ಯರಿಂದ ಮರಣೋತ್ತರ ಪರೀಕ್ಷೆ (Post-Mortem) ಮಾಡಿಸಿ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಬೇಕು.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [kaswdc.karnataka.gov.in](https://kaswdc.karnataka.gov.in)""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://kaswdc.karnataka.gov.in",
        "keywords": "sheep rearing subsidy, amrutha kuri scheme, anugraha sheep mortality 5000, ಕುರಿ ಸಾಕಾಣಿಕೆ ಸಬ್ಸಿಡಿ, ಅನುಗ್ರಹ ಪರಿಹಾರ",
        "action_label": "🐑 ಕುರಿ ಅಭಿವೃದ್ಧಿ ನಿಗಮ",
        "action_url": "https://kaswdc.karnataka.gov.in"
    },
    {
        "id": "faq_bbmp_dog_179",
        "question": "ಬೆಂಗಳೂರಿನಲ್ಲಿ ಬೀದಿ ನಾಯಿಗಳ ನಿಯಂತ್ರಣ (ABC/ARV) ಮತ್ತು ಸಾಕು ನಾಯಿ ಲೈಸೆನ್ಸ್‌ಗೆ BBMP ಸಹಾಯವಾಣಿ ಯಾವುದು?",
        "normalized_question": "bbmp stray dog complaint animal birth control pet dog license anti rabies ಬಿಬಿಎಂಪಿ ಬೀದಿ ನಾಯಿ ದೂರು",
        "answer": """### 🐕 BBMP ಪಶುಸಂಗೋಪನೆ ಮತ್ತು ಬೀದಿ ನಾಯಿ ನಿಯಂತ್ರಣ ಸೇವೆಗಳು

ಬೆಂಗಳೂರು ಮಹಾನಗರದಲ್ಲಿ ರೇಬೀಸ್ ಮುಕ್ತ ವಾತಾವರಣ ನಿರ್ಮಿಸಲು ಬಿಬಿಎಂಪಿಯು ಪ್ರಾಣಿ ಜನನ ನಿಯಂತ್ರಣ (ABC) ಮತ್ತು ಆಂಟಿ-ರೇಬೀಸ್ ಲಸಿಕಾ (ARV) ಕಾರ್ಯಕ್ರಮಗಳನ್ನು ನಿರಂತರವಾಗಿ ನಡೆಸುತ್ತದೆ.

---

### 📞 ಬೀದಿ ನಾಯಿ ದೂರು & ರೇಬೀಸ್ ಸಹಾಯವಾಣಿ:
* **BBMP 24x7 ಕಂಟ್ರೋಲ್ ರೂಂ:** **080-22660000**
* **WhatsApp ದೂರು ಸಂಖ್ಯೆ:** 9480685700
* ಬೀದಿ ನಾಯಿಗಳ ಹಾವಳಿ ಅಥವಾ ಲಸಿಕೆ ಹಾಕದ ನಾಯಿಗಳು ಕಂಡುಬಂದಲ್ಲಿ ವಾರ್ಡ್ ವಿವರ ನೀಡಿ ದೂರು ದಾಖಲಿಸಿದರೆ BBMP ಶ್ವಾನ ರಕ್ಷಕ ತಂಡ ಸ್ಥಳಕ್ಕೆ ಬಂದು ಸಂತಾನಹರಣ ಚಿಕಿತ್ಸೆ ಮತ್ತು ಲಸಿಕೆ ನೀಡಿ ಅದೇ ಸ್ಥಳಕ್ಕೆ ಬಿಡುತ್ತದೆ.

💡 ಸಾಕು ನಾಯಿಗಳಿಗೆ (Pet Dogs) ಮೈಕ್ರೋಚಿಪ್ ಅಳವಡಿಸಿ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ BBMP Pet License ಪಡೆಯುವುದು ಕಡ್ಡಾಯ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bbmp.gov.in",
        "keywords": "bbmp stray dog complaint, pet dog license online, anti rabies vaccination bangalore, ಬಿಬಿಎಂಪಿ ಬೀದಿ ನಾಯಿ, ಶ್ವಾನ ಲೈಸೆನ್ಸ್",
        "action_label": "🐕 BBMP ಪೋರ್ಟಲ್",
        "action_url": "https://bbmp.gov.in"
    },
    {
        "id": "faq_kmvt_tax_180",
        "question": "ಕರ್ನಾಟಕದಲ್ಲಿ ಹೊರರಾಜ್ಯ ವಾಹನಗಳ ಚಾಲನೆ, ಲೈಫ್‌ಟೈಮ್ ರೋಡ್ ಟ್ಯಾಕ್ಸ್ (KMVT) ಮತ್ತು BH ಸರಣಿ ನಿಯಮಗಳೇನು?",
        "normalized_question": "karnataka motor vehicle lifetime road tax bh series out of station vehicle kmvt ಹೊರರಾಜ್ಯ ವಾಹನ ತೆರಿಗೆ",
        "answer": """### 🚘 ಕರ್ನಾಟಕ ಮೋಟಾರು ವಾಹನಗಳ ಜೀವಿತಾವಧಿ ತೆರಿಗೆ (KMVT & BH Series Rules)

* **ಹೊರರಾಜ್ಯ ವಾಹನಗಳು (Out-of-State Vehicles):** ಕರ್ನಾಟಕ ಮೋಟಾರು ವಾಹನ ತೆರಿಗೆ ಕಾಯ್ದೆಯನ್ವಯ, ಹೊರರಾಜ್ಯದ ನೋಂದಣಿ ಹೊಂದಿರುವ ವಾಹನವನ್ನು ಕರ್ನಾಟಕದಲ್ಲಿ ಸತತವಾಗಿ **12 ತಿಂಗಳುಗಳಿಗಿಂತ ಹೆಚ್ಚು** ಓಡಿಸಿದರೆ ರಾಜ್ಯದ ಲೈಫ್‌ಟೈಮ್ ರೋಡ್ ಟ್ಯಾಕ್ಸ್ ಪಾವತಿಸಿ ಸ್ಥಳೀಯ KA ನೋಂದಣಿ ಪಡೆಯುವುದು ಕಡ್ಡಾಯ.
* **BH (Bharat) ಸರಣಿ ನೋಂದಣಿ:** ಕೇಂದ್ರ ಸರ್ಕಾರಿ ನೌಕರರು, ರಕ್ಷಣಾ ಸಿಬ್ಬಂದಿ, ಬ್ಯಾಂಕ್ ನೌಕರರು ಮತ್ತು ಕನಿಷ್ಠ 4 ರಾಜ್ಯಗಳಲ್ಲಿ ಕಚೇರಿ ಹೊಂದಿರುವ ಖಾಸಗಿ ಕಂಪನಿಗಳ ಉದ್ಯೋಗಿಗಳು ವರ್ಗಾವಣೆಯಾದಾಗ ಯಾವುದೇ ತೆರಿಗೆ ತೊಂದರೆಯಿಲ್ಲದೆ ಓಡಿಸಲು BH ಸರಣಿ ನೋಂದಣಿ ಪಡೆಯಬಹುದು.

🔗 **ಸಾರಿಗೆ ಪೋರ್ಟಲ್:** [transport.karnataka.gov.in](https://transport.karnataka.gov.in)""",
        "category": "TRANSPORT",
        "language": "kn",
        "source_url": "https://transport.karnataka.gov.in",
        "keywords": "kmvt road tax karnataka, bh series registration karnataka, out of state vehicle rto, ಹೊರರಾಜ್ಯ ವಾಹನ ತೆರಿಗೆ, ಬಿಹೆಚ್ ಸರಣಿ",
        "action_label": "🚘 ಸಾರಿಗೆ ಇಲಾಖೆ ವಿವರ",
        "action_url": "https://transport.karnataka.gov.in"
    },
    {
        "id": "faq_shg_181",
        "question": "ಸಂಜೀವಿನಿ (Sanjeevini - KSRLPS) ಗ್ರಾಮೀಣ ಮಹಿಳಾ ಸ್ವಸಹಾಯ ಸಂಘಗಳಿಗೆ ಸಿಗುವ ಸಾಲ ಮತ್ತು ಸಹಾಯಧನವೇನು?",
        "normalized_question": "sanjeevini ksrlps women self help group bank linkage subsidy ಸಂಜೀವಿನಿ ಸ್ವಸಹಾಯ ಸಂಘ",
        "answer": """### 👩‍🌾 ಸಂಜೀವಿನಿ (KSRLPS - ಕರ್ನಾಟಕ ರಾಜ್ಯ ಗ್ರಾಮೀಣ ಜೀವನೋಪಾಯ ಸಂವರ್ಧನಾ ಸಂಸ್ಥೆ)

ಗ್ರಾಮೀಣ ಬಡ ಮಹಿಳೆಯರನ್ನು ಸ್ವಸಹಾಯ ಸಂಘಗಳಲ್ಲಿ (SHG) ಸಂಘಟಿಸಿ ಕಿರು ಹಣಕಾಸು ಹಾಗೂ ಸ್ವಯಂ ಉದ್ಯೋಗ ಕಲ್ಪಿಸುವ ಯೋಜನೆ.

---

### 💰 ಆರ್ಥಿಕ ನೆರವು & ಸಾಲ ಸೌಲಭ್ಯಗಳು:
1. **ಸಮುದಾಯ ಬಂಡವಾಳ ನಿಧಿ (CIF - Community Investment Fund):** ಸಂಘದ ಸದಸ್ಯರ ಕಿರು ವ್ಯಾಪಾರ, ಹೈನುಗಾರಿಕೆ, ಹೊಲಿಗೆ ಕೆಲಸಗಳಿಗೆ ಕಡಿಮೆ ಬಡ್ಡಿದರದಲ್ಲಿ ಆವರ್ತಕ ನಿಧಿ.
2. **ಬ್ಯಾಂಕ್ ಲಿಂಕೇಜ್ ಸಾಲ (SHG Bank Linkage):** ಉತ್ತಮ ಉಳಿತಾಯ ಹೊಂದಿರುವ ಸ್ವಸಹಾಯ ಸಂಘಗಳಿಗೆ ಬ್ಯಾಂಕ್‌ಗಳಿಂದ ₹5 ಲಕ್ಷದಿಂದ ₹20 ಲಕ್ಷದವರೆಗೆ ರಿಯಾಯಿತಿ ಬಡ್ಡಿದರದಲ್ಲಿ ಜಾಮೀನುರಹಿತ ಸಾಲ.
3. **ಬಡ್ಡಿ ಸಹಾಯಧನ (Interest Subvention):** ಸಕಾಲದಲ್ಲಿ ಮರುಪಾವತಿಸುವ ಸಂಘಗಳಿಗೆ ಕೇವಲ 4% ಬಡ್ಡಿದರದಲ್ಲಿ ಸಾಲ ದೊರೆಯುತ್ತದೆ.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [sanjeevini.karnataka.gov.in](https://sanjeevini.karnataka.gov.in)""",
        "category": "WELFARE",
        "language": "kn",
        "source_url": "https://sanjeevini.karnataka.gov.in",
        "keywords": "sanjeevini ksrlps, women shg loan, self help group bank linkage, ಸಂಜೀವಿನಿ ಸ್ವಸಹಾಯ ಸಂಘ, ಮಹಿಳಾ ಸಾಲ",
        "action_label": "👩‍🌾 ಸಂಜೀವಿನಿ ಪೋರ್ಟಲ್",
        "action_url": "https://sanjeevini.karnataka.gov.in"
    },
    {
        "id": "faq_hostel_182",
        "question": "ರಾಜ್ಯ ಹಾಸ್ಟೆಲ್ ನಿರ್ವಹಣಾ ತಂತ್ರಾಂಶದಲ್ಲಿ (State Hostel Management System) ಉಚಿತ ಹಾಸ್ಟೆಲ್ ಪ್ರವೇಶ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "state hostel management system apply sc st obc free hostel karnataka ಸರ್ಕಾರಿ ಹಾಸ್ಟೆಲ್ ಪ್ರವೇಶ",
        "answer": """### 🏢 ಸಮಾಜ ಕಲ್ಯಾಣ ಮತ್ತು ಹಿಂದುಳಿದ ವರ್ಗಗಳ ಇಲಾಖೆ ಉಚಿತ ಹಾಸ್ಟೆಲ್ ಪ್ರವೇಶ

ಮೆಟ್ರಿಕ್-ಪೂರ್ವ ಮತ್ತು ಮೆಟ್ರಿಕ್-ನಂತರದ ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಉಚಿತ ಊಟ, ವಸತಿ ಮತ್ತು ಗ್ರಂಥಾಲಯ ಸೌಲಭ್ಯವಿರುವ ಸರ್ಕಾರಿ ಹಾಸ್ಟೆಲ್‌ಗಳಿಗೆ ಆನ್‌ಲೈನ್ ಮೂಲಕವೇ ಮೆರಿಟ್ ಆಧಾರದಲ್ಲಿ ಸೀಟು ಹಂಚಲಾಗುತ್ತದೆ.

---

### 📋 ಅರ್ಜಿ ಸಲ್ಲಿಕೆಯ ವಿಧಾನ:
1. [sw.karnataka.gov.in](https://sw.karnataka.gov.in) ಅಥವಾ [bcwd.karnataka.gov.in](https://bcwd.karnataka.gov.in) ಹಾಸ್ಟೆಲ್ ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ.
2. ವಿದ್ಯಾರ್ಥಿಯ ಆಧಾರ್ ಕಾರ್ಡ್, ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರದ (RD Number) ವಿವರ ನಮೂದಿಸಿ.
3. ಕಾಲೇಜು ಪ್ರವೇಶ ರಶೀದಿ ಹಾಗೂ ಹಿಂದಿನ ತರಗತಿಯ ಅಂಕಪಟ್ಟಿ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
4. ನಿಮ್ಮ ಕಾಲೇಜಿನ ಸಮೀಪವಿರುವ 3 ಹಾಸ್ಟೆಲ್‌ಗಳ ಆದ್ಯತೆ (Preference) ಆಯ್ಕೆಮಾಡಿ ಸಬ್ಮಿಟ್ ಮಾಡಿ.
5. ಮೆರಿಟ್ ಮತ್ತು ಮೀಸಲಾತಿ ಪಟ್ಟಿ ಪ್ರಕಟವಾದ ನಂತರ ಹಾಸ್ಟೆಲ್‌ಗೆ ತೆರಳಿ ದಾಖಲೆ ಸಲ್ಲಿಸಿ ಪ್ರವೇಶ ಪಡೆಯಬಹುದು.""",
        "category": "EDUCATION",
        "language": "kn",
        "source_url": "https://sw.karnataka.gov.in",
        "keywords": "state hostel management system, bcm hostel admission, social welfare hostel online, ಸರ್ಕಾರಿ ಹಾಸ್ಟೆಲ್ ಅರ್ಜಿ, ಬಿಸಿಎಂ ಹಾಸ್ಟೆಲ್",
        "action_label": "🏢 ಹಾಸ್ಟೆಲ್ ಪೋರ್ಟಲ್",
        "action_url": "https://sw.karnataka.gov.in"
    },
    {
        "id": "faq_widow_183",
        "question": "ವಿಧವಾ ವೇತನ (Widow Pension Scheme) ಮತ್ತು ಪರಿಹಾರಕ್ಕೆ ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ನಿಯಮಗಳೇನು?",
        "normalized_question": "widow pension scheme karnataka destitute monthly amount nadakacheri ವಿಧವಾ ವೇತನ ಮಾಸಾಶನ",
        "answer": """### 🌸 ವಿಧವಾ ವೇತನ ಯೋಜನೆ (Widow Pension Scheme)

ಪತಿಯನ್ನು ಕಳೆದುಕೊಂಡು ಆರ್ಥಿಕ ಸಂಕಷ್ಟದಲ್ಲಿರುವ ನಿರ್ಗತಿಕ ಮಹಿಳೆಯರಿಗೆ ಗೌರವಯುತ ಜೀವನ ನಡೆಸಲು ಕಂದಾಯ ಇಲಾಖೆಯ ಸಾಮಾಜಿಕ ಭದ್ರತಾ ನಿರ್ದೇಶನಾಲಯವು ಮಾಸಿಕ ಪಿಂಚಣಿ ನೀಡುತ್ತದೆ.

---

### 💰 ಮಾಸಿಕ ಪಿಂಚಣಿ ಮೊತ್ತ:
* ಪ್ರತಿ ತಿಂಗಳು **₹800** ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT).

---

### 📌 ಅರ್ಹತೆಯ ಮಾನದಂಡಗಳು:
1. ಫಲಾನುಭವಿಯು ಕರ್ನಾಟಕದ ನಿವಾಸಿಯಾಗಿರಬೇಕು.
2. ಕುಟುಂಬದ ಒಟ್ಟು ವಾರ್ಷಿಕ ಆದಾಯ ಗ್ರಾಮೀಣ ಮತ್ತು ನಗರ ಪ್ರದೇಶದಲ್ಲಿ ₹32,000 ಮೀರಿರಬಾರದು.
3. ಮರು-ವಿವಾಹವಾಗಿರಬಾರದು ಅಥವಾ ಸರ್ಕಾರಿ/ಖಾಸಗಿ ವಲಯದಿಂದ ಯಾವುದೇ ಇತರ ನಿಯಮಿತ ಪಿಂಚಣಿ ಪಡೆಯುತ್ತಿರಬಾರದು.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
* ಪತಿಯ ಅಧಿಕೃತ ಮರಣ ಪ್ರಮಾಣಪತ್ರ (Death Certificate).
* ಅರ್ಜಿದಾರರ ಆಧಾರ್ ಕಾರ್ಡ್, ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ.
* ನಾಡಕಚೇರಿ ಅಥವಾ ಗ್ರಾಮ ಒನ್ ಕೇಂದ್ರದಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು.""",
        "category": "WELFARE",
        "language": "kn",
        "source_url": "https://nadakacheri.karnataka.gov.in",
        "keywords": "widow pension karnataka, destitute widow monthly dbt, nadakacheri widow scheme, ವಿಧವಾ ವೇತನ, ಮಾಸಾಶನ",
        "action_label": "🌸 ನಾಡಕಚೇರಿ ಸೇವೆಗಳು",
        "action_url": "https://nadakacheri.karnataka.gov.in"
    },
    {
        "id": "faq_ptcl_184",
        "question": "ಪಿಟಿಸಿಎಲ್ ಕಾಯ್ದೆ (PTCL Act) ಎಂದರೇನು? ದಲಿತರಿಗೆ ಮಂಜೂರಾದ ಜಮೀನು ರಕ್ಷಣೆ ಹೇಗೆ?",
        "normalized_question": "ptcl act karnataka sc st granted land transfer prohibition assistant commissioner ಪಿಟಿಸಿಎಲ್ ಕಾಯ್ದೆ ಮಂಜೂರಾದ ಜಮೀನು",
        "answer": """### ⚖️ ಪಿಟಿಸಿಎಲ್ ಕಾಯ್ದೆ (PTCL Act 1978 - ಪರಿಶಿಷ್ಟ ಜಾತಿ ಮತ್ತು ಪರಿಶಿಷ್ಟ ಪಂಗಡಗಳ ಮಂಜೂರಾದ ಭೂಮಿ ವರ್ಗಾವಣೆ ನಿಷೇಧ ಕಾಯ್ದೆ)

ಸರ್ಕಾರದಿಂದ ಪರಿಶಿಷ್ಟ ಜಾತಿ (SC) ಮತ್ತು ಪರಿಶಿಷ್ಟ ಪಂಗಡದ (ST) ಬಡವರಿಗೆ ಉಚಿತವಾಗಿ ಅಥವಾ ರಿಯಾಯಿತಿ ದರದಲ್ಲಿ ಮಂಜೂರಾದ ಕೃಷಿ ಜಮೀನುಗಳನ್ನು ಅಕ್ರಮವಾಗಿ ಅನ್ಯರಿಗೆ ಪರಭಾರೆ ಮಾಡುವುದನ್ನು ತಡೆಯಲು ರೂಪಿಸಲಾದ ಪ್ರಬಲ ರಕ್ಷಣಾತ್ಮಕ ಕಾಯ್ದೆ.

---

### 🛡️ ಪ್ರಮುಖ ಕಾನೂನು ಅಂಶಗಳು:
* **ಸರ್ಕಾರದ ಪೂರ್ವಾನುಮತಿ ಕಡ್ಡಾಯ:** ಮಂಜೂರಾದ ಜಮೀನನ್ನು ಸರ್ಕಾರದ (ಸರ್ಕಾರ/ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ) ಸ್ಪಷ್ಟ ಲಿಖಿತ ಅನುಮತಿಯಿಲ್ಲದೆ ಮಾರಾಟ ಮಾಡುವಂತಿಲ್ಲ. ಅನುಮತಿಯಿಲ್ಲದೆ ಮಾಡಲಾದ ಯಾವುದೇ ನೋಂದಣಿ, ಜಿಪಿಎ (GPA) ಅಥವಾ ಒಪ್ಪಂದಗಳು ಕಾನೂನುಬಾಹಿರ ಮತ್ತು ಶೂನ್ಯ (Null & Void).
* **ಜಮೀನು ಮರುಸ್ಥಾಪನೆ (Restoration):** ಅಕ್ರಮವಾಗಿ ಮಾರಾಟವಾಗಿದ್ದಲ್ಲಿ ಮೂಲ ಮಂಜೂರುದಾರರು ಅಥವಾ ಅವರ ವಾರಸುದಾರರು ಸಹಾಯಕ ಆಯುಕ್ತರ (AC Court) ಮುಂದೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ಜಮೀನನ್ನು ಯಾವುದೇ ಪರಿಹಾರ ನೀಡದೆ ಮರಳಿ ಪಡೆಯಬಹುದು.
* ಯಾವುದೇ ಭೂಮಿ ಖರೀದಿಸುವ ಮುನ್ನ ಪಹಣಿಯಲ್ಲಿ 'ಮಂಜೂರಾದ ಜಮೀನು (Granted Land / Sarakari Jameen)' ಎಂದು ನಮೂದಾಗಿದೆಯೇ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳುವುದು ಕಡ್ಡಾಯ.""",
        "category": "LEGAL",
        "language": "kn",
        "source_url": "https://bhoomi.karnataka.gov.in",
        "keywords": "ptcl act karnataka, sc st granted land prohibition, ac court restoration, ಪಿಟಿಸಿಎಲ್ ಕಾಯ್ದೆ, ಮಂಜೂರಾದ ಭೂಮಿ",
        "action_label": "⚖️ ಕಂದಾಯ ಇಲಾಖೆ",
        "action_url": "https://bhoomi.karnataka.gov.in"
    }
]

# =========================================================================
# 13. EXPANSION BATCH 5: EVERYDAY CITIZEN REAL-WORLD QUESTIONS (185 - 202)
# =========================================================================

ADDITIONAL_EXPANSION_FAQS_BATCH_5 = [
    {
        "id": "faq_user_185",
        "question": "ನನ್ನ ವೋಟರ್ ಐಡಿ ಕಳೆದುಹೋಗಿದೆ, ಹೊಸ PVC ವೋಟರ್ ಕಾರ್ಡ್ ಮನೆ ಬಾಗಿಲಿಗೆ ತರಿಸಿಕೊಳ್ಳುವುದು ಹೇಗೆ?",
        "normalized_question": "lost voter id apply replacement pvc card online form 8 postal delivery ವೋಟರ್ ಐಡಿ ಕಳೆದುಹೋಗಿದೆ ಹೊಸ ಕಾರ್ಡ್",
        "answer": """### 🪪 ಕಳೆದುಹೋದ ವೋಟರ್ ಐಡಿ ಕಾರ್ಡ್ ಮರುಪಡೆಯುವುದು (Replacement PVC Voter ID)

ನಿಮ್ಮ ವೋಟರ್ ಐಡಿ ಕಳೆದುಹೋಗಿದ್ದರೆ, ಹರಿದುಹೋಗಿದ್ದರೆ ಅಥವಾ ಹಾಳಾಗಿದ್ದರೆ ಚುನಾವಣಾ ಆಯೋಗದಿಂದ ನೇರವಾಗಿ ಉಚಿತವಾಗಿ ಹೊಸ PVC ಸ್ಮಾರ್ಟ್ ಕಾರ್ಡ್ ಅನ್ನು ಮನೆ ವಿಳಾಸಕ್ಕೆ ಸ್ಪೀಡ್ ಪೋಸ್ಟ್ ಮೂಲಕ ಪಡೆಯಬಹುದು.

---

### 🚀 ಹಂತ-ಹಂತದ ವಿಧಾನ (Form 8):
1. **ECI ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [voters.eci.gov.in](https://voters.eci.gov.in) ಅಥವಾ **Voter Helpline App** ತೆರೆಯಿರಿ.
2. ಮೊಬೈಲ್ ನಂಬರ್ ಮೂಲಕ ಲಾಗಿನ್ ಆಗಿ **'Form 8'** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ EPIC (ವೋಟರ್ ಐಡಿ) ಸಂಖ್ಯೆ ನಮೂದಿಸಿ.
4. ಅಲ್ಲಿ ನೀಡಲಾದ ಆಯ್ಕೆಗಳಲ್ಲಿ **'Issue of Replacement EPIC without correction'** (ಯಾವುದೇ ತಿದ್ದುಪಡಿಯಿಲ್ಲದೆ ಬದಲಿ ಕಾರ್ಡ್) ಆಯ್ಕೆಮಾಡಿ.
5. ಕಾರ್ಡ್ ಮರುಕೋರಿಕೆಗೆ ಕಾರಣವನ್ನು (Lost / Destroyed due to reason like flood, fire, etc. / Mutilated) ಆಯ್ಕೆಮಾಡಿ.
   *(ಕಳೆದುಹೋಗಿದ್ದರೆ ಪೊಲೀಸ್ E-Lost ವರದಿ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ).*
6. ಅರ್ಜಿ ಸಬ್ಮಿಟ್ ಮಾಡಿ. 2 ರಿಂದ 4 ವಾರಗಳಲ್ಲಿ ಅಂಚೆ ಮೂಲಕ ಹೊಸ ಒರಿಜಿನಲ್ PVC ವೋಟರ್ ಕಾರ್ಡ್ ನಿಮ್ಮ ಮನೆ ಬಾಗಿಲಿಗೆ ಬರುತ್ತದೆ.

💡 ಕಾರ್ಡ್ ಬರುವವರೆಗೆ ತುರ್ತು ಬಳಕೆಗೆ ಇದೇ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ **'e-EPIC'** ಡಿಜಿಟಲ್ PDF ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.""",
        "category": "SIR",
        "language": "kn",
        "source_url": "https://voters.eci.gov.in",
        "keywords": "lost voter card, replacement pvc epic, voter id reprint, ವೋಟರ್ ಐಡಿ ಕಳೆದುಹೋಗಿದೆ, ಹೊಸ ವೋಟರ್ ಕಾರ್ಡ್",
        "action_label": "🪪 PVC ವೋಟರ್ ಕಾರ್ಡ್ ಅರ್ಜಿ",
        "action_url": "https://voters.eci.gov.in"
    },
    {
        "id": "faq_user_186",
        "question": "ನನ್ನ ವಾಹನದ ಮೇಲಿರುವ ಟ್ರಾಫಿಕ್ ಫೈನ್ (Traffic Fine) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಚೆಕ್ ಮಾಡಿ ಕಟ್ಟುವುದು ಹೇಗೆ?",
        "normalized_question": "check bangalore karnataka traffic fine challan online pay btp mparivahan ksp ಟ್ರಾಫಿಕ್ ಫೈನ್ ಚೆಕ್ ಆನ್‌ಲೈನ್ ಪಾವತಿ",
        "answer": """### 🚦 ಟ್ರಾಫಿಕ್ ಚಲನ್ (Traffic Violation Fine) ಪರಿಶೀಲನೆ & ಪಾವತಿ

ಬೆಂಗಳೂರು ಹಾಗೂ ಕರ್ನಾಟಕದ ಯಾವುದೇ ಜಿಲ್ಲೆಯಲ್ಲಿ ಸಂಚಾರ ನಿಯಮ ಉಲ್ಲಂಘನೆಗಾಗಿ ಕ್ಯಾಮೆರಾ ಅಥವಾ ಪೊಲೀಸರು ಹಾಕಿರುವ ಬಾಕಿ ದಂಡವನ್ನು ಮೊಬೈಲ್‌ನಲ್ಲೇ ಪರಿಶೀಲಿಸಿ ಪಾವತಿಸಬಹುದು.

---

### 📱 ಬೆಂಗಳೂರು ನಗರ ವಾಹನಗಳಿಗೆ (Bangalore City - BTP):
1. [btp.gov.in](https://btp.gov.in) ಅಥವಾ **Bangalore Traffic Police (BTP)** ಪೋರ್ಟಲ್ ಅಥವಾ **Karnataka One** ಗೆ ಭೇಟಿ ನೀಡಿ.
2. ನಿಮ್ಮ ವಾಹನದ ನೋಂದಣಿ ಸಂಖ್ಯೆ (ಉದಾ: KA01AB1234) ನಮೂದಿಸಿ.
3. ಸಂಚಾರ ಉಲ್ಲಂಘನೆಯ ಫೋಟೋ, ಸ್ಥಳ, ದಿನಾಂಕ ಮತ್ತು ದಂಡದ ಮೊತ್ತ ಕಾಣಿಸುತ್ತದೆ.
4. UPI (Google Pay, PhonePe, Paytm) ಅಥವಾ ನೆಟ್ ಬ್ಯಾಂಕಿಂಗ್ ಮೂಲಕ ತಕ್ಷಣ ಪಾವತಿಸಿ ರಶೀದಿ ಪಡೆಯಿರಿ.

---

### 🏍️ ಇಡೀ ಕರ್ನಾಟಕದ ಇತರ ಜಿಲ್ಲೆಗಳಿಗೆ:
* [ksp.karnataka.gov.in](https://ksp.karnataka.gov.in) ಅಥವಾ ಕೇಂದ್ರ ಸರ್ಕಾರದ **Parivahan e-Challan** ([echallan.parivahan.gov.in](https://echallan.parivahan.gov.in)) ನಲ್ಲಿ ವಾಹನ ಸಂಖ್ಯೆ ಮತ್ತು ಚಾಸಿಸ್ ಸಂಖ್ಯೆಯ ಕೊನೆಯ 5 ಅಂಕಿ ಹಾಕಿ ದಂಡ ಪಾವತಿಸಬಹುದು.""",
        "category": "TRANSPORT",
        "language": "kn",
        "source_url": "https://echallan.parivahan.gov.in",
        "keywords": "traffic fine check, btp echallan, pay traffic violation fine karnataka, ಟ್ರಾಫಿಕ್ ಫೈನ್ ಚೆಕ್, ಚಲನ್ ಪಾವತಿ",
        "action_label": "🚦 ಟ್ರಾಫಿಕ್ ಫೈನ್ ಪೋರ್ಟಲ್",
        "action_url": "https://echallan.parivahan.gov.in"
    },
    {
        "id": "faq_user_187",
        "question": "ಪಹಣಿಯಲ್ಲಿ (Bhoomi RTC) ಹೆಸರು ತಪ್ಪಾಗಿದ್ದರೆ ಅಥವಾ ಅಕ್ಷರ ದೋಷವಿದ್ದರೆ ಸರಿಪಡಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "bhoomi rtc name correction spelling mistake pahani durasti online ಪಹಣಿ ಹೆಸರು ತಿದ್ದುಪಡಿ ಅಕ್ಷರ ದೋಷ",
        "answer": """### 🌾 ಪಹಣಿ / RTC ಯಲ್ಲಿ ಹೆಸರು ಮತ್ತು ವಿಸ್ತೀರ್ಣ ತಿದ್ದುಪಡಿ ಮಾಡುವ ವಿಧಾನ

ಭೂಮಿ ಪೋರ್ಟಲ್‌ನಲ್ಲಿರುವ ಪಹಣಿಯಲ್ಲಿ ಮಾಲೀಕರ ಹೆಸರು ತಪ್ಪಾಗಿದ್ದರೆ, ಕಾಗುಣಿತ ದೋಷವಿದ್ದರೆ ಅಥವಾ ಆಧಾರ್ ಕಾರ್ಡ್‌ನಲ್ಲಿರುವಂತೆ ಹೊಂದಾಣಿಕೆಯಾಗದಿದ್ದರೆ ಅದನ್ನು ಸರಿಪಡಿಸಲು ಕಂದಾಯ ಇಲಾಖೆಯ ನಿಯಮಾವಳಿ:

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
* ಮೂಲ ಕ್ರಯಪತ್ರ (Registered Sale Deed) ಅಥವಾ ಮಂಜೂರಾತಿ ಆದೇಶದ ಪ್ರತಿ.
* ಅರ್ಜಿದಾರರ ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ವೋಟರ್ ಐಡಿ.
* ಚಾಲ್ತಿ ಸಾಲಿನ ಪಹಣಿ (RTC) ಮತ್ತು ಮ್ಯುಟೇಶನ್ ಪ್ರತಿ (MR Extract).

---

### 🛠️ ಅರ್ಜಿ ಸಲ್ಲಿಕೆಯ ವಿಧಾನ:
1. **ಕಂದಾಯ ಅದಾಲತ್ / ಗ್ರಾಮ ಒನ್:** ಗ್ರಾಮ ಒನ್ ಅಥವಾ ತಾಲೂಕು ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿಯ ಕಂದಾಯ ಶಾಖೆಗೆ **'ಪಹಣಿ ಅಕ್ಷರ ದೋಷ ತಿದ್ದುಪಡಿ' (Clerical Name Correction)** ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.
2. **ಭೂಮಿ ತಂತ್ರಾಂಶದ ಆನ್‌ಲೈನ್ ಅರ್ಜಿ:** [bhoomi.karnataka.gov.in](https://bhoomi.karnataka.gov.in) ನಲ್ಲಿ 'Citizen Services -> RTC Name Correction' ಮೂಲಕ ಮೂಲ ನೋಂದಾಯಿತ ದಾಖಲೆಗಳನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
3. ಗ್ರಾಮ ಆಡಳಿತಾಧಿಕಾರಿ (VA) ಮತ್ತು ಕಂದಾಯ ನಿರೀಕ್ಷಕರು (RI) ಮೂಲ ಕ್ರಯಪತ್ರ ಪರಿಶೀಲಿಸಿ 15 ರಿಂದ 30 ದಿನಗಳಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಡಿಜಿಟಲ್ ಸಹಿಯೊಂದಿಗೆ ಪಹಣಿಯನ್ನು ನವೀಕರಿಸುತ್ತಾರೆ.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://bhoomi.karnataka.gov.in",
        "keywords": "rtc name correction, bhoomi spelling mistake, pahani durasti, ಪಹಣಿ ಹೆಸರು ತಿದ್ದುಪಡಿ, ಭೂಮಿ ದಾಖಲೆ",
        "action_label": "🌾 ಭೂಮಿ ತಿದ್ದುಪಡಿ ಸೇವೆ",
        "action_url": "https://bhoomi.karnataka.gov.in"
    },
    {
        "id": "faq_user_188",
        "question": "ಗೃಹಲಕ್ಷ್ಮಿ ₹2,000 ಹಣ ಯಾವ ತಿಂಗಳವರೆಗೂ ಜಮೆಯಾಗಿದೆ ಎಂದು ಮೊಬೈಲ್‌ನಲ್ಲೇ ಚೆಕ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "how to check gruha lakshmi credited months passbook dbt karnataka app ಗೃಹಲಕ್ಷ್ಮಿ ಹಣ ಚೆಕ್",
        "answer": """### 🌸 ಗೃಹಲಕ್ಷ್ಮಿ ಮಾಸಿಕ ಕಂತುಗಳ ಸ್ಥಿತಿ ಪರಿಶೀಲನೆ (DBT Status Tracking)

ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆಯ ₹2,000 ಹಣ ಪ್ರತಿ ತಿಂಗಳು ಯಾವ ದಿನಾಂಕದಂದು ಯಾವ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾಗಿದೆ ಎಂಬುದನ್ನು ತಿಳಿಯುವ ವಿಧಾನ:

---

### 📱 1. DBT Karnataka App ಮೂಲಕ (ಅತ್ಯಂತ ಸುಲಭ):
1. ಗೂಗಲ್ ಪ್ಲೇ ಸ್ಟೋರ್‌ನಿಂದ **'DBT Karnataka'** ಆ್ಯಪ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ.
2. ಫಲಾನುಭವಿ ಮಹಿಳೆಯ **12 ಅಂಕಿಗಳ ಆಧಾರ್ ಸಂಖ್ಯೆ** ಹಾಕಿ OTP ಮೂಲಕ mPIN ಸೆಟ್ ಮಾಡಿ.
3. ಮುಖಪುಟದಲ್ಲಿ **'Payment Status'** ಆಯ್ಕೆಮಾಡಿ.
4. **'Gruha Lakshmi'** ಯೋಜನೆ ಮೇಲೆ ಕ್ಲಿಕ್ ಮಾಡಿದರೆ, ಪ್ರತಿಯೊಂದು ತಿಂಗಳ ಜಮೆಯಾದ ಹಣ, ದಿನಾಂಕ, ಬ್ಯಾಂಕ್ ಹೆಸರು ಮತ್ತು UTR ಸಂಖ್ಯೆ ಲೈವ್ ಆಗಿ ಕಾಣಿಸುತ್ತದೆ.

---

### 🌐 2. ಸೇವಾ ಸಿಂಧು ಗ್ಯಾರಂಟಿ ಪೋರ್ಟಲ್ ಮೂಲಕ:
* [sevasindhugs.karnataka.gov.in](https://sevasindhugs.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ ರೇಷನ್ ಕಾರ್ಡ್ ಸಂಖ್ಯೆ ಹಾಕಿ ನೇರ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಬಹುದು.""",
        "category": "SCHEME",
        "language": "kn",
        "source_url": "https://sevasindhugs.karnataka.gov.in",
        "keywords": "gruha lakshmi payment status, dbt karnataka app check, ಗೃಹಲಕ್ಷ್ಮಿ ಹಣ ಬಂದಿದೆಯಾ ಚೆಕ್, ಡಿಬಿಟಿ ಸ್ಟೇಟಸ್",
        "action_label": "🌸 DBT ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಿ",
        "action_url": "/guarantee-schemes.html"
    },
    {
        "id": "faq_user_189",
        "question": "ಆಧಾರ್ ಕಾರ್ಡ್‌ಗೆ ಯಾವ ಮೊಬೈಲ್ ನಂಬರ್ ಲಿಂಕ್ ಆಗಿದೆ ಎಂದು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಚೆಕ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "check aadhaar mobile number link status verify email mobile uidai online ಆಧಾರ್ ಮೊಬೈಲ್ ನಂಬರ್ ಲಿಂಕ್",
        "answer": """### 🔍 ಆಧಾರ್ ಕಾರ್ಡ್ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಪರಿಶೀಲನೆ (UIDAI Online Verification)

ಯಾವುದೇ ಸರ್ಕಾರಿ ಸೌಲಭ್ಯ, ಗ್ಯಾರಂಟಿ ಯೋಜನೆ ಅಥವಾ ಇ-ಕೆವೈಸಿ ಮಾಡಲು ನಿಮ್ಮ ಆಧಾರ್‌ಗೆ ಚಾಲ್ತಿಯಲ್ಲಿರುವ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಲಿಂಕ್ ಆಗಿರುವುದು ಕಡ್ಡಾಯ.

---

### 💻 ಚೆಕ್ ಮಾಡುವ ಹಂತಗಳು:
1. **ಅಧಿಕೃತ UIDAI ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [myaadhaar.uidai.gov.in](https://myaadhaar.uidai.gov.in)
2. ಮುಖಪುಟದಲ್ಲಿರುವ **'Check Aadhaar Validity'** ಅಥವಾ **'Verify Mobile Number'** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ **12 ಅಂಕಿಗಳ ಆಧಾರ್ ಸಂಖ್ಯೆ** ಮತ್ತು ಕ್ಯಾಪ್ಚಾ (Captcha) ಕೋಡ್ ನಮೂದಿಸಿ.
4. ಪರದೆಯ ಮೇಲೆ ನಿಮ್ಮ ವಯಸ್ಸಿನ ಮಿತಿ, ಲಿಂಗ, ರಾಜ್ಯ ಮತ್ತು ನಿಮ್ಮ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಯ **ಕೊನೆಯ 3 ಅಂಕಿಗಳು (ಉದಾ: *******789)** ಕಾಣಿಸುತ್ತವೆ.

⚠️ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಲಿಂಕ್ ಆಗಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ಹಳೆಯ ನಂಬರ್ ಬದಲಾಗಿದ್ದರೆ, ಸಮೀಪದ ಆಧಾರ್ ಸೇವಾ ಕೇಂದ್ರ ಅಥವಾ ಅಂಚೆ ಕಚೇರಿಗೆ ತೆರಳಿ ಬಯೋಮೆಟ್ರಿಕ್ ಮೂಲಕ ಲಿಂಕ್ ಮಾಡಿಸಿಕೊಳ್ಳಬೇಕು.""",
        "category": "CERTIFICATES",
        "language": "kn",
        "source_url": "https://myaadhaar.uidai.gov.in",
        "keywords": "check aadhaar mobile link, uidai verify mobile, myaadhaar status, ಆಧಾರ್ ಮೊಬೈಲ್ ಲಿಂಕ್ ಚೆಕ್, ಆಧಾರ್ ಕಾರ್ಡ್",
        "action_label": "🔍 UIDAI ಪೋರ್ಟಲ್",
        "action_url": "https://myaadhaar.uidai.gov.in"
    },
    {
        "id": "faq_user_190",
        "question": "ಜಮೀನಿನ ಗಡಿ ಗುರುತಿಸಲು ಹದ್ದುಬಸ್ತು ಸರ್ವೆಗೆ (Haddubasthu Survey) ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಹಾಕುವುದು ಹೇಗೆ?",
        "normalized_question": "haddubasthu land boundary survey application mojini karnataka ಹದ್ದುಬಸ್ತು ಸರ್ವೆ ಅರ್ಜಿ ಗಡಿ ಗುರುತು",
        "answer": """### 📐 ಹದ್ದುಬಸ್ತು ಸರ್ವೆ (Haddubasthu / Boundary Demarcation Survey)

ಪಕ್ಕದ ಜಮೀನಿನವರೊಂದಿಗೆ ಗಡಿ ತಕರಾರು ಇದ್ದಾಗ ಅಥವಾ ಸ್ವಂತ ಜಮೀನಿನ ನಿಖರ ಗಡಿಯನ್ನು ಸರ್ಕಾರಿ ಭೂಮಾಪಕರಿಂದ ಅಳೆದು ಕಲ್ಲು ನೆಡಿಸಲು **ಹದ್ದುಬಸ್ತು ಸರ್ವೆ** ಮಾಡಿಸಲಾಗುತ್ತದೆ.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
1. ಚಾಲ್ತಿ ಸಾಲಿನ ಪಹಣಿ (RTC) ಮತ್ತು ಮ್ಯುಟೇಶನ್ ಪ್ರತಿ (MR Extract).
2. ಕ್ರಯಪತ್ರ ಅಥವಾ ಹಕ್ಕುಪತ್ರದ ಪ್ರತಿ.
3. ಅರ್ಜಿದಾರರ ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ಜಮೀನಿನ ಅಕ್ಕಪಕ್ಕದ ರೈತರ (ಪಕ್ಕದ ಸರ್ವೆ ನಂಬರ್ ಮಾಲೀಕರ) ಹೆಸರು ಮತ್ತು ವಿಳಾಸ.

---

### 💻 ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಹಂತಗಳು:
1. [mojini.karnataka.gov.in](https://mojini.karnataka.gov.in) ಅಥವಾ ನಿಮ್ಮ ಹತ್ತಿರದ ಗ್ರಾಮ ಒನ್ / ನಾಡಕಚೇರಿಗೆ ತೆರಳಿ.
2. **'Haddubasthu Application'** ಆಯ್ಕೆಮಾಡಿ ಸರ್ವೆ ನಂಬರ್ ವಿವರ ದಾಖಲಿಸಿ.
3. ನಿಗದಿತ ಸರ್ಕಾರಿ ಸರ್ವೆ ಶುಲ್ಕ (ಎಕರೆಗೆ ತಕ್ಕಂತೆ) ಆನ್‌ಲೈನ್ ಪಾವತಿಸಿ.
4. ಕಂದಾಯ ಇಲಾಖೆಯ ಭೂಮಾಪಕರು ಪಕ್ಕದ ಜಮೀನಿನವರಿಗೆ ಮುಂಚಿತವಾಗಿ ನೋಟಿಸ್ ನೀಡಿ ಸ್ಥಳಕ್ಕೆ ಬಂದು ಇಟಿಎಸ್ (ETS) ಯಂತ್ರದ ಮೂಲಕ ಜಮೀನು ಅಳೆದು ಗಡಿ ನಿಗದಿಪಡಿಸುತ್ತಾರೆ.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://mojini.karnataka.gov.in",
        "keywords": "haddubasthu survey, land boundary dispute, mojini survey application, ಹದ್ದುಬಸ್ತು ಸರ್ವೆ, ಗಡಿ ಗುರುತು, ಭೂ ಅಳತೆ",
        "action_label": "📐 ಮೋಜಿನಿ ಸರ್ವೆ ಸೇವೆ",
        "action_url": "https://mojini.karnataka.gov.in"
    },
    {
        "id": "faq_user_191",
        "question": "ಗೃಹಜ್ಯೋತಿ ಯೋಜನೆಯಲ್ಲಿ 200 ಯೂನಿಟ್ ಮೀರಿದರೆ ಬಿಲ್ ಎಷ್ಟು ಬರುತ್ತದೆ? ಲೆಕ್ಕ ಹೇಗೆ?",
        "normalized_question": "what happens if electricity consumption exceeds 200 units gruha jyothi calculation 200 ಯೂನಿಟ್ ದಾಟಿದರೆ ಬಿಲ್",
        "answer": """### ⚡ ಗೃಹಜ್ಯೋತಿ — 200 ಯೂನಿಟ್ ಮೀರಿದಾಗ ಬಿಲ್ಲಿಂಗ್ ನಿಯಮಗಳು

ಗೃಹಜ್ಯೋತಿ ಯೋಜನೆಯಡಿ ತಿಂಗಳಿಗೆ ಗರಿಷ್ಠ 200 ಯೂನಿಟ್‌ವರೆಗೆ ಮಾತ್ರ ರಿಯಾಯಿತಿ ಸೌಲಭ್ಯ ಅನ್ವಯಿಸುತ್ತದೆ.

---

### 📊 ಬಳಕೆಯ 3 ಸಂದರ್ಭಗಳ ನಿಖರ ಲೆಕ್ಕಾಚಾರ:
1. **ಅರ್ಹತಾ ಮಿತಿಯೊಳಗೆ ಬಳಸಿದರೆ (ಉದಾ: ನಿಮ್ಮ ಮಿತಿ 120 ಯೂನಿಟ್, ಬಳಕೆ 110 ಯೂನಿಟ್):** ಸಂಪೂರ್ಣ **ಶೂನ್ಯ ಬಿಲ್ (Zero Bill - ₹0)** ಬರುತ್ತದೆ.
2. **ಅರ್ಹತಾ ಮಿತಿ ಮೀರಿ ಆದರೆ 200 ಯೂನಿಟ್‌ಗಿಂತ ಕಡಿಮೆ ಬಳಸಿದರೆ (ಉದಾ: ನಿಮ್ಮ ಮಿತಿ 120 ಯೂನಿಟ್, ಬಳಕೆ 160 ಯೂನಿಟ್):** ನೀವು ಬಳಸಿದ ಹೆಚ್ಚುವರಿ **40 ಯೂನಿಟ್‌ಗೆ ಮಾತ್ರ** ಸರ್ಕಾರ ನಿಗದಿಪಡಿಸಿದ ದರದಲ್ಲಿ ಬಿಲ್ ಪಾವತಿಸಬೇಕು.
3. **200 ಯೂನಿಟ್‌ಗಿಂತ ಹೆಚ್ಚು ಬಳಸಿದರೆ (ಉದಾ: ಬಳಕೆ 205 ಅಥವಾ 220 ಯೂನಿಟ್):** ನಿಮಗೆ **ಯಾವುದೇ ಸಬ್ಸಿಡಿ ಸಿಗುವುದಿಲ್ಲ**. ಆ ತಿಂಗಳು ಬಳಸಿದ ಎಲ್ಲಾ 205 ಯೂನಿಟ್‌ಗಳ ಪೂರ್ಣ ವಿದ್ಯುತ್ ದರ, ಫಿಕ್ಸ್ಡ್ ಚಾರ್ಜಸ್ ಹಾಗೂ ಇಂಧನ ಹೊಂದಾಣಿಕೆ ಶುಲ್ಕವನ್ನು (FAC) ನೀವೇ ಪೂರ್ಣವಾಗಿ ಪಾವತಿಸಬೇಕು.

💡 ಆದ್ದರಿಂದ ಪ್ರತಿ ತಿಂಗಳು ನಿಮ್ಮ ವಿದ್ಯುತ್ ಬಳಕೆ 200 ಯೂನಿಟ್‌ ಮೀರದಂತೆ ನಿಗಾ ವಹಿಸಿ.""",
        "category": "SCHEME",
        "language": "kn",
        "source_url": "https://sevasindhugs.karnataka.gov.in",
        "keywords": "gruha jyothi bill calculation, exceeds 200 units power bill, ಗೃಹಜ್ಯೋತಿ ಬಿಲ್ ಲೆಕ್ಕ, 200 ಯೂನಿಟ್ ಜಾಸ್ತಿ ಬಿಲ್",
        "action_label": "⚡ ಗ್ಯಾರಂಟಿ ವಿವರ ನೋಡಿ",
        "action_url": "/guarantee-schemes.html"
    },
    {
        "id": "faq_user_192",
        "question": "ನಾಡಕಚೇರಿಯ ಯಾವುದೇ ಪ್ರಮಾಣಪತ್ರದ RD ಸಂಖ್ಯೆಯ ಸ್ಥಿತಿ (RD Number Status) ಮೊಬೈಲ್‌ನಲ್ಲೇ ನೋಡುವುದು ಹೇಗೆ?",
        "normalized_question": "nadakacheri rd number status check caste income certificate online track ಆರ್‌ಡಿ ನಂಬರ್ ಚೆಕ್",
        "answer": """### 📑 ನಾಡಕಚೇರಿ RD ನಂಬರ್ ಅಪ್ಲಿಕೇಶನ್ ಸ್ಟೇಟಸ್ ಪರಿಶೀಲನೆ

ಜಾತಿ, ಆದಾಯ, ವಾಸಸ್ಥಳ ಅಥವಾ ವಿಧವಾ ವೇತನಕ್ಕೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿದಾಗ ಸಿಗುವ **RD ಸಂಖ್ಯೆ (ಉದಾ: RD00384729101)** ಮೂಲಕ ಪ್ರಮಾಣಪತ್ರ ಅನುಮೋದನೆಯಾಗಿದೆಯೇ ಎಂದು ತಿಳಿಯುವ ವಿಧಾನ:

---

### 🔍 ಪರಿಶೀಲಿಸುವ ಹಂತಗಳು:
1. [nadakacheri.karnataka.gov.in](https://nadakacheri.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ.
2. ಮುಖಪುಟದಲ್ಲಿ **'Application Status' (ಅರ್ಜಿ ಸ್ಥಿತಿ)** ಲಿಂಕ್ ಕ್ಲಿಕ್ ಮಾಡಿ.
3. ನಿಮ್ಮ **Application Number (RD Number)** ನಮೂದಿಸಿ 'Fetch Details' ಕ್ಲಿಕ್ ಮಾಡಿ.
4. **ಹಂತಗಳ ವಿವರಗಳು ಲಭ್ಯವಾಗುತ್ತವೆ:**
   - ಗ್ರಾಮ ಆಡಳಿತಾಧಿಕಾರಿ (VA) ಪರಿಶೀಲನೆ.
   - ಕಂದಾಯ ನಿರೀಕ್ಷಕರ (RI) ರಿಪೋರ್ಟ್.
   - ತಹಶೀಲ್ದಾರ್ ಅನುಮೋದನೆ (Approved / Rejected).
5. 'Approved' ಎಂದು ಬಂದ ತಕ್ಷಣ ಅಲ್ಲಿಯೇ **'Print Certificate'** ಕ್ಲಿಕ್ ಮಾಡಿ ಅಧಿಕೃತ ಪ್ರಮಾಣಪತ್ರವನ್ನು ನೇರವಾಗಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.""",
        "category": "CERTIFICATES",
        "language": "kn",
        "source_url": "https://nadakacheri.karnataka.gov.in",
        "keywords": "nadakacheri application status, check rd number online, download caste certificate, ಆರ್‌ಡಿ ನಂಬರ್ ಸ್ಟೇಟಸ್, ನಾಡಕಚೇರಿ",
        "action_label": "📑 RD ಸ್ಟೇಟಸ್ ಪರಿಶೀಲಿಸಿ",
        "action_url": "https://nadakacheri.karnataka.gov.in"
    },
    {
        "id": "faq_user_193",
        "question": "ಆಯುಷ್ಮಾನ್ ಕಾರ್ಡ್ (PMJAY / Arogya Karnataka Card) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "download ayushman card online beneficiary pmjay bis portal pdf ಆಯುಷ್ಮಾನ್ ಕಾರ್ಡ್ ಡೌನ್‌ಲೋಡ್",
        "answer": """### 🏥 ಆಯುಷ್ಮಾನ್ ಭಾರತ್ PMJAY ಗೋಲ್ಡನ್ ಕಾರ್ಡ್ ಡೌನ್‌ಲೋಡ್

₹5 ಲಕ್ಷದವರೆಗೆ ಉಚಿತ ಚಿಕಿತ್ಸೆ ನೀಡುವ ಅಧಿಕೃತ ಆಯುಷ್ಮಾನ್ ಕಾರ್ಡ್ ಅನ್ನು ನಿಮ್ಮ ಮೊಬೈಲ್‌ನಲ್ಲೇ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.

---

### 📥 ಡೌನ್‌ಲೋಡ್ ಮಾಡುವ ಹಂತಗಳು:
1. **ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [beneficiary.nha.gov.in](https://beneficiary.nha.gov.in)
2. **'Beneficiary'** ಆಯ್ಕೆಮಾಡಿ ನಿಮ್ಮ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಮತ್ತು OTP ಹಾಕಿ ಲಾಗಿನ್ ಆಗಿ.
3. ರಾಜ್ಯವನ್ನು **'Karnataka'**, ಯೋಜನೆಯನ್ನು **'PMJAY'** ಮತ್ತು ಜಿಲ್ಲೆ ಆಯ್ಕೆಮಾಡಿ.
4. ನಿಮ್ಮ **ಆಧಾರ್ ಸಂಖ್ಯೆ** ಅಥವಾ **ರೇಷನ್ ಕಾರ್ಡ್ ಸಂಖ್ಯೆ** ನಮೂದಿಸಿ ಹುಡುಕಿ.
5. ನಿಮ್ಮ ಕುಟುಂಬದ ಎಲ್ಲಾ ಸದಸ್ಯರ ಹೆಸರುಗಳು ಕಾಣಿಸುತ್ತವೆ. ಇ-ಕೆವೈಸಿ ಪೂರ್ಣಗೊಂಡಿರುವ ಹೆಸರಿನ ಪಕ್ಕದಲ್ಲಿರುವ **'Download Card'** ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ ಆಧಾರ್ ಒಟಿಪಿ ದೃಢೀಕರಿಸಿ ಅಧಿಕೃತ PVC ಮಾದರಿಯ ಆಯುಷ್ಮಾನ್ ಕಾರ್ಡ್ PDF ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಿ.""",
        "category": "HEALTH",
        "language": "kn",
        "source_url": "https://beneficiary.nha.gov.in",
        "keywords": "ayushman card download pdf, beneficiary nha gov in, pmjay arogya karnataka card, ಆಯುಷ್ಮಾನ್ ಕಾರ್ಡ್ ಡೌನ್‌ಲೋಡ್",
        "action_label": "🏥 ಆಯುಷ್ಮಾನ್ ಪೋರ್ಟಲ್",
        "action_url": "https://beneficiary.nha.gov.in"
    },
    {
        "id": "faq_user_194",
        "question": "ಬೆಂಗಳೂರಿನಲ್ಲಿ ಕಾವೇರಿ ನೀರಿನ ಹೊಸ ಸಂಪರ್ಕಕ್ಕೆ (BWSSB New Water Connection) ಅರ್ಜಿ ಹಾಕುವುದು ಹೇಗೆ?",
        "normalized_question": "bwssb new water connection online apply bangalore sajala portal ಬೆಂಗಳೂರು ಕಾವೇರಿ ನೀರು ಸಂಪರ್ಕ",
        "answer": """### 🚰 BWSSB ಕಾವೇರಿ ಕುಡಿಯುವ ನೀರಿನ ಹೊಸ ಸಂಪರ್ಕ (Sajala Portal)

ಬೆಂಗಳೂರು ಜಲ ಮಂಡಳಿಯ (BWSSB) ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಹೊಸ ಮನೆ ಅಥವಾ ಅಪಾರ್ಟ್‌ಮೆಂಟ್‌ಗಳಿಗೆ ಕುಡಿಯುವ ನೀರು ಮತ್ತು ಒಳಚರಂಡಿ (Sanitary) ಸಂಪರ್ಕ ಪಡೆಯುವ ವಿಧಾನ:

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
* ಆಸ್ತಿಯ BBMP ಇ-ಖಾತಾ ಪ್ರತಿ ಮತ್ತು ಇತ್ತೀಚಿನ ಆಸ್ತಿ ತೆರಿಗೆ ಪಾವತಿ ರಶೀದಿ.
* ಅನುಮೋದಿತ ಕಟ್ಟಡ ನಕ್ಷೆ (Sanctioned Building Plan).
* ಆಸ್ತಿಯ ಕ್ರಯಪತ್ರ (Sale Deed) ಮತ್ತು ಮಾಲೀಕರ ಆಧಾರ್ ಕಾರ್ಡ್.

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಪ್ರಕ್ರಿಯೆ:
1. [bwssb.karnataka.gov.in](https://bwssb.karnataka.gov.in) ನಲ್ಲಿರುವ **'Sajala 2.0'** ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ.
2. ಅರ್ಜಿದಾರರ ವಿವರ ಹಾಗೂ ನಿವೇಶನದ ವಿಸ್ತೀರ್ಣ (Built-up Area) ನಮೂದಿಸಿ ದಾಖಲೆಗಳನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
3. ಜಲ ಮಂಡಳಿಯ ಸಹಾಯಕ ಕಾರ್ಯಪಾಲಕ ಇಂಜಿನಿಯರ್ (AEE) ಸ್ಥಳ ಪರಿಶೀಲನೆ ನಡೆಸಿ ಅಂದಾಜು ಮೊತ್ತದ (Estimation Demand Note) ಚಲನ್ ನೀಡುತ್ತಾರೆ.
4. ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಶುಲ್ಕ ಪಾವತಿಸಿದ ನಂತರ ಅಧಿಕೃತ ಪೈಪ್‌ಲೈನ್ ಮೀಟರ್ ಸಂಪರ್ಕ ಕಲ್ಪಿಸಲಾಗುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bwssb.karnataka.gov.in",
        "keywords": "bwssb new water connection, sajala portal, kaveri water connection online, ಕಾವೇರಿ ನೀರು ಸಂಪರ್ಕ, ಜಲ ಮಂಡಳಿ",
        "action_label": "🚰 BWSSB ಪೋರ್ಟಲ್",
        "action_url": "https://bwssb.karnataka.gov.in"
    },
    {
        "id": "faq_user_195",
        "question": "ಕರ್ನಾಟಕದಲ್ಲಿ ಪಾಸ್‌ಪೋರ್ಟ್ (Passport) ಮಾಡಿಸಲು ಆನ್‌ಲೈನ್ ಸ್ಲಾಟ್ ಬುಕಿಂಗ್ ಮತ್ತು ಪೊಲೀಸ್ ವೆರಿಫಿಕೇಶನ್ ಹೇಗೆ?",
        "normalized_question": "apply passport online passport seva kendra bangalore psk appointment ಪೊಲೀಸ್ ವೆರಿಫಿಕೇಶನ್ ಪಾಸ್‌ಪೋರ್ಟ್",
        "answer": """### 🛂 ಪಾಸ್‌ಪೋರ್ಟ್ ಸೇವಾ ಕೇಂದ್ರ (Passport Seva Kendra - PSK Karnataka) ಅರ್ಜಿ ವಿಧಾನ

ವಿದೇಶ ಪ್ರಯಾಣಕ್ಕಾಗಿ ಭಾರತೀಯ ಪಾಸ್‌ಪೋರ್ಟ್ ಪಡೆಯಲು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ಸಮೀಪದ ಪಾಸ್‌ಪೋರ್ಟ್ ಸೇವಾ ಕೇಂದ್ರಕ್ಕೆ (ಬೆಂಗಳೂರು, ಮಂಗಳೂರು, ಹುಬ್ಬಳ್ಳಿ, ಮೈಸೂರು, ಕಲಬುರಗಿ, ಬೆಳಗಾವಿ ಇತ್ಯಾದಿ) ಅಪಾಯಿಂಟ್‌ಮೆಂಟ್ ಬುಕ್ ಮಾಡಬಹುದು.

---

### 📋 ಅಗತ್ಯ ಮೂಲ ದಾಖಲೆಗಳು:
* **ವಿಳಾಸದ ಪುರಾವೆ:** ಆಧಾರ್ ಕಾರ್ಡ್ / ವಿದ್ಯುತ್ ಬಿಲ್ / ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್.
* **ಜನ್ಮ ದಿನಾಂಕದ ಪುರಾವೆ:** SSLC ಅಂಕಪಟ್ಟಿ / ಜನನ ಪ್ರಮಾಣಪತ್ರ / ಪ್ಯಾನ್ ಕಾರ್ಡ್.
* **ಶೈಕ್ಷಣಿಕ ಅರ್ಹತೆ (ECNR ಗಾಗಿ):** 10 ನೇ ತರಗತಿ ಅಥವಾ ಪದವಿ ಪ್ರಮಾಣಪತ್ರ (Non-ECR ಪಾಸ್‌ಪೋರ್ಟ್‌ಗಾಗಿ).

---

### 🚀 ಪ್ರಕ್ರಿಯೆ:
1. [passportindia.gov.in](https://passportindia.gov.in) ನಲ್ಲಿ ನೋಂದಾಯಿಸಿ **'Apply for Fresh Passport'** ಭರ್ತಿ ಮಾಡಿ.
2. ₹1,500 ಸಾಮಾನ್ಯ ಶುಲ್ಕ (ತತ್ಕಾಲ್ ಆಗಿದ್ದರೆ ₹3,500) ಪಾವತಿಸಿ PSK ಕೇಂದ್ರಕ್ಕೆ ದಿನಾಂಕ ಮತ್ತು ಸಮಯದ ಸ್ಲಾಟ್ ಬುಕ್ ಮಾಡಿ.
3. ನಿಗದಿತ ದಿನದಂದು PSK ಕೇಂದ್ರಕ್ಕೆ ತೆರಳಿ ಬಯೋಮೆಟ್ರಿಕ್ ಫಿಂಗರ್‌ಪ್ರಿಂಟ್ ಮತ್ತು ಫೋಟೋ ನೀಡಿ.
4. ಸ್ಥಳೀಯ ಠಾಣೆಯ ಪೊಲೀಸರು ನಿಮ್ಮ ಮನೆಗೆ ಬಂದು ವಿಳಾಸ ಪರಿಶೀಲನೆ (Police Verification) ನಡೆಸಿದ 7-10 ದಿನಗಳಲ್ಲಿ ಪಾಸ್‌ಪೋರ್ಟ್ ಸ್ಪೀಡ್ ಪೋಸ್ಟ್ ಮೂಲಕ ಮನೆಗೆ ತಲುಪುತ್ತದೆ.""",
        "category": "PASSPORT",
        "language": "kn",
        "source_url": "https://passportindia.gov.in",
        "keywords": "passport apply online karnataka, psk bangalore appointment, passport police verification, ಪಾಸ್‌ಪೋರ್ಟ್ ಅರ್ಜಿ, ಪಾಸ್‌ಪೋರ್ಟ್ ಸೇವಾ ಕೇಂದ್ರ",
        "action_label": "🛂 ಪಾಸ್‌ಪೋರ್ಟ್ ಪೋರ್ಟಲ್",
        "action_url": "https://passportindia.gov.in"
    },
    {
        "id": "faq_user_196",
        "question": "ಸರ್ಕಾರಿ ಶಾಲೆಗಳಲ್ಲಿ 1 ನೇ ತರಗತಿ ಮತ್ತು LKG/UKG ಪ್ರವೇಶಕ್ಕೆ (SATS Admission) ಮಗುವಿನ ವಯಸ್ಸಿನ ಮಿತಿ ಎಷ್ಟು?",
        "normalized_question": "school admission age limit karnataka class 1 sats lkg ukg ಶಾಲೆ ಪ್ರವೇಶ ವಯಸ್ಸಿನ ಮಿತಿ",
        "answer": """### 🏫 ಕರ್ನಾಟಕ ಶಾಲಾ ಶಿಕ್ಷಣ ಇಲಾಖೆ — ಪ್ರವೇಶ ವಯೋಮಿತಿ ನಿಯಮಗಳು (SATS Karnataka)

ರಾಜ್ಯದ ಸರ್ಕಾರಿ, ಅನುದಾನಿತ ಮತ್ತು ಖಾಸಗಿ ಶಾಲೆಗಳಲ್ಲಿ ಮಕ್ಕಳ ಪ್ರವೇಶಕ್ಕೆ ರಾಷ್ಟ್ರೀಯ ಶಿಕ್ಷಣ ನೀತಿ (NEP) ಮತ್ತು ಶಾಲಾ ಶಿಕ್ಷಣ ಇಲಾಖೆಯು ನಿಗದಿಪಡಿಸಿರುವ ವಯಸ್ಸಿನ ಮಿತಿ:

---

### 👶 ತರಗತಿವಾರು ವಯಸ್ಸಿನ ಮಾನದಂಡ (ಜೂನ್ 1 ಕ್ಕೆ ಅನ್ವಯವಾಗುವಂತೆ):
* **LKG ಪ್ರವೇಶಕ್ಕೆ:** ಮಗುವಿಗೆ ಕನಿಷ್ಠ **4 ವರ್ಷ** ತುಂಬಿರಬೇಕು.
* **UKG ಪ್ರವೇಶಕ್ಕೆ:** ಮಗುವಿಗೆ ಕನಿಷ್ಠ **5 ವರ್ಷ** ತುಂಬಿರಬೇಕು.
* **1 ನೇ ತರಗತಿ (Class 1) ಪ್ರವೇಶಕ್ಕೆ:** ಜೂನ್ 1 ನೇ ತಾರೀಖಿನ ವೇಳೆಗೆ ಮಗುವಿಗೆ ಕಡ್ಡಾಯವಾಗಿ **6 ವರ್ಷ ಪೂರ್ಣಗೊಂಡಿರಬೇಕು (6+ Years)**.

---

### 📋 ಪ್ರವೇಶಕ್ಕೆ ಅಗತ್ಯವಿರುವ ದಾಖಲೆಗಳು:
1. ಮಗುವಿನ ಅಧಿಕೃತ ಜನನ ಪ್ರಮಾಣಪತ್ರ (Birth Certificate).
2. ಮಗುವಿನ ಮತ್ತು ಪೋಷಕರ ಆಧಾರ್ ಕಾರ್ಡ್.
3. ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ (ಅನ್ವಯವಾದಲ್ಲಿ).
4. ರಾಜ್ಯದ ವಿದ್ಯಾರ್ಥಿ ಟ್ರ್ಯಾಕಿಂಗ್ ವ್ಯವಸ್ಥೆಯಲ್ಲಿ (SATS Portal) ಮಗುವಿಗೆ ಶಾಲೆ ವತಿಯಿಂದ ಅನನ್ಯ **SATS Student ID** ಸೃಷ್ಟಿಸಲಾಗುತ್ತದೆ.""",
        "category": "EDUCATION",
        "language": "kn",
        "source_url": "https://sats.karnataka.gov.in",
        "keywords": "school admission age karnataka, class 1 age 6 years sats, lkg ukg admission, ಶಾಲಾ ಪ್ರವೇಶ ವಯಸ್ಸು, 1ನೇ ತರಗತಿ ಪ್ರವೇಶ",
        "action_label": "🏫 SATS ಪೋರ್ಟಲ್",
        "action_url": "https://sats.karnataka.gov.in"
    },
    {
        "id": "faq_user_197",
        "question": "ಆಟೋ ಅಥವಾ ಟ್ಯಾಕ್ಸಿ ಚಾಲಕರು ಮೀಟರ್ ಹಾಕದಿದ್ದರೆ ಅಥವಾ ಅಧಿಕ ಬಾಡಿಗೆ ಕೇಳಿದರೆ ಎಲ್ಲಿ ದೂರು ನೀಡಬೇಕು?",
        "normalized_question": "auto rickshaw excess fare complaint bangalore rto traffic police helpline ಆಟೋ ಮೀಟರ್ ದೂರು ಸಹಾಯವಾಣಿ",
        "answer": """### 🛺 ಆಟೋ/ಕ್ಯಾಬ್ ಅಧಿಕ ಬಾಡಿಗೆ & ನಿರಾಕರಣೆ ದೂರು ಸಹಾಯವಾಣಿ

ಬೆಂಗಳೂರು ಹಾಗೂ ಇತರ ನಗರಗಳಲ್ಲಿ ಆಟೋ ಅಥವಾ ಟ್ಯಾಕ್ಸಿ ಚಾಲಕರು ಪ್ರಯಾಣ ನಿರಾಕರಿಸಿದರೆ (Refusal to ply), ದುಪ್ಪಟ್ಟು ಬಾಡಿಗೆ ಕೇಳಿದರೆ ಅಥವಾ ಅನುಚಿತವಾಗಿ ವರ್ತಿಸಿದರೆ ತಕ್ಷಣ ದೂರು ದಾಖಲಿಸಬಹುದು.

---

### 📞 ತುರ್ತು ದೂರು ಮಾರ್ಗಗಳು:
* **ಬೆಂಗಳೂರು ಟ್ರಾಫಿಕ್ ಪೊಲೀಸ್ ಕಂಟ್ರೋಲ್ ರೂಂ:** **080-22943014 / 080-22943131**
* **ಕರ್ನಾಟಕ ಪೊಲೀಸ್ ತುರ್ತು ಸಂಖ್ಯೆ:** **112**
* **BTP WhatsApp ಸಹಾಯವಾಣಿ:** **9480801800**
* **ಸಾರಿಗೆ ಇಲಾಖೆ ಆಟೋ ದೂರು ಸಹಾಯವಾಣಿ:** **080-22864666 / 22864777**

📝 ದೂರು ನೀಡುವಾಗ ಆಟೋ/ಕ್ಯಾಬ್ ವಾಹನದ ನೋಂದಣಿ ಸಂಖ್ಯೆ (Vehicle Number), ಸ್ಥಳ ಮತ್ತು ಸಮಯವನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ತಿಳಿಸಿ. ಪೊಲೀಸರು ಚಾಲಕನಿಗೆ ನೋಟಿಸ್ ಜಾರಿ ಮಾಡಿ ದಂಡ ವಿಧಿಸುತ್ತಾರೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://btp.gov.in",
        "keywords": "auto fare complaint, auto meter refusal btp, auto helpline bangalore, ಆಟೋ ಮೀಟರ್ ದೂರು, ಟ್ರಾಫಿಕ್ ಪೊಲೀಸ್ ಸಹಾಯವಾಣಿ",
        "action_label": "🛺 BTP ಸಹಾಯವಾಣಿ",
        "action_url": "https://btp.gov.in"
    },
    {
        "id": "faq_user_198",
        "question": "ಕೃಷಿ ಪಂಪ್‌ಸೆಟ್‌ಗಳಿಗೆ 3-ಫೇಸ್ ಉಚಿತ ವಿದ್ಯುತ್ ಸರಬರಾಜು ಸಮಯ (3 Phase Power Timing) ತಿಳಿಯುವುದು ಹೇಗೆ?",
        "normalized_question": "karnataka agriculture pumpset 3 phase free power supply hours escom ರೈತರ ಕೃಷಿ ಪಂಪ್‌ಸೆಟ್ 3 ಫೇಸ್ ವಿದ್ಯುತ್",
        "answer": """### ⚡ ಕೃಷಿ ಪಂಪ್‌ಸೆಟ್ 3-ಫೇಸ್ ಉಚಿತ ವಿದ್ಯುತ್ ಸರಬರಾಜು ನಿಯಮಗಳು

ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಇಂಧನ ಇಲಾಖೆಯು ರಾಜ್ಯದ ರೈತರ ಕೃಷಿ ಪಂಪ್‌ಸೆಟ್‌ಗಳಿಗೆ ಪ್ರತಿದಿನ **7 ಗಂಟೆಗಳ ಕಾಲ ಗುಣಮಟ್ಟದ 3-ಫೇಸ್ ವಿದ್ಯುತ್** ಅನ್ನು ಸಂಪೂರ್ಣ ಉಚಿತವಾಗಿ ನೀಡುತ್ತದೆ.

---

### ⏱️ ವಿದ್ಯುತ್ ಸರಬರಾಜು ವೇಳಾಪಟ್ಟಿ:
* ಲೋಡ್ ಬ್ಯಾಲೆನ್ಸಿಂಗ್‌ಗಾಗಿ ಪ್ರತಿ ಫೀಡರ್ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ದಿನದ ಪಾಳಿ (Day Shift) ಮತ್ತು ರಾತ್ರಿಯ ಪಾಳಿಯಲ್ಲಿ (Night Shift) ಹಂತ-ಹಂತವಾಗಿ 7 ಗಂಟೆ ವಿದ್ಯುತ್ ನೀಡಲಾಗುತ್ತದೆ.
* ನಿಮ್ಮ ಹಳ್ಳಿ ಅಥವಾ ಫೀಡರ್‌ನ ನಿಖರ 3-ಫೇಸ್ ವಿದ್ಯುತ್ ಸಮಯ ತಿಳಿಯಲು ನಿಮ್ಮ ವ್ಯಾಪ್ತಿಯ ವಿದ್ಯುತ್ ನಿಗಮದ (BESCOM, HESCOM, GESCOM, MESCOM, CESC) ಸ್ಥಳೀಯ ಸೆಕ್ಷನ್ ಆಫೀಸ್ ಅಥವಾ ಲೈನ್‌ಮ್ಯಾನ್ ಅನ್ನು ಸಂಪರ್ಕಿಸಬಹುದು.
* **24x7 ವಿದ್ಯುತ್ ಸಹಾಯವಾಣಿ:** ಯಾವುದೇ ತಾಲೂಕಿನಿಂದ **1912** ಸಂಖ್ಯೆಗೆ ಕರೆ ಮಾಡಿ ವಿದ್ಯುತ್ ಪೂರೈಕೆ ವೇಳಾಪಟ್ಟಿ ಹಾಗೂ ಫೀಡರ್ ಟ್ರಿಪ್ಪಿಂಗ್ ವಿವರ ಪಡೆಯಬಹುದು.""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://energy.karnataka.gov.in",
        "keywords": "3 phase power agriculture karnataka, 7 hours free farm power, escom 1912, ಕೃಷಿ ಪಂಪ್‌ಸೆಟ್ 3 ಫೇಸ್ ವಿದ್ಯುತ್, ಉಚಿತ ವಿದ್ಯುತ್",
        "action_label": "⚡ ಇಂಧನ ಇಲಾಖೆ",
        "action_url": "https://energy.karnataka.gov.in"
    },
    {
        "id": "faq_user_199",
        "question": "ಗ್ರಾಮೀಣ ಮತ್ತು ನಗರ ಪ್ರದೇಶಗಳಲ್ಲಿ ಮನೆ ಕಟ್ಟಲು ಪ್ಲಾನ್ ಸ್ಯಾಂಕ್ಷನ್ (Building Plan Approval) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "building plan sanction bbmp gram panchayat online approval ಮನೆ ಕಟ್ಟಲು ಪ್ಲಾನ್ ಸ್ಯಾಂಕ್ಷನ್ ನಕ್ಷೆ ಮಂಜೂರಾತಿ",
        "answer": """### 🏠 ಕಟ್ಟಡ ನಕ್ಷೆ ಮಂಜೂರಾತಿ (Building Plan Approval) ಪ್ರಕ್ರಿಯೆ

ಯಾವುದೇ ಹೊಸ ಮನೆ ಅಥವಾ ವಾಣಿಜ್ಯ ಕಟ್ಟಡ ನಿರ್ಮಿಸುವ ಮುನ್ನ ಸ್ಥಳೀಯ ಯೋಜನಾ ಪ್ರಾಧಿಕಾರದಿಂದ ನಕ್ಷೆ ಮಂಜೂರಾತಿ ಪಡೆಯುವುದು ಕಾನೂನುಬದ್ಧ ಸುರಕ್ಷತೆ ಮತ್ತು ಬ್ಯಾಂಕ್ ಸಾಲಕ್ಕೆ ಕಡ್ಡಾಯ.

---

### 🏛️ ಪ್ರಾಧಿಕಾರವಾರು ಅರ್ಜಿ ವಿಧಾನ:
1. **BBMP ವ್ಯಾಪ್ತಿಯಲ್ಲಿ (ಬೆಂಗಳೂರು):**
   - [bbmpsonline.in](https://bbmpsonline.in) (OBPAS - Online Building Plan Approval System) ಮೂಲಕ ನೋಂದಾಯಿತ ಆರ್ಕಿಟೆಕ್ಟ್/ಇಂಜಿನಿಯರ್ ಮೂಲಕ ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ಸ್ವಯಂಚಾಲಿತ ಅನುಮೋದನೆ ಪಡೆಯಬಹುದು.
2. **ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ:**
   - [panchatantra.karnataka.gov.in](https://panchatantra.karnataka.gov.in) ನಲ್ಲಿ ಇ-ಸ್ವತ್ತು ನಮೂನೆ 9/11, ಕ್ರಯಪತ್ರ ಮತ್ತು ಬ್ಲೂಪ್ರಿಂಟ್ ನಕ್ಷೆ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ಪಿಡಿಒ (PDO) ಅನುಮೋದನೆ ಪಡೆಯಬೇಕು.
3. **ನಗರಸಭೆ / ಪುರಸಭೆ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ:**
   - ನಗರಾಭಿವೃದ್ಧಿ ಪ್ರಾಧಿಕಾರದ (KUWSDB / DULT) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನಿಗದಿತ ಶುಲ್ಕ ಪಾವತಿಸಿ ಅನುಮೋದನೆ ಪಡೆಯಬೇಕು.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bbmpsonline.in",
        "keywords": "building plan sanction online, bbmp obpas, gram panchayat building permission, ನಕ್ಷೆ ಮಂಜೂರಾತಿ, ಪ್ಲಾನ್ ಸ್ಯಾಂಕ್ಷನ್",
        "action_label": "🏠 ನಕ್ಷೆ ಮಂಜೂರಾತಿ ಪೋರ್ಟಲ್",
        "action_url": "https://bbmpsonline.in"
    },
    {
        "id": "faq_user_200",
        "question": "ಕಾಲೇಜು ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಸರ್ಕಾರದ ಉಚಿತ ಲ್ಯಾಪ್‌ಟಾಪ್ ಯೋಜನೆಗೆ (Free Laptop Scheme) ಅರ್ಜಿ ಸಲ್ಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "free laptop scheme karnataka sc st degree medical engineering college ಉಚಿತ ಲ್ಯಾಪ್‌ಟಾಪ್ ಯೋಜನೆ ಕಾಲೇಜು ವಿದ್ಯಾರ್ಥಿ",
        "answer": """### 💻 ಕರ್ನಾಟಕ ಉಚಿತ ಲ್ಯಾಪ್‌ಟಾಪ್ ಯೋಜನೆ (Free Laptop Scheme for Higher Education)

ಸರ್ಕಾರಿ ಮತ್ತು ಅನುದಾನಿತ ಕಾಲೇಜುಗಳಲ್ಲಿ ಪ್ರಥಮ ವರ್ಷದ ಪದವಿ, ಇಂಜಿನಿಯರಿಂಗ್, ವೈದ್ಯಕೀಯ, ಪಾಲಿಟೆಕ್ನಿಕ್ ಹಾಗೂ ಸ್ನಾತಕೋತ್ತರ ವ್ಯಾಸಂಗಕ್ಕೆ ಪ್ರವೇಶ ಪಡೆದ SC, ST ಮತ್ತು ಹಿಂದುಳಿದ ವರ್ಗಗಳ ಬಡ ಪ್ರತಿಭಾವಂತ ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಡಿಜಿಟಲ್ ಕಲಿಕೆಗೆ ಉಚಿತ ಲ್ಯಾಪ್‌ಟಾಪ್ ವಿತರಿಸಲಾಗುತ್ತದೆ.

---

### 📌 ಅರ್ಹತಾ ಮಾನದಂಡಗಳು:
1. ವಿದ್ಯಾರ್ಥಿಯು ಕರ್ನಾಟಕದ ಕಾಯಂ ನಿವಾಸಿಯಾಗಿರಬೇಕು.
2. ಸರ್ಕಾರಿ ಪ್ರಥಮ ದರ್ಜೆ ಕಾಲೇಜು (GFGC), ಸರ್ಕಾರಿ ಇಂಜಿನಿಯರಿಂಗ್ ಅಥವಾ ವೈದ್ಯಕೀಯ ಕಾಲೇಜಿನಲ್ಲಿ ಪ್ರಥಮ ವರ್ಷಕ್ಕೆ ಪ್ರವೇಶ ಪಡೆದಿರಬೇಕು.
3. ಕುಟುಂಬದ ವಾರ್ಷಿಕ ಆದಾಯ ಮಿತಿ ₹2.50 ಲಕ್ಷದ ಒಳಗಿರಬೇಕು.

---

### 📝 ಅರ್ಜಿ ಪ್ರಕ್ರಿಯೆ:
ಪ್ರತ್ಯೇಕ ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಇರುವುದಿಲ್ಲ. ಕಾಲೇಜು ಪ್ರವೇಶದ ವೇಳೆ ನಿಮ್ಮ ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರದ RD ಸಂಖ್ಯೆ ಮತ್ತು ಆಧಾರ್ ನೀಡಿದರೆ, ಕಾಲೇಜಿನ ಪ್ರಾಂಶುಪಾಲರೇ ಇಲಾಖಾ ತಂತ್ರಾಂಶದಲ್ಲಿ ನೇರವಾಗಿ ಅರ್ಹ ವಿದ್ಯಾರ್ಥಿಗಳ ಪಟ್ಟಿ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ಲ್ಯಾಪ್‌ಟಾಪ್ ವಿತರಿಸುತ್ತಾರೆ.

🔗 **ಕಾಲೇಜು ಶಿಕ್ಷಣ ಇಲಾಖೆ:** [dce.karnataka.gov.in](https://dce.karnataka.gov.in)""",
        "category": "EDUCATION",
        "language": "kn",
        "source_url": "https://dce.karnataka.gov.in",
        "keywords": "free laptop scheme karnataka, dce laptop distribution, degree student laptop, ಉಚಿತ ಲ್ಯಾಪ್‌ಟಾಪ್, ಕಾಲೇಜು ಶಿಕ್ಷಣ ಇಲಾಖೆ",
        "action_label": "💻 ಕಾಲೇಜು ಶಿಕ್ಷಣ ಇಲಾಖೆ",
        "action_url": "https://dce.karnataka.gov.in"
    },
    {
        "id": "faq_user_201",
        "question": "ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ NPCI ಮ್ಯಾಪಿಂಗ್ ಮತ್ತು ಆಧಾರ್ ಸೀಡಿಂಗ್ ಆಗಿದೆಯಾ ಎಂದು ಮೊಬೈಲ್‌ನಲ್ಲಿ ಚೆಕ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "check aadhar npci seeding status online resident uidai bank mapping ಬ್ಯಾಂಕ್ ಆಧಾರ್ ಸೀಡಿಂಗ್ ಚೆಕ್",
        "answer": """### 🏦 ಬ್ಯಾಂಕ್ ಖಾತೆ Aadhaar NPCI Seeding ಸ್ಟೇಟಸ್ ಚೆಕ್ ಮಾಡುವ ವಿಧಾನ

ಸರ್ಕಾರದ ಗೃಹಲಕ್ಷ್ಮಿ, ಅನ್ನಭಾಗ್ಯ, ವಿದ್ಯಾರ್ಥಿವೇತನ, ಕಿಸಾನ್ ಸಮ್ಮಾನ್ ನಿಧಿ ಹಣ ನೇರವಾಗಿ ನಿಮ್ಮ ಖಾತೆಗೆ ಬರಲು ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ NPCI ಮ್ಯಾಪಿಂಗ್ ಸಕ್ರಿಯವಾಗಿರಬೇಕು (Active).

---

### 📱 ಆನ್‌ಲೈನ್ ಪರಿಶೀಲನಾ ಹಂತಗಳು:
1. **UIDAI ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [myaadhaar.uidai.gov.in](https://myaadhaar.uidai.gov.in)
2. **'Bank Seeding Status'** ಲಿಂಕ್ ಕ್ಲಿಕ್ ಮಾಡಿ.
3. ನಿಮ್ಮ 12 ಅಂಕಿಗಳ ಆಧಾರ್ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ, ಮೊಬೈಲ್‌ಗೆ ಬರುವ **OTP** ಹಾಕಿ ಲಾಗಿನ್ ಆಗಿ.
4. ಪರದೆಯ ಮೇಲೆ ನಿಮ್ಮ ಯಾವ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಆಧಾರ್ ಲಿಂಕ್ ಆಗಿದೆ (ಉದಾ: State Bank of India / Canara Bank / IPPB) ಮತ್ತು ಸ್ಥಿತಿ **'Active'** ಇದೆಯೇ ಎಂದು ಸ್ಪಷ್ಟವಾಗಿ ಕಾಣಿಸುತ್ತದೆ.

💡 'Inactive' ಅಥವಾ 'No Bank Mapped' ಎಂದು ಬಂದರೆ, ತಕ್ಷಣ ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಶಾಖೆಗೆ ತೆರಳಿ DBT Consent Form ನೀಡಿ ಸೀಡಿಂಗ್ ಮಾಡಿಸಿ.""",
        "category": "SCHEME",
        "language": "kn",
        "source_url": "https://myaadhaar.uidai.gov.in",
        "keywords": "check npci seeding status, aadhar bank mapping active, uidai bank status, ಎನ್‌ಪಿಸಿಐ ಸೀಡಿಂಗ್ ಚೆಕ್, ಬ್ಯಾಂಕ್ ಆಧಾರ್ ಮ್ಯಾಪಿಂಗ್",
        "action_label": "🏦 NPCI ಸ್ಟೇಟಸ್ ನೋಡಿ",
        "action_url": "https://myaadhaar.uidai.gov.in"
    },
    {
        "id": "faq_user_202",
        "question": "ಬೆಳೆ ಸಾಲ ಮನ್ನಾ ಅಥವಾ ಹೊಸ ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ (KCC Farm Loan) ಸೌಲಭ್ಯ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "kisan credit card kcc loan application farmer fruits fid crop loan ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ ಬೆಳೆ ಸಾಲ",
        "answer": """### 👨‍🌾 ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ (KCC - Kisan Credit Card) ಸಾಲ ಸೌಲಭ್ಯ

ರೈತರಿಗೆ ಕೃಷಿ ಖರ್ಚು, ಬಿತ್ತನೆ ಬೀಜ, ಗೊಬ್ಬರ, ಕೀಟನಾಶಕ ಮತ್ತು ಕೃಷಿ ಕೂಲಿ ವೆಚ್ಚವನ್ನು ಭರಿಸಲು ರಾಷ್ಟ್ರೀಕೃತ ಮತ್ತು ಗ್ರಾಮೀಣ ಬ್ಯಾಂಕ್‌ಗಳು ರಿಯಾಯಿತಿ ಬಡ್ಡಿದರದಲ್ಲಿ KCC ಸಾಲ ಒದಗಿಸುತ್ತವೆ.

---

### 💰 KCC ಸಾಲದ ಪ್ರಮುಖ ಸೌಲಭ್ಯಗಳು:
* **₹3.00 ಲಕ್ಷದವರೆಗೆ ಸಾಲ:** ಕೇವಲ **4% ರಿಯಾಯಿತಿ ಬಡ್ಡಿದರದಲ್ಲಿ** (ಸರ್ಕಾರದ 3% ಬಡ್ಡಿ ಸಹಾಯಧನದ ನಂತರ).
* **ಮರುಪಾವತಿ ಅವಧಿ:** ಬೆಳೆ ಕಟಾವಿನ ಆಧಾರದ ಮೇಲೆ 12 ತಿಂಗಳು.
* **ಕಾರ್ಡ್ ಸೌಲಭ್ಯ:** ಎಟಿಎಂ ಮೂಲಕ ಅಗತ್ಯವಿದ್ದಾಗ ಹಣ ಡ್ರಾ ಮಾಡಿಕೊಳ್ಳುವ RuPay KCC ಡೆಬಿಟ್ ಕಾರ್ಡ್ ನೀಡಲಾಗುತ್ತದೆ.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
1. ಜಮೀನಿನ ಚಾಲ್ತಿ ಪಹಣಿ (Bhoomi RTC) ಮತ್ತು ಮ್ಯುಟೇಶನ್ ಪ್ರತಿ.
2. ರೈತರ **FRUITS FID ಕಾರ್ಡ್** ಮತ್ತು ಆಧಾರ್ ಕಾರ್ಡ್.
3. 2 ಪಾಸ್‌ಪೋರ್ಟ್ ಸೈಜ್ ಫೋಟೋಗಳು.
ಹತ್ತಿರದ ಕೆನರಾ ಬ್ಯಾಂಕ್, ಎಸ್‌ಬಿಐ, ಕರ್ನಾಟಕ ಗ್ರಾಮೀಣ ಬ್ಯಾಂಕ್ ಅಥವಾ ಡಿಸಿಸಿ ಬ್ಯಾಂಕ್ ಶಾಖೆಯಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು.""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://fruits.karnataka.gov.in",
        "keywords": "kcc loan application, kisan credit card interest rate, fruits fid crop loan, ಕಿಸಾನ್ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್, ಬೆಳೆ ಸಾಲ, ಕೆಸಿಸಿ",
        "action_label": "👨‍🌾 FRUITS ಪೋರ್ಟಲ್",
        "action_url": "https://fruits.karnataka.gov.in"
    }
]

# =========================================================================
# 14. EXPANSION BATCH 6: HIGH-UTILITY DAILY CITIZEN FAQS (203 - 217)
# =========================================================================

ADDITIONAL_EXPANSION_FAQS_BATCH_6 = [
    {
        "id": "faq_user_203",
        "question": "ಆರ್‌ಟಿಒ ಕಚೇರಿಗೆ ಹೋಗದೆ ಮನೆಯಲ್ಲೇ ಡ್ರೈವಿಂಗ್ ಲೈಸೆನ್ಸ್ (DL Renewal) ನವೀಕರಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "driving license renewal online parivahan faceless service rto karnataka ಡಿಎಲ್ ನವೀಕರಣ ಆನ್‌ಲೈನ್",
        "answer": """### 🚗 ಫೇಸ್‌ಲೆಸ್ ಡಿಎಲ್ ನವೀಕರಣ (Online DL Renewal via Parivahan)

ಕರ್ನಾಟಕ ಸಾರಿಗೆ ಇಲಾಖೆಯು ಕಾಗದರಹಿತ (Faceless) ಸೇವೆ ಒದಗಿಸುತ್ತಿದ್ದು, ಚಾಲನಾ ಪರವಾನಗಿ ಅವಧಿ ಮುಗಿದಿದ್ದರೆ ಆರ್‌ಟಿಒ ಕಚೇರಿಗೆ ಭೌತಿಕವಾಗಿ ಭೇಟಿ ನೀಡದೆ ಆನ್‌ಲೈನ್‌ನಲ್ಲೇ ನವೀಕರಿಸಬಹುದು.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
* ಅವಧಿ ಮುಗಿದಿರುವ ಮೂಲ ಡ್ರೈವಿಂಗ್ ಲೈಸೆನ್ಸ್ (DL) ಸಂಖ್ಯೆ.
* ಅರ್ಜಿದಾರರ ಆಧಾರ್ ಕಾರ್ಡ್ (ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಲಿಂಕ್ ಆಗಿರಬೇಕು).
* **ವೈದ್ಯಕೀಯ ಪ್ರಮಾಣಪತ್ರ (Form 1A):** 40 ವರ್ಷ ಮೀರಿದ ವ್ಯಕ್ತಿಗಳಿಗೆ ಅಥವಾ ವಾಣಿಜ್ಯ (Commercial) ವಾಹನ ಚಾಲಕರಿಗೆ ನೋಂದಾಯಿತ ಎಂಬಿಬಿಎಸ್ ವೈದ್ಯರಿಂದ ಡಿಜಿಟಲ್ ಸಹಿಯುಳ್ಳ ಮೆಡಿಕಲ್ ಸರ್ಟಿಫಿಕೇಟ್ ಅಗತ್ಯ.

---

### 💻 ನವೀಕರಣ ಹಂತಗಳು:
1. **ಪರಿವಾಹನ್ ಪೋರ್ಟಲ್:** [parivahan.gov.in](https://parivahan.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ 'Driving License Related Services' ಆಯ್ಕೆಮಾಡಿ.
2. ರಾಜ್ಯವನ್ನು **'Karnataka'** ಎಂದು ಆರಿಸಿ **'Apply for DL Renewal'** ಕ್ಲಿಕ್ ಮಾಡಿ.
3. ಆಧಾರ್ ದೃಢೀಕರಣ (Aadhaar Authentication) ಮೂಲಕ ಲಾಗಿನ್ ಆಗಿ DL ಸಂಖ್ಯೆ ಮತ್ತು ಜನ್ಮ ದಿನಾಂಕ ನಮೂದಿಸಿ.
4. ವಿಳಾಸ ದೃಢೀಕರಿಸಿ, Form 1A ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ನಿಗದಿತ ನವೀಕರಣ ಶುಲ್ಕ (₹400 ರಿಂದ ₹600) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪಾವತಿಸಿ.
5. ಆರ್‌ಟಿಒ ಅಧಿಕಾರಿಗಳು ಡಿಜಿಟಲ್ ಪರಿಶೀಲನೆ ನಡೆಸಿದ ನಂತರ ನವೀಕರಿಸಿದ ಸ್ಮಾರ್ಟ್ ಕಾರ್ಡ್ DL ನಿಮ್ಮ ವಿಳಾಸಕ್ಕೆ ಸ್ಪೀಡ್ ಪೋಸ್ಟ್ ಮೂಲಕ ಬರುತ್ತದೆ.

💡 ತುರ್ತು ಬಳಕೆಗೆ ತಕ್ಷಣ **DigiLocker** ಅಥವಾ **mParivahan** ಆ್ಯಪ್‌ನಲ್ಲಿ ಡಿಜಿಟಲ್ DL ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.""",
        "category": "TRANSPORT",
        "language": "kn",
        "source_url": "https://parivahan.gov.in",
        "keywords": "dl renewal online karnataka, driving license renewal parivahan, form 1a medical certificate, ಡಿಎಲ್ ನವೀಕರಣ, ಚಾಲನಾ ಪರವಾನಗಿ",
        "action_label": "🚗 ಪರಿವಾಹನ್ DL ನವೀಕರಣ",
        "action_url": "https://parivahan.gov.in"
    },
    {
        "id": "faq_user_204",
        "question": "ಮೊಬೈಲ್ ಕಳೆದುಹೋದರೆ ಅಥವಾ ಕಳ್ಳತನವಾದರೆ CEIR ಪೋರ್ಟಲ್ ಮೂಲಕ ಬ್ಲಾಕ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "lost mobile block ceir sancharsaathi ksp police imei block find phone ಕಳೆದುಹೋದ ಮೊಬೈಲ್ ಬ್ಲಾಕ್",
        "answer": """### 📱 CEIR ಪೋರ್ಟಲ್ — ಕಳೆದುಹೋದ ಮೊಬೈಲ್ ಫೋನ್ ಬ್ಲಾಕ್ & ಪತ್ತೆಹಚ್ಚುವ ವಿಧಾನ

ಕೇಂದ್ರ ಸರ್ಕಾರದ ದೂರಸಂಪರ್ಕ ಇಲಾಖೆಯ **ಸಂಚಾರ್ ಸಾಥಿ (Sanchar Saathi / CEIR)** ಪೋರ್ಟಲ್ ಮೂಲಕ ಕಳುವಾದ ಮೊಬೈಲ್‌ನ IMEI ಸಂಖ್ಯೆಯನ್ನು ಬ್ಲಾಕ್ ಮಾಡಿ ದುರ್ಬಳಕೆ ತಡೆಯಬಹುದು.

---

### 🚀 ಹಂತ-ಹಂತದ ವಿಧಾನ:
1. **ಮೊದಲು ಸಿಮ್ ಬ್ಲಾಕ್ & ಡೂಪ್ಲಿಕೇಟ್ ಸಿಮ್ ಪಡೆಯಿರಿ:** ನಿಮ್ಮ ಟೆಲಿಕಾಂ ಆಪರೇಟರ್ (Airtel/Jio/Vi/BSNL) ಸಂಪರ್ಕಿಸಿ ಕಳೆದುಹೋದ ಸಿಮ್ ಬ್ಲಾಕ್ ಮಾಡಿಸಿ ಅದೇ ನಂಬರ್‌ನ ಹೊಸ ಸಿಮ್ ಕಾರ್ಡ್ ಪಡೆದುಕೊಳ್ಳಿ.
2. **ಪೊಲೀಸ್ ಇ-ಲಾಸ್ಟ್ ದೂರು:** **KSP App** ಅಥವಾ [ksp.karnataka.gov.in](https://ksp.karnataka.gov.in) ನಲ್ಲಿ E-Lost ದೂರು ದಾಖಲಿಸಿ ದೂರಿನ ರಶೀದಿ (Ack No) ಪಡೆದುಕೊಳ್ಳಿ.
3. **CEIR ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಬ್ಲಾಕ್ ಮಾಡಿ:** [ceir.sancharsaathi.gov.in](https://ceir.sancharsaathi.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ **'Block Stolen/Lost Mobile'** ಆಯ್ಕೆಮಾಡಿ.
4. ಮೊಬೈಲ್‌ನ **15 ಅಂಕಿಗಳ IMEI 1 ಮತ್ತು IMEI 2** ಸಂಖ್ಯೆ, ಮೊಬೈಲ್ ಬಿಲ್ ಹಾಗೂ ಪೊಲೀಸ್ ಕಂಪ್ಲೈಂಟ್ ಪ್ರತಿ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
5. ಬ್ಲಾಕ್ ಆದ ತಕ್ಷಣ ಆ ಫೋನ್‌ಗೆ ಯಾರೇ ಬೇರೆ ಸಿಮ್ ಹಾಕಿದರೂ ಫೋನ್ ಕೆಲಸ ಮಾಡುವುದಿಲ್ಲ ಮತ್ತು ಪೊಲೀಸ್ ಕಂಟ್ರೋಲ್ ರೂಂಗೆ ಲೊಕೇಶನ್ ಟ್ರ್ಯಾಕ್ ಆಗುತ್ತದೆ.
6. ಫೋನ್ ಮರಳಿ ಸಿಕ್ಕಿದಾಗ ಅದೇ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ **'Unblock Found Mobile'** ಮೂಲಕ ಪುನಃ ಅನ್‌ಬ್ಲಾಕ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.""",
        "category": "POLICE",
        "language": "kn",
        "source_url": "https://ceir.sancharsaathi.gov.in",
        "keywords": "ceir portal mobile block, lost phone tracker sanchar saathi, imei block ksp, ಕಳೆದುಹೋದ ಮೊಬೈಲ್ ಬ್ಲಾಕ್, ಸಿಇಐಆರ್",
        "action_label": "📱 ಸಂಚಾರ್ ಸಾಥಿ CEIR",
        "action_url": "https://ceir.sancharsaathi.gov.in"
    },
    {
        "id": "faq_user_205",
        "question": "ವಾಹನದ ಮೂಲ ಆರ್‌ಸಿ (RC Book / Smart Card) ಕಳೆದುಹೋದರೆ ಡೂಪ್ಲಿಕೇಟ್ ಆರ್‌ಸಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "duplicate rc online parivahan vahan karnataka lost rc smart card ಡೂಪ್ಲಿಕೇಟ್ ಆರ್‌ಸಿ ಬುಕ್",
        "answer": """### 🏍️ ಡೂಪ್ಲಿಕೇಟ್ ವಾಹನ ನೋಂದಣಿ ಪ್ರಮಾಣಪತ್ರ (Duplicate RC) ಪಡೆಯುವ ವಿಧಾನ

ವಾಹನದ ಆರ್‌ಸಿ ಕಾರ್ಡ್ ಕಳೆದುಹೋದರೆ, ಹರಿದುಹೋದರೆ ಅಥವಾ ಕಳ್ಳತನವಾದರೆ ಪರಿವಾಹನ್ ಪೋರ್ಟಲ್ ಮೂಲಕ ಅಧಿಕೃತ ಡೂಪ್ಲಿಕೇಟ್ ಆರ್‌ಸಿ ಪಡೆಯಬಹುದು.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
* ಕರ್ನಾಟಕ ಪೊಲೀಸ್ **E-Lost ವರದಿ** ಪ್ರತಿ (KSP App ಮೂಲಕ ಪಡೆದದ್ದು).
* ಚಾಲ್ತಿಯಲ್ಲಿರುವ ವಾಹನ ವಿಮೆ (Vehicle Insurance) ಮತ್ತು ಮಾಲಿನ್ಯ ನಿಯಂತ್ರಣ ಪ್ರಮಾಣಪತ್ರ (PUC).
* ವಾಹನ ಮಾಲೀಕರ ಆಧಾರ್ ಕಾರ್ಡ್.
* ಬ್ಯಾಂಕ್ ಸಾಲವಿದ್ದರೆ ಬ್ಯಾಂಕ್‌ನಿಂದ ನಿರಾಕ್ಷೇಪಣಾ ಪತ್ರ (NOC from Financier / Form 26).

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ವಿಧಾನ:
1. [parivahan.gov.in](https://parivahan.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ **'Vehicle Related Services'** ಆಯ್ಕೆಮಾಡಿ.
2. ವಾಹನ ನೋಂದಣಿ ಸಂಖ್ಯೆ (Vehicle Number) ಮತ್ತು ಚಾಸಿಸ್ ಸಂಖ್ಯೆ ಹಾಕಿ ಲಾಗಿನ್ ಆಗಿ.
3. **'Apply for Duplicate RC'** ಆಯ್ಕೆಮಾಡಿ ಕಾರಣ ನಮೂದಿಸಿ (Lost / Torn).
4. ನಿಗದಿತ ಶುಲ್ಕ (ದ್ವಿಚಕ್ರ ವಾಹನಕ್ಕೆ ₹300, ಕಾರಿಗೆ ₹500 ರಿಂದ ₹1,000) ಆನ್‌ಲೈನ್ ಪಾವತಿಸಿ ರಶೀದಿ ಪ್ರಿಂಟ್ ತೆಗೆದುಕೊಳ್ಳಿ.
5. ದಾಖಲೆಗಳ ಪರಿಶೀಲನೆಯ ನಂತರ ಹೊಸ ಸ್ಮಾರ್ಟ್ ಕಾರ್ಡ್ ಆರ್‌ಸಿ ನಿಮ್ಮ ನೋಂದಾಯಿತ ವಿಳಾಸಕ್ಕೆ ಬರುತ್ತದೆ.""",
        "category": "TRANSPORT",
        "language": "kn",
        "source_url": "https://parivahan.gov.in",
        "keywords": "duplicate rc online karnataka, form 26 lost rc, vahan parivahan rc smart card, ಡೂಪ್ಲಿಕೇಟ್ ಆರ್‌ಸಿ, ವಾಹನ ದಾಖಲೆ",
        "action_label": "🏍️ ಡೂಪ್ಲಿಕೇಟ್ RC ಅರ್ಜಿ",
        "action_url": "https://parivahan.gov.in"
    },
    {
        "id": "faq_user_206",
        "question": "ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆಯ ₹2,000 ಹಣ ಪಡೆಯಲು ಬ್ಯಾಂಕ್ ಖಾತೆ ಬದಲಾಯಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "change gruha lakshmi bank account dbt npci post office ippb ಗೃಹಲಕ್ಷ್ಮಿ ಬ್ಯಾಂಕ್ ಖಾತೆ ಬದಲಾವಣೆ",
        "answer": """### 🌸 ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆ — ಬ್ಯಾಂಕ್ ಖಾತೆ ಬದಲಾವಣೆ ಪ್ರಕ್ರಿಯೆ

ಗೃಹಲಕ್ಷ್ಮಿ ಹಣ ಬರುತ್ತಿರುವ ಹಳೆಯ ಬ್ಯಾಂಕ್ ಖಾತೆ ಕ್ಲೋಸ್ ಆಗಿದ್ದರೆ ಅಥವಾ ಹೊಸ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಹಣ ವರ್ಗಾವಣೆಯಾಗಬೇಕಿದ್ದರೆ ಪ್ರತ್ಯೇಕವಾಗಿ ಸೇವಾ ಸಿಂಧು ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಖಾತೆ ಸಂಖ್ಯೆ ತಿದ್ದುವಂತಿಲ್ಲ; ಸರ್ಕಾರದ ಡಿಬಿಟಿ ನಿಯಮಾವಳಿ ಪ್ರಕಾರ **Aadhaar NPCI Mapping** ಬದಲಾಯಿಸಬೇಕು.

---

### 🔧 ಖಾತೆ ಬದಲಾಯಿಸುವ 2 ಅಧಿಕೃತ ಮಾರ್ಗಗಳು:
1. **ಹೊಸ ಬ್ಯಾಂಕ್ ಶಾಖೆಯಲ್ಲಿ DBT Consent Form ಸಲ್ಲಿಸಿ:**
   - ನೀವು ಯಾವ ಬ್ಯಾಂಕ್‌ಗೆ (ಉದಾ: SBI, Canara Bank, Union Bank) ಗೃಹಲಕ್ಷ್ಮಿ ಹಣ ಬರಬೇಕೆಂದು ಬಯಸುತ್ತೀರೋ ಆ ಶಾಖೆಗೆ ಭೇಟಿ ನೀಡಿ.
   - **'Aadhaar Mandate / NPCI DBT Seeding Form'** ಭರ್ತಿ ಮಾಡಿ ನೀಡಿ ನಿಮ್ಮ ಹೊಸ ಖಾತೆಗೆ ಪ್ರೈಮರಿ ಸೀಡಿಂಗ್ ಮಾಡಿಸಿ.
2. **ಅಂಚೆ ಕಚೇರಿ IPPB ಖಾತೆ (ತಕ್ಷಣದ ಪರಿಹಾರ):**
   - ಹತ್ತಿರದ ಅಂಚೆ ಕಚೇರಿಗೆ (Post Office) ಅಥವಾ ಪೋಸ್ಟ್‌ಮ್ಯಾನ್ ಬಳಿ ತೆರಳಿ ಕೇವಲ 5 ನಿಮಿಷಗಳಲ್ಲಿ ಬಯೋಮೆಟ್ರಿಕ್ ಮೂಲಕ **India Post Payments Bank (IPPB)** ಖಾತೆ ತೆರೆಯಿರಿ.
   - ಖಾತೆ ತೆರೆಯುವಾಗಲೇ 'DBT Mapping' ಆಯ್ಕೆಮಾಡಿದರೆ ಮುಂದಿನ ತಿಂಗಳ ಗೃಹಲಕ್ಷ್ಮಿ ಹಣ ನೇರವಾಗಿ ಈ ಅಂಚೆ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ.""",
        "category": "SCHEME",
        "language": "kn",
        "source_url": "https://sevasindhugs.karnataka.gov.in",
        "keywords": "gruha lakshmi bank change, npci dbt account shift, ippb gruha lakshmi, ಗೃಹಲಕ್ಷ್ಮಿ ಖಾತೆ ಬದಲಾವಣೆ, ಬ್ಯಾಂಕ್ ಸೀಡಿಂಗ್",
        "action_label": "🌸 ಗ್ಯಾರಂಟಿ ವಿವರ ನೋಡಿ",
        "action_url": "/guarantee-schemes.html"
    },
    {
        "id": "faq_user_207",
        "question": "ಅಸಂಘಟಿತ ಕಾರ್ಮಿಕರ ಇ-ಶ್ರಮ್ ಕಾರ್ಡ್ (e-Shram Card) ಪ್ರಯೋಜನಗಳೇನು? ನೋಂದಣಿ ಹೇಗೆ?",
        "normalized_question": "eshram card apply karnataka unorganized workers 2 lakh accident insurance ಇ-ಶ್ರಮ್ ಕಾರ್ಡ್ ನೋಂದಣಿ",
        "answer": """### 👷 ಇ-ಶ್ರಮ್ ಕಾರ್ಡ್ (e-Shram Card) — ಅಸಂಘಟಿತ ವಲಯದ ಕಾರ್ಮಿಕರ ರಾಷ್ಟ್ರೀಯ ಗುರುತು

ಕೃಷಿ ಕೂಲಿ ಕಾರ್ಮಿಕರು, ಆಟೋ/ಕ್ಯಾಬ್ ಚಾಲಕರು, ಗೃಹ ಸಹಾಯಕಿಯರು, ಕಟ್ಟಡ ಕಾರ್ಮಿಕರು, ಬೀದಿಬದಿ ವ್ಯಾಪಾರಿಗಳು ಹಾಗೂ ಗಿಗ್ ವರ್ಕರ್ಸ್‌ಗಳಿಗೆ ಕೇಂದ್ರ-ರಾಜ್ಯ ಸರ್ಕಾರದ ಸಾಮಾಜಿಕ ಭದ್ರತೆ ಒದಗಿಸುವ ಕಾರ್ಡ್.

---

### 🌟 ಪ್ರಮುಖ ಪ್ರಯೋಜನಗಳು:
* **12 ಅಂಕಿಗಳ UAN (Universal Account Number):** ದೇಶಾದ್ಯಂತ ಮಾನ್ಯತೆ ಇರುವ ಏಕೈಕ ಕಾರ್ಮಿಕ ಗುರುತಿನ ಸಂಖ್ಯೆ.
* **₹2 ಲಕ್ಷ ಉಚಿತ ಅಪಘಾತ ವಿಮೆ (PMSBY):** ಕೆಲಸದ ವೇಳೆ ಆಕಸ್ಮಿಕ ಮರಣ ಅಥವಾ ಶಾಶ್ವತ ಅಂಗವಿಕಲತೆ ಸಂಭವಿಸಿದರೆ ₹2 ಲಕ್ಷ ಹಾಗೂ ಭಾಗಶಃ ಅಂಗವಿಕಲತೆಗೆ ₹1 ಲಕ್ಷ ವಿಮಾ ಪರಿಹಾರ.
* ತುರ್ತು ಪ್ರಕೃತಿ ವಿಕೋಪ ಅಥವಾ ಸಾಂಕ್ರಾಮಿಕ ರೋಗದ ಸಂದರ್ಭದಲ್ಲಿ ನೇರ ಆರ್ಥಿಕ ನೆರವು.

---

### 📝 ಆನ್‌ಲೈನ್ ನೋಂದಣಿ:
* [eshram.gov.in](https://eshram.gov.in) ನಲ್ಲಿ ಅಥವಾ ಹತ್ತಿರದ CSC / ಗ್ರಾಮ ಒನ್ ಕೇಂದ್ರದಲ್ಲಿ ಆಧಾರ್ ಸಂಖ್ಯೆ ಮತ್ತು ಬ್ಯಾಂಕ್ ವಿವರ ನೀಡಿ ಉಚಿತವಾಗಿ ಕಾರ್ಡ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.""",
        "category": "LABOUR",
        "language": "kn",
        "source_url": "https://eshram.gov.in",
        "keywords": "eshram card apply online, unorganized worker insurance, uan card, ಇ-ಶ್ರಮ್ ಕಾರ್ಡ್, ಅಪಘಾತ ವಿಮೆ",
        "action_label": "👷 e-Shram ಪೋರ್ಟಲ್",
        "action_url": "https://eshram.gov.in"
    },
    {
        "id": "faq_user_208",
        "question": "ಹಾವು ಕಡಿತ ಅಥವಾ ಕಾಡು ಪ್ರಾಣಿಗಳ ದಾಳಿಗೆ ಅರಣ್ಯ ಮತ್ತು ಕಂದಾಯ ಇಲಾಖೆಯಿಂದ ಪರಿಹಾರ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "snake bite compensation wild animal attack ex gratia forest department karnataka ಹಾವು ಕಡಿತ ಪರಿಹಾರ ಕಾಡು ಪ್ರಾಣಿ ದಾಳಿ",
        "answer": """### 🌿 ವನ್ಯಜೀವಿ ದಾಳಿ ಮತ್ತು ಹಾವು ಕಡಿತ ಪರಿಹಾರ (Forest Dept Ex-Gratia Relief)

ಕರ್ನಾಟಕದಲ್ಲಿ ಕಾಡು ಪ್ರಾಣಿಗಳ (ಆನೆ, ಚಿರತೆ, ಹುಲಿ, ಕಾಡುಹಂದಿ) ದಾಳಿ ಅಥವಾ ಹಾವು ಕಡಿತದಿಂದ ಸಾವು/ಗಾಯ ಸಂಭವಿಸಿದರೆ ಸರ್ಕಾರದಿಂದ ಪರಿಹಾರ ಧನ ನೀಡಲಾಗುತ್ತದೆ.

---

### 💰 ಸರ್ಕಾರದ ಪರಿಹಾರ ಮೊತ್ತದ ವಿವರ:
* **ವನ್ಯಜೀವಿ ದಾಳಿಯಿಂದ ಮರಣ ಸಂಭವಿಸಿದರೆ:** ಮೃತರ ಕುಟುಂಬಕ್ಕೆ **₹15.00 ಲಕ್ಷ** ಏಕಗಂಟಿನ ಪರಿಹಾರ + ಅವಲಂಬಿತರಿಗೆ ಮಾಸಿಕ ₹4,000 ಪಿಂಚಣಿ.
* **ಹಾವು ಕಡಿತದಿಂದ ಮರಣ ಸಂಭವಿಸಿದರೆ (Snake Bite):** ಕಂದಾಯ ಮತ್ತು ವಿಪತ್ತು ನಿರ್ವಹಣಾ ಇಲಾಖೆಯಿಂದ **₹2.00 ಲಕ್ಷ** ಪರಿಹಾರ.
* **ಶಾಶ್ವತ ಅಂಗವಿಕಲತೆಗೆ:** ₹10.00 ಲಕ್ಷದವರೆಗೆ.
* **ಬೆಳೆ ನಾಶ ಅಥವಾ ಜಾನುವಾರು ಸಾವು:** ಅರಣ್ಯ ಇಲಾಖೆಯಿಂದ ನಿಗದಿತ ಮೌಲ್ಯಮಾಪನದಂತೆ ಪರಿಹಾರ.

---

### 📋 ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಪ್ರಕ್ರಿಯೆ:
ಘಟನೆ ನಡೆದ 48 ಗಂಟೆಗಳ ಒಳಗಾಗಿ ಸ್ಥಳೀಯ ವಲಯ ಅರಣ್ಯಾಧಿಕಾರಿ (RFO) ಅಥವಾ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿಗೆ ಮರಣೋತ್ತರ ಪರೀಕ್ಷಾ ವರದಿ (Post-Mortem Report), ಪೊಲೀಸ್ ಪಂಚನಾಮೆ ಮತ್ತು ಮೃತರ ಆಧಾರ್/ಬ್ಯಾಂಕ್ ವಿವರ ಸಲ್ಲಿಸಬೇಕು.""",
        "category": "WELFARE",
        "language": "kn",
        "source_url": "https://aranya.karnataka.gov.in",
        "keywords": "snake bite compensation karnataka, wild animal attack relief 15 lakh, rfo forest ex gratia, ಹಾವು ಕಡಿತ ಪರಿಹಾರ, ವನ್ಯಜೀವಿ ದಾಳಿ ಪರಿಹಾರ",
        "action_label": "🌿 ಅರಣ್ಯ ಇಲಾಖೆ",
        "action_url": "https://aranya.karnataka.gov.in"
    },
    {
        "id": "faq_user_209",
        "question": "ಜನನ ಅಥವಾ ಮರಣ ಪ್ರಮಾಣಪತ್ರದಲ್ಲಿ ಹೆಸರಿನ ಅಕ್ಷರ ದೋಷ ತಿದ್ದುಪಡಿ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "birth certificate name correction spelling mistake ejanma municipal corporation ಜನನ ಪ್ರಮಾಣಪತ್ರ ಹೆಸರು ತಿದ್ದುಪಡಿ",
        "answer": """### 📑 ಜನನ/ಮರಣ ಪ್ರಮಾಣಪತ್ರ ತಿದ್ದುಪಡಿ (Correction in Birth/Death Certificate)

e-JanMa ಅಥವಾ ಪಾಲಿಕೆ ಜನನ ಪ್ರಮಾಣಪತ್ರದಲ್ಲಿ ಮಗುವಿನ ಹೆಸರು, ಪೋಷಕರ ಹೆಸರಿನ ಕಾಗುಣಿತ ದೋಷವಿದ್ದರೆ ಅದನ್ನು ಸರಿಪಡಿಸುವ ಕಾನೂನುಬದ್ಧ ನಿಯಮ:

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
1. ಆಸ್ಪತ್ರೆಯ ಮೂಲ ಜನನ ವರದಿ (Original Hospital Birth Intimation Form 1).
2. ತಾಯಿ ಮತ್ತು ತಂದೆಯ ಆಧಾರ್ ಕಾರ್ಡ್, ವೋಟರ್ ಐಡಿ ಅಥವಾ ಪಾಸ್‌ಪೋರ್ಟ್ ಪ್ರತಿ.
3. ಶಾಲಾ ದಾಖಲೆ (ಮಗುವಿಗೆ ಶಾಲೆ ಸೇರಿದ್ದರೆ).
4. ₹20 ಅಥವಾ ₹100 ರ ಇ-ಸ್ಟ್ಯಾಂಪ್ ಪೇಪರ್‌ನಲ್ಲಿ ನೋಟರಿ ಅಫಿಡವಿಟ್ (Notary Affidavit).

---

### 🛠️ ಪ್ರಕ್ರಿಯೆ:
* ಜನನ ನೋಂದಣಿಯಾದ ಸಂಬಂಧಪಟ್ಟ ಪುರಸಭೆ/BBMP ವೈದ್ಯಾಧಿಕಾರಿ (MOH) ಅಥವಾ ಗ್ರಾಮೀಣ ಭಾಗದಲ್ಲಿ ತಾಲೂಕು ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಬೇಕು.
* ಸಣ್ಣ ಅಕ್ಷರ ದೋಷಗಳನ್ನು ರಿಜಿಸ್ಟ್ರಾರ್ ಅವರೇ ಸರಿಪಡಿಸಿ ನವೀಕರಿಸಿದ e-JanMa ಪ್ರಮಾಣಪತ್ರ ನೀಡುತ್ತಾರೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://ejanma.karnataka.gov.in",
        "keywords": "birth certificate correction, ejanma name change, moh bbmp birth death, ಜನನ ಪ್ರಮಾಣಪತ್ರ ತಿದ್ದುಪಡಿ, ಇ-ಜನ್ಮ",
        "action_label": "📑 e-JanMa ಪೋರ್ಟಲ್",
        "action_url": "https://ejanma.karnataka.gov.in"
    },
    {
        "id": "faq_user_210",
        "question": "ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ವ್ಯಾಪ್ತಿಯ ಮನೆ ಮತ್ತು ನಿವೇಶನದ ಆಸ್ತಿ ತೆರಿಗೆಯನ್ನು (Property Tax) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಕಟ್ಟುವುದು ಹೇಗೆ?",
        "normalized_question": "gram panchayat property tax online payment panchatantra bapuji seva kendra ಗ್ರಾಮ ಪಂಚಾಯತಿ ಮನೆ ತೆರಿಗೆ",
        "answer": """### 🏡 ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ಆಸ್ತಿ ತೆರಿಗೆ (Gram Panchayat Property Tax) ಆನ್‌ಲೈನ್ ಪಾವತಿ

ಗ್ರಾಮೀಣ ಭಾಗದ ನಾಗರಿಕರು ತಮ್ಮ ಮನೆ, ಖಾಲಿ ನಿವೇಶನ ಮತ್ತು ವಾಣಿಜ್ಯ ಅಂಗಡಿಗಳ ಆಸ್ತಿ ತೆರಿಗೆಯನ್ನು ಸುಲಭವಾಗಿ ಡಿಜಿಟಲ್ ರೂಪದಲ್ಲಿ ಪಾವತಿಸಬಹುದು.

---

### 💻 ಪಾವತಿ ಮಾಡುವ ವಿಧಾನ:
1. **ಬಾಪುಜಿ ಸೇವಾ ಕೇಂದ್ರ / ಗ್ರಾಮ ಒನ್:** ನಿಮ್ಮ ಗ್ರಾಮ ಪಂಚಾಯಿತಿಯ ಇ-ಸ್ವತ್ತು ನಮೂನೆ 9/11 ರ ಆಸ್ತಿ ಸಂಖ್ಯೆ (Property ID) ನೀಡಿ ತೆರಿಗೆ ಪಾವತಿಸಿ ಡಿಜಿಟಲ್ ರಶೀದಿ ಪಡೆಯಿರಿ.
2. **ಪಂಚತಂತ್ರ 2.0 ಪೋರ್ಟಲ್:** [panchatantra.karnataka.gov.in](https://panchatantra.karnataka.gov.in) ನಲ್ಲಿ ಆಸ್ತಿ ವಿವರ ಹುಡುಕಿ UPI (PhonePe, Google Pay), ನೆಟ್ ಬ್ಯಾಂಕಿಂಗ್ ಮೂಲಕ ಪಾವತಿಸಬಹುದು.
3. ತೆರಿಗೆ ಪಾವತಿಸಿದ ತಕ್ಷಣ ಗ್ರಾಮ ಪಂಚಾಯಿತಿಯ ಅಧಿಕೃತ ಡಿಜಿಟಲ್ ತೆರಿಗೆ ಪಾವತಿ ರಶೀದಿ (Tax Receipt) ರಚನೆಯಾಗುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://panchatantra.karnataka.gov.in",
        "keywords": "gram panchayat property tax online, panchatantra 2.0 tax payment, ಗ್ರಾಮ ಪಂಚಾಯತಿ ತೆರಿಗೆ, ಮನೆ ತೆರಿಗೆ ರಶೀದಿ",
        "action_label": "🏡 ಪಂಚತಂತ್ರ ತೆರಿಗೆ ಪೋರ್ಟಲ್",
        "action_url": "https://panchatantra.karnataka.gov.in"
    },
    {
        "id": "faq_user_211",
        "question": "ಆಸ್ತಿ ನೋಂದಣಿಯಾದ ನಂತರ ಕಂದಾಯ ಇ-ಖಾತಾ ವರ್ಗಾವಣೆ (Khata Transfer / Mutation) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಆಗುವುದು ಹೇಗೆ?",
        "normalized_question": "automatic khata transfer after registry bhoomi jameeni khata vargavane ಖಾತಾ ವರ್ಗಾವಣೆ ಮ್ಯುಟೇಶನ್",
        "answer": """### 📜 ಆಸ್ತಿ ಖರೀದಿಯ ನಂತರ ಸ್ವಯಂಚಾಲಿತ ಖಾತಾ ವರ್ಗಾವಣೆ (Seamless Mutation)

ಉಪನೋಂದಣಾಧಿಕಾರಿ ಕಚೇರಿಯಲ್ಲಿ (Sub-Registrar Office) ಆಸ್ತಿ ಮಾರಾಟ ಪತ್ರ ನೋಂದಣಿಯಾದ ತಕ್ಷಣ ಕಂದಾಯ ಇಲಾಖೆಯ ಕಾವೇರಿ 2.0 ಮತ್ತು ಭೂಮಿ ಪೋರ್ಟಲ್ ಪರಸ್ಪರ ಲಿಂಕ್ ಆಗಿರುವುದರಿಂದ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಮ್ಯುಟೇಶನ್ ಪ್ರಕ್ರಿಯೆ ಪ್ರಾರಂಭವಾಗುತ್ತದೆ.

---

### ⏱️ ಮ್ಯುಟೇಶನ್ ಹಂತಗಳು:
1. **J-Form ಸಲ್ಲಿಕೆ:** ನೋಂದಣಿ ಮುಗಿದ ದಿನವೇ ಸಬ್-ರಿಜಿಸ್ಟ್ರಾರ್ ಕಚೇರಿಯಿಂದ ಭೂಮಿ ತಂತ್ರಾಂಶಕ್ಕೆ 'ಜೆ-ಫಾರ್ಮ್' ವರ್ಗಾವಣೆಯಾಗಿ **MR ಸಂಖ್ಯೆ (Mutation Request)** ಸೃಷ್ಟಿಯಾಗುತ್ತದೆ.
2. **30 ದಿನಗಳ ಆಕ್ಷೇಪಣಾ ಅವಧಿ (Notice Period):** ಸಾರ್ವಜನಿಕ ಆಕ್ಷೇಪಣೆಗಾಗಿ 30 ದಿನಗಳ ಕಾಲಾವಕಾಶ ನೀಡಲಾಗುತ್ತದೆ.
3. **ತಹಶೀಲ್ದಾರ್ ಅನುಮೋದನೆ:** ಯಾವುದೇ ತಕರಾರು ಇಲ್ಲದಿದ್ದರೆ ಕಂದಾಯ ನಿರೀಕ್ಷಕರು ಪರಿಶೀಲಿಸಿ ತಹಶೀಲ್ದಾರ್ ಡಿಜಿಟಲ್ ಸಹಿ ಮಾಡುತ್ತಾರೆ.
4. ಮ್ಯುಟೇಶನ್ ಮುಗಿದ ತಕ್ಷಣ ಹೊಸ ಮಾಲೀಕರ ಹೆಸರಿನ ಪಹಣಿ (RTC) ಸಿದ್ಧವಾಗುತ್ತದೆ.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://bhoomi.karnataka.gov.in",
        "keywords": "seamless mutation bhoomi, j form sub registrar khata transfer, ಖಾತಾ ವರ್ಗಾವಣೆ, ಕಂದಾಯ ಮ್ಯುಟೇಶನ್",
        "action_label": "📜 ಭೂಮಿ ಮ್ಯುಟೇಶನ್ ಪರಿಶೀಲನೆ",
        "action_url": "https://bhoomi.karnataka.gov.in"
    },
    {
        "id": "faq_user_212",
        "question": "ಅರ್ಹರಲ್ಲದವರು ಬಿಪಿಎಲ್ ಕಾರ್ಡ್ ರದ್ದುಪಡಿಸಿ ಎಪಿಎಲ್ ಕಾರ್ಡ್‌ಗೆ (BPL to APL Surrender) ಬದಲಾಯಿಸಿಕೊಳ್ಳುವುದು ಹೇಗೆ?",
        "normalized_question": "surrender bpl card convert to apl card ahara karnataka penalty ಬಿಪಿಎಲ್ ಕಾರ್ಡ್ ರದ್ದು ಎಪಿಎಲ್",
        "answer": """### 🛒 ಅನರ್ಹ ಬಿಪಿಎಲ್ ಕಾರ್ಡ್ ಸ್ವಯಂಪ್ರೇರಿತ ರದ್ದತಿ (BPL Surrender / Conversion to APL)

ಆದಾಯ ತೆರಿಗೆ ಪಾವತಿದಾರರು, ಸರ್ಕಾರಿ ನೌಕರರು ಅಥವಾ ವಾರ್ಷಿಕ ₹1.20 ಲಕ್ಷಕ್ಕಿಂತ ಹೆಚ್ಚು ಆದಾಯ ಹೊಂದಿರುವ ಕುಟುಂಬಗಳು ದಂಡ ಅಥವಾ ಕ್ರಿಮಿನಲ್ ಕ್ರಮದಿಂದ ತಪ್ಪಿಸಿಕೊಳ್ಳಲು BPL ಕಾರ್ಡ್ ಅನ್ನು ಸ್ವಯಂಪ್ರೇರಿತವಾಗಿ APL ಕಾರ್ಡ್ ಆಗಿ ಪರಿವರ್ತಿಸಿಕೊಳ್ಳಬಹುದು.

---

### 🚀 ಪ್ರಕ್ರಿಯೆ:
1. [ahara.kar.nic.in](https://ahara.kar.nic.in) ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ 'E-Services -> Surrender BPL / Convert to Non-Priority (APL)' ಆಯ್ಕೆಮಾಡಿ.
2. ಅಥವಾ ನಿಮ್ಮ ತಾಲೂಕು ತಹಶೀಲ್ದಾರ್ / ಆಹಾರ ಶಿರಸ್ತೇದಾರ್ ಕಚೇರಿಗೆ ತೆರಳಿ ಲಿಖಿತ ಅರ್ಜಿ ನೀಡಿ.
3. ನಿಮ್ಮ ಕಾರ್ಡ್ ತಕ್ಷಣ APL (Non-Priority Household) ಆಗಿ ಬದಲಾಗುತ್ತದೆ.""",
        "category": "FOOD",
        "language": "kn",
        "source_url": "https://ahara.kar.nic.in",
        "keywords": "surrender bpl card, bpl to apl conversion, ahara surrender portal, ಬಿಪಿಎಲ್ ಕಾರ್ಡ್ ವಾಪಸ್, ಎಪಿಎಲ್ ಕಾರ್ಡ್",
        "action_label": "🛒 ಆಹಾರ ಇಲಾಖೆ",
        "action_url": "https://ahara.kar.nic.in"
    },
    {
        "id": "faq_user_213",
        "question": "ವಿದ್ಯುತ್ ಟ್ಯಾರಿಫ್ ಅನ್ನು ವಾಣಿಜ್ಯದಿಂದ ಗೃಹಬಳಕೆಗೆ (Commercial to Domestic LT-2 Tariff Change) ಬದಲಾಯಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "bescom tariff change commercial to domestic lt1 lt2 application ವಿದ್ಯುತ್ ಟ್ಯಾರಿಫ್ ಬದಲಾವಣೆ",
        "answer": """### ⚡ ವಿದ್ಯುತ್ ಟ್ಯಾರಿಫ್ ಬದಲಾವಣೆ (Change of Electricity Tariff)

ಹಿಂದೆ ಅಂಗಡಿ/ವಾಣಿಜ್ಯ ಉದ್ದೇಶಕ್ಕೆ ಬಳಸುತ್ತಿದ್ದ ಕಟ್ಟಡವನ್ನು ಮನೆ ಬಳಕೆಗೆ ಬದಲಾಯಿಸಿದಾಗ ಹೆಚ್ಚಿನ ವಾಣಿಜ್ಯ ವಿದ್ಯುತ್ ದರ ತಪ್ಪಿಸಲು LT-2 (ಗೃಹಬಳಕೆ) ಟ್ಯಾರಿಫ್‌ಗೆ ಬದಲಾವಣೆ ಮಾಡಿಕೊಳ್ಳಬೇಕು (ಇದರಿಂದ ಗೃಹಜ್ಯೋತಿ ಸೌಲಭ್ಯವೂ ಸಿಗುತ್ತದೆ).

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
* ಸ್ಥಳೀಯ ಪಾಲಿಕೆ/ಪಂಚಾಯಿತಿಯಿಂದ ವಸತಿ ಬಳಕೆಯ ಇ-ಖಾತಾ ಪ್ರತಿ.
* ಇತ್ತೀಚಿನ ವಿದ್ಯುತ್ ಬಿಲ್ ಪಾವತಿ ರಶೀದಿ (ಶೂನ್ಯ ಬಾಕಿ).
* ಮಾಲೀಕರ ಆಧಾರ್ ಕಾರ್ಡ್.

---

### 💻 ಅರ್ಜಿ ವಿಧಾನ:
1. ನಿಮ್ಮ ಎಸ್ಕಾಂ (BESCOM/HESCOM/MESCOM/GESCOM/CESC) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ **'Change of Tariff'** ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.
2. ಸೆಕ್ಷನ್ ಆಫೀಸರ್ ಭೌತಿಕ ತನಿಖೆ ನಡೆಸಿ ಸ್ಥಳ ಪರಿಶೀಲಿಸಿದ ನಂತರ ಟ್ಯಾರಿಫ್ ಬದಲಾವಣೆ ಆದೇಶ ಹೊರಡಿಸುತ್ತಾರೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bescom.karnataka.gov.in",
        "keywords": "tariff change bescom, commercial to domestic electricity, lt2 tariff application, ವಿದ್ಯುತ್ ಟ್ಯಾರಿಫ್ ಬದಲಾವಣೆ, ಬೆಸ್ಕಾಂ ಬಿಲ್",
        "action_label": "⚡ ಎಸ್ಕಾಂ ಸೇವೆಗಳು",
        "action_url": "https://bescom.karnataka.gov.in"
    },
    {
        "id": "faq_user_214",
        "question": "ಹಿರಿಯ ನಾಗರಿಕರಿಗೆ KSRTC ಬಸ್ ಪ್ರಯಾಣದಲ್ಲಿ ಶೇಕಡಾ 25% ರಿಯಾಯಿತಿ (Senior Citizen Bus Concession) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "ksrtc senior citizen 25 percent discount bus fare smart card ಹಿರಿಯ ನಾಗರಿಕರಿಗೆ ಬಸ್ ರಿಯಾಯಿತಿ",
        "answer": """### 🚌 ಕೆಎಸ್‌ಆರ್‌ಟಿಸಿ ಹಿರಿಯ ನಾಗರಿಕರ ಶೇ. 25% ಬಸ್ ಪ್ರಯಾಣ ರಿಯಾಯಿತಿ

ಕರ್ನಾಟಕ ಸಾರಿಗೆ ನಿಗಮವು (KSRTC, NWKRTC, KKRTC) ರಾಜ್ಯದ 60 ವರ್ಷ ಮತ್ತು ಅದಕ್ಕಿಂತ ಮೇಲ್ಪಟ್ಟ ಹಿರಿಯ ನಾಗರಿಕರಿಗೆ ರಾಜಹಂಸ, ನಾನ್-ಎಸಿ ಸ್ಲೀಪರ್ ಸೇರಿದಂತೆ ದೂರದ ಊರುಗಳ ಪ್ರಯಾಣಕ್ಕೆ ಬಸ್ ಟಿಕೆಟ್ ದರದಲ್ಲಿ **25% ರಿಯಾಯಿತಿ** ನೀಡುತ್ತದೆ.

---

### 🎫 ರಿಯಾಯಿತಿ ಪಡೆಯುವ ವಿಧಾನ:
* **ಆನ್‌ಲೈನ್ ಬುಕಿಂಗ್ (ksrtc.in):** ಟಿಕೆಟ್ ಬುಕ್ ಮಾಡುವಾಗ 'Senior Citizen' ಕೋಟಾ ಆಯ್ಕೆಮಾಡಿ ಜನ್ಮ ದಿನಾಂಕ ನಮೂದಿಸಿದರೆ 25% ದರ ಕಡಿತವಾಗುತ್ತದೆ.
* **ಕೌಂಟರ್ / ಬಸ್‌ನಲ್ಲಿ:** ನಿರ್ವಾಹಕರಿಗೆ ಸರ್ಕಾರದ ಅಧಿಕೃತ ವಯಸ್ಸಿನ ಪುರಾವೆ (ಆಧಾರ್ ಕಾರ್ಡ್ / ವೋಟರ್ ಐಡಿ / ಹಿರಿಯ ನಾಗರಿಕರ ಐಡಿ ಕಾರ್ಡ್) ತೋರಿಸಿ ರಿಯಾಯಿತಿ ಟಿಕೆಟ್ ಪಡೆಯಬಹುದು.""",
        "category": "TRANSIT",
        "language": "kn",
        "source_url": "https://ksrtc.in",
        "keywords": "ksrtc senior citizen concession, 25 percent bus discount, ksrtc rajahamsa discount, ಹಿರಿಯ ನಾಗರಿಕ ಬಸ್ ರಿಯಾಯಿತಿ, ಕೆಎಸ್ಆರ್ಟಿಸಿ",
        "action_label": "🚌 KSRTC ಬುಕಿಂಗ್",
        "action_url": "https://ksrtc.in"
    },
    {
        "id": "faq_user_215",
        "question": "ವಿವಾಹ ಪ್ರಮಾಣಪತ್ರದ ಡೂಪ್ಲಿಕೇಟ್ ಪ್ರತಿ (Certified Copy of Marriage Certificate) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "duplicate marriage certificate online kaveri 2.0 download certified copy ವಿವಾಹ ಪ್ರಮಾಣಪತ್ರ ನಕಲು ಪ್ರತಿ",
        "answer": """### 💍 ವಿವಾಹ ಪ್ರಮಾಣಪತ್ರದ ಅಧಿಕೃತ ನಕಲು ಪ್ರತಿ (Certified Copy via Kaveri 2.0)

ಪಾಸ್‌ಪೋರ್ಟ್, ವೀಸಾ ಅಥವಾ ಜಂಟಿ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಮೂಲ ವಿವಾಹ ಪ್ರಮಾಣಪತ್ರ ಕಳೆದುಹೋಗಿದ್ದರೆ ಕಾವೇರಿ 2.0 ಪೋರ್ಟಲ್ ಮೂಲಕ ಸಬ್-ರಿಜಿಸ್ಟ್ರಾರ್ ಡಿಜಿಟಲ್ ಸಹಿಯುಳ್ಳ ನಕಲು ಪ್ರತಿ ಪಡೆಯಬಹುದು.

---

### 📥 ಡೌನ್‌ಲೋಡ್ ಮಾಡುವ ಹಂತಗಳು:
1. [kaveri.karnataka.gov.in](https://kaveri.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ ಸಿಟಿಜನ್ ಲಾಗಿನ್ ಆಗಿ.
2. **'Online Certified Copy (CC) of Registered Document'** ಆಯ್ಕೆಮಾಡಿ.
3. ನೋಂದಣಿಯಾದ ಉಪನೋಂದಣಾಧಿಕಾರಿ ಕಚೇರಿ (SRO Office), ಮದುವೆ ನೋಂದಣಿ ಸಂಖ್ಯೆ ಮತ್ತು ವರ್ಷ ನಮೂದಿಸಿ.
4. ನಿಗದಿತ ಶುಲ್ಕ ಪಾವತಿಸಿ ಡಿಜಿಟಲ್ ವಾಟರ್‌ಮಾರ್ಕ್ ಇರುವ ಅಧಿಕೃತ ವಿವಾಹ ಪ್ರಮಾಣಪತ್ರ PDF ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಿ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://kaveri.karnataka.gov.in",
        "keywords": "certified copy marriage certificate, duplicate marriage certificate kaveri, ವಿವಾಹ ಪ್ರಮಾಣಪತ್ರ ನಕಲು ಪ್ರತಿ, ಕಾವೇರಿ 2.0",
        "action_label": "💍 ಕಾವೇರಿ 2.0 ಪೋರ್ಟಲ್",
        "action_url": "https://kaveri.karnataka.gov.in"
    },
    {
        "id": "faq_user_216",
        "question": "ಸರ್ಕಾರಿ ಹಾಸ್ಟೆಲ್‌ಗಳಲ್ಲಿ ವ್ಯಾಸಂಗ ಮಾಡುವ ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಮಾಸಿಕ ಊಟ ಮತ್ತು ನಿರ್ವಹಣಾ ಭತ್ಯೆ ಎಷ್ಟು ಸಿಗುತ್ತದೆ?",
        "normalized_question": "post matric hostel food mess charges maintenance allowance swd bcwd ಸರ್ಕಾರಿ ಹಾಸ್ಟೆಲ್ ಊಟದ ಭತ್ಯೆ",
        "answer": """### 🍲 ಸರ್ಕಾರಿ ಹಾಸ್ಟೆಲ್ ವಿದ್ಯಾರ್ಥಿ ಭತ್ಯೆ & ಊಟದ ಸೌಲಭ್ಯ (SWD & BCWD)

ಸಮಾಜ ಕಲ್ಯಾಣ ಮತ್ತು ಹಿಂದುಳಿದ ವರ್ಗಗಳ ಕಲ್ಯಾಣ ಇಲಾಖೆಯ ಹಾಸ್ಟೆಲ್‌ಗಳಲ್ಲಿ ಪ್ರವೇಶ ಪಡೆದ ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಸಂಪೂರ್ಣ ಉಚಿತ ಊಟ, ವಸತಿ, ಹಾಸಿಗೆ-ಹೊದಿಕೆ, ಗ್ರಂಥಾಲಯ ಹಾಗೂ ಸ್ಪರ್ಧಾತ್ಮಕ ಪರೀಕ್ಷಾ ತರಬೇತಿ ಪುಸ್ತಕಗಳನ್ನು ಒದಗಿಸಲಾಗುತ್ತದೆ.

---

### 💰 ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಸಿಗುವ ನೆರವು:
* **ಮೆಟ್ರಿಕ್ ನಂತರದ ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ (Post-Matric):** ಸರ್ಕಾರವೇ ಪ್ರತಿ ವಿದ್ಯಾರ್ಥಿಗೆ ಮಾಸಿಕ ನಿಗದಿತ ಊಟದ ಮೆಸ್ ವೆಚ್ಚ ಭರಿಸುತ್ತದೆ.
* **ಹಾಸ್ಟೆಲ್ ಸೀಟು ಸಿಗದ ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ (ವಿದ್ಯಾಸಿರಿ):** ಸರ್ಕಾರಿ ಹಾಸ್ಟೆಲ್‌ಗಳಲ್ಲಿ ಕೊಠಡಿ ಕೊರತೆಯಿಂದ ಪ್ರವೇಶ ಸಿಗದ ಅರ್ಹ ಹಿಂದುಳಿದ/ದಲಿತ ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ ಪ್ರತಿ ತಿಂಗಳು **₹1,500 ಊಟ ಮತ್ತು ವಸತಿ ಸಹಾಯಧನ (Vidyasiri)** ನೇರವಾಗಿ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [sw.karnataka.gov.in](https://sw.karnataka.gov.in) | [bcwd.karnataka.gov.in](https://bcwd.karnataka.gov.in)""",
        "category": "EDUCATION",
        "language": "kn",
        "source_url": "https://sw.karnataka.gov.in",
        "keywords": "hostel mess allowance, vidyasiri 1500 monthly, bcwd hostel food, ಹಾಸ್ಟೆಲ್ ಊಟದ ಭತ್ಯೆ, ವಿದ್ಯಾಸಿರಿ ಸಹಾಯಧನ",
        "action_label": "🍲 ಸಮಾಜ ಕಲ್ಯಾಣ ಇಲಾಖೆ",
        "action_url": "https://sw.karnataka.gov.in"
    },
    {
        "id": "faq_user_217",
        "question": "ಬಿಬಿಎಂಪಿ ಹೊರವಲಯ / ನಗರಸಭೆ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಇ-ಆಸ್ತಿ (e-Aasthi) ಇ-ಖಾತಾ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "eaasthi karnataka urban local bodies e khata download municipality ಇ-ಆಸ್ತಿ ನಗರಸಭೆ ಇ-ಖಾತಾ",
        "answer": """### 🏢 ನಗರ ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಗಳ ಇ-ಆಸ್ತಿ ಪೋರ್ಟಲ್ (e-Aasthi Karnataka)

ಬೆಂಗಳೂರು ಹೊರತುಪಡಿಸಿ ರಾಜ್ಯದ ಎಲ್ಲಾ ನಗರ ಮಹಾನಗರ ಪಾಲಿಕೆಗಳು, ನಗರಸಭೆ, ಪುರಸಭೆ ಮತ್ತು ಪಟ್ಟಣ ಪಂಚಾಯಿತಿಗಳ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಡಿಜಿಟಲ್ ಇ-ಖಾತಾ ನೀಡಲು ನಗರಾಭಿವೃದ್ಧಿ ಇಲಾಖೆಯು **e-Aasthi** ತಂತ್ರಾಂಶ ಬಳಸುತ್ತದೆ.

---

### 📜 ಇ-ಖಾತಾ ಡೌನ್‌ಲೋಡ್ ಮಾಡುವ ವಿಧಾನ:
1. [eaasthi.karnataka.gov.in](https://eaasthi.karnataka.gov.in) ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ.
2. ನಿಮ್ಮ ಜಿಲ್ಲೆ ಮತ್ತು ನಗರ ಸ್ಥಳೀಯ ಸಂಸ್ಥೆಯನ್ನು (City Municipal Council / TMC) ಆಯ್ಕೆಮಾಡಿ.
3. ಆಸ್ತಿ ಗುರುತಿನ ಸಂಖ್ಯೆ (Property PID / SAS Application No) ನಮೂದಿಸಿ.
4. ಪಾಲಿಕೆ ಆಯುಕ್ತರು/ಮುಖ್ಯಾಧಿಕಾರಿಗಳ ಡಿಜಿಟಲ್ ಸಹಿ ಮಾಡಿರುವ ಅಧಿಕೃತ **ನಮೂನೆ-3 (Form-3 Property Register Extract)** ಇ-ಖಾತಾ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://eaasthi.karnataka.gov.in",
        "keywords": "eaasthi portal, municipality e khata form 3, urban local body property tax, ಇ-ಆಸ್ತಿ, ನಗರಸಭೆ ಇ-ಖಾತಾ",
        "action_label": "🏢 e-Aasthi ಪೋರ್ಟಲ್",
        "action_url": "https://eaasthi.karnataka.gov.in"
    }
]

# =========================================================================
# 15. EXPANSION BATCH 7: EVERYDAY CITIZEN ESSENTIALS (218 - 235)
# =========================================================================

ADDITIONAL_EXPANSION_FAQS_BATCH_7 = [
    {
        "id": "faq_user_218",
        "question": "ಜನಸೇವಕ (Janasevaka) ಯೋಜನೆ ಮೂಲಕ ಮನೆ ಬಾಗಿಲಿಗೇ ಸರ್ಕಾರಿ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು ತರಿಸಿಕೊಳ್ಳುವುದು ಹೇಗೆ?",
        "normalized_question": "janasevaka doorstep delivery of government services karnataka booking 08044554455 ಜನಸೇವಕ ಯೋಜನೆ",
        "answer": """### 🚪 ಜನಸೇವಕ ಯೋಜನೆ (Janasevaka Doorstep Delivery of Citizen Services)

ಸರ್ಕಾರಿ ಕಚೇರಿಗಳಿಗೆ ಅಲೆಯದೆ ಕೇವಲ ಒಂದು ಫೋನ್ ಕರೆ ಅಥವಾ ಆನ್‌ಲೈನ್ ಸ್ಲಾಟ್ ಬುಕಿಂಗ್ ಮೂಲಕ ಮನೆ ಬಾಗಿಲಿಗೇ ಸರ್ಕಾರಿ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು ತಲುಪಿಸುವ ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಜನಸ್ನೇಹಿ ಸೇವೆ.

---

### 📋 ಮನೆ ಬಾಗಿಲಿಗೆ ಲಭ್ಯವಿರುವ ಪ್ರಮುಖ 50+ ಸೇವೆಗಳು:
* **ಕಂದಾಯ ಪ್ರಮಾಣಪತ್ರಗಳು:** ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ, ವಾಸಸ್ಥಳ ದೃಢೀಕರಣ, ಜೀವಂತ ಪ್ರಮಾಣಪತ್ರ (Life Certificate).
* **ಆರೋಗ್ಯ & ಗುರುತು:** ಆಯುಷ್ಮಾನ್ ಭಾರತ್ ಕಾರ್ಡ್, ಹಿರಿಯ ನಾಗರಿಕರ ಗುರುತಿನ ಚೀಟಿ, ವಿಶೇಷ ಚೇತನರ ಕಾರ್ಡ್.
* **ಆಹಾರ & ಸಾರಿಗೆ:** ರೇಷನ್ ಕಾರ್ಡ್ ತಿದ್ದುಪಡಿ/ಹೊಸ ಕಾರ್ಡ್ ಅರ್ಜಿ, ಸಾರಿಗೆ ಇಲಾಖೆಯ ಲರ್ನರ್ಸ್ ಲೈಸೆನ್ಸ್ (LLR) ಸಹಾಯ.

---

### 📞 ಸ್ಲಾಟ್ ಬುಕ್ ಮಾಡುವ ವಿಧಾನ:
1. **ಟೋಲ್-ಫ್ರೀ ಕಾಲ್ ಸೆಂಟರ್:** **080-44554455** ಗೆ ಕರೆ ಮಾಡಿ ನಿಮಗೆ ಬೇಕಾದ ಸೇವೆ ಮತ್ತು ಅನುಕೂಲಕರ ಸಮಯದ ಸ್ಲಾಟ್ ಬುಕ್ ಮಾಡಿ.
2. **ವೆಬ್‌ಸೈಟ್ ಮೂಲಕ:** [janasevaka.karnataka.gov.in](https://janasevaka.karnataka.gov.in) ನಲ್ಲಿ ಲಾಗಿನ್ ಆಗಿ ಅಪಾಯಿಂಟ್‌ಮೆಂಟ್ ಬುಕ್ ಮಾಡಿ.
3. ನಿಗದಿತ ಸಮಯಕ್ಕೆ ಜನಸೇವಕ ಪ್ರತಿನಿಧಿ ನಿಮ್ಮ ಮನೆಗೆ ಬಂದು ಬಯೋಮೆಟ್ರಿಕ್ ಸ್ಕ್ಯಾನರ್ ಮೂಲಕ ದಾಖಲೆ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ಪ್ರಕ್ರಿಯೆ ಮುಗಿಸುತ್ತಾರೆ. ಪ್ರಮಾಣಪತ್ರ ಮುದ್ರಣವಾದ ನಂತರ ನೇರವಾಗಿ ಮನೆಗೆ ತಲುಪಿಸಲಾಗುತ್ತದೆ (ಸೇವಾ ಶುಲ್ಕ: ಕೇವಲ ₹115).""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://janasevaka.karnataka.gov.in",
        "keywords": "janasevaka karnataka, doorstep government services, 08044554455 helpline, ಜನಸೇವಕ ಯೋಜನೆ, ಮನೆ ಬಾಗಿಲಿಗೆ ಸೇವೆ",
        "action_label": "🚪 ಜನಸೇವಕ ಪೋರ್ಟಲ್",
        "action_url": "https://janasevaka.karnataka.gov.in"
    },
    {
        "id": "faq_user_219",
        "question": "ಇ-ದಾಖಿಲ್ (e-Daakhil) ಮೂಲಕ ಗ್ರಾಹಕರ ವೇದಿಕೆಗೆ (Consumer Court) ಆನ್‌ಲೈನ್ ವಂಚನೆ ದೂರು ಸಲ್ಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "edaakhil consumer court online complaint compensation karnataka ಇ-ದಾಖಿಲ್ ಗ್ರಾಹಕರ ದೂರು ವೇದಿಕೆ",
        "answer": """### ⚖️ ಇ-ದಾಖಿಲ್ (e-Daakhil) — ಗ್ರಾಹಕರ ನ್ಯಾಯಾಲಯ ಆನ್‌ಲೈನ್ ದೂರು ಪೋರ್ಟಲ್

ಆನ್‌ಲೈನ್ ಶಾಪಿಂಗ್ ವಂಚನೆ, ದೋಷಪೂರಿತ ಎಲೆಕ್ಟ್ರಾನಿಕ್ ವಸ್ತುಗಳು, ಬಿಲ್ಡರ್ ವೈಫಲ್ಯ, ಆಸ್ಪತ್ರೆ ಅಥವಾ ವಿಮಾ ಕಂಪನಿಗಳ ಸೇವಾ ನ್ಯೂನತೆಯ ವಿರುದ್ಧ ಪರಿಹಾರ ಪಡೆಯಲು ವಕೀಲರಿಲ್ಲದೆಯೇ ಜಿಲ್ಲಾ ಗ್ರಾಹಕರ ಆಯೋಗಕ್ಕೆ (District Consumer Forum) ದೂರು ಸಲ್ಲಿಸಬಹುದು.

---

### 💻 ಆನ್‌ಲೈನ್ ದೂರು ಸಲ್ಲಿಕೆಯ ಹಂತಗಳು:
1. **ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [edaakhil.nic.in](https://edaakhil.nic.in)
2. ಗ್ರಾಹಕರಾಗಿ (Consumer) ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಹಾಗೂ ಇಮೇಲ್ ಮೂಲಕ ನೋಂದಾಯಿಸಿಕೊಳ್ಳಿ.
3. ನಿಮ್ಮ ಜಿಲ್ಲೆಯ **ಜಿಲ್ಲಾ ಗ್ರಾಹಕರ ವ್ಯಾಜ್ಯಗಳ ಪರಿಹಾರ ಆಯೋಗ (DCDRC)** ಆಯ್ಕೆಮಾಡಿ.
4. ಕಳಪೆ ಸೇವೆ ನೀಡಿದ ಕಂಪನಿ/ವ್ಯಕ್ತಿಯ ಹೆಸರು, ವಿಳಾಸ, ಬಿಲ್ ಪ್ರತಿ, ವಾರಂಟಿ ಕಾರ್ಡ್ ಹಾಗೂ ನೀವು ಅನುಭವಿಸಿದ ನಷ್ಟಕ್ಕೆ ಕೋರಿದ ಪರಿಹಾರ ಮೊತ್ತವನ್ನು ನಮೂದಿಸಿ.
5. ಆನ್‌ಲೈನ್ ಕೋರ್ಟ್ ಶುಲ್ಕ ಪಾವತಿಸಿ (₹5 ಲಕ್ಷದವರೆಗಿನ ಕ್ಲೇಮ್‌ಗಳಿಗೆ ಕೋರ್ಟ್ ಫೀ ಸಂಪೂರ್ಣ ಉಚಿತ).
6. ನೋಟಿಸ್ ಜಾರಿ ಮತ್ತು ವಿಚಾರಣೆಯ ಹಂತಗಳನ್ನು ಪೋರ್ಟಲ್‌ನಲ್ಲೇ ಲೈವ್ ಆಗಿ ಟ್ರ್ಯಾಕ್ ಮಾಡಬಹುದು.""",
        "category": "LEGAL",
        "language": "kn",
        "source_url": "https://edaakhil.nic.in",
        "keywords": "edaakhil consumer complaint, district consumer court karnataka, online consumer fraud case, ಇ-ದಾಖಿಲ್, ಗ್ರಾಹಕರ ವೇದಿಕೆ ದೂರು",
        "action_label": "⚖️ e-Daakhil ಪೋರ್ಟಲ್",
        "action_url": "https://edaakhil.nic.in"
    },
    {
        "id": "faq_user_220",
        "question": "ಪ್ಯಾನ್ ಕಾರ್ಡ್ ಮತ್ತು ಆಧಾರ್ ಕಾರ್ಡ್ ಲಿಂಕ್ ಆಗಿದೆಯೇ ಎಂದು ಉಚಿತವಾಗಿ ಚೆಕ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "check pan aadhaar link status income tax portal online ಪ್ಯಾನ್ ಆಧಾರ್ ಲಿಂಕ್ ಚೆಕ್",
        "answer": """### 💳 ಪ್ಯಾನ್-ಆಧಾರ್ ಜೋಡಣೆ ಸ್ಥಿತಿ ಪರಿಶೀಲನೆ (PAN-Aadhaar Link Status)

ಬ್ಯಾಂಕ್ ವಹಿವಾಟು, ಆದಾಯ ತೆರಿಗೆ ರಿಟರ್ನ್ಸ್ (ITR), ಮುದ್ರಾಂಕ ನೋಂದಣಿ ಹಾಗೂ ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳ ಸೌಲಭ್ಯಕ್ಕೆ ಪ್ಯಾನ್ ಕಾರ್ಡ್‌ಗೆ ಆಧಾರ್ ಲಿಂಕ್ ಆಗಿರುವುದು ಕಡ್ಡಾಯ.

---

### 🔍 ಪರಿಶೀಲಿಸುವ ವಿಧಾನ:
1. **ಆದಾಯ ತೆರಿಗೆ ಇ-ಫೈಲಿಂಗ್ ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [incometax.gov.in](https://www.incometax.gov.in)
2. ಮುಖಪುಟದಲ್ಲಿರುವ **'Link Aadhaar Status'** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ **10 ಅಂಕಿಗಳ PAN ನಂಬರ್** ಮತ್ತು **12 ಅಂಕಿಗಳ ಆಧಾರ್ ನಂಬರ್** ನಮೂದಿಸಿ.
4. **'View Link Aadhaar Status'** ಬಟನ್ ಕ್ಲಿಕ್ ಮಾಡಿ.
5. *"Your PAN is already linked to given Aadhaar"* ಎಂದು ಬಂದರೆ ಲಿಂಕ್ ಸಕ್ರಿಯವಾಗಿದೆ.
6. ಲಿಂಕ್ ಆಗಿರದಿದ್ದರೆ ಅದೇ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ 'Link Aadhaar' ಮೂಲಕ ಶುಲ್ಕ ಪಾವತಿಸಿ ತಕ್ಷಣ ಲಿಂಕ್ ಮಾಡಿಕೊಳ್ಳಬೇಕು.""",
        "category": "CERTIFICATES",
        "language": "kn",
        "source_url": "https://www.incometax.gov.in",
        "keywords": "pan aadhaar link status, check pan link incometax, uti nsdl pan status, ಪ್ಯಾನ್ ಆಧಾರ್ ಲಿಂಕ್ ಚೆಕ್, ಆದಾಯ ತೆರಿಗೆ",
        "action_label": "💳 ಆದಾಯ ತೆರಿಗೆ ಪೋರ್ಟಲ್",
        "action_url": "https://www.incometax.gov.in"
    },
    {
        "id": "faq_user_221",
        "question": "ವಾಹನ ಮಾಲೀಕರು ಮೃತಪಟ್ಟಾಗ ವಾರಸುದಾರರಿಗೆ ಆರ್‌ಸಿ ವರ್ಗಾವಣೆ (Transfer of Ownership on Death) ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "vehicle rc transfer after death of owner form 31 legal heir parivahan ವಾಹನ ಮಾಲೀಕರ ಮರಣ ಆರ್‌ಸಿ ವರ್ಗಾವಣೆ",
        "answer": """### 🚘 ಮೃತ ವ್ಯಕ್ತಿಯ ವಾಹನದ ಆರ್‌ಸಿ ವರ್ಗಾವಣೆ ಪ್ರಕ್ರಿಯೆ (Form 31)

ವಾಹನದ ನೋಂದಾಯಿತ ಮಾಲೀಕರು ಮೃತಪಟ್ಟಾಗ ಕಾನೂನುಬದ್ಧ ವಾರಸುದಾರರ ಹೆಸರಿಗೆ ಆರ್‌ಸಿ ವರ್ಗಾಯಿಸಲು ಮೋಟಾರು ವಾಹನ ಕಾಯ್ದೆಯನ್ವಯ 30 ದಿನಗಳೊಳಗೆ ಆರ್‌ಟಿಒಗೆ ಮಾಹಿತಿ ನೀಡಬೇಕು.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
1. ಮೂಲ ವಾಹನ ನೋಂದಣಿ ಪ್ರಮಾಣಪತ್ರ (Original RC) ಮತ್ತು ವಾಹನ ವಿಮೆ.
2. ಮಾಲೀಕರ ಅಧಿಕೃತ ಮರಣ ಪ್ರಮಾಣಪತ್ರ (Death Certificate).
3. ತಹಶೀಲ್ದಾರ್ ನೀಡಿದ ವಾರಸುದಾರಿಕೆ ಪ್ರಮಾಣಪತ್ರ (Family Tree / Surviving Member Certificate).
4. ಇತರ ಎಲ್ಲಾ ಕಾನೂನುಬದ್ಧ ವಾರಸುದಾರರಿಂದ ನಿರಾಕ್ಷೇಪಣಾ ಅಫಿಡವಿಟ್ (No Objection Affidavit).
5. ಹೊಸ ಮಾಲೀಕರ ಆಧಾರ್ ಕಾರ್ಡ್, ಫೋಟೋ ಮತ್ತು ಮಾಲಿನ್ಯ ನಿಯಂತ್ರಣ ಪ್ರಮಾಣಪತ್ರ (PUC).

---

### 💻 ಅರ್ಜಿ ವಿಧಾನ:
* [parivahan.gov.in](https://parivahan.gov.in) ನಲ್ಲಿ **'Transfer of Ownership (Death Case - Form 31)'** ಅರ್ಜಿ ಭರ್ತಿ ಮಾಡಿ ಶುಲ್ಕ ಪಾವತಿಸಿ ಸಂಬಂಧಪಟ್ಟ ಆರ್‌ಟಿಒ ಕಚೇರಿಗೆ ದಾಖಲೆ ಸಲ್ಲಿಸಬೇಕು.""",
        "category": "TRANSPORT",
        "language": "kn",
        "source_url": "https://parivahan.gov.in",
        "keywords": "rc transfer after death, form 31 parivahan, legal heir vehicle transfer, ವಾಹನ ಆರ್‌ಸಿ ವರ್ಗಾವಣೆ, ವಾರಸುದಾರಿಕೆ ಆರ್‌ಸಿ",
        "action_label": "🚘 ಪರಿವಾಹನ್ ವಾಹನ ಸೇವೆ",
        "action_url": "https://parivahan.gov.in"
    },
    {
        "id": "faq_user_222",
        "question": "ಬೆಂಗಳೂರಿನಲ್ಲಿ ಮಳೆನೀರು ಕೊಯ್ಲು (Rainwater Harvesting - RWH) ಕಡ್ಡಾಯವೇ? ದಂಡ ತಪ್ಪಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "bwssb rainwater harvesting rwh rules mandatory penalty bangalore ಮಳೆನೀರು ಕೊಯ್ಲು ಜಲಮಂಡಳಿ",
        "answer": """### 🌧️ BWSSB ಮಳೆನೀರು ಕೊಯ್ಲು (RWH) ಕಡ್ಡಾಯ ನಿಯಮಾವಳಿ & ದಂಡ ವಿನಾಯಿತಿ

ಬೆಂಗಳೂರು ನಗರದಲ್ಲಿ ಅಂತರ್ಜಲ ಸಂರಕ್ಷಣೆಗಾಗಿ ಜಲ ಮಂಡಳಿಯು (BWSSB) ನಿರ್ದಿಷ್ಟ ಅಳತೆಯ ಕಟ್ಟಡಗಳಿಗೆ ಮಳೆನೀರು ಕೊಯ್ಲು ಅಳವಡಿಕೆಯನ್ನು ಶಾಸನಬದ್ಧವಾಗಿ ಕಡ್ಡಾಯಗೊಳಿಸಿದೆ.

---

### 📌 ನಿಯಮ ಯಾರಿಗೆ ಅನ್ವಯಿಸುತ್ತದೆ?:
* **60x40 ಅಡಿ (2,400 ಚದರಡಿ) ಮತ್ತು ಅದಕ್ಕಿಂತ ಹೆಚ್ಚಿನ** ವಿಸ್ತೀರ್ಣದ ನಿವೇಶನದಲ್ಲಿರುವ ಎಲ್ಲಾ ಹಳೆಯ ಕಟ್ಟಡಗಳು.
* **30x40 ಅಡಿ (1,200 ಚದರಡಿ) ಮತ್ತು ಅದಕ್ಕಿಂತ ಹೆಚ್ಚಿನ** ವಿಸ್ತೀರ್ಣದಲ್ಲಿ ಹೊಸದಾಗಿ ನಿರ್ಮಿಸುವ ಎಲ್ಲಾ ಕಟ್ಟಡಗಳು.

---

### ⚠️ ಅಳವಡಿಸದಿದ್ದರೆ ವಿಧಿಸುವ ದಂಡ:
* RWH ಅಳವಡಿಸದಿದ್ದರೆ ಮೊದಲ 3 ತಿಂಗಳು ನೀರಿನ ಬಿಲ್‌ನಲ್ಲಿ **25% ದಂಡ**, ನಂತರ ಪ್ರತಿ ತಿಂಗಳು ನೀರಿನ ಬಿಲ್‌ನಲ್ಲಿ **50% ಹೆಚ್ಚುವರಿ ದಂಡ** ವಿಧಿಸಲಾಗುತ್ತದೆ.

---

### 🛠️ ದಂಡ ತಪ್ಪಿಸುವ ವಿಧಾನ:
ಮಳೆನೀರು ಶೇಖರಣಾ ಟ್ಯಾಂಕ್ ಅಥವಾ ಇಂಗುಗುಂಡಿ (Recharge Well) ನಿರ್ಮಿಸಿ BWSSB ಪೋರ್ಟಲ್‌ನಲ್ಲಿ [bwssb.karnataka.gov.in](https://bwssb.karnataka.gov.in) ಪೋಟೋ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ಇಂಜಿನಿಯರ್ ಪರಿಶೀಲನೆಗೆ ವಿನಂತಿಸಿದರೆ ದಂಡ ತಕ್ಷಣ ರದ್ದಾಗುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bwssb.karnataka.gov.in",
        "keywords": "bwssb rwh rules, rainwater harvesting mandatory bangalore, rwh penalty waiver, ಮಳೆನೀರು ಕೊಯ್ಲು, ಜಲ ಮಂಡಳಿ ದಂಡ",
        "action_label": "🌧️ BWSSB RWH ವಿವರ",
        "action_url": "https://bwssb.karnataka.gov.in"
    },
    {
        "id": "faq_user_223",
        "question": "ಪಿಎಫ್ (EPFO PF) ಹಣವನ್ನು ಮುಂಗಡವಾಗಿ (PF Advance / Form 31) ಮೊಬೈಲ್‌ನಲ್ಲೇ ಡ್ರಾ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "epfo pf advance withdrawal online form 31 uan member portal ಪಿಎಫ್ ಮುಂಗಡ ಹಣ ಡ್ರಾ",
        "answer": """### 💰 ಇಪಿಎಫ್‌ಒ ಮುಂಗಡ ಹಣ ಹಿಂಪಡೆಯುವಿಕೆ (Online PF Advance Withdrawal)

ತುರ್ತು ವೈದ್ಯಕೀಯ ಚಿಕಿತ್ಸೆ, ಮನೆ ನಿರ್ಮಾಣ, ಮದುವೆ ಅಥವಾ ನಿರುದ್ಯೋಗದ ಸಂದರ್ಭದಲ್ಲಿ ನಿಮ್ಮ PF ಖಾತೆಯಲ್ಲಿರುವ ಹಣವನ್ನು ಕೆಲಸದಲ್ಲಿದ್ದಾಗಲೇ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಮುಂಗಡವಾಗಿ ಹಿಂಪಡೆಯಬಹುದು.

---

### 📋 ಅರ್ಹತಾ ಷರತ್ತುಗಳು:
1. ನಿಮ್ಮ UAN (Universal Account Number) ಸಕ್ರಿಯವಾಗಿರಬೇಕು.
2. UAN ಗೆ ಆಧಾರ್, ಪ್ಯಾನ್ ಮತ್ತು ಬ್ಯಾಂಕ್ ಖಾತೆ (IFSC ಕೋಡ್ ಸಮೇತ) ಲಿಂಕ್ ಆಗಿರಬೇಕು.
3. ಆಧಾರ್ ಲಿಂಕ್ ಆಗಿರುವ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಚಾಲ್ತಿಯಲ್ಲಿರಬೇಕು.

---

### 🚀 ಮುಂಗಡ ಕ್ಲೇಮ್ ಮಾಡುವ ವಿಧಾನ:
1. **UAN ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [unifiedportal-mem.epfindia.gov.in](https://unifiedportal-mem.epfindia.gov.in)
2. UAN ಮತ್ತು ಪಾಸ್‌ವರ್ಡ್ ಹಾಕಿ ಲಾಗಿನ್ ಆಗಿ.
3. **'Online Services -> Claim (Form-31, 19, 10C)'** ಆಯ್ಕೆಮಾಡಿ.
4. ಬ್ಯಾಂಕ್ ಖಾತೆ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ ವೆರಿಫೈ ಮಾಡಿ.
5. **'Form 31 (PF Advance)'** ಆಯ್ಕೆಮಾಡಿ ಕಾರಣ (Illness / Purchase of House / Marriage) ನಮೂದಿಸಿ ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್/ಕ್ಯಾನ್ಸಲ್ ಚೆಕ್ ಫೋಟೋ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
6. ಆಧಾರ್ OTP ದೃಢೀಕರಿಸಿ ಸಲ್ಲಿಸಿ. 3 ರಿಂದ 7 ದಿನಗಳಲ್ಲಿ ಹಣ ನೇರವಾಗಿ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ.""",
        "category": "LABOUR",
        "language": "kn",
        "source_url": "https://unifiedportal-mem.epfindia.gov.in",
        "keywords": "epfo pf advance form 31, uan pf withdrawal online, umang app pf claim, ಪಿಎಫ್ ಹಣ ಡ್ರಾ, ಇಪಿಎಫ್ ಮುಂಗಡ",
        "action_label": "💰 EPFO ಸದಸ್ಯ ಪೋರ್ಟಲ್",
        "action_url": "https://unifiedportal-mem.epfindia.gov.in"
    },
    {
        "id": "faq_user_224",
        "question": "ಸಪ್ತಪದಿ ಯೋಜನೆ ಮತ್ತು ಸರಳ ಸಾಮೂಹಿಕ ವಿವಾಹ ಯೋಜನೆಯಡಿ ₹50,000 ಪ್ರೋತ್ಸಾಹಧನ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "saptapadi scheme muzrai mass marriage 50000 gold thali assistance ಸಪ್ತಪದಿ ಯೋಜನೆ ಧಾರ್ಮಿಕ ದತ್ತಿ",
        "answer": """### 💍 ಮುಜರಾಯಿ ಇಲಾಖೆಯ ಸಪ್ತಪದಿ ಸರಳ ಸಾಮೂಹಿಕ ವಿವಾಹ ಯೋಜನೆ

ಧಾರ್ಮಿಕ ದತ್ತಿ (ಮುಜರಾಯಿ) ಇಲಾಖೆಯ 'ಎ' ಮತ್ತು 'ಬಿ' ದರ್ಜೆಯ ದೇವಾಲಯಗಳಲ್ಲಿ ನಡೆಯುವ ಸರಳ ಸಾಮೂಹಿಕ ವಿವಾಹಗಳಲ್ಲಿ ಮದುವೆಯಾಗುವ ನವದಂಪತಿಗಳಿಗೆ ಸರ್ಕಾರ ಆರ್ಥಿಕ ಹಾಗೂ ಬಂಗಾರದ ನೆರವು ನೀಡುತ್ತದೆ.

---

### 🎁 ನವದಂಪತಿಗಳಿಗೆ ಸಿಗುವ ಸೌಲಭ್ಯಗಳು:
* **ವಧುವಿಗೆ:** ಮಾಂಗಲ್ಯ (ಚಿನ್ನದ ತಾಳಿ) ಖರೀದಿಗೆ **₹40,000** ನೇರ ನಗದು ಸಹಾಯಧನ.
* **ಧಾರೆ ಸೀರೆ & ಉಡುಗೊರೆ:** ವಧುವಿನ ಬಟ್ಟೆ ಖರೀದಿಗೆ **₹5,000** ಪ್ರೋತ್ಸಾಹಧನ.
* **ವರನಿಗೆ:** ಧೋತಿ, ಶರ್ಟ್ ಮತ್ತು ವಸ್ತ್ರ ಖರೀದಿಗೆ **₹5,000** ಪ್ರೋತ್ಸಾಹಧನ.
* ಒಟ್ಟು **₹50,000 ಮೌಲ್ಯದ ನೆರವು** ನೇರವಾಗಿ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾಗುತ್ತದೆ ಹಾಗೂ ದೇವಾಲಯದಲ್ಲಿ ಊಟ-ವಸತಿ ಉಚಿತ.

📝 ಮದುವೆ ನಿಗದಿತ ದಿನಾಂಕಕ್ಕೆ ಕನಿಷ್ಠ 30 ದಿನ ಮುಂಚಿತವಾಗಿ ಸಂಬಂಧಪಟ್ಟ ಮುಜರಾಯಿ ದೇವಾಲಯದ ಕಾರ್ಯನಿರ್ವಾಹಕ ಅಧಿಕಾರಿಗೆ (EO) ಅರ್ಜಿ ಸಲ್ಲಿಸಬೇಕು.""",
        "category": "WELFARE",
        "language": "kn",
        "source_url": "https://muzrai.karnataka.gov.in",
        "keywords": "saptapadi yojana muzrai, mass marriage 50000 scheme, temple marriage gold thali, ಸಪ್ತಪದಿ ಯೋಜನೆ, ಮುಜರಾಯಿ ವಿವಾಹ",
        "action_label": "💍 ಮುಜರಾಯಿ ಇಲಾಖೆ",
        "action_url": "https://muzrai.karnataka.gov.in"
    },
    {
        "id": "faq_user_225",
        "question": "ಪಶು ಸಂಜೀವಿನಿ (1962) ಆಂಬ್ಯುಲೆನ್ಸ್ ಮತ್ತು ಜಾನುವಾರುಗಳಿಗೆ ಉಚಿತ ಕೃತಕ ಗರ್ಭಧಾರಣೆ ಸೌಲಭ್ಯ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "pashu sanjeevini 1962 animal ambulance cattle ear tagging inaf ಪಶು ಸಂಜೀವಿನಿ 1962 ಸಹಾಯವಾಣಿ",
        "answer": """### 🐄 ಪಶು ಸಂಜೀವಿನಿ (1962) — ರೈತರ ಮನೆ ಬಾಗಿಲಿಗೆ ಜಾನುವಾರು ತುರ್ತು ಚಿಕಿತ್ಸಾ ಆಂಬ್ಯುಲೆನ್ಸ್

ಕರ್ನಾಟಕ ಪಶುಸಂಗೋಪನಾ ಇಲಾಖೆಯು ಹಳ್ಳಿಗಳಲ್ಲಿ ರೈತರ ಹಸು, ಎಮ್ಮೆ, ಕುರಿ ಮತ್ತು ಮೇಕೆಗಳಿಗೆ ತುರ್ತು ಚಿಕಿತ್ಸೆ ನೀಡಲು ಸುಸಜ್ಜಿತ ಪಶು ಆಂಬ್ಯುಲೆನ್ಸ್ ಸೇವೆ ಒದಗಿಸುತ್ತದೆ.

---

### 📞 ತುರ್ತು ಪಶು ವೈದ್ಯಕೀಯ ಸಹಾಯವಾಣಿ:
* **ಟೋಲ್-ಫ್ರೀ ಕಾಲ್ ಸೆಂಟರ್: 1962** (ಬೆಳಗ್ಗೆಯಿಂದ ರಾತ್ರಿಯವರೆಗೆ ಲಭ್ಯ).
* ಹಸು ಕರು ಹಾಕಲು ತೊಂದರೆಯಾದಾಗ, ವಿಷ ಪ್ರಾಶನ, ಹೊಟ್ಟೆ ಉಬ್ಬರ, ಅಪಘಾತ ಅಥವಾ ತೀವ್ರ ಜ್ವರ ಬಂದಾಗ 1962 ಗೆ ಕರೆ ಮಾಡಿದರೆ ಪಶುವೈದ್ಯರು ಮತ್ತು ಶಸ್ತ್ರಚಿಕಿತ್ಸಾ ಸಲಕರಣೆಗಳಿರುವ ಆಂಬ್ಯುಲೆನ್ಸ್ ನೇರವಾಗಿ ನಿಮ್ಮ ಕೊಟ್ಟಿಗೆಗೆ ಬರುತ್ತದೆ.

---

### 🏷️ ಇನಾಫ್ (INAF / Pashu Aadhaar) ಕಿವಿ ಓಲೆ ಮಹತ್ವ:
ಪ್ರತಿ ಜಾನುವಾರಿಗೆ 12 ಅಂಕಿಗಳ ಬಾರ್‌ಕೋಡ್ ಕಿವಿ ಓಲೆ (Ear Tag) ಹಾಕಿ ಡಿಜಿಟಲ್ ನೋಂದಣಿ ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಟ್ಯಾಗ್ ಇದ್ದರೆ ಮಾತ್ರ ಉಚಿತ ಕಾಲುಬಾಯಿ ಲಸಿಕೆ, ಕೃತಕ ಗರ್ಭಧಾರಣೆ ಹಾಗೂ ಹಾಲು ಪ್ರೋತ್ಸಾಹಧನ ಸಿಗುತ್ತದೆ.""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://ahvs.karnataka.gov.in",
        "keywords": "pashu sanjeevini 1962, animal mobile ambulance karnataka, inaf ear tag, ಪಶು ಸಂಜೀವಿನಿ, ಪಶು ವೈದ್ಯಕೀಯ ಆಂಬ್ಯುಲೆನ್ಸ್",
        "action_label": "🐄 ಪಶುಸಂಗೋಪನಾ ಇಲಾಖೆ",
        "action_url": "https://ahvs.karnataka.gov.in"
    },
    {
        "id": "faq_user_226",
        "question": "ಸಣ್ಣ ಹೋಟೆಲ್, ಮೆಸ್, ಬೇಕರಿ ಅಥವಾ ಬೀದಿ ಆಹಾರ ವ್ಯಾಪಾರಕ್ಕೆ FSSAI ಫುಡ್ ಲೈಸೆನ್ಸ್ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "fssai food license registration online foscos small hotel mess home bakery ಎಫ್‌ಎಸ್‌ಎಸ್‌ಎಐ ಆಹಾರ ಪರವಾನಗಿ",
        "answer": """### 🍲 ಎಫ್‌ಎಸ್‌ಎಸ್‌ಎಐ ಆಹಾರ ಸುರಕ್ಷತಾ ಪರವಾನಗಿ (FSSAI Food License / FosCoS)

ಆಹಾರ ಪದಾರ್ಥ ತಯಾರಿಸುವ, ಮಾರಾಟ ಮಾಡುವ ಸಣ್ಣ ಕ್ಯಾಂಟೀನ್, ಬೇಕರಿ, ಗೃಹ ಆಧಾರಿತ ಕೇಕ್ ತಯಾರಕರು (Home Bakers), ದಿನಸಿ ಅಂಗಡಿ ಮತ್ತು ಜ್ಯೂಸ್ ಸೆಂಟರ್‌ಗಳಿಗೆ FSSAI ನೋಂದಣಿ ಕಾನೂನುಬದ್ಧವಾಗಿ ಕಡ್ಡಾಯ.

---

### 📜 2 ವಿಧದ ಪರವಾನಗಿಗಳು:
1. **FSSAI Basic Registration (ಸಣ್ಣ ವ್ಯಾಪಾರಿಗಳಿಗೆ):** ವಾರ್ಷಿಕ ವಹಿವಾಟು ₹12 ಲಕ್ಷದ ಒಳಗಿರುವ ಸಣ್ಣ ಅಂಗಡಿ/ಮೆಸ್‌ಗಳಿಗೆ (ವಾರ್ಷಿಕ ಸರ್ಕಾರಿ ಶುಲ್ಕ ಕೇವಲ ₹100).
2. **State Food License:** ವಾರ್ಷಿಕ ವಹಿವಾಟು ₹12 ಲಕ್ಷದಿಂದ ₹20 ಕೋಟಿ ವರೆಗಿನ ಹೋಟೆಲ್/ರೆಸ್ಟೋರೆಂಟ್‌ಗಳಿಗೆ.

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ವಿಧಾನ:
1. [foscos.fssai.gov.in](https://foscos.fssai.gov.in) ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ.
2. ವ್ಯಾಪಾರಿಯ ಆಧಾರ್ ಕಾರ್ಡ್, ಪಾಸ್‌ಪೋರ್ಟ್ ಫೋಟೋ ಮತ್ತು ವ್ಯಾಪಾರ ಸ್ಥಳದ ವಿಳಾಸ ದಾಖಲೆ (ವಿದ್ಯುತ್ ಬಿಲ್/ಬಾಡಿಗೆ ಒಪ್ಪಂದ) ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
3. ಆನ್‌ಲೈನ್ ಶುಲ್ಕ ಪಾವತಿಸಿದ 7 ರಿಂದ 15 ದಿನಗಳಲ್ಲಿ ಡಿಜಿಟಲ್ ಕ್ಯೂಆರ್ ಕೋಡ್ ಹೊಂದಿರುವ **14 ಅಂಕಿಗಳ FSSAI Registration Certificate** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://foscos.fssai.gov.in",
        "keywords": "fssai registration online, foscos food license, food safety certificate karnataka, ಎಫ್‌ಎಸ್‌ಎಸ್‌ಎಐ ಲೈಸೆನ್ಸ್, ಆಹಾರ ಸುರಕ್ಷತೆ",
        "action_label": "🍲 FSSAI FosCoS ಪೋರ್ಟಲ್",
        "action_url": "https://foscos.fssai.gov.in"
    },
    {
        "id": "faq_user_227",
        "question": "ತಾಲೂಕು ಮತ್ತು ಜಿಲ್ಲಾ ಸರ್ಕಾರಿ ಆಸ್ಪತ್ರೆಗಳಲ್ಲಿ ಉಚಿತ ಡಯಾಲಿಸಿಸ್ (Free Dialysis) ಸೇವೆ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "free dialysis services government taluk hospital suvarana arogya nephrology ಉಚಿತ ಡಯಾಲಿಸಿಸ್ ಸೇವೆ",
        "answer": """### 🏥 ಸರ್ಕಾರಿ ಆಸ್ಪತ್ರೆಗಳಲ್ಲಿ ಉಚಿತ ಡಯಾಲಿಸಿಸ್ ಸೇವೆ (Free Dialysis Network)

ಮೂತ್ರಪಿಂಡ (Kidney Failure) ವೈಫಲ್ಯದಿಂದ ಬಳಲುತ್ತಿರುವ ರೋಗಿಗಳಿಗೆ ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಆರೋಗ್ಯ ಇಲಾಖೆಯು ಎಲ್ಲಾ ಜಿಲ್ಲಾ ಆಸ್ಪತ್ರೆಗಳು ಹಾಗೂ ಪ್ರಮುಖ ತಾಲೂಕು ಸಾರ್ವಜನಿಕ ಆಸ್ಪತ್ರೆಗಳಲ್ಲಿ ಸಂಪೂರ್ಣ ಉಚಿತ ಹೆಮೋಡಯಾಲಿಸಿಸ್ (Hemodialysis) ಸೇವೆ ಒದಗಿಸುತ್ತದೆ.

---

### 🌟 ಸೌಲಭ್ಯದ ಮುಖ್ಯಾಂಶಗಳು:
* **ಸಂಪೂರ್ಣ ಉಚಿತ:** ಬಿಪಿಎಲ್ ಮತ್ತು ಎಪಿಎಲ್ ಎರಡೂ ವರ್ಗದ ರೋಗಿಗಳಿಗೆ ಡಯಾಲಿಸಿಸ್ ಕಿಟ್, ಡಯಲೈಸರ್, ಔಷಧಿ ಹಾಗೂ ಇಂಜೆಕ್ಷನ್‌ಗಳು ಉಚಿತ.
* **ಏಕ-ಬಳಕೆಯ ಡಯಲೈಸರ್ (Single-Use Dialyzer):** ಸೋಂಕು ತಡೆಗಟ್ಟಲು ಪ್ರತಿ ಡಯಾಲಿಸಿಸ್‌ಗೆ ಹೊಸ ಕಿಟ್ ಬಳಸಲಾಗುತ್ತದೆ.

---

### 📝 ನೋಂದಣಿ ಪ್ರಕ್ರಿಯೆ:
ರೋಗಿಯ ಆಧಾರ್ ಕಾರ್ಡ್, ರೇಷನ್ ಕಾರ್ಡ್ ಮತ್ತು ನೆಫ್ರಾಲಜಿಸ್ಟ್ (ಕಿಡ್ನಿ ತಜ್ಞ ವೈದ್ಯರ) ಡಯಾಲಿಸಿಸ್ ಶಿಫಾರಸು ಪತ್ರದೊಂದಿಗೆ ಸಮೀಪದ ತಾಲೂಕು/ಜಿಲ್ಲಾ ಸರ್ಕಾರಿ ಆಸ್ಪತ್ರೆಯ ಡಯಾಲಿಸಿಸ್ ಕೇಂದ್ರಕ್ಕೆ ತೆರಳಿ ವಾರಕ್ಕೆ 2 ರಿಂದ 3 ಬಾರಿಯ ಸ್ಲಾಟ್ ನಿಗದಿಪಡಿಸಿಕೊಳ್ಳಬಹುದು.""",
        "category": "HEALTH",
        "language": "kn",
        "source_url": "https://arogya.karnataka.gov.in",
        "keywords": "free dialysis karnataka, taluk hospital dialysis center, sast kidney care, ಉಚಿತ ಡಯಾಲಿಸಿಸ್, ಆರೋಗ್ಯ ಇಲಾಖೆ",
        "action_label": "🏥 ಆರೋಗ್ಯ ಇಲಾಖೆ",
        "action_url": "https://arogya.karnataka.gov.in"
    },
    {
        "id": "faq_user_228",
        "question": "ಜಮೀನಿನ 11E ಸ್ಕೆಚ್ (11E Sketch Online Download) ಭೂಮಿ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "11e sketch online download mojini bhoomi land registration map 11ಇ ಸ್ಕೆಚ್ ಡೌನ್‌ಲೋಡ್",
        "answer": """### 📐 11E ಸ್ಕೆಚ್ (11E Sketch) ಡೌನ್‌ಲೋಡ್ ಮಾಡುವ ವಿಧಾನ

ಕೃಷಿ ಜಮೀನಿನ ಒಂದು ಭಾಗವನ್ನು ಮಾರಾಟ ಮಾಡಲು ಅಥವಾ ನೋಂದಣಿ ಮಾಡಿಸಲು ಜಮೀನಿನ ಪ್ರತ್ಯೇಕ ನಕ್ಷೆಯನ್ನು ದೃಢೀಕರಿಸುವ **11E ಸ್ಕೆಚ್** ಕಡ್ಡಾಯ.

---

### 💻 ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪಡೆಯುವ ಹಂತಗಳು:
1. **ಮೋಜಿನಿ ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [mojini.karnataka.gov.in](https://mojini.karnataka.gov.in)
2. **'Application Status / Download Sketch'** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ಜಿಲ್ಲೆ, ತಾಲೂಕು, ಹೋಬಳಿ, ಗ್ರಾಮ ಮತ್ತು **11E ಅರ್ಜಿ ಸಂಖ್ಯೆ (Application Number)** ನಮೂದಿಸಿ.
4. ಸರ್ಕಾರಿ ಭೂಮಾಪಕರು ಅಳೆದು ತಹಶೀಲ್ದಾರ್ ಅನುಮೋದನೆ ನೀಡಿದ ಡಿಜಿಟಲ್ ಸಹಿಯುಳ್ಳ ಅಧಿಕೃತ **11E ಸ್ಕೆಚ್ PDF** ಅನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಿ.
5. ಈ ಸ್ಕೆಚ್ ಅನ್ನು ಕಾವೇರಿ 2.0 ನಲ್ಲಿ ಕ್ರಯಪತ್ರ ನೋಂದಣಿಗೆ ನೇರವಾಗಿ ಬಳಸಬಹುದು.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://mojini.karnataka.gov.in",
        "keywords": "11e sketch download, mojini sketch online, bhoomi 11e map, 11ಇ ಸ್ಕೆಚ್, ಮೋಜಿನಿ ನಕ್ಷೆ",
        "action_label": "📐 ಮೋಜಿನಿ 11E ಪೋರ್ಟಲ್",
        "action_url": "https://mojini.karnataka.gov.in"
    },
    {
        "id": "faq_user_229",
        "question": "ಮನೆ ಖಾಲಿ ಇರುವಾಗ ಬೆಸ್ಕಾಂ ವಿದ್ಯುತ್ ಮೀಟರ್ ಅನ್ನು ತಾತ್ಕಾಲಿಕವಾಗಿ ನಿಲುಗಡೆ (Temporary Disconnection) ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "bescom temporary meter disconnection vacant house fixed charges waiver ಬೆಸ್ಕಾಂ ವಿದ್ಯುತ್ ಮೀಟರ್ ನಿಲುಗಡೆ",
        "answer": """### ⚡ ವಿದ್ಯುತ್ ಸಂಪರ್ಕ ತಾತ್ಕಾಲಿಕ ನಿಲುಗಡೆ (Temporary Disconnection of Power Supply)

ಮನೆ ದೀರ್ಘಕಾಲ ಖಾಲಿ ಇದ್ದಾಗ ಅಥವಾ ನವೀಕರಣ (Renovation) ಕಾಮಗಾರಿ ನಡೆಯುವಾಗ ಕನಿಷ್ಠ ಮಾಸಿಕ ಫಿಕ್ಸ್ಡ್ ಚಾರ್ಜಸ್ (Fixed Charges) ಹೊರೆ ತಪ್ಪಿಸಲು ಮೀಟರ್ ಸಂಪರ್ಕವನ್ನು ತಾತ್ಕಾಲಿಕವಾಗಿ ನಿಲುಗಡೆ ಮಾಡಬಹುದು.

---

### 📋 ನಿಯಮಗಳು & ಹಂತಗಳು:
1. ಎಲ್ಲಾ ಹಿಂದಿನ ವಿದ್ಯುತ್ ಬಿಲ್ ಬಾಕಿಯನ್ನು ಶೂನ್ಯ (Zero Balance) ಪಾವತಿಸಿ.
2. ನಿಮ್ಮ ಸ್ಥಳೀಯ ಎಸ್ಕಾಂ ಸೆಕ್ಷನ್ ಆಫೀಸರ್‌ಗೆ (AE/AEE) ಲಿಖಿತ ಅರ್ಜಿ ನೀಡಿ ಅಥವಾ ಎಸ್ಕಾಂ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ 'Request for Temporary Disconnection' ಸಲ್ಲಿಸಿ.
3. ಎಸ್ಕಾಂ ಸಿಬ್ಬಂದಿ ಮೀಟರ್ ರೀಡಿಂಗ್ ದಾಖಲಿಸಿ ತಾತ್ಕಾಲಿಕವಾಗಿ ಫ್ಯೂಸ್ ಸಂಪರ್ಕ ಕಡಿತಗೊಳಿಸುತ್ತಾರೆ.
4. ಪುನಃ ಸಂಪರ್ಕ ಬೇಕಾದಾಗ ರೀ-ಕನೆಕ್ಷನ್ ಶುಲ್ಕ (Reconnection Fee: ಸುಮಾರು ₹100 ರಿಂದ ₹250) ಪಾವತಿಸಿ 24 ಗಂಟೆಗಳಲ್ಲಿ ವಿದ್ಯುತ್ ಮರುಪಡೆಯಬಹುದು.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bescom.karnataka.gov.in",
        "keywords": "temporary power disconnection bescom, meter fixed charge waiver, ವಿದ್ಯುತ್ ಮೀಟರ್ ತಾತ್ಕಾಲಿಕ ನಿಲುಗಡೆ, ಬೆಸ್ಕಾಂ",
        "action_label": "⚡ ಬೆಸ್ಕಾಂ ಸೇವೆಗಳು",
        "action_url": "https://bescom.karnataka.gov.in"
    },
    {
        "id": "faq_user_230",
        "question": "ಕರ್ನಾಟಕ ಸ್ಕಿಲ್ ಕನೆಕ್ಟ್ (Karnataka Skill Connect Portal) ನಲ್ಲಿ ಉದ್ಯೋಗ ಮತ್ತು ಕೌಶಲ್ಯ ತರಬೇತಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "karnataka skill connect portal register job seekers free training youth ಸ್ಕಿಲ್ ಕನೆಕ್ಟ್ ಉದ್ಯೋಗ ಪೋರ್ಟಲ್",
        "answer": """### 🎓 ಕರ್ನಾಟಕ ಸ್ಕಿಲ್ ಕನೆಕ್ಟ್ ಪೋರ್ಟಲ್ (Skill Connect Portal — Kaushalya Karnataka)

ರಾಜ್ಯದ ನಿರುದ್ಯೋಗಿ ಯುವಕ-ಯುವತಿಯರು, ಐಟಿಐ, ಡಿಪ್ಲೋಮಾ ಮತ್ತು ಪದವೀಧರರಿಗೆ ಉಚಿತ ಉದ್ಯೋಗ ತರಬೇತಿ ಹಾಗೂ ಖಾಸಗಿ ಕಂಪನಿಗಳಲ್ಲಿ ನೇರ ಉದ್ಯೋಗ ಕಲ್ಪಿಸುವ ಸರ್ಕಾರದ ಅಧಿಕೃತ ವೇದಿಕೆ.

---

### 🌟 ಪೋರ್ಟಲ್‌ನ ಪ್ರಮುಖ ಲಾಭಗಳು:
* **ನೇರ ಉದ್ಯೋಗಾವಕಾಶಗಳು:** ಸಾವಿರಾರು ನೋಂದಾಯಿತ ಕಂಪನಿಗಳ ಖಾಲಿ ಹುದ್ದೆಗಳಿಗೆ ಯಾವುದೇ ಶುಲ್ಕವಿಲ್ಲದೆ ನೇರ ಅರ್ಜಿ ಸಲ್ಲಿಕೆ.
* **ಉಚಿತ ತರಬೇತಿ ಕೋರ್ಸ್‌ಗಳು:** ಕೃತಕ ಬುದ್ಧಿಮತ್ತೆ (AI), ಸೈಬರ್ ಸೆಕ್ಯುರಿಟಿ, ಡೇಟಾ ಎಂಟ್ರಿ, ಸಿಎನ್‌ಸಿ ಆಪರೇಟರ್, ಹೆಲ್ತ್‌ಕೇರ್ ಅಸಿಸ್ಟೆಂಟ್ ಸೇರಿದಂತೆ ಬೇಡಿಕೆಯುಳ್ಳ ಕೋರ್ಸ್‌ಗಳಿಗೆ ಸರ್ಕಾರಿ ಪ್ರಮಾಣಪತ್ರದೊಂದಿಗೆ ಉಚಿತ ತರಬೇತಿ.
* **ಉದ್ಯೋಗ ಮೇಳ (Mega Job Fairs):** ರಾಜ್ಯಾದ್ಯಂತ ನಡೆಯುವ ಉದ್ಯೋಗ ಮೇಳಗಳ ನೇರ ಮಾಹಿತಿ ಮತ್ತು ಹಾಲ್ ಟಿಕೆಟ್.

🔗 **ನೋಂದಣಿ ಪೋರ್ಟಲ್:** [skillconnect.kaushalkar.com](https://skillconnect.kaushalkar.com)""",
        "category": "EDUCATION",
        "language": "kn",
        "source_url": "https://skillconnect.kaushalkar.com",
        "keywords": "skill connect karnataka, kaushalya karnataka job portal, free skill training youth, ಸ್ಕಿಲ್ ಕನೆಕ್ಟ್, ಕೌಶಲ್ಯ ಕರ್ನಾಟಕ, ಉದ್ಯೋಗ ಮೇಳ",
        "action_label": "🎓 ಸ್ಕಿಲ್ ಕನೆಕ್ಟ್ ಪೋರ್ಟಲ್",
        "action_url": "https://skillconnect.kaushalkar.com"
    },
    {
        "id": "faq_user_231",
        "question": "ಮಕ್ಕಳು ಪೋಷಕರ ಆಸ್ತಿ ಕಸಿದುಕೊಂಡು ನಿರ್ಲಕ್ಷಿಸಿದರೆ ಹಿರಿಯ ನಾಗರಿಕರ ಕಾಯ್ದೆಯಡಿ ಆಸ್ತಿ ವಾಪಸ್ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "senior citizens maintenance act cancel gift deed property restoration ac court ಹಿರಿಯ ನಾಗರಿಕರ ಆಸ್ತಿ ರಕ್ಷಣೆ",
        "answer": """### 👵 ಹಿರಿಯ ನಾಗರಿಕರ ಪೋಷಣೆ ಮತ್ತು ರಕ್ಷಣೆ ಕಾಯ್ದೆ 2007 (Senior Citizens Maintenance Act)

ಪೋಷಕರು ಪ್ರೀತಿ-ವಿಶ್ವಾಸದಿಂದ ಮಕ್ಕಳಿಗೆ ದಾನಪತ್ರ (Gift Deed) ಅಥವಾ ವಿಭಾಗಪತ್ರದ ಮೂಲಕ ಬರೆದುಕೊಟ್ಟ ಆಸ್ತಿಯನ್ನು, ಮಕ್ಕಳು ಪೋಷಕರನ್ನು ಸರಿಯಾಗಿ ನೋಡಿಕೊಳ್ಳದಿದ್ದರೆ ಸಂಪೂರ್ಣ ರದ್ದುಪಡಿಸಿ ವಾಪಸ್ ಪಡೆಯುವ ಪ್ರಬಲ ಕಾನೂನು ರಕ್ಷಣೆ.

---

### ⚖️ ಆಸ್ತಿ ವಾಪಸ್ ಪಡೆಯುವ ಪ್ರಕ್ರಿಯೆ:
1. **ಸಹಾಯಕ ಆಯುಕ್ತರ (AC Court) ಮುಂದೆ ಅರ್ಜಿ:** ಹಿರಿಯ ನಾಗರಿಕರು ವಕೀಲರ ಅಗತ್ಯವಿಲ್ಲದೆ ನೇರವಾಗಿ ಉಪವಿಭಾಗಾಧಿಕಾರಿಗಳ (Assistant Commissioner - AC) ನ್ಯಾಯಾಲಯಕ್ಕೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು.
2. **ದಾನಪತ್ರ ರದ್ದತಿ ಆದೇಶ:** ಮಕ್ಕಳು ಮೂಲ ಷರತ್ತಿನಂತೆ ಊಟ, ವಸತಿ, ಔಷಧಿ ನೀಡದೆ ವಂಚಿಸಿದ್ದರೆ, ಎಸಿ ಕೋರ್ಟ್ ಆ ದಾನಪತ್ರವನ್ನು **ಶೂನ್ಯ (Null & Void)** ಎಂದು ಘೋಷಿಸಿ ಆಸ್ತಿಯನ್ನು ಪುನಃ ಪೋಷಕರ ಹೆಸರಿಗೇ ವರ್ಗಾಯಿಸಲು ಆದೇಶಿಸುತ್ತದೆ.
3. **ಮಾಸಿಕ ಜೀವನಾಂಶ:** ನಿರ್ಲಕ್ಷ್ಯ ಮಾಡುವ ಮಕ್ಕಳಿಂದ ಪೋಷಕರಿಗೆ ಮಾಸಿಕ ಗರಿಷ್ಠ ₹10,000 ವರೆಗೆ ಜೀವನಾಂಶ ಕೊಡಿಸಲಾಗುತ್ತದೆ.

📞 **ತುರ್ತು ಸಹಾಯವಾಣಿ: 14567 (Elderline)**""",
        "category": "LEGAL",
        "language": "kn",
        "source_url": "https://welfare.karnataka.gov.in",
        "keywords": "senior citizens act cancellation gift deed, ac court maintenance parents, elderline 14567, ಹಿರಿಯ ನಾಗರಿಕರ ರಕ್ಷಣೆ, ದಾನಪತ್ರ ರದ್ದು",
        "action_label": "👵 ಹಿರಿಯ ನಾಗರಿಕರ ವೇದಿಕೆ",
        "action_url": "https://welfare.karnataka.gov.in"
    },
    {
        "id": "faq_user_232",
        "question": "ಕೆಎಸ್‌ಆರ್‌ಟಿಸಿ ನಮ್ಮ ಕಾರ್ಗೋ (Namma Cargo) ಮೂಲಕ ಪಾರ್ಸಲ್ ಬುಕ್ ಮಾಡುವುದು ಮತ್ತು ಟ್ರ್ಯಾಕ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "ksrtc namma cargo parcel courier booking tracking rates ನಮ್ಮ ಕಾರ್ಗೋ ಪಾರ್ಸಲ್ ಬುಕಿಂಗ್",
        "answer": """### 📦 ಕೆಎಸ್‌ಆರ್‌ಟಿಸಿ 'ನಮ್ಮ ಕಾರ್ಗೋ' (Namma Cargo Parcel Services)

ಕರ್ನಾಟಕ ಸಾರಿಗೆ ನಿಗಮವು ರಾಜ್ಯದ ಪ್ರತಿಯೊಂದು ನಗರ, ಪಟ್ಟಣ ಹಾಗೂ ಹಳ್ಳಿಗಳಿಗೆ ಅತಿ ಕಡಿಮೆ ದರದಲ್ಲಿ ಅತಿ ವೇಗವಾಗಿ ಪಾರ್ಸಲ್ ಮತ್ತು ಕೊರಿಯರ್ ತಲುಪಿಸುವ ಸರಕು ಸಾರಿಗೆ ಸೇವೆ.

---

### 🚚 ಪ್ರಮುಖ ಅನುಕೂಲಗಳು:
* **ಅದೇ ದಿನ ತಲುಪಿಸುವ ಸೇವೆ (Same Day Delivery):** ಬಸ್ ಮಾರ್ಗಗಳ ಮೂಲಕ ಕೆಲವೇ ಗಂಟೆಗಳಲ್ಲಿ ಸರಕು ತಲುಪುತ್ತದೆ.
* **ಕಡಿಮೆ ದರ:** ಖಾಸಗಿ ಕೊರಿಯರ್‌ಗಳಿಗಿಂತ 40% ಕಡಿಮೆ ದರದಲ್ಲಿ ಲಗೇಜ್ ಮತ್ತು ವಾಣಿಜ್ಯ ಸರಕು ರವಾನೆ.
* **ಲೈವ್ ಟ್ರ್ಯಾಕಿಂಗ್:** ಬುಕಿಂಗ್ ರಶೀದಿಯಲ್ಲಿರುವ LR Number ಬಳಸಿ ಮೊಬೈಲ್‌ನಲ್ಲೇ ಪಾರ್ಸಲ್ ಎಲ್ಲಿದೆ ಎಂದು ಟ್ರ್ಯಾಕ್ ಮಾಡಬಹುದು.

---

### 📦 ಬುಕ್ ಮಾಡುವ ವಿಧಾನ:
ನಿಮ್ಮ ಹತ್ತಿರದ KSRTC ಬಸ್ ನಿಲ್ದಾಣದಲ್ಲಿರುವ ಅಧಿಕೃತ **'Namma Cargo Counter'** ಗೆ ಭೇಟಿ ನೀಡಿ ಕಳುಹಿಸುವವರ ಮತ್ತು ಸ್ವೀಕರಿಸುವವರ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ ಬುಕ್ ಮಾಡಬಹುದು.""",
        "category": "TRANSIT",
        "language": "kn",
        "source_url": "https://ksrtc.in",
        "keywords": "ksrtc namma cargo, parcel courier service karnataka, namma cargo tracking lr number, ನಮ್ಮ ಕಾರ್ಗೋ, ಕೆಎಸ್ಆರ್ಟಿಸಿ ಪಾರ್ಸಲ್",
        "action_label": "📦 ನಮ್ಮ ಕಾರ್ಗೋ ವಿವರ",
        "action_url": "https://ksrtc.in"
    },
    {
        "id": "faq_user_233",
        "question": "ನನ್ನ ಏರಿಯಾದ ಪೊಲೀಸ್ ಬೀಟ್ ಅಧಿಕಾರಿ (Know Your Police Beat Officer) ಯಾರು ಎಂದು ತಿಳಿಯುವುದು ಹೇಗೆ?",
        "normalized_question": "know your beat police officer contact number ksp citizen portal ಬೀಟ್ ಪೊಲೀಸ್ ಅಧಿಕಾರಿ ವಿವರ",
        "answer": """### 👮 ನನ್ನ ಪೊಲೀಸ್ ಬೀಟ್ ಅಧಿಕಾರಿ (Karnataka Police Beat System)

ನಿಮ್ಮ ಬಡಾವಣೆ ಅಥವಾ ಗ್ರಾಮದ ಸುರಕ್ಷತೆಗಾಗಿ ನಿಯೋಜಿಸಲಾದ ಸ್ಥಳೀಯ ಪೊಲೀಸ್ ಕಾನ್‌ಸ್ಟೇಬಲ್ / ಹೆಡ್ ಕಾನ್‌ಸ್ಟೇಬಲ್ (Beat Officer) ಸಂಪರ್ಕ ವಿವರಗಳನ್ನು ಸುಲಭವಾಗಿ ಪಡೆಯಬಹುದು.

---

### 🔍 ಬೀಟ್ ಅಧಿಕಾರಿ ವಿವರ ತಿಳಿಯುವ ವಿಧಾನ:
1. **KSP Citizen Portal / App:** [ksp.karnataka.gov.in](https://ksp.karnataka.gov.in) ಅಥವಾ **KSP App** ತೆರೆಯಿರಿ.
2. **'Know Your Police Station / Beat Officer'** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ಜಿಲ್ಲೆ, ಪೊಲೀಸ್ ಠಾಣೆ ಮತ್ತು ನಿಮ್ಮ ರಸ್ತೆ/ಗ್ರಾಮದ ಹೆಸರು ಆಯ್ಕೆಮಾಡಿ.
4. ನಿಮ್ಮ ಏರಿಯಾ ಬೀಟ್ ಅಧಿಕಾರಿಯ ಹೆಸರು, ಅವರ ಅಧಿಕೃತ ಸಿಮ್ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಹಾಗೂ ಠಾಣಾಧಿಕಾರಿಯ (PSI/Inspector) ಸಂಖ್ಯೆ ಲಭ್ಯವಾಗುತ್ತದೆ.

💡 ತುರ್ತು ಸಂದರ್ಭಗಳಲ್ಲಿ ನೇರವಾಗಿ **112** ಗೆ ಕರೆ ಮಾಡಬಹುದು.""",
        "category": "POLICE",
        "language": "kn",
        "source_url": "https://ksp.karnataka.gov.in",
        "keywords": "beat police officer contact, ksp know your police, police station officer number, ಬೀಟ್ ಪೊಲೀಸ್ ಅಧಿಕಾರಿ, ಕರ್ನಾಟಕ ಪೊಲೀಸ್",
        "action_label": "👮 ಪೊಲೀಸ್ ಬೀಟ್ ವಿವರ",
        "action_url": "https://ksp.karnataka.gov.in"
    },
    {
        "id": "faq_user_234",
        "question": "ಹೊಸ ವಾಹನಕ್ಕೆ ಫ್ಯಾನ್ಸಿ / ಚಾಯ್ಸ್ ನಂಬರ್ (Fancy Vehicle Registration Number) ಆನ್‌ಲೈನ್ ಹರಾಜಿನಲ್ಲಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "fancy vehicle registration number online auction parivahan rto karnataka ಫ್ಯಾನ್ಸಿ ನಂಬರ್ ಹರಾಜು ವಾಹನ",
        "answer": """### 🚗 ಫ್ಯಾನ್ಸಿ & ಚಾಯ್ಸ್ ನಂಬರ್ ಇ-ಹರಾಜು (Fancy Number Online Auction — Parivahan)

ನಿಮ್ಮ ಹೊಸ ಕಾರು ಅಥವಾ ಬೈಕ್‌ಗೆ ವಿಶೇಷ ನೋಂದಣಿ ಸಂಖ್ಯೆಗಳನ್ನು (ಉದಾ: 0001, 0007, 0999, 1111, 8055 ಇತ್ಯಾದಿ) ಸಾರಿಗೆ ಇಲಾಖೆಯ ಆನ್‌ಲೈನ್ ಹರಾಜು ಮೂಲಕ ಪಾರದರ್ಶಕವಾಗಿ ಪಡೆಯಬಹುದು.

---

### 💻 ಆನ್‌ಲೈನ್ ಹರಾಜಿನಲ್ಲಿ ಭಾಗವಹಿಸುವ ವಿಧಾನ:
1. [parivahan.gov.in](https://parivahan.gov.in) ನಲ್ಲಿ **'Fancy Number Allocation'** ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ.
2. ಸಾರ್ವಜನಿಕ ಬಳಕೆದಾರರಾಗಿ (Public User) ಸೈನ್ ಅಪ್ ಆಗಿ.
3. ನಿಮ್ಮ ಆರ್‌ಟಿಒ (RTO) ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಲಭ್ಯವಿರುವ ನಂಬರ್‌ಗಳ ಪಟ್ಟಿ ವೀಕ್ಷಿಸಿ ಬಯಸಿದ ಸಂಖ್ಯೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.
4. ನಿಗದಿತ ನೋಂದಣಿ ಶುಲ್ಕ (Registration Fee) ಮತ್ತು ಇಎಂಡಿ (EMD) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪಾವತಿಸಿ.
5. ಬಿಡ್ಡಿಂಗ್ ದಿನದಂದು ಆನ್‌ಲೈನ್ ಹರಾಜಿನಲ್ಲಿ ಭಾಗವಹಿಸಿ. ಅತಿ ಹೆಚ್ಚು ಮೊತ್ತ ನಮೂದಿಸಿದವರಿಗೆ ಆ ಸಂಖ್ಯೆಯ ಹಂಚಿಕೆ ಪತ್ರ (Allotment Letter) ದೊರೆಯುತ್ತದೆ.""",
        "category": "TRANSPORT",
        "language": "kn",
        "source_url": "https://parivahan.gov.in",
        "keywords": "fancy number booking parivahan, choice vehicle registration auction, rto fancy number karnataka, ಫ್ಯಾನ್ಸಿ ನಂಬರ್ ಹರಾಜು, ವಾಹನ ಸಂಖ್ಯೆ",
        "action_label": "🚗 ಪರಿವಾಹನ್ ಫ್ಯಾನ್ಸಿ ನಂಬರ್",
        "action_url": "https://parivahan.gov.in"
    },
    {
        "id": "faq_user_235",
        "question": "ಗ್ರಾಮ ಪಂಚಾಯಿತಿಯಲ್ಲಿ ಕುಡಿಯುವ ನೀರಿನ ಗುಣಮಟ್ಟವನ್ನು FTK ಕಿಟ್ ಮೂಲಕ ಉಚಿತವಾಗಿ ಪರೀಕ್ಷಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "drinking water quality testing ftk field test kit gram panchayat jal jeevan mission ನೀರಿನ ಗುಣಮಟ್ಟ ಪರೀಕ್ಷೆ",
        "answer": """### 💧 ಜಲ ಜೀವನ್ ಮಿಷನ್ — ಕುಡಿಯುವ ನೀರಿನ ಗುಣಮಟ್ಟ ಪರೀಕ್ಷೆ (Water Quality Testing FTK Kit)

ಗ್ರಾಮೀಣ ಭಾಗದ ನಳ್ಳಿ ನೀರು ಮತ್ತು ಕೊಳವೆಬಾವಿ ನೀರಿನಲ್ಲಿ ಫ್ಲೋರೈಡ್, ನೈಟ್ರೇಟ್, ಉಪ್ಪು, ಕಬ್ಬಿಣಾಂಶ ಅಥವಾ ಬ್ಯಾಕ್ಟೀರಿಯಾ ಕಲ್ಮಶಗಳಿವೆಯೇ ಎಂದು ಪರೀಕ್ಷಿಸುವ ಗ್ರಾಮೀಣ ನೀರು ಸರಬರಾಜು ಇಲಾಖೆಯ ಸೌಲಭ್ಯ.

---

### 🧪 ಪರೀಕ್ಷೆ ಮಾಡಿಸುವ ವಿಧಾನ:
* ಪ್ರತಿ ಗ್ರಾಮ ಪಂಚಾಯಿತಿಯ 5 ಜನ ಮಹಿಳೆಯರಿಗೆ (ಸ್ವಸಹಾಯ ಸಂಘದ ಸದಸ್ಯೆಯರು / ಆಶಾ ಕಾರ್ಯಕರ್ತೆಯರು) **FTK (Field Test Kit)** ತರಬೇತಿ ನೀಡಲಾಗಿರುತ್ತದೆ.
* ನಿಮ್ಮ ಮನೆಯ ಕುಡಿಯುವ ನೀರಿನ ಸ್ಯಾಂಪಲ್ ಅನ್ನು ಗ್ರಾಮ ಪಂಚಾಯಿತಿಗೆ ತೆಗೆದುಕೊಂಡು ಹೋದರೆ ಸ್ಥಳದಲ್ಲೇ ರಾಸಾಯನಿಕ ಕಿಟ್ ಮೂಲಕ ಪರೀಕ್ಷಿಸಿ ನೀರು ಕುಡಿಯಲು ಯೋಗ್ಯವೇ (Potable) ಎಂದು ತಿಳಿಸುತ್ತಾರೆ.
* ಗಂಭೀರ ಕಲ್ಮಶ ಕಂಡುಬಂದಲ್ಲಿ ತಾಲೂಕು/ಜಿಲ್ಲಾ ನೀರು ಪರೀಕ್ಷಾ ಪ್ರಯೋಗಾಲಯಕ್ಕೆ (DWD Laboratory) ಕಳುಹಿಸಿ ಶುದ್ಧೀಕರಣ ಘಟಕ (RO Plant) ಅಥವಾ ಪೈಪ್‌ಲೈನ್ ದುರಸ್ತಿ ಮಾಡಲಾಗುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://rdpr.karnataka.gov.in",
        "keywords": "drinking water test ftk kit, jal jeevan mission water quality, gram panchayat water safety, ನೀರಿನ ಗುಣಮಟ್ಟ ಪರೀಕ್ಷೆ, ಗ್ರಾಮೀಣ ನೀರು ಸರಬರಾಜು",
        "action_label": "💧 ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಇಲಾಖೆ",
        "action_url": "https://rdpr.karnataka.gov.in"
    }
]


# =========================================================================
# 16. EXPANSION BATCH 8: HIGH-VALUE CITIZEN WORKFLOWS & POLICIES (236 - 251)
# =========================================================================

ADDITIONAL_EXPANSION_FAQS_BATCH_8 = [
    {
        "id": "faq_user_236",
        "question": "ವಂಶವೃಕ್ಷ ಪ್ರಮಾಣಪತ್ರ (Family Tree / Surviving Member Certificate) ನಾಡಕಚೇರಿಯಲ್ಲಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "family tree certificate online nadakacheri vanshavruksha legal heir ವಂಶವೃಕ್ಷ ಪ್ರಮಾಣಪತ್ರ",
        "answer": """### 🌳 ವಂಶವೃಕ್ಷ ಪ್ರಮಾಣಪತ್ರ (Family Tree / Vamshavruksha Certificate)

ಕುಟುಂಬದ ಹಿರಿಯರು ಮೃತಪಟ್ಟಾಗ ಅವರ ಜಮೀನು, ಬ್ಯಾಂಕ್ ಠೇವಣಿ, ಚಿನ್ನ, ವಾಹನ ಅಥವಾ ಆಸ್ತಿಗಳನ್ನು ಕಾನೂನುಬದ್ಧ ವಾರಸುದಾರರಿಗೆ ವರ್ಗಾಯಿಸಲು ವಂಶವೃಕ್ಷ ಅತ್ಯಗತ್ಯ.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
1. ಕುಟುಂಬದ ಮೃತ ಮುಖ್ಯಸ್ಥರ ಅಧಿಕೃತ **ಮರಣ ಪ್ರಮಾಣಪತ್ರ (Death Certificate)**.
2. ಎಲ್ಲಾ ಜೀವಂತ ವಾರಸುದಾರರ (ಪತ್ನಿ, ಮಕ್ಕಳು) ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ರೇಷನ್ ಕಾರ್ಡ್.
3. ಮಕ್ಕಳ ಶಾಲಾ ವರ್ಗಾವಣೆ ಪ್ರಮಾಣಪತ್ರ (TC) ಅಥವಾ ಜನ್ಮ ದಿನಾಂಕದ ದಾಖಲೆ.
4. ₹100 ರ ಇ-ಸ್ಟ್ಯಾಂಪ್ ಪೇಪರ್‌ನಲ್ಲಿ ಸಿದ್ಧಪಡಿಸಿದ **ನೋಟರಿ ಅಫಿಡವಿಟ್ (Genealogy Affidavit)**.

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ವಿಧಾನ:
1. [nadakacheri.karnataka.gov.in](https://nadakacheri.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ ಲಾಗಿನ್ ಆಗಿ.
2. **'Attestation of Family Tree'** ಆಯ್ಕೆಮಾಡಿ ಮೃತ ವ್ಯಕ್ತಿ ಹಾಗೂ ಎಲ್ಲಾ ವಾರಸುದಾರರ ಹೆಸರು ಮತ್ತು ಸಂಬಂಧ ನಮೂದಿಸಿ.
3. ಗ್ರಾಮ ಆಡಳಿತಾಧಿಕಾರಿ (VA) ಮನೆಗೆ ಭೇಟಿ ನೀಡಿ ನೆರೆಹೊರೆಯವರ ಪಂಚನಾಮೆ ನಡೆಸಿ ತಹಶೀಲ್ದಾರ್ ಅನುಮೋದನೆಗೆ ಸಲ್ಲಿಸುತ್ತಾರೆ.
4. 15 ರಿಂದ 30 ದಿನಗಳಲ್ಲಿ ನಿಮ್ಮ **RD ಸಂಖ್ಯೆ** ಬಳಸಿ ಅಧಿಕೃತ ಡಿಜಿಟಲ್ ಸಹಿಯುಳ್ಳ ವಂಶವೃಕ್ಷ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.""",
        "category": "CERTIFICATES",
        "language": "kn",
        "source_url": "https://nadakacheri.karnataka.gov.in",
        "keywords": "family tree certificate online, vanshavruksha nadakacheri, legal heir tree, ವಂಶವೃಕ್ಷ ಪ್ರಮಾಣಪತ್ರ, ವಾರಸುದಾರಿಕೆ",
        "action_label": "🌳 ನಾಡಕಚೇರಿ ಪೋರ್ಟಲ್",
        "action_url": "https://nadakacheri.karnataka.gov.in"
    },
    {
        "id": "faq_user_237",
        "question": "ಆಸ್ತಿ ದಾನಪತ್ರ (Gift Deed) ಮತ್ತು ವಿಲ್ (Will) ನಡುವಿನ ವ್ಯತ್ಯಾಸವೇನು? ಮುದ್ರಾಂಕ ಶುಲ್ಕ ಎಷ್ಟು?",
        "normalized_question": "gift deed vs will stamp duty registration charges kaveri 2.0 ದಾನಪತ್ರ ಮತ್ತು ವಿಲ್ ವ್ಯತ್ಯಾಸ",
        "answer": """### 📜 ದಾನಪತ್ರ (Gift Deed) vs ಮರಣ ಶಾಸನ (Will) — ಕಾನೂನು ಮಾರ್ಗದರ್ಶಿ

* **ದಾನಪತ್ರ (Gift Deed):** ಜೀವಿತಾವಧಿಯಲ್ಲೇ ಪ್ರೀತಿ-ವಿಶ್ವಾಸದಿಂದ ಆಸ್ತಿಯನ್ನು ಕುಟುಂಬದ ಸದಸ್ಯರಿಗೆ (ಪತ್ನಿ, ಮಕ್ಕಳು, ಮೊಮ್ಮಕ್ಕಳು) ಸಂಪೂರ್ಣ ಮಾಲೀಕತ್ವ ವರ್ಗಾಯಿಸುವ ಪತ್ರ. ನೋಂದಣಿಯಾದ ತಕ್ಷಣವೇ ಆಸ್ತಿ ಪಡೆಯುವವರ ಪಾಲಾಗುತ್ತದೆ; ಇದನ್ನು ನಂತರ ಏಕಪಕ್ಷೀಯವಾಗಿ ರದ್ದುಪಡಿಸಲು ಬರುವುದಿಲ್ಲ.
* **ವಿಲ್ / ಉಯಿಲು (Will):** ವ್ಯಕ್ತಿಯು ತಾನು ಮರಣ ಹೊಂದಿದ ನಂತರ ತನ್ನ ಆಸ್ತಿ ಯಾರಿಗೆ ಸೇರಬೇಕೆಂದು ಬರೆದಿಡುವ ದಾಖಲೆ. ವ್ಯಕ್ತಿ ಜೀವಂತವಿರುವವರೆಗೂ ಎಷ್ಟು ಬಾರಿಯಾದರೂ ವಿಲ್ ಬದಲಾಯಿಸಬಹುದು ಅಥವಾ ರದ್ದುಪಡಿಸಬಹುದು.

---

### 💰 ಕಾವೇರಿ 2.0 ನೋಂದಣಿ ಮತ್ತು ಮುದ್ರಾಂಕ ಶುಲ್ಕ:
* **ಕುಟುಂಬ ಸದಸ್ಯರ ನಡುವಿನ ದಾನಪತ್ರ:** ಕೇವಲ **₹1,000 ಮುದ್ರಾಂಕ ಶುಲ್ಕ + ₹500 ನೋಂದಣಿ ಶುಲ್ಕ** ಮತ್ತು ಸೆಸ್ (ಒಟ್ಟು ಅತ್ಯಂತ ಕಡಿಮೆ ನಿಗದಿತ ಶುಲ್ಕ).
* **ವಿಲ್ ನೋಂದಣಿ:** ಕೇವಲ ₹200 ನೋಂದಣಿ ಶುಲ್ಕ.

🔗 **ಕಾವೇರಿ 2.0 ಪೋರ್ಟಲ್:** [kaveri.karnataka.gov.in](https://kaveri.karnataka.gov.in)""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://kaveri.karnataka.gov.in",
        "keywords": "gift deed stamp duty family, will registration kaveri, ದಾನಪತ್ರ ಮುದ್ರಾಂಕ ಶುಲ್ಕ, ಉಯಿಲು ನೋಂದಣಿ, ಕಾವೇರಿ 2.0",
        "action_label": "📜 ಕಾವೇರಿ 2.0 ಪೋರ್ಟಲ್",
        "action_url": "https://kaveri.karnataka.gov.in"
    },
    {
        "id": "faq_user_238",
        "question": "ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರದಲ್ಲಿ ಮಣ್ಣು ಪರೀಕ್ಷೆ (Soil Health Card) ಮಾಡಿಸುವುದು ಹೇಗೆ? ವೆಚ್ಚವೆಷ್ಟು?",
        "normalized_question": "soil health card raitha samparka kendra soil testing cost karnataka ಮಣ್ಣು ಪರೀಕ್ಷೆ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ",
        "answer": """### 🌾 ಮಣ್ಣು ಆರೋಗ್ಯ ಪತ್ರಿಕೆ (Soil Health Card Scheme)

ರಸಗೊಬ್ಬರಗಳ ಅತಿಯಾದ ಬಳಕೆಯನ್ನು ತಡೆದು, ಜಮೀನಿನಲ್ಲಿರುವ ಸಾರಜನಕ (N), ರಂಜಕ (P), ಪೊಟ್ಯಾಷ್ (K), ಸಾವಯವ ಇಂಗಾಲ ಮತ್ತು ಪಿಎಚ್ (pH) ಮಟ್ಟವನ್ನು ನಿಖರವಾಗಿ ತಿಳಿಯಲು ಮಣ್ಣು ಪರೀಕ್ಷೆ ಅತ್ಯಗತ್ಯ.

---

### 🧪 ಮಣ್ಣಿನ ಮಾದರಿ ಸಂಗ್ರಹಿಸುವ ವಿಧಾನ:
1. ಜಮೀನಿನ 4-5 ಭಾಗಗಳಲ್ಲಿ 'V' ಆಕಾರದಲ್ಲಿ 6 ರಿಂದ 9 ಇಂಚು ಆಳಕ್ಕೆ ಅಗೆದು ಮೇಲಿನ ಮಣ್ಣು ತೆಗೆಯಿರಿ.
2. ಆ ಮಣ್ಣನ್ನು ಶುದ್ಧ ಬಟ್ಟೆಯ ಮೇಲೆ ಚೆನ್ನಾಗಿ ಮಿಶ್ರಣ ಮಾಡಿ 500 ಗ್ರಾಂ ನಷ್ಟು ಒಣಗಿದ ಮಣ್ಣನ್ನು ಪ್ಲಾಸ್ಟಿಕ್ ಚೀಲದಲ್ಲಿ ಸಂಗ್ರಹಿಸಿ.
3. ರೈತರ ಹೆಸರು, ಸರ್ವೆ ನಂಬರ್ ಮತ್ತು ಬೆಳೆಯುವ ಬೆಳೆಯ ವಿವರವನ್ನು ಚೀಟಿಯಲ್ಲಿ ಬರೆದು ಚೀಲದಲ್ಲಿಡಿ.

---

### 📍 ಎಲ್ಲಿ ಪರೀಕ್ಷಿಸಬೇಕು?:
* ನಿಮ್ಮ ಹೋಬಳಿಯ **ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ (RSK)** ಅಥವಾ ತಾಲೂಕು ಕೃಷಿ ಇಲಾಖೆ ಪ್ರಯೋಗಾಲಯಕ್ಕೆ ಕೇವಲ **₹20 ರಿಂದ ₹50 ರ ನಾಮಮಾತ್ರ ಶುಲ್ಕದಲ್ಲಿ** ಮಣ್ಣಿನ ಮಾದರಿ ಸಲ್ಲಿಸಿ.
* 10 ದಿನಗಳಲ್ಲಿ ಡಿಜಿಟಲ್ **Soil Health Card** ಲಭ್ಯವಾಗುತ್ತದೆ. ಇದರಲ್ಲಿ ಯಾವ ಬೆಳೆಗೆ ಎಷ್ಟು ಪ್ರಮಾಣದ ಗೊಬ್ಬರ ಹಾಕಬೇಕೆಂಬ ನಿಖರ ಶಿಫಾರಸು ಇರುತ್ತದೆ.

🔗 **ಕೃಷಿ ಇಲಾಖೆ:** [raitamitra.karnataka.gov.in](https://raitamitra.karnataka.gov.in)""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://raitamitra.karnataka.gov.in",
        "keywords": "soil health card karnataka, raitha samparka kendra soil test, rsk soil lab, ಮಣ್ಣು ಪರೀಕ್ಷೆ, ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ",
        "action_label": "🌾 ರೈತಮಿತ್ರ ಪೋರ್ಟಲ್",
        "action_url": "https://raitamitra.karnataka.gov.in"
    },
    {
        "id": "faq_user_239",
        "question": "KSRTC ಬಸ್‌ಗಳಲ್ಲಿ ಸಾಕು ಪ್ರಾಣಿಗಳನ್ನು (Pet Animals / Dogs / Cats) ಕರೆದೊಯ್ಯುವ ನಿಯಮಗಳೇನು?",
        "normalized_question": "ksrtc pet travel policy dog cat ticket fare rules ಕೆಎಸ್‌ಆರ್‌ಟಿಸಿ ಸಾಕುಪ್ರಾಣಿ ಪ್ರಯಾಣ ನಿಯಮ",
        "answer": """### 🐕 ಕೆಎಸ್‌ಆರ್‌ಟಿಸಿ ಸಾಕುಪ್ರಾಣಿ ಸಾಗಣೆ ನೀತಿ (KSRTC Pet Carriage Policy)

ಕೆಎಸ್‌ಆರ್‌ಟಿಸಿಯು ತನ್ನ ಸಾಮಾನ್ಯ ಮತ್ತು ನಗರ ಬಸ್‌ಗಳಲ್ಲಿ ಪ್ರಯಾಣಿಕರು ತಮ್ಮ ಸಾಕು ನಾಯಿ, ಬೆಕ್ಕು ಹಾಗೂ ಪಕ್ಷಿಗಳನ್ನು ಕರೆದೊಯ್ಯಲು ನಿರ್ದಿಷ್ಟ ಷರತ್ತುಗಳೊಂದಿಗೆ ಅವಕಾಶ ನೀಡಿದೆ.

---

### 📋 ಪ್ರಮುಖ ಪ್ರಯಾಣ ನಿಯಮಗಳು:
1. **ಅನುಮತಿಸಲಾದ ಬಸ್‌ಗಳು:** ನಗರ, ಸಾಮಾನ್ಯ ಮತ್ತು ಗ್ರಾಮಾಂತರ ಸಾರಿಗೆ ಬಸ್‌ಗಳಲ್ಲಿ ಮಾತ್ರ ಅವಕಾಶ (ಐರಾವತ, ಕ್ಲಬ್ ಕ್ಲಾಸ್ ಮತ್ತು ಎಸಿ ಸ್ಲೀಪರ್ ಬಸ್‌ಗಳಲ್ಲಿ ಸಾಕುಪ್ರಾಣಿಗಳಿಗೆ ಅವಕಾಶವಿಲ್ಲ).
2. **ಟಿಕೆಟ್ ದರ:**
   - ನಾಯಿಗಳಿಗೆ **ಪೂರ್ಣ ವಯಸ್ಕರ ಟಿಕೆಟ್ ದರ (Full Adult Fare)** ಪಡೆಯಲಾಗುತ್ತದೆ.
   - ಚಿಕ್ಕ ನಾಯಿಮರಿ, ಬೆಕ್ಕು ಅಥವಾ ಪಂಜರದಲ್ಲಿರುವ ಹಕ್ಕಿಗಳಿಗೆ **ಅರ್ಧ ಟಿಕೆಟ್ (Child Fare)** ವಿಧಿಸಲಾಗುತ್ತದೆ.
3. **ಸುರಕ್ಷತಾ ಷರತ್ತು:** ನಾಯಿಗೆ ಕಡ್ಡಾಯವಾಗಿ ಬಾಯಿಕವಚ (Muzzle) ಮತ್ತು ಸರಪಳಿ (Leash) ಹಾಕಿರಬೇಕು ಹಾಗೂ ಸಹಪ್ರಯಾಣಿಕರಿಗೆ ಯಾವುದೇ ತೊಂದರೆಯಾಗದಂತೆ ಮಾಲೀಕರೇ ಜವಾಬ್ದಾರಿ ವಹಿಸಬೇಕು.""",
        "category": "TRANSIT",
        "language": "kn",
        "source_url": "https://ksrtc.in",
        "keywords": "ksrtc pet dog ticket fare, carrying pets in ksrtc bus, pet carriage rules karnataka, ಕೆಎಸ್‌ಆರ್‌ಟಿಸಿ ಸಾಕುಪ್ರಾಣಿ ಟಿಕೆಟ್",
        "action_label": "🚌 KSRTC ನಿಯಮಗಳು",
        "action_url": "https://ksrtc.in"
    },
    {
        "id": "faq_user_240",
        "question": "ಕೃಷಿ ಯಂತ್ರೋಪಕರಣಗಳ ಖರೀದಿಗೆ ಸರ್ಕಾರದ 50% ರಿಂದ 90% ಸಬ್ಸಿಡಿ (Krishi Yantra Dhare / DBT) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "farm machinery subsidy karnataka krishi yantradhare tractor power tiller subsidy ಕೃಷಿ ಯಂತ್ರೋಪಕರಣ ಸಬ್ಸಿಡಿ",
        "answer": """### 🚜 ಕೃಷಿ ಯಾಂತ್ರೀಕರಣ ಯೋಜನೆ (Farm Mechanization & Krishi Yantra Dhare)

ಟ್ರ್ಯಾಕ್ಟರ್, ಪವರ್ ಟಿಲ್ಲರ್, ರೋಟಾವೇಟರ್, ಕಳೆ ಕೀಳುವ ಯಂತ್ರ, ಡ್ರೋನ್ ಮತ್ತು ಸ್ಪ್ರೇಯರ್‌ಗಳ ಖರೀದಿಗೆ ಕೃಷಿ ಇಲಾಖೆಯು ನೇರ ಸಹಾಯಧನ (DBT) ನೀಡುತ್ತದೆ.

---

### 💰 ಸಬ್ಸಿಡಿ ರಚನೆ:
* **ಪರಿಶಿಷ್ಟ ಜಾತಿ / ಪರಿಶಿಷ್ಟ ಪಂಗಡದ ರೈತರಿಗೆ (SC/ST):** ಯಂತ್ರದ ಮೌಲ್ಯದ **90% ವರೆಗೆ ಸಬ್ಸಿಡಿ**.
* **ಸಾಮಾನ್ಯ ಮತ್ತು ಸಣ್ಣ/ಅತಿ ಸಣ್ಣ ರೈತರಿಗೆ:** ಯಂತ್ರದ ಮೌಲ್ಯದ **50% ವರೆಗೆ ಸಬ್ಸಿಡಿ**.
* **ಕೃಷಿ ಯಂತ್ರಧಾರೆ (ಬಾಡಿಗೆ ಕೇಂದ್ರಗಳು):** ಕೃಷಿ ಯಂತ್ರಗಳನ್ನು ಖರೀದಿಸಲು ಸಾಧ್ಯವಾಗದ ರೈತರು ಅತ್ಯಂತ ಕಡಿಮೆ ಗಂಟೆಯ ಬಾಡಿಗೆ ದರದಲ್ಲಿ ಹೋಬಳಿ ಮಟ್ಟದ ಕೃಷಿ ಯಂತ್ರಧಾರೆ ಕೇಂದ್ರಗಳಿಂದ ಟ್ರ್ಯಾಕ್ಟರ್ ಮತ್ತು ಹಾರ್ವೆಸ್ಟರ್ ಪಡೆಯಬಹುದು.

---

### 📝 ಅರ್ಜಿ ಸಲ್ಲಿಕೆ:
* ಜಮೀನಿನ ಪಹಣಿ (RTC), ರೈತರ **FID ಕಾರ್ಡ್**, ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್‌ನೊಂದಿಗೆ [raitamitra.karnataka.gov.in](https://raitamitra.karnataka.gov.in) ನಲ್ಲಿ ಅಥವಾ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರದಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಬೇಕು.""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://raitamitra.karnataka.gov.in",
        "keywords": "tractor subsidy karnataka, krishi yantradhare rental, farm mechanization dbt, ಕೃಷಿ ಯಂತ್ರೋಪಕರಣ ಸಬ್ಸಿಡಿ, ಟ್ರ್ಯಾಕ್ಟರ್ ಸಬ್ಸಿಡಿ",
        "action_label": "🚜 ರೈತಮಿತ್ರ ಪೋರ್ಟಲ್",
        "action_url": "https://raitamitra.karnataka.gov.in"
    },
    {
        "id": "faq_user_241",
        "question": "ಬಾಡಿಗೆ ಮನೆ ನೀಡುವ ಮುನ್ನ ಬಾಡಿಗೆದಾರರ ಪೊಲೀಸ್ ಪರಿಶೀಲನೆ (Tenant Police Verification) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಮಾಡಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "tenant police verification karnataka police ksp portal online rent ಬಾಡಿಗೆದಾರರ ಪೊಲೀಸ್ ವೆರಿಫಿಕೇಶನ್",
        "answer": """### 🏠 ಬಾಡಿಗೆದಾರರ ಪೊಲೀಸ್ ಪರಿಶೀಲನೆ (Online Tenant Police Verification — KSP)

ಮನೆ ಮಾಲೀಕರು ಅಪರಿಚಿತರಿಗೆ ಮನೆ, ಫ್ಲಾಟ್ ಅಥವಾ ಪಿಜಿ (PG) ಬಾಡಿಗೆಗೆ ನೀಡುವ ಮುನ್ನ ಸುರಕ್ಷತೆಯ ದೃಷ್ಟಿಯಿಂದ ಹಾಗೂ ಅಪರಾಧ ತಡೆಗಟ್ಟಲು ಪೊಲೀಸ್ ಪರಿಶೀಲನೆ ಮಾಡಿಸುವುದು ಉತ್ತಮ.

---

### 💻 ಆನ್‌ಲೈನ್ ಪ್ರಕ್ರಿಯೆ:
1. **ಕರ್ನಾಟಕ ಪೊಲೀಸ್ ಪೋರ್ಟಲ್:** [ksp.karnataka.gov.in](https://ksp.karnataka.gov.in) ಅಥವಾ **KSP App** ತೆರೆಯಿರಿ.
2. **'Citizen Services -> Tenant / Paying Guest Verification'** ಆಯ್ಕೆಮಾಡಿ.
3. ಮನೆ ಮಾಲೀಕರ ವಿವರ ಮತ್ತು ಬಾಡಿಗೆದಾರರ ಆಧಾರ್ ಕಾರ್ಡ್, ಫೋಟೋ, ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಮತ್ತು ಶಾಶ್ವತ ಊರಿನ ವಿಳಾಸ ನಮೂದಿಸಿ.
4. ನಿಗದಿತ ಶುಲ್ಕ ಪಾವತಿಸಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.
5. ಪೊಲೀಸ್ ಇಲಾಖೆಯು ಬಾಡಿಗೆದಾರರ ಮೇಲೆ ಯಾವುದೇ ಕ್ರಿಮಿನಲ್ ಹಿನ್ನೆಲೆ ಅಥವಾ ಎಫ್‌ಐಆರ್ ದಾಖಲಾಗಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ ಡಿಜಿಟಲ್ ಕ್ಲಿಯರೆನ್ಸ್ ವರದಿ ನೀಡುತ್ತದೆ.""",
        "category": "POLICE",
        "language": "kn",
        "source_url": "https://ksp.karnataka.gov.in",
        "keywords": "tenant verification karnataka police, ksp tenant pg verification online, ಬಾಡಿಗೆದಾರರ ಪೊಲೀಸ್ ಪರಿಶೀಲನೆ, ಕೆಎಸ್‌ಪಿ ಆ್ಯಪ್",
        "action_label": "🏠 KSP ಪೊಲೀಸ್ ಸೇವೆ",
        "action_url": "https://ksp.karnataka.gov.in"
    },
    {
        "id": "faq_user_242",
        "question": "RTE (Right to Education) ಅಡಿಯಲ್ಲಿ ಖಾಸಗಿ ಶಾಲೆಗಳಲ್ಲಿ 25% ಉಚಿತ ಸೀಟು ಪಡೆಯುವ ನಿಯಮಗಳೇನು?",
        "normalized_question": "rte karnataka 25 percent free school admission lottery eligibility ಆರ್‌ಟಿಇ ಉಚಿತ ಶಾಲೆ ಪ್ರವೇಶ",
        "answer": """### 🎒 ಆರ್‌ಟಿಇ (Right to Education - ಶಿಕ್ಷಣ ಹಕ್ಕು ಕಾಯ್ದೆ) ಉಚಿತ ಪ್ರವೇಶ

ಆರ್ಥಿಕವಾಗಿ ಮತ್ತು ಸಾಮಾಜಿಕವಾಗಿ ಹಿಂದುಳಿದ ವರ್ಗಗಳ ಮಕ್ಕಳಿಗೆ ಅನುದಾನರಹಿತ ಖಾಸಗಿ ಶಾಲೆಗಳಲ್ಲಿ LKG ಅಥವಾ 1 ನೇ ತರಗತಿಗೆ 25% ಸೀಟುಗಳನ್ನು ಸಂಪೂರ್ಣ ಉಚಿತವಾಗಿ ನೀಡಲಾಗುತ್ತದೆ (ಶಾಲಾ ಶುಲ್ಕವನ್ನು ಸರ್ಕಾರವೇ ಭರಿಸುತ್ತದೆ).

---

### 📌 ನಿಯಮ & ಆದ್ಯತೆ:
* ಮಗುವಿನ ವಾಸಸ್ಥಳದ 1 ಕಿ.ಮೀ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಯಾವುದೇ ಸರ್ಕಾರಿ ಅಥವಾ ಅನುದಾನಿತ ಶಾಲೆ ಲಭ್ಯವಿಲ್ಲದಿದ್ದರೆ ಮಾತ್ರ ಖಾಸಗಿ ಶಾಲೆಗಳಲ್ಲಿ ಆರ್‌ಟಿಇ ಸೀಟು ಹಂಚಿಕೆ ಮಾಡಲಾಗುತ್ತದೆ.
* ಕುಟುಂಬದ ವಾರ್ಷಿಕ ಆದಾಯ ಮಿತಿ ₹3.50 ಲಕ್ಷ ಮೀರಬಾರದು.

---

### 📋 ಅರ್ಜಿ ವಿಧಾನ:
1. ಶಾಲಾ ಶಿಕ್ಷಣ ಇಲಾಖೆಯ [schooleducation.karnataka.gov.in](https://schooleducation.karnataka.gov.in) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.
2. ಮಗುವಿನ ಜನನ ಪ್ರಮಾಣಪತ್ರ, ಜಾತಿ/ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ (RD Number) ಮತ್ತು ಆಧಾರ್ ಕಾರ್ಡ್ ಲಗತ್ತಿಸಿ.
3. ಕಂಪ್ಯೂಟರೀಕೃತ ಪಾರದರ್ಶಕ ಲಾಟರಿ (Online Lottery System) ಮೂಲಕ ಸೀಟು ಹಂಚಿಕೆಯಾಗುತ್ತದೆ.""",
        "category": "EDUCATION",
        "language": "kn",
        "source_url": "https://schooleducation.karnataka.gov.in",
        "keywords": "rte karnataka online application, right to education free seat, rte lottery result, ಆರ್‌ಟಿಇ ಉಚಿತ ಪ್ರವೇಶ, ಶಿಕ್ಷಣ ಇಲಾಖೆ",
        "action_label": "🎒 ಶಾಲಾ ಶಿಕ್ಷಣ ಪೋರ್ಟಲ್",
        "action_url": "https://schooleducation.karnataka.gov.in"
    },
    {
        "id": "faq_user_243",
        "question": "ಬೆಂಗಳೂರು ಉಪನಗರ ರೈಲು ಯೋಜನೆ (Bengaluru Suburban Railway - BSRP / K-RIDE) ಮಾರ್ಗಗಳು ಮತ್ತು ಕಾರಿಡಾರ್‌ಗಳು ಯಾವುವು?",
        "normalized_question": "bengaluru suburban railway bsrp k ride corridors routes map ಬೆಂಗಳೂರು ಉಪನಗರ ರೈಲು",
        "answer": """### 🚆 ಬೆಂಗಳೂರು ಉಪನಗರ ರೈಲು ಯೋಜನೆ (BSRP — K-RIDE)

ಬೆಂಗಳೂರು ಮಹಾನಗರದ ಟ್ರಾಫಿಕ್ ದಟ್ಟಣೆ ಕಡಿಮೆ ಮಾಡಲು ₹15,767 ಕೋಟಿ ವೆಚ್ಚದಲ್ಲಿ 148.17 ಕಿ.ಮೀ ಉದ್ದದ 4 ಪ್ರಮುಖ ರೈಲು ಕಾರಿಡಾರ್‌ಗಳನ್ನು ನಿರ್ಮಿಸಲಾಗುತ್ತಿದೆ.

---

### 🗺️ 4 ಪ್ರಮುಖ ಉಪನಗರ ಕಾರಿಡಾರ್‌ಗಳು:
1. **ಕಾರಿಡಾರ್ 1 (ಸಂಪಿಗೆ ಲೈನ್):** ಕೆಎಸ್‌ಆರ್ ಬೆಂಗಳೂರು ಸಿಟಿ ರೈಲ್ವೆ ನಿಲ್ದಾಣದಿಂದ ದೇವನಹಳ್ಳಿ (ಕೆಂಪೇಗೌಡ ವಿಮಾನ ನಿಲ್ದಾಣ) ವರೆಗೆ (41.40 ಕಿ.ಮೀ).
2. **ಕಾರಿಡಾರ್ 2 (ಮಲ್ಲಿಗೆ ಲೈನ್):** ಬೈಯಪ್ಪನಹಳ್ಳಿಯಿಂದ ಚಿಕ್ಕಬಾಣಾವರ ವರೆಗೆ (25.01 ಕಿ.ಮೀ - ಯಶವಂತಪುರ, ಹೆಬ್ಬಾಳ ಮಾರ್ಗ).
3. **ಕಾರಿಡಾರ್ 3 (ಪಾರಿಜಾತ ಲೈನ್):** ಕೆಂಗೇರಿಯಿಂದ ವೈಟ್‌ಫೀಲ್ಡ್ ವರೆಗೆ (35.52 ಕಿ.ಮೀ).
4. **ಕಾರಿಡಾರ್ 4 (ಕನಕ ಲೈನ್):** ಹೀಲಲಿಗೆ (ಬೊಮ್ಮಸಂದ್ರ/ಎಲೆಕ್ಟ್ರಾನಿಕ್ ಸಿಟಿ ಸಮೀಪ) ಇಂದ ರಾಜಾನುಕುಂಟೆ ವರೆಗೆ (46.24 ಕಿ.ಮೀ).

💡 ಈ ಎಲ್ಲಾ ರೈಲು ನಿಲ್ದಾಣಗಳು ನಮ್ಮ ಮೆಟ್ರೋ ಮತ್ತು ಬಿಎಂಟಿಸಿ ಬಸ್ ನಿಲ್ದಾಣಗಳೊಂದಿಗೆ ಏಕೀಕೃತ ಇಂಟರ್‌ಚೇಂಜ್ ಸಂಪರ್ಕ ಹೊಂದಲಿವೆ.""",
        "category": "TRANSIT",
        "language": "kn",
        "source_url": "https://kride.in",
        "keywords": "bsrp kride, suburban railway bangalore, mallige corridor 2, sampige line, ಬೆಂಗಳೂರು ಸಬರ್ಬನ್ ರೈಲು, ಕೆ-ರೈಡ್",
        "action_label": "🚆 K-RIDE ಪೋರ್ಟಲ್",
        "action_url": "https://kride.in"
    },
    {
        "id": "faq_user_244",
        "question": "ಹೊಸ ಮನೆ ಕಟ್ಟಿದಾಗ ಹೊಸ ವಿದ್ಯುತ್ ಮೀಟರ್ ಸಂಪರ್ಕಕ್ಕೆ (New Electricity Connection) ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಹಾಕುವುದು ಹೇಗೆ?",
        "normalized_question": "new electricity meter connection online apply bescom hescom escom ಹೊಸ ವಿದ್ಯುತ್ ಸಂಪರ್ಕ",
        "answer": """### ⚡ ಹೊಸ ವಿದ್ಯುತ್ ಮೀಟರ್ ಸಂಪರ್ಕ (Online New Service Connection — Escoms)

ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ವಿದ್ಯುತ್ ಕಂಪನಿಗಳ (BESCOM, HESCOM, GESCOM, MESCOM, CESC) ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ನೂತನ ಮನೆ ಅಥವಾ ಕಟ್ಟಡಗಳಿಗೆ ಆನ್‌ಲೈನ್‌ನಲ್ಲೇ ಹೊಸ ಮೀಟರ್ ಸಂಪರ್ಕ ಪಡೆಯಬಹುದು.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
* ಕಟ್ಟಡದ ಅಧಿಕೃತ ಇ-ಖಾತಾ ಪ್ರತಿ (BBMP / e-Aasthi / E-Swathu Form 9/11).
* ಅನುಮೋದಿತ ಕಟ್ಟಡ ನಕ್ಷೆ (Sanctioned Plan).
* ಮಾಲೀಕರ ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ಪಾಸ್‌ಪೋರ್ಟ್ ಫೋಟೋ.
* ಸರ್ಕಾರಿ ಪರವಾನಗಿ ಪಡೆದ ಎಲೆಕ್ಟ್ರಿಕಲ್ ಕಂಟ್ರಾಕ್ಟರ್‌ನಿಂದ ವೈರಿಂಗ್ ಕಂಪ್ಲೀಷನ್ ರಿಪೋರ್ಟ್ (Wiring Completion Certificate / Form A).

---

### 💻 ಅರ್ಜಿ ಹಂತಗಳು:
1. ನಿಮ್ಮ ಎಸ್ಕಾಂ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ **'Apply for New Connection'** ಆಯ್ಕೆಮಾಡಿ.
2. ಅಗತ್ಯವಿರುವ ಲೋಡ್ (ಉದಾ: 3 kW / 5 kW ಗೃಹಬಳಕೆ) ಮತ್ತು ದಾಖಲೆಗಳನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
3. ಸೆಕ್ಯುರಿಟಿ ಠೇವಣಿ (MSD) ಮತ್ತು ಲೈನ್ ಸರ್ವಿಸ್ ಶುಲ್ಕವನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪಾವತಿಸಿ.
4. ಎಸ್ಕಾಂ ಅಧಿಕಾರಿಗಳು 7 ದಿನಗಳಲ್ಲಿ ಸ್ಥಳಕ್ಕೆ ಬಂದು ಡಿಜಿಟಲ್ ಸ್ಮಾರ್ಟ್ ಮೀಟರ್ ಅಳವಡಿಸಿ ವಿದ್ಯುತ್ ಸಂಪರ್ಕ ಕಲ್ಪಿಸುತ್ತಾರೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bescom.karnataka.gov.in",
        "keywords": "new power connection online, bescom meter application, escom new connection, ಹೊಸ ವಿದ್ಯುತ್ ಮೀಟರ್, ಬೆಸ್ಕಾಂ ಸಂಪರ್ಕ",
        "action_label": "⚡ ಎಸ್ಕಾಂ ಹೊಸ ಸಂಪರ್ಕ",
        "action_url": "https://bescom.karnataka.gov.in"
    },
    {
        "id": "faq_user_245",
        "question": "ರಿಯಲ್ ಎಸ್ಟೇಟ್ ಏಜೆಂಟ್ / ಬ್ರೋಕರ್ K-RERA ನೋಂದಾಯಿತರೇ ಎಂದು ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "verify rera registered real estate agent broker karnataka ರೇರಾ ಏಜೆಂಟ್ ಪರಿಶೀಲನೆ",
        "answer": """### 🏢 ಕೆ-ರೇರಾ ನೋಂದಾಯಿತ ಏಜೆಂಟ್ ಪರಿಶೀಲನೆ (Verify RERA Agent Online)

ರಿಯಲ್ ಎಸ್ಟೇಟ್ ವಹಿವಾಟುಗಳಲ್ಲಿ ಮೋಸ ಹೋಗುವುದನ್ನು ತಪ್ಪಿಸಲು ಫ್ಲಾಟ್ ಅಥವಾ ಸೈಟ್ ಖರೀದಿಸುವ ಮುನ್ನ ಬ್ರೋಕರ್ ಅಥವಾ ಏಜೆನ್ಸಿ RERA ಪರವಾನಗಿ ಹೊಂದಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸುವುದು ಕಡ್ಡಾಯ.

---

### 🔍 ಪರಿಶೀಲಿಸುವ ವಿಧಾನ:
1. [rera.karnataka.gov.in](https://rera.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ.
2. **'Agent Status -> Registered Agents'** ಆಯ್ಕೆಮಾಡಿ.
3. ಏಜೆಂಟ್ ಹೆಸರು ಅಥವಾ ಅವರ 12 ಅಂಕಿಗಳ **RERA Registration Number (ಉದಾ: PRM/KA/RERA/1251/...)** ನಮೂದಿಸಿ.
4. ಏಜೆಂಟ್‌ನ ಮಾನ್ಯತೆಯ ಅವಧಿ, ವಿಳಾಸ ಮತ್ತು ಅವರ ಮೇಲೆ ಯಾವುದಾದರೂ ದೂರುಗಳು ದಾಖಲಾಗಿವೆಯೇ ಎಂಬ ವಿವರಗಳು ಪರದೆಯ ಮೇಲೆ ಲಭ್ಯವಾಗುತ್ತವೆ.

⚠️ RERA ನೋಂದಣಿ ಇಲ್ಲದ ಅನಧಿಕೃತ ಏಜೆಂಟ್‌ಗಳ ಮೂಲಕ ಜಮೀನು/ಫ್ಲಾಟ್ ಖರೀದಿಸಿ ವಂಚನೆಗೊಳಗಾಗಬೇಡಿ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://rera.karnataka.gov.in",
        "keywords": "rera registered agent check, k rera broker verification, real estate agent license karnataka, ರೇರಾ ಏಜೆಂಟ್ ಪರಿಶೀಲನೆ",
        "action_label": "🏢 K-RERA ಏಜೆಂಟ್ ವಿವರ",
        "action_url": "https://rera.karnataka.gov.in"
    },
    {
        "id": "faq_user_246",
        "question": "ಬೀದಿಗಳಲ್ಲಿ ಅಡ್ಡಾದಿಡ್ಡಿ ಬಿಡುವ ದನ-ಕರುಗಳ (Stray Cattle) ನಿಯಂತ್ರಣಕ್ಕೆ BBMP ದೂರು ನೀಡುವುದು ಹೇಗೆ? ದಂಡವೆಷ್ಟು?",
        "normalized_question": "bbmp stray cattle cow complaint penalty control room bangalore ಬೀದಿ ದನಗಳ ಹಾವಳಿ ಬಿಬಿಎಂಪಿ ದೂರು",
        "answer": """### 🐄 ಬೀದಿ ದನ-ಕರುಗಳ ಹಾವಳಿ ನಿಯಂತ್ರಣ & BBMP ದೂರು ಸಹಾಯವಾಣಿ

ಬೆಂಗಳೂರು ನಗರದ ಪ್ರಮುಖ ರಸ್ತೆಗಳಲ್ಲಿ ಟ್ರಾಫಿಕ್ ಅಡೆತಡೆ ಉಂಟುಮಾಡುವ ಮತ್ತು ಸಾರ್ವಜನಿಕರಿಗೆ ಅಪಾಯ ತಂದೊಡ್ಡುವ ಬೀದಿ ದನಗಳ ವಿರುದ್ಧ ಬಿಬಿಎಂಪಿ ಕಠಿಣ ಕ್ರಮ ಕೈಗೊಳ್ಳುತ್ತದೆ.

---

### 📞 ದೂರು ನೀಡುವ ಮಾರ್ಗಗಳು:
* **BBMP 24x7 ಕಂಟ್ರೋಲ್ ರೂಂ:** **080-22660000**
* **BBMP ಸಹಾಯ ಆ್ಯಪ್:** 'Namma Bengaluru / Sahaaya 2.0' ಆ್ಯಪ್‌ನಲ್ಲಿ ಫೋಟೋ ಸಮೇತ ದೂರು ಅಪ್‌ಲೋಡ್ ಮಾಡಬಹುದು.

---

### ⚠️ ಮಾಲೀಕರಿಗೆ ವಿಧಿಸುವ ದಂಡ:
* ರಸ್ತೆಯಲ್ಲಿ ಬಿಡಲಾದ ದನಗಳನ್ನು BBMP ಪಶುಸಂಗೋಪನಾ ವಿಭಾಗವು ಜಪ್ತಿ ಮಾಡಿ ಗೋಶಾಲೆಗೆ ರವಾನಿಸುತ್ತದೆ.
* ಮೊದಲ ಬಾರಿಗೆ **₹10,000 ದಂಡ**, ಎರಡನೇ ಬಾರಿ ಪುನರಾವರ್ತನೆಯಾದರೆ **₹20,000 ದಂಡ** ವಿಧಿಸಲಾಗುತ್ತದೆ ಹಾಗೂ ಮಾಲೀಕರ ವಿರುದ್ಧ ಪೊಲೀಸ್ ಕೇಸ್ ದಾಖಲಾಗುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bbmp.gov.in",
        "keywords": "bbmp stray cattle complaint, cow nuisance bangalore penalty 10000, ಬೀದಿ ದನಗಳ ಹಾವಳಿ, ಬಿಬಿಎಂಪಿ ದೂರು",
        "action_label": "🐄 BBMP ದೂರು ಪೋರ್ಟಲ್",
        "action_url": "https://bbmp.gov.in"
    },
    {
        "id": "faq_user_247",
        "question": "ಸೊಸೈಟಿ / ಸಂಘ-ಸಂಸ್ಥೆಗಳ ನೋಂದಣಿ (Registration of Societies) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "society registration online karnataka societies registration act 1960 sahakara ಸೊಸೈಟಿ ನೋಂದಣಿ",
        "answer": """### 🏛️ ಕರ್ನಾಟಕ ಸಂಘ-ಸಂಸ್ಥೆಗಳ ನೋಂದಣಿ ಅಧಿನಿಯಮ 1960 (Society Registration)

ಅಪಾರ್ಟ್‌ಮೆಂಟ್ ನಿವಾಸಿಗಳ ಕ್ಷೇಮಾಭಿವೃದ್ಧಿ ಸಂಘ (RWA), ಕ್ರೀಡಾ ಕ್ಲಬ್, ಸಾಂಸ್ಕೃತಿಕ ಟ್ರಸ್ಟ್ ಅಥವಾ ಚಾರಿಟೇಬಲ್ ಸಂಸ್ಥೆಗಳನ್ನು ಕಾನೂನುಬದ್ಧವಾಗಿ ನೋಂದಾಯಿಸುವ ಪ್ರಕ್ರಿಯೆ.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
1. ಸಂಸ್ಥೆಯ ಉದ್ದೇಶಗಳು ಮತ್ತು ನಿಯಮಾವಳಿಗಳ ಜ್ಞಾಪನ ಪತ್ರ (Memorandum of Association & Rules/Bye-laws).
2. ಕನಿಷ್ಠ 7 ಜನ ಸಂಸ್ಥಾಪಕ ಸದಸ್ಯರ (ಕಾರ್ಯಕಾರಿ ಸಮಿತಿ) ಆಧಾರ್ ಕಾರ್ಡ್, ವಿಳಾಸ ಪುರಾವೆ ಮತ್ತು ಫೋಟೋಗಳು.
3. ಸಂಘದ ಕಚೇರಿ ವಿಳಾಸದ ಬಾಡಿಗೆ ಒಪ್ಪಂದ/ವಿದ್ಯುತ್ ಬಿಲ್ ಮತ್ತು ಮಾಲೀಕರ NOC.
4. ಸದಸ್ಯರ ಮೊದಲ ಸಭೆಯ ನಡಾವಳಿ ಪುಸ್ತಕದ ಪ್ರತಿ (Proceedings of First Meeting).

---

### 💻 ಅರ್ಜಿ ವಿಧಾನ:
* ಸಹಕಾರ ಇಲಾಖೆಯ [sahakara.kar.gov.in](https://sahakara.kar.gov.in) ಅಥವಾ ಜಿಲ್ಲಾ ಸೊಸೈಟಿಗಳ ನೋಂದಣಾಧಿಕಾರಿ (Registrar of Societies) ಕಚೇರಿಗೆ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ನೋಂದಣಿ ಪ್ರಮಾಣಪತ್ರ ಪಡೆಯಬಹುದು.""",
        "category": "LEGAL",
        "language": "kn",
        "source_url": "https://sahakara.kar.gov.in",
        "keywords": "society registration karnataka, rwa apartment association registration, sahakara societies act, ಸೊಸೈಟಿ ನೋಂದಣಿ, ಸಂಘ ಸಂಸ್ಥೆಗಳ ನೋಂದಣಿ",
        "action_label": "🏛️ ಸಹಕಾರ ಇಲಾಖೆ",
        "action_url": "https://sahakara.kar.gov.in"
    },
    {
        "id": "faq_user_248",
        "question": "ಸಹಕಾರ ಸಂಘಗಳ ವಿವಾದ ಇತ್ಯರ್ಥಕ್ಕೆ ಕಲಂ 70 (Section 70 Cooperative Dispute) ಅರ್ಜಿ ಸಲ್ಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "section 70 cooperative dispute karnataka sahakara court recovery ಕಲಂ 70 ಸಹಕಾರ ವಿವಾದ",
        "answer": """### ⚖️ ಕರ್ನಾಟಕ ಸಹಕಾರ ಸಂಘಗಳ ಕಾಯ್ದೆ — ಕಲಂ 70 (Section 70 Dispute Resolution)

ಸಹಕಾರಿ ಬ್ಯಾಂಕ್‌ಗಳು, ಹೌಸಿಂಗ್ ಸೊಸೈಟಿಗಳು (BDCC / PACS / Souharda) ಮತ್ತು ಸದಸ್ಯರ ನಡುವಿನ ಹಣಕಾಸು ವಂಚನೆ, ಸಾಲ ವಸೂಲಾತಿ, ನಿವೇಶನ ಹಂಚಿಕೆ ವಿವಾದಗಳನ್ನು ಸಿವಿಲ್ ಕೋರ್ಟ್‌ಗೆ ಹೋಗದೆ ತ್ವರಿತವಾಗಿ ಇತ್ಯರ್ಥಪಡಿಸುವ ನ್ಯಾಯಾಂಗ ಪ್ರಕ್ರಿಯೆ.

---

### 🏛️ ವಿಚಾರಣಾ ಪ್ರಾಧಿಕಾರ:
* ಸಹಕಾರ ಸಂಘಗಳ ಜಂಟಿ ನಿಬಂಧಕರು / ಉಪನಿಬಂಧಕರ (Joint Registrar of Cooperative Societies - JRCS / DRCS Court) ನ್ಯಾಯಾಲಯದಲ್ಲಿ ಕಲಂ 70 ಅಡಿಯಲ್ಲಿ ದಾವೆ ಹೂಡಬಹುದು.

---

### 🌟 ಅನುಕೂಲಗಳು:
* ಸಿವಿಲ್ ನ್ಯಾಯಾಲಯಗಳಿಗಿಂತ ಅತಿ ವೇಗವಾಗಿ ವಿಚಾರಣೆ ನಡೆದು ತೀರ್ಪು ಪ್ರಕಟವಾಗುತ್ತದೆ.
* ಹೊರಡಿಸಲಾದ ಅವಾರ್ಡ್ (Award / Decree) ಆಧಾರದ ಮೇಲೆ ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಮೂಲಕ ಭೂಕಂದಾಯ ಬಾಕಿಯಂತೆ (Land Revenue Arrears) ಆಸ್ತಿ ಜಪ್ತಿ ಮಾಡಿ ಹಣ ವಸೂಲಿ ಮಾಡಬಹುದು.""",
        "category": "LEGAL",
        "language": "kn",
        "source_url": "https://sahakara.kar.gov.in",
        "keywords": "section 70 karnataka cooperative societies act, jrcs court dispute, souharda sahakari recovery, ಕಲಂ 70 ಸಹಕಾರ ವಿವಾದ, ಜೆಆರ್‌ಸಿಎಸ್ ಕೋರ್ಟ್",
        "action_label": "⚖️ ಸಹಕಾರ ನ್ಯಾಯಾಲಯ",
        "action_url": "https://sahakara.kar.gov.in"
    },
    {
        "id": "faq_user_249",
        "question": "ಅಲ್ಪಸಂಖ್ಯಾತರ ಕಲ್ಯಾಣ ಇಲಾಖೆಯ ಶಾದಿ ಮಹಲ್ ಮತ್ತು ಸಮುದಾಯ ಭವನ ನಿರ್ಮಾಣ ಅನುದಾನ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "shaadi mahal grant minority welfare karnataka community hall shrama shakti ಶಾದಿ ಮಹಲ್ ಅನುದಾನ",
        "answer": """### 🏛️ ಅಲ್ಪಸಂಖ್ಯಾತರ ಶಾದಿ ಮಹಲ್ ಮತ್ತು ಸಮುದಾಯ ಭವನ ಅನುದಾನ ಯೋಜನೆ

ಮುಸ್ಲಿಂ, ಕ್ರಿಶ್ಚಿಯನ್, ಜೈನ, ಬೌದ್ಧ ಮತ್ತು ಸಿಖ್ ಸಮುದಾಯದ ಬಡ ಕುಟುಂಬಗಳ ಮದುವೆ ಮತ್ತು ಸಾಮಾಜಿಕ ಸಮಾರಂಭಗಳಿಗೆ ಕೈಗೆಟುಕುವ ದರದಲ್ಲಿ ಭವನ ಒದಗಿಸಲು ನೋಂದಾಯಿತ ಟ್ರಸ್ಟ್‌ಗಳು ಮತ್ತು ವಕ್ಫ್ ಸಂಸ್ಥೆಗಳಿಗೆ ಸರ್ಕಾರ ಅನುದಾನ ನೀಡುತ್ತದೆ.

---

### 💰 ಸರ್ಕಾರದ ಅನುದಾನ ಮೊತ್ತ:
* ಹೊಸ ಶಾದಿ ಮಹಲ್ / ಸಮುದಾಯ ಭವನ ನಿರ್ಮಾಣಕ್ಕೆ **₹1.00 ಕೋಟಿಯಿಂದ ₹2.00 ಕೋಟಿವರೆಗೆ** ಹಂತ-ಹಂತವಾಗಿ ಸರ್ಕಾರದ ಆರ್ಥಿಕ ನೆರವು.
* ಹಳೆಯ ಸಮುದಾಯ ಭವನಗಳ ನವೀಕರಣಕ್ಕೆ ₹25 ಲಕ್ಷದಿಂದ ₹50 ಲಕ್ಷದವರೆಗೆ ಅನುದಾನ.

---

### 📋 ಅರ್ಹತೆ:
1. ಸಂಸ್ಥೆಯು ನೋಂದಾಯಿತ ವಕ್ಫ್ ಅಥವಾ ಧಾರ್ಮಿಕ ಟ್ರಸ್ಟ್ ಆಗಿರಬೇಕು.
2. ಸಂಸ್ಥೆಯ ಹೆಸರಿನಲ್ಲಿ ಕನಿಷ್ಠ 5,000 ರಿಂದ 10,000 ಚದರಡಿ ಸ್ವಂತ ಋಣಭಾರರಹಿತ (Clear Title) ನಿವೇಶನ ಇರಬೇಕು.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [minoritywelfare.karnataka.gov.in](https://minoritywelfare.karnataka.gov.in)""",
        "category": "WELFARE",
        "language": "kn",
        "source_url": "https://minoritywelfare.karnataka.gov.in",
        "keywords": "shaadi mahal construction grant, minority welfare community hall, kmdc fund, ಶಾದಿ ಮಹಲ್ ಅನುದಾನ, ಅಲ್ಪಸಂಖ್ಯಾತರ ಕಲ್ಯಾಣ",
        "action_label": "🏛️ ಅಲ್ಪಸಂಖ್ಯಾತರ ಇಲಾಖೆ",
        "action_url": "https://minoritywelfare.karnataka.gov.in"
    },
    {
        "id": "faq_user_250",
        "question": "ಬೆಂಗಳೂರು ಒನ್ / ಕರ್ನಾಟಕ ಒನ್ ಕೇಂದ್ರಗಳಲ್ಲಿ FASTag ಮತ್ತು ನಮ್ಮ ಮೆಟ್ರೋ ಕಾರ್ಡ್ ರೀಚಾರ್ಜ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "karnataka one bangalore one fastag recharge metro card top up services ಕರ್ನಾಟಕ ಒನ್ ಫಾಸ್ಟ್ಯಾಗ್",
        "answer": """### 💳 ಕರ್ನಾಟಕ ಒನ್ / ಬೆಂಗಳೂರು ಒನ್ ಕೌಂಟರ್ ಡಿಜಿಟಲ್ ರೀಚಾರ್ಜ್ ಸೇವೆಗಳು

ಆನ್‌ಲೈನ್ ಪಾವತಿ ಮಾಡಲು ಕಷ್ಟಪಡುವ ಗ್ರಾಮೀಣ ಮತ್ತು ಹಿರಿಯ ನಾಗರಿಕರು ಹತ್ತಿರದ ಕರ್ನಾಟಕ ಒನ್ ಅಥವಾ ಬೆಂಗಳೂರು ಒನ್ ಕೌಂಟರ್‌ಗಳಲ್ಲಿ ನಗದು (Cash) ಅಥವಾ UPI ಮೂಲಕ ತಕ್ಷಣ ರೀಚಾರ್ಜ್ ಮಾಡಿಸಿಕೊಳ್ಳಬಹುದು.

---

### 🚀 ಕೌಂಟರ್‌ನಲ್ಲಿ ಲಭ್ಯವಿರುವ ಪ್ರಮುಖ ತ್ವರಿತ ಸೇವೆಗಳು:
1. **ಎಲ್ಲಾ ಬ್ಯಾಂಕ್‌ಗಳ FASTag ರೀಚಾರ್ಜ್:** ವಾಹನ ಸಂಖ್ಯೆ ಅಥವಾ ಫಾಸ್ಟ್ಯಾಗ್ ಐಡಿ ನೀಡಿ ತಕ್ಷಣ ರೀಚಾರ್ಜ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.
2. **ನಮ್ಮ ಮೆಟ್ರೋ (BMRCL) ಸ್ಮಾರ್ಟ್ ಕಾರ್ಡ್ ಟಾಪ್-ಅಪ್:** ಮೆಟ್ರೋ ಕಾರ್ಡ್ ನೀಡಿ ಕನಿಷ್ಠ ₹50 ರಿಂದ ಬ್ಯಾಲೆನ್ಸ್ ಸೇರಿಸಬಹುದು.
3. **ಸಂಚಾರ ದಂಡ (Traffic Challan) ಪಾವತಿ:** ವಾಹನ ಸಂಖ್ಯೆ ನೀಡಿ ರಿಯಾಯಿತಿ ದರದ ದಂಡ ತಕ್ಷಣ ಪಾವತಿಸಿ ರಶೀದಿ ಪಡೆಯಬಹುದು.
4. **ಯುಟಿಲಿಟಿ ಬಿಲ್‌ಗಳು:** ಬೆಸ್ಕಾಂ ವಿದ್ಯುತ್, BWSSB ನೀರು, ಗ್ಯಾಸ್ ಬಿಲ್, BSNL ಲ್ಯಾಂಡ್‌ಲೈನ್ ಬಿಲ್ ಪಾವತಿ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://karnatakaone.gov.in",
        "keywords": "karnataka one fastag recharge, bangalore one metro card topup, traffic challan payment karnataka one, ಕರ್ನಾಟಕ ಒನ್ ಸೇವೆಗಳು",
        "action_label": "💳 ಕರ್ನಾಟಕ ಒನ್ ಪೋರ್ಟಲ್",
        "action_url": "https://karnatakaone.gov.in"
    },
    {
        "id": "faq_user_251",
        "question": "ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆಯ ₹2,000 ಜಮೆಯಾಗುವಾಗ SMS ಬಾರದಿದ್ದರೆ ಮೊಬೈಲ್ ನಂಬರ್ ಅಪ್‌ಡೇಟ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "gruha lakshmi dbt sms not receiving update mobile number ration card fair price shop ಗೃಹಲಕ್ಷ್ಮಿ ಎಸ್ಎಂಎಸ್ ಮೊಬೈಲ್ ನಂಬರ್",
        "answer": """### 📱 ಗೃಹಲಕ್ಷ್ಮಿ DBT SMS ಅಲರ್ಟ್ ಮತ್ತು ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ನವೀಕರಣ

ಗೃಹಲಕ್ಷ್ಮಿ ಹಣ ಬ್ಯಾಂಕ್‌ಗೆ ಜಮೆಯಾದಾಗ ನಿಮ್ಮ ಮೊಬೈಲ್‌ಗೆ ಸರ್ಕಾರದ SMS ಬಾರದಿದ್ದರೆ ರೇಷನ್ ಕಾರ್ಡ್ ಅಥವಾ ಬ್ಯಾಂಕ್ ಖಾತೆಯಲ್ಲಿ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಅಪ್‌ಡೇಟ್ ಮಾಡಬೇಕಾಗುತ್ತದೆ.

---

### 🔧 ಸರಿಪಡಿಸುವ 2 ಹಂತಗಳು:
1. **ನ್ಯಾಯಬೆಲೆ ಅಂಗಡಿಯಲ್ಲಿ (Fair Price Shop) ರೇಷನ್ ಕಾರ್ಡ್ ಮೊಬೈಲ್ ಅಪ್‌ಡೇಟ್:**
   - ನಿಮ್ಮ ಮಾಸಿಕ ಪಡಿತರ ಪಡೆಯುವ ನ್ಯಾಯಬೆಲೆ ಅಂಗಡಿಗೆ ತೆರಳಿ ಬಯೋಮೆಟ್ರಿಕ್ ಇ-ಕೆವೈಸಿ (e-KYC) ಮಾಡುವಾಗ ನಿಮ್ಮ ಚಾಲ್ತಿಯಲ್ಲಿರುವ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ ಲಿಂಕ್ ಮಾಡಿಸಿ.
2. **ಬ್ಯಾಂಕ್ ಖಾತೆಯಲ್ಲಿ SMS ಅಲರ್ಟ್ ಸಕ್ರಿಯಗೊಳಿಸಿ:**
   - ಹಣ ಜಮೆಯಾಗುವ ಬ್ಯಾಂಕ್ ಶಾಖೆಗೆ ತೆರಳಿ 'Mobile Number Update / SMS Alert Activation' ಫಾರ್ಮ್ ನೀಡಿ.
3. ತಕ್ಷಣದ ಸ್ಥಿತಿ ತಿಳಿಯಲು **'DBT Karnataka'** ಮೊಬೈಲ್ ಆ್ಯಪ್ ಮೂಲಕ ಲೈವ್ ಆಗಿ ಜಮೆಯಾದ ವಿವರಗಳನ್ನು ಪರಿಶೀಲಿಸಬಹುದು.""",
        "category": "SCHEME",
        "language": "kn",
        "source_url": "https://sevasindhugs.karnataka.gov.in",
        "keywords": "gruha lakshmi sms not receiving, update mobile number ration card, dbt karnataka app, ಗೃಹಲಕ್ಷ್ಮಿ ಮೊಬೈಲ್ ನಂಬರ್ ಲಿಂಕ್, ಪಡಿತರ ಚೀಟಿ",
        "action_label": "📱 ಗ್ಯಾರಂಟಿ ಪೋರ್ಟಲ್",
        "action_url": "/guarantee-schemes.html"
    }
]

# =========================================================================
# 17. EXPANSION BATCH 9: VITAL CITIZEN UTILITIES & WELFARE (252 - 269)
# =========================================================================

ADDITIONAL_EXPANSION_FAQS_BATCH_9 = [
    {
        "id": "faq_user_252",
        "question": "ಬಡವರಿಗೆ ಮತ್ತು ಮಹಿಳೆಯರಿಗೆ ಉಚಿತ ಕಾನೂನು ನೆರವು ಹಾಗೂ ಉಚಿತ ವಕೀಲರ ಸೌಲಭ್ಯ (Free Legal Aid) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "free legal aid karnataka state legal services authority kslsa advocate ಉಚಿತ ಕಾನೂನು ನೆರವು ವಕೀಲರು",
        "answer": """### ⚖️ ಕರ್ನಾಟಕ ರಾಜ್ಯ ಕಾನೂನು ಸೇವೆಗಳ ಪ್ರಾಧಿಕಾರ (KSLSA — Free Legal Aid)

ನ್ಯಾಯಾಲಯದ ಶುಲ್ಕ ಮತ್ತು ಖಾಸಗಿ ವಕೀಲರ ಶುಲ್ಕ ಭರಿಸಲು ಸಾಧ್ಯವಾಗದ ಬಡವರು, ಮಹಿಳೆಯರು, ಮಕ್ಕಳು, ಪರಿಶಿಷ್ಟ ಜಾತಿ/ಪಂಗಡದವರು ಹಾಗೂ ಕಾರ್ಮಿಕರಿಗೆ ಸರ್ಕಾರವೇ ಉಚಿತ ವಕೀಲರನ್ನು ನೇಮಿಸುತ್ತದೆ.

---

### 📌 ಉಚಿತ ಕಾನೂನು ನೆರವಿಗೆ ಯಾರು ಅರ್ಹರು?:
1. ಎಲ್ಲಾ ಮಹಿಳೆಯರು ಮತ್ತು 18 ವರ್ಷದೊಳಗಿನ ಮಕ್ಕಳು (ಯಾವುದೇ ಆದಾಯ ಮಿತಿಯಿಲ್ಲ).
2. ಪರಿಶಿಷ್ಟ ಜಾತಿ (SC) ಮತ್ತು ಪರಿಶಿಷ್ಟ ಪಂಗಡದ (ST) ನಾಗರಿಕರು.
3. ವಾರ್ಷಿಕ ₹3.00 ಲಕ್ಷಕ್ಕಿಂತ ಕಡಿಮೆ ಆದಾಯ ಹೊಂದಿರುವ ಎಲ್ಲಾ ಸಾಮಾನ್ಯ/ಹಿಂದುಳಿದ ವರ್ಗಗಳ ನಾಗರಿಕರು.
4. ವಿಕಲಚೇತನರು, ಗಲಭೆ/ಅಪಘಾತ ಸಂತ್ರಸ್ತರು ಮತ್ತು ವಿಚಾರಣಾಧೀನ ಕೈದಿಗಳು.

---

### 📋 ಸೌಲಭ್ಯ ಪಡೆಯುವ ವಿಧಾನ:
* ನಿಮ್ಮ ಜಿಲ್ಲಾ ನ್ಯಾಯಾಲಯ ಅಥವಾ ತಾಲೂಕು ಕೋರ್ಟ್ ಸಂಕೀರ್ಣದಲ್ಲಿರುವ **ತಾಲೂಕು ಕಾನೂನು ಸೇವಾ ಸಮಿತಿ (TLSC / DLSA)** ಕಚೇರಿಗೆ ಭೇಟಿ ನೀಡಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.
* **ಟೋಲ್-ಫ್ರೀ ಲೀಗಲ್ ಹೆಲ್ಪ್‌ಲೈನ್: 15100** ಅಥವಾ **080-22111714** ಗೆ ಕರೆ ಮಾಡಿ ಉಚಿತ ಸಲಹೆ ಪಡೆಯಬಹುದು.
* ಪ್ರಾಧಿಕಾರವೇ ನುರಿತ ವಕೀಲರನ್ನು ನೇಮಿಸಿ, ನ್ಯಾಯಾಲಯದ ಶುಲ್ಕ, ಟೈಪಿಂಗ್ ಮತ್ತು ಸಾಕ್ಷಿದಾರರ ಖರ್ಚನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ಭರಿಸುತ್ತದೆ.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [kslsa.kar.nic.in](https://kslsa.kar.nic.in)""",
        "category": "LEGAL",
        "language": "kn",
        "source_url": "https://kslsa.kar.nic.in",
        "keywords": "free legal aid karnataka, kslsa free lawyer, 15100 legal helpline, ಉಚಿತ ಕಾನೂನು ನೆರವು, ಉಚಿತ ವಕೀಲರು, ಕೋರ್ಟ್ ನೆರವು",
        "action_label": "⚖️ KSLSA ಪೋರ್ಟಲ್",
        "action_url": "https://kslsa.kar.nic.in"
    },
    {
        "id": "faq_user_253",
        "question": "ಮಹಾತ್ಮ ಗಾಂಧಿ ಉದ್ಯೋಗ ಖಾತರಿ (MGNREGA Job Card) ಜಾಬ್ ಕಾರ್ಡ್ ಪಡೆಯುವುದು ಮತ್ತು ಕೂಲಿ ಹಣ ಚೆಕ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "mgnrega job card apply nrega wage rate dbt status karnataka ಮಹಾತ್ಮ ಗಾಂಧಿ ಉದ್ಯೋಗ ಖಾತರಿ ಜಾಬ್ ಕಾರ್ಡ್",
        "answer": """### 👷 ನರೇಗಾ ಜಾಬ್ ಕಾರ್ಡ್ (MGNREGA 100 Days Guaranteed Wage Employment)

ಗ್ರಾಮೀಣ ಭಾಗದ ಪ್ರತಿ ಕುಟುಂಬಕ್ಕೆ ವರ್ಷಕ್ಕೆ ಕನಿಷ್ಠ 100 ದಿನಗಳ ಖಾತರಿಪಡಿಸಿದ ಅಕುಶಲ ದೈಹಿಕ ಉದ್ಯೋಗ ಹಾಗೂ ನೇರ ದಿನಗೂಲಿ ಒದಗಿಸುವ ಕೇಂದ್ರ-ರಾಜ್ಯ ಸರ್ಕಾರದ ಯೋಜನೆ.

---

### 💰 ದಿನಗೂಲಿ & ಕೆಲಸದ ವಿವರ:
* **ದಿನಗೂಲಿ ದರ:** ಕರ್ನಾಟಕದಲ್ಲಿ ಪ್ರತಿ ದಿನದ ಅಕುಶಲ ಕೂಲಿ ಮೊತ್ತವು ಪರಿಷ್ಕೃತ ದರದಂತೆ ನೇರವಾಗಿ ಕಾರ್ಮಿಕರ ಆಧಾರ್ ಸೀಡೆಡ್ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ (DBT) ಜಮೆಯಾಗುತ್ತದೆ.
* **ಒಳಗೊಂಡ ಕಾಮಗಾರಿಗಳು:** ಕೃಷಿ ಹೊಂಡ ನಿರ್ಮಾಣ, ಬದು ನಿರ್ಮಾಣ, ದನದ ಕೊಟ್ಟಿಗೆ, ಮನೆ ನಿರ್ಮಾಣದ ಕೂಲಿ, ರಸ್ತೆ ಕಾಮಗಾರಿ, ಮತ್ತು ಚೆಕ್ ಡ್ಯಾಂ ನಿರ್ಮಾಣ.

---

### 📝 ಜಾಬ್ ಕಾರ್ಡ್ ಪಡೆಯುವ ವಿಧಾನ:
1. ಗ್ರಾಮ ಪಂಚಾಯಿತಿಗೆ ಭೇಟಿ ನೀಡಿ ಕುಟುಂಬದ ವಯಸ್ಕ ಸದಸ್ಯರ ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ನೀಡಿ **Form 1** ಭರ್ತಿ ಮಾಡಿ.
2. 15 ದಿನಗಳೊಳಗೆ ಉಚಿತವಾಗಿ ಫೋಟೋ ಇರುವ **MGNREGA Job Card** ನೀಡಲಾಗುತ್ತದೆ.
3. ಕೆಲಸ ಕೋರಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿದ 15 ದಿನಗಳಲ್ಲಿ ಕೆಲಸ ನೀಡದಿದ್ದರೆ ನಿರುದ್ಯೋಗ ಭತ್ಯೆ (Unemployment Allowance) ಪಡೆಯಲು ಅರ್ಹತೆ ಇರುತ್ತದೆ.

🔗 **ಆನ್‌ಲೈನ್ ಪೋರ್ಟಲ್:** [nrega.nic.in](https://nrega.nic.in)""",
        "category": "LABOUR",
        "language": "kn",
        "source_url": "https://nrega.nic.in",
        "keywords": "mgnrega job card apply, nrega daily wage rate karnataka, nrega dbt wage, ನರೇಗಾ ಜಾಬ್ ಕಾರ್ಡ್, ಉದ್ಯೋಗ ಖಾತರಿ ಕೂಲಿ",
        "action_label": "👷 ನರೇಗಾ ಪೋರ್ಟಲ್",
        "action_url": "https://nrega.nic.in"
    },
    {
        "id": "faq_user_254",
        "question": "KCET ಕೃಷಿ ಕೋಟಾ ಸೀಟುಗಳಿಗೆ 'ಕೃಷಿಕ ಪ್ರಮಾಣಪತ್ರ' (Agriculturist / Agricultural Family Certificate) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "kcet agriculture quota certificate nadakacheri rtc practical exam ಕೃಷಿಕ ಕೋಟಾ ಪ್ರಮಾಣಪತ್ರ ಕೆಸಿಇಟಿ",
        "answer": """### 🌾 ಕೆಸಿಇಟಿ ಕೃಷಿ ಕೋಟಾ (KCET Practical Agriculture Quota Certificate)

ಕರ್ನಾಟಕ ಪರೀಕ್ಷಾ ಪ್ರಾಧಿಕಾರ (KEA) ನಡೆಸುವ ಬಿ.ಎಸ್ಸಿ ಕೃಷಿ, ತೋಟಗಾರಿಕೆ, ರೇಷ್ಮೆ ಕೃಷಿ, ಅರಣ್ಯಶಾಸ್ತ್ರ ಮತ್ತು ಪಶುವೈದ್ಯಕೀಯ (BVSc) ಕೋರ್ಸ್‌ಗಳಲ್ಲಿ ರೈತರ ಮಕ್ಕಳಿಗೆ **15% ಕೃಷಿಕ ಮೀಸಲಾತಿ ಕೋಟಾ** ಲಭ್ಯವಿರುತ್ತದೆ.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
1. ಪೋಷಕರ (ತಂದೆ/ತಾಯಿ) ಹೆಸರಿನಲ್ಲಿರುವ ಚಾಲ್ತಿ ಸಾಲಿನ ಜಮೀನಿನ ಪಹಣಿ (Bhoomi RTC).
2. ಕೃಷಿ ಕೂಲಿ ಕಾರ್ಮಿಕರಾಗಿದ್ದರೆ ತಹಶೀಲ್ದಾರ್ ನೀಡಿದ ಕೃಷಿ ಕೂಲಿ ಕಾರ್ಮಿಕ ಪ್ರಮಾಣಪತ್ರ (Agricultural Labourer Certificate).
3. ಅಭ್ಯರ್ಥಿಯ ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ಶಾಲಾ ವ್ಯಾಸಂಗ ಪ್ರಮಾಣಪತ್ರ.

---

### 💻 ಅರ್ಜಿ ಸಲ್ಲಿಕೆ:
* ನಾಡಕಚೇರಿ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ [nadakacheri.karnataka.gov.in](https://nadakacheri.karnataka.gov.in) ಅಥವಾ ಗ್ರಾಮ ಒನ್‌ನಲ್ಲಿ **'Agriculturist / Agricultural Family Certificate'** ಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ RD ಸಂಖ್ಯೆ ಪಡೆಯಬೇಕು.
* ನಂತರ ಕೃಷಿ ವಿಶ್ವವಿದ್ಯಾಲಯಗಳು (UAS Bangalore, Dharwad, Raichur, Shivamogga) ನಡೆಸುವ ಕೃಷಿ ಪ್ರಾಯೋಗಿಕ ಪರೀಕ್ಷೆಗೆ (Practical Test) ಹಾಜರಾಗಬೇಕು.""",
        "category": "EDUCATION",
        "language": "kn",
        "source_url": "https://cetonline.karnataka.gov.in",
        "keywords": "kcet agriculture quota certificate, uas practical test certificate, krushika quota nadakacheri, ಕೃಷಿಕ ಕೋಟಾ ಪ್ರಮಾಣಪತ್ರ, ಕೆಸಿಇಟಿ ಕೃಷಿ ಸೀಟು",
        "action_label": "🌾 KEA ಕೃಷಿಕ ಕೋಟಾ",
        "action_url": "https://cetonline.karnataka.gov.in"
    },
    {
        "id": "faq_user_255",
        "question": "ನೈಸರ್ಗಿಕ ವಿಕೋಪ / ಮಳೆಯಿಂದ ಮನೆ ಹಾನಿಯಾದರೆ ಸರ್ಕಾರದ ಎಸ್‌ಡಿಆರ್‌ಎಫ್ (SDRF House Damage Relief) ಪರಿಹಾರ ಎಷ್ಟು ಸಿಗುತ್ತದೆ?",
        "normalized_question": "sdrf house collapse compensation natural calamity karnataka parihara ಮನೆ ಹಾನಿ ಪರಿಹಾರ ನೈಸರ್ಗಿಕ ವಿಕೋಪ",
        "answer": """### 🏠 ನೈಸರ್ಗಿಕ ವಿಕೋಪ ಮನೆ ಹಾನಿ ಪರಿಹಾರ (SDRF & NDRF Housing Assistance)

ಭಾರೀ ಮಳೆ, ಪ್ರವಾಹ, ಭೂಕುಸಿತ ಅಥವಾ ಚಂಡಮಾರುತದಿಂದ ಮನೆಗಳು ಕುಸಿದುಬಿದ್ದಾಗ ಕಂದಾಯ ಮತ್ತು ವಿಪತ್ತು ನಿರ್ವಹಣಾ ಇಲಾಖೆಯು ಪರಿಹಾರ ನೀಡುತ್ತದೆ.

---

### 💰 ಹಾನಿಯ ಶ್ರೇಣಿವಾರು ಪರಿಹಾರ ಮೊತ್ತ (SDRF Slabs):
* **ಸಂಪೂರ್ಣ ಕುಸಿದುಬಿದ್ದ / ತೀವ್ರ ಹಾನಿಗೊಳಗಾದ ಪಕ್ಕಾ-ಕಚ್ಚಾ ಮನೆಗಳು (Category-A / >75% Damage):** ಹೊಸ ಮನೆ ನಿರ್ಮಾಣಕ್ಕೆ **₹5.00 ಲಕ್ಷ**.
* **ತೀವ್ರ ಹಾನಿಗೊಳಗಾದ ಮನೆಗಳು (Category-B / 25% to 75% Damage):** ದುರಸ್ತಿಗೆ **₹3.00 ಲಕ್ಷ**.
* **ಭಾಗಶಃ ಹಾನಿಗೊಳಗಾದ ಮನೆಗಳು (Category-C / 15% to 25% Damage):** ದುರಸ್ತಿಗೆ **₹50,000**.
* ತಕ್ಷಣದ ತುರ್ತು ಬಟ್ಟೆ ಮತ್ತು ಗೃಹೋಪಯೋಗಿ ವಸ್ತುಗಳ ಖರೀದಿಗೆ ₹10,000 ತಕ್ಷಣದ ನಗದು ಪರಿಹಾರ.

---

### 📸 ಪರಿಶೀಲನೆ & ಹಣ ಜಮೆ:
ಗ್ರಾಮ ಆಡಳಿತಾಧಿಕಾರಿ (VA) ಮತ್ತು ಇಂಜಿನಿಯರ್ ಸ್ಥಳಕ್ಕೆ ಭೇಟಿ ನೀಡಿ ಜಿಪಿಎಸ್ ಫೋಟೋ ಅಪ್‌ಲೋಡ್ ಮಾಡಿದ ನಂತರ ಪರಿಹಾರ ಮೊತ್ತವು ನೇರವಾಗಿ ಸಂತ್ರಸ್ತರ ಖಾತೆಗೆ **Parihara Portal** ಮೂಲಕ DBT ಆಗುತ್ತದೆ.""",
        "category": "WELFARE",
        "language": "kn",
        "source_url": "https://parihara.karnataka.gov.in",
        "keywords": "sdrf house damage compensation karnataka, flood house collapse relief 5 lakh, parihara house damage, ಮನೆ ಕುಸಿತ ಪರಿಹಾರ, ಮಳೆ ಹಾನಿ ಪರಿಹಾರ",
        "action_label": "🏠 ಪರಿಹಾರ ಪೋರ್ಟಲ್",
        "action_url": "https://parihara.karnataka.gov.in"
    },
    {
        "id": "faq_user_256",
        "question": "ವಿಶೇಷ ಚೇತನರಿಗೆ KSRTC / NWKRTC / KKRTC ಬಸ್‌ಗಳಲ್ಲಿ 100% ಉಚಿತ ಪಾಸ್ (Free Bus Pass for PwD) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "free bus pass disabled pwd blind smart card ksrtc seva sindhu ವಿಕಲಚೇತನರ ಉಚಿತ ಬಸ್ ಪಾಸ್",
        "answer": """### ♿ ವಿಶೇಷ ಚೇತನರಿಗೆ ಸಾರಿಗೆ ನಿಗಮಗಳ ಸಂಪೂರ್ಣ ಉಚಿತ ಬಸ್ ಪಾಸ್

ಕರ್ನಾಟಕದ ನಾಲ್ಕೂ ಸಾರಿಗೆ ನಿಗಮಗಳ (KSRTC, BMTC, NWKRTC, KKRTC) ನಗರ ಮತ್ತು ಗ್ರಾಮಾಂತರ ಬಸ್‌ಗಳಲ್ಲಿ 40% ಕ್ಕಿಂತ ಹೆಚ್ಚು ಅಂಗವಿಕಲತೆ ಹೊಂದಿರುವ ವಿಶೇಷ ಚೇತನರಿಗೆ ಉಚಿತ ಬಸ್ ಪಾಸ್ ಒದಗಿಸಲಾಗುತ್ತದೆ.

---

### 📌 ಅರ್ಹತೆ & ರಿಯಾಯಿತಿ:
* **ಅರ್ಹತೆ:** 40% ಅಥವಾ ಅದಕ್ಕಿಂತ ಹೆಚ್ಚಿನ ಅಂಗವಿಕಲತೆ (ದೃಷ್ಟಿದೋಷ, ಚಲನವಲನ ದೋಷ, ಬುದ್ಧಿಮಾಂದ್ಯತೆ, ಶ್ರವಣದೋಷ).
* **ಸಹಾಯಕರ ಉಚಿತ ಪ್ರಯಾಣ (Escort Pass):** 100% ಅಂಧತ್ವ ಅಥವಾ ತೀವ್ರ ಮಾನಸಿಕ ಅಸ್ವಸ್ಥತೆ ಹೊಂದಿರುವವರ ಜೊತೆ ಒಬ್ಬ ಸಹಾಯಕರಿಗೆ (Escort) ಸಹ ಉಚಿತ ಪ್ರಯಾಣದ ಅವಕಾಶವಿರುತ್ತದೆ.

---

### 📋 ಅರ್ಜಿ ವಿಧಾನ:
1. [sevasindhu.karnataka.gov.in](https://sevasindhu.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ **'Differently Abled Bus Pass'** ಆಯ್ಕೆಮಾಡಿ.
2. ನಿಮ್ಮ **UDID ಕಾರ್ಡ್ ಸಂಖ್ಯೆ**, ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ಇತ್ತೀಚಿನ ಪಾಸ್‌ಪೋರ್ಟ್ ಫೋಟೋ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
3. ಅನುಮೋದನೆಯಾದ ನಂತರ ಹತ್ತಿರದ KSRTC / BMTC ಪಾಸಿಂಗ್ ಕೌಂಟರ್‌ನಲ್ಲಿ ಸ್ಮಾರ್ಟ್ ಕಾರ್ಡ್ ಪಡೆದುಕೊಳ್ಳಿ.""",
        "category": "TRANSIT",
        "language": "kn",
        "source_url": "https://sevasindhu.karnataka.gov.in",
        "keywords": "free bus pass disabled pwd, ksrtc blind concession pass, udid card bus pass, ವಿಕಲಚೇತನರ ಉಚಿತ ಬಸ್ ಪಾಸ್, ಸೇವಾ ಸಿಂಧು",
        "action_label": "♿ ಬಸ್ ಪಾಸ್ ಅರ್ಜಿ",
        "action_url": "https://sevasindhu.karnataka.gov.in"
    },
    {
        "id": "faq_user_257",
        "question": "ಗೃಹ ಆರೋಗ್ಯ ಯೋಜನೆ (Gruha Arogya Scheme) ಅಡಿಯಲ್ಲಿ ಮನೆ ಬಾಗಿಲಿಗೆ ಉಚಿತ ಆರೋಗ್ಯ ತಪಾಸಣೆ ಸೌಲಭ್ಯವೇನು?",
        "normalized_question": "gruha arogya scheme karnataka free doorstep health checkup bp sugar cancer ಗೃಹ ಆರೋಗ್ಯ ಯೋಜನೆ",
        "answer": """### 🩺 ಗೃಹ ಆರೋಗ್ಯ ಯೋಜನೆ — ಮನೆ ಬಾಗಿಲಿಗೇ ಉಚಿತ ಆರೋಗ್ಯ ತಪಾಸಣೆ

ಕರ್ನಾಟಕ ಆರೋಗ್ಯ ಇಲಾಖೆಯು 30 ವರ್ಷ ಮೇಲ್ಪಟ್ಟ ಎಲ್ಲಾ ನಾಗರಿಕರಲ್ಲಿ ಸಾಂಕ್ರಾಮಿಕವಲ್ಲದ ರೋಗಗಳನ್ನು (NCD) ಮೊದಲೇ ಪತ್ತೆಹಚ್ಚಿ ಉಚಿತ ಚಿಕಿತ್ಸೆ ನೀಡಲು ಮನೆ ಮನೆಗೆ ಭೇಟಿ ನೀಡುವ ಯೋಜನೆ.

---

### 🧪 ಮನೆ ಬಾಗಿಲಿಗೆ ಲಭ್ಯವಿರುವ ಉಚಿತ ತಪಾಸಣೆಗಳು:
1. **ರಕ್ತದೊತ್ತಡ (High Blood Pressure / BP) ಪರೀಕ್ಷೆ.**
2. **ಮಧುಮೇಹ (Diabetes / Sugar) ರಕ್ತ ಪರೀಕ್ಷೆ.**
3. **ಬಾಯಿ, ಸ್ತನ ಹಾಗೂ ಗರ್ಭಕೋಶದ ಕ್ಯಾನ್ಸರ್ (Cancer Screening) ಆರಂಭಿಕ ತಪಾಸಣೆ.**
4. **ಮಾನಸಿಕ ಆರೋಗ್ಯ ಮತ್ತು ಕಣ್ಣಿನ ತಪಾಸಣೆ.**

---

### 💊 ಉಚಿತ ಔಷಧಿ ವಿತರಣೆ:
ಬಿಪಿ ಅಥವಾ ಶುಗರ್ ಇರುವುದು ದೃಢಪಟ್ಟ ರೋಗಿಗಳಿಗೆ ಪ್ರಾಥಮಿಕ ಆರೋಗ್ಯ ಕೇಂದ್ರಗಳ (PHC) ಮೂಲಕ ಪ್ರತಿ ತಿಂಗಳು ಬೇಕಾಗುವ ಔಷಧಿಗಳನ್ನು ಆಶಾ ಕಾರ್ಯಕರ್ತೆಯರೇ ನೇರವಾಗಿ ಮನೆ ಬಾಗಿಲಿಗೆ ತಲುಪಿಸುತ್ತಾರೆ.""",
        "category": "HEALTH",
        "language": "kn",
        "source_url": "https://arogya.karnataka.gov.in",
        "keywords": "gruha arogya karnataka, doorstep bp sugar checkup, free cancer screening asha, ಗೃಹ ಆರೋಗ್ಯ ಯೋಜನೆ, ಮನೆ ಆರೋಗ್ಯ ತಪಾಸಣೆ",
        "action_label": "🩺 ಆರೋಗ್ಯ ಇಲಾಖೆ",
        "action_url": "https://arogya.karnataka.gov.in"
    },
    {
        "id": "faq_user_258",
        "question": "ಸೌರ ವಾಟರ್ ಹೀಟರ್ (Solar Water Heater) ಅಳವಡಿಸಿದರೆ ಬೆಸ್ಕಾಂ ವಿದ್ಯುತ್ ಬಿಲ್‌ನಲ್ಲಿ ಮಾಸಿಕ ರಿಯಾಯಿತಿ (Rebate) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "bescom solar water heater monthly bill rebate subsidy application ಬೆಸ್ಕಾಂ ಸೋಲಾರ್ ವಾಟರ್ ಹೀಟರ್ ರಿಯಾಯಿತಿ",
        "answer": """### ☀️ ಬೆಸ್ಕಾಂ ಸೋಲಾರ್ ವಾಟರ್ ಹೀಟರ್ ಮಾಸಿಕ ಬಿಲ್ ರಿಯಾಯಿತಿ (Solar Rebate)

ಮನೆಯ ಛಾವಣಿಯ ಮೇಲೆ ಸೋಲಾರ್ ವಾಟರ್ ಹೀಟರ್ ಅಳವಡಿಸಿಕೊಂಡಿರುವ ಗೃಹಬಳಕೆಯ ವಿದ್ಯುತ್ ಗ್ರಾಹಕರಿಗೆ ಮಾಸಿಕ ವಿದ್ಯುತ್ ಬಿಲ್‌ನಲ್ಲಿ ಶಾಶ್ವತ ರಿಯಾಯಿತಿ ನೀಡಲಾಗುತ್ತದೆ.

---

### 💰 ರಿಯಾಯಿತಿ ಮೊತ್ತ:
* ಪ್ರತಿ ತಿಂಗಳ ವಿದ್ಯುತ್ ಬಿಲ್‌ನಲ್ಲಿ **ಪ್ರತಿ ಯೂನಿಟ್‌ಗೆ 50 ಪೈಸೆ ರಿಯಾಯಿತಿ (ಗರಿಷ್ಠ ₹50 / ತಿಂಗಳಿಗೆ)** ಕಡಿತವಾಗುತ್ತದೆ.

---

### 📋 ರಿಯಾಯಿತಿ ಪಡೆಯುವ ವಿಧಾನ:
1. ಸೋಲಾರ್ ವಾಟರ್ ಹೀಟರ್ ಅಳವಡಿಸಿದ ಜಾಗದ ಫೋಟೋ, ಖರೀದಿ ಬಿಲ್ (Invoice) ಮತ್ತು ನಿಮ್ಮ ಇತ್ತೀಚಿನ ವಿದ್ಯುತ್ ಬಿಲ್ ಪ್ರತಿ ಲಗತ್ತಿಸಿ.
2. [bescom.karnataka.gov.in](https://bescom.karnataka.gov.in) ನಲ್ಲಿ ಅಥವಾ ನಿಮ್ಮ ಸ್ಥಳೀಯ ಎಸ್ಕಾಂ ಸೆಕ್ಷನ್ ಆಫೀಸರ್‌ಗೆ (AE) **'Solar Water Heater Rebate Application'** ಸಲ್ಲಿಸಿ.
3. ಎಸ್ಕಾಂ ಸಿಬ್ಬಂದಿ ಭೌತಿಕ ಪರಿಶೀಲನೆ ನಡೆಸಿದ ನಂತರ ಮುಂದಿನ ತಿಂಗಳಿನಿಂದ ವಿದ್ಯುತ್ ಬಿಲ್‌ನಲ್ಲಿ ಸ್ವಯಂಚಾಲಿತವಾಗಿ 'Solar Rebate' ಕಡಿತವಾಗುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bescom.karnataka.gov.in",
        "keywords": "solar water heater rebate bescom, electricity bill solar discount, ಸೋಲಾರ್ ವಾಟರ್ ಹೀಟರ್ ರಿಯಾಯಿತಿ, ಬೆಸ್ಕಾಂ ಬಿಲ್",
        "action_label": "☀️ ಬೆಸ್ಕಾಂ ಸೋಲಾರ್ ರಿಯಾಯಿತಿ",
        "action_url": "https://bescom.karnataka.gov.in"
    },
    {
        "id": "faq_user_259",
        "question": "ಬೆಂಗಳೂರು ನೀರಿನ ಮೀಟರ್ ಕೆಟ್ಟುಹೋದರೆ ಅಥವಾ ತಪ್ಪು ಬಿಲ್ ಬಂದರೆ BWSSB ಗೆ ದೂರು ನೀಡುವುದು ಹೇಗೆ?",
        "normalized_question": "bwssb faulty water meter complaint meter testing excess water bill bangalore ಜಲಮಂಡಳಿ ಮೀಟರ್ ದೂರು",
        "answer": """### 🚰 BWSSB ದೋಷಪೂರಿತ ವಾಟರ್ ಮೀಟರ್ ಪರೀಕ್ಷೆ & ಬಿಲ್ ತಿದ್ದುಪಡಿ

ನಿಮ್ಮ ನೀರಿನ ಮೀಟರ್ ಅತಿಯಾದ ವೇಗದಲ್ಲಿ ಓಡುತ್ತಿದ್ದರೆ, ಕೆಟ್ಟುಹೋಗಿದ್ದರೆ ಅಥವಾ ಅತಿಯಾದ ಬಿಲ್ ಬಂದಿದ್ದರೆ ಜಲ ಮಂಡಳಿಯಿಂದ ಅಧಿಕೃತ ಲ್ಯಾಬ್ ಪರೀಕ್ಷೆ ಮಾಡಿಸಬಹುದು.

---

### 🛠️ ದೂರು ದಾಖಲಿಸುವ ಹಂತಗಳು:
1. **BWSSB 24x7 ಕಾಲ್ ಸೆಂಟರ್:** **1916** ಸಂಖ್ಯೆಗೆ ಕರೆ ಮಾಡಿ ನಿಮ್ಮ 8 ಅಂಕಿಗಳ Consumer Water ID ನೀಡಿ ದೂರು ದಾಖಲಿಸಿ.
2. **ಮೀಟರ್ ಟೆಸ್ಟಿಂಗ್ ಶುಲ್ಕ:** ನಿಗದಿತ ಮೀಟರ್ ಪರೀಕ್ಷಾ ಶುಲ್ಕವನ್ನು ಪಾವತಿಸಿದರೆ BWSSB ಇಂಜಿನಿಯರ್ ಬಂದು ಮೀಟರ್ ಬಿಚ್ಚಿ ಜಲ ಮಂಡಳಿಯ ಮೀಟರ್ ಟೆಸ್ಟಿಂಗ್ ಲ್ಯಾಬ್‌ಗೆ ಕಳುಹಿಸುತ್ತಾರೆ.
3. ಮೀಟರ್‌ನಲ್ಲಿ ದೋಷವಿರುವುದು ದೃಢಪಟ್ಟರೆ, ಹಿಂದಿನ 3 ತಿಂಗಳ ಸರಾಸರಿ ಬಳಕೆಯ ಆಧಾರದ ಮೇಲೆ ಹೆಚ್ಚುವರಿ ಬಿಲ್ ಮೊತ್ತವನ್ನು ಮುಂದಿನ ಬಿಲ್‌ನಲ್ಲಿ ಹೊಂದಾಣಿಕೆ (Adjustment) ಮಾಡಲಾಗುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bwssb.karnataka.gov.in",
        "keywords": "bwssb faulty meter testing, excess water bill complaint 1916, bwssb meter replacement, ಜಲಮಂಡಳಿ ಮೀಟರ್ ದೂರು, ನೀರಿನ ಬಿಲ್",
        "action_label": "🚰 BWSSB ದೂರು ಪೋರ್ಟಲ್",
        "action_url": "https://bwssb.karnataka.gov.in"
    },
    {
        "id": "faq_user_260",
        "question": "ಬೆಂಗಳೂರಿನಲ್ಲಿ ಹಸಿ ಕಸ ಮತ್ತು ಒಣ ಕಸ ವಿಂಗಡಣೆ (Waste Segregation Rules) ನಿಯಮಗಳೇನು? ಉಲ್ಲಂಘಿಸಿದರೆ ದಂಡವೆಷ್ಟು?",
        "normalized_question": "bbmp solid waste management segregation rules wet dry waste penalty bangalore ಹಸಿ ಕಸ ಒಣ ಕಸ ವಿಂಗಡಣೆ ಬಿಬಿಎಂಪಿ",
        "answer": """### 🗑️ BBMP ಕಸ ವಿಂಗಡಣೆ ನಿಯಮಗಳು (Solid Waste Management & Segregation at Source)

ಬೆಂಗಳೂರು ಮಹಾನಗರದಲ್ಲಿ ಕಸವನ್ನು ಮೂಲದಲ್ಲೇ 3 ಭಾಗಗಳಾಗಿ ವಿಂಗಡಿಸಿ ನೀಡುವುದು ಪ್ರತಿಯೊಬ್ಬ ನಾಗರಿಕ ಮತ್ತು ಅಪಾರ್ಟ್‌ಮೆಂಟ್‌ಗೆ ಕಾನೂನುಬದ್ಧವಾಗಿ ಕಡ್ಡಾಯ.

---

### 🟢 3 ವಿಧದ ಕಸ ವಿಂಗಡಣೆ ವಿಧಾನ:
1. **ಹಸಿ ಕಸ (Wet Waste - ಹಸಿರು ಡಸ್ಟ್‌ಬಿನ್):** ಹಣ್ಣು-ತರಕಾರಿ ಸಿಪ್ಪೆ, ಅಡುಗೆ ಉಳಿಕೆ ಆಹಾರ, ತರಕಾರಿ ತ್ಯಾಜ್ಯ, ಹೂವು, ಎಲೆ (ಪ್ರತಿದಿನ ಆಟೋ ಟಿಪ್ಪರ್‌ಗೆ ನೀಡಬೇಕು).
2. **ಒಣ ಕಸ (Dry Waste - ನೀಲಿ ಡಸ್ಟ್‌ಬಿನ್):** ಪ್ಲಾಸ್ಟಿಕ್ ಕವರ್, ಪೇಪರ್, ರಟ್ಟಿನ ಬಾಕ್ಸ್, ಗಾಜಿನ ಬಾಟಲಿ, ಹಾಲಿನ ಪ್ಯಾಕೆಟ್ (ವಾರಕ್ಕೆ 2 ದಿನ ಸಂಗ್ರಹ).
3. **ಸ್ಯಾನಿಟರಿ ತ್ಯಾಜ್ಯ (Sanitary / Hazardous Waste):** ನ್ಯಾಪ್ಕಿನ್, ಡೈಪರ್, ಬ್ಯಾಂಡೇಜ್, ಸಿರಿಂಜ್ (ಪೇಪರ್‌ನಲ್ಲಿ ಪ್ರತ್ಯೇಕವಾಗಿ ಕಟ್ಟಿ ಕೆಂಪು ಗುರುತು ಹಾಕಿ ನೀಡಬೇಕು).

---

### ⚠️ ಕಸ ಮಿಶ್ರಣ ಮಾಡಿದರೆ ವಿಧಿಸುವ ದಂಡ:
* ಮೊದಲ ಬಾರಿಗೆ ಕಸ ವಿಂಗಡಿಸದೆ ನೀಡಿದರೆ **₹500 ದಂಡ**, ಎರಡನೇ ಬಾರಿ ಪುನರಾವರ್ತನೆಯಾದರೆ **₹1,000 ದಂಡ**.
* ರಾಜಕಾಲುವೆ ಅಥವಾ ರಸ್ತೆ ಬದಿಯಲ್ಲಿ ಕಸ ಎಸೆದರೆ (Littering) **₹1,000 ದಿಂದ ₹5,000 ವರೆಗೆ ದಂಡ** ವಿಧಿಸಲಾಗುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bbmp.gov.in",
        "keywords": "bbmp waste segregation rules, wet dry sanitary waste penalty, solid waste management bangalore, ಕಸ ವಿಂಗಡಣೆ ಬಿಬಿಎಂಪಿ, ಒಣ ಕಸ ಹಸಿ ಕಸ",
        "action_label": "🗑️ BBMP ಘನತ್ಯಾಜ್ಯ ನಿರ್ವಹಣೆ",
        "action_url": "https://bbmp.gov.in"
    },
    {
        "id": "faq_user_261",
        "question": "ಆಯುಷ್ ಆರೋಗ್ಯ ಮಂದಿರಗಳಲ್ಲಿ (AYUSH Hospitals) ಉಚಿತ ಪಂಚಕರ್ಮ ಮತ್ತು ಆಯುರ್ವೇದ ಚಿಕಿತ್ಸೆ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "ayush arogya mandir karnataka free ayurveda panchakarma treatment yoga ಆಯುಷ್ ಆಸ್ಪತ್ರೆ ಉಚಿತ ಪಂಚಕರ್ಮ",
        "answer": """### 🌿 ಆಯುಷ್ ಆರೋಗ್ಯ ಮಂದಿರ (AYUSH — ಆಯುರ್ವೇದ, ಯೋಗ, ಯುನಾನಿ, ಸಿದ್ಧ, ಹೋಮಿಯೋಪತಿ)

ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಆಯುಷ್ ಇಲಾಖೆಯು ಎಲ್ಲಾ ಜಿಲ್ಲಾ ಆಯುರ್ವೇದ ಆಸ್ಪತ್ರೆಗಳು ಹಾಗೂ ಆಯುಷ್ ಆರೋಗ್ಯ ಮಂದಿರಗಳ ಮೂಲಕ ಪ್ರಾಕೃತಿಕ ಮತ್ತು ಸಾಂಪ್ರದಾಯಿಕ ಚಿಕಿತ್ಸೆಗಳನ್ನು ಉಚಿತವಾಗಿ ನೀಡುತ್ತದೆ.

---

### 🌟 ಉಚಿತವಾಗಿ ಲಭ್ಯವಿರುವ ಪ್ರಮುಖ ಚಿಕಿತ್ಸೆಗಳು:
* **ಪಂಚಕರ್ಮ ಚಿಕಿತ್ಸೆಗಳು (Panchakarma):** ವಾತ, ಕೀಲುನೋವು (Arthritis), ಬೆನ್ನುನೋವು, ಪಾರ್ಶ್ವವಾಯು (Paralysis), ಸಿಯಾಟಿಕಾ ಮತ್ತು ಚರ್ಮರೋಗಗಳಿಗೆ ತಜ್ಞ ವೈದ್ಯರ ಉಸ್ತುವಾರಿಯಲ್ಲಿ ಪೂರ್ಣ ಉಚಿತ ತೈಲ ಮರ್ದನ, ಸ್ವೇದನ ಮತ್ತು ಬಸ್ತಿ ಚಿಕಿತ್ಸೆ.
* **ದಿನನಿತ್ಯದ ಯೋಗ ಮತ್ತು ಧ್ಯಾನ ತರಬೇತಿ.**
* **ಉಚಿತ ಆಯುರ್ವೇದ ಮತ್ತು ಹೋಮಿಯೋಪತಿ ಕಷಾಯ, ಮಾತ್ರೆ ಮತ್ತು ಎಣ್ಣೆಗಳ ವಿತರಣೆ.**

📝 ದಾಖಲಾಗಲು ನಿಮ್ಮ ಆಧಾರ್ ಕಾರ್ಡ್‌ನೊಂದಿಗೆ ಸಮೀಪದ ಸರ್ಕಾರಿ ಆಯುರ್ವೇದ ಆಸ್ಪತ್ರೆಗೆ ಭೇಟಿ ನೀಡಿ ಒಪಿಡಿ (OPD) ನೋಂದಣಿ ಮಾಡಿಕೊಳ್ಳಿ.""",
        "category": "HEALTH",
        "language": "kn",
        "source_url": "https://ayush.karnataka.gov.in",
        "keywords": "ayush karnataka, free ayurveda panchakarma hospital, homeopathy government hospital, ಆಯುಷ್ ಆಸ್ಪತ್ರೆ, ಉಚಿತ ಪಂಚಕರ್ಮ",
        "action_label": "🌿 ಆಯುಷ್ ಇಲಾಖೆ",
        "action_url": "https://ayush.karnataka.gov.in"
    },
    {
        "id": "faq_user_262",
        "question": "ವಾಣಿಜ್ಯ ಮತ್ತು ಹೆವಿ ವಾಹನಗಳ ಚಾಲನೆಗೆ ಬ್ಯಾಡ್ಜ್ / ಟ್ರಾನ್ಸ್‌ಪೋರ್ಟ್ ಎಂಡಾರ್ಸ್‌ಮೆಂಟ್ (Transport Vehicle Endorsement) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "commercial transport vehicle endorsement badge driving license parivahan karnataka ಕಮರ್ಷಿಯಲ್ ವಾಹನ ಬ್ಯಾಡ್ಜ್ ಡಿಎಲ್",
        "answer": """### 🚛 ವಾಣಿಜ್ಯ ಮತ್ತು ಸಾರಿಗೆ ವಾಹನ ಚಾಲನಾ ಅನುಮೋದನೆ (Transport DL Endorsement)

ಆಟೋ, ಟ್ಯಾಕ್ಸಿ, ಮ್ಯಾಕ್ಸಿ ಕ್ಯಾಬ್, ಬಸ್, ಲಾರಿ ಮತ್ತು ಅಪಾಯಕಾರಿ ಸರಕು ವಾಹನಗಳನ್ನು (Hazardous Goods Carrier) ವಾಣಿಜ್ಯ ಉದ್ದೇಶಕ್ಕೆ ಓಡಿಸಲು ಲೈಸೆನ್ಸ್‌ನಲ್ಲಿ Transport Endorsement ಪಡೆಯಬೇಕು.

---

### 📋 ಅಗತ್ಯ ಅರ್ಹತೆಗಳು:
* ಕನಿಷ್ಠ 1 ವರ್ಷ ಲಘು ಮೋಟಾರು ವಾಹನ (LMV Non-Transport) ಚಾಲನಾ ಪರವಾನಗಿ ಹೊಂದಿರಬೇಕು.
* ಅರ್ಜಿದಾರರ ಕನಿಷ್ಠ ವಯಸ್ಸು 20 ವರ್ಷ ತುಂಬಿರಬೇಕು.
* ಸರ್ಕಾರಿ ಮಾನ್ಯತೆ ಪಡೆದ ಹೆವಿ ಡ್ರೈವಿಂಗ್ ಸ್ಕೂಲ್‌ನಿಂದ (HMV Driving Institute) ತರಬೇತಿ ಪ್ರಮಾಣಪತ್ರ (Form 5).
* ನೋಂದಾಯಿತ ಎಂಬಿಬಿಎಸ್ ವೈದ್ಯರಿಂದ ಮೆಡಿಕಲ್ ಸರ್ಟಿಫಿಕೇಟ್ (Form 1A).

---

### 💻 ಅರ್ಜಿ ವಿಧಾನ:
* [parivahan.gov.in](https://parivahan.gov.in) ನಲ್ಲಿ **'Apply for Endorsement to DL'** ಆಯ್ಕೆಮಾಡಿ ಸಂಬಂಧಪಟ್ಟ ಆರ್‌ಟಿಒ ಕಚೇರಿಯಲ್ಲಿ ಡ್ರೈವಿಂಗ್ ಟೆಸ್ಟ್ ಪೂರ್ಣಗೊಳಿಸಬೇಕು.""",
        "category": "TRANSPORT",
        "language": "kn",
        "source_url": "https://parivahan.gov.in",
        "keywords": "transport dl endorsement, commercial vehicle badge karnataka, hmv driving license slot, ಕಮರ್ಷಿಯಲ್ ಲೈಸೆನ್ಸ್, ಹೆವಿ ವಾಹನ ಬ್ಯಾಡ್ಜ್",
        "action_label": "🚛 ಪರಿವಾಹನ್ ಎಂಡಾರ್ಸ್‌ಮೆಂಟ್",
        "action_url": "https://parivahan.gov.in"
    },
    {
        "id": "faq_user_263",
        "question": "KIADB ಅಥವಾ NHAI ರಸ್ತೆ ವಿಸ್ತರಣೆಗೆ ಜಮೀನು ಸ್ವಾಧೀನವಾದಾಗ ನ್ಯಾಯಯುತ ಪರಿಹಾರ (Land Acquisition Compensation) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "kiadb nhai land acquisition compensation 4 times market value award karnataka ಭೂಸ್ವಾಧೀನ ಪರಿಹಾರ ಕಾಯ್ದೆ",
        "answer": """### 🛣️ ಭೂಸ್ವಾಧೀನ, ಪುನರ್ವಸತಿ ಮತ್ತು ಮರುವ್ಯವಸ್ಥೆಯಲ್ಲಿ ನ್ಯಾಯಯುತ ಪರಿಹಾರ ಹಕ್ಕು ಕಾಯ್ದೆ 2013

ರಾಷ್ಟ್ರೀಯ ಹೆದ್ದಾರಿ (NHAI), ರೈಲ್ವೆ, ಕೈಗಾರಿಕಾ ಪ್ರದೇಶ (KIADB) ಅಥವಾ ನೀರಾವರಿ ಯೋಜನೆಗಳಿಗಾಗಿ ಖಾಸಗಿ ಕೃಷಿ ಜಮೀನು ಸ್ವಾಧೀನಪಡಿಸಿಕೊಂಡಾಗ ಸರ್ಕಾರ ಭಾರಿ ಪರಿಹಾರ ನೀಡುತ್ತದೆ.

---

### 💰 ಕಾಯ್ದೆಯನ್ವಯ ಸಿಗುವ ಕಡ್ಡಾಯ ಪರಿಹಾರ ಮೊತ್ತ:
* **ಗ್ರಾಮೀಣ ಕೃಷಿ ಜಮೀನಿಗೆ:** ಮಾರುಕಟ್ಟೆ ಮೌಲ್ಯದ (Guidance Value / Market Value) **ಕನಿಷ್ಠ 2 ರಿಂದ 4 ಪಟ್ಟು ಪರಿಹಾರ**.
* **ನಗರ ಪ್ರದೇಶದ ಜಮೀನಿಗೆ:** ಮಾರುಕಟ್ಟೆ ಮೌಲ್ಯದ **2 ಪಟ್ಟು ಪರಿಹಾರ**.
* **ಸಾಲಿಟಿಯಂ (Solatium - 100% ಬೋನಸ್):** ಮೂಲ ಪರಿಹಾರ ಮೊತ್ತಕ್ಕೆ ಸಮನಾದ ಹೆಚ್ಚುವರಿ 100% ಸಾಲಿಟಿಯಂ ಬೋನಸ್.
* ಜಮೀನಿನಲ್ಲಿದ್ದ ಮರಗಳು, ಕೊಳವೆಬಾವಿ, ಪಂಪ್‌ಹೌಸ್, ಮನೆ ಮತ್ತು ಬೆಳೆಗಳಿಗೆ ತೋಟಗಾರಿಕೆ/ಲೋಕೋಪಯೋಗಿ ಇಲಾಖೆಯಿಂದ ಪ್ರತ್ಯೇಕ ಮೌಲ್ಯಮಾಪನ ಪರಿಹಾರ.

---

### ⚖️ ಪರಿಹಾರ ಪಡೆಯಲು ಅಥವಾ ಹೆಚ್ಚಳ ಕೋರಲು:
ವಿಶೇಷ ಭೂಸ್ವಾಧೀನಾಧಿಕಾರಿಗಳ (SLAO) ಮುಂದೆ ಮೂಲ ಪಹಣಿ, ಕ್ರಯಪತ್ರ ಮತ್ತು ಬ್ಯಾಂಕ್ ವಿವರ ಸಲ್ಲಿಸಿ ಅವಾರ್ಡ್ ಮೊತ್ತ ಪಡೆಯಬಹುದು. ಪರಿಹಾರ ಕಡಿಮೆ ಎನಿಸಿದರೆ **ಭೂಸ್ವಾಧೀನ ನ್ಯಾಯಮಂಡಳಿಗೆ (Land Acquisition Tribunal / Civil Court)** ಹೆಚ್ಚಳ ಕೋರಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://kiadb.karnataka.gov.in",
        "keywords": "kiadb land acquisition compensation, nhai road widening compensation 4 times, land acquisition tribunal, ಭೂಸ್ವಾಧೀನ ಪರಿಹಾರ, ಕೆಐಎಡಿಬಿ ಪರಿಹಾರ",
        "action_label": "🛣️ KIADB ಭೂಸ್ವಾಧೀನ",
        "action_url": "https://kiadb.karnataka.gov.in"
    },
    {
        "id": "faq_user_264",
        "question": "ವ್ಯಾಪಾರ ಮುಚ್ಚಿದಾಗ ಅಥವಾ ವಹಿವಾಟು ಇಲ್ಲದಾಗ ಜಿಎಸ್‌ಟಿ ನೋಂದಣಿ ರದ್ದು (GST Surrender / Cancellation) ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "gst cancellation surrender online application reg 16 small business commercial tax ಜಿಎಸ್‌ಟಿ ರದ್ದು ಆನ್‌ಲೈನ್",
        "answer": """### 🧾 ಜಿಎಸ್‌ಟಿ ನೋಂದಣಿ ರದ್ದತಿ ಪ್ರಕ್ರಿಯೆ (GST Surrender / Cancellation — Form REG-16)

ಅಂಗಡಿ/ಉದ್ಯಮ ಮುಚ್ಚಿದಾಗ, ಮಾಲೀಕರು ಮೃತಪಟ್ಟಾಗ ಅಥವಾ ವಾರ್ಷಿಕ ವಹಿವಾಟು ಮಿತಿಗಿಂತ ಕಡಿಮೆಯಿದ್ದಾಗ ಪ್ರತಿ ತಿಂಗಳು ಶೂನ್ಯ ರಿಟರ್ನ್ಸ್ (Nil Return) ಹಾಕುವ ತಲೆನೋವು ತಪ್ಪಿಸಲು ಜಿಎಸ್‌ಟಿ ರದ್ದು ಮಾಡಿಕೊಳ್ಳಬೇಕು.

---

### 💻 ಆನ್‌ಲೈನ್ ರದ್ದತಿ ಹಂತಗಳು:
1. [gst.gov.in](https://www.gst.gov.in) ಪೋರ್ಟಲ್‌ಗೆ ಲಾಗಿನ್ ಆಗಿ.
2. **'Services -> Registration -> Application for Cancellation of Registration (REG-16)'** ಆಯ್ಕೆಮಾಡಿ.
3. ರದ್ದತಿಗೆ ಕಾರಣ (Discontinuation of business / Closure of firm) ಮತ್ತು ದಿನಾಂಕ ನಮೂದಿಸಿ.
4. ಕ್ಲೋಸಿಂಗ್ ಸ್ಟಾಕ್ ಮತ್ತು ಇನ್‌ಪುಟ್ ಟ್ಯಾಕ್ಸ್ ಕ್ರೆಡಿಟ್ (ITC) ರಿವರ್ಸಲ್ ಬಾಕಿ ಇದ್ದರೆ ಲೆಕ್ಕ ತೋರಿಸಿ.
5. ಡಿಜಿಟಲ್ ಸಿಗ್ನೇಚರ್ (DSC) ಅಥವಾ ಆಧಾರ್ OTP ಮೂಲಕ ಸಬ್ಮಿಟ್ ಮಾಡಿ.
6. ವಾಣಿಜ್ಯ ತೆರಿಗೆ ಅಧಿಕಾರಿ ಪರಿಶೀಲಿಸಿ 30 ದಿನಗಳಲ್ಲಿ ಅಧಿಕೃತ ರದ್ದತಿ ಆದೇಶ (Order for Cancellation - REG-19) ಹೊರಡಿಸುತ್ತಾರೆ.""",
        "category": "INDUSTRY",
        "language": "kn",
        "source_url": "https://gst.karnataka.gov.in",
        "keywords": "gst cancellation online reg 16, surrender gst number karnataka, commercial tax gst closure, ಜಿಎಸ್‌ಟಿ ರದ್ದು, ಜಿಎಸ್‌ಟಿ ಸರೆಂಡರ್",
        "action_label": "🧾 GST ಪೋರ್ಟಲ್",
        "action_url": "https://www.gst.gov.in"
    },
    {
        "id": "faq_user_265",
        "question": "ಸರ್ಕಾರಿ ರೇಷ್ಮೆ ಮಾರುಕಟ್ಟೆಗಳಲ್ಲಿ ಇ-ಹರಾಜು (e-Auction) ಮತ್ತು ನೇರ ಪಾವತಿ (Direct Silk Payment) ಸೌಲಭ್ಯವೇನು?",
        "normalized_question": "sericulture e auction cocoon market ramanagara direct bank payment reshme mandi ರೇಷ್ಮೆ ಇ-ಹರಾಜು ಮಾರುಕಟ್ಟೆ",
        "answer": """### 🐛 ಏಷ್ಯಾದ ಅತಿದೊಡ್ಡ ರೇಷ್ಮೆ ಗೂಡು ಮಾರುಕಟ್ಟೆ ಇ-ಹರಾಜು (e-Cocoon Trading)

ರಾಮನಗರ, ಶಿಡ್ಲಘಟ್ಟ, ಕೋಲಾರ ಮತ್ತು ವಿಜಯಪುರ ರೇಷ್ಮೆ ಗೂಡು ಮಾರುಕಟ್ಟೆಗಳಲ್ಲಿ ದಲ್ಲಾಳಿಗಳ ಹಾವಳಿ ತಪ್ಪಿಸಲು ಸಂಪೂರ್ಣ ಕಂಪ್ಯೂಟರೀಕೃತ ಇ-ಹರಾಜು ಜಾರಿಯಲ್ಲಿದೆ.

---

### 🌟 ವ್ಯವಸ್ಥೆಯ ಪ್ರಮುಖ ವೈಶಿಷ್ಟ್ಯಗಳು:
* **ಸ್ವಯಂಚಾಲಿತ ತೂಕ ಮತ್ತು ಇ-ಹರಾಜು:** ಗೂಡು ತಂದ ತಕ್ಷಣ ಡಿಜಿಟಲ್ ತೂಕ ಯಂತ್ರದ ಮೂಲಕ ತೂಕ ಹಾಕಿ ಆನ್‌ಲೈನ್ ಬಿಡ್ಡಿಂಗ್‌ನಲ್ಲಿ ಗರಿಷ್ಠ ಬೆಲೆಗೆ ಮಾರಾಟ ಮಾಡಲಾಗುತ್ತದೆ.
* **ಅದೇ ದಿನ ಬ್ಯಾಂಕ್‌ಗೆ ಹಣ ಜಮೆ:** ರೀಲರ್‌ಗಳು ಖರೀದಿಸಿದ ಗೂಡಿನ ಸಂಪೂರ್ಣ ಹಣ ಮತ್ತು ಸರ್ಕಾರದ ಪ್ರೋತ್ಸಾಹಧನವು ಅದೇ ದಿನ ಸಂಜೆಯೊಳಗೆ ರೈತರ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ನೇರವಾಗಿ RTGS/NEFT ಮೂಲಕ ಜಮೆಯಾಗುತ್ತದೆ.

🔗 **ರೇಷ್ಮೆ ಇಲಾಖೆ:** [sericulture.karnataka.gov.in](https://sericulture.karnataka.gov.in)""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://sericulture.karnataka.gov.in",
        "keywords": "ramanagara silk cocoon market, sericulture e auction, direct cocoon payment, ರಾಮನಗರ ರೇಷ್ಮೆ ಮಾರುಕಟ್ಟೆ, ರೇಷ್ಮೆ ಇ-ಹರಾಜು",
        "action_label": "🐛 ರೇಷ್ಮೆ ಮಾರುಕಟ್ಟೆ ವಿವರ",
        "action_url": "https://sericulture.karnataka.gov.in"
    },
    {
        "id": "faq_user_266",
        "question": "ಹಿರಿಯ ನಾಗರಿಕರ ಸುರಕ್ಷತೆಗಾಗಿ ಕರ್ನಾಟಕ ಪೊಲೀಸ್ 'ಹಿರಿಯ ನಾಗರಿಕರ ಸುರಕ್ಷಾ ಕಾರ್ಡ್' (Elder Protection Registry) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "senior citizen suraksha card karnataka police elder protection helpline 1090 ಹಿರಿಯ ನಾಗರಿಕರ ಸುರಕ್ಷಾ ಕಾರ್ಡ್",
        "answer": """### 👮 ಕರ್ನಾಟಕ ಪೊಲೀಸ್ ಹಿರಿಯ ನಾಗರಿಕರ ಸುರಕ್ಷಾ ಯೋಜನೆ (Senior Citizen Protection)

ಮನೆಯಲ್ಲಿ ಒಂಟಿಯಾಗಿ ವಾಸಿಸುವ ಹಿರಿಯ ನಾಗರಿಕರ ರಕ್ಷಣೆ, ತುರ್ತು ವೈದ್ಯಕೀಯ ನೆರವು ಮತ್ತು ಕಳ್ಳತನ ತಡೆಗಟ್ಟಲು ಪೊಲೀಸ್ ಇಲಾಖೆಯು ವಿಶೇಷ ನೋಂದಣಿ ಅಭಿಯಾನ ನಡೆಸುತ್ತದೆ.

---

### 🛡️ ಸುರಕ್ಷಾ ನೋಂದಣಿಯ ಪ್ರಯೋಜನಗಳು:
* **ಸ್ಥಳೀಯ ಬೀಟ್ ಪೊಲೀಸ್ ನಿರಂತರ ಭೇಟಿ:** ಸ್ಥಳೀಯ ಠಾಣೆಯ ಬೀಟ್ ಕಾನ್‌ಸ್ಟೇಬಲ್ ವಾರಕ್ಕೊಮ್ಮೆ ಮನೆಗೆ ಭೇಟಿ ನೀಡಿ ಕ್ಷೇಮ ವಿಚಾರಿಸುತ್ತಾರೆ.
* **ತುರ್ತು ಸಹಾಯವಾಣಿ:** **1090 (Senior Citizen Helpline)** ಅಥವಾ **112** ಗೆ ಕರೆ ಮಾಡಿದರೆ ಆದ್ಯತೆಯ ಮೇಲೆ ಪೊಲೀಸ್ ನೆರವು.
* ಹಿರಿಯ ನಾಗರಿಕರ ಸುರಕ್ಷಾ ಗುರುತಿನ ಚೀಟಿ (Senior Citizen Suraksha ID Card) ವಿತರಣೆ.

📝 [ksp.karnataka.gov.in](https://ksp.karnataka.gov.in) ನಲ್ಲಿ ಅಥವಾ ಸ್ಥಳೀಯ ಪೊಲೀಸ್ ಠಾಣೆಗೆ ತೆರಳಿ ಉಚಿತವಾಗಿ ಹೆಸರು ನೋಂದಾಯಿಸಿಕೊಳ್ಳಬಹುದು.""",
        "category": "POLICE",
        "language": "kn",
        "source_url": "https://ksp.karnataka.gov.in",
        "keywords": "senior citizen suraksha card, elder helpline 1090 bangalore, police protection elderly, ಹಿರಿಯ ನಾಗರಿಕರ ಸುರಕ್ಷಾ ಕಾರ್ಡ್, ಪೊಲೀಸ್ 1090",
        "action_label": "👮 ಪೊಲೀಸ್ ಸುರಕ್ಷಾ ಪೋರ್ಟಲ್",
        "action_url": "https://ksp.karnataka.gov.in"
    },
    {
        "id": "faq_user_267",
        "question": "ಅಲ್ಪಸಂಖ್ಯಾತ ವಿದ್ಯಾರ್ಥಿನಿಯರ 'ಬೇಗಂ ಹಜರತ್ ಮಹಲ್' ರಾಷ್ಟ್ರೀಯ ವಿದ್ಯಾರ್ಥಿವೇತನಕ್ಕೆ ಅರ್ಜಿ ಸಲ್ಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "begum hazrat mahal scholarship minority girls apply national scholarship portal ಬೇಗಂ ಹಜರತ್ ಮಹಲ್ ವಿದ್ಯಾರ್ಥಿವೇತನ",
        "answer": """### 🎓 ಬೇಗಂ ಹಜರತ್ ಮಹಲ್ ರಾಷ್ಟ್ರೀಯ ವಿದ್ಯಾರ್ಥಿವೇತನ (Begum Hazrat Mahal National Scholarship)

ಮುಸ್ಲಿಂ, ಕ್ರಿಶ್ಚಿಯನ್, ಜೈನ, ಬೌದ್ಧ, ಸಿಖ್ ಮತ್ತು ಪಾರ್ಸಿ ಸಮುದಾಯದ 9 ನೇ ತರಗತಿಯಿಂದ 12 ನೇ ತರಗತಿ (PUC) ವರೆಗೆ ವ್ಯಾಸಂಗ ಮಾಡುವ ಬಡ ಪ್ರತಿಭಾವಂತ ಹೆಣ್ಣು ಮಕ್ಕಳಿಗೆ ಕೇಂದ್ರ ಅಲ್ಪಸಂಖ್ಯಾತರ ಸಚಿವಾಲಯ ನೀಡುವ ವಿದ್ಯಾರ್ಥಿವೇತನ.

---

### 💰 ವಿದ್ಯಾರ್ಥಿವೇತನ ಮೊತ್ತ:
* **9 ನೇ ಮತ್ತು 10 ನೇ ತರಗತಿ ವಿದ್ಯಾರ್ಥಿನಿಯರಿಗೆ:** ವಾರ್ಷಿಕ **₹5,000**.
* **11 ನೇ ಮತ್ತು 12 ನೇ ತರಗತಿ (1st & 2nd PUC) ವಿದ್ಯಾರ್ಥಿನಿಯರಿಗೆ:** ವಾರ್ಷಿಕ **₹6,000**.

---

### 📌 ಅರ್ಹತೆ & ಅರ್ಜಿ:
1. ಹಿಂದಿನ ತರಗತಿಯಲ್ಲಿ ಕನಿಷ್ಠ 50% ಅಂಕಗಳನ್ನು ಪಡೆದಿರಬೇಕು.
2. ಪೋಷಕರ ಒಟ್ಟು ವಾರ್ಷಿಕ ಆದಾಯ ₹2.00 ಲಕ್ಷ ಮೀರಬಾರದು.
3. [scholarships.gov.in](https://scholarships.gov.in) (National Scholarship Portal - NSP) ನಲ್ಲಿ ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಸಬೇಕು.""",
        "category": "EDUCATION",
        "language": "kn",
        "source_url": "https://scholarships.gov.in",
        "keywords": "begum hazrat mahal scholarship, nsp minority girl scholarship, puc girl scholarship, ಬೇಗಂ ಹಜರತ್ ಮಹಲ್ ವಿದ್ಯಾರ್ಥಿವೇತನ, ಅಲ್ಪಸಂಖ್ಯಾತ ಹೆಣ್ಣು ಮಕ್ಕಳ ಸ್ಕಾಲರ್‌ಶಿಪ್",
        "action_label": "🎓 NSP ಪೋರ್ಟಲ್",
        "action_url": "https://scholarships.gov.in"
    },
    {
        "id": "faq_user_268",
        "question": "ಗ್ರಾಮ ನ್ಯಾಯಾಲಯಗಳು (Grama Nyayalaya) ಎಂದರೇನು? ಹಳ್ಳಿಗಳಲ್ಲಿ ಸುಲಭ ನ್ಯಾಯ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "grama nyayalaya karnataka rural speedy justice petty disputes civil criminal ಗ್ರಾಮ ನ್ಯಾಯಾಲಯ",
        "answer": """### ⚖️ ಗ್ರಾಮ ನ್ಯಾಯಾಲಯ ಅಧಿನಿಯಮ (Grama Nyayalaya — ಹಳ್ಳಿ ಜನರ ಮನೆ ಬಾಗಿಲಿಗೆ ನ್ಯಾಯ)

ಗ್ರಾಮೀಣ ಭಾಗದ ಬಡ ಜನರಿಗೆ ತಾಲೂಕು ಅಥವಾ ಜಿಲ್ಲಾ ಕೋರ್ಟ್‌ಗಳಿಗೆ ಅಲೆದಾಡದೆ, ಕಡಿಮೆ ಖರ್ಚಿನಲ್ಲಿ ಸ್ಥಳೀಯ ಮಟ್ಟದಲ್ಲೇ ಸಿವಿಲ್ ಮತ್ತು ಸಣ್ಣ ಕ್ರಿಮಿನಲ್ ವ್ಯಾಜ್ಯಗಳನ್ನು ತ್ವರಿತವಾಗಿ ಇತ್ಯರ್ಥಪಡಿಸುವ ನ್ಯಾಯಾಲಯ.

---

### 🏛️ ಗ್ರಾಮ ನ್ಯಾಯಾಲಯದ ಪ್ರಮುಖ ಅಧಿಕಾರಗಳು:
* **ನ್ಯಾಯಾಧಿಕಾರಿ (Nyayadhikari):** ಪ್ರಥಮ ದರ್ಜೆ ಜ್ಯುಡಿಷಿಯಲ್ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ (JMFC) ದರ್ಜೆಯ ನ್ಯಾಯಾಧೀಶರು ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ಕೇಂದ್ರಕ್ಕೆ ಭೇಟಿ ನೀಡಿ ಕಲಾಪ ನಡೆಸುತ್ತಾರೆ.
* **ವಿಚಾರಣೆ ನಡೆಸುವ ವ್ಯಾಜ್ಯಗಳು:** ಜಮೀನು ಗಡಿ ತಕರಾರು, ಕೌಟುಂಬಿಕ ಕಲಹಗಳು, ಜಂಟಿ ಆಸ್ತಿ ವಿವಾದ, ಕೂಲಿ ಹಣದ ವಿವಾದ, ಕಳ್ಳತನ, ಸಣ್ಣ ಹೊಡೆದಾಟ ಪ್ರಕರಣಗಳು.
* **ರಾಜಿ ಸಂಧಾನಕ್ಕೆ ಆದ್ಯತೆ:** ಮೊದಲು ಸಂಧಾನಕಾರರ (Conciliators) ಮೂಲಕ ಪರಸ್ಪರ ರಾಜಿ ಮಾಡಿಸಲು ಪ್ರಯತ್ನಿಸಲಾಗುತ್ತದೆ. 6 ತಿಂಗಳಲ್ಲಿ ಪ್ರಕರಣ ಇತ್ಯರ್ಥಪಡಿಸುವುದು ಇದರ ಗುರಿ.""",
        "category": "LEGAL",
        "language": "kn",
        "source_url": "https://karnatakajudiciary.kar.nic.in",
        "keywords": "grama nyayalaya karnataka, rural court speedy justice, nyayadhikari mobile court, ಗ್ರಾಮ ನ್ಯಾಯಾಲಯ, ಗ್ರಾಮೀಣ ನ್ಯಾಯ",
        "action_label": "⚖️ ಹೈಕೋರ್ಟ್ ಪೋರ್ಟಲ್",
        "action_url": "https://karnatakajudiciary.kar.nic.in"
    },
    {
        "id": "faq_user_269",
        "question": "ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆಗೆ ವಾರ್ಷಿಕ ಇ-ಕೆವೈಸಿ ಅಥವಾ ಜೀವಂತ ಪ್ರಮಾಣಪತ್ರ (Life Certificate / Annual Re-KYC) ಅಗತ್ಯವೇ?",
        "normalized_question": "gruha lakshmi annual ekyc life certificate physical verification fraud prevention ಗೃಹಲಕ್ಷ್ಮಿ ವಾರ್ಷಿಕ ಇ-ಕೆವೈಸಿ",
        "answer": """### 🌸 ಗೃಹಲಕ್ಷ್ಮಿ ವಾರ್ಷಿಕ ಪರಿಶೀಲನೆ ಮತ್ತು e-KYC ಮಾರ್ಗಸೂಚಿ

ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆಯ ₹2,000 ಹಣ ಯಾವುದೇ ಮಧ್ಯವರ್ತಿಗಳಿಲ್ಲದೆ ನಿರಂತರವಾಗಿ ಜಮೆಯಾಗಲು ಫಲಾನುಭವಿಗಳು ಪಾಲಿಸಬೇಕಾದ ನಿಯಮಗಳು:

---

### 📌 ನಿಯಮಾವಳಿಗಳು:
1. **ನಿಯಮಿತ ಇ-ಕೆವೈಸಿ:** ರೇಷನ್ ಕಾರ್ಡ್‌ನಲ್ಲಿರುವ ಎಲ್ಲಾ ಸದಸ್ಯರು ನ್ಯಾಯಬೆಲೆ ಅಂಗಡಿಗಳಲ್ಲಿ ನಿಯಮಿತವಾಗಿ ಬಯೋಮೆಟ್ರಿಕ್ e-KYC ಮಾಡಿಸುತ್ತಿರಬೇಕು.
2. **ಜೀವಂತ ಪ್ರಮಾಣಪತ್ರ / ಭೌತಿಕ ಪರಿಶೀಲನೆ:** ಫಲಾನುಭವಿ ಮಹಿಳೆ ಜೀವಂತವಾಗಿರುವುದನ್ನು ಮತ್ತು ಅದೇ ವಿಳಾಸದಲ್ಲಿ ವಾಸಿಸುತ್ತಿರುವುದನ್ನು ದೃಢೀಕರಿಸಲು ಮಹಿಳಾ ಮತ್ತು ಮಕ್ಕಳ ಕಲ್ಯಾಣ ಇಲಾಖೆಯ ಅಂಗನವಾಡಿ ಕಾರ್ಯಕರ್ತೆಯರು ನಿಯಮಿತವಾಗಿ ಪರಿಶೀಲನೆ ನಡೆಸುತ್ತಾರೆ.
3. ಮೃತಪಟ್ಟ ಫಲಾನುಭವಿಗಳ ಹೆಸರನ್ನು ತಕ್ಷಣ ರೇಷನ್ ಕಾರ್ಡ್‌ನಿಂದ ತೆಗೆದುಹಾಕಿ ಕುಟುಂಬದ ಮುಂದಿನ ಹಿರಿಯ ಮಹಿಳೆಯನ್ನು ಯಜಮಾನಿ ಎಂದು ನವೀಕರಿಸಿದರೆ ಮಾತ್ರ ಹಣ ಮುಂದುವರಿಯುತ್ತದೆ.""",
        "category": "SCHEME",
        "language": "kn",
        "source_url": "https://sevasindhugs.karnataka.gov.in",
        "keywords": "gruha lakshmi annual ekyc, life certificate head of family, ration card verification, ಗೃಹಲಕ್ಷ್ಮಿ ವಾರ್ಷಿಕ ಇ-ಕೆವೈಸಿ, ಜೀವಂತ ಪ್ರಮಾಣಪತ್ರ",
        "action_label": "🌸 ಗ್ಯಾರಂಟಿ ಪೋರ್ಟಲ್",
        "action_url": "/guarantee-schemes.html"
    }
]

# =========================================================================
# 18. EXPANSION BATCH 10: BENGALURU-CENTRIC CIVIC & URBAN TRANSIT (270 - 285)
# =========================================================================

ADDITIONAL_EXPANSION_FAQS_BATCH_10 = [
    {
        "id": "faq_blr_270",
        "question": "ಬೆಂಗಳೂರಿನ 110 ಹಳ್ಳಿಗಳಿಗೆ ಕಾವೇರಿ 5ನೇ ಹಂತದ (Cauvery Stage 5) ಕುಡಿಯುವ ನೀರಿನ ಸಂಪರ್ಕ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "cauvery stage 5 bwssb drinking water connection 110 villages mahadevapura bommanahalli ಕಾವೇರಿ 5ನೇ ಹಂತ",
        "answer": """### 🚰 BWSSB ಕಾವೇರಿ 5ನೇ ಹಂತ — 110 ಹಳ್ಳಿಗಳಿಗೆ ಕುಡಿಯುವ ನೀರು ಸಂಪರ್ಕ

ಬಿಬಿಎಂಪಿ ವ್ಯಾಪ್ತಿಗೆ ಸೇರ್ಪಡೆಗೊಂಡಿರುವ ಮಹದೇವಪುರ, ಬೊಮ್ಮನಹಳ್ಳಿ, ರಾಜರಾಜೇಶ್ವರಿ ನಗರ, ದಾಸರಹಳ್ಳಿ ಮತ್ತು ಬ್ಯಾಟರಾಯನಪುರ ವಲಯಗಳ 110 ಹಳ್ಳಿಗಳ ನಿವಾಸಿಗಳಿಗೆ ಪ್ರತಿದಿನ 775 ಎಂಎಲ್‌ಡಿ ಶುದ್ಧ ಕಾವೇರಿ ನೀರು ಒದಗಿಸುವ ಯೋಜನೆ.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
* ಆಸ್ತಿಯ BBMP ಇ-ಖಾತಾ (A-Khata ಅಥವಾ e-Aasthi ದಾಖಲೆ).
* ಇತ್ತೀಚಿನ ಆಸ್ತಿ ತೆರಿಗೆ ಪಾವತಿ ರಶೀದಿ (Tax Receipt).
* ಮಾಲೀಕರ ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ಅನುಮೋದಿತ ಕಟ್ಟಡ ನಕ್ಷೆ (Sanctioned Plan).

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಕೆ:
1. **ಜಲ ಮಂಡಳಿ ಪೋರ್ಟಲ್:** [bwssb.karnataka.gov.in](https://bwssb.karnataka.gov.in) ನಲ್ಲಿ **'Sajala 2.0'** ಗೆ ಭೇಟಿ ನೀಡಿ.
2. ನಿವೇಶನದ ವಿಸ್ತೀರ್ಣ (Dimension - ಉದಾ: 30x40, 40x60) ಮತ್ತು ಕೊಳಾಯಿ ಗಾತ್ರ (Pipe Size) ನಮೂದಿಸಿ.
3. ಪ್ರೊ-ರೇಟಾ ಶುಲ್ಕ (Pro-rata charges) ಮತ್ತು ಮೀಟರ್ ಶುಲ್ಕವನ್ನು ಆನ್‌ಲೈನ್ ಚಲನ್ ಮೂಲಕ ಪಾವತಿಸಿ.
4. ಜಲ ಮಂಡಳಿ ಸಿಬ್ಬಂದಿ ಪೈಪ್‌ಲೈನ್ ಅಳವಡಿಸಿ ವಾಟರ್ ಮೀಟರ್ ಸಂಪರ್ಕ ನೀಡುತ್ತಾರೆ.

🔗 **ಸಹಾಯವಾಣಿ:** **1916** (24x7 BWSSB Call Centre)""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bwssb.karnataka.gov.in",
        "keywords": "cauvery stage 5, 110 villages water connection, bwssb sajala online, ಕಾವೇರಿ 5ನೇ ಹಂತ, ಮಹದೇವಪುರ ಕಾವೇರಿ ನೀರು",
        "action_label": "🚰 Sajala 2.0 ಪೋರ್ಟಲ್",
        "action_url": "https://bwssb.karnataka.gov.in"
    },
    {
        "id": "faq_blr_271",
        "question": "ನಮ್ಮ ಮೆಟ್ರೋ ಹಳದಿ (Yellow Line) ಮತ್ತು ಗುಲಾಬಿ (Pink Line) ಮಾರ್ಗಗಳ ವಿವರ ಹಾಗೂ ಇಂಟರ್‌ಚೇಂಜ್ ನಿಲ್ದಾಣಗಳು ಯಾವುವು?",
        "normalized_question": "namma metro yellow line bommasandra pink line nagawara driverless cbtc interchange ನಮ್ಮ ಮೆಟ್ರೋ ಹಳದಿ ಮಾರ್ಗ",
        "answer": """### 🚇 ನಮ್ಮ ಮೆಟ್ರೋ ಹಳದಿ & ಗುಲಾಬಿ ಮಾರ್ಗಗಳ ಸಂಪೂರ್ಣ ವಿವರ (BMRCL)

ಬೆಂಗಳೂರಿನ ಟೆಕ್ ಕಾರಿಡಾರ್ ಹಾಗೂ ಉತ್ತರ-ದಕ್ಷಿಣ ಸಂಪರ್ಕವನ್ನು ಕಲ್ಪಿಸುವ ನೂತನ ಮೆಟ್ರೋ ಮಾರ್ಗಗಳು:

---

### 🟡 1. ಹಳದಿ ಮಾರ್ಗ (Yellow Line - Reach 5):
* **ಮಾರ್ಗ:** ಆರ್.ವಿ. ರಸ್ತೆ (RV Road) ಯಿಂದ ಬೊಮ್ಮಸಂದ್ರ (Bommasandra - Electronic City).
* **ಉದ್ದ & ನಿಲ್ದಾಣಗಳು:** 18.82 ಕಿ.ಮೀ, 16 ಎಲಿವೇಟೆಡ್ ನಿಲ್ದಾಣಗಳು (ಜಯದೇವ, ಸಿಲ್ಕ್ ಬೋರ್ಡ್, ಎಲೆಕ್ಟ್ರಾನಿಕ್ ಸಿಟಿ ಮಾರ್ಗ).
* **ವಿಶೇಷತೆ:** ಭಾರತದಲ್ಲೇ ಮೊದಲ ಬಾರಿಗೆ ಅತ್ಯಾಧುನಿಕ **ಚಾಲಕರಹಿತ CBTC (Driverless Trains)** ತಂತ್ರಜ್ಞಾನ.

---

### 🌸 2. ಗುಲಾಬಿ ಮಾರ್ಗ (Pink Line - Reach 6):
* **ಮಾರ್ಗ:** ಕಾಳೇನ ಅಗ್ರಹಾರ (ಬನ್ನೇರುಘಟ್ಟ ರಸ್ತೆ) ದಿಂದ ನಾಗವಾರ ವರೆಗೆ (21.38 ಕಿ.ಮೀ).
* **ವಿಶೇಷತೆ:** 13.8 ಕಿ.ಮೀ ಉದ್ದದ ಬೆಂಗಳೂರಿನ ಅತಿ ಉದ್ದದ ಭೂಗತ (Underground) ಸುರಂಗ ಮಾರ್ಗ.

---

### 🔄 ಪ್ರಮುಖ ಮೆಗಾ ಇಂಟರ್‌ಚೇಂಜ್ ಹಬ್:
* **ಜಯದೇವ ಇಂಟರ್‌ಚೇಂಜ್ (Jayadeva Flyover Station):** ಹಳದಿ ಮಾರ್ಗ ಮತ್ತು ಗುಲಾಬಿ ಮಾರ್ಗಗಳು ಸಂಧಿಸುವ ಭಾರತದ ಅತಿದೊಡ್ಡ ಬಹುಮಹಡಿ ಮೆಟ್ರೋ ಜಂಕ್ಷನ್.""",
        "category": "TRANSIT",
        "language": "kn",
        "source_url": "https://english.bmrc.co.in",
        "keywords": "namma metro yellow line electronic city, pink line underground nagawara, jayadeva interchange, ನಮ್ಮ ಮೆಟ್ರೋ ಹಳದಿ ಮಾರ್ಗ, ಬೊಮ್ಮಸಂದ್ರ ಮೆಟ್ರೋ",
        "action_label": "🚇 BMRCL ಅಧಿಕೃತ ಪೋರ್ಟಲ್",
        "action_url": "https://english.bmrc.co.in"
    },
    {
        "id": "faq_blr_272",
        "question": "BMTC ದಿನದ ಪಾಸ್ (Daily Pass) ಮತ್ತು ಮಾಸಿಕ ಪಾಸ್ ಮೊಬೈಲ್‌ನಲ್ಲೇ Tummoc / Namma BMTC App ನಲ್ಲಿ ಬುಕ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "bmtc daily pass monthly bus pass online tummoc app namma bmtc digital ticket ಬಿಎಂಟಿಸಿ ದಿನದ ಪಾಸ್",
        "answer": """### 🚌 BMTC ಡಿಜಿಟಲ್ ದಿನದ ಪಾಸ್ & ಮಾಸಿಕ ಪಾಸ್ (Tummoc & Namma BMTC App)

ಬೆಂಗಳೂರು ಮಹಾನಗರ ಸಾರಿಗೆ ಸಂಸ್ಥೆಯು (BMTC) ನಗದುರಹಿತ ಪ್ರಯಾಣಕ್ಕಾಗಿ ಮೊಬೈಲ್‌ನಲ್ಲೇ ಡಿಜಿಟಲ್ ಪಾಸ್ ಮತ್ತು ಕ್ಯೂಆರ್ ಟಿಕೆಟ್ ಸೌಲಭ್ಯ ಒದಗಿಸಿದೆ.

---

### 📱 ದಿನದ ಪಾಸ್ (Daily Pass - ₹70) ಬುಕ್ ಮಾಡುವ ವಿಧಾನ:
1. ಗೂಗಲ್ ಪ್ಲೇ ಸ್ಟೋರ್‌ನಿಂದ **'Tummoc'** ಅಥವಾ **'Namma BMTC'** ಆ್ಯಪ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ.
2. ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಹಾಕಿ ಸೈನ್ ಇನ್ ಆಗಿ **'BMTC Bus Pass'** ಆಯ್ಕೆಮಾಡಿ.
3. **'Daily Pass (Non-AC Ordinary ₹70 / Vajra AC ₹120)'** ಆಯ್ಕೆಮಾಡಿ.
4. ನಿಮ್ಮ ಲೈವ್ ಸೆಲ್ಫಿ ಫೋಟೋ ಮತ್ತು ಸರ್ಕಾರದ ಐಡಿ ಕಾರ್ಡ್ (ಆಧಾರ್/ಪ್ಯಾನ್) ಸಂಖ್ಯೆ ನಮೂದಿಸಿ.
5. UPI ಮೂಲಕ ಪಾವತಿಸಿ. ಬಸ್ ಹತ್ತಿದಾಗ ನಿರ್ವಾಹಕರಿಗೆ ಮೊಬೈಲ್‌ನಲ್ಲಿರುವ ಡೈನಾಮಿಕ್ ಕ್ಯೂಆರ್ ಕೋಡ್ ತೋರಿಸಿ ಪ್ರಯಾಣಿಸಿ.

💡 ಮಾಸಿಕ ಪಾಸುಗಳನ್ನೂ (Monthly Pass) ಇದೇ ಆ್ಯಪ್ ಮೂಲಕ ಮನೆಯಲ್ಲೇ ಕುಳಿತು ನವೀಕರಿಸಿಕೊಳ್ಳಬಹುದು.""",
        "category": "TRANSIT",
        "language": "kn",
        "source_url": "https://mybmtc.karnataka.gov.in",
        "keywords": "bmtc daily pass tummoc, namma bmtc monthly pass online, bmtc bus tracking app, ಬಿಎಂಟಿಸಿ ದಿನದ ಪಾಸ್, ತುಮ್ಮೊಕ್ ಆ್ಯಪ್",
        "action_label": "🚌 BMTC ಪೋರ್ಟಲ್",
        "action_url": "https://mybmtc.karnataka.gov.in"
    },
    {
        "id": "faq_blr_273",
        "question": "ಬೆಂಗಳೂರಿನ ರಸ್ತೆ ಗುಂಡಿಗಳ ಬಗ್ಗೆ 'Fix My Street / Namma Bengaluru' ಆ್ಯಪ್‌ನಲ್ಲಿ ದೂರು ನೀಡುವುದು ಹೇಗೆ?",
        "normalized_question": "bbmp pothole complaint fix my street app namma bengaluru sahaaya 2.0 ರಸ್ತೆ ಗುಂಡಿ ದೂರು ಬಿಬಿಎಂಪಿ",
        "answer": """### 🛣️ BBMP ರಸ್ತೆ ಗುಂಡಿ ನಿವಾರಣೆ & 'ಫಿಕ್ಸ್ ಮೈ ಸ್ಟ್ರೀಟ್' (Fix My Street) ದೂರು ವ್ಯವಸ್ಥೆ

ಬೆಂಗಳೂರಿನ ರಸ್ತೆಗಳಲ್ಲಿ ಗುಂಡಿಗಳು, ಒಡೆದ ಪಾದಚಾರಿ ಮಾರ್ಗಗಳು (Footpaths) ಅಥವಾ ಒಳಚರಂಡಿ ಮುಚ್ಚಳ ತೆರೆದಿದ್ದರೆ ಮೊಬೈಲ್ ಮೂಲಕ ಜಿಪಿಎಸ್ ಫೋಟೋ ಸಮೇತ ದೂರು ನೀಡಬಹುದು.

---

### 📱 ದೂರು ದಾಖಲಿಸುವ ಹಂತಗಳು:
1. **Fix My Street** ಅಥವಾ **Namma Bengaluru (BBMP Sahaaya 2.0)** ಆ್ಯಪ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ.
2. ರಸ್ತೆ ಗುಂಡಿಯ ನೇರ ಫೋಟೋ ತೆಗೆಯಿರಿ (ಆ್ಯಪ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಜಿಪಿಎಸ್ ಲೊಕೇಶನ್ ಮತ್ತು ವಾರ್ಡ್ ಸಂಖ್ಯೆ ಗುರುತಿಸುತ್ತದೆ).
3. ಸಮಸ್ಯೆಯ ವಿವರ ನಮೂದಿಸಿ ಸಬ್ಮಿಟ್ ಮಾಡಿ.
4. **48 ಗಂಟೆಗಳ ಕಾಲಮಿತಿ:** ಸಂಬಂಧಪಟ್ಟ ಬಿಬಿಎಂಪಿ ವಾರ್ಡ್ ಇಂಜಿನಿಯರ್‌ಗೆ ಎಸ್‌ಎಂಎಸ್ ಹೋಗಲಿದ್ದು, ಗುಂಡಿ ಮುಚ್ಚಿದ ನಂತರ ರಿಪೇರಿ ಮಾಡಿದ ಫೋಟೋವನ್ನು ಆ್ಯಪ್‌ನಲ್ಲಿ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ದೂರು ಮುಕ್ತಾಯಗೊಳಿಸಬೇಕು.

📞 **BBMP 24x7 ಕಂಟ್ರೋಲ್ ರೂಂ:** **080-22660000** | **WhatsApp:** 9480685700""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bbmp.gov.in",
        "keywords": "fix my street bbmp, pothole complaint bangalore, bbmp sahaaya 2.0, ರಸ್ತೆ ಗುಂಡಿ ದೂರು, ಬಿಬಿಎಂಪಿ ಕಂಟ್ರೋಲ್ ರೂಂ",
        "action_label": "🛣️ BBMP ದೂರು ಪೋರ್ಟಲ್",
        "action_url": "https://bbmp.gov.in"
    },
    {
        "id": "faq_blr_274",
        "question": "ಬಿಡಿಎ (BDA Layout) ಬಡಾವಣೆಗಳ ನಿವೇಶನಗಳಿಗೆ BBMP ಇ-ಖಾತಾ (A-Khata) ಮಾಡಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "bda layout to bbmp e khata a khata transfer amalgamation e aasthi ಬಿಡಿಎ ಇ-ಖಾತಾ ಬಿಬಿಎಂಪಿ",
        "answer": """### 🏛️ BDA ಯಿಂದ BBMP ಗೆ ಹಸ್ತಾಂತರಗೊಂಡ ಬಡಾವಣೆಗಳ ಇ-ಖಾತಾ ಪ್ರಕ್ರಿಯೆ

ಬೆಂಗಳೂರು ಅಭಿವೃದ್ಧಿ ಪ್ರಾಧಿಕಾರವು (BDA) ಅಭಿವೃದ್ಧಿಪಡಿಸಿ ಬಿಬಿಎಂಪಿಗೆ ಹಸ್ತಾಂತರಿಸಿದ ಬಡಾವಣೆಗಳಲ್ಲಿ (ಉದಾ: ಬನಶಂಕರಿ 6ನೇ ಹಂತ, ಅಂಜನಾಪುರ, ಸರ್. ಎಂ. ವಿಶ್ವೇಶ್ವರಯ್ಯ ಲೇಔಟ್, ನಾಡಪ್ರಭು ಕೆಂಪೇಗೌಡ ಲೇಔಟ್) ಇ-ಖಾತಾ ಪಡೆಯುವ ನಿಯಮ:

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
1. ಬಿಡಿಎ ಹಂಚಿಕೆ ಪತ್ರ (BDA Allotment Letter) ಮತ್ತು ಸ್ವಾಧೀನ ಪತ್ರ (Possession Certificate).
2. ನೋಂದಾಯಿತ ಬಿಡಿಎ ಕ್ರಯಪತ್ರ (Registered BDA Sale Deed / Lease-cum-Sale Deed).
3. ಬಿಡಿಎ ನಿವೇಶನ ನಕ್ಷೆ (Site Possession Sketch).
4. ಚಾಲ್ತಿ ಸಾಲಿನ ಬಿಬಿಎಂಪಿ ಆಸ್ತಿ ತೆರಿಗೆ ಪಾವತಿ ರಶೀದಿ.

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ:
* [bbmpeaasthi.karnataka.gov.in](https://bbmpeaasthi.karnataka.gov.in) ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ಬಿಡಿಎ ದಾಖಲೆಗಳನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿದರೆ ಸಹಾಯಕ ಕಂದಾಯ ಅಧಿಕಾರಿ (ARO) ಪರಿಶೀಲಿಸಿ ಡಿಜಿಟಲ್ **BBMP A-Khata Certificate** ವಿತರಿಸುತ್ತಾರೆ.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://bbmpeaasthi.karnataka.gov.in",
        "keywords": "bda to bbmp khata transfer, bda layout a khata, bbmpeaasthi bda plot, ಬಿಡಿಎ ಲೇಔಟ್ ಇ-ಖಾತಾ, ಎ-ಖಾತಾ ವರ್ಗಾವಣೆ",
        "action_label": "🏢 BBMP ಇ-ಆಸ್ತಿ",
        "action_url": "https://bbmpeaasthi.karnataka.gov.in"
    },
    {
        "id": "faq_blr_275",
        "question": "ಬೆಂಗಳೂರು ಸ್ಯಾಟಲೈಟ್ ಟೌನ್ ರಿಂಗ್ ರೋಡ್ (STRR / NH-948A) ಮಾರ್ಗ ಮತ್ತು ಸಂಪರ್ಕ ನಗರಗಳು ಯಾವುವು?",
        "normalized_question": "strr bangalore satellite town ring road nh 948a doddaballapur hoskote dobspet ಸ್ಯಾಟಲೈಟ್ ಟೌನ್ ರಿಂಗ್ ರೋಡ್",
        "answer": """### 🛣️ ಬೆಂಗಳೂರು ಸ್ಯಾಟಲೈಟ್ ಟೌನ್ ರಿಂಗ್ ರೋಡ್ (STRR — NH-948A)

ಬೆಂಗಳೂರು ನಗರದೊಳಗೆ ಬಾರದೆ ಹೊರವಲಯದಲ್ಲೇ ಸರಕು ಲಾರಿಗಳು ಮತ್ತು ಪ್ರಯಾಣಿಕ ವಾಹನಗಳು ಸಂಚರಿಸಲು ₹17,000 ಕೋಟಿ ವೆಚ್ಚದಲ್ಲಿ ನಿರ್ಮಿಸಲಾಗುತ್ತಿರುವ 288 ಕಿ.ಮೀ ಉದ್ದದ 6-ಪಥದ ಪ್ರವೇಶ-ನಿಯಂತ್ರಿತ ಎಕ್ಸ್‌ಪ್ರೆಸ್‌ವೇ (Expressway).

---

### 🗺️ ಸಂಪರ್ಕಿಸುವ ಪ್ರಮುಖ 12 ಉಪನಗರಗಳು:
* **ದಾಬಸ್‌ಪೇಟೆ (Dabaspet) -> ದೊಡ್ಡಬಳ್ಳಾಪುರ (Doddaballapur) -> ದೇವನಹಳ್ಳಿ (Devanahalli - Airport) -> ಹೊಸಕೋಟೆ (Hoskote) -> ಮಾಲೂರು -> ಹೊಸೂರು (ತಮಿಳುನಾಡು ಗಡಿ) -> ಆನೇಕಲ್ -> ಕನಕಪುರ -> ರಾಮನಗರ -> ಮಾಗಡಿ -> ದಾಬಸ್‌ಪೇಟೆ.**

---

### 🚗 ಪ್ರಮುಖ ಪ್ರಯೋಜನಗಳು:
* ಚೆನ್ನೈ ಎಕ್ಸ್‌ಪ್ರೆಸ್‌ವೇ (NE-7), ಬೆಂಗಳೂರು-ಮೈಸೂರು ಎಕ್ಸ್‌ಪ್ರೆಸ್‌ವೇ ಮತ್ತು ಮುಂಬೈ ಕಾರಿಡಾರ್‌ಗಳಿಗೆ (NH-48) ನೇರ ಸಿಗ್ನಲ್-ಮುಕ್ತ ಬೈಪಾಸ್ ಸಂಪರ್ಕ ಕಲ್ಪಿಸುತ್ತದೆ.
* ಬೆಂಗಳೂರು ನಗರದ ಒಳಗಿನ ಪೀಣ್ಯ, ಹೆಬ್ಬಾಳ ಮತ್ತು ಕೆ.ಆರ್. ಪುರಂ ಟ್ರಾಫಿಕ್ ದಟ್ಟಣೆಯನ್ನು 30% ಕ್ಕಿಂತ ಹೆಚ್ಚು ಕಡಿಮೆ ಮಾಡುತ್ತದೆ.""",
        "category": "TRANSPORT",
        "language": "kn",
        "source_url": "https://nhai.gov.in",
        "keywords": "strr bangalore route map, nh 948a satellite ring road, doddaballapur hoskote expressway, ಸ್ಯಾಟಲೈಟ್ ರಿಂಗ್ ರೋಡ್, ಎಸ್‌ಟಿಆರ್‌ಆರ್",
        "action_label": "🛣️ NHAI ಪೋರ್ಟಲ್",
        "action_url": "https://nhai.gov.in"
    },
    {
        "id": "faq_blr_276",
        "question": "ಬೆಂಗಳೂರಿನಲ್ಲಿ ನೋ-ಪಾರ್ಕಿಂಗ್ ವಾಹನಗಳಿಗೆ ಕ್ಲಾಂಪ್ (Wheel Clamp) ಹಾಕಿದರೆ ದಂಡ ಕಟ್ಟಿ ಬಿಡಿಸಿಕೊಳ್ಳುವುದು ಹೇಗೆ?",
        "normalized_question": "bangalore traffic police wheel clamp no parking fine btp payment ನೋ ಪಾರ್ಕಿಂಗ್ ಕ್ಲಾಂಪ್ ದಂಡ ಬಿಟಿಪಿ",
        "answer": """### 🚗 ಬೆಂಗಳೂರು ಟ್ರಾಫಿಕ್ ಪೊಲೀಸ್ ವೀಲ್ ಕ್ಲಾಂಪ್ & ನೋ-ಪಾರ್ಕಿಂಗ್ ನಿಯಮಗಳು (BTP Protocol)

ಬೆಂಗಳೂರಿನಲ್ಲಿ ವಾಹನ ಟೋಯಿಂಗ್ (Towing) ಬದಲಿಗೆ ಅಡ್ಡಾದಿಡ್ಡಿ ನಿಲ್ಲಿಸಿದ ವಾಹನಗಳಿಗೆ ಪೊಲೀಸರು ಚಕ್ರಕ್ಕೆ ಬೀಗ (Wheel Clamp) ಅಳವಡಿಸುತ್ತಾರೆ.

---

### 🔓 ಕ್ಲಾಂಪ್ ಬಿಡಿಸುವ ಹಂತಗಳು:
1. ವಾಹನದ ಮುಂಭಾಗದ ಗ್ಲಾಸ್ ಅಥವಾ ಹ್ಯಾಂಡಲ್‌ಬಾರ್ ಮೇಲೆ ಪೊಲೀಸರು ಅಂಟಿಸಿರುವ **ದಂಡದ ಸ್ಟಿಕ್ಕರ್ (Violation Notice)** ಪರಿಶೀಲಿಸಿ. ಅದರಲ್ಲಿ ಸಂಬಂಧಪಟ್ಟ ಟ್ರಾಫಿಕ್ ಪೊಲೀಸ್ ಠಾಣೆಯ ಹೆಸರು ಮತ್ತು ಎಎಸ್‌ಐ/ಹೆಡ್ ಕಾನ್‌ಸ್ಟೇಬಲ್ ಅಧಿಕೃತ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಇರುತ್ತದೆ.
2. ಆ ಸಂಖ್ಯೆಗೆ ಕರೆ ಮಾಡಿ ನಿಮ್ಮ ವಾಹನ ಸಂಖ್ಯೆ ತಿಳಿಸಿ.
3. ಪೊಲೀಸರ **Blackberry / e-Challan** ಯಂತ್ರದ ಮೂಲಕ ಅಥವಾ Paytm / Google Pay / BTP Portal ನಲ್ಲಿ ನಿಗದಿತ ನೋ-ಪಾರ್ಕಿಂಗ್ ದಂಡ (ದ್ವಿಚಕ್ರ ವಾಹನಕ್ಕೆ ₹500, ಕಾರುಗಳಿಗೆ ₹1,000) ಆನ್‌ಲೈನ್ ಪಾವತಿಸಿ ರಶೀದಿ ತೋರಿಸಿ.
4. ಪೊಲೀಸರು ಸ್ಥಳಕ್ಕೆ ಬಂದು ತಕ್ಷಣ ಕ್ಲಾಂಪ್ ತೆಗೆಯುತ್ತಾರೆ.

⚠️ ಬಲವಂತವಾಗಿ ಕ್ಲಾಂಪ್ ಮುರಿಯಲು ಪ್ರಯತ್ನಿಸಿದರೆ ಸರ್ಕಾರಿ ಆಸ್ತಿ ಹಾನಿ ಕಾಯ್ದೆಯಡಿ ಕ್ರಿಮಿನಲ್ ಕೇಸ್ ದಾಖಲಾಗುತ್ತದೆ.""",
        "category": "TRANSPORT",
        "language": "kn",
        "source_url": "https://btp.gov.in",
        "keywords": "btp wheel clamp fine, no parking violation bangalore, pay clamp fine online, ನೋ ಪಾರ್ಕಿಂಗ್ ಕ್ಲಾಂಪ್, ಬೆಂಗಳೂರು ಟ್ರಾಫಿಕ್ ಪೊಲೀಸ್",
        "action_label": "🚦 BTP ಚಲನ್ ಪೋರ್ಟಲ್",
        "action_url": "https://btp.gov.in"
    },
    {
        "id": "faq_blr_277",
        "question": "ಕೆಂಪೇಗೌಡ ಅಂತಾರಾಷ್ಟ್ರೀಯ ವಿಮಾನ ನಿಲ್ದಾಣಕ್ಕೆ (KIA Airport) ವಾಯುವಜ್ರ (Vayu Vajra AC) ಬಸ್ ಮಾರ್ಗಗಳು ಮತ್ತು ದರವೇನು?",
        "normalized_question": "vayu vajra airport bus routes timings bmtc majestic electronic city whitefield ವಾಯುವಜ್ರ ಏರ್‌ಪೋರ್ಟ್ ಬಸ್",
        "answer": """### ✈️ BMTC ವಾಯುವಜ್ರ (Vayu Vajra) ವಿಮಾನ ನಿಲ್ದಾಣ ಎಸಿ ಬಸ್ ಸೇವೆಗಳು

ಬೆಂಗಳೂರು ನಗರದ ಪ್ರಮುಖ ಬಡಾವಣೆಗಳಿಂದ ಕೆಂಪೇಗೌಡ ಅಂತಾರಾಷ್ಟ್ರೀಯ ವಿಮಾನ ನಿಲ್ದಾಣಕ್ಕೆ (KIA Terminal 1 & 2) 24x7 ಹವಾನಿಯಂತ್ರಿತ ವೋಲ್ವೋ ಬಸ್ ಸೇವೆ ಲಭ್ಯವಿದೆ.

---

### 🗺️ ಪ್ರಮುಖ ಜನಪ್ರಿಯ ಮಾರ್ಗಗಳು:
* **KIA-9:** ಮೆಜೆಸ್ಟಿಕ್ (KSRTC Kempegowda Bus Station) ನಿಂದ ವಿಮಾನ ನಿಲ್ದಾಣ (ದರ: ಸುಮಾರು ₹250).
* **KIA-8:** ಎಲೆಕ್ಟ್ರಾನಿಕ್ ಸಿಟಿ (Electronic City) ನಿಂದ ಸಿಲ್ಕ್ ಬೋರ್ಡ್, ಹೆಬ್ಬಾಳ ಮಾರ್ಗವಾಗಿ (ದರ: ಸುಮಾರು ₹320).
* **KIA-6:** ಕಾಡುಗೋಡಿ / ವೈಟ್‌ಫೀಲ್ಡ್ (Whitefield) ನಿಂದ ಕೆ.ಆರ್. ಪುರಂ ಮಾರ್ಗವಾಗಿ (ದರ: ಸುಮಾರು ₹300).
* **KIA-5:** ಬನಶಂಕರಿ / ಜಯನಗರ ನಿಂದ (ದರ: ಸುಮಾರು ₹280).

---

### 💼 ಸೌಲಭ್ಯಗಳು:
* ಲಗೇಜ್ ಇಡಲು ಪ್ರತ್ಯೇಕ ಜಾಗ, ಮೊಬೈಲ್ ಚಾರ್ಜಿಂಗ್ ಪಾಯಿಂಟ್ಸ್ ಹಾಗೂ ಡಿಜಿಟಲ್ ಯುಪಿಐ ಪಾವತಿ ಸೌಲಭ್ಯ.
* ಲೈವ್ ಬಸ್ ಎಲ್ಲಿದೆ ಎಂದು ತಿಳಿಯಲು **'Namma BMTC'** ಆ್ಯಪ್‌ನಲ್ಲಿ ಬಸ್ ನಂಬರ್ ಹಾಕಿ ಟ್ರ್ಯಾಕ್ ಮಾಡಬಹುದು.""",
        "category": "TRANSIT",
        "language": "kn",
        "source_url": "https://mybmtc.karnataka.gov.in",
        "keywords": "vayu vajra bus routes timings, kia 9 majestic to airport, kia 8 electronic city to airport, ವಾಯುವಜ್ರ ಬಸ್, ಏರ್‌ಪೋರ್ಟ್ ಬಸ್ ಬಿಎಂಟಿಸಿ",
        "action_label": "✈️ BMTC ವಾಯುವಜ್ರ ವೇಳಾಪಟ್ಟಿ",
        "action_url": "https://mybmtc.karnataka.gov.in"
    },
    {
        "id": "faq_blr_278",
        "question": "ಮಳೆಗಾಲದಲ್ಲಿ ಅಪಾಯಕಾರಿ ಮರ ಬಿದ್ದರೆ ಅಥವಾ ರೆಂಬೆ ಕತ್ತರಿಸಲು (BBMP Tree Trimming) ಎಲ್ಲಿ ದೂರು ನೀಡಬೇಕು?",
        "normalized_question": "bbmp forest cell tree trimming dangerous tree fall complaint 08022660000 ಮರ ಬಿದ್ದಾಗ ಬಿಬಿಎಂಪಿ ದೂರು",
        "answer": """### 🌳 BBMP ಅರಣ್ಯ ವಿಭಾಗ (Tree Trimming & Emergency Tree Fall Clearance)

ಮಳೆಗಾಲ ಮತ್ತು ಬಿರುಗಾಳಿಗೆ ಮರದ ಒಣಗಿದ ರೆಂಬೆಗಳು ವಿದ್ಯುತ್ ತಂತಿಯ ಮೇಲೆ ಬಿದ್ದರೆ ಅಥವಾ ರಸ್ತೆಗೆ ಅಡ್ಡಲಾಗಿ ಬಿದ್ದರೆ ತೆರವುಗೊಳಿಸಲು ಬಿಬಿಎಂಪಿ ಅರಣ್ಯ ವಿಭಾಗದ ತುರ್ತು ಕಂಟ್ರೋಲ್ ರೂಂ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ.

---

### 📞 ತುರ್ತು ದೂರು ಮಾರ್ಗಗಳು:
* **BBMP 24x7 ಕಂಟ್ರೋಲ್ ರೂಂ:** **080-22660000 / 080-22221188**
* **ವಾಟ್ಸಾಪ್ ದೂರು:** **9480685700**
* **ಬೆಸ್ಕಾಂ ಸಹಾಯವಾಣಿ (ವಿದ್ಯುತ್ ತಂತಿಗೆ ತಾಗಿದ್ದರೆ):** **1912**

---

### 🪓 ರೆಂಬೆ ಕತ್ತರಿಸುವ ನಿಯಮಗಳು:
ನಿಮ್ಮ ಮನೆ ಮುಂಭಾಗದ ರಸ್ತೆ ಮರದ ರೆಂಬೆಗಳು ಅಪಾಯಕಾರಿಯಾಗಿದ್ದರೆ, ಸ್ಥಳೀಯ ವಾರ್ಡ್ ಅರಣ್ಯಾಧಿಕಾರಿಗೆ (DCF/RFO BBMP) ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಸಿದರೆ ಪಾಲಿಕೆ ಸಿಬ್ಬಂದಿಯೇ ಬಂದು ಉಚಿತವಾಗಿ ರೆಂಬೆಗಳನ್ನು ಕತ್ತರಿಸಿ ತೆರವು ಮಾಡುತ್ತಾರೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bbmp.gov.in",
        "keywords": "bbmp tree trimming request, dangerous tree fall complaint bangalore, bbmp forest cell, ಮರ ಬಿದ್ದಾಗ ದೂರು, ಬಿಬಿಎಂಪಿ ಅರಣ್ಯ ವಿಭಾಗ",
        "action_label": "🌳 BBMP ಕಂಟ್ರೋಲ್ ರೂಂ",
        "action_url": "https://bbmp.gov.in"
    },
    {
        "id": "faq_blr_279",
        "question": "ಬೆಂಗಳೂರಿನಲ್ಲಿ ಖಾಸಗಿ ವಾಟರ್ ಟ್ಯಾಂಕರ್ ದರ ನಿಯಂತ್ರಣ (Water Tanker Price Cap) ಮತ್ತು ದೂರು ಸಹಾಯವಾಣಿ ಯಾವುದು?",
        "normalized_question": "bangalore water tanker price cap complaint dc bengaluru urban bwssb ವಾಟರ್ ಟ್ಯಾಂಕರ್ ದರ ನಿಯಂತ್ರಣ",
        "answer": """### 💧 ಬೆಂಗಳೂರು ಖಾಸಗಿ ವಾಟರ್ ಟ್ಯಾಂಕರ್ ದರ ನಿಯಂತ್ರಣ & ದೂರು ಪರಿಹಾರ

ಬೇಸಿಗೆಯಲ್ಲಿ ಅಥವಾ ನೀರಿನ ಕೊರತೆಯ ಸಂದರ್ಭದಲ್ಲಿ ಖಾಸಗಿ ವಾಟರ್ ಟ್ಯಾಂಕರ್ ಮಾಲೀಕರು ಅತಿಯಾದ ದರ ವಸೂಲಿ ಮಾಡುವುದನ್ನು ತಡೆಯಲು ಬೆಂಗಳೂರು ನಗರ ಜಿಲ್ಲಾಧಿಕಾರಿಗಳು ಗರಿಷ್ಠ ದರ ನಿಗದಿಪಡಿಸಿದ್ದಾರೆ.

---

### 💰 ಸರ್ಕಾರದ ಅಧಿಕೃತ ದರ ಮಿತಿ (Cap Rates):
* **6,000 ಲೀಟರ್ ಟ್ಯಾಂಕರ್ (5 ಕಿ.ಮೀ ವ್ಯಾಪ್ತಿಯೊಳಗೆ):** ಗರಿಷ್ಠ **₹600 ರಿಂದ ₹750**.
* **12,000 ಲೀಟರ್ ಟ್ಯಾಂಕರ್ (5 ಕಿ.ಮೀ ವ್ಯಾಪ್ತಿಯೊಳಗೆ):** ಗರಿಷ್ಠ **₹1,000 ರಿಂದ ₹1,200**.
* 5 ಕಿ.ಮೀ ಗಿಂತ ಹೆಚ್ಚಿನ ದೂರವಿದ್ದರೆ ಹೆಚ್ಚುವರಿ ₹50 ರಿಂದ ₹100 ಸಾರಿಗೆ ವೆಚ್ಚ.

---

### 📞 ಅಧಿಕ ದರ ವಸೂಲಿ ವಿರುದ್ಧ ದೂರು ನೀಡಲು:
ಟ್ಯಾಂಕರ್ ಮಾಲೀಕರು ನಿಗದಿತ ದರಕ್ಕಿಂತ ಹೆಚ್ಚು ಹಣ ಕೇಳಿದರೆ ಅಥವಾ ನೀರು ಪೂರೈಸಲು ನಿರಾಕರಿಸಿದರೆ **BWSSB ಕಾಲ್ ಸೆಂಟರ್: 1916** ಅಥವಾ ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಸಹಾಯವಾಣಿಗೆ ವಾಹನ ನೋಂದಣಿ ಸಂಖ್ಯೆ ಸಮೇತ ದೂರು ನೀಡಬಹುದು.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bwssb.karnataka.gov.in",
        "keywords": "bangalore water tanker rates, water tanker price cap dc urban, 1916 water complaint, ವಾಟರ್ ಟ್ಯಾಂಕರ್ ದರ, ಜಲಮಂಡಳಿ ದೂರು",
        "action_label": "💧 BWSSB ಸಹಾಯವಾಣಿ",
        "action_url": "https://bwssb.karnataka.gov.in"
    },
    {
        "id": "faq_blr_280",
        "question": "ಬಿಎಂಆರ್‌ಡಿಎ (BMRDA) ಅನುಮೋದಿತ ಬಡಾವಣೆಗಳನ್ನು ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ? ಗ್ರಾಮಠಾಣಾ ಸೈಟ್ ವಂಚನೆ ತಪ್ಪಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "bmrda layout approval verification gramathana site fraud prevention ಬಿಎಂಆರ್‌ಡಿಎ ಬಡಾವಣೆ ಪರಿಶೀಲನೆ",
        "answer": """### 📐 BMRDA / DTCP ಅನುಮೋದಿತ ಲೇಔಟ್ ಪರಿಶೀಲನೆ (Avoiding Illegal Layout Traps)

ಬೆಂಗಳೂರು ಹೊರವಲಯದಲ್ಲಿ (ಆನೇಕಲ್, ನೆಲಮಂಗಲ, ದೇವನಹಳ್ಳಿ, ಹೊಸಕೋಟೆ, ಮಾಗಡಿ) ಕೃಷಿ ಜಮೀನಿನಲ್ಲಿ ಅನಧಿಕೃತವಾಗಿ ನಿರ್ಮಿಸಿದ ಗ್ರಾಮಠಾಣಾ ಸೈಟುಗಳನ್ನು ಖರೀದಿಸಿ ವಂಚನೆಗೊಳಗಾಗುವುದನ್ನು ತಡೆಯುವ ಮಾರ್ಗಸೂಚಿ.

---

### ⚠️ ಕಾನೂನುಬದ್ಧ ನಿವೇಶನದ ಲಕ್ಷಣಗಳು:
1. **DC ಕನ್ವರ್ಶನ್ (Land Conversion):** ಜಮೀನು ಕೃಷಿಯಿಂದ ಕೃಷಿಯೇತರ (ವಸತಿ) ಉದ್ದೇಶಕ್ಕೆ ಪರಿವರ್ತನೆಯಾಗಿರಬೇಕು.
2. **BMRDA / BIAAPA / STRRPA ಅನುಮೋದನೆ:** ಯೋಜನಾ ಪ್ರಾಧಿಕಾರದಿಂದ ಅನುಮೋದಿತ ಬಡಾವಣೆ ನಕ್ಷೆ (Approved Layout Plan - LP No) ಇರಬೇಕು.
3. **ರೇರಾ ನೋಂದಣಿ (K-RERA Registered):** 500 ಚದರ ಮೀಟರ್‌ಗಿಂತ ಹೆಚ್ಚಿನ ಯಾವುದೇ ಬಡಾವಣೆ RERA ನೋಂದಣಿ ಹೊಂದಿರಲೇಬೇಕು.
4. ಕೇವಲ ಗ್ರಾಮ ಪಂಚಾಯಿತಿ 9/11 ಅಥವಾ ಕಚ್ಚಾ ಪತ್ರಗಳ ಮೇಲೆ ಸೈಟ್ ಖರೀದಿಸಿದರೆ ಭವಿಷ್ಯದಲ್ಲಿ ಬ್ಯಾಂಕ್ ಸಾಲ ಅಥವಾ ಕಟ್ಟಡ ನಿರ್ಮಾಣ ಪರವಾನಗಿ ಸಿಗುವುದಿಲ್ಲ.

🔗 **ಪರಿಶೀಲನಾ ಪೋರ್ಟಲ್:** [bmrda.karnataka.gov.in](https://bmrda.karnataka.gov.in)""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://bmrda.karnataka.gov.in",
        "keywords": "bmrda layout approval search, gramathana site risk, biaapa approved layout check, ಬಿಎಂಆರ್‌ಡಿಎ ಬಡಾವಣೆ, ಅನಧಿಕೃತ ಸೈಟ್ ವಂಚನೆ",
        "action_label": "📐 BMRDA ಪೋರ್ಟಲ್",
        "action_url": "https://bmrda.karnataka.gov.in"
    },
    {
        "id": "faq_blr_281",
        "question": "ಬೆಸ್ಕಾಂ 'EV ಮಿತ್ರ' (BESCOM EV Mitra App) ಮೂಲಕ ಬೆಂಗಳೂರಿನಲ್ಲಿ ಎಲೆಕ್ಟ್ರಿಕ್ ವಾಹನ ಚಾರ್ಜಿಂಗ್ ಸ್ಟೇಷನ್ ಹುಡುಕುವುದು ಹೇಗೆ?",
        "normalized_question": "bescom ev mitra app charging station locator bangalore rates ಬೆಸ್ಕಾಂ ಇವಿ ಮಿತ್ರ ಚಾರ್ಜಿಂಗ್ ಸ್ಟೇಷನ್",
        "answer": """### ⚡ ಬೆಸ್ಕಾಂ ಇವಿ ಮಿತ್ರ (BESCOM EV Mitra) — ಎಲೆಕ್ಟ್ರಿಕ್ ವಾಹನ ಚಾರ್ಜಿಂಗ್ ನೆಟ್‌ವರ್ಕ್

ಬೆಂಗಳೂರು ಮಹಾನಗರದಲ್ಲಿ ಎಲೆಕ್ಟ್ರಿಕ್ ಕಾರು, ಬೈಕ್ ಮತ್ತು ಆಟೋ ಚಾಲಕರಿಗೆ ಸಾರ್ವಜನಿಕ ಇವಿ ಚಾರ್ಜಿಂಗ್ ಸ್ಟೇಷನ್‌ಗಳನ್ನು ಹುಡುಕಲು ಮತ್ತು ಸ್ಲಾಟ್ ಬುಕ್ ಮಾಡಲು ಬೆಸ್ಕಾಂ ರೂಪಿಸಿರುವ ಆ್ಯಪ್.

---

### 📱 EV Mitra ಆ್ಯಪ್‌ನ ಪ್ರಮುಖ ಸೌಲಭ್ಯಗಳು:
* **ಲೈವ್ ಸ್ಟೇಷನ್ ಲೊಕೇಟರ್:** ನಿಮ್ಮ ಸಮೀಪದಲ್ಲಿರುವ ಬೆಸ್ಕಾಂ ಫಾಸ್ಟ್ ಚಾರ್ಜರ್ (CCS2 / CHAdeMO / AC Type 2) ಲೊಕೇಶನ್ ಮತ್ತು ಚಾರ್ಜರ್ ಲಭ್ಯತೆ (Available/Busy) ತಿಳಿಯಬಹುದು.
* **ಸ್ಲಾಟ್ ಬುಕಿಂಗ್ & ಪಾವತಿ:** ಸರದಿಯಲ್ಲಿ ನಿಲ್ಲದೆ ಮುಂಚಿತವಾಗಿ ಚಾರ್ಜಿಂಗ್ ಸ್ಲಾಟ್ ಬುಕ್ ಮಾಡಿ ಆನ್‌ಲೈನ್ ವಾಲೆಟ್ ಮೂಲಕ ಯೂನಿಟ್‌ಗೆ ತಕ್ಕಂತೆ ಪಾವತಿಸಬಹುದು.
* **ದರ:** ಖಾಸಗಿ ಚಾರ್ಜರ್‌ಗಳಿಗಿಂತ ಸರ್ಕಾರಿ ಬೆಸ್ಕಾಂ ಸ್ಟೇಷನ್‌ಗಳಲ್ಲಿ ಅತ್ಯಂತ ಕಡಿಮೆ ಯೂನಿಟ್ ದರದಲ್ಲಿ ವಿದ್ಯುತ್ ದೊರೆಯುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bescom.karnataka.gov.in",
        "keywords": "bescom ev mitra app, electric vehicle charging stations bangalore, ev fast charger slot booking, ಬೆಸ್ಕಾಂ ಇವಿ ಮಿತ್ರ, ಎಲೆಕ್ಟ್ರಿಕ್ ವಾಹನ ಚಾರ್ಜಿಂಗ್",
        "action_label": "⚡ ಬೆಸ್ಕಾಂ EV ಮಿತ್ರ",
        "action_url": "https://bescom.karnataka.gov.in"
    },
    {
        "id": "faq_blr_282",
        "question": "ಬೆಂಗಳೂರಿನಲ್ಲಿ ರಾಜಕಾಲುವೆ ಬಫರ್ ಝೋನ್ (Rajakaluve Buffer Zone) ನಿಯಮಗಳೇನು? ಆಸ್ತಿ ಖರೀದಿಗೆ ಮುನ್ನ ತಿಳಿಯುವುದು ಹೇಗೆ?",
        "normalized_question": "rajakaluve buffer zone rules ngt supreme court distance bangalore ರಾಜಕಾಲುವೆ ಬಫರ್ ಝೋನ್ ನಿಯಮ",
        "answer": """### 🌊 ಬೆಂಗಳೂರು ರಾಜಕಾಲುವೆ (Storm Water Drain) ಬಫರ್ ಝೋನ್ ನಿಯಮಗಳು

ನ್ಯಾಷನಲ್ ಗ್ರೀನ್ ಟ್ರಿಬ್ಯುನಲ್ (NGT) ಮತ್ತು ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ ಆದೇಶಗಳ ಅನ್ವಯ ಬೆಂಗಳೂರಿನಲ್ಲಿ ರಾಜಕಾಲುವೆಗಳ ಪಕ್ಕದಲ್ಲಿ ಯಾವುದೇ ನಿರ್ಮಾಣ ಮಾಡಬಾರದೆಂದು ಬಫರ್ ವಲಯ ನಿಗದಿಪಡಿಸಲಾಗಿದೆ.

---

### 📏 ರಾಜಕಾಲುವೆಯ ಶ್ರೇಣಿವಾರು ಅಂತರ (Buffer Distances):
1. **ಪ್ರಾಥಮಿಕ ರಾಜಕಾಲುವೆ (Primary Drain - Major Storm Drain):** ಕಾಲುವೆಯ ಎರಡೂ ಬದಿಯ ಗಡಿಯಿಂದ **50 ಮೀಟರ್** ವರೆಗೆ ಯಾವುದೇ ಕಟ್ಟಡ ನಿರ್ಮಾಣ ನಿಷೇಧ.
2. **ದ್ವಿತೀಯ ರಾಜಕಾಲುವೆ (Secondary Drain):** ಕಾಲುವೆಯ ಎರಡೂ ಬದಿಯಿಂದ **25 ಮೀಟರ್** ಬಫರ್ ಝೋನ್.
3. **ತೃತೀಯ ರಾಜಕಾಲುವೆ (Tertiary Drain / ಸಣ್ಣ ಚರಂಡಿ):** ಎರಡೂ ಬದಿಯಿಂದ **15 ಮೀಟರ್** ಬಫರ್ ಝೋನ್.
4. **ಕೆರೆಗಳ ಬಫರ್ ಝೋನ್ (Lake Buffer):** ಕೆರೆಯ ಪೂರ್ಣ ನೀರಿನ ಮಟ್ಟದ (FTL) ಗಡಿಯಿಂದ **30 ಮೀಟರ್** ವರೆಗೆ ಬಫರ್ ಝೋನ್.

💡 ಆಸ್ತಿ ಖರೀದಿಸುವ ಮುನ್ನ **ದಿಶಾಂಕ್ ಆ್ಯಪ್ (Dishank App)** ಮತ್ತು ಬಿಬಿಎಂಪಿ ರಾಜಕಾಲುವೆ ನಕ್ಷೆ ಪರಿಶೀಲಿಸಿ ಬಫರ್ ಝೋನ್ ವ್ಯಾಪ್ತಿಯಲ್ಲಿಲ್ಲ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://bbmp.gov.in",
        "keywords": "rajakaluve buffer zone rules, ngt storm water drain distance, lake buffer zone 30 meters, ರಾಜಕಾಲುವೆ ಬಫರ್ ಝೋನ್, ದಿಶಾಂಕ್ ನಕ್ಷೆ",
        "action_label": "🌊 ಬಿಬಿಎಂಪಿ ರಾಜಕಾಲುವೆ ನಕ್ಷೆ",
        "action_url": "https://bbmp.gov.in"
    },
    {
        "id": "faq_blr_283",
        "question": "ನಮ್ಮ ಮೆಟ್ರೋ ವಿಮಾನ ನಿಲ್ದಾಣ ಮಾರ್ಗ (Blue Line Airport Metro) ಯಾವಾಗ ಪೂರ್ಣಗೊಳ್ಳಲಿದೆ? ನಿಲ್ದಾಣಗಳು ಯಾವುವು?",
        "normalized_question": "namma metro blue line airport silk board to kia stations kr puram hebbal ಬ್ಲೂ ಲೈನ್ ಏರ್‌ಪೋರ್ಟ್ ಮೆಟ್ರೋ",
        "answer": """### ✈️ ನಮ್ಮ ಮೆಟ್ರೋ ನೀಲಿ ಮಾರ್ಗ (Blue Line — Phase 2A & 2B Airport Line)

ಸೆಂಟ್ರಲ್ ಸಿಲ್ಕ್ ಬೋರ್ಡ್‌ನಿಂದ ಕೆಂಪೇಗೌಡ ಅಂತಾರಾಷ್ಟ್ರೀಯ ವಿಮಾನ ನಿಲ್ದಾಣದವರೆಗೆ 58.19 ಕಿ.ಮೀ ಉದ್ದದ ಮೆಗಾ ಮೆಟ್ರೋ ಕಾರಿಡಾರ್.

---

### 🗺️ 2 ಹಂತಗಳ ವಿವರ:
* **Phase 2A (ORR Line):** ಸಿಲ್ಕ್ ಬೋರ್ಡ್‌ನಿಂದ ಕೆ.ಆರ್. ಪುರಂ ವರೆಗೆ (ಔಟರ್ ರಿಂಗ್ ರೋಡ್ ಟೆಕ್ ಪಾರ್ಕ್‌ಗಳು - HSR Layout, Bellandur, Marathahalli, Mahadevapura).
* **Phase 2B (Airport Line):** ಕೆ.ಆರ್. ಪುರಂ ನಿಂದ ಹೆಬ್ಬಾಳ, ಯಲಹಂಕ, ಜಕ್ಕೂರು ಮಾರ್ಗವಾಗಿ ವಿಮಾನ ನಿಲ್ದಾಣದ (KIA Terminal) ವರೆಗೆ.

---

### 🚆 ಪ್ರಮುಖ ಇಂಟರ್‌ಚೇಂಜ್ ಹಬ್‌ಗಳು:
* **ಸಿಲ್ಕ್ ಬೋರ್ಡ್:** ಹಳದಿ ಮಾರ್ಗ ಮತ್ತು ನೀಲಿ ಮಾರ್ಗ ಸಂಧಿಸುವ ಸ್ಥಳ.
* **ಕೆ.ಆರ್. ಪುರಂ:** ನೇರಳೆ ಮಾರ್ಗ (Purple Line) ಮತ್ತು ನೀಲಿ ಮಾರ್ಗದ ಸಂಪರ್ಕ.
* **ಹೆಬ್ಬಾಳ:** ಉಪನಗರ ರೈಲು, ಬಸ್ ಮತ್ತು ಮೆಟ್ರೋ ಸಂಪರ್ಕ ಕಲ್ಪಿಸುವ ಪ್ರಮುಖ ಜಂಕ್ಷನ್.""",
        "category": "TRANSIT",
        "language": "kn",
        "source_url": "https://english.bmrc.co.in",
        "keywords": "blue line airport metro bangalore, silk board to kr puram orr metro, hebbal yelahanka metro station, ಏರ್‌ಪೋರ್ಟ್ ಮೆಟ್ರೋ ಬ್ಲೂ ಲೈನ್, ಬಿಎಂಆರ್‌ಸಿಎಲ್",
        "action_label": "✈️ BMRCL ಬ್ಲೂ ಲೈನ್",
        "action_url": "https://english.bmrc.co.in"
    },
    {
        "id": "faq_blr_284",
        "question": "ಸಾರ್ವಜನಿಕ ಸ್ಥಳಗಳಲ್ಲಿ ಅನಧಿಕೃತ ಫ್ಲೆಕ್ಸ್, ಬ್ಯಾನರ್ ಹಾಕಿದರೆ BBMP ದೂರು ನೀಡುವುದು ಹೇಗೆ? ದಂಡ ಮತ್ತು ಶಿಕ್ಷೆ ಏನು?",
        "normalized_question": "illegal flex banner complaint bbmp high court penalty 50000 ksp ಅನಧಿಕೃತ ಫ್ಲೆಕ್ಸ್ ಬ್ಯಾನರ್ ದೂರು",
        "answer": """### 🚫 ಅನಧಿಕೃತ ಫ್ಲೆಕ್ಸ್, ಬ್ಯಾನರ್ ಮತ್ತು ಹೋರ್ಡಿಂಗ್ ನಿಷೇಧ ನಿಯಮಗಳು (BBMP Flex Ban)

ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ ಕಟ್ಟುನಿಟ್ಟಿನ ಆದೇಶದಂತೆ ಬೆಂಗಳೂರು ನಗರದಲ್ಲಿ ರಾಜಕೀಯ, ಜನ್ಮದಿನ ಅಥವಾ ವಾಣಿಜ್ಯ ಜಾಹೀರಾತುಗಳ ಯಾವುದೇ ಅನಧಿಕೃತ ಫ್ಲೆಕ್ಸ್ ಅಥವಾ ಬ್ಯಾನರ್ ಕಟ್ಟುವುದು ಸಂಪೂರ್ಣ ನಿಷೇಧಿಸಲಾಗಿದೆ.

---

### ⚠️ ಕಾನೂನು ಕ್ರಮ ಮತ್ತು ದಂಡ:
* **ಕರ್ನಾಟಕ ಮುನಿಸಿಪಲ್ ಕಾರ್ಪೊರೇಷನ್ ಕಾಯ್ದೆ ಕಲಂ 135:** ಅನಧಿಕೃತ ಬ್ಯಾನರ್ ಹಾಕಿದ ವ್ಯಕ್ತಿ ಮತ್ತು ಪ್ರಿಂಟರ್ ವಿರುದ್ಧ ಎಫ್‌ಐಆರ್ ದಾಖಲಾಗುತ್ತದೆ.
* **ದಂಡ & ಶಿಕ್ಷೆ:** ಪ್ರತಿ ಬ್ಯಾನರ್‌ಗೆ ಗರಿಷ್ಠ **₹50,000 ದಂಡ** ಮತ್ತು **6 ತಿಂಗಳವರೆಗೆ ಜೈಲು ಶಿಕ್ಷೆ**.

---

### 📞 ಸಾರ್ವಜನಿಕರು ದೂರು ನೀಡಲು:
ರಸ್ತೆ, ವಿದ್ಯುತ್ ಕಂಬ ಅಥವಾ ಪಾದಚಾರಿ ಮಾರ್ಗದಲ್ಲಿ ಬ್ಯಾನರ್ ಕಂಡುಬಂದಲ್ಲಿ **BBMP ಕಂಟ್ರೋಲ್ ರೂಂ: 080-22660000** ಅಥವಾ **112** ಗೆ ಕರೆ ಮಾಡಿ ಫೋಟೋ ಸಮೇತ ದೂರು ನೀಡಬಹುದು.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bbmp.gov.in",
        "keywords": "illegal flex banner complaint bbmp, flex ban high court bangalore penalty 50000, ಅನಧಿಕೃತ ಫ್ಲೆಕ್ಸ್ ದೂರು, ಬಿಬಿಎಂಪಿ ಬ್ಯಾನರ್ ನಿಷೇಧ",
        "action_label": "🚫 BBMP ದೂರು ಪೋರ್ಟಲ್",
        "action_url": "https://bbmp.gov.in"
    },
    {
        "id": "faq_blr_285",
        "question": "ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಆಡಳಿತ ಕಾಯ್ದೆ (Greater Bengaluru Governance Act - GBA) ಮತ್ತು ಪಾಲಿಕೆಗಳ ಪುನರ್ವಿಂಗಡಣೆ ಎಂದರೇನು?",
        "normalized_question": "greater bengaluru governance act gba restructuring bbmp multiple city corporations ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಪ್ರಾಧಿಕಾರ",
        "answer": """### 🏛️ ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಆಡಳಿತ ಕಾಯ್ದೆ (Greater Bengaluru Governance Act — GBA)

ಬೆಂಗಳೂರು ಮಹಾನಗರದ ತ್ವರಿತ ಬೆಳವಣಿಗೆ, ಸಂಚಾರ ದಟ್ಟಣೆ ಮತ್ತು ನಾಗರಿಕ ಸೇವೆಗಳನ್ನು ವಿಕೇಂದ್ರೀಕೃತಗೊಳಿಸಲು ಬಿಬಿಎಂಪಿಯನ್ನು ಮರುರಚನೆ ಮಾಡುವ ನೂತನ ಆಡಳಿತಾತ್ಮಕ ಚೌಕಟ್ಟು.

---

### 🌟 ಪ್ರಮುಖ ಮುಖ್ಯಾಂಶಗಳು:
1. **ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಪ್ರಾಧಿಕಾರ (GBA):** ಮುಖ್ಯಮಂತ್ರಿಗಳ ಅಧ್ಯಕ್ಷತೆಯಲ್ಲಿ ಇಡೀ ಮಹಾನಗರದ ಸಮಗ್ರ ಯೋಜನೆ, ಬಜೆಟ್ ಮತ್ತು ಮೆಟ್ರೋ-ಬಿಎಂಟಿಸಿ-ಜಲಮಂಡಳಿ ಸಮನ್ವಯಕ್ಕಾಗಿ ಉನ್ನತ ಮಟ್ಟದ ಪ್ರಾಧಿಕಾರ.
2. **ಬಹು ನಗರ ಪಾಲಿಕೆಗಳು (Multiple City Corporations):** ಬಿಬಿಎಂಪಿಯನ್ನು 3 ರಿಂದ 5 ಸಣ್ಣ ಸ್ವತಂತ್ರ ನಗರ ಪಾಲಿಕೆಗಳಾಗಿ ವಿಂಗಡಿಸಿ ಸ್ಥಳೀಯ ಮೇಯರ್ ಮತ್ತು ಆಯುಕ್ತರ ನೇತೃತ್ವದಲ್ಲಿ ತ್ವರಿತ ಸೇವೆ ಒದಗಿಸುವುದು.
3. **ವಾರ್ಡ್ ಸಮಿತಿಗಳ ಸಬಲೀಕರಣ:** ಪ್ರತಿ ವಾರ್ಡ್‌ನ ಸ್ಥಳೀಯ ರಸ್ತೆ, ಕಸ, ಬೀದಿದೀಪಗಳ ನಿರ್ವಹಣೆಗೆ ವಾರ್ಡ್ ಸಮಿತಿಗಳಿಗೆ ನೇರ ಆರ್ಥಿಕ ಅನುದಾನ.

🔗 **ನಗರಾಭಿವೃದ್ಧಿ ಇಲಾಖೆ:** [udd.karnataka.gov.in](https://udd.karnataka.gov.in)""",
        "category": "ADMIN",
        "language": "kn",
        "source_url": "https://udd.karnataka.gov.in",
        "keywords": "greater bengaluru governance act, gba bbmp restructuring, multiple corporations bangalore, ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಪ್ರಾಧಿಕಾರ, ಬಿಬಿಎಂಪಿ ಪುನರ್ವಿಂಗಡಣೆ",
        "action_label": "🏛️ ನಗರಾಭಿವೃದ್ಧಿ ಇಲಾಖೆ",
        "action_url": "https://udd.karnataka.gov.in"
    }
]

# =========================================================================
# 20. EXPANSION BATCH 12: NAMMA GUIDE CIVIC SERVICES & WORKFLOW SUITE
#     (Derived directly from Namma Guide Portal Architecture & Checklists)
# =========================================================================

NAMMAGUIDE_SCREENSHOTS_FAQS = [
    # -------------------------------------------------------------------------
    # MODULE 1: BBMP e-AASTHI, eKHATA CONVERSION & PROPERTY TAX
    # -------------------------------------------------------------------------
    {
        "id": "faq_ng_ekhata_001",
        "question": "ಬಿಬಿಎಂಪಿ ಎ-ಖಾತಾ (A Khata) ದಿಂದ ಡಿಜಿಟಲ್ ಇ-ಖಾತಾ (eKhata) ಗೆ ಪರಿವರ್ತನೆ ಮಾಡುವುದು ಹೇಗೆ? ಅಗತ್ಯ ದಾಖಲೆಗಳೇನು?",
        "normalized_question": "a khata to ekhata conversion online bbmp eaasthi portal steps documents ಎ-ಖಾತಾ ಇ-ಖಾತಾ ಪರಿವರ್ತನೆ",
        "answer": """### 🏢 ಬಿಬಿಎಂಪಿ ಎ-ಖಾತಾ ದಿಂದ ಡಿಜಿಟಲ್ ಇ-ಖಾತಾ (eKhata) ಪರಿವರ್ತನೆ ಮಾರ್ಗದರ್ಶಿ

ಬೆಂಗಳೂರು ಮಹಾನಗರ ಪಾಲಿಕೆ ವ್ಯಾಪ್ತಿಯ ಆಸ್ತಿಗಳ ನಕಲಿ ವಹಿವಾಟು ತಡೆಯಲು ಹಾಗೂ ಆಸ್ತಿ ನೋಂದಣಿಗೆ (Kaveri 2.0) ಕಡ್ಡಾಯವಾಗಿರುವ ಡಿಜಿಟಲ್ **e-Aasthi eKhata** ಪಡೆಯುವ ವಿಧಾನ:

---

### 📋 ಅಗತ್ಯವಿರುವ ಕಡ್ಡಾಯ ದಾಖಲೆಗಳು (Typical Documents):
1. **ಹಳೆಯ ಭೌತಿಕ ಎ-ಖಾತಾ ಪ್ರಮಾಣಪತ್ರ & ಖಾತಾ ಸಾರಾಂಶ (Previous Khata Certificate & Extract).**
2. **ನೋಂದಾಯಿತ ಕ್ರಯಪತ್ರ (Registered Sale Deed) / ಹಕ್ಕುಪತ್ರ / ವಿಭಾಗಪತ್ರ.**
3. **ಇತ್ತೀಚಿನ ಋಣಭಾರ ಪ್ರಮಾಣಪತ್ರ (Encumbrance Certificate - EC):** ಪ್ರಸ್ತುತ ದಿನಾಂಕದವರೆಗೆ ಆಸ್ತಿ ಮಾಲೀಕರ ಹೆಸರು ನಮೂದಾಗಿರಬೇಕು.
4. **ಇತ್ತೀಚಿನ ಆಸ್ತಿ ತೆರಿಗೆ ಪಾವತಿ ರಶೀದಿ (Tax Paid Receipt - SAS 10 Digit PID).**
5. **ಮಾಲೀಕರ ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ಪಾಸ್‌ಪೋರ್ಟ್ ಭಾವಚಿತ್ರ.**

---

### ⚠️ ಅರ್ಜಿ ಸಲ್ಲಿಸುವಾಗ ಮಾಡಬಾರದ ತಪ್ಪುಗಳು (Watch For):
* **ಮಸುಕಾದ ದಾಖಲೆಗಳ ಅಪ್‌ಲೋಡ್ (Blurry Uploads):** ಸ್ಕ್ಯಾನ್ ಪ್ರತಿಗಳು 200 DPI ಗಿಂತ ಹೆಚ್ಚು ಸ್ಪಷ್ಟತೆಯುಳ್ಳ PDF ಆಗಿರಬೇಕು.
* **ಹೆಸರು ಹೊಂದಾಣಿಕೆ ದೋಷ (Name Mismatch):** ಕ್ರಯಪತ್ರ, ಖಾತಾ ಮತ್ತು ಆಧಾರ್‌ನಲ್ಲಿ ಮಾಲೀಕರ ಹೆಸರು ಮತ್ತು ಇನಿಷಿಯಲ್ಸ್ ಒಂದೇ ರೀತಿ ಇರಬೇಕು.
* **ಹಳೆಯ ವಿವರಗಳ ಅಂಧ ನಂಬಿಕೆ:** ಹಳೆಯ ಕೈಬರಹದ ಖಾತಾದಲ್ಲಿದ್ದ ಅಳತೆ ಮತ್ತು ಪ್ರಸ್ತುತ ಕ್ರಯಪತ್ರದ ಅಳತೆ (Dimensions) ಸರಿಯಾಗಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ.

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಹಂತಗಳು:
1. [bbmpeaasthi.karnataka.gov.in](https://bbmpeaasthi.karnataka.gov.in) ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ.
2. ನಿಮ್ಮ 10 ಅಂಕಿಗಳ ಆಸ್ತಿ PID ಸಂಖ್ಯೆ ನಮೂದಿಸಿ ಆಸ್ತಿ ವಿವರ ಫೆಚ್ ಮಾಡಿ.
3. ಆಸ್ತಿಯ ಜಿಪಿಎಸ್ ಫೋಟೋ ಮತ್ತು ದಾಖಲೆಗಳನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
4. ಸಹಾಯಕ ಕಂದಾಯ ಅಧಿಕಾರಿ (ARO) ಪರಿಶೀಲಿಸಿ ಡಿಜಿಟಲ್ ಸಹಿ ಮಾಡಿದ eKhata PDF ನೀಡುತ್ತಾರೆ.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://bbmpeaasthi.karnataka.gov.in",
        "keywords": "a khata to ekhata conversion, bbmp eaasthi property, ec tax receipt khata, ಎ-ಖಾತಾ ಇ-ಖಾತಾ ಪರಿವರ್ತನೆ, ಬಿಬಿಎಂಪಿ ಇ-ಆಸ್ತಿ",
        "action_label": "🏢 BBMP e-Aasthi ಪೋರ್ಟಲ್",
        "action_url": "https://bbmpeaasthi.karnataka.gov.in"
    },
    {
        "id": "faq_ng_ekhata_002",
        "question": "ಹೊಸದಾಗಿ ಆಸ್ತಿ ಖರೀದಿಸಿದಾಗ ಹೊಸ ಇ-ಖಾತಾ (New Khata Registration) ಪಡೆಯುವುದು ಹೇಗೆ? ಚೈನ್ ಡಾಕ್ಯುಮೆಂಟ್ಸ್ ಎಂದರೇನು?",
        "normalized_question": "new khata guidance after property purchase chain of documents bbmp e aasthi ಹೊಸ ಇ-ಖಾತಾ ನೋಂದಣಿ",
        "answer": """### 📜 ಹೊಸ ಇ-ಖಾತಾ ನೋಂದಣಿ & ಚೈನ್ ಡಾಕ್ಯುಮೆಂಟ್ಸ್ (New Khata Guidance)

ಹೊಸ ಮನೆ, ಫ್ಲಾಟ್ ಅಥವಾ ನಿವೇಶನ ಖರೀದಿಸಿದ ನಂತರ ಅಥವಾ ಪಿತ್ರಾರ್ಜಿತವಾಗಿ ಆಸ್ತಿ ಬಂದಾಗ ಮೊದಲ ಬಾರಿಗೆ ಬಿಬಿಎಂಪಿ/ಪಾಲಿಕೆ ದಾಖಲೆಯಲ್ಲಿ ಖಾತೆ ಸೃಷ್ಟಿಸುವ ಪ್ರಕ್ರಿಯೆ.

---

### 🔗 ಚೈನ್ ಡಾಕ್ಯುಮೆಂಟ್ಸ್ (Chain of Documents) ಮಹತ್ವ:
* ಆಸ್ತಿಯ ಮೊದಲ ಮಾಲೀಕರಿಂದ ಹಿಡಿದು ಇಂದಿನ ಮಾರಾಟಗಾರರವರೆಗಿನ ಎಲ್ಲಾ ಹಿಂದಿನ ನೋಂದಾಯಿತ ಕ್ರಯಪತ್ರಗಳು (Mother Deeds / Prior Deeds).
* ಚೈನ್ ಡಾಕ್ಯುಮೆಂಟ್ ಇಲ್ಲದಿದ್ದರೆ ಅಥವಾ ನಡುವೆ ಯಾವುದೇ ಲಿಂಕ್ ಕಡಿದುಹೋಗಿದ್ದರೆ ಖಾತಾ ಅರ್ಜಿ ತಿರಸ್ಕೃತಗೊಳ್ಳುತ್ತದೆ.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳ ಪಟ್ಟಿ:
* ನೋಂದಾಯಿತ ಪ್ರಸ್ತುತ ಕ್ರಯಪತ್ರ (Latest Registered Sale Deed).
* ಕನಿಷ್ಠ 15 ರಿಂದ 30 ವರ್ಷಗಳ ಋಣಭಾರ ಪ್ರಮಾಣಪತ್ರ (Nil Encumbrance Certificate - Form 15).
* ಕಟ್ಟಡ ಸ್ವಾಧೀನ ಪ್ರಮಾಣಪತ್ರ (Possession Certificate / Occupancy Certificate for Flats).
* ಅನುಮೋದಿತ ಕಟ್ಟಡ ನಕ್ಷೆ (Sanctioned Plan) ಮತ್ತು ಭೂ-ಪರಿವರ್ತನೆ (DC Conversion) ಆದೇಶ.
* [bbmpeaasthi.karnataka.gov.in](https://bbmpeaasthi.karnataka.gov.in) ಮೂಲಕ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ 2% ಖಾತಾ ಶುಲ್ಕ ಪಾವತಿಸಿ ಹೊಸ ಇ-ಖಾತಾ ಪಡೆಯಬಹುದು.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://bbmpeaasthi.karnataka.gov.in",
        "keywords": "new khata registration, chain of documents property, occupancy certificate oc, ಹೊಸ ಇ-ಖಾತಾ ಅರ್ಜಿ, ಮದರ್ ಡೀಡ್",
        "action_label": "📜 ಹೊಸ ಖಾತಾ ಪೋರ್ಟಲ್",
        "action_url": "https://bbmpeaasthi.karnataka.gov.in"
    },
    {
        "id": "faq_ng_ekhata_003",
        "question": "ಇ-ಖಾತಾದಲ್ಲಿ ಮಾಲೀಕರ ಹೆಸರು ತಿದ್ದುಪಡಿ (eKhata Name Correction) ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "ekhata name correction spelling mismatch bbmp eaasthi aro office ಇ-ಖಾತಾ ಹೆಸರು ತಿದ್ದುಪಡಿ",
        "answer": """### ✏️ ಬಿಬಿಎಂಪಿ ಇ-ಖಾತಾ ಹೆಸರು & ಕಾಗುಣಿತ ತಿದ್ದುಪಡಿ (eKhata Name Correction)

ಇ-ಖಾತಾ ಪ್ರಮಾಣಪತ್ರದಲ್ಲಿ ಮಾಲೀಕರ ಹೆಸರು ತಪ್ಪಾಗಿ ಮುದ್ರಿತವಾಗಿದ್ದರೆ, ಇನಿಷಿಯಲ್ಸ್ ಬಿಟ್ಟುಹೋಗಿದ್ದರೆ ಅಥವಾ ಜಂಟಿ ಮಾಲೀಕರ ಹೆಸರು ಸೇರಿಸಬೇಕಿದ್ದರೆ ಅನುಸರಿಸಬೇಕಾದ ಕ್ರಮ:

---

### ⚠️ ಪೂರ್ವಭಾವಿ ಪರಿಶೀಲನೆ (Mismatch Mapping):
* ನಿಮ್ಮ ನೋಂದಾಯಿತ ಕ್ರಯಪತ್ರ (Sale Deed) ಮತ್ತು ಆಧಾರ್ ಕಾರ್ಡ್‌ನಲ್ಲಿರುವ ಹೆಸರನ್ನು ಇ-ಖಾತಾದಲ್ಲಿರುವ ಹೆಸರಿನೊಂದಿಗೆ ತಾಳೆ ನೋಡಿ (ಅಕ್ಷರ ದೋಷವನ್ನು ಗುರುತಿಸಿ).

---

### 📋 ಅಗತ್ಯವಿರುವ ಪೂರಕ ದಾಖಲೆಗಳು:
1. ಸರಿಪಡಿಸಲು ಕೋರಿದ ಮೂಲ ನೋಂದಾಯಿತ ಕ್ರಯಪತ್ರದ ಪ್ರತಿ.
2. ಗೆಜೆಟ್ ಅಧಿಸೂಚನೆ (ಹೆಸರು ಬದಲಾವಣೆ ಮಾಡಿಕೊಂಡಿದ್ದರೆ) ಅಥವಾ ನೋಟರಿ ಅಫಿಡವಿಟ್.
3. ಆಧಾರ್ ಕಾರ್ಡ್, ಪ್ಯಾನ್ ಕಾರ್ಡ್ ಮತ್ತು ಚಾಲ್ತಿ ಸಾಲಿನ ಆಸ್ತಿ ತೆರಿಗೆ ರಶೀದಿ.
4. ಇ-ಆಸ್ತಿ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ 'Correction in Khata' ಅಡಿಯಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ, ARO ಅನುಮೋದನೆಯ ನಂತರ ತಿದ್ದುಪಡಿ ಮಾಡಿದ ಇ-ಖಾತಾ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://bbmpeaasthi.karnataka.gov.in",
        "keywords": "ekhata name correction, spelling error in property tax, aro khata correction, ಇ-ಖಾತಾ ಹೆಸರು ತಿದ್ದುಪಡಿ, ಬಿಬಿಎಂಪಿ ಖಾತೆ",
        "action_label": "✏️ ಖಾತಾ ತಿದ್ದುಪಡಿ ಪೋರ್ಟಲ್",
        "action_url": "https://bbmpeaasthi.karnataka.gov.in"
    },
    {
        "id": "faq_ng_tax_004",
        "question": "ಬಿಬಿಎಂಪಿ ಆಸ್ತಿ ತೆರಿಗೆ (Property Tax) ಪಾವತಿಯಲ್ಲಿ PID ಸಂಖ್ಯೆ ಕಂಡುಹಿಡಿಯುವುದು ಮತ್ತು ಬಾಕಿ ತೆರಿಗೆ (Arrears) ಸರಿಪಡಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "bbmp property tax payment find 10 digit pid sas arrears receipt download ಬಿಬಿಎಂಪಿ ಆಸ್ತಿ ತೆರಿಗೆ ಪಿಐಡಿ",
        "answer": """### 💳 BBMP ಆಸ್ತಿ ತೆರಿಗೆ ಪಾವತಿ & PID ಮಾರ್ಗದರ್ಶಿ (Property Tax Advisory)

ಬೆಂಗಳೂರು ಮಹಾನಗರ ಪಾಲಿಕೆ ವ್ಯಾಪ್ತಿಯಲ್ಲಿ ಆಸ್ತಿ ತೆರಿಗೆಯನ್ನು SAS (Self Assessment Scheme) ಅಡಿಯಲ್ಲಿ ಪಾವತಿಸುವ ನಿಯಮಗಳು:

---

### 🔍 10 ಅಂಕಿಗಳ PID (Property Identification Number) ಹುಡುಕುವುದು ಹೇಗೆ?:
1. [bbmptax.karnataka.gov.in](https://bbmptax.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ.
2. **'Fetch PID'** ಆಯ್ಕೆಮಾಡಿ ನಿಮ್ಮ ವಾರ್ಡ್ ಸಂಖ್ಯೆ, ಹಳೆಯ 08-ಅಂಕಿಗಳ SAS ಅಪ್ಲಿಕೇಶನ್ ನಂಬರ್ ಅಥವಾ ಹಿಂದಿನ ತೆರಿಗೆ ರಶೀದಿಯ ಸಂಖ್ಯೆ ಹಾಕಿ ಹುಡುಕಿ.

---

### ⚠️ ತೆರಿಗೆ ಕಟ್ಟುವಾಗ ಎಚ್ಚರವಹಿಸಬೇಕಾದ ಅಂಶಗಳು:
* **ತಪ್ಪು PID ಬಳಕೆ ತಪ್ಪಿಸಿ:** ಪಕ್ಕದ ನಿವೇಶನದ ಅಥವಾ ಬೇರೆ ವಾರ್ಡ್‌ನ PID ಗೆ ತೆರಿಗೆ ಕಟ್ಟಬೇಡಿ.
* **ಬಾಕಿ ತೆರಿಗೆ (Arrears Penalty):** ಹಿಂದಿನ ವರ್ಷಗಳ ಬಾಕಿ ತೆರಿಗೆಯಿದ್ದರೆ ವಾರ್ಷಿಕ 2% ಬಡ್ಡಿ ಅನ್ವಯಿಸುತ್ತದೆ.
* **ರಶೀದಿ ಡೌನ್‌ಲೋಡ್:** ಹಣ ಪಾವತಿಯಾದ ತಕ್ಷಣ ಬ್ಯಾಂಕ್ ಟ್ರಾನ್ಸಾಕ್ಷನ್ ರೆಫರೆನ್ಸ್ ಇರುವ ಅಧಿಕೃತ **Receipt PDF** ಅನ್ನು ಕಡ್ಡಾಯವಾಗಿ ಕಂಪ್ಯೂಟರ್/ಮೊಬೈಲ್‌ನಲ್ಲಿ ಸುರಕ್ಷಿತವಾಗಿ ಸೇವ್ ಮಾಡಿಟ್ಟುಕೊಳ್ಳಿ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bbmptax.karnataka.gov.in",
        "keywords": "bbmp property tax payment, find 10 digit pid, sas property tax arrears, ಆಸ್ತಿ ತೆರಿಗೆ ಪಾವತಿ, ಬಿಬಿಎಂಪಿ ತೆರಿಗೆ ರಶೀದಿ",
        "action_label": "💳 BBMP ತೆರಿಗೆ ಪಾವತಿ",
        "action_url": "https://bbmptax.karnataka.gov.in"
    },

    # -------------------------------------------------------------------------
    # MODULE 2: BESCOM & BWSSB UTILITY TRANSFERS & COMPLAINTS
    # -------------------------------------------------------------------------
    {
        "id": "faq_ng_bescom_005",
        "question": "ಬೆಸ್ಕಾಂ (BESCOM) ವಿದ್ಯುತ್ ಬಿಲ್‌ನಲ್ಲಿ ಹೆಸರು ವರ್ಗಾವಣೆ (Name Transfer) ಮಾಡುವಾಗ ಗಮನಿಸಬೇಕಾದ ಅಂಶಗಳೇನು?",
        "normalized_question": "bescom name transfer guidance electricity bill ownership change noc account id ಬೆಸ್ಕಾಂ ಹೆಸರು ವರ್ಗಾವಣೆ",
        "answer": """### ⚡ ಬೆಸ್ಕಾಂ ವಿದ್ಯುತ್ ಮೀಟರ್ ಹೆಸರು ವರ್ಗಾವಣೆ ಮಾರ್ಗದರ್ಶಿ (BESCOM Name Transfer Guidance)

ಮನೆ ಖರೀದಿಸಿದ ನಂತರ ವಿದ್ಯುತ್ ಮೀಟರ್‌ನ ಖಾತೆದಾರರ ಹೆಸರನ್ನು (Account ID / Consumer ID) ಹೊಸ ಮಾಲೀಕರ ಹೆಸರಿಗೆ ಬದಲಾಯಿಸುವ ಪ್ರಕ್ರಿಯೆ:

---

### 📋 ಕಡ್ಡಾಯ ದಾಖಲೆಗಳ ಪಟ್ಟಿ (Typical Documents):
1. ಇತ್ತೀಚಿನ ವಿದ್ಯುತ್ ಬಿಲ್ ಪ್ರತಿ (ಶೂನ್ಯ ಬಾಕಿ / No Arrears Receipt).
2. ನೋಂದಾಯಿತ ಕ್ರಯಪತ್ರ (Registered Sale Deed) ಮತ್ತು ಇ-ಖಾತಾ ಪ್ರತಿ.
3. ಹಿಂದಿನ ಮಾಲೀಕರಿಂದ ನಿರಾಕ್ಷೇಪಣಾ ಪತ್ರ (**NOC - No Objection Certificate**) ಅಥವಾ ಹಿಂದಿನ ಮಾಲೀಕರು ಮೃತಪಟ್ಟಿದ್ದರೆ ಮರಣ ಪ್ರಮಾಣಪತ್ರ & ವಾರಸುದಾರಿಕೆ ದಾಖಲೆ.
4. ಹೊಸ ಮಾಲೀಕರ ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ಪಾಸ್‌ಪೋರ್ಟ್ ಫೋಟೋ.

---

### ⚠️ ಸಾಮಾನ್ಯ ದೋಷಗಳು (Watch For):
* **ತಪ್ಪು ಗ್ರಾಹಕ ಸಂಖ್ಯೆ (Wrong Consumer Number):** ಬಿಲ್‌ನಲ್ಲಿರುವ 10-ಅಂಕಿಗಳ Account ID ನಿಖರವಾಗಿರಬೇಕು.
* **ಸೆಕ್ಯುರಿಟಿ ಠೇವಣಿ ವರ್ಗಾವಣೆ (Transfer of MMD):** ಹಳೆಯ ಮಾಲೀಕರು ಪಾವತಿಸಿದ್ದ ಮೀಟರ್ ಸೆಕ್ಯುರಿಟಿ ಠೇವಣಿಯನ್ನು ಹೊಸ ಮಾಲೀಕರಿಗೆ ವರ್ಗಾಯಿಸಲು ಒಪ್ಪಿಗೆ ಪತ್ರ ಅಗತ್ಯ.
* [bescom.karnataka.gov.in](https://bescom.karnataka.gov.in) ನಲ್ಲಿ ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ₹100 ವರ್ಗಾವಣೆ ಶುಲ್ಕ ಪಾವತಿಸಿ ಪ್ರಕ್ರಿಯೆ ಮುಗಿಸಬಹುದು.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bescom.karnataka.gov.in",
        "keywords": "bescom name transfer guidance, meter ownership noc, transfer electricity bill, ಬೆಸ್ಕಾಂ ಹೆಸರು ವರ್ಗಾವಣೆ, ವಿದ್ಯುತ್ ಮೀಟರ್ ಎನ್‌ಒಸಿ",
        "action_label": "⚡ ಬೆಸ್ಕಾಂ ಪೋರ್ಟಲ್",
        "action_url": "https://bescom.karnataka.gov.in"
    },
    {
        "id": "faq_ng_bwssb_006",
        "question": "BWSSB ನೀರಿನ ಬಿಲ್‌ನಲ್ಲಿ ಮಾಲೀಕರ ಹೆಸರು ಬದಲಾವಣೆ ಮತ್ತು ಹೆಚ್ಚುವರಿ ಬಿಲ್ ದೂರು (Water Bill Guidance) ನೀಡುವುದು ಹೇಗೆ?",
        "normalized_question": "bwssb water bill name change rr number excess billing complaint sajala ಜಲಮಂಡಳಿ ನೀರಿನ ಬಿಲ್ ಹೆಸರು ಬದಲಾವಣೆ",
        "answer": """### 🚰 BWSSB ನೀರಿನ ಬಿಲ್ ಹೆಸರು ವರ್ಗಾವಣೆ & ದೂರು ನಿವಾರಣೆ (Water Bill Guidance)

ಬೆಂಗಳೂರು ಜಲ ಮಂಡಳಿಯ (BWSSB) ನೀರಿನ ಸಂಪರ್ಕದಲ್ಲಿ ಮಾಲೀಕತ್ವ ಬದಲಾವಣೆ ಹಾಗೂ ಬಿಲ್ಲಿಂಗ್ ದೂರುಗಳ ನಿರ್ವಹಣೆ:

---

### 📋 ಹೆಸರು ಬದಲಾವಣೆಗೆ ಅಗತ್ಯ ದಾಖಲೆಗಳು:
* ನೀರಿನ ಬಿಲ್‌ನಲ್ಲಿರುವ **RR Number (Revenue Register Number)**.
* ಆಸ್ತಿಯ BBMP ಇ-ಖಾತಾ ಮತ್ತು ನೋಂದಾಯಿತ ಕ್ರಯಪತ್ರದ ಪ್ರತಿ.
* ಇತ್ತೀಚಿನ ನೀರಿನ ಬಿಲ್ ಪಾವತಿ ರಶೀದಿ.
* ಮಾಲೀಕರ ಆಧಾರ್ ಕಾರ್ಡ್.

---

### ⚠️ ಬಿಲ್ ಪರಿಶೀಲನೆ & ದೂರು (Watch For):
* **ತಪ್ಪು RR ಸಂಖ್ಯೆ:** ಹಣ ಪಾವತಿಸುವಾಗ ನಿಮ್ಮದೇ ಕಟ್ಟಡದ RR ಸಂಖ್ಯೆ ಇದೆಯೇ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.
* **ಅತಿಯಾದ ಬಿಲ್ ಬಂದಾಗ:** ಮೀಟರ್ ರೀಡಿಂಗ್ ಫೋಟೋ ತೆಗೆದು [bwssb.karnataka.gov.in](https://bwssb.karnataka.gov.in) ನಲ್ಲಿ 'Grievance' ದಾಖಲಿಸಿ ಅಥವಾ **1916** ಸಹಾಯವಾಣಿಗೆ ಕರೆ ಮಾಡಿ ಮೀಟರ್ ತಪಾಸಣೆಗೆ ವಿನಂತಿಸಿ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bwssb.karnataka.gov.in",
        "keywords": "bwssb water bill name change, rr number correction, excess water bill complaint, ಜಲಮಂಡಳಿ ಹೆಸರು ಬದಲಾವಣೆ, ಆರ್‌ಆರ್ ನಂಬರ್",
        "action_label": "🚰 BWSSB Sajala ಪೋರ್ಟಲ್",
        "action_url": "https://bwssb.karnataka.gov.in"
    },

    # -------------------------------------------------------------------------
    # MODULE 3: PAN CARD, PROTEAN, INCOME TAX & AADHAAR LINKING
    # -------------------------------------------------------------------------
    {
        "id": "faq_ng_pan_007",
        "question": "ಪ್ರೋಟೀನ್ (Protean / NSDL) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಪ್ಯಾನ್ ಕಾರ್ಡ್ ತಿದ್ದುಪಡಿ (PAN Correction) ಮಾಡುವುದು ಹೇಗೆ? ಹೆಸರು ಮತ್ತು ಜನ್ಮದಿನಾಂಕ ಹೊಂದಾಣಿಕೆ ಹೇಗೆ?",
        "normalized_question": "protean pan card correction name mismatch dob update nsdl aadhaar linking ಪ್ಯಾನ್ ಕಾರ್ಡ್ ತಿದ್ದುಪಡಿ",
        "answer": """### 💳 ಪ್ರೋಟೀನ್ (Protean eGov / NSDL) ಪ್ಯಾನ್ ಕಾರ್ಡ್ ತಿದ್ದುಪಡಿ ಮಾರ್ಗದರ್ಶಿ

ಪ್ಯಾನ್ ಕಾರ್ಡ್‌ನಲ್ಲಿ ಹೆಸರು, ತಂದೆಯ ಹೆಸರು, ಜನ್ಮ ದಿನಾಂಕ ಅಥವಾ ಸಹಿ ತಪ್ಪಾಗಿದ್ದರೆ ಅಥವಾ ಆಧಾರ್ ಜೊತೆ ಲಿಂಕ್ ಆಗದಿದ್ದರೆ ಪ್ರೋಟೀನ್ ಪೋರ್ಟಲ್ ಮೂಲಕ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ತಿದ್ದುಪಡಿ ಮಾಡಬಹುದು.

---

### ⚠️ ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮುನ್ನ (Before You Apply):
* ನಿಮ್ಮ **ಆಧಾರ್ ಕಾರ್ಡ್‌ನಲ್ಲಿರುವ ಹೆಸರು ಮತ್ತು ಜನ್ಮ ದಿನಾಂಕ** ಹಾಗೂ ಪ್ಯಾನ್ ಕಾರ್ಡ್‌ನಲ್ಲಿ ನಮೂದಿಸಲಿರುವ ವಿವರಗಳು 100% ಹೊಂದಾಣಿಕೆಯಾಗಬೇಕು.
* ಅಕ್ಷರ ದೋಷವಿದ್ದರೆ (Spelling Mismatch) ಮೊದಲು ಆಧಾರ್ ತಿದ್ದುಪಡಿ ಮಾಡಿಸಿ ನಂತರ ಪ್ಯಾನ್ ತಿದ್ದುಪಡಿಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು (Typical Documents):
1. ಪ್ರಸ್ತುತ ಪ್ಯಾನ್ ಕಾರ್ಡ್ ಪ್ರತಿ (Existing PAN Copy).
2. ಆಧಾರ್ ಕಾರ್ಡ್ (ಹೆಸರು, ವಿಳಾಸ ಮತ್ತು ಜನ್ಮ ದಿನಾಂಕದ ಪುರಾವೆಯಾಗಿ).
3. ಪಾಸ್‌ಪೋರ್ಟ್ ಸೈಜ್ ಫೋಟೋ ಮತ್ತು ಡಿಜಿಟಲ್ ಸಹಿ.

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಹಂತಗಳು:
1. [protean-tinpan.com](https://www.protean-tinpan.com) ಗೆ ಭೇಟಿ ನೀಡಿ.
2. **'Changes or Correction in existing PAN data'** ಆಯ್ಕೆಮಾಡಿ.
3. ತಿದ್ದುಪಡಿ ಮಾಡಬೇಕಾದ ಬಾಕ್ಸ್ ಟಿಕ್ ಮಾಡಿ ಸರಿಯಾದ ವಿವರ ನಮೂದಿಸಿ.
4. e-KYC (Aadhaar OTP) ಮೂಲಕ ಕಾಗದರಹಿತವಾಗಿ ದೃಢೀಕರಿಸಿ ₹107 ಶುಲ್ಕ ಪಾವತಿಸಿ.
5. 10 ದಿನಗಳಲ್ಲಿ ಹೊಸ PVC ಪ್ಯಾನ್ ಕಾರ್ಡ್ ಮನೆಗೆ ಬರುತ್ತದೆ.""",
        "category": "CERTIFICATES",
        "language": "kn",
        "source_url": "https://www.protean-tinpan.com",
        "keywords": "protean pan services, pan card correction nsdl, pan aadhaar name mismatch, ಪ್ಯಾನ್ ಕಾರ್ಡ್ ತಿದ್ದುಪಡಿ, ಪ್ರೋಟೀನ್ ಪ್ಯಾನ್ ಸೇವೆ",
        "action_label": "💳 Protean PAN ಪೋರ್ಟಲ್",
        "action_url": "https://www.protean-tinpan.com"
    },

    # -------------------------------------------------------------------------
    # MODULE 4: EPFO, NPS TRUST & RETIREMENT SERVICES
    # -------------------------------------------------------------------------
    {
        "id": "faq_ng_epfo_008",
        "question": "ಇಪಿಎಫ್‌ಒ (EPFO) ಕ್ಲೇಮ್ ತಿರಸ್ಕೃತವಾಗುವುದನ್ನು ತಡೆಯುವುದು ಹೇಗೆ? ಯುಎಎನ್ (UAN) ಪ್ರೊಫೈಲ್ ಅಪ್‌ಡೇಟ್ ಹೇಗೆ?",
        "normalized_question": "epfo claim rejection reason uan member portal profile kyc name mismatch father name ಇಪಿಎಫ್ ಕ್ಲೇಮ್ ರಿಜೆಕ್ಟ್ ಪರಿಹಾರ",
        "answer": """### 💰 EPFO ಕ್ಲೇಮ್ ತಿರಸ್ಕೃತವಾಗುವುದನ್ನು ತಡೆಯುವ ಮಾರ್ಗದರ್ಶಿ (Unified Member Portal)

ಪಿಎಫ್ ಹಣ ಹಿಂಪಡೆಯುವಾಗ (Form 19, 10C, 31) ಕ್ಲೇಮ್ ರಿಜೆಕ್ಟ್ ಆಗುವುದನ್ನು ತಪ್ಪಿಸಲು UAN ಪ್ರೊಫೈಲ್ ಅನ್ನು ಸರಿಯಾಗಿ ಸಿದ್ಧಪಡಿಸಿಕೊಳ್ಳಬೇಕು.

---

### ⚠️ ಕ್ಲೇಮ್ ತಿರಸ್ಕೃತವಾಗಲು ಪ್ರಮುಖ 4 ಕಾರಣಗಳು (Watch For):
1. **ಬ್ಯಾಂಕ್ ವಿವರಗಳ ದೋಷ:** ಅಪ್‌ಲೋಡ್ ಮಾಡಿದ ಚೆಕ್ ಅಥವಾ ಪಾಸ್‌ಬುಕ್‌ನಲ್ಲಿ ಬ್ಯಾಂಕ್ ಹೆಸರು, IFSC ಕೋಡ್, ಖಾತೆ ಸಂಖ್ಯೆ ಮತ್ತು ಸದಸ್ಯರ ಹೆಸರು ಸ್ಪಷ್ಟವಾಗಿರದಿದ್ದರೆ (Blurry / Name not printed).
2. **ತಂದೆಯ ಹೆಸರು / ಜನ್ಮ ದಿನಾಂಕ ಹೊಂದಾಣಿಕೆ ಕೊರತೆ:** ಆಧಾರ್ ಮತ್ತು EPFO ದಾಖಲೆಯಲ್ಲಿ ಹೆಸರು ಅಥವಾ ತಂದೆಯ ಹೆಸರು ವ್ಯತ್ಯಾಸವಿದ್ದರೆ.
3. **ಸೇವಾ ವರ್ಗಾವಣೆ (Transfer) ಬಾಕಿ:** ಹಿಂದಿನ ಕಂಪನಿಯ PF ಹಣವನ್ನು ಪ್ರಸ್ತುತ ಕಂಪನಿಯ ಖಾತೆಗೆ ವರ್ಗಾಯಿಸದೆ (Annexure-K ಇಲ್ಲದೆ) ನೇರ ಕ್ಲೇಮ್ ಸಲ್ಲಿಸಿದಾಗ.
4. **Date of Exit ನಮೂದಿಸದಿರುವುದು:** ಕಂಪನಿ ಬಿಟ್ಟ ದಿನಾಂಕವನ್ನು ಉದ್ಯೋಗದಾತರು ಅಪ್‌ಡೇಟ್ ಮಾಡಿರದಿದ್ದರೆ.

---

### 🛠️ ಪರಿಹಾರ ಹಂತಗಳು:
* [unifiedportal-mem.epfindia.gov.in](https://unifiedportal-mem.epfindia.gov.in) ನಲ್ಲಿ 'Joint Declaration (JD Form)' ಮೂಲಕ ಹೆಸರು/ತಂದೆಯ ಹೆಸರು ಆನ್‌ಲೈನ್‌ನಲ್ಲೇ ತಿದ್ದಿ ಕ್ಲೇಮ್ ಸಲ್ಲಿಸಿ.""",
        "category": "LABOUR",
        "language": "kn",
        "source_url": "https://unifiedportal-mem.epfindia.gov.in",
        "keywords": "epfo claim rejection reasons, uan joint declaration form, epfo bank kyc attestation, ಇಪಿಎಫ್ ಕ್ಲೇಮ್ ರಿಜೆಕ್ಟ್, ಯುಎಎನ್ ಪ್ರೊಫೈಲ್",
        "action_label": "💰 EPFO ಸದಸ್ಯ ಪೋರ್ಟಲ್",
        "action_url": "https://unifiedportal-mem.epfindia.gov.in"
    },
    {
        "id": "faq_ng_nps_009",
        "question": "ರಾಷ್ಟ್ರೀಯ ಪಿಂಚಣಿ ವ್ಯವಸ್ಥೆ (NPS Trust) ಖಾತೆಯಿಂದ ಭಾಗಶಃ ಹಿಂಪಡೆಯುವಿಕೆ (Partial Withdrawal) ಮತ್ತು ಎಕ್ಸಿಟ್ ನಿಯಮಗಳೇನು?",
        "normalized_question": "nps trust national pension system pran partial withdrawal exit annuity guidelines ಎನ್‌ಪಿಎಸ್ ಟ್ರಸ್ಟ್ ಪಿಂಚಣಿ",
        "answer": """### 🏦 ರಾಷ್ಟ್ರೀಯ ಪಿಂಚಣಿ ವ್ಯವಸ್ಥೆ (NPS Trust) — ಹಿಂಪಡೆಯುವಿಕೆ & ಎಕ್ಸಿಟ್ ಮಾರ್ಗದರ್ಶಿ

NPS ಚಂದಾದಾರರು ತಮ್ಮ PRAN (Permanent Retirement Account Number) ಖಾತೆಯಲ್ಲಿರುವ ಹಣವನ್ನು ಹಿಂಪಡೆಯುವ ನಿಯಮಗಳು:

---

### 💰 1. ಭಾಗಶಃ ಹಿಂಪಡೆಯುವಿಕೆ (Partial Withdrawal Rules):
* ಕನಿಷ್ಠ **3 ವರ್ಷಗಳ ಚಂದಾದಾರಿಕೆ** ಪೂರ್ಣಗೊಂಡಿರಬೇಕು.
* ಚಂದಾದಾರರು ಸ್ವಂತವಾಗಿ ಕಟ್ಟಿದ ವಂತಿಕೆಯ (Own Contribution) **ಗರಿಷ್ಠ 25% ರಷ್ಟು ಹಣವನ್ನು ಮಾತ್ರ** ಮಕ್ಕಳ ಉನ್ನತ ಶಿಕ್ಷಣ, ಮದುವೆ, ಸ್ವಂತ ಮನೆ ಖರೀದಿ ಅಥವಾ ಗಂಭೀರ ಕಾಯಿಲೆಯ ಚಿಕಿತ್ಸೆಗಾಗಿ ಹಿಂಪಡೆಯಬಹುದು (ಸಂಪೂರ್ಣ ತೆರಿಗೆ ಮುಕ್ತ).

---

### 🚪 2. ನಿವೃತ್ತಿ / ಅಂತಿಮ ಎಕ್ಸಿಟ್ (Superannuation Exit at 60):
* ಒಟ್ಟು ಸಂಗ್ರಹವಾದ ಕಾರ್ಪಸ್‌ನಲ್ಲಿ ಕನಿಷ್ಠ **40% ಮೊತ್ತಕ್ಕೆ ಜೀವಿತಾವಧಿ ಪಿಂಚಣಿಗಾಗಿ ಆನ್ಯೂಟಿ (Annuity Plan)** ಖರೀದಿಸಬೇಕು.
* ಉಳಿದ **60% ಮೊತ್ತವನ್ನು ಏಕಗಂಟಿನಲ್ಲಿ ಸಂಪೂರ್ಣ ತೆರಿಗೆ ಮುಕ್ತವಾಗಿ (Lump sum Tax-Free)** ಹಿಂಪಡೆಯಬಹುದು.
* ಒಟ್ಟು ಕಾರ್ಪಸ್ ₹5 ಲಕ್ಷಕ್ಕಿಂತ ಕಡಿಮೆಯಿದ್ದರೆ ಸಂಪೂರ್ಣ 100% ಹಣವನ್ನು ಒಂದೇ ಬಾರಿಗೆ ಹಿಂಪಡೆಯಬಹುದು.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [npstrust.org.in](https://www.npstrust.org.in) | [cra-nsdl.com](https://www.cra-nsdl.com)""",
        "category": "WELFARE",
        "language": "kn",
        "source_url": "https://www.npstrust.org.in",
        "keywords": "nps trust partial withdrawal rules, pran exit annuity guidelines, nps 60 percent tax free, ಎನ್‌ಪಿಎಸ್ ಟ್ರಸ್ಟ್, ರಾಷ್ಟ್ರೀಯ ಪಿಂಚಣಿ",
        "action_label": "🏦 NPS Trust ಪೋರ್ಟಲ್",
        "action_url": "https://www.npstrust.org.in"
    },

    # -------------------------------------------------------------------------
    # MODULE 5: DIGILOCKER & GOVERNMENT PORTAL NAVIGATION
    # -------------------------------------------------------------------------
    {
        "id": "faq_ng_digi_010",
        "question": "ಡಿಜಿಲಾಕರ್‌ನಲ್ಲಿ (DigiLocker) ದಾಖಲೆಗಳನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡುವ ಬದಲು 'Fetch Issued Document' ಮಾಡುವುದು ಹೇಗೆ? ಕಾನೂನು ಮಾನ್ಯತೆ ಏನು?",
        "normalized_question": "digilocker fetch issued document vs upload legal validity it act 2000 டிಜಿಲಾಕರ್ ಅಧಿಕೃತ ದಾಖಲೆ",
        "answer": """### 📱 ಡಿಜಿಲಾಕರ್ (DigiLocker) — 'Fetch Issued Documents' ಬಳಕೆ & ಕಾನೂನು ಮಾನ್ಯತೆ

ಡಿಜಿಲಾಕರ್‌ನಲ್ಲಿ ಕೇವಲ ಫೋಟೋ ಸ್ಕ್ಯಾನ್ ಮಾಡಿ ಅಪ್‌ಲೋಡ್ (Upload) ಮಾಡಿದರೆ ಅದಕ್ಕೆ ಕಾನೂನು ಮಾನ್ಯತೆ ಇರುವುದಿಲ್ಲ; ಬದಲಿಗೆ ಸರ್ಕಾರದ ಇಲಾಖೆಗಳಿಂದ ನೇರವಾಗಿ **'Fetch Issued Document'** ಮಾಡಿಕೊಳ್ಳಬೇಕು.

---

### ⚖️ ಕಾನೂನು ಮಾನ್ಯತೆ (IT Act 2000 Rule 9A):
* ಮಾಹಿತಿ ತಂತ್ರಜ್ಞಾನ ಕಾಯ್ದೆಯನ್ವಯ, ಡಿಜಿಲಾಕರ್‌ನ 'Issued Documents' ವಿಭಾಗದಲ್ಲಿರುವ ಡಿಜಿಟಲ್ ಸಹಿಯುಳ್ಳ ದಾಖಲೆಗಳು ಮೂಲ ಭೌತಿಕ ದಾಖಲೆಗೆ ಸಮಾನ ಕಾನೂನು ಮಾನ್ಯತೆ ಹೊಂದಿವೆ (ಟ್ರಾಫಿಕ್ ಪೊಲೀಸರು, ವಿಮಾನ ನಿಲ್ದಾಣ ಮತ್ತು ಸರ್ಕಾರಿ ವೆರಿಫಿಕೇಶನ್‌ಗೆ ಮಾನ್ಯ).

---

### 🚀 ಸರಿಯಾಗಿ ದಾಖಲೆ ಫೆಚ್ ಮಾಡುವ ಹಂತಗಳು:
1. [digilocker.gov.in](https://digilocker.gov.in) ಅಥವಾ ಆ್ಯಪ್ ತೆರೆದು ಆಧಾರ್ ಮೂಲಕ ಲಾಗಿನ್ ಆಗಿ.
2. **'Search Documents'** ವಿಭಾಗಕ್ಕೆ ತೆರಳಿ ಸಂಬಂಧಪಟ್ಟ ಸಂಸ್ಥೆಯನ್ನು (ಉದಾ: Karnataka State Board, Transport Dept, Income Tax) ಹುಡುಕಿ.
3. ನಿಮ್ಮ ನೋಂದಣಿ ಸಂಖ್ಯೆ (Register No / Vehicle No / Roll No) ನಮೂದಿಸಿ **'Get Document'** ಕ್ಲಿಕ್ ಮಾಡಿ.
4. ಅಧಿಕೃತ ಡಿಜಿಟಲ್ ಕ್ಯೂಆರ್ ಕೋಡ್ ಇರುವ ಪ್ರಮಾಣಪತ್ರ ನೇರವಾಗಿ ನಿಮ್ಮ Issued Documents ಪಟ್ಟಿಗೆ ಸೇರ್ಪಡೆಯಾಗುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://digilocker.gov.in",
        "keywords": "digilocker fetch issued document, it act 2000 rule 9a validity, digilocker vs uploaded drive, ಡಿಜಿಲಾಕರ್ ಅಧಿಕೃತ ದಾಖಲೆ, ಇ-ದಾಖಲೆಗಳು",
        "action_label": "📱 ಡಿಜಿಲಾಕರ್ ಪ್ರವೇಶಿಸಿ",
        "action_url": "https://digilocker.gov.in"
    },
    {
        "id": "faq_ng_docs_011",
        "question": "ಸರ್ಕಾರಿ ಪೋರ್ಟಲ್‌ಗಳಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮುನ್ನ ದಾಖಲೆಗಳನ್ನು ಸರಿಯಾಗಿ ಸಿದ್ಧಪಡಿಸುವುದು (Documentation Assistance) ಹೇಗೆ?",
        "normalized_question": "government portal documentation assistance file format size upload errors ಸರ್ಕಾರಿ ಅರ್ಜಿ ದಾಖಲೆ ಸಿದ್ಧತೆ",
        "answer": """### 🗂️ ಸರ್ಕಾರಿ ಅರ್ಜಿಗಳ ದಾಖಲೆ ಸಿದ್ಧತೆ ಮಾರ್ಗದರ್ಶಿ (Documentation Readiness)

ಸೇವಾ ಸಿಂಧು, ನಾಡಕಚೇರಿ ಅಥವಾ ಪಾಸ್‌ಪೋರ್ಟ್ ಅರ್ಜಿಗಳು ಸಣ್ಣ ದಾಖಲಾತಿ ದೋಷಗಳಿಂದ ತಿರಸ್ಕೃತವಾಗುವುದನ್ನು ತಪ್ಪಿಸುವ ವಿಧಾನ:

---

### 📋 ಪರಿಶೀಲನಾ ಪಟ್ಟಿ (Document Inventory):
1. **ಕಡತದ ಹೆಸರು (Clear File Names):** ಫೈಲ್‌ಗಳಿಗೆ `Aadhaar_Front_Back.pdf`, `SaleDeed_Registered.pdf` ಎಂದು ಸ್ಪಷ್ಟವಾಗಿ ಹೆಸರಿಸಿ (`image1.jpg`, `doc.pdf` ಎಂದು ಇಡಬೇಡಿ).
2. **ಫೈಲ್ ಗಾತ್ರ & ಫಾರ್ಮ್ಯಾಟ್:** ಹೆಚ್ಚಿನ ಪೋರ್ಟಲ್‌ಗಳು 100 KB ಯಿಂದ 2 MB ವರೆಗಿನ PDF ಅಥವಾ JPEG ಫೈಲ್‌ಗಳನ್ನು ಮಾತ್ರ ಸ್ವೀಕರಿಸುತ್ತವೆ.
3. **ಮುಕ್ತಾಯ ದಿನಾಂಕ ಪರಿಶೀಲನೆ (Expired Proofs):** ವಾಹನ ವಿಮೆ, ಬಾಡಿಗೆ ಒಪ್ಪಂದ, ಅಥವಾ ಜಾತಿ-ಆದಾಯ ಪ್ರಮಾಣಪತ್ರದ ಮಾನ್ಯತೆಯ ಅವಧಿ ಮುಗಿದಿಲ್ಲ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.
4. **ಎರಡೂ ಬದಿಯ ಸ್ಕ್ಯಾನ್:** ಆಧಾರ್ ಮತ್ತು ವೋಟರ್ ಐಡಿಯ ಮುಂಭಾಗ ಮತ್ತು ಹಿಂಭಾಗ (ವಿಳಾಸವಿರುವ ಭಾಗ) ಎರಡನ್ನೂ ಒಂದೇ ಪುಟದಲ್ಲಿ ಸ್ಕ್ಯಾನ್ ಮಾಡಿ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://sevasindhu.karnataka.gov.in",
        "keywords": "government portal documentation assistance, pdf upload size format, avoid application rejection, ಸರ್ಕಾರಿ ಅರ್ಜಿ ದಾಖಲೆ ಸಿದ್ಧತೆ, ಫೈಲ್ ಅಪ್‌ಲೋಡ್",
        "action_label": "🗂️ ಸೇವಾ ಸಿಂಧು ಪೋರ್ಟಲ್",
        "action_url": "https://sevasindhu.karnataka.gov.in"
    },

    # -------------------------------------------------------------------------
    # MODULE 6: LPG GAS GRIEVANCE & DISTRIBUTOR ESCALATION
    # -------------------------------------------------------------------------
    {
        "id": "faq_ng_lpg_012",
        "question": "ಗ್ಯಾಸ್ ಸಿಲಿಂಡರ್ ವಿತರಕರು (LPG Distributor) ಹೆಚ್ಚು ಹಣ ಕೇಳಿದರೆ ಅಥವಾ ಸಬ್ಸಿಡಿ ಬಾರದಿದ್ದರೆ ದೂರು ನೀಡುವುದು ಹೇಗೆ?",
        "normalized_question": "lpg distributor complaint overcharging delivery subsidy confusion 1906 escalation ಗ್ಯಾಸ್ ಸಿಲಿಂಡರ್ ದೂರು",
        "answer": """### 🔥 ಎಲ್‌ಪಿಜಿ ಗ್ಯಾಸ್ ಸಿಲಿಂಡರ್ ದೂರು & ಸಬ್ಸಿಡಿ ಪರಿಹಾರ ಮಾರ್ಗದರ್ಶಿ

ಇಂಡೇನ್ (Indane), ಭಾರತ್ ಗ್ಯಾಸ್ (Bharatgas) ಅಥವಾ ಹೆಚ್‌ಪಿ ಗ್ಯಾಸ್ (HP Gas) ಏಜೆನ್ಸಿಗಳು ಡೆಲಿವರಿ ಶುಲ್ಕಕ್ಕಿಂತ ಹೆಚ್ಚು ಹಣ ಕೇಳಿದರೆ ಅಥವಾ DBT ಸಬ್ಸಿಡಿ ಬಾರದಿದ್ದರೆ ಕ್ರಮ ಕೈಗೊಳ್ಳುವ ವಿಧಾನ:

---

### ⚠️ ಸಾಮಾನ್ಯ ಸಮಸ್ಯೆಗಳು & ಎಚ್ಚರಿಕೆ:
* **ಅಧಿಕ ಡೆಲಿವರಿ ಶುಲ್ಕ ವಸೂಲಿ:** ಸಿಲಿಂಡರ್ ಬಿಲ್‌ನಲ್ಲಿ ನಮೂದಿಸಿದ ಮೊತ್ತಕ್ಕಿಂತ ಹೆಚ್ಚುವರಿಯಾಗಿ ₹30 ರಿಂದ ₹50 ಕೇಳುವುದು ಕಾನೂನುಬಾಹಿರ (ಡೆಲಿವರಿ ಚಾರ್ಜ್ ಬಿಲ್‌ನಲ್ಲೇ ಒಳಗೊಂಡಿರುತ್ತದೆ).
* **ಸಬ್ಸಿಡಿ ಗೊಂದಲ:** ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ Aadhaar e-KYC ಲಿಂಕ್ ಆಗಿರದಿದ್ದರೆ PMUY / PAHAL ಸಬ್ಸಿಡಿ ನಿಲ್ಲುತ್ತದೆ.

---

### 📞 ದೂರು ನೀಡುವ 3 ಹಂತಗಳ ವ್ಯವಸ್ಥೆ:
1. **ಕಂಪನಿ ಟೋಲ್-ಫ್ರೀ ದೂರು ಸಂಖ್ಯೆ:** **1800-2333-555** ಗೆ ಕರೆ ಮಾಡಿ ಕನ್ಸ್ಯೂಮರ್ ನಂಬರ್ ನೀಡಿ ದೂರು ದಾಖಲಿಸಿ.
2. **ಆನ್‌ಲೈನ್ ಪೋರ್ಟಲ್:** [mylpg.in](https://www.mylpg.in) ನಲ್ಲಿ ನಿಮ್ಮ ಗ್ಯಾಸ್ ಕಂಪನಿ ಆಯ್ಕೆಮಾಡಿ 'Feedback / Complaint' ಸಲ್ಲಿಸಿ.
3. **ತುರ್ತು ಗ್ಯಾಸ್ ಸೋರಿಕೆ ಸಹಾಯವಾಣಿ:** **1906** (24x7 Emergency Helpline).""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://www.mylpg.in",
        "keywords": "lpg cylinder overcharging complaint, lpg subsidy not credited, 1906 gas leakage helpline, ಗ್ಯಾಸ್ ಸಿಲಿಂಡರ್ ದೂರು, ಎಲ್‌ಪಿಜಿ ಸಬ್ಸಿಡಿ",
        "action_label": "🔥 MyLPG ಪೋರ್ಟಲ್",
        "action_url": "https://www.mylpg.in"
    },

    # -------------------------------------------------------------------------
    # MODULE 7: GRIEVANCE DRAFTING & ESCALATION FRAMEWORK
    # -------------------------------------------------------------------------
    {
        "id": "faq_ng_grievance_013",
        "question": "ಸರ್ಕಾರಿ ಇಲಾಖೆಗಳಿಗೆ ಪರಿಣಾಮಕಾರಿ ದೂರು ಪತ್ರ (Grievance Escalation Structure) ಬರೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "how to write structured government grievance complaint timeline evidence escalation ದೂರು ಪತ್ರ ಬರೆಯುವ ವಿಧಾನ",
        "answer": """### 📝 ಪರಿಣಾಮಕಾರಿ ಸರ್ಕಾರಿ ದೂರು ಪತ್ರ ರಚನೆ & ಹಂತ-ಹಂತದ ಮೇಲ್ಮನವಿ (Grievance Guidance)

ಸರ್ಕಾರಿ ಕಚೇರಿಗಳಲ್ಲಿ ಸಮಸ್ಯೆ ಬಗೆಹರಿಯದಿದ್ದಾಗ ಭಾವನಾತ್ಮಕವಾಗಿ ಅಸ್ಪಷ್ಟ ದೂರು ಬರೆಯುವ ಬದಲು, ಶಾಸನಬದ್ಧವಾಗಿ ಕ್ರಮ ಕೈಗೊಳ್ಳುವಂತೆ ಸಾಕ್ಷ್ಯಾಧಾರಿತ ದೂರು ರಚಿಸುವ ಚೌಕಟ್ಟು:

---

### 📋 ದೂರಿನ 4 ಕಡ್ಡಾಯ ಹಂತಗಳು (Chronological Structure):
1. **ದೂರಿನ ಸಾರಾಂಶ (Subject Line):** ಆಸ್ತಿ PID / ಅರ್ಜಿ ಸಂಖ್ಯೆ / ಖಾತೆ ಸಂಖ್ಯೆಯನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ವಿಷಯದಲ್ಲಿ ನಮೂದಿಸಿ.
2. **ಘಟನಾವಳಿಗಳ ಕಾಲಾನುಕ್ರಮ (Timeline Notes):**
   - *ಉದಾ: ದಿನಾಂಕ 10-01-2026 ರಂದು ಅರ್ಜಿ ಸಲ್ಲಿಸಲಾಯಿತು (Ack No: 12345).*
   - *ದಿನಾಂಕ 25-01-2026 ರಂದು ಸ್ಥಳ ಪರಿಶೀಲನೆ ಮುಗಿದರೂ ಯಾವುದೇ ಆದೇಶ ನೀಡಿಲ್ಲ.*
3. **ಸಾಕ್ಷ್ಯಾಧಾರಗಳ ಲಗತ್ತು (Evidence Attachment):** ಹಿಂದಿನ ಅರ್ಜಿ ರಶೀದಿ, ವಾಟ್ಸಾಪ್/ಇಮೇಲ್ ಸಂಭಾಷಣೆ, ಫೋಟೋಗಳು ಮತ್ತು ಪಾವತಿ ರಶೀದಿ.
4. **ಕೋರಿಕೆ (Specific Relief):** ನೀವು ಇಲಾಖೆಯಿಂದ ನಿಖರವಾಗಿ ಏನು ನಿರೀಕ್ಷಿಸುತ್ತಿದ್ದೀರಿ ಎಂಬುದನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ಬರೆಯಿರಿ.

---

### 🚀 ಹಂತ-ಹಂತದ ಮೇಲ್ಮನವಿ (Escalation Ladder):
* **ಹಂತ 1:** ಸ್ಥಳೀಯ ಅಧಿಕಾರಿ (ವಾರ್ಡ್ ಇಂಜಿನಿಯರ್ / ಗ್ರಾಮ ಆಡಳಿತಾಧಿಕಾರಿ).
* **ಹಂತ 2:** ಇಲಾಖಾ ಮುಖ್ಯಸ್ಥರು / ಆಯುಕ್ತರು (BBMP Commissioner / DC).
* **ಹಂತ 3:** ಮುಖ್ಯಮಂತ್ರಿಗಳ ಜನಸ್ಪಂದನ (1902) ಅಥವಾ ಸಕಾಲ ಮೇಲ್ಮನವಿ.""",
        "category": "ADMIN",
        "language": "kn",
        "source_url": "https://janaspandana.karnataka.gov.in",
        "keywords": "grievance escalation structure, how to write government complaint letter, sakala appeal timeline, ದೂರು ಪತ್ರ ಬರೆಯುವ ವಿಧಾನ, ಜನಸ್ಪಂದನ",
        "action_label": "📝 ಜನಸ್ಪಂದನ ದೂರು ಪೋರ್ಟಲ್",
        "action_url": "https://janaspandana.karnataka.gov.in"
    }
]

# =========================================================================
# 21. EXPANSION BATCH 13: NAMMA GUIDE DEEP-DIVE PROCEDURAL WORKFLOWS
# =========================================================================

NAMMAGUIDE_DEEP_DIVE_FAQS_BATCH_13 = [
    {
        "id": "faq_ng_pass_014",
        "question": "ಪಾಸ್‌ಪೋರ್ಟ್ (Passport Seva) ಅರ್ಜಿ ಸಲ್ಲಿಸುವಾಗ ವಿಳಾಸದ ಇತಿಹಾಸ (Address History) ಮತ್ತು ಪೊಲೀಸ್ ವೆರಿಫಿಕೇಶನ್ ತೊಂದರೆ ತಪ್ಪಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "passport application guidance normal tatkaal address history proof police verification ಪಾಸ್‌ಪೋರ್ಟ್ ಅರ್ಜಿ ಮಾರ್ಗದರ್ಶಿ",
        "answer": """### 🛂 ಪಾಸ್‌ಪೋರ್ಟ್ ಅರ್ಜಿ & ಪೊಲೀಸ್ ಪರಿಶೀಲನಾ ಸಮಗ್ರ ಮಾರ್ಗದರ್ಶಿ (Passport Guidance)

ಪಾಸ್‌ಪೋರ್ಟ್ ಸೇವಾ ಕೇಂದ್ರದಲ್ಲಿ (PSK) ಅರ್ಜಿ ಸಲ್ಲಿಸುವಾಗ ಸಣ್ಣ ದಾಖಲಾತಿ ದೋಷಗಳು ಅಥವಾ ವಿಳಾಸದ ಇತಿಹಾಸ ತಪ್ಪಾಗಿ ನಮೂದಿಸುವುದರಿಂದ ಅರ್ಜಿ ತಿರಸ್ಕೃತವಾಗುವುದನ್ನು ತಡೆಯುವ ವಿಧಾನ:

---

### ⚠️ ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ಮುನ್ನ ಪರಿಶೀಲಿಸಿ (Before You Apply):
* **ಕಳೆದ 1 ವರ್ಷದ ವಿಳಾಸದ ಇತಿಹಾಸ (Address History):** ನೀವು ಕಳೆದ 1 ವರ್ಷದಲ್ಲಿ ಒಂದಕ್ಕಿಂತ ಹೆಚ್ಚು ಸ್ಥಳಗಳಲ್ಲಿ/ಬಾಡಿಗೆ ಮನೆಯಲ್ಲಿ ವಾಸಿಸಿದ್ದರೆ, ಆ ಎಲ್ಲಾ ವಿಳಾಸಗಳನ್ನು ಅರ್ಜಿಯಲ್ಲಿ ಕಡ್ಡಾಯವಾಗಿ ನಮೂದಿಸಬೇಕು (ಮುಚ್ಚಿಟ್ಟರೆ ₹5,000 ದಂಡ ಮತ್ತು ವೆರಿಫಿಕೇಶನ್ ಫೇಲ್ ಆಗುತ್ತದೆ).
* **ದಾಖಲೆಗಳಲ್ಲಿ ಹೆಸರಿನ ಹೊಂದಾಣಿಕೆ:** ಆಧಾರ್ ಕಾರ್ಡ್, SSLC ಅಂಕಪಟ್ಟಿ ಮತ್ತು ಪ್ಯಾನ್ ಕಾರ್ಡ್‌ನಲ್ಲಿ ನಿಮ್ಮ ಹೆಸರು, ತಂದೆಯ ಹೆಸರು ಮತ್ತು ಜನ್ಮ ದಿನಾಂಕ ಒಂದೇ ರೀತಿ ಇರಬೇಕು.

---

### 📋 ಕಡ್ಡಾಯ ಮೂಲ ದಾಖಲೆಗಳು (Typical Documents Checklist):
1. **ವಿಳಾಸದ ಪುರಾವೆ (ಯಾವುದಾದರೂ 1 ಪ್ರಬಲ ದಾಖಲೆ):** ಆಧಾರ್ ಕಾರ್ಡ್ / ಸಕ್ರಿಯ ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ (ಫೋಟೋ ಮೇಲೆ ಮ್ಯಾನೇಜರ್ ಸಹಿ ಮತ್ತು ಸೀಲ್ ಇರಬೇಕು) / ವಿದ್ಯುತ್ ಬಿಲ್ / ನೋಂದಾಯಿತ ಬಾಡಿಗೆ ಒಪ್ಪಂದ (Registered Rental Agreement).
2. **ಜನ್ಮ ದಿನಾಂಕದ ಪುರಾವೆ:** ಜನನ ಪ್ರಮಾಣಪತ್ರ / SSLC ಅಂಕಪಟ್ಟಿ / ಪ್ಯಾನ್ ಕಾರ್ಡ್.
3. **ಶೈಕ್ಷಣಿಕ ಅರ್ಹತೆ (Non-ECR ಸ್ಟೇಟಸ್‌ಗೆ):** 10 ನೇ ತರಗತಿ ಅಥವಾ ಅದಕ್ಕಿಂತ ಹೆಚ್ಚಿನ ಪದವಿ ಅಂಕಪಟ್ಟಿ (ECNR ಮುದ್ರೆಗಾಗಿ).

---

### 🚀 ಪೊಲೀಸ್ ಪರಿಶೀಲನೆ (Police Verification) ಸುಲಭಗೊಳಿಸುವ ಹಂತಗಳು:
* PSK ಕೇಂದ್ರದ ಭೇಟಿ ಮುಗಿದ 3 ರಿಂದ 5 ದಿನಗಳಲ್ಲಿ ಸ್ಥಳೀಯ ಠಾಣೆಯಿಂದ ನಿಮ್ಮ ಮೊಬೈಲ್‌ಗೆ ಕರೆ ಬರುತ್ತದೆ.
* ನಿಮ್ಮೊಂದಿಗೆ ಇಬ್ಬರು ನೆರೆಹೊರೆಯವರ (Neighbours) ಹೆಸರು, ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಹಾಗೂ ಅವರ ಆಧಾರ್ ಜೆರಾಕ್ಸ್ ಪ್ರತಿಯನ್ನು ರೆಡಿ ಇಟ್ಟುಕೊಳ್ಳಿ.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [passportindia.gov.in](https://passportindia.gov.in) | **ಸಹಾಯವಾಣಿ:** 1800-258-1800""",
        "category": "PASSPORT",
        "language": "kn",
        "source_url": "https://passportindia.gov.in",
        "keywords": "passport application guidance, passport address history proof, psk tatkaal normal, non ecr documents, ಪಾಸ್‌ಪೋರ್ಟ್ ಅರ್ಜಿ ವಿಧಾನ, ಪೊಲೀಸ್ ವೆರಿಫಿಕೇಶನ್",
        "action_label": "🛂 ಪಾಸ್‌ಪೋರ್ಟ್ ಪೋರ್ಟಲ್",
        "action_url": "https://passportindia.gov.in"
    },
    {
        "id": "faq_ng_aadhaar_015",
        "question": "ಆಧಾರ್ ಕಾರ್ಡ್‌ನಲ್ಲಿ ಹೆಸರು, ಜನ್ಮದಿನಾಂಕ ತಿದ್ದುಪಡಿಯ ಮಿತಿಗಳು (UIDAI Update Limits) ಮತ್ತು ಪ್ರಮಾಣಿತ ಪ್ರಮಾಣಪತ್ರ (Standard Certificate) ಬಳಸುವುದು ಹೇಗೆ?",
        "normalized_question": "aadhaar update limits name dob gender standard certificate gazetted officer uidai ಆಧಾರ್ ತಿದ್ದುಪಡಿ ಮಿತಿಗಳು",
        "answer": """### 🪪 ಆಧಾರ್ ತಿದ್ದುಪಡಿ ಮಿತಿಗಳು & ಗೆಜೆಟೆಡ್ ಅಧಿಕಾರಿ ಪ್ರಮಾಣಪತ್ರ ಮಾರ್ಗದರ್ಶಿ

UIDAI ನಿಯಮಾವಳಿಗಳ ಪ್ರಕಾರ ಆಧಾರ್ ಕಾರ್ಡ್‌ನಲ್ಲಿರುವ ವಿವರಗಳನ್ನು ಜೀವನದಲ್ಲಿ ಇಂತಿಷ್ಟೇ ಬಾರಿ ತಿದ್ದುಪಡಿ ಮಾಡಲು ಕಟ್ಟುನಿಟ್ಟಾದ ಮಿತಿಗಳಿವೆ:

---

### 🛑 UIDAI ಅಧಿಕೃತ ತಿದ್ದುಪಡಿ ಮಿತಿಗಳು (Update Limits):
* **ಹೆಸರು (Name):** ಜೀವಿತಾವಧಿಯಲ್ಲಿ ಕೇವಲ **2 ಬಾರಿ ಮಾತ್ರ**.
* **ಜನ್ಮ ದಿನಾಂಕ (Date of Birth):** ಜೀವಿತಾವಧಿಯಲ್ಲಿ ಕೇವಲ **1 ಬಾರಿ ಮಾತ್ರ** (ಕೇವಲ ದೃಢೀಕೃತ ಜನನ ಪ್ರಮಾಣಪತ್ರ/SSLC ಮೂಲಕ).
* **ಲಿಂಗ (Gender):** ಜೀವಿತಾವಧಿಯಲ್ಲಿ ಕೇವಲ **1 ಬಾರಿ ಮಾತ್ರ**.
* **ವಿಳಾಸ ಮತ್ತು ಮೊಬೈಲ್ ಸಂಖ್ಯೆ:** ಎಷ್ಟು ಬಾರಿಯಾದರೂ ಅಗತ್ಯಕ್ಕೆ ತಕ್ಕಂತೆ ಬದಲಾಯಿಸಬಹುದು.

---

### 📑 ಮಾನ್ಯತೆ ಇರುವ ದಾಖಲೆ ಇಲ್ಲದಿದ್ದರೆ ಪರಿಹಾರ (Standard Certificate):
* ನಿಮ್ಮ ಬಳಿ ಯಾವುದೇ ವಿಳಾಸ ಅಥವಾ ಜನ್ಮ ದಿನಾಂಕದ ಅಧಿಕೃತ ದಾಖಲೆ ಇಲ್ಲದಿದ್ದರೆ, UIDAI ನ **'Standard Certificate by Gazetted Officer / MP / MLA / Tehsildar / Village Panchayat Head'** ಫಾರ್ಮ್ ಅನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ.
* ಫಾರ್ಮ್‌ನಲ್ಲಿ ಯಾವುದೇ ವೈಟ್ನರ್ ಅಥವಾ ತಿದ್ದುವಿಕೆ (Overwriting) ಇರಬಾರದು.
* ಗೆಜೆಟೆಡ್ ಅಧಿಕಾರಿಯ ಸಹಿ, ಕಚೇರಿ ಮೊಹರು (Official Seal) ಮತ್ತು ಫೋಟೋದ ಮೇಲೆ ಅರ್ಧ ಸಹಿ-ಮೊಹರು ಹಾಕಿಸಿ ಆಧಾರ್ ಸೇವಾ ಕೇಂದ್ರದಲ್ಲಿ ಸಲ್ಲಿಸಿ ಅಪ್‌ಡೇಟ್ ಮಾಡಬಹುದು.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [myaadhaar.uidai.gov.in](https://myaadhaar.uidai.gov.in)""",
        "category": "CERTIFICATES",
        "language": "kn",
        "source_url": "https://myaadhaar.uidai.gov.in",
        "keywords": "aadhaar update limit cross, standard certificate uidai format, gazetted officer signature aadhaar, ಆಧಾರ್ ತಿದ್ದುಪಡಿ ಮಿತಿ, ಗೆಜೆಟೆಡ್ ಅಧಿಕಾರಿ ಪ್ರಮಾಣಪತ್ರ",
        "action_label": "🪪 myAadhaar ಪೋರ್ಟಲ್",
        "action_url": "https://myaadhaar.uidai.gov.in"
    },
    {
        "id": "faq_ng_panlink_016",
        "question": "ಪ್ಯಾನ್-ಆಧಾರ್ ಲಿಂಕ್ ಆಗದಿದ್ದರೆ ₹1,000 ದಂಡದ ಚಲನ್ (Challan ITNS 280) ಕಟ್ಟಿ ಆಕ್ಟಿವೇಟ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "pan aadhaar link penalty 1000 challan itns 280 minor head 500 inoperative pan ಪ್ಯಾನ್ ಆಧಾರ್ ಲಿಂಕ್ ದಂಡ",
        "answer": """### 💳 ನಿಷ್ಕ್ರಿಯ ಪ್ಯಾನ್ ಆಕ್ಟಿವೇಟ್ ಮಾಡುವುದು & ₹1,000 ಚಲನ್ ಪಾವತಿ ವಿಧಾನ

ನಿಗದಿತ ದಿನಾಂಕದೊಳಗೆ ಆಧಾರ್ ಲಿಂಕ್ ಮಾಡದ ಕಾರಣ ನಿಮ್ಮ ಪ್ಯಾನ್ ಕಾರ್ಡ್ ನಿಷ್ಕ್ರಿಯವಾಗಿದ್ದರೆ (Inoperative PAN), ಆದಾಯ ತೆರಿಗೆ ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ₹1,000 ದಂಡ ಪಾವತಿಸಿ ಪುನಃ ಸಕ್ರಿಯಗೊಳಿಸಬಹುದು.

---

### ⚠️ ನಿಷ್ಕ್ರಿಯ ಪ್ಯಾನ್‌ನಿಂದಾಗುವ ನಷ್ಟಗಳು:
* ಬ್ಯಾಂಕ್ ಖಾತೆಯಿಂದ ₹50,000 ಕ್ಕಿಂತ ಹೆಚ್ಚು ವಹಿವಾಟು ನಡೆಸಲು ಸಾಧ್ಯವಾಗುವುದಿಲ್ಲ.
* ಯಾವುದೇ ಆದಾಯ ತೆರಿಗೆ ರಿಫಂಡ್ (ITR Refund) ಜಮೆಯಾಗುವುದಿಲ್ಲ ಮತ್ತು 20% ಹೆಚ್ಚಿನ TDS ಕಡಿತವಾಗುತ್ತದೆ.

---

### 💸 ₹1,000 ದಂಡ ಪಾವತಿಸಿ ಲಿಂಕ್ ಮಾಡುವ ಹಂತಗಳು:
1. [incometax.gov.in](https://www.incometax.gov.in) ನಲ್ಲಿ **'Link Aadhaar'** ಆಯ್ಕೆಮಾಡಿ.
2. ನಿಮ್ಮ ಪ್ಯಾನ್ ಮತ್ತು ಆಧಾರ್ ಸಂಖ್ಯೆ ಹಾಕಿ 'Continue to Pay Through e-Pay Tax' ಕ್ಲಿಕ್ ಮಾಡಿ.
3. **ಪ್ರಮುಖ ಆಯ್ಕೆಗಳು:**
   - **Tax Applicable:** Income Tax (Other than Companies) - 0021.
   - **Type of Payment:** *Other Receipts (Fee for delay in linking PAN with Aadhaar - 500)*.
4. ₹1,000 ಮೊತ್ತವನ್ನು UPI ಅಥವಾ ನೆಟ್ ಬ್ಯಾಂಕಿಂಗ್ ಮೂಲಕ ಪಾವತಿಸಿ.
5. ಪಾವತಿಯಾದ 24 ರಿಂದ 48 ಗಂಟೆಗಳ ನಂತರ ಪುನಃ 'Link Aadhaar' ಪುಟಕ್ಕೆ ತೆರಳಿ ಆಧಾರ್ ಒಟಿಪಿ ದೃಢೀಕರಿಸಿ ಲಿಂಕ್ ಪೂರ್ಣಗೊಳಿಸಿ.""",
        "category": "CERTIFICATES",
        "language": "kn",
        "source_url": "https://www.incometax.gov.in",
        "keywords": "pan aadhaar link penalty challan 500, inoperative pan activation, epay tax challan 280, ಪ್ಯಾನ್ ಆಧಾರ್ ಲಿಂಕ್ ದಂಡ 1000, ಆದಾಯ ತೆರಿಗೆ",
        "action_label": "💳 ಆದಾಯ ತೆರಿಗೆ ಪೋರ್ಟಲ್",
        "action_url": "https://www.incometax.gov.in"
    },
    {
        "id": "faq_ng_birth_late_017",
        "question": "1 ವರ್ಷ ಮೀರಿದ ಹಳೆಯ ಜನನ ಅಥವಾ ಮರಣ ಪ್ರಮಾಣಪತ್ರವನ್ನು (Delayed Registration Section 13) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "delayed birth death registration section 13 magistrate order tahsildar karnataka ವಿಳಂಬ ಜನನ ಮರಣ ನೋಂದಣಿ",
        "answer": """### 👶 ವಿಳಂಬ ಜನನ/ಮರಣ ನೋಂದಣಿ ಕಾಯ್ದೆ ಕಲಂ 13 (Delayed Registration under RBD Act 1969)

ಜನನ ಅಥವಾ ಮರಣ ಸಂಭವಿಸಿದ 1 ವರ್ಷದೊಳಗೆ ನೋಂದಣಿ ಮಾಡಿಸದಿದ್ದರೆ, ನೇರವಾಗಿ ಆಸ್ಪತ್ರೆ ಅಥವಾ ಪಾಲಿಕೆಯಿಂದ ಪ್ರಮಾಣಪತ್ರ ಸಿಗುವುದಿಲ್ಲ; ಕಂದಾಯ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಅವರ ಅನುಮತಿ ಆದೇಶ ಕಡ್ಡಾಯ.

---

### 📋 ಅಗತ್ಯವಿರುವ ದಾಖಲೆಗಳು (Case Type Mapping):
1. **ಲಭ್ಯವಿಲ್ಲದಿರುವ ಪ್ರಮಾಣಪತ್ರ (Non-Availability Certificate - NAC):** ಸ್ಥಳೀಯ ಗ್ರಾಮ ಪಂಚಾಯಿತಿ ಅಥವಾ ಬಿಬಿಎಂಪಿಯಿಂದ 'ದಾಖಲೆ ಲಭ್ಯವಿಲ್ಲ' ಎಂಬ ಹಿಂಬರಹ.
2. ಆಸ್ಪತ್ರೆಯ ಡಿಸ್ಚಾರ್ಜ್ ಬುಕ್ / ಜನನ ದಿನಚರಿ ಪ್ರತಿ ಅಥವಾ ಶಾಲಾ ಅಂಕಪಟ್ಟಿ.
3. ₹100 ರ ಇ-ಸ್ಟ್ಯಾಂಪ್‌ನಲ್ಲಿ ಸಿದ್ಧಪಡಿಸಿದ ನೋಟರಿ ಅಫಿಡವಿಟ್.
4. ಮೂವರು ನೆರೆಹೊರೆಯವರ ಸಾಕ್ಷ್ಯ ಪತ್ರ ಮತ್ತು ರೇಷನ್ ಕಾರ್ಡ್.

---

### 🏛️ ಪ್ರಕ್ರಿಯೆ:
* ಸೇವಾ ಸಿಂಧು ಅಥವಾ ನಾಡಕಚೇರಿ ಮೂಲಕ ತಾಲೂಕು ತಹಶೀಲ್ದಾರ್ / ಸಹಾಯಕ ಆಯುಕ್ತರ (AC Court) ಮುಂದೆ ಕಲಂ 13(3) ರ ಅಡಿಯಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.
* ಕಂದಾಯ ನಿರೀಕ್ಷಕರ ಸ್ಥಳ ವಿಚಾರಣೆ ಮತ್ತು ಪತ್ರಿಕಾ ಪ್ರಕಟಣೆಯ ನಂತರ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಆದೇಶ ಹೊರಡಿಸುತ್ತಾರೆ. ಈ ಆದೇಶದ ಆಧಾರದ ಮೇಲೆ e-JanMa ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಅಧಿಕೃತ ಪ್ರಮಾಣಪತ್ರ ಮುದ್ರಣವಾಗುತ್ತದೆ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://ejanma.karnataka.gov.in",
        "keywords": "delayed birth registration section 13, non availability certificate nac, magistrate order birth certificate, ವಿಳಂಬ ಜನನ ನೋಂದಣಿ, ತಹಶೀಲ್ದಾರ್ ಜನನ ಪ್ರಮಾಣಪತ್ರ",
        "action_label": "👶 e-JanMa ಪೋರ್ಟಲ್",
        "action_url": "https://ejanma.karnataka.gov.in"
    },
    {
        "id": "faq_ng_sevasindhu_018",
        "question": "ಸೇವಾ ಸಿಂಧು ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ ಅರ್ಜಿ ತಿರಸ್ಕೃತವಾದರೆ (Rejection Reasons) ಮೇಲ್ಮನವಿ ಸಲ್ಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "seva sindhu caste income certificate rejection reasons appeal assistant commissioner ಸೇವಾ ಸಿಂಧು ಅರ್ಜಿ ತಿರಸ್ಕಾರ ಪರಿಹಾರ",
        "answer": """### 📑 ಸೇವಾ ಸಿಂಧು ಜಾತಿ/ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ ತಿರಸ್ಕಾರ & ಮೇಲ್ಮನವಿ ಮಾರ್ಗದರ್ಶಿ

ನಾಡಕಚೇರಿ ಅಥವಾ ಸೇವಾ ಸಿಂಧು ಮೂಲಕ ಸಲ್ಲಿಸಿದ ಜಾತಿ, ಆದಾಯ ಅಥವಾ ವಾಸಸ್ಥಳ ಪ್ರಮಾಣಪತ್ರದ ಅರ್ಜಿ ತಿರಸ್ಕೃತಗೊಂಡರೆ (Rejected) ಕೈಗೊಳ್ಳಬೇಕಾದ ಪರಿಹಾರಗಳು:

---

### ⚠️ ಅರ್ಜಿ ತಿರಸ್ಕೃತವಾಗಲು ಪ್ರಮುಖ 3 ಕಾರಣಗಳು (Watch For):
1. **ತಪ್ಪು ಪ್ರವರ್ಗ ಆಯ್ಕೆ (Wrong Certificate Type):** ಉದಾಹರಣೆಗೆ 3A ಪ್ರವರ್ಗಕ್ಕೆ ಬದಲಾಗಿ 2A ಅಥವಾ ಸಾಮಾನ್ಯ ಜಾತಿ ಪ್ರಮಾಣಪತ್ರಕ್ಕೆ ಅರ್ಜಿ ಹಾಕುವುದು.
2. **ಅಸಮರ್ಪಕ ಶಾಲಾ ದಾಖಲೆ (Missing Supporting Proof):** ಶಾಲಾ ಟ್ರಾನ್ಸ್‌ಫರ್ ಸರ್ಟಿಫಿಕೇಟ್‌ನಲ್ಲಿ (TC) ಜಾತಿ ಸ್ಪಷ್ಟವಾಗಿ ನಮೂದಾಗಿರದಿದ್ದರೆ.
3. **ಭೂಹಿಡುವಳಿ ಮಿತಿ (Land Ceiling):** ಕೃಷಿ ಜಮೀನಿನ ಪಹಣಿಯಲ್ಲಿ ಆದಾಯದ ಮಿತಿ ಸರ್ಕಾರ ನಿಗದಿಪಡಿಸಿದ ಸೀಲಿಂಗ್‌ಗಿಂತ ಹೆಚ್ಚಿದ್ದಾಗ.

---

### ⚖️ ಮೇಲ್ಮನವಿ ಸಲ್ಲಿಸುವ ವಿಧಾನ (Appellate Authority):
* ತಹಶೀಲ್ದಾರ್ ತಿರಸ್ಕರಿಸಿದ ಆದೇಶದ ಪ್ರತಿಯೊಂದಿಗೆ **30 ದಿನಗಳ ಒಳಗಾಗಿ ಉಪವಿಭಾಗಾಧಿಕಾರಿಗಳಿಗೆ (Assistant Commissioner - AC Court)** ಮೇಲ್ಮನವಿ (Appeal) ಸಲ್ಲಿಸಬಹುದು.
* ಎಸಿ ನ್ಯಾಯಾಲಯವು ನಿಮ್ಮ ದಾಖಲೆಗಳನ್ನು ಮರುಪರಿಶೀಲಿಸಿ ಜಾತಿ/ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ ಮಂಜೂರು ಮಾಡಲು ತಹಶೀಲ್ದಾರ್‌ಗೆ ಆದೇಶಿಸುತ್ತದೆ.""",
        "category": "CERTIFICATES",
        "language": "kn",
        "source_url": "https://sevasindhu.karnataka.gov.in",
        "keywords": "caste certificate rejection reasons, appeal against tehsildar caste order, assistant commissioner appeal seva sindhu, ಜಾತಿ ಪ್ರಮಾಣಪತ್ರ ತಿರಸ್ಕಾರ, ಸೇವಾ ಸಿಂಧು ಮೇಲ್ಮನವಿ",
        "action_label": "📑 ಸೇವಾ ಸಿಂಧು ಪೋರ್ಟಲ್",
        "action_url": "https://sevasindhu.karnataka.gov.in"
    },
    {
        "id": "faq_ng_lpg_pahal_019",
        "question": "ಎಲ್‌ಪಿಜಿ ಗ್ಯಾಸ್ ಸಂಪರ್ಕವನ್ನು ಬೇರೆ ಏಜೆನ್ಸಿಗೆ ವರ್ಗಾವಣೆ (LPG Connection Transfer) ಮಾಡುವುದು ಮತ್ತು ಇ-ಕೆವೈಸಿ ಮಾಡಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "lpg gas connection transfer distributor mismatch ekyc indane bharatgas hp gas ಗ್ಯಾಸ್ ಏಜೆನ್ಸಿ ವರ್ಗಾವಣೆ",
        "answer": """### 🔥 ಎಲ್‌ಪಿಜಿ ಗ್ಯಾಸ್ ಏಜೆನ್ಸಿ ವರ್ಗಾವಣೆ & ಬಯೋಮೆಟ್ರಿಕ್ e-KYC (Gas Connection Guidance)

ಮನೆ ಬದಲಾಯಿಸಿದಾಗ ಅಥವಾ ಹಳೆಯ ವಿತರಕರ ಸೇವೆ ಸರಿಯಿಲ್ಲದಿದ್ದರೆ ಇಂಡೇನ್, ಭಾರತ್ ಗ್ಯಾಸ್ ಅಥವಾ ಹೆಚ್‌ಪಿ ಗ್ಯಾಸ್ ಸಂಪರ್ಕವನ್ನು ಬೇರೆ ಏಜೆನ್ಸಿಗೆ ವರ್ಗಾಯಿಸುವ ವಿಧಾನ:

---

### 🚚 1. ಒಂದೇ ನಗರದೊಳಗೆ ವರ್ಗಾವಣೆ (Transfer within Same City):
* ಹಳೆಯ ವಿತರಕರ ಬಳಿಗೆ ಹೋಗುವ ಅಗತ್ಯವಿಲ್ಲ; [mylpg.in](https://www.mylpg.in) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಅಥವಾ ಹೊಸ ವಿತರಕರ ಬಳಿಗೆ ತೆರಳಿ ನಿಮ್ಮ 17-ಅಂಕಿಗಳ LPG Consumer ID ಮತ್ತು ಹೊಸ ವಿಳಾಸದ ಪುರಾವೆ ನೀಡಿ **CTA (Customer Transfer Advice)** ಪಡೆಯಬಹುದು.

---

### 📦 2. ಬೇರೆ ಊರಿಗೆ ವರ್ಗಾವಣೆ (Transfer to Another District / City):
* ಹಳೆಯ ಏಜೆನ್ಸಿಗೆ ಸಿಲಿಂಡರ್ ಮತ್ತು ರೆಗ್ಯುಲೇಟರ್ ಒಪ್ಪಿಸಿ **SV (Subscription Voucher)** ಮತ್ತು **TTV (Transfer Termination Voucher)** ಪಡೆಯಿರಿ ಹಾಗೂ ನಿಮ್ಮ ಸೆಕ್ಯುರಿಟಿ ಠೇವಣಿ ಹಣವನ್ನು ವಾಪಸ್ ಪಡೆಯಿರಿ.
* ಹೊಸ ಊರಿನ ವಿತರಕರಿಗೆ ಈ TTV ರಶೀದಿ ನೀಡಿ ಹೊಸ ಸಿಲಿಂಡರ್ ಪಡೆಯಿರಿ.

---

### 📱 ಬಯೋಮೆಟ್ರಿಕ್ e-KYC ಪೂರ್ಣಗೊಳಿಸಲು:
* ಗ್ಯಾಸ್ ಸಬ್ಸಿಡಿ ನಿರಂತರವಾಗಿ ಬರಲು ನಿಮ್ಮ ಏಜೆನ್ಸಿಗೆ ಭೇಟಿ ನೀಡಿ ಫಿಂಗರ್‌ಪ್ರಿಂಟ್ ಅಥವಾ **IndianOil One / HP Pay App** ನಲ್ಲಿ ಫೇಸ್ ಅಥೆಂಟಿಕೇಷನ್ (Face Authentication) ಮೂಲಕ ಇ-ಕೆವೈಸಿ ಮಾಡಿಸಿ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://www.mylpg.in",
        "keywords": "lpg connection transfer online, ttv voucher gas agency, lpg face ekyc app, ಗ್ಯಾಸ್ ಸಂಪರ್ಕ ವರ್ಗಾವಣೆ, ಎಲ್‌ಪಿಜಿ ಇ-ಕೆವೈಸಿ",
        "action_label": "🔥 MyLPG ಪೋರ್ಟಲ್",
        "action_url": "https://www.mylpg.in"
    },
    {
        "id": "faq_ng_tax_zone_020",
        "question": "ಬಿಬಿಎಂಪಿ ಆಸ್ತಿ ತೆರಿಗೆ ವಲಯ ಮರುವಿಂಗಡಣೆ (BBMP SAS Zone Reclassification A to F) ಮತ್ತು ವಲಯ ವ್ಯತ್ಯಾಸ ದಂಡ ಸರಿಪಡಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "bbmp property tax zone reclassification zone a to f calculation excess penalty relief ಆಸ್ತಿ ತೆರಿಗೆ ವಲಯ ಮರುವಿಂಗಡಣೆ",
        "answer": """### 🏢 BBMP ಆಸ್ತಿ ತೆರಿಗೆ ವಲಯ ಮರುವಿಂಗಡಣೆ & ದಂಡ ನಿವಾರಣೆ (Zonal Guidance)

ಬೆಂಗಳೂರು ಮಹಾನಗರ ಪಾಲಿಕೆಯು ಮಾರ್ಗಸೂಚಿ ಮೌಲ್ಯದ (Guidance Value) ಆಧಾರದ ಮೇಲೆ ಆಸ್ತಿಗಳನ್ನು **Zone A ಯಿಂದ Zone F ವರೆಗೆ (6 ವಲಯಗಳು)** ವಿಂಗಡಿಸಿದೆ.

---

### ⚠️ ಸಾಮಾನ್ಯ ಸಮಸ್ಯೆಗಳು & ನೋಟಿಸ್ ಪರಿಹಾರ:
* **ತಪ್ಪು ವಲಯ ಆಯ್ಕೆ (Wrong Zone Selection):** ಆಸ್ತಿ 'Zone B' ನಲ್ಲಿದ್ದರೂ ಹಿಂದಿನ ವರ್ಷಗಳಲ್ಲಿ 'Zone C' ಎಂದು ತೆರಿಗೆ ಕಟ್ಟಿದ್ದರೆ, ಸಾಫ್ಟ್‌ವೇರ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ವ್ಯತ್ಯಾಸದ ಮೊತ್ತಕ್ಕೆ 100% ದಂಡ ಮತ್ತು ಬಡ್ಡಿ ವಿಧಿಸಿ ಡಿಮಾಂಡ್ ನೋಟಿಸ್ ನೀಡುತ್ತದೆ.
* **ಸ್ವಯಂ ದುರಸ್ತಿ ವಿಧಾನ:** [bbmptax.karnataka.gov.in](https://bbmptax.karnataka.gov.in) ನಲ್ಲಿ ನಿಮ್ಮ ವಾರ್ಡ್ ಮತ್ತು ರಸ್ತೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ ಅಧಿಕೃತ ವಲಯವನ್ನು ಪರಿಶೀಲಿಸಿ.
* ತಪ್ಪು ನೋಟಿಸ್ ಬಂದಿದ್ದರೆ ಸಹಾಯಕ ಕಂದಾಯ ಅಧಿಕಾರಿ (ARO) ಕಚೇರಿಗೆ ಹಿಂದಿನ ಚಲನ್ ಮತ್ತು ಮಾರ್ಗಸೂಚಿ ದಾಖಲೆ ಸಲ್ಲಿಸಿ ದಂಡ ಮನ್ನಾ ಮಾಡಿಸಿಕೊಳ್ಳಬಹುದು.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bbmptax.karnataka.gov.in",
        "keywords": "bbmp tax zone reclassification, zone a to f guidance value, aro property tax penalty relief, ಬಿಬಿಎಂಪಿ ಆಸ್ತಿ ತೆರಿಗೆ ವಲಯ, ತೆರಿಗೆ ದಂಡ ಪರಿಹಾರ",
        "action_label": "🏢 BBMP ಆಸ್ತಿ ತೆರಿಗೆ",
        "action_url": "https://bbmptax.karnataka.gov.in"
    },
    {
        "id": "faq_ng_bescom_mmd_021",
        "question": "ಬೆಸ್ಕಾಂ ಮೀಟರ್ ಸೆಕ್ಯುರಿಟಿ ಠೇವಣಿ (MMD / Additional Security Deposit - ASD) ಹೆಚ್ಚಳ ಬಿಲ್ ಬಂದರೆ ಏನು ಮಾಡಬೇಕು?",
        "normalized_question": "bescom mmd asd security deposit excess bill explanation electricity meter ಬೆಸ್ಕಾಂ ಸೆಕ್ಯುರಿಟಿ ಠೇವಣಿ ಹೆಚ್ಚಳ",
        "answer": """### ⚡ ಬೆಸ್ಕಾಂ ಎಂಡಿಡಿ / ಎಎಸ್‌ಡಿ ಸೆಕ್ಯುರಿಟಿ ಠೇವಣಿ ಹೆಚ್ಚಳ ವಿವರ (MMD / ASD Advisory)

ವರ್ಷಕ್ಕೊಮ್ಮೆ ಬೆಸ್ಕಾಂ ವಿದ್ಯುತ್ ಬಿಲ್‌ನಲ್ಲಿ 'MMD (Monthly Minimum Deposit)' ಅಥವಾ 'ASD (Additional Security Deposit)' ಎಂದು ಹೆಚ್ಚುವರಿ ಶುಲ್ಕ ಬರುವುದರ ನಿಯಮಾವಳಿ:

---

### 📊 ಸೆಕ್ಯುರಿಟಿ ಠೇವಣಿ ಲೆಕ್ಕಾಚಾರದ ಸೂತ್ರ:
* ನಿಯಮಾವಳಿಯಂತೆ, ಗ್ರಾಹಕರು ಬಳಸುವ ಹಿಂದಿನ 12 ತಿಂಗಳ ಸರಾಸರಿ ವಿದ್ಯುತ್ ಬಿಲ್‌ನ **2 ತಿಂಗಳ ಮೊತ್ತಕ್ಕೆ ಸಮನಾದ ಸೆಕ್ಯುರಿಟಿ ಠೇವಣಿಯನ್ನು** ಎಸ್ಕಾಂ ತನ್ನ ಬಳಿ ಇಟ್ಟುಕೊಳ್ಳುತ್ತದೆ.
* ಹಿಂದಿನ ವರ್ಷಕ್ಕಿಂತ ನಿಮ್ಮ ವಿದ್ಯುತ್ ಬಳಕೆ ಗಣನೀಯವಾಗಿ ಹೆಚ್ಚಾಗಿದ್ದರೆ, ವ್ಯತ್ಯಾಸದ ಮೊತ್ತವನ್ನು ASD ಎಂದು ಬಿಲ್‌ನಲ್ಲಿ ಸೇರಿಸಲಾಗುತ್ತದೆ.

---

### 💡 ಗ್ರಾಹಕರು ತಿಳಿಯಬೇಕಾದ ಹಕ್ಕುಗಳು:
1. ನಿಮ್ಮ ಸೆಕ್ಯುರಿಟಿ ಠೇವಣಿ ಮೊತ್ತಕ್ಕೆ ಬೆಸ್ಕಾಂ ಪ್ರತಿವರ್ಷ ಬ್ಯಾಂಕ್ ಬಡ್ಡಿದರದಂತೆ **ಬಡ್ಡಿಯನ್ನು (Interest on Security Deposit)** ನಿಮ್ಮ ವಿದ್ಯುತ್ ಬಿಲ್‌ನಲ್ಲಿ ಕಡಿತ ಮಾಡಿ ವಾಪಸ್ ನೀಡುತ್ತದೆ.
2. ಮಾಲೀಕತ್ವ ಬದಲಾವಣೆ ಮಾಡಿದಾಗ ಹಳೆಯ ಠೇವಣಿಯನ್ನು ಹೊಸ ಮಾಲೀಕರ ಹೆಸರಿಗೆ ವರ್ಗಾಯಿಸಿಕೊಳ್ಳಬಹುದು.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bescom.karnataka.gov.in",
        "keywords": "bescom mmd asd security deposit, additional security deposit interest, electricity bill asd charges, ಬೆಸ್ಕಾಂ ಸೆಕ್ಯುರಿಟಿ ಠೇವಣಿ, ಎಂಡಿಡಿ ಶುಲ್ಕ",
        "action_label": "⚡ ಬೆಸ್ಕಾಂ ಪೋರ್ಟಲ್",
        "action_url": "https://bescom.karnataka.gov.in"
    }
]
# =========================================================================
# 22. EXPANSION BATCH 14: ADVANCED PROCEDURAL CITIZEN GUIDELINES (324 - 339)
# =========================================================================

ADDITIONAL_EXPANSION_FAQS_BATCH_14 = [
    {
        "id": "faq_user_324",
        "question": "ಯುಐಡಿಎಐ (UIDAI) ಅಧಿಕೃತ ಪಿವಿಸಿ ಆಧಾರ್ ಕಾರ್ಡ್ (Order Aadhaar PVC Card) ಅನ್ನು ₹50 ಪಾವತಿಸಿ ಮನೆಗೆ ತರಿಸಿಕೊಳ್ಳುವುದು ಹೇಗೆ?",
        "normalized_question": "order aadhaar pvc card online uidai 50 rupees speed post qr code ಅಧಿಕೃತ ಆಧಾರ್ ಪಿವಿಸಿ ಕಾರ್ಡ್",
        "answer": """### 🪪 ಅಧಿಕೃತ UIDAI ಪಿವಿಸಿ ಆಧಾರ್ ಕಾರ್ಡ್ (Order Aadhaar PVC Card)

ಮಾರುಕಟ್ಟೆಯಲ್ಲಿ ಸಿಗುವ ನಕಲಿ ಪ್ಲಾಸ್ಟಿಕ್ ಲ್ಯಾಮಿನೇಷನ್ ಕಾರ್ಡ್‌ಗಳ ಬದಲು, ಯುಐಡಿಎಐ ನೀಡುವ ಅಧಿಕೃತ ಕ್ಯೂಆರ್ ಕೋಡ್, ಹೊಲೊಗ್ರಾಮ್ ಮತ್ತು ಗಿಲೋಚ್ ಪ್ಯಾಟರ್ನ್ ಹೊಂದಿರುವ ಜಲನಿರೋಧಕ (Waterproof) ಸ್ಮಾರ್ಟ್ PVC ಕಾರ್ಡ್ ಪಡೆಯುವ ವಿಧಾನ:

---

### 💰 ಶುಲ್ಕ & ವಿತರಣೆ:
* **ಶುಲ್ಕ:** ಕೇವಲ **₹50** (ಜಿಎಸ್‌ಟಿ ಮತ್ತು ಸ್ಪೀಡ್ ಪೋಸ್ಟ್ ಡೆಲಿವರಿ ಶುಲ್ಕ ಒಳಗೊಂಡಿದೆ).
* ನಿಮ್ಮ ಆಧಾರ್‌ನಲ್ಲಿರುವ ಅಧಿಕೃತ ವಿಳಾಸಕ್ಕೆ ಸ್ಪೀಡ್ ಪೋಸ್ಟ್ ಮೂಲಕ 7 ರಿಂದ 15 ದಿನಗಳಲ್ಲಿ ತಲುಪುತ್ತದೆ.

---

### 💻 ಆರ್ಡರ್ ಮಾಡುವ ಹಂತಗಳು:
1. **ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [myaadhaar.uidai.gov.in](https://myaadhaar.uidai.gov.in)
2. ಮುಖಪುಟದಲ್ಲಿ **'Order Aadhaar PVC Card'** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ **12 ಅಂಕಿಗಳ ಆಧಾರ್ ಸಂಖ್ಯೆ** ಅಥವಾ 28 ಅಂಕಿಗಳ EID ಸಂಖ್ಯೆ ಮತ್ತು ಕ್ಯಾಪ್ಚಾ ನಮೂದಿಸಿ.
4. *ಆಧಾರ್‌ಗೆ ಮೊಬೈಲ್ ಲಿಂಕ್ ಇದ್ದರೆ:* ನೇರ OTP ಮೂಲಕ ಲಾಗಿನ್ ಆಗಿ.
   *ಮೊಬೈಲ್ ಲಿಂಕ್ ಇಲ್ಲದಿದ್ದರೆ:* 'My Mobile number is not registered' ಟಿಕ್ ಮಾಡಿ ನಿಮ್ಮ ಬಳಿಯಿರುವ ಯಾವುದೇ ಚಾಲ್ತಿ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ OTP ಪಡೆಯಿರಿ.
5. ಕಾರ್ಡ್ ಪ್ರಿವ್ಯೂ ನೋಡಿ UPI, ಡೆಬಿಟ್ ಕಾರ್ಡ್ ಅಥವಾ ನೆಟ್ ಬ್ಯಾಂಕಿಂಗ್ ಮೂಲಕ ₹50 ಪಾವತಿಸಿ.
6. ಬರುವ **SRN (Service Request Number)** ಬಳಸಿ ಡೆಲಿವರಿ ಸ್ಥಿತಿಯನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಬಹುದು.""",
        "category": "CERTIFICATES",
        "language": "kn",
        "source_url": "https://myaadhaar.uidai.gov.in",
        "keywords": "order aadhaar pvc card, uidai pvc smart card 50 rupees, myaadhaar track srn status, ಪಿವಿಸಿ ಆಧಾರ್ ಕಾರ್ಡ್, ಸ್ಮಾರ್ಟ್ ಆಧಾರ್ ಕಾರ್ಡ್",
        "action_label": "🪪 myAadhaar ಪೋರ್ಟಲ್",
        "action_url": "https://myaadhaar.uidai.gov.in"
    },
    {
        "id": "faq_user_325",
        "question": "ಕರ್ನಾಟಕದಲ್ಲಿ ಸೈಟ್ ಅಥವಾ ಮನೆ ಖರೀದಿಸುವ ಮುನ್ನ 30 ವರ್ಷಗಳ ಟೈಟಲ್ ಪರಿಶೀಲನೆ (Property Title Verification) ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "property title verification checklist 30 years mother deed ec legal scrutiny karnataka ಆಸ್ತಿ ಖರೀದಿ ದಾಖಲೆ ಪರಿಶೀಲನೆ",
        "answer": """### 🏡 ಆಸ್ತಿ ಖರೀದಿಸುವ ಮುನ್ನ 10 ಹಂತಗಳ ಕಾನೂನು ಪರಿಶೀಲನಾ ಮಾರ್ಗದರ್ಶಿ (Title Scrutiny Checklist)

ಜಮೀನು, ಸೈಟ್ ಅಥವಾ ಫ್ಲಾಟ್ ಖರೀದಿಸುವಾಗ ವಂಚನೆಗೊಳಗಾಗುವುದನ್ನು ತಡೆಯಲು ಪರಿಶೀಲಿಸಬೇಕಾದ ಕಡ್ಡಾಯ ದಾಖಲೆಗಳ ಪಟ್ಟಿ:

---

### 📋 ಕಡ್ಡಾಯವಾಗಿ ಪರಿಶೀಲಿಸಬೇಕಾದ ದಾಖಲೆಗಳು:
1. **30 ವರ್ಷಗಳ ಮೂಲ ಕ್ರಯಪತ್ರಗಳು (Mother Deeds / Prior Title Deeds):** ಆಸ್ತಿಯು ಮೊದಲ ಮಾಲೀಕರಿಂದ ಪ್ರಸ್ತುತ ಮಾರಾಟಗಾರರವರೆಗೆ ಹೇಗೆ ವರ್ಗಾವಣೆಯಾಗಿದೆ ಎಂಬ ಸಂಪೂರ್ಣ ಸರಪಳಿ (Chain).
2. **30 ವರ್ಷಗಳ ಋಣಭಾರ ಪ್ರಮಾಣಪತ್ರ (Nil Encumbrance Certificate - Form 15):** ಕಾವೇರಿ 2.0 ಪೋರ್ಟಲ್ ಮೂಲಕ ಬ್ಯಾಂಕ್ ಸಾಲ, ಅಡಮಾನ, ಅಥವಾ ಕೋರ್ಟ್ ತಡೆಯಾಜ್ಞೆ ಇಲ್ಲದಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.
3. **ಕಂದಾಯ ದಾಖಲೆಗಳು:** ಚಾಲ್ತಿ ಸಾಲಿನ ಪಹಣಿ (RTC), ಮ್ಯುಟೇಶನ್ ಪ್ರತಿ (MR Extract) ಮತ್ತು ಆಸ್ತಿ ರಿಜಿಸ್ಟರ್ ಸಾರಾಂಶ.
4. **ಯೋಜನಾ ಪ್ರಾಧಿಕಾರ ಅನುಮೋದನೆ:** BDA / BMRDA / DTCP ಅನುಮೋದಿತ ಲೇಔಟ್ ನಕ್ಷೆ (Approved Layout Plan).
5. **ಕನ್ವರ್ಶನ್ & ಕಂದಾಯ ತಕರಾರು:** ಕೃಷಿ ಜಮೀನಾಗಿದ್ದರೆ DC ಕನ್ವರ್ಶನ್ ಆದೇಶ ಹಾಗೂ **ದಿಶಾಂಕ್ ಆ್ಯಪ್** ಮೂಲಕ ರಾಜಕಾಲುವೆ/ಕೆರೆ ಬಫರ್ ಝೋನ್‌ನಲ್ಲಿಲ್ಲ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.
6. **ಪಿಟಿಸಿಎಲ್ & ವಕ್ಫ್ ಪರಿಶೀಲನೆ:** ಆಸ್ತಿಯು SC/ST ಮಂಜೂರಾದ ಜಮೀನು (PTCL Act) ಅಥವಾ ವಕ್ಫ್/ದೇವಾಲಯದ ಆಸ್ತಿಯಲ್ಲವೆಂದು ಪರಿಶೀಲಿಸಿ.

💡 ಅಂತಿಮ ಹಣ ಪಾವತಿಸುವ ಮುನ್ನ ನುರಿತ ಸಿವಿಲ್ ವಕೀಲರಿಂದ ಅಧಿಕೃತ **ಲೀಗಲ್ ಒಪಿನಿಯನ್ (Legal Scrutiny Report)** ಪಡೆದುಕೊಳ್ಳಿ.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://kaveri.karnataka.gov.in",
        "keywords": "property title verification checklist, 30 years mother deed scrutiny, nil encumbrance form 15, ಆಸ್ತಿ ಖರೀದಿ ಪರಿಶೀಲನೆ, ಲೀಗಲ್ ಒಪಿನಿಯನ್",
        "action_label": "📜 ಕಾವೇರಿ 2.0 EC ಪರಿಶೀಲನೆ",
        "action_url": "https://kaveri.karnataka.gov.in"
    },
    {
        "id": "faq_user_326",
        "question": "ವಾಹನದ ಬ್ಯಾಂಕ್ ಸಾಲ ತೀರಿದ ನಂತರ ಆರ್‌ಸಿಯಿಂದ ಹೈಪೋಥಿಕೇಷನ್ ರದ್ದು (Vehicle Hypothecation Removal - Form 35) ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "vehicle hypothecation cancellation form 35 bank loan close noc parivahan ವಾಹನ ಸಾಲ ಮುಕ್ತಾಯ ಆರ್‌ಸಿ ತಿದ್ದುಪಡಿ",
        "answer": """### 🚘 ವಾಹನ ಸಾಲ ಮುಕ್ತಾಯ & ಆರ್‌ಸಿ ಹೈಪೋಥಿಕೇಷನ್ ರದ್ದತಿ (Hypothecation Termination - HPT)

ಕಾರು ಅಥವಾ ಬೈಕ್ ಮೇಲಿನ ಬ್ಯಾಂಕ್ ಸಾಲ (Loan/EMI) ಪೂರ್ಣಗೊಂಡ ನಂತರ ವಾಹನದ ಆರ್‌ಸಿ ಬುಕ್‌ನಲ್ಲಿರುವ ಬ್ಯಾಂಕಿನ ಹೆಸರನ್ನು ರದ್ದುಪಡಿಸಿ ನಿಮ್ಮ ಹೆಸರಿಗೆ ಸಂಪೂರ್ಣ ಮಾಲೀಕತ್ವ ಪಡೆಯುವ ವಿಧಾನ:

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
1. ಬ್ಯಾಂಕ್‌ನಿಂದ ನೀಡಲಾದ **ಸಾಲ ತೀರುವಳಿ ಪ್ರಮಾಣಪತ್ರ (Loan Closure NOC)**.
2. ಬ್ಯಾಂಕ್ ಅಧಿಕೃತ ಸಹಿ ಮತ್ತು ಸೀಲ್ ಇರುವ **Form 35 (2 ಪ್ರತಿಗಳು)**.
3. ಮೂಲ ವಾಹನ ನೋಂದಣಿ ಪ್ರಮಾಣಪತ್ರ (Original RC Smart Card).
4. ಚಾಲ್ತಿಯಲ್ಲಿರುವ ವಾಹನ ವಿಮೆ (Insurance) ಮತ್ತು ಮಾಲಿನ್ಯ ನಿಯಂತ್ರಣ ಪ್ರಮಾಣಪತ್ರ (PUC).

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಪ್ರಕ್ರಿಯೆ:
1. [parivahan.gov.in](https://parivahan.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ 'Vehicle Related Services' ಆಯ್ಕೆಮಾಡಿ.
2. ವಾಹನ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ **'Application for Hypothecation Termination (HPT)'** ಆಯ್ಕೆಮಾಡಿ.
3. ಬ್ಯಾಂಕ್ NOC ದಿನಾಂಕ ಮತ್ತು ವಿವರ ದಾಖಲಿಸಿ ದಾಖಲೆಗಳನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
4. ನಿಗದಿತ ಶುಲ್ಕ (ದ್ವಿಚಕ್ರ ವಾಹನಕ್ಕೆ ₹300, ಕಾರುಗಳಿಗೆ ₹500) ಆನ್‌ಲೈನ್ ಪಾವತಿಸಿ.
5. ಆರ್‌ಟಿಒ ಪರಿಶೀಲನೆಯ ನಂತರ ಹೈಪೋಥಿಕೇಷನ್ ರದ್ದಾಗಿ ಶುದ್ಧ ಮಾಲೀಕತ್ವದ ಹೊಸ ಸ್ಮಾರ್ಟ್ ಕಾರ್ಡ್ ಆರ್‌ಸಿ ನಿಮ್ಮ ಮನೆಗೆ ಸ್ಪೀಡ್ ಪೋಸ್ಟ್ ಮೂಲಕ ಬರುತ್ತದೆ.""",
        "category": "TRANSPORT",
        "language": "kn",
        "source_url": "https://parivahan.gov.in",
        "keywords": "vehicle hypothecation removal form 35, bank loan closure noc rto, hpt parivahan karnataka, ವಾಹನ ಸಾಲ ರದ್ದತಿ ಆರ್‌ಸಿ, ಹೈಪೋಥಿಕೇಷನ್ ಕ್ಯಾನ್ಸಲ್",
        "action_label": "🚘 ಪರಿವಾಹನ್ HPT ಸೇವೆ",
        "action_url": "https://parivahan.gov.in"
    },
    {
        "id": "faq_user_327",
        "question": "18 ವರ್ಷ ತುಂಬಿದಾಗ ಮೈನರ್ ಪ್ಯಾನ್ ಕಾರ್ಡ್ ಅನ್ನು ಮೇಜರ್ ಪ್ಯಾನ್ ಕಾರ್ಡ್ ಆಗಿ (Minor to Major PAN Update) ಬದಲಾಯಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "minor to major pan card update photo signature guardian removal protean nsdl ಮೈನರ್ ಪ್ಯಾನ್ ಕಾರ್ಡ್ ಮೇಜರ್ ಅಪ್‌ಡೇಟ್",
        "answer": """### 💳 ಅಪ್ರಾಪ್ತ (Minor) ಪ್ಯಾನ್ ಕಾರ್ಡ್ ಅನ್ನು ವಯಸ್ಕ (Major) ಪ್ಯಾನ್ ಕಾರ್ಡ್ ಆಗಿ ನವೀಕರಿಸುವ ವಿಧಾನ

ಮಕ್ಕಳಿಗೆ 18 ವರ್ಷ ತುಂಬಿದ ತಕ್ಷಣ ಅವರ ಹಳೆಯ ಅಪ್ರಾಪ್ತ ಪ್ಯಾನ್ ಕಾರ್ಡ್‌ನಲ್ಲಿ ಫೋಟೋ ಮತ್ತು ಸಹಿ ಇರುವುದಿಲ್ಲ; ಪೋಷಕರ (Guardian) ಅಧಿಕಾರ ರದ್ದಾಗಿ ಸ್ವತಂತ್ರ ಬ್ಯಾಂಕ್ ವಹಿವಾಟು ನಡೆಸಲು ಮೇಜರ್ ಪ್ಯಾನ್ ಕಾರ್ಡ್ ಆಗಿ ನವೀಕರಿಸಬೇಕು.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
* ಪ್ರಸ್ತುತ ಹೊಂದಿರುವ ಮೈನರ್ ಪ್ಯಾನ್ ಕಾರ್ಡ್ ಪ್ರತಿ.
* 18 ವರ್ಷ ಪೂರ್ಣಗೊಂಡಿರುವುದಕ್ಕೆ ಪುರಾವೆ (ಆಧಾರ್ ಕಾರ್ಡ್ / ಜನನ ಪ್ರಮಾಣಪತ್ರ / 10th Marks Card).
* ಅರ್ಜಿದಾರರ ಇತ್ತೀಚಿನ ಪಾಸ್‌ಪೋರ್ಟ್ ಭಾವಚಿತ್ರ ಮತ್ತು ಬಿಳಿ ಹಾಳೆಯ ಮೇಲಿನ ಡಿಜಿಟಲ್ ಸಹಿ.

---

### 💻 ಆನ್‌ಲೈನ್ ನವೀಕರಣ ಹಂತಗಳು:
1. [protean-tinpan.com](https://www.protean-tinpan.com) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ **'Changes or Correction in PAN Data'** ಆಯ್ಕೆಮಾಡಿ.
2. ಪ್ಯಾನ್ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ, 'Photo Mismatch' ಮತ್ತು 'Signature Mismatch' ಬಾಕ್ಸ್‌ಗಳನ್ನು ಟಿಕ್ ಮಾಡಿ.
3. ಪೋಷಕರ (Guardian) ವಿವರವನ್ನು ತೆಗೆದುಹಾಕಿ ಅರ್ಜಿದಾರರ ಸ್ವಂತ ವಿವರ ಭರ್ತಿ ಮಾಡಿ.
4. ಹೊಸ ಫೋಟೋ, ಸಹಿ ಮತ್ತು ಆಧಾರ್ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ₹107 ಶುಲ್ಕ ಪಾವತಿಸಿ.
5. 10 ದಿನಗಳಲ್ಲಿ ಫೋಟೋ ಮತ್ತು ಸಹಿ ಹೊಂದಿರುವ ಪೂರ್ಣ ಪ್ರಮಾಣದ ಮೇಜರ್ PVC ಪ್ಯಾನ್ ಕಾರ್ಡ್ ವಿತರಣೆಯಾಗುತ್ತದೆ.""",
        "category": "CERTIFICATES",
        "language": "kn",
        "source_url": "https://www.protean-tinpan.com",
        "keywords": "minor to major pan card update, add photo signature pan card, guardian removal pan nsdl, ಮೈನರ್ ಪ್ಯಾನ್ ಕಾರ್ಡ್ ಮೇಜರ್, ಪ್ಯಾನ್ ಫೋಟೋ ಅಪ್‌ಡೇಟ್",
        "action_label": "💳 Protean PAN ಪೋರ್ಟಲ್",
        "action_url": "https://www.protean-tinpan.com"
    },
    {
        "id": "faq_user_328",
        "question": "ಬಿಬಿಎಂಪಿಯಲ್ಲಿ ಖಾತಾ ವಿಭಜನೆ (Khata Bifurcation) ಮತ್ತು ಖಾತಾ ಸಂಯೋಜನೆ (Khata Amalgamation) ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "khata bifurcation amalgamation online bbmp e aasthi property division ಖಾತಾ ವಿಭಜನೆ ಖಾತಾ ಸಂಯೋಜನೆ",
        "answer": """### 🏢 ಬಿಬಿಎಂಪಿ ಖಾತಾ ವಿಭಜನೆ & ಸಂಯೋಜನೆ ಮಾರ್ಗದರ್ಶಿ (BBMP e-Aasthi)

ಒಂದೇ ಆಸ್ತಿಯನ್ನು ಭಾಗ ಮಾಡಿ ಪ್ರತ್ಯೇಕ ಖಾತೆ ಮಾಡುವುದನ್ನು **ಖಾತಾ ವಿಭಜನೆ (Bifurcation)** ಹಾಗೂ ಪಕ್ಕಪಕ್ಕದ ಎರಡು ನಿವೇಶನಗಳನ್ನು ಸೇರಿಸಿ ಒಂದೇ ಖಾತೆ ಮಾಡುವುದನ್ನು **ಖಾತಾ ಸಂಯೋಜನೆ (Amalgamation)** ಎನ್ನಲಾಗುತ್ತದೆ.

---

### ✂️ 1. ಖಾತಾ ವಿಭಜನೆ (Khata Bifurcation):
* **ಸನ್ನಿವೇಶ:** ಪಿತ್ರಾರ್ಜಿತ ಆಸ್ತಿಯನ್ನು ಅಣ್ಣ-ತಮ್ಮಂದಿರು ವಿಭಾಗ ಮಾಡಿಕೊಂಡಾಗ ಅಥವಾ ಒಂದು ದೊಡ್ಡ ನಿವೇಶನವನ್ನು 2 ಭಾಗಗಳಾಗಿ ಮಾರಾಟ ಮಾಡಿದಾಗ.
* **ದಾಖಲೆಗಳು:** ನೋಂದಾಯಿತ ವಿಭಾಗಪತ್ರ (Registered Partition Deed) / ಬಿಡುಗಡೆ ಪತ್ರ, ಅನುಮೋದಿತ ವಿಭಜನಾ ನಕ್ಷೆ, ಮತ್ತು ಇತ್ತೀಚಿನ ಆಸ್ತಿ ತೆರಿಗೆ ರಶೀದಿ.

---

### ➕ 2. ಖಾತಾ ಸಂಯೋಜನೆ (Khata Amalgamation):
* **ಸನ್ನಿವೇಶ:** ಪಕ್ಕಪಕ್ಕದ ಎರಡು 30x40 ನಿವೇಶನಗಳನ್ನು ಖರೀದಿಸಿ ಒಂದೇ ದೊಡ್ಡ ಮನೆ ಕಟ್ಟಲು ಒಂದೇ PID ಅಡಿಯಲ್ಲಿ ತರಲು.
* **ದಾಖಲೆಗಳು:** ಎರಡೂ ನಿವೇಶನಗಳ ನೋಂದಾಯಿತ ಕ್ರಯಪತ್ರಗಳು, ಹಳೆಯ ಖಾತಾಗಳು, ಸಂಯೋಜಿತ ನಕ್ಷೆ ಮತ್ತು ಕಾಂಪೌಂಡಿಂಗ್ ಶುಲ್ಕ.

🔗 [bbmpeaasthi.karnataka.gov.in](https://bbmpeaasthi.karnataka.gov.in) ನಲ್ಲಿ ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ಎಆರ್‌ಒ ಪರಿಶೀಲನೆಯ ನಂತರ ಪ್ರತ್ಯೇಕ/ಸಂಯೋಜಿತ ಇ-ಖಾತಾ ಪಡೆಯಬಹುದು.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://bbmpeaasthi.karnataka.gov.in",
        "keywords": "khata bifurcation bbmp, khata amalgamation e aasthi, partition deed khata division, ಖಾತಾ ವಿಭಜನೆ, ಖಾತಾ ಸಂಯೋಜನೆ, ಬಿಬಿಎಂಪಿ ಇ-ಆಸ್ತಿ",
        "action_label": "🏢 BBMP e-Aasthi",
        "action_url": "https://bbmpeaasthi.karnataka.gov.in"
    },
    {
        "id": "faq_user_329",
        "question": "ಇರುವ ಬೈಕ್ ಡ್ರೈವಿಂಗ್ ಲೈಸೆನ್ಸ್‌ಗೆ (DL) ಕಾರು / ಲಘು ವಾಹನ (Add LMV to Existing DL) ಸೇರಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "add lmv car to existing mcwg driving license endorsement parivahan ಡಿಎಲ್‌ಗೆ ಕಾರು ಲೈಸೆನ್ಸ್ ಸೇರ್ಪಡೆ",
        "answer": """### 🚗 ಚಾಲ್ತಿ ಲೈಸೆನ್ಸ್‌ಗೆ ಹೊಸ ವಾಹನ ವರ್ಗ ಸೇರ್ಪಡೆ (Addition of Class of Vehicle - AEDL)

ನಿಮ್ಮ ಬಳಿ ಈಗಾಗಲೇ ದ್ವಿಚಕ್ರ ವಾಹನದ (MCWG) ಲೈಸೆನ್ಸ್ ಇದ್ದು, ಕಾರು/ಲಘು ವಾಹನದ (LMV) ಚಾಲನಾ ಪರವಾನಗಿ ಸೇರಿಸಿಕೊಳ್ಳಲು ಪ್ರತ್ಯೇಕ ಹೊಸ ಕಾರ್ಡ್ ಮಾಡುವ ಅಗತ್ಯವಿಲ್ಲ; ಎಂಡಾರ್ಸ್‌ಮೆಂಟ್ ಮೂಲಕ ಸೇರಿಸಬಹುದು.

---

### 🚀 ಹಂತ-ಹಂತದ ವಿಧಾನ:
1. **ಹೊಸ ವರ್ಗಕ್ಕೆ LLR ಅರ್ಜಿ:** [parivahan.gov.in](https://parivahan.gov.in) ನಲ್ಲಿ 'Apply for Learner License' ಆಯ್ಕೆಮಾಡಿ, ನಿಮ್ಮ ಹಾಲಿ DL ಸಂಖ್ಯೆ ಹಾಕಿ 'LMV (Light Motor Vehicle)' ವರ್ಗವನ್ನು ಆರಿಸಿ.
2. ಹಾಲಿ DL ಇರುವುದರಿಂದ ನೀವು ಯಾವುದೇ ಕಂಪ್ಯೂಟರ್ ಥಿಯರಿ ಪರೀಕ್ಷೆ (Theory Test) ಬರೆಯುವಂತಿಲ್ಲ; ತಕ್ಷಣ LLR ಸಿಗುತ್ತದೆ.
3. 30 ದಿನಗಳ ನಂತರ **'Apply for Driving License -> Add Class of Vehicle'** ಆಯ್ಕೆಮಾಡಿ ಆರ್‌ಟಿಒ ಟ್ರ್ಯಾಕ್ ಟೆಸ್ಟ್‌ಗೆ ಸ್ಲಾಟ್ ಬುಕ್ ಮಾಡಿ.
4. ಆರ್‌ಟಿಒ ಇನ್‌ಸ್ಪೆಕ್ಟರ್ ಮುಂದೆ ಕಾರು ಚಾಲನಾ ಪರೀಕ್ಷೆ ಉತ್ತೀರ್ಣರಾದ ನಂತರ ನಿಮ್ಮ ಹಳೆಯ ಲೈಸೆನ್ಸ್‌ನಲ್ಲೇ **MCWG + LMV** ಎರಡೂ ವರ್ಗಗಳು ಸೇರ್ಪಡೆಯಾಗಿ ನವೀಕೃತ ಸ್ಮಾರ್ಟ್ ಕಾರ್ಡ್ ಬರುತ್ತದೆ.""",
        "category": "TRANSPORT",
        "language": "kn",
        "source_url": "https://parivahan.gov.in",
        "keywords": "add lmv to existing dl, addition of class of vehicle parivahan, aedl driving test karnataka, ಲೈಸೆನ್ಸ್‌ಗೆ ಕಾರು ಸೇರ್ಪಡೆ, ಡಿಎಲ್ ಎಂಡಾರ್ಸ್‌ಮೆಂಟ್",
        "action_label": "🚗 ಪರಿವಾಹನ್ DL ಸೇವೆ",
        "action_url": "https://parivahan.gov.in"
    },
    {
        "id": "faq_user_330",
        "question": "ಬೇರೆ ಜಿಲ್ಲೆ ಅಥವಾ ಊರಿಗೆ ಸ್ಥಳಾಂತರಗೊಂಡಾಗ ರೇಷನ್ ಕಾರ್ಡ್ ನ್ಯಾಯಬೆಲೆ ಅಂಗಡಿ (Fair Price Shop Transfer) ಬದಲಾಯಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "ration card fair price shop fps transfer district shifting ahara karnataka ರೇಷನ್ ಕಾರ್ಡ್ ಅಂಗಡಿ ವರ್ಗಾವಣೆ",
        "answer": """### 🛒 ರೇಷನ್ ಕಾರ್ಡ್ ನ್ಯಾಯಬೆಲೆ ಅಂಗಡಿ (FPS) & ವಿಳಾಸ ವರ್ಗಾವಣೆ

ಉದ್ಯೋಗ, ಮದುವೆ ಅಥವಾ ವಾಸಸ್ಥಳ ಬದಲಾವಣೆಯ ಕಾರಣದಿಂದ ಬೇರೆ ಜಿಲ್ಲೆ ಅಥವಾ ತಾಲೂಕಿಗೆ ಸ್ಥಳಾಂತರಗೊಂಡಾಗ ಹತ್ತಿರದ ನ್ಯಾಯಬೆಲೆ ಅಂಗಡಿಗೆ ರೇಷನ್ ಕಾರ್ಡ್ ವರ್ಗಾಯಿಸುವ ವಿಧಾನ:

---

### 💻 ಆನ್‌ಲೈನ್ ವರ್ಗಾವಣೆ ಹಂತಗಳು (Ahara Portal):
1. [ahara.kar.nic.in](https://ahara.kar.nic.in) ಗೆ ಭೇಟಿ ನೀಡಿ **'E-Services -> Change of Fair Price Shop / Address'** ಆಯ್ಕೆಮಾಡಿ.
2. ನಿಮ್ಮ ರೇಷನ್ ಕಾರ್ಡ್ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ ಕುಟುಂಬದ ಮುಖ್ಯಸ್ಥರ ಆಧಾರ್ OTP ಮೂಲಕ ಲಾಗಿನ್ ಆಗಿ.
3. ನಿಮ್ಮ ನೂತನ ಜಿಲ್ಲೆ, ತಾಲೂಕು, ಗ್ರಾಮ/ವಾರ್ಡ್ ಮತ್ತು ಸಮೀಪದ **ನ್ಯಾಯಬೆಲೆ ಅಂಗಡಿ ಸಂಖ್ಯೆಯನ್ನು (Fair Price Shop Code)** ಆಯ್ಕೆಮಾಡಿ.
4. ನೂತನ ವಿಳಾಸದ ಪುರಾವೆ (ವಿದ್ಯುತ್ ಬಿಲ್ / ಗ್ಯಾಸ್ ಬಿಲ್ / ಬಾಡಿಗೆ ಒಪ್ಪಂದ) ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
5. ತಾಲೂಕು ಆಹಾರ ಶಿರಸ್ತೇದಾರ್ ಅನುಮೋದಿಸಿದ 7 ದಿನಗಳಲ್ಲಿ ಮುಂದಿನ ತಿಂಗಳಿನಿಂದ ಹೊಸ ಅಂಗಡಿಯಲ್ಲೇ ಪಡಿತರ ಅಕ್ಕಿ ಮತ್ತು ಧಾನ್ಯ ಲಭ್ಯವಾಗುತ್ತದೆ.

💡 ರಾಷ್ಟ್ರೀಯ **One Nation One Ration Card (ONORC)** ಅಡಿಯಲ್ಲಿ ಕಾರ್ಡ್ ವರ್ಗಾವಣೆ ಮಾಡದೆಯೂ ಸಹ ಬಯೋಮೆಟ್ರಿಕ್ ಮೂಲಕ ರಾಜ್ಯದ ಯಾವುದೇ ನ್ಯಾಯಬೆಲೆ ಅಂಗಡಿಯಲ್ಲಿ ಪಡಿತರ ಪಡೆಯಬಹುದು.""",
        "category": "FOOD",
        "language": "kn",
        "source_url": "https://ahara.kar.nic.in",
        "keywords": "ration card fps transfer online, change fair price shop ahara, onorc portability karnataka, ರೇಷನ್ ಕಾರ್ಡ್ ಅಂಗಡಿ ಬದಲಾವಣೆ, ಆಹಾರ ಇಲಾಖೆ",
        "action_label": "🛒 ಆಹಾರ ಇಲಾಖೆ ಪೋರ್ಟಲ್",
        "action_url": "https://ahara.kar.nic.in"
    },
    {
        "id": "faq_user_331",
        "question": "ಗಂಗಾ ಕಲ್ಯಾಣ ಯೋಜನೆಯಲ್ಲಿ ಕೊರೆದ ಬೋರ್‌ವೆಲ್‌ನಲ್ಲಿ ನೀರು ಬಾರದಿದ್ದರೆ (Borewell Failure) ಸರ್ಕಾರದ ನಿಯಮಾವಳಿ ಏನು?",
        "normalized_question": "ganga kalyana borewell failure yield compensation re survey re drilling karnataka ಗಂಗಾ ಕಲ್ಯಾಣ ಬೋರ್‌ವೆಲ್ ನೀರು ಬಾರದಿದ್ದರೆ",
        "answer": """### 🌾 ಗಂಗಾ ಕಲ್ಯಾಣ ಬೋರ್‌ವೆಲ್ ವೈಫಲ್ಯ & ಮರು-ಸರ್ವೆ ನಿಯಮಗಳು

ಗಂಗಾ ಕಲ್ಯಾಣ ಯೋಜನೆಯಡಿ ಸರ್ಕಾರದ ವೆಚ್ಚದಲ್ಲಿ ಕೊರೆಸಿದ ಕೊಳವೆಬಾವಿಯಲ್ಲಿ ನೀರು ಸಿಗದಿದ್ದರೆ (Dry / Failure Borewell) ಅನುಸರಿಸಲಾಗುವ ಇಲಾಖಾ ಮಾರ್ಗಸೂಚಿ:

---

### 📋 ಪರಿಹಾರ & ಮರು-ಕೊರೆಯುವಿಕೆ ನಿಯಮಗಳು:
1. **ಹೈಡ್ರೋ-ಜಿಯಾಲಾಜಿಕಲ್ ಜಂಟಿ ಮಹಜರು:** ಬೋರ್‌ವೆಲ್ ಕೊರೆದ ತಕ್ಷಣ ನೀರು ಬಾರದಿದ್ದರೆ, ಗಣಿ ಮತ್ತು ಭೂವಿಜ್ಞಾನ ಇಲಾಖೆಯ ವಿಜ್ಞಾನಿ, ನಿಗಮದ ಇಂಜಿನಿಯರ್ ಮತ್ತು ಫಲಾನುಭವಿ ರೈತರ ಸಮ್ಮುಖದಲ್ಲಿ ಸ್ಥಳದಲ್ಲೇ ವೈಫಲ್ಯ ಮಹಜರು (Failure Mahazar Report) ಸಿದ್ಧಪಡಿಸಲಾಗುತ್ತದೆ.
2. **ದ್ವಿತೀಯ ಕೊರೆಯುವಿಕೆಗೆ ಅವಕಾಶ (Re-drilling Permission):** ರೈತರ ಜಮೀನಿನಲ್ಲಿ ಬೇರೆ ಜಲಮೂಲದ ಪಾಯಿಂಟ್ ಲಭ್ಯವಿದ್ದರೆ, ಜಿಲ್ಲಾ ಮಟ್ಟದ ಸಮಿತಿಯ ಅನುಮೋದನೆ ಪಡೆದು ಅದೇ ಯೋಜನೆಯಡಿ ಮತ್ತೊಮ್ಮೆ ಬೋರ್‌ವೆಲ್ ಕೊರೆಯಲು ಆದೇಶ ನೀಡಲಾಗುತ್ತದೆ.
3. ಬೋರ್‌ವೆಲ್ ಯಶಸ್ವಿಯಾದ ನಂತರವೇ ಪಂಪ್, ಮೋಟಾರ್, ಪೈಪ್‌ಲೈನ್ ಮತ್ತು ವಿದ್ಯುತ್ ಸಂಪರ್ಕವನ್ನು ನಿಗಮದ ವತಿಯಿಂದ ಸಂಪೂರ್ಣ ಉಚಿತವಾಗಿ ಅಳವಡಿಸಲಾಗುತ್ತದೆ.

🔗 **ಅಧಿಕೃತ ನಿಗಮ:** [adcl.karnataka.gov.in](https://adcl.karnataka.gov.in) | [kmdconline.karnataka.gov.in](https://kmdconline.karnataka.gov.in)""",
        "category": "AGRICULTURE",
        "language": "kn",
        "source_url": "https://adcl.karnataka.gov.in",
        "keywords": "ganga kalyana borewell failure rules, re drilling borewell karnataka, failure mahazar report, ಗಂಗಾ ಕಲ್ಯಾಣ ಬೋರ್‌ವೆಲ್ ವೈಫಲ್ಯ, ಮರು ಕೊರೆಯುವಿಕೆ",
        "action_label": "🌾 ಗಂಗಾ ಕಲ್ಯಾಣ ವಿವರ",
        "action_url": "https://adcl.karnataka.gov.in"
    },
    {
        "id": "faq_user_332",
        "question": "ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ ಮತ್ತು ಜಿಲ್ಲಾ ನ್ಯಾಯಾಲಯಗಳ ಆದೇಶ ಪ್ರತಿ (Certified Copy of Judgment / Order) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "high court karnataka certified copy judgment online e copying portal ಇ-ಕಾಪಿಯಿಂಗ್ ಕೋರ್ಟ್ ಆದೇಶ ಪ್ರತಿ",
        "answer": """### ⚖️ ಕರ್ನಾಟಕ ನ್ಯಾಯಾಂಗ ಇ-ಕಾಪಿಯಿಂಗ್ ಪೋರ್ಟಲ್ (Online Certified Copy — e-Copying)

ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ (ಬೆಂಗಳೂರು, ಧಾರವಾಡ, ಕಲಬುರಗಿ ಪೀಠಗಳು) ಹಾಗೂ ಜಿಲ್ಲಾ ನ್ಯಾಯಾಲಯಗಳು ಹೊರಡಿಸಿದ ತೀರ್ಪು, ಮಧ್ಯಂತರ ಆದೇಶ ಮತ್ತು ಸಾಕ್ಷ್ಯ ನಡಾವಳಿಗಳ ಅಧಿಕೃತ ಮುದ್ರಾಂಕಿತ ಪ್ರಮಾಣೀಕೃತ ಪ್ರತಿಯನ್ನು (Certified Copy) ಆನ್‌ಲೈನ್‌ನಲ್ಲೇ ಪಡೆಯುವ ವಿಧಾನ:

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಪ್ರಕ್ರಿಯೆ:
1. [karnatakajudiciary.kar.nic.in](https://karnatakajudiciary.kar.nic.in) ನಲ್ಲಿ **'Online Certified Copy Application (e-Copying)'** ಆಯ್ಕೆಮಾಡಿ.
2. ನ್ಯಾಯಾಲಯದ ವಿಧ (High Court / District Court), ಪ್ರಕರಣದ ವಿಧ (WP / CRLA / OS / CC) ಮತ್ತು ಕೇಸ್ ನಂಬರ್ ನಮೂದಿಸಿ.
3. ನಿಮಗೆ ಅಗತ್ಯವಿರುವ ಆದೇಶದ ದಿನಾಂಕ (Order Date) ಆಯ್ಕೆಮಾಡಿ.
4. ಪುಟಗಳಿಗೆ ತಕ್ಕಂತೆ ಕೋರ್ಟ್ ಕಾಪಿಯಿಂಗ್ ಶುಲ್ಕವನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪಾವತಿಸಿ.
5. ಪ್ರಮಾಣೀಕೃತ ಪ್ರತಿಯು ಸಿದ್ಧವಾದಾಗ ಡಿಜಿಟಲ್ ವಾಟರ್‌ಮಾರ್ಕ್ ಇರುವ ಅಧಿಕೃತ PDF ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು ಅಥವಾ ಸ್ಪೀಡ್ ಪೋಸ್ಟ್ ಮೂಲಕ ಮನೆಗೆ ತರಿಸಿಕೊಳ್ಳಬಹುದು.""",
        "category": "LEGAL",
        "language": "kn",
        "source_url": "https://karnatakajudiciary.kar.nic.in",
        "keywords": "karnataka high court certified copy online, e copying court order portal, judgment copy download, ಹೈಕೋರ್ಟ್ ಆದೇಶ ಪ್ರತಿ, ಇ-ಕಾಪಿಯಿಂಗ್",
        "action_label": "⚖️ ಹೈಕೋರ್ಟ್ e-Copying",
        "action_url": "https://karnatakajudiciary.kar.nic.in"
    },
    {
        "id": "faq_user_333",
        "question": "ಕರ್ನಾಟಕ ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳ ಹೆಸರಿನಲ್ಲಿ ನಕಲಿ ಆ್ಯಪ್ ಮತ್ತು ಲಿಂಕ್‌ಗಳ ವಂಚನೆ ತಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "fake guarantee scheme app fraud warning official karnataka gov in cyber crime awareness ಗ್ಯಾರಂಟಿ ನಕಲಿ ಲಿಂಕ್ ವಂಚನೆ",
        "answer": """### 🛡️ ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್‌ಗಳು vs ನಕಲಿ ಪೋರ್ಟಲ್ ವಂಚನೆ ಎಚ್ಚರಿಕೆ

ಗೃಹಲಕ್ಷ್ಮಿ ₹2,000, ಯುವನಿಧಿ ಅಥವಾ ಗೃಹಜ್ಯೋತಿ ಹೆಸರಿನಲ್ಲಿ ವಾಟ್ಸಾಪ್/ಟೆಲಿಗ್ರಾಂನಲ್ಲಿ ಬರುವ ನಕಲಿ APK ಫೈಲ್‌ಗಳು ಮತ್ತು ನಕಲಿ ಲಿಂಕ್‌ಗಳ ಮೂಲಕ ಬ್ಯಾಂಕ್ ಖಾತೆ ಹ್ಯಾಕ್ ಆಗುವುದನ್ನು ತಡೆಯುವ ಮಾರ್ಗಸೂಚಿ:

---

### ⚠️ ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್ ಗುರುತಿಸುವ ಸೂತ್ರಗಳು:
1. **ಡೊಮೈನ್ ಪರಿಶೀಲಿಸಿ:** ಸರ್ಕಾರದ ಎಲ್ಲಾ ಅಧಿಕೃತ ಪೋರ್ಟಲ್‌ಗಳು ಕೇವಲ **`.karnataka.gov.in`** ಅಥವಾ **`.gov.in`** ಅಥವಾ **`.nic.in`** ನಲ್ಲಿ ಮಾತ್ರ ಕೊನೆಗೊಳ್ಳುತ್ತವೆ (`.org`, `.com`, `.in`, `.online`, `.xyz` ಸರ್ಕಾರಿ ಸೈಟ್‌ಗಳಲ್ಲ).
2. **ಯಾವುದೇ ಅಜ್ಞಾತ APK ಡೌನ್‌ಲೋಡ್ ಮಾಡಬೇಡಿ:** ವಾಟ್ಸಾಪ್‌ನಲ್ಲಿ ಯಾರೇ ಕಳುಹಿಸಿದ 'Gruha_Lakshmi_App.apk' ಫೈಲ್‌ಗಳನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಬೇಡಿ (ಕೇವಲ Google Play Store ನಲ್ಲಿರುವ ಸರ್ಕಾರದ ಅಧಿಕೃತ 'DBT Karnataka' ಆ್ಯಪ್ ಮಾತ್ರ ಬಳಸಿ).
3. **OTP ಯಾರೊಂದಿಗೂ ಹಂಚಿಕೊಳ್ಳಬೇಡಿ:** ಸರ್ಕಾರದ ಯಾವುದೇ ಅಧಿಕಾರಿ ಅಥವಾ ಬ್ಯಾಂಕ್ ಮ್ಯಾನೇಜರ್ ಕರೆ ಮಾಡಿ ಗ್ಯಾರಂಟಿ ಹಣ ಜಮೆ ಮಾಡಲು ನಿಮ್ಮ OTP ಅಥವಾ ಬ್ಯಾಂಕ್ ಕಾರ್ಡ್ ವಿವರ ಕೇಳುವುದಿಲ್ಲ.

📞 **ವಂಚನೆ ನಡೆದರೆ ತಕ್ಷಣ ಕರೆ ಮಾಡಿ: 1930 (ಸೈಬರ್ ಕ್ರೈಮ್ ಸಹಾಯವಾಣಿ)**""",
        "category": "POLICE",
        "language": "kn",
        "source_url": "https://cybercrime.gov.in",
        "keywords": "fake guarantee scheme app fraud, official karnataka gov in domain check, 1930 cyber fraud complaint, ಗ್ಯಾರಂಟಿ ನಕಲಿ ಆ್ಯಪ್ ವಂಚನೆ, ಸೈಬರ್ ಕ್ರೈಮ್ 1930",
        "action_label": "🛡️ ಸೈಬರ್ ಕ್ರೈಮ್ ಪೋರ್ಟಲ್",
        "action_url": "https://cybercrime.gov.in"
    },
    {
        "id": "faq_user_334",
        "question": "ಕೆಎಸ್‌ಆರ್‌ಟಿಸಿ (KSRTC) ಬಸ್‌ಗಳಲ್ಲಿ ಲಗೇಜ್ ತೂಕದ ಮಿತಿ ಮತ್ತು ಹೆಚ್ಚುವರಿ ಲಗೇಜ್ ದರ (Luggage Rules) ನಿಯಮಗಳೇನು?",
        "normalized_question": "ksrtc free luggage allowance 30 kg excess baggage charges rules ಕೆಎಸ್‌ಆರ್‌ಟಿಸಿ ಲಗೇಜ್ ತೂಕ ನಿಯಮ",
        "answer": """### 🧳 ಕೆಎಸ್‌ಆರ್‌ಟಿಸಿ ಬಸ್ ಪ್ರಯಾಣಿಕರ ಲಗೇಜ್ ನಿಯಮಾವಳಿ (Luggage Allowance & Charges)

ಕರ್ನಾಟಕ ರಾಜ್ಯ ರಸ್ತೆ ಸಾರಿಗೆ ನಿಗಮದ (KSRTC) ಬಸ್‌ಗಳಲ್ಲಿ ಪ್ರಯಾಣಿಕರು ತಮ್ಮೊಂದಿಗೆ ಉಚಿತವಾಗಿ ತೆಗೆದುಕೊಂಡು ಹೋಗಬಹುದಾದ ಲಗೇಜ್ ಮಿತಿ ಮತ್ತು ಶುಲ್ಕ:

---

### ⚖️ ಉಚಿತ ಲಗೇಜ್ ಮಿತಿ (Free Luggage Allowance):
* ಪ್ರತಿ ವಯಸ್ಕ ಪ್ರಯಾಣಿಕರಿಗೆ (Adult Ticket) ಗರಿಷ್ಠ **30 ಕೆಜಿ (30 kg)** ವೈಯಕ್ತಿಕ ಲಗೇಜ್ ಸಂಪೂರ್ಣ ಉಚಿತ.
* ಅರ್ಧ ಟಿಕೆಟ್ ಹೊಂದಿರುವ ಮಕ್ಕಳಿಗೆ ಗರಿಷ್ಠ **15 ಕೆಜಿ (15 kg)** ಉಚಿತ.

---

### 📦 ಹೆಚ್ಚುವರಿ ಲಗೇಜ್ & ಕಮರ್ಷಿಯಲ್ ಸರಕು ದರ:
* 30 ಕೆಜಿಗಿಂತ ಹೆಚ್ಚಿರುವ ಲಗೇಜ್, ಟಿವಿ, ಸೈಕಲ್, ಹಣ್ಣು/ತರಕಾರಿ ಬಾಕ್ಸ್‌ಗಳು ಅಥವಾ ದೊಡ್ಡ ಸರಕುಗಳಿಗೆ ನಿಗದಿತ ಲಗೇಜ್ ಟಿಕೆಟ್ (Luggage Ticket) ಪಡೆಯುವುದು ಕಡ್ಡಾಯ.
* ಅನುಮತಿಯಿಲ್ಲದೆ ಅಧಿಕ ತೂಕದ ಲಗೇಜ್ ಸಾಗಿಸಿದರೆ ತನಿಖಾಧಿಕಾರಿಗಳು ಪೂರ್ಣ ದರ + ದುಪ್ಪಟ್ಟು ದಂಡ ವಿಧಿಸುತ್ತಾರೆ.
* ಗ್ಯಾಸ್ ಸಿಲಿಂಡರ್, ಪಟಾಕಿ, ಆಸಿಡ್ ಮತ್ತು ದಹನಕಾರಿ ಪದಾರ್ಥಗಳನ್ನು ಬಸ್‌ನಲ್ಲಿ ಸಾಗಿಸುವುದು ಕಟ್ಟುನಿಟ್ಟಾಗಿ ನಿಷೇಧಿಸಲಾಗಿದೆ.""",
        "category": "TRANSIT",
        "language": "kn",
        "source_url": "https://ksrtc.in",
        "keywords": "ksrtc luggage rules, free 30 kg luggage allowance, excess luggage charges bus, ಕೆಎಸ್‌ಆರ್‌ಟಿಸಿ ಲಗೇಜ್ ನಿಯಮ, ಬಸ್ ಲಗೇಜ್ ದರ",
        "action_label": "🧳 KSRTC ನಿಯಮಗಳು",
        "action_url": "https://ksrtc.in"
    },
    {
        "id": "faq_user_335",
        "question": "ವಿದೇಶಿ ವ್ಯಾಸಂಗಕ್ಕೆ ಕೆಎಸ್‌ಒಯು / ಬೆಂಗಳೂರು ವಿವಿ ಟ್ರಾನ್ಸ್‌ಕ್ರಿಪ್ಟ್ ಮತ್ತು ಡಿಗ್ರಿ ವೆರಿಫಿಕೇಶನ್ (Transcript & Degree Verification) ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "university marks card transcript verification wes migration certificate ksou bangalore university ವಿಶ್ವವಿದ್ಯಾಲಯ ಟ್ರಾನ್ಸ್‌ಕ್ರಿಪ್ಟ್",
        "answer": """### 🎓 ವಿಶ್ವವಿದ್ಯಾಲಯಗಳ ಅಂಕಪಟ್ಟಿ ಟ್ರಾನ್ಸ್‌ಕ್ರಿಪ್ಟ್ & ಡಿಗ್ರಿ ವೆರಿಫಿಕೇಶನ್ (University Transcript & WES Process)

ವಿದೇಶದಲ್ಲಿ ಉನ್ನತ ವ್ಯಾಸಂಗ (WES Verification / US / UK / Canada Visa) ಅಥವಾ ವಿದೇಶಿ ಉದ್ಯೋಗಕ್ಕೆ ಅರ್ಜಿ ಸಲ್ಲಿಸುವಾಗ ವಿಶ್ವವಿದ್ಯಾಲಯದಿಂದ ಅಧಿಕೃತ ಸೀಲ್ ಇರುವ ಅಫಿಷಿಯಲ್ ಟ್ರಾನ್ಸ್‌ಕ್ರಿಪ್ಟ್ ಪಡೆಯುವ ವಿಧಾನ:

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
1. ಎಲ್ಲಾ ಸೆಮಿಸ್ಟರ್ / ವರ್ಷಗಳ ಅಂಕಪಟ್ಟಿಗಳ (Marks Cards) ಸ್ಪಷ್ಟ ಪ್ರತಿಗಳು.
2. ಕಾನ್ವೊಕೇಷನ್ ಡಿಗ್ರಿ ಪ್ರಮಾಣಪತ್ರ (Degree Certificate) ಮತ್ತು ಪ್ರಾವಿಷನಲ್ ಸರ್ಟಿಫಿಕೇಟ್.
3. WES / ವಿದೇಶಿ ಸಂಸ್ಥೆಯ Academic Records Request Form (Reference Number ಸಮೇತ).
4. ಪಾಸ್‌ಪೋರ್ಟ್ ಪ್ರತಿ ಮತ್ತು ವಿದ್ಯಾರ್ಥಿ ಆಧಾರ್ ಕಾರ್ಡ್.

---

### 🚀 ಪ್ರಕ್ರಿಯೆ:
* ಬೆಂಗಳೂರು ವಿವಿ, ಮೈಸೂರು ವಿವಿ, ವಿಟಿಯು (VTU) ಅಥವಾ ಕೆಎಸ್‌ಒಯು (KSOU) ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್‌ನ 'Online Transcript Portal' ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ ನಿಗದಿತ ಶುಲ್ಕ ಪಾವತಿಸಿ.
* ವಿಶ್ವವಿದ್ಯಾಲಯವು ದಾಖಲೆಗಳನ್ನು ಪರಿಶೀಲಿಸಿ ನೇರವಾಗಿ ಅಧಿಕೃತ ಇಮೇಲ್ ಮೂಲಕ WES ಸಂಸ್ಥೆಗೆ ಕಳುಹಿಸುತ್ತದೆ ಅಥವಾ ಸೀಲ್ಡ್ ಕವರ್‌ನಲ್ಲಿ (Sealed Envelope) ವಿದ್ಯಾರ್ಥಿಗೆ ನೀಡುತ್ತದೆ.""",
        "category": "EDUCATION",
        "language": "kn",
        "source_url": "https://dce.karnataka.gov.in",
        "keywords": "university transcript online karnataka, wes degree verification vtu bangalore university, ksou transcript, ವಿಶ್ವವಿದ್ಯಾಲಯ ಟ್ರಾನ್ಸ್‌ಕ್ರಿಪ್ಟ್, ಡಿಗ್ರಿ ವೆರಿಫಿಕೇಶನ್",
        "action_label": "🎓 ಉನ್ನತ ಶಿಕ್ಷಣ ಇಲಾಖೆ",
        "action_url": "https://dce.karnataka.gov.in"
    }
]

# =========================================================================
# 23. EXPANSION BATCH 15: CIVIC COMPLIANCE, PROPERTY LAW & ADVANCED ACCESS (340 - 355)
# =========================================================================

ADDITIONAL_EXPANSION_FAQS_BATCH_15 = [
    {
        "id": "faq_user_340",
        "question": "ಬಿಬಿಎಂಪಿ ಖಾತಾ ಪ್ರಮಾಣಪತ್ರ (Khata Certificate) ಮತ್ತು ಖಾತಾ ಸಾರಾಂಶದ (Khata Extract) ನಡುವಿನ ವ್ಯತ್ಯಾಸವೇನು?",
        "normalized_question": "difference between khata certificate and khata extract bbmp e aasthi ಖಾತಾ ಪ್ರಮಾಣಪತ್ರ ಮತ್ತು ಖಾತಾ ಸಾರಾಂಶ ವ್ಯತ್ಯಾಸ",
        "answer": """### 🏢 ಖಾತಾ ಪ್ರಮಾಣಪತ್ರ vs ಖಾತಾ ಸಾರಾಂಶ — ಸ್ಪಷ್ಟ ವ್ಯತ್ಯಾಸ ಮಾರ್ಗದರ್ಶಿ

ಆಸ್ತಿ ಖರೀದಿ, ಮಾರಾಟ ಅಥವಾ ಬ್ಯಾಂಕ್ ಗೃಹ ಸಾಲ (Home Loan) ಪಡೆಯುವಾಗ ಬಿಬಿಎಂಪಿ ನೀಡುವ ಈ ಎರಡೂ ದಾಖಲೆಗಳು ಅತ್ಯಗತ್ಯ:

---

### 📜 1. ಖಾತಾ ಪ್ರಮಾಣಪತ್ರ (Khata Certificate):
* **ಏನಿದು?:** ನಿರ್ದಿಷ್ಟ ಆಸ್ತಿ ಸಂಖ್ಯೆ (PID) ಮತ್ತು ಮಾಲೀಕರ ಹೆಸರು ಬಿಬಿಎಂಪಿ ಆಸ್ತಿ ನೋಂದಣಿ ಪುಸ್ತಕದಲ್ಲಿದೆ ಎಂದು ದೃಢೀಕರಿಸುವ ಅಧಿಕೃತ ಪ್ರಮಾಣಪತ್ರ.
* **ಬಳಕೆ:** ಬ್ಯಾಂಕ್ ಸಾಲಕ್ಕೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಲು, ಹೊಸ ವಿದ್ಯುತ್/ನೀರು ಸಂಪರ್ಕ ಪಡೆಯಲು ಮತ್ತು ಕಟ್ಟಡ ನಕ್ಷೆ ಮಂಜೂರಾತಿಗೆ (Building Plan) ಇದು ಕಡ್ಡಾಯ.

---

### 📑 2. ಖಾತಾ ಸಾರಾಂಶ (Khata Extract):
* **ಏನಿದು?:** ಆಸ್ತಿಯ ಸಂಪೂರ್ಣ ವಿವರಗಳಿರುವ ರಿಜಿಸ್ಟರ್ ಪುಟದ ನಕಲು ಪ್ರತಿ.
* **ಒಳಗೊಂಡಿರುವ ವಿವರಗಳು:** ನಿವೇಶನದ ನಿಖರ ಅಳತೆ (Dimensions), ಕಟ್ಟಡದ ವಿಸ್ತೀರ್ಣ (Built-up area), ವಸತಿ ಅಥವಾ ವಾಣಿಜ್ಯ ಬಳಕೆಯ ಸ್ವರೂಪ ಹಾಗೂ ನಿಗದಿಪಡಿಸಲಾದ ವಾರ್ಷಿಕ ಆಸ್ತಿ ತೆರಿಗೆ ಮೌಲ್ಯಮಾಪನ.
* **ಬಳಕೆ:** ಸಬ್-ರಿಜಿಸ್ಟ್ರಾರ್ ಕಚೇರಿಯಲ್ಲಿ ಆಸ್ತಿ ಮಾರಾಟ ಪತ್ರ ನೋಂದಣಿ ಮಾಡಲು ಇದು ಕಡ್ಡಾಯ.

💡 ಇವೆರಡನ್ನೂ [bbmpeaasthi.karnataka.gov.in](https://bbmpeaasthi.karnataka.gov.in) ಮೂಲಕ ಆನ್‌ಲೈನ್‌ನಲ್ಲೇ ಡಿಜಿಟಲ್ ಸಹಿಯೊಂದಿಗೆ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.""",
        "category": "REVENUE",
        "language": "kn",
        "source_url": "https://bbmpeaasthi.karnataka.gov.in",
        "keywords": "khata certificate vs khata extract difference, bbmp a khata extract online, e aasthi khata extract, ಖಾತಾ ಪ್ರಮಾಣಪತ್ರ, ಖಾತಾ ಸಾರಾಂಶ ವ್ಯತ್ಯಾಸ",
        "action_label": "🏢 BBMP e-Aasthi",
        "action_url": "https://bbmpeaasthi.karnataka.gov.in"
    },
    {
        "id": "faq_user_341",
        "question": "ಕಂದಾಯ ವಾರಸುದಾರಿಕೆ ಪ್ರಮಾಣಪತ್ರ (Legal Heir Certificate) ಮತ್ತು ಸಿವಿಲ್ ಕೋರ್ಟ್ ಸಕ್ಸೇಷನ್ ಪ್ರಮಾಣಪತ್ರದ (Succession Certificate) ನಡುವಿನ ವ್ಯತ್ಯಾಸವೇನು?",
        "normalized_question": "legal heir certificate vs succession certificate civil court bank claim ಕಂದಾಯ ವಾರಸುದಾರಿಕೆ vs ಸಕ್ಸೇಷನ್ ಸರ್ಟಿಫಿಕೇಟ್",
        "answer": """### ⚖️ ವಾರಸುದಾರಿಕೆ ಪ್ರಮಾಣಪತ್ರ vs ಸಕ್ಸೇಷನ್ ಸರ್ಟಿಫಿಕೇಟ್ — ಕಾನೂನು ಮಾರ್ಗದರ್ಶಿ

ವ್ಯಕ್ತಿಯು ಯಾವುದೇ ಉಯಿಲು (Will) ಬರೆಯದೆ ಮೃತಪಟ್ಟಾಗ ಅವರ ಆಸ್ತಿ ಮತ್ತು ಬ್ಯಾಂಕ್ ಠೇವಣಿ ಪಡೆಯಲು ಈ ದಾಖಲೆಗಳು ಬೇಕಾಗುತ್ತವೆ:

---

### 🏛️ 1. ಕಂದಾಯ ವಾರಸುದಾರಿಕೆ ಪ್ರಮಾಣಪತ್ರ (Legal Heir / Family Tree via Tahsildar):
* **ನೀಡುವ ಪ್ರಾಧಿಕಾರ:** ತಾಲೂಕು ತಹಶೀಲ್ದಾರ್ / ನಾಡಕಚೇರಿ (ಕಂದಾಯ ಇಲಾಖೆ).
* **ಉದ್ದೇಶ:** ಮೃತರ ಕೃಷಿ ಜಮೀನಿನ ಪಹಣಿ (RTC) ವರ್ಗಾವಣೆ, ಇ-ಖಾತಾ ವರ್ಗಾವಣೆ, ಅನುಕಂಪದ ನೌಕರಿ ಮತ್ತು ಸಣ್ಣ ಮೊತ್ತದ ಬ್ಯಾಂಕ್ ಕ್ಲೇಮ್‌ಗಳಿಗೆ ಅನ್ವಯ.
* **ಪಡೆಯುವ ಸಮಯ:** 15 ರಿಂದ 30 ದಿನಗಳು.

---

### ⚖️ 2. ಸಿವಿಲ್ ಕೋರ್ಟ್ ಸಕ್ಸೇಷನ್ ಪ್ರಮಾಣಪತ್ರ (Succession Certificate via Court):
* **ನೀಡುವ ಪ್ರಾಧಿಕಾರ:** ಸಿವಿಲ್ ಜಡ್ಜ್ ನ್ಯಾಯಾಲಯ (Civil Court under Indian Succession Act).
* **ಉದ್ದೇಶ:** ಮೃತರ ಹೆಸರಿನಲ್ಲಿರುವ ದೊಡ್ಡ ಮೊತ್ತದ ಬ್ಯಾಂಕ್ ಫಿಕ್ಸ್ಡ್ ಡೆಪಾಸಿಟ್ (FD), ಮ್ಯೂಚುಯಲ್ ಫಂಡ್, ಶೇರುಗಳು (Shares/Demat), ಜೀವ ವಿಮೆ ಮತ್ತು ಸಾಲಪತ್ರಗಳ ವಾರಸುದಾರಿಕೆ ವರ್ಗಾವಣೆಗೆ ಬ್ಯಾಂಕ್‌ಗಳು ಇದನ್ನು ಕಡ್ಡಾಯವಾಗಿ ಕೇಳುತ್ತವೆ.
* **ಪಡೆಯುವ ಸಮಯ:** ಪತ್ರಿಕಾ ಪ್ರಕಟಣೆ ಮತ್ತು ವಿಚಾರಣೆಯ ನಂತರ 3 ರಿಂದ 6 ತಿಂಗಳು.""",
        "category": "LEGAL",
        "language": "kn",
        "source_url": "https://karnatakajudiciary.kar.nic.in",
        "keywords": "legal heir vs succession certificate difference, tahsildar legal heir certificate, civil court succession act, ವಾರಸುದಾರಿಕೆ ಪ್ರಮಾಣಪತ್ರ, ಸಕ್ಸೇಷನ್ ಸರ್ಟಿಫಿಕೇಟ್",
        "action_label": "⚖️ ಹೈಕೋರ್ಟ್ ಪೋರ್ಟಲ್",
        "action_url": "https://karnatakajudiciary.kar.nic.in"
    },
    {
        "id": "faq_user_342",
        "question": "ಅನಾರೋಗ್ಯದಿಂದ ಮಲಗಿರುವ ವೃದ್ಧರು ಮತ್ತು ರೋಗಿಗಳಿಗೆ ಮನೆ ಬಾಗಿಲಿಗೆ ರೇಷನ್ ಕಾರ್ಡ್ ಇ-ಕೆವೈಸಿ (Home Visit e-KYC for Bedridden) ಸೌಲಭ್ಯ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "ration card ekyc bedridden senior citizen home visit ahara karnataka ಬಯೋಮೆಟ್ರಿಕ್ ರೇಷನ್ ಇ-ಕೆವೈಸಿ ಮನೆ ಭೇಟಿ",
        "answer": """### 🛒 ಅಶಕ್ತ ವೃದ್ಧರು & ರೋಗಿಗಳಿಗೆ ಮನೆ ಬಾಗಿಲಲ್ಲೇ ರೇಷನ್ ಇ-ಕೆವೈಸಿ ಸೌಲಭ್ಯ

ನ್ಯಾಯಬೆಲೆ ಅಂಗಡಿಗೆ ತೆರಳಿ ಬೆರಳಚ್ಚು ಬಯೋಮೆಟ್ರಿಕ್ ನೀಡಲು ಸಾಧ್ಯವಾಗದ ಹಾಸಿಗೆ ಹಿಡಿದ ವೃದ್ಧರು, ಕ್ಯಾನ್ಸರ್/ಪಾರ್ಶ್ವವಾಯು ರೋಗಿಗಳು ಮತ್ತು ಗಂಭೀರ ವಿಶೇಷ ಚೇತನರಿಗೆ ಆಹಾರ ಇಲಾಖೆಯ ವಿನಾಯಿತಿ ಮಾರ್ಗಸೂಚಿ:

---

### 📋 ಸೌಲಭ್ಯ ಪಡೆಯುವ ಹಂತಗಳು:
1. **ವೈದ್ಯಕೀಯ ಪ್ರಮಾಣಪತ್ರ:** ಸರ್ಕಾರಿ ಆಸ್ಪತ್ರೆಯ ವೈದ್ಯರಿಂದ ರೋಗಿಯು ಅಂಗಡಿಗೆ ಬರಲು ಅಸಮರ್ಥರಾಗಿದ್ದಾರೆ ಎಂಬ ವೈದ್ಯಕೀಯ ದೃಢೀಕರಣ ಪತ್ರ (Medical Fitness Certificate) ಪಡೆಯಿರಿ.
2. **ಆಹಾರ ಶಿರಸ್ತೇದಾರ್ ಭೇಟಿ:** ತಾಲೂಕು ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿಯ ಆಹಾರ ಶಾಖೆಗೆ (Food Inspector) ಲಿಖಿತ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.
3. **ಮನೆ ಬಾಗಿಲಿಗೆ ಬಯೋಮೆಟ್ರಿಕ್ ಯಂತ್ರ:** ಆಹಾರ ನಿರೀಕ್ಷಕರು (Food Inspector) ಅಥವಾ ನ್ಯಾಯಬೆಲೆ ಅಂಗಡಿ ಪ್ರತಿನಿಧಿಯು ಪೋರ್ಟಬಲ್ ಬಯೋಮೆಟ್ರಿಕ್/ಐರಿಸ್ (ಕಣ್ಣಿನ ಸ್ಕ್ಯಾನರ್) ಯಂತ್ರದೊಂದಿಗೆ ರೋಗಿಯ ಮನೆಗೆ ಖುದ್ದಾಗಿ ಭೇಟಿ ನೀಡಿ e-KYC ಪೂರ್ಣಗೊಳಿಸುತ್ತಾರೆ.
4. ಬೆರಳಚ್ಚು ಸಂಪೂರ್ಣವಾಗಿ ಸವೆದುಹೋಗಿದ್ದರೆ 'OTP ಆಧಾರಿತ ದೃಢೀಕರಣ' ಅಥವಾ ನಾಮಿನಿ (Nominee Authorization) ಮೂಲಕ ಪಡಿತರ ಪಡೆಯಲು ಅವಕಾಶ ನೀಡಲಾಗುತ್ತದೆ.""",
        "category": "FOOD",
        "language": "kn",
        "source_url": "https://ahara.kar.nic.in",
        "keywords": "ration card home visit ekyc, bedridden senior citizen ration biometric bypass, ahara food inspector home ekyc, ರೇಷನ್ ಇ-ಕೆವೈಸಿ ಮನೆ ಭೇಟಿ, ಆಹಾರ ಇಲಾಖೆ",
        "action_label": "🛒 ಆಹಾರ ಇಲಾಖೆ ಪೋರ್ಟಲ್",
        "action_url": "https://ahara.kar.nic.in"
    },
    {
        "id": "faq_user_343",
        "question": "ಕರ್ನಾಟಕ ವಾಹನ ಸ್ಕ್ರ್ಯಾಪ್ ನೀತಿ (Vehicle Scrappage Policy) ಯಡಿ ಹಳೆಯ ವಾಹನ ಸ್ಕ್ರ್ಯಾಪ್ ಮಾಡಿ ಹೊಸ ವಾಹನ ಖರೀದಿಗೆ ತೆರಿಗೆ ರಿಯಾಯಿತಿ ಪಡೆಯುವುದು ಹೇಗೆ?",
        "normalized_question": "vehicle scrappage policy karnataka road tax concession certificate of deposit rvsf ವಾಹನ ಸ್ಕ್ರ್ಯಾಪ್ ನೀತಿ ರಿಯಾಯಿತಿ",
        "answer": """### 🚗 ಕರ್ನಾಟಕ ವಾಹನ ಸ್ಕ್ರ್ಯಾಪ್ ನೀತಿ — ಹೊಸ ವಾಹನ ತೆರಿಗೆ ರಿಯಾಯಿತಿ ಮಾರ್ಗದರ್ಶಿ

15 ವರ್ಷ ಮೀರಿದ ಹಳೆಯ ಮಾಲಿನ್ಯಕಾರಕ ವಾಹನಗಳನ್ನು ಅಧಿಕೃತ ವಾಹನ ಸ್ಕ್ರ್ಯಾಪಿಂಗ್ ಕೇಂದ್ರದಲ್ಲಿ (RVSF - Registered Vehicle Scrapping Facility) ಗುಜರಿಗೆ ಹಾಕಿದಾಗ ಸರ್ಕಾರ ಭಾರಿ ತೆರಿಗೆ ರಿಯಾಯಿತಿ ನೀಡುತ್ತದೆ.

---

### 💰 ಸಿಗುವ ಪ್ರಮುಖ ಆರ್ಥಿಕ ಲಾಭಗಳು:
* **ರೋಡ್ ಟ್ಯಾಕ್ಸ್ ರಿಯಾಯಿತಿ (Motor Vehicle Tax Concession):** ಸ್ಕ್ರ್ಯಾಪ್ ಮಾಡಿದ ನಂತರ ಸಿಗುವ **Certificate of Deposit (CD)** ಬಳಸಿ ಹೊಸ ವಾಹನ ಖರೀದಿಸಿದರೆ ನೋಂದಣಿ ತೆರಿಗೆಯಲ್ಲಿ **25% (ಖಾಸಗಿ ಕಾರು/ಬೈಕ್)** ಹಾಗೂ **15% (ವಾಣಿಜ್ಯ ವಾಹನಗಳಿಗೆ)** ರಿಯಾಯಿತಿ ಸಿಗುತ್ತದೆ.
* **ಸ್ಕ್ರ್ಯಾಪ್ ಮೌಲ್ಯ (Scrap Value):** ಹಳೆಯ ವಾಹನದ ತೂಕಕ್ಕೆ ತಕ್ಕಂತೆ ವಾಹನ ತಯಾರಕ ಎಕ್ಸ್-ಶೋರೂಂ ಬೆಲೆಯ 4% ರಿಂದ 6% ನಷ್ಟು ಹಣವನ್ನು ಸ್ಕ್ರ್ಯಾಪ್ ಕೇಂದ್ರವೇ ನೇರವಾಗಿ ನೀಡುತ್ತದೆ.
* ಹೊಸ ವಾಹನ ಖರೀದಿಸುವಾಗ ಶೋರೂಂಗಳು 5% ಹೆಚ್ಚುವರಿ ರಿಯಾಯಿತಿ ನೀಡುತ್ತವೆ.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [vscrap.parivahan.gov.in](https://vscrap.parivahan.gov.in)""",
        "category": "TRANSPORT",
        "language": "kn",
        "source_url": "https://transport.karnataka.gov.in",
        "keywords": "vehicle scrappage policy karnataka, certificate of deposit tax concession, rvsf scrap centre, ವಾಹನ ಸ್ಕ್ರ್ಯಾಪ್ ನೀತಿ, ರೋಡ್ ಟ್ಯಾಕ್ಸ್ ರಿಯಾಯಿತಿ",
        "action_label": "🚗 ಪರಿವಾಹನ್ V-Scrap",
        "action_url": "https://vscrap.parivahan.gov.in"
    },
    {
        "id": "faq_user_344",
        "question": "ರಾತ್ರಿ 10 ಗಂಟೆಯ ನಂತರ ಧ್ವನಿವರ್ಧಕ (Loudspeaker Noise Pollution) ಕಿರಿಕಿರಿ ಉಂಟಾದರೆ 112 ಗೆ ದೂರು ನೀಡುವುದು ಹೇಗೆ?",
        "normalized_question": "noise pollution complaint 112 loudspeaker ban after 10 pm ksp police decibel limit ಶಬ್ದ ಮಾಲಿನ್ಯ ದೂರು ಧ್ವನಿವರ್ಧಕ",
        "answer": """### 🔇 ಶಬ್ದ ಮಾಲಿನ್ಯ ನಿಯಂತ್ರಣ ಕಾಯ್ದೆ & ರಾತ್ರಿ ಧ್ವನಿವರ್ಧಕ ನಿಷೇಧ (Noise Pollution Rules)

ಸುಪ್ರೀಂ ಕೋರ್ಟ್ ಮತ್ತು ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್ ಆದೇಶಗಳ ಅನ್ವಯ, ಸಾರ್ವಜನಿಕ ಶಾಂತಿಗೆ ಭಂಗ ತರದಂತೆ ರಾತ್ರಿ ವೇಳೆಯಲ್ಲಿ ಧ್ವನಿವರ್ಧಕಗಳ ಬಳಕೆಗೆ ಕಟ್ಟುನಿಟ್ಟಾದ ನಿರ್ಬಂಧವಿದೆ.

---

### ⏰ ನಿಷೇಧಿತ ಸಮಯ & ಡೆಸಿಬಲ್ ಮಿತಿ:
* **ರಾತ್ರಿ 10:00 ರಿಂದ ಬೆಳಗ್ಗೆ 06:00 ರವರೆಗೆ:** ಸಾರ್ವಜನಿಕ ಸ್ಥಳಗಳಲ್ಲಿ, ಕಲ್ಯಾಣ ಮಂಟಪ, ಪಬ್, ಬಾರ್ ಅಥವಾ ಧಾರ್ಮಿಕ ಕೇಂದ್ರಗಳಲ್ಲಿ ಧ್ವನಿವರ್ಧಕಗಳು (Loudspeakers), ಪಟಾಕಿ ಮತ್ತು ಡಿಜೆ (DJ Music) ಬಳಕೆಯನ್ನು ಸಂಪೂರ್ಣವಾಗಿ ನಿಷೇಧಿಸಲಾಗಿದೆ.
* ವಸತಿ ಪ್ರದೇಶಗಳಲ್ಲಿ ಹಗಲು ಹೊತ್ತಿನಲ್ಲಿ ಗರಿಷ್ಠ 55 dB ಹಾಗೂ ರಾತ್ರಿ ವೇಳೆ 45 dB ಮೀರಬಾರದು.

---

### 📞 ತಕ್ಷಣ ದೂರು ನೀಡುವ ವಿಧಾನ:
* ಶಬ್ದ ಮಾಲಿನ್ಯ ಉಂಟಾದ ತಕ್ಷಣ **ಕರ್ನಾಟಕ ಪೊಲೀಸ್ ತುರ್ತು ಸಹಾಯವಾಣಿ: 112** ಗೆ ಕರೆ ಮಾಡಿ ಸ್ಥಳ ತಿಳಿಸಿ.
* ಪೊಲೀಸರು ಹೊಯ್ಸಳ ವಾಹನದೊಂದಿಗೆ ಸ್ಥಳಕ್ಕೆ ಬಂದು ಸೌಂಡ್ ಸಿಸ್ಟಮ್ ಜಪ್ತಿ ಮಾಡಿ ಮಾಲೀಕರ ವಿರುದ್ಧ ಪರಿಸರ ಸಂರಕ್ಷಣಾ ಕಾಯ್ದೆಯಡಿ ಪ್ರಕರಣ ದಾಖಲಿಸುತ್ತಾರೆ.""",
        "category": "POLICE",
        "language": "kn",
        "source_url": "https://ksp.karnataka.gov.in",
        "keywords": "noise pollution complaint 112, loudspeaker ban after 10 pm bangalore, decibel limit residential area, ಶಬ್ದ ಮಾಲಿನ್ಯ ದೂರು, ರಾತ್ರಿ ಧ್ವನಿವರ್ಧಕ ನಿಷೇಧ",
        "action_label": "👮 ಪೊಲೀಸ್ 112 ತುರ್ತು ಸೇವೆ",
        "action_url": "https://ksp.karnataka.gov.in"
    },
    {
        "id": "faq_user_345",
        "question": "ಬೆಂಗಳೂರಿನಲ್ಲಿ ಒಳಚರಂಡಿ ಬ್ಲಾಕ್ ಆದರೆ (Sanitary Sewage Blockage) ಜಲ ಮಂಡಳಿಯ ಜೆಟ್ಟಿಂಗ್ ಯಂತ್ರ (Jetting Machine) ಬುಕ್ ಮಾಡುವುದು ಹೇಗೆ?",
        "normalized_question": "bwssb sanitary sewage overflow blockage jetting machine booking 1916 ಒಳಚರಂಡಿ ಬ್ಲಾಕ್ ಜೆಟ್ಟಿಂಗ್ ಮೆಷಿನ್",
        "answer": """### 🚰 BWSSB ಒಳಚರಂಡಿ ಬ್ಲಾಕ್ & ಜೆಟ್ಟಿಂಗ್ ಯಂತ್ರ ಬುಕಿಂಗ್ (Sanitary Grievance)

ಮನೆಯ ಮುಂಭಾಗದ ಒಳಚರಂಡಿ ಮ್ಯಾನ್‌ಹೋಲ್ ಉಕ್ಕಿ ಹರಿಯುತ್ತಿದ್ದರೆ (Sewage Overflow) ಅಥವಾ ಸ್ಯಾನಿಟರಿ ಲೈನ್ ಬ್ಲಾಕ್ ಆಗಿದ್ದರೆ ಜಲ ಮಂಡಳಿಯ ಹೈಡ್ರಾಲಿಕ್ ಜೆಟ್ಟಿಂಗ್-ಸಕ್ಕಿಂಗ್ ವಾಹನವನ್ನು ಬಳಸಬಹುದು.

---

### 📞 ದೂರು & ಬುಕಿಂಗ್ ಪ್ರಕ್ರಿಯೆ:
1. **BWSSB 24x7 ಕಾಲ್ ಸೆಂಟರ್:** **1916** ಗೆ ಕರೆ ಮಾಡಿ ನಿಮ್ಮ ಆಸ್ತಿಯ RR ಸಂಖ್ಯೆ ಮತ್ತು ವಿಳಾಸ ನೀಡಿ 'Sewage Blockage Grievance' ದಾಖಲಿಸಿ.
2. **ಸೇವಾ ವಾಹನ ಆಗಮನ:** ಜಲ ಮಂಡಳಿಯ ವಾರ್ಡ್ ಸ್ಯಾನಿಟರಿ ಇಂಜಿನಿಯರ್ ಉಸ್ತುವಾರಿಯಲ್ಲಿ ಹೈ-ಪ್ರೆಶರ್ ಜೆಟ್ಟಿಂಗ್ ಮೆಷಿನ್ (Jetting & Sucking Machine) ಬಂದು ಮ್ಯಾನ್‌ಹೋಲ್ ಕಲ್ಮಶವನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸುತ್ತದೆ.
3. ಸಾರ್ವಜನಿಕ ಮುಖ್ಯ ಒಳಚರಂಡಿ ಲೈನ್ ಸ್ವಚ್ಛತೆಗೆ ಯಾವುದೇ ಪ್ರತ್ಯೇಕ ಶುಲ್ಕವಿರುವುದಿಲ್ಲ (ಉಚಿತ ಸೇವೆ).

⚠️ ಯಾವುದೇ ಕಾರಣಕ್ಕೂ ಮಾನವ ಚರಂಡಿ ಸ್ವಚ್ಛತೆ (Manual Scavenging) ಮಾಡಿಸಬೇಡಿ; ಇದು ಕಾನೂನುಬಾಹಿರ ಮತ್ತು ಶಿಕ್ಷಾರ್ಹ ಅಪರಾಧ.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://bwssb.karnataka.gov.in",
        "keywords": "bwssb sanitary blockage complaint, sewage overflow jetting machine 1916, sanitary manhole cleaning bangalore, ಒಳಚರಂಡಿ ಬ್ಲಾಕ್ ದೂರು, ಜಲಮಂಡಳಿ ಜೆಟ್ಟಿಂಗ್",
        "action_label": "🚰 BWSSB ದೂರು ಪೋರ್ಟಲ್",
        "action_url": "https://bwssb.karnataka.gov.in"
    },
    {
        "id": "faq_user_346",
        "question": "ಬಿಬಿಎಂಪಿ ವಾಣಿಜ್ಯ ಪರವಾನಗಿ (BBMP Trade License) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ನವೀಕರಿಸುವುದು ಹೇಗೆ? ವಿಳಂಬ ದಂಡದ ನಿಯಮಗಳೇನು?",
        "normalized_question": "bbmp trade license renewal online fee penalty march deadline ಬಿಬಿಎಂಪಿ ಟ್ರೇಡ್ ಲೈಸೆನ್ಸ್ ನವೀಕರಣ",
        "answer": """### 🏢 BBMP ವಾಣಿಜ್ಯ ಪರವಾನಗಿ ನವೀಕರಣ ಮಾರ್ಗದರ್ಶಿ (Trade License Renewal)

ಬೆಂಗಳೂರು ನಗರದಲ್ಲಿ ಅಂಗಡಿ, ಹೋಟೆಲ್, ಸೂಪರ್‌ಮಾರ್ಕೆಟ್, ಸಾಫ್ಟ್‌ವೇರ್ ಕಚೇರಿ ಅಥವಾ ಯಾವುದೇ ವ್ಯಾಪಾರ ಸಂಸ್ಥೆ ನಡೆಸಲು ಬಿಬಿಎಂಪಿಯಿಂದ ಟ್ರೇಡ್ ಲೈಸೆನ್ಸ್ ಹೊಂದಿರುವುದು ಮತ್ತು ಪ್ರತಿವರ್ಷ ನವೀಕರಿಸುವುದು ಕಡ್ಡಾಯ.

---

### 📅 ನವೀಕರಣ ಅವಧಿ & ದಂಡ:
* **ಸಾಮಾನ್ಯ ನವೀಕರಣ ಅವಧಿ:** ಪ್ರತಿ ವರ್ಷ **ಜನವರಿ 1 ರಿಂದ ಫೆಬ್ರವರಿ 28 ರವರೆಗೆ** ಯಾವುದೇ ದಂಡವಿಲ್ಲದೆ ನವೀಕರಿಸಬಹುದು.
* **ಮಾರ್ಚ್ 1 ರಿಂದ 31 ರವರೆಗೆ:** 25% ವಿಳಂಬ ದಂಡ.
* **ಏಪ್ರಿಲ್ 1 ರ ನಂತರ:** 50% ದಂಡ + ವ್ಯಾಪಾರ ಮುಚ್ಚುವ ನೋಟಿಸ್ (Closure Notice).

---

### 💻 ಆನ್‌ಲೈನ್ ನವೀಕರಣ ಹಂತಗಳು:
1. [tradelicense.bbmp.gov.in](https://tradelicense.bbmp.gov.in) ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ.
2. ನಿಮ್ಮ ಹಿಂದಿನ Trade License Number ನಮೂದಿಸಿ ವಿವರ ಪರಿಶೀಲಿಸಿ.
3. ಆಸ್ತಿಯ ಇತ್ತೀಚಿನ ಆಸ್ತಿ ತೆರಿಗೆ ರಶೀದಿ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
4. ಆನ್‌ಲೈನ್ ಶುಲ್ಕ ಪಾವತಿಸಿದ ತಕ್ಷಣ ಕ್ಯೂಆರ್ ಕೋಡ್ ಇರುವ ನವೀಕೃತ **Digital Trade License Certificate** ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.""",
        "category": "CIVIC",
        "language": "kn",
        "source_url": "https://tradelicense.bbmp.gov.in",
        "keywords": "bbmp trade license renewal online, trade license fee calculation, trade license penalty march, ಬಿಬಿಎಂಪಿ ಟ್ರೇಡ್ ಲೈಸೆನ್ಸ್ ನವೀಕರಣ, ವಾಣಿಜ್ಯ ಪರವಾನಗಿ",
        "action_label": "🏢 BBMP Trade License",
        "action_url": "https://tradelicense.bbmp.gov.in"
    },
    {
        "id": "faq_user_347",
        "question": "ಕರ್ನಾಟಕ ಹೈಕೋರ್ಟ್‌ನಲ್ಲಿ ಇ-ಫೈಲಿಂಗ್ 3.0 (e-Filing 3.0) ಮೂಲಕ ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಸ್ವತಃ ಕೇಸ್ ದಾಖಲಿಸುವುದು ಹೇಗೆ?",
        "normalized_question": "high court karnataka efiling 3.0 party in person case registration online ಇ-ಫೈಲಿಂಗ್ ಹೈಕೋರ್ಟ್ ಕೇಸ್ ದಾಖಲು",
        "answer": """### ⚖️ ಕರ್ನಾಟಕ ನ್ಯಾಯಾಂಗ ಇ-ಫೈಲಿಂಗ್ 3.0 (e-Filing 3.0 Portal)

ವಕೀಲರು ಹಾಗೂ ಸಾರ್ವಜನಿಕರು (Party-in-Person) ಕೋರ್ಟ್‌ಗೆ ಖುದ್ದಾಗಿ ಹಾಜರಾಗದೆ ಆನ್‌ಲೈನ್‌ನಲ್ಲೇ ರಿಟ್ ಅರ್ಜಿ (Writ Petition), ಸಿವಿಲ್ ಮತ್ತು ಕ್ರಿಮಿನಲ್ ಮೊಕದ್ದಮೆಗಳನ್ನು ದಾಖಲಿಸುವ ಅತ್ಯಾಧುನಿಕ ಡಿಜಿಟಲ್ ಪೋರ್ಟಲ್.

---

### 💻 ಆನ್‌ಲೈನ್ ಕೇಸ್ ಫೈಲಿಂಗ್ ಹಂತಗಳು:
1. **ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [efiling.ecourts.gov.in](https://efiling.ecourts.gov.in)
2. ಆಧಾರ್ ಮತ್ತು ಮೊಬೈಲ್ ಒಟಿಪಿ ಮೂಲಕ ಸೈನ್ ಅಪ್ ಆಗಿ 'Litigant / Advocate' ಪ್ರೊಫೈಲ್ ರಚಿಸಿ.
3. ನ್ಯಾಯಾಲಯವನ್ನು **'High Court of Karnataka (Principal Bench Bengaluru / Dharwad / Kalaburagi)'** ಎಂದು ಆಯ್ಕೆಮಾಡಿ.
4. ಅರ್ಜಿ (Petition), ಅಫಿಡವಿಟ್ ಮತ್ತು ಸಾಕ್ಷ್ಯಾಧಾರಗಳ PDF ಗಳನ್ನು OCR (Searchable PDF) ಫಾರ್ಮ್ಯಾಟ್‌ನಲ್ಲಿ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.
5. ಇ-ಕೋರ್ಟ್ ಫೀ (Online Court Fee) ಪಾವತಿಸಿ ಡಿಜಿಟಲ್ ಸಹಿ (e-Sign) ಮಾಡಿ ಸಬ್ಮಿಟ್ ಮಾಡಿ.
6. ರಿಜಿಸ್ಟ್ರಾರ್ ಸ್ಕ್ರೂಟಿನಿ ಮುಗಿದ 24 ಗಂಟೆಗಳಲ್ಲಿ ನಿಮ್ಮ ಕೇಸ್ ನಂಬರ್ (Case Number & FR Number) ಜನರೇಟ್ ಆಗುತ್ತದೆ.""",
        "category": "LEGAL",
        "language": "kn",
        "source_url": "https://efiling.ecourts.gov.in",
        "keywords": "karnataka high court efiling 3.0, party in person online petition filing, ecourts efiling portal, ಇ-ಫೈಲಿಂಗ್ ಹೈಕೋರ್ಟ್, ಆನ್‌ಲೈನ್ ಕೇಸ್ ದಾಖಲು",
        "action_label": "⚖️ e-Filing ಪೋರ್ಟಲ್",
        "action_url": "https://efiling.ecourts.gov.in"
    }
]

def generate_seed_sql():
    statements = []
    statements.append("DELETE FROM ai_faq WHERE id LIKE 'faq_%';")
    statements.append("DELETE FROM ai_documents WHERE id LIKE 'doc_%';")
    
    for f in FAQS:
        q = f["question"].replace("'", "''")
        nq = f["normalized_question"].replace("'", "''")
        ans = f["answer"].replace("'", "''")
        cat = f["category"].replace("'", "''")
        lang = f["language"].replace("'", "''")
        s_url = f.get("source_url", "").replace("'", "''")
        kw = f.get("keywords", "").replace("'", "''")
        al = f.get("action_label", "").replace("'", "''")
        au = f.get("action_url", "").replace("'", "''")
        
        sql = f"""INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('{f["id"]}', '{q}', '{nq}', '{ans}', '{cat}', '{lang}', '{s_url}', '{kw}', '{al}', '{au}');"""
        statements.append(sql)
        
    for d in DOCUMENTS:
        title = d["title"].replace("'", "''")
        content = d["content"].replace("'", "''")
        url = d.get("url", "").replace("'", "''")
        cat = d.get("category", "GENERAL").replace("'", "''")
        st = d.get("source_type", "karnata").replace("'", "''")
        su = d.get("source_url", "").replace("'", "''")
        kw = d.get("keywords", "").replace("'", "''")
        
        sql = f"""INSERT INTO ai_documents (id, title, content, url, category, source_type, source_url, keywords)
VALUES ('{d["id"]}', '{title}', '{content}', '{url}', '{cat}', '{st}', '{su}', '{kw}');"""
        statements.append(sql)
        
    MIGRATIONS_DIR.mkdir(parents=True, exist_ok=True)
    out_file = MIGRATIONS_DIR / "0002_seed_ai_knowledge.sql"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(statements))
        
    print("=" * 60)
    print(f"✅ Generated SQL seed migration: {out_file}")
    print(f"📊 Total High-Quality FAQs Seeded: {len(FAQS)}")
    print(f"📚 Total Knowledge Documents Seeded: {len(DOCUMENTS)}")
    print("=" * 60)
    return out_file

if __name__ == "__main__":
    generate_seed_sql()