import json
import re
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

with open("data/myscheme_raw_harvest.json", "r", encoding="utf-8") as f:
    myscheme_list = json.load(f)

with open("data/government_schemes.json", "r", encoding="utf-8") as f:
    curated_db = json.load(f)

curated_schemes = curated_db.get("schemes", [])

print(f"myScheme count: {len(myscheme_list)} (State: {sum(1 for s in myscheme_list if s['level']=='State')}, Central: {sum(1 for s in myscheme_list if s['level']=='Central')})")
print(f"Curated count: {len(curated_schemes)}")

CATEGORY_MAP_KN = {
    "Agriculture,Rural & Environment": "ಕೃಷಿ, ಗ್ರಾಮೀಣ ಮತ್ತು ಪರಿಸರ",
    "Banking,Financial Services and Insurance": "ಬ್ಯಾಂಕಿಂಗ್, ಹಣಕಾಸು ಮತ್ತು ವಿಮೆ",
    "Business & Entrepreneurship": "ವ್ಯಾಪಾರ ಮತ್ತು ಉದ್ಯಮಶೀಲತೆ",
    "Education & Learning": "ಶಿಕ್ಷಣ ಮತ್ತು ಕಲಿಕೆ",
    "Health & Wellness": "ಆರೋಗ್ಯ ಮತ್ತು ಯೋಗಕ್ಷೇಮ",
    "Housing & Shelter": "ವಸತಿ ಮತ್ತು ಆಶ್ರಯ",
    "Public Safety,Law & Justice": "ಸಾರ್ವಜನಿಕ ಸುರಕ್ಷತೆ, ಕಾನೂನು ಮತ್ತು ನ್ಯಾಯ",
    "Science, IT & Communications": "ವಿಜ್ಞಾನ, ಐಟಿ ಮತ್ತು ಸಂವಹನ",
    "Skills & Employment": "ಕೌಶಲ್ಯ ಮತ್ತು ಉದ್ಯೋಗ",
    "Social welfare & Empowerment": "ಸಮಾಜ ಕಲ್ಯಾಣ ಮತ್ತು ಸಬಲೀಕರಣ",
    "Sports & Culture": "ಕ್ರೀಡೆ ಮತ್ತು ಸಂಸ್ಕೃತಿ",
    "Transport & Infrastructure": "ಸಾರಿಗೆ ಮತ್ತು ಮೂಲಸೌಕರ್ಯ",
    "Travel & Tourism": "ಪ್ರವಾಸ ಮತ್ತು ಪ್ರವಾಸೋದ್ಯಮ",
    "Utility & Sanitation": "ಉಪಯುಕ್ತತೆ ಮತ್ತು ನೈರ್ಮಲ್ಯ",
    "Women and Child": "ಮಹಿಳಾ ಮತ್ತು ಮಕ್ಕಳ ಕಲ್ಯಾಣ"
}

LEGACY_CAT_TO_MYSCHEME = {
    "agriculture": "Agriculture,Rural & Environment",
    "financial": "Banking,Financial Services and Insurance",
    "loan": "Business & Entrepreneurship",
    "education": "Education & Learning",
    "health": "Health & Wellness",
    "housing": "Housing & Shelter",
    "employment": "Skills & Employment",
    "sc_st_obc": "Social welfare & Empowerment",
    "pension": "Social welfare & Empowerment",
    "disability": "Social welfare & Empowerment",
    "guarantee": "Social welfare & Empowerment",
    "women": "Women and Child",
}

def norm(s):
    s = (s or "").lower()
    s = re.sub(r'\b(yojana|scheme|karnataka|chief minister|mukhyamantri|pradhan mantri|pm)\b', '', s)
    return re.sub(r'[^a-z0-9]', '', s)

ms_by_exact = {}
ms_by_norm = {}
for s in myscheme_list:
    exact_k = re.sub(r'[^a-z0-9]', '', (s["name_en"] or "").lower())
    if exact_k:
        ms_by_exact[exact_k] = s
    nk = norm(s["name_en"])
    if len(nk) >= 6:
        ms_by_norm[nk] = s

extra_curated = []
matched_count = 0

