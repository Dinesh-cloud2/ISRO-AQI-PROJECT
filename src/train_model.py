import pandas as pd
from sklearn.linear_model import LinearRegression

# Read data
df = pd.read_csv("data/aqi_data.csv")

# Features (inputs)
X = df[["Temperature", "PM2.5"]]

# Target (output)
y = df["AQI"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

print("Model trained successfully!")

# Predict AQI


new_data = pd.DataFrame({
    "Temperature": [30],
    "PM2.5": [5]
})

prediction = model.predict(new_data)

print("Predicted AQI:", prediction[0])