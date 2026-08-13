import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os
import re
import difflib
import folium
import streamlit.components.v1 as components

# ಪೇಜ್ ಸೆಟ್ಟಿಂಗ್ಸ್
st.set_page_config(page_title="ಕರ್ನಾಟಕ ವಿಧಾನಸಭೆ ಚುನಾವಣಾ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್", layout="wide")

# ಪಕ್ಷಗಳ ಬಣ್ಣದ ಕೋಡ್ (Party Colors)
PARTY_COLORS = {
    "INC": "#1f77b4", "INC(I)": "#3182bd",
    "BJP": "#ff7f0e", "JNP": "#ff7f0e",
    "JD": "#2ca02c", "JD(S)": "#31a354",
    "KRPP": "#9467bd", "SKP": "#e377c2",
    "IND": "#7f7f7f",
    "CPI": "#de2d26", "CPM": "#a50f15",
    "RPI": "#8c564b", "MUL": "#3182bd"
}
DEFAULT_COLOR = "#bdc3c7"

# ಪಕ್ಷಗಳ ಹೆಸರುಗಳ ಕನ್ನಡ ವಿವರಣೆ
PARTY_KANNADA = {
    "INC": "ಕಾಂಗ್ರೆಸ್ (INC)",
    "INC(I)": "ಕಾಂಗ್ರೆಸ್ ಐ (INC-I)",
    "BJP": "ಬಿಜೆಪಿ (BJP)",
    "JNP": "ಜನತಾ ಪಕ್ಷ (JNP)",
    "JD(S)": "ಜೆಡಿಎಸ್ (JD-S)",
    "JD": "ಜನತಾ ದಳ (JD)",
    "IND": "ಪಕ್ಷೇತರ (IND)",
    "KRPP": "ಕೆಆರ್‌ಪಿಪಿ (KRPP)",
    "SKP": "ಎಸ್‌.ಕೆ.ಪಿ (SKP)",
    "CPI": "ಸಿಪಿಐ (CPI)",
    "CPM": "ಸಿಪಿಎಂ (CPM)",
    "RPI": "ಆರ್‌ಪಿಐ (RPI)"
}

