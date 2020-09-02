#===============================================================================
import streamlit as st
from screens import *

#===============================================================================

PAGE_CONFIG = {"page_title":"QG_QA_demo.io","page_icon":":shark:","layout":"centered"}
st.beta_set_page_config(**PAGE_CONFIG)

# App start: 
def main():
    menu = ["About", "Question Answering", "Question Generation"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    #===========================================================================
    # Main Page: 
    if choice == "About":
        main_screen()

    #===========================================================================
    # QA Page: 
    if choice == "Question Answering": 
        QA_screen()

    #===========================================================================
    # QG Page: 
    if choice == "Question Generation":
        QG_screen()


if __name__ == '__main__':
    main()