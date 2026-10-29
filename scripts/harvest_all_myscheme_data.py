import urllib.request
import urllib.parse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.stdout.reconfigure(encoding="utf-8")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "x-api-key": "tYTy5eEhlu9rFjyxuCr7ra7ACp4dv1RH8gWuHTDc",
    "Origin": "https://www.myscheme.gov.in",
    "Referer": "https://www.myscheme.gov.in/"
}

BASE_FILTERS = [
    {"identifier": "beneficiaryState", "value": "All"},
    {"identifier": "beneficiaryState", "value": "Karnataka"}
]

def fetch_search_page(lang, filters, from_offset=0, size=100):
    q = urllib.parse.quote(json.dumps(filters))
    url = f"https://www.myscheme.gov.in/api/apisetu/search/schemes?lang={lang}&q={q}&keyword=&sort=&from={from_offset}&size={size}"
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            resp = urllib.request.urlopen(req, timeout=25).read().decode("utf-8", "ignore")
            data = json.loads(resp).get("data", {})
            return data
        except Exception as e:
            if attempt == 2:
                print(f"Error fetching {lang} offset={from_offset} filters={filters}: {e}")
                return {}
            time.sleep(0.5)

def fetch_all_for_filter(lang, extra_filters):
    filters = BASE_FILTERS + extra_filters
    first = fetch_search_page(lang, filters, 0, 100)
    hits = first.get("hits", {})
    total = hits.get("page", {}).get("total", 0)
    items = list(hits.get("items", []))
    if total > 100:
        for offset in range(100, total, 100):
            more = fetch_search_page(lang, filters, offset, 100)
            items.extend(more.get("hits", {}).get("items", []))
    return items, first.get("facets", [])

