import streamlit as st
from datetime import datetime

st.title("Sign Up Page")

# Session state setup
if "signed_up" not in st.session_state:
    st.session_state.signed_up = False

if "go_to_book" not in st.session_state:
    st.session_state.go_to_book = False

# Handle sign up
if not st.session_state.signed_up:
    with st.form("signup_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=16, max_value=100)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        occupation = st.text_input("Occupation")
        submitted = st.form_submit_button("Sign Up")

    if submitted:
        st.session_state.user_info = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "name": name,
            "age": age,
            "gender": gender,
            "occupation": occupation
        }
        st.session_state.signed_up = True
        st.session_state.go_to_book = True
        st.rerun()  # Correct rerun method
else:
    # Redirect if sign up just happened
    if st.session_state.go_to_book:
        st.session_state.go_to_book = False
        st.switch_page("pages/book_ride.py")

    # Otherwise show message
    st.info("You’re already signed up. Use the sidebar to book a ride.")
