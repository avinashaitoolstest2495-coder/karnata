# -*- coding: utf-8 -*-
"""
Script to update bbk13-data.js to real-time Week 8 (Day 53) state.
"""
import re

DATA_PATH = "bbk13-data.js"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Update header fields
content = re.sub(r'currentDay:\s*\d+,', 'currentDay: 53,', content)
content = re.sub(r'totalPassengers:\s*\d+,', 'totalPassengers: 14,', content)

# Update C01 (Jagadish)
c01_old = r'("id":\s*"C01",[\s\S]*?"personality":\s*"[^"]*",\s*)"status":\s*"CAPTAIN",\s*"statusKn":\s*"[^"]*",\s*"captaincyStatus":\s*"ACTIVE_CAPTAIN",\s*"nominationStatus":\s*false,\s*"eliminated":\s*false,'
c01_new = r'\1"status": "SAFE",\n    "statusKn": "ಸುರಕ್ಷಿತ (🟢 SAFE)",\n    "captaincyStatus": "PASSENGER",\n    "nominationStatus": false,\n    "eliminated": false,'
content = re.sub(c01_old, c01_new, content)

# Update C02 (Soundarya Shetty)
c02_old = r'("id":\s*"C02",[\s\S]*?"personality":\s*"[^"]*",\s*)"status":\s*"NOMINATED",\s*"statusKn":\s*"[^"]*",\s*"captaincyStatus":\s*"PASSENGER",\s*"nominationStatus":\s*false,\s*"eliminated":\s*false,'
c02_new = r'\1"status": "CAPTAIN",\n    "statusKn": "ಕ್ಯಾಪ್ಟನ್ (👑 CAPTAIN)",\n    "captaincyStatus": "ACTIVE_CAPTAIN",\n    "nominationStatus": false,\n    "eliminated": false,'
content = re.sub(c02_old, c02_new, content)

# Update C05 (Gagan Chinnappa - Nominated)
c05_old = r'("id":\s*"C05",[\s\S]*?"personality":\s*"[^"]*",\s*)"status":\s*"SAFE",\s*"statusKn":\s*"[^"]*",\s*"captaincyStatus":\s*"PASSENGER",\s*"nominationStatus":\s*false,\s*"eliminated":\s*false,'
c05_new = r'\1"status": "NOMINATED",\n    "statusKn": "ನಾಮಿನೇಟೆಡ್ (🔴 NOMINATED)",\n    "captaincyStatus": "PASSENGER",\n    "nominationStatus": true,\n    "eliminated": false,'
content = re.sub(c05_old, c05_new, content)

# Update C06 (Sangeetha Bhat - Nominated, ensure nominationStatus is true)
c06_old = r'("id":\s*"C06",[\s\S]*?"status":\s*"NOMINATED",\s*"statusKn":\s*"[^"]*",\s*"captaincyStatus":\s*"PASSENGER",\s*)"nominationStatus":\s*false,'
c06_new = r'\1"nominationStatus": true,'
content = re.sub(c06_old, c06_new, content)

# Update C08 (Om Prakash Rao - Nominated, ensure nominationStatus is true)
c08_old = r'("id":\s*"C08",[\s\S]*?"status":\s*"NOMINATED",\s*"statusKn":\s*"[^"]*",\s*"captaincyStatus":\s*"PASSENGER",\s*)"nominationStatus":\s*false,'
c08_new = r'\1"nominationStatus": true,'
content = re.sub(c08_old, c08_new, content)

# Update C10 (Asiya Firdose - Nominated)
c10_old = r'("id":\s*"C10",[\s\S]*?"personality":\s*"[^"]*",\s*)"status":\s*"SAFE",\s*"statusKn":\s*"[^"]*",\s*"captaincyStatus":\s*"PASSENGER",\s*"nominationStatus":\s*false,\s*"eliminated":\s*false,'
c10_new = r'\1"status": "NOMINATED",\n    "statusKn": "ನಾಮಿನೇಟೆಡ್ (🔴 NOMINATED)",\n    "captaincyStatus": "PASSENGER",\n    "nominationStatus": true,\n    "eliminated": false,'
content = re.sub(c10_old, c10_new, content)

# Update C12 (Tandav Ram - Nominated)
c12_old = r'("id":\s*"C12",[\s\S]*?"personality":\s*"[^"]*",\s*)"status":\s*"SAFE",\s*"statusKn":\s*"[^"]*",\s*"captaincyStatus":\s*"PASSENGER",\s*"nominationStatus":\s*false,\s*"eliminated":\s*false,'
c12_new = r'\1"status": "NOMINATED",\n    "statusKn": "ನಾಮಿನೇಟೆಡ್ (🔴 NOMINATED)",\n    "captaincyStatus": "PASSENGER",\n    "nominationStatus": true,\n    "eliminated": false,'
content = re.sub(c12_old, c12_new, content)

# Update C14 (Dhanush Manjunath - Nominated)
c14_old = r'("id":\s*"C14",[\s\S]*?"personality":\s*"[^"]*",\s*)"status":\s*"SAFE",\s*"statusKn":\s*"[^"]*",\s*"captaincyStatus":\s*"PASSENGER",\s*"nominationStatus":\s*false,\s*"eliminated":\s*false,'
c14_new = r'\1"status": "NOMINATED",\n    "statusKn": "ನಾಮಿನೇಟೆಡ್ (🔴 NOMINATED)",\n    "captaincyStatus": "PASSENGER",\n    "nominationStatus": true,\n    "eliminated": false,'
content = re.sub(c14_old, c14_new, content)

