import streamlit as st

st.set_page_config(page_title="Coupon System", page_icon="🚗")

st.title("In-Vehicle Coupon Recommendation App")
st.write("Start by signing up.")

if st.button("Go to Sign Up"):
    st.switch_page("pages/sign_up.py")