for cs in curated_schemes:
    title_en = cs.get("scheme_name_en") or cs.get("title_en") or cs.get("name_en") or ""
    title_kn = cs.get("scheme_name_kn") or cs.get("title_kn") or cs.get("name_kn") or ""
    desc_en = cs.get("description_en") or cs.get("summary_en") or ""
    desc_kn = cs.get("description_kn") or cs.get("summary_kn") or cs.get("short_description_kn") or ""
    min_en = cs.get("ministry_en") or cs.get("department_en") or "Government of Karnataka"
    min_kn = cs.get("ministry_kn") or cs.get("department_kn") or "ಕರ್ನಾಟಕ ಸರ್ಕಾರ"

    exact_k = re.sub(r'[^a-z0-9]', '', title_en.lower())
    nk = norm(title_en)
    matched = ms_by_exact.get(exact_k) or (ms_by_norm.get(nk) if len(nk) >= 8 else None)

    if matched:
        matched_count += 1
        matched["curated_id"] = cs.get("id")
        if title_kn and (not matched.get("name_kn") or matched["name_kn"] == matched["name_en"]):
            matched["name_kn"] = title_kn
        if desc_kn and (not matched.get("description_kn") or matched["description_kn"] == matched["description_en"]):
            matched["description_kn"] = desc_kn
        matched["benefits_kn"] = cs.get("benefits_kn")
        matched["benefits_en"] = cs.get("benefits_en")
        matched["documents_kn"] = cs.get("documents_kn")
        matched["documents_en"] = cs.get("documents_en")
        matched["how_to_apply_kn"] = cs.get("application_process_kn") or cs.get("how_to_apply_kn")
        matched["how_to_apply_en"] = cs.get("application_process_en")
        matched["apply_link"] = cs.get("application_url") or cs.get("apply_link")
        matched["helpline"] = cs.get("helpline")
        matched["annual_monetary_value"] = cs.get("annual_monetary_value", 0)
        matched["benefit_category"] = cs.get("benefit_category", "composite")
        matched["is_guarantee"] = (cs.get("category") == "guarantee" or "guarantee" in (cs.get("tags") or []))
    else:
        raw_lvl = (cs.get("level") or cs.get("scheme_type") or "state").lower()
        lvl = "State" if raw_lvl == "state" else "Central"
        cat_label = LEGACY_CAT_TO_MYSCHEME.get(cs.get("category"), "Social welfare & Empowerment")
        el = cs.get("eligibility", {})

        raw_genders = [g.lower() for g in (cs.get("gender") or el.get("gender") or ["all"])]
        genders = ["All"]
        if "female" in raw_genders and "male" not in raw_genders:
            genders = ["Female", "All"]
        elif "male" in raw_genders and "female" not in raw_genders:
            genders = ["Male", "All"]
        elif "transgender" in raw_genders:
            genders = ["Transgender", "All"]

        raw_castes = [c.lower() for c in (cs.get("categories") or el.get("caste") or ["all"])]
        castes = ["All"]
        if "all" not in raw_castes:
            castes = ["All"]
            if "sc" in raw_castes: castes.append("Scheduled Caste (SC)")
            if "st" in raw_castes: castes.append("Scheduled Tribe (ST)")
            if "obc" in raw_castes: castes.append("Other Backward Class (OBC)")
            if "general" in raw_castes: castes.append("General")

        raw_area = (cs.get("residence_type") or "any").lower()
        residences = ["Both"]
        if raw_area == "rural": residences = ["Rural", "Both"]
        elif raw_area == "urban": residences = ["Urban", "Both"]

        min_age = cs.get("min_age") if cs.get("min_age") is not None else el.get("min_age", 0)
        max_age = cs.get("max_age") if cs.get("max_age") is not None else el.get("max_age", 100)
        age_brackets = [a for a in range(0, 101, 10) if min_age <= a <= max_age or (a <= min_age <= a+10)]

        raw_occ = [o.lower() for o in (cs.get("occupations") or el.get("occupation") or ["all"])]
        occupations = ["All"]
        if "all" not in raw_occ:
            occ_map = {
                "farmer": "Farmer",
                "student": "Student",
                "artisan": "Artisans, Spinners & Weavers",
                "labor": "Construction Worker",
                "unorganised_worker": "Unorganized Worker",
                "worker": "Construction Worker",
                "entrepreneur": "Self-Employed/ Entrepreneur",
                "self_employed": "Self-Employed/ Entrepreneur",
                "fisherman": "Fishermen",
                "weaver": "Artisans, Spinners & Weavers"
            }
            occupations = list({occ_map[o] for o in raw_occ if o in occ_map}) + ["All"]

        emp_statuses = ["All"]
        if "unemployed" in raw_occ:
            emp_statuses = ["Unemployed", "All"]
        elif "entrepreneur" in raw_occ or "self_employed" in raw_occ:
            emp_statuses = ["Self-Employed/ Entrepreneur", "All"]

        b_cat = cs.get("benefit_category", "composite")
        b_type = "Cash" if b_cat in ["cash_dbt", "pension", "scholarship"] else ("In Kind" if b_cat in ["free_service", "insurance"] else "Composite")

        spec = [x.lower() for x in (cs.get("special_criteria") or el.get("special_conditions") or [])]
        is_guar = (cs.get("category") == "guarantee" or "guarantee" in (cs.get("tags") or []))

        extra_curated.append({
            "id": cs.get("id"),
            "slug": cs.get("id"),
            "myscheme_id": cs.get("id"),
            "curated_id": cs.get("id"),
            "name_en": title_en,
            "name_kn": title_kn,
            "short_title": "",
            "level": lvl,
            "beneficiaryState": ["Karnataka"] if lvl == "State" else ["All"],
            "ministry_en": min_en,
            "ministry_kn": min_kn,
            "department_en": min_en,
            "description_en": desc_en,
            "description_kn": desc_kn,
            "categories": [cat_label],
            "tags_en": cs.get("tags") or [],
            "tags_kn": cs.get("tags_kn") or cs.get("tags") or [],
            "schemeFor": "Individual",
            "priority": 0 if is_guar else 1,
            "genders": genders,
            "castes": castes,
            "residences": residences,
            "benefitTypes": [b_type],
            "maritalStatuses": ["Widowed", "All"] if "widow" in spec else ["All"],
            "employmentStatuses": emp_statuses,
            "occupations": occupations,
            "applicationModes": ["Online", "Offline"],
            "schemeTypes": ["State Sector Scheme" if lvl == "State" else "Central Sector Scheme"],
            "ageBrackets": age_brackets,
            "disabilityPercentages": [40, 50, 60, 70, 80, 90, 100] if ("disabled" in spec or cs.get("category") == "disability") else [],
            "minority": "minority" in raw_castes,
            "disability": ("disabled" in spec or cs.get("category") == "disability"),
            "dbtScheme": b_cat in ["cash_dbt", "pension", "scholarship"],
            "isBpl": (cs.get("income_max") or 999999) <= 200000,
            "isStudent": "student" in raw_occ or cs.get("category") == "education",
            "isGovEmployee": False,
            "isEconomicDistress": False,
            "benefits_kn": cs.get("benefits_kn"),
            "benefits_en": cs.get("benefits_en"),
            "eligibility_text_kn": cs.get("eligibility_text_kn"),
            "documents_kn": cs.get("documents_kn"),
            "documents_en": cs.get("documents_en"),
            "how_to_apply_kn": cs.get("application_process_kn") or cs.get("how_to_apply_kn"),
            "how_to_apply_en": cs.get("application_process_en"),
            "apply_link": cs.get("application_url") or cs.get("apply_link"),
            "helpline": cs.get("helpline"),
            "annual_monetary_value": cs.get("annual_monetary_value", 0),
            "benefit_category": b_cat,
            "is_guarantee": is_guar
        })

print(f"Matched {matched_count} schemes; adding {len(extra_curated)} extra curated Karnataka/Union schemes.")

combined = extra_curated + myscheme_list
combined.sort(key=lambda x: (0 if x.get("is_guarantee") else 1, 0 if x["level"] == "State" else 1, x.get("priority") if x.get("priority") is not None else 4))

state_count = sum(1 for x in combined if x["level"] == "State")
central_count = sum(1 for x in combined if x["level"] == "Central")
print(f"FINAL COMBINED TOTAL: {len(combined)} schemes (State: {state_count}, Central: {central_count})")

out_payload = {
    "last_updated": "2026-10-29",
    "source": "myScheme.gov.in + Seva Sindhu Karnataka",
    "total_schemes": len(combined),
    "state_schemes_count": state_count,
    "central_schemes_count": central_count,
    "category_map_kn": CATEGORY_MAP_KN,
    "schemes": combined
}

with open("data/myscheme_karnataka_all.json", "w", encoding="utf-8") as f:
    json.dump(out_payload, f, ensure_ascii=False, separators=(",", ":"))

print("Saved data/myscheme_karnataka_all.json, size:", round(os.path.getsize("data/myscheme_karnataka_all.json") / 1024, 1), "KB")
