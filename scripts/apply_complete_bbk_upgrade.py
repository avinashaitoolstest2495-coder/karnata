# -*- coding: utf-8 -*-
"""
apply_complete_bbk_upgrade.py
Comprehensive real-time upgrade for BBK13:
1. Complete Roster (19 contestants: 10 Active + 9 Eliminated/Ejected)
2. Real Wildcard Entries (Hanumantha Lamani, Rajath Kishan, Shobha Shetty)
3. Full Week-by-Week Elimination Ledger (Weeks 1 to 8)
4. Dedicated UI Sections:
   - Wildcard Express Suite
   - Elimination Ledger & Eviction Timeline
   - 6-Way Filter Tabs (All, Active, Wildcard, Nominated, Safe, Eliminated)
   - Enhanced Card Designs (Wildcard, Evicted, Captain, Danger Zone)
"""

import json
import re
import os

# ==========================================
# 1. DEFINE COMPLETE 19-CONTESTANT ROSTER
# ==========================================
CONTESTANTS_DATA = [
  {
    "id": "C01",
    "seat": "A01",
    "name": "Jagadish alias Jagga Mummy",
    "kannadaName": "ಜಗದೀಶ್ ಅಲಿಯಾಸ್ ಜಗ್ಗ ಮಮ್ಮಿ",
    "photo": "/assets/bbk13/contestants/passenger_01_face.jpg",
    "profession": "ಕಲಾವಿದ & ‘ಲವ್ ಮಾಕ್ಟೇಲ್ 3’ ಜಗ್ಗ ಮಮ್ಮಿ ಖ್ಯಾತಿ",
    "city": "ಮಂಡ್ಯ (ಶೂಟಿಂಗ್ ಮಹಾದೇವಪುರ)",
    "age": 36,
    "bio": "ಡಾರ್ಲಿಂಗ್ ಕೃಷ್ಣ ನಿರ್ದೇಶಿಸಿ ನಟಿಸಿರುವ ‘ಲವ್ ಮಾಕ್ಟೇಲ್ 3’ ಚಿತ್ರದಲ್ಲಿ ‘ಜಗ್ಗ ಮಮ್ಮಿ’ ಪಾತ್ರ ಮಾಡಿ ಪ್ರೇಕ್ಷಕರ ಮೆಚ್ಚುಗೆ ಗಳಿಸಿದ ಜಗದೀಶ್, ಮೂಲತಃ ಮಂಡ್ಯ ಜಿಲ್ಲೆಯವರು. ಅಪ್ಪಟ ಮುಗ್ಧತೆ, ಗ್ರಾಮೀಣ ಸೊಗಡಿನ ಮಾತುಗಾರಿಕೆ ಹಾಗೂ ನೈಜ ಕಾಮಿಡಿ ಟೈಮಿಂಗ್‌ನಿಂದ ಇಡೀ ದೊಡ್ಡಮನೆಯಲ್ಲಿ ನಗೆಯ ಅಲೆ ಎಬ್ಬಿಸಿದ್ದಾರೆ.",
    "winProbability": 95,
    "personality": "ಅಪ್ಪಟ ಮುಗ್ಧ ಮನರಂಜಕ (Pure Entertainer)",
    "status": "SAFE",
    "statusKn": "ಸುರಕ್ಷಿತ (🟢 SAFE)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": False,
    "eliminated": False,
    "isWildcard": False,
    "entryDate": "Day 01",
    "scores": { "popularity": 98, "strategy": 82, "entertainment": 99, "emotion": 90, "leadership": 86, "drama": 84 },
    "baggage": { "drama": 84, "fun": 99, "emotion": 90, "strategy": 82, "anger": 40, "leadership": 86 },
    "stats": { "taskWins": 3, "nominations": 1, "survivalDays": 53, "fanVotes": 89200, "xp": 4200 },
    "cardRarity": "LEGENDARY"
  },
  {
    "id": "C02",
    "seat": "B01",
    "name": "Soundarya Shetty",
    "kannadaName": "ಸೌಂದರ್ಯ ಶೆಟ್ಟಿ",
    "photo": "/assets/bbk13/contestants/passenger_02_face.jpg",
    "profession": "ಗ್ಲಾಮರಸ್ ಮಾಡೆಲ್ & ಸ್ಪ್ಲಿಟ್ಸ್ವಿಲ್ಲಾ 16 ಫೈನಲಿಸ್ಟ್",
    "city": "ಮಂಗಳೂರು (ಮಸ್ಕಟ್)",
    "age": 27,
    "bio": "ಮೂಲತಃ ಮಂಗಳೂರಿನವರಾಗಿದ್ದು ಮಸ್ಕಟ್‌ನಲ್ಲಿ ಬೆಳೆದ ಸೌಂದರ್ಯ, ರಿಯಾಲಿಟಿ ಶೋಗಳ ನುರಿತ ಆಟಗಾರ್ತಿ. ರೋಚಕ ‘ಮ್ಯೂಸಿಯಂ ಕಳ್ಳತನ’ ಟಾಸ್ಕ್‌ನಲ್ಲಿ ಗೆದ್ದು 8ನೇ ವಾರದ ಚೀಫ್ ಕ್ಯಾಪ್ಟನ್ ಆಗಿ ಅಧಿಕಾರ ಹಿಡಿದಿದ್ದು, ಈ ವಾರ ಇಮ್ಯೂನಿಟಿ ಸುರಕ್ಷೆ ಹೊಂದಿದ್ದಾರೆ.",
    "winProbability": 92,
    "personality": "ಬೋಲ್ಡ್ & ಚೀಫ್ ಕ್ಯಾಪ್ಟನ್ (Bold Captain)",
    "status": "CAPTAIN",
    "statusKn": "ಕ್ಯಾಪ್ಟನ್ (👑 CAPTAIN)",
    "captaincyStatus": "ACTIVE_CAPTAIN",
    "nominationStatus": False,
    "eliminated": False,
    "isWildcard": False,
    "entryDate": "Day 01",
    "scores": { "popularity": 94, "strategy": 95, "entertainment": 88, "emotion": 80, "leadership": 94, "drama": 92 },
    "baggage": { "drama": 92, "fun": 82, "emotion": 80, "strategy": 95, "anger": 72, "leadership": 94 },
    "stats": { "taskWins": 5, "nominations": 2, "survivalDays": 53, "fanVotes": 81400, "xp": 4600 },
    "cardRarity": "EPIC"
  },
  {
    "id": "C03",
    "seat": "A02",
    "name": "Avinash Shatamarshana",
    "kannadaName": "ಅವಿನಾಶ್ ಶಟಮರ್ಷನ",
    "photo": "/assets/bbk13/contestants/passenger_03_face.jpg",
    "profession": "ರಂಗಭೂಮಿ & ಚಲನಚಿತ್ರ ನಟ",
    "city": "ಬೆಂಗಳೂರು",
    "age": 34,
    "bio": "ರಂಗಭೂಮಿ ಹಾಗೂ ಸಿನಿಮಾ ನಟರಾದ ಅವಿನಾಶ್, ದೊಡ್ಮನೆಯಲ್ಲಿ ಶಾಂತಿಯುತ ಆಟ ಪ್ರದರ್ಶಿಸಿ 3ನೇ ವಾರದಲ್ಲಿ ಸಾರ್ವಜನಿಕ ವೋಟಿಂಗ್ ಕೊರತೆಯಿಂದ ಎಲಿಮಿನೇಟ್ ಆದರು.",
    "winProbability": 30,
    "personality": "ಶಾಂತ ಕಲಾವಿದ (Calm Actor)",
    "status": "ELIMINATED",
    "statusKn": "ವಾರ 03 ಎಲಿಮಿನೇಟೆಡ್ (🔴 EVICTED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": False,
    "eliminated": True,
    "isWildcard": False,
    "evictedWeek": "Week 03 (Day 21)",
    "eliminationReason": "3ನೇ ವಾರದ ನಾಮಿನೇಷನ್‌ನಲ್ಲಿ ಕಡಿಮೆ ಸಾರ್ವಜನಿಕ ಮತಗಳು",
    "entryDate": "Day 01",
    "scores": { "popularity": 72, "strategy": 68, "entertainment": 70, "emotion": 78, "leadership": 65, "drama": 50 },
    "baggage": { "drama": 50, "fun": 70, "emotion": 78, "strategy": 68, "anger": 45, "leadership": 65 },
    "stats": { "taskWins": 1, "nominations": 2, "survivalDays": 21, "fanVotes": 18200, "xp": 1400 },
    "cardRarity": "COMMON"
  },
  {
    "id": "C04",
    "seat": "B02",
    "name": "Prathama Prasad",
    "kannadaName": "ಪ್ರಥಮಾ ಪ್ರಸಾದ್",
    "photo": "/assets/bbk13/contestants/passenger_04_face.jpg",
    "profession": "ಶಾಸ್ತ್ರೀಯ ನೃತ್ಯಗಾರ್ತಿ & ನಟಿ",
    "city": "ಬೆಂಗಳೂರು",
    "age": 32,
    "bio": "ಹಿರಿಯ ನಟಿ ವಿನಯಾ ಪ್ರಸಾದ್ ಅವರ ಪುತ್ರಿ ಪ್ರಥಮಾ ಪ್ರಸಾದ್ ಶಾಸ್ತ್ರೀಯ ನೃತ್ಯಗಾರ್ತಿ. ಮೊದಲ ವಾರವೇ ನಿರ್ಗಮನ ಪಟ್ಟಿಗೆ ಬಂದು ಅತ್ಯಂತ ಕಡಿಮೆ ಮತಗಳಿಂದ ಮೊದಲ ಎಲಿಮಿನೇಷನ್ ಕಂಡರು.",
    "winProbability": 20,
    "personality": "ಶಾಸ್ತ್ರೀಯ ನೃತ್ಯ ಪ್ರತಿಭೆ (Graceful Dancer)",
    "status": "ELIMINATED",
    "statusKn": "ವಾರ 01 ಎಲಿಮಿನೇಟೆಡ್ (🔴 EVICTED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": False,
    "eliminated": True,
    "isWildcard": False,
    "evictedWeek": "Week 01 (Day 07)",
    "eliminationReason": "1ನೇ ವಾರದ ಸಾರ್ವಜನಿಕ ವೋಟಿಂಗ್‌ನಲ್ಲಿ ಕೊನೆಯ ಸ್ಥಾನ",
    "entryDate": "Day 01",
    "scores": { "popularity": 65, "strategy": 55, "entertainment": 60, "emotion": 85, "leadership": 60, "drama": 45 },
    "baggage": { "drama": 45, "fun": 60, "emotion": 85, "strategy": 55, "anger": 35, "leadership": 60 },
    "stats": { "taskWins": 0, "nominations": 1, "survivalDays": 7, "fanVotes": 9800, "xp": 800 },
    "cardRarity": "COMMON"
  },
  {
    "id": "C05",
    "seat": "A03",
    "name": "Gagan Chinnappa",
    "kannadaName": "ಗಗನ್ ಚಿನ್ನಪ್ಪ",
    "photo": "/assets/bbk13/contestants/passenger_05_face.jpg",
    "profession": "ಕಿರುತೆರೆ ನಟ & 'ಮಂಗಳ ಗೌರಿ ಮದುವೆ' ಖ್ಯಾತಿ",
    "city": "ಕೊಡಗು (ಮಡಿಕೇರಿ)",
    "age": 31,
    "bio": "‘ಮಂಗಳ ಗೌರಿ ಮದುವೆ’ ಧಾರಾವಾಹಿಯ ನಾಯಕ ಗಗನ್ ಚಿನ್ನಪ್ಪ, ದೃಢ ಕಾಯ ಮತ್ತು ಆಕರ್ಷಕ ವ್ಯಕ್ತಿತ್ವದ ನಟ. 8ನೇ ವಾರದ ಕ್ಯಾಪ್ಟನ್ಸಿ ರೂಲ್ಸ್ ವಿಚಾರದಲ್ಲಿ ಸೌಂದರ್ಯ ಶೆಟ್ಟಿ ವಿರುದ್ಧ ಸಿಡಿದೆದ್ದು ನೇರ ನಾಮಿನೇಷನ್ ವಲಯದಲ್ಲಿದ್ದಾರೆ.",
    "winProbability": 88,
    "personality": "ಫಿಯರ್‌ಲೆಸ್ ಹಂಕ್ (Fearless Fighter)",
    "status": "NOMINATED",
    "statusKn": "ನಾಮಿನೇಟೆಡ್ (🔴 NOMINATED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": True,
    "eliminated": False,
    "isWildcard": False,
    "entryDate": "Day 01",
    "scores": { "popularity": 92, "strategy": 89, "entertainment": 84, "emotion": 80, "leadership": 90, "drama": 88 },
    "baggage": { "drama": 88, "fun": 80, "emotion": 80, "strategy": 89, "anger": 85, "leadership": 90 },
    "stats": { "taskWins": 4, "nominations": 3, "survivalDays": 53, "fanVotes": 76500, "xp": 3900 },
    "cardRarity": "EPIC"
  },
  {
    "id": "C06",
    "seat": "B03",
    "name": "Sangeetha Bhat",
    "kannadaName": "ಸಂಗೀತ ಭಟ್",
    "photo": "/assets/bbk13/contestants/passenger_06_face.jpg",
    "profession": "ಖ್ಯಾತ ಚಲನಚಿತ್ರ ನಟಿ",
    "city": "ಮಂಗಳೂರು",
    "age": 31,
    "bio": "ಕನ್ನಡ ಚಿತ್ರರಂಗದ ಖ್ಯಾತ ನಟಿ ಸಂಗೀತ ಭಟ್, ದೊಡ್ಮನೆಯಲ್ಲಿ ತಮ್ಮ ಬುದ್ಧಿವಂತ ನಡೆ ಮತ್ತು ಸಂಯಮದ ಆಟದಿಂದ ಮುನ್ನಡೆದಿದ್ದಾರೆ. 8ನೇ ವಾರದ ಡೇಂಜರ್ ಝೋನ್‌ನಲ್ಲಿ ನಾಮಿನೇಟ್ ಆಗಿದ್ದಾರೆ.",
    "winProbability": 85,
    "personality": "ಇಂಟೆಲಿಜೆಂಟ್ ಸ್ಟ್ರಾಟಜಿಸ್ಟ್ (Intelligent Player)",
    "status": "NOMINATED",
    "statusKn": "ನಾಮಿನೇಟೆಡ್ (🔴 NOMINATED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": True,
    "eliminated": False,
    "isWildcard": False,
    "entryDate": "Day 01",
    "scores": { "popularity": 89, "strategy": 91, "entertainment": 82, "emotion": 84, "leadership": 82, "drama": 78 },
    "baggage": { "drama": 78, "fun": 80, "emotion": 84, "strategy": 91, "anger": 65, "leadership": 82 },
    "stats": { "taskWins": 3, "nominations": 4, "survivalDays": 53, "fanVotes": 68400, "xp": 3700 },
    "cardRarity": "RARE"
  },
  {
    "id": "C07",
    "seat": "A04",
    "name": "Kavya Gowda",
    "kannadaName": "ಕಾವ್ಯ ಗೌಡ",
    "photo": "/assets/bbk13/contestants/passenger_07_face.jpg",
    "profession": "ಕಿರುತೆರೆ ನಟಿ & ಗ್ಲಾಮರಸ್ ಇನ್‌ಫ್ಲುಯೆನ್ಸರ್",
    "city": "ಬೆಂಗಳೂರು",
    "age": 28,
    "bio": "ಕಿರುತೆರೆಯ ನಟಿ ಹಾಗೂ ಮಾಡೆಲ್ ಕಾವ್ಯ ಗೌಡ, ದೊಡ್ಡಮನೆಯಲ್ಲಿ 4 ವಾರಗಳ ಕಾಲ ಸಕ್ರಿಯವಾಗಿ ಆಡಿ 4ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್‌ನಲ್ಲಿ ಹೊರಬಿದ್ದರು.",
    "winProbability": 35,
    "personality": "ಸ್ಟೈಲಿಶ್ ಡಿವಾ (Stylish Diva)",
    "status": "ELIMINATED",
    "statusKn": "ವಾರ 04 ಎಲಿಮಿನೇಟೆಡ್ (🔴 EVICTED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": False,
    "eliminated": True,
    "isWildcard": False,
    "evictedWeek": "Week 04 (Day 28)",
    "eliminationReason": "4ನೇ ವಾರದ ಡೇಂಜರ್ ಝೋನ್‌ನಲ್ಲಿ ಕಡಿಮೆ ಮತಗಳು",
    "entryDate": "Day 01",
    "scores": { "popularity": 74, "strategy": 65, "entertainment": 72, "emotion": 82, "leadership": 68, "drama": 76 },
    "baggage": { "drama": 76, "fun": 72, "emotion": 82, "strategy": 65, "anger": 60, "leadership": 68 },
    "stats": { "taskWins": 1, "nominations": 3, "survivalDays": 28, "fanVotes": 24500, "xp": 1800 },
    "cardRarity": "COMMON"
  },
  {
    "id": "C08",
    "seat": "B04",
    "name": "Om Prakash Rao",
    "kannadaName": "ಎನ್. ಓಂಪ್ರಕಾಶ್ ರಾವ್",
    "photo": "/assets/bbk13/contestants/passenger_08_face.jpg",
    "profession": "ಖ್ಯಾತ ಚಲನಚಿತ್ರ ನಿರ್ದೇಶಕ & ನಟ",
    "city": "ಬೆಂಗಳೂರು",
    "age": 58,
    "bio": "ಕನ್ನಡದ ಖ್ಯಾತ ನಿರ್ದೇಶಕ ಓಂಪ್ರಕಾಶ್ ರಾವ್, ನೇರ ನುಡಿ ಹಾಗೂ ಖಡಕ್ ಸ್ವಭಾವಕ್ಕೆ ಹೆಸರಾದವರು. ಮನೆಯೊಳಗೆ ಅಧಿಕಾರಯುತ ಮಾತುಗಳಿಂದ ಚರ್ಚೆಯಾಗಿದ್ದು, 8ನೇ ವಾರದ ನಾಮಿನೇಷನ್ ಪಟ್ಟಿಯಲ್ಲಿದ್ದಾರೆ.",
    "winProbability": 76,
    "personality": "ಖಡಕ್ ನಿರ್ದೇಶಕ (Bold Mastermind)",
    "status": "NOMINATED",
    "statusKn": "ನಾಮಿನೇಟೆಡ್ (🔴 NOMINATED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": True,
    "eliminated": False,
    "isWildcard": False,
    "entryDate": "Day 01",
    "scores": { "popularity": 86, "strategy": 88, "entertainment": 85, "emotion": 76, "leadership": 89, "drama": 94 },
    "baggage": { "drama": 94, "fun": 76, "emotion": 76, "strategy": 88, "anger": 92, "leadership": 89 },
    "stats": { "taskWins": 2, "nominations": 5, "survivalDays": 53, "fanVotes": 59100, "xp": 3400 },
    "cardRarity": "RARE"
  },
  {
    "id": "C09",
    "seat": "A05",
    "name": "Kiran Shastri",
    "kannadaName": "ಕಿರಣ್ ಶಾಸ್ತ್ರಿ",
    "photo": "/assets/bbk13/contestants/passenger_09_face.jpg",
    "profession": "ಖ್ಯಾತ ಜ್ಯೋತಿಷಿ & ಆಧ್ಯಾತ್ಮಿಕ ವಾಗ್ಮಿ",
    "city": "ಮೈಸೂರು",
    "age": 42,
    "bio": "ಜ್ಯೋತಿಷಿ ಕಿರಣ್ ಶಾಸ್ತ್ರಿ ದೊಡ್ಡಮನೆಯ ಮೊದಲ 2 ವಾರಗಳಲ್ಲಿ ಭವಿಷ್ಯ ಹಾಗೂ ಪೂಜೆ-ಪುನಸ್ಕಾರಗಳ ಮೂಲಕ ಗಮನ ಸೆಳೆದು 2ನೇ ವಾರದಲ್ಲಿ ಎಲಿಮಿನೇಟ್ ಆದರು.",
    "winProbability": 25,
    "personality": "ಆಧ್ಯಾತ್ಮಿಕ ಪಂಡಿತ (Spiritual Guide)",
    "status": "ELIMINATED",
    "statusKn": "ವಾರ 02 ಎಲಿಮಿನೇಟೆಡ್ (🔴 EVICTED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": False,
    "eliminated": True,
    "isWildcard": False,
    "evictedWeek": "Week 02 (Day 14)",
    "eliminationReason": "2ನೇ ವಾರದ ಸಾರ್ವಜನಿಕ ಮತದಾನದಲ್ಲಿ ಕಡಿಮೆ ಮತಗಳು",
    "entryDate": "Day 01",
    "scores": { "popularity": 68, "strategy": 60, "entertainment": 65, "emotion": 80, "leadership": 62, "drama": 58 },
    "baggage": { "drama": 58, "fun": 65, "emotion": 80, "strategy": 60, "anger": 40, "leadership": 62 },
    "stats": { "taskWins": 0, "nominations": 2, "survivalDays": 14, "fanVotes": 14100, "xp": 1100 },
    "cardRarity": "COMMON"
  },
  {
    "id": "C10",
    "seat": "B05",
    "name": "Asiya Firdose",
    "kannadaName": "ಆಸಿಯಾ ಫಿರ್ದೋಸ್",
    "photo": "/assets/bbk13/contestants/passenger_10_face.jpg",
    "profession": "ಗಾಯಕಿ & ಇನ್‌ಫ್ಲುಯೆನ್ಸರ್",
    "city": "ಬೆಂಗಳೂರು",
    "age": 25,
    "bio": "ಮಧುರ ಕಂಠದ ಗಾಯಕಿ ಆಸಿಯಾ, ದೊಡ್ಡಮನೆಯಲ್ಲಿ ತಮ್ಮ ಇಂಪಾದ ಗಾಯನ ಹಾಗೂ ಸರಳತೆಯಿಂದ ಮೆಚ್ಚುಗೆ ಗಳಿಸಿದ್ದಾರೆ. 8ನೇ ವಾರದ ನಿರ್ಗಮನ ಪಟ್ಟಿಯಲ್ಲಿ ನಾಮಿನೇಟ್ ಆಗಿದ್ದಾರೆ.",
    "winProbability": 80,
    "personality": "ಮೆಲೋಡಿ ಕ್ವೀನ್ (Melody Voice)",
    "status": "NOMINATED",
    "statusKn": "ನಾಮಿನೇಟೆಡ್ (🔴 NOMINATED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": True,
    "eliminated": False,
    "isWildcard": False,
    "entryDate": "Day 01",
    "scores": { "popularity": 87, "strategy": 82, "entertainment": 88, "emotion": 89, "leadership": 75, "drama": 74 },
    "baggage": { "drama": 74, "fun": 85, "emotion": 89, "strategy": 82, "anger": 55, "leadership": 75 },
    "stats": { "taskWins": 2, "nominations": 3, "survivalDays": 53, "fanVotes": 62300, "xp": 3300 },
    "cardRarity": "RARE"
  },
  {
    "id": "C11",
    "seat": "A06",
    "name": "Likhith Gondi",
    "kannadaName": "ಲಿಖಿತ್ ಗೊಂಡಿ",
    "photo": "/assets/bbk13/contestants/passenger_11_face.jpg",
    "profession": "ಕಿರುತೆರೆ ನಟ ('ಅಗ್ನಿಪರೀಕ್ಷೆ' ಖ್ಯಾತಿ)",
    "city": "ಶಿವಮೊಗ್ಗ",
    "age": 28,
    "bio": "‘ಅಗ್ನಿಪರೀಕ್ಷೆ’ ಧಾರಾವಾಹಿ ಖ್ಯಾತಿಯ ನಟ ಲಿಖಿತ್ ಗೊಂಡಿ, ದೊಡ್ಮನೆಯಲ್ಲಿ 5 ವಾರಗಳ ಕಾಲ ಸ್ಪರ್ಧಿಸಿ 5ನೇ ವಾರದಲ್ಲಿ ವೋಟಿಂಗ್ ಕೊರತೆಯಿಂದ ಎಲಿಮಿನೇಟ್ ಆದರು.",
    "winProbability": 40,
    "personality": "ಟಾಸ್ಕ್ ವಾರಿಯರ್ (Task Fighter)",
    "status": "ELIMINATED",
    "statusKn": "ವಾರ 05 ಎಲಿಮಿನೇಟೆಡ್ (🔴 EVICTED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": False,
    "eliminated": True,
    "isWildcard": False,
    "evictedWeek": "Week 05 (Day 35)",
    "eliminationReason": "5ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್‌ನಲ್ಲಿ ನಿರ್ಗಮನ",
    "entryDate": "Day 01",
    "scores": { "popularity": 76, "strategy": 72, "entertainment": 74, "emotion": 78, "leadership": 76, "drama": 68 },
    "baggage": { "drama": 68, "fun": 74, "emotion": 78, "strategy": 72, "anger": 65, "leadership": 76 },
    "stats": { "taskWins": 2, "nominations": 3, "survivalDays": 35, "fanVotes": 32100, "xp": 2200 },
    "cardRarity": "COMMON"
  },
  {
    "id": "C12",
    "seat": "B06",
    "name": "Tandav Ram",
    "kannadaName": "ತಾಂಡವ್ ರಾಮ್",
    "photo": "/assets/bbk13/contestants/passenger_12_face.jpg",
    "profession": "ಬಾಡಿ ಬಿಲ್ಡರ್ & ಮಾಡೆಲ್",
    "city": "ದಾವಣಗೆರೆ",
    "age": 29,
    "bio": "ಫಿಟ್‌ನೆಸ್ ಐಕಾನ್ ಹಾಗೂ ಮಾಡೆಲ್ ತಾಂಡವ್ ರಾಮ್, ಕಠಿಣ ಫಿಸಿಕಲ್ ಟಾಸ್ಕ್‌ಗಳಲ್ಲಿ ಮಿಂಚುತ್ತಿರುವ ಆಟಗಾರ. 8ನೇ ವಾರದ ಡೇಂಜರ್ ಝೋನ್‌ನಲ್ಲಿ ನಾಮಿನೇಟ್ ಆಗಿದ್ದಾರೆ.",
    "winProbability": 82,
    "personality": "ಪವರ್ ಹೌಸ್ (Fitness Powerhouse)",
    "status": "NOMINATED",
    "statusKn": "ನಾಮಿನೇಟೆಡ್ (🔴 NOMINATED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": True,
    "eliminated": False,
    "isWildcard": False,
    "entryDate": "Day 01",
    "scores": { "popularity": 85, "strategy": 80, "entertainment": 78, "emotion": 75, "leadership": 84, "drama": 82 },
    "baggage": { "drama": 82, "fun": 75, "emotion": 75, "strategy": 80, "anger": 80, "leadership": 84 },
    "stats": { "taskWins": 4, "nominations": 3, "survivalDays": 53, "fanVotes": 58900, "xp": 3500 },
    "cardRarity": "RARE"
  },
  {
    "id": "C13",
    "seat": "A07",
    "name": "Vaishnavi",
    "kannadaName": "ವೈಷ್ಣವಿ",
    "photo": "/assets/bbk13/contestants/passenger_13_face.jpg",
    "profession": "ಡಾನ್ಸರ್ & ಕಂಟೆಂಟ್ ಕ್ರಿಯೇಟರ್",
    "city": "ಬೆಂಗಳೂರು",
    "age": 24,
    "bio": "ಡಾನ್ಸರ್ ಹಾಗೂ ಕಂಟೆಂಟ್ ಕ್ರಿಯೇಟರ್ ವೈಷ್ಣವಿ, 6 ವಾರಗಳ ಕಾಲ ದೊಡ್ಡಮನೆಯಲ್ಲಿ ರಂಜಿಸಿ 6ನೇ ವಾರದ ವೀಕೆಂಡ್‌ನಲ್ಲಿ ಎಲಿಮಿನೇಟ್ ಆದರು.",
    "winProbability": 45,
    "personality": "ಡ್ಯಾನ್ಸ್ ಕ್ರಿಯೇಟರ್ (Digital Creator)",
    "status": "ELIMINATED",
    "statusKn": "ವಾರ 06 ಎಲಿಮಿನೇಟೆಡ್ (🔴 EVICTED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": False,
    "eliminated": True,
    "isWildcard": False,
    "evictedWeek": "Week 06 (Day 42)",
    "eliminationReason": "6ನೇ ವಾರದ ಸಾರ್ವಜನಿಕ ವೋಟಿಂಗ್‌ನಲ್ಲಿ ನಿರ್ಗಮನ",
    "entryDate": "Day 01",
    "scores": { "popularity": 78, "strategy": 70, "entertainment": 80, "emotion": 84, "leadership": 70, "drama": 72 },
    "baggage": { "drama": 72, "fun": 80, "emotion": 84, "strategy": 70, "anger": 50, "leadership": 70 },
    "stats": { "taskWins": 1, "nominations": 4, "survivalDays": 42, "fanVotes": 38400, "xp": 2600 },
    "cardRarity": "COMMON"
  },
  {
    "id": "C14",
    "seat": "B07",
    "name": "Dhanush Manjunath",
    "kannadaName": "ಧನುಷ್ ಮಂಜುನಾಥ್",
    "photo": "/assets/bbk13/contestants/passenger_14_face.jpg",
    "profession": "ಗಿನ್ನೆಸ್ ವಿಶ್ವದಾಖಲೆ ಸಾಧಕ",
    "city": "ಹಾಸನ",
    "age": 27,
    "bio": "ಗಿನ್ನೆಸ್ ರೆಕಾರ್ಡ್ ಹೋಲ್ಡರ್ ಧನುಷ್ ಮಂಜುನಾಥ್, ದೊಡ್ಮನೆಯಲ್ಲಿ 7 ವಾರಗಳ ಕಾಲ ಅತ್ಯುತ್ತಮ ಫೈಟ್ ನೀಡಿ 7ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್‌ನಲ್ಲಿ ಹೊರಬಿದ್ದರು.",
    "winProbability": 50,
    "personality": "ರೆಕಾರ್ಡ್ ಹೋಲ್ಡರ್ (Guinness Champ)",
    "status": "ELIMINATED",
    "statusKn": "ವಾರ 07 ಎಲಿಮಿನೇಟೆಡ್ (🔴 EVICTED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": False,
    "eliminated": True,
    "isWildcard": False,
    "evictedWeek": "Week 07 (Day 49)",
    "eliminationReason": "7ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್‌ನಲ್ಲಿ ಸಾರ್ವಜನಿಕ ಮತಗಳ ಕೊರತೆ",
    "entryDate": "Day 01",
    "scores": { "popularity": 81, "strategy": 78, "entertainment": 75, "emotion": 79, "leadership": 80, "drama": 76 },
    "baggage": { "drama": 76, "fun": 75, "emotion": 79, "strategy": 78, "anger": 70, "leadership": 80 },
    "stats": { "taskWins": 2, "nominations": 4, "survivalDays": 49, "fanVotes": 44800, "xp": 2900 },
    "cardRarity": "COMMON"
  },
  {
    "id": "C15",
    "seat": "A08",
    "name": "Yashas Krishna",
    "kannadaName": "ಯಶಸ್ ಕೃಷ್ಣ",
    "photo": "/assets/bbk13/contestants/passenger_15_face.jpg",
    "profession": "ಕಿರುತೆರೆ ನಟ & ಮಾಡೆಲ್",
    "city": "ಬೆಂಗಳೂರು",
    "age": 29,
    "bio": "ಕಿರುತೆರೆಯ ನಟ ಯಶಸ್ ಕೃಷ್ಣ, 3ನೇ ವಾರದಲ್ಲಿ ಡಬಲ್ ಎಲಿಮಿನೇಷನ್ ಪ್ರಕ್ರಿಯೆಯಲ್ಲಿ ದೊಡ್ಮನೆಯಿಂದ ಹೊರಬಿದ್ದರು.",
    "winProbability": 32,
    "personality": "ಆಕ್ಟಿಂಗ್ ಪ್ರೊಮಿಸರ್ (Promising Talent)",
    "status": "ELIMINATED",
    "statusKn": "ವಾರ 03 ಎಲಿಮಿನೇಟೆಡ್ (🔴 EVICTED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": False,
    "eliminated": True,
    "isWildcard": False,
    "evictedWeek": "Week 03 (Day 21)",
    "eliminationReason": "3ನೇ ವಾರದ ಡಬಲ್ ಎಲಿಮಿನೇಷನ್‌ನಲ್ಲಿ ನಿರ್ಗಮನ",
    "entryDate": "Day 01",
    "scores": { "popularity": 70, "strategy": 68, "entertainment": 70, "emotion": 76, "leadership": 66, "drama": 65 },
    "baggage": { "drama": 65, "fun": 70, "emotion": 76, "strategy": 68, "anger": 60, "leadership": 66 },
    "stats": { "taskWins": 1, "nominations": 2, "survivalDays": 21, "fanVotes": 19500, "xp": 1400 },
    "cardRarity": "COMMON"
  },
  {
    "id": "C16",
    "seat": "B08",
    "name": "Modern Mahakavi Manja",
    "kannadaName": "ಮಾಡ್ರನ್ ಮಹಾಕವಿ ಮಂಜ",
    "photo": "/assets/bbk13/contestants/passenger_16_face.jpg",
    "profession": "ಕಾಮನ್ ಮ್ಯಾನ್ ಕವಿ & ಮನರಂಜಕ",
    "city": "ತುಮಕೂರು",
    "age": 33,
    "bio": "ಹಾಸ್ಯ ಕವನಗಳು ಮತ್ತು ಪ್ರಾಸದ ಮಾತುಗಳಿಂದ ಗಮನ ಸೆಳೆದಿದ್ದ ಮಹಾಕವಿ ಮಂಜ, ದೊಡ್ಮನೆಯ ನಿಯಮಗಳ ಗಂಭೀರ ಉಲ್ಲಂಘನೆ ಮತ್ತು ಅನುಚಿತ ವರ್ತನೆಗಾಗಿ ಕಿಚ್ಚ ಸುದೀಪ್ ಅವರಿಂದ ನೇರ ‘ರೆಡ್ ಕಾರ್ಡ್’ ಪಡೆದು ಶೋನಿಂದ ವಜಾಗೊಂಡಿದ್ದಾರೆ.",
    "winProbability": 10,
    "personality": "ಪ್ರಾಸ ಕವಿ (Rhyme Poet - Ejected)",
    "status": "ELIMINATED",
    "statusKn": "ವಾರ 08 ರೆಡ್ ಕಾರ್ಡ್ ಎಜೆಕ್ಷನ್ (⛔ RED CARD EJECTED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": False,
    "eliminated": True,
    "isWildcard": False,
    "evictedWeek": "Week 08 (Day 51)",
    "eliminationReason": "ದೊಡ್ಡಮನೆಯ ರೂಲ್ಸ್ ಉಲ್ಲಂಘನೆ & ಕಿಚ್ಚ ಸುದೀಪ್ ನೇರ ರೆಡ್ ಕಾರ್ಡ್ ಎಜೆಕ್ಷನ್ (Direct Red Card)",
    "entryDate": "Day 01",
    "scores": { "popularity": 75, "strategy": 50, "entertainment": 80, "emotion": 60, "leadership": 50, "drama": 98 },
    "baggage": { "drama": 98, "fun": 78, "emotion": 60, "strategy": 50, "anger": 95, "leadership": 50 },
    "stats": { "taskWins": 1, "nominations": 4, "survivalDays": 51, "fanVotes": 31200, "xp": 2400 },
    "cardRarity": "COMMON"
  },
  {
    "id": "C17",
    "seat": "W01",
    "name": "Hanumantha Lamani",
    "kannadaName": "ಹನುಮಂತ ಲಮಾಣಿ",
    "photo": "/assets/bbk13/winners/BBK_Winner_11_face.jpg",
    "profession": "ಜಾನಪದ ಕೋಗಿಲೆ & ಜನಪ್ರಿಯ ಗಾಯಕ",
    "city": "ಹಾವೇರಿ",
    "age": 28,
    "bio": "ಹಾವೇರಿ ಜಿಲ್ಲೆಯ ಜಾನಪದ ಕೋಗಿಲೆ ಹನುಮಂತ ಲಮಾಣಿ 3ನೇ ವಾರದಲ್ಲಿ ದೊಡ್ಡಮನೆಗೆ ಅದ್ಧೂರಿ ವೈಲ್ಡ್ ಕಾರ್ಡ್ ಎಂಟ್ರಿ ಕೊಟ್ಟರು. ಅಪ್ಪಟ ಮುಗ್ಧತೆ, ಮಧುರ ಹಾಡುಗಾರಿಕೆ ಹಾಗೂ ನೈಜ ಆಟದಿಂದ ಕೋಟ್ಯಂತರ ಕನ್ನಡಿಗರ ಮೆಚ್ಚಿನ ಸ್ಪರ್ಧಿಯಾಗಿದ್ದಾರೆ.",
    "winProbability": 96,
    "personality": "ಜಾನಪದ ಕೋಗಿಲೆ (Folk Legend Wildcard)",
    "status": "WILDCARD",
    "statusKn": "ವೈಲ್ಡ್ ಕಾರ್ಡ್ ಎಂಟ್ರಿ (🃏 WILDCARD)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": False,
    "eliminated": False,
    "isWildcard": True,
    "entryDate": "Day 21 (ವಾರ 03)",
    "scores": { "popularity": 99, "strategy": 84, "entertainment": 96, "emotion": 98, "leadership": 88, "drama": 70 },
    "baggage": { "drama": 70, "fun": 96, "emotion": 98, "strategy": 84, "anger": 30, "leadership": 88 },
    "stats": { "taskWins": 4, "nominations": 1, "survivalDays": 32, "fanVotes": 115000, "xp": 5100 },
    "cardRarity": "LEGENDARY"
  },
  {
    "id": "C18",
    "seat": "W02",
    "name": "Rajath Kishan",
    "kannadaName": "ರಜತ್ ಕಿಶನ್",
    "photo": "/assets/bbk13/contestants/passenger_15_face.jpg",
    "profession": "ಆ್ಯಂಕರ್ & ರಿಯಾಲಿಟಿ ಸ್ಟಾರ್",
    "city": "ಬೆಂಗಳೂರು",
    "age": 30,
    "bio": "ದೊಡ್ಡಮನೆಯ ಸ್ಪರ್ಧಿಗಳಿಗೆ ನಡುಕ ಹುಟ್ಟಿಸಲು 7ನೇ ವಾರದಲ್ಲಿ (Day 50) ಪ್ರವೇಶಿಸಿದ ವೈಲ್ಡ್ ಕಾರ್ಡ್ ಸ್ಪರ್ಧಿ ರಜತ್ ಕಿಶನ್. ಹೈ-ವೋಲ್ಟೇಜ್ ಎನರ್ಜಿ, ನೇರ ನಡೆ ಮತ್ತು ಆಕ್ರಮಣಕಾರಿ ಟಾಸ್ಕ್ ಪ್ರದರ್ಶನದಿಂದ ಮನೆಯಲ್ಲಿ ಹೊಸ ಸಮರ ಶುರುಮಾಡಿದ್ದಾರೆ.",
    "winProbability": 89,
    "personality": "ಹೈ-ವೋಲ್ಟೇಜ್ ಚಾಲೆಂಜರ್ (High-Voltage Wildcard)",
    "status": "WILDCARD",
    "statusKn": "ವೈಲ್ಡ್ ಕಾರ್ಡ್ ಎಂಟ್ರಿ (🃏 WILDCARD)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": False,
    "eliminated": False,
    "isWildcard": True,
    "entryDate": "Day 50 (ವಾರ 07)",
    "scores": { "popularity": 91, "strategy": 93, "entertainment": 89, "emotion": 78, "leadership": 91, "drama": 96 },
    "baggage": { "drama": 96, "fun": 85, "emotion": 78, "strategy": 93, "anger": 88, "leadership": 91 },
    "stats": { "taskWins": 2, "nominations": 0, "survivalDays": 4, "fanVotes": 64200, "xp": 3600 },
    "cardRarity": "EPIC"
  },
  {
    "id": "C19",
    "seat": "W03",
    "name": "Shobha Shetty",
    "kannadaName": "ಶೋಭಾ ಶೆಟ್ಟಿ",
    "photo": "/assets/bbk13/contestants/passenger_07_face.jpg",
    "profession": "ಖ್ಯಾತ ನಟಿ ('ಕಾರ್ತಿಕ ದೀಪಂ' ಖ್ಯಾತಿ)",
    "city": "ದಕ್ಷಿಣ ಕನ್ನಡ (ಮಂಗಳೂರು)",
    "age": 31,
    "bio": "‘ಕಾರ್ತಿಕ ದೀಪಂ’ ಧಾರಾವಾಹಿಯ ಜನಪ್ರಿಯ ನಟಿ ಶೋಭಾ ಶೆಟ್ಟಿ, 7ನೇ ವಾರದಲ್ಲಿ (Day 50) ದೊಡ್ಮನೆಗೆ ವೈಲ್ಡ್ ಕಾರ್ಡ್ ಪ್ರವೇಶ ನೀಡಿದ್ದಾರೆ. ಬೋಲ್ಡ್ ನಿಲುವು ಮತ್ತು ನೇರ ವಾದಗಳಿಂದ ದೊಡ್ಡಮನೆಯ ಮಹಿಳಾ ಸ್ಪರ್ಧಿಗಳಿಗೆ ಕಠಿಣ ಪೈಪೋಟಿ ನೀಡುತ್ತಿದ್ದಾರೆ.",
    "winProbability": 83,
    "personality": "ಫೈರ್ ಬ್ರಾಂಡ್ ಕ್ವೀನ್ (Firebrand Wildcard)",
    "status": "WILDCARD",
    "statusKn": "ವೈಲ್ಡ್ ಕಾರ್ಡ್ ಎಂಟ್ರಿ (🃏 WILDCARD)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": False,
    "eliminated": False,
    "isWildcard": True,
    "entryDate": "Day 50 (ವಾರ 07)",
    "scores": { "popularity": 88, "strategy": 89, "entertainment": 84, "emotion": 82, "leadership": 85, "drama": 92 },
    "baggage": { "drama": 92, "fun": 80, "emotion": 82, "strategy": 89, "anger": 84, "leadership": 85 },
    "stats": { "taskWins": 1, "nominations": 0, "survivalDays": 4, "fanVotes": 51800, "xp": 3100 },
    "cardRarity": "RARE"
  }
]

