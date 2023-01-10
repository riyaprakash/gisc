import requests
import streamlit as st


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="GISC Flight Suit Outfitter", page_icon= ":rocket:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.title("Welcome to the Girl in Space Club Outfitter")
    st.subheader("CUSTOM PAGE")

# ---- CUSTOMER INFO ----
with st.form("login"):
    st.text_input("Username")
    st.text_input("Password")
    st.form_submit_button("Login")
    st.form_submit_button("Create New Account")