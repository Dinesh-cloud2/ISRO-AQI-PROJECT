import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", page_icon="🛰️", layout="wide")

st.title("🛰️ ISRO AI Surface AQI Intelligence Platform")

# Load dataset
df = pd.read_csv("data/final_dataset/daily_satellite_dataset.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Sidebar
st.sidebar.header("Controls")

city = st.sidebar.selectbox(
    "Select City",
    sorted(df["City"].unique())
)

city_df = df[df["City"] == city]
latest = city_df.iloc[-1]

# Top Metrics
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("AQI", round(latest["AQI"], 1))
col2.metric("NO₂", round(latest["NO2"], 6))
col3.metric("HCHO", round(latest["HCHO"], 6))
col4.metric("Temperature", f'{latest["Temperature"]:.1f} °C')
col5.metric("Humidity", f'{latest["Humidity"]:.1f}%')

st.divider()

# AQI Trend
fig = px.line(
    city_df,
    x="Date",
    y="AQI",
    title=f"{city} AQI Trend",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# Health Advisory
aqi = latest["AQI"]

st.subheader("🏥 Health Advisory")

if aqi <= 50:
    st.success("🟢 Good Air Quality")
elif aqi <= 100:
    st.info("🟡 Moderate Air Quality")
elif aqi <= 200:
    st.warning("🟠 Poor Air Quality. Sensitive groups should reduce outdoor activity.")
elif aqi <= 300:
    st.error("🔴 Very Poor Air Quality. Wear an N95 mask.")
else:
    st.error("⚫ Severe Air Quality. Stay indoors if possible.")

st.divider()

# AI Summary
st.subheader("🧠 AI Summary")

st.write(f"""
The AI predicts an AQI of **{aqi:.1f}** for **{city}**.

This prediction is based on:

- 🛰️ NO₂ concentration
- 🛰️ HCHO concentration
- 🌡️ Temperature
- 💧 Humidity
- 🌬️ Wind Speed
""")