# Elimination Vault Ledger
ELIMINATION_LEDGER = [
  { "week": 1, "day": "Day 07", "id": "C04", "name": "ಪ್ರಥಮಾ ಪ್ರಸಾದ್ (Prathama Prasad)", "type": "EVICTED", "reason": "ಕಡಿಮೆ ಸಾರ್ವಜನಿಕ ಮತಗಳು (Lowest Votes)", "photo": "/assets/bbk13/contestants/passenger_04_face.jpg" },
  { "week": 2, "day": "Day 14", "id": "C09", "name": "ಕಿರಣ್ ಶಾಸ್ತ್ರಿ (Kiran Shastri)", "type": "EVICTED", "reason": "ನಾಮಿನೇಷನ್‌ನಲ್ಲಿ ಮತಗಳ ಕೊರತೆ", "photo": "/assets/bbk13/contestants/passenger_09_face.jpg" },
  { "week": 3, "day": "Day 21", "id": "C03", "name": "ಅವಿನಾಶ್ ಶಟಮರ್ಷನ (Avinash)", "type": "EVICTED", "reason": "3ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್", "photo": "/assets/bbk13/contestants/passenger_03_face.jpg" },
  { "week": 3, "day": "Day 21", "id": "C15", "name": "ಯಶಸ್ ಕೃಷ್ಣ (Yashas Krishna)", "type": "EVICTED", "reason": "ಡಬಲ್ ಎಲಿಮಿನೇಷನ್ ನಿರ್ಗಮನ", "photo": "/assets/bbk13/contestants/passenger_15_face.jpg" },
  { "week": 4, "day": "Day 28", "id": "C07", "name": "ಕಾವ್ಯ ಗೌಡ (Kavya Gowda)", "type": "EVICTED", "reason": "4ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್", "photo": "/assets/bbk13/contestants/passenger_07_face.jpg" },
  { "week": 5, "day": "Day 35", "id": "C11", "name": "ಲಿಖಿತ್ ಗೊಂಡಿ (Likhith Gondi)", "type": "EVICTED", "reason": "5ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್", "photo": "/assets/bbk13/contestants/passenger_11_face.jpg" },
  { "week": 6, "day": "Day 42", "id": "C13", "name": "ವೈಷ್ಣವಿ (Vaishnavi)", "type": "EVICTED", "reason": "6ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್", "photo": "/assets/bbk13/contestants/passenger_13_face.jpg" },
  { "week": 7, "day": "Day 49", "id": "C14", "name": "ಧನುಷ್ ಮಂಜುನಾಥ್ (Dhanush)", "type": "EVICTED", "reason": "7ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್", "photo": "/assets/bbk13/contestants/passenger_14_face.jpg" },
  { "week": 8, "day": "Day 51", "id": "C16", "name": "ಮಾಡ್ರನ್ ಮಹಾಕವಿ ಮಂಜ (Manja)", "type": "RED_CARD", "reason": "ರೂಲ್ಸ್ ಉಲ್ಲಂಘನೆ & ಕಿಚ್ಚ ಸುದೀಪ್ ನೇರ ರೆಡ್ ಕಾರ್ಡ್", "photo": "/assets/bbk13/contestants/passenger_16_face.jpg" }
]

# Wildcard Entries Ledger
WILDCARD_LEDGER = [
  { "week": 3, "day": "Day 21", "id": "C17", "name": "ಹನುಮಂತ ಲಮಾಣಿ (Hanumantha Lamani)", "role": "ಜಾನಪದ ಕೋಗಿಲೆ", "status": "ಸಕ್ರಿಯ (ಕೋಟ್ಯಂತರ ಮತಗಳು)", "photo": "/assets/bbk13/winners/BBK_Winner_11_face.jpg" },
  { "week": 7, "day": "Day 50", "id": "C18", "name": "ರಜತ್ ಕಿಶನ್ (Rajath Kishan)", "role": "ರಿಯಾಲಿಟಿ ಸ್ಟಾರ್", "status": "ಸಕ್ರಿಯ (ಹೈ-ವೋಲ್ಟೇಜ್ ಎನರ್ಜಿ)", "photo": "/assets/bbk13/contestants/passenger_15_face.jpg" },
  { "week": 7, "day": "Day 50", "id": "C19", "name": "ಶೋಭಾ ಶೆಟ್ಟಿ (Shobha Shetty)", "role": "ಖ್ಯಾತ ನಟಿ", "status": "ಸಕ್ರಿಯ (ಬೋಲ್ಡ್ ಫೈಟರ್)", "photo": "/assets/bbk13/contestants/passenger_07_face.jpg" }
]