# Update C16 (Modern Mahakavi Manja - Red Card Evicted)
c16_old = r'("id":\s*"C16",[\s\S]*?"personality":\s*"[^"]*",\s*)"status":\s*"SAFE",\s*"statusKn":\s*"[^"]*",\s*"captaincyStatus":\s*"PASSENGER",\s*"nominationStatus":\s*false,\s*"eliminated":\s*false,'
c16_new = r'\1"status": "ELIMINATED",\n    "statusKn": "ರೆಡ್ ಕಾರ್ಡ್ ಎಲಿಮಿನೇಟೆಡ್ (🔴 RED CARD EVICTED)",\n    "captaincyStatus": "PASSENGER",\n    "nominationStatus": false,\n    "eliminated": true,\n    "eliminationReason": "ರೂಲ್ಸ್ ಉಲ್ಲಂಘನೆ & ರೆಡ್ ಕಾರ್ಡ್ (Direct Red Card Ejection by Kiccha Sudeep)",'
content = re.sub(c16_old, c16_new, content)

# Update atcEvents
new_atc = '''  // Air Traffic Control (Events)
  atcEvents: [
    {
      id: "ATC01",
      category: "👑 CHIEF CAPTAIN",
      headline: "ಮ್ಯೂಸಿಯಂ ಟಾಸ್ಕ್ ಗೆದ್ದು 8ನೇ ವಾರದ ನಾಯಕಿಯಾದ ಸೌಂದರ್ಯ ಶೆಟ್ಟಿ!",
      time: "ವಾರ 08 ಲೈವ್",
      contestant: "ಸೌಂದರ್ಯ ಶೆಟ್ಟಿ (B01)",
      desc: "ರೋಚಕ ‘ಮ್ಯೂಸಿಯಂ ಕಳ್ಳತನ’ ಚಾಲೆಂಜ್‌ನಲ್ಲಿ ಜಯಗಳಿಸಿ ದೊಡ್ಮನೆಯ 8ನೇ ವಾರದ ಚೀಫ್ ಕ್ಯಾಪ್ಟನ್ ಆಗಿ ಅಧಿಕಾರ ಸ್ವೀಕಾರ.",
      badgeColor: "#F59E0B"
    },
    {
      id: "ATC02",
      category: "🚨 RED CARD EJECTION",
      headline: "ಮಾಡ್ರನ್ ಮಹಾಕವಿ ಮಂಜಗೆ ಕಿಚ್ಚ ಸುದೀಪ್ ನೇರ ರೆಡ್ ಕಾರ್ಡ್!",
      time: "ವಾರ 08 ಬ್ರೇಕಿಂಗ್",
      contestant: "ಮಾಡ್ರನ್ ಮಹಾಕವಿ ಮಂಜ (B08)",
      desc: "ದೊಡ್ಡಮನೆಯ ನಿಯಮಗಳ ಗಂಭೀರ ಉಲ್ಲಂಘನೆ ಹಾಗೂ ಯಶಸ್ ಕೃಷ್ಣ ವಿರುದ್ಧ ಅನುಚಿತ ವರ್ತನೆಗೆ ಸುದೀಪ್ ಖಡಕ್ ನಿರ್ಧಾರ - ತಕ್ಷಣವೇ ದೊಡ್ಮನೆಯಿಂದ ಗೇಟ್ ಪಾಸ್.",
      badgeColor: "#EF4444"
    },
    {
      id: "ATC03",
      category: "🔴 DANGER ZONE",
      headline: "ವಾರ 08 ರ ಡೇಂಜರ್ ಝೋನ್‌ನಲ್ಲಿ 6 ಸ್ಪರ್ಧಿಗಳು ನಾಮಿನೇಟ್!",
      time: "ಇಂದು ಲೈವ್",
      contestant: "ತಾಂಡವ್, ಆಸಿಯಾ, ಗಗನ್, ಧನುಷ್, ಓಂಪ್ರಕಾಶ್, ಸಂಗೀತ",
      desc: "ಎಲಿಮಿನೇಷನ್ ಭೀತಿಯಲ್ಲಿರುವ ಆರು ಸ್ಪರ್ಧಿಗಳು. ಈ ವಾರಾಂತ್ಯದಲ್ಲಿ ಯಾರ ಜರ್ನಿ ಕೊನೆಗೊಳ್ಳಲಿದೆ?",
      badgeColor: "#F97316"
    },
    {
      id: "ATC04",
      category: "🎤 PANCHAYAT ALERT",
      headline: "₹2.5 ಲಕ್ಷ ಬೆಲೆಯ ಮೈಕ್ ಡ್ಯಾಮೇಜ್ ಪ್ರಕರಣಕ್ಕೆ ಕಿಚ್ಚ ಸುದೀಪ್ ಖಡಕ್ ಎಚ್ಚರಿಕೆ!",
      time: "ವಾರಾಂತ್ಯ ಪಂಚಾಯ್ತಿ",
      contestant: "ಕಿಚ್ಚ ಸುದೀಪ್",
      desc: "ದೊಡ್ಡಮನೆಯ ಆಸ್ತಿ ಹಾನಿ ಮಾಡಿದ ಸ್ಪರ್ಧಿಗಳಿಗೆ ಸುದೀಪ್ ಕಠಿಣ ವಾರ್ನಿಂಗ್, ನಿಯಮ ಪಾಲಿಸದಿದ್ದರೆ ಕಠಿಣ ಕ್ರಮದ ಎಚ್ಚರಿಕೆ.",
      badgeColor: "#10B981"
    }
  ],'''

content = re.sub(r'  // Air Traffic Control \(Events\)[\s\S]*?atcEvents:\s*\[[\s\S]*?\],\n', new_atc + '\n', content)

with open(DATA_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("bbk13-data.js updated successfully!")
