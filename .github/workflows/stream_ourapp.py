import requests
import streamlit as st


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="GISC Flight Suit Outfitter", page_icon= ":rocket:", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.title("Welcome to the Girl in Space Club Outfitter")
    st.subheader("Enter your information below and continue to sizing to design your flight suit")

# ---- SIZING PREFERENCE ----
with st.container():
    st.write("---")
    ##create 2 columns
    with st.form("size"):
        ##Print size questions 
        st.header("Sizing Preference")
        st.write("##")

        st.selectbox("Do you want to purchase a space suit with custom measurements or with standard sizing?",
        ("Custom", "Standard"))
        
        ##If user chooses custom measurements
        st.selectbox("What is your preferred unit of measurement?",("cm", "in"))

        ##If user chooses cm then convert the answers to inches

        st.text_input("Enter Height")
        st.text_input("Enter Chest")
        st.text_input("Enter Waist")
        st.text_input("Enter waist")
        st.text_input("Enter Total Arm Length")
        st.text_input("Enter Inseam")
        st.text_input("Enter Body Length")

        ##If user chooses standard sizing
        st.selectbox("Which size suit do you want to purchase?",("XXS", "XS", "S", "M", "L", "XL"))
        st.form_submit_button()



# ---- SUIT COLOR ----
with st.container():
    st.write("---")
    with st.form("color"):
        ##Print color questions
        st.header("Suit Color")
        st.write("##")
        st.selectbox("What color do you want your suit to be?", (Red, Yellow, Blue))
        st.form_submit_button()

# ---- PATCHES ----
with st.container():
    st.write("---")
    with st.form("patches"):
        ##Print color questions
        st.header("Patches")
        st.write("##")
        st.write("Would you like the Girl in Space Club Embroidery on the back?")
        st.button("Yes")
        st.button("No")
        st.write("We are currently unable to provide custom patches. However, if you would like to get your own, you have the option of including three blank patch spaces for the following dimensions:")
        st.checkbox("2 circular patches (diameter 3.75': right chest, left arm")
        st.checkbox("1 rectangular patch (2 x 4): left chest")
        st.form_submit_button()


# ---- FINISH ORDERING ----
with st.container():
    st.write("---")
    ##create 2 columns
    left_column, right_column = st.columns(2)
    with left_column:
        ##Show finish ordering button
        st.button("Finish Ordering Suit")
        st.write("Thank you for designing a Girl in Space Club flight suit!")
