# Karnata — Karnata.in
## Universe Of Karnataka · ಕನ್ನಡಿಗರ ಸಂಪೂರ್ಣ ಮಾಹಿತಿ ಕೇಂದ್ರ

> Live data · Civic info · Tools · News · All in Kannada

---

## 📂 Project Structure

```
namma-karnataka/
├── index.html              ← Homepage (notifications, geolocation, weather)
├── gold-rate.html          ← Live gold & silver rates
├── dam-levels.html         ← Karnataka dam water levels
├── civic-finder.html       ← MLA / MP / DC / SP / GP finder
├── emi-calculator.html     ← EMI + loan calculator (affiliate)
├── more-tools.html         ← Petrol · SIP · APMC · Scheme checker
├── kannada-typing.html     ← English → Kannada typing tool
├── status-checker.html     ← DL · RTC · Sakala · PAN · Voter ID
├── news-explainers.html    ← Kannada news in simple language
├── data-loader.js          ← Connects HTML pages to live JSON data
├── manifest.json           ← PWA manifest (install as app)
├── sw.js                   ← Service Worker (offline + push)
├── sitemap.xml             ← Google SEO sitemap
├── robots.txt              ← Search engine crawl rules
├── data/                   ← JSON data files (populated by scrapers)
│   ├── gold_rates.json
│   ├── petrol_rates.json
│   ├── dam_levels.json
│   ├── apmc_prices.json
│   └── weather.json
└── scraper/                ← Python scrapers
    ├── main.py             ← Master scheduler
    ├── gold_scraper.py     ← Gold & silver rates
    ├── petrol_scraper.py   ← Petrol & diesel prices
    ├── dam_scraper.py      ← Dam water levels (KSNDMC)
    ├── apmc_scraper.py     ← APMC crop prices (agmarknet)
    ├── weather_scraper.py  ← Weather (Open-Meteo + IMD)
    ├── utils.py            ← Shared utilities
    ├── generate_mock_data.py ← Test data generator
    ├── cloudflare_worker.js ← Serverless scraper (Cloudflare)
    ├── wrangler.toml       ← Cloudflare deployment config
    └── requirements.txt    ← Python dependencies
```

---

## 🚀 STEP 1 — Local Testing (5 minutes)

```bash
# 1. Go to scraper folder
cd scraper

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Generate test data
python generate_mock_data.py

# 4. Open in browser
# Double-click index.html OR:
cd ..
python -m http.server 8080
# Open: http://localhost:8080
```

---

## 🌐 STEP 2 — Deploy to Cloudflare Pages (Free Hosting)

### 2a. Get a domain
- Go to **godaddy.com** or **namecheap.com**
- Search: `karnata.in` (≈ ₹699/year)
- Alternatives: `kannadatools.in` · `karnatakainfo.in` · `nammaka.in`

### 2b. Deploy to Cloudflare Pages
```
1. Go to: pages.cloudflare.com
2. Click "Create a project"
3. Choose "Direct Upload"
4. Upload your entire project folder
   (include: all .html, data-loader.js, manifest.json, sw.js, sitemap.xml, robots.txt, data/ folder)
5. Project name: namma-karnataka
6. Click Deploy
```

### 2c. Connect your domain
```
Cloudflare Dashboard → Pages → namma-karnataka → Custom domains
→ Add domain → karnata.in
→ Update nameservers at your domain registrar to Cloudflare
```

**Result:** Your site is live at https://karnata.in — FREE, with global CDN!

---

## ⏰ STEP 3 — Automate Live Data (Two Options)

### Option A: Cloudflare Workers (Recommended — Serverless)

```bash
# Install Wrangler CLI
npm install -g wrangler

# Login to Cloudflare
wrangler login

# Create KV namespace for data storage
wrangler kv:namespace create NK_DATA
# Copy the ID from output → paste into wrangler.toml

# Set Telegram alert (optional)
wrangler secret put TELEGRAM_BOT_TOKEN
wrangler secret put TELEGRAM_CHAT_ID

# Deploy the worker
cd scraper
wrangler deploy

# Test it
curl https://karnata-scraper.YOUR_SUBDOMAIN.workers.dev/api/health
curl https://karnata-scraper.YOUR_SUBDOMAIN.workers.dev/api/gold
```

