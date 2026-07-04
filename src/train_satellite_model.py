import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("data/satellite_data.csv")

# Features
X = df[["NO2", "HCHO", "Temperature"]]

# Target
y = df["AQI"]

# Train model
model = LinearRegression()
model.fit(X, y)

print("Model trained successfully!")

# Example prediction
sample = pd.DataFrame({
    "NO2": [0.00018],
    "HCHO": [0.00020],
    "Temperature": [25]
})

prediction = model.predict(sample)

print("Predicted AQI:", prediction[0])