import pandas as pd

df = pd.read_csv("data/aqi_data.csv")

print("Ground AQI")
print(df)

# Simulated satellite AQI
df["Satellite_AQI"] = df["AQI"] + [5, -8, 10, -3, 6]

print("\nComparison")
print(df[["City", "AQI", "Satellite_AQI"]])

df["Difference"] = df["Satellite_AQI"] - df["AQI"]

print("\nDifference")
print(df[["City", "Difference"]])