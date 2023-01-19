import requests
import streamlit as st

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


# ---- HEADER SECTION ----
with st.container():
    st.title("Your Orders")

st.write("##")
st.write("ORDER 1 DETAILS")
st.write("##")
st.write("ORDER 2 DETAILS")
st.write("##")
st.write("ORDER 3 DETAILS")

# ---- CUSTOMIZE ANOTHER SUIT  ----
st.write("---")
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
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