def main():
    print("1. Fetching all English schemes (base Karnataka + All India)...")
    en_items, en_facets = fetch_all_for_filter("en", [])
    print(f"   Fetched {len(en_items)} English schemes.")

    print("2. Fetching all Kannada schemes (lang=kn)...")
    kn_items, kn_facets = fetch_all_for_filter("kn", [])
    print(f"   Fetched {len(kn_items)} Kannada schemes.")

    schemes_by_slug = {}
    for item in en_items:
        f = item.get("fields", {})
        slug = f.get("slug") or item.get("id")
        if not slug:
            continue
        schemes_by_slug[slug] = {
            "id": slug,
            "slug": slug,
            "myscheme_id": item.get("id"),
            "name_en": (f.get("schemeName") or "").strip(),
            "name_kn": (f.get("schemeName") or "").strip(),
            "short_title": f.get("schemeShortTitle") or "",
            "level": f.get("level") or "Central",
            "beneficiaryState": f.get("beneficiaryState") or ["All"],
            "ministry_en": f.get("nodalMinistryName") or f.get("nodalDepartmentName") or "Government of India",
            "ministry_kn": f.get("nodalMinistryName") or f.get("nodalDepartmentName") or "ಭಾರತ ಸರ್ಕಾರ",
            "department_en": f.get("nodalDepartmentName") or "",
            "description_en": (f.get("briefDescription") or "").strip(),
            "description_kn": (f.get("briefDescription") or "").strip(),
            "categories": f.get("schemeCategory") or [],
            "tags_en": f.get("tags") or [],
            "tags_kn": f.get("tags") or [],
            "schemeFor": f.get("schemeFor") or "Individual",
            "priority": f.get("priority", 4),
            # Facet attributes to be populated
            "genders": set(),
            "castes": set(),
            "residences": set(),
            "benefitTypes": set(),
            "maritalStatuses": set(),
            "employmentStatuses": set(),
            "occupations": set(),
            "applicationModes": set(),
            "schemeTypes": set(),
            "ageBrackets": set(),
            "disabilityPercentages": set(),
            "minority": False,
            "disability": False,
            "dbtScheme": False,
            "isBpl": False,
            "isStudent": False,
            "isGovEmployee": False,
            "isEconomicDistress": False,
        }

    for item in kn_items:
        f = item.get("fields", {})
        slug = f.get("slug") or item.get("id")
        if not slug:
            continue
        if slug in schemes_by_slug:
            s = schemes_by_slug[slug]
            if f.get("schemeName"):
                s["name_kn"] = f.get("schemeName").strip()
            if f.get("briefDescription"):
                s["description_kn"] = f.get("briefDescription").strip()
            if f.get("tags"):
                s["tags_kn"] = f.get("tags")
            if f.get("nodalMinistryName"):
                s["ministry_kn"] = f.get("nodalMinistryName")
        else:
            schemes_by_slug[slug] = {
                "id": slug,
                "slug": slug,
                "myscheme_id": item.get("id"),
                "name_en": (f.get("schemeNameEng") or f.get("schemeName") or "").strip(),
                "name_kn": (f.get("schemeName") or "").strip(),
                "short_title": f.get("schemeShortTitle") or "",
                "level": f.get("level") or "Central",
                "beneficiaryState": f.get("beneficiaryState") or ["All"],
                "ministry_en": f.get("nodalMinistryName") or "Government of India",
                "ministry_kn": f.get("nodalMinistryName") or "ಭಾರತ ಸರ್ಕಾರ",
                "department_en": f.get("nodalDepartmentName") or "",
                "description_en": (f.get("briefDescriptionEng") or f.get("briefDescription") or "").strip(),
                "description_kn": (f.get("briefDescription") or "").strip(),
                "categories": f.get("schemeCategory") or [],
                "tags_en": f.get("tagsEng") or f.get("tags") or [],
                "tags_kn": f.get("tags") or [],
                "schemeFor": f.get("schemeFor") or "Individual",
                "priority": f.get("priority", 4),
                "genders": set(),
                "castes": set(),
                "residences": set(),
                "benefitTypes": set(),
                "maritalStatuses": set(),
                "employmentStatuses": set(),
                "occupations": set(),
                "applicationModes": set(),
                "schemeTypes": set(),
                "ageBrackets": set(),
                "disabilityPercentages": set(),
                "minority": False,
                "disability": False,
                "dbtScheme": False,
                "isBpl": False,
                "isStudent": False,
                "isGovEmployee": False,
                "isEconomicDistress": False,
            }

    print(f"Total unique slugs from myScheme: {len(schemes_by_slug)}")

    # Build facet query tasks from en_facets
    tasks = []
    target_facets = {
        "gender": "genders",
        "caste": "castes",
        "residence": "residences",
        "benefitTypes": "benefitTypes",
        "maritalStatus": "maritalStatuses",
        "employmentStatus": "employmentStatuses",
        "occupation": "occupations",
        "applicationMode": "applicationModes",
        "schemeType": "schemeTypes",
        "age-general": "ageBrackets",
        "disabilityPercentage": "disabilityPercentages",
        "minority": "minority",
        "disability": "disability",
        "dbtScheme": "dbtScheme",
        "isBpl": "isBpl",
        "isStudent": "isStudent",
        "isGovEmployee": "isGovEmployee",
        "isEconomicDistress": "isEconomicDistress",
    }

    for facet in en_facets:
        ident = facet.get("identifier")
        if ident not in target_facets:
            continue
        for entry in facet.get("entries", []):
            label = entry.get("label")
            count = entry.get("count", 0)
            if count == 0:
                continue
            # For boolean facets, only query "Yes"
            if ident in ["minority", "disability", "dbtScheme", "isBpl", "isStudent", "isGovEmployee", "isEconomicDistress"]:
                if label != "Yes":
                    continue
                tasks.append((ident, label, [{"identifier": ident, "value": "Yes"}]))
            elif ident in ["age-general", "disabilityPercentage"]:
                tasks.append((ident, label, [{"identifier": ident, "min": label, "max": label}]))
            else:
                # Skip "All" or "Both" if we want specific tags, OR query them too so we know exact membership
                tasks.append((ident, label, [{"identifier": ident, "value": label}]))

    print(f"3. Running {len(tasks)} facet membership queries in parallel...")
    with ThreadPoolExecutor(max_workers=20) as ex:
        future_map = {
            ex.submit(fetch_all_for_filter, "en", f_list): (ident, label)
            for (ident, label, f_list) in tasks
        }
        done_count = 0
        for fut in as_completed(future_map):
            ident, label = future_map[fut]
            done_count += 1
            try:
                items, _ = fut.result()
                field_key = target_facets[ident]
                for it in items:
                    slug = it.get("fields", {}).get("slug") or it.get("id")
                    if slug in schemes_by_slug:
                        if isinstance(schemes_by_slug[slug][field_key], set):
                            schemes_by_slug[slug][field_key].add(label)
                        else:
                            schemes_by_slug[slug][field_key] = True
                if done_count % 10 == 0 or done_count == len(tasks):
                    print(f"   [{done_count}/{len(tasks)}] Completed {ident}={label} ({len(items)} hits)")
            except Exception as e:
                print(f"   Failed {ident}={label}: {e}")

    # Convert sets to sorted lists
    output_list = []
    for slug, s in schemes_by_slug.items():
        for k, v in list(s.items()):
            if isinstance(v, set):
                s[k] = sorted(list(v), key=lambda x: str(x))
        output_list.append(s)

    # Sort State schemes first, then by priority and name
    output_list.sort(key=lambda x: (0 if x["level"] == "State" else 1, x.get("priority") if x.get("priority") is not None else 4, x["name_en"] or ""))

    with open("data/myscheme_raw_harvest.json", "w", encoding="utf-8") as f:
        json.dump(output_list, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(output_list)} schemes to data/myscheme_raw_harvest.json")

if __name__ == "__main__":
    main()
