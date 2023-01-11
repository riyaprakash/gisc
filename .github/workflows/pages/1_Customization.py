import requests
import streamlit as st
from PIL import Image
from streamlit.components.v1 import html

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)


image = Image.open('suit.jpg')

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="GISC Flight Suit Outfitter", page_icon= ":rocket:", layout="wide")

st.title("Flight Suit Customization")
st.write("---")

leftcol, rightcol = st.columns([5,4]);

with leftcol:
    st.write("##")
    st.image(image)
with rightcol:
    # ---- SIZING PREFERENCE ----
    tab1, tab2, tab3 = st.tabs(["Sizing", "Suit Color", "Patches"])
    with tab1:
        ##create 2 columns
        with st.container():
            ##Print size questions 
            st.header("Sizing Preference")
            st.write("##")

            choice = st.selectbox("Do you want to purchase a space suit with custom measurements or with standard sizing?",
            ["-", "Custom", "Standard"])
            
            if 'Custom' in choice:
                with st.form("custom"):
                    ##If user chooses custom measurements
                    st.selectbox("What is your preferred unit of measurement?",("cm", "in"))

                    ##If user chooses cm then convert the answers to inches

                    st.number_input("Enter Height")
                    st.number_input("Enter Chest")
                    st.number_input("Enter Waist")
                    st.number_input("Enter Total Arm Length")
                    st.number_input("Enter Inseam")
                    st.number_input("Enter Body Length")
                    st.form_submit_button("Save")

            if 'Standard' in choice:
                with st.form("standard"):
                    ##If user chooses standard sizing
                    st.selectbox("Which size suit do you want to purchase?",("XXS", "XS", "S", "M", "L", "XL"))
                    st.form_submit_button("Save")
                



    # ---- SUIT COLOR ----
    with tab2:
        st.write("---")
        colors = st.form("color")
        with colors:
            ##Print color questions
            st.header("Suit Color")
            st.write("##")
            st.selectbox("What color do you want your suit to be?", ("Red", "Yellow", "Blue"))
            st.write("##")
            colors.form_submit_button("Save")

    # ---- PATCHES ----
    with tab3:
        st.write("---")
        patches = st.form("patches")
        with patches:
            ##Print color questions
            st.header("Patches")
            st.write("##")
            st.selectbox("Would you like the Girl in Space Club Embroidery on the back?", ("Yes", "No"))
            st.write("We are currently unable to provide custom patches. However, if you would like to get your own, you have the option of including three blank patch spaces for the following dimensions:")
            st.checkbox("2 circular patches (diameter 3.75': right chest, left arm")
            st.checkbox("1 rectangular patch (2 x 4): left chest")
            patches.form_submit_button("Save")
    # ---- FINISH ORDERING ----
    st.write("---")
    if st.button("Finish Ordering Suit"):
        nav_page("Cart")