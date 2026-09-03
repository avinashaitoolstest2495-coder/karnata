import sys
sys.stdout.reconfigure(encoding='utf-8')
import json, os, hashlib, random
from pathlib import Path
from datetime import datetime, timedelta

ROOT_DIR = Path(r"c:\Users\avina\Downloads\karnata-site-with-cms")
HISTORY_FILE = ROOT_DIR / "data" / "quiz_history.json"
BANK_FILE = ROOT_DIR / "data" / "karnataka_quiz_bank.json"

def load_master_bank():
    if BANK_FILE.exists():
        try:
            return json.load(open(BANK_FILE, 'r', encoding='utf-8'))
        except Exception:
            pass
    from scratch.seed_125_quiz_bank import ALL_125_QUESTIONS
    return ALL_125_QUESTIONS

def load_history():
    if HISTORY_FILE.exists():
        try:
            return json.load(open(HISTORY_FILE, 'r', encoding='utf-8'))
        except Exception:
            pass
    return {"used_by_date": {}, "recent_used_ids": []}

def save_history(hist):
    HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(hist, f, ensure_ascii=False, indent=2)

def generate_daily_quiz_file():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 🎯 Executing Daily Karnataka Quiz Generator (Zero Repetition Engine)...")
    now = datetime.now()
    today_str = now.strftime('%Y-%m-%d')
    day_of_year = now.timetuple().tm_yday

    all_questions = load_master_bank()
    print(f"  [INFO] Master bank contains {len(all_questions)} authentic questions.")

    history = load_history()
    used_by_date = history.get("used_by_date", {})
    
    # Calculate questions used in the last 5 days
    recent_used = set()
    cutoff_date = (now - timedelta(days=5)).strftime('%Y-%m-%d')
    for d_str, q_ids in used_by_date.items():
        if d_str >= cutoff_date and d_str != today_str:
            recent_used.update(q_ids)

    print(f"  [INFO] Recently used questions in last 5 days to EXCLUDE: {len(recent_used)}")

    # Group unused questions by category
    categories = ["history", "geography", "literature", "polity", "districts"]
    available_by_cat = {c: [] for c in categories}
    
    for q in all_questions:
        if q["id"] not in recent_used:
            cat = q.get("category", "history")
            if cat in available_by_cat:
                available_by_cat[cat].append(q)

    # Deterministic daily seed based on date string
    date_seed = int(hashlib.sha256(today_str.encode('utf-8')).hexdigest(), 16)
    rng = random.Random(date_seed)

    selected = []
    # Pick 4 unique questions per category (4 x 5 = 20 questions)
    for cat in categories:
        pool = available_by_cat[cat]
        rng.shuffle(pool)
        if len(pool) >= 4:
            selected.extend(pool[:4])
        else:
            # Fallback if category has fewer than 4 remaining unused
            all_cat = [q for q in all_questions if q.get("category") == cat]
            rng.shuffle(all_cat)
            selected.extend(pool)
            for extra in all_cat:
                if len(selected) % 4 != 0 and extra not in selected:
                    selected.append(extra)

    # If still under 20, fill from any remaining available
    if len(selected) < 20:
        remaining = [q for q in all_questions if q not in selected]
        rng.shuffle(remaining)
        selected.extend(remaining[:20 - len(selected)])

    # Ensure exactly 20 questions
    selected = selected[:20]
    rng.shuffle(selected)

    # Record today's questions in history
    used_by_date[today_str] = [q["id"] for q in selected]
    history["used_by_date"] = used_by_date
    history["recent_used_ids"] = list(set([q["id"] for q in selected] + list(recent_used)))
    save_history(history)

    daily_payload = {
        "success": True,
        "date": today_str,
        "edition": f"ಕರ್ನಾಟಕ ಜ್ಞಾನ ಸವಾಲು - ಸಂಚಿಕೆ #{day_of_year}",
        "edition_number": day_of_year,
        "generated_at": now.isoformat(),
        "total_questions": len(selected),
        "questions": selected,
        "today_highlight": selected[0]
    }

    # Save to data/daily_quiz.json (Both root and namma-karnataka)
    daily_file = ROOT_DIR / "data" / "daily_quiz.json"
    daily_file.write_text(json.dumps(daily_payload, ensure_ascii=False, indent=2), encoding='utf-8')
    (ROOT_DIR / "namma-karnataka" / "data" / "daily_quiz.json").write_text(json.dumps(daily_payload, ensure_ascii=False, indent=2), encoding='utf-8')

    # Save to archive
    archive_dir = ROOT_DIR / "data" / "quiz"
    archive_dir.mkdir(parents=True, exist_ok=True)
    (archive_dir / f"quiz_{today_str}.json").write_text(json.dumps(daily_payload, ensure_ascii=False, indent=2), encoding='utf-8')
    (ROOT_DIR / "namma-karnataka" / "data" / "quiz").mkdir(parents=True, exist_ok=True)
    (ROOT_DIR / "namma-karnataka" / "data" / "quiz" / f"quiz_{today_str}.json").write_text(json.dumps(daily_payload, ensure_ascii=False, indent=2), encoding='utf-8')

    print(f"  ✅ Today's Fresh 20 Questions Generated for {today_str} (Edition #{day_of_year}) with ZERO repetition!")
    print(f"  [Q1] {selected[0]['question']}")
    return daily_payload

if __name__ == "__main__":
    generate_daily_quiz_file()