# ಪ್ರಮುಖ ಕ್ಷೇತ್ರಗಳ ಮತ್ತು ವರ್ಗಗಳ ಕನ್ನಡ ನಿಘಂಟು
KANNADA_DICT = {
    "afzalpur": "ಅಫ್ಜಲ್ ಪುರ",
    "alland": "ಆಳಂದ",
    "anekal": "ಆನೇಕಲ್",
    "ankola": "ಅಂಕೋಲ",
    "arabhavi": "ಅರಭಾವಿ",
    "arkalgud": "ಅರಕಲಗೂಡು",
    "arsikere": "ಅರಸೀಕೆರೆ",
    "athani": "ಅಥಣಿ",
    "aurad": "ಔರಾದ್",
    "btmlayout": "ಬಿ.ಟಿ.ಎಂ. ಲೇಔಟ್",
    "btm layout": "ಬಿ.ಟಿ.ಎಂ. ಲೇಔಟ್",
    "babaleshwar": "ಬಬಲೇಶ್ವರ",
    "badami": "ಬಾದಾಮಿ",
    "bagalkot": "ಬಾಗಲಕೋಟೆ",
    "bagepalli": "ಬಾಗೇಪಲ್ಲಿ",
    "bailhongal": "ಬೈಲಹೊಂಗಲ",
    "bangalore south": "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ",
    "bengaluru south": "ಬೆಂಗಳೂರು ದಕ್ಷಿಣ",
    "bangalore north": "ಬೆಂಗಳೂರು ಉತ್ತರ",
    "bengaluru north": "ಬೆಂಗಳೂರು ಉತ್ತರ",
    "bangalore central": "ಬೆಂಗಳೂರು ಕೇಂದ್ರ",
    "bengaluru central": "ಬೆಂಗಳೂರು ಕೇಂದ್ರ",
    "basavakalyan": "ಬಸವಕಲ್ಯಾಣ",
    "basavanagudi": "ಬಸವನಗುಡಿ",
    "belgaum": "ಬೆಳಗಾವಿ",
    "belagavi": "ಬೆಳಗಾವಿ",
    "bellary": "ಬಳ್ಳಾರಿ",
    "ballari": "ಬಳ್ಳಾರಿ",
    "bhadravati": "ಭದ್ರಾವತಿ",
    "bhalki": "ಭಾಲ್ಕಿ",
    "bidar": "ಬೀದರ್",
    "bijapur": "ವಿಜಯಪುರ",
    "vijayapura": "ವಿಜಯಪುರ",
    "channapatna": "ಚನ್ನಪಟ್ಟಣ",
    "chikmagalur": "ಚಿಕ್ಕಮಗಳೂರು",
    "chikkamagaluru": "ಚಿಕ್ಕಮಗಳೂರು",
    "chitradurga": "ಚಿತ್ರದುರ್ಗ",
    "davangere": "ದಾವಣಗೆರೆ",
    "dharwad": "ಧಾರವಾಡ",
    "gulbarga": "ಕಲಬುರಗಿ",
    "kalaburagi": "ಕಲಬುರಗಿ",
    "hassan": "ಹಾಸನ",
    "hospet": "ಹೊಸಪೇಟೆ",
    "hosapete": "ಹೊಸಪೇಟೆ",
    "hubli": "ಹುಬ್ಬಳ್ಳಿ",
    "hubballi": "ಹುಬ್ಬಳ್ಳಿ",
    "kolar": "ಕೋಲಾರ",
    "mandya": "ಮಂಡ್ಯ",
    "mangalore": "ಮಂಗಳೂರು",
    "mangaluru": "ಮಂಗಳೂರು",
    "mysore": "ಮೈಸೂರು",
    "mysuru": "ಮೈಸೂರು",
    "raichur": "ರಾಯಚೂರು",
    "shimoga": "ಶಿವಮೊಗ್ಗ",
    "shivamogga": "ಶಿವಮೊಗ್ಗ",
    "tumkur": "ತುಮಕೂರು",
    "tumakuru": "ತುಮಕೂರು",
    "udupi": "ಉಡುಪಿ",
    "varuna": "ವರುಣ",
    "yelburga": "ಯಲಬುರ್ಗಾ",
    "yelahanka": "ಯಲಹಂಕ",

    "sc": "ಪರಿಶಿಷ್ಟ ಜಾತಿ (SC)",
    "st": "ಪರಿಶಿಷ್ಟ ಪಂಗಡ (ST)",
    "none": "ಸಾಮಾನ್ಯ",
    "general": "ಸಾಮಾನ್ಯ"
}

