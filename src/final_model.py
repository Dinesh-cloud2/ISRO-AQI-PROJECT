import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib

# Load dataset
df = pd.read_csv("data/final_dataset/daily_satellite_dataset.csv")

# Remove missing values
df = df.dropna()

# Features
X = df[["NO2", "HCHO", "Temperature", "Humidity", "WindSpeed"]]

# Target
y = df["AQI"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
pred = model.predict(X_test)

# Accuracy
mae = mean_absolute_error(y_test, pred)

print("Training completed!")
print("Mean Absolute Error:", round(mae, 2))

# Save model
joblib.dump(model, "models/final_aqi_model.pkl")

print("Model saved successfully!")