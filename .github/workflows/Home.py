import requests
import streamlit as st


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="GISC Flight Suit Outfitter", page_icon= ":rocket:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    _, col2, _ = st.columns([1, 1, 1])
    with col2:
        st.title("Welcome to the Girl in Space Club Outfitter")
        st.subheader("Design Your Dream Flight Suit Here")
        st.write("##" "##")
    
    col1, col2, col3 = st.columns(3)
    with col2 :
        center_button = st.button('Button')