# ಅಭ್ಯರ್ಥಿಗಳ ಹೆಸರುಗಳು ಮತ್ತು ಮನೆತನದ ಹೆಸರುಗಳನ್ನು ಕನ್ನಡಕ್ಕೆ ಭಾಷಾಂತರಿಸುವ ನಿಯಮಗಳು
NAME_REPLACEMENTS = [
    (r'\bM\.Y\.\b', 'ಎಂ.ವೈ.'),
    (r'\bB\.\b', 'ಬಿ.'),
    (r'\bD\.K\.\b', 'ಡಿ.ಕೆ.'),
    (r'\bH\.D\.\b', 'ಎಚ್.ಡಿ.'),
    (r'\bK\.S\.\b', 'ಕೆ.ಎಸ್.'),
    (r'\bA\.T\.\b', 'ಎ.ಟಿ.'),
    (r'\bK\.M\.\b', 'ಕೆ.ಎಂ.'),
    (r'\bM\.T\.\b', 'ಎಂ.ಟಿ.'),
    (r'\bN\.R\.\b', 'ಎನ್.ಆರ್.'),
    (r'\bG\.B\.\b', 'ಜಿ.ಬಿ.'),
    (r'\bB\.R\.\b', 'ಬಿ.ಆರ್.'),
    (r'\bA\.\b', 'ಎ.'), (r'\bC\.\b', 'ಸಿ.'), (r'\bD\.\b', 'ಡಿ.'),
    (r'\bG\.\b', 'ಜಿ.'), (r'\bH\.\b', 'ಎಚ್.'), (r'\bJ\.\b', 'ಜೆ.'),
    (r'\bK\.\b', 'ಕೆ.'), (r'\bL\.\b', 'ಎಲ್.'), (r'\bM\.\b', 'ಎಂ.'),
    (r'\bN\.\b', 'ಎನ್.'), (r'\bP\.\b', 'ಪಿ.'), (r'\bR\.\b', 'ಆರ್.'),
    (r'\bS\.\b', 'ಎಸ್.'), (r'\bT\.\b', 'ಟಿ.'), (r'\bV\.\b', 'ವಿ.'),
    (r'\bPatil\b', 'ಪಾಟೀಲ್'), (r'\bGowda\b', 'ಗೌಡ'), (r'\bReddy\b', 'ರೆಡ್ಡಿ'),
    (r'\bShettar\b', 'ಶೆಟ್ಟರ್'), (r'\bDesai\b', 'ದೇಸಾಯಿ'), (r'\bGuttedar\b', 'ಗುತ್ತೇದಾರ್'),
    (r'\bJarkiholi\b', 'ಜಾರಕಿಹೊಳಿ'), (r'\bBommai\b', 'ಬೊಮ್ಮಾಯಿ'), (r'\bShivakumar\b', 'ಶಿವಕುಮಾರ್'),
    (r'\bSiddaramaiah\b', 'ಸಿದ್ದರಾಮಯ್ಯ'), (r'\bRao\b', 'ರಾವ್'), (r'\bKumar\b', 'ಕುಮಾರ್'),
    (r'\bNaik\b', 'ನಾಯಕ್'), (r'\bPujari\b', 'ಪೂಜಾರಿ'), (r'\bHegde\b', 'ಹೆಗಡೆ'),
    (r'\bSwamy\b', 'ಸ್ವಾಮಿ'), (r'\bSwami\b', 'ಸ್ವಾಮಿ'), (r'\bPrabhu\b', 'ಪ್ರಭು'),
    (r'\bChauhan\b', 'ಚೌಹಾಣ್'), (r'\bShivanna\b', 'ಶಿವಣ್ಣ'), (r'\bBhojaraj\b', 'ಭೋಜರಾಜ್'),
    (r'\bManju\b', 'ಮಂಜು'), (r'\bKumathalli\b', 'ಕುಮಟಳ್ಳಿ'), (r'\bRamalinga\b', 'ರಾಮಲಿಂಗ'),
    (r'\bSrinivas\b', 'ಶ್ರೀನಿವಾಸ್'), (r'\bHullahalli\b', 'ಹುಲ್ಲಹಳ್ಳಿ')
]

# ಕನ್ನಡಕ್ಕೆ ಭಾಷಾಂತರಿಸುವ ಫಂಕ್ಷನ್
def to_kannada(text):
    if not text or pd.isna(text):
        return ""
    s_raw = str(text).strip()
    s_clean = s_raw.lower()
    
    if s_clean in KANNADA_DICT:
        return KANNADA_DICT[s_clean]
        
    out = s_raw
    for pattern, repl in NAME_REPLACEMENTS:
        out = re.sub(pattern, repl, out, flags=re.IGNORECASE)
        
    return out

def clean_str(val):
    if not val:
        return ""
    s = str(val).lower()
    s = re.sub(r'\s*\((sc|st)\)', '', s)
    s = re.sub(r'[^a-z0-9]', '', s)
    return s

ALIAS_MAP = {
    "bengaluru": "bangalore", "ballari": "bellary", "kalaburagi": "gulbarga",
    "vijayapura": "bijapur", "belagavi": "belgaum", "mysuru": "mysore",
    "mangaluru": "mangalore", "shivamogga": "shimoga", "tumakuru": "tumkur",
    "chikkamagaluru": "chikmagalur", "hubballi": "hubli"
}

def resolve_name(geo_clean, csv_dict_keys):
    if geo_clean in csv_dict_keys:
        return geo_clean
    alt = geo_clean
    for k, v in ALIAS_MAP.items():
        if k in alt:
            alt = alt.replace(k, v)
    if alt in csv_dict_keys:
        return alt

    matches = difflib.get_close_matches(geo_clean, csv_dict_keys, n=1, cutoff=0.75)
    return matches[0] if matches else None

