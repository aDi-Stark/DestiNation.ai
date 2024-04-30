# Dashboard.py

import streamlit as st
from Home import main as home_main
from InterestModel import main as interest_main
from Personality import main as personality_main
from Domain import main as domain_main
# from Chatbot import main as chatbot_main

def run_dashboard():
    # Define the navigation tabs
    tabs = {
        "Home": "home",
        "Personality Test": "personality_test",
        "Interest Inventory Test": "interest_inventory_test",
        "Domain Mastery Test": "domain_test",
        # "DestiNation Bot": "chatbot"
    }

    # Render the navigation bar
    st.sidebar.title("DestiNation")
    selected_tab = st.sidebar.radio("", list(tabs.keys()))

    if selected_tab == "Home":
        home_main()
        
    elif selected_tab == "Interest Inventory Test":
        interest_main()

    elif selected_tab == "Personality Test":
        personality_main()

    elif selected_tab == "Domain Mastery Test":
        domain_main()

    # elif selected_tab == "DestiNation Bot":
    #     chatbot_main()