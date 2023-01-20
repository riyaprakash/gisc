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
    st.title("Welcome to the Girl in Space Club Outfitter")
    st.subheader("Enter your login information:")

# ---- CUSTOMER INFO ----
with st.form("login"):
    st.text_input("Username")
    st.text_input("Password")
    if st.form_submit_button("Login"):
        nav_page("Customization")
    if st.form_submit_button("Create New Account"):
        nav_page("Create_New_Account")

#when the user logs add, add their email and name to the csv file before they place an order


    with st.form("custom", clear_on_submit=True):

                    ##If user chooses custom measurements
                    add_col1 = st.selectbox('What is your preferred unit of measurement?',('cm', 'in'))

                    ##If user chooses cm then convert the answers to inches
                    ##add min and max values!!!
                    add_col2 = st.number_input('Enter Height',0,500)
                    add_col3 = st.number_input('Enter Chest',0,500)
                    add_col4 = st.number_input('Enter Waist',0,500)
                    add_col5 = st.number_input('Enter Total Arm Length',0,500)
                    add_col6 = st.number_input('Enter Inseam',0,500)
                    add_col7 = st.number_input('Enter Body Length',0,500)
                    custom_measure=st.form_submit_button("Save")
                    
                    new_data = {'What is your preferred unit of measurement?':[add_col1], 'Enter Height': [add_col2], 'Enter Chest': [add_col3], 
                        'Enter Waist': [add_col4], 'Enter Total Arm Length': [add_col5], 'Enter Inseam': [add_col6], 'Enter Body Length': [add_col7]}
                    
                    if custom_measure == True:
                        df = pd.read_csv("Orders.csv")

                        df=df.append(new_data, ignore_index = True)
                        open('Orders.csv', 'w').write(df.to_csv())