def normalize_column_names(df):
    if df.empty:
        return df
    df.columns = [str(c).strip() for c in df.columns]
    mapping = {}
    for col in df.columns:
        c_clean = clean_str(col)
        if c_clean in ["constituency", "constituencyname", "acname", "name"]:
            mapping[col] = "Constituency"
        elif c_clean in ["acno", "acnum", "acnumber", "constituencyno", "constituencynumber", "ac"]:
            mapping[col] = "AC_No"
        elif c_clean in ["winner", "winnername"]:
            mapping[col] = "Winner"
        elif "party" in c_clean and "runner" not in c_clean:
            mapping[col] = "Winner_Party"
        elif "vote" in c_clean and "runner" not in c_clean and "share" not in c_clean:
            mapping[col] = "Winner_Votes"
        elif "share" in c_clean:
            mapping[col] = "Vote_Share"
        elif c_clean in ["runnerup", "runnerupname", "runner"]:
            mapping[col] = "Runner_Up"
        elif "party" in c_clean and "runner" in c_clean:
            mapping[col] = "Runner_Up_Party"
        elif "vote" in c_clean and "runner" in c_clean:
            mapping[col] = "Runner_Up_Votes"
        elif c_clean in ["margin", "winmargin"]:
            mapping[col] = "Margin"
        elif c_clean in ["category", "cat"]:
            mapping[col] = "Category"
        elif c_clean in ["year"]:
            mapping[col] = "Year"
    return df.rename(columns=mapping)

