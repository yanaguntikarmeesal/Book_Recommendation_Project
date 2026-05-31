

import streamlit as st
import pickle
import pandas as pd

# Page configuration
st.set_page_config(page_title="Book Recommender", layout="wide")

# Load data
@st.cache_data
def load_data():
    return pickle.load(open('popular.pkl', 'rb'))

popular_df = load_data()

# --- Advanced CSS for UI Customization ---
st.markdown("""
    <style>
    /* 1. BOLD TABS */
    button[data-baseweb="tab"] p {
        font-size: 18px !important;
        font-weight: bold !important;
        color: #1e293b !important;
    }

    /* 2. CENTERED RECOMMEND BUTTON */
    .stButton {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    /* 3. RECOMMEND BUTTON CSS */
    .stButton > button {
        background-color: #4F46E5 !important;
        color: white !important;
        border-radius: 20px !important;
        padding: 10px 30px !important;
        border: none !important;
        font-weight: bold !important;
        transition: 0.3s;
    }

    /* 4. SMALLER OUTPUT BOXES */
    .rec-card {
        background-color: white;
        padding: 10px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        text-align: center;
        width: 100%;
        margin: auto;
    }
    .rec-img {
        width: 100%;
        height: 160px;
        object-fit: contain;
        border-radius: 4px;
    }

    /* 5. CUSTOM FOOTER CSS */
    .footer {
        position: relative;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: #64748b;
        text-align: center;
        padding: 20px;
        font-family: 'Trebuchet MS', sans-serif;
        font-size: 14px;
        font-weight: bold;
        border-top: 1px solid #e2e8f0;
        margin-top: 50px;
        letter-spacing: 1px;
    }
    .footer span {
        color: #ef4444; /* Red heart color */
    }

    /* Home Card Styling */
    .book-card {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>📖 Book Hub</h1>", unsafe_allow_html=True)
tab1, tab2 = st.tabs(["🏠 Home", "🔍 Recommend"])

# --- TAB 1: HOME ---
with tab1:
    st.markdown("### Top Trending Books")
    cols_per_row = 5
    for i in range(0, 50, cols_per_row):
        cols = st.columns(cols_per_row)
        batch = popular_df.iloc[i : i + cols_per_row]
        for col, (index, row) in zip(cols, batch.iterrows()):
            with col:
                st.markdown(f"""
                    <div class="book-card">
                        <img src="{row['Image-URL-M']}" style="width:100%; border-radius:8px;">
                        <div style="font-weight:bold; margin-top:10px; font-size:14px;">{row['Book-Title']}</div>
                        <div style="color:gray; font-size:11px;">{row['Book-Author']}</div>
                    </div>
                    """, unsafe_allow_html=True)

# --- TAB 2: RECOMMEND ---
with tab2:
    st.markdown("<h3 style='text-align: center;'>Find Your Next Read</h3>", unsafe_allow_html=True)
    book_list = popular_df['Book-Title'].unique()
    selected_book = st.selectbox("Search Book", book_list, index=None, label_visibility="collapsed")

    if st.button("Get Recommendations"):
        if selected_book:
            st.markdown(f"<p style='text-align:center;'>Top picks for fans of <b>{selected_book}</b></p>", unsafe_allow_html=True)
            res_cols = st.columns(6)
            sample_results = popular_df.sample(6)
            for col, (idx, row) in zip(res_cols, sample_results.iterrows()):
                with col:
                    st.markdown(f"""
                        <div class="rec-card">
                            <img src="{row['Image-URL-M']}" class="rec-img">
                            <div style="font-size:11px; font-weight:bold; margin-top:5px; height:30px; overflow:hidden;">{row['Book-Title']}</div>
                        </div>
                        """, unsafe_allow_html=True)
        else:
            st.warning("Please select a book first!")

# --- BEAUTIFUL CUSTOM FOOTER ---
st.markdown("""
    <div class="footer">
        Designed & Developed with <span>❤</span> by Yanaguntikar Meesal
    </div>
    """, unsafe_allow_html=True)

