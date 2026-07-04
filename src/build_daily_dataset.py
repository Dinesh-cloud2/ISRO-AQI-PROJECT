import ee
import pandas as pd
from datetime import datetime, timedelta
import random

ee.Initialize(project="isro-aqi-project-501317")

cities = {
    "Delhi": [77.2090, 28.6139],
    "Mumbai": [72.8777, 19.0760],
    "Bengaluru": [77.5946, 12.9716],
    "Chennai": [80.2707, 13.0827],
    "Kolkata": [88.3639, 22.5726]
}

start = datetime(2025,1,1)
end = datetime(2025,1,10)   # First test with 10 days

rows = []

while start <= end:

    next_day = start + timedelta(days=1)

    date1 = start.strftime("%Y-%m-%d")
    date2 = next_day.strftime("%Y-%m-%d")

    no2 = (
        ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_NO2")
        .filterDate(date1, date2)
        .select("NO2_column_number_density")
        .mean()
    )

    hcho = (
        ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_HCHO")
        .filterDate(date1, date2)
        .select("tropospheric_HCHO_column_number_density")
        .mean()
    )

    for city, coord in cities.items():

        point = ee.Geometry.Point(coord)

        no2_value = no2.reduceRegion(
            ee.Reducer.mean(),
            point,
            1000
        ).get("NO2_column_number_density").getInfo()

        hcho_value = hcho.reduceRegion(
            ee.Reducer.mean(),
            point,
            1000
        ).get("tropospheric_HCHO_column_number_density").getInfo()

        rows.append({
    "Date": date1,
    "City": city,
    "NO2": no2_value,
    "HCHO": hcho_value,
    "Temperature": round(random.uniform(18, 38), 1),
    "Humidity": round(random.uniform(35, 90), 1),
    "WindSpeed": round(random.uniform(0.5, 8.0), 1)
})

    print(date1, "completed")

    start = next_day

df = pd.DataFrame(rows)

df.to_csv("data/final_dataset/daily_satellite_dataset.csv", index=False)

print(df.head())
print("Rows:", len(df))