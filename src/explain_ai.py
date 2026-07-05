import pandas as pd
import joblib
import shap

# Load model
model = joblib.load("models/final_aqi_model.pkl")

# Load dataset
df = pd.read_csv("data/final_dataset/daily_satellite_dataset.csv")

X = df[["NO2", "HCHO", "Temperature", "Humidity", "WindSpeed"]]

# Create SHAP explainer
explainer = shap.TreeExplainer(model)

# Calculate SHAP values
shap_values = explainer.shap_values(X)

# Feature importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": abs(shap_values).mean(axis=0)
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance)