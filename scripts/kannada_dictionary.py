"""
Karnata — kannada_dictionary.py
Centralized Kannada Data Dictionary & Normalization Module
Contains authoritative mappings for Party Names, Election Terminology, Districts, and Constituencies.
"""

# ─── 1. ELECTION TERMINOLOGY DICTIONARY ───────────────────────
TERMINOLOGY = {
    "Assembly Constituency": "ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ",
    "Lok Sabha Constituency": "ಲೋಕಸಭಾ ಕ್ಷೇತ್ರ",
    "District": "ಜಿಲ್ಲೆ",
    "Current MLA": "ಪ್ರಸ್ತುತ ಶಾಸಕರು",
    "Previous MLA": "ಹಿಂದಿನ ಶಾಸಕರು",
    "Election Results": "ಚುನಾವಣಾ ಫಲಿತಾಂಶಗಳು",
    "Election History": "ಚುನಾವಣಾ ಇತಿಹಾಸ",
    "Winner": "ವಿಜೇತ ಅಭ್ಯರ್ಥಿ",
    "Runner-up": "ಸಮೀಪದ ಸ್ಪರ್ಧಿ",
    "Votes": "ಮತಗಳು",
    "Vote Share": "ಮತ ಹಂಚಿಕೆ",
    "Winning Margin": "ಗೆಲುವಿನ ಅಂತರ",
    "Turnout": "ಮತದಾನ ಪ್ರಮಾಣ",
    "Electors": "ಒಟ್ಟು ಮತದಾರರು",
    "General": "ಸಾಮಾನ್ಯ",
    "Reserved (SC)": "ಮೀಸಲು (ಎಸ್‌ಸಿ)",
    "Reserved (ST)": "ಮೀಸಲು (ಎಸ್‌ಟಿ)",
    "Candidate": "ಅಭ್ಯರ್ಥಿ",
    "Party": "ಪಕ್ಷ",
    "Year": "ವರ್ಷ",
    "Political Overview": "ಕ್ಷೇತ್ರದ ರಾಜಕೀಯ ಚಿತ್ರಣ",
    "Data Sources": "ಮಾಹಿತಿಯ ಮೂಲಗಳು",
    "Election Commission": "ಚುನಾವಣಾ ಆಯೋಗ",
    "Official Records": "ಸಂಬಂಧಿತ ಅಧಿಕೃತ ಮೂಲಗಳು",
    "Last Updated": "ನವೀಕರಿಸಿದ ದಿನಾಂಕ",
    "Special Report": "ವಿಶೇಷ ವರದಿ",
    "Constituency Info": "ಕ್ಷೇತ್ರ ಮಾಹಿತಿ"
}

# ─── 2. CENTRALIZED PARTY DICTIONARY ──────────────────────────
PARTY_DICT = {
    "BJP": {"en": "BJP", "kn": "ಬಿಜೆಪಿ", "full_kn": "ಭಾರತೀಯ ಜನತಾ ಪಕ್ಷ"},
    "INC": {"en": "INC", "kn": "ಕಾಂಗ್ರೆಸ್", "full_kn": "ಭಾರತೀಯ ರಾಷ್ಟ್ರೀಯ ಕಾಂಗ್ರೆಸ್"},
    "INC(I)": {"en": "INC(I)", "kn": "ಕಾಂಗ್ರೆಸ್ (ಐ)", "full_kn": "ಭಾರತೀಯ ರಾಷ್ಟ್ರೀಯ ಕಾಂಗ್ರೆಸ್ (ಇಂದಿರಾ)"},
    "JD(S)": {"en": "JD(S)", "kn": "ಜೆಡಿಎಸ್", "full_kn": "ಜನತಾ ದಳ (ಜಾತ್ಯತೀತ)"},
    "JDS": {"en": "JD(S)", "kn": "ಜೆಡಿಎಸ್", "full_kn": "ಜನತಾ ದಳ (ಜಾತ್ಯತೀತ)"},
    "JD": {"en": "JD", "kn": "ಜನತಾ ದಳ", "full_kn": "ಜನತಾ ದಳ"},
    "JNP": {"en": "JNP", "kn": "ಜನತಾ ಪಕ್ಷ", "full_kn": "ಜನತಾ ಪಕ್ಷ"},
    "IND": {"en": "Independent", "kn": "ಪಕ್ಷೇತರ", "full_kn": "ಪಕ್ಷೇತರ ಅಭ್ಯರ್ಥಿ"},
    "KRPP": {"en": "KRPP", "kn": "ಕೆಆರ್‌ಪಿಪಿ", "full_kn": "ಕಲ್ಯಾಣ ರಾಜ್ಯ ಪ್ರಗತಿ ಪಕ್ಷ"},
    "SKP": {"en": "SKP", "kn": "ಎಸ್‌.ಕೆ.ಪಿ", "full_kn": "ಸರ್ವೋದಯ ಕರ್ನಾಟಕ ಪಕ್ಷ"},
    "AAP": {"en": "AAP", "kn": "ಆಮ್ ಆದ್ಮಿ ಪಕ್ಷ", "full_kn": "ಆಮ್ ಆದ್ಮಿ ಪಕ್ಷ"},
    "BSP": {"en": "BSP", "kn": "ಬಹುಜನ ಸಮಾಜ ಪಕ್ಷ", "full_kn": "ಬಹುಜನ ಸಮಾಜ ಪಕ್ಷ"},
    "CPI": {"en": "CPI", "kn": "ಸಿಪಿಐ", "full_kn": "ಭಾರತೀಯ ಕಮ್ಯುನಿಸ್ಟ್ ಪಕ್ಷ"},
    "CPM": {"en": "CPM", "kn": "ಸಿಪಿಎಂ", "full_kn": "ಭಾರತೀಯ ಕಮ್ಯುನಿಸ್ಟ್ ಪಕ್ಷ (ಮಾರ್ಕ್ಸ್‌ವಾದಿ)"},
    "RPI": {"en": "RPI", "kn": "ಆರ್‌ಪಿಐ", "full_kn": "ರಿಪಬ್ಲಿಕನ್ ಪಾರ್ಟಿ ಆಫ್ ಇಂಡಿಯಾ"},
    "NCP": {"en": "NCP", "kn": "ಎನ್‌ಸಿಪಿ", "full_kn": "ರಾಷ್ಟ್ರವಾದಿ ಕಾಂಗ್ರೆಸ್ ಪಕ್ಷ"},
    "MUL": {"en": "IUML", "kn": "ಮುಸ್ಲಿಂ ಲೀಗ್", "full_kn": "ಇಂಡಿಯನ್ ಯೂನಿಯನ್ ಮುಸ್ಲಿಂ ಲೀಗ್"}
}

