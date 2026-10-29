import sys

sys.stdout.reconfigure(encoding="utf-8")

HTML_CONTENT = r'''<!DOCTYPE html>
<html lang="kn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="index, follow">
    <title>ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು ಮತ್ತು ಅರ್ಹತಾ ಪರೀಕ್ಷಕ | Karnataka & Central Schemes (885+)</title>
    <meta name="description" content="ಕರ್ನಾಟಕ ರಾಜ್ಯ ಮತ್ತು ಕೇಂದ್ರ ಸರ್ಕಾರದ 885+ ಯೋಜನೆಗಳ ಸಂಪೂರ್ಣ ಮಾಹಿತಿ, ಅರ್ಹತಾ ಪ್ರಶ್ನಾವಳಿ (Check Eligibility in Kannada), ಬೇಕಾಗುವ ದಾಖಲೆಗಳು ಮತ್ತು ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್ ಲಿಂಕ್‌ಗಳು.">
    <link rel="canonical" href="https://karnata.in/scheme-checker.html">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Anek+Kannada:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/styles.css">
    <script src="/nav-component.js" defer></script>

    <style>
        :root {
            --bg-app: #f3f6fa;
            --bg-surface: #ffffff;
            --bg-subtle: #f8fafc;
            --text-main: #0f172a;
            --text-secondary: #334155;
            --text-muted: #64748b;
            --border-light: #e2e8f0;
            --border-hover: #cbd5e1;
            --primary: #16a34a;
            --primary-dark: #15803d;
            --primary-soft: #dcfce7;
            --state-accent: #059669;
            --state-soft: #ecfdf5;
            --central-accent: #2563eb;
            --central-soft: #eff6ff;
            --gold-accent: #d97706;
            --gold-soft: #fef3c7;
            --radius-xl: 18px;
            --radius-lg: 14px;
            --radius-md: 10px;
            --shadow-xs: 0 1px 3px rgba(15, 23, 42, 0.04);
            --shadow-sm: 0 4px 14px rgba(15, 23, 42, 0.06);
            --shadow-md: 0 12px 28px -6px rgba(15, 23, 42, 0.1);
        }

        *, *::before, *::after {
            box-sizing: border-box;
            font-family: 'Anek Kannada', system-ui, -apple-system, sans-serif;
        }

        body {
            margin: 0;
            padding: 0;
            background: var(--bg-app);
            color: var(--text-main);
            font-family: 'Anek Kannada', system-ui, -apple-system, sans-serif;
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
        }

        /* 1. COMPACT COMMAND BAR (ZERO FLUFF) */
        .command-header {
            background: var(--bg-surface);
            border-bottom: 1px solid var(--border-light);
            position: sticky;
            top: 0;
            z-index: 90;
            box-shadow: var(--shadow-xs);
        }

        .command-inner {
            max-width: 1460px;
            margin: 0 auto;
            padding: 11px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            flex-wrap: wrap;
        }

        .level-seg {
            display: inline-flex;
            background: #f1f5f9;
            padding: 4px;
            border-radius: 12px;
            border: 1px solid var(--border-light);
            gap: 4px;
        }

        .level-btn {
            border: none;
            background: transparent;
            color: var(--text-secondary);
            padding: 7px 14px;
            border-radius: 9px;
            font-size: 0.9rem;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 7px;
            transition: all 0.16s ease;
            white-space: nowrap;
        }

        .level-btn:hover {
            color: var(--text-main);
        }

        .level-btn.active {
            background: var(--bg-surface);
            color: var(--primary-dark);
            box-shadow: 0 2px 6px rgba(15, 23, 42, 0.08);
        }

        .level-count {
            background: #e2e8f0;
            color: #334155;
            padding: 1px 8px;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 800;
        }

        .level-btn.active .level-count {
            background: var(--primary-soft);
            color: var(--primary-dark);
        }

        .search-wrap {
            flex: 1;
            min-width: 250px;
            max-width: 520px;
            position: relative;
            display: flex;
            align-items: center;
        }

        .search-icon {
            position: absolute;
            left: 14px;
            color: var(--text-muted);
            font-size: 0.98rem;
            pointer-events: none;
        }

        .search-input {
            width: 100%;
            padding: 9px 38px 9px 40px;
            border-radius: 12px;
            border: 1.5px solid var(--border-light);
            background: var(--bg-subtle);
            font-size: 0.95rem;
            font-weight: 600;
            color: var(--text-main);
            transition: all 0.18s ease;
        }

        .search-input:focus {
            outline: none;
            background: var(--bg-surface);
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(22, 163, 74, 0.14);
        }

        .search-clear {
            position: absolute;
            right: 10px;
            border: none;
            background: #e2e8f0;
            color: #475569;
            width: 22px;
            height: 22px;
            border-radius: 50%;
            font-size: 0.75rem;
            cursor: pointer;
            display: none;
            align-items: center;
            justify-content: center;
        }

        .header-controls {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .lang-switch {
            display: inline-flex;
            background: #f1f5f9;
            border: 1px solid var(--border-light);
            border-radius: 10px;
            padding: 3px;
        }

        .lang-btn {
            border: none;
            background: transparent;
            padding: 5px 11px;
            border-radius: 7px;
            font-size: 0.82rem;
            font-weight: 800;
            color: var(--text-secondary);
            cursor: pointer;
        }

        .lang-btn.active {
            background: #0f172a;
            color: #ffffff;
        }

        .sort-select {
            padding: 7px 12px;
            border-radius: 10px;
            border: 1px solid var(--border-light);
            background: var(--bg-surface);
            font-size: 0.86rem;
            font-weight: 700;
            color: var(--text-main);
            cursor: pointer;
        }

        .mobile-filter-trigger {
            display: none;
            padding: 8px 12px;
            border-radius: 10px;
            border: 1px solid var(--primary);
            background: var(--primary-soft);
            color: var(--primary-dark);
            font-size: 0.86rem;
            font-weight: 800;
            cursor: pointer;
            align-items: center;
            gap: 6px;
        }

        /* 2. VISUAL CATEGORY RIBBON */
        .category-ribbon-wrap {
            background: var(--bg-surface);
            border-bottom: 1px solid var(--border-light);
        }

        .category-ribbon {
            max-width: 1460px;
            margin: 0 auto;
            padding: 10px 20px;
            display: flex;
            align-items: center;
            gap: 8px;
            overflow-x: auto;
            scrollbar-width: thin;
        }

        .category-ribbon::-webkit-scrollbar {
            height: 4px;
        }

        .category-ribbon::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 999px;
        }

        .cat-chip {
            border: 1px solid var(--border-light);
            background: var(--bg-subtle);
            color: var(--text-secondary);
            padding: 6px 13px;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            white-space: nowrap;
            transition: all 0.15s ease;
            flex-shrink: 0;
        }

        .cat-chip:hover {
            border-color: var(--primary);
            color: var(--text-main);
            background: #f0fdf4;
        }

        .cat-chip.active {
            background: var(--primary);
            border-color: var(--primary);
            color: #ffffff;
            box-shadow: 0 3px 10px rgba(22, 163, 74, 0.22);
        }

        .cat-chip-count {
            font-size: 0.74rem;
            padding: 1px 7px;
            border-radius: 999px;
            background: rgba(15, 23, 42, 0.08);
            font-weight: 800;
        }

        .cat-chip.active .cat-chip-count {
            background: rgba(255, 255, 255, 0.24);
            color: #ffffff;
        }

        /* 3. MAIN WORKSPACE */
        .workspace {
            max-width: 1460px;
            margin: 0 auto;
            padding: 18px 20px 60px;
            display: grid;
            grid-template-columns: 325px 1fr;
            gap: 22px;
            align-items: start;
        }

        /* LEFT DYNAMIC FILTER DOCK */
        .filter-dock {
            background: var(--bg-surface);
            border: 1px solid var(--border-light);
            border-radius: var(--radius-xl);
            padding: 16px;
            position: sticky;
            top: 70px;
            max-height: calc(100vh - 86px);
            overflow-y: auto;
            box-shadow: var(--shadow-xs);
        }

        .filter-dock::-webkit-scrollbar {
            width: 5px;
        }

        .filter-dock::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 999px;
        }

        .dock-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-bottom: 10px;
            margin-bottom: 12px;
            border-bottom: 1px solid var(--border-light);
        }

        .dock-title {
            font-size: 0.98rem;
            font-weight: 800;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .reset-btn {
            border: none;
            background: #f0fdf4;
            color: var(--primary-dark);
            font-size: 0.8rem;
            font-weight: 800;
            cursor: pointer;
            padding: 4px 10px;
            border-radius: 7px;
            border: 1px solid #bbf7d0;
        }

        .reset-btn:hover {
            background: var(--primary-soft);
        }

        .quick-toggles {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 7px;
            margin-bottom: 14px;
        }

        .q-toggle {
            border: 1px solid var(--border-light);
            background: var(--bg-subtle);
            border-radius: 10px;
            padding: 7px 9px;
            font-size: 0.8rem;
            font-weight: 700;
            color: var(--text-secondary);
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 4px;
            text-align: left;
            transition: all 0.15s ease;
        }

        .q-toggle:hover {
            border-color: var(--border-hover);
            color: var(--text-main);
        }

        .q-toggle.active {
            background: var(--primary-soft);
            border-color: var(--primary);
            color: var(--primary-dark);
        }

        .q-badge {
            font-size: 0.72rem;
            font-weight: 800;
            background: rgba(15, 23, 42, 0.08);
            padding: 1px 6px;
            border-radius: 6px;
        }

        .q-toggle.active .q-badge {
            background: var(--primary);
            color: #ffffff;
        }

        .f-group {
            margin-bottom: 13px;
            padding-bottom: 13px;
            border-bottom: 1px solid #f1f5f9;
        }

        .f-group:last-child {
            margin-bottom: 0;
            padding-bottom: 0;
            border-bottom: none;
        }

        .f-label {
            display: flex;
            align-items: center;
            justify-content: space-between;
            font-size: 0.85rem;
            font-weight: 800;
            color: var(--text-main);
            margin-bottom: 7px;
        }

        .f-pills {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }

        .f-pill {
            border: 1px solid var(--border-light);
            background: #ffffff;
            color: var(--text-secondary);
            padding: 5px 10px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            transition: all 0.14s ease;
        }

        .f-pill:hover {
            border-color: var(--border-hover);
            color: var(--text-main);
        }

        .f-pill.active {
            background: #0f172a;
            border-color: #0f172a;
            color: #ffffff;
        }

        .f-pill-cnt {
            font-size: 0.7rem;
            opacity: 0.75;
            font-weight: 800;
        }

        .f-select {
            width: 100%;
            padding: 8px 10px;
            border-radius: 9px;
            border: 1px solid var(--border-light);
            background: var(--bg-subtle);
            font-size: 0.84rem;
            font-weight: 600;
            color: var(--text-main);
            cursor: pointer;
        }

        .f-select:focus {
            outline: none;
            border-color: var(--primary);
            background: #ffffff;
        }

        /* RIGHT MAIN AREA */
        .feed-area {
            min-width: 0;
        }

        /* Interactive Citizen Profile Quick-Matcher Bar */
        .profile-matcher-bar {
            background: linear-gradient(135deg, #ffffff 0%, #f0fdf4 100%);
            border: 1px solid #bbf7d0;
            border-radius: var(--radius-xl);
            padding: 14px 18px;
            margin-bottom: 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            flex-wrap: wrap;
            box-shadow: var(--shadow-xs);
        }

        .pm-left {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        .pm-badge {
            background: var(--primary);
            color: #fff;
            font-size: 0.8rem;
            font-weight: 800;
            padding: 4px 10px;
            border-radius: 8px;
            white-space: nowrap;
        }

        .pm-personas {
            display: flex;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
        }

        .pm-chip {
            border: 1px solid #cbd5e1;
            background: #ffffff;
            color: var(--text-main);
            padding: 5px 11px;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.15s ease;
        }

        .pm-chip:hover, .pm-chip.active {
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
        }

        .feed-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            margin-bottom: 14px;
            flex-wrap: wrap;
        }

        .results-summary {
            font-size: 0.96rem;
            font-weight: 700;
            color: var(--text-secondary);
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
        }

        .results-summary strong {
            color: var(--primary-dark);
            font-size: 1.15rem;
            font-weight: 800;
        }

        .active-chips {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            align-items: center;
        }

        .active-chip {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            background: #dcfce7;
            color: #166534;
            border: 1px solid #86efac;
            padding: 3px 10px;
            border-radius: 999px;
            font-size: 0.78rem;
            font-weight: 700;
            cursor: pointer;
        }

        .active-chip:hover {
            background: #bbf7d0;
        }

        .view-toggle {
            display: inline-flex;
            background: var(--bg-surface);
            border: 1px solid var(--border-light);
            border-radius: 9px;
            padding: 2px;
        }

        .v-btn {
            border: none;
            background: transparent;
            padding: 5px 10px;
            border-radius: 7px;
            cursor: pointer;
            font-size: 0.85rem;
            color: var(--text-muted);
        }

        .v-btn.active {
            background: #f1f5f9;
            color: var(--text-main);
            font-weight: 800;
        }

        /* POINTS-TYPE SCHEME CARDS */
        .schemes-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(355px, 1fr));
            gap: 16px;
        }

        .schemes-grid.list-view {
            grid-template-columns: 1fr;
            gap: 12px;
        }

        .scheme-card {
            background: var(--bg-surface);
            border: 1px solid var(--border-light);
            border-radius: var(--radius-xl);
            padding: 18px 20px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 12px;
            transition: transform 0.16s ease, box-shadow 0.16s ease, border-color 0.16s ease;
            position: relative;
            overflow: hidden;
        }

        .scheme-card::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: var(--central-accent);
        }

        .scheme-card.state-card::before {
            background: var(--state-accent);
        }

        .scheme-card.guarantee-card::before {
            background: linear-gradient(90deg, #f59e0b, #16a34a);
            height: 5px;
        }

        .scheme-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
            border-color: #94a3b8;
        }

        .card-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
            flex-wrap: wrap;
        }

        .badge-group {
            display: flex;
            align-items: center;
            gap: 6px;
            flex-wrap: wrap;
        }

        .lvl-badge {
            font-size: 0.74rem;
            font-weight: 800;
            padding: 3px 9px;
            border-radius: 6px;
        }

        .lvl-badge.state {
            background: var(--state-soft);
            color: var(--state-accent);
            border: 1px solid #a7f3d0;
        }

        .lvl-badge.central {
            background: var(--central-soft);
            color: var(--central-accent);
            border: 1px solid #bfdbfe;
        }

        .guar-badge {
            background: var(--gold-soft);
            color: #b45309;
            border: 1px solid #fde68a;
            font-size: 0.74rem;
            font-weight: 800;
            padding: 3px 9px;
            border-radius: 6px;
        }

        .dbt-badge {
            background: #f0fdf4;
            color: #15803d;
            border: 1px solid #bbf7d0;
            font-size: 0.72rem;
            font-weight: 800;
            padding: 2px 8px;
            border-radius: 6px;
        }

        .btype-badge {
            background: #f8fafc;
            color: #475569;
            border: 1px solid #e2e8f0;
            font-size: 0.72rem;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 6px;
        }

        .ministry-line {
            font-size: 0.8rem;
            font-weight: 700;
            color: var(--text-muted);
            margin-top: 6px;
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .scheme-title-primary {
            margin: 4px 0 0;
            font-size: 1.12rem;
            font-weight: 800;
            color: var(--text-main);
            line-height: 1.4;
            cursor: pointer;
        }

        .scheme-title-primary:hover {
            color: var(--primary-dark);
        }

        .scheme-title-secondary {
            margin: 2px 0 0;
            font-size: 0.82rem;
            font-weight: 600;
            color: var(--text-muted);
            line-height: 1.35;
        }

        /* BULLET POINTS INSIDE CARD (NO CRAMPED BLOCKS) */
        .card-points {
            margin: 10px 0 4px;
            padding: 10px 12px;
            background: #f8fafc;
            border-radius: 10px;
            border-left: 3px solid #cbd5e1;
            list-style: none;
        }

        .scheme-card.state-card .card-points {
            border-left-color: var(--state-accent);
            background: #f0fdf4;
        }

        .card-points li {
            position: relative;
            padding-left: 16px;
            font-size: 0.88rem;
            color: var(--text-secondary);
            line-height: 1.55;
            margin-bottom: 5px;
        }

        .card-points li:last-child {
            margin-bottom: 0;
        }

        .card-points li::before {
            content: "•";
            position: absolute;
            left: 2px;
            top: 0;
            color: var(--primary);
            font-weight: 900;
        }

        .tag-row {
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            margin-top: 4px;
        }

        .tag-pill {
            font-size: 0.74rem;
            font-weight: 700;
            color: #0f766e;
            background: #f0fdfa;
            border: 1px solid #ccfbf1;
            padding: 2px 9px;
            border-radius: 999px;
            cursor: pointer;
            transition: background 0.14s ease;
        }

        .tag-pill:hover {
            background: #ccfbf1;
        }

        .card-footer {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 8px;
            padding-top: 12px;
            border-top: 1px solid #f1f5f9;
            flex-wrap: wrap;
        }

        .btn-card-elig {
            border: 1.5px solid var(--primary);
            background: #f0fdf4;
            color: var(--primary-dark);
            padding: 7px 12px;
            border-radius: 9px;
            font-size: 0.82rem;
            font-weight: 800;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            transition: all 0.15s ease;
        }

        .btn-card-elig:hover {
            background: var(--primary);
            color: #ffffff;
        }

        .btn-card-details {
            border: none;
            background: #0f172a;
            color: #ffffff;
            padding: 7px 13px;
            border-radius: 9px;
            font-size: 0.82rem;
            font-weight: 800;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 5px;
            transition: all 0.15s ease;
        }

        .btn-card-details:hover {
            background: #1e293b;
        }

        /* PAGINATION */
        .pagination-bar {
            margin-top: 26px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            flex-wrap: wrap;
        }

        .page-btn {
            min-width: 38px;
            height: 38px;
            padding: 0 12px;
            border-radius: 10px;
            border: 1px solid var(--border-light);
            background: var(--bg-surface);
            color: var(--text-main);
            font-size: 0.86rem;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }

        .page-btn:hover:not(:disabled) {
            border-color: var(--primary);
            color: var(--primary-dark);
        }

        .page-btn.active {
            background: var(--primary);
            border-color: var(--primary);
            color: #ffffff;
        }

        .page-btn:disabled {
            opacity: 0.45;
            cursor: not-allowed;
        }

        /* ==============================================================
           4. WIDE 2-COLUMN STRUCTURED POINTS SCHEME VIEWER MODAL
           ============================================================== */
        dialog.scheme-drawer {
            border: none;
            border-radius: 20px;
            padding: 0;
            width: min(1080px, 96vw);
            max-height: 92vh;
            background: var(--bg-surface);
            color: var(--text-main);
            box-shadow: 0 25px 60px -12px rgba(15, 23, 42, 0.4);
            overflow: hidden;
        }

        dialog.scheme-drawer::backdrop,
        dialog.elig-modal::backdrop {
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(4px);
        }

        .drawer-head {
            padding: 18px 26px;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: #ffffff;
            display: flex;
            align-items: flex-start;
            justify-content: space-between;
            gap: 16px;
        }

        .drawer-close {
            border: none;
            background: rgba(255, 255, 255, 0.14);
            color: #ffffff;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            font-size: 1.05rem;
            cursor: pointer;
            flex-shrink: 0;
        }

        .drawer-close:hover {
            background: rgba(255, 255, 255, 0.25);
        }

        .drawer-split {
            display: grid;
            grid-template-columns: 240px 1fr;
            max-height: calc(92vh - 155px);
            overflow: hidden;
        }

        .drawer-nav {
            background: #f8fafc;
            border-right: 1px solid var(--border-light);
            padding: 16px 12px;
            overflow-y: auto;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .d-nav-link {
            border: none;
            background: transparent;
            text-align: left;
            padding: 10px 14px;
            border-radius: 10px;
            font-size: 0.9rem;
            font-weight: 700;
            color: var(--text-secondary);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.14s ease;
        }

        .d-nav-link:hover, .d-nav-link.active {
            background: #e2e8f0;
            color: #0f172a;
            font-weight: 800;
        }

        .d-nav-elig-cta {
            margin-top: 12px;
            padding: 12px;
            border-radius: 12px;
            background: #f0fdf4;
            border: 1.5px solid #86efac;
            text-align: center;
        }

        .drawer-content {
            padding: 24px 30px;
            overflow-y: auto;
            scroll-behavior: smooth;
        }

        .pt-section {
            margin-bottom: 28px;
            padding-bottom: 22px;
            border-bottom: 1px solid #e2e8f0;
        }

        .pt-section:last-child {
            border-bottom: none;
            margin-bottom: 0;
        }

        .pt-sec-title {
            margin: 0 0 14px;
            font-size: 1.25rem;
            font-weight: 800;
            color: #0f172a;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        /* AST & POINTS STYLING (CLEAN NUMBERED & BULLETED LISTS) */
        .ast-subheading {
            font-size: 1rem;
            font-weight: 800;
            color: #0f172a;
            text-decoration: underline;
            text-underline-offset: 4px;
            margin: 16px 0 10px;
        }

        .ast-ol {
            margin: 8px 0 14px;
            padding-left: 24px;
        }

        .ast-ol > li {
            margin-bottom: 10px;
            font-size: 0.96rem;
            color: #1e293b;
            line-height: 1.7;
            padding-left: 4px;
        }

        .ast-ol > li::marker {
            font-weight: 800;
            color: #0f172a;
        }

        .ast-ul {
            margin: 8px 0 14px;
            padding-left: 22px;
            list-style-type: disc;
        }

        .ast-ul > li {
            margin-bottom: 9px;
            font-size: 0.96rem;
            color: #1e293b;
            line-height: 1.7;
            padding-left: 4px;
        }

        .ast-ul > li::marker {
            color: var(--primary);
            font-size: 1.1em;
        }

        .ast-callout {
            background: #f0fdf4;
            border-left: 4px solid var(--primary);
            padding: 12px 16px;
            border-radius: 8px;
            margin: 10px 0;
            font-size: 0.95rem;
            color: #14532d;
            font-weight: 600;
        }

        .ast-step-card {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 12px 16px;
            margin-bottom: 10px;
            font-size: 0.95rem;
            line-height: 1.65;
            color: #1e293b;
        }

        .ast-table-wrap {
            overflow-x: auto;
            margin: 12px 0;
        }

        .ast-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.9rem;
        }

        .ast-table th, .ast-table td {
            border: 1px solid #cbd5e1;
            padding: 9px 12px;
            text-align: left;
        }

        .ast-table th {
            background: #f1f5f9;
            font-weight: 800;
        }

        .faq-item {
            border: 1px solid var(--border-light);
            border-radius: 12px;
            margin-bottom: 10px;
            background: #ffffff;
            overflow: hidden;
        }

        .faq-q {
            padding: 12px 16px;
            font-size: 0.96rem;
            font-weight: 800;
            color: #0f172a;
            cursor: pointer;
            background: #f8fafc;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .faq-a {
            padding: 12px 16px;
            font-size: 0.93rem;
            color: var(--text-secondary);
            border-top: 1px solid var(--border-light);
        }

        .drawer-foot {
            padding: 14px 26px;
            border-top: 1px solid var(--border-light);
            background: var(--bg-surface);
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
            flex-wrap: wrap;
        }

        .btn-primary-action {
            background: var(--primary);
            color: #ffffff;
            text-decoration: none;
            padding: 10px 18px;
            border-radius: 10px;
            font-size: 0.9rem;
            font-weight: 800;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            border: none;
            cursor: pointer;
        }

        .btn-primary-action:hover {
            background: var(--primary-dark);
        }

        .btn-secondary-action {
            background: #f1f5f9;
            color: var(--text-main);
            text-decoration: none;
            padding: 10px 16px;
            border-radius: 10px;
            font-size: 0.88rem;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            border: 1px solid var(--border-light);
            cursor: pointer;
        }

        /* ==============================================================
           5. INTERACTIVE KANNADA "CHECK ELIGIBILITY" QUESTIONNAIRE MODAL
              (MATCHING SCREENSHOT 1 STYLE IN KANNADA!)
           ============================================================== */
        dialog.elig-modal {
            border: none;
            border-radius: 18px;
            padding: 0;
            width: min(680px, 95vw);
            max-height: 90vh;
            background: #ffffff;
            color: #0f172a;
            box-shadow: 0 25px 60px -12px rgba(15, 23, 42, 0.45);
            overflow: hidden;
        }

        .elig-head {
            padding: 16px 24px;
            border-bottom: 1px solid #e2e8f0;
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #ffffff;
        }

        .elig-head h3 {
            margin: 0;
            font-size: 1.2rem;
            font-weight: 800;
            color: #0f172a;
        }

        .elig-close {
            border: none;
            background: transparent;
            color: #ef4444;
            font-size: 1.3rem;
            font-weight: 800;
            cursor: pointer;
            padding: 4px 8px;
        }

        .elig-body {
            padding: 20px 26px 28px;
            overflow-y: auto;
            max-height: calc(90vh - 135px);
        }

        .elig-scheme-banner {
            text-align: center;
            color: #16a34a;
            font-size: 1.22rem;
            font-weight: 800;
            margin: 0 0 18px;
            padding-bottom: 12px;
            border-bottom: 1px dashed #cbd5e1;
        }

        .elig-q-block {
            margin-bottom: 20px;
            padding-bottom: 18px;
            border-bottom: 1px solid #f1f5f9;
        }

        .elig-q-title {
            font-size: 1rem;
            font-weight: 700;
            color: #1e293b;
            margin-bottom: 8px;
            line-height: 1.55;
        }

        .elig-q-title .req-star {
            color: #ef4444;
            font-weight: 800;
            margin-left: 3px;
        }

        .elig-q-points {
            margin: 6px 0 12px;
            padding-left: 24px;
            list-style-type: disc;
        }

        .elig-q-points li {
            font-size: 0.93rem;
            color: #334155;
            margin-bottom: 5px;
            line-height: 1.55;
        }

        .elig-radios {
            display: flex;
            align-items: center;
            gap: 22px;
            margin-top: 8px;
        }

        .elig-radio-label {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 0.96rem;
            font-weight: 700;
            color: #1e293b;
            cursor: pointer;
            padding: 6px 14px;
            border-radius: 999px;
            border: 1.5px solid #e2e8f0;
            background: #f8fafc;
            transition: all 0.14s ease;
        }

        .elig-radio-label:hover {
            border-color: #16a34a;
        }

        .elig-radio-label.selected-yes {
            border-color: #16a34a;
            background: #f0fdf4;
            color: #15803d;
        }

        .elig-radio-label.selected-no {
            border-color: #16a34a;
            background: #f0fdf4;
            color: #15803d;
        }

        .elig-radio-label input[type="radio"] {
            accent-color: #16a34a;
            width: 17px;
            height: 17px;
            cursor: pointer;
        }

        .elig-verdict {
            margin-top: 18px;
            padding: 16px 20px;
            border-radius: 14px;
            display: none;
        }

        .elig-verdict.pass {
            display: block;
            background: #f0fdf4;
            border: 2px solid #22c55e;
            color: #14532d;
        }

        .elig-verdict.fail {
            display: block;
            background: #fef2f2;
            border: 2px solid #f87171;
            color: #7f1d1d;
        }

        .elig-verdict.pending {
            display: block;
            background: #f8fafc;
            border: 1px dashed #94a3b8;
            color: #475569;
        }

        @media (max-width: 980px) {
            .workspace {
                grid-template-columns: 1fr;
            }
            .mobile-filter-trigger {
                display: inline-flex;
            }
            .filter-dock {
                display: none;
                position: fixed;
                inset: 0;
                z-index: 200;
                max-height: 100vh;
                border-radius: 0;
                padding: 20px;
            }
            .filter-dock.open {
                display: block;
            }
            .drawer-split {
                grid-template-columns: 1fr;
            }
            .drawer-nav {
                flex-direction: row;
                overflow-x: auto;
                border-right: none;
                border-bottom: 1px solid var(--border-light);
                padding: 10px 14px;
            }
            .d-nav-link {
                white-space: nowrap;
                padding: 7px 12px;
            }
            .d-nav-elig-cta {
                display: none;
            }
        }

        @media (max-width: 640px) {
            .command-inner {
                padding: 10px 14px;
            }
            .level-seg {
                width: 100%;
                justify-content: space-between;
            }
            .level-btn {
                flex: 1;
                justify-content: center;
                padding: 7px 8px;
                font-size: 0.8rem;
            }
            .search-wrap {
                max-width: 100%;
                width: 100%;
            }
            .schemes-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>

    <!-- 1. COMPACT COMMAND BAR -->
    <section class="command-header" aria-label="Scheme Controls">
        <div class="command-inner">
            <div class="level-seg" role="tablist">
                <button type="button" class="level-btn active" data-level="all" onclick="setLevelFilter('all')">
                    <span id="lbl-tab-all">ಎಲ್ಲಾ ಯೋಜನೆಗಳು</span>
                    <span class="level-count" id="cnt-all">885</span>
                </button>
                <button type="button" class="level-btn" data-level="State" onclick="setLevelFilter('State')">
                    <span id="lbl-tab-state">🏛️ ಕರ್ನಾಟಕ ರಾಜ್ಯ</span>
                    <span class="level-count" id="cnt-state">112</span>
                </button>
                <button type="button" class="level-btn" data-level="Central" onclick="setLevelFilter('Central')">
                    <span id="lbl-tab-central">🇮🇳 ಕೇಂದ್ರ ಸರ್ಕಾರ</span>
                    <span class="level-count" id="cnt-central">773</span>
                </button>
            </div>

            <div class="search-wrap">
                <span class="search-icon">🔍</span>
                <input type="search" id="scheme-search" class="search-input" placeholder="ಯೋಜನೆ, ಇಲಾಖೆ ಅಥವಾ ಟ್ಯಾಗ್ ಹುಡುಕಿ... (Search 885 schemes)" oninput="onSearchInput(this.value)">
                <button type="button" id="search-clear-btn" class="search-clear" onclick="clearSearch()" title="Clear">✕</button>
            </div>

            <div class="header-controls">
                <button type="button" class="mobile-filter-trigger" onclick="toggleMobileFilters()">
                    <span>⚙️ ಫಿಲ್ಟರ್</span>
                </button>
                <select id="sort-select" class="sort-select" onchange="setSortOrder(this.value)" aria-label="Sort schemes">
                    <option value="relevance">ಆದ್ಯತೆ (Relevance)</option>
                    <option value="state_first">ರಾಜ್ಯ ಮೊದಲು (State First)</option>
                    <option value="az">ಹೆಸರು (A → Z)</option>
                    <option value="za">ಹೆಸರು (Z → A)</option>
                </select>
                <div class="lang-switch" role="group" aria-label="Language">
                    <button type="button" class="lang-btn active" id="lang-kn" onclick="setLang('kn')">ಕನ್ನಡ</button>
                    <button type="button" class="lang-btn" id="lang-en" onclick="setLang('en')">EN</button>
                </div>
            </div>
        </div>
    </section>

    <!-- 2. HORIZONTAL CATEGORY RIBBON -->
    <section class="category-ribbon-wrap" aria-label="Scheme Categories">
        <div class="category-ribbon" id="category-ribbon"></div>
    </section>

    <!-- 3. WORKSPACE: DYNAMIC FILTER DOCK + POINTS FEED -->
    <main class="workspace">
        <!-- LEFT DYNAMIC FILTER DOCK -->
        <aside class="filter-dock" id="filter-dock" aria-label="Filter By">
            <div class="dock-header">
                <div class="dock-title">
                    <span>⚡ ಡೈನಾಮಿಕ್ ಫಿಲ್ಟರ್ (Filter By)</span>
                </div>
                <div style="display:flex; gap:6px; align-items:center;">
                    <button type="button" class="reset-btn" onclick="resetAllFilters()">ಮರುಹೊಂದಿಸಿ (Reset)</button>
                    <button type="button" class="reset-btn" id="close-mobile-dock" style="display:none;" onclick="toggleMobileFilters()">✕</button>
                </div>
            </div>

            <!-- Quick Boolean Facets -->
            <div class="quick-toggles">
                <button type="button" class="q-toggle" id="tog-dbt" onclick="toggleBoolFilter('dbtScheme')">
                    <span>🏦 DBT ನೇರ ನಗದು</span>
                    <span class="q-badge" id="cnt-dbt">0</span>
                </button>
                <button type="button" class="q-toggle" id="tog-bpl" onclick="toggleBoolFilter('isBpl')">
                    <span>🪪 BPL ಕಾರ್ಡ್</span>
                    <span class="q-badge" id="cnt-bpl">0</span>
                </button>
                <button type="button" class="q-toggle" id="tog-student" onclick="toggleBoolFilter('isStudent')">
                    <span>🎓 ವಿದ್ಯಾರ್ಥಿ</span>
                    <span class="q-badge" id="cnt-student">0</span>
                </button>
                <button type="button" class="q-toggle" id="tog-disability" onclick="toggleBoolFilter('disability')">
                    <span>♿ ವಿಕಲಚೇತನರು</span>
                    <span class="q-badge" id="cnt-disability">0</span>
                </button>
                <button type="button" class="q-toggle" id="tog-minority" onclick="toggleBoolFilter('minority')">
                    <span>🕌 ಅಲ್ಪಸಂಖ್ಯಾತರು</span>
                    <span class="q-badge" id="cnt-minority">0</span>
                </button>
                <button type="button" class="q-toggle" id="tog-guarantee" onclick="toggleBoolFilter('is_guarantee')">
                    <span>⭐ 5 ಗ್ಯಾರಂಟಿ</span>
                    <span class="q-badge" id="cnt-guarantee">5</span>
                </button>
            </div>

            <!-- Gender (Dynamic Counts) -->
            <div class="f-group">
                <div class="f-label"><span>ಲಿಂಗ / Gender</span></div>
                <div class="f-pills" id="pills-gender"></div>
            </div>

            <!-- Age -->
            <div class="f-group">
                <div class="f-label"><span>ವಯಸ್ಸು / Age</span></div>
                <select id="sel-age" class="f-select" onchange="setFacet('age', this.value)"></select>
            </div>

            <!-- Caste (Dynamic Counts) -->
            <div class="f-group">
                <div class="f-label"><span>ಜಾತಿ ವರ್ಗ / Caste</span></div>
                <div class="f-pills" id="pills-caste"></div>
            </div>

            <!-- Residence (Dynamic Counts) -->
            <div class="f-group">
                <div class="f-label"><span>ವಾಸಸ್ಥಳ / Residence</span></div>
                <div class="f-pills" id="pills-residence"></div>
            </div>

            <!-- Benefit Type (Dynamic Counts) -->
            <div class="f-group">
                <div class="f-label"><span>ಸೌಲಭ್ಯದ ಪ್ರಕಾರ / Benefit Type</span></div>
                <div class="f-pills" id="pills-benefitType"></div>
            </div>

            <!-- Occupation (Dynamic Counts) -->
            <div class="f-group">
                <div class="f-label"><span>ವೃತ್ತಿ / Occupation</span></div>
                <select id="sel-occupation" class="f-select" onchange="setFacet('occupation', this.value)"></select>
            </div>

            <!-- Employment Status -->
            <div class="f-group">
                <div class="f-label"><span>ಉದ್ಯೋಗ ಸ್ಥಿತಿ / Employment Status</span></div>
                <select id="sel-employment" class="f-select" onchange="setFacet('employmentStatus', this.value)"></select>
            </div>

            <!-- Marital Status -->
            <div class="f-group">
                <div class="f-label"><span>ವೈವಾಹಿಕ ಸ್ಥಿತಿ / Marital Status</span></div>
                <select id="sel-marital" class="f-select" onchange="setFacet('maritalStatus', this.value)"></select>
            </div>

            <!-- Disability Percentage -->
            <div class="f-group">
                <div class="f-label"><span>ಅಂಗವೈಕಲ್ಯ ಶೇಕಡಾವಾರು / Disability %</span></div>
                <select id="sel-disability-pct" class="f-select" onchange="setFacet('disabilityPercentage', this.value)"></select>
            </div>

            <!-- Application Mode (Dynamic Counts) -->
            <div class="f-group">
                <div class="f-label"><span>ಅರ್ಜಿ ವಿಧಾನ / Application Mode</span></div>
                <div class="f-pills" id="pills-appMode"></div>
            </div>

            <!-- Ministry / Department -->
            <div class="f-group">
                <div class="f-label"><span>ಸಚಿವಾಲಯ / ಇಲಾಖೆ (Ministry)</span></div>
                <select id="sel-ministry" class="f-select" onchange="setFacet('ministry', this.value)"></select>
            </div>
        </aside>

        <!-- RIGHT MAIN RESULTS AREA -->
        <section class="feed-area">
            <!-- 1-Click Citizen Persona Matcher -->
            <div class="profile-matcher-bar">
                <div class="pm-left">
                    <span class="pm-badge">🎯 ತ್ವರಿತ ಅರ್ಹತಾ ಆಯ್ಕೆ</span>
                    <div class="pm-personas" id="persona-bar">
                        <button type="button" class="pm-chip" data-p="woman" onclick="applyPersona('woman')">👩 ಮಹಿಳೆ / ಗೃಹಿಣಿ</button>
                        <button type="button" class="pm-chip" data-p="farmer" onclick="applyPersona('farmer')">🌾 ರೈತ / ಕೃಷಿಕ</button>
                        <button type="button" class="pm-chip" data-p="student" onclick="applyPersona('student')">🎓 ವಿದ್ಯಾರ್ಥಿ</button>
                        <button type="button" class="pm-chip" data-p="youth" onclick="applyPersona('youth')">🧑‍💻 ನಿರುದ್ಯೋಗಿ ಯುವಕ</button>
                        <button type="button" class="pm-chip" data-p="worker" onclick="applyPersona('worker')">👷 ಕಟ್ಟಡ / ಕುಶಲಕರ್ಮಿ</button>
                        <button type="button" class="pm-chip" data-p="business" onclick="applyPersona('business')">🏪 ಉದ್ಯಮಿ / ವ್ಯಾಪಾರಿ</button>
                        <button type="button" class="pm-chip" data-p="senior" onclick="applyPersona('senior')">👴 ಹಿರಿಯ ನಾಗರಿಕ (60+)</button>
                        <button type="button" class="pm-chip" data-p="disabled" onclick="applyPersona('disabled')">♿ ವಿಕಲಚೇತನರು</button>
                    </div>
                </div>
            </div>

            <div class="feed-bar">
                <div class="results-summary">
                    <span id="results-count-text"><strong id="results-num">885</strong> ಯೋಜನೆಗಳು ಲಭ್ಯವಿವೆ</span>
                    <div class="active-chips" id="active-chips"></div>
                </div>
                <div class="view-toggle" role="group" aria-label="View Mode">
                    <button type="button" class="v-btn active" id="view-grid-btn" onclick="setViewMode('grid')" title="Grid View">⊞</button>
                    <button type="button" class="v-btn" id="view-list-btn" onclick="setViewMode('list')" title="List View">☰</button>
                </div>
            </div>

            <div class="schemes-grid" id="schemes-grid"></div>
            <div class="pagination-bar" id="pagination-bar"></div>
        </section>
    </main>

    <!-- 4. WIDE 2-COLUMN STRUCTURED POINTS SCHEME VIEWER MODAL -->
    <dialog class="scheme-drawer" id="scheme-drawer" onclick="if(event.target===this) closeSchemeDrawer()">
        <div class="drawer-head">
            <div>
                <div id="drawer-badges" style="display:flex; gap:6px; flex-wrap:wrap; margin-bottom:8px;"></div>
                <h2 id="drawer-title" style="margin:0; font-size:1.3rem; font-weight:800; line-height:1.35;"></h2>
                <div id="drawer-subtitle" style="margin-top:4px; font-size:0.86rem; color:#cbd5e1;"></div>
            </div>
            <div style="display:flex; align-items:center; gap:10px;">
                <button type="button" class="btn-primary-action" id="drawer-top-elig-btn" style="background:#22c55e;">✅ ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ (Check Eligibility)</button>
                <button type="button" class="drawer-close" onclick="closeSchemeDrawer()">✕</button>
            </div>
        </div>
        <div class="drawer-split">
            <nav class="drawer-nav" id="drawer-nav">
                <button type="button" class="d-nav-link active" onclick="scrollToSection('sec-details', this)">📌 ವಿವರಗಳು (Details)</button>
                <button type="button" class="d-nav-link" onclick="scrollToSection('sec-benefits', this)">🎁 ಸೌಲಭ್ಯಗಳು (Benefits)</button>
                <button type="button" class="d-nav-link" onclick="scrollToSection('sec-eligibility', this)">✅ ಅರ್ಹತೆ (Eligibility)</button>
                <button type="button" class="d-nav-link" id="nav-btn-exclusions" onclick="scrollToSection('sec-exclusions', this)">🚫 ವಿನಾಯಿತಿಗಳು (Exclusions)</button>
                <button type="button" class="d-nav-link" onclick="scrollToSection('sec-process', this)">📝 ಅರ್ಜಿ ವಿಧಾನ (Application)</button>
                <button type="button" class="d-nav-link" onclick="scrollToSection('sec-docs', this)">📄 ಅಗತ್ಯ ದಾಖಲೆಗಳು (Documents)</button>
                <button type="button" class="d-nav-link" id="nav-btn-faqs" onclick="scrollToSection('sec-faqs', this)">❓ ಪ್ರಶ್ನೋತ್ತರಗಳು (FAQs)</button>
                <button type="button" class="d-nav-link" onclick="scrollToSection('sec-sources', this)">🌐 ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್ (Website)</button>
                <div class="d-nav-elig-cta">
                    <div style="font-size:0.8rem; font-weight:800; color:#14532d; margin-bottom:8px;">ನೀವು ಈ ಯೋಜನೆಗೆ ಅರ್ಹರೇ?</div>
                    <button type="button" class="btn-primary-action" id="drawer-side-elig-btn" style="width:100%; justify-content:center; padding:8px 12px; font-size:0.82rem;">✅ ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ</button>
                </div>
            </nav>
            <div class="drawer-content" id="drawer-body"></div>
        </div>
        <div class="drawer-foot" id="drawer-foot"></div>
    </dialog>

    <!-- 5. INTERACTIVE KANNADA "CHECK ELIGIBILITY" QUESTIONNAIRE MODAL -->
    <dialog class="elig-modal" id="elig-modal" onclick="if(event.target===this) closeEligModal()">
        <div class="elig-head">
            <h3>ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ (Check Eligibility)</h3>
            <button type="button" class="elig-close" onclick="closeEligModal()">✕</button>
        </div>
        <div class="elig-body">
            <div class="elig-scheme-banner" id="elig-scheme-title"></div>
            <div id="elig-questions-container"></div>
            <div class="elig-verdict pending" id="elig-verdict-box"></div>
        </div>
    </dialog>

    <script>
        let ALL_SCHEMES = [];
        let FILTERED_SCHEMES = [];
        let CATEGORY_MAP_KN = {};
        let CURRENT_LANG = 'kn';
        let VIEW_MODE = 'grid';
        let CURRENT_PAGE = 1;
        let ACTIVE_PERSONA = '';
        const PAGE_SIZE = 24;
        const SCHEME_API_CACHE = {};

        const STATE = {
            level: 'all',
            category: '',
            query: '',
            sort: 'relevance',
            gender: '',
            age: '',
            caste: '',
            residence: '',
            benefitType: '',
            occupation: '',
            employmentStatus: '',
            maritalStatus: '',
            disabilityPercentage: '',
            applicationMode: '',
            ministry: '',
            dbtScheme: false,
            isBpl: false,
            isStudent: false,
            disability: false,
            minority: false,
            is_guarantee: false
        };

        const CATEGORY_ICONS = {
            "Education & Learning": "🎓",
            "Business & Entrepreneurship": "💼",
            "Social welfare & Empowerment": "🤝",
            "Agriculture,Rural & Environment": "🌾",
            "Skills & Employment": "🛠️",
            "Banking,Financial Services and Insurance": "🏦",
            "Science, IT & Communications": "💻",
            "Women and Child": "👩",
            "Sports & Culture": "🏅",
            "Health & Wellness": "🏥",
            "Transport & Infrastructure": "🚌",
            "Utility & Sanitation": "💧",
            "Housing & Shelter": "🏠",
            "Public Safety,Law & Justice": "⚖️",
            "Travel & Tourism": "✈️"
        };

        /* Official Portal Fallbacks by Category/Level (NO myscheme.gov.in links!) */
        function getOfficialSchemeWebsite(s, apiRefs = [], apiProcess = []) {
            // 1. Check API references for a real non-myscheme http URL
            for (const ref of (apiRefs || [])) {
                if (ref && ref.url && ref.url.startsWith('http') && !ref.url.includes('myscheme.gov.in')) {
                    return ref.url;
                }
            }
            // 2. Check links embedded inside applicationProcess AST
            const procLinks = [];
            function findLinks(nodes) {
                if (!Array.isArray(nodes)) return;
                for (const n of nodes) {
                    if (n.link && n.link.startsWith('http') && !n.link.includes('myscheme.gov.in')) {
                        procLinks.push(n.link);
                    }
                    if (n.children) findLinks(n.children);
                    if (n.process) findLinks(n.process);
                }
            }
            findLinks(apiProcess);
            if (procLinks.length > 0) return procLinks[0];

            // 3. Check curated apply_link if not myscheme
            if (s.apply_link && s.apply_link.startsWith('http') && !s.apply_link.includes('myscheme.gov.in')) {
                return s.apply_link;
            }

            // 4. Smart department/ministry official portal mapping
            const min = ((s.ministry_en || '') + ' ' + (s.categories || []).join(' ')).toLowerCase();
            if (s.level === 'State') {
                if (min.includes('agriculture') || min.includes('horticulture')) return 'https://raitamitra.karnataka.gov.in';
                if (min.includes('education') || s.isStudent) return 'https://ssp.postmatric.karnataka.gov.in';
                if (min.includes('labour') || min.includes('construction')) return 'https://karbwwb.karnataka.gov.in';
                if (min.includes('finance') || s.slug === 'iss') return 'https://ksfc.karnataka.gov.in';
                if (min.includes('housing')) return 'https://ashraya.karnataka.gov.in';
                return 'https://sevasindhu.karnataka.gov.in';
            } else {
                if (min.includes('agriculture') || min.includes('farmers')) return 'https://agricoop.gov.in';
                if (min.includes('science') || min.includes('technology')) return 'https://onlinedst.gov.in';
                if (min.includes('msme') || min.includes('entrepreneur')) return 'https://msme.gov.in';
                if (min.includes('education') || s.isStudent) return 'https://scholarships.gov.in';
                if (min.includes('labour')) return 'https://eshram.gov.in';
                if (min.includes('social justice')) return 'https://socialjustice.gov.in';
                if (min.includes('women')) return 'https://wcd.nic.in';
                if (min.includes('health')) return 'https://pmjay.gov.in';
                return 'https://www.india.gov.in/my-government/schemes';
            }
        }

        async function initPortal() {
            try {
                const res = await fetch('/data/myscheme_karnataka_all.json');
                const data = await res.json();
                ALL_SCHEMES = data.schemes || [];
                CATEGORY_MAP_KN = data.category_map_kn || {};

                applyAllFilters();

                // Check if URL has ?id=slug (e.g., /scheme-checker?id=iss)
                const params = new URLSearchParams(window.location.search);
                const idParam = params.get('id') || params.get('scheme');
                if (idParam) {
                    setTimeout(() => openSchemeDrawer(idParam), 120);
                }
            } catch (err) {
                console.error('Failed to load schemes:', err);
                document.getElementById('schemes-grid').innerHTML = '<div style="padding:32px;text-align:center;">ಡೇಟಾ ಲೋಡ್ ಮಾಡಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ. ದಯವಿಟ್ಟು ಪುಟವನ್ನು ರಿಫ್ರೆಶ್ ಮಾಡಿ.</div>';
            }
        }

        function schemeMatches(s, ignoreKey = null) {
            if (ignoreKey !== 'level' && STATE.level !== 'all') {
                if (s.level !== STATE.level) return false;
            }
            if (ignoreKey !== 'category' && STATE.category) {
                if (!(s.categories || []).includes(STATE.category)) return false;
            }
            if (ignoreKey !== 'query' && STATE.query) {
                const q = STATE.query.toLowerCase();
                const hay = [
                    s.name_kn, s.name_en, s.short_title,
                    s.ministry_kn, s.ministry_en,
                    s.description_kn, s.description_en,
                    ...(s.tags_kn || []), ...(s.tags_en || []),
                    ...(s.categories || [])
                ].join(' ').toLowerCase();
                if (!hay.includes(q)) return false;
            }
            if (ignoreKey !== 'dbtScheme' && STATE.dbtScheme && !s.dbtScheme) return false;
            if (ignoreKey !== 'isBpl' && STATE.isBpl && !s.isBpl) return false;
            if (ignoreKey !== 'isStudent' && STATE.isStudent && !s.isStudent) return false;
            if (ignoreKey !== 'disability' && STATE.disability && !s.disability) return false;
            if (ignoreKey !== 'minority' && STATE.minority && !s.minority) return false;
            if (ignoreKey !== 'is_guarantee' && STATE.is_guarantee && !s.is_guarantee) return false;

            if (ignoreKey !== 'gender' && STATE.gender) {
                const g = s.genders || [];
                if (!g.includes(STATE.gender)) return false;
            }
            if (ignoreKey !== 'age' && STATE.age !== '') {
                const ageNum = parseInt(STATE.age, 10);
                const ab = s.ageBrackets || [];
                if (ab.length > 0 && !ab.includes(ageNum)) return false;
            }
            if (ignoreKey !== 'caste' && STATE.caste) {
                const c = s.castes || [];
                if (!c.includes(STATE.caste)) return false;
            }
            if (ignoreKey !== 'residence' && STATE.residence) {
                const r = s.residences || [];
                if (!r.includes(STATE.residence)) return false;
            }
            if (ignoreKey !== 'benefitType' && STATE.benefitType) {
                const b = s.benefitTypes || [];
                if (!b.includes(STATE.benefitType)) return false;
            }
            if (ignoreKey !== 'occupation' && STATE.occupation) {
                const o = s.occupations || [];
                if (!o.includes(STATE.occupation)) return false;
            }
            if (ignoreKey !== 'employmentStatus' && STATE.employmentStatus) {
                const e = s.employmentStatuses || [];
                if (!e.includes(STATE.employmentStatus)) return false;
            }
            if (ignoreKey !== 'maritalStatus' && STATE.maritalStatus) {
                const m = s.maritalStatuses || [];
                if (!m.includes(STATE.maritalStatus)) return false;
            }
            if (ignoreKey !== 'disabilityPercentage' && STATE.disabilityPercentage !== '') {
                const dp = parseInt(STATE.disabilityPercentage, 10);
                const list = s.disabilityPercentages || [];
                if (!list.includes(dp)) return false;
            }
            if (ignoreKey !== 'applicationMode' && STATE.applicationMode) {
                const am = s.applicationModes || [];
                if (!am.some(x => x.includes(STATE.applicationMode))) return false;
            }
            if (ignoreKey !== 'ministry' && STATE.ministry) {
                if (s.ministry_en !== STATE.ministry) return false;
            }
            return true;
        }

        function applyAllFilters() {
            FILTERED_SCHEMES = ALL_SCHEMES.filter(s => schemeMatches(s));

            if (STATE.sort === 'az') {
                FILTERED_SCHEMES.sort((a, b) => (a.name_en || '').localeCompare(b.name_en || ''));
            } else if (STATE.sort === 'za') {
                FILTERED_SCHEMES.sort((a, b) => (b.name_en || '').localeCompare(a.name_en || ''));
            } else if (STATE.sort === 'state_first') {
                FILTERED_SCHEMES.sort((a, b) => (a.level === 'State' ? 0 : 1) - (b.level === 'State' ? 0 : 1));
            } else {
                FILTERED_SCHEMES.sort((a, b) => {
                    const ga = a.is_guarantee ? 0 : 1;
                    const gb = b.is_guarantee ? 0 : 1;
                    if (ga !== gb) return ga - gb;
                    const pa = a.priority ?? 4;
                    const pb = b.priority ?? 4;
                    return pa - pb;
                });
            }

            CURRENT_PAGE = 1;
            renderDynamicSidebarFacets();
            renderCategoryRibbon();
            renderActiveChips();
            renderSchemesPage();
        }

        /* DYNAMIC FACET RENDERER: Every option shows live count based on current active filters! */
        function renderDynamicSidebarFacets() {
            const baseForLevel = ALL_SCHEMES.filter(s => schemeMatches(s, 'level'));
            document.getElementById('cnt-all').textContent = baseForLevel.length;
            document.getElementById('cnt-state').textContent = baseForLevel.filter(s => s.level === 'State').length;
            document.getElementById('cnt-central').textContent = baseForLevel.filter(s => s.level === 'Central').length;

            document.getElementById('cnt-dbt').textContent = ALL_SCHEMES.filter(s => schemeMatches(s, 'dbtScheme') && s.dbtScheme).length;
            document.getElementById('cnt-bpl').textContent = ALL_SCHEMES.filter(s => schemeMatches(s, 'isBpl') && s.isBpl).length;
            document.getElementById('cnt-student').textContent = ALL_SCHEMES.filter(s => schemeMatches(s, 'isStudent') && s.isStudent).length;
            document.getElementById('cnt-disability').textContent = ALL_SCHEMES.filter(s => schemeMatches(s, 'disability') && s.disability).length;
            document.getElementById('cnt-minority').textContent = ALL_SCHEMES.filter(s => schemeMatches(s, 'minority') && s.minority).length;
            document.getElementById('cnt-guarantee').textContent = ALL_SCHEMES.filter(s => schemeMatches(s, 'is_guarantee') && s.is_guarantee).length;

            // 1. Gender Pills
            const baseGender = ALL_SCHEMES.filter(s => schemeMatches(s, 'gender'));
            const genderOpts = [
                { val: '', label: 'ಎಲ್ಲಾ' },
                { val: 'Female', label: 'ಮಹಿಳೆ' },
                { val: 'Male', label: 'ಪುರುಷ' },
                { val: 'Transgender', label: 'ತೃತೀಯ ಲಿಂಗಿ' }
            ];
            document.getElementById('pills-gender').innerHTML = genderOpts.map(o => {
                const cnt = o.val === '' ? baseGender.length : baseGender.filter(s => (s.genders || []).includes(o.val)).length;
                return `<button type="button" class="f-pill ${STATE.gender === o.val ? 'active' : ''}" onclick="setFacet('gender', '${o.val}')">
                    <span>${o.label}</span><span class="f-pill-cnt">(${cnt})</span>
                </button>`;
            }).join('');

            // 2. Caste Pills
            const baseCaste = ALL_SCHEMES.filter(s => schemeMatches(s, 'caste'));
            const casteOpts = [
                { val: '', label: 'ಎಲ್ಲಾ' },
                { val: 'Scheduled Caste (SC)', label: 'SC' },
                { val: 'Scheduled Tribe (ST)', label: 'ST' },
                { val: 'Other Backward Class (OBC)', label: 'OBC' },
                { val: 'Particularly Vulnerable Tribal Group (PVTG)', label: 'PVTG' },
                { val: 'General', label: 'General' }
            ];
            document.getElementById('pills-caste').innerHTML = casteOpts.map(o => {
                const cnt = o.val === '' ? baseCaste.length : baseCaste.filter(s => (s.castes || []).includes(o.val)).length;
                return `<button type="button" class="f-pill ${STATE.caste === o.val ? 'active' : ''}" onclick="setFacet('caste', '${o.val}')">
                    <span>${o.label}</span><span class="f-pill-cnt">(${cnt})</span>
                </button>`;
            }).join('');

            // 3. Residence Pills
            const baseRes = ALL_SCHEMES.filter(s => schemeMatches(s, 'residence'));
            const resOpts = [
                { val: '', label: 'ಎಲ್ಲಾ' },
                { val: 'Rural', label: '🌾 ಗ್ರಾಮೀಣ' },
                { val: 'Urban', label: '🏙️ ನಗರ' }
            ];
            document.getElementById('pills-residence').innerHTML = resOpts.map(o => {
                const cnt = o.val === '' ? baseRes.length : baseRes.filter(s => (s.residences || []).includes(o.val)).length;
                return `<button type="button" class="f-pill ${STATE.residence === o.val ? 'active' : ''}" onclick="setFacet('residence', '${o.val}')">
                    <span>${o.label}</span><span class="f-pill-cnt">(${cnt})</span>
                </button>`;
            }).join('');

            // 4. Benefit Type Pills
            const baseBen = ALL_SCHEMES.filter(s => schemeMatches(s, 'benefitType'));
            const benOpts = [
                { val: '', label: 'ಎಲ್ಲಾ' },
                { val: 'Cash', label: '💰 ನಗದು (Cash)' },
                { val: 'Composite', label: '🎁 ಸಂಯೋಜಿತ' },
                { val: 'In Kind', label: '📦 ವಸ್ತು ರೂಪ' }
            ];
            document.getElementById('pills-benefitType').innerHTML = benOpts.map(o => {
                const cnt = o.val === '' ? baseBen.length : baseBen.filter(s => (s.benefitTypes || []).includes(o.val)).length;
                return `<button type="button" class="f-pill ${STATE.benefitType === o.val ? 'active' : ''}" onclick="setFacet('benefitType', '${o.val}')">
                    <span>${o.label}</span><span class="f-pill-cnt">(${cnt})</span>
                </button>`;
            }).join('');

            // 5. Application Mode Pills
            const baseMode = ALL_SCHEMES.filter(s => schemeMatches(s, 'applicationMode'));
            const modeOpts = [
                { val: '', label: 'ಎಲ್ಲಾ' },
                { val: 'Online', label: '🌐 ಆನ್‌ಲೈನ್' },
                { val: 'Offline', label: '📄 ಆಫ್‌ಲೈನ್' }
            ];
            document.getElementById('pills-appMode').innerHTML = modeOpts.map(o => {
                const cnt = o.val === '' ? baseMode.length : baseMode.filter(s => (s.applicationModes || []).some(x => x.includes(o.val))).length;
                return `<button type="button" class="f-pill ${STATE.applicationMode === o.val ? 'active' : ''}" onclick="setFacet('applicationMode', '${o.val}')">
                    <span>${o.label}</span><span class="f-pill-cnt">(${cnt})</span>
                </button>`;
            }).join('');

            // 6. Age Select with Dynamic Counts
            const baseAge = ALL_SCHEMES.filter(s => schemeMatches(s, 'age'));
            const ageOpts = [
                { val: '', label: `ಎಲ್ಲಾ ವಯಸ್ಸಿನವರು (${baseAge.length})` },
                { val: '0', label: '0 – 10 ವರ್ಷ (ಮಕ್ಕಳು)' },
                { val: '10', label: '11 – 20 ವರ್ಷ (ವಿದ್ಯಾರ್ಥಿ / ಯುವಕರು)' },
                { val: '20', label: '21 – 30 ವರ್ಷ (ಯುವಜನತೆ)' },
                { val: '30', label: '31 – 40 ವರ್ಷ (ವಯಸ್ಕರು)' },
                { val: '40', label: '41 – 50 ವರ್ಷ (ಮಧ್ಯವಯಸ್ಕರು)' },
                { val: '50', label: '51 – 60 ವರ್ಷ' },
                { val: '60', label: '60+ ವರ್ಷ (ಹಿರಿಯ ನಾಗರಿಕರು)' }
            ];
            document.getElementById('sel-age').innerHTML = ageOpts.map(o => {
                if (o.val === '') return `<option value="" ${STATE.age === '' ? 'selected' : ''}>${o.label}</option>`;
                const n = parseInt(o.val, 10);
                const c = baseAge.filter(s => !(s.ageBrackets || []).length || (s.ageBrackets || []).includes(n)).length;
                return `<option value="${o.val}" ${STATE.age === o.val ? 'selected' : ''}>${o.label} (${c})</option>`;
            }).join('');

            // 7. Occupation Select with Dynamic Counts
            const baseOcc = ALL_SCHEMES.filter(s => schemeMatches(s, 'occupation'));
            const occOpts = [
                { val: '', label: `ಎಲ್ಲಾ ವೃತ್ತಿಗಳು (${baseOcc.length})` },
                { val: 'Student', label: '🎓 ವಿದ್ಯಾರ್ಥಿ (Student)' },
                { val: 'Farmer', label: '🌾 ರೈತ / ಕೃಷಿಕ (Farmer)' },
                { val: 'Artisans, Spinners & Weavers', label: '🧶 ಕುಶಲಕರ್ಮಿ ಮತ್ತು ನೇಕಾರ (Artisan)' },
                { val: 'Construction Worker', label: '👷 ಕಟ್ಟಡ ಕಾರ್ಮಿಕ (Construction Worker)' },
                { val: 'Unorganized Worker', label: '🛠️ ಅಸಂಘಟಿತ ಕಾರ್ಮಿಕ (Unorganized Worker)' },
                { val: 'Sportsperson', label: '🏅 ಕ್ರೀಡಾಪಟು (Sportsperson)' },
                { val: 'Ex Servicemen', label: '🎖️ ಮಾಜಿ ಸೈನಿಕ (Ex Servicemen)' },
                { val: 'Safai Karamchari', label: '🧹 ಪೌರಕಾರ್ಮಿಕ (Safai Karamchari)' },
                { val: 'Teacher / Faculty', label: '👩‍🏫 ಶಿಕ್ಷಕ / ಪ್ರಾಧ್ಯಾಪಕ (Teacher)' },
                { val: 'Artists', label: '🎭 ಕಲಾವಿದರು (Artists)' },
                { val: 'Fishermen', label: '🐟 ಮೀನುಗಾರರು (Fishermen)' }
            ];
            document.getElementById('sel-occupation').innerHTML = occOpts.map(o => {
                if (o.val === '') return `<option value="" ${STATE.occupation === '' ? 'selected' : ''}>${o.label}</option>`;
                const c = baseOcc.filter(s => (s.occupations || []).includes(o.val)).length;
                return `<option value="${o.val}" ${STATE.occupation === o.val ? 'selected' : ''}>${o.label} (${c})</option>`;
            }).join('');

            // 8. Employment Status Select
            const baseEmp = ALL_SCHEMES.filter(s => schemeMatches(s, 'employmentStatus'));
            const empOpts = [
                { val: '', label: `ಎಲ್ಲಾ (${baseEmp.length})` },
                { val: 'Self-Employed/ Entrepreneur', label: 'ಸ್ವಯಂ ಉದ್ಯೋಗಿ / ಉದ್ಯಮಿ (Self-Employed)' },
                { val: 'Employed', label: 'ಉದ್ಯೋಗಿ (Employed)' },
                { val: 'Unemployed', label: 'ನಿರುದ್ಯೋಗಿ (Unemployed)' }
            ];
            document.getElementById('sel-employment').innerHTML = empOpts.map(o => {
                if (o.val === '') return `<option value="" ${STATE.employmentStatus === '' ? 'selected' : ''}>${o.label}</option>`;
                const c = baseEmp.filter(s => (s.employmentStatuses || []).includes(o.val)).length;
                return `<option value="${o.val}" ${STATE.employmentStatus === o.val ? 'selected' : ''}>${o.label} (${c})</option>`;
            }).join('');

            // 9. Marital Status Select
            const baseMar = ALL_SCHEMES.filter(s => schemeMatches(s, 'maritalStatus'));
            const marOpts = [
                { val: '', label: `ಎಲ್ಲಾ (${baseMar.length})` },
                { val: 'Married', label: 'ವಿವಾಹಿತ (Married)' },
                { val: 'Widowed', label: 'ವಿಧವೆ (Widowed)' },
                { val: 'Never Married', label: 'ಅವಿವಾಹಿತ (Never Married)' },
                { val: 'Divorced', label: 'ವಿಚ್ಛೇದಿತ (Divorced)' },
                { val: 'Separated', label: 'ಪ್ರತ್ಯೇಕ (Separated)' }
            ];
            document.getElementById('sel-marital').innerHTML = marOpts.map(o => {
                if (o.val === '') return `<option value="" ${STATE.maritalStatus === '' ? 'selected' : ''}>${o.label}</option>`;
                const c = baseMar.filter(s => (s.maritalStatuses || []).includes(o.val)).length;
                return `<option value="${o.val}" ${STATE.maritalStatus === o.val ? 'selected' : ''}>${o.label} (${c})</option>`;
            }).join('');

            // 10. Disability % Select
            const baseDis = ALL_SCHEMES.filter(s => schemeMatches(s, 'disabilityPercentage'));
            const disOpts = [
                { val: '', label: `ಯಾವುದೇ (${baseDis.length})` },
                { val: '40', label: '40% ಅಥವಾ ಹೆಚ್ಚು' },
                { val: '50', label: '50% ಅಥವಾ ಹೆಚ್ಚು' },
                { val: '60', label: '60% ಅಥವಾ ಹೆಚ್ಚು' },
                { val: '80', label: '80% ಅಥವಾ ಹೆಚ್ಚು' }
            ];
            document.getElementById('sel-disability-pct').innerHTML = disOpts.map(o => {
                if (o.val === '') return `<option value="" ${STATE.disabilityPercentage === '' ? 'selected' : ''}>${o.label}</option>`;
                const c = baseDis.filter(s => (s.disabilityPercentages || []).includes(parseInt(o.val, 10))).length;
                return `<option value="${o.val}" ${STATE.disabilityPercentage === o.val ? 'selected' : ''}>${o.label} (${c})</option>`;
            }).join('');

            // 11. Ministry Select with Dynamic Counts
            const baseMin = ALL_SCHEMES.filter(s => schemeMatches(s, 'ministry'));
            const mCounts = {};
            baseMin.forEach(s => {
                const m = s.ministry_en || 'Other';
                mCounts[m] = (mCounts[m] || 0) + 1;
            });
            const sortedMin = Object.entries(mCounts).sort((a, b) => b[1] - a[1]);
            document.getElementById('sel-ministry').innerHTML = `<option value="">ಎಲ್ಲಾ ಇಲಾಖೆಗಳು (${baseMin.length})</option>` +
                sortedMin.map(([m, c]) => `<option value="${escapeHtml(m)}" ${STATE.ministry === m ? 'selected' : ''}>${escapeHtml(m)} (${c})</option>`).join('');

            const numEl = document.getElementById('results-count-text');
            if (CURRENT_LANG === 'kn') {
                numEl.innerHTML = `<strong id="results-num">${FILTERED_SCHEMES.length}</strong> ಯೋಜನೆಗಳು ಲಭ್ಯವಿವೆ`;
            } else {
                numEl.innerHTML = `Found <strong id="results-num">${FILTERED_SCHEMES.length}</strong> schemes`;
            }
        }

        function renderCategoryRibbon() {
            const ribbon = document.getElementById('category-ribbon');
            const baseForCat = ALL_SCHEMES.filter(s => schemeMatches(s, 'category'));
            const catCounts = {};
            baseForCat.forEach(s => {
                (s.categories || []).forEach(c => {
                    catCounts[c] = (catCounts[c] || 0) + 1;
                });
            });

            const allCategories = Object.keys(CATEGORY_ICONS);
            allCategories.sort((a, b) => (catCounts[b] || 0) - (catCounts[a] || 0));

            let html = `<button type="button" class="cat-chip ${STATE.category === '' ? 'active' : ''}" onclick="setCategory('')">
                <span>✨ ${CURRENT_LANG === 'kn' ? 'ಎಲ್ಲಾ ವಿಭಾಗಗಳು' : 'All Categories'}</span>
                <span class="cat-chip-count">${baseForCat.length}</span>
            </button>`;

            allCategories.forEach(cat => {
                const cnt = catCounts[cat] || 0;
                if (cnt === 0 && STATE.category !== cat) return;
                const icon = CATEGORY_ICONS[cat] || '📌';
                const label = CURRENT_LANG === 'kn' ? (CATEGORY_MAP_KN[cat] || cat) : cat;
                const active = STATE.category === cat ? 'active' : '';
                html += `<button type="button" class="cat-chip ${active}" onclick="setCategory('${escapeAttr(cat)}')">
                    <span>${icon} ${escapeHtml(label)}</span>
                    <span class="cat-chip-count">${cnt}</span>
                </button>`;
            });

            ribbon.innerHTML = html;
        }

        function renderActiveChips() {
            const wrap = document.getElementById('active-chips');
            const chips = [];

            if (STATE.category) {
                const lbl = CURRENT_LANG === 'kn' ? (CATEGORY_MAP_KN[STATE.category] || STATE.category) : STATE.category;
                chips.push({ label: lbl, clear: () => setCategory('') });
            }
            if (STATE.query) chips.push({ label: `"${STATE.query}"`, clear: () => clearSearch() });
            if (STATE.dbtScheme) chips.push({ label: 'DBT ನೇರ ನಗದು', clear: () => toggleBoolFilter('dbtScheme') });
            if (STATE.isBpl) chips.push({ label: 'BPL ಕಾರ್ಡ್', clear: () => toggleBoolFilter('isBpl') });
            if (STATE.isStudent) chips.push({ label: 'ವಿದ್ಯಾರ್ಥಿ', clear: () => toggleBoolFilter('isStudent') });
            if (STATE.disability) chips.push({ label: 'ವಿಕಲಚೇತನರು', clear: () => toggleBoolFilter('disability') });
            if (STATE.minority) chips.push({ label: 'ಅಲ್ಪಸಂಖ್ಯಾತರು', clear: () => toggleBoolFilter('minority') });
            if (STATE.is_guarantee) chips.push({ label: '5 ಗ್ಯಾರಂಟಿ', clear: () => toggleBoolFilter('is_guarantee') });
            if (STATE.gender) chips.push({ label: STATE.gender, clear: () => setFacet('gender', '') });
            if (STATE.age !== '') chips.push({ label: `ವಯಸ್ಸು ${STATE.age}+`, clear: () => setFacet('age', '') });
            if (STATE.caste) chips.push({ label: STATE.caste, clear: () => setFacet('caste', '') });
            if (STATE.residence) chips.push({ label: STATE.residence, clear: () => setFacet('residence', '') });
            if (STATE.benefitType) chips.push({ label: STATE.benefitType, clear: () => setFacet('benefitType', '') });
            if (STATE.occupation) chips.push({ label: STATE.occupation, clear: () => setFacet('occupation', '') });
            if (STATE.employmentStatus) chips.push({ label: STATE.employmentStatus, clear: () => setFacet('employmentStatus', '') });
            if (STATE.maritalStatus) chips.push({ label: STATE.maritalStatus, clear: () => setFacet('maritalStatus', '') });
            if (STATE.disabilityPercentage !== '') chips.push({ label: `ಅಂಗವೈಕಲ್ಯ ${STATE.disabilityPercentage}%+`, clear: () => setFacet('disabilityPercentage', '') });
            if (STATE.applicationMode) chips.push({ label: STATE.applicationMode, clear: () => setFacet('applicationMode', '') });
            if (STATE.ministry) chips.push({ label: STATE.ministry, clear: () => setFacet('ministry', '') });

            wrap.innerHTML = '';
            chips.forEach(c => {
                const btn = document.createElement('button');
                btn.type = 'button';
                btn.className = 'active-chip';
                btn.innerHTML = `<span>${escapeHtml(c.label)}</span><span>✕</span>`;
                btn.onclick = c.clear;
                wrap.appendChild(btn);
            });
        }

        /* Extract 2-3 clean bullet points for card display */
        function extractCardPoints(s) {
            const pts = [];
            const rawDesc = CURRENT_LANG === 'kn' ? (s.description_kn || s.description_en || '') : (s.description_en || s.description_kn || '');
            const benText = CURRENT_LANG === 'kn' ? (s.benefits_kn || '') : (s.benefits_en || '');

            if (benText && benText !== rawDesc) {
                pts.push(benText);
            }
            const sentences = rawDesc
                .split(/(?<=[.।])\s+/)
                .map(x => x.trim())
                .filter(x => x.length > 12);

            for (const sen of sentences) {
                if (pts.length >= 2) break;
                if (!pts.includes(sen)) pts.push(sen);
            }
            if (pts.length === 0 && rawDesc) pts.push(rawDesc);

            // Add concise eligibility summary point
            const eligParts = [];
            const g = (s.genders || []).filter(x => x !== 'All');
            if (g.length) eligParts.push(g.includes('Female') ? 'ಮಹಿಳೆಯರಿಗೆ' : g.join('/'));
            const c = (s.castes || []).filter(x => x !== 'All');
            if (c.length) eligParts.push(c.map(x => x.replace(/.*\((.*)\)/, '$1')).join('/'));
            if (s.isBpl) eligParts.push('BPL ಕಾರ್ಡ್');
            if (s.isStudent) eligParts.push('ವಿದ್ಯಾರ್ಥಿಗಳಿಗೆ');
            const modes = (s.applicationModes || []).join('/');
            if (modes) eligParts.push(`ಅರ್ಜಿ: ${modes}`);

            if (eligParts.length > 0 && pts.length < 3) {
                pts.push(`ಅರ್ಹತೆ & ವಿಧಾನ: ${eligParts.join(' • ')}`);
            }
            return pts.slice(0, 3);
        }

        function renderSchemesPage() {
            const grid = document.getElementById('schemes-grid');
            grid.className = VIEW_MODE === 'list' ? 'schemes-grid list-view' : 'schemes-grid';

            if (FILTERED_SCHEMES.length === 0) {
                grid.innerHTML = `<div style="grid-column:1/-1; background:#fff; border:1px solid #e2e8f0; border-radius:16px; padding:42px 20px; text-align:center;">
                    <div style="font-size:2.2rem; margin-bottom:8px;">🔍</div>
                    <h3 style="margin:0 0 6px; font-size:1.1rem;">ಯಾವುದೇ ಯೋಜನೆಗಳು ಕಂಡುಬಂದಿಲ್ಲ (No matching schemes)</h3>
                    <p style="margin:0 0 14px; color:#64748b; font-size:0.9rem;">ಫಿಲ್ಟರ್‌ಗಳನ್ನು ಬದಲಾಯಿಸಿ ಅಥವಾ ಎಲ್ಲಾ ಫಿಲ್ಟರ್ ಮರುಹೊಂದಿಸಿ.</p>
                    <button type="button" class="btn-primary-action" onclick="resetAllFilters()">ಎಲ್ಲಾ 885 ಯೋಜನೆಗಳನ್ನು ತೋರಿಸಿ (Reset Filters)</button>
                </div>`;
                document.getElementById('pagination-bar').innerHTML = '';
                return;
            }

            const totalPages = Math.ceil(FILTERED_SCHEMES.length / PAGE_SIZE);
            if (CURRENT_PAGE > totalPages) CURRENT_PAGE = 1;

            const start = (CURRENT_PAGE - 1) * PAGE_SIZE;
            const slice = FILTERED_SCHEMES.slice(start, start + PAGE_SIZE);

            grid.innerHTML = slice.map(s => renderCardHTML(s)).join('');
            renderPagination(totalPages);
        }

        function renderCardHTML(s) {
            const isState = s.level === 'State';
            const isGuar = !!s.is_guarantee;
            const cardClass = isGuar ? 'scheme-card guarantee-card' : (isState ? 'scheme-card state-card' : 'scheme-card');

            const primaryTitle = CURRENT_LANG === 'kn' ? (s.name_kn || s.name_en) : (s.name_en || s.name_kn);
            const secondaryTitle = CURRENT_LANG === 'kn'
                ? (s.name_en && s.name_en !== s.name_kn ? s.name_en : '')
                : (s.name_kn && s.name_kn !== s.name_en ? s.name_kn : '');

            const ministry = CURRENT_LANG === 'kn' ? (s.ministry_kn || s.ministry_en) : (s.ministry_en || s.ministry_kn);
            const tags = (CURRENT_LANG === 'kn' ? (s.tags_kn && s.tags_kn.length ? s.tags_kn : s.tags_en) : (s.tags_en || [])).slice(0, 4);
            const bType = (s.benefitTypes && s.benefitTypes[0]) || '';
            const points = extractCardPoints(s);

            return `<article class="${cardClass}">
                <div>
                    <div class="card-top">
                        <div class="badge-group">
                            <span class="lvl-badge ${isState ? 'state' : 'central'}">${isState ? (CURRENT_LANG === 'kn' ? '🏛️ ಕರ್ನಾಟಕ ರಾಜ್ಯ' : '🏛️ Karnataka State') : (CURRENT_LANG === 'kn' ? '🇮🇳 ಕೇಂದ್ರ ಸರ್ಕಾರ' : '🇮🇳 Central Govt')}</span>
                            ${isGuar ? `<span class="guar-badge">⭐ ಪಂಚ ಗ್ಯಾರಂಟಿ</span>` : ''}
                            ${s.dbtScheme ? `<span class="dbt-badge">⚡ DBT</span>` : ''}
                            ${bType ? `<span class="btype-badge">${escapeHtml(bType)}</span>` : ''}
                        </div>
                    </div>
                    <div class="ministry-line">🏢 ${escapeHtml(ministry)}</div>
                    <h3 class="scheme-title-primary" onclick="openSchemeDrawer('${escapeAttr(s.slug)}')">${escapeHtml(primaryTitle)}</h3>
                    ${secondaryTitle ? `<div class="scheme-title-secondary">${escapeHtml(secondaryTitle)}</div>` : ''}
                    <ul class="card-points">
                        ${points.map(pt => `<li>${escapeHtml(pt)}</li>`).join('')}
                    </ul>
                </div>
                <div>
                    ${tags.length ? `<div class="tag-row">${tags.map(t => `<span class="tag-pill" onclick="filterByTag('${escapeAttr(t)}')">${escapeHtml(t)}</span>`).join('')}</div>` : ''}
                    <div class="card-footer">
                        <button type="button" class="btn-card-elig" onclick="openEligibilityChecker('${escapeAttr(s.slug)}')">
                            ✅ ${CURRENT_LANG === 'kn' ? 'ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ' : 'Check Eligibility'}
                        </button>
                        <button type="button" class="btn-card-details" onclick="openSchemeDrawer('${escapeAttr(s.slug)}')">
                            📋 ${CURRENT_LANG === 'kn' ? 'ಪೂರ್ಣ ವಿವರ & ಅರ್ಜಿ →' : 'Full Points & Apply →'}
                        </button>
                    </div>
                </div>
            </article>`;
        }

        function renderPagination(totalPages) {
            const bar = document.getElementById('pagination-bar');
            if (totalPages <= 1) {
                bar.innerHTML = '';
                return;
            }
            let html = `<button type="button" class="page-btn" ${CURRENT_PAGE === 1 ? 'disabled' : ''} onclick="goToPage(${CURRENT_PAGE - 1})">← ಹಿಂದೆ</button>`;
            const pages = [];
            for (let p = 1; p <= totalPages; p++) {
                if (p === 1 || p === totalPages || Math.abs(p - CURRENT_PAGE) <= 2) {
                    pages.push(p);
                } else if (pages[pages.length - 1] !== '...') {
                    pages.push('...');
                }
            }
            pages.forEach(p => {
                if (p === '...') {
                    html += `<span style="padding:0 6px; color:#64748b; font-weight:700;">…</span>`;
                } else {
                    html += `<button type="button" class="page-btn ${p === CURRENT_PAGE ? 'active' : ''}" onclick="goToPage(${p})">${p}</button>`;
                }
            });
            html += `<button type="button" class="page-btn" ${CURRENT_PAGE === totalPages ? 'disabled' : ''} onclick="goToPage(${CURRENT_PAGE + 1})">ಮುಂದೆ →</button>`;
            bar.innerHTML = html;
        }

        function goToPage(p) {
            CURRENT_PAGE = p;
            renderSchemesPage();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        /* PERSONA QUICK MATCHER */
        function applyPersona(p) {
            if (ACTIVE_PERSONA === p) {
                ACTIVE_PERSONA = '';
                resetAllFilters();
                return;
            }
            resetAllFilters(false);
            ACTIVE_PERSONA = p;
            document.querySelectorAll('.pm-chip').forEach(c => c.classList.toggle('active', c.getAttribute('data-p') === p));

            if (p === 'woman') {
                STATE.gender = 'Female';
            } else if (p === 'farmer') {
                STATE.category = 'Agriculture,Rural & Environment';
            } else if (p === 'student') {
                STATE.isStudent = true;
                document.getElementById('tog-student').classList.add('active');
            } else if (p === 'youth') {
                STATE.employmentStatus = 'Unemployed';
            } else if (p === 'worker') {
                STATE.category = 'Skills & Employment';
            } else if (p === 'business') {
                STATE.category = 'Business & Entrepreneurship';
            } else if (p === 'senior') {
                STATE.age = '60';
            } else if (p === 'disabled') {
                STATE.disability = true;
                document.getElementById('tog-disability').classList.add('active');
            }
            applyAllFilters();
        }

        /* FILTER CONTROLS */
        function setLevelFilter(lvl) {
            STATE.level = lvl;
            document.querySelectorAll('.level-btn').forEach(b => b.classList.toggle('active', b.getAttribute('data-level') === lvl));
            applyAllFilters();
        }

        function setCategory(cat) {
            STATE.category = STATE.category === cat ? '' : cat;
            applyAllFilters();
        }

        function onSearchInput(val) {
            STATE.query = val.trim();
            document.getElementById('search-clear-btn').style.display = STATE.query ? 'inline-flex' : 'none';
            applyAllFilters();
        }

        function clearSearch() {
            document.getElementById('scheme-search').value = '';
            STATE.query = '';
            document.getElementById('search-clear-btn').style.display = 'none';
            applyAllFilters();
        }

        function filterByTag(tag) {
            document.getElementById('scheme-search').value = tag;
            onSearchInput(tag);
        }

        function toggleBoolFilter(key) {
            STATE[key] = !STATE[key];
            const mapId = {
                dbtScheme: 'tog-dbt',
                isBpl: 'tog-bpl',
                isStudent: 'tog-student',
                disability: 'tog-disability',
                minority: 'tog-minority',
                is_guarantee: 'tog-guarantee'
            };
            const el = document.getElementById(mapId[key]);
            if (el) el.classList.toggle('active', STATE[key]);
            applyAllFilters();
        }

        function setFacet(key, val) {
            STATE[key] = val;
            applyAllFilters();
        }

        function setSortOrder(val) {
            STATE.sort = val;
            applyAllFilters();
        }

        function setLang(lang) {
            CURRENT_LANG = lang;
            document.getElementById('lang-kn').classList.toggle('active', lang === 'kn');
            document.getElementById('lang-en').classList.toggle('active', lang === 'en');
            document.getElementById('lbl-tab-all').textContent = lang === 'kn' ? 'ಎಲ್ಲಾ ಯೋಜನೆಗಳು' : 'All Schemes';
            document.getElementById('lbl-tab-state').textContent = lang === 'kn' ? '🏛️ ಕರ್ನಾಟಕ ರಾಜ್ಯ' : '🏛️ State Schemes';
            document.getElementById('lbl-tab-central').textContent = lang === 'kn' ? '🇮🇳 ಕೇಂದ್ರ ಸರ್ಕಾರ' : '🇮🇳 Central Schemes';
            applyAllFilters();
        }

        function setViewMode(mode) {
            VIEW_MODE = mode;
            document.getElementById('view-grid-btn').classList.toggle('active', mode === 'grid');
            document.getElementById('view-list-btn').classList.toggle('active', mode === 'list');
            renderSchemesPage();
        }

        function resetAllFilters(reapply = true) {
            ACTIVE_PERSONA = '';
            document.querySelectorAll('.pm-chip').forEach(c => c.classList.remove('active'));
            STATE.level = 'all';
            STATE.category = '';
            STATE.query = '';
            STATE.gender = '';
            STATE.age = '';
            STATE.caste = '';
            STATE.residence = '';
            STATE.benefitType = '';
            STATE.occupation = '';
            STATE.employmentStatus = '';
            STATE.maritalStatus = '';
            STATE.disabilityPercentage = '';
            STATE.applicationMode = '';
            STATE.ministry = '';
            STATE.dbtScheme = false;
            STATE.isBpl = false;
            STATE.isStudent = false;
            STATE.disability = false;
            STATE.minority = false;
            STATE.is_guarantee = false;

            document.getElementById('scheme-search').value = '';
            document.getElementById('search-clear-btn').style.display = 'none';
            document.querySelectorAll('.level-btn').forEach(b => b.classList.toggle('active', b.getAttribute('data-level') === 'all'));
            document.querySelectorAll('.q-toggle').forEach(b => b.classList.remove('active'));
            if (reapply) applyAllFilters();
        }

        function toggleMobileFilters() {
            const dock = document.getElementById('filter-dock');
            const closeBtn = document.getElementById('close-mobile-dock');
            dock.classList.toggle('open');
            closeBtn.style.display = dock.classList.contains('open') ? 'inline-block' : 'none';
        }

        /* ==============================================================
           SLATE AST -> CLEAN STRUCTURED POINTS RENDERER
           ============================================================== */
        function renderSlateAST(nodes) {
            if (!nodes || !Array.isArray(nodes) || nodes.length === 0) return '';
            let html = '';

            for (const node of nodes) {
                if (!node) continue;
                const t = node.type;

                if (t === 'align_justify' || t === 'align_left' || t === 'align_center' || t === 'align_right') {
                    html += renderSlateAST(node.children);
                } else if (t === 'ol_list') {
                    html += `<ol class="ast-ol">${renderSlateAST(node.children)}</ol>`;
                } else if (t === 'ul_list') {
                    html += `<ul class="ast-ul">${renderSlateAST(node.children)}</ul>`;
                } else if (t === 'list_item') {
                    html += `<li>${renderSlateChildren(node.children)}</li>`;
                } else if (t === 'block_quote') {
                    const inner = renderSlateChildren(node.children).trim();
                    if (inner) html += `<div class="ast-callout">${inner}</div>`;
                } else if (t === 'table') {
                    html += `<div class="ast-table-wrap"><table class="ast-table">${renderSlateAST(node.children)}</table></div>`;
                } else if (t === 'table_row') {
                    html += `<tr>${renderSlateAST(node.children)}</tr>`;
                } else if (t === 'table_cell' || t === 'table_header_cell') {
                    const tag = t === 'table_header_cell' ? 'th' : 'td';
                    html += `<${tag}>${renderSlateChildren(node.children)}</${tag}>`;
                } else if (t === 'paragraph' || !t) {
                    const ch = node.children || [];
                    const plain = ch.map(c => c.text || '').join('').trim();
                    if (!plain) continue;

                    const isHeading = ch.length <= 2 && ch.every(c => !c.text || !c.text.trim() || c.bold || c.underline) && plain.length < 95;
                    if (isHeading) {
                        html += `<div class="ast-subheading">${escapeHtml(plain)}</div>`;
                    } else if (/^(ಹಂತ|Step)\s*\d+/i.test(plain)) {
                        html += `<div class="ast-step-card">${renderSlateChildren(ch)}</div>`;
                    } else {
                        // Split multi-sentence long paragraphs into clean bullet points!
                        const sents = plain.split(/(?<=[.।])\s+/).map(x => x.trim()).filter(x => x.length > 5);
                        if (sents.length > 1 && plain.length > 160 && !ch.some(c => c.type === 'link')) {
                            html += `<ul class="ast-ul">${sents.map(s => `<li>${escapeHtml(s)}</li>`).join('')}</ul>`;
                        } else {
                            html += `<ul class="ast-ul"><li>${renderSlateChildren(ch)}</li></ul>`;
                        }
                    }
                }
            }
            return html;
        }

        function renderSlateChildren(children) {
            if (!Array.isArray(children)) return '';
            return children.map(c => {
                if (!c) return '';
                if (c.type === 'ol_list' || c.type === 'ul_list' || c.type === 'paragraph' || c.type === 'table') {
                    return renderSlateAST([c]);
                }
                if (c.type === 'link') {
                    const label = renderSlateChildren(c.children) || 'ಅಧಿಕೃತ ಲಿಂಕ್';
                    if (c.link && c.link.startsWith('http') && !c.link.includes('myscheme.gov.in')) {
                        return ` <a href="${escapeAttr(c.link)}" target="_blank" rel="noopener" style="color:#16a34a;font-weight:800;text-decoration:underline;">${label} ↗</a> `;
                    }
                    return label;
                }
                let txt = escapeHtml(c.text || '');
                if (!txt) return '';
                if (c.bold) txt = `<strong>${txt}</strong>`;
                if (c.underline) txt = `<u>${txt}</u>`;
                if (c.italic) txt = `<em>${txt}</em>`;
                return txt;
            }).join('');
        }

        function textToPointsHTML(text) {
            if (!text) return '<p style="color:#64748b;">ಮಾಹಿತಿ ಲಭ್ಯವಿಲ್ಲ</p>';
            if (Array.isArray(text)) {
                return `<ul class="ast-ul">${text.map(t => `<li>${escapeHtml(t)}</li>`).join('')}</ul>`;
            }
            const lines = String(text)
                .replace(/\*\*/g, '')
                .split(/\n|(?<=[.।])\s+/)
                .map(x => x.replace(/^[\d\-\*\•\.]+\s*/, '').trim())
                .filter(x => x.length > 3);
            return `<ul class="ast-ul">${lines.map(l => `<li>${escapeHtml(l)}</li>`).join('')}</ul>`;
        }

        /* Fetch and cache full scheme details + documents + FAQs in Kannada */
        async function fetchFullSchemeData(slug) {
            if (SCHEME_API_CACHE[slug]) return SCHEME_API_CACHE[slug];
            const headers = { 'x-api-key': 'tYTy5eEhlu9rFjyxuCr7ra7ACp4dv1RH8gWuHTDc' };
            const result = { kn: null, en: null, docs: [], faqs: [] };

            try {
                const r = await fetch(`https://api.myscheme.gov.in/schemes/v6/public/schemes?slug=${encodeURIComponent(slug)}&lang=kn`, { headers });
                if (r.ok) {
                    const j = await r.json();
                    if (j && j.data) {
                        result.kn = j.data.kn || j.data.en || null;
                        const sid = j.data._id;
                        if (sid) {
                            const [docRes, faqRes] = await Promise.allSettled([
                                fetch(`https://api.myscheme.gov.in/schemes/v6/public/schemes/${sid}/documents?lang=kn`, { headers }),
                                fetch(`https://api.myscheme.gov.in/schemes/v6/public/schemes/${sid}/faqs?lang=kn`, { headers })
                            ]);
                            if (docRes.status === 'fulfilled' && docRes.value.ok) {
                                const dj = await docRes.value.json();
                                result.docs = dj?.data?.kn?.documents_required || dj?.data?.en?.documents_required || [];
                            }
                            if (faqRes.status === 'fulfilled' && faqRes.value.ok) {
                                const fj = await faqRes.value.json();
                                result.faqs = fj?.data?.kn?.faqs || fj?.data?.en?.faqs || [];
                            }
                        }
                    }
                }
            } catch (e) {}

            SCHEME_API_CACHE[slug] = result;
            return result;
        }

        /* ==============================================================
           OPEN WIDE 2-COLUMN STRUCTURED POINTS SCHEME VIEWER
           ============================================================== */
        async function openSchemeDrawer(slug) {
            const s = ALL_SCHEMES.find(x => x.slug === slug || x.id === slug || x.curated_id === slug);
            if (!s) return;

            const dlg = document.getElementById('scheme-drawer');
            const isState = s.level === 'State';
            document.getElementById('drawer-badges').innerHTML = `
                <span class="lvl-badge ${isState ? 'state' : 'central'}">${isState ? '🏛️ ಕರ್ನಾಟಕ ರಾಜ್ಯ ಯೋಜನೆ' : '🇮🇳 ಕೇಂದ್ರ ಸರ್ಕಾರದ ಯೋಜನೆ'}</span>
                ${s.dbtScheme ? '<span class="dbt-badge">⚡ DBT ನೇರ ನಗದು</span>' : ''}
                ${(s.benefitTypes || []).map(b => `<span class="btype-badge">${escapeHtml(b)}</span>`).join('')}
            `;

            const primaryTitle = CURRENT_LANG === 'kn' ? (s.name_kn || s.name_en) : (s.name_en || s.name_kn);
            const secondaryTitle = CURRENT_LANG === 'kn' ? s.name_en : s.name_kn;
            document.getElementById('drawer-title').textContent = primaryTitle;
            document.getElementById('drawer-subtitle').textContent = `${secondaryTitle && secondaryTitle !== primaryTitle ? secondaryTitle + ' • ' : ''}${s.ministry_kn || s.ministry_en}`;

            document.getElementById('drawer-top-elig-btn').onclick = () => openEligibilityChecker(s.slug);
            document.getElementById('drawer-side-elig-btn').onclick = () => openEligibilityChecker(s.slug);

            const body = document.getElementById('drawer-body');
            body.innerHTML = `<div style="padding:28px; text-align:center; color:#64748b; font-weight:700;">⏳ ಯೋಜನೆಯ ಸಂಪೂರ್ಣ ಪಾಯಿಂಟ್ಸ್ ಮಾಹಿತಿ ಲೋಡ್ ಆಗುತ್ತಿದೆ...</div>`;

            dlg.showModal();

            const full = await fetchFullSchemeData(s.slug);
            const kn = full.kn || {};
            const sc = kn.schemeContent || {};
            const ec = kn.eligibilityCriteria || {};
            const appProc = kn.applicationProcess || [];
            const refs = (sc.references || []).filter(r => r && r.url && r.url.startsWith('http') && !r.url.includes('myscheme.gov.in'));
            const officialSite = getOfficialSchemeWebsite(s, refs, appProc);

            // Build Details Section (Points)
            const detailsHTML = renderSlateAST(sc.detailedDescription) || textToPointsHTML(s.description_kn || s.description_en);

            // Build Benefits Section (Points)
            const benefitsHTML = renderSlateAST(sc.benefits) || textToPointsHTML(s.benefits_kn || s.benefits_en || s.description_kn);

            // Build Eligibility Section (Points)
            const eligibilityHTML = renderSlateAST(ec.eligibilityDescription) || textToPointsHTML(s.eligibility_text_kn || [
                `ವಯಸ್ಸಿನ ಮಿತಿ: ${(s.ageBrackets && s.ageBrackets.length) ? Math.min(...s.ageBrackets) + ' ರಿಂದ ' + Math.max(...s.ageBrackets) + '+ ವರ್ಷಗಳು' : 'ಎಲ್ಲಾ ವಯಸ್ಸಿನವರು'}`,
                `ಲಿಂಗ: ${(s.genders || []).filter(x => x !== 'All').join(', ') || 'ಎಲ್ಲರಿಗೂ ಅನ್ವಯ'}`,
                `ಜಾತಿ ವರ್ಗ: ${(s.castes || []).filter(x => x !== 'All').join(', ') || 'ಎಲ್ಲಾ ವರ್ಗಗಳು'}`,
                `ವಾಸಸ್ಥಳ: ${(s.residences || []).filter(x => x !== 'Both').join(', ') || 'ಗ್ರಾಮೀಣ ಮತ್ತು ನಗರ ಪ್ರದೇಶ'}`
            ]);

            // Build Exclusions Section (Points)
            const exclusionsHTML = renderSlateAST(sc.exclusions);
            document.getElementById('nav-btn-exclusions').style.display = exclusionsHTML ? 'flex' : 'none';

            // Build Application Process Section (Points)
            let processHTML = '';
            if (appProc.length > 0) {
                processHTML = appProc.map(ap => `
                    <div style="margin-bottom:12px;">
                        <span class="lvl-badge state" style="display:inline-block; margin-bottom:8px;">ವಿಧಾನ: ${escapeHtml(ap.mode || 'Online / Offline')}</span>
                        ${renderSlateAST(ap.process)}
                    </div>
                `).join('');
            } else {
                processHTML = textToPointsHTML(s.how_to_apply_kn || s.how_to_apply_en || 'ಯೋಜನೆಯ ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್ ಅಥವಾ ಸಂಬಂಧಪಟ್ಟ ಇಲಾಖೆಯ ಕಚೇರಿ ಮೂಲಕ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ.');
            }

            // Build Documents Required Section (Points)
            const docsHTML = renderSlateAST(full.docs) || textToPointsHTML(s.documents_kn || s.documents_en || [
                'ಆಧಾರ್ ಕಾರ್ಡ್ (Aadhaar Card)',
                'ಬ್ಯಾಂಕ್ ಪಾಸ್‌ಬುಕ್ / ಖಾತೆ ವಿವರ (Bank Account Details)',
                'ಜಾತಿ ಮತ್ತು ಆದಾಯ ಪ್ರಮಾಣಪತ್ರ (Caste & Income Certificate)',
                'ಪಾಸ್‌ಪೋರ್ಟ್ ಅಳತೆಯ ಭಾವಚಿತ್ರ (Passport Size Photograph)'
            ]);

            // Build FAQs Section
            let faqsHTML = '';
            if (full.faqs && full.faqs.length > 0) {
                faqsHTML = full.faqs.map(f => `
                    <div class="faq-item">
                        <div class="faq-q"><span>❓ ${escapeHtml(f.question)}</span></div>
                        <div class="faq-a">${renderSlateAST(f.answer) || escapeHtml(f.answer_md || '')}</div>
                    </div>
                `).join('');
            }
            document.getElementById('nav-btn-faqs').style.display = faqsHTML ? 'flex' : 'none';

            // Build Official Website & Guidelines Section (NO myscheme link!)
            let sourcesHTML = `<ul class="ast-ul">
                <li><strong>ಅಧಿಕೃತ ಪೋರ್ಟಲ್ (Official Scheme Website):</strong> <a href="${escapeAttr(officialSite)}" target="_blank" rel="noopener" style="color:#16a34a;font-weight:800;text-decoration:underline;">${escapeHtml(officialSite)} ↗</a></li>
                ${refs.map(r => `<li><strong>${escapeHtml(r.title || 'ಮಾರ್ಗಸೂಚಿ / ವೆಬ್‌ಸೈಟ್')}:</strong> <a href="${escapeAttr(r.url)}" target="_blank" rel="noopener" style="color:#2563eb;font-weight:700;text-decoration:underline;">${escapeHtml(r.url)} ↗</a></li>`).join('')}
            </ul>`;

            body.innerHTML = `
                <div class="pt-section" id="sec-details">
                    <h3 class="pt-sec-title">📌 ವಿವರಗಳು (Details)</h3>
                    ${detailsHTML}
                </div>
                <div class="pt-section" id="sec-benefits">
                    <h3 class="pt-sec-title">🎁 ಸೌಲಭ್ಯಗಳು (Benefits)</h3>
                    ${benefitsHTML}
                </div>
                <div class="pt-section" id="sec-eligibility">
                    <h3 class="pt-sec-title">✅ ಅರ್ಹತೆ (Eligibility)</h3>
                    ${eligibilityHTML}
                </div>
                ${exclusionsHTML ? `
                <div class="pt-section" id="sec-exclusions">
                    <h3 class="pt-sec-title">🚫 ವಿನಾಯಿತಿಗಳು (Exclusions)</h3>
                    ${exclusionsHTML}
                </div>` : ''}
                <div class="pt-section" id="sec-process">
                    <h3 class="pt-sec-title">📝 ಅರ್ಜಿ ಸಲ್ಲಿಸುವ ವಿಧಾನ (Application Process)</h3>
                    ${processHTML}
                </div>
                <div class="pt-section" id="sec-docs">
                    <h3 class="pt-sec-title">📄 ಅಗತ್ಯ ದಾಖಲೆಗಳು (Documents Required)</h3>
                    ${docsHTML}
                </div>
                ${faqsHTML ? `
                <div class="pt-section" id="sec-faqs">
                    <h3 class="pt-sec-title">❓ ಪ್ರಶ್ನೋತ್ತರಗಳು (Frequently Asked Questions)</h3>
                    ${faqsHTML}
                </div>` : ''}
                <div class="pt-section" id="sec-sources">
                    <h3 class="pt-sec-title">🌐 ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್ ಮತ್ತು ಮಾರ್ಗಸೂಚಿಗಳು (Official Website & Guidelines)</h3>
                    ${sourcesHTML}
                </div>
            `;

            document.getElementById('drawer-foot').innerHTML = `
                <button type="button" class="btn-secondary-action" onclick="openEligibilityChecker('${escapeAttr(s.slug)}')">✅ ಅರ್ಹತೆ ಪರಿಶೀಲಿಸಿ (Check Eligibility)</button>
                <div style="display:flex; gap:10px; flex-wrap:wrap;">
                    <a href="${escapeAttr(officialSite)}" target="_blank" rel="noopener" class="btn-primary-action">🌐 ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್‌ನಲ್ಲಿ ಅರ್ಜಿ ಸಲ್ಲಿಸಿ (Visit Scheme Website) ↗</a>
                </div>
            `;
        }

        function scrollToSection(secId, btn) {
            document.querySelectorAll('#drawer-nav .d-nav-link').forEach(b => b.classList.remove('active'));
            if (btn) btn.classList.add('active');
            const el = document.getElementById(secId);
            if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }

        function closeSchemeDrawer() {
            const dlg = document.getElementById('scheme-drawer');
            if (dlg && dlg.open) dlg.close();
        }

        /* ==============================================================
           5. INTERACTIVE KANNADA "CHECK ELIGIBILITY" QUESTION BUILDER
              (Generates dynamic Kannada questions with bullet points & Yes/No radios)
           ============================================================== */
        let CURRENT_ELIG_QUESTIONS = [];
        let CURRENT_ELIG_ANSWERS = {};
        let CURRENT_ELIG_SCHEME = null;
        let CURRENT_ELIG_WEBSITE = '';

        function extractPlainTextFromASTNode(node) {
            if (!node) return '';
            if (typeof node.text === 'string') return node.text;
            if (Array.isArray(node.children)) return node.children.map(extractPlainTextFromASTNode).join('');
            return '';
        }

        function buildKannadaQuestionsForScheme(s, knData) {
            const questions = [];
            const ec = (knData && knData.eligibilityCriteria) || {};
            const sc = (knData && knData.schemeContent) || {};

            // 1. Parse structured eligibility points from kn.eligibilityCriteria.eligibilityDescription
            const eligAST = ec.eligibilityDescription || [];
            function walkEligNodes(nodes) {
                if (!Array.isArray(nodes)) return;
                for (let i = 0; i < nodes.length; i++) {
                    const n = nodes[i];
                    if (!n) continue;
                    if (n.type === 'align_justify' || n.type === 'align_left') {
                        walkEligNodes(n.children);
                    } else if (n.type === 'ol_list' || n.type === 'ul_list') {
                        for (const li of (n.children || [])) {
                            const txt = extractPlainTextFromASTNode(li).trim();
                            if (txt.length > 10) {
                                // Check if this criterion is negative ("ಅರ್ಹವಾಗಿರುವುದಿಲ್ಲ" / "ಲಭ್ಯವಿಲ್ಲ")
                                const isNegative = /ಅರ್ಹವಾಗಿರುವುದಿಲ್ಲ|ಅರ್ಹರಲ್ಲ|ಲಭ್ಯವಿಲ್ಲ|ಮೀರಿರಬಾರದು/.test(txt);
                                const subPts = txt.split(/[,;]\s*/).filter(x => x.length > 4);
                                questions.push({
                                    id: 'q_' + questions.length,
                                    prompt: isNegative
                                        ? `ನಿಮ್ಮ ಅರ್ಜಿ ಅಥವಾ ಘಟಕವು ಈ ಕೆಳಗಿನ ಅನರ್ಹ ಸ್ಥಿತಿಯನ್ನು ಹೊಂದಿದೆಯೇ?`
                                        : `ನೀವು ಈ ಕೆಳಗಿನ ಅರ್ಹತಾ ನಿಯಮವನ್ನು ಪೂರೈಸುತ್ತೀರಾ?`,
                                    points: subPts.length >= 3 && txt.length > 90 ? [txt] : [txt],
                                    expected: isNegative ? 'No' : 'Yes'
                                });
                            }
                        }
                    } else if (n.type === 'paragraph') {
                        const txt = extractPlainTextFromASTNode(n).trim();
                        const nextNode = nodes[i + 1];
                        if (txt && nextNode && (nextNode.type === 'ul_list' || nextNode.type === 'ol_list')) {
                            const pts = (nextNode.children || []).map(li => extractPlainTextFromASTNode(li).trim()).filter(Boolean);
                            // Split comma-separated lists into clean bullet points!
                            let expandedPts = [];
                            pts.forEach(p => {
                                if (p.includes(',') && p.length > 60) {
                                    expandedPts.push(...p.split(/,\s*/).map(x => x.trim()).filter(Boolean));
                                } else {
                                    expandedPts.push(p);
                                }
                            });
                            if (expandedPts.length > 0) {
                                questions.push({
                                    id: 'q_' + questions.length,
                                    prompt: `${txt.replace(/[:ಃ]$/, '')} — ಇವುಗಳಲ್ಲಿ ಯಾವುದಾದರೂ ಒಂದಕ್ಕೆ ನಿಮ್ಮ ಅರ್ಜಿ ಸಂಬಂಧಿಸಿದೆಯೇ?`,
                                    points: expandedPts,
                                    expected: 'Yes'
                                });
                                i++; // Skip nextNode since we consumed it
                            }
                        }
                    }
                }
            }
            walkEligNodes(eligAST);

            // 2. Parse Exclusions from kn.schemeContent.exclusions
            const exclAST = sc.exclusions || [];
            const exclPoints = [];
            function collectExcl(nodes) {
                if (!Array.isArray(nodes)) return;
                for (const n of nodes) {
                    if (!n) continue;
                    if (n.type === 'list_item') {
                        const t = extractPlainTextFromASTNode(n).trim();
                        if (t) exclPoints.push(t);
                    } else if (n.children) {
                        collectExcl(n.children);
                    }
                }
            }
            collectExcl(exclAST);
            if (exclPoints.length > 0) {
                questions.push({
                    id: 'q_excl',
                    prompt: `ನಿಮ್ಮ ಅರ್ಜಿ ಅಥವಾ ಉದ್ಯಮವು ಈ ಕೆಳಗಿನ ಅನರ್ಹ (ವಿನಾಯಿತಿ) ಚಟುವಟಿಕೆಗಳಿಗೆ ಸಂಬಂಧಿಸಿದೆಯೇ?`,
                    points: exclPoints.slice(0, 7),
                    expected: 'No'
                });
            }

            // 3. Fallback / Supplemental Questions from Scheme Facets if AST had few questions
            if (questions.length === 0) {
                if (s.level === 'State') {
                    questions.push({
                        id: 'q_state',
                        prompt: 'ನೀವು ಕರ್ನಾಟಕ ರಾಜ್ಯದ ಖಾಯಂ ನಿವಾಸಿಯಾಗಿದ್ದೀರಾ?',
                        points: ['ಕರ್ನಾಟಕ ರಾಜ್ಯದ ಆಧಾರ್ ಕಾರ್ಡ್ / ವಾಸಸ್ಥಳ ಪ್ರಮಾಣಪತ್ರ ಹೊಂದಿರಬೇಕು'],
                        expected: 'Yes'
                    });
                }
                const g = (s.genders || []).filter(x => x !== 'All');
                if (g.length > 0) {
                    const gKn = g.includes('Female') ? 'ಮಹಿಳೆ (Female)' : (g.includes('Male') ? 'ಪುರುಷ (Male)' : 'ತೃತೀಯ ಲಿಂಗಿ');
                    questions.push({
                        id: 'q_gender',
                        prompt: `ಅರ್ಜಿದಾರರು '${gKn}' ವರ್ಗಕ್ಕೆ ಸೇರಿದವರಾಗಿದ್ದಾರೆಯೇ?`,
                        points: [],
                        expected: 'Yes'
                    });
                }
                const c = (s.castes || []).filter(x => x !== 'All');
                if (c.length > 0) {
                    questions.push({
                        id: 'q_caste',
                        prompt: 'ಅರ್ಜಿದಾರರು ಈ ಕೆಳಗಿನ ಜಾತಿ ವರ್ಗಕ್ಕೆ ಸೇರಿದ್ದಾರೆಯೇ?',
                        points: c,
                        expected: 'Yes'
                    });
                }
                if (s.isBpl) {
                    questions.push({
                        id: 'q_bpl',
                        prompt: 'ನಿಮ್ಮ ಕುಟುಂಬವು ಬಿಪಿಎಲ್ (BPL / ಅಂತ್ಯೋದಯ) ರೇಷನ್ ಕಾರ್ಡ್ ಹೊಂದಿದೆಯೇ?',
                        points: ['ಬಡತನ ರೇಖೆಗಿಂತ ಕೆಳಗಿರುವ ಕುಟುಂಬಗಳಿಗೆ ಮಾತ್ರ ಅನ್ವಯ'],
                        expected: 'Yes'
                    });
                }
                const descPts = (s.description_kn || s.description_en || '').split(/(?<=[.।])\s+/).filter(x => x.length > 10);
                if (descPts.length > 0) {
                    questions.push({
                        id: 'q_desc',
                        prompt: 'ನೀವು ಈ ಯೋಜನೆಯ ಉದ್ದೇಶಿತ ಫಲಾನುಭವಿ ಮಾನದಂಡಗಳನ್ನು ಪೂರೈಸುತ್ತೀರಾ?',
                        points: descPts,
                        expected: 'Yes'
                    });
                }
            }

            return questions.slice(0, 7);
        }

        async function openEligibilityChecker(slug) {
            const s = ALL_SCHEMES.find(x => x.slug === slug || x.id === slug || x.curated_id === slug);
            if (!s) return;

            CURRENT_ELIG_SCHEME = s;
            CURRENT_ELIG_ANSWERS = {};

            const modal = document.getElementById('elig-modal');
            document.getElementById('elig-scheme-title').textContent = s.name_kn || s.name_en;
            document.getElementById('elig-questions-container').innerHTML = `<div style="padding:20px; text-align:center; color:#64748b; font-weight:700;">⏳ ಅರ್ಹತಾ ಪ್ರಶ್ನೆಗಳನ್ನು ಸಿದ್ಧಪಡಿಸಲಾಗುತ್ತಿದೆ...</div>`;
            document.getElementById('elig-verdict-box').className = 'elig-verdict';
            modal.showModal();

            const full = await fetchFullSchemeData(s.slug);
            const kn = full.kn || {};
            const sc = kn.schemeContent || {};
            const refs = (sc.references || []).filter(r => r && r.url && r.url.startsWith('http') && !r.url.includes('myscheme.gov.in'));
            CURRENT_ELIG_WEBSITE = getOfficialSchemeWebsite(s, refs, kn.applicationProcess || []);

            CURRENT_ELIG_QUESTIONS = buildKannadaQuestionsForScheme(s, kn);
            renderEligibilityQuestions();
        }

        function renderEligibilityQuestions() {
            const container = document.getElementById('elig-questions-container');
            container.innerHTML = CURRENT_ELIG_QUESTIONS.map((q, idx) => {
                const ans = CURRENT_ELIG_ANSWERS[q.id] || '';
                return `<div class="elig-q-block">
                    <div class="elig-q-title">${idx + 1}. ${escapeHtml(q.prompt)}<span class="req-star">*</span></div>
                    ${q.points && q.points.length ? `
                        <ul class="elig-q-points">
                            ${q.points.map(pt => `<li>${escapeHtml(pt)}</li>`).join('')}
                        </ul>
                    ` : ''}
                    <div class="elig-radios">
                        <label class="elig-radio-label ${ans === 'Yes' ? 'selected-yes' : ''}">
                            <input type="radio" name="${q.id}" value="Yes" ${ans === 'Yes' ? 'checked' : ''} onchange="onEligAnswer('${q.id}', 'Yes')">
                            <span>ಹೌದು (Yes)</span>
                        </label>
                        <label class="elig-radio-label ${ans === 'No' ? 'selected-no' : ''}">
                            <input type="radio" name="${q.id}" value="No" ${ans === 'No' ? 'checked' : ''} onchange="onEligAnswer('${q.id}', 'No')">
                            <span>ಇಲ್ಲ (No)</span>
                        </label>
                    </div>
                </div>`;
            }).join('');

            updateEligibilityVerdict();
        }

        function onEligAnswer(qId, val) {
            CURRENT_ELIG_ANSWERS[qId] = val;
            renderEligibilityQuestions();
        }

        function updateEligibilityVerdict() {
            const box = document.getElementById('elig-verdict-box');
            const total = CURRENT_ELIG_QUESTIONS.length;
            const answered = Object.keys(CURRENT_ELIG_ANSWERS).length;

            // Check if any answered question failed immediately
            const failedQ = CURRENT_ELIG_QUESTIONS.find(q => CURRENT_ELIG_ANSWERS[q.id] && CURRENT_ELIG_ANSWERS[q.id] !== q.expected);
            if (failedQ) {
                box.className = 'elig-verdict fail';
                box.innerHTML = `
                    <div style="font-size:1.08rem; font-weight:800; margin-bottom:6px;">❌ ಕ್ಷಮಿಸಿ, ನೀವು ಈ ಯೋಜನೆಗೆ ಅರ್ಹರಾಗಿಲ್ಲ (Not Eligible)</div>
                    <div style="font-size:0.9rem;">ಮೇಲಿನ ಅರ್ಹತಾ ನಿಯಮಗಳ ಪ್ರಕಾರ ("${escapeHtml(failedQ.prompt)}") ನಿಮ್ಮ ಆಯ್ಕೆಯು ಯೋಜನೆಯ ಮಾನದಂಡಕ್ಕೆ ಹೊಂದಿಕೆಯಾಗುತ್ತಿಲ್ಲ.</div>
                `;
                return;
            }

            if (answered < total) {
                box.className = 'elig-verdict pending';
                box.innerHTML = `<div style="font-size:0.92rem; font-weight:700;">👆 ನಿಮ್ಮ ಅರ್ಹತೆಯನ್ನು ತಿಳಿಯಲು ಮೇಲಿನ ಎಲ್ಲಾ <strong>${total}</strong> ಪ್ರಶ್ನೆಗಳಿಗೆ <strong>ಹೌದು / ಇಲ್ಲ</strong> ಆಯ್ಕೆ ಮಾಡಿ. (${answered}/${total} ಉತ್ತರಿಸಲಾಗಿದೆ)</div>`;
                return;
            }

            box.className = 'elig-verdict pass';
            box.innerHTML = `
                <div style="font-size:1.15rem; font-weight:800; margin-bottom:8px;">🎉 ಅಭಿನಂದನೆಗಳು! ನೀವು ಈ ಯೋಜನೆಗೆ ಅರ್ಹರಾಗಿದ್ದೀರಿ (You are Eligible!)</div>
                <div style="font-size:0.92rem; margin-bottom:14px;">ನೀವು ಎಲ್ಲಾ ಅರ್ಹತಾ ಮಾನದಂಡಗಳನ್ನು ಪೂರೈಸಿದ್ದೀರಿ. ಕೆಳಗಿನ ಅಧಿಕೃತ ವೆಬ್‌ಸೈಟ್ ಮೂಲಕ ಅರ್ಜಿ ಸಲ್ಲಿಸಬಹುದು:</div>
                <div style="display:flex; gap:10px; flex-wrap:wrap;">
                    <a href="${escapeAttr(CURRENT_ELIG_WEBSITE)}" target="_blank" rel="noopener" class="btn-primary-action">🌐 ಅಧಿಕೃತ ಯೋಜನೆಯ ವೆಬ್‌ಸೈಟ್ ತೆರೆಯಿರಿ ↗</a>
                    <button type="button" class="btn-secondary-action" onclick="closeEligModal(); openSchemeDrawer('${escapeAttr(CURRENT_ELIG_SCHEME.slug)}')">📋 ಪೂರ್ಣ ವಿವರ ಮತ್ತು ದಾಖಲೆಗಳನ್ನು ನೋಡಿ</button>
                </div>
            `;
        }

        function closeEligModal() {
            const modal = document.getElementById('elig-modal');
            if (modal && modal.open) modal.close();
        }

        function escapeHtml(str) {
            return String(str || '')
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;');
        }

        function escapeAttr(str) {
            return String(str || '').replace(/'/g, "\\'").replace(/"/g, '&quot;');
        }

        document.addEventListener('DOMContentLoaded', initPortal);
    </script>
</body>
</html>
'''

with open("scheme-checker.html", "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print("Generated upgraded scheme-checker.html with Anek Kannada, Points Layout, Kannada Check Eligibility Questionnaire, and Official Scheme Website Links. Lines:", len(HTML_CONTENT.splitlines()))
