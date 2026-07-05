import streamlit as st
import pandas as pd
import joblib
import shap
import plotly.express as px

st.set_page_config(page_title="AI Insights", layout="wide")

st.title("🧠 Explainable AI Dashboard")

# Load model
model = joblib.load("models/final_aqi_model.pkl")

# Load dataset
df = pd.read_csv("data/final_dataset/daily_satellite_dataset.csv")
df = df.dropna()

X = df[["NO2", "HCHO", "Temperature", "Humidity", "WindSpeed"]]

# SHAP Explainer
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# Feature Importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": abs(shap_values).mean(axis=0)
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

st.subheader("📊 Feature Importance")

fig = px.bar(
    importance,
    x="Importance",
    y="Feature",
    orientation="h",
    title="AI Feature Importance"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("💡 AI Interpretation")

top = importance.iloc[0]["Feature"]

st.success(f"The AI model considers **{top}** to be the most influential feature for AQI prediction.")