# ಡೇಟಾ ಲೋಡರ್
@st.cache_data
def load_data():
    excel_path = "karnataka_elections_1978_2023.xlsx"
    csv_path = "karnataka_elections_1978_2023.csv"
    
    df = pd.DataFrame()
    if os.path.exists(csv_path):
        try:
            df = pd.read_csv(csv_path)
        except Exception:
            pass

    if df.empty and os.path.exists(excel_path):
        try:
            with open(excel_path, "rb") as f:
                df = pd.read_excel(f)
        except Exception:
            pass

    if df.empty:
        return pd.DataFrame()

    df = normalize_column_names(df)

    if "Constituency" not in df.columns and len(df.columns) >= 2:
        df["Constituency"] = df.iloc[:, 1].astype(str)

    if "AC_No" in df.columns:
        df["AC_No"] = pd.to_numeric(df["AC_No"], errors="coerce")

    for col in ["Winner_Votes", "Runner_Up_Votes", "Margin"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.replace(",", "").str.strip()
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
        
    if "Constituency" in df.columns:
        df["clean_constituency"] = df["Constituency"].apply(clean_str)
        
    return df

df = load_data()

LOCAL_GEOJSON = "karnataka_assembly_224.json"

@st.cache_data
def load_ac_geojson():
    if os.path.exists(LOCAL_GEOJSON):
        if os.path.getsize(LOCAL_GEOJSON) < 50000:
            os.remove(LOCAL_GEOJSON)
            return None
        try:
            with open(LOCAL_GEOJSON, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            os.remove(LOCAL_GEOJSON)
            return None
    return None

geojson_data = load_ac_geojson()

def extract_geojson_ac_no(props):
    for key in ["AC_NO", "ac_no", "AC_NUM", "ac_num", "AC_No", "ac"]:
        if key in props:
            try:
                return int(float(str(props[key])))
            except ValueError:
                pass
    return None

if geojson_data:
    sample_props = geojson_data["features"][0]["properties"]
    ac_name_key = "AC_NAME" if "AC_NAME" in sample_props else ("ac_name" if "ac_name" in sample_props else list(sample_props.keys())[0])

    for feature in geojson_data["features"]:
        raw_name = feature["properties"].get(ac_name_key, "")
        feature["properties"]["clean_name"] = clean_str(raw_name)
        feature["properties"]["parsed_ac_no"] = extract_geojson_ac_no(feature["properties"])

# --- ಹೆಡರ್ ಮತ್ತು ನಿಯಂತ್ರಣಗಳು ---
st.title("🗳️ ಕರ್ನಾಟಕ ವಿಧಾನಸಭೆ ಚುನಾವಣಾ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್")
st.markdown("ವಿಧಾನಸಭಾ ಚುನಾವಣಾ ಫಲಿತಾಂಶಗಳ ವಿವರ (1978 – 2023)")

if df.empty or "Year" not in df.columns:
    st.error("❌ ಡೇಟಾ ಲೋಡ್ ಮಾಡಲು ಸಾಧ್ಯವಾಗಿಲ್ಲ!")
    st.stop()

years = sorted(df["Year"].unique(), reverse=True)
selected_year = st.selectbox("ಚುನಾವಣಾ ವರ್ಷವನ್ನು ಆಯ್ಕೆ ಮಾಡಿ:", years, index=0)
df_year = df[df["Year"] == selected_year].copy()

# ಕನ್ನಡದ ಹೆಸರುಗಳು
df_year["Party_Kannada"] = df_year["Winner_Party"].apply(lambda p: PARTY_KANNADA.get(p, p))
df_year["Constituency_Kannada"] = df_year["Constituency"].apply(to_kannada)
df_year["Winner_Kannada"] = df_year["Winner"].apply(to_kannada)
df_year["Runner_Up_Kannada"] = df_year["Runner_Up"].apply(to_kannada)

# --- ಪ್ರಮುಖ ಮುಖ್ಯಾಂಶಗಳು (KPI) ---
total_seats = len(df_year)
total_winner_votes = int(df_year["Winner_Votes"].sum()) if "Winner_Votes" in df_year else 0
total_runner_votes = int(df_year["Runner_Up_Votes"].sum()) if "Runner_Up_Votes" in df_year else 0

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("ಒಟ್ಟು ಕ್ಷೇತ್ರಗಳು", f"{total_seats}")
with col2:
    st.metric("ಗೆದ್ದವರ ಒಟ್ಟು ಮತಗಳು", f"{total_winner_votes:,}")
with col3:
    st.metric("ಅಂದಾಜು ಒಟ್ಟು ಮತಗಳು", f"{total_winner_votes + total_runner_votes:,}")
with col4:
    st.metric("ಚುನಾವಣಾ ವರ್ಷ", f"{selected_year}")

st.divider()

# --- ಚಾರ್ಟ್‌ಗಳು ---
col_left, col_right = st.columns(2)

party_tally = df_year["Party_Kannada"].value_counts().reset_index()
party_tally.columns = ["ಪಕ್ಷ", "ಸ್ಥಾನಗಳು"]

# ಬಣ್ಣದ ಮ್ಯಾಪಿಂಗ್
party_tally["Color"] = party_tally["ಪಕ್ಷ"].map(
    lambda p: PARTY_COLORS.get(next((k for k, v in PARTY_KANNADA.items() if v == p), p), DEFAULT_COLOR)
)

with col_left:
    st.subheader("ಗೆದ್ದ ಸ್ಥಾನಗಳ ಹಂಚಿಕೆ (Donut Chart)")
    fig_donut = px.pie(
        party_tally,
        names="ಪಕ್ಷ",
        values="ಸ್ಥಾನಗಳು",
        hole=0.5,
        color="ಪಕ್ಷ",
        color_discrete_map={row["ಪಕ್ಷ"]: row["Color"] for _, row in party_tally.iterrows()}
    )
    fig_donut.update_traces(textinfo="percent+label")
    st.plotly_chart(fig_donut, use_container_width=True)

with col_right:
    st.subheader("ಪಕ್ಷವಾರು ಸ್ಥಾನಗಳ ಸಂಖ್ಯೆ (Bar Chart)")
    fig_bar = px.bar(
        party_tally,
        x="ಪಕ್ಷ",
        y="ಸ್ಥಾನಗಳು",
        text="ಸ್ಥಾನಗಳು",
        color="ಪಕ್ಷ",
        color_discrete_map={row["ಪಕ್ಷ"]: row["Color"] for _, row in party_tally.iterrows()}
    )
    fig_bar.update_layout(showlegend=False, yaxis_title="ಗೆದ್ದ ಸ್ಥಾನಗಳು", xaxis_title="ರಾಜಕೀಯ ಪಕ್ಷಗಳು")
    st.plotly_chart(fig_bar, use_container_width=True)

st.divider()

# --- ನಕ್ಷೆ (MAP) ---
st.subheader("🗺️ ಕರ್ನಾಟಕ — ಪ್ರತಿಯೊಂದು ಕ್ಷೇತ್ರದ ವಿಜೇತರು")

if geojson_data:
    has_ac_no_data = "AC_No" in df_year.columns and df_year["AC_No"].notna().sum() > 0
    use_ac_no_matching = (selected_year >= 2008) and has_ac_no_data

    matched_features = 0
    feature_row_map = {}

    if use_ac_no_matching:
        ac_no_lookup = {int(row["AC_No"]): row.to_dict() for _, row in df_year.iterrows() if pd.notna(row["AC_No"])}

        for feature in geojson_data["features"]:
            g_ac_no = feature["properties"].get("parsed_ac_no")
            g_clean = feature["properties"]["clean_name"]
            
            row = None
            if g_ac_no and g_ac_no in ac_no_lookup:
                row = ac_no_lookup[g_ac_no]
            else:
                best_match_key = resolve_name(g_clean, set(df_year["clean_constituency"]))
                if best_match_key:
                    row = df_year[df_year["clean_constituency"] == best_match_key].iloc[0].to_dict()

            if row:
                matched_features += 1
                feature_row_map[g_clean] = row
                
                c_kn = to_kannada(row.get("Constituency", ""))
                w_kn = to_kannada(row.get("Winner", ""))
                r_kn = to_kannada(row.get("Runner_Up", ""))
                wp_kn = PARTY_KANNADA.get(row.get('Winner_Party', ''), row.get('Winner_Party', ''))
                rp_kn = PARTY_KANNADA.get(row.get('Runner_Up_Party', ''), row.get('Runner_Up_Party', ''))

                feature["properties"]["tt_constituency"] = c_kn
                feature["properties"]["tt_winner"] = f"{w_kn} ({wp_kn})"
                feature["properties"]["tt_runner"] = f"{r_kn} ({rp_kn})"
                feature["properties"]["tt_margin"] = f"{int(row.get('Margin', 0)):,}"
            else:
                feature_row_map[g_clean] = None
                feature["properties"]["tt_constituency"] = feature["properties"].get(ac_name_key, "")
                feature["properties"]["tt_winner"] = "ಮಾಹಿತಿಯಿಲ್ಲ"
                feature["properties"]["tt_runner"] = "ಮಾಹಿತಿಯಿಲ್ಲ"
                feature["properties"]["tt_margin"] = "0"

        st.caption(f"⚡ **{matched_features}** / **{len(geojson_data['features'])}** ಕ್ಷೇತ್ರಗಳನ್ನು ಯಶಸ್ವಿಯಾಗಿ ನಕ್ಷೆಯಲ್ಲಿ ಗುರುತಿಸಲಾಗಿದೆ.")
    else:
        data_lookup = {row["clean_constituency"]: row.to_dict() for _, row in df_year.iterrows()}
        csv_keys = set(data_lookup.keys())

        for feature in geojson_data["features"]:
            g_clean = feature["properties"]["clean_name"]
            best_match_key = resolve_name(g_clean, csv_keys)
            row = data_lookup.get(best_match_key) if best_match_key else None
            
            if row:
                matched_features += 1
                feature_row_map[g_clean] = row
                c_kn = to_kannada(row.get("Constituency", ""))
                w_kn = to_kannada(row.get("Winner", ""))
                r_kn = to_kannada(row.get("Runner_Up", ""))
                wp_kn = PARTY_KANNADA.get(row.get('Winner_Party', ''), row.get('Winner_Party', ''))
                rp_kn = PARTY_KANNADA.get(row.get('Runner_Up_Party', ''), row.get('Runner_Up_Party', ''))

                feature["properties"]["tt_constituency"] = c_kn
                feature["properties"]["tt_winner"] = f"{w_kn} ({wp_kn})"
                feature["properties"]["tt_runner"] = f"{r_kn} ({rp_kn})"
                feature["properties"]["tt_margin"] = f"{int(row.get('Margin', 0)):,}"
            else:
                feature_row_map[g_clean] = None
                feature["properties"]["tt_constituency"] = feature["properties"].get(ac_name_key, "")
                feature["properties"]["tt_winner"] = "ಮಾಹಿತಿಯಿಲ್ಲ"
                feature["properties"]["tt_runner"] = "ಮಾಹಿತಿಯಿಲ್ಲ"
                feature["properties"]["tt_margin"] = "0"

        st.caption(f"📍 **{matched_features}** / **{len(geojson_data['features'])}** ಕ್ಷೇತ್ರಗಳನ್ನು ಯಶಸ್ವಿಯಾಗಿ ನಕ್ಷೆಯಲ್ಲಿ ಗುರುತಿಸಲಾಗಿದೆ.")

    def style_function(feature):
        g_clean = feature["properties"].get("clean_name", "")
        row = feature_row_map.get(g_clean)
        if row:
            party = row.get("Winner_Party", "")
            fill_color = PARTY_COLORS.get(party, DEFAULT_COLOR)
        else:
            fill_color = "#bdbdbd"
            
        return {
            "fillColor": fill_color,
            "color": "#333333",
            "weight": 0.6,
            "fillOpacity": 0.85
        }

    m = folium.Map(
        location=[14.8, 76.2],
        zoom_start=7,
        tiles="CartoDB positron"
    )

    m.fit_bounds([[11.5, 74.0], [18.5, 78.5]])

    folium.GeoJson(
        geojson_data,
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(
            fields=["tt_constituency", "tt_winner", "tt_runner", "tt_margin"],
            aliases=["ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ:", "ವಿಜೇತರು:", "ಸಮೀಪದ ಸ್ಪರ್ಧಿ:", "ಮತಗಳ ಅಂತರ:"],
            style="""
                background-color: #1e1e1e;
                color: #ffffff;
                font-family: Arial, sans-serif;
                font-size: 13px;
                padding: 8px 12px;
                border-radius: 6px;
                box-shadow: 2px 2px 8px rgba(0,0,0,0.4);
            """
        )
    ).add_to(m)

    map_html = m._repr_html_()
    components.html(map_html, height=720)

# --- ಫಲಿತಾಂಶಗಳ ಕೋಷ್ಟಕ (TABLE) ---
st.subheader(f"📋 ಪೂರ್ಣ ಫಲಿತಾಂಶಗಳ ವಿವರ ({selected_year})")

df_display = pd.DataFrame()
if "AC_No" in df_year.columns and df_year["AC_No"].notna().sum() > 0:
    df_display["ಕ್ಷೇತ್ರ ಸಂಖ್ಯೆ"] = df_year["AC_No"]

df_display["ವಿಧಾನಸಭಾ ಕ್ಷೇತ್ರ"] = df_year["Constituency"].apply(to_kannada)
if "Category" in df_year.columns:
    df_display["ವರ್ಗ"] = df_year["Category"].apply(to_kannada)

df_display["ವಿಜೇತ ಅಭ್ಯರ್ಥಿ"] = df_year["Winner"].apply(to_kannada)
df_display["ಪಕ್ಷ"] = df_year["Winner_Party"].apply(lambda p: PARTY_KANNADA.get(p, p))

if "Winner_Votes" in df_year.columns:
    df_display["ಪಡೆದ ಮತಗಳು"] = df_year["Winner_Votes"]

if "Vote_Share" in df_year.columns:
    df_display["ಮತಗಳ ಪಾಲು (%)"] = df_year["Vote_Share"]

if "Runner_Up" in df_year.columns:
    df_display["ಸಮೀಪದ ಸ್ಪರ್ಧಿ"] = df_year["Runner_Up"].apply(to_kannada)

if "Runner_Up_Party" in df_year.columns:
    df_display["ಸ್ಪರ್ಧಿ ಪಕ್ಷ"] = df_year["Runner_Up_Party"].apply(lambda p: PARTY_KANNADA.get(p, p))

if "Margin" in df_year.columns:
    df_display["ಅಂತರ"] = df_year["Margin"]

st.dataframe(
    df_display,
    use_container_width=True,
    hide_index=True
)