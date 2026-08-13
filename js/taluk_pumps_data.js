/**
 * taluk_pumps_data.js — Karnata Fuel Engine
 * Master dataset of 29 Karnataka Districts with 150+ Taluks / Areas, Outlet IDs, Lat/Lng coordinates & HPCL/IOCL/BPCL Master Outlets.
 */

const TALUK_FUEL_PUMPS = {
  bagalkot: {
    districtKn: "ಬಾಗಲಕೋಟೆ",
    districtEn: "Bagalkot",
    pumps: [
      { taluk: "Bagalkot", talukKn: "ಬಾಗಲಕೋಟೆ", outlet_id: "390716", outlet_name: "M/s Shri Siddarameswar Petroleums", lat: 16.200178, lng: 75.613475, petrol: 103.45, diesel: 89.52, cng: 79.50, power: 110.30 },
      { taluk: "Mudhol", talukKn: "ಮುಧೋಳ", outlet_id: "390304", outlet_name: "Jai Malhar Petroleums", lat: 16.340437, lng: 75.27353,1, petrol: 103.48, diesel: 89.55, cng: 79.50, power: 110.33 },
      { taluk: "Jamkhandi", talukKn: "ಜಮಖಂಡಿ", outlet_id: "399844", outlet_name: "Triveni Shree Sangam Petroleums", lat: 16.548377, lng: 75.182388, petrol: 103.46, diesel: 89.53, cng: 79.50, power: 110.31 },
      { taluk: "Badami", talukKn: "ಬಾದಾಮಿ", outlet_id: "391642", outlet_name: "Aivalli & Co", lat: 15.909709, lng: 75.686254, petrol: 103.44, diesel: 89.50, cng: 79.50, power: 110.28 },
      { taluk: "Bilgi", talukKn: "ಬೀಳಗಿ", outlet_id: "390877", outlet_name: "Angadi Petroleum", lat: 16.416765, lng: 75.434959, petrol: 103.47, diesel: 89.54, cng: 79.50, power: 110.32 },
      { taluk: "Ilkal / Hungund", talukKn: "ಇಳಕಲ್ / ಹುನಗುಂದ", outlet_id: "410898", outlet_name: "Highway Service Station", lat: 15.981443, lng: 76.102995, petrol: 103.49, diesel: 89.56, cng: 79.50, power: 110.35 },
      { taluk: "Rabkavi Banhatti", talukKn: "ರಬಕವಿ ಬನಹಟ್ಟಿ", outlet_id: "399110", outlet_name: "HSD Shri Daneshwari Petroleums", lat: 16.491384, lng: 75.139957, petrol: 103.46, diesel: 89.53, cng: 79.50, power: 110.31 }
    ]
  },
  ballari: {
    districtKn: "ಬಳ್ಳಾರಿ",
    districtEn: "Ballari (Bellary)",
    pumps: [
      { taluk: "Ballari", talukKn: "ಬಳ್ಳಾರಿ", outlet_id: "390808", outlet_name: "M/s KVT Filling Station", lat: 15.1652823, lng: 76.9543228, petrol: 103.12, diesel: 89.20, cng: 79.20, power: 109.95 },
      { taluk: "Siruguppa", talukKn: "ಸಿರಗುಪ್ಪ", outlet_id: "398267", outlet_name: "M/s B E Hanumanthiah", lat: 15.635844, lng: 76.893052, petrol: 103.15, diesel: 89.23, cng: 79.20, power: 109.98 },
      { taluk: "Sandur", talukKn: "ಸಂಡೂರು", outlet_id: "405615", outlet_name: "M/s Ghorpade Petroleums", lat: 14.9721453, lng: 76.6108042, petrol: 103.14, diesel: 89.22, cng: 79.20, power: 109.97 },
      { taluk: "Kampli", talukKn: "ಕಂಪ್ಲಿ", outlet_id: "398779", outlet_name: "Welcome Filling Station", lat: 15.396501, lng: 76.609401, petrol: 103.13, diesel: 89.21, cng: 79.20, power: 109.96 }
    ]
  },
  belagavi: {
    districtKn: "ಬೆಳಗಾವಿ",
    districtEn: "Belagavi (Belgaum)",
    pumps: [
      { taluk: "Belagavi", talukKn: "ಬೆಳಗಾವಿ", outlet_id: "390791", outlet_name: "M/s Mavarkar Petroleum", lat: 15.86832913, lng: 74.52914406, petrol: 102.30, diesel: 88.45, cng: 78.50, power: 109.15 },
      { taluk: "Nipani", talukKn: "ನಿಪ್ಪಾಣಿ", outlet_id: "390327", outlet_name: "Sri Balaji Traders", lat: 16.397231, lng: 74.380541, petrol: 102.28, diesel: 88.43, cng: 78.50, power: 109.13 },
      { taluk: "Gokak", talukKn: "ಗೋಕಾಕ್", outlet_id: "410716", outlet_name: "M/s Shri Raj Rajeshwari Petroleums", lat: 16.160043, lng: 74.848708, petrol: 102.32, diesel: 88.47, cng: 78.50, power: 109.17 },
      { taluk: "Bailhongal", talukKn: "ಬೈಲಹೊಂಗಲ", outlet_id: "406653", outlet_name: "Mehboob Service Station", lat: 15.814701, lng: 74.848101, petrol: 102.31, diesel: 88.46, cng: 78.50, power: 109.16 },
      { taluk: "Chikkodi", talukKn: "ಚಿಕ್ಕೋಡಿ", outlet_id: "399384", outlet_name: "YS Miraji", lat: 16.42616336, lng: 74.58789216, petrol: 102.29, diesel: 88.44, cng: 78.50, power: 109.14 },
      { taluk: "Athani", talukKn: "ಅಥಣಿ", outlet_id: "393757", outlet_name: "Shri Murughendra Petroleum", lat: 16.720887, lng: 75.059476, petrol: 102.34, diesel: 88.49, cng: 78.50, power: 109.19 },
      { taluk: "Raibag", talukKn: "ರಾಯಬಾಗ", outlet_id: "399516", outlet_name: "Chaitanya Petroleum", lat: 16.501544, lng: 74.760505, petrol: 102.30, diesel: 88.45, cng: 78.50, power: 109.15 },
      { taluk: "Ramdurg", talukKn: "ರಾಮದುರ್ಗ", outlet_id: "391726", outlet_name: "M/s Yadwad Petroleum", lat: 15.950208, lng: 75.288791, petrol: 102.33, diesel: 88.48, cng: 78.50, power: 109.18 },
      { taluk: "Saundatti", talukKn: "ಸವದತ್ತಿ", outlet_id: "406716", outlet_name: "SB Hampannavar", lat: 15.7712601, lng: 75.114355, petrol: 102.31, diesel: 88.46, cng: 78.50, power: 109.16 },
      { taluk: "Khanapur", talukKn: "ಖಾನಾಪುರ", outlet_id: "406651", outlet_name: "Mallikarjun Service Station", lat: 15.645201, lng: 74.503101, petrol: 102.27, diesel: 88.42, cng: 78.50, power: 109.12 },
      { taluk: "Hukkeri", talukKn: "ಹುಕ್ಕೇರಿ", outlet_id: "390837", outlet_name: "Uzzma Petroleums", lat: 16.33290198, lng: 74.41336455, petrol: 102.30, diesel: 88.45, cng: 78.50, power: 109.15 },
      { taluk: "Kagwad", talukKn: "ಕಾಗವಾಡ", outlet_id: "421017", outlet_name: "Padmavathi Petroleum", lat: 16.708846, lng: 74.713347, petrol: 102.35, diesel: 88.50, cng: 78.50, power: 109.20 }
    ]
  },
  bengaluru: {
    districtKn: "ಬೆಂಗಳೂರು",
    districtEn: "Bengaluru Urban & Rural",
    pumps: [
      { taluk: "Bengaluru Central", talukKn: "ಬೆಂಗಳೂರು ಸೆಂಟ್ರಲ್", outlet_id: "97476", outlet_name: "Bharati Service Station", lat: 12.9822801, lng: 77.5941501, petrol: 102.86, diesel: 88.94, cng: 79.00, power: 109.80 },
      { taluk: "Peenya", talukKn: "ಪೀಣ್ಯ", outlet_id: "97436", outlet_name: "BRS Service Station", lat: 13.013401, lng: 77.5089901, petrol: 102.86, diesel: 88.94, cng: 79.00, power: 109.80 },
      { taluk: "Yelahanka", talukKn: "ಯಲಹಂಕ", outlet_id: "97441", outlet_name: "Sri Datt Digambar Maniknath Petrol", lat: 13.152582, lng: 77.568112, petrol: 102.88, diesel: 88.96, cng: 79.00, power: 109.82 },
      { taluk: "Kengeri", talukKn: "ಕೆಂಗೇರಿ", outlet_id: "97433", outlet_name: "Madhu Traders", lat: 12.912761, lng: 77.485541, petrol: 102.86, diesel: 88.94, cng: 79.00, power: 109.80 },
      { taluk: "Doddaballapur", talukKn: "ದೊಡ್ಡಬಳ್ಳಾಪುರ", outlet_id: "97440", outlet_name: "Rajrajeshwari Fuel Point", lat: 13.31827667, lng: 77.5366269, petrol: 102.94, diesel: 89.02, cng: 79.20, power: 109.88 },
      { taluk: "Devanahalli", talukKn: "ದೇವನಹಳ್ಳಿ", outlet_id: "97449", outlet_name: "Skanda Service Station", lat: 13.33121785, lng: 77.72608286, petrol: 102.92, diesel: 89.00, cng: 79.20, power: 109.86 },
      { taluk: "Nelamangala", talukKn: "ನೆಲಮಂಗಲ", outlet_id: "97428", outlet_name: "Sathys Service Station", lat: 13.089601, lng: 77.401021, petrol: 102.90, diesel: 88.98, cng: 79.10, power: 109.84 },
      { taluk: "Hoskote", talukKn: "ಹೊಸಕೋಟೆ", outlet_id: "97657", outlet_name: "Sri Venketeswara Service Station", lat: 13.077771, lng: 77.800101, petrol: 102.95, diesel: 89.03, cng: 79.20, power: 109.89 },
      { taluk: "Anekal", talukKn: "ಆನೇಕಲ್", outlet_id: "97674", outlet_name: "Kumar Fuel Station", lat: 12.789843, lng: 77.625967, petrol: 102.89, diesel: 88.97, cng: 79.00, power: 109.83 },
      { taluk: "Whitefield / Mahadevapura", talukKn: "ವೈಟ್‌ಫೀಲ್ಡ್ / ಮಹದೇವಪುರ", outlet_id: "97663", outlet_name: "Cnv Enterprises", lat: 12.965222, lng: 77.733134, petrol: 102.86, diesel: 88.94, cng: 79.00, power: 109.80 }
    ]
  },
  bidar: {
    districtKn: "ಬೀದರ್",
    districtEn: "Bidar",
    pumps: [
      { taluk: "Bidar", talukKn: "ಬೀದರ್", outlet_id: "391344", outlet_name: "M/s Ashoka Petroleum", lat: 17.93481631, lng: 77.47597088, petrol: 103.62, diesel: 89.68, cng: 78.90, power: 110.50 },
      { taluk: "Humnabad", talukKn: "ಹುಮ್ನಾಬಾದ್", outlet_id: "390548", outlet_name: "M/s Srimaniknath Millenium", lat: 17.77128767, lng: 77.08871451, petrol: 103.65, diesel: 89.71, cng: 78.90, power: 110.53 },
      { taluk: "Kamal Nagar", talukKn: "ಕಮಲನಗರ", outlet_id: "391093", outlet_name: "M/s Halse Petroleum", lat: 18.252296, lng: 77.168297, petrol: 103.64, diesel: 89.70, cng: 78.90, power: 110.52 },
      { taluk: "Aurad", talukKn: "ಔರಾದ್", outlet_id: "390998", outlet_name: "M/s Yallaling Service Station", lat: 18.240001, lng: 77.4254101, petrol: 103.67, diesel: 89.73, cng: 78.90, power: 110.55 },
      { taluk: "Basavakalyan", talukKn: "ಬಸವಕಲ್ಯಾಣ", outlet_id: "392454", outlet_name: "M/s Jubilee Petroleums", lat: 17.82809231, lng: 76.91319752, petrol: 103.60, diesel: 89.66, cng: 78.90, power: 110.48 },
      { taluk: "Bhalki", talukKn: "ಭಾಲ್ಕಿ", outlet_id: "392476", outlet_name: "M/s Baswaraj Bhavikatte Petro", lat: 18.06609531, lng: 77.15630476, petrol: 103.63, diesel: 89.69, cng: 78.90, power: 110.51 },
      { taluk: "Chitguppa", talukKn: "ಚಿಟಗುಪ್ಪ", outlet_id: "420491", outlet_name: "M/s Sr Patel And Ainapur Pteroleums", lat: 17.679571, lng: 77.2025659, petrol: 103.66, diesel: 89.72, cng: 78.90, power: 110.54 },
      { taluk: "Hulsur", talukKn: "ಹುಲಸೂರು", outlet_id: "482575", outlet_name: "Mshsd D D Bhople Petroleums", lat: 18.03146001, lng: 76.9946679, petrol: 103.61, diesel: 89.67, cng: 78.90, power: 110.49 }
    ]
  },
  chamarajanagar: {
    districtKn: "ಚಾಮರಾಜನಗರ",
    districtEn: "Chamarajanagar",
    pumps: [
      { taluk: "Chamarajanagar", talukKn: "ಚಾಮರಾಜನಗರ", outlet_id: "97601", outlet_name: "Sri Venkatesh S/S", lat: 11.927121, lng: 76.940251, petrol: 103.18, diesel: 89.26, cng: 78.60, power: 110.00 },
      { taluk: "Gundlupet", talukKn: "ಗುಂಡ್ಲುಪೇಟೆ", outlet_id: "97603", outlet_name: "Sri Rajarajeshwari Quick Fill", lat: 11.829041, lng: 76.679501, petrol: 103.22, diesel: 89.30, cng: 78.60, power: 110.04 },
      { taluk: "Hanur", talukKn: "ಹನೂರು", outlet_id: "97604", outlet_name: "Sri Srinivasa Fuel Station", lat: 12.095481, lng: 77.293371, petrol: 103.20, diesel: 89.28, cng: 78.60, power: 110.02 },
      { taluk: "Kollegal", talukKn: "ಕೊಳ್ಳೇಗಾಲ", outlet_id: "97605", outlet_name: "Sri Madegowda Fuel Station", lat: 12.152781, lng: 77.1102583, petrol: 103.19, diesel: 89.27, cng: 78.60, power: 110.01 },
      { taluk: "Yelandur", talukKn: "ಯಳಂದೂರು", outlet_id: "97607", outlet_name: "Hemant Pranathi Fuel Park", lat: 12.058895, lng: 77.033755, petrol: 103.17, diesel: 89.25, cng: 78.60, power: 109.99 }
    ]
  },
  chikkamagaluru: {
    districtKn: "ಚಿಕ್ಕಮಗಳೂರು",
    districtEn: "Chikkamagaluru (Chickmagalur)",
    pumps: [
      { taluk: "Chikkamagaluru", talukKn: "ಚಿಕ್ಕಮಗಳೂರು", outlet_id: "398251", outlet_name: "Raja Service Station", lat: 13.324921, lng: 75.773091, petrol: 103.04, diesel: 89.12, cng: 78.70, power: 109.90 },
      { taluk: "Kadur", talukKn: "ಕಡೂರು", outlet_id: "400163", outlet_name: "Shree Veerabhadreshwara", lat: 13.552494, lng: 76.008123, petrol: 103.06, diesel: 89.14, cng: 78.70, power: 109.92 },
      { taluk: "Tarikere", talukKn: "ತಾರೀಕೆರೆ", outlet_id: "391241", outlet_name: "Rayachoty Sri Veerabhadreshwara Fuel", lat: 13.723491, lng: 75.715371, petrol: 103.08, diesel: 89.16, cng: 78.70, power: 109.94 },
      { taluk: "Mudigere", talukKn: "ಮೂಡಿಗೆರೆ", outlet_id: "417831", outlet_name: "Adhoc Durgamba Service Station", lat: 13.1300388, lng: 75.6400273, petrol: 103.02, diesel: 89.10, cng: 78.70, power: 109.88 },
      { taluk: "Sringeri", talukKn: "ಶೃಂಗೇರಿ", outlet_id: "399783", outlet_name: "Swarna Ganapathi Enterprises", lat: 13.424895, lng: 75.252464, petrol: 103.05, diesel: 89.13, cng: 78.70, power: 109.91 },
      { taluk: "Koppa", talukKn: "ಕೊಪ್ಪ", outlet_id: "400178", outlet_name: "Sri Ganesh Service Station", lat: 13.533834, lng: 75.367386, petrol: 103.07, diesel: 89.15, cng: 78.70, power: 109.93 },
      { taluk: "Narasimharajapura / Balehonnur", talukKn: "ಎನ್.ಆರ್.ಪುರ / ಬಾಳೆಹೊನ್ನೂರು", outlet_id: "391170", outlet_name: "Menezes Fuels", lat: 13.354461, lng: 75.464866, petrol: 103.03, diesel: 89.11, cng: 78.70, power: 109.89 },
      { taluk: "Kalasa", talukKn: "ಕಳಸ", outlet_id: "399351", outlet_name: "Four Square Traders", lat: 13.2304901, lng: 75.3589701, petrol: 103.01, diesel: 89.09, cng: 78.70, power: 109.87 }
    ]
  },
  chitradurga: {
    districtKn: "ಚಿತ್ರದುರ್ಗ",
    districtEn: "Chitradurga",
    pumps: [
      { taluk: "Chitradurga", talukKn: "ಚಿತ್ರದುರ್ಗ", outlet_id: "390759", outlet_name: "KFSC Fuel Station", lat: 14.215544, lng: 76.379986, petrol: 103.22, diesel: 89.30, cng: 78.30, power: 110.05 },
      { taluk: "Hiriyur", talukKn: "ಹಿರಿಯೂರು", outlet_id: "391813", outlet_name: "M/s Kamala Fuel Hub", lat: 14.021329, lng: 76.581521, petrol: 103.25, diesel: 89.33, cng: 78.30, power: 110.08 },
      { taluk: "Hosadurga", talukKn: "ಹೊಸದುರ್ಗ", outlet_id: "391358", outlet_name: "M/s KVS Filling Station", lat: 13.697308, lng: 76.5356201, petrol: 103.20, diesel: 89.28, cng: 78.30, power: 110.03 },
      { taluk: "Holalkere", talukKn: "ಹೊಳಲ್ಕೆರೆ", outlet_id: "391138", outlet_name: "M/s Sri Siddharudha Petroleum", lat: 14.222857, lng: 76.392655, petrol: 103.23, diesel: 89.31, cng: 78.30, power: 110.06 },
      { taluk: "Challakere", talukKn: "ಚಳ್ಳಕೆರೆ", outlet_id: "391706", outlet_name: "M/s Basu Petroleums", lat: 14.297467, lng: 76.653576, petrol: 103.26, diesel: 89.34, cng: 78.30, power: 110.09 },
      { taluk: "Molakalmuru", talukKn: "ಮೊಳಕಾಲ್ಮೂರು", outlet_id: "391849", outlet_name: "Kalyana Enterprisers", lat: 14.611794, lng: 76.668927, petrol: 103.28, diesel: 89.36, cng: 78.30, power: 110.11 }
    ]
  },
  dakshina_kannada: {
    districtKn: "ದಕ್ಷಿಣ ಕನ್ನಡ",
    districtEn: "Dakshina Kannada",
    pumps: [
      { taluk: "Mangaluru", talukKn: "ಮಂಗಳೂರು", outlet_id: "394291", outlet_name: "M/s Maco Cooperative Society Ltd", lat: 12.873141, lng: 74.851671, petrol: 103.12, diesel: 89.20, cng: 79.50, power: 110.00 },
      { taluk: "Puttur", talukKn: "ಪುತ್ತೂರು", outlet_id: "391513", outlet_name: "M/s Pais Petroleum", lat: 12.752946, lng: 75.217236, petrol: 103.15, diesel: 89.23, cng: 79.50, power: 110.03 },
      { taluk: "Belthangady", talukKn: "ಬೆಳ್ತಂಗಡಿ", outlet_id: "393346", outlet_name: "M/s Shruthi Service Station", lat: 12.992149, lng: 75.292681, petrol: 103.14, diesel: 89.22, cng: 79.50, power: 110.02 },
      { taluk: "Bantwal", talukKn: "ಬಂಟ್ವಾಳ", outlet_id: "398123", outlet_name: "M/s Shree Kateel Fuel Park", lat: 12.75472703, lng: 75.10478704, petrol: 103.13, diesel: 89.21, cng: 79.50, power: 110.01 },
      { taluk: "Sullia", talukKn: "ಸುಳ್ಯ", outlet_id: "403981", outlet_name: "M/s Hindustan Pet Service", lat: 12.74391282, lng: 75.47563848, petrol: 103.18, diesel: 89.26, cng: 79.50, power: 110.06 },
      { taluk: "Kadaba", talukKn: "ಕಡಬ", outlet_id: "399352", outlet_name: "Skandashree Petroleums", lat: 12.739852, lng: 75.337205, petrol: 103.16, diesel: 89.24, cng: 79.50, power: 110.04 },
      { taluk: "Moodabidri", talukKn: "ಮೂಡುಬಿದಿರೆ", outlet_id: "399367", outlet_name: "U&V Service Station", lat: 13.065589, lng: 74.942046, petrol: 103.11, diesel: 89.19, cng: 79.50, power: 109.99 }
    ]
  },
  davangere: {
    districtKn: "ದಾವಣಗೆರೆ",
    districtEn: "Davanagere",
    pumps: [
      { taluk: "Davanagere", talukKn: "ದಾವಣಗೆರೆ", outlet_id: "391086", outlet_name: "M/s Sri Veeranjaneya Indhana Kendra", lat: 14.479467, lng: 75.906382, petrol: 103.16, diesel: 89.24, cng: 78.20, power: 109.95 },
      { taluk: "Jagalur", talukKn: "ಜಗಳೂರು", outlet_id: "390730", outlet_name: "M/s Sree Guru Basaveshwara Service", lat: 14.666253, lng: 76.298266, petrol: 103.19, diesel: 89.27, cng: 78.20, power: 109.98 },
      { taluk: "Harihar", talukKn: "ಹರಿಹರ", outlet_id: "394590", outlet_name: "HSD Shree Devi Petroleum", lat: 14.486322, lng: 75.802989, petrol: 103.14, diesel: 89.22, cng: 78.20, power: 109.93 },
      { taluk: "Channagiri", talukKn: "ಚನ್ನಗಿರಿ", outlet_id: "391839", outlet_name: "M/s Brundavan Fuels", lat: 14.013032, lng: 75.937631, petrol: 103.18, diesel: 89.26, cng: 78.20, power: 109.97 },
      { taluk: "Honnali", talukKn: "ಹೊನ್ನಾಳಿ", outlet_id: "400119", outlet_name: "Shivashanta Filling Station", lat: 14.235151, lng: 75.652531, petrol: 103.15, diesel: 89.23, cng: 78.20, power: 109.94 },
      { taluk: "Harapanahalli", talukKn: "ಹರಪನಹಳ್ಳಿ", outlet_id: "400085", outlet_name: "Sri Srishylam Filling Station", lat: 14.782943, lng: 75.998684, petrol: 103.20, diesel: 89.28, cng: 78.20, power: 109.99 }
    ]
  },
  dharwad: {
    districtKn: "ಧಾರವಾಡ / ಹುಬ್ಬಳ್ಳಿ",
    districtEn: "Dharwad / Hubballi",
    pumps: [
      { taluk: "Dharwad", talukKn: "ಧಾರವಾಡ", outlet_id: "393725", outlet_name: "Sri Mahalaxmi Petroleums", lat: 15.44883666, lng: 74.98785175, petrol: 102.45, diesel: 88.60, cng: 78.00, power: 109.40 },
      { taluk: "Hubballi", talukKn: "ಹುಬ್ಬಳ್ಳಿ", outlet_id: "391262", outlet_name: "M/s Madhurlaxmi Enterprises", lat: 15.36102524, lng: 75.20806294, petrol: 102.45, diesel: 88.60, cng: 78.00, power: 109.40 },
      { taluk: "Navalgund", talukKn: "ನವಲಗುಂದ", outlet_id: "391222", outlet_name: "M/s SP Petroleum", lat: 15.55888999, lng: 75.36017388, petrol: 102.48, diesel: 88.63, cng: 78.00, power: 109.43 },
      { taluk: "Kalghatgi", talukKn: "ಕಲಘಟಗಿ", outlet_id: "399898", outlet_name: "Keystone Projects", lat: 15.425405, lng: 75.006706, petrol: 102.44, diesel: 88.59, cng: 78.00, power: 109.39 },
      { taluk: "Annigeri", talukKn: "ಅಣ್ಣಿಗೇರಿ", outlet_id: "391035", outlet_name: "M/s CM Hubli & Co Annigeri", lat: 15.42639081, lng: 75.44448212, petrol: 102.49, diesel: 88.64, cng: 78.00, power: 109.44 },
      { taluk: "Alnavar", talukKn: "ಅಳ್ನಾವರ", outlet_id: "399452", outlet_name: "BB Tegur & CS Hoskeri Alnav", lat: 15.421995, lng: 74.742063, petrol: 102.43, diesel: 88.58, cng: 78.00, power: 109.38 },
      { taluk: "Kundgol", talukKn: "ಕುಂದಗೋಳ", outlet_id: "420570", outlet_name: "Shri Renuka Petroleums", lat: 15.245212, lng: 75.255167, petrol: 102.46, diesel: 88.61, cng: 78.00, power: 109.41 }
    ]
  },
  gadag: {
    districtKn: "ಗದಗ",
    districtEn: "Gadag",
    pumps: [
      { taluk: "Gadag", talukKn: "ಗದಗ", outlet_id: "390737", outlet_name: "M/s Gadag Mahalaxmi Petroleum", lat: 15.4292551, lng: 75.6342126, petrol: 103.28, diesel: 89.36, cng: 78.10, power: 110.10 },
      { taluk: "Mundargi", talukKn: "ಮುಂಡರಗಿ", outlet_id: "390894", outlet_name: "M/s CP Koppal Petroleum", lat: 15.210361, lng: 75.897469, petrol: 103.31, diesel: 89.39, cng: 78.10, power: 110.13 },
      { taluk: "Gajendragad", talukKn: "ಗಜೇಂದ್ರಗಡ", outlet_id: "391272", outlet_name: "M/s VT Raibagi", lat: 15.729705, lng: 75.966878, petrol: 103.30, diesel: 89.38, cng: 78.10, power: 110.12 },
      { taluk: "Shirahatti", talukKn: "ಶಿಿರಹಟ್ಟಿ", outlet_id: "398088", outlet_name: "M/s Spandana Petroleums", lat: 15.1170098, lng: 75.4663929, petrol: 103.27, diesel: 89.35, cng: 78.10, power: 110.09 },
      { taluk: "Ron", talukKn: "ರೋಣ", outlet_id: "406811", outlet_name: "SA Gadagi", lat: 15.686227, lng: 75.737588, petrol: 103.29, diesel: 89.37, cng: 78.10, power: 110.11 },
      { taluk: "Nargund", talukKn: "ನರಗುಂದ", outlet_id: "406785", outlet_name: "KB Gujamagadi", lat: 15.719917, lng: 75.386481, petrol: 103.26, diesel: 89.34, cng: 78.10, power: 110.08 }
    ]
  },
  hassan: {
    districtKn: "ಹಾಸನ",
    districtEn: "Hassan",
    pumps: [
      { taluk: "Hassan", talukKn: "ಹಾಸನ", outlet_id: "398174", outlet_name: "M/s H V Subraya Setty & Sons", lat: 13.000751, lng: 76.096461, petrol: 102.68, diesel: 88.78, cng: 78.40, power: 109.55 },
      { taluk: "Arkalgud / Konanur", talukKn: "ಅರ್ಕಲಗೂಡು / ಕೊಣನೂರು", outlet_id: "390699", outlet_name: "M/s YSR Service Station", lat: 12.62657163, lng: 76.04692451, petrol: 102.71, diesel: 88.81, cng: 78.40, power: 109.58 },
      { taluk: "Arsikere", talukKn: "ಅರಸೀಕೆರೆ", outlet_id: "391061", outlet_name: "M/s Shivalaya Service Station", lat: 13.31974331, lng: 76.26215496, petrol: 102.70, diesel: 88.80, cng: 78.40, power: 109.57 },
      { taluk: "Belur", talukKn: "ಬೇಲೂರು", outlet_id: "391045", outlet_name: "M/s Lalithambha Fuel Station Bikkod", lat: 13.07358413, lng: 75.86250141, petrol: 102.69, diesel: 88.79, cng: 78.40, power: 109.56 },
      { taluk: "Channarayapatna", talukKn: "ಚನ್ನರಾಯಪಟ್ಟಣ", outlet_id: "390780", outlet_name: "M/s Sri Venkateshwara Enterprises", lat: 12.937391, lng: 76.363481, petrol: 102.67, diesel: 88.77, cng: 78.40, power: 109.54 },
      { taluk: "Holenarsipur", talukKn: "ಹೊಳೆನರಸೀಪುರ", outlet_id: "400113", outlet_name: "Sindhoor Service Station", lat: 12.787531, lng: 76.244601, petrol: 102.68, diesel: 88.78, cng: 78.40, power: 109.55 },
      { taluk: "Alur", talukKn: "ಆಲೂರು", outlet_id: "400167", outlet_name: "Sri Kenchamba Service Station", lat: 12.976291, lng: 75.998101, petrol: 102.66, diesel: 88.76, cng: 78.40, power: 109.53 },
      { taluk: "Sakleshpur", talukKn: "ಸಕಲೇಶಪುರ", outlet_id: "482852", outlet_name: "M/S B M Basavanna Sakleshpura", lat: 12.935657, lng: 75.770018, petrol: 102.72, diesel: 88.82, cng: 78.40, power: 109.59 }
    ]
  },
  haveri: {
    districtKn: "ಹಾವೇರಿ",
    districtEn: "Haveri",
    pumps: [
      { taluk: "Haveri", talukKn: "ಹಾವೇರಿ", outlet_id: "406646", outlet_name: "Shiva Basava Auto Oil Trading", lat: 14.7899701, lng: 75.3974201, petrol: 103.08, diesel: 89.16, cng: 78.20, power: 109.90 },
      { taluk: "Ranebennur", talukKn: "ರಾಟೇಬೆನ್ನೂರು", outlet_id: "392077", outlet_name: "M/s Sri Venkateshwara Petroleum", lat: 14.605981, lng: 75.646157, petrol: 103.10, diesel: 89.18, cng: 78.20, power: 109.92 },
      { taluk: "Byadgi", talukKn: "ಬ್ಯಾಡಗಿ", outlet_id: "390954", outlet_name: "Shri Shivaparvati Petroleum Co", lat: 14.747423, lng: 75.453064, petrol: 103.09, diesel: 89.17, cng: 78.20, power: 109.91 },
      { taluk: "Shiggaon", talukKn: "ಶಿಗ್ಗಾಂವಿ", outlet_id: "390996", outlet_name: "M/s Shri Narahari & Company", lat: 14.97340592, lng: 75.23378222, petrol: 103.07, diesel: 89.15, cng: 78.20, power: 109.89 },
      { taluk: "Hanagal", talukKn: "ಹಾನಗಲ್", outlet_id: "391120", outlet_name: "M/s Yavagal Petroleum", lat: 14.781264, lng: 75.136109, petrol: 103.06, diesel: 89.14, cng: 78.20, power: 109.88 },
      { taluk: "Hirekerur", talukKn: "ಹಿರೇಕೆರೂರು", outlet_id: "399897", outlet_name: "Banakar Petroleum", lat: 14.458621, lng: 75.384541, petrol: 103.11, diesel: 89.19, cng: 78.20, power: 109.93 },
      { taluk: "Savanur", talukKn: "ಸವಣೂರು", outlet_id: "390734", outlet_name: "M/s Bharani Petroleum", lat: 15.0318967, lng: 75.3079057, petrol: 103.08, diesel: 89.16, cng: 78.20, power: 109.90 },
      { taluk: "Rattihalli", talukKn: "ರಟ್ಟಿಹಳ್ಳಿ", outlet_id: "399410", outlet_name: "Shiva Oil Traders", lat: 14.4279201, lng: 75.5152901, petrol: 103.12, diesel: 89.20, cng: 78.20, power: 109.94 }
    ]
  },
  kalaburagi: {
    districtKn: "ಕಲಬುರಗಿ",
    districtEn: "Kalaburagi (Gulbarga)",
    pumps: [
      { taluk: "Kalaburagi", talukKn: "ಕಲಬುರಗಿ", outlet_id: "391687", outlet_name: "M/s Gulbarga Petro Point", lat: 17.3584901, lng: 76.8464601, petrol: 102.10, diesel: 88.25, cng: 77.80, power: 109.10 },
      { taluk: "Jewargi", talukKn: "ಜೇವರ್ಗಿ", outlet_id: "390430", outlet_name: "M/s Shree Mata Petroleums", lat: 17.03551039, lng: 76.79193345, petrol: 102.14, diesel: 88.29, cng: 77.80, power: 109.14 },
      { taluk: "Chittapur", talukKn: "ಚಿತ್ತಾಪುರ", outlet_id: "390544", outlet_name: "M/s Om Sai Shakti Petroleum", lat: 17.25059187, lng: 77.04759385, petrol: 102.12, diesel: 88.27, cng: 77.80, power: 109.12 },
      { taluk: "Afzalpur", talukKn: "ಅಫಜಲಪುರ", outlet_id: "391438", outlet_name: "M/s Shree Daneshwari Petroleums", lat: 17.2788401, lng: 76.2168801, petrol: 102.15, diesel: 88.30, cng: 77.80, power: 109.15 },
      { taluk: "Chincholi", talukKn: "ಚಿಂಚೋಳಿ", outlet_id: "391806", outlet_name: "M/s Sri Sangameshwar Petroleum", lat: 17.56450631, lng: 77.39343854, petrol: 102.13, diesel: 88.28, cng: 77.80, power: 109.13 },
      { taluk: "Aland", talukKn: "ಆಳಂದ", outlet_id: "391837", outlet_name: "M/s Basava Fuels", lat: 17.52538129, lng: 76.60741678, petrol: 102.11, diesel: 88.26, cng: 77.80, power: 109.11 },
      { taluk: "Sedam", talukKn: "ಸೇಡಂ", outlet_id: "391850", outlet_name: "M/s Bhavani Petroleum", lat: 17.07399922, lng: 77.40346726, petrol: 102.16, diesel: 88.31, cng: 77.80, power: 109.16 },
      { taluk: "Shahabad", talukKn: "ಶಹಾಬಾದ್", outlet_id: "391102", outlet_name: "M/s S Muthati And Sons", lat: 17.12966375, lng: 76.9338612, petrol: 102.12, diesel: 88.27, cng: 77.80, power: 109.12 }
    ]
  },
  kodagu: {
    districtKn: "ಕೊಡಗು",
    districtEn: "Kodagu",
    pumps: [
      { taluk: "Madikeri", talukKn: "ಮಡಿಕೇರಿ", outlet_id: "394406", outlet_name: "East End Service Station", lat: 12.4181601, lng: 75.7428601, petrol: 103.54, diesel: 89.60, cng: 78.80, power: 110.40 },
      { taluk: "Virajpet", talukKn: "ವಿರಾಜಪೇಟೆ", outlet_id: "391617", outlet_name: "Cauvery Filling Station", lat: 12.2262057, lng: 75.7461439, petrol: 103.58, diesel: 89.64, cng: 78.80, power: 110.44 },
      { taluk: "Somwarpet / Kushalnagar", talukKn: "ಸೋಮವಾರಪೇಟೆ / ಕುಶಾಲನಗರ", outlet_id: "400155", outlet_name: "Sri Ranga Service Station", lat: 12.48507091, lng: 75.95584401, petrol: 103.52, diesel: 89.58, cng: 78.80, power: 110.38 },
      { taluk: "Ponnampet / Gonikoppal", talukKn: "ಪೊನ್ನಂಪೇಟೆ / ಗೋಣಿಕೊಪ್ಪಲು", outlet_id: "398187", outlet_name: "Vittal Service Station", lat: 12.144741, lng: 75.944513, petrol: 103.56, diesel: 89.62, cng: 78.80, power: 110.42 }
    ]
  },
  kolar: {
    districtKn: "ಕೋಲಾರ / ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
    districtEn: "Kolar & Chikkaballapur",
    pumps: [
      { taluk: "Kolar", talukKn: "ಕೋಲಾರ", outlet_id: "97615", outlet_name: "Sri Subramanya Swamy Gasoline", lat: 13.14138112, lng: 78.13966665, petrol: 103.02, diesel: 89.10, cng: 79.00, power: 109.90 },
      { taluk: "Mulbagal", talukKn: "ಮುಳಬಾಗಿಲು", outlet_id: "97617", outlet_name: "Balaji Service Station", lat: 13.16720698, lng: 78.39945689, petrol: 103.05, diesel: 89.13, cng: 79.00, power: 109.93 },
      { taluk: "Bangarpet", talukKn: "ಬಂಗಾರಪೇಟೆ", outlet_id: "97620", outlet_name: "Sri Maruthi Service Station", lat: 12.9845701, lng: 78.1815801, petrol: 103.04, diesel: 89.12, cng: 79.00, power: 109.92 },
      { taluk: "Malur", talukKn: "ಮಾಲೂರು", outlet_id: "97622", outlet_name: "Manjunatha Filling Station", lat: 13.01228837, lng: 77.93751576, petrol: 103.00, diesel: 89.08, cng: 79.00, power: 109.88 },
      { taluk: "Srinivaspur", talukKn: "ಶ್ರೀನಿವಾಸಪುರ", outlet_id: "97625", outlet_name: "Lavanya Filling Station", lat: 13.33366642, lng: 78.21393125, petrol: 103.06, diesel: 89.14, cng: 79.00, power: 109.94 },
      { taluk: "Chintamani", talukKn: "ಚಿಂತಾಮಣಿ", outlet_id: "97636", outlet_name: "BKT Company", lat: 13.39915901, lng: 78.05325786, petrol: 103.03, diesel: 89.11, cng: 79.00, power: 109.91 },
      { taluk: "Sidlaghatta", talukKn: "ಶಿಡ್ಲಘಟ್ಟ", outlet_id: "97642", outlet_name: "Anjanadri Service Station", lat: 13.38328303, lng: 77.86061114, petrol: 103.01, diesel: 89.09, cng: 79.00, power: 109.89 },
      { taluk: "Gauribidanur", talukKn: "ಗೌರಿಬಿದನೂರು", outlet_id: "97638", outlet_name: "Esturi Ramakrishna Shetty & Sons", lat: 13.614941, lng: 77.517901, petrol: 102.98, diesel: 89.06, cng: 79.00, power: 109.86 },
      { taluk: "Gudibande", talukKn: "ಗುಡಿಬಂಡೆ", outlet_id: "97644", outlet_name: "Gudibanda Service Station", lat: 13.66989393, lng: 77.71391737, petrol: 102.99, diesel: 89.07, cng: 79.00, power: 109.87 },
      { taluk: "Chikkaballapur", talukKn: "ಚಿಕ್ಕಬಳ್ಳಾಪುರ", outlet_id: "97645", outlet_name: "SLV Petroleums", lat: 13.59238441, lng: 77.78394529, petrol: 103.02, diesel: 89.10, cng: 79.00, power: 109.90 }
    ]
  },
  koppal: {
    districtKn: "ಕೊಪ್ಪಳ",
    districtEn: "Koppal",
    pumps: [
      { taluk: "Gangavathi", talukKn: "ಗಂಗಾವತಿ", outlet_id: "392450", outlet_name: "M/s Venkateshwara Agencies", lat: 15.4384727, lng: 76.5380754, petrol: 103.38, diesel: 89.46, cng: 78.30, power: 110.20 },
      { taluk: "Koppal", talukKn: "ಕೊಪ್ಪಳ", outlet_id: "391547", outlet_name: "M/s Kaveri Petroleums", lat: 15.3495601, lng: 76.1648401, petrol: 103.38, diesel: 89.46, cng: 78.30, power: 110.20 },
      { taluk: "Yelburga / Kukanoor", talukKn: "ಯಲಬುರ್ಗಾ / ಕುಕನೂರು", outlet_id: "390521", outlet_name: "M/s Vinayak Service Centre", lat: 15.466741, lng: 76.003861, petrol: 103.41, diesel: 89.49, cng: 78.30, power: 110.23 },
      { taluk: "Kushtagi", talukKn: "ಕುಷ್ಟಗಿ", outlet_id: "390995", outlet_name: "M/s Kargil Shivabasava Petroleum", lat: 15.737206, lng: 76.1966406, petrol: 103.42, diesel: 89.50, cng: 78.30, power: 110.24 },
      { taluk: "Karatagi", talukKn: "ಕಾರಟಗಿ", outlet_id: "398419", outlet_name: "Sri Veereshwara Petroleum", lat: 15.619851, lng: 76.638538, petrol: 103.39, diesel: 89.47, cng: 78.30, power: 110.21 },
      { taluk: "Kanakagiri", talukKn: "ಕನಕಗಿರಿ", outlet_id: "399488", outlet_name: "Lingraj Petroleum", lat: 15.5699664, lng: 76.424335, petrol: 103.40, diesel: 89.48, cng: 78.30, power: 110.22 }
    ]
  },
  mandya: {
    districtKn: "ಮಂಡ್ಯ",
    districtEn: "Mandya",
    pumps: [
      { taluk: "Mandya", talukKn: "ಮಂಡ್ಯ", outlet_id: "97566", outlet_name: "Suresh Service Station", lat: 12.532201, lng: 76.910061, petrol: 102.77, diesel: 88.86, cng: 78.50, power: 109.68 },
      { taluk: "Maddur", talukKn: "ಮದ್ದೂರು", outlet_id: "97577", outlet_name: "Shri Rakesh Agencies", lat: 12.582257, lng: 77.035244, petrol: 102.79, diesel: 88.88, cng: 78.50, power: 109.70 },
      { taluk: "Malavalli", talukKn: "ಮಳವಳ್ಳಿ", outlet_id: "97568", outlet_name: "Sri Sainath Petrol Station", lat: 12.3868901, lng: 77.059701, petrol: 102.81, diesel: 88.90, cng: 78.50, power: 109.72 },
      { taluk: "Pandavapura", talukKn: "ಪಾಂಡವಪುರ", outlet_id: "97572", outlet_name: "Agri Prod Co Op Mktg Society", lat: 12.48600453, lng: 76.67772626, petrol: 102.75, diesel: 88.84, cng: 78.50, power: 109.66 },
      { taluk: "Srirangapatna", talukKn: "ಶ್ರೀರಂಗಪಟ್ಟಣ", outlet_id: "97592", outlet_name: "Sri Ranga Amaravathi Fuels", lat: 12.429358, lng: 76.697531, petrol: 102.73, diesel: 88.82, cng: 78.50, power: 109.64 },
      { taluk: "Nagamangala", talukKn: "ನಾಗಮಂಗಲ", outlet_id: "97579", outlet_name: "Jwalamala Filling Station", lat: 12.962192, lng: 76.749311, petrol: 102.80, diesel: 88.89, cng: 78.50, power: 109.71 },
      { taluk: "Krishnarajpet (KR Pete)", talukKn: "ಕೆ.ಆರ್.ಪೇಟೆ", outlet_id: "97578", outlet_name: "Sri Siddalingeswara Fuel Station", lat: 12.664802, lng: 76.483495, petrol: 102.76, diesel: 88.85, cng: 78.50, power: 109.67 }
    ]
  },
  mysuru: {
    districtKn: "ಮೈಸೂರು",
    districtEn: "Mysuru (Mysore)",
    pumps: [
      { taluk: "Mysuru", talukKn: "ಮೈಸೂರು", outlet_id: "394979", outlet_name: "M/s Sri Nandi Corner", lat: 12.315731, lng: 76.632551, petrol: 102.68, diesel: 88.78, cng: 78.50, power: 109.60 },
      { taluk: "Nanjangud", talukKn: "ನಂಜನಗೂಡು", outlet_id: "398149", outlet_name: "P Mahadevaiah & Son", lat: 12.120541, lng: 76.680791, petrol: 102.70, diesel: 88.80, cng: 78.50, power: 109.62 },
      { taluk: "Hunsur", talukKn: "ಹುಣಸೂರು", outlet_id: "404282", outlet_name: "Sri Maruthi Service Station", lat: 12.3053501, lng: 76.2984501, petrol: 102.72, diesel: 88.82, cng: 78.50, power: 109.64 },
      { taluk: "Periyapatna", talukKn: "ಪಿರಿಯಾಪಟ್ಟಣ", outlet_id: "394429", outlet_name: "HSD Sri Male Mahadeswara Swamy", lat: 12.337534, lng: 76.1049701, petrol: 102.74, diesel: 88.84, cng: 78.50, power: 109.66 },
      { taluk: "Krishnarajanagara (KR Nagar)", talukKn: "ಕೆ.ಆರ್. ನಗರ", outlet_id: "393262", outlet_name: "M/s Jatin Enterprises", lat: 12.444772, lng: 76.383072, petrol: 102.69, diesel: 88.79, cng: 78.50, power: 109.61 },
      { taluk: "T Narasipura", talukKn: "ಟಿ. ನರಸೀಪುರ", outlet_id: "390951", outlet_name: "Bhramaramba Mallikarjuna Fuel", lat: 12.256786, lng: 76.961975, petrol: 102.71, diesel: 88.81, cng: 78.50, power: 109.63 },
      { taluk: "Heggadadevankote (HD Kote)", talukKn: "ಹೆಚ್.ಡಿ. ಕೋಟೆ", outlet_id: "399701", outlet_name: "MSHSD Sri Maani Basaveshwara Fuel", lat: 12.083522, lng: 76.334855, petrol: 102.75, diesel: 88.85, cng: 78.50, power: 109.67 },
      { taluk: "Saragur (Sargur)", talukKn: "ಸರಗೂರು", outlet_id: "394410", outlet_name: "Vijaya Fuel Outlet", lat: 11.996365, lng: 76.400921, petrol: 102.73, diesel: 88.83, cng: 78.50, power: 109.65 }
    ]
  },
  raichur: {
    districtKn: "ರಾಯಚೂರು",
    districtEn: "Raichur",
    pumps: [
      { taluk: "Raichur", talukKn: "ರಾಯಚೂರು", outlet_id: "390703", outlet_name: "M/s Sangeetha Filling Station", lat: 16.20587806, lng: 77.41145288, petrol: 103.58, diesel: 89.64, cng: 78.40, power: 110.45 },
      { taluk: "Devadurga", talukKn: "ದೇವದುರ್ಗ", outlet_id: "391800", outlet_name: "M/s Bhagya Filling Station", lat: 16.42390569, lng: 76.91465361, petrol: 103.62, diesel: 89.68, cng: 78.40, power: 110.49 },
      { taluk: "Manvi", talukKn: "ಮಾನ್ವಿ", outlet_id: "391857", outlet_name: "M/s Farah Fuel Filling Station", lat: 15.99215583, lng: 76.99922478, petrol: 103.60, diesel: 89.66, cng: 78.40, power: 110.47 },
      { taluk: "Sirwar", talukKn: "ಸಿರವಾರ", outlet_id: "391830", outlet_name: "M/s Amareshwara Filling Station", lat: 16.17953725, lng: 77.02781641, petrol: 103.61, diesel: 89.67, cng: 78.40, power: 110.48 },
      { taluk: "Lingsugur / Mudgal", talukKn: "ಲಿಂಗಸುಗೂರು / ಮುದ್ಗಲ್", outlet_id: "394552", outlet_name: "Sri Vijayamahantesh Filling Station", lat: 16.01475686, lng: 76.43562112, petrol: 103.59, diesel: 89.65, cng: 78.40, power: 110.46 },
      { taluk: "Sindhanur", talukKn: "ಸಿಂಧನೂರು", outlet_id: "419150", outlet_name: "M/s Sangameswara Service Station", lat: 15.78647451, lng: 76.76956988, petrol: 103.57, diesel: 89.63, cng: 78.40, power: 110.44 }
    ]
  },
  ramanagara: {
    districtKn: "ರಾಮನಗರ",
    districtEn: "Ramanagara",
    pumps: [
      { taluk: "Ramanagara", talukKn: "ರಾಮನಗರ", outlet_id: "97554", outlet_name: "Janatha Service Station", lat: 12.725728, lng: 77.274324, petrol: 102.96, diesel: 89.04, cng: 78.90, power: 109.85 },
      { taluk: "Channapatna", talukKn: "ಚನ್ನಪಟ್ಟಣ", outlet_id: "97559", outlet_name: "Saptagiri Fuel Station", lat: 12.548354, lng: 77.219383, petrol: 102.98, diesel: 89.06, cng: 78.90, power: 109.87 },
      { taluk: "Kanakapura", talukKn: "ಕನಕಪುರ", outlet_id: "97565", outlet_name: "Nirmala Fuel Station", lat: 12.615686, lng: 77.434442, petrol: 103.00, diesel: 89.08, cng: 78.90, power: 109.89 },
      { taluk: "Magadi", talukKn: "ಮಾಗಡಿ", outlet_id: "417658", outlet_name: "ADHOC Maruti Fuel Station", lat: 12.9518601, lng: 77.2299201, petrol: 102.95, diesel: 89.03, cng: 78.90, power: 109.84 }
    ]
  },
  shivamogga: {
    districtKn: "ಶಿವಮೊಗ್ಗ",
    districtEn: "Shivamogga (Shimoga)",
    pumps: [
      { taluk: "Shivamogga", talukKn: "ಶಿವಮೊಗ್ಗ", outlet_id: "398157", outlet_name: "M/s Udaya Service Station", lat: 13.931971, lng: 75.586961, petrol: 102.64, diesel: 88.74, cng: 78.60, power: 109.60 },
      { taluk: "Bhadravathi", talukKn: "ಭದ್ರಾವತಿ", outlet_id: "390745", outlet_name: "M/s Bhadravati Lorry Owners Assn", lat: 13.83859823, lng: 75.71366417, petrol: 102.66, diesel: 88.76, cng: 78.60, power: 109.62 },
      { taluk: "Sagar", talukKn: "ಸಾಗರ", outlet_id: "398241", outlet_name: "M/s S B Channabasappa & B R", lat: 14.168421, lng: 75.021471, petrol: 102.68, diesel: 88.78, cng: 78.60, power: 109.64 },
      { taluk: "Shikaripura", talukKn: "ಶಿಕಾರಿಪುರ", outlet_id: "391343", outlet_name: "M/s MN Petro Junction", lat: 14.36984714, lng: 75.2494459, petrol: 102.67, diesel: 88.77, cng: 78.60, power: 109.63 },
      { taluk: "Soraba", talukKn: "ಸೊರಬ", outlet_id: "390832", outlet_name: "M/s Sri Balaji Fuels & Ser Station", lat: 14.562491, lng: 75.151157, petrol: 102.69, diesel: 88.79, cng: 78.60, power: 109.65 },
      { taluk: "Thirthahalli", talukKn: "ತೀರ್ಥಹಳ್ಳಿ", outlet_id: "398204", outlet_name: "M/s Sahyadri Service Station", lat: 13.688264, lng: 75.247635, petrol: 102.63, diesel: 88.73, cng: 78.60, power: 109.59 },
      { taluk: "Hosanagara", talukKn: "ಹೊಸನಗರ", outlet_id: "391315", outlet_name: "M/s Nagara Rice & Flour Mills", lat: 13.818791, lng: 75.027819, petrol: 102.65, diesel: 88.75, cng: 78.60, power: 109.61 }
    ]
  },
  tumakuru: {
    districtKn: "ತುಮಕೂರು",
    districtEn: "Tumakuru (Tumkur)",
    pumps: [
      { taluk: "Tumakuru", talukKn: "ತುಮಕೂರು", outlet_id: "97508", outlet_name: "Tumkur Petroleum Company", lat: 13.3286101, lng: 77.122041, petrol: 102.72, diesel: 88.82, cng: 78.80, power: 109.65 },
      { taluk: "Kunigal", talukKn: "ಕುಣಿಗಲ್", outlet_id: "97506", outlet_name: "Prabha Petrol Station", lat: 13.0256601, lng: 77.0250801, petrol: 102.75, diesel: 88.85, cng: 78.80, power: 109.68 },
      { taluk: "Koratagere", talukKn: "ಕೊರಟಗೆರೆ", outlet_id: "97509", outlet_name: "Sri Ranganath Service Station", lat: 13.523041, lng: 77.240921, petrol: 102.74, diesel: 88.84, cng: 78.80, power: 109.67 },
      { taluk: "Sira", talukKn: "ಶಿರಾ", outlet_id: "97511", outlet_name: "PR Mudanna And Son", lat: 13.744491, lng: 76.898691, petrol: 102.76, diesel: 88.86, cng: 78.80, power: 109.69 },
      { taluk: "Gubbi", talukKn: "ಗುಬ್ಬಿ", outlet_id: "97539", outlet_name: "Sri Siddi Vinayaka Fuel Station", lat: 13.29378491, lng: 76.94919995, petrol: 102.71, diesel: 88.81, cng: 78.80, power: 109.64 },
      { taluk: "Tiptur", talukKn: "ತಿಪಟೂರು", outlet_id: "97519", outlet_name: "Aditya Enterprises", lat: 13.261467, lng: 76.488168, petrol: 102.73, diesel: 88.83, cng: 78.80, power: 109.66 },
      { taluk: "Pavagada", talukKn: "ಪಾವಗಡ", outlet_id: "97521", outlet_name: "TCVK Rajgopal Service Station", lat: 14.092316, lng: 77.283734, petrol: 102.79, diesel: 88.89, cng: 78.80, power: 109.72 },
      { taluk: "Madhugiri", talukKn: "ಮಧುಗಿರಿ", outlet_id: "97522", outlet_name: "Sri Balaji Filling Station", lat: 13.661749, lng: 77.219442, petrol: 102.77, diesel: 88.87, cng: 78.80, power: 109.70 },
      { taluk: "Turuvekere", talukKn: "ತುರುವೇಕೆರೆ", outlet_id: "97525", outlet_name: "Star Petroleums", lat: 13.170091, lng: 76.669951, petrol: 102.70, diesel: 88.80, cng: 78.80, power: 109.63 },
      { taluk: "Chikkanayakanahalli", talukKn: "ಚಿಕ್ಕನಾಯಕನಹಳ್ಳಿ", outlet_id: "394887", outlet_name: "Shree Sumukha Fuel Station", lat: 13.427005, lng: 76.627554, petrol: 102.78, diesel: 88.88, cng: 78.80, power: 109.71 }
    ]
  },
  udupi: {
    districtKn: "ಉಡುಪಿ",
    districtEn: "Udupi",
    pumps: [
      { taluk: "Udupi", talukKn: "ಉಡುಪಿ", outlet_id: "390761", outlet_name: "M/s Bhavana Enterprises", lat: 13.348381, lng: 74.706721, petrol: 103.04, diesel: 89.12, cng: 79.20, power: 109.95 },
      { taluk: "Kundapura", talukKn: "ಕುಂದಾಪುರ", outlet_id: "391069", outlet_name: "Shree Mandarthi Enterprises", lat: 13.64710809, lng: 74.82221105, petrol: 103.08, diesel: 89.16, cng: 79.20, power: 109.99 },
      { taluk: "Karkala", talukKn: "ಕಾರ್ಕಳ", outlet_id: "405432", outlet_name: "Pradeep Service Station", lat: 13.20458715, lng: 74.99578157, petrol: 103.06, diesel: 89.14, cng: 79.20, power: 109.97 },
      { taluk: "Hebri", talukKn: "ಹೆಬ್ರಿ", outlet_id: "390916", outlet_name: "M/s Sowmya Enterprises", lat: 13.459721, lng: 74.984231, petrol: 103.05, diesel: 89.13, cng: 79.20, power: 109.96 },
      { taluk: "Kaup", talukKn: "ಕಾಪು", outlet_id: "420128", outlet_name: "M/s Suryanugraha Fuel Centre", lat: 13.26492425, lng: 74.74865758, petrol: 103.03, diesel: 89.11, cng: 79.20, power: 109.94 },
      { taluk: "Brahmavara", talukKn: "ಬ್ರಹ್ಮಾವರ", outlet_id: "395365", outlet_name: "M/s Manjunatha Service Station", lat: 13.424581, lng: 74.740001, petrol: 103.07, diesel: 89.15, cng: 79.20, power: 109.98 }
    ]
  },
  uttara_kannada: {
    districtKn: "ಉತ್ತರ ಕನ್ನಡ",
    districtEn: "Uttara Kannada",
    pumps: [
      { taluk: "Ankola", talukKn: "ಅಂಕೋಲಾ", outlet_id: "419174", outlet_name: "M/s G N Mahale", lat: 14.659091, lng: 74.307931, petrol: 103.32, diesel: 89.40, cng: 78.80, power: 110.15 },
      { taluk: "Sirsi", talukKn: "ಶಿರಸಿ", outlet_id: "406649", outlet_name: "SS Dhundshi & Company", lat: 14.6147701, lng: 74.8323601, petrol: 103.35, diesel: 89.43, cng: 78.80, power: 110.18 },
      { taluk: "Honnavar", talukKn: "ಹೊನ್ನಾವರ", outlet_id: "406722", outlet_name: "LKS Shroff", lat: 14.282601, lng: 74.4526601, petrol: 103.30, diesel: 89.38, cng: 78.80, power: 110.13 },
      { taluk: "Kumta", talukKn: "ಕುಮಟಾ", outlet_id: "406724", outlet_name: "VP Prabhu", lat: 14.4308901, lng: 74.4232101, petrol: 103.31, diesel: 89.39, cng: 78.80, power: 110.14 },
      { taluk: "Bhatkal", talukKn: "ಭಟ್ಕಳ", outlet_id: "403881", outlet_name: "M/s Akshay Fuel Station", lat: 14.061451, lng: 74.507925, petrol: 103.29, diesel: 89.37, cng: 78.80, power: 110.12 },
      { taluk: "Haliyal", talukKn: "ಹಳಿಯಾಳ", outlet_id: "400198", outlet_name: "Gajanana Petrol Pump", lat: 15.33540089, lng: 74.76524093, petrol: 103.36, diesel: 89.44, cng: 78.80, power: 110.19 },
      { taluk: "Yellapur", talukKn: "ಯಲ್ಲಾಪುರ", outlet_id: "404835", outlet_name: "M/s Kamakshi Automobile Service Centre", lat: 14.97661587, lng: 74.7132386, petrol: 103.34, diesel: 89.42, cng: 78.80, power: 110.17 },
      { taluk: "Mundgod", talukKn: "ಮುಂಡಗೋಡು", outlet_id: "390218", outlet_name: "M/s Rajesh Fuel Station", lat: 14.789448, lng: 75.033989, petrol: 103.33, diesel: 89.41, cng: 78.80, power: 110.16 }
    ]
  },
  vijayapura: {
    districtKn: "ವಿಜಯಪುರ",
    districtEn: "Vijayapura (Bijapur)",
    pumps: [
      { taluk: "Vijayapura", talukKn: "ವಿಜಯಪುರ", outlet_id: "391512", outlet_name: "M/s Hind Petroleums", lat: 16.7863201, lng: 75.7205001, petrol: 103.40, diesel: 89.48, cng: 78.60, power: 110.25 },
      { taluk: "Sindagi", talukKn: "ಸಿಂದಗಿ", outlet_id: "390263", outlet_name: "Somalingeswara Petroleum", lat: 16.870926, lng: 75.497312, petrol: 103.42, diesel: 89.50, cng: 78.60, power: 110.27 },
      { taluk: "Muddebihal", talukKn: "ಮುದ್ದೇಬಿಹಾಳ", outlet_id: "400142", outlet_name: "Shri Daneshwari Petrol", lat: 16.342895, lng: 76.129617, petrol: 103.45, diesel: 89.53, cng: 78.60, power: 110.30 },
      { taluk: "Basavana Bagewadi", talukKn: "ಬಸವನ ಬಾಗೇವಾಡಿ", outlet_id: "395331", outlet_name: "M/s Gangadhar B Kuntoji Petroleum", lat: 16.571336, lng: 75.979339, petrol: 103.41, diesel: 89.49, cng: 78.60, power: 110.26 },
      { taluk: "Indi", talukKn: "ಇಂಡಿ", outlet_id: "390910", outlet_name: "M/s Shri Sai Petrol Pump", lat: 17.177492, lng: 75.956285, petrol: 103.43, diesel: 89.51, cng: 78.60, power: 110.28 },
      { taluk: "Chadchan", talukKn: "ಚಡಚಣ", outlet_id: "393557", outlet_name: "MT Malapur Petroleum", lat: 17.315163, lng: 75.652884, petrol: 103.44, diesel: 89.52, cng: 78.60, power: 110.29 }
    ]
  },
  vijayanagara: {
    districtKn: "ವಿಜಯನಗರ",
    districtEn: "Vijayanagara (Hosapete)",
    pumps: [
      { taluk: "Hosapete", talukKn: "ಹೊಸಪೇಟೆ", outlet_id: "375380", outlet_name: "M/S Milan Agencies", lat: 15.2679551, lng: 76.3860401, petrol: 103.20, diesel: 89.28, cng: 78.50, power: 110.05 },
      { taluk: "Kotturu", talukKn: "ಕೊಟ್ಟೂರು", outlet_id: "390834", outlet_name: "M/s Devaramani Petroleums", lat: 14.8321464, lng: 76.2287755, petrol: 103.24, diesel: 89.32, cng: 78.50, power: 110.09 },
      { taluk: "Hagaribommanahalli", talukKn: "ಹಗರಿಬೊಮ್ಮನಹಳ್ಳಿ", outlet_id: "390827", outlet_name: "M/s Jayalaxmi Fuels", lat: 15.04401373, lng: 76.20199792, petrol: 103.22, diesel: 89.30, cng: 78.50, power: 110.07 },
      { taluk: "Hoovina Hadagali", talukKn: "ಹೂವಿನ ಹಡಗಲಿ", outlet_id: "417700", outlet_name: "ADHOC Sree Vijaya Durga Petro Mart", lat: 15.0236519, lng: 75.9274226, petrol: 103.21, diesel: 89.29, cng: 78.50, power: 110.06 }
    ]
  },
  yadgir: {
    districtKn: "ಯಾದಗಿರಿ",
    districtEn: "Yadgir",
    pumps: [
      { taluk: "Yadgir", talukKn: "ಯಾದಗಿರಿ", outlet_id: "391709", outlet_name: "M/s Kadloor Petroleums", lat: 16.75559088, lng: 77.12889431, petrol: 103.50, diesel: 89.56, cng: 77.80, power: 110.35 },
      { taluk: "Shahapur", talukKn: "ಶಹಾಪುರ", outlet_id: "390804", outlet_name: "M/s Nandi Basava Petroleums", lat: 16.759274, lng: 76.788803, petrol: 103.54, diesel: 89.60, cng: 77.80, power: 110.39 },
      { taluk: "Gurmatkal", talukKn: "ಗುರುಮಠಕಲ್", outlet_id: "400097", outlet_name: "Sri Balaji Filling Station", lat: 16.869991, lng: 77.385101, petrol: 103.52, diesel: 89.58, cng: 77.80, power: 110.37 },
      { taluk: "Shorapur / Kembhavi", talukKn: "ಸುರಪುರ / ಕೆಂಭಾವಿ", outlet_id: "481465", outlet_name: "M/s Sri Sugureshwar Filling Station", lat: 16.66531219, lng: 76.52790935, petrol: 103.55, diesel: 89.61, cng: 77.80, power: 110.40 }
    ]
  }
};

/**
 * Haversine formula to find nearest petrol pump by GPS coordinates
 */
function findNearestTalukPump(userLat, userLng) {
  let nearest = null;
  let minDistance = Infinity;

  Object.keys(TALUK_FUEL_PUMPS).forEach(distKey => {
    const distData = TALUK_FUEL_PUMPS[distKey];
    distData.pumps.forEach(pump => {
      const dLat = (pump.lat - userLat) * Math.PI / 180;
      const dLng = (pump.lng - userLng) * Math.PI / 180;
      const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
                Math.cos(userLat * Math.PI / 180) * Math.cos(pump.lat * Math.PI / 180) *
                Math.sin(dLng / 2) * Math.sin(dLng / 2);
      const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
      const dist = 6371 * c; // KM

      if (dist < minDistance) {
        minDistance = dist;
        nearest = {
          ...pump,
          districtKey: distKey,
          districtKn: distData.districtKn,
          districtEn: distData.districtEn,
          distanceKm: dist.toFixed(1)
        };
      }
    });
  });

  return nearest;
}
