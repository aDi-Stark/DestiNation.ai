# app.py

import streamlit as st

# Initialize session state for user authentication
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Initialize user database
if 'user_database' not in st.session_state:
    st.session_state['user_database'] = {
        "user1": "password1",
        "user2": "password2",
        "Aditya": "Aditya1"
    }

def main_page():
    if st.session_state['authenticated']:
        from Dashboard import run_dashboard
        run_dashboard()
    else:
        st.error("You are not logged in. Please log in to continue.")
        login_page()

def login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user_database = st.session_state['user_database']
        if username in user_database and user_database[username] == password:
            st.session_state['authenticated'] = True
            st.experimental_rerun()  # Rerun the app, which will now enter the dashboard due to the updated session state
        else:
            st.error("Invalid username or password")

def logout():
    if st.button("Logout"):
        st.session_state['authenticated'] = False
        st.experimental_rerun()

def signup_page():
    st.title("Sign Up")

    new_username = st.text_input("Choose a Username", key="new_user")
    new_password = st.text_input("Choose a Password", type="password", key="new_pass")

    if st.button("Sign Up"):
        user_database = st.session_state['user_database']
        if new_username in user_database:
            st.error("User already exists")
        else:
            user_database[new_username] = new_password
            st.session_state['user_database'] = user_database  # Update user database in session state
            st.success("User created successfully. Please login.")

def app_router():
    st.sidebar.title("Navigation")
    if st.session_state['authenticated']:
        logout()
        main_page()  # Directly go to the dashboard if authenticated
    else:
        page = st.sidebar.radio("Go to", ["Login", "Sign Up"])
        if page == "Login":
            login_page()
        elif page == "Sign Up":
            signup_page()

app_router()