**Cron Schedule (automatic):**
| Time (IST) | What runs |
|------------|-----------|
| 6:00 AM | Petrol & Diesel prices |
| 7:00 AM | Gold & Silver rates |
| 8:00 AM | Dam water levels |
| 9:30 AM | APMC crop prices |
| Every hour | Weather update |

**Cost: FREE** (Cloudflare Workers free tier = 100k requests/day)

---

### Option B: Python on VPS / Railway (If you prefer Python)

```bash
# On a cheap VPS (₹200/month on DigitalOcean/Hetzner) or Railway.app:

# Clone your project
git clone YOUR_REPO

# Setup
cd scraper
pip install -r requirements.txt
cp .env.example .env
# Fill in .env with your Cloudflare KV credentials

# Run once to test
python main.py once

# Run as daemon (stays running, auto-schedules)
python main.py daemon

# Or add to Linux cron (crontab -e):
30 0 * * * cd /path/to/scraper && python main.py petrol
30 1 * * * cd /path/to/scraper && python main.py gold
30 2 * * * cd /path/to/scraper && python main.py dam
0  4 * * * cd /path/to/scraper && python main.py apmc
*/30 * * * * cd /path/to/scraper && python main.py weather
```

---

## 🔍 STEP 4 — Google Search Console Setup

```
1. Go to: search.google.com/search-console
2. Add property → Domain → karnata.in
3. Verify domain (add TXT record in Cloudflare DNS)
4. Sitemaps → Add → https://karnata.in/sitemap.xml
5. URL Inspection → Request indexing for each important page
```

**Priority pages to submit first:**
- `/live/gold-rate-today` — "today gold rate Karnataka" (50k+ monthly searches)
- `/live/dam-levels` — "KRS dam level today" (viral during monsoon)
- `/civic/who-is-my-mla` — "who is my MLA Karnataka" (zero competition)
- `/tools/emi-calculator` — "EMI calculator Kannada" (high CPC)

---

## 💰 STEP 5 — Monetization (Week 1)

### Google AdSense
```
1. adsense.google.com/start
2. Add site: karnata.in
3. Paste AdSense code in <head> of all HTML files
4. Approval: 3-7 days
5. Finance tool pages = ₹20-40 RPM (high CPC)
```

### Affiliate Links (Instant Revenue — No Approval Needed)
Add these links to tool pages immediately:

| Page | Affiliate | Earnings |
|------|-----------|----------|
| EMI Calculator | HDFC Bank · SBI · Bajaj | ₹500-2000/lead |
| SIP Calculator | Groww · Zerodha | ₹500-1500/signup |
| Gold Rate | Muthoot · Manappuram | ₹300-800/lead |
| Insurance tools | PolicyBazaar | ₹800-3000/lead |

```
Groww Partner: groww.in/partner
Zerodha: zerodha.com/partners
PolicyBazaar: policybazaar.com/affiliates
```

### Push Notifications (OneSignal — Free)
```
1. onesignal.com → Create Web App
2. Get App ID + Safari Web ID
3. Add to index.html (replace sw.js with OneSignal SW)
4. Send daily: gold price, dam alert, petrol price
5. Subscribers = returning traffic = more ad revenue
```

---

## 📊 STEP 6 — Connect Live Data to HTML Pages

Add this ONE line to each HTML file `<head>`:
```html
<script src="/data-loader.js"></script>
```

The `data-loader.js` automatically:
- Detects which page you're on
- Loads the right JSON from `/data/` folder
- Updates all price/level displays
- Auto-refreshes every 5-30 minutes

### Data flow:
```
Python Scraper (daily)
    ↓ writes
/data/gold_rates.json
    ↓ served by
Cloudflare Pages CDN
    ↓ fetched by
data-loader.js (in browser)
    ↓ updates
HTML elements (live display)
```

---

## 📝 STEP 7.5 — Content Management (Articles & Images)

A lightweight CMS lives in `/cms` — write and publish articles with
images through a web UI, no code changes or redeploys needed per
article. Full setup: **[cms/README.md](cms/README.md)**.

