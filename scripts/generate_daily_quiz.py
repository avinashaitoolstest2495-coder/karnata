import sys
sys.stdout.reconfigure(encoding='utf-8')
import json, os, hashlib, random, urllib.request, urllib.error
from pathlib import Path
from datetime import datetime, timedelta

ROOT_DIR = Path(r"c:\Users\avina\Downloads\karnata-site-with-cms")
HISTORY_FILE = ROOT_DIR / "data" / "quiz_history.json"
BANK_FILE = ROOT_DIR / "data" / "karnataka_quiz_bank.json"

def get_gemini_api_key():
    key = os.getenv("GEMINI_API_KEY", "").strip()
    if key:
        return key
    
    env_file = ROOT_DIR / ".env"
    if env_file.exists():
        try:
            for line in env_file.read_text(encoding='utf-8', errors='ignore').splitlines():
                line = line.strip()
                if line.startswith("GEMINI_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('\"\'')
        except Exception:
            pass
    return ""

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

def generate_with_gemini_ai(api_key, today_str):
    print(f"  [GEMINI AI] Contacting Google Gemini AI to generate 20 fresh questions for {today_str}...")
    models = [
        "gemini-3.8-flash",
        "gemini-3.7-flash",
        "gemini-3.6-flash",
        "gemini-3.1-pro"
    ]
    
    prompt = f"""You are Karnataka's chief KPSC/KAS exam quizmaster. Generate today's ({today_str}) official set of exactly 20 high-quality, authentic Karnataka General Knowledge questions in pure Kannada.

Categories (4 questions each):
1. 'history' - ಇತಿಹಾಸ & ರಾಜವಂಶಗಳು (ಕದಂಬ, ಚಾಲುಕ್ಯ, ಹೊಯ್ಸಳ, ವಿಜಯನಗರ, ಒಡೆಯರ್, ಸ್ವಾತಂತ್ರ್ಯ ಹೋರಾಟ)
2. 'geography' - ಭೂಗೋಳ, ನದಿಗಳು, ಜಲಾಶಯಗಳು, ಪಶ್ಚಿಮ ಘಟ್ಟಗಳು & ಅರಣ್ಯ
3. 'literature' - ಸಾಹಿತ್ಯ, 8 ಜ್ಞಾನಪೀಠ ಪುರಸ್ಕೃತರು, ವಚನ ಸಾಹಿತ್ಯ, ದಾಸ ಸಾಹಿತ್ಯ, ಯಕ್ಷಗಾನ
4. 'polity' - ಆಡಳಿತ, ಸಂವಿಧಾನ, ವಿಧಾನಸೌಧ, ಪ್ರಸಿದ್ಧ ವ್ಯಕ್ತಿಗಳು (ಸರ್ ಎಂ.ವಿ., ಕುವೆಂಪು)
5. 'districts' - 31 ಜಿಲ್ಲೆಗಳ ಪರಂಪರೆ, ಜಿಐ ಟ್ಯಾಗ್, ಯುನೆಸ್ಕೋ ತಾಣಗಳು

Requirements:
- Each question must have 4 options.
- 'answer_index' is an integer (0, 1, 2, or 3).
- 'explanation' must be deeply detailed in Kannada with HTML formatting (<strong> and <br>). Explain clearly:
  • ಇದು ಏಕೆ ಸರಿ? (Why the correct answer is right)
  • ಇದು ಏಕೆ ತಪ್ಪು? (Why other notable options are wrong or their actual context)

Return ONLY a valid JSON array of 20 objects with structure:
[
  {{
    "id": "gemini_{today_str}_01",
    "category": "history",
    "question": "...",
    "options": ["...", "...", "...", "..."],
    "answer_index": 0,
    "explanation": "<strong>...</strong><br>• <strong>ಇದು ಏಕೆ ಸರಿ?</strong> ...<br>• <strong>ಇದು ಏಕೆ ತಪ್ಪು?</strong> ..."
  }},
  ...
]
"""
    for model in models:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
            payload = json.dumps({
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {
                    "temperature": 0.3,
                    "response_mime_type": "application/json"
                }
            }).encode('utf-8')

            req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                raw_text = data['candidates'][0]['content']['parts'][0]['text']
                questions = json.loads(raw_text)
                if isinstance(questions, list) and len(questions) >= 15:
                    print(f"  [GEMINI AI SUCCESS] Successfully generated {len(questions)} questions using {model}!")
                    return questions[:20]
        except urllib.error.HTTPError as e:
            err_body = e.read().decode('utf-8', errors='ignore')
            print(f"  [GEMINI AI NOTICE] {model} returned HTTP {e.code}: {err_body[:120]}")
            if "suspended" in err_body.lower() or "api_key_invalid" in err_body.lower():
                print("  ⚠️ [GEMINI KEY ISSUE] Your Gemini API Key in .env is suspended or invalid by Google Cloud.")
                print("  💡 Get a new free key at https://aistudio.google.com and set GEMINI_API_KEY in .env!")
                break
        except Exception as e:
            print(f"  [GEMINI AI NOTICE] {model} failed: {e}")
    
    return None

def generate_daily_quiz_file():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 🎯 Executing Daily Karnataka Quiz Generator...")
    now = datetime.now()
    today_str = now.strftime('%Y-%m-%d')
    day_of_year = now.timetuple().tm_yday

    selected = None
    gemini_key = get_gemini_api_key()

    if gemini_key:
        try:
            selected = generate_with_gemini_ai(gemini_key, today_str)
        except Exception as e:
            print(f"  [GEMINI FALLBACK] Error calling Gemini: {e}")

    # Fallback to zero-repetition 125-question bank if Gemini was not available or key was suspended
    if not selected:
        print("  [FALLBACK ENGINE] Selecting 20 unique questions from the verified 125-question bank with Zero Repetition...")
        all_questions = load_master_bank()
        history = load_history()
        used_by_date = history.get("used_by_date", {})

        recent_used = set()
        cutoff_date = (now - timedelta(days=5)).strftime('%Y-%m-%d')
        for d_str, q_ids in used_by_date.items():
            if d_str >= cutoff_date and d_str != today_str:
                recent_used.update(q_ids)

        categories = ["history", "geography", "literature", "polity", "districts"]
        available_by_cat = {c: [] for c in categories}
        for q in all_questions:
            if q["id"] not in recent_used:
                cat = q.get("category", "history")
                if cat in available_by_cat:
                    available_by_cat[cat].append(q)

        date_seed = int(hashlib.sha256(today_str.encode('utf-8')).hexdigest(), 16)
        rng = random.Random(date_seed)

        selected = []
        for cat in categories:
            pool = available_by_cat[cat]
            rng.shuffle(pool)
            if len(pool) >= 4:
                selected.extend(pool[:4])
            else:
                all_cat = [q for q in all_questions if q.get("category") == cat]
                rng.shuffle(all_cat)
                selected.extend(pool)
                for extra in all_cat:
                    if len(selected) % 4 != 0 and extra not in selected:
                        selected.append(extra)

        if len(selected) < 20:
            remaining = [q for q in all_questions if q not in selected]
            rng.shuffle(remaining)
            selected.extend(remaining[:20 - len(selected)])

        selected = selected[:20]
        rng.shuffle(selected)

        # Record in history
        history = load_history()
        history.setdefault("used_by_date", {})[today_str] = [q["id"] for q in selected]
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

    print(f"  ✅ Today's Quiz Generated for {today_str} (Edition #{day_of_year}) with {len(selected)} Questions!")
    print(f"  [Q1] {selected[0]['question']}")
    return daily_payload

if __name__ == "__main__":
    generate_daily_quiz_file()
