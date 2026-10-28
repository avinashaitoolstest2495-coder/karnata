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
  totalPassengers: 14,
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
    "bio": "ಡಾರ್ಲಿಂಗ್ ಕೃಷ್ಣ ನಿರ್ದೇಶಿಸಿ ನಟಿಸಿರುವ ‘ಲವ್ ಮಾಕ್ಟೇಲ್ 3’ ಚಿತ್ರದಲ್ಲಿ ‘ಜಗ್ಗ ಮಮ್ಮಿ’ ಪಾತ್ರ ಮಾಡಿ ಪ್ರೇಕ್ಷಕರ ಮೆಚ್ಚುಗೆ ಗಳಿಸಿದ ಜಗದೀಶ್, ಮೂಲತಃ ಮಂಡ್ಯ ಜಿಲ್ಲೆಯ ಶೂಟಿಂಗ್ ಮಹಾದೇವಪುರದವರು. ಅಪ್ಪಟ ಮುಗ್ಧತೆ, ಗ್ರಾಮೀಣ ಸೊಗಡಿನ ಮಾತುಗಾರಿಕೆ ಹಾಗೂ ನೈಜ ಕಾಮಿಡಿ ಟೈಮಿಂಗ್ ಹೊಂದಿರುವ ಇವರು ವೇದಿಕೆಯಿಂದಲೇ ಗಮನ ಸೆಳೆದಿದ್ದಾರೆ.",
    "firstImpression": "ಅತ್ಯಂತ ಮುಗ್ಧ, ಡೌನ್ ಟು ಅರ್ಥ್ ಹಾಗೂ ಸಹಜ ಮನರಂಜನೆ ನೀಡುವ ಸ್ಪರ್ಧಿ. ಮನೆಯೊಳಗಿನ ಗಂಭೀರ ಸನ್ನಿವೇಶಗಳನ್ನು ತಿಳಿಗೊಳಿಸುವ ಶಕ್ತಿ ಇವರಿಗಿದೆ.",
    "winProbability": 85,
    "winProbabilityDesc": "85% (ಜನಸಾಮಾನ್ಯರ ಅಪಾರ ಪ್ರೀತಿ ಗಳಿಸುವ ಲಕ್ಷಣಗಳಿದ್ದು, ಕೊನೆಯವರೆಗೂ ಮುಂದುವರಿಯುವ ಭರವಸೆ ಮೂಡಿಸಿದ್ದಾರೆ)",
    "personality": "ಅಪ್ಪಟ ಮುಗ್ಧ ಮನರಂಜಕ (Pure Entertainer)",
    "status": "SAFE",
    "statusKn": "ಸುರಕ್ಷಿತ (🟢 SAFE)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": false,
    "eliminated": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 95,
      "strategy": 84,
      "entertainment": 98,
      "emotion": 88,
      "leadership": 90,
      "drama": 82
    },
    "baggage": {
      "drama": 82,
      "fun": 98,
      "emotion": 88,
      "strategy": 84,
      "anger": 45,
      "leadership": 90
    },
    "stats": {
      "taskWins": 2,
      "nominations": 0,
      "survivalDays": 1,
      "fanVotes": 48500,
      "xp": 2600
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
    "bio": "ಮೂಲತಃ ಮಂಗಳೂರಿನವರಾಗಿದ್ದು ಮಸ್ಕಟ್‌ನಲ್ಲಿ ಬೆಳೆದ ಸೌಂದರ್ಯ, ಹಿಂದಿಯ ಖ್ಯಾತ ರಿಯಾಲಿಟಿ ಶೋ ‘ಸ್ಪ್ಲಿಟ್ಸ್ವಿಲ್ಲಾ 16’ನಲ್ಲಿ ಫೈನಲಿಸ್ಟ್ ಆಗಿ ದೇಶಾದ್ಯಂತ ಸದ್ದು ಮಾಡಿದ್ದವರು. ಗ್ಲಾಮರಸ್ ಮಾಡೆಲ್ ಆಗಿರುವ ಇವರು ನೇರ, ದಿಟ್ಟ ಹಾಗೂ ಬೋಲ್ಡ್ ವ್ಯಕ್ತಿತ್ವಕ್ಕೆ ಹೆಸರಾಗಿದ್ದಾರೆ.",
    "firstImpression": "ಯಾವುದೇ ಮುಲಾಜಿಲ್ಲದೆ ತನ್ನ ನಿಲುವನ್ನು ಸ್ಪಷ್ಟವಾಗಿ ಮಂಡಿಸುವ ಫಿಯರ್‌ಲೆಸ್ ಸ್ಪರ್ಧಿ. ಮನೆಯಲ್ಲಿ ಇವರ ನಡೆ ದೊಡ್ಡ ಸಂಚಲನ ಮೂಡಿಸಲಿದೆ.",
    "winProbability": 80,
    "winProbabilityDesc": "80% (ರಿಯಾಲಿಟಿ ಶೋಗಳ ಅಪಾರ ಅನುಭವವಿದ್ದು, ಗೇಮ್ ಪ್ಲ್ಯಾನ್ ಮಾಡುವಲ್ಲಿ ಮುಂಚೂಣಿಯಲ್ಲಿರಲಿದ್ದಾರೆ)",
    "personality": "ಬೋಲ್ಡ್ & ಫಿಯರ್‌ಲೆಸ್ (Bold Warrior)",
    "status": "CAPTAIN",
    "statusKn": "ಕ್ಯಾಪ್ಟನ್ (👑 CAPTAIN)",
    "captaincyStatus": "ACTIVE_CAPTAIN",
    "nominationStatus": false,
    "eliminated": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 89,
      "strategy": 92,
      "entertainment": 85,
      "emotion": 75,
      "leadership": 84,
      "drama": 94
    },
    "baggage": {
      "drama": 94,
      "fun": 76,
      "emotion": 75,
      "strategy": 92,
      "anger": 75,
      "leadership": 84
    },
    "stats": {
      "taskWins": 0,
      "nominations": 1,
      "survivalDays": 1,
      "fanVotes": 32400,
      "xp": 1950
    },
    "cardRarity": "EPIC"
  },
  {
    "id": "C03",
    "seat": "A02",
    "name": "Avinash Shatamarshana",
    "kannadaName": "ಅವಿನಾಶ್ ಷಠಮರ್ಷಣ್",
    "photo": "/assets/bbk13/contestants/passenger_03_face.jpg",
    "profession": "ಕನ್ನಡ ರಂಗಭೂಮಿ & ಸಿನಿಮಾ ಹಿರಿಯ ನಟ, ನಿರ್ದೇಶಕ, ಬರಹಗಾರ",
    "city": "ಮೈಸೂರು / ಬೆಂಗಳೂರು",
    "age": 42,
    "bio": "ಕನ್ನಡ ರಂಗಭೂಮಿ ಹಾಗೂ ಚಿತ್ರರಂಗದಲ್ಲಿ ನಟ, ಬರಹಗಾರ ಮತ್ತು ನಿರ್ದೇಶಕರಾಗಿ ಸುಮಾರು ವರ್ಷಗಳಿಂದ ಸೇವೆ ಸಲ್ಲಿಸುತ್ತಿರುವ ಹಿರಿಯ ಪ್ರತಿಭೆ. ಹಲವು ಪ್ರಸಿದ್ಧ ನಾಟಕಗಳನ್ನು ನಿರ್ದೇಶಿಸಿರುವ ಇವರು ಪ್ರಬುದ್ಧ ಚಿಂತನೆ ಹಾಗೂ ಆಳವಾದ ಮಾತುಕತೆಗೆ ಹೆಸರುವಾಸಿ.",
    "firstImpression": "ಶಾಂತ, ಬೌದ್ಧಿಕ ಮತ್ತು ತಾರ್ಕಿಕ ವ್ಯಕ್ತಿತ್ವ. ಯಾವುದೇ ಗಲಾಟೆಯಲ್ಲೂ ತಾಳ್ಮೆಯಿಂದ ಪರಿಸ್ಥಿತಿ ನಿಭಾಯಿಸುವ ಸಾಮರ್ಥ್ಯ ತೋರಿಸಿದ್ದಾರೆ.",
    "winProbability": 75,
    "winProbabilityDesc": "75% (ಬುದ್ಧಿವಂತಿಕೆಯ ಆಟದಿಂದ ಗೇಮ್‌ನಲ್ಲಿ ಗಟ್ಟಿಯಾಗಿ ನಿಲ್ಲಬಲ್ಲರು)",
    "personality": "ಪ್ರಬುದ್ಧ ಚಿಂತಕ (Master Mind)",
    "status": "SAFE",
    "statusKn": "ಸುರಕ್ಷಿತ (🟢 SAFE)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": false,
    "eliminated": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 88,
      "strategy": 94,
      "entertainment": 80,
      "emotion": 86,
      "leadership": 92,
      "drama": 62
    },
    "baggage": {
      "drama": 62,
      "fun": 72,
      "emotion": 86,
      "strategy": 94,
      "anger": 38,
      "leadership": 92
    },
    "stats": {
      "taskWins": 1,
      "nominations": 0,
      "survivalDays": 1,
      "fanVotes": 30100,
      "xp": 1850
    },
    "cardRarity": "EPIC"
  },
  {
    "id": "C04",
    "seat": "B02",
    "name": "Prathama Prasad",
    "kannadaName": "ಪ್ರಥಮಾ ಪ್ರಸಾದ್",
    "photo": "/assets/bbk13/contestants/passenger_04_face.jpg",
    "profession": "ಖ್ಯಾತ ನಟಿ ವಿನಯಾ ಪ್ರಸಾದ್ ಪುತ್ರಿ, ಕೂಚಿಪುಡಿ & ಭರತನಾಟ್ಯ ವಿದುಷಿ, ನಟಿ",
    "city": "ಬೆಂಗಳೂರು",
    "age": 35,
    "bio": "ಖ್ಯಾತ ಹಿರಿಯ ನಟಿ ವಿನಯಾ ಪ್ರಸಾದ್ ಅವರ ಸುಪುತ್ರಿ. ಪ್ರಸಿದ್ಧ ಕೂಚಿಪುಡಿ ಹಾಗೂ ಭರತನಾಟ್ಯ ಕಲಾವಿದೆಯಾಗಿರುವ ಇವರು ಕಿರುತೆರೆ ಮತ್ತು ಬೆಳ್ಳಿತೆರೆಯಲ್ಲೂ ನಟಿಯಾಗಿ ಗುರುತಿಸಿಕೊಂಡಿದ್ದಾರೆ. ಕಲೆ ಮತ್ತು ಸಾಂಸ್ಕೃತಿಕ ಹಿನ್ನೆಲೆಯಿಂದ ಬಂದ ಪ್ರತಿಭಾವಂತೆ.",
    "firstImpression": "ಸ್ವಾಭಿಮಾನಿ ಹಾಗೂ ಶಿಸ್ತುಬದ್ಧ ವ್ಯಕ್ತಿತ್ವ. ಮನೆಯ ಆರಂಭದಲ್ಲೇ ಕಿರಣ್ ಶಾಸ್ತ್ರಿ ಅವರೊಂದಿಗೆ ನಡೆದ ಮಾತಿನ ಚಕಮಕಿಯಲ್ಲಿ ತಮ್ಮ ನೇರ ನಿಲುವನ್ನು ತೋರಿಸಿಕೊಟ್ಟಿದ್ದಾರೆ.",
    "winProbability": 78,
    "winProbabilityDesc": "78% (ಟಾಸ್ಕ್‌ಗಳಲ್ಲಿ ಚುರುಕುತನ ಹಾಗೂ ಮಹಿಳಾ ಸ್ಪರ್ಧಿಗಳಲ್ಲಿ ಬಲಿಷ್ಠ ಧ್ವನಿಯಾಗುವ ಸಾಧ್ಯತೆ ಇದೆ)",
    "personality": "ಸ್ವಾಭಿಮಾನಿ ಕಲಾತಾರೆ (Grace & Fire)",
    "status": "SAFE",
    "statusKn": "ಸುರಕ್ಷಿತ (🟢 SAFE)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": false,
    "eliminated": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 89,
      "strategy": 82,
      "entertainment": 84,
      "emotion": 92,
      "leadership": 86,
      "drama": 72
    },
    "baggage": {
      "drama": 72,
      "fun": 80,
      "emotion": 92,
      "strategy": 82,
      "anger": 55,
      "leadership": 86
    },
    "stats": {
      "taskWins": 1,
      "nominations": 0,
      "survivalDays": 1,
      "fanVotes": 29800,
      "xp": 1880
    },
    "cardRarity": "EPIC"
  },
  {
    "id": "C05",
    "seat": "A03",
    "name": "Gagan Chinnappa",
    "kannadaName": "ಗಗನ್ ಚಿನ್ನಪ್ಪ",
    "photo": "/assets/bbk13/contestants/passenger_05_face.jpg",
    "poster": "/assets/bbk13/contestants/passenger_05.jpg",
    "profession": "‘ಮಂಗಳಗೌರಿ ಮದುವೆ’, ‘ಸೀತಾ ರಾಮ’ ಖ್ಯಾತಿಯ ಹ್ಯಾಂಡ್‌ಸಮ್ ನಟ",
    "city": "ಕೊಡಗು / ಬೆಂಗಳೂರು",
    "age": 33,
    "bio": "‘ಮಂಗಳಗೌರಿ ಮದುವೆ’ ಹಾಗೂ ‘ಸೀತಾ ರಾಮ’ ಧಾರಾವಾಹಿಗಳ ಮೂಲಕ ಕಿರುತೆರೆ ವೀಕ್ಷಕರ ಮನಗೆದ್ದಿರುವ ಹ್ಯಾಂಡ್‌ಸಮ್ ನಟ. ಈ ಹಿಂದೆ ‘ಬಿಗ್ ಬಾಸ್ ಮಿನಿ ಸೀಸನ್’ನಲ್ಲಿ ಭಾಗವಹಿಸಿ ಅನುಭವ ಪಡೆದುಕೊಂಡಿದ್ದು, ಇದೀಗ ಪೂರ್ಣ ಪ್ರಮಾಣದ ಸ್ಪರ್ಧಿಯಾಗಿ ಬಂದಿದ್ದಾರೆ.",
    "firstImpression": "ಆತ್ಮವಿಶ್ವಾಸ, ಉತ್ತಮ ಮ್ಯಾನರಿಸಂ ಹಾಗೂ ನಾಯಕತ್ವದ ಗುಣಗಳನ್ನು ಪ್ರದರ್ಶಿಸಿದ್ದಾರೆ.",
    "winProbability": 88,
    "winProbabilityDesc": "88% (ಅಪಾರ ಅಭಿಮಾನಿ ಬಳಗ, ರಿಯಾಲಿಟಿ ಶೋ ಅನುಭವ ಹಾಗೂ ಫಿಟ್‌ನೆಸ್ ಇವರಿಗೆ ಪ್ಲಸ್ ಪಾಯಿಂಟ್)",
    "personality": "ಡ್ಯಾಶಿಂಗ್ ಲೀಡರ್ (Dashing Leader)",
    "status": "NOMINATED",
    "statusKn": "ನಾಮಿನೇಟೆಡ್ (🔴 NOMINATED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": true,
    "eliminated": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 95,
      "strategy": 88,
      "entertainment": 89,
      "emotion": 82,
      "leadership": 94,
      "drama": 74
    },
    "baggage": {
      "drama": 74,
      "fun": 86,
      "emotion": 80,
      "strategy": 88,
      "anger": 48,
      "leadership": 94
    },
    "stats": {
      "taskWins": 1,
      "nominations": 0,
      "survivalDays": 1,
      "fanVotes": 44200,
      "xp": 2350
    },
    "cardRarity": "LEGENDARY"
  },
  {
    "id": "C06",
    "seat": "B03",
    "name": "Sangeetha Bhat",
    "kannadaName": "ಸಂಗೀತಾ ಭಟ್",
    "photo": "/assets/bbk13/contestants/passenger_06_face.jpg",
    "poster": "/assets/bbk13/contestants/passenger_06.jpg",
    "profession": "‘ಎರಡನೇ ಸಲ’ ಖ್ಯಾತಿಯ ನಟಿ & ಸುದರ್ಶನ್ ರಂಗಪ್ರಸಾದ್ ಪತ್ನಿ",
    "city": "ಮೈಸೂರು / ಬೆಂಗಳೂರು",
    "age": 32,
    "bio": "‘ಪ್ರೀತಿ ಗೀತಿ ಇತ್ಯಾದಿ’, ‘ಎರಡನೇ ಸಲ’ ಸಿನಿಮಾಗಳ ನಾಯಕಿ. ನಟ ಸುದರ್ಶನ್ ರಂಗಪ್ರಸಾದ್ ಅವರ ಧರ್ಮಪತ್ನಿ. ಇತ್ತೀಚೆಗೆ ಶಸ್ತ್ರಚಿಕಿತ್ಸೆಗೆ ಒಳಗಾಗಿ ಚೇತರಿಸಿಕೊಂಡು ದೊಡ್ಮನೆಗೆ ಬಂದಿರುವ ಇವರಿಗೆ ಒಸಿಡಿ (OCD - ಸ್ವಚ್ಛತೆಯ ಹಠ) ಸ್ವಭಾವವಿದೆ.",
    "firstImpression": "ನೇರ ಮಾತು ಹಾಗೂ ಸ್ವಚ್ಛತೆಯ ವಿಷಯದಲ್ಲಿ ಕಾಂಪ್ರಮೈಸ್ ಆಗದ ಗಟ್ಟಿ ವ್ಯಕ್ತಿತ್ವ. ಮನೆಯವರೊಂದಿಗೆ ಜಗಳ ಅಥವಾ ಸಮನ್ವಯ ಎರಡರಲ್ಲೂ ಪ್ರಮುಖ ಕೇಂದ್ರಬಿಂದುವಾಗಲಿದ್ದಾರೆ.",
    "winProbability": 82,
    "winProbabilityDesc": "82% (ಭಾವನಾತ್ಮಕವಾಗಿ ಹಾಗೂ ಮಾನಸಿಕವಾಗಿ ಪ್ರಬಲ ಆಟಗಾರ್ತಿ)",
    "personality": "ದೃಢ ಸಂಕಲ್ಪದ ನಾಯಕಿ (Strong Will)",
    "status": "NOMINATED",
    "statusKn": "ನಾಮಿನೇಟೆಡ್ (🔴 NOMINATED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": true,
    "eliminated": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 91,
      "strategy": 86,
      "entertainment": 84,
      "emotion": 92,
      "leadership": 82,
      "drama": 88
    },
    "baggage": {
      "drama": 88,
      "fun": 76,
      "emotion": 92,
      "strategy": 86,
      "anger": 68,
      "leadership": 82
    },
    "stats": {
      "taskWins": 0,
      "nominations": 1,
      "survivalDays": 1,
      "fanVotes": 34100,
      "xp": 1980
    },
    "cardRarity": "EPIC"
  },
  {
    "id": "C07",
    "seat": "A04",
    "name": "Kavya Gowda",
    "kannadaName": "ಕಾವ್ಯ ಗೌಡ",
    "photo": "/assets/bbk13/contestants/passenger_07_face.jpg",
    "poster": "/assets/bbk13/contestants/passenger_07.jpg",
    "profession": "‘ಭಾಗ್ಯಲಕ್ಷ್ಮೀ’ ಶ್ರೇಷ್ಠಾ ಖ್ಯಾತಿಯ ನಟಿ & ‘ಕ್ವಾಟ್ಲೆ ಕಿಚನ್’ ಸ್ಪರ್ಧಿ",
    "city": "ಹಾಸನ / ಬೆಂಗಳೂರು",
    "age": 28,
    "bio": "‘ಭಾಗ್ಯಲಕ್ಷ್ಮೀ’ ಧಾರಾವಾಹಿಯ ಶ್ರೇಷ್ಠಾ ಪಾತ್ರದ ಮೂಲಕ ಮನೆಮಾತಾಗಿರುವ ಖಳನಾಯಕಿ. ಇತ್ತೀಚೆಗೆ ‘ಕ್ವಾಟ್ಲೆ ಕಿಚನ್’ ಶೋನಲ್ಲೂ ಭಾಗವಹಿಸಿದ್ದರು. ವಿಶೇಷವೆಂದರೆ, ಆ ಸೀರಿಯಲ್‌ನಲ್ಲಿ ಇವರ ನಾಯಕನಾಗಿದ್ದ ಸುದರ್ಶನ್ ಅವರ ರಿಯಲ್ ವೈಫ್ ಸಂಗೀತಾ ಭಟ್ ಜೊತೆಯಲ್ಲೇ ಇವರು ಮನೆ ಪ್ರವೇಶಿಸಿದ್ದಾರೆ.",
    "firstImpression": "ಚುರುಕು, ಬಬ್ಲಿ ಹಾಗೂ ಗೇಮ್‌ಗೆ ತಕ್ಕಂತೆ ಹೊಂದಿಕೊಳ್ಳುವ ಸ್ವಭಾವ. ಸಂಗೀತಾ ಅವರೊಂದಿಗಿನ ಇವರ ಸಮೀಕರಣ ಕುತೂಹಲ ಮೂಡಿಸಿದೆ.",
    "winProbability": 80,
    "winProbabilityDesc": "80% (ಕಿರುತೆರೆ ವೀಕ್ಷಕರ ಬೆಂಬಲ ಮತ್ತು ತಂತ್ರಗಾರಿಕೆಯ ಆಟ ಇವರ ಬಲ)",
    "personality": "ಚುರುಕಿನ ತಂತ್ರಗಾರ್ತಿ (Clever & Bubbly)",
    "status": "SAFE",
    "statusKn": "ಸುರಕ್ಷಿತ (🟢 SAFE)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": false,
    "eliminated": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 93,
      "strategy": 86,
      "entertainment": 92,
      "emotion": 82,
      "leadership": 80,
      "drama": 76
    },
    "baggage": {
      "drama": 76,
      "fun": 92,
      "emotion": 82,
      "strategy": 86,
      "anger": 46,
      "leadership": 80
    },
    "stats": {
      "taskWins": 1,
      "nominations": 0,
      "survivalDays": 1,
      "fanVotes": 40500,
      "xp": 2280
    },
    "cardRarity": "LEGENDARY"
  },
  {
    "id": "C08",
    "seat": "B04",
    "name": "Om Prakash Rao",
    "kannadaName": "ಓಂ ಪ್ರಕಾಶ್ ರಾವ್",
    "photo": "/assets/bbk13/contestants/passenger_08_face.jpg",
    "poster": "/assets/bbk13/contestants/passenger_08.jpg",
    "profession": "ಕನ್ನಡ ಚಿತ್ರರಂಗದ ಮಾಸ್ ನಿರ್ದೇಶಕ & ನಟ",
    "city": "ಬೆಂಗಳೂರು",
    "age": 58,
    "bio": "ಕನ್ನಡ ಚಿತ್ರರಂಗದ ಮಾಸ್ ನಿರ್ದೇಶಕ ಹಾಗೂ ನಟ. ಬಿಗ್ ಬಾಸ್ ಕನ್ನಡ ಸೀಸನ್ 4ರಲ್ಲಿ ಭಾಗವಹಿಸಿ ಅನಾರೋಗ್ಯದ ಕಾರಣ ಅರ್ಧದಲ್ಲೇ ಹೊರಬಂದಿದ್ದರು. ಇತ್ತೀಚೆಗೆ ‘ಕ್ವಾಟ್ಲೆ ಕಿಚನ್ ಸೀಸನ್ 2’ನಲ್ಲಿ ತಮ್ಮ ಪಾಕಶಾಸ್ತ್ರ ಕೌಶಲ್ಯದಿಂದ ಜನಮನ ಗೆದ್ದಿದ್ದರು.",
    "firstImpression": "ದೊಡ್ಮನೆಯ ಹಿರಿಯಣ್ಣ. ಅಡುಗೆ ಮನೆಯ ಉಸ್ತುವಾರಿ ಹಾಗೂ ಕಥೆ-ಜೋಕ್‌ಗಳ ಮೂಲಕ ಎಲ್ಲರನ್ನೂ ಹಿಡಿದಿಟ್ಟುಕೊಳ್ಳುವ ಆಕರ್ಷಕ ವ್ಯಕ್ತಿತ್ವ.",
    "winProbability": 76,
    "winProbabilityDesc": "76% (ಅನುಭವ ದೊಡ್ಡದಿದ್ದರೂ, ದೈಹಿಕ ಟಾಸ್ಕ್‌ಗಳನ್ನು ನಿಭಾಯಿಸುವುದರ ಮೇಲೆ ಇವರ ಪಯಣ ನಿರ್ಧಾರವಾಗಲಿದೆ)",
    "personality": "ದೊಡ್ಮನೆಯ ಮಾಸ್ ಹಿರಿಯಣ್ಣ (The Mass Veteran)",
    "status": "NOMINATED",
    "statusKn": "ನಾಮಿನೇಟೆಡ್ (🔴 NOMINATED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": true,
    "eliminated": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 94,
      "strategy": 90,
      "entertainment": 94,
      "emotion": 78,
      "leadership": 96,
      "drama": 96
    },
    "baggage": {
      "drama": 96,
      "fun": 85,
      "emotion": 76,
      "strategy": 90,
      "anger": 85,
      "leadership": 96
    },
    "stats": {
      "taskWins": 0,
      "nominations": 1,
      "survivalDays": 1,
      "fanVotes": 42300,
      "xp": 2450
    },
    "cardRarity": "LEGENDARY"
  },
  {
    "id": "C09",
    "seat": "A05",
    "name": "Kiran Shastri",
    "kannadaName": "ಕಿರಣ್ ಶಾಸ್ತ್ರಿ",
    "photo": "/assets/bbk13/contestants/passenger_09_face.jpg",
    "poster": "/assets/bbk13/contestants/passenger_09.jpg",
    "profession": "ಬಾಗಲಕೋಟೆ ಪ್ರತಿಭೆ & ‘ಅಗ್ನಿಪರೀಕ್ಷೆ’ ಸಾರ್ವಜನಿಕ ವೋಟಿಂಗ್ ವಿನ್ನರ್",
    "city": "ಬಾಗಲಕೋಟೆ",
    "age": 34,
    "bio": "ಬಾಗಲಕೋಟೆ ಮೂಲದ ಕಿರಣ್ ಶಾಸ್ತ್ರಿ, ‘ಬಿಗ್ ಬಾಸ್ ಅಗ್ನಿಪರೀಕ್ಷೆ’ ಶೋನಲ್ಲಿ ಅತಿ ಹೆಚ್ಚು ಸಾರ್ವಜನಿಕ ಮತಗಳನ್ನು ಪಡೆದು ಮುಖ್ಯ ವೇದಿಕೆಗೆ ಆಯ್ಕೆಯಾದ ಪ್ರತಿಭೆ. ಮಾತುಗಾರಿಕೆ ಹಾಗೂ ವಾದ ಮಾಡುವುದರಲ್ಲಿ ಎತ್ತಿದ ಕೈ.",
    "firstImpression": "ಹೆಚ್ಚು ಮಾತನಾಡುವ, ಚರ್ಚೆಗಿಳಿಯುವ ಆಕ್ರಮಣಕಾರಿ ವ್ಯಕ್ತಿತ್ವ. ಪ್ರವೇಶಿಸುತ್ತಿದ್ದಂತೆಯೇ ಪ್ರಥಮಾ ಪ್ರಸಾದ್ ಜೊತೆ ವಾದಕ್ಕಿಳಿದು ಮೊದಲ ದಿನವೇ ಸದ್ದು ಮಾಡಿದ್ದಾರೆ.",
    "winProbability": 70,
    "winProbabilityDesc": "70% (ಮಾತು ಅತಿಯಾದರೆ ಮನೆಯವರಿಗೆ ಕಿರಿಕಿರಿಯಾಗಬಹುದು; ನಿಯಂತ್ರಣ ಸಾಧಿಸಿದರೆ ಮುಂದಕ್ಕೆ ಸಾಗಲಿದ್ದಾರೆ)",
    "personality": "ಪ್ರಖರ ವಾಗ್ಮಿ (Fire Debater)",
    "status": "SAFE",
    "statusKn": "ಸುರಕ್ಷಿತ (🟢 SAFE)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": false,
    "eliminated": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 86,
      "strategy": 88,
      "entertainment": 82,
      "emotion": 78,
      "leadership": 82,
      "drama": 88
    },
    "baggage": {
      "drama": 88,
      "fun": 70,
      "emotion": 78,
      "strategy": 88,
      "anger": 72,
      "leadership": 82
    },
    "stats": {
      "taskWins": 0,
      "nominations": 0,
      "survivalDays": 1,
      "fanVotes": 26800,
      "xp": 1550
    },
    "cardRarity": "RARE"
  },
  {
    "id": "C10",
    "seat": "B05",
    "name": "Asiya Firdose",
    "kannadaName": "ಆಸಿಯಾ ಫಿರ್ದೋಸ್",
    "photo": "/assets/bbk13/contestants/passenger_10_face.jpg",
    "poster": "/assets/bbk13/contestants/passenger_10.jpg",
    "profession": "‘ಕನ್ಯಾಕುಮಾರಿ’, ‘ಶ್ರಾವಣಿ ಸುಬ್ರಮಣ್ಯ’ ಖ್ಯಾತಿಯ ಯುವ ನಟಿ",
    "city": "ಮಂಗಳೂರು / ಬೆಂಗಳೂರು",
    "age": 26,
    "bio": "‘ಕನ್ಯಾಕುಮಾರಿ’ ಹಾಗೂ ‘ಶ್ರಾವಣಿ ಸುಬ್ರಮಣ್ಯ’ ಧಾರಾವಾಹಿಗಳಲ್ಲಿ ಪ್ರಮುಖ ಪಾತ್ರಗಳಲ್ಲಿ ನಟಿಸಿರುವ ಯುವ ನಟಿ. ಸೀರಿಯಲ್ ಮುಗಿದ ಬೆನ್ನಲ್ಲೇ ಬಿಗ್ ಬಾಸ್ ವೇದಿಕೆ ಹತ್ತಿರುವ ಇವರು ಸೋಶಿಯಲ್ ಮೀಡಿಯಾದಲ್ಲೂ ಅಪಾರ ಫಾಲೋವರ್ಸ್ ಹೊಂದಿದ್ದಾರೆ.",
    "firstImpression": "ಫನ್ ಲವಿಂಗ್, ಉತ್ಸಾಹಿ ಹಾಗೂ ಸದಾ ನಗುಮುಖದಿಂದ ಕೂಡಿರುವ ಕ್ಯೂಟ್ ಸ್ಪರ್ಧಿ.",
    "winProbability": 77,
    "winProbabilityDesc": "77% (ಯುವ ಪ್ರೇಕ್ಷಕರ ವೋಟಿಂಗ್ ಬೆಂಬಲವಿದ್ದು, ಮನೆಯ ಒಳಗೆ ಡ್ರಾಮಾಗಳನ್ನು ಹೇಗೆ ನಿಭಾಯಿಸುತ್ತಾರೆ ಎಂಬುದರ ಮೇಲೆ ಗೆಲುವು ನಿಂತಿದೆ)",
    "personality": "ಕ್ಯೂಟ್ & ಚಾರ್ಮಿಂಗ್ (Sweet Youth Icon)",
    "status": "NOMINATED",
    "statusKn": "ನಾಮಿನೇಟೆಡ್ (🔴 NOMINATED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": true,
    "eliminated": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 90,
      "strategy": 80,
      "entertainment": 88,
      "emotion": 86,
      "leadership": 78,
      "drama": 68
    },
    "baggage": {
      "drama": 68,
      "fun": 88,
      "emotion": 86,
      "strategy": 80,
      "anger": 38,
      "leadership": 78
    },
    "stats": {
      "taskWins": 0,
      "nominations": 0,
      "survivalDays": 1,
      "fanVotes": 32500,
      "xp": 1880
    },
    "cardRarity": "EPIC"
  },
  {
    "id": "C11",
    "seat": "A06",
    "name": "Likhith Gondi",
    "kannadaName": "ಲಿಖಿತ್ ಗೊಂದಿ",
    "photo": "/assets/bbk13/contestants/passenger_11_face.jpg",
    "poster": "/assets/bbk13/contestants/passenger_11.jpg",
    "profession": "‘ಅಗ್ನಿಪರೀಕ್ಷೆ’ ವಿನ್ನರ್ & ಫಿಟ್‌ನೆಸ್ ವಾರಿಯರ್",
    "city": "ಮಂಡ್ಯ / ಬೆಂಗಳೂರು",
    "age": 26,
    "bio": "‘ಅಗ್ನಿಪರೀಕ್ಷೆ’ ಸ್ಪರ್ಧೆಯಲ್ಲಿ ಭರ್ಜರಿ ಪರ್ಫಾರ್ಮೆನ್ಸ್ ನೀಡಿ ಜನರಿಂದ ನೇರ ಮತ ಪಡೆದು ಆಯ್ಕೆಯಾದ ಸ್ಪರ್ಧಿ. ಅತ್ಯಂತ ಫಿಟ್ ಆಗಿರುವ ಇವರು ದೈಹಿಕ ಹಾಗೂ ಮಾನಸಿಕ ಟಾಸ್ಕ್‌ಗಳಲ್ಲಿ ಪಳಗಿದ್ದಾರೆ.",
    "firstImpression": "ಸೈಲೆಂಟ್ ಆದರೆ ಕಿಲ್ಲರ್ ಆಟಗಾರ. ಟಾಸ್ಕ್ ವೇಳೆ ಪೂರ್ಣ ಏಕಾಗ್ರತೆ ತೋರುವ ಕ್ರೀಡಾಪಟುವಿನ ಮನಸ್ಥಿತಿ.",
    "winProbability": 83,
    "winProbabilityDesc": "83% (ದೈಹಿಕ ಟಾಸ್ಕ್‌ಗಳಲ್ಲಿ ಇವರನ್ನು ಮಣಿಸುವುದು ಇತರರಿಗೆ ಕಷ್ಟವಾಗಲಿದ್ದು, ಫಿನಾಲೆ ರೇಸ್‌ನ ಪ್ರಬಲ ಸ್ಪರ್ಧಿ)",
    "personality": "ಸೈಲೆಂಟ್ ಕಿಲ್ಲರ್ (Task Beast)",
    "status": "SAFE",
    "statusKn": "ಸುರಕ್ಷಿತ (🟢 SAFE)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": false,
    "eliminated": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 91,
      "strategy": 88,
      "entertainment": 78,
      "emotion": 80,
      "leadership": 86,
      "drama": 60
    },
    "baggage": {
      "drama": 60,
      "fun": 76,
      "emotion": 80,
      "strategy": 88,
      "anger": 52,
      "leadership": 86
    },
    "stats": {
      "taskWins": 1,
      "nominations": 0,
      "survivalDays": 1,
      "fanVotes": 35600,
      "xp": 2050
    },
    "cardRarity": "EPIC"
  },
  {
    "id": "C12",
    "seat": "B06",
    "name": "Tandav Ram",
    "kannadaName": "ತಾಂಡವ್ ರಾಮ್",
    "photo": "/assets/bbk13/contestants/passenger_12_face.jpg",
    "poster": "/assets/bbk13/contestants/passenger_12.jpg",
    "profession": "‘ಜೋಡಿ ಹಕ್ಕಿ’ ಖ್ಯಾತಿಯ ನಟ, ನ್ಯಾಷನಲ್ ಬಾಡಿ ಬಿಲ್ಡರ್ & ಕುಸ್ತಿ ಪಟು",
    "city": "ಹಾಸನ",
    "age": 31,
    "bio": "‘ಜೋಡಿ ಹಕ್ಕಿ’ ಖ್ಯಾತಿಯ ನಟ, ನ್ಯಾಷನಲ್ ಲೆವೆಲ್ ಬಾಡಿ ಬಿಲ್ಡರ್ ಹಾಗೂ ಕುಸ್ತಿ ಪಟು. ಹಾಸನ ಮೂಲದ ಇವರು ಇತ್ತೀಚೆಗೆ ‘ಕ್ವಾಟ್ಲೆ ಕಿಚನ್’ ಶೋನಲ್ಲೂ ಭಾಗವಹಿಸಿದ್ದರು. ಜೀವನದಲ್ಲಿ ದೊಡ್ಡ ಸಾಧನೆ ಮಾಡಿ ಮದುವೆಯಾಗಬೇಕೆಂಬ ಹಂಬಲ ಹೊತ್ತಿದ್ದಾರೆ.",
    "firstImpression": "ಅಪ್ರತಿಮ ದೈಹಿಕ ಶಕ್ತಿ, ಸಭ್ಯತೆ ಹಾಗೂ ಗುರಿ ಮುಟ್ಟುವ ಗಟ್ಟಿತನ.",
    "winProbability": 87,
    "winProbabilityDesc": "87% (ಕನ್ನಡ ರಿಯಾಲಿಟಿ ಶೋಗಳಲ್ಲಿ ಆ್ಯಕ್ಷನ್ ಮತ್ತು ನೇರ ವ್ಯಕ್ತಿತ್ವದ ಹುಡುಗರಿಗೆ ಸಿಗುವ ಜನಪ್ರಿಯತೆ ಇವರಿಗೆ ವರದಾನ)",
    "personality": "ಕರುನಾಡ ಪೈಲ್ವಾನ್ (Gentle Giant)",
    "status": "NOMINATED",
    "statusKn": "ನಾಮಿನೇಟೆಡ್ (🔴 NOMINATED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": true,
    "eliminated": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 93,
      "strategy": 84,
      "entertainment": 85,
      "emotion": 88,
      "leadership": 90,
      "drama": 65
    },
    "baggage": {
      "drama": 65,
      "fun": 82,
      "emotion": 88,
      "strategy": 84,
      "anger": 58,
      "leadership": 90
    },
    "stats": {
      "taskWins": 1,
      "nominations": 0,
      "survivalDays": 1,
      "fanVotes": 41200,
      "xp": 2280
    },
    "cardRarity": "LEGENDARY"
  },
  {
    "id": "C13",
    "seat": "A07",
    "name": "Vaishnavi",
    "kannadaName": "ವೈಷ್ಣವಿ",
    "photo": "/assets/bbk13/contestants/passenger_13_face.jpg",
    "poster": "/assets/bbk13/contestants/passenger_13.jpg",
    "profession": "‘ಪ್ರೇಮ ಕಾವ್ಯ’ ಸೀರಿಯಲ್ ನಟಿ & ‘ಬಿಗ್ ಬಾಸ್ ಮಿನಿ’ ಸ್ಪರ್ಧಿ",
    "city": "ಬೆಂಗಳೂರು",
    "age": 26,
    "bio": "‘ಪ್ರೇಮ ಕಾವ್ಯ’ ಸೀರಿಯಲ್ ನಟಿ ಹಾಗೂ ಈ ಹಿಂದೆ ‘ಬಿಗ್ ಬಾಸ್ ಮಿನಿ ಸೀಸನ್’ನಲ್ಲಿ ಮಿಂಚಿದ್ದ ಸ್ಪರ್ಧಿ. ಇವರಿಗೂ ಸ್ವಚ್ಛತೆಯ ಕಡೆಗೆ ತೀವ್ರ ಗಮನ (OCD) ಕೊಡುವ ಅಭ್ಯಾಸವಿದೆ.",
    "firstImpression": "ಮುದ್ದಾದ ನಗು, ಸೂಕ್ಷ್ಮ ಮನಸ್ಸು ಹಾಗೂ ಮನೆಯ ಜವಾಬ್ದಾರಿಗಳನ್ನು ತಕ್ಷಣವೇ ನಿಭಾಯಿಸುವ ಆಸಕ್ತಿ.",
    "winProbability": 74,
    "winProbabilityDesc": "74% (ಮನೆಯ ಒತ್ತಡಗಳನ್ನು ಸಕಾರಾತ್ಮಕವಾಗಿ ಎದುರಿಸಿದರೆ ದೀರ್ಘಕಾಲ ಉಳಿಯಲಿದ್ದಾರೆ)",
    "personality": "ಸೂಕ್ಷ್ಮ ಸಂವೇದನೆಯ ತಾರೆ (Sweet & Delicate)",
    "status": "SAFE",
    "statusKn": "ಸುರಕ್ಷಿತ (🟢 SAFE)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": false,
    "eliminated": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 87,
      "strategy": 78,
      "entertainment": 84,
      "emotion": 90,
      "leadership": 76,
      "drama": 66
    },
    "baggage": {
      "drama": 66,
      "fun": 84,
      "emotion": 90,
      "strategy": 78,
      "anger": 40,
      "leadership": 76
    },
    "stats": {
      "taskWins": 0,
      "nominations": 0,
      "survivalDays": 1,
      "fanVotes": 27900,
      "xp": 1650
    },
    "cardRarity": "RARE"
  },
  {
    "id": "C14",
    "seat": "B07",
    "name": "Dhanush Manjunath",
    "kannadaName": "ಧನುಷ್ ಮಂಜುನಾಥ್",
    "photo": "/assets/bbk13/contestants/passenger_14_face.jpg",
    "poster": "/assets/bbk13/contestants/passenger_14.jpg",
    "profession": "ಗಿನ್ನೆಸ್ ವರ್ಲ್ಡ್ ರೆಕಾರ್ಡ್ ಹೋಲ್ಡರ್ & ‘ಅಗ್ನಿಪರೀಕ್ಷೆ’ ಸಾಹಸಿ ಯುವಕ",
    "city": "ಶಿವಮೊಗ್ಗ / ಬೆಂಗಳೂರು",
    "age": 27,
    "bio": "‘ಅಗ್ನಿಪರೀಕ್ಷೆ’ ಗೆದ್ದು ಬಂದ ಗಿನ್ನೆಸ್ ವರ್ಲ್ಡ್ ರೆಕಾರ್ಡ್ ಹೋಲ್ಡರ್. ಬಿಗ್ ಬಾಸ್ ಶೋಗಾಗಿ ತಮ್ಮ ಗಿನ್ನೆಸ್ ರೆಕಾರ್ಡ್ ಸರ್ಟಿಫಿಕೇಟ್ ಹರಿದುಹಾಕಿ ಛಲದಿಂದ ಬಂದಿರುವ ಸಾಹಸಿ ಯುವಕ. ಜೀವನದಲ್ಲಿ ಹಲವು ತಿರಸ್ಕಾರಗಳನ್ನು ಎದುರಿಸಿ ಮೇಲೆ ಬಂದವರು.",
    "firstImpression": "ಛಲ, ತೀವ್ರ ಆವೇಗ ಹಾಗೂ ತನಗೆ ತಾನೇ ಸಾಬೀತುಪಡಿಸಿಕೊಳ್ಳಬೇಕೆಂಬ ಅದಮ್ಯ ಉತ್ಸಾಹ.",
    "winProbability": 86,
    "winProbabilityDesc": "86% (ಭಾವನಾತ್ಮಕ ಕನೆಕ್ಟ್ ಹಾಗೂ ಟಾಸ್ಕ್ ಸಾಮರ್ಥ್ಯ ಇವರನ್ನು ಟಾಪ್ ಹಂತಕ್ಕೆ ಕೊಂಡೊಯ್ಯಬಲ್ಲದು)",
    "personality": "ಛಲದ ಸಾಹಸಿ (Fearless Record Maker)",
    "status": "NOMINATED",
    "statusKn": "ನಾಮಿನೇಟೆಡ್ (🔴 NOMINATED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": true,
    "eliminated": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 92,
      "strategy": 86,
      "entertainment": 84,
      "emotion": 94,
      "leadership": 88,
      "drama": 78
    },
    "baggage": {
      "drama": 78,
      "fun": 82,
      "emotion": 94,
      "strategy": 86,
      "anger": 66,
      "leadership": 88
    },
    "stats": {
      "taskWins": 1,
      "nominations": 0,
      "survivalDays": 1,
      "fanVotes": 39100,
      "xp": 2200
    },
    "cardRarity": "LEGENDARY"
  },
  {
    "id": "C15",
    "seat": "A08",
    "name": "Yashas Krishna",
    "kannadaName": "ಯಶಸ್ ಕೃಷ್ಣ",
    "photo": "/assets/bbk13/contestants/passenger_15_face.jpg",
    "poster": "/assets/bbk13/contestants/passenger_15.jpg",
    "profession": "‘ಪವಿತ್ರ ಬಂಧನ’ ನಟ & ಕಿಚ್ಚ ಸುದೀಪ್ ಕಟ್ಟಾ ಅಭಿಮಾನಿ",
    "city": "ಮಂಡ್ಯ",
    "age": 28,
    "bio": "‘ಪವಿತ್ರ ಬಂಧನ’ ಧಾರಾವಾಹಿಯ ನಟ, ಮಂಡ್ಯ ಮೂಲದ ಇಂಜಿನಿಯರಿಂಗ್ ಪದವೀಧರ. ಕಿಚ್ಚ ಸುದೀಪ್ ಅವರ ಕಟ್ಟಾ ಅಭಿಮಾನಿ. ತಮ್ಮ ತಾಯಿಯ ಆಸೆಯಂತೆ ಈ ರಿಯಾಲಿಟಿ ಶೋ ಪ್ರವೇಶಿಸಿದ್ದಾರೆ.",
    "firstImpression": "ಹ್ಯಾಂಡ್‌ಸಮ್, ಮುಕ್ತ ಮಾತು ಹಾಗೂ ಇತರರನ್ನು ಬೇಗ ನಂಬುವ ನೇರ ಹೃದಯಿ. ಯುವತಿಯರ ನೆಚ್ಚಿನ ಸ್ಪರ್ಧಿಯಾಗುವ ಲಕ್ಷಣಗಳಿವೆ.",
    "winProbability": 81,
    "winProbabilityDesc": "81% (ಸಹಜ ನಡವಳಿಕೆ ಹಾಗೂ ಅಭಿಮಾನಿಗಳ ಬೆಂಬಲದಿಂದ ಪ್ರಬಲ ಸ್ಪರ್ಧೆ ನೀಡಲಿದ್ದಾರೆ)",
    "personality": "ನೇರ ಹೃದಯಿ ಹ್ಯಾಂಡ್‌ಸಮ್ (Pure Heart)",
    "status": "SAFE",
    "statusKn": "ಸುರಕ್ಷಿತ (🟢 SAFE)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": false,
    "eliminated": false,
    "entryDate": "Day 01",
    "scores": {
      "popularity": 90,
      "strategy": 82,
      "entertainment": 86,
      "emotion": 88,
      "leadership": 82,
      "drama": 68
    },
    "baggage": {
      "drama": 68,
      "fun": 86,
      "emotion": 88,
      "strategy": 82,
      "anger": 45,
      "leadership": 82
    },
    "stats": {
      "taskWins": 0,
      "nominations": 0,
      "survivalDays": 1,
      "fanVotes": 33900,
      "xp": 1920
    },
    "cardRarity": "EPIC"
  },
  {
    "id": "C16",
    "seat": "B08",
    "name": "Modern Mahakavi Manja",
    "kannadaName": "ಮಾಡ್ರನ್ ಮಹಾಕವಿ ಮಂಜ",
    "photo": "/assets/bbk13/contestants/passenger_16_face.jpg",
    "poster": "/assets/bbk13/contestants/passenger_16.jpg",
    "profession": "‘ಅಗ್ನಿಪರೀಕ್ಷೆ’ ಜಡ್ಜಸ್ ವಿಶೇಷ ಆಯ್ಕೆಯ ಕಾಮನ್ನರ್ ಕವಿ & ಹಾಸ್ಯಗಾರ",
    "city": "ಚಿತ್ರದುರ್ಗ / ಬೆಂಗಳೂರು",
    "age": 30,
    "bio": "‘ಅಗ್ನಿಪರೀಕ್ಷೆ’ ವೇದಿಕೆಯಲ್ಲಿ ತೀರ್ಪುಗಾರರ (Judges) ವಿಶೇಷ ಆಯ್ಕೆಯಾಗಿ ನೇರವಾಗಿ ಬಿಗ್ ಬಾಸ್ ಮುಖ್ಯ ಮನೆಗೆ ಲಗ್ಗೆಯಿಟ್ಟ ಕಾಮನ್ನರ್ ಸ್ಪರ್ಧಿ. ವಿಶಿಷ್ಟ ಕವನಗಳು, ಪ್ರಾಸಬದ್ಧ ಮಾತುಗಳು ಹಾಗೂ ನವ್ಯ ಹಾಸ್ಯ ಶೈಲಿಗೆ ಹೆಸರಾದವರು.",
    "firstImpression": "ಅನ್‌ಪ್ರೆಡಿಕ್ಟೇಬಲ್ ಮನರಂಜನೆ, ಜಾಣ್ಮೆ ಹಾಗೂ ತನ್ನದೇ ಆದ ಹಳ್ಳಿ ಶೈಲಿಯ ವಿಶಿಷ್ಟ ಆಕರ್ಷಣೆ.",
    "winProbability": 79,
    "winProbabilityDesc": "79% (ಕಾಮನ್ನರ್ ಕಾರ್ಡ್ ಮತ್ತು ಮನರಂಜನೆಯಿಂದ ವೀಕ್ಷಕರ ಅಚ್ಚುಮೆಚ್ಚಿನ ಡಾರ್ಕ್ ಹಾರ್ಸ್ ಆಗಿ ಹೊರಹೊಮ್ಮಬಹುದು)",
    "personality": "ಮಾಡ್ರನ್ ಮಹಾಕವಿ (Poetic Entertainer)",
    "status": "ELIMINATED",
    "statusKn": "ರೆಡ್ ಕಾರ್ಡ್ ಎಲಿಮಿನೇಟೆಡ್ (🔴 RED CARD EVICTED)",
    "captaincyStatus": "PASSENGER",
    "nominationStatus": false,
    "eliminated": true,
    "eliminationReason": "ರೂಲ್ಸ್ ಉಲ್ಲಂಘನೆ & ರೆಡ್ ಕಾರ್ಡ್ (Direct Red Card Ejection by Kiccha Sudeep)",
    "entryDate": "Day 01",
    "scores": {
      "popularity": 92,
      "strategy": 84,
      "entertainment": 97,
      "emotion": 85,
      "leadership": 82,
      "drama": 76
    },
    "baggage": {
      "drama": 76,
      "fun": 97,
      "emotion": 85,
      "strategy": 84,
      "anger": 48,
      "leadership": 82
    },
    "stats": {
      "taskWins": 1,
      "nominations": 0,
      "survivalDays": 1,
      "fanVotes": 38700,
      "xp": 2250
    },
    "cardRarity": "LEGENDARY"
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