## 🔔 STEP 7 — Push Notification Types

Already built in `sw.js` and `index.html`:

| Trigger | Notification |
|---------|-------------|
| Gold ↑ > ₹100 | "ಚಿನ್ನ ಬೆಲೆ ₹100 ಹೆಚ್ಚಾಗಿದೆ" |
| Dam > 95% | "🚨 KRS ಅಣೆಕಟ್ಟು ಅಪಾಯ ಮಟ್ಟಕ್ಕೆ ತಲುಪಿದೆ" |
| Rain > 80% | "🌧️ ನಿಮ್ಮ ಪ್ರದೇಶದಲ್ಲಿ ಭಾರೀ ಮಳೆ ಸಾಧ್ಯತೆ" |
| Petrol changes | "⛽ ಇಂದಿನಿಂದ ಪೆಟ್ರೋಲ್ ಬೆಲೆ ₹X" |
| New scheme | "📋 ಹೊಸ ಯೋಜನೆ: ನೀವು ಅರ್ಹರೇ?" |

---

## 📱 STEP 8 — Android App (Phase 2)

Convert this PWA to Android app using TWA (Trusted Web Activity):
```bash
# Install Bubblewrap CLI
npm install -g @bubblewrap/cli

# Initialize TWA project
bubblewrap init --manifest https://karnata.in/manifest.json

# Build APK
bubblewrap build

# Sign and upload to Google Play Store
# Cost: $25 one-time registration
```

---

## 📈 Expected Traffic Growth

| Month | Daily Users | Revenue |
|-------|-------------|---------|
| Month 1 | 200-500 | ₹2,000-5,000 |
| Month 2 | 1,000-3,000 | ₹8,000-20,000 |
| Month 3 | 5,000-15,000 | ₹30,000-80,000 |
| Month 6 | 20,000-50,000 | ₹1,00,000+ |

**Key traffic drivers:**
- Dam levels during monsoon (June-October) = viral sharing
- Gold rate pages = daily returning users
- Civic finder = WhatsApp viral potential
- APMC prices = farmer communities (daily use)

---

## 🛠️ Remaining Modules to Build (Phase 2)

- [ ] Salary / take-home calculator
- [ ] Weather full page (district-wise)
- [ ] 30 district pages (massive SEO)
- [ ] Kannada calendar / panchanga
- [ ] AI news auto-publisher (connect Gemini pipeline)
- [ ] BMI + health calculator
- [ ] Land area converter (guntha, acre)
- [ ] RTC pahani search integration
- [ ] Court case status checker

---

## 📞 Data Sources

| Data | Source | API/Scrape | Cost |
|------|--------|------------|------|
| Gold rate | ibjarates.com / GoodReturns | Scrape | Free |
| Petrol price | PriceOfPetrol.in / IOCL | Scrape | Free |
| Dam levels | ksndmc.gov.in | Scrape | Free |
| APMC prices | agmarknet.gov.in | Open data | Free |
| Weather | api.open-meteo.com | REST API | Free |
| MLA/MP data | Lok Dhaba (ECI) | Open API | Free |
| Voter roll | electoralsearch.eci.gov.in | Link | Free |
| RTC/Pahani | landrecords.karnataka.gov.in | Link | Free |

---

## 🆘 Troubleshooting

**Q: HTML pages not showing live data?**
- Check `data/` folder has JSON files
- Run `python generate_mock_data.py` first
- Make sure `data-loader.js` is in same folder

**Q: Scraper not running?**
- Check `.env` file has correct credentials
- Run `python main.py test` for quick test
- Check `scraper.log` for errors

**Q: AdSense rejected?**
- Need 15-20 pages of original content
- Add 3-4 informational articles about Karnataka
- Wait 7 days after site launch before applying

**Q: Google not indexing pages?**
- Submit sitemap in Search Console
- Use URL Inspection tool → Request indexing
- Make sure robots.txt allows crawling

---

Built with ❤️ for ಕನ್ನಡ · Karnataka · ಕರ್ನಾಟ
#   k a r n a t a  
 