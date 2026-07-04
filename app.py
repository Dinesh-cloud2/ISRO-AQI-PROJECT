import folium
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# --------------------------
# PAGE TITLE
# --------------------------
st.set_page_config(page_title="ISRO AQI Predictor", layout="wide")

st.title("🛰️ ISRO AI-Based AQI Prediction System")
st.write("Predict Surface AQI using Satellite Data")

# --------------------------
# LOAD DATA
# --------------------------
df = pd.read_csv("data/satellite_data.csv")

X = df[["NO2", "HCHO", "Temperature"]]
y = df["AQI"]

model = RandomForestRegressor(random_state=42)
model.fit(X, y)

# --------------------------
# CITY SELECTION
# --------------------------
city = st.selectbox("Select City", df["City"])

city_data = df[df["City"] == city]

st.subheader("Satellite Data")

st.write(city_data)

# --------------------------
# PREDICTION
# --------------------------
prediction = model.predict(city_data[["NO2","HCHO","Temperature"]])

st.metric("Predicted AQI", round(prediction[0],2))

# --------------------------
# HEALTH ALERT
# --------------------------
aqi = prediction[0]

if aqi <= 50:
    category = "Good 😊"
    color = "🟢"

elif aqi <= 100:
    category = "Moderate 🙂"
    color = "🟡"

elif aqi <= 200:
    category = "Poor 😷"
    color = "🟠"

elif aqi <= 300:
    category = "Very Poor 🚨"
    color = "🔴"

else:
    category = "Severe ☠️"
    color = "🟣"

st.metric("AQI Category", category)

st.subheader("🏥 Health Advisory")

if aqi <= 50:
    st.success("Air quality is good. Outdoor activities are safe.")

elif aqi <= 100:
    st.info("Sensitive people should reduce prolonged outdoor activity.")

elif aqi <= 200:
    st.warning("Wear a mask if spending long periods outdoors.")

elif aqi <= 300:
    st.error("Avoid outdoor exercise. Children and elderly should stay indoors.")

else:
    st.error("Health emergency. Everyone should avoid unnecessary outdoor exposure.")

st.subheader("📊 Satellite Pollution Levels")

st.bar_chart(city_data[["NO2", "HCHO"]].T)

st.subheader("🗺️ Live Pollution Map")

m = folium.Map(location=[22.5, 80], zoom_start=5)

cities = {
    "Delhi": [28.6139, 77.2090],
    "Mumbai": [19.0760, 72.8777],
    "Bengaluru": [12.9716, 77.5946],
    "Chennai": [13.0827, 80.2707],
    "Kolkata": [22.5726, 88.3639]
}

for city_name, coords in cities.items():
    folium.Marker(
        location=coords,
        popup=city_name,
        tooltip=city_name
    ).add_to(m)

st_folium(m, width=700, height=500)