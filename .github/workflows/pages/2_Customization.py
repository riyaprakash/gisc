import requests
import streamlit as st
import csv
import pandas as pd
from csv import writer
from PIL import Image
from streamlit.components.v1 import html
##from streamlit_extras.switch_page_button import switch_page
from streamlit.source_util import get_pages

def nav_page(page_name, timeout_secs=3):
     #links is the array, window is the page you are currently on, accessing the parent file of the customization page(pages folder) 
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parents.document.getElementsByTagName("a");
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

def balloons():
    st.balloons()

def switch_page(page_name: str):
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")

    page_name = standardize_name(page_name)

    pages = get_pages("streamlit_app.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")
    
image = Image.open('flightsuit.jpg')

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


st.title("Flight Suit Customization")
st.write("---")

leftcol,rightcol = st.columns([8,7], gap="large");


##filepath = f"Orders.csv"
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
            size_chart=pd.read_csv('Sizing_Chart.csv')
            with st.expander("Size Chart"):
                st.write(size_chart.head(7))

            choice = st.selectbox("Do you want to purchase a space suit with custom measurements or with standard sizing?", ["-", "Custom", "Standard"])
            if 'Custom' in choice:
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
                    
                    if st.form_submit_button("Save"):
                        st.write(pd.DataFrame({
                        'first column': [1, 2, 3, 4],
                        'second column': [10, 20, 30, 40],
                        }))
                        ##file= "Orders1.csv"
                        ##headerList = ['col1', 'col2', 'col3', 'col4']
  
                        # open CSV file and assign header
                        ##with open("Orders.csv", 'w') as file:
                            ##dw = csv.DictWriter(file, delimiter=',', 
                                                ##fieldnames=headerList)
                            ##dw.writeheader()
                        # display csv file
                        ##fileContent = pd.read_csv("Orders.csv")
                        ##fileContent
                        ##dff = pd.read_csv("Orders1.csv")
                        ##st.write(dff)

                        ##df=df.append(new_data, ignore_index = True)
                        ##open('Orders.csv', 'w').write(df.to_csv())
                        ##fake_data = [{'Unit': 'cm', 'Height' : '1', 'Chest': '2', 'Waist': '3', 'Total Arm Length': '4', 'Inseam': '5', 'Body Length': '6'},
                        ##{'Unit': 'in', 'Height': '11', 'Chest': '22', 'Waist': '33', 'Total Arm Length': '44', 'Inseam': '55', 'Body Length': '66'}]
                        rows = [ ['Nikhil', 'COE', '2', '9.0'], 
                        ['Sanchit', 'COE', '2', '9.1'], 
                        ['Aditya', 'IT', '2', '9.3'], 
                        ['Sagar', 'SE', '1', '9.5'], 
                        ['Prateek', 'MCE', '3', '7.8'], 
                        ['Sahil', 'EP', '2', '9.1']] 
                        ##custom = {'Unit': [add_col1], 'Height': [add_col2], 'Chest': [add_col3], 'Waist': [add_col4], 'Total Arm Length': [add_col5], 'Inseam': [add_col6], 'Body Length': [add_col7]}
                       ##fields = ['Unit', 'Height', 'Chest', 'Waist', 'Total Arm Length', 'Inseam', 'Body Length']
                        ##with open('Orders.csv', 'w', newline='') as file: 
                            ##w = csv.writer(file)

                            ##w.writeheader() 

                            ##w.writerows(rows)
                            ##file.close()

                        f = open("Orders.csv", "wb")
                        w = csv.writer(f)
                        w.writerows(rows)
                        f.close()
                        ##table=st.dataframe()
                        ##df=pd.DataFrame(header)
                        ##st.write("Hello")

            if 'Standard' in choice:
                with st.form("standard"):
                    ##If user chooses standard sizing
                    add_col1 = st.selectbox("Which size suit do you want to purchase?",("XXS", "XS", "S", "M", "L", "XL"))
                    st.form_submit_button("Save")

                    new_data = {'col1': add_col1}

                    
                



    # ---- SUIT COLOR ----
    with tab2:
        st.write("---")
        colors = st.form("color")
        with colors:
            ##Print color questions
            st.header("Suit Color")
            st.write("##")
            st.selectbox("What color do you want your suit to be?", ("Black", "Blue"))
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
             #display balloons on button click
            patches.form_submit_button("Save", on_click= balloons)
 
 
    # ---- FINISH ORDERING ----
    st.text_input(" ", placeholder="Name your Order")
    addtocart = st.button("Add to Cart", disabled = True)

    
    # ---- VIEW CART ----
    st.write("---")
    if st.button("View Cart"):
        switch_page("Cart")

    # ---- BACK TO HOME ----
    if st.button("Return to home"):
        switch_page("Home")




#####################



#""" Data Source   """
#web location for csv file, 'df.csv'
data_src = r'https://raw.githubusercontent.com/clueple/free_resources/master/df.csv'
# data_src = r'https://github.com/clueple/free_resources/blob/master/df.csv'

#web location for csv file, 'dfc.csv'
data_src1 = r'https://raw.githubusercontent.com/clueple/free_resources/master/dfc.csv'
# data_src1 = r'https://github.com/clueple/free_resources/blob/master/dfc.csv'


#""" test folder  """
file_dir = r'd:/Downloads'
file_name = 'df1.csv'

filepath = f"{file_dir}/{file_name}"

