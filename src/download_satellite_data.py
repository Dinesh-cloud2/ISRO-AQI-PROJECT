import ee
import pandas as pd

ee.Initialize(project="isro-aqi-project-501317")

cities = {
    "Delhi": [77.2090, 28.6139],
    "Mumbai": [72.8777, 19.0760],
    "Bengaluru": [77.5946, 12.9716],
    "Chennai": [80.2707, 13.0827],
    "Kolkata": [88.3639, 22.5726]
}

collection = (
    ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_NO2")
    .filterDate("2025-01-01", "2025-01-31")
    .select("NO2_column_number_density")
)

image = collection.mean()

data = []

for city, coord in cities.items():
    point = ee.Geometry.Point(coord)

    value = image.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=point,
        scale=1000
    )

    no2 = value.get("NO2_column_number_density").getInfo()

    data.append({
        "City": city,
        "NO2": no2
    })

df = pd.DataFrame(data)

df.to_csv("data/live_satellite_data.csv", index=False)

print(df)