import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analytics", layout="wide")

st.title("📊 Air Quality Analytics")

# Load dataset
df = pd.read_csv("data/final_dataset/daily_satellite_dataset.csv")

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# City selector
city = st.selectbox("Select City", sorted(df["City"].unique()))

city_df = df[df["City"] == city]

# AQI Trend
fig1 = px.line(
    city_df,
    x="Date",
    y="AQI",
    title=f"{city} AQI Trend",
    markers=True
)

st.plotly_chart(fig1, use_container_width=True)

# NO2 Trend
fig2 = px.line(
    city_df,
    x="Date",
    y="NO2",
    title="NO₂ Trend",
    markers=True
)

st.plotly_chart(fig2, use_container_width=True)

# Temperature Trend
fig3 = px.line(
    city_df,
    x="Date",
    y="Temperature",
    title="Temperature Trend",
    markers=True
)

st.plotly_chart(fig3, use_container_width=True)

# Correlation Heatmap
corr = city_df[["AQI","NO2","HCHO","Temperature","Humidity","WindSpeed"]].corr()

fig4 = px.imshow(
    corr,
    text_auto=True,
    title="Feature Correlation"
)

st.plotly_chart(fig4, use_container_width=True)