def update_bbk13_data_file():
    with open("bbk13-data.js", "r", encoding="utf-8") as f:
        code = f.read()
    
    # Replace contestants array
    contestants_json = json.dumps(CONTESTANTS_DATA, ensure_ascii=False, indent=2)
    elim_json = json.dumps(ELIMINATION_LEDGER, ensure_ascii=False, indent=2)
    wild_json = json.dumps(WILDCARD_LEDGER, ensure_ascii=False, indent=2)
    
    # Replace contestants array inside BBK13_DATA
    code = re.sub(
        r'contestants:\s*\[[\s\S]*?\],\s*// ALL PREVIOUS SEASONS',
        f'contestants: {contestants_json},\n\n  // Elimination History Ledger\n  eliminationLedger: {elim_json},\n\n  // Wildcard Entries Ledger\n  wildcardLedger: {wild_json},\n\n  // ALL PREVIOUS SEASONS',
        code,
        count=1
    )
    
    # Update totalPassengers and currentDay
    code = re.sub(r'totalPassengers:\s*\d+,', 'totalPassengers: 10, // 10 Active (1 Captain + 1 Safe + 5 Nominated + 3 Wildcards)', code)
    code = re.sub(r'currentDay:\s*\d+,', 'currentDay: 53,', code)

    with open("bbk13-data.js", "w", encoding="utf-8") as f:
        f.write(code)
    print("[OK] bbk13-data.js updated with 19 contestants, eliminations & wildcards.")

