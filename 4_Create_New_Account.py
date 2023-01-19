import requests
import streamlit as st
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
    if st.form_submit_button("Create New Account"):
        nav_page("Login")