# ─── 3. DISTRICT NORMALIZATION DICTIONARY ─────────────────────
DISTRICT_DICT = {
    "bengaluru-urban": {"en": "Bengaluru Urban", "kn": "ಬೆಂಗಳೂರು ನಗರ"},
    "bengaluru-rural": {"en": "Bengaluru Rural", "kn": "ಬೆಂಗಳೂರು ಗ್ರಾಮಾಂತರ"},
    "ramanagara": {"en": "Ramanagara", "kn": "ರಾಮನಗರ"},
    "chikkaballapura": {"en": "Chikkaballapura", "kn": "ಚಿಕ್ಕಬಳ್ಳಾಪುರ"},
    "kolar": {"en": "Kolar", "kn": "ಕೋಲಾರ"},
    "tumakuru": {"en": "Tumakuru", "kn": "ತುಮಕೂರು"},
    "chitradurga": {"en": "Chitradurga", "kn": "ಚಿತ್ರದುರ್ಗ"},
    "davanagere": {"en": "Davanagere", "kn": "ದಾವಣಗೆರೆ"},
    "shivamogga": {"en": "Shivamogga", "kn": "ಶಿವಮೊಗ್ಗ"},
    "mysuru": {"en": "Mysuru", "kn": "ಮೈಸೂರು"},
    "mandya": {"en": "Mandya", "kn": "ಮಂಡ್ಯ"},
    "hassan": {"en": "Hassan", "kn": "ಹಾಸನ"},
    "kodagu": {"en": "Kodagu", "kn": "ಕೊಡಗು"},
    "chamarajanagara": {"en": "Chamarajanagara", "kn": "ಚಾಮರಾಜನಗರ"},
    "chikkamagaluru": {"en": "Chikkamagaluru", "kn": "ಚಿಕ್ಕಮಗಳೂರು"},
    "dakshina-kannada": {"en": "Dakshina Kannada", "kn": "ದಕ್ಷಿಣ ಕನ್ನಡ"},
    "udupi": {"en": "Udupi", "kn": "ಉಡುಪಿ"},
    "uttara-kannada": {"en": "Uttara Kannada", "kn": "ಉತ್ತರ ಕನ್ನಡ"},
    "belagavi": {"en": "Belagavi", "kn": "ಬೆಳಗಾವಿ"},
    "dharwad": {"en": "Dharwad", "kn": "ಧಾರವಾಡ"},
    "gadag": {"en": "Gadag", "kn": "ಗದಗ"},
    "haveri": {"en": "Haveri", "kn": "ಹಾವೇರಿ"},
    "bagalkote": {"en": "Bagalkote", "kn": "ಬಾಗಲಕೋಟೆ"},
    "vijayapura": {"en": "Vijayapura", "kn": "ವಿಜಯಪುರ"},
    "kalaburagi": {"en": "Kalaburagi", "kn": "ಕಲಬುರಗಿ"},
    "yadgir": {"en": "Yadgir", "kn": "ಯಾದಗಿರಿ"},
    "raichur": {"en": "Raichur", "kn": "ರಾಯಚೂರು"},
    "koppal": {"en": "Koppal", "kn": "ಕೊಪ್ಪಳ"},
    "ballari": {"en": "Ballari", "kn": "ಬಳ್ಳಾರಿ"},
    "vijayanagara": {"en": "Vijayanagara", "kn": "ವಿಜಯನಗರ"},
    "bidar": {"en": "Bidar", "kn": "ಬೀದರ್"}
}

def get_party_kn(party_code: str) -> str:
    """Returns official Kannada name for a party code."""
    if not party_code:
        return "ಪಕ್ಷೇತರ"
    code = str(party_code).strip().upper()
    info = PARTY_DICT.get(code)
    if info:
        return info["kn"]
    return str(party_code)

def get_term_kn(term: str) -> str:
    """Returns official Kannada terminology translation."""
    return TERMINOLOGY.get(term, term)

def get_district_kn(district_name: str) -> str:
    """Normalizes district name to official Kannada."""
    if not district_name:
        return "ಕರ್ನಾಟಕ"
    key = str(district_name).lower().replace(" ", "-").replace("_", "-")
    info = DISTRICT_DICT.get(key)
    if info:
        return info["kn"]
    for k, v in DISTRICT_DICT.items():
        if k in key or key in k:
            return v["kn"]
    return str(district_name)
