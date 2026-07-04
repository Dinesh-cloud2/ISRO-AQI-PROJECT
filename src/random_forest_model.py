import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv("data/satellite_data.csv")

# Features
X = df[["NO2", "HCHO", "Temperature"]]

# Target
y = df["AQI"]

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

print("✅ Random Forest Model Trained Successfully!")

# Predict
sample = pd.DataFrame({
    "NO2": [0.00018],
    "HCHO": [0.00020],
    "Temperature": [25]
})

prediction = model.predict(sample)

print("Predicted AQI:", prediction[0])

# Check training error
train_prediction = model.predict(X)
mae = mean_absolute_error(y, train_prediction)

print("Training MAE:", mae)