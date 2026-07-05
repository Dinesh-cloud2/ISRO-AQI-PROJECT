import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Live AQI Map", page_icon="🗺️", layout="wide")

st.title("🗺️ Live AQI Map")

# Load Dataset
df = pd.read_csv("data/final_dataset/daily_satellite_dataset.csv")

# Coordinates (expand later)
city_locations = {
    "Delhi": [28.6139, 77.2090],
    "Mumbai": [19.0760, 72.8777],
    "Bengaluru": [12.9716, 77.5946],
    "Chennai": [13.0827, 80.2707],
    "Kolkata": [22.5726, 88.3639]
}

# Create Map
m = folium.Map(
    location=[22.5, 78.9],
    zoom_start=5,
    tiles="CartoDB Positron"
)

latest = df.groupby("City").last().reset_index()

for _, row in latest.iterrows():

    city = row["City"]

    if city in city_locations:

        lat, lon = city_locations[city]

        aqi = float(row["AQI"])

        if aqi <= 50:
            color = "green"
        elif aqi <= 100:
            color = "blue"
        elif aqi <= 200:
            color = "orange"
        elif aqi <= 300:
            color = "red"
        else:
            color = "darkred"

        popup = f"""
        <b>{city}</b><br>
        AQI : {aqi:.1f}<br>
        NO₂ : {row['NO2']}<br>
        HCHO : {row['HCHO']}<br>
        Temp : {row['Temperature']} °C<br>
        Humidity : {row['Humidity']} %
        """

        folium.CircleMarker(
            location=[lat, lon],
            radius=12,
            popup=popup,
            tooltip=city,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.8
        ).add_to(m)

st_folium(m, width=1200, height=650)