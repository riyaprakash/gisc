import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="GISC Flight Suit Outfitter", page_icon= ":rocket:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# Imports PIL module 
from PIL import Image
  
# open method used to open different extension image file
sizechart = Image.open("C:\Users\System-Pc\Desktop\Website-size-chart.png") 
  
# This method will show sizechart in any image viewer 
sizechart.show()


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
        st.write("##")
        st.write("What is your name?")
        st.write("What is your email?")
        st.write("For what purpose are you purchasing this suit?")
    with right_column:
        ##can add an image here
        ##st_lottie(lottie_coding, height=300, key="coding"

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
        st.write("Enter chest")
        st.write("Enter waist")
        st.write("Enter hips/seat")
        st.write("Enter total arm length")
        st.write("Enter inseam")
        st.write("Enter body length")

        ##If user chooses standard sizing
        st.write("Which size suit do you want to purchase?")
        st.write("XXS  XS  S  M  L  XL")

    with right_column:
        ##can add an image here
        ##add size chart
        ##add measurement images
        ##st_lottie(lottie_coding, height=300, key="coding")


# ---- SUIT COLOR ----
with st.container():
    st.write("---")
    ##create 2 columns
    left_column, right_column = st.columns(2)
    with left_column:
        ##Print color questions
        st.header("Suit Color")
        st.write("##")
        st.write("What color do you want your suit to be?")
    with right_column:


# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


