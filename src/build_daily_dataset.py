import ee
import pandas as pd
import random
from datetime import datetime, timedelta

# Initialize Earth Engine
ee.Initialize(project="isro-aqi-project-501317")

# Cities (Longitude, Latitude)
cities = {
    "Delhi": [77.1025, 28.7041],
    "Mumbai": [72.8777, 19.0760],
    "Bengaluru": [77.5946, 12.9716],
    "Chennai": [80.2707, 13.0827],
    "Kolkata": [88.3639, 22.5726]
}

rows = []

start = datetime(2025, 1, 1)
end = datetime(2025, 1, 31)

while start <= end:

    next_day = start + timedelta(days=1)

    date1 = start.strftime("%Y-%m-%d")
    date2 = next_day.strftime("%Y-%m-%d")

    # NO2 Dataset
    no2 = (
        ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_NO2")
        .filterDate(date1, date2)
        .select("NO2_column_number_density")
        .mean()
    )

    # HCHO Dataset
    hcho = (
        ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_HCHO")
        .filterDate(date1, date2)
        .select("tropospheric_HCHO_column_number_density")
        .mean()
    )

    # Weather Dataset
    weather = (
        ee.ImageCollection("ECMWF/ERA5_LAND/DAILY_AGGR")
        .filterDate(date1, date2)
        .mean()
    )

    for city, coord in cities.items():

        point = ee.Geometry.Point(coord)

        no2_value = no2.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=point,
            scale=1000
        ).get("NO2_column_number_density").getInfo()

        hcho_value = hcho.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=point,
            scale=1000
        ).get("tropospheric_HCHO_column_number_density").getInfo()

        temp = weather.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=point,
            scale=1000
        ).get("temperature_2m").getInfo()

        wind = weather.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=point,
            scale=1000
        ).get("u_component_of_wind_10m").getInfo()

        # Convert Kelvin to Celsius
        if temp is not None:
            temp = round(temp - 273.15, 1)

        # Temporary humidity
        humidity = 60

        # Temporary AQI
        aqi = random.randint(40, 350)

        rows.append({
            "Date": date1,
            "City": city,
            "NO2": no2_value,
            "HCHO": hcho_value,
            "Temperature": temp,
            "Humidity": humidity,
            "WindSpeed": wind,
            "AQI": aqi
        })

    print(date1, "completed")

    start = next_day

df = pd.DataFrame(rows)

df.to_csv(
    "data/final_dataset/daily_satellite_dataset.csv",
    index=False
)

print(df.head())
print("Rows:", len(df))
print("Dataset created successfully!")