import ee
import pandas as pd

ee.Initialize(project="isro-aqi-project-501317")

cities = {
    "Delhi": [77.2090, 28.6139],
    "Mumbai": [72.8777, 19.0760],
    "Bengaluru": [77.5946, 12.9716],
    "Chennai": [80.2707, 13.0827],
    "Kolkata": [88.3639, 22.5726],
    "Hyderabad": [78.4867, 17.3850],
    "Ahmedabad": [72.5714, 23.0225],
    "Pune": [73.8567, 18.5204],
    "Jaipur": [75.7873, 26.9124],
    "Lucknow": [80.9462, 26.8467]
}
no2_collection = (
    ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_NO2")
    .filterDate("2025-01-01","2025-03-31")
    .select("NO2_column_number_density")
)

hcho_collection = (
    ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_HCHO")
    .filterDate("2025-01-01","2025-01-31")
    .select("tropospheric_HCHO_column_number_density")
)

no2_image = no2_collection.mean()
hcho_image = hcho_collection.mean()

data = []

for city, coord in cities.items():

    point = ee.Geometry.Point(coord)

    no2 = no2_image.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=point,
        scale=1000
    ).get("NO2_column_number_density").getInfo()

    hcho = hcho_image.reduceRegion(
        reducer=ee.Reducer.mean(),
        geometry=point,
        scale=1000
    ).get("tropospheric_HCHO_column_number_density").getInfo()

    data.append({
        "City": city,
        "NO2": no2,
        "HCHO": hcho
    })

df = pd.DataFrame(data)

df.to_csv("data/final_dataset/satellite_dataset.csv", index=False)

print(df)
print("✅ Dataset Created Successfully")