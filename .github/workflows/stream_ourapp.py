import requests
import streamlit as st


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="GISC Flight Suit Outfitter", page_icon= ":rocket:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.title("Welcome to the Girl in Space Club Outfitter")
    st.subheader("Enter your information below and continue to sizing to design your flight suit")

# ---- CUSTOMER INFO ----
with st.container():
    st.write("---")
    ##create 2 columns
    left_column, right_column = st.columns(2)
    with left_column:
        ##Print customer info questions
        st.header("Customer Info")
        st.write("What is your name?")
        st.text_input()
        st.write("What is your email?")
        st.text_input()
        st.write("For what purpose are you purchasing this suit?")
        st.text_input()
    

# ---- SIZING PREFERENCE ----
with st.container():
    st.write("---")
    ##create 2 columns
    left_column, right_column = st.columns(2)
    with left_column:
        ##Print size questions 
        st.header("Sizing Preference")
        st.write("##")

        st.write("Do you want to purchase a space suit with custom measurements or with standard sizing?")
        st.write("Custom     Standard")
        
        ##If user chooses custom measurements
        st.write("What is your preferred unit of measurement?")
        st.write("cm     in")

        ##If user chooses cm then convert the answers to inches

        st.write("Enter height")
        st.text_input()
        st.write("Enter chest")
        st.text_input()
        st.write("Enter waist")
        st.text_input()
        st.write("Enter hips/seat")
        st.text_input()
        st.write("Enter total arm length")
        st.text_input()
        st.write("Enter inseam")
        st.text_input()
        st.write("Enter body length")
        st.text_input()

        ##If user chooses standard sizing
        st.write("Which size suit do you want to purchase?")
        st.write("XXS  XS  S  M  L  XL")



# ---- SUIT COLOR ----
with st.container():
    st.write("---")
    ##create 2 columns
    left_column, right_column = st.columns(2)
    with left_column:
        ##Print color questions
        st.header("Suit Color")
        st.write("##")
        st.selectbox("What color do you want your suit to be?", (Red, Yellow, Blue))

# ---- PATCHES ----
with st.container():
    st.write("---")
    ##create 2 columns
    left_column, right_column = st.columns(2)
    with left_column:
        ##Print color questions
        st.header("Patches")
        st.write("##")
        st.write("Would you like the Girl in Space Club Embroidery on the back?")
        st.button("Yes")
        st.button("No")
        st.write("We are currently unable to provide custom patches. However, if you would like to get your own, you have the option of including three blank patch spaces for the following dimensions:")
        st.write("2 circular patches (diameter 3.75': right chest, left arm")
        st.write("1 rectangular patch (2 x 4): left chest")


# ---- FINISH ORDERING ----
with st.container():
    st.write("---")
    ##create 2 columns
    left_column, right_column = st.columns(2)
    with left_column:
        ##Show finish ordering button
        st.button("Finish Ordering Suit")
        st.write("Thank you for designing a Girl in Space Club flight suit!")