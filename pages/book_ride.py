import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import joblib
import os

# Load model and preprocessor ONCE (can be done at top)
model = joblib.load('models/coupon_model.pkl')
preprocessor = joblib.load('models/preprocessor.pkl')



def get_weather(city_name, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "weather": data['weather'][0]['description'],
            "temperature": data['main']['temp'],
            "humidity": data['main']['humidity'],
            "wind_speed": data['wind']['speed']
        }
    else:
        return None

st.title("Book a Ride")

if "signed_up" not in st.session_state or not st.session_state.signed_up:
    st.warning("Please sign up first from the 'Sign Up' page.")
else:
    user = st.session_state.user_info
    st.subheader(f"Welcome, {user['name']}!")

    with st.form("ride_form"):
        destination = st.text_input("Destination (City)")
        time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
        book = st.form_submit_button("Book Ride")

    if book:
        api_key = "986e581547467814f882c97bec81f189"
        weather = get_weather(destination, api_key)

        if weather:
            full_data = {
                **user,
                "destination": destination,
                "time_of_day": time_of_day,
                **weather
            }


            # Save raw data

            df = pd.DataFrame([full_data])
            try:
                existing = pd.read_csv("user_data.csv")
                df = pd.concat([existing, df], ignore_index=True)
            except FileNotFoundError:
                pass
            df.to_csv("user_data.csv", index=False)

            # Prepare only features model needs (adjust as per training dataset)
            input_features = pd.DataFrame([{
                "weather": weather["weather"],
                "destination": destination,
                "age": user["age"],
                "gender": user["gender"],
                "time": time_of_day,
            }])

            # Preprocess
            processed = preprocessor.transform(input_features)

            # Predict
            prediction = model.predict(processed)[0]

            # Show prediction
            coupon_map = {
                "Bar": "Free Drink at the Bar!",
                "Carry out & Take away": "25% off on takeout!",
                "Coffee House": "Get a Free Coffee!",
                "Restaurant(20-50)": "Save up to 50% at a Restaurant!",
                "Restaurant(<20)": "Enjoy a Budget Meal!"
            }

            st.success("Ride booked successfully!")
            st.info(f"Recommended Coupon: {coupon_map.get(prediction, prediction)}")
            st.dataframe(df.tail(1))
        else:
            st.error("Could not fetch weather data.")