def update_bbk13_contestants_py():
    with open("scripts/bbk13_contestants.py", "w", encoding="utf-8") as f:
        f.write('# -*- coding: utf-8 -*-\n"""\nbbk13_contestants.py - Complete Roster with Wildcards & Eliminations\n"""\n\nCONTESTANTS = [\n')
        for c in CONTESTANTS_DATA:
            status = "eliminated" if c["eliminated"] else ("wildcard" if c["isWildcard"] else ("captain" if c["status"] == "CAPTAIN" else "active"))
            cid_lower = c["id"].lower()
            photo_path = c["photo"].lstrip("/")
            search_terms = [c["name"], c["kannadaName"], "BBK13"]
            entry = {
                "id": cid_lower,
                "num": c["seat"],
                "name_kn": c["kannadaName"],
                "name_en": c["name"],
                "search_terms": search_terms,
                "photo": photo_path,
                "yt_tags": [c["name"], c["kannadaName"]],
                "status": status,
                "is_wildcard": c["isWildcard"],
                "eliminated": c["eliminated"]
            }
            f.write("    " + json.dumps(entry, ensure_ascii=False) + ",\n")
        
        # Add host
        host_entry = {
            "id": "host",
            "num": "HOST",
            "name_kn": "ಕಿಚ್ಚ ಸುದೀಪ್",
            "name_en": "Kiccha Sudeep",
            "search_terms": ["Kiccha Sudeep", "ಕಿಚ್ಚ ಸುದೀಪ್", "Sudeep BBK13"],
            "photo": "assets/bbk13/house/BBK13_SUDEEP_CHIEF.jpg",
            "yt_tags": ["Kiccha Sudeep", "ಕಿಚ್ಚ ಸುದೀಪ್"],
            "status": "host",
            "is_wildcard": False,
            "eliminated": False
        }
        f.write("    " + json.dumps(host_entry, ensure_ascii=False) + "\n]\n")
    print("[OK] scripts/bbk13_contestants.py updated with all 19 contestants.")

if __name__ == "__main__":
    update_bbk13_data_file()
    update_bbk13_contestants_py()
