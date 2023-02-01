import requests
import streamlit as st
from streamlit.components.v1 import html
from pathlib import Path


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
st.set_page_config(page_title="GISC Flight Suit Outfitter", page_icon= ":rocket:", layout="wide", initial_sidebar_state="collapsed")

# Hide streamlit branding
hide_streamlit_style = """
  <style>
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
  </style>
  """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

stripe_checkout = "https://buy.stripe.com/test_eVa16wgok9VUcMMcMM"


# ---- HEADER SECTION ----
with st.container():
    st.title("Your Orders")

left, right = st.columns(2, gap = "large")

with left:
    st.write("##")
    with st.expander("ORDER 1: Riya's Suit"):
        st.write("Size: Custom  \n  Color: Blue  \n  Embroidery: Yes  \n  Patches: Circular, Rectangular")
    st.write("##")
    with st.expander("ORDER 2: Jordyn's Suit"):
        st.write("Size: Standard, XS  \n  Color: Black  \n  Embroidery: No  \n  Patches: Circular, Rectangular")

# Continue to Payment button is disabled until email is entered
with right:
    input= st.text_input("Email", placeholder= "Required")
    email_address = input
    response = requests.get(
        "https://isitarealemail.com/api/email/validate",
        params = {'email': email_address})

    status = response.json()['status']
   
        
    ##email = st.text_input("Email", placeholder= "Required")
    phone = st.text_input("Phone Number", placeholder="Optional")
    ##complete = True
    ##if email:
        ##complete = False
    with open('style.css') as f:
            st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

            ##button only shows up when user puts in email
            if status== "valid:":
                st.markdown(
                f'<a type="click" href={stripe_checkout}>Continue to Payment</a>',
                unsafe_allow_html=True,
                )
            else:
                st.markdown(
                f'<span class="disabled"><a type="click" href={stripe_checkout}>Continue to Payment</a></span>',
                unsafe_allow_html=True,
                )


# ---- CUSTOMIZE ANOTHER SUIT  ----
st.write("##")
if st.button("Customize Another Suit"):
    nav_page("Customization")

# ---- CONTACT ----
st.write("---")
st.subheader("Contact us:")

# Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
        contact_form = """
        <form action="https://formsubmit.co/jnblume2@yahoo.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="word" name="name" placeholder="Your name" required>
            <input type="em" name="email" placeholder="Your email" required>
            <textarea name="mess" placeholder="Your message here" required></textarea>
            <br>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

