import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Scenario Simulator", page_icon="🎮", layout="wide")

st.title("🎮 Pollution Scenario Simulator")

# Load trained model
model = joblib.load("models/final_aqi_model.pkl")

# Sliders
no2 = st.slider("NO₂", 0.00000, 0.00050, 0.00020, format="%.5f")

hcho = st.slider("HCHO", 0.00000, 0.00100, 0.00030, format="%.5f")

temp = st.slider("Temperature (°C)", 10.0, 50.0, 30.0)

humidity = st.slider("Humidity (%)", 10.0, 100.0, 60.0)

wind = st.slider("Wind Speed (m/s)", 0.0, 20.0, 4.0)

# Predict
input_df = pd.DataFrame({
    "NO2": [no2],
    "HCHO": [hcho],
    "Temperature": [temp],
    "Humidity": [humidity],
    "WindSpeed": [wind]
})

prediction = model.predict(input_df)[0]

st.metric("Predicted AQI", f"{prediction:.1f}")

# Health advice
if prediction <= 50:
    st.success("🟢 Good Air Quality")
elif prediction <= 100:
    st.info("🟡 Moderate Air Quality")
elif prediction <= 200:
    st.warning("🟠 Poor Air Quality")
elif prediction <= 300:
    st.error("🔴 Very Poor Air Quality")
else:
    st.error("⚫ Severe Air Quality")

st.subheader("💡 What does this mean?")

st.write("""
Move the sliders to simulate changes in environmental conditions.
The AI instantly predicts how the AQI changes based on the new inputs.This will help you understand the impact of various factors on air quality and make informed decisions to improve it. 
""")