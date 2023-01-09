import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="GISC Flight Suit Outfitter", page_icon= ":rocket:", layout="wide")


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


# ---- HEADER SECTION ----
with st.container():
    st.title("Create a New Account")
    st.subheader("Enter your information:")

# ---- CUSTOMER INFO ----
with st.form("new_account"):
    ##Print customer info questions
    st.write("What is your name?")
    st.text_input()
    st.write("What is your email?")
    st.text_input()
    st.write("For what purpose are you purchasing this suit?")
    st.text_input()
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
    st.text_input()
    st.write("Re-enter your password")
    st.text_input()
    st.form_submit_button("Create New Account")