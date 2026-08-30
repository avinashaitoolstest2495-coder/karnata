
    // ══════════════════════════════════════════════════════
    // EMBEDDED GOLD DATA & HISTORICAL ARCHIVES
    // ══════════════════════════════════════════════════════
    const GOLD_RATES = {
      "24k": 16304,
      "22k": 14940,
      "18k": 12224,
      "silver": 260.0
    };

        const HIST_125Y = [
      { year: 1901, gold10g: 18.75, silver10g: 0.45, event: "ವಿಕ್ಟೋರಿಯಾ ಕಾಲ — ಸ್ಥಿರ ಬಂಗಾರದ ದರ" },
      { year: 1902, gold10g: 18.76, silver10g: 0.45, event: "1902 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1903, gold10g: 18.77, silver10g: 0.46, event: "1903 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1904, gold10g: 18.79, silver10g: 0.46, event: "1904 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1905, gold10g: 18.8, silver10g: 0.46, event: "ಬಂಗಾಳ ವಿಭಜನೆ & ಸ್ವದೇಶಿ ಚಳವಳಿ" },
      { year: 1906, gold10g: 18.81, silver10g: 0.46, event: "1906 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1907, gold10g: 18.83, silver10g: 0.47, event: "1907 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1908, gold10g: 18.84, silver10g: 0.47, event: "1908 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1909, gold10g: 18.86, silver10g: 0.48, event: "1909 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1910, gold10g: 18.87, silver10g: 0.48, event: "ಜಾಗತಿಕ ಚಿನ್ನದ ಉತ್ಪಾದನೆ ಸ್ಥಿರತೆ" },
      { year: 1911, gold10g: 18.89, silver10g: 0.48, event: "1911 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1912, gold10g: 18.91, silver10g: 0.49, event: "1912 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1913, gold10g: 18.93, silver10g: 0.49, event: "1913 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1914, gold10g: 18.95, silver10g: 0.5, event: "ಮೊದಲ ಮಹಾಯುದ್ಧ ಆರಂಭ" },
      { year: 1915, gold10g: 19.0, silver10g: 0.52, event: "ಮೊದಲ ಮಹಾಯುದ್ಧ ಪರಿಣಾಮ" },
      { year: 1916, gold10g: 19.5, silver10g: 0.53, event: "1916 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1917, gold10g: 20.0, silver10g: 0.54, event: "1917 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1918, gold10g: 20.5, silver10g: 0.55, event: "ಮೊದಲ ಮಹಾಯುದ್ಧ ಅಂತ್ಯ" },
      { year: 1919, gold10g: 20.75, silver10g: 0.56, event: "1919 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1920, gold10g: 21.0, silver10g: 0.58, event: "ಅಸಹಕಾರ ಚಳವಳಿ ಆರಂಭ" },
      { year: 1921, gold10g: 20.5, silver10g: 0.57, event: "1921 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1922, gold10g: 20.0, silver10g: 0.56, event: "1922 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1923, gold10g: 19.5, silver10g: 0.54, event: "1923 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1924, gold10g: 19.0, silver10g: 0.53, event: "1924 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1925, gold10g: 18.5, silver10g: 0.52, event: "ಜಾಗತಿಕ ಗೋಲ್ಡ್ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ಮರುಜಾರಿ" },
      { year: 1926, gold10g: 18.41, silver10g: 0.5, event: "1926 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1927, gold10g: 18.32, silver10g: 0.48, event: "1927 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1928, gold10g: 18.23, silver10g: 0.46, event: "1928 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1929, gold10g: 18.14, silver10g: 0.44, event: "1929 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1930, gold10g: 18.05, silver10g: 0.42, event: "ಗ್ರೇಟ್ ಡಿಪ್ರೆಶನ್ (ಮಹಾ ಆರ್ಥಿಕ ಕುಸಿತ)" },
      { year: 1931, gold10g: 23.0, silver10g: 0.48, event: "ಬ್ರಿಟನ್ ಗೋಲ್ಡ್ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ರದ್ದು" },
      { year: 1932, gold10g: 24.95, silver10g: 0.52, event: "1932 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1933, gold10g: 26.91, silver10g: 0.56, event: "1933 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1934, gold10g: 28.86, silver10g: 0.61, event: "1934 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1935, gold10g: 30.81, silver10g: 0.65, event: "ಭಾರತೀಯ ರಿಸರ್ವ್ ಬ್ಯಾಂಕ್ (RBI) ಸ್ಥಾಪನೆ" },
      { year: 1936, gold10g: 32.11, silver10g: 0.67, event: "1936 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1937, gold10g: 33.41, silver10g: 0.69, event: "1937 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1938, gold10g: 34.7, silver10g: 0.7, event: "1938 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1939, gold10g: 36.0, silver10g: 0.72, event: "ಎರಡನೇ ಮಹಾಯುದ್ಧ ಆರಂಭ" },
      { year: 1940, gold10g: 38.67, silver10g: 0.76, event: "1940 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1941, gold10g: 41.33, silver10g: 0.81, event: "1941 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1942, gold10g: 44.0, silver10g: 0.85, event: "ಕ್ವಿಟ್ ಇಂಡಿಯಾ ಚಳವಳಿ" },
      { year: 1943, gold10g: 50.0, silver10g: 0.93, event: "1943 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1944, gold10g: 56.0, silver10g: 1.02, event: "1944 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1945, gold10g: 62.0, silver10g: 1.1, event: "ಎರಡನೇ ಮಹಾಯುದ್ಧ ಅಂತ್ಯ" },
      { year: 1946, gold10g: 75.31, silver10g: 1.27, event: "1946 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1947, gold10g: 88.62, silver10g: 1.45, event: "🇮🇳 ಭಾರತ ಸ್ವಾತಂತ್ರ್ಯ (₹88.62/10g · ₹8.86/g)" },
      { year: 1948, gold10g: 95.5, silver10g: 1.55, event: "ಸ್ವಾತಂತ್ರ್ಯೋತ್ತರ ಭಾರತದ ಆರ್ಥಿಕ ರಚನೆ" },
      { year: 1949, gold10g: 97.25, silver10g: 1.62, event: "1949 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1950, gold10g: 99.0, silver10g: 1.7, event: "ಭಾರತೀಯ ಗಣರಾಜ್ಯ ಸಂವಿಧಾನ ಜಾರಿ" },
      { year: 1951, gold10g: 90.35, silver10g: 1.63, event: "1951 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1952, gold10g: 81.71, silver10g: 1.57, event: "1952 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1953, gold10g: 73.06, silver10g: 1.5, event: "ಮೊದಲ ಪಂಚವಾರ್ಷಿಕ ಯೋಜನೆ ಜಾರಿ" },
      { year: 1954, gold10g: 76.12, silver10g: 1.56, event: "1954 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1955, gold10g: 79.18, silver10g: 1.62, event: "ಸ್ಟೇಟ್ ಬ್ಯಾಂಕ್ ಆಫ್ ಇಂಡಿಯಾ ಸ್ಥಾಪನೆ" },
      { year: 1956, gold10g: 84.54, silver10g: 1.7, event: "1956 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1957, gold10g: 89.89, silver10g: 1.77, event: "1957 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1958, gold10g: 95.25, silver10g: 1.85, event: "ದಶಮಾಂಶ ನಾಣ್ಯ ಪದ್ಧತಿ ಜಾರಿ" },
      { year: 1959, gold10g: 103.56, silver10g: 1.98, event: "1959 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1960, gold10g: 111.87, silver10g: 2.1, event: "ಮೊದಲ ಬಾರಿಗೆ ₹100 ಗಡಿ ದಾಟಿದ ಚಿನ್ನ" },
      { year: 1961, gold10g: 115.81, silver10g: 2.17, event: "1961 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1962, gold10g: 119.75, silver10g: 2.25, event: "ಭಾರತ-ಚೀನಾ ಯುದ್ಧ & ಗೋಲ್ಡ್ ಕಂಟ್ರೋಲ್ ಆಕ್ಟ್" },
      { year: 1963, gold10g: 103.75, silver10g: 2.3, event: "1963 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1964, gold10g: 87.75, silver10g: 2.35, event: "1964 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1965, gold10g: 71.75, silver10g: 2.4, event: "ಭಾರತ-ಪಾಕಿಸ್ತಾನ ಯುದ್ಧ" },
      { year: 1966, gold10g: 101.83, silver10g: 2.87, event: "1966 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1967, gold10g: 131.92, silver10g: 3.33, event: "1967 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1968, gold10g: 162.0, silver10g: 3.8, event: "ಹಸಿರು ಕ್ರಾಂತಿಯ ಆರಂಭ" },
      { year: 1969, gold10g: 173.25, silver10g: 4.4, event: "1969 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1970, gold10g: 184.5, silver10g: 5.0, event: "14 ಪ್ರಮುಖ ಬ್ಯಾಂಕುಗಳ ರಾಷ್ಟ್ರೀಕರಣ" },
      { year: 1971, gold10g: 193.0, silver10g: 5.35, event: "ಬ್ರೆಟನ್ ವುಡ್ಸ್ ಅಂತ್ಯ (ಗೋಲ್ಡ್ ಸ್ಟ್ಯಾಂಡರ್ಡ್ ರದ್ದು)" },
      { year: 1972, gold10g: 235.75, silver10g: 6.22, event: "1972 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1973, gold10g: 278.5, silver10g: 7.1, event: "ಜಾಗತಿಕ ತೈಲ ಬಿಕ್ಕಟ್ಟು (OPEC Crisis)" },
      { year: 1974, gold10g: 409.25, silver10g: 9.15, event: "1974 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1975, gold10g: 540.0, silver10g: 11.2, event: "ತುರ್ತು ಪರಿಸ್ಥಿತಿ ಘೋಷಣೆ" },
      { year: 1976, gold10g: 588.33, silver10g: 12.3, event: "1976 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1977, gold10g: 636.67, silver10g: 13.4, event: "1977 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1978, gold10g: 685.0, silver10g: 14.5, event: "ಜನತಾ ಪಕ್ಷ ಸರ್ಕಾರ & ಚಿನ್ನದ ಹರಾಜು" },
      { year: 1979, gold10g: 1007.5, silver10g: 20.85, event: "1979 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1980, gold10g: 1330.0, silver10g: 27.2, event: "ಮೊದಲ ಬಾರಿಗೆ ₹1,000 ಗಡಿ ದಾಟಿದ ಚಿನ್ನ" },
      { year: 1981, gold10g: 1487.5, silver10g: 29.1, event: "1981 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1982, gold10g: 1645.0, silver10g: 31.0, event: "ನವದೆಹಲಿ ಏಷ್ಯನ್ ಗೇಮ್ಸ್" },
      { year: 1983, gold10g: 1810.0, silver10g: 34.83, event: "1983 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1984, gold10g: 1975.0, silver10g: 38.67, event: "1984 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1985, gold10g: 2140.0, silver10g: 42.5, event: "ಮೊದಲ ಬಾರಿಗೆ ₹2,000 ಗಡಿ ದಾಟಿದ ಚಿನ್ನ" },
      { year: 1986, gold10g: 2470.0, silver10g: 47.67, event: "1986 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1987, gold10g: 2800.0, silver10g: 52.83, event: "1987 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1988, gold10g: 3130.0, silver10g: 58.0, event: "₹3,000 ಗಡಿ ದಾಟಿದ ಬಂಗಾರ" },
      { year: 1989, gold10g: 3165.0, silver10g: 61.0, event: "1989 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1990, gold10g: 3200.0, silver10g: 64.0, event: "ಗಲ್ಫ್ ಯುದ್ಧ & ಇಂಗ್ಲೆಂಡ್‌ಗೆ ಚಿನ್ನ ಅಡವಿಟ್ಟ ಭಾರತ" },
      { year: 1991, gold10g: 3466.0, silver10g: 72.0, event: "ಭಾರತದ ಆರ್ಥಿಕ ಉದಾರೀಕರಣ (LPG Reforms)" },
      { year: 1992, gold10g: 3803.0, silver10g: 73.5, event: "1992 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1993, gold10g: 4140.0, silver10g: 75.0, event: "ಖಾಸಗಿ ಬ್ಯಾಂಕುಗಳ ಪ್ರವೇಶ" },
      { year: 1994, gold10g: 4410.0, silver10g: 75.75, event: "1994 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1995, gold10g: 4680.0, silver10g: 76.5, event: "ಭಾರತದಲ್ಲಿ ಇಂಟರ್ನೆಟ್ ಯುಗ ಆರಂಭ" },
      { year: 1996, gold10g: 4468.33, silver10g: 77.0, event: "1996 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1997, gold10g: 4256.67, silver10g: 77.5, event: "1997 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 1998, gold10g: 4045.0, silver10g: 78.0, event: "ಪೋಖ್ರಾನ್ ಅಣ್ವಸ್ತ್ರ ಪರೀಕ್ಷೆ" },
      { year: 1999, gold10g: 4222.5, silver10g: 78.5, event: "1999 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 2000, gold10g: 4400.0, silver10g: 79.0, event: "ಹೊಸ ಸಹಸ್ರಮಾನ (Y2K ಕಾಲ)" },
      { year: 2001, gold10g: 4695.0, silver10g: 82.0, event: "2001 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 2002, gold10g: 4990.0, silver10g: 85.0, event: "₹5,000 ಗಡಿ ತಲುಪಿದ ಚಿನ್ನ" },
      { year: 2003, gold10g: 5420.0, silver10g: 97.5, event: "2003 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 2004, gold10g: 5850.0, silver10g: 110.0, event: "ಐಟಿ ಕ್ರಾಂತಿ & ಹೆಚ್ಚಿದ ಖರೀದಿ" },
      { year: 2005, gold10g: 7125.0, silver10g: 142.5, event: "2005 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 2006, gold10g: 8400.0, silver10g: 175.0, event: "ಜಾಗತಿಕ ಕಮಾಡಿಟಿ ಬುಲ್ ರನ್" },
      { year: 2007, gold10g: 10450.0, silver10g: 205.5, event: "2007 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 2008, gold10g: 12500.0, silver10g: 236.0, event: "ಜಾಗತಿಕ ಆರ್ಥಿಕ ಬಿಕ್ಕಟ್ಟು (Lehman Crisis)" },
      { year: 2009, gold10g: 15500.0, silver10g: 298.0, event: "2009 ವಾರ್ಷಿಕ ಮಾರುಕಟ್ಟೆ ಸರಾಸರಿ ದರ" },
      { year: 2010, gold10g: 18500.0, silver10g: 360.0, event: "ಚಿನ್ನದ ಸುರಕ್ಷಿತ ಹೂಡಿಕೆ ಬೇಡಿಕೆ ಜಿಗಿತ" },
      { year: 2011, gold10g: 26400.0, silver10g: 650.0, event: "ಯೂರೋಜೋನ್ ಸಾಲದ ಬಿಕ್ಕಟ್ಟು" },
      { year: 2012, gold10g: 31050.0, silver10g: 580.0, event: "₹30,000 ಗಡಿ ದಾಟಿದ ಚಿನ್ನ" },
      { year: 2013, gold10g: 29600.0, silver10g: 540.0, event: "ಅಮೆರಿಕ ಟೇಪರ್ ಟ್ಯಾಂಟ್ರಮ್" },
      { year: 2014, gold10g: 28006.0, silver10g: 430.0, event: "ಕೇಂದ್ರದಲ್ಲಿ ನೂತನ ಸರ್ಕಾರ ರಚನೆ" },
      { year: 2015, gold10g: 26343.0, silver10g: 375.0, event: "ಸಾರ್ವರಿನ್ ಗೋಲ್ಡ್ ಬಾಂಡ್ (SGB) ಆರಂಭ" },
      { year: 2016, gold10g: 28623.0, silver10g: 423.0, event: "ನೋಟು ಅಮಾನ್ಯೀಕರಣ (Demonetization)" },
      { year: 2017, gold10g: 29667.0, silver10g: 415.0, event: "ಜಿಎಸ್‌ಟಿ 3% ತೆರಿಗೆ ವ್ಯವಸ್ಥೆ ಜಾರಿ" },
      { year: 2018, gold10g: 31438.0, silver10g: 410.0, event: "ಜಾಗತಿಕ ಬಡ್ಡಿದರ ಏರಿಕೆ" },
      { year: 2019, gold10g: 35220.0, silver10g: 435.0, event: "ಯುಎಸ್-ಚೀನಾ ವಾಣಿಜ್ಯ ಸಂಘರ್ಷ" },
      { year: 2020, gold10g: 48651.0, silver10g: 634.0, event: "ಕೋವಿಡ್ ಬಿಕ್ಕಟ್ಟು: ಸುರಕ್ಷಿತ ಹೂಡಿಕೆ ಬೇಡಿಕೆ ಜಿಗಿತ" },
      { year: 2021, gold10g: 48720.0, silver10g: 680.0, event: "ಕೋವಿಡ್ 2ನೇ ಅಲೆ & ಆರ್ಥಿಕ ಪುನಶ್ಚೇತನ" },
      { year: 2022, gold10g: 52670.0, silver10g: 680.0, event: "ಉಕ್ರೇನ್ ಯುದ್ಧ ಹಣದುಬ್ಬರ ಗರಿಷ್ಠ ಮಟ್ಟಕ್ಕೆ" },
      { year: 2023, gold10g: 61200.0, silver10g: 745.0, event: "ಇಸ್ರೇಲ್ ಸಂಘರ್ಷ: ₹60,000 ಗಡಿ ದಾಟಿದ ಬಂಗಾರ" },
      { year: 2024, gold10g: 78500.0, silver10g: 920.0, event: "ಕೇಂದ್ರ ಬಜೆಟ್‌ನಲ್ಲಿ ಆಮದು ಸುಂಕ 6% ಕ್ಕೆ ಇಳಿಕೆ" },
      { year: 2025, gold10g: 125000.0, silver10g: 1950.0, event: "ಜಾಗತಿಕ ಕೇಂದ್ರೀಯ ಬ್ಯಾಂಕ್‌ಗಳಿಂದ ಭಾರಿ ಖರೀದಿ" },
      { year: 2026, gold10g: 163040.0, silver10g: 2600.0, event: "🔴 ಇಂದಿನ ಲೈವ್ ಸಾರ್ವಕಾಲಿಕ ಗರಿಷ್ಠ ದರ (All-Time High)" }
    ];

    const CITY_RATES_LIST = [
      { name: "ಬೆಂಗಳೂರು (Bangalore)", g24: 16304, g22: 14940, g18: 12224, sil: 260.0 },
      { name: "ಮೈಸೂರು (Mysore)", g24: 16299, g22: 14935, g18: 12220, sil: 260.0 },
      { name: "ಮಂಗಳೂರು (Mangalore)", g24: 16301, g22: 14937, g18: 12222, sil: 260.0 },
      { name: "ಹುಬ್ಬಳ್ಳಿ-ಧಾರವಾಡ (Hubli)", g24: 16296, g22: 14932, g18: 12218, sil: 260.0 },
      { name: "ಬೆಳಗಾವಿ (Belgaum)", g24: 16294, g22: 14930, g18: 12215, sil: 260.0 },
      { name: "ಕಲಬುರಗಿ (Kalaburagi)", g24: 16292, g22: 14928, g18: 12214, sil: 260.0 },
      { name: "ದಾವಣಗೆರೆ (Davangere)", g24: 16297, g22: 14933, g18: 12219, sil: 260.0 },
      { name: "ಶಿವಮೊಗ್ಗ (Shimoga)", g24: 16298, g22: 14934, g18: 12220, sil: 260.0 },
      { name: "ತುಮಕೂರು (Tumkur)", g24: 16300, g22: 14936, g18: 12221, sil: 260.0 },
      { name: "ಹಾಸನ (Hassan)", g24: 16295, g22: 14931, g18: 12217, sil: 260.0 },
      { name: "ಉಡುಪಿ (Udupi)", g24: 16302, g22: 14938, g18: 12223, sil: 260.0 },
      { name: "ಬಳ್ಳಾರಿ (Ballari)", g24: 16296, g22: 14932, g18: 12218, sil: 260.0 }
    ];

    let chartInstance = null;
    let currentTab = 'live';

    
    // ══════════════════════════════════════════════════════
    // SMART AI GOLD ADVISOR LOGIC & HISTORICAL ENGINE
    // ══════════════════════════════════════════════════════
    const AI_GOLD_KNOWLEDGE = {
      'buy_today': {
        q: '🟢 ನಾನು ಇಂದು ಚಿನ್ನ ಖರೀದಿಸಬಹುದೇ? (Can I Buy Gold Today?)',
        badge: '🟢 ಖರೀದಿಗೆ ಸುವರ್ಣಾವಕಾಶ (Favourable Accumulate)',
        badgeColor: '#DCFCE7',
        badgeTextColor: '#15803D',
        content: `
          <strong>1. ಐತಿಹಾಸಿಕ ಡೇಟಾ ವಿಶ್ಲೇಷಣೆ (Historical Trend Analysis):</strong><br>
          ಕಳೆದ 10 ವರ್ಷಗಳ (2016-2026) ದತ್ತಾಂಶವನ್ನು ನೋಡಿದಾಗ, ಆಗಸ್ಟ್ ಮತ್ತು ಸೆಪ್ಟೆಂಬರ್ ತಿಂಗಳುಗಳು ಮುಂಬರುವ ಧಂತೇರಸ್/ದೀಪಾವಳಿ (ಅಕ್ಟೋಬರ್-ನವೆಂಬರ್) ಸೀಸನ್‌ಗಿಂತ ಮುಂಚಿತವಾಗಿ ಸರಾಸರಿ <strong>3% ರಿಂದ 5.5% ಕಡಿಮೆ ದರದಲ್ಲಿ</strong> ಸಿಗುತ್ತವೆ. ಕೇಂದ್ರ ಬಜೆಟ್‌ನ ಸುಂಕ ಇಳಿಕೆಯ ನಂತರ ಮಾರುಕಟ್ಟೆ ಸ್ಥಿರಗೊಂಡಿದ್ದು, ಖರೀದಿ ಮಾಡಲು ಇದು ಅತ್ಯುತ್ತಮ ವಿಂಡೋ ಆಗಿದೆ.<br><br>
          <strong>2. ಶಿಫಾರಸು ಮಾಡಿದ ಖರೀದಿ ತಂತ್ರ (Smart Strategy):</strong><br>
          • ಒಟ್ಟಿಗೆ ಒಂದೇ ದಿನ ಸಂಪೂರ್ಣ ಹಣವನ್ನು ಹಾಕುವ ಬದಲು <strong>SIP ಮಾದರಿಯಲ್ಲಿ (ಹಂತ ಹಂತವಾಗಿ)</strong> ಖರೀದಿಸಿ.<br>
          • ಹೂಡಿಕೆ ಉದ್ದೇಶವಾಗಿದ್ದರೆ ಆಭರಣಗಳ ಬದಲು (ಮೇಕಿಂಗ್ ಶುಲ್ಕ ನಷ್ಟ ತಪ್ಪಿಸಲು) 24K ಚಿನ್ನದ ನಾಣ್ಯ ಅಥವಾ ಡಿಜಿಟಲ್ ಗೋಲ್ಡ್ / SGB ಆರಿಸಿಕೊಳ್ಳಿ.<br><br>
          <strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong> ✅ <strong>ಹೌದು, ಖರೀದಿಸಬಹುದು!</strong> ಹಬ್ಬದ ದಿನಗಳಲ್ಲಿ ಹೆಚ್ಚಾಗುವ ಗರಿಷ್ಠ ಮೇಕಿಂಗ್ ಶುಲ್ಕದಿಂದ ನೀವು ಈಗಲೇ ಬಚಾವಾಗಬಹುದು.
        `
      },
      'sell_today': {
        q: '🔴 ನಾನು ಈಗ ಚಿನ್ನ ಮಾರಾಟ ಮಾಡಬಹುದೇ? (Can I Sell Gold Now?)',
        badge: '🟡 ಭಾಗಶಃ ಲಾಭ ಗಳಿಕೆ ಮಾತ್ರ (Partial Profit Booking)',
        badgeColor: '#FEF3C7',
        badgeTextColor: '#92400E',
        content: `
          <strong>1. ಐತಿಹಾಸಿಕ ಡೇಟಾ ವಿಶ್ಲೇಷಣೆ (Historical Trend Analysis):</strong><br>
          2016 ರಲ್ಲಿ 10 ಗ್ರಾಂ ಚಿನ್ನದ ಬೆಲೆ ₹28,623 ಇತ್ತು. ಇಂದು 2026 ರಲ್ಲಿ ₹1,63,040 ತಲುಪಿದ್ದು, ಕಳೆದ 10 ವರ್ಷಗಳಲ್ಲಿ ಬರೋಬ್ಬರಿ <strong>469% ನಿವ್ವಳ ಲಾಭ (+18.9% CAGR)</strong> ನೀಡಿದೆ. ಚಿನ್ನವು ಸಾರ್ವಕಾಲಿಕ ದಾಖಲೆಯ ಉತ್ತುಂಗದಲ್ಲಿದೆ.<br><br>
          <strong>2. ಯಾವಾಗ ಮಾರಾಟ ಮಾಡುವುದು ಸೂಕ್ತ?:</strong><br>
          • ನಿಮಗೆ ತುರ್ತು ನಗದು ಹಣದ ಅಗತ್ಯವಿದ್ದರೆ ಅಥವಾ ರಿಯಲ್ ಎಸ್ಟೇಟ್/ವ್ಯಾಪಾರದಲ್ಲಿ ಮರುಹೂಡಿಕೆ ಮಾಡುವುದಿದ್ದರೆ, ನಿಮ್ಮ ಒಟ್ಟು ಚಿನ್ನದ <strong>20% ರಿಂದ 30% ಭಾಗವನ್ನು ಮಾತ್ರ ಮಾರಿ ಲಾಭ ಗಳಿಸಿ (Partial Profit)</strong>.<br>
          • ಸಂಪೂರ್ಣ ಚಿನ್ನವನ್ನು ಮಾರಬೇಡಿ; ಏಕೆಂದರೆ ಜಾಗತಿಕ ಸೆಂಟ್ರಲ್ ಬ್ಯಾಂಕ್‌ಗಳು ನಿರಂತರವಾಗಿ ಚಿನ್ನವನ್ನು ಸಂಗ್ರಹಿಸುತ್ತಿರುವುದರಿಂದ ದೀರ್ಘಾವಧಿಯಲ್ಲಿ ಬೆಲೆ ಮತ್ತಷ್ಟು ಏರುವ ಪ್ರವೃತ್ತಿ ಹೊಂದಿದೆ.<br><br>
          <strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong> ⚠️ <strong>ಅಗತ್ಯವಿದ್ದರೆ ಮಾತ್ರ ಭಾಗಶಃ ಮಾರಿ!</strong> ಸಂಪೂರ್ಣ ಮಾರಾಟಕ್ಕೆ ಇದು ಸೂಕ್ತವಲ್ಲ.
        `
      },
      'wedding': {
        q: '💍 ಮದುವೆಗೆ ಒಡವೆ ಕೊಳ್ಳಲು ಇದು ಸರಿಯಾದ ಸಮಯವೇ? (Wedding Jewellery Timing)',
        badge: '🟢 ಅತ್ಯುತ್ತಮ ಪೂರ್ವಭಾವಿ ಖರೀದಿ ಸಮಯ',
        badgeColor: '#DCFCE7',
        badgeTextColor: '#15803D',
        content: `
          <strong>1. ಐತಿಹಾಸಿಕ ಡೇಟಾ ವಿಶ್ಲೇಷಣೆ:</strong><br>
          ಕರ್ನಾಟಕದಲ್ಲಿ ನವೆಂಬರ್, ಡಿಸೆಂಬರ್ ಮತ್ತು ಜನವರಿ-ಫೆಬ್ರವರಿ ತಿಂಗಳುಗಳಲ್ಲಿ ಮದುವೆ ಸೀಸನ್ ಉತ್ತುಂಗದಲ್ಲಿರುತ್ತದೆ. ಆ ಸಮಯದಲ್ಲಿ ಶೋರೂಂಗಳಲ್ಲಿ ಮೇಕಿಂಗ್ ಚಾರ್ಜ್ 14% ರಿಂದ 18% ವರೆಗೆ ಏರಿಕೆಯಾಗುತ್ತದೆ ಮತ್ತು ರಶ್ ಇರುತ್ತದೆ.<br><br>
          <strong>2. ನಿಮ್ಮ ಉಳಿತಾಯ ಲೆಕ್ಕಾಚಾರ:</strong><br>
          ಈಗಲೇ (2-3 ತಿಂಗಳು ಮುಂಚಿತವಾಗಿ) ಆರ್ಡರ್ ಮಾಡಿ ಆಭರಣ ತಯಾರಿಸಿಕೊಂಡರೆ:<br>
          • ಮೇಕಿಂಗ್ ಚಾರ್ಜ್‌ನಲ್ಲಿ 8% ರಿಂದ 10% ರಿಯಾಯಿತಿ ಚೌಕಾಸಿ ಮಾಡಬಹುದು (100 ಗ್ರಾಂ ಒಡವೆಗೆ ಸುಮಾರು ₹30,000 - ₹50,000 ಉಳಿತಾಯ!).<br>
          • ನಿಖರ ಹಾಲ್‌ಮಾರ್ಕ್ ಮತ್ತು ಡಿಸೈನ್ ಫಿನಿಶಿಂಗ್ ಪಡೆಯಲು ಸಾಕಷ್ಟು ಸಮಯಾವಕಾಶ ಸಿಗುತ್ತದೆ.<br><br>
          <strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong> ✅ <strong>ತಕ್ಷಣ ಆರ್ಡರ್ ಮಾಡಿ!</strong> ಮದುವೆ ದಿನದವರೆಗೆ ಕಾಯಬೇಡಿ.
        `
      },
      'long_term': {
        q: '📈 5-10 ವರ್ಷಗಳ ಹೂಡಿಕೆಗೆ ಚಿನ್ನ ಈಗ ಉತ್ತಮವೇ? (5-10 Yr Investment)',
        badge: '🟢 ದೀರ್ಘಾವಧಿಗೆ ಅತ್ಯುನ್ನತ ರಕ್ಷಣೆ & ಬೆಳವಣಿಗೆ',
        badgeColor: '#DCFCE7',
        badgeTextColor: '#15803D',
        content: `
          <strong>1. 125 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಸಾಕ್ಷ್ಯ (1901-2026 Archive):</strong><br>
          1947 ರಲ್ಲಿ ಕೇವಲ ₹88.62 ಇದ್ದ 10 ಗ್ರಾಂ ಚಿನ್ನ, 2000 ರಲ್ಲಿ ₹4,400, 2016 ರಲ್ಲಿ ₹28,623, ಇಂದು 2026 ರಲ್ಲಿ ₹1,63,040 ಆಗಿದೆ. ಕಳೆದ ಯಾವುದೇ 10-ವರ್ಷಗಳ ಅವಧಿಯನ್ನು ತೆಗೆದುಕೊಂಡರೂ ಚಿನ್ನವು ನಷ್ಟ ನೀಡಿದ ಯಾವುದೇ ಇತಿಹಾಸವಿಲ್ಲ!<br><br>
          <strong>2. ಹಣದುಬ್ಬರ ವಿರುದ್ಧ ಅತ್ಯುತ್ತಮ ಗುರಾಣಿ (Inflation Hedge):</strong><br>
          ಕರೆನ್ಸಿ ಮೌಲ್ಯ ಕುಸಿತ ಮತ್ತು ಬ್ಯಾಂಕ್ ಎಫ್‌ಡಿ ಬಡ್ಡಿದರಗಳಿಗಿಂತ (6.8%) ಚಿನ್ನವು ಮೂರು ಪಟ್ಟು ಹೆಚ್ಚಿನ ವಾರ್ಷಿಕ ರಿಟರ್ನ್ಸ್ (+18.9% CAGR) ತಂದುಕೊಡುತ್ತದೆ.<br><br>
          <strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong> ✅ <strong>ಖಂಡಿತ ಹೂಡಿಕೆ ಮಾಡಿ!</strong> 5 ರಿಂದ 10 ವರ್ಷಗಳ ಕಾಲಾವಧಿಗೆ ಚಿನ್ನಕ್ಕಿಂತ ಸುರಕ್ಷಿತ ಸ್ವತ್ತು ಇನ್ನೊಂದಿಲ್ಲ.
        `
      },
      'gold_vs_silver': {
        q: '⚖️ ಚಿನ್ನಕ್ಕಿಂತ ಈಗ ಬೆಳ್ಳಿ ಖರೀದಿಸುವುದು ಲಾಭದಾಯಕವೇ? (Gold vs Silver Right Now)',
        badge: '🥈 ಬೆಳ್ಳಿಯಲ್ಲಿ ಹೂಡಿಕೆಗೆ ಭಾರಿ ಸಾಮರ್ಥ್ಯವಿದೆ',
        badgeColor: '#EFF6FF',
        badgeTextColor: '#0284C7',
        content: `
          <strong>1. Gold-to-Silver Ratio (GSR) ವಿಶ್ಲೇಷಣೆ:</strong><br>
          ಇಂದಿನ ಚಿನ್ನ-ಬೆಳ್ಳಿ ಅನುಪಾತ <strong>62.7</strong> ರಷ್ಟಿದೆ. ಜಾಗತಿಕವಾಗಿ ಸೋಲಾರ್ ಪ್ಯಾನಲ್‌ಗಳು, ಎಲೆಕ್ಟ್ರಿಕ್ ವಾಹನಗಳು (EV) ಮತ್ತು ಎಲೆಕ್ಟ್ರಾನಿಕ್ಸ್ ಚಿಪ್‌ಗಳಲ್ಲಿ ಬೆಳ್ಳಿಯ ಕೈಗಾರಿಕಾ ಬಳಕೆ ಶೇಕಡಾ 60% ಕ್ಕಿಂತ ಹೆಚ್ಚಾಗಿದೆ.<br><br>
          <strong>2. ಬೆಳವಣಿಗೆಯ ಸಂಭಾವ್ಯತೆ (Upside Potential):</strong><br>
          ಚಿನ್ನವು ಈಗಾಗಲೇ ಸಾರ್ವಕಾಲಿಕ ಎತ್ತರದಲ್ಲಿದೆ. ಆದರೆ ಬೆಳ್ಳಿಯು ಮುಂದಿನ 2-3 ವರ್ಷಗಳಲ್ಲಿ ಚಿನ್ನಕ್ಕಿಂತಲೂ ಹೆಚ್ಚಿನ ಶೇಕಡಾವಾರು ಜಿಗಿತ ಕಾಣುವ ಸಾಧ್ಯತೆಯಿದೆ ಎಂದು ಜಾಗತಿಕ ಕಮಾಡಿಟಿ ವರದಿಗಳು ಸೂಚಿಸುತ್ತವೆ.<br><br>
          <strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong> 💡 ನಿಮ್ಮ ಹೂಡಿಕೆಯ <strong>70% ಚಿನ್ನದಲ್ಲಿ ಮತ್ತು 30% 999 ಶುದ್ಧ ಬೆಳ್ಳಿಯಲ್ಲಿ (Silver Bars)</strong> ಹಂಚಿಕೆ ಮಾಡುವುದು ಅತ್ಯಂತ ಜಾಣತನದ ತಂತ್ರ.
        `
      }
    };

        // ══════════════════════════════════════════════════════
    // REAL LLM AI GOLD ADVISOR BACKEND CONNECTION
    // ══════════════════════════════════════════════════════
    async function queryGoldLLM(userPrompt, defaultBadge = '🟢 AI ವಿಶ್ಲೇಷಣೆ') {
      const outBox = document.getElementById('ai-gold-output-box');
      const qElem = document.getElementById('ai-output-question');
      const badgeElem = document.getElementById('ai-output-verdict-badge');
      const contentElem = document.getElementById('ai-output-content');

      qElem.textContent = '❓ ' + userPrompt;
      badgeElem.textContent = '⚡ AI ವಿಶ್ಲೇಷಿಸುತ್ತಿದೆ...';
      badgeElem.style.background = '#FEF3C7';
      badgeElem.style.color = '#92400E';
      contentElem.innerHTML = '<div style="display:flex; align-items:center; gap:12px; padding:18px 0;"><div style="width:24px; height:24px; border:3px solid #D97706; border-top-color:transparent; border-radius:50%; animation:spin 0.8s linear infinite;"></div><div style="font-size:15px; font-weight:700; color:#475569;">10 ವರ್ಷಗಳ ಐತಿಹಾಸಿಕ ಮಾರುಕಟ್ಟೆ ಡೇಟಾ ಮತ್ತು ರಿಯಲ್ AI ಮಾದರಿಯಿಂದ ವಿಶ್ಲೇಷಿಸಲಾಗುತ್ತಿದೆ...</div></div>';
      
      outBox.style.display = 'block';
      outBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

      try {
        const resp = await fetch('/api/ask-ai', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ prompt: userPrompt })
        });

        if (!resp.ok) throw new Error('API Response not ok');
        const data = await resp.json();
        
        let answerText = data.answer || 'ಕ್ಷಮಿಸಿ, ವಿಶ್ಲೇಷಣೆ ಪಡೆಯಲು ಸಾಧ್ಯವಾಗಲಿಲ್ಲ. ದಯವಿಟ್ಟು ಮತ್ತೊಮ್ಮೆ ಪ್ರಯತ್ನಿಸಿ.';
        
        // Extract verdict badge if present in text
        let verdict = defaultBadge;
        if (answerText.includes('ಖರೀದಿಸಬಹುದು') || answerText.includes('ಖರೀದಿಗೆ')) {
          verdict = '🟢 ಖರೀದಿಗೆ ಸುವರ್ಣಾವಕಾಶ';
          badgeElem.style.background = '#DCFCE7';
          badgeElem.style.color = '#15803D';
        } else if (answerText.includes('ಮಾರಾಟ') || answerText.includes('ಲಾಭ')) {
          verdict = '🟡 ಭಾಗಶಃ ಲಾಭ ಗಳಿಕೆ';
          badgeElem.style.background = '#FEF3C7';
          badgeElem.style.color = '#92400E';
        } else if (answerText.includes('ಬೆಳ್ಳಿ') || answerText.includes('Silver')) {
          verdict = '🥈 ಬೆಳ್ಳಿಯಲ್ಲಿ ಹೂಡಿಕೆ ಸಾಮರ್ಥ್ಯ';
          badgeElem.style.background = '#EFF6FF';
          badgeElem.style.color = '#0284C7';
        } else {
          verdict = '🔮 AI ತಜ್ಞರ ಮುನ್ನೋಟ & ವಿಶ್ಲೇಷಣೆ';
          badgeElem.style.background = '#FEF3C7';
          badgeElem.style.color = '#92400E';
        }

        badgeElem.textContent = verdict;

        // Convert markdown bold and bullets to HTML
        let formatted = answerText
          .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
          .replace(/^[•\-]\s+(.*)$/gm, '<li style="margin-bottom:6px;">$1</li>')
          .replace(/\n\n/g, '<br><br>')
          .replace(/\n/g, '<br>');

        contentElem.innerHTML = `<div style="font-size:15.5px; line-height:1.8; color:#1E293B;">${formatted}</div>
          <div style="margin-top:14px; padding-top:10px; border-top:1px dashed #E2E8F0; font-size:12px; color:#64748B; display:flex; justify-content:space-between; align-items:center;">
            <span>🤖 Provider: ${data.provider || 'Karnata Neural Edge AI'}</span>
            <span>⚡ ರಿಯಲ್-ಟೈಮ್ ಲೈವ್ ವಿಶ್ಲೇಷಣೆ</span>
          </div>`;

      } catch (err) {
        console.warn('Real AI API Error, using fallback:', err);
        askGoldAILocalFallback(userPrompt);
      }
    }

    function askGoldAI(key) {
      const questions = {
        'buy_today': 'ನಾನು ಇಂದು ಚಿನ್ನ ಖರೀದಿಸಬಹುದೇ? ಇಂದಿನ ದರ ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಸ್ಥಿತಿ ವಿಶ್ಲೇಷಿಸಿ.',
        'sell_today': 'ನಾನು ಈಗ ನನ್ನ ಬಳಿಯಿರುವ ಚಿನ್ನವನ್ನು ಮಾರಾಟ ಮಾಡಬಹುದೇ? ಲಾಭ ಗಳಿಕೆಗೆ ಇದು ಸರಿಯಾದ ಸಮಯವೇ?',
        'wedding': 'ಮುಂಬರುವ ಮದುವೆಗೆ ಒಡವೆ ಕೊಳ್ಳಲು ಇದು ಸರಿಯಾದ ಸಮಯವೇ? ಎಷ್ಟು ಉಳಿತಾಯ ಮಾಡಬಹುದು?',
        'long_term': '5 ರಿಂದ 10 ವರ್ಷಗಳ ದೀರ್ಘಾವಧಿ ಹೂಡಿಕೆಗೆ ಚಿನ್ನ ಈಗ ಉತ್ತಮವೇ? ರಿಟರ್ನ್ಸ್ ಹೇಗಿರಬಹುದು?',
        'gold_vs_silver': 'ಚಿನ್ನಕ್ಕಿಂತ ಈಗ ಬೆಳ್ಳಿ ಖರೀದಿಸುವುದು ಲಾಭದಾಯಕವೇ? ಗೋಲ್ಡ್-ಟು-ಸಿಲ್ವರ್ ಅನುಪಾತವೇನು?'
      };
      const q = questions[key] || 'ಚಿನ್ನದ ಮಾರುಕಟ್ಟೆ ವಿಶ್ಲೇಷಣೆ ತಿಳಿಸಿ';
      queryGoldLLM(q);
    }

    function askCustomGoldAI() {
      const input = document.getElementById('ai-gold-custom-input');
      const text = (input.value || '').trim();
      if (!text) {
        askGoldAI('buy_today');
        return;
      }
      queryGoldLLM(text, '🔍 AI ಕಸ್ಟಮ್ ವಿಶ್ಲೇಷಣೆ');
    }

    function askGoldAILocalFallback(qText) {
      const outBox = document.getElementById('ai-gold-output-box');
      const badgeElem = document.getElementById('ai-output-verdict-badge');
      const contentElem = document.getElementById('ai-output-content');
      
      const g24 = GOLD_RATES['24k'];
      const g22 = GOLD_RATES['22k'];

      badgeElem.textContent = '🟢 AI ಲೈವ್ ವಿಶ್ಲೇಷಣೆ';
      badgeElem.style.background = '#DCFCE7';
      badgeElem.style.color = '#15803D';
      
      contentElem.innerHTML = `
        <strong>1. ಇಂದಿನ ಲೈವ್ ಮಾರುಕಟ್ಟೆ ಸ್ಥಿತಿ (2026 Rates):</strong><br>
        ಇಂದು 24K ಅಪರಂಜಿ ಚಿನ್ನದ ದರ ₹${g24.toLocaleString('en-IN')}/ಗ್ರಾಂ (₹${(g24*10).toLocaleString('en-IN')}/10g) ಮತ್ತು 22K ಆಭರಣ ಬಂಗಾರ ₹${g22.toLocaleString('en-IN')}/ಗ್ರಾಂ ಆಗಿದೆ.<br><br>
        <strong>2. AI ತಜ್ಞರ ಶಿಫಾರಸು:</strong><br>
        • ಹೂಡಿಕೆ ಉದ್ದೇಶಕ್ಕೆ SGB ಅಥವಾ ಡಿಜಿಟಲ್ ಗೋಲ್ಡ್‌ನಲ್ಲಿ SIP ಮಾದರಿಯಲ್ಲಿ ಹೂಡಿಕೆ ಮಾಡಿ.<br>
        • ಆಭರಣ ಖರೀದಿಗೆ ಮುಂಚಿತವಾಗಿ ಆರ್ಡರ್ ನೀಡಿ 8-10% ಮೇಕಿಂಗ್ ಶುಲ್ಕ ರಿಯಾಯಿತಿ ಪಡೆಯಿರಿ.<br><br>
        <strong>3. ಅಂತಿಮ ತೀರ್ಮಾನ:</strong> ✅ <strong>ಖರೀದಿಗೆ ಅನುಕೂಲಕರ ಸಮಯವಾಗಿದೆ.</strong>
      `;
    }


      if (text.includes('ಮಾರಾಟ') || text.includes('sell') || text.includes('ಮಾರ')) {
        askGoldAI('sell_today');
      } else if (text.includes('ಮದುವೆ') || text.includes('wedding') || text.includes('ಆಭರಣ') || text.includes('ಒಡವೆ')) {
        askGoldAI('wedding');
      } else if (text.includes('ಬೆಳ್ಳಿ') || text.includes('silver') || text.includes('ಹೋಲಿಕೆ')) {
        askGoldAI('gold_vs_silver');
      } else if (text.includes('ವರ್ಷ') || text.includes('ಹೂಡಿಕೆ') || text.includes('invest') || text.includes('sgb') || text.includes('ಬಾಂಡ್')) {
        askGoldAI('long_term');
      } else {
        askGoldAI('buy_today');
      }
    }

    function switchGoldTab(tab) {
      currentTab = tab;
      document.getElementById('tab-live').classList.toggle('active', tab === 'live');
      document.getElementById('tab-analyzer').classList.toggle('active', tab === 'analyzer');
      document.getElementById('tab-calculator').classList.toggle('active', tab === 'calculator');

      document.getElementById('view-live').style.display = tab === 'live' ? 'block' : 'none';
      document.getElementById('view-analyzer').style.display = tab === 'analyzer' ? 'block' : 'none';
      document.getElementById('view-calculator').style.display = tab === 'calculator' ? 'block' : 'none';

      if (tab === 'analyzer') {
        renderGoldTrendChart('10y');
      }
    }

    function initGoldData() {
      fetch('/data/gold_rates.json?v=' + Date.now())
        .then(r => r.json())
        .then(data => {
          if (data && data.base) {
            GOLD_RATES['24k'] = data.base['24k_per_gram'] || GOLD_RATES['24k'];
            GOLD_RATES['22k'] = data.base['22k_per_gram'] || GOLD_RATES['22k'];
            GOLD_RATES['18k'] = data.base['18k_per_gram'] || GOLD_RATES['18k'];
            GOLD_RATES['silver'] = data.base['silver_per_gram'] || GOLD_RATES['silver'];
          }
          renderLiveDisplay();
        })
        .catch(e => {
          console.warn("Gold rates fetch fallback:", e);
          renderLiveDisplay();
        });
    }

    function renderLiveDisplay() {
      const g24 = GOLD_RATES['24k'];
      const g22 = GOLD_RATES['22k'];
      const sil = GOLD_RATES['silver'];

      document.getElementById('stat-24k-rate').textContent = `₹${g24.toLocaleString('en-IN')}`;
      document.getElementById('stat-22k-rate').textContent = `₹${g22.toLocaleString('en-IN')}`;
      document.getElementById('stat-silver-rate').textContent = `₹${sil.toFixed(2)}`;

      const gsr = (g24 / sil).toFixed(1);
      document.getElementById('stat-gsr-val').textContent = gsr;

      document.getElementById('card-24k-rate').textContent = `₹${g24.toLocaleString('en-IN')}`;
      document.getElementById('card-24k-8g').textContent = `₹${(g24 * 8).toLocaleString('en-IN')}`;
      document.getElementById('card-24k-10g').textContent = `₹${(g24 * 10).toLocaleString('en-IN')}`;
      document.getElementById('card-24k-100g').textContent = `₹${(g24 * 100).toLocaleString('en-IN')}`;

      document.getElementById('card-22k-rate').textContent = `₹${g22.toLocaleString('en-IN')}`;
      document.getElementById('card-22k-8g').textContent = `₹${(g22 * 8).toLocaleString('en-IN')}`;
      document.getElementById('card-22k-10g').textContent = `₹${(g22 * 10).toLocaleString('en-IN')}`;
      document.getElementById('card-22k-100g').textContent = `₹${(g22 * 100).toLocaleString('en-IN')}`;

      document.getElementById('card-silver-rate').textContent = `₹${sil.toFixed(2)}`;
      document.getElementById('card-silver-10g').textContent = `₹${(sil * 10).toLocaleString('en-IN')}`;
      document.getElementById('card-silver-100g').textContent = `₹${(sil * 100).toLocaleString('en-IN')}`;
      document.getElementById('card-silver-1kg').textContent = `₹${(sil * 1000).toLocaleString('en-IN')}`;

      // Render City Table
      const cityTbody = document.getElementById('city-rates-tbody');
      cityTbody.innerHTML = '';
      CITY_RATES_LIST.forEach(c => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight:800; color:#0F172A;">${c.name}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹${c.g24.toLocaleString('en-IN')}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#D97706;">₹${c.g22.toLocaleString('en-IN')}</td>
          <td style="font-family:'Inter',sans-serif; color:#64748B;">₹${c.g18.toLocaleString('en-IN')}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#334155;">₹${c.sil.toFixed(2)}</td>
          <td style="font-family:'Inter',sans-serif; color:#475569;">₹${(c.sil * 1000).toLocaleString('en-IN')}</td>
        `;
        cityTbody.appendChild(tr);
      });

      // Render 125Y Historical Table
      const histTbody = document.getElementById('hist-125y-tbody');
      histTbody.innerHTML = '';
      HIST_125Y.forEach(h => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#78350F;">${h.year}</td>
          <td style="font-weight:900; font-family:'Inter',sans-serif; color:#B45309;">₹${h.gold10g.toLocaleString('en-IN')}</td>
          <td style="font-family:'Inter',sans-serif; color:#64748B;">₹${(h.gold10g / 10).toFixed(2)}</td>
          <td style="font-family:'Inter',sans-serif; color:#475569;">₹${h.silver10g.toLocaleString('en-IN')}</td>
          <td style="font-size:13px; color:#334155;">${h.event}</td>
        `;
        histTbody.appendChild(tr);
      });

      calculateJewelleryBill();
      calculateOldGoldExchange();
    }

    function calculateJewelleryBill() {
      const purity = document.getElementById('bill-purity').value;
      const weight = parseFloat(document.getElementById('bill-weight').value) || 0;
      const makingPct = parseFloat(document.getElementById('bill-making').value) || 0;

      const ratePerGram = purity === '24' ? GOLD_RATES['24k'] : (purity === '18' ? GOLD_RATES['18k'] : GOLD_RATES['22k']);
      const rawGoldVal = Math.round(weight * ratePerGram);
      const makingVal = Math.round(rawGoldVal * (makingPct / 100));
      const subTotal = rawGoldVal + makingVal;
      const gstVal = Math.round(subTotal * 0.03);
      const totalInvoice = subTotal + gstVal;

      document.getElementById('bill-raw-val').textContent = `₹${rawGoldVal.toLocaleString('en-IN')}`;
      document.getElementById('bill-making-val').textContent = `₹${makingVal.toLocaleString('en-IN')}`;
      document.getElementById('bill-gst-val').textContent = `₹${gstVal.toLocaleString('en-IN')}`;
      document.getElementById('bill-total-val').textContent = `₹${totalInvoice.toLocaleString('en-IN')}`;
    }

    function calculateOldGoldExchange() {
      const purityFactor = parseFloat(document.getElementById('old-purity').value) || 0.916;
      const grossWt = parseFloat(document.getElementById('old-gross-wt').value) || 0;
      const stoneDeduct = parseFloat(document.getElementById('old-stone-wt').value) || 0;

      const netGoldWt = Math.max(0, grossWt - stoneDeduct);
      const meltLossWt = netGoldWt * 0.015; // 1.5% standard melting loss
      const pureGoldWt = (netGoldWt - meltLossWt) * purityFactor;

      const g24Rate = GOLD_RATES['24k'];
      const totalCashValue = Math.round(pureGoldWt * g24Rate);

      document.getElementById('old-net-wt').textContent = `${netGoldWt.toFixed(2)} ಗ್ರಾಂ`;
      document.getElementById('old-melt-loss').textContent = `-${meltLossWt.toFixed(2)} ಗ್ರಾಂ`;
      document.getElementById('old-pure-wt').textContent = `${pureGoldWt.toFixed(2)} ಗ್ರಾಂ (24K Equiv)`;
      document.getElementById('old-cash-val').textContent = `₹${totalCashValue.toLocaleString('en-IN')}`;
    }

    function shareGoldWhatsApp() {
      const g24 = GOLD_RATES['24k'];
      const g22 = GOLD_RATES['22k'];
      const sil = GOLD_RATES['silver'];
      const text = `👑 *Karnata.in — ಇಂದಿನ ಚಿನ್ನ & ಬೆಳ್ಳಿ ದರ (Karnataka Live)*\n\n• 24K ಅಪರಂಜಿ ಚಿನ್ನ: *₹${g24.toLocaleString('en-IN')} / ಗ್ರಾಂ*\n• 22K ಆಭರಣ ಚಿನ್ನ: *₹${g22.toLocaleString('en-IN')} / ಗ್ರಾಂ*\n• 1 ಪವನ್ (8g): *₹${(g22*8).toLocaleString('en-IN')}*\n• 999 ಬೆಳ್ಳಿ ದರ: *₹${sil.toFixed(2)} / ಗ್ರಾಂ* (₹${(sil*1000).toLocaleString('en-IN')}/Kg)\n\nಎಲ್ಲಾ ಜಿಲ್ಲೆಗಳ ಲೈವ್ ದರ, ಆಭರಣ ಬಿಲ್ & ಎಕ್ಸ್‌ಚೇಂಜ್ ಕ್ಯಾಲ್ಕುಲೇಟರ್ ವೀಕ್ಷಿಸಿ:\nhttps://karnata.in/gold-rate.html`;
      window.open('https://api.whatsapp.com/send?text=' + encodeURIComponent(text), '_blank');
    }

    function updateChartTimeframe(tf, btn) {
      document.querySelectorAll('.time-pill').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderGoldTrendChart(tf);
    }

    function renderGoldTrendChart(tf) {
      const ctx = document.getElementById('goldTrendChart').getContext('2d');
      if (chartInstance) {
        chartInstance.destroy();
      }

      let labels = [];
      let prices = [];

      if (tf === '1y') {
        labels = ['ಆಗ 25', 'ಸೆಪ್ 25', 'ಅಕ್ಟೋ 25', 'ನವೆಂ 25', 'ಡಿಸೆಂ 25', 'ಜನ 26', 'ಫೆಬ್ರ 26', 'ಮಾರ್ಚ್ 26', 'ಏಪ್ರಿ 26', 'ಮೇ 26', 'ಜೂನ್ 26', 'ಆಗ 26'];
        prices = [12800, 13100, 13650, 14200, 14500, 14800, 15100, 15300, 15650, 15900, 16150, 16304];
      } else if (tf === '5y') {
        labels = ['2022', '2023', '2024', '2025', '2026'];
        prices = [5267, 6150, 7850, 12500, 16304];
      } else if (tf === '125y') {
        labels = HIST_125Y.map(h => h.year.toString());
        prices = HIST_125Y.map(h => h.gold10g / 10);
      } else {
        // 10 Years (2016-2026)
        labels = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026'];
        prices = [2862, 2966, 3143, 3522, 4865, 4872, 5267, 6150, 7850, 12500, 16304];
      }

      const gradient = ctx.createLinearGradient(0, 0, 0, 260);
      gradient.addColorStop(0, 'rgba(245, 158, 11, 0.35)');
      gradient.addColorStop(1, 'rgba(245, 158, 11, 0.0)');

      chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: labels,
          datasets: [{
            label: '24K ಚಿನ್ನದ ದರ (₹/ಗ್ರಾಂ)',
            data: prices,
            borderColor: '#D97706',
            backgroundColor: gradient,
            fill: true,
            tension: 0.35,
            borderWidth: 3.5,
            pointBackgroundColor: '#78350F',
            pointBorderColor: '#FFFFFF',
            pointBorderWidth: 2,
            pointRadius: 5,
            pointHoverRadius: 7
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: { display: false },
            tooltip: {
              backgroundColor: '#0F172A',
              titleFont: { family: 'Inter', size: 12, weight: 'bold' },
              bodyFont: { family: 'Inter', size: 13, weight: 'bold' },
              padding: 10,
              cornerRadius: 8,
              callbacks: {
                label: function(c) {
                  return ` 24K ಚಿನ್ನ: ₹${c.parsed.y.toLocaleString('en-IN')} / ಗ್ರಾಂ`;
                }
              }
            }
          },
          scales: {
            y: {
              ticks: {
                callback: function(v) { return '₹' + v.toLocaleString('en-IN'); },
                font: { family: 'Inter', size: 11, weight: '600' },
                color: '#64748B'
              },
              grid: { color: '#E2E8F0', strokeDash: [4, 4] }
            },
            x: {
              grid: { display: false },
              ticks: { font: { family: 'Inter', size: 11, weight: 'bold' }, color: '#334155' }
            }
          }
        }
      });
    }

    document.addEventListener('DOMContentLoaded', () => {
      initGoldData();
    });
  