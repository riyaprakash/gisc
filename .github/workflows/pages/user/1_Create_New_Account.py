import requests
import streamlit as st

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="GISC Flight Suit Outfitter", page_icon= ":rocket:", layout="wide")


# ---- HEADER SECTION ----
with st.container():
    st.title("Create a New Account")
    st.subheader("Enter your information:")

# ---- CUSTOMER INFO ----
with st.form("new_account"):
    ##Print customer info questions
    st.text_input("What is your name?")
    st.text_input("What is your email?")
    st.text_input("What purpose are you purchasing this suit?")
    st.write("Enter your password")
    st.caption(
        """
        -At least 8 characters \n
        -One Uppercase \n
        -One Lowercase \n
        -One Number \n
        -One Special Character """)
    st.text_input("")
    st.text_input("Re-enter your password")
    st.form_submit_button("Create New Account")