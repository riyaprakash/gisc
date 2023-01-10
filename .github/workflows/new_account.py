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
    st.write(
        """
        -At least 8 characters
        -One Uppercase
        -One Lowercase
        -One Number
        -One Special Character
        """
    )
    st.text_input("")
    st.text_input("Re-enter yout password")
    st.form_submit_button("Create New Account")