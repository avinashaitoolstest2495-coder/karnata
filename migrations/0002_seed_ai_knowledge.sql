DELETE FROM ai_faq WHERE id LIKE 'faq_%';
DELETE FROM ai_documents WHERE id LIKE 'doc_%';
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_sir_001', 'SIR ಎಂದರೇನು? ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯಲ್ಲಿ ಹೆಸರು ಹೇಗೆ ಪರಿಶೀಲಿಸುವುದು?', 'sir ಎಂದರೇನು ಕರಡು ಮತದಾರರ ಪಟ್ಟಿ ಹೆಸರು ಹೇಗೆ ಪರಿಶೀಲಿಸುವುದು what is sir check draft roll', '### 🗳️ SIR (Special Summary Revision) ಮತ್ತು ಕರಡು ಮತದಾರರ ಪಟ್ಟಿ ಪರಿಶೀಲನೆ

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

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [ceokarnataka.kar.nic.in](https://ceokarnataka.kar.nic.in) | **ಸಹಾಯವಾಣಿ:** 1950', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'sir, eci, summary revision, draft roll, ಕರಡು, ಮತದಾರ, ಪರಿಷ್ಕರಣೆ, ಹೆಸರು, ಪರಿಶೀಲಿಸುವುದು, voter list', '🔎 SIR Draft Roll ಪರಿಶೀಲಿಸಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_sir_002', 'ಹೊಸದಾಗಿ ವೋಟರ್ ಐಡಿಗೆ (Form 6) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸುವುದು ಹೇಗೆ?', 'ಹೊಸ ವೋಟರ್ ಐಡಿ ಅರ್ಜಿ form 6 apply new voter id registration online', '### 📝 ಹೊಸ ಮತದಾರರ ಗುರುತಿನ ಚೀಟಿ ನೋಂದಣಿ (Form 6)

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

💡 **ಸಲಹೆ:** ನಿಮ್ಮ ನೋಂದಾಯಿತ ಮೊಬೈಲ್ ಮೂಲಕವೇ e-EPIC ಡಿಜಿಟಲ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.', 'SIR', 'kn', 'https://voters.eci.gov.in', 'form 6, new voter id, apply voter card, ಹೊಸ ಮತದಾರರ ಗುರುತಿನ ಚೀಟಿ, ನೋಂದಣಿ', '🌐 Form 6 ಅರ್ಜಿ ಸಲ್ಲಿಸಿ', 'https://voters.eci.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_sir_003', 'ವೋಟರ್ ಐಡಿಯಲ್ಲಿ ವಿಳಾಸ ಬದಲಾವಣೆ, ಹೆಸರು ತಿದ್ದುಪಡಿ (Form 8) ಮಾಡುವುದು ಹೇಗೆ?', 'ವೋಟರ್ ಐಡಿ ಹೆಸರು ವಿಳಾಸ ತಿದ್ದುಪಡಿ form 8 correction voter id shifting address update', '### 🛠️ ವೋಟರ್ ಐಡಿ ತಿದ್ದುಪಡಿ ಮತ್ತು ಸ್ಥಳಾಂತರ ಪ್ರಕ್ರಿಯೆ (Form 8)

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
4. ಸೂಕ್ತ ಅಧಿಕೃತ ಪೂರಕ ದಾಖಲೆಯನ್ನು (ಆಧಾರ್/ವಿದ್ಯುತ್ ಬಿಲ್/ಗೆಜೆಟ್ ನೋಟಿಫಿಕೇಶನ್) ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ಸಬ್ಮಿಟ್ ಮಾಡಿ.', 'SIR', 'kn', 'https://voters.eci.gov.in', 'form 8, voter id correction, address change, name correction, ತಿದ್ದುಪಡಿ, ವಿಳಾಸ ಬದಲಾವಣೆ', '✏️ Form 8 ತಿದ್ದುಪಡಿ ಮಾಡಿ', 'https://voters.eci.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_sir_004', 'ಡಿಜಿಟಲ್ ವೋಟರ್ ಐಡಿ (e-EPIC) ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡುವುದು ಹೇಗೆ?', 'e-epic download digital voter card online pdf ವೋಟರ್ ಕಾರ್ಡ್ ಡೌನ್‌ಲೋಡ್', '### 📱 ಅಧಿಕೃತ e-EPIC (ಡಿಜಿಟಲ್ ಮತದಾರರ ಚೀಟಿ) ಡೌನ್‌ಲೋಡ್

e-EPIC ಎಂಬುದು ಭಾರತೀಯ ಚುನಾವಣಾ ಆಯೋಗವು ಅಧಿಕೃತವಾಗಿ ನೀಡುವ ಸುರಕ್ಷಿತ PDF ಆವೃತ್ತಿಯ ಮತದಾರರ ಗುರುತಿನ ಚೀಟಿಯಾಗಿದ್ದು, ಭೌತಿಕ ಕಾರ್ಡ್‌ನಷ್ಟೇ ಸಂಪೂರ್ಣ ಕಾನೂನು ಮಾನ್ಯತೆ ಹೊಂದಿದೆ.

---

### 📥 e-EPIC ಡೌನ್‌ಲೋಡ್ ಮಾಡುವ ವಿಧಾನ:
1. **ವೆಬ್‌ಸೈಟ್ ಪ್ರವೇಶಿಸಿ:** [voters.eci.gov.in](https://voters.eci.gov.in)
2. ಮುಖಪುಟದಲ್ಲಿರುವ **''E-EPIC Download''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ **EPIC ಸಂಖ್ಯೆ** ಅಥವಾ Form 6 **Reference No.** ನಮೂದಿಸಿ, ರಾಜ್ಯವನ್ನು **''Karnataka''** ಎಂದು ಆಯ್ಕೆಮಾಡಿ.
4. ನಿಮ್ಮ ನೋಂದಾಯಿತ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಗೆ 6 ಅಂಕಿಗಳ **OTP** ರವಾನೆಯಾಗುತ್ತದೆ.
5. OTP ನಮೂದಿಸಿ ದೃಢೀಕರಿಸಿ **''Download e-EPIC''** ಕ್ಲಿಕ್ ಮಾಡಿ.

💡 **ಗಮನಿಸಿ:** ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆಗೆ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಲಿಂಕ್ ಆಗಿರದಿದ್ದರೆ, ಮೊದಲು **Form 8** ಸಲ್ಲಿಸಿ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಅಪ್‌ಡೇಟ್ ಮಾಡಿಕೊಳ್ಳಬೇಕು.', 'SIR', 'kn', 'https://voters.eci.gov.in', 'e-epic, digital voter id, download epic, ವೋಟರ್ ಕಾರ್ಡ್ ಡೌನ್‌ಲೋಡ್, ಇ ಎಪಿಕ್', '📥 e-EPIC ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ', 'https://voters.eci.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_sir_005', 'ನನ್ನ ಮತಗಟ್ಟೆ (Polling Booth) ಮತ್ತು BLO ಅಧಿಕಾರಿಯ ವಿವರ ಪತ್ತೆಹಚ್ಚುವುದು ಹೇಗೆ?', 'find my blo booth polling station ಮತಗಟ್ಟೆ ಅಧಿಕಾರಿ ವಿವರ', '### 📍 ನಿಮ್ಮ ಮತಗಟ್ಟೆ ಮತ್ತು BLO (Booth Level Officer) ಮಾಹಿತಿ ಪಡೆಯುವುದು

ಪ್ರತಿ ಮತಗಟ್ಟೆ ವ್ಯಾಪ್ತಿಗೆ ಸ್ಥಳೀಯ ಮತದಾರರ ಪಟ್ಟಿ ಉಸ್ತುವಾರಿಗಾಗಿ ಒಬ್ಬ ಸರ್ಕಾರಿ ಅಧಿಕಾರಿಯನ್ನು (BLO) ನಿಯೋಜಿಸಲಾಗಿರುತ್ತದೆ.

---

### 🔍 BLO ಹಾಗೂ ಮತಗಟ್ಟೆ ತಿಳಿಯುವ 3 ಸುಲಭ ವಿಧಾನಗಳು:
1. **ಆನ್‌ಲೈನ್ ಪೋರ್ಟಲ್:** [electoralsearch.eci.gov.in](https://electoralsearch.eci.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ನಮೂದಿಸಿ ''Know Your Polling Officer'' ಕ್ಲಿಕ್ ಮಾಡಿ.
2. **ECI Voter Helpline App:** ಆ್ಯಪ್‌ನಲ್ಲಿ ''Know Your BLO/ERO'' ವಿಭಾಗಕ್ಕೆ ಹೋಗಿ EPIC ಹಾಕಿ.
3. **SMS ಸೌಲಭ್ಯ:** ನಿಮ್ಮ ಮೊಬೈಲ್‌ನಿಂದ `ECIBLO <ಸ್ಪೇಸ್> <EPIC ಸಂಖ್ಯೆ>` ಎಂದು ಟೈಪ್ ಮಾಡಿ **1950** ಸಂಖ್ಯೆಗೆ ಕಳುಹಿಸಿ.

ಇಲ್ಲಿ ನಿಮ್ಮ ಮತಗಟ್ಟೆಯ ಹೆಸರು, ಕೊಠಡಿ ಸಂಖ್ಯೆ, BLO ಹೆಸರು ಹಾಗೂ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಲಭ್ಯವಾಗುತ್ತದೆ.', 'SIR', 'kn', 'https://electoralsearch.eci.gov.in', 'blo contact, polling booth, voting center, ಬಿಎಲ್ಒ, ಮತಗಟ್ಟೆ', '🔍 BLO ವಿವರ ಹುಡುಕಿ', 'https://electoralsearch.eci.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_sir_006', 'ಮೃತಪಟ್ಟವರ ಅಥವಾ ಶಾಶ್ವತ ಸ್ಥಳಾಂತರಗೊಂಡವರ ಹೆಸರು ಮತದಾರರ ಪಟ್ಟಿಯಿಂದ ರದ್ದುಪಡಿಸುವುದು ಹೇಗೆ (Form 7)?', 'ಮತದಾರರ ಪಟ್ಟಿ ಹೆಸರು ತೆಗೆದುಹಾಕುವುದು form 7 deletion dead voter shifting objection', '### ❌ ಮತದಾರರ ಪಟ್ಟಿಯಿಂದ ಹೆಸರು ರದ್ದುಗೊಳಿಸುವ ಪ್ರಕ್ರಿಯೆ (Form 7)

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
3. ಮರಣ ಪ್ರಮಾಣಪತ್ರವನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ಸಬ್ಮಿಟ್ ಮಾಡಿ. ಸ್ಥಳೀಯ BLO ಪರಿಶೀಲನೆ ನಡೆಸಿ ಹೆಸರು ರದ್ದುಪಡಿಸುತ್ತಾರೆ.', 'SIR', 'kn', 'https://voters.eci.gov.in', 'form 7, delete voter, dead voter deletion, ಹೆಸರು ತೆಗೆಯುವುದು, ಮೃತ ಮತದಾರ', '📄 Form 7 ವಿವರ ನೋಡಿ', 'https://voters.eci.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_sch_007', 'ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆ: ₹2,000 DBT ಸ್ಥಿತಿ ನೋಡುವುದು ಹೇಗೆ? ಹಣ ಬಾರದಿದ್ದರೆ ಪರಿಹಾರವೇನು?', 'ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆ ಯಾರು ಅರ್ಹರು dbt ಸ್ಥಿತಿ gruha lakshmi scheme amount eligibility bank aadhaar', '### 🌸 ಗೃಹಲಕ್ಷ್ಮಿ ಯೋಜನೆ (Gruha Lakshmi Scheme) — ₹2,000 ಮಾಸಿಕ ನೆರವು

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
* **ಹಣ ಬಂದಿರುವ ಸ್ಥಿತಿ ತಿಳಿಯಲು:** Google Play Store ನಿಂದ ಅಧಿಕೃತ **''DBT Karnataka''** ಆ್ಯಪ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ ನಿಮ್ಮ ಆಧಾರ್ ಸಂಖ್ಯೆ ಹಾಕಿ ತಿಂಗಳಾವಾರು ಪಾವತಿ ವಿವರಗಳನ್ನು ನೇರವಾಗಿ ಪರಿಶೀಲಿಸಿ.

🔗 **ಅಧಿಕೃತ ಪೋರ್ಟಲ್:** [sevasindhugs.karnataka.gov.in](https://sevasindhugs.karnataka.gov.in) | **ಸಹಾಯವಾಣಿ:** 1902', 'SCHEME', 'kn', 'https://sevasindhugs.karnataka.gov.in', 'gruha lakshmi, 2000 dbt, ಗೃಹಲಕ್ಷ್ಮಿ, ಯಜಮಾನಿ ಮಹಿಳೆ, ಗ್ಯಾರಂಟಿ ಯೋಜನೆ, ಅರ್ಹರು, dbt, npci', '📜 ಗೃಹಲಕ್ಷ್ಮಿ ವಿವರ ನೋಡಿ', '/guarantee-schemes.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_sch_008', 'ಗೃಹಜ್ಯೋತಿ ಯೋಜನೆ: 200 ಯೂನಿಟ್ ಉಚಿತ ವಿದ್ಯುತ್ ಲೆಕ್ಕಾಚಾರ ಹೇಗೆ? ಶೂನ್ಯ ಬಿಲ್ ಪಡೆಯುವುದು ಹೇಗೆ?', 'ಗೃಹಜ್ಯೋತಿ 200 ಯೂನಿಟ್ ಲೆಕ್ಕಾಚಾರ gruha jyothi calculation 200 units free electricity zero bill', '### ⚡ ಗೃಹಜ್ಯೋತಿ ಯೋಜನೆ (Gruha Jyothi Scheme) — ಉಚಿತ ವಿದ್ಯುತ್ ನಿಯಮಗಳು

ಕರ್ನಾಟಕದ ಎಲ್ಲಾ ಮನೆಬಳಕೆಯ ಗ್ರಾಹಕರಿಗೆ ಮಾಸಿಕ ಗರಿಷ್ಠ **200 ಯೂನಿಟ್‌ವರೆಗೆ** ಉಚಿತ ವಿದ್ಯುತ್ ಒದಗಿಸಲಾಗುತ್ತದೆ.

---

### 📊 ಉಚಿತ ಯೂನಿಟ್ ಲೆಕ್ಕಾಚಾರದ ಅಧಿಕೃತ ಸೂತ್ರ:
* **ವಾರ್ಷಿಕ ಸರಾಸರಿ ಬಳಕೆ (Average Consumption):** ಹಿಂದಿನ 12 ತಿಂಗಳ (ಹಿಂದಿನ ವರ್ಷದ ಜುಲೈನಿಂದ ಜೂನ್‌ವರೆಗೆ) ಒಟ್ಟು ಬಳಕೆಯ ಸರಾಸರಿ ಯೂನಿಟ್ ಲೆಕ್ಕಹಾಕಲಾಗುತ್ತದೆ.
* **10% ಹೆಚ್ಚುವರಿ ಅರ್ಹತೆ (Entitled Units):** ವಾರ್ಷಿಕ ಸರಾಸರಿ ಯೂನಿಟ್‌ಗೆ 10% ಹೆಚ್ಚುವರಿ ಯೂನಿಟ್ ಸೇರಿಸಲಾಗುತ್ತದೆ (ಗರಿಷ್ಠ ಮಿತಿ 200 ಯೂನಿಟ್‌ಗಳು).

---

### 💡 ಬಿಲ್ಲಿಂಗ್ ನಿಯಮಗಳು:
1. **ಶೂನ್ಯ ಬಿಲ್ (Zero Bill):** ನಿಮ್ಮ ಮಾಸಿಕ ಬಳಕೆ ನಿಮ್ಮ ''ಅರ್ಹತಾ ಯೂನಿಟ್'' ಅಥವಾ 200 ಯೂನಿಟ್‌ಗಿಂತ ಕಡಿಮೆಯಿದ್ದರೆ ವಿದ್ಯುತ್ ಬಿಲ್ ₹0 (Zero) ಬರುತ್ತದೆ.
2. **ಭಾಗಶಃ ಬಿಲ್:** ಅರ್ಹತಾ ಮಿತಿಗಿಂತ ಹೆಚ್ಚಿದ್ದು ಆದರೆ 200 ಯೂನಿಟ್‌ಗಿಂತ ಒಳಗಿದ್ದರೆ ಹೆಚ್ಚುವರಿ ಯೂನಿಟ್‌ಗೆ ಮಾತ್ರ ಬಿಲ್ ಕಟ್ಟಬೇಕು.
3. **ಪೂರ್ಣ ಬಿಲ್:** ಮಾಸಿಕ ಬಳಕೆ 200 ಯೂನಿಟ್‌ ಮೀರಿದರೆ ಆ ತಿಂಗಳ ಸಂಪೂರ್ಣ ಬಿಲ್ ಗ್ರಾಹಕರೇ ಪಾವತಿಸಬೇಕು.

🔗 **ಅರ್ಜಿ ಸಲ್ಲಿಕೆ:** ಸೇವಾ ಸಿಂಧು ಪೋರ್ಟಲ್ ಅಥವಾ ವಿದ್ಯುತ್ ಸರಬರಾಜು ಕಂಪನಿಗಳ (BESCOM, HESCOM, GESCOM, MESCOM, CESC) ಪೋರ್ಟಲ್.', 'SCHEME', 'kn', 'https://sevasindhugs.karnataka.gov.in', 'gruha jyothi, free power calculation, 200 units, ಗೃಹಜ್ಯೋತಿ, ಉಚಿತ ವಿದ್ಯುತ್, zero bill', '⚡ ಗೃಹಜ್ಯೋತಿ ವಿವರ ನೋಡಿ', '/guarantee-schemes.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_sch_009', 'ಬಾಡಿಗೆ ಮನೆಯಲ್ಲಿರುವವರು ಗೃಹಜ್ಯೋತಿ ಯೋಜನೆಗೆ ನೋಂದಾಯಿಸಿಕೊಳ್ಳುವುದು ಹೇಗೆ?', 'ಬಾಡಿಗೆದಾರರಿಗೆ ಗೃಹಜ್ಯೋತಿ gruha jyothi tenant rental agreement apply seva sindhu', '### 🏠 ಬಾಡಿಗೆದಾರರಿಗೆ ಗೃಹಜ್ಯೋತಿ ಯೋಜನೆಯ ನೋಂದಣಿ ಪ್ರಕ್ರಿಯೆ

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
3. ಗ್ರಾಹಕರ ವಿಧದಲ್ಲಿ **''Tenant (ಬಾಡಿಗೆದಾರ)''** ಎಂದು ಆಯ್ಕೆಮಾಡಿ.
4. ಬಾಡಿಗೆದಾರರ ಆಧಾರ್ ಸಂಖ್ಯೆ ಹಾಕಿ OTP ಮೂಲಕ ಇ-ಸಹಿ ಮಾಡಿ ಸಲ್ಲಿಸಿ.

💡 **ಗಮನಿಸಿ:** ಒಂದು ಆಧಾರ್ ಸಂಖ್ಯೆಗೆ ಕೇವಲ ಒಂದು ವಿದ್ಯುತ್ ಮೀಟರ್ ಸಂಪರ್ಕಕ್ಕೆ ಮಾತ್ರ ಗೃಹಜ್ಯೋತಿ ಸೌಲಭ್ಯ ಲಭ್ಯವಿರುತ್ತದೆ.', 'SCHEME', 'kn', 'https://sevasindhugs.karnataka.gov.in', 'gruha jyothi tenant, rental agreement, ಬಾಡಿಗೆದಾರರು, ಗೃಹಜ್ಯೋತಿ, ಬಾಡಿಗೆ ಮನೆ', '⚡ ಗೃಹಜ್ಯೋತಿ ಪೋರ್ಟಲ್', 'https://sevasindhugs.karnataka.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_sch_010', 'ಶಕ್ತಿ ಯೋಜನೆಯಡಿ ಮಹಿಳೆಯರು ಯಾವ ಕೆಎಸ್‌ಆರ್‌ಟಿಸಿ/ಬಿಎಂಟಿಸಿ ಬಸ್‌ಗಳಲ್ಲಿ ಉಚಿತವಾಗಿ ಪ್ರಯಾಣಿಸಬಹುದು?', 'ಶಕ್ತಿ ಯೋಜನೆ ಉಚಿತ ಬಸ್ ಯಾವ ಬಸ್ shakti scheme free bus allowed bus types smart card', '### 🚌 ಶಕ್ತಿ ಯೋಜನೆ (Shakti Scheme) — ಮಹಿಳೆಯರಿಗೆ ಉಚಿತ ಬಸ್ ಪ್ರಯಾಣ

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
ಮಹಿಳೆಯರು ತಮ್ಮ ಕರ್ನಾಟಕ ವಿಳಾಸವಿರುವ ಅಧಿಕೃತ ಸರ್ಕಾರದ ಗುರುತಿನ ಚೀಟಿ (ಆಧಾರ್ ಕಾರ್ಡ್, ವೋಟರ್ ಐಡಿ, ಚಾಲನಾ ಪರವಾನಗಿ) ತೋರಿಸಿ ನಿರ್ವಾಹಕರಿಂದ **ಶೂನ್ಯ ದರದ ಟಿಕೆಟ್ (Zero Fare Ticket)** ಪಡೆದುಕೊಳ್ಳಬೇಕು.', 'SCHEME', 'kn', 'https://ksrtc.in', 'shakti scheme, free bus travel women, ksrtc bmtc, ಶಕ್ತಿ ಯೋಜನೆ, ಉಚಿತ ಬಸ್, ಝೀರೋ ಟಿಕೆಟ್', '🚌 ಶಕ್ತಿ ಯೋಜನೆ ನಿಯಮಗಳು', '/guarantee-schemes.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_sch_011', 'ಅನ್ನಭಾಗ್ಯ ಯೋಜನೆಯಡಿ ಅಕ್ಕಿ ಮತ್ತು ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT) ನಿಯಮಗಳು ಯಾವುವು?', 'ಅನ್ನಭಾಗ್ಯ ಅಕ್ಕಿ ಹಣ dbt anna bhagya 5kg rice 170 cash bpl phh aay', '### 🍚 ಅನ್ನಭಾಗ್ಯ ಯೋಜನೆ (Anna Bhagya Scheme) ವಿವರ

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

🔗 **ಆಹಾರ ಇಲಾಖೆ ಪೋರ್ಟಲ್:** [ahara.kar.nic.in](https://ahara.kar.nic.in)', 'SCHEME', 'kn', 'https://ahara.kar.nic.in', 'anna bhagya, 10kg rice, 170 cash dbt, bpl ration, ಅನ್ನಭಾಗ್ಯ, ನಗದು ವರ್ಗಾವಣೆ, ಆಹಾರ ಇಲಾಖೆ', '🍚 ಆಹಾರ ಇಲಾಖೆ ಪೋರ್ಟಲ್', 'https://ahara.kar.nic.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_sch_012', 'ಯುವನಿಧಿ (Yuva Nidhi) ನಿರುದ್ಯೋಗ ಭತ್ಯೆ ಯೋಜನೆ: ಯಾರು ಅರ್ಹರು? ಮಾಸಿಕ ಭತ್ಯೆ ಎಷ್ಟು?', 'ಯುವನಿಧಿ ಅರ್ಹತೆ ಹಣ yuva nidhi eligibility graduate diploma stipend 3000 1500', '### 🎓 ಯುವನಿಧಿ ಯೋಜನೆ (Yuva Nidhi Scheme) — ಯುವಜನರಿಗೆ ಆರ್ಥಿಕ ನೆರವು

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
ಪ್ರತಿ ತಿಂಗಳು 25 ನೇ ತಾರೀಖಿನೊಳಗೆ ಸೇವಾ ಸಿಂಧು ಪೋರ್ಟಲ್‌ನಲ್ಲಿ *"ನನಗೆ ಯಾವುದೇ ಉದ್ಯೋಗ ಸಿಕ್ಕಿಲ್ಲ"* ಎಂದು OTP ಮೂಲಕ ದೃಢೀಕರಿಸುವುದು ಕಡ್ಡಾಯ.', 'SCHEME', 'kn', 'https://sevasindhugs.karnataka.gov.in', 'yuva nidhi, 3000 degree stipend, 1500 diploma, ಯುವನಿಧಿ, ನಿರುದ್ಯೋಗ ಭತ್ಯೆ, ಸೇವಾ ಸಿಂಧು', '🎓 ಯುವನಿಧಿ ಪೋರ್ಟಲ್', 'https://sevasindhugs.karnataka.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_rev_013', 'ಭೂಮಿ (Bhoomi) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಡಿಜಿಟಲ್ ಪಹಣಿ (RTC) ಡೌನ್‌ಲೋಡ್ ಮಾಡುವುದು ಹೇಗೆ?', 'bhoomi rtc download pahani online ಪಹಣಿ ಡೌನ್‌ಲೋಡ್ ಭೂಮಿ ಸರ್ವೆ ನಂಬರ್', '### 🌾 ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಪಹಣಿ / RTC (Record of Rights, Tenancy and Crops) ಡೌನ್‌ಲೋಡ್

ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಕಂದಾಯ ಇಲಾಖೆಯ ಅಧಿಕೃತ **ಭೂಮಿ (Bhoomi)** ಪೋರ್ಟಲ್ ಮೂಲಕ ನಿಮ್ಮ ಜಮೀನಿನ ನೈಜ ಪಹಣಿ ವೀಕ್ಷಿಸಬಹುದು ಮತ್ತು ಡೌನ್‌ಲೋಡ್ ಮಾಡಬಹುದು.

---

### 💻 ಹಂತ-ಹಂತದ ವಿಧಾನ:
1. **ಭೂಮಿ ವೆಬ್‌ಸೈಟ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [bhoomi.karnataka.gov.in](https://bhoomi.karnataka.gov.in)
2. ಮುಖಪುಟದಲ್ಲಿ **''View RTC Information''** ಅಥವಾ **''RTC Wallet''** ಕ್ಲಿಕ್ ಮಾಡಿ.
3. ನಿಮ್ಮ **ಜಿಲ್ಲೆ (District), ತಾಲೂಕು (Taluk), ಹೋಬಳಿ (Hobli), ಗ್ರಾಮ (Village)** ಆಯ್ಕೆಮಾಡಿ.
4. ನಿಮ್ಮ ಜಮೀನಿನ **ಸರ್ವೆ ನಂಬರ್ (Survey No)** ಹಾಕಿ ''Go'' ಕ್ಲಿಕ್ ಮಾಡಿ.
5. ಸರ್ನೋಕ್ (Surnoc), ಹಿಸ್ಸಾ (Hissa) ಮತ್ತು ಅವಧಿ (Period) ಆರಿಸಿ **''Fetch Details''** ಒತ್ತಿರಿ.
6. **View RTC:** ಉಚಿತವಾಗಿ ಪರದೆಯ ಮೇಲೆ ಪಹಣಿ ವೀಕ್ಷಿಸಿ.
7. **ಡಿಜಿಟಲ್ ಸಹಿ ಇರುವ RTC:** ₹15 ಆನ್‌ಲೈನ್ ಶುಲ್ಕ ಪಾವತಿಸಿ ಕಂದಾಯ ಇಲಾಖೆಯ ಅಧಿಕೃತ ಡಿಜಿಟಲ್ ಸಹಿ ಇರುವ ವಾಟರ್‌ಮಾರ್ಕ್ ಪಹಣಿ PDF ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಿ.', 'REVENUE', 'kn', 'https://bhoomi.karnataka.gov.in', 'bhoomi rtc, download pahani, survey number, hissa, ಪಹಣಿ, ಭೂಮಿ, ಲ್ಯಾಂಡ್ ರೆಕಾರ್ಡ್', '🌾 ಭೂಮಿ ಪೋರ್ಟಲ್ ಪ್ರವೇಶಿಸಿ', 'https://bhoomi.karnataka.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_rev_014', 'ಮ್ಯುಟೇಶನ್ (Mutation Extract / MR) ಎಂದರೇನು? ಅದರ ಆನ್‌ಲೈನ್ ಸ್ಥಿತಿ ನೋಡುವುದು ಹೇಗೆ?', 'mutation status bhoomi mr extract ಮ್ಯುಟೇಶನ್ ಸ್ಥಿತಿ ಖಾತಾ ಬದಲಾವಣೆ ವಾರಸುದಾರಿಕೆ', '### 📜 ಮ್ಯುಟೇಶನ್ (Mutation Extract) ಮತ್ತು ಖಾತೆ ಬದಲಾವಣೆ

ಜಮೀನು ಮಾರಾಟವಾದಾಗ, ದಾನ ನೀಡಿದಾಗ, ವಿಭಾಗ ಪತ್ರವಾದಾಗ ಅಥವಾ ಮಾಲೀಕರು ಮೃತಪಟ್ಟು ವಾರಸುದಾರರಿಗೆ ವರ್ಗಾವಣೆಯಾದಾಗ ಕಂದಾಯ ದಾಖಲೆಯಲ್ಲಿ ಮಾಲೀಕತ್ವ ಬದಲಾಯಿಸುವ ಅಧಿಕೃತ ಪ್ರಕ್ರಿಯೆಯನ್ನು **ಮ್ಯುಟೇಶನ್ (ಹಕ್ಕು ಬದಲಾವಣೆ)** ಎನ್ನಲಾಗುತ್ತದೆ.

---

### 🔍 ಮ್ಯುಟೇಶನ್ ಸ್ಥಿತಿ (MR Status) ಟ್ರ್ಯಾಕ್ ಮಾಡುವ ವಿಧಾನ:
1. [bhoomi.karnataka.gov.in](https://bhoomi.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ **''Mutation Status''** ಆಯ್ಕೆಮಾಡಿ.
2. ನಿಮ್ಮ ಜಿಲ್ಲೆ, ತಾಲೂಕು, ಹೋಬಳಿ, ಗ್ರಾಮ ಮತ್ತು ಸರ್ವೆ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ.
3. ಅಥವಾ ಉಪನೋಂದಣಾಧಿಕಾರಿ ಕಚೇರಿಯಲ್ಲಿ ನೋಂದಣಿಯಾದ ನಂತರ ಸಿಕ್ಕ **MR Number** ಹಾಕಿ.
4. **ಹಂತಗಳ ಪರಿಶೀಲನೆ:**
   - ನೋಟಿಸ್ ಜಾರಿ (Form 9, 10 & 12 Notice period - 30 days).
   - ಗ್ರಾಮ ಆಡಳಿತಾಧಿಕಾರಿ (VA) ಪರಿಶೀಲನೆ.
   - ಕಂದಾಯ ನಿರೀಕ್ಷಕರ (RI) ಅನುಮೋದನೆ ಮತ್ತು ತಹಶೀಲ್ದಾರ್ ಡಿಜಿಟಲ್ ಸಹಿ.', 'REVENUE', 'kn', 'https://bhoomi.karnataka.gov.in', 'mutation status, mr register, bhoomi mutation, ಮ್ಯುಟೇಶನ್, ಖಾತೆ ಬದಲಾವಣೆ, ವಾರಸುದಾರಿಕೆ', '📜 ಮ್ಯುಟೇಶನ್ ಸ್ಥಿತಿ ಪರಿಶೀಲಿಸಿ', 'https://bhoomi.karnataka.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_rev_015', 'ಕಾವೇರಿ 2.0 (Kaveri 2.0) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಋಣಭಾರ ಪ್ರಮಾಣಪತ್ರ (EC) ಪಡೆಯುವುದು ಹೇಗೆ?', 'kaveri 2.0 encumbrance certificate ec download online ಋಣಭಾರ ಪ್ರಮಾಣ ಪತ್ರ ಈಸಿ', '### 🏛️ ಕಾವೇರಿ 2.0 (Kaveri 2.0) ನಲ್ಲಿ ಆನ್‌ಲೈನ್ EC (Encumbrance Certificate)

ಯಾವುದೇ ಸ್ಥಿರಾಸ್ತಿಯ ಮೇಲೆ ಬ್ಯಾಂಕ್ ಸಾಲ, ಅಡಮಾನ, ಕೋರ್ಟ್ ತಡೆಯಾಜ್ಞೆ ಅಥವಾ ಹಿಂದಿನ ಮಾರಾಟ ವಹಿವಾಟುಗಳು ಇವೆಯೇ ಎಂದು ತಿಳಿಯಲು **EC (ಋಣಭಾರ ಪ್ರಮಾಣಪತ್ರ)** ಅತ್ಯಗತ್ಯ.

---

### 💻 ಆನ್‌ಲೈನ್ EC ಪಡೆಯುವ ವಿಧಾನ:
1. **ಕಾವೇರಿ 2.0 ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [kaveri.karnataka.gov.in](https://kaveri.karnataka.gov.in)
2. ನಾಗರಿಕ ಲಾಗಿನ್ (Citizen Login) ಮೂಲಕ ಸೈನ್ ಇನ್ ಆಗಿ.
3. **''Online EC''** ಸೇವೆ ಆಯ್ಕೆಮಾಡಿ.
4. ಆಸ್ತಿಯ ವಿವರ (ಜಿಲ್ಲೆ, ಉಪನೋಂದಣಾಧಿಕಾರಿ ಕಚೇರಿ, ಸರ್ವೆ ನಂಬರ್ / ನಿವೇಶನ ಸಂಖ್ಯೆ, ಮತ್ತು ಹುಡುಕಾಟದ ಅವಧಿ ಉದಾ: 15 ಅಥವಾ 30 ವರ್ಷ) ನಮೂದಿಸಿ.
5. ಶುಲ್ಕ ಪಾವತಿಸಿ (Search Fee).
6. ಸಬ್-ರಿಜಿಸ್ಟ್ರಾರ್ ಅವರ ಡಿಜಿಟಲ್ ಸಹಿ ಇರುವ **Form 15 (ವಹಿವಾಟು ಇದ್ದರೆ)** ಅಥವಾ **Form 16 (Nil Encumbrance Certificate)** ತಕ್ಷಣ ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.', 'REVENUE', 'kn', 'https://kaveri.karnataka.gov.in', 'kaveri 2.0, encumbrance certificate, ec download, stamp duty, ಕಾವೇರಿ 2.0, ಈಸಿ, ಋಣಭಾರ', '🏛️ ಕಾವೇರಿ 2.0 ಪೋರ್ಟಲ್', 'https://kaveri.karnataka.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_rev_016', 'ದಿಶಾಂಕ್ (Dishank) ಆ್ಯಪ್ ಮತ್ತು ಮೋಜಿನಿ (Mojini) ಮೂಲಕ ಸರ್ವೆ ನಂಬರ್ ಮತ್ತು ಗಡಿ ತಿಳಿಯುವುದು ಹೇಗೆ?', 'dishank app mojini survey number boundary 11e sketch ದಿಶಾಂಕ್ ಆ್ಯಪ್ ಮೋಜಿನಿ ನಕ್ಷೆ', '### 🗺️ ದಿಶಾಂಕ್ (Dishank) ಮತ್ತು ಮೋಜಿನಿ (Mojini) ತಂತ್ರಜ್ಞಾನಗಳು

ಕರ್ನಾಟಕ ಕಂದಾಯ ಇಲಾಖೆಯು ಭೂಮಾಪನ ಮತ್ತು ಗಡಿ ವಿವಾದಗಳನ್ನು ತಡೆಯಲು ಅಭಿವೃದ್ಧಿಪಡಿಸಿರುವ ಎರಡು ಅತ್ಯಾಧುನಿಕ ಡಿಜಿಟಲ್ ಸಾಧನಗಳು:

---

### 📱 1. ದಿಶಾಂಕ್ ಆ್ಯಪ್ (Dishank App):
* ನೀವು ಯಾವುದೇ ಜಮೀನಿನಲ್ಲಿ ನಿಂತು ಆ್ಯಪ್ ಆನ್ ಮಾಡಿದರೆ ನಿಮ್ಮ ಫೋನಿನ ಜಿಪಿಎಸ್ (GPS) ಲೊಕೇಶನ್ ಆಧರಿಸಿ ಆ ಜಾಗದ **ನೈಜ ಸರ್ವೆ ನಂಬರ್**, ಹಿಸ್ಸಾ ಮತ್ತು ಗ್ರಾಮದ ನಕ್ಷೆಯನ್ನು ಪರದೆಯ ಮೇಲೆ ಲೈವ್ ಆಗಿ ತೋರಿಸುತ್ತದೆ.
* ಆ ಜಮೀನು ರಾಜಕಾಲುವೆ, ಅರಣ್ಯ ಪ್ರದೇಶ, ಗೋಮಾಳ ಅಥವಾ ಸರ್ಕಾರಿ ಜಾಗವೇ ಎಂಬುದನ್ನು ಖರೀದಿಸುವ ಮುನ್ನವೇ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಬಹುದು.

---

### 📐 2. ಮೋಜಿನಿ ಪೋರ್ಟಲ್ (Mojini):
* ಜಮೀನಿನ ವಿಭಜನೆ (11E ಸ್ಕೆಚ್), ತತ್ಕಾಲ್ ಪೋಡಿ, ಹದ್ದುಬಸ್ತು ಮತ್ತು ಅಲೈನ್ಮೆಂಟ್ ನಕ್ಷೆಗಳ ಅರ್ಜಿ ಸಲ್ಲಿಕೆ ಹಾಗೂ ಸ್ಟೇಟಸ್ ತಿಳಿಯಲು [mojini.karnataka.gov.in](https://mojini.karnataka.gov.in) ಬಳಸಲಾಗುತ್ತದೆ.', 'REVENUE', 'kn', 'https://mojini.karnataka.gov.in', 'dishank app, mojini survey, 11e sketch, podi, ದಿಶಾಂಕ್, ಮೋಜಿನಿ, ಸರ್ವೆ ನಂಬರ್', '🗺️ ಮೋಜಿನಿ ಪೋರ್ಟಲ್', 'https://mojini.karnataka.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_cert_017', 'ನಾಡಕಚೇರಿಯಲ್ಲಿ ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ (Caste & Income Certificate) ಪಡೆಯುವುದು ಹೇಗೆ?', 'nadakacheri caste income certificate online apply ಜಾತಿ ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರ rd number', '### 📑 ನಾಡಕಚೇರಿ (Nadakacheri / Atalji Janasnehi Kendra) ಸೇವೆಗಳು

ಶೈಕ್ಷಣಿಕ ವಿದ್ಯಾರ್ಥಿವೇತನಗಳು, ಶಾಲಾ ಪ್ರವೇಶ, ಸರ್ಕಾರಿ ಉದ್ಯೋಗ ಹಾಗೂ ಸಬ್ಸಿಡಿ ಯೋಜನೆಗಳಿಗೆ ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ ಅತ್ಯಗತ್ಯ.

---

### 📋 ಅಗತ್ಯ ದಾಖಲೆಗಳು:
* ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ರೇಷನ್ ಕಾರ್ಡ್.
* ಶಾಲಾ ವರ್ಗಾವಣೆ ಪ್ರಮಾಣಪತ್ರ (TC / Study Certificate) - ಜಾತಿ ನಮೂದಾಗಿರಬೇಕು.
* ಸ್ವಯಂ ಘೋಷಣಾ ಪತ್ರ ಮತ್ತು ಆದಾಯದ ಪುರಾವೆ (ವೇತನ ಚೀಟಿ / ಪಹಣಿ).

---

### 💻 ಆನ್‌ಲೈನ್ ಅರ್ಜಿ ಸಲ್ಲಿಕೆಯ ವಿಧಾನ:
1. [nadakacheri.karnataka.gov.in](https://nadakacheri.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ ಮೊಬೈಲ್ ಸಂಖ್ಯೆ ಮೂಲಕ ಲಾಗಿನ್ ಆಗಿ.
2. **''Online Application'' -> ''Caste / Income Certificate''** ಆಯ್ಕೆಮಾಡಿ.
3. ಪ್ರವರ್ಗ (Category 1, 2A, 2B, 3A, 3B, SC, ST) ಆಯ್ಕೆಮಾಡಿ ಕುಟುಂಬದ ವಿವರ ಭರ್ತಿ ಮಾಡಿ.
4. ₹40 ಆನ್‌ಲೈನ್ ಸೇವಾ ಶುಲ್ಕ ಪಾವತಿಸಿ.
5. ಗ್ರಾಮ ಆಡಳಿತಾಧಿಕಾರಿ (VA) ಮತ್ತು ಕಂದಾಯ ನಿರೀಕ್ಷಕರು (RI) ಸ್ಥಳ ತನಿಖೆ ನಡೆಸಿ ಅನುಮೋದಿಸಿದ ನಂತರ ನಿಮ್ಮ **RD Number** ಬಳಸಿ ಡಿಜಿಟಲ್ ಸಹಿಯುಳ್ಳ ಸರ್ಟಿಫಿಕೇಟ್ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.', 'CERTIFICATES', 'kn', 'https://nadakacheri.karnataka.gov.in', 'caste income certificate, nadakacheri rd number, ಜಾತಿ ಆದಾಯ ಪ್ರಮಾಣ ಪತ್ರ, ನಾಡಕಚೇರಿ, ಆರ್‌ಡಿ ನಂಬರ್', '📑 ನಾಡಕಚೇರಿ ಪೋರ್ಟಲ್', 'https://nadakacheri.karnataka.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_cert_018', 'ಸಂಧ್ಯಾ ಸುರಕ್ಷಾ ಮತ್ತು ವೃದ್ಧಾಪ್ಯ ವೇತನಕ್ಕೆ ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ನಿಯಮಗಳೇನು?', 'sandhya suraksha old age pension monthly amount ಸಂಧ್ಯಾ ಸುರಕ್ಷಾ ಮಾಸಾಶನ ವೃದ್ಧಾಪ್ಯ ವೇತನ', '### 👵 ಸಂಧ್ಯಾ ಸುರಕ್ಷಾ ಯೋಜನೆ (Sandhya Suraksha Scheme)

ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಸಾಮಾಜಿಕ ಭದ್ರತಾ ಯೋಜನೆಯಡಿ ನಿರ್ಗತಿಕ ಮತ್ತು ಬಡ ಹಿರಿಯ ನಾಗರಿಕರಿಗೆ ಮಾಸಿಕ ಪಿಂಚಣಿ ನೀಡಲಾಗುತ್ತದೆ.

---

### 📌 ಅರ್ಹತೆ & ನೆರವು:
* **ವಯಸ್ಸು:** 65 ವರ್ಷ ಮತ್ತು ಅದಕ್ಕಿಂತ ಮೇಲ್ಪಟ್ಟ ಹಿರಿಯ ನಾಗರಿಕರು.
* **ಮಾಸಿಕ ಪಿಂಚಣಿ:** ಪ್ರತಿ ತಿಂಗಳು **₹1,200** ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT).
* **ಆದಾಯ ಮಿತಿ:** ಫಲಾನುಭವಿ ಹಾಗೂ ಅವರ ಸಂಗಾತಿಯ ಒಟ್ಟು ವಾರ್ಷಿಕ ಆದಾಯ ₹32,000 ಮೀರಬಾರದು.
* ಯಾವುದೇ ಸಾರ್ವಜನಿಕ ಅಥವಾ ಖಾಸಗಿ ಸಂಸ್ಥೆಯಿಂದ ಬೇರೆ ಯಾವುದೇ ಪಿಂಚಣಿ ಪಡೆಯುತ್ತಿರಬಾರದು.

---

### 📝 ಅರ್ಜಿ ಸಲ್ಲಿಕೆ:
ಗ್ರಾಮ ಒನ್, ಕರ್ನಾಟಕ ಒನ್ ಅಥವಾ ನಾಡಕಚೇರಿ ಕೇಂದ್ರಗಳಲ್ಲಿ ವಯಸ್ಸಿನ ದಾಖಲೆ (ಆಧಾರ್/ವೋಟರ್ ಐಡಿ), ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರದೊಂದಿಗೆ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು.', 'WELFARE', 'kn', 'https://nadakacheri.karnataka.gov.in', 'sandhya suraksha, senior citizen pension, ವೃದ್ಧಾಪ್ಯ ವೇತನ, ಸಂಧ್ಯಾ ಸುರಕ್ಷಾ, ಮಾಸಾಶನ', '👵 ನಾಡಕಚೇರಿ ಪಿಂಚಣಿ ಸೇವೆ', 'https://nadakacheri.karnataka.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_adm_019', 'ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಪ್ರಸ್ತುತ ಮುಖ್ಯಮಂತ್ರಿ, ಸಚಿವ ಸಂಪುಟ ಮತ್ತು ಸಾಂವಿಧಾನಿಕ ನಾಯಕರು ಯಾರು?', 'ಕರ್ನಾಟಕ ಮುಖ್ಯಮಂತ್ರಿ ಸಂಪುಟ ನಾಯಕರು ಯಾರು cm of karnataka leadership cabinet', '### 🏛️ ಕರ್ನಾಟಕ ರಾಜ್ಯ ಕಾರ್ಯಾಂಗ & ಆಡಳಿತ ನಾಯಕತ್ವ

* **ಮುಖ್ಯಮಂತ್ರಿ:** **ಡಿ.ಕೆ. ಶಿವಕುಮಾರ್ (D.K. Shivakumar)** (ಕನಕಪುರ ಕ್ಷೇತ್ರ - INC)
* **ಉಪಮುಖ್ಯಮಂತ್ರಿ:** **ಡಾ. ಜಿ. ಪರಮೇಶ್ವರ್ (Dr. G. Parameshwara)** (ಕೊರಟಗೆರೆ ಕ್ಷೇತ್ರ - INC)
* **ರಾಜ್ಯಪಾಲರು:** **ಥಾವರ್‌ಚಂದ್ ಗೆಹ್ಲೋಟ್ (Thaawarchand Gehlot)**
* **ಮುಖ್ಯ ಕಾರ್ಯದರ್ಶಿ (Chief Secretary):** **ಡಾ. ಶಾಲಿನಿ ರಜನೀಶ್, IAS**
* **ವಿಧಾನಸಭಾ ಸಂಖ್ಯಾಬಲ:** ಒಟ್ಟು 224 ಚುನಾಯಿತ ಸದಸ್ಯರು.
* **ಲೋಕಸಭಾ ಕ್ಷೇತ್ರಗಳು:** 28 ಸಂಸದರು.', 'ADMIN', 'kn', 'https://karnataka.gov.in', 'cm, chief minister, dks, parameshwara, ಮುಖ್ಯಮಂತ್ರಿ, ಆಡಳಿತ, ಸಚಿವ ಸಂಪುಟ, cabinet', '👥 ಅಧಿಕಾರಿಗಳು & ಸಂಪುಟ ನೋಡಿ', '/officers.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_adm_020', 'ಕರ್ನಾಟಕದ 4 ಕಂದಾಯ ವಿಭಾಗಗಳು ಮತ್ತು 31 ಜಿಲ್ಲೆಗಳ ವಿನ್ಯಾಸವೇನು?', 'karnataka 4 revenue divisions 31 districts list ಕರ್ನಾಟಕ ಕಂದಾಯ ವಿಭಾಗಗಳು ಜಿಲ್ಲೆಗಳು', '### 🗺️ ಕರ್ನಾಟಕದ ಕಂದಾಯ ವಿಭಾಗಗಳು (Revenue Divisions) ಮತ್ತು 31 ಜಿಲ್ಲೆಗಳು:

ಆಡಳಿತಾತ್ಮಕ ಅನುಕೂಲಕ್ಕಾಗಿ ಕರ್ನಾಟಕವನ್ನು 4 ಪ್ರಮುಖ ವಿಭಾಗಗಳಾಗಿ ವಿಂಗಡಿಸಲಾಗಿದೆ:

---

1. **ಬೆಂಗಳೂರು ವಿಭಾಗ (Bengaluru Division - 9 ಜಿಲ್ಲೆಗಳು):**
   - ಬೆಂಗಳೂರು ನಗರ, ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ, ರಾಮನಗರ, ಕೋಲಾರ, ಚಿಕ್ಕಬಳ್ಳಾಪುರ, ತುಮಕೂರು, ಶಿವಮೊಗ್ಗ, ಚಿತ್ರದುರ್ಗ, ದಾವಣಗೆರೆ.
2. **ಮೈಸೂರು ವಿಭಾಗ (Mysuru Division - 8 ಜಿಲ್ಲೆಗಳು):**
   - ಮೈಸೂರು, ಮಂಡ್ಯ, ಹಾಸನ, ಚಿಕ್ಕಮಗಳೂರು, ದಕ್ಷಿಣ ಕನ್ನಡ, ಉಡುಪಿ, ಕೊಡಗು, ಚಾಮರಾಜನಗರ.
3. **ಬೆಳಗಾವಿ ವಿಭಾಗ (Belagavi Division - 7 ಜಿಲ್ಲೆಗಳು):**
   - ಬೆಳಗಾವಿ, ಧಾರವಾಡ, ವಿಜಯಪುರ, ಬಾಗಲಕೋಟೆ, ಗದಗ, ಹಾವೇರಿ, ಉತ್ತರ ಕನ್ನಡ.
4. **ಕಲಬುರಗಿ ವಿಭಾಗ (Kalaburagi Division - 7 ಜಿಲ್ಲೆಗಳು):**
   - ಕಲಬುರಗಿ, ಬೀದರ್, ರಾಯಚೂರು, ಕೊಪ್ಪಳ, ಬಳ್ಳಾರಿ, ಯಾದಗಿರಿ, ವಿಜಯನಗರ (ರಾಜ್ಯದ 31ನೇ ನೂತನ ಜಿಲ್ಲೆ).', 'ADMIN', 'kn', 'https://karnataka.gov.in', '31 districts, revenue divisions, bengaluru, mysuru, belagavi, kalaburagi, ಕಂದಾಯ ವಿಭಾಗ', '🗺️ 31 ಜಿಲ್ಲೆಗಳ ಮ್ಯಾಟ್ರಿಕ್ಸ್', '/districts.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_edu_021', 'SSP (State Scholarship Portal) ಪೋಸ್ಟ್-ಮೆಟ್ರಿಕ್ ವಿದ್ಯಾರ್ಥಿವೇತನಕ್ಕೆ ಅರ್ಜಿ ಸಲ್ಲಿಸುವುದು ಹೇಗೆ?', 'ssp scholarship karnataka post matric apply e-attestation ಎಸ್ಎಸ್ಪಿ ವಿದ್ಯಾರ್ಥಿವೇತನ', '### 🎓 SSP (State Scholarship Portal) ಪೋಸ್ಟ್-ಮೆಟ್ರಿಕ್ ವಿದ್ಯಾರ್ಥಿವೇತನ

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
3. ಕಾಲೇಜು ಮತ್ತು ಕೋರ್ಸ್ ಆಯ್ಕೆಮಾಡಿ ಸಬ್ಮಿಟ್ ಮಾಡಿ.', 'EDUCATION', 'kn', 'https://ssp.postmatric.karnataka.gov.in', 'ssp scholarship, post matric scholarship, e-attestation, ಎಸ್ಎಸ್ಪಿ ವಿದ್ಯಾರ್ಥಿವೇತನ, ಇ-ಅಟೆಸ್ಟೇಷನ್', '🎓 SSP ಪೋರ್ಟಲ್', 'https://ssp.postmatric.karnataka.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_civ_022', 'ಬೆಂಗಳೂರಿನಲ್ಲಿ BBMP ಇ-ಖಾತಾ ಮತ್ತು ಆಸ್ತಿ ತೆರಿಗೆ (Property Tax) ಪಾವತಿಸುವುದು ಹೇಗೆ?', 'bbmp e khata download online property tax a khata b khata ಬಿಬಿಎಂಪಿ ಇ-ಖಾತಾ ಆಸ್ತಿ ತೆರಿಗೆ', '### 🏢 BBMP ಇ-ಖಾತಾ (e-Aasthi) ಮತ್ತು ಆಸ್ತಿ ತೆರಿಗೆ ಪಾವತಿ

ಗ್ರೇಟರ್ ಬೆಂಗಳೂರು ಮಹಾನಗರ ವ್ಯಾಪ್ತಿಯ ಆಸ್ತಿಗಳ ನಿರ್ವಹಣೆಗೆ ಬಿಬಿಎಂಪಿ ಇ-ಖಾತಾ ಕಡ್ಡಾಯವಾಗಿದೆ.

---

### 📜 ಇ-ಖಾತಾ (e-Aasthi) ಡೌನ್‌ಲೋಡ್:
* [bbmpeaasthi.karnataka.gov.in](https://bbmpeaasthi.karnataka.gov.in) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ನಿಮ್ಮ 10 ಅಂಕಿಗಳ Property PID ಸಂಖ್ಯೆ ನಮೂದಿಸಿ ಡಿಜಿಟಲ್ ಇ-ಖಾತಾ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.

---

### 💳 ಆಸ್ತಿ ತೆರಿಗೆ ಪಾವತಿ ವಿಧಾನ:
1. [bbmptax.karnataka.gov.in](https://bbmptax.karnataka.gov.in) ಗೆ ಭೇಟಿ ನೀಡಿ.
2. SAS Base Application Number ಅಥವಾ PID ನಮೂದಿಸಿ ''Fetch'' ಕ್ಲಿಕ್ ಮಾಡಿ.
3. ಬಾಕಿ ತೆರಿಗೆ ವಿವರ ಪರಿಶೀಲಿಸಿ UPI, ನೆಟ್ ಬ್ಯಾಂಕಿಂಗ್ ಅಥವಾ ಕ್ರೆಡಿಟ್ ಕಾರ್ಡ್ ಮೂಲಕ ಪಾವತಿಸಿ ತಕ್ಷಣ ಅಧಿಕೃತ ರಶೀದಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಿ.', 'CIVIC', 'kn', 'https://bbmptax.karnataka.gov.in', 'bbmp e khata, bbmp property tax, a khata, b khata, ಬೆಂಗಳೂರು ಆಸ್ತಿ ತೆರಿಗೆ, ಇ-ಖಾತಾ', '🏢 BBMP ಆಸ್ತಿ ಪೋರ್ಟಲ್', 'https://bbmptax.karnataka.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_civ_023', 'ಬೆಸ್ಕಾಂ (BESCOM) ವಿದ್ಯುತ್ ಬಿಲ್ ಪಾವತಿ ಮತ್ತು ತುರ್ತು ದೂರು ಸಹಾಯವಾಣಿ ಯಾವುದು?', 'bescom bill payment power cut complaint 1912 ಬೆಸ್ಕಾಂ ವಿದ್ಯುತ್ ಬಿಲ್ ದೂರು', '### 💡 ಬೆಸ್ಕಾಂ (BESCOM) ವಿದ್ಯುತ್ ಸೇವೆಗಳು & 24/7 ಸಹಾಯವಾಣಿ

* **ತುರ್ತು ವಿದ್ಯುತ್ ದೂರು ಸಂಖ್ಯೆ:** **1912** (ಟೋಲ್-ಫ್ರೀ / ವಿದ್ಯುತ್ ಕಡಿತ, ಟ್ರಾನ್ಸ್‌ಫಾರ್ಮರ್ ಸಮಸ್ಯೆ, ತುರ್ತು ಅಪಾಯಗಳಿಗೆ).
* **WhatsApp ದೂರು ಸಂಖ್ಯೆ:** 9483191212 / 9483191222.
* **ಆನ್‌ಲೈನ್ ಬಿಲ್ ಪಾವತಿ:** [bescom.karnataka.gov.in](https://bescom.karnataka.gov.in) ಅಥವಾ **BESCOM Mithra App** ನಲ್ಲಿ ನಿಮ್ಮ 10 ಅಂಕಿಗಳ Account ID ನಮೂದಿಸಿ ಪಾವತಿಸಬಹುದು.', 'CIVIC', 'kn', 'https://bescom.karnataka.gov.in', 'bescom 1912, electricity bill online, power complaint, ಬೆಸ್ಕಾಂ ಬಿಲ್, ವಿದ್ಯುತ್ ದೂರು', '💡 ಬೆಸ್ಕಾಂ ಪೋರ್ಟಲ್', 'https://bescom.karnataka.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_civ_024', 'ಆಯುಷ್ಮಾನ್ ಭಾರತ್ - ಆರೋಗ್ಯ ಕರ್ನಾಟಕ (AB-ArK) ಯೋಜನೆಯಡಿ ಉಚಿತ ಚಿಕಿತ್ಸೆ ಪಡೆಯುವುದು ಹೇಗೆ?', 'ayushman bharat arogya karnataka free treatment ಆಯುಷ್ಮಾನ್ ಭಾರತ್ ಆರೋಗ್ಯ ಕರ್ನಾಟಕ', '### 🏥 ಆಯುಷ್ಮಾನ್ ಭಾರತ್ - ಆರೋಗ್ಯ ಕರ್ನಾಟಕ (AB-ArK) ಆರೋಗ್ಯ ಭದ್ರತೆ

ರಾಜ್ಯದ ಪ್ರತಿಯೊಬ್ಬ ನಾಗರಿಕರಿಗೂ ಗುಣಮಟ್ಟದ ಚಿಕಿತ್ಸೆ ಒದಗಿಸುವ ಸಾರ್ವತ್ರಿಕ ಆರೋಗ್ಯ ಯೋಜನೆ.

---

### 💰 ಚಿಕಿತ್ಸಾ ಮಿತಿ:
* **BPL / ಅಂತ್ಯೋದಯ ಕಾರ್ಡ್‌ದಾರರು:** ವರ್ಷಕ್ಕೆ ಪ್ರತಿ ಕುಟುಂಬಕ್ಕೆ ಗರಿಷ್ಠ **₹5 ಲಕ್ಷದವರೆಗೆ** ಸಂಪೂರ್ಣ ಉಚಿತ ಚಿಕಿತ್ಸೆ.
* **APL ಕಾರ್ಡ್‌ದಾರರು:** ಪ್ಯಾಕೇಜ್ ದರದ **30% ರಿಯಾಯಿತಿ** (ವರ್ಷಕ್ಕೆ ಗರಿಷ್ಠ ₹1.50 ಲಕ್ಷ).

---

### 🏥 ಚಿಕಿತ್ಸೆ ಪಡೆಯುವ ವಿಧಾನ:
1. ಸಾಮಾನ್ಯ ಚಿಕಿತ್ಸೆಗಳಿಗೆ ನೇರವಾಗಿ ತಾಲೂಕು ಅಥವಾ ಜಿಲ್ಲಾ ಸರ್ಕಾರಿ ಆಸ್ಪತ್ರೆಗೆ ಭೇಟಿ ನೀಡಿ.
2. ಸರ್ಕಾರಿ ಆಸ್ಪತ್ರೆಯಲ್ಲಿ ಲಭ್ಯವಿಲ್ಲದ ಸೂಪರ್ ಸ್ಪೆಷಾಲಿಟಿ ಚಿಕಿತ್ಸೆಗಳಿಗೆ ವೈದ್ಯರಿಂದ **ರೆಫರಲ್ ಪತ್ರ (Referral Letter)** ಪಡೆದು ಎಂಪ್ಯಾನೆಲ್ ಆದ ಖಾಸಗಿ ಆಸ್ಪತ್ರೆಗಳಿಗೆ ಹೋಗಬಹುದು.
3. ತುರ್ತು ಅಪಘಾತ ಮತ್ತು ಜೀವನ್ಮರಣ ಸ್ಥಿತಿಯಲ್ಲಿ ರೆಫರಲ್ ಇಲ್ಲದೆಯೇ ನೇರವಾಗಿ ಖಾಸಗಿ ಆಸ್ಪತ್ರೆಗೆ ದಾಖಲಾಗಬಹುದು.', 'HEALTH', 'kn', 'https://arogya.karnataka.gov.in', 'arogya karnataka, ayushman bharat ark, 5 lakh free hospital, ಆರೋಗ್ಯ ಕರ್ನಾಟಕ, ಉಚಿತ ಚಿಕಿತ್ಸೆ', '🏥 ಆರೋಗ್ಯ ಕರ್ನಾಟಕ ವಿವರ', 'https://arogya.karnataka.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_civ_025', 'ಫ್ರೂಟ್ಸ್ (FRUITS) ಪೋರ್ಟಲ್ ಎಂದರೇನು? ರೈತರ FID ನಂಬರ್ ಪಡೆಯುವುದು ಹೇಗೆ?', 'fruits portal fid number farmer registration ಫ್ರೂಟ್ಸ್ ತಂತ್ರಾಂಶ ಎಫ್ಐಡಿ ಕೃಷಿ ಸಾಲ', '### 👨‍🌾 FRUITS (Farmer Registration & Unified Beneficiary Information System)

ಕರ್ನಾಟಕ ಸರ್ಕಾರದ ಕೃಷಿ, ತೋಟಗಾರಿಕೆ, ರೇಷ್ಮೆ ಮತ್ತು ಪಶುಸಂಗೋಪನಾ ಇಲಾಖೆಗಳ ಸೌಲಭ್ಯಗಳನ್ನು ಒಂದೇ ಸೂರಿನಡಿ ತರಲು ಅಭಿವೃದ್ಧಿಪಡಿಸಲಾದ ತಂತ್ರಾಂಶ.

---

### 📌 FID (Farmer Identification Number) ಮಹತ್ವ:
* ಪ್ರತಿ ರೈತ ಕುಟುಂಬಕ್ಕೆ ನೀಡಲಾಗುವ ವಿಶಿಷ್ಟ ಗುರುತಿನ ಸಂಖ್ಯೆಯೇ **FID**.
* ಬೆಳೆ ವಿಮೆ ಪರಿಹಾರ, ಕಿಸಾನ್ ಸಮ್ಮಾನ್ ನಿಧಿ, ಬಿತ್ತನೆ ಬೀಜ/ರಸಗೊಬ್ಬರ ಸಬ್ಸಿಡಿ, ಟ್ರ್ಯಾಕ್ಟರ್ ಸಹಾಯಧನ ಮತ್ತು ಶೂನ್ಯ ಬಡ್ಡಿ ಸಾಲ ಪಡೆಯಲು FID ಕಡ್ಡಾಯ.

---

### 📝 FID ಪಡೆಯುವ ವಿಧಾನ:
1. ಹತ್ತಿರದ ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ (RSK) ಅಥವಾ ಗ್ರಾಮ ಪಂಚಾಯಿತಿಗೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಮೀನಿನ ಪಹಣಿ (RTC), ಆಧಾರ್ ಕಾರ್ಡ್ ಮತ್ತು ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ ಸಲ್ಲಿಸಿ ತಕ್ಷಣ FID ರಚಿಸಿಕೊಳ್ಳಿ.
3. ಆನ್‌ಲೈನ್ ಸ್ಥಿತಿ ಪರಿಶೀಲನೆ: [fruits.karnataka.gov.in](https://fruits.karnataka.gov.in)', 'AGRICULTURE', 'kn', 'https://fruits.karnataka.gov.in', 'fruits portal, fid number, farmer id, ಬೆಳೆ ಸಾಲ, ಸಬ್ಸಿಡಿ, ರೈತ ಸಂಪರ್ಕ ಕೇಂದ್ರ', '🌾 FRUITS ಪೋರ್ಟಲ್', 'https://fruits.karnataka.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_civ_026', 'ಪರಿಹಾರ (Parihara) ಪೋರ್ಟಲ್‌ನಲ್ಲಿ ಬೆಳೆ ಹಾನಿ ಮತ್ತು ಬರ ಪರಿಹಾರ ಚೆಕ್ ಮಾಡುವುದು ಹೇಗೆ?', 'parihara crop loss drought compensation check online ಪರಿಹಾರ ಬೆಳೆ ಹಾನಿ ಹಣ', '### 🌾 ಪರಿಹಾರ (Parihara) ಪೋರ್ಟಲ್ — ಬೆಳೆ ಹಾನಿ ಪರಿಹಾರ ಟ್ರ್ಯಾಕಿಂಗ್

ಅತಿವೃಷ್ಟಿ, ಅನಾವೃಷ್ಟಿ ಅಥವಾ ಬರಗಾಲದಿಂದ ಹಾನಿಗೊಳಗಾದ ಬೆಳೆಗಳಿಗೆ ರಾಜ್ಯ ಮತ್ತು ಎನ್‌ಡಿಆರ್‌ಎಫ್ (NDRF) ನಿಧಿಯಿಂದ ನೇರವಾಗಿ ರೈತರ ಖಾತೆಗೆ DBT ಜಮೆ ಮಾಡಲಾಗುತ್ತದೆ.

---

### 🔍 ಪರಿಹಾರ ಹಣ ಚೆಕ್ ಮಾಡುವ ವಿಧಾನ:
1. **ಪೋರ್ಟಲ್‌ಗೆ ಭೇಟಿ ನೀಡಿ:** [parihara.karnataka.gov.in](https://parihara.karnataka.gov.in)
2. **''Parihara Payment Status''** ಆಯ್ಕೆಮಾಡಿ.
3. ವರ್ಷ ಮತ್ತು ಋತು (Kharif / Rabi) ಆಯ್ಕೆಮಾಡಿ.
4. ರೈತರ **ಆಧಾರ್ ಸಂಖ್ಯೆ** ಅಥವಾ **FID ಸಂಖ್ಯೆ** ಅಥವಾ **ಸರ್ವೆ ನಂಬರ್** ನಮೂದಿಸಿ ''Fetch Details'' ಕ್ಲಿಕ್ ಮಾಡಿ.
5. ನಿಮ್ಮ ಬ್ಯಾಂಕ್ ಖಾತೆಗೆ ಜಮೆಯಾದ ಮೊತ್ತ, ದಿನಾಂಕ ಮತ್ತು UTR ನಂಬರ್ ಪರದೆಯ ಮೇಲೆ ಲಭ್ಯವಾಗುತ್ತದೆ.', 'AGRICULTURE', 'kn', 'https://parihara.karnataka.gov.in', 'parihara status, crop loss dbt, drought compensation, ಪರಿಹಾರ ಬೆಳೆ ಹಾನಿ, ಬರ ಪರಿಹಾರ', '🌾 ಪರಿಹಾರ ಸ್ಥಿತಿ ನೋಡಿ', 'https://parihara.karnataka.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_civ_027', 'ಕರ್ನಾಟಕ ಪೊಲೀಸ್ ತುರ್ತು ಸಹಾಯವಾಣಿ 112 ಮತ್ತು KSP App ನ ಪ್ರಯೋಜನಗಳೇನು?', 'karnataka police emergency 112 ksp app e-lost complaint ಪೊಲೀಸ್ ಸಹಾಯವಾಣಿ', '### 👮 ಕರ್ನಾಟಕ ಪೊಲೀಸ್ (KSP) ತುರ್ತು ಸೇವೆಗಳು & ನಾಗರಿಕ ಸೌಲಭ್ಯಗಳು

* **ತುರ್ತು ಸಹಾಯವಾಣಿ: 112 (Emergency Response Support System):** ಪೊಲೀಸ್, ಅಗ್ನಿಶಾಮಕ ಮತ್ತು ಆಂಬ್ಯುಲೆನ್ಸ್ ಮೂರೂ ಸೇವೆಗಳಿಗೆ ಒಂದೇ ತುರ್ತು ಸಂಖ್ಯೆ. ಕರೆ ಮಾಡಿದ 15 ನಿಮಿಷಗಳಲ್ಲಿ ಹೊಯ್ಸಳ/ಪೊಲೀಸ್ ವಾಹನ ಸ್ಥಳಕ್ಕೆ ತಲುಪುತ್ತದೆ.
* **KSP Citizen Mobile App:**
  - **E-Lost Report:** ಮೊಬೈಲ್, ಪಾಸ್‌ಪೋರ್ಟ್, ದಾಖಲೆಗಳು ಕಳೆದುಹೋದರೆ ಠಾಣೆಗೆ ಹೋಗದೆ ಮೊಬೈಲ್‌ನಲ್ಲೇ ಡಿಜಿಟಲ್ ಪ್ರಮಾಣಪತ್ರ ಪಡೆಯಬಹುದು.
  - **FIR Status:** ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ಎಫ್‌ಐಆರ್ ಪ್ರತಿಯನ್ನು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿಕೊಳ್ಳಬಹುದು.
  - **ಹಿರಿಯ ನಾಗರಿಕರ ರಕ್ಷಣೆ:** ಹಿರಿಯ ನಾಗರಿಕರು ತುರ್ತು ರಕ್ಷಣೆಗಾಗಿ ನೋಂದಾಯಿಸಿಕೊಳ್ಳಬಹುದು.', 'POLICE', 'kn', 'https://ksp.karnataka.gov.in', 'ksp app, 112 emergency, e lost app, ಕರ್ನಾಟಕ ಪೊಲೀಸ್, ತುರ್ತು ಸಹಾಯವಾಣಿ', '👮 ಪೊಲೀಸ್ ಪೋರ್ಟಲ್', 'https://ksp.karnataka.gov.in');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_028', 'ಬೆಂಗಳೂರು ನಗರ (Bengaluru Urban) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಬೆಂಗಳೂರು ನಗರ Bengaluru Urban ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಬೆಂಗಳೂರು ನಗರ (Bengaluru Urban) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಬೆಂಗಳೂರು ನಗರ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 28 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಬೆಂಗಳೂರು ಉತ್ತರ, ಬೆಂಗಳೂರು ದಕ್ಷಿಣ, ಬೆಂಗಳೂರು ಪೂರ್ವ, ಆನೇಕಲ್, ಯಲಹಂಕ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಮಾಹಿತಿ ತಂತ್ರಜ್ಞಾನ, ಜೈವಿಕ ತಂತ್ರಜ್ಞಾನ, ಕೈಗಾರಿಕೆ ಹಾಗೂ ವಾಣಿಜ್ಯ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://bengaluruurban.nic.in', 'ಬೆಂಗಳೂರು ನಗರ, Bengaluru Urban, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಬೆಂಗಳೂರು ನಗರ ಜಿಲ್ಲಾ ಪುಟ', '/districts/bengaluru_urban.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_029', 'ಬೆಂಗಳೂರು ನಗರ ಜಿಲ್ಲೆಯ 28 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಬೆಂಗಳೂರು ನಗರ Bengaluru Urban sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಬೆಂಗಳೂರು ನಗರ (Bengaluru Urban) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಬೆಂಗಳೂರು ನಗರ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **28 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಬೆಂಗಳೂರು ನಗರ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಬೆಂಗಳೂರು ನಗರ, Bengaluru Urban, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 28 mla', '🔎 ಬೆಂಗಳೂರು ನಗರ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_030', 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ (Bengaluru Rural) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ Bengaluru Rural ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ (Bengaluru Rural) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 4 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ದೇವನಹಳ್ಳಿ, ನೆಲಮಂಗಲ, ದೊಡ್ಡಬಳ್ಳಾಪುರ, ಹೊಸಕೋಟೆ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ರೇಷ್ಮೆ, ಕೃಷಿ, ಕೈಗಾರಿಕಾ ಕಾರಿಡಾರ್ ಹಾಗೂ ಕೆಂಪೇಗೌಡ ಅಂತಾರಾಷ್ಟ್ರೀಯ ವಿಮಾನ ನಿಲ್ದಾಣ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://bengalururural.nic.in', 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ, Bengaluru Rural, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ ಜಿಲ್ಲಾ ಪುಟ', '/districts/bengaluru_rural.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_031', 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ ಜಿಲ್ಲೆಯ 4 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ Bengaluru Rural sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ (Bengaluru Rural) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **4 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ, Bengaluru Rural, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 4 mla', '🔎 ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_032', 'ರಾಮನಗರ (Ramanagara) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ರಾಮನಗರ Ramanagara ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ರಾಮನಗರ (Ramanagara) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ರಾಮನಗರ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 4 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ರಾಮನಗರ, ಕನಕಪುರ, ಚನ್ನಪಟ್ಟಣ, ಮಾಗಡಿ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ರೇಷ್ಮೆ ಮಾರುಕಟ್ಟೆ (ಸಿಲ್ಕ್ ಸಿಟಿ), ಚನ್ನಪಟ್ಟಣದ ಮರದ ಬೊಂಬೆಗಳು ಮತ್ತು ಕೃಷಿ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://ramanagara.nic.in', 'ರಾಮನಗರ, Ramanagara, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ರಾಮನಗರ ಜಿಲ್ಲಾ ಪುಟ', '/districts/ramanagara.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_033', 'ರಾಮನಗರ ಜಿಲ್ಲೆಯ 4 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ರಾಮನಗರ Ramanagara sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ರಾಮನಗರ (Ramanagara) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ರಾಮನಗರ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **4 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ರಾಮನಗರ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ರಾಮನಗರ, Ramanagara, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 4 mla', '🔎 ರಾಮನಗರ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_034', 'ಕೋಲಾರ (Kolar) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಕೋಲಾರ Kolar ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಕೋಲಾರ (Kolar) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಕೋಲಾರ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 6 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಕೋಲಾರ, ಬಂಗಾರಪೇಟೆ, ಮಾಲೂರು, ಮುಳಬಾಗಿಲು, ಶ್ರೀನಿವಾಸಪುರ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಮಾವು ಬೆಳೆ, ಚಿನ್ನದ ಗಣಿ ಇತಿಹಾಸ, ಹಾಲು ಉತ್ಪಾದನೆ ಮತ್ತು ರೇಷ್ಮೆ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://kolar.nic.in', 'ಕೋಲಾರ, Kolar, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಕೋಲಾರ ಜಿಲ್ಲಾ ಪುಟ', '/districts/kolar.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_035', 'ಕೋಲಾರ ಜಿಲ್ಲೆಯ 6 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಕೋಲಾರ Kolar sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಕೋಲಾರ (Kolar) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಕೋಲಾರ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **6 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಕೋಲಾರ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಕೋಲಾರ, Kolar, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 6 mla', '🔎 ಕೋಲಾರ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_036', 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ (Chikkaballapur) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ Chikkaballapur ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಚಿಕ್ಕಬಳ್ಳಾಪುರ (Chikkaballapur) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಚಿಕ್ಕಬಳ್ಳಾಪುರ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 5 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಚಿಕ್ಕಬಳ್ಳಾಪುರ, ಬಾಗೇಪಲ್ಲಿ, ಗೌರಿಬಿದನೂರು, ಚಿಂತಾಮಣಿ, ಶಿಡ್ಲಘಟ್ಟ, ಗುಡಿಬಂಡೆ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ದ್ರಾಕ್ಷಿ ಬೆಳೆ, ನಂದಿಬೆಟ್ಟ ಪ್ರವಾಸೋದ್ಯಮ ಮತ್ತು ರೇಷ್ಮೆ ಕೃಷಿ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://chikkaballapur.nic.in', 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ, Chikkaballapur, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಚಿಕ್ಕಬಳ್ಳಾಪುರ ಜಿಲ್ಲಾ ಪುಟ', '/districts/chikkaballapur.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_037', 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ ಜಿಲ್ಲೆಯ 5 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ Chikkaballapur sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಚಿಕ್ಕಬಳ್ಳಾಪುರ (Chikkaballapur) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಚಿಕ್ಕಬಳ್ಳಾಪುರ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **5 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಚಿಕ್ಕಬಳ್ಳಾಪುರ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಚಿಕ್ಕಬಳ್ಳಾಪುರ, Chikkaballapur, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 5 mla', '🔎 ಚಿಕ್ಕಬಳ್ಳಾಪುರ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_038', 'ತುಮಕೂರು (Tumakuru) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ತುಮಕೂರು Tumakuru ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ತುಮಕೂರು (Tumakuru) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ತುಮಕೂರು
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 11 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ತುಮಕೂರು, ಕುಣಿಗಲ್, ಗುಬ್ಬಿ, ತಿಪಟೂರು, ಚಿಕ್ಕನಾಯಕನಹಳ್ಳಿ, ಶಿರಾ, ಪಾವಗಡ, ಮಧುಗಿರಿ, ಕೊರಟಗೆರೆ, ತುರುವೇಕೆರೆ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ತೆಂಗು ಉತ್ಪಾದನೆ (ಕಲ್ಪತರು ನಾಡು), ಪಾವಗಡ ಸೋಲಾರ್ ಪಾರ್ಕ್, ಕೈಗಾರಿಕೆಗಳು.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://tumakuru.nic.in', 'ತುಮಕೂರು, Tumakuru, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ತುಮಕೂರು ಜಿಲ್ಲಾ ಪುಟ', '/districts/tumakuru.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_039', 'ತುಮಕೂರು ಜಿಲ್ಲೆಯ 11 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ತುಮಕೂರು Tumakuru sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ತುಮಕೂರು (Tumakuru) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ತುಮಕೂರು ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **11 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ತುಮಕೂರು''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ತುಮಕೂರು, Tumakuru, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 11 mla', '🔎 ತುಮಕೂರು Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_040', 'ಶಿವಮೊಗ್ಗ (Shivamogga) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಶಿವಮೊಗ್ಗ Shivamogga ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಶಿವಮೊಗ್ಗ (Shivamogga) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಶಿವಮೊಗ್ಗ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 7 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಶಿವಮೊಗ್ಗ, ಭದ್ರಾವತಿ, ತೀರ್ಥಹಳ್ಳಿ, ಸಾಗರ, ಶಿಕಾರಿಪುರ, ಸೊರಬ, ಹೊಸನಗರ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಅಡಿಕೆ ಬೆಳೆ, ಜೋಗ ಜಲಪಾತ, ಮಲೆನಾಡಿನ ನಿಸರ್ಗ ಸಂಪತ್ತು ಮತ್ತು ಕಬ್ಬಿಣ ಕೈಗಾರಿಕೆ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://shivamogga.nic.in', 'ಶಿವಮೊಗ್ಗ, Shivamogga, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲಾ ಪುಟ', '/districts/shivamogga.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_041', 'ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆಯ 7 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಶಿವಮೊಗ್ಗ Shivamogga sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಶಿವಮೊಗ್ಗ (Shivamogga) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಶಿವಮೊಗ್ಗ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **7 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಶಿವಮೊಗ್ಗ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಶಿವಮೊಗ್ಗ, Shivamogga, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 7 mla', '🔎 ಶಿವಮೊಗ್ಗ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_042', 'ಚಿತ್ರದುರ್ಗ (Chitradurga) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಚಿತ್ರದುರ್ಗ Chitradurga ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಚಿತ್ರದುರ್ಗ (Chitradurga) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಚಿತ್ರದುರ್ಗ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 6 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಚಿತ್ರದುರ್ಗ, ಚಳ್ಳಕೆರೆ, ಹಿರಿಯೂರು, ಹೊಳಲ್ಕೆರೆ, ಹೊಸದುರ್ಗ, ಮೊಳಕಾಲ್ಮುರು.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಏಳು ಸುತ್ತಿನ ಕೋಟೆ, ಸೈನ್ಸ್ ಸಿಟಿ (ಚಳ್ಳಕೆರೆ), ಸಿರಿಧಾನ್ಯ ಮತ್ತು ಪವನ ಶಕ್ತಿ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://chitradurga.nic.in', 'ಚಿತ್ರದುರ್ಗ, Chitradurga, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಚಿತ್ರದುರ್ಗ ಜಿಲ್ಲಾ ಪುಟ', '/districts/chitradurga.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_043', 'ಚಿತ್ರದುರ್ಗ ಜಿಲ್ಲೆಯ 6 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಚಿತ್ರದುರ್ಗ Chitradurga sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಚಿತ್ರದುರ್ಗ (Chitradurga) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಚಿತ್ರದುರ್ಗ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **6 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಚಿತ್ರದುರ್ಗ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಚಿತ್ರದುರ್ಗ, Chitradurga, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 6 mla', '🔎 ಚಿತ್ರದುರ್ಗ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_044', 'ದಾವಣಗೆರೆ (Davanagere) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ದಾವಣಗೆರೆ Davanagere ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ದಾವಣಗೆರೆ (Davanagere) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ದಾವಣಗೆರೆ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 7 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ದಾವಣಗೆರೆ, ಹರಿಹರ, ಜಗಳೂರು, ಚನ್ನಗಿರಿ, ಹೊನ್ನಾಳಿ, ನ್ಯಾಮತಿ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಬೆಣ್ಣೆ ದೋಸೆ, ಜವಳಿ ಕೈಗಾರಿಕೆ (ಮ್ಯಾಂಚೆಸ್ಟರ್), ಅಡಿಕೆ ಮತ್ತು ಮೆಕ್ಕೆಜೋಳ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://davanagere.nic.in', 'ದಾವಣಗೆರೆ, Davanagere, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ದಾವಣಗೆರೆ ಜಿಲ್ಲಾ ಪುಟ', '/districts/davanagere.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_045', 'ದಾವಣಗೆರೆ ಜಿಲ್ಲೆಯ 7 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ದಾವಣಗೆರೆ Davanagere sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ದಾವಣಗೆರೆ (Davanagere) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ದಾವಣಗೆರೆ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **7 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ದಾವಣಗೆರೆ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ದಾವಣಗೆರೆ, Davanagere, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 7 mla', '🔎 ದಾವಣಗೆರೆ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_046', 'ಮೈಸೂರು (Mysuru) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಮೈಸೂರು Mysuru ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಮೈಸೂರು (Mysuru) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಮೈಸೂರು
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 11 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಮೈಸೂರು, ನಂಜನಗೂಡು, ಹುಣಸೂರು, ಪಿರಿಯಾಪಟ್ಟಣ, ಕೆ.ಆರ್.ನಗರ, ಹೆಚ್.ಡಿ.ಕೋಟೆ, ಸರಗೂರು, ಟಿ.ನರಸೀಪುರ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಸಾಂಸ್ಕೃತಿಕ ರಾಜಧಾನಿ, ಅರಮನೆ, ಪ್ರವಾಸೋದ್ಯಮ, ಮೈಸೂರು ಪಾಕ್ ಮತ್ತು ರೇಷ್ಮೆ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://mysuru.nic.in', 'ಮೈಸೂರು, Mysuru, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಮೈಸೂರು ಜಿಲ್ಲಾ ಪುಟ', '/districts/mysuru.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_047', 'ಮೈಸೂರು ಜಿಲ್ಲೆಯ 11 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಮೈಸೂರು Mysuru sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಮೈಸೂರು (Mysuru) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಮೈಸೂರು ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **11 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಮೈಸೂರು''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಮೈಸೂರು, Mysuru, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 11 mla', '🔎 ಮೈಸೂರು Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_048', 'ಮಂಡ್ಯ (Mandya) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಮಂಡ್ಯ Mandya ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಮಂಡ್ಯ (Mandya) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಮಂಡ್ಯ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 7 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಮಂಡ್ಯ, ಮದ್ದೂರು, ಮಳವಳ್ಳಿ, ಪಾಂಡವಪುರ, ಶ್ರೀರಂಗಪಟ್ಟಣ, ಕೃಷ್ಣರಾಜಪೇಟೆ, ನಾಗಮಂಗಲ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಸಕ್ಕರೆ ನಾಡು, ಕಾವೇರಿ ನೀರಾವರಿ ಕೃಷಿ, ಬೆಲ್ಲ ಮತ್ತು ಭತ್ತ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://mandya.nic.in', 'ಮಂಡ್ಯ, Mandya, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಮಂಡ್ಯ ಜಿಲ್ಲಾ ಪುಟ', '/districts/mandya.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_049', 'ಮಂಡ್ಯ ಜಿಲ್ಲೆಯ 7 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಮಂಡ್ಯ Mandya sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಮಂಡ್ಯ (Mandya) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಮಂಡ್ಯ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **7 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಮಂಡ್ಯ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಮಂಡ್ಯ, Mandya, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 7 mla', '🔎 ಮಂಡ್ಯ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_050', 'ಹಾಸನ (Hassan) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಹಾಸನ Hassan ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಹಾಸನ (Hassan) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಹಾಸನ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 7 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಹಾಸನ, ಅರಸೀಕೆರೆ, ಚನ್ನರಾಯಪಟ್ಟಣ, ಹೊಳೆನರಸೀಪುರ, ಸಕಲೇಶಪುರ, ಆಲೂರು, ಅರಕಲಗೂಡು, ಬೇಲೂರು.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಶಿಲ್ಪಕಲೆ (ಬೇಲೂರು-ಹಳೇಬೀಡು), ಹಾಸನಾಂಬೆ ದೇವಾಲಯ, ಕಾಫಿ ಮತ್ತು ಏಲಕ್ಕಿ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://hassan.nic.in', 'ಹಾಸನ, Hassan, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಹಾಸನ ಜಿಲ್ಲಾ ಪುಟ', '/districts/hassan.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_051', 'ಹಾಸನ ಜಿಲ್ಲೆಯ 7 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಹಾಸನ Hassan sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಹಾಸನ (Hassan) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಹಾಸನ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **7 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಹಾಸನ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಹಾಸನ, Hassan, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 7 mla', '🔎 ಹಾಸನ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_052', 'ಚಿಕ್ಕಮಗಳೂರು (Chikkamagaluru) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಚಿಕ್ಕಮಗಳೂರು Chikkamagaluru ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಚಿಕ್ಕಮಗಳೂರು (Chikkamagaluru) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಚಿಕ್ಕಮಗಳೂರು
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 5 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಚಿಕ್ಕಮಗಳೂರು, ಕಡೂರು, ತರೀಕೆರೆ, ಮೂಡಿಗೆರೆ, ಕೊಪ್ಪ, ಶೃಂಗೇರಿ, ನರಸಿಂಹರಾಜಪುರ, ಅಜ್ಜಂಪುರ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಕಾಫಿಯ ತವರು, ಮುಳ್ಳಯ್ಯನಗಿರಿ, ಶೃಂಗೇರಿ ಶಾರದಾಂಬೆ ಮತ್ತು ಮಲೆನಾಡು ಪ್ರವಾಸೋದ್ಯಮ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://chikkamagaluru.nic.in', 'ಚಿಕ್ಕಮಗಳೂರು, Chikkamagaluru, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಚಿಕ್ಕಮಗಳೂರು ಜಿಲ್ಲಾ ಪುಟ', '/districts/chikkamagaluru.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_053', 'ಚಿಕ್ಕಮಗಳೂರು ಜಿಲ್ಲೆಯ 5 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಚಿಕ್ಕಮಗಳೂರು Chikkamagaluru sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಚಿಕ್ಕಮಗಳೂರು (Chikkamagaluru) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಚಿಕ್ಕಮಗಳೂರು ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **5 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಚಿಕ್ಕಮಗಳೂರು''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಚಿಕ್ಕಮಗಳೂರು, Chikkamagaluru, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 5 mla', '🔎 ಚಿಕ್ಕಮಗಳೂರು Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_054', 'ದಕ್ಷಿಣ ಕನ್ನಡ (Dakshina Kannada) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ದಕ್ಷಿಣ ಕನ್ನಡ Dakshina Kannada ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ದಕ್ಷಿಣ ಕನ್ನಡ (Dakshina Kannada) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ದಕ್ಷಿಣ ಕನ್ನಡ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 8 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಮಂಗಳೂರು, ಬಂಟ್ವಾಳ, ಪುತ್ತೂರು, ಬೆಳ್ತಂಗಡಿ, ಸುಳ್ಯ, ಕಡಬ, ಮೂಡುಬಿದಿರೆ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ನವ ಮಂಗಳೂರು ಬಂದರು, ಬ್ಯಾಂಕಿಂಗ್ ರಾಜಧಾನಿ, ಕರಾವಳಿ ಶಿಕ್ಷಣ ಹಬ್ ಮತ್ತು ಗೋಡಂಬಿ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://dakshinakannada.nic.in', 'ದಕ್ಷಿಣ ಕನ್ನಡ, Dakshina Kannada, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ದಕ್ಷಿಣ ಕನ್ನಡ ಜಿಲ್ಲಾ ಪುಟ', '/districts/dakshina_kannada.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_055', 'ದಕ್ಷಿಣ ಕನ್ನಡ ಜಿಲ್ಲೆಯ 8 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ದಕ್ಷಿಣ ಕನ್ನಡ Dakshina Kannada sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ದಕ್ಷಿಣ ಕನ್ನಡ (Dakshina Kannada) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ದಕ್ಷಿಣ ಕನ್ನಡ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **8 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ದಕ್ಷಿಣ ಕನ್ನಡ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ದಕ್ಷಿಣ ಕನ್ನಡ, Dakshina Kannada, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 8 mla', '🔎 ದಕ್ಷಿಣ ಕನ್ನಡ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_056', 'ಉಡುಪಿ (Udupi) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಉಡುಪಿ Udupi ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಉಡುಪಿ (Udupi) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಉಡುಪಿ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 5 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಉಡುಪಿ, ಕುಂದಾಪುರ, ಕಾರ್ಕಳ, ಬೈಂದೂರು, ಬ್ರಹ್ಮಾವರ, ಕಾಪು, ಹೆಬ್ರಿ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಶ್ರೀಕೃಷ್ಣ ಮಠ, ಕರಾವಳಿ ಪ್ರವಾಸೋದ್ಯಮ, ಮೀನುಗಾರಿಕೆ ಮತ್ತು ಉನ್ನತ ಶಿಕ್ಷಣ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://udupi.nic.in', 'ಉಡುಪಿ, Udupi, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಉಡುಪಿ ಜಿಲ್ಲಾ ಪುಟ', '/districts/udupi.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_057', 'ಉಡುಪಿ ಜಿಲ್ಲೆಯ 5 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಉಡುಪಿ Udupi sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಉಡುಪಿ (Udupi) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಉಡುಪಿ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **5 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಉಡುಪಿ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಉಡುಪಿ, Udupi, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 5 mla', '🔎 ಉಡುಪಿ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_058', 'ಕೊಡಗು (Kodagu) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಕೊಡಗು Kodagu ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಕೊಡಗು (Kodagu) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಕೊಡಗು
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 2 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಮಡಿಕೇರಿ, ವಿರಾಜಪೇಟೆ, ಸೋಮವಾರಪೇಟೆ, ಪೊನ್ನಂಪೇಟೆ, ಕುಶಾಲನಗರ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಭಾರತದ ಸ್ಕಾಟ್‌ಲ್ಯಾಂಡ್, ಕಾಫಿ ಎಸ್ಟೇಟ್, ಕಿತ್ತಳೆ, ಏಲಕ್ಕಿ ಮತ್ತು ಯೋಧರ ನಾಡು.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://kodagu.nic.in', 'ಕೊಡಗು, Kodagu, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಕೊಡಗು ಜಿಲ್ಲಾ ಪುಟ', '/districts/kodagu.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_059', 'ಕೊಡಗು ಜಿಲ್ಲೆಯ 2 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಕೊಡಗು Kodagu sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಕೊಡಗು (Kodagu) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಕೊಡಗು ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **2 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಕೊಡಗು''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಕೊಡಗು, Kodagu, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 2 mla', '🔎 ಕೊಡಗು Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_060', 'ಚಾಮರಾಜನಗರ (Chamarajanagar) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಚಾಮರಾಜನಗರ Chamarajanagar ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಚಾಮರಾಜನಗರ (Chamarajanagar) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಚಾಮರಾಜನಗರ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 4 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಚಾಮರಾಜನಗರ, ಗುಂಡ್ಲುಪೇಟೆ, ಕೊಳ್ಳೇಗಾಲ, ಹನೂರು, ಯಳಂದೂರು.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಬಂಡೀಪುರ ಹುಲಿ ಸಂರಕ್ಷಿತಾರಣ್ಯ, ಮಲೆ ಮಹದೇಶ್ವರ ಬೆಟ್ಟ, ರೇಷ್ಮೆ ಮತ್ತು ಅರಣ್ಯ ಉತ್ಪನ್ನಗಳು.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://chamarajanagar.nic.in', 'ಚಾಮರಾಜನಗರ, Chamarajanagar, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಚಾಮರಾಜನಗರ ಜಿಲ್ಲಾ ಪುಟ', '/districts/chamarajanagar.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_061', 'ಚಾಮರಾಜನಗರ ಜಿಲ್ಲೆಯ 4 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಚಾಮರಾಜನಗರ Chamarajanagar sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಚಾಮರಾಜನಗರ (Chamarajanagar) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಚಾಮರಾಜನಗರ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **4 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಚಾಮರಾಜನಗರ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಚಾಮರಾಜನಗರ, Chamarajanagar, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 4 mla', '🔎 ಚಾಮರಾಜನಗರ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_062', 'ಬೆಳಗಾವಿ (Belagavi) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಬೆಳಗಾವಿ Belagavi ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಬೆಳಗಾವಿ (Belagavi) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಬೆಳಗಾವಿ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 18 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಬೆಳಗಾವಿ, ಗೋಕಾಕ್, ಚಿಕ್ಕೋಡಿ, ಅಥಣಿ, ಬೈಲಹೊಂಗಲ, ಹುಕ್ಕೇರಿ, ರಾಮದುರ್ಗ, ಸವದತ್ತಿ, ಖಾನಾಪುರ, ರಾಯಬಾಗ, ನಿಪ್ಪಾಣಿ, ಮೂಡಲಗಿ, ಕಾಗವಾಡ, ಕಿತ್ತೂರು.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಸುವರ್ಣ ಸೌಧ, ಕುಂದಾ ಸಿಹಿ, ಕಬ್ಬು ಮತ್ತು ಸಕ್ಕರೆ ಕಾರ್ಖಾನೆಗಳು, ಗಡಿ ವಾಣಿಜ್ಯ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://belagavi.nic.in', 'ಬೆಳಗಾವಿ, Belagavi, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಬೆಳಗಾವಿ ಜಿಲ್ಲಾ ಪುಟ', '/districts/belagavi.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_063', 'ಬೆಳಗಾವಿ ಜಿಲ್ಲೆಯ 18 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಬೆಳಗಾವಿ Belagavi sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಬೆಳಗಾವಿ (Belagavi) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಬೆಳಗಾವಿ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **18 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಬೆಳಗಾವಿ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಬೆಳಗಾವಿ, Belagavi, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 18 mla', '🔎 ಬೆಳಗಾವಿ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_064', 'ಧಾರವಾಡ (Dharwad) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಧಾರವಾಡ Dharwad ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಧಾರವಾಡ (Dharwad) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಧಾರವಾಡ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 7 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಧಾರವಾಡ, ಹುಬ್ಬಳ್ಳಿ ನಗರ, ಹುಬ್ಬಳ್ಳಿ ಗ್ರಾಮೀಣ, ಕುಂದಗೋಳ, ನವಲಗುಂದ, ಕಲಘಟಗಿ, ಅಣ್ಣಿಗೇರಿ, ಅಳ್ನಾವರ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ವಿದ್ಯಾನಗರಿ, ಧಾರವಾಡ ಪೇಡ, ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ ಸ್ಮಾರ್ಟ್ ಸಿಟಿ ಮತ್ತು ಹೈಕೋರ್ಟ್ ಪೀಠ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://dharwad.nic.in', 'ಧಾರವಾಡ, Dharwad, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಧಾರವಾಡ ಜಿಲ್ಲಾ ಪುಟ', '/districts/dharwad.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_065', 'ಧಾರವಾಡ ಜಿಲ್ಲೆಯ 7 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಧಾರವಾಡ Dharwad sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಧಾರವಾಡ (Dharwad) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಧಾರವಾಡ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **7 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಧಾರವಾಡ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಧಾರವಾಡ, Dharwad, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 7 mla', '🔎 ಧಾರವಾಡ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_066', 'ವಿಜಯಪುರ (Vijayapura) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ವಿಜಯಪುರ Vijayapura ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ವಿಜಯಪುರ (Vijayapura) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ವಿಜಯಪುರ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 8 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ವಿಜಯಪುರ, ಇಂಡಿ, ಮುದ್ದೇಬಿಹಾಳ, ಬಸವನ ಬಾಗೇವಾಡಿ, ಸಿಂದಗಿ, ತಾಳಿಕೋಟೆ, ಚಡಚಣ, ತಿಕೋಟಾ, ಬಬಲೇಶ್ವರ, ದೇವರಹಿಪ್ಪರಗಿ, ಕೊಲ್ಹಾರ, ಆಲಮೇಲ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಗೋಳಗುಮ್ಮಟ, ಐತಿಹಾಸಿಕ ಸ್ಮಾರಕಗಳು, ದ್ರಾಕ್ಷಿ ಮತ್ತು ನಿಂಬೆ ಬೆಳೆ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://vijayapura.nic.in', 'ವಿಜಯಪುರ, Vijayapura, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ವಿಜಯಪುರ ಜಿಲ್ಲಾ ಪುಟ', '/districts/vijayapura.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_067', 'ವಿಜಯಪುರ ಜಿಲ್ಲೆಯ 8 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ವಿಜಯಪುರ Vijayapura sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ವಿಜಯಪುರ (Vijayapura) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ವಿಜಯಪುರ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **8 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ವಿಜಯಪುರ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ವಿಜಯಪುರ, Vijayapura, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 8 mla', '🔎 ವಿಜಯಪುರ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_068', 'ಬಾಗಲಕೋಟೆ (Bagalkote) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಬಾಗಲಕೋಟೆ Bagalkote ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಬಾಗಲಕೋಟೆ (Bagalkote) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಬಾಗಲಕೋಟೆ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 7 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಬಾಗಲಕೋಟೆ, ಬಾದಾಮಿ, ಜಮಖಂಡಿ, ಮುಧೋಳ, ಹುನಗುಂದ, ಬೀಳಗಿ, ರಬಕವಿ ಬನಹಟ್ಟಿ, ಇಳಕಲ್, ಗುಳೇದಗುಡ್ಡ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಇಳಕಲ್ ಸೀರೆ, ಬಾದಾಮಿ ಗುಹಾಂತರ ದೇವಾಲಯಗಳು, ಪಟ್ಟದಕಲ್ಲು ಮತ್ತು ಕಬ್ಬು.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://bagalkote.nic.in', 'ಬಾಗಲಕೋಟೆ, Bagalkote, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಬಾಗಲಕೋಟೆ ಜಿಲ್ಲಾ ಪುಟ', '/districts/bagalkote.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_069', 'ಬಾಗಲಕೋಟೆ ಜಿಲ್ಲೆಯ 7 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಬಾಗಲಕೋಟೆ Bagalkote sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಬಾಗಲಕೋಟೆ (Bagalkote) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಬಾಗಲಕೋಟೆ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **7 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಬಾಗಲಕೋಟೆ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಬಾಗಲಕೋಟೆ, Bagalkote, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 7 mla', '🔎 ಬಾಗಲಕೋಟೆ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_070', 'ಗದಗ (Gadag) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಗದಗ Gadag ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಗದಗ (Gadag) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಗದಗ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 4 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಗದಗ, ರೋಣ, ಶಿರಹಟ್ಟಿ, ನರಗುಂದ, ಮುಂಡರಗಿ, ಗಜೇಂದ್ರಗಡ, ಲಕ್ಷ್ಮೇಶ್ವರ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಮುದ್ರಣ ನಗರಿ, ಸಹಕಾರಿ ಚಳವಳಿಯ ತವರು, ಕಪ್ಪತಗುಡ್ಡ ಮತ್ತು ಪವನ ವಿದ್ಯುತ್.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://gadag.nic.in', 'ಗದಗ, Gadag, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಗದಗ ಜಿಲ್ಲಾ ಪುಟ', '/districts/gadag.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_071', 'ಗದಗ ಜಿಲ್ಲೆಯ 4 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಗದಗ Gadag sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಗದಗ (Gadag) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಗದಗ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **4 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಗದಗ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಗದಗ, Gadag, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 4 mla', '🔎 ಗದಗ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_072', 'ಹಾವೇರಿ (Haveri) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಹಾವೇರಿ Haveri ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಹಾವೇರಿ (Haveri) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಹಾವೇರಿ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 6 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಹಾವೇರಿ, ರಾಣೆಬೆನ್ನೂರು, ಬ್ಯಾಡಗಿ, ಹಿರೇಕೆರೂರು, ಹಾನಗಲ್, ಸವಣೂರು, ಶಿಗ್ಗಾಂವಿ, ರಟ್ಟಿಹಳ್ಳಿ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಬ್ಯಾಡಗಿ ಮೆಣಸಿನಕಾಯಿ, ಏಲಕ್ಕಿ ಹಾರ, ಕನಕದಾಸರ ತವರು (ಕಾಗಿನೆಲೆ) ಮತ್ತು ಬೀಜೋತ್ಪಾದನೆ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://haveri.nic.in', 'ಹಾವೇರಿ, Haveri, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಹಾವೇರಿ ಜಿಲ್ಲಾ ಪುಟ', '/districts/haveri.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_073', 'ಹಾವೇರಿ ಜಿಲ್ಲೆಯ 6 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಹಾವೇರಿ Haveri sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಹಾವೇರಿ (Haveri) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಹಾವೇರಿ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **6 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಹಾವೇರಿ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಹಾವೇರಿ, Haveri, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 6 mla', '🔎 ಹಾವೇರಿ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_074', 'ಉತ್ತರ ಕನ್ನಡ (Uttara Kannada) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಉತ್ತರ ಕನ್ನಡ Uttara Kannada ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಉತ್ತರ ಕನ್ನಡ (Uttara Kannada) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಉತ್ತರ ಕನ್ನಡ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 6 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಕಾರವಾರ, ಅಂಕೋಲಾ, ಕುಮಟಾ, ಹೊನ್ನಾವರ, ಭಟ್ಕಳ, ಶಿರಸಿ, ಸಿದ್ದಾಪುರ, ಯಲ್ಲಾಪುರ, ಹಳಿಯಾಳ, ಜೋಯಿಡಾ, ಮುಂಡಗೋಡ, ದಾಂಡೇಲಿ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಐಎನ್‌ಎಸ್ ಕದಂಬ ನೌಕಾನೆಲೆ, ದಾಂಡೇಲಿ ಅರಣ್ಯ, ಗೋಕರ್ಣ ಪ್ರವಾಸೋದ್ಯಮ ಮತ್ತು ಅಡಿಕೆ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://uttarakannada.nic.in', 'ಉತ್ತರ ಕನ್ನಡ, Uttara Kannada, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಉತ್ತರ ಕನ್ನಡ ಜಿಲ್ಲಾ ಪುಟ', '/districts/uttara_kannada.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_075', 'ಉತ್ತರ ಕನ್ನಡ ಜಿಲ್ಲೆಯ 6 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಉತ್ತರ ಕನ್ನಡ Uttara Kannada sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಉತ್ತರ ಕನ್ನಡ (Uttara Kannada) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಉತ್ತರ ಕನ್ನಡ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **6 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಉತ್ತರ ಕನ್ನಡ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಉತ್ತರ ಕನ್ನಡ, Uttara Kannada, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 6 mla', '🔎 ಉತ್ತರ ಕನ್ನಡ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_076', 'ಕಲಬುರಗಿ (Kalaburagi) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಕಲಬುರಗಿ Kalaburagi ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಕಲಬುರಗಿ (Kalaburagi) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಕಲಬುರಗಿ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 9 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಕಲಬುರಗಿ, ಆಳಂದ, ಅಫಜಲಪುರ, ಜೇವರ್ಗಿ, ಸೇಡಂ, ಚಿತ್ತಾಪುರ, ಚಿಂಚೋಳಿ, ಕಾಳಗಿ, ಕಮಲಾಪುರ, ಶಹಾಬಾದ್, ಯಡ್ರಾಮಿ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ತೊಗರಿ ಕಣಜ, ಸಿಮೆಂಟ್ ಕೈಗಾರಿಕೆಗಳು, ಗುಲಬರ್ಗಾ ಕೋಟೆ ಮತ್ತು ಹೈಕೋರ್ಟ್ ಪೀಠ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://kalaburagi.nic.in', 'ಕಲಬುರಗಿ, Kalaburagi, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಕಲಬುರಗಿ ಜಿಲ್ಲಾ ಪುಟ', '/districts/kalaburagi.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_077', 'ಕಲಬುರಗಿ ಜಿಲ್ಲೆಯ 9 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಕಲಬುರಗಿ Kalaburagi sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಕಲಬುರಗಿ (Kalaburagi) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಕಲಬುರಗಿ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **9 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಕಲಬುರಗಿ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಕಲಬುರಗಿ, Kalaburagi, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 9 mla', '🔎 ಕಲಬುರಗಿ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_078', 'ಬೀದರ್ (Bidar) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಬೀದರ್ Bidar ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಬೀದರ್ (Bidar) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಬೀದರ್
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 6 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಬೀದರ್, ಬಸವಕಲ್ಯಾಣ, ಭಾಲ್ಕಿ, ಹುಮ್ನಾಬಾದ್, ಔರಾದ್, ಕಮಲನಗರ, ಚಿಟಗುಪ್ಪ, ಹುಲಸೂರು.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಬಿದ್ರಿ ಕಲೆ, ಗುರು ನಾನಕ್ ಝೀರಾ, ಅನುಭವ ಮಂಟಪ (ಬಸವಕಲ್ಯಾಣ) ಮತ್ತು ಐತಿಹಾಸಿಕ ಕೋಟೆ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://bidar.nic.in', 'ಬೀದರ್, Bidar, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಬೀದರ್ ಜಿಲ್ಲಾ ಪುಟ', '/districts/bidar.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_079', 'ಬೀದರ್ ಜಿಲ್ಲೆಯ 6 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಬೀದರ್ Bidar sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಬೀದರ್ (Bidar) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಬೀದರ್ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **6 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಬೀದರ್''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಬೀದರ್, Bidar, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 6 mla', '🔎 ಬೀದರ್ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_080', 'ರಾಯಚೂರು (Raichur) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ರಾಯಚೂರು Raichur ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ರಾಯಚೂರು (Raichur) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ರಾಯಚೂರು
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 7 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ರಾಯಚೂರು, ಮಾನ್ವಿ, ಸಿಂಧನೂರು, ದೇವದುರ್ಗ, ಲಿಂಗಸುಗೂರು, ಮಸ್ಕಿ, ಸಿರವಾರ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಶಾಖೋತ್ಪನ್ನ ವಿದ್ಯುತ್ ಸ್ಥಾವರ (RTPS), ಸೋನಾ ಮಸೂರಿ ಭತ್ತ ಮತ್ತು ಹತ್ತಿ ಬೆಳೆ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://raichur.nic.in', 'ರಾಯಚೂರು, Raichur, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ರಾಯಚೂರು ಜಿಲ್ಲಾ ಪುಟ', '/districts/raichur.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_081', 'ರಾಯಚೂರು ಜಿಲ್ಲೆಯ 7 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ರಾಯಚೂರು Raichur sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ರಾಯಚೂರು (Raichur) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ರಾಯಚೂರು ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **7 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ರಾಯಚೂರು''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ರಾಯಚೂರು, Raichur, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 7 mla', '🔎 ರಾಯಚೂರು Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_082', 'ಕೊಪ್ಪಳ (Koppal) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಕೊಪ್ಪಳ Koppal ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಕೊಪ್ಪಳ (Koppal) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಕೊಪ್ಪಳ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 5 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಕೊಪ್ಪಳ, ಗಂಗಾವತಿ, ಕುಷ್ಟಗಿ, ಯಲಬುರ್ಗಾ, ಕನಕಗಿರಿ, ಕಾರಟಗಿ, ಕುಕನೂರು.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಕಿನ್ನಾಳ ಕರಕುಶಲ ಕಲೆ, ಭತ್ತದ ಕಣಜ (ಗಂಗಾವತಿ), ಅಂಜನಾದ್ರಿ ಬೆಟ್ಟ ಮತ್ತು ಆನೆಗೊಂದಿ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://koppal.nic.in', 'ಕೊಪ್ಪಳ, Koppal, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಕೊಪ್ಪಳ ಜಿಲ್ಲಾ ಪುಟ', '/districts/koppal.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_083', 'ಕೊಪ್ಪಳ ಜಿಲ್ಲೆಯ 5 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಕೊಪ್ಪಳ Koppal sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಕೊಪ್ಪಳ (Koppal) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಕೊಪ್ಪಳ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **5 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಕೊಪ್ಪಳ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಕೊಪ್ಪಳ, Koppal, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 5 mla', '🔎 ಕೊಪ್ಪಳ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_084', 'ಬಳ್ಳಾರಿ (Ballari) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಬಳ್ಳಾರಿ Ballari ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಬಳ್ಳಾರಿ (Ballari) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಬಳ್ಳಾರಿ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 5 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಬಳ್ಳಾರಿ, ಸಿರುಗುಪ್ಪ, ಸಂಡೂರು, ಕುರುಗೋಡು, ಕಂಪ್ಲಿ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಉಕ್ಕು ಕೈಗಾರಿಕೆ (ಜಿಂದಾಲ್), ಕಬ್ಬಿಣದ ಅದಿರು, ಜೀನ್ಸ್ ವಸ್ತ್ರೋದ್ಯಮ ಮತ್ತು ಬಳ್ಳಾರಿ ಕೋಟೆ.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://ballari.nic.in', 'ಬಳ್ಳಾರಿ, Ballari, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಬಳ್ಳಾರಿ ಜಿಲ್ಲಾ ಪುಟ', '/districts/ballari.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_085', 'ಬಳ್ಳಾರಿ ಜಿಲ್ಲೆಯ 5 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಬಳ್ಳಾರಿ Ballari sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಬಳ್ಳಾರಿ (Ballari) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಬಳ್ಳಾರಿ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **5 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಬಳ್ಳಾರಿ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಬಳ್ಳಾರಿ, Ballari, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 5 mla', '🔎 ಬಳ್ಳಾರಿ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_086', 'ಯಾದಗಿರಿ (Yadgir) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ಯಾದಗಿರಿ Yadgir ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ಯಾದಗಿರಿ (Yadgir) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ಯಾದಗಿರಿ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 4 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಯಾದಗಿರಿ, ಶಹಾಪುರ, ಸುರಪುರ, ಗುರುಮಿಠಕಲ್, ವಡಗೇರಾ, ಹುಣಸಗಿ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಬೋನಾಳ ಪಕ್ಷಿಧಾಮ, ತೊಗರಿ ಮತ್ತು ಭತ್ತದ ಕೃಷಿ, ಕೃಷ್ಣಾ ನದಿ ಕಣಿವೆ ಯೋಜನೆಗಳು.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://yadgir.nic.in', 'ಯಾದಗಿರಿ, Yadgir, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ಯಾದಗಿರಿ ಜಿಲ್ಲಾ ಪುಟ', '/districts/yadgir.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_087', 'ಯಾದಗಿರಿ ಜಿಲ್ಲೆಯ 4 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ಯಾದಗಿರಿ Yadgir sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ಯಾದಗಿರಿ (Yadgir) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ಯಾದಗಿರಿ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **4 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ಯಾದಗಿರಿ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ಯಾದಗಿರಿ, Yadgir, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 4 mla', '🔎 ಯಾದಗಿರಿ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_088', 'ವಿಜಯನಗರ (Vijayanagara) ಜಿಲ್ಲೆಯ ತಾಲೂಕುಗಳು, ಆಡಳಿತ ಕೇಂದ್ರ ಮತ್ತು ಪ್ರಮುಖ ವಿವರಗಳು ಯಾವುವು?', 'ವಿಜಯನಗರ Vijayanagara ಜಿಲ್ಲೆ ತಾಲೂಕು dc office taluks list administration mla', '### 🏛️ ವಿಜಯನಗರ (Vijayanagara) ಜಿಲ್ಲಾ ಆಡಳಿತ ಸಮಗ್ರ ವಿವರ

* **ಜಿಲ್ಲಾ ಕೇಂದ್ರ:** ವಿಜಯನಗರ
* **ಒಟ್ಟು ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು (MLA Seats):** 5 ಕ್ಷೇತ್ರಗಳು.
* **ಒಳಗೊಂಡಿರುವ ತಾಲೂಕುಗಳು:** ಹೊಸಪೇಟೆ, ಹರಪನಹಳ್ಳಿ, ಹೂವಿನಹಡಗಲಿ, ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ, ಕೊಟ್ಟೂರು, ಕೂಡ್ಲಿಗಿ.
* **ಪ್ರಮುಖ ಆರ್ಥಿಕತೆ & ವೈಶಿಷ್ಟ್ಯ:** ಹಂಪಿ ವಿಶ್ವ ಪರಂಪರೆ ತಾಣ, ತುಂಗಭದ್ರಾ ಜಲಾಶಯ (ಹೊಸಪೇಟೆ) ಮತ್ತು ಕೈಗಾರಿಕೆಗಳು.

---

### 👥 ಪ್ರಮುಖ ಜಿಲ್ಲಾ ಕಚೇರಿಗಳು & ಸಂಪರ್ಕ:
1. **ಜಿಲ್ಲಾಧಿಕಾರಿಗಳ ಕಚೇರಿ (DC Office):** ಕಂದಾಯ ಆಡಳಿತ, ವಿಪತ್ತು ನಿರ್ವಹಣೆ ಹಾಗೂ ಜಿಲ್ಲಾ ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳು.
2. **ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ ಕಚೇರಿ (SP Office):** ಜಿಲ್ಲೆಯ ಕಾನೂನು ಸುವ್ಯವಸ್ಥೆ ಮತ್ತು ಸಂಚಾರ ನಿಯಂತ್ರಣ.
3. **ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ ಕಾರ್ಯಾಲಯ (ZP CEO Office):** ಗ್ರಾಮೀಣಾಭಿವೃದ್ಧಿ ಮತ್ತು ಪಂಚಾಯತ್ ರಾಜ್ ಯೋಜನೆಗಳು.

💡 ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರ್ ಕಚೇರಿ ಮತ್ತು ನಾಡಕಚೇರಿಗಳು ಸಾರ್ವಜನಿಕ ಪ್ರಮಾಣಪತ್ರ ಸೇವೆಗಳನ್ನು ಒದಗಿಸುತ್ತವೆ.', 'DISTRICTS', 'kn', 'https://vijayanagara.nic.in', 'ವಿಜಯನಗರ, Vijayanagara, taluks, dc office, ಜಿಲ್ಲಾಡಳಿತ, ತಾಲೂಕುಗಳು, mla seats', '🏛️ ವಿಜಯನಗರ ಜಿಲ್ಲಾ ಪುಟ', '/districts/vijayanagara.html');
INSERT INTO ai_faq (id, question, normalized_question, answer, category, language, source_url, keywords, action_label, action_url)
VALUES ('faq_dist_sir_089', 'ವಿಜಯನಗರ ಜಿಲ್ಲೆಯ 5 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ಮತದಾರರ ಪಟ್ಟಿ (SIR Draft Roll) ಪರಿಶೀಲಿಸುವುದು ಹೇಗೆ?', 'ವಿಜಯನಗರ Vijayanagara sir voter list draft roll ceo karnataka ಮತದಾರರ ಪಟ್ಟಿ polling booth', '### 🗳️ ವಿಜಯನಗರ (Vijayanagara) ಜಿಲ್ಲೆಯ ಮತದಾರರ ಪಟ್ಟಿ (Draft Roll) ಪರಿಶೀಲನೆ

ವಿಜಯನಗರ ಜಿಲ್ಲೆಯ ಎಲ್ಲಾ **5 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ** ಅಧಿಕೃತ ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ಆನ್‌ಲೈನ್‌ನಲ್ಲಿ ವೀಕ್ಷಿಸಬಹುದು.

---

### 📋 ಹಂತ-ಹಂತದ ಪರಿಶೀಲನಾ ವಿಧಾನ:
1. ಕರ್ನಾಟ ಪೋರ್ಟಲ್‌ನ **SIR Voter Roll** ವಿಭಾಗಕ್ಕೆ ಭೇಟಿ ನೀಡಿ.
2. ಜಿಲ್ಲೆಗಳ ಪಟ್ಟಿಯಲ್ಲಿ **''ವಿಜಯನಗರ''** ಆಯ್ಕೆಮಾಡಿ.
3. ನಿಮ್ಮ ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ ಹಾಗೂ ನಿಮ್ಮ ಬಡಾವಣೆಗೆ ನಿಗದಿಪಡಿಸಲಾದ **Part Number (ಮತಗಟ್ಟೆ ಭಾಗ ಸಂಖ್ಯೆ)** ಆಯ್ಕೆಮಾಡಿ.
4. ಅಧಿಕೃತ **Draft Roll PDF** ಡೌನ್‌ಲೋಡ್ ಆಗುತ್ತದೆ.
5. ನಿಮ್ಮ EPIC ಸಂಖ್ಯೆ ಅಥವಾ ಹೆಸರಿನಿಂದ ಪಟ್ಟಿಯಲ್ಲಿ ನಿಮ್ಮ ವಿವರ ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

⚠️ ಹೆಸರಿಲ್ಲದಿದ್ದರೆ ಅಥವಾ ವಿಳಾಸ ಬದಲಾಗಿದ್ದರೆ ತಕ್ಷಣ [voters.eci.gov.in](https://voters.eci.gov.in) ನಲ್ಲಿ **Form 6 / Form 8** ಸಲ್ಲಿಸಿ.', 'SIR', 'kn', 'https://ceokarnataka.kar.nic.in', 'ವಿಜಯನಗರ, Vijayanagara, voter list, draft roll, ಮತದಾರರ ಪಟ್ಟಿ, ಕರಡು ಪಟ್ಟಿ, 5 mla', '🔎 ವಿಜಯನಗರ Draft Roll ನೋಡಿ', '/karnataka-sir-voter-roll.html');
INSERT INTO ai_documents (id, title, content, url, category, source_type, source_url, keywords)
VALUES ('doc_sir_overview', 'Karnataka SIR Electoral Roll Complete Guide & Methodology', 'ಕರ್ನಾಟಕ ವಿಶೇಷ ಸಂಕ್ಷಿಪ್ತ ಪರಿಷ್ಕರಣೆ (SIR) ಪ್ರಕ್ರಿಯೆಯು ಭಾರತೀಯ ಚುನಾವಣಾ ಆಯೋಗದ (ECI) ಕಟ್ಟುನಿಟ್ಟಾದ ಮಾರ್ಗಸೂಚಿಗಳ ಅಡಿಯಲ್ಲಿ ನಡೆಯುತ್ತದೆ.
ರಾಜ್ಯದ 31 ಜಿಲ್ಲೆಗಳ 224 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳ ವ್ಯಾಪ್ತಿಯಲ್ಲಿರುವ ಸುಮಾರು 5.4 ಕೋಟಿ ಮತದಾರರ ಮಾಹಿತಿಯನ್ನು ನಿರಂತರವಾಗಿ ನವೀಕರಿಸಲಾಗುತ್ತದೆ.
ಕರಡು ಮತದಾರರ ಪಟ್ಟಿಯನ್ನು ತಾಲೂಕು ಕಚೇರಿಗಳು, ಮತಗಟ್ಟೆಗಳು ಹಾಗೂ ceokarnataka.kar.nic.in ಮತ್ತು karnata.in ಪೋರ್ಟಲ್‌ಗಳಲ್ಲಿ ಪ್ರಕಟಿಸಲಾಗುತ್ತದೆ.
ಪ್ರತಿ ಮತಗಟ್ಟೆಗೆ ಒಬ್ಬ ಬೂತ್ ಮಟ್ಟದ ಅಧಿಕಾರಿಯನ್ನು (BLO) ನೇಮಿಸಲಾಗಿದ್ದು, ಫಾರ್ಮ್ 6, 7, 8 ಅರ್ಜಿಗಳನ್ನು ಆನ್‌ಲೈನ್ ಮತ್ತು ಆಫ್‌ಲೈನ್‌ನಲ್ಲಿ ಸ್ವೀಕರಿಸಲಾಗುತ್ತದೆ.
ಮತದಾರರ ಸಹಾಯವಾಣಿ 1950 ಮೂಲಕ ಸಾರ್ವಜನಿಕರು ಯಾವುದೇ ದೂರುಗಳನ್ನು ದಾಖಲಿಸಬಹುದು.', '/karnataka-sir-voter-roll.html', 'SIR', 'official_eci', 'https://ceokarnataka.kar.nic.in', 'sir, electoral roll, draft roll, voter list, eci, blo, form 6, form 8');
INSERT INTO ai_documents (id, title, content, url, category, source_type, source_url, keywords)
VALUES ('doc_schemes_overview', 'Karnataka 5 Guarantee Welfare Schemes Master Guide', 'ಕರ್ನಾಟಕ ಸರ್ಕಾರದ 5 ಪ್ರಮುಖ ಗ್ಯಾರಂಟಿ ಯೋಜನೆಗಳ ನಿಯಮಾವಳಿ ಮತ್ತು ಅನುಷ್ಠಾನ:
1. ಗೃಹಲಕ್ಷ್ಮಿ: ಕುಟುಂಬದ ಯಜಮಾನಿ ಮಹಿಳೆಗೆ ಪ್ರತಿ ತಿಂಗಳು ₹2,000 ನೇರ ನಗದು ವರ್ಗಾವಣೆ (DBT). ತೆರಿಗೆ ಪಾವತಿದಾರರಲ್ಲದ ಕುಟುಂಬಗಳಿಗೆ ಸೌಲಭ್ಯ.
2. ಗೃಹಜ್ಯೋತಿ: ಗೃಹಬಳಕೆಯ ಪ್ರತಿ ಮನೆಗೆ ಮಾಸಿಕ 200 ಯೂನಿಟ್‌ವರೆಗೆ ಉಚಿತ ವಿದ್ಯುತ್. ವಾರ್ಷಿಕ ಸರಾಸರಿ ಬಳಕೆ + 10% ಹೆಚ್ಚುವರಿ ಯೂನಿಟ್ ಸೂತ್ರ.
3. ಶಕ್ತಿ ಯೋಜನೆ: ರಾಜ್ಯದ ನಾಲ್ಕೂ ಸಾರಿಗೆ ನಿಗಮಗಳ (KSRTC, BMTC, NWKRTC, KKRTC) ಸಾಮಾನ್ಯ ಮತ್ತು ಎಕ್ಸ್‌ಪ್ರೆಸ್ ಬಸ್‌ಗಳಲ್ಲಿ ಮಹಿಳೆಯರಿಗೆ ಸಂಪೂರ್ಣ ಉಚಿತ ಪ್ರಯಾಣ.
4. ಅನ್ನಭಾಗ್ಯ: BPL ಮತ್ತು ಅಂತ್ಯೋದಯ ಕಾರ್ಡ್‌ನ ಪ್ರತಿ ಸದಸ್ಯರಿಗೆ 10 ಕೆಜಿ ಆಹಾರ ಧಾನ್ಯ (5 ಕೆಜಿ ಅಕ್ಕಿ + 5 ಕೆಜಿಗೆ ತಲಾ ₹34 ರಂತೆ ₹170 DBT ನಗದು).
5. ಯುವನಿಧಿ: ಪದವೀಧರರಿಗೆ ₹3,000 ಮತ್ತು ಡಿಪ್ಲೋಮಾದಾರರಿಗೆ ₹1,500 ಮಾಸಿಕ ನಿರುದ್ಯೋಗ ಭತ್ಯೆ (ಗರಿಷ್ಠ 2 ವರ್ಷಗಳವರೆಗೆ).', '/guarantee-schemes.html', 'SCHEMES', 'official_gov', 'https://sevasindhugs.karnataka.gov.in', 'guarantee schemes, gruha lakshmi, gruha jyothi, shakti, anna bhagya, yuva nidhi');
INSERT INTO ai_documents (id, title, content, url, category, source_type, source_url, keywords)
VALUES ('doc_land_revenue_overview', 'Karnataka Digital Land Records & Property Registration Guide', 'ಕರ್ನಾಟಕ ಕಂದಾಯ ಇಲಾಖೆಯ ಡಿಜಿಟಲ್ ಪೋರ್ಟಲ್‌ಗಳು ಮತ್ತು ಸೇವೆಗಳು:
1. ಭೂಮಿ (Bhoomi): ಪಹಣಿ (RTC), ಮ್ಯುಟೇಶನ್ ರೆಜಿಸ್ಟರ್ (MR Extract), ಕಂದಾಯ ನಕ್ಷೆಗಳು ಮತ್ತು ಇ-ಕನ್ವರ್ಶನ್ ಸೇವೆಗಳು.
2. ಕಾವೇರಿ 2.0 (Kaveri 2.0): ಆನ್‌ಲೈನ್ ಆಸ್ತಿ ನೋಂದಣಿ, ಮುದ್ರಾಂಕ ಶುಲ್ಕ ಲೆಕ್ಕಾಚಾರ, ಅಪಾಯಿಂಟ್‌ಮೆಂಟ್ ಸ್ಲಾಟ್ ಬುಕಿಂಗ್ ಮತ್ತು ಆನ್‌ಲೈನ್ ಋಣಭಾರ ಪ್ರಮಾಣಪತ್ರ (EC).
3. ಮೋಜಿನಿ (Mojini): ಭೂ ಅಳತೆ, 11E ಸ್ಕೆಚ್, ತತ್ಕಾಲ್ ಪೋಡಿ ಮತ್ತು ಸರ್ವೆ ಅರ್ಜಿಗಳ ಲೈವ್ ಟ್ರ್ಯಾಕಿಂಗ್.
4. ದಿಶಾಂಕ್ (Dishank): ಜಿಪಿಎಸ್ ಆಧಾರಿತ ನೈಜ ಸರ್ವೆ ನಂಬರ್ ಮತ್ತು ಜಮೀನಿನ ಸ್ವರೂಪ ತಿಳಿಸುವ ಮೊಬೈಲ್ ಆ್ಯಪ್.', '/revenue-services.html', 'REVENUE', 'official_gov', 'https://bhoomi.karnataka.gov.in', 'bhoomi, kaveri 2.0, mojini, dishank, land records, rtc, mutation, ec');
INSERT INTO ai_documents (id, title, content, url, category, source_type, source_url, keywords)
VALUES ('doc_districts_overview', 'Karnataka 31 Districts Administrative & Assembly Matrix', 'ಕರ್ನಾಟಕ ರಾಜ್ಯವು 4 ಕಂದಾಯ ವಿಭಾಗಗಳು (ಬೆಂಗಳೂರು, ಮೈಸೂರು, ಬೆಳಗಾವಿ, ಕಲಬುರಗಿ) ಮತ್ತು 31 ಜಿಲ್ಲೆಗಳನ್ನು ಒಳಗೊಂಡಿದೆ.
ರಾಜ್ಯದಲ್ಲಿ ಒಟ್ಟು 224 ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರಗಳು ಹಾಗೂ 28 ಲೋಕಸಭಾ ಕ್ಷೇತ್ರಗಳಿವೆ.
ಪ್ರತಿ ಜಿಲ್ಲೆಯ ಆಡಳಿತವನ್ನು ಜಿಲ್ಲಾಧಿಕಾರಿ (DC), ಪೊಲೀಸ್ ವರಿಷ್ಠಾಧಿಕಾರಿ (SP) ಹಾಗೂ ಜಿಲ್ಲಾ ಪಂಚಾಯತ್ ಸಿಇಒ (CEO) ಮುನ್ನಡೆಸುತ್ತಾರೆ.
ತಾಲೂಕು ಮಟ್ಟದಲ್ಲಿ ತಹಶೀಲ್ದಾರರು ಕಂದಾಯ ಮತ್ತು ಮ್ಯಾಜಿಸ್ಟ್ರೇಟ್ ಕರ್ತವ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸುತ್ತಾರೆ.', '/districts.html', 'DISTRICTS', 'official_gov', 'https://karnataka.gov.in', '31 districts, dc, sp, tahsildar, taluk, mla, mp, karnataka, revenue divisions');