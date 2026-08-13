const fs = require('fs');
const path = require('path');

const rootDir = path.join(__dirname, '..');

const aboutHtml = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>About Us — Karnata.in</title>
<meta name="description" content="Learn about Karnata.in — Karnataka's premier digital portal providing live data across all 31 districts, MLAs, APMC market rates, fuel prices, and news.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/karnata-theme.css">
<style>
body { font-family: 'Outfit', sans-serif; background: #F8FAFC; color: #0F172A; margin: 0; padding: 0; }
.policy-hero { background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 100%); color: #FFF; padding: 56px 20px; text-align: center; border-bottom: 4px solid #E11D48; }
.policy-hero h1 { font-size: 38px; font-weight: 900; margin-bottom: 8px; }
.policy-wrap { max-width: 900px; margin: 40px auto 80px; padding: 0 20px; }
.policy-card { background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 18px; padding: 32px; box-shadow: 0 10px 30px rgba(0,0,0,0.04); margin-bottom: 24px; line-height: 1.8; font-size: 16px; color: #334155; }
.policy-card h2 { font-size: 22px; font-weight: 900; color: #0F172A; border-bottom: 2px solid #F1F5F9; padding-bottom: 8px; margin-top: 0; }
</style>
</head>
<body>

<div class="policy-hero">
  <h1>About Us</h1>
  <p>Karnata.in — The Digital Information Gateway for Karnataka</p>
</div>

<div class="policy-wrap">
  <div class="policy-card">
    <h2>🎯 Our Mission</h2>
    <p><strong>Karnata.in</strong> is an independent digital portal designed to empower citizens, farmers, students, and travelers with accurate, real-time public information across the state of Karnataka, India.</p>
    <p>Our objective is to deliver comprehensive data covering all 31 districts of Karnataka, including Deputy Commissioner (DC) & Superintendent of Police (SP) administration contacts, 224 Assembly Constituencies (MLA & MP data), daily agricultural APMC market prices, gold and silver bullion rates, fuel prices, dam water storage levels, and verified local news update feeds.</p>
  </div>

  <div class="policy-card">
    <h2>💡 Key Features & Services</h2>
    <ul>
      <li><strong>31 District Directories:</strong> Detailed profiles for every Karnataka district including administrative officers, taluk counts, population census, and geographical statistics.</li>
      <li><strong>Constituency & Legislative Data:</strong> Verified profiles for all 224 Karnataka MLAs and Lok Sabha MPs with historical winning margins and party affiliations.</li>
      <li><strong>Real-time APMC Agricultural Rates:</strong> Daily commodity prices for crops like Tomato, Onion, Paddy, Coconut, and Cotton across major APMC markets in Karnataka.</li>
      <li><strong>Live Market & Commodity Indicators:</strong> Accurate daily updates for 22K/24K Gold, Silver, Petrol, and Diesel rates across key Karnataka cities.</li>
      <li><strong>Hydrological & Weather Reporting:</strong> Daily water storage metrics for major dams (KRS, Almatti, Hemavathi, Supa, Kabini) and Open-Meteo weather forecasts.</li>
    </ul>
  </div>

  <div class="policy-card">
    <h2>🔒 Editorial Integrity & Quality Standard</h2>
    <p>Karnata.in is committed to maintaining high editorial and data standards. All public data feeds are aggregated from official government portals, public APMC disclosures, and reputable news feeds, ensuring accurate and objective information for our visitors.</p>
  </div>
</div>

<script src="/data-loader.js"></script>
<script src="/nav-component.js"></script>
</body>
</html>`;

const contactHtml = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Contact Us — Karnata.in</title>
<meta name="description" content="Contact the Karnata.in editorial and technical support team. Send us your feedback, inquiries, or data updates.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/karnata-theme.css">
<style>
body { font-family: 'Outfit', sans-serif; background: #F8FAFC; color: #0F172A; margin: 0; padding: 0; }
.policy-hero { background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 100%); color: #FFF; padding: 56px 20px; text-align: center; border-bottom: 4px solid #E11D48; }
.policy-hero h1 { font-size: 38px; font-weight: 900; margin-bottom: 8px; }
.policy-wrap { max-width: 900px; margin: 40px auto 80px; padding: 0 20px; display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
@media(max-width: 768px) { .policy-wrap { grid-template-columns: 1fr; } }
.policy-card { background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 18px; padding: 32px; box-shadow: 0 10px 30px rgba(0,0,0,0.04); font-size: 15px; color: #334155; line-height: 1.8; }
.policy-card h2 { font-size: 22px; font-weight: 900; color: #0F172A; border-bottom: 2px solid #F1F5F9; padding-bottom: 8px; margin-top: 0; }
.c-input { width: 100%; padding: 12px 16px; border: 1.5px solid #CBD5E1; border-radius: 10px; margin-bottom: 14px; font-size: 14px; font-family: inherit; box-sizing: border-box; }
.c-btn { background: #E11D48; color: #FFF; border: none; padding: 14px 24px; border-radius: 10px; font-weight: 900; font-size: 15px; cursor: pointer; width: 100%; transition: background 0.2s; }
.c-btn:hover { background: #BE123C; }
</style>
</head>
<body>

<div class="policy-hero">
  <h1>Contact Us</h1>
  <p>We'd love to hear from you. Get in touch with the Karnata.in team.</p>
</div>

<div class="policy-wrap">
  <div class="policy-card">
    <h2>📍 Office & Contact Info</h2>
    <p>🌐 <strong>Website:</strong> https://karnata.in</p>
    <p>📧 <strong>Email Support:</strong> contact@karnata.in</p>
    <p>🏢 <strong>Location:</strong> Bengaluru, Karnataka, India — 560001</p>
    <p>⏰ <strong>Operating Hours:</strong> Monday – Saturday (9:00 AM – 6:00 PM IST)</p>
  </div>

  <div class="policy-card">
    <h2>✉️ Send Us a Message</h2>
    <form onsubmit="alert('Thank you! Your message has been received.'); return false;">
      <input type="text" class="c-input" placeholder="Your Name" required>
      <input type="email" class="c-input" placeholder="Your Email Address" required>
      <textarea class="c-input" rows="4" placeholder="Your message or feedback..." required></textarea>
      <button type="submit" class="c-btn">Send Message</button>
    </form>
  </div>
</div>

<script src="/data-loader.js"></script>
<script src="/nav-component.js"></script>
</body>
</html>`;

const privacyHtml = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Privacy Policy — Karnata.in</title>
<meta name="description" content="Official Privacy Policy for Karnata.in detailing user privacy, cookies policy, and Google AdSense compliance.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/karnata-theme.css">
<style>
body { font-family: 'Outfit', sans-serif; background: #F8FAFC; color: #0F172A; margin: 0; padding: 0; }
.policy-hero { background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 100%); color: #FFF; padding: 56px 20px; text-align: center; border-bottom: 4px solid #E11D48; }
.policy-hero h1 { font-size: 38px; font-weight: 900; margin-bottom: 8px; }
.policy-wrap { max-width: 900px; margin: 40px auto 80px; padding: 0 20px; }
.policy-card { background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 18px; padding: 32px; box-shadow: 0 10px 30px rgba(0,0,0,0.04); margin-bottom: 24px; line-height: 1.8; font-size: 15px; color: #334155; }
.policy-card h2 { font-size: 22px; font-weight: 900; color: #0F172A; border-bottom: 2px solid #F1F5F9; padding-bottom: 8px; margin-top: 0; }
</style>
</head>
<body>

<div class="policy-hero">
  <h1>Privacy Policy</h1>
  <p>Your privacy is important to us at Karnata.in</p>
</div>

<div class="policy-wrap">
  <div class="policy-card">
    <h2>🔒 Privacy Policy Overview</h2>
    <p>At <strong>Karnata.in</strong>, accessible from https://karnata.in, one of our main priorities is the privacy of our visitors. This Privacy Policy document outlines the types of information collected and recorded by Karnata.in and how we use it.</p>
  </div>

  <div class="policy-card">
    <h2>🍪 Google AdSense & Third-Party Cookies Policy</h2>
    <p>Karnata.in partners with Google AdSense to display third-party advertisements.</p>
    <ul>
      <li>Google, as a third-party vendor, uses cookies to serve ads on Karnata.in based on users' prior visits to our website or other websites on the Internet.</li>
      <li>Google's use of advertising cookies enables it and its partners to serve ads to our users based on their visit to Karnata.in and/or other sites on the Internet.</li>
      <li>Users may opt out of personalized advertising by visiting <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ads Settings</a>.</li>
    </ul>
  </div>

  <div class="policy-card">
    <h2>📊 Log Files & Analytics</h2>
    <p>Karnata.in follows a standard procedure of using log files. These files log visitors when they visit websites. The information collected by log files includes internet protocol (IP) addresses, browser type, Internet Service Provider (ISP), date and time stamp, referring/exit pages, and possibly the number of clicks. These are not linked to any information that is personally identifiable.</p>
  </div>

  <div class="policy-card">
    <h2>🛡️ Children's Information</h2>
    <p>Another part of our priority is adding protection for children while using the internet. We encourage parents and guardians to observe, participate in, and/or monitor and guide their online activity. Karnata.in does not knowingly collect any Personal Identifiable Information from children under the age of 13.</p>
  </div>
</div>

<script src="/data-loader.js"></script>
<script src="/nav-component.js"></script>
</body>
</html>`;

const termsHtml = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Terms and Conditions — Karnata.in</title>
<meta name="description" content="Terms and Conditions for using Karnata.in services, data disclaimers, and intellectual property.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/karnata-theme.css">
<style>
body { font-family: 'Outfit', sans-serif; background: #F8FAFC; color: #0F172A; margin: 0; padding: 0; }
.policy-hero { background: linear-gradient(135deg, #0F172A 0%, #1E1B4B 100%); color: #FFF; padding: 56px 20px; text-align: center; border-bottom: 4px solid #E11D48; }
.policy-hero h1 { font-size: 38px; font-weight: 900; margin-bottom: 8px; }
.policy-wrap { max-width: 900px; margin: 40px auto 80px; padding: 0 20px; }
.policy-card { background: #FFF; border: 1.5px solid #E2E8F0; border-radius: 18px; padding: 32px; box-shadow: 0 10px 30px rgba(0,0,0,0.04); margin-bottom: 24px; line-height: 1.8; font-size: 15px; color: #334155; }
.policy-card h2 { font-size: 22px; font-weight: 900; color: #0F172A; border-bottom: 2px solid #F1F5F9; padding-bottom: 8px; margin-top: 0; }
</style>
</head>
<body>

<div class="policy-hero">
  <h1>Terms and Conditions</h1>
  <p>Terms of Service & Public Data Disclaimer for Karnata.in</p>
</div>

<div class="policy-wrap">
  <div class="policy-card">
    <h2>📜 Terms of Service</h2>
    <p>By accessing and using <strong>Karnata.in</strong>, you accept and agree to be bound by the terms and provision of this agreement. If you do not agree to abide by these terms, please do not use this site.</p>
  </div>

  <div class="policy-card">
    <h2>⚠️ Market Data Disclaimer</h2>
    <p>Agricultural APMC prices, bullion rates, fuel prices, and hydrological storage metrics displayed on Karnata.in are aggregated from publicly accessible government reports and market data feeds. While we strive to present accurate data, market prices fluctuate rapidly. Visitors are advised to re-verify prices with local authorities or market boards before entering into commercial transactions.</p>
  </div>

  <div class="policy-card">
    <h2>©️ Intellectual Property</h2>
    <p>All content, branding, design elements, and underlying codebase of Karnata.in are protected under intellectual property laws. Unauthorized reproduction of proprietary site components without prior written consent is strictly prohibited.</p>
  </div>
</div>

<script src="/data-loader.js"></script>
<script src="/nav-component.js"></script>
</body>
</html>`;

fs.writeFileSync(path.join(rootDir, 'about.html'), aboutHtml, 'utf8');
fs.writeFileSync(path.join(rootDir, 'contact.html'), contactHtml, 'utf8');
fs.writeFileSync(path.join(rootDir, 'privacy-policy.html'), privacyHtml, 'utf8');
fs.writeFileSync(path.join(rootDir, 'terms.html'), termsHtml, 'utf8');

console.log('Successfully generated English AdSense Policy Pages: about.html, contact.html, privacy-policy.html, terms.html!');
