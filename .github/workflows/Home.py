import requests
import streamlit as st


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="GISC Flight Suit Outfitter", page_icon= ":rocket:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.title("Welcome to the Girl in Space Club Outfitter")
    st.subheader("Design Your Dream Flight Suit Here")
    st.write("##" "##")
    left_column, right_column = st.columns(2)
    with left_column:
        st.button("Create New Suit")
    with right_column:
        st.button("View Cart")

