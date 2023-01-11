import requests
import streamlit as st


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="GISC Flight Suit Outfitter", page_icon= ":rocket:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        st.title("Welcome to the Girl in Space Club Outfitter")
        st.subheader("Design Your Dream Flight Suit Here")
        st.write("##" "##")
    
        st.markdown("<button type='button;' style='text-align: center;'>Click Me!</button>", unsafe_allow_html=True)

