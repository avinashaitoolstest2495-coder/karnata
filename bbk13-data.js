/**
 * bbk13-data.js — Official Data Model & Engine for Karnata BBK13 Airlines
 * Complete 18 Contestant Roster, Automated Simulation Layer, Previous Seasons Hall of Fame (S1–S12)
 */

window.BBK13_DATA = {
  season: 13,
  flightNumber: "BBK-013",
  departureAirport: "ಬೆಂಗಳೂರು ಕೆಂಪೇಗೌಡ (BLR)",
  destination: "ದೊಡ್ಡಮನೆ ಗಗನಧಾಮ (DDM)",
  host: "ಕಿಚ್ಚ ಸುದೀಪ್ (Chief Captain)",
  currentDay: 53,
  totalPassengers: 10, // 10 Active (1 Captain + 1 Safe + 5 Nominated + 3 Wildcards) // 10 Active (1 Captain + 1 Safe + 5 Nominated + 3 Wildcards) // 10 Active (1 Captain + 1 Safe + 5 Nominated + 3 Wildcards)
  status: "🟢 LIVE IN FLIGHT",

  // 18 Contestants Roster (Easy to customize, realistic Kannada profiles)
  contestants: [
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
    "nominationStatus": false,
    "eliminated": false,
    "isWildcard": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 98,
      "strategy": 82,
      "entertainment": 99,
      "emotion": 90,
      "leadership": 86,
      "drama": 84
    },
    "baggage": {
      "drama": 84,
      "fun": 99,
      "emotion": 90,
      "strategy": 82,
      "anger": 40,
      "leadership": 86
    },
    "stats": {
      "taskWins": 3,
      "nominations": 1,
      "survivalDays": 53,
      "fanVotes": 89200,
      "xp": 4200
    },
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
    "nominationStatus": false,
    "eliminated": false,
    "isWildcard": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 94,
      "strategy": 95,
      "entertainment": 88,
      "emotion": 80,
      "leadership": 94,
      "drama": 92
    },
    "baggage": {
      "drama": 92,
      "fun": 82,
      "emotion": 80,
      "strategy": 95,
      "anger": 72,
      "leadership": 94
    },
    "stats": {
      "taskWins": 5,
      "nominations": 2,
      "survivalDays": 53,
      "fanVotes": 81400,
      "xp": 4600
    },
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
    "nominationStatus": false,
    "eliminated": true,
    "isWildcard": false,
    "evictedWeek": "Week 03 (Day 21)",
    "eliminationReason": "3ನೇ ವಾರದ ನಾಮಿನೇಷನ್‌ನಲ್ಲಿ ಕಡಿಮೆ ಸಾರ್ವಜನಿಕ ಮತಗಳು",
    "entryDate": "Day 01",
    "scores": {
      "popularity": 72,
      "strategy": 68,
      "entertainment": 70,
      "emotion": 78,
      "leadership": 65,
      "drama": 50
    },
    "baggage": {
      "drama": 50,
      "fun": 70,
      "emotion": 78,
      "strategy": 68,
      "anger": 45,
      "leadership": 65
    },
    "stats": {
      "taskWins": 1,
      "nominations": 2,
      "survivalDays": 21,
      "fanVotes": 18200,
      "xp": 1400
    },
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
    "nominationStatus": false,
    "eliminated": true,
    "isWildcard": false,
    "evictedWeek": "Week 01 (Day 07)",
    "eliminationReason": "1ನೇ ವಾರದ ಸಾರ್ವಜನಿಕ ವೋಟಿಂಗ್‌ನಲ್ಲಿ ಕೊನೆಯ ಸ್ಥಾನ",
    "entryDate": "Day 01",
    "scores": {
      "popularity": 65,
      "strategy": 55,
      "entertainment": 60,
      "emotion": 85,
      "leadership": 60,
      "drama": 45
    },
    "baggage": {
      "drama": 45,
      "fun": 60,
      "emotion": 85,
      "strategy": 55,
      "anger": 35,
      "leadership": 60
    },
    "stats": {
      "taskWins": 0,
      "nominations": 1,
      "survivalDays": 7,
      "fanVotes": 9800,
      "xp": 800
    },
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
    "nominationStatus": true,
    "eliminated": false,
    "isWildcard": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 92,
      "strategy": 89,
      "entertainment": 84,
      "emotion": 80,
      "leadership": 90,
      "drama": 88
    },
    "baggage": {
      "drama": 88,
      "fun": 80,
      "emotion": 80,
      "strategy": 89,
      "anger": 85,
      "leadership": 90
    },
    "stats": {
      "taskWins": 4,
      "nominations": 3,
      "survivalDays": 53,
      "fanVotes": 76500,
      "xp": 3900
    },
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
    "nominationStatus": true,
    "eliminated": false,
    "isWildcard": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 89,
      "strategy": 91,
      "entertainment": 82,
      "emotion": 84,
      "leadership": 82,
      "drama": 78
    },
    "baggage": {
      "drama": 78,
      "fun": 80,
      "emotion": 84,
      "strategy": 91,
      "anger": 65,
      "leadership": 82
    },
    "stats": {
      "taskWins": 3,
      "nominations": 4,
      "survivalDays": 53,
      "fanVotes": 68400,
      "xp": 3700
    },
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
    "nominationStatus": false,
    "eliminated": true,
    "isWildcard": false,
    "evictedWeek": "Week 04 (Day 28)",
    "eliminationReason": "4ನೇ ವಾರದ ಡೇಂಜರ್ ಝೋನ್‌ನಲ್ಲಿ ಕಡಿಮೆ ಮತಗಳು",
    "entryDate": "Day 01",
    "scores": {
      "popularity": 74,
      "strategy": 65,
      "entertainment": 72,
      "emotion": 82,
      "leadership": 68,
      "drama": 76
    },
    "baggage": {
      "drama": 76,
      "fun": 72,
      "emotion": 82,
      "strategy": 65,
      "anger": 60,
      "leadership": 68
    },
    "stats": {
      "taskWins": 1,
      "nominations": 3,
      "survivalDays": 28,
      "fanVotes": 24500,
      "xp": 1800
    },
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
    "nominationStatus": true,
    "eliminated": false,
    "isWildcard": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 86,
      "strategy": 88,
      "entertainment": 85,
      "emotion": 76,
      "leadership": 89,
      "drama": 94
    },
    "baggage": {
      "drama": 94,
      "fun": 76,
      "emotion": 76,
      "strategy": 88,
      "anger": 92,
      "leadership": 89
    },
    "stats": {
      "taskWins": 2,
      "nominations": 5,
      "survivalDays": 53,
      "fanVotes": 59100,
      "xp": 3400
    },
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
    "nominationStatus": false,
    "eliminated": true,
    "isWildcard": false,
    "evictedWeek": "Week 02 (Day 14)",
    "eliminationReason": "2ನೇ ವಾರದ ಸಾರ್ವಜನಿಕ ಮತದಾನದಲ್ಲಿ ಕಡಿಮೆ ಮತಗಳು",
    "entryDate": "Day 01",
    "scores": {
      "popularity": 68,
      "strategy": 60,
      "entertainment": 65,
      "emotion": 80,
      "leadership": 62,
      "drama": 58
    },
    "baggage": {
      "drama": 58,
      "fun": 65,
      "emotion": 80,
      "strategy": 60,
      "anger": 40,
      "leadership": 62
    },
    "stats": {
      "taskWins": 0,
      "nominations": 2,
      "survivalDays": 14,
      "fanVotes": 14100,
      "xp": 1100
    },
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
    "nominationStatus": true,
    "eliminated": false,
    "isWildcard": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 87,
      "strategy": 82,
      "entertainment": 88,
      "emotion": 89,
      "leadership": 75,
      "drama": 74
    },
    "baggage": {
      "drama": 74,
      "fun": 85,
      "emotion": 89,
      "strategy": 82,
      "anger": 55,
      "leadership": 75
    },
    "stats": {
      "taskWins": 2,
      "nominations": 3,
      "survivalDays": 53,
      "fanVotes": 62300,
      "xp": 3300
    },
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
    "nominationStatus": false,
    "eliminated": true,
    "isWildcard": false,
    "evictedWeek": "Week 05 (Day 35)",
    "eliminationReason": "5ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್‌ನಲ್ಲಿ ನಿರ್ಗಮನ",
    "entryDate": "Day 01",
    "scores": {
      "popularity": 76,
      "strategy": 72,
      "entertainment": 74,
      "emotion": 78,
      "leadership": 76,
      "drama": 68
    },
    "baggage": {
      "drama": 68,
      "fun": 74,
      "emotion": 78,
      "strategy": 72,
      "anger": 65,
      "leadership": 76
    },
    "stats": {
      "taskWins": 2,
      "nominations": 3,
      "survivalDays": 35,
      "fanVotes": 32100,
      "xp": 2200
    },
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
    "nominationStatus": true,
    "eliminated": false,
    "isWildcard": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 85,
      "strategy": 80,
      "entertainment": 78,
      "emotion": 75,
      "leadership": 84,
      "drama": 82
    },
    "baggage": {
      "drama": 82,
      "fun": 75,
      "emotion": 75,
      "strategy": 80,
      "anger": 80,
      "leadership": 84
    },
    "stats": {
      "taskWins": 4,
      "nominations": 3,
      "survivalDays": 53,
      "fanVotes": 58900,
      "xp": 3500
    },
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
    "nominationStatus": false,
    "eliminated": true,
    "isWildcard": false,
    "evictedWeek": "Week 06 (Day 42)",
    "eliminationReason": "6ನೇ ವಾರದ ಸಾರ್ವಜನಿಕ ವೋಟಿಂಗ್‌ನಲ್ಲಿ ನಿರ್ಗಮನ",
    "entryDate": "Day 01",
    "scores": {
      "popularity": 78,
      "strategy": 70,
      "entertainment": 80,
      "emotion": 84,
      "leadership": 70,
      "drama": 72
    },
    "baggage": {
      "drama": 72,
      "fun": 80,
      "emotion": 84,
      "strategy": 70,
      "anger": 50,
      "leadership": 70
    },
    "stats": {
      "taskWins": 1,
      "nominations": 4,
      "survivalDays": 42,
      "fanVotes": 38400,
      "xp": 2600
    },
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
    "nominationStatus": false,
    "eliminated": true,
    "isWildcard": false,
    "evictedWeek": "Week 07 (Day 49)",
    "eliminationReason": "7ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್‌ನಲ್ಲಿ ಸಾರ್ವಜನಿಕ ಮತಗಳ ಕೊರತೆ",
    "entryDate": "Day 01",
    "scores": {
      "popularity": 81,
      "strategy": 78,
      "entertainment": 75,
      "emotion": 79,
      "leadership": 80,
      "drama": 76
    },
    "baggage": {
      "drama": 76,
      "fun": 75,
      "emotion": 79,
      "strategy": 78,
      "anger": 70,
      "leadership": 80
    },
    "stats": {
      "taskWins": 2,
      "nominations": 4,
      "survivalDays": 49,
      "fanVotes": 44800,
      "xp": 2900
    },
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
    "nominationStatus": false,
    "eliminated": true,
    "isWildcard": false,
    "evictedWeek": "Week 03 (Day 21)",
    "eliminationReason": "3ನೇ ವಾರದ ಡಬಲ್ ಎಲಿಮಿನೇಷನ್‌ನಲ್ಲಿ ನಿರ್ಗಮನ",
    "entryDate": "Day 01",
    "scores": {
      "popularity": 70,
      "strategy": 68,
      "entertainment": 70,
      "emotion": 76,
      "leadership": 66,
      "drama": 65
    },
    "baggage": {
      "drama": 65,
      "fun": 70,
      "emotion": 76,
      "strategy": 68,
      "anger": 60,
      "leadership": 66
    },
    "stats": {
      "taskWins": 1,
      "nominations": 2,
      "survivalDays": 21,
      "fanVotes": 19500,
      "xp": 1400
    },
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
    "nominationStatus": false,
    "eliminated": true,
    "isWildcard": false,
    "evictedWeek": "Week 08 (Day 51)",
    "eliminationReason": "ದೊಡ್ಡಮನೆಯ ರೂಲ್ಸ್ ಉಲ್ಲಂಘನೆ & ಕಿಚ್ಚ ಸುದೀಪ್ ನೇರ ರೆಡ್ ಕಾರ್ಡ್ ಎಜೆಕ್ಷನ್ (Direct Red Card)",
    "entryDate": "Day 01",
    "scores": {
      "popularity": 75,
      "strategy": 50,
      "entertainment": 80,
      "emotion": 60,
      "leadership": 50,
      "drama": 98
    },
    "baggage": {
      "drama": 98,
      "fun": 78,
      "emotion": 60,
      "strategy": 50,
      "anger": 95,
      "leadership": 50
    },
    "stats": {
      "taskWins": 1,
      "nominations": 4,
      "survivalDays": 51,
      "fanVotes": 31200,
      "xp": 2400
    },
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
    "nominationStatus": false,
    "eliminated": false,
    "isWildcard": true,
    "entryDate": "Day 21 (ವಾರ 03)",
    "scores": {
      "popularity": 99,
      "strategy": 84,
      "entertainment": 96,
      "emotion": 98,
      "leadership": 88,
      "drama": 70
    },
    "baggage": {
      "drama": 70,
      "fun": 96,
      "emotion": 98,
      "strategy": 84,
      "anger": 30,
      "leadership": 88
    },
    "stats": {
      "taskWins": 4,
      "nominations": 1,
      "survivalDays": 32,
      "fanVotes": 115000,
      "xp": 5100
    },
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
    "nominationStatus": false,
    "eliminated": false,
    "isWildcard": true,
    "entryDate": "Day 50 (ವಾರ 07)",
    "scores": {
      "popularity": 91,
      "strategy": 93,
      "entertainment": 89,
      "emotion": 78,
      "leadership": 91,
      "drama": 96
    },
    "baggage": {
      "drama": 96,
      "fun": 85,
      "emotion": 78,
      "strategy": 93,
      "anger": 88,
      "leadership": 91
    },
    "stats": {
      "taskWins": 2,
      "nominations": 0,
      "survivalDays": 4,
      "fanVotes": 64200,
      "xp": 3600
    },
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
    "nominationStatus": false,
    "eliminated": false,
    "isWildcard": true,
    "entryDate": "Day 50 (ವಾರ 07)",
    "scores": {
      "popularity": 88,
      "strategy": 89,
      "entertainment": 84,
      "emotion": 82,
      "leadership": 85,
      "drama": 92
    },
    "baggage": {
      "drama": 92,
      "fun": 80,
      "emotion": 82,
      "strategy": 89,
      "anger": 84,
      "leadership": 85
    },
    "stats": {
      "taskWins": 1,
      "nominations": 0,
      "survivalDays": 4,
      "fanVotes": 51800,
      "xp": 3100
    },
    "cardRarity": "RARE"
  }
],

  // Elimination History Ledger
  eliminationLedger: [
  {
    "week": 1,
    "day": "Day 07",
    "id": "C04",
    "name": "ಪ್ರಥಮಾ ಪ್ರಸಾದ್ (Prathama Prasad)",
    "type": "EVICTED",
    "reason": "ಕಡಿಮೆ ಸಾರ್ವಜನಿಕ ಮತಗಳು (Lowest Votes)",
    "photo": "/assets/bbk13/contestants/passenger_04_face.jpg"
  },
  {
    "week": 2,
    "day": "Day 14",
    "id": "C09",
    "name": "ಕಿರಣ್ ಶಾಸ್ತ್ರಿ (Kiran Shastri)",
    "type": "EVICTED",
    "reason": "ನಾಮಿನೇಷನ್‌ನಲ್ಲಿ ಮತಗಳ ಕೊರತೆ",
    "photo": "/assets/bbk13/contestants/passenger_09_face.jpg"
  },
  {
    "week": 3,
    "day": "Day 21",
    "id": "C03",
    "name": "ಅವಿನಾಶ್ ಶಟಮರ್ಷನ (Avinash)",
    "type": "EVICTED",
    "reason": "3ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್",
    "photo": "/assets/bbk13/contestants/passenger_03_face.jpg"
  },
  {
    "week": 3,
    "day": "Day 21",
    "id": "C15",
    "name": "ಯಶಸ್ ಕೃಷ್ಣ (Yashas Krishna)",
    "type": "EVICTED",
    "reason": "ಡಬಲ್ ಎಲಿಮಿನೇಷನ್ ನಿರ್ಗಮನ",
    "photo": "/assets/bbk13/contestants/passenger_15_face.jpg"
  },
  {
    "week": 4,
    "day": "Day 28",
    "id": "C07",
    "name": "ಕಾವ್ಯ ಗೌಡ (Kavya Gowda)",
    "type": "EVICTED",
    "reason": "4ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್",
    "photo": "/assets/bbk13/contestants/passenger_07_face.jpg"
  },
  {
    "week": 5,
    "day": "Day 35",
    "id": "C11",
    "name": "ಲಿಖಿತ್ ಗೊಂಡಿ (Likhith Gondi)",
    "type": "EVICTED",
    "reason": "5ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್",
    "photo": "/assets/bbk13/contestants/passenger_11_face.jpg"
  },
  {
    "week": 6,
    "day": "Day 42",
    "id": "C13",
    "name": "ವೈಷ್ಣವಿ (Vaishnavi)",
    "type": "EVICTED",
    "reason": "6ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್",
    "photo": "/assets/bbk13/contestants/passenger_13_face.jpg"
  },
  {
    "week": 7,
    "day": "Day 49",
    "id": "C14",
    "name": "ಧನುಷ್ ಮಂಜುನಾಥ್ (Dhanush)",
    "type": "EVICTED",
    "reason": "7ನೇ ವಾರದ ಎಲಿಮಿನೇಷನ್",
    "photo": "/assets/bbk13/contestants/passenger_14_face.jpg"
  },
  {
    "week": 8,
    "day": "Day 51",
    "id": "C16",
    "name": "ಮಾಡ್ರನ್ ಮಹಾಕವಿ ಮಂಜ (Manja)",
    "type": "RED_CARD",
    "reason": "ರೂಲ್ಸ್ ಉಲ್ಲಂಘನೆ & ಕಿಚ್ಚ ಸುದೀಪ್ ನೇರ ರೆಡ್ ಕಾರ್ಡ್",
    "photo": "/assets/bbk13/contestants/passenger_16_face.jpg"
  }
],

  // Wildcard Entries Ledger
  wildcardLedger: [
  {
    "week": 3,
    "day": "Day 21",
    "id": "C17",
    "name": "ಹನುಮಂತ ಲಮಾಣಿ (Hanumantha Lamani)",
    "role": "ಜಾನಪದ ಕೋಗಿಲೆ",
    "status": "ಸಕ್ರಿಯ (ಕೋಟ್ಯಂತರ ಮತಗಳು)",
    "photo": "/assets/bbk13/winners/BBK_Winner_11_face.jpg"
  },
  {
    "week": 7,
    "day": "Day 50",
    "id": "C18",
    "name": "ರಜತ್ ಕಿಶನ್ (Rajath Kishan)",
    "role": "ರಿಯಾಲಿಟಿ ಸ್ಟಾರ್",
    "status": "ಸಕ್ರಿಯ (ಹೈ-ವೋಲ್ಟೇಜ್ ಎನರ್ಜಿ)",
    "photo": "/assets/bbk13/contestants/passenger_15_face.jpg"
  },
  {
    "week": 7,
    "day": "Day 50",
    "id": "C19",
    "name": "ಶೋಭಾ ಶೆಟ್ಟಿ (Shobha Shetty)",
    "role": "ಖ್ಯಾತ ನಟಿ",
    "status": "ಸಕ್ರಿಯ (ಬೋಲ್ಡ್ ಫೈಟರ್)",
    "photo": "/assets/bbk13/contestants/passenger_07_face.jpg"
  }
],

  // ALL PREVIOUS SEASONS (Season 1 to Season 12) HALL OF FAME & WINNERS
  previousSeasons: [
    { season: 1, year: "2013", winner: "ವಿಜಯ್ ರಾಘವೇಂದ್ರ", runnerUp: "ಅರುಣ್ ಸಾಗರ್", host: "ಕಿಚ್ಚ ಸುದೀಪ್", days: 98, contestantsCount: 15, photo: "assets/bbk13/winners/BBK_Winner_01_face.jpg", highlight: "ಚಿನ್ನಾರಿ ಮುತ್ತ ವಿಜಯ್ ರಾಘವೇಂದ್ರ ಮೊದಲ ಬಿಗ್ ಬಾಸ್ ಟ್ರೋಫಿ ಮುಡಿಗೇರಿಸಿಕೊಂಡ ಐತಿಹಾಸಿಕ ಕ್ಷಣ." },
    { season: 2, year: "2014", winner: "ಅಕುಲ್ ಬಾಲಾಜಿ", runnerUp: "ಸೃಜನ್ ಲೋಕೇಶ್", host: "ಕಿಚ್ಚ ಸುದೀಪ್", days: 98, contestantsCount: 15, photo: "assets/bbk13/winners/BBK_Winner_02_face.jpg", highlight: "ಅಕುಲ್ ಬಾಲಾಜಿ ಮತ್ತು ಸೃಜನ್ ಲೋಕೇಶ್ ನಡುವಿನ ಜಿದ್ದಾಜಿದ್ದಿನ ಫಿನಾಲೆ ಕದನ." },
    { season: 3, year: "2015-16", winner: "ಶ್ರುತಿ", runnerUp: "ಚಂದನ್ ಕುಮಾರ್", host: "ಕಿಚ್ಚ ಸುದೀಪ್", days: 98, contestantsCount: 18, photo: "assets/bbk13/winners/BBK_Winner_03_face.jpg", highlight: "ಹಿರಿಯ ನಟಿ ಶ್ರುತಿ ಮೊದಲ ಮಹಿಳಾ ಬಿಗ್ ಬಾಸ್ ಚಾಂಪಿಯನ್ ಆಗಿ ಇತಿಹಾಸ ಸೃಷ್ಟಿ." },
    { season: 4, year: "2016-17", winner: "ಪ್ರಥಮ್ (ಒಳ್ಳೇ ಹುಡ್ಗ)", runnerUp: "ಕೀರ್ತಿ ಕುಮಾರ್", host: "ಕಿಚ್ಚ ಸುದೀಪ್", days: 112, contestantsCount: 18, photo: "assets/bbk13/winners/BBK_Winner_04_face.jpg", highlight: "ಜನಸಾಮಾನ್ಯರ ಧ್ವನಿ ಒಳ್ಳೇ ಹುಡ್ಗ ಪ್ರಥಮ್ ಅತಿ ಹೆಚ್ಚು ವೋಟ್ ಪಡೆದು ಗೆಲುವು." },
    { season: 5, year: "2017-18", winner: "ಚಂದನ್ ಶೆಟ್ಟಿ", runnerUp: "ದಿವಾಕರ್", host: "ಕಿಚ್ಚ ಸುದೀಪ್", days: 105, contestantsCount: 19, photo: "assets/bbk13/winners/BBK_Winner_05_face.jpg", highlight: "ಕನ್ನಡ ರಾಪರ್ ಚಂದನ್ ಶೆಟ್ಟಿ ಸಂಗೀತ ಮತ್ತು ವ್ಯಕ್ತಿತ್ವದಿಂದ ಕರುನಾಡ ಜನಮನ ಗೆದ್ದರು." },
    { season: 6, year: "2018-19", winner: "ಶಶಿ ಕುಮಾರ್ (ಆಧುನಿಕ ರೈತ)", runnerUp: "ನವೀನ್ ಸಜ್ಜು", host: "ಕಿಚ್ಚ ಸುದೀಪ್", days: 105, contestantsCount: 18, photo: "assets/bbk13/winners/BBK_Winner_06_face.jpg", highlight: "ಕೃಷಿ ತಜ್ಞ ಆಧುನಿಕ ರೈತ ಶಶಿ ಕುಮಾರ್ ಕಿರೀಟ ಧರಿಸಿ ರೈತರಿಗೆ ಗೌರವ ತಂದರು." },
    { season: 7, year: "2019-20", winner: "ಶೈನ್ ಶೆಟ್ಟಿ", runnerUp: "ಕುರಿ ಪ್ರತಾಪ್", host: "ಕಿಚ್ಚ ಸುದೀಪ್", days: 112, contestantsCount: 20, photo: "assets/bbk13/winners/BBK_Winner_07_face.jpg", highlight: "ಶೈನ್ ಶೆಟ್ಟಿ ಅವರ ಕಮ್‌ಬ್ಯಾಕ್ ಮತ್ತು ಕುರಿ ಪ್ರತಾಪ್ ಅವರ ಅನ್‌ಲಿಮಿಟೆಡ್ ಕಾಮಿಡಿ." },
    { season: 8, year: "2021", winner: "ಮಂಜು ಪಾವಗಡ (ಲಗೋರಿ ಮಂಜ)", runnerUp: "ಅರವಿಂದ್ ಕೆ.ಪಿ.", host: "ಕಿಚ್ಚ ಸುದೀಪ್", days: 120, contestantsCount: 20, photo: "assets/bbk13/winners/BBK_Winner_08_face.jpg", highlight: "ಮಜಾ ಭಾರತದ ಲಗೋರಿ ಮಂಜ ಹಾಗೂ ಬೈಕರ್ ಅರವಿಂದ್ ಕೆ.ಪಿ. ನಡುವಿನ ಮಹಾಸಮರ." },
    { season: 9, year: "2022", winner: "ರೂಪೇಶ್ ಶೆಟ್ಟಿ", runnerUp: "ರಾಕೇಶ್ ಅಡಿಗ", host: "ಕಿಚ್ಚ ಸುದೀಪ್", days: 100, contestantsCount: 18, photo: "assets/bbk13/winners/BBK_Winner_09_face.jpg", highlight: "OTT ಮತ್ತು ಟಿವಿ ಎರಡರಲ್ಲೂ ರೂಪೇಶ್ ಶೆಟ್ಟಿ ಡಬಲ್ ಚಾಂಪಿಯನ್ ಕಿರೀಟ." },
    { season: 10, year: "2023-24", winner: "ಕಾರ್ತಿಕ್ ಮಹೇಶ್", runnerUp: "ಡ್ರೋನ್ ಪ್ರತಾಪ್", host: "ಕಿಚ್ಚ ಸುದೀಪ್", days: 112, contestantsCount: 21, photo: "assets/bbk13/winners/BBK_Winner_10_face.jpg", highlight: "10 ನೇ ದಶಮಾನೋತ್ಸವದ ರೋಚಕ ಫಿನಾಲೆಯಲ್ಲಿ ಕಾರ್ತಿಕ್ ಮಹೇಶ್ ಚಾಂಪಿಯನ್." },
    { season: 11, year: "2024-25", winner: "ಹನುಮಂತ ಲಮಾಣಿ", runnerUp: "ತ್ರಿವಿಕ್ರಮ್", winnerImg: "", runnerUpImg: "", host: "ಕಿಚ್ಚ ಸುದೀಪ್", days: 112, contestantsCount: 19, photo: "assets/bbk13/winners/BBK_Winner_11_face.jpg", highlight: "ಗ್ರಾಮೀಣ ಜಾನಪದ ಕೋಗಿಲೆ ಹನುಮಂತ ಲಮಾಣಿ ಚಾಂಪಿಯನ್, ತ್ರಿವಿಕ್ರಮ್ ರನ್ನರ್-ಅಪ್ ಆಗಿ ಅಪಾರ ಜನಮನ್ನಣೆ ಗಳಿಸಿದರು." },
    { season: 12, year: "2025-26", winner: "ಗಿಲ್ಲಿ ನಟ", runnerUp: "ರಕ್ಷಿತಾ ಶೆಟ್ಟಿ", winnerImg: "", runnerUpImg: "", host: "ಕಿಚ್ಚ ಸುದೀಪ್", days: 105, contestantsCount: 18, photo: "assets/bbk13/winners/BBK_Winner_12_face.jpg", highlight: "ಗಿಲ್ಲಿ ನಟ ಅದ್ಭುತ ಆಟದ ಮೂಲಕ ವಿನ್ನರ್ ಕಿರೀಟ ಮುಡಿಗೇರಿಸಿಕೊಂಡರೆ, ರಕ್ಷಿತಾ ಶೆಟ್ಟಿ ಪ್ರಥಮ ರನ್ನರ್-ಅಪ್ ಆದರು." }
  ],

  // Live Flight Departure Board
  flightBoard: [
    { flight: "BBK-013", route: "ಬೆಂಗಳೂರು ➔ ದೊಡ್ಡಮನೆ", time: "21:30", gate: "G-13", status: "🟢 LIVE", statusKn: "ಹಾರಾಟದಲ್ಲಿದೆ (LIVE)" },
    { flight: "BBK-013A", route: "ವೀಕೆಂಡ್ ವಿತ್ ಕಿಚ್ಚ ಸುದೀಪ್", time: "ಶನಿವಾರ 21:00", gate: "G-01", status: "🟡 UPCOMING", statusKn: "ಮುಂದಿನದು (UPCOMING)" },
    { flight: "BBK-013B", route: "ಮೊದಲ ನಾಮಿನೇಷನ್ ಕದನ", time: "ಸೋಮವಾರ 21:30", gate: "G-03", status: "🚨 ALERT", statusKn: "ಎಚ್ಚರಿಕೆ (ALERT)" },
    { flight: "BBK-013C", route: "ಕ್ಯಾಪ್ಟನ್ಸಿ ಟಾಸ್ಕ್ ಸಮರ", time: "ಗುರುವಾರ 22:00", gate: "G-07", status: "👑 UPCOMING", statusKn: "ಸಿದ್ಧತೆ (PREP)" }
  ],

  // Air Traffic Control (Events)
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
  ],

  // World Tour Destinations (Progressive Unlocks)
  worldTour: [
    { id: "DEST01", city: "ಬೆಂಗಳೂರು (BLR)", country: "ಕರ್ನಾಟಕ", stage: "Stage 01: Take-Off", unlocked: true, missionTitle: "ದೊಡ್ಡಮನೆ ಟೇಕ್-ಆಫ್ ಕ್ವಿಜ್", missionDesc: "BBK13 ಆರಂಭದ ರೋಚಕ ಕ್ಷಣಗಳ 3 ಸರಳ ಪ್ರಶ್ನೆಗಳಿಗೆ ಉತ್ತರಿಸಿ 250 XP ಗೆಲ್ಲಿರಿ.", xpReward: 250 },
    { id: "DEST02", city: "ದುಬೈ (DXB)", country: "UAE", stage: "Stage 02: Luxury Oasis", unlocked: true, missionTitle: "ಲಕ್ಸುರಿ ಬಜೆಟ್ ರಹಸ್ಯ ಲಾಕ್", missionDesc: "ದುಬೈ ಹಂತದಲ್ಲಿ ದೊಡ್ಮನೆಗೆ ಬೇಕಾದ ರೇಷನ್ ಕೋಡ್ ಭೇದಿಸಿ 350 XP ಪಡೆಯಿರಿ.", xpReward: 350 },
    { id: "DEST03", city: "ಪ್ಯಾರಿಸ್ (CDG)", country: "France", stage: "Stage 03: Fashion & Drama", unlocked: false, missionTitle: "ಪ್ಯಾರಿಸ್ ರನ್‌ವೇ ಟಾಸ್ಕ್", missionDesc: "ದೊಡ್ಮನೆಯ ಬೆಸ್ಟ್ ಲುಕ್ ಯಾರದ್ದು ಊಹಿಸಿ. (Day 15 ರಂದು ಅನ್‌ಲಾಕ್)", xpReward: 500 },
    { id: "DEST04", city: "ಲಂಡನ್ (LHR)", country: "UK", stage: "Stage 04: Royal Captaincy", unlocked: false, missionTitle: "ರಾಯಲ್ ಕ್ಯಾಪ್ಟನ್ಸಿ ಚಾಲೆಂಜ್", missionDesc: "ಕ್ವೀನ್ಸ್ ಪ್ಯಾಲೇಸ್ ಮಾದರಿಯ ಕ್ಯಾಪ್ಟನ್ಸಿ ಪರೀಕ್ಷೆ. (Day 30 ರಂದು ಅನ್‌ಲಾಕ್)", xpReward: 750 },
    { id: "DEST05", city: "ಟೋಕಿಯೋ (HND)", country: "Japan", stage: "Stage 05: High-Tech Escape", unlocked: false, missionTitle: "ಬುಲೆಟ್ ಟ್ರೇನ್ ಸ್ಪೀಡ್ ಟಾಸ್ಕ್", missionDesc: "60 ಸೆಕೆಂಡುಗಳ ಹೈ-ಸ್ಪೀಡ್ ಬಜರ್ ಗೇಮ್. (Day 50 ರಂದು ಅನ್‌ಲಾಕ್)", xpReward: 1000 },
    { id: "DEST06", city: "ನ್ಯೂಯಾರ್ಕ್ (JFK)", country: "USA", stage: "Stage 06: Grand Finale", unlocked: false, missionTitle: "ಫೈನಲ್ ಟ್ರೋಫಿ ಲ್ಯಾಂಡಿಂಗ್", missionDesc: "BBK13 ಚಾಂಪಿಯನ್ ಪಟ್ಟ ಯಾರಿಗೆ? ಮಹಾ ಸಮರ. (Day 100 ರಂದು ಅನ್‌ಲಾಕ್)", xpReward: 2500 }
  ],

  // Who Said It Game Data
  quotesGame: [
    { id: "Q01", quote: "“ನಾವು ಕೋರ್ಟ್‌ನಲ್ಲೇ ವಾದ ಮಾಡಿ ಗೆದ್ದವರು, ಈ ಮನೆಯಲ್ಲಿ ನಮ್ಮ ಮಾತೆ ಕಾನೂನು!”", options: ["ನ್ಯಾಯವಾದಿ (A08)", "ಪ್ರಖರ ವಾಗ್ಮಿ (B01)", "ಸಿನಿಮಾ ನಟ (A01)", "ಖಳನಟ (B05)"], correctIndex: 0, xp: 100 },
    { id: "Q02", quote: "“ನಾನು ನಗಿಸೋಕೆ ಬಂದಿರೋನು, ಆದ್ರೆ ನನ್ನ ತಾಳ್ಮೆ ಪರೀಕ್ಷೆ ಮಾಡಿದ್ರೆ ನಗುವೇ ಮಾಯ ಆಗುತ್ತೆ!”", options: ["ಕಾಮಿಡಿಯನ್ (A02)", "ಜಾನಪದ ಗಾಯಕ (A08)", "ಫಿಟ್‌ನೆಸ್ ಕೋಚ್ (A07)", "ನೃತ್ಯಪಟು (A06)"], correctIndex: 0, xp: 100 },
    { id: "Q03", quote: "“ಟಾಸ್ಕ್‌ನಲ್ಲಿ ಗಂಡು ಹೆಣ್ಣು ಅನ್ನೋ ಭೇದ ಇಲ್ಲ, ಧೈರ್ಯ ಇರೋರೆ ಗೆಲ್ಲೋದು!”", options: ["ಧಾರಾವಾಹಿ ನಾಯಕಿ (A03)", "ಹಿರಿಯ ನಟಿ (B02)", "ಮಾಡೆಲ್ (B07)", "ರೇಡಿಯೋ ಜಾಕಿ (B06)"], correctIndex: 0, xp: 100 },
    { id: "Q04", quote: "“ಕ್ಯಾಪ್ಟನ್ ಆದವನು ಎಲ್ಲರನ್ನೂ ಸಮಾನವಾಗಿ ನೋಡಬೇಕು, ನನ್ನ ಆಡಳಿತ ನ್ಯಾಯಯುತವಾಗಿರುತ್ತದೆ!”", options: ["ಸಿನಿಮಾ ನಟ (A01)", "ಸೂಪರ್‌ಸ್ಟಾರ್ (A09)", "ನಾಟಕಕಾರ (B08)", "ಜಾನಪದ ಗಾಯಕ (A08)"], correctIndex: 0, xp: 100 }
  ],

  // Who Am I Game Data
  whoAmIGame: [
    { id: "W01", clues: ["1. ನಾನು ಕರಾವಳಿ ತೀರದಿಂದ ಬಂದಿದ್ದೇನೆ.", "2. ಹಾಸ್ಯ, ಸ್ಟ್ಯಾಂಡಪ್ ಕಾಮಿಡಿ ಮತ್ತು ಮಿಮಿಕ್ರಿ ನನ್ನ ಮುಖ್ಯ ಆಯುಧ.", "3. ದೊಡ್ಮನೆಯಲ್ಲಿ ಪ್ರತಿಯೊಬ್ಬರ ಧ್ವನಿ ಅನುಕರಣೆ ಮಾಡಿ ನಗಿಸುತ್ತೇನೆ."], answerId: "C03", answerName: "ಕಾಮಿಡಿಯನ್ (A02)", xpValues: [300, 200, 100] },
    { id: "W02", clues: ["1. ನಾನು ಕಿರುತೆರೆಯಲ್ಲಿ ನಾಯಕಿಯಾಗಿ ಕೋಟ್ಯಂತರ ಮನ ಗೆದ್ದಿದ್ದೇನೆ.", "2. ಸೌಮ್ಯ ಮುಖ, ಆದರೆ ಟಾಸ್ಕ್‌ಗಳಲ್ಲಿ ಚಾಣಾಕ್ಷ ಬುದ್ಧಿ.", "3. ದೊಡ್ಮನೆಯ ಮೊದಲ ದಿನವೇ ಟಾಸ್ಕ್ ವಿಜೇತೆಯಾಗಿದ್ದೇನೆ."], answerId: "C05", answerName: "ಧಾರಾವಾಹಿ ನಾಯಕಿ (A03)", xpValues: [300, 200, 100] }
  ],

  // 60-Second Timed Quiz Questions
  timedQuizQuestions: [
    { q: "ಬಿಗ್ ಬಾಸ್ ಕನ್ನಡ ಸೀಸನ್ 1 ರ ಮೊದಲ ಐತಿಹಾಸಿಕ ವಿಜೇತರು ಯಾರು?", o: ["ಅಕುಲ್ ಬಾಲಾಜಿ", "ವಿಜಯ್ ರಾಘವೇಂದ್ರ", "ಪ್ರಥಮ್", "ಶ್ರುತಿ"], a: 1 },
    { q: "ಬಿಗ್ ಬಾಸ್ ಕನ್ನಡವನ್ನು 13 ಸೀಸನ್‌ಗಳಿಂದ ಯಶಸ್ವಿಯಾಗಿ ಮುನ್ನಡೆಸುತ್ತಿರುವ ಚೀಫ್ ಕ್ಯಾಪ್ಟನ್ ಯಾರು?", o: ["ಉಪೇಂದ್ರ", "ಕಿಚ್ಚ ಸುದೀಪ್", "ಪುನೀತ್ ರಾಜ್‌ಕುಮಾರ್", "ಶಿವಣ್ಣ"], a: 1 },
    { q: "BBK ಸೀಸನ್ 8 ರ ಜನಪ್ರಿಯ ವಿಜೇತ ಯಾರು?", o: ["ಮಂಜು ಪಾವಗಡ (ಲಗೋರಿ ಮಂಜ)", "ಅರವಿಂದ್ ಕೆ.ಪಿ.", "ರೂಪೇಶ್ ಶೆಟ್ಟಿ", "ಶೈನ್ ಶೆಟ್ಟಿ"], a: 0 },
    { q: "BBK13 ಏರ್ಲೈನ್ಸ್‌ನಲ್ಲಿ ಒಟ್ಟು ಎಷ್ಟು ಮಂದಿ ಪ್ಯಾಸೆಂಜರ್ಸ್ (ಸ್ಪರ್ಧಿಗಳು) ಇದ್ದಾರೆ?", o: ["13", "16", "18", "20"], a: 2 },
    { q: "ಬಿಗ್ ಬಾಸ್ ಕನ್ನಡ 11 ರ ಟ್ರೋಫಿ ಗೆದ್ದ ಜಾನಪದ ಪ್ರತಿಭೆ ಯಾರು?", o: ["ಹನುಮಂತ ಲಮಾಣಿ", "ಧನರಾಜ್", "ತ್ರಿವಿಕ್ರಮ್", "ಕಾರ್ತಿಕ್ ಮಹೇಶ್"], a: 0 },
    { q: "ದೊಡ್ಮನೆಯಲ್ಲಿ ಸದಸ್ಯರಿಗೆ ಬೇಕಾದ ದಿನಸಿ ಪದಾರ್ಥ ನಿರ್ಧರಿಸುವ ಬಜೆಟ್ ಯಾವುದು?", o: ["ಸರ್ಕಾರಿ ಬಜೆಟ್", "ಲಕ್ಸುರಿ ಬಜೆಟ್", "ರೈತ ಬಜೆಟ್", "ವಾರಾಂತ್ಯ ಬಜೆಟ್"], a: 1 }
  ],

  // Doddamane Escape Room
  escapeRoomPuzzles: [
    { stage: 1, title: "ಲಾಕ್ 1: ಲಗೇಜ್ ಕನ್ವೇಯರ್ ಕೋಡ್", puzzle: "ವಿಮಾನದ ಸೀಟು ಸಂಖ್ಯೆ A01 ರಿಂದ A09 ವರೆಗೆ ಒಟ್ಟು ಎಷ್ಟು ಸ್ಪರ್ಧಿಗಳಿದ್ದಾರೆ? (ಸಂಖ್ಯೆ ನಮೂದಿಸಿ)", answer: "9", xp: 200 },
    { stage: 2, title: "ಲಾಕ್ 2: ಕಾಕ್‌ಪಿಟ್ ಪಾಸ್‌ವರ್ಡ್", puzzle: "ಚೀಫ್ ಕ್ಯಾಪ್ಟನ್ ಸುದೀಪ್ ಅವರ ಪ್ರೀತಿಯ ಬಿರುದು ಯಾವುದು? (ಕಿಚ್ಚ / ಬಾದ್ಷಾ / ಸೂಪರ್‌ಸ್ಟಾರ್)", answer: "ಕಿಚ್ಚ", xp: 200 }
  ],

  // Flight Challenge Situations
  flightSituations: [
    {
      id: "S01",
      situation: "ಅಡುಗೆ ಮನೆಯಲ್ಲಿ ಗ್ಯಾಸ್ ಸಿಲಿಂಡರ್ ಕೊರತೆ ಮತ್ತು ಸದಸ್ಯರ ನಡುವೆ ಹಾಲಿನ ವಿಚಾರಕ್ಕೆ ತೀವ್ರ ಗಲಾಟೆ ಶುರುವಾಗಿದೆ!",
      question: "ವಿಮಾನದ ಪೈಲಟ್ ಆಗಿ ನಿಮ್ಮ ನಿರ್ಧಾರವೇನು?",
      choices: [
        { text: "ಎಲ್ಲರಿಗೂ ಪಡಿತರ ಮಿತಿ ಹೇರಿ ನಿಯಮ ಜಾರಿ ಮಾಡಿ (+ಸ್ಟೆಬಿಲಿಟಿ)", stability: +20, drama: -10, happiness: +10, xp: 250 },
        { text: "ವಾಗ್ಮಿ ಮತ್ತು ವಕೀಲರಿಗೆ ಬಗೆಹರಿಸಲು ಜವಾಬ್ದಾರಿ ನೀಡಿ (+ಡ್ರಾಮಾ)", stability: -15, drama: +35, happiness: -15, xp: 300 },
        { text: "ಸಂಜೆವರೆಗೆ ಅಡುಗೆ ಕೋಣೆಗೆ ಬೀಗ ಹಾಕಿ ಶಿಕ್ಷೆ ನೀಡಿ (+ಅಧಿಕಾರ)", stability: +10, drama: +20, happiness: -25, xp: 200 }
      ]
    }
  ],

  // Daily Wheel Spin Rewards
  wheelRewards: [
    { label: "+100 XP", value: 100, type: "XP", color: "#1E293B" },
    { label: "+250 XP", value: 250, type: "XP", color: "#C0392B" },
    { label: "⭐ RARE CARD", value: "RARE", type: "CARD", color: "#2563EB" },
    { label: "+500 XP", value: 500, type: "XP", color: "#D97706" },
    { label: "+1000 XP JACKPOT", value: 1000, type: "XP", color: "#E11D48" }
  ],

  // BBK13 Journey Timeline
  journeyTimeline: [
    { day: "Day 01", title: "ಗ್ರ್ಯಾಂಡ್ ಟೇಕ್-ಆಫ್ (Grand Take-Off)", desc: "18 ಜನ ಸ್ಪರ್ಧಿಗಳ ರಂಗುರಂಗಿನ ಎಂಟ್ರಿ ಹಾಗೂ ಬಿಗ್ ಬಾಸ್ ವಿಮಾನ ಹಾರಾಟ ಆರಂಭ.", status: "COMPLETED" },
    { day: "Day 03", title: "ಮೊದಲ ನಾಮಿನೇಷನ್ ಕದನ", desc: "ಸೀಟು ಕಸಿದುಕೊಳ್ಳುವ ಬಿರುಗಾಳಿಯ ನಾಮಿನೇಷನ್ ಪ್ರಕ್ರಿಯೆ.", status: "UPCOMING" },
    { day: "Day 07", title: "ವೀಕೆಂಡ್ ವಿತ್ ಸುದೀಪ್ - ಮೊದಲ ಪಂಚಾಯಿತಿ", desc: "ವಾರದ ತಪ್ಪು-ಒಪ್ಪುಗಳ ವಿಶ್ಲೇಷಣೆ & ಕಿಚ್ಚನ ಚಪ್ಪಾಳೆ.", status: "UPCOMING" },
    { day: "Day 14", title: "ಕ್ಯಾಪ್ಟನ್ಸಿ ಅಗ್ನಿಪರೀಕ್ಷೆ & ಸೀಕ್ರೆಟ್ ರೂಮ್", desc: "ಕ್ಯಾಪ್ಟನ್ ಅಧಿಕಾರ ಮತ್ತು ಮನೆಯ ಹೊಸ ನಿಯಮಗಳ ಜಾರಿ.", status: "UPCOMING" },
    { day: "Day 50", title: "ಮಿಡ್-ಸೀಸನ್ ಟರ್ಬುಲೆನ್ಸ್ & ವೈಲ್ಡ್ ಕಾರ್ಡ್", desc: "ಹೊಸ ಸ್ಪರ್ಧಿಗಳ ಆಗಮನದಿಂದ ನಡುಗುವ ದೊಡ್ಮನೆ.", status: "UPCOMING" },
    { day: "Day 100", title: "ಗ್ರ್ಯಾಂಡ್ ಫಿನಾಲೆ ಲ್ಯಾಂಡಿಂಗ್ (Trophy Landing)", desc: "ಕರ್ನಾಟಕದ ಜನತೆ ಆರಿಸಿದ BBK13 ಮಹಾ ವಿಜೇತನ ಕಿರೀಟ ಧಾರಣೆ.", status: "UPCOMING" }
  ],

  // Automated Simulation Engine (Daily In-Flight Updates)
  simulateDayProgress() {
    this.contestants.forEach(c => {
      const deltaVotes = Math.floor(Math.random() * 800) + 100;
      c.stats.fanVotes += deltaVotes;
      c.baggage.drama = Math.min(100, Math.max(20, c.baggage.drama + (Math.floor(Math.random() * 7) - 3)));
      c.baggage.fun = Math.min(100, Math.max(20, c.baggage.fun + (Math.floor(Math.random() * 7) - 3)));
      c.baggage.strategy = Math.min(100, Math.max(20, c.baggage.strategy + (Math.floor(Math.random() * 5) - 2)));
    });
  }
};