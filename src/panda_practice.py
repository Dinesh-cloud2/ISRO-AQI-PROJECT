import pandas as pd
data ={
    "city": ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Kolkata'],
    "aqi": [65, 82, 72, 95, 110],
    "PM2.5": [35, 40, 30, 45, 50],
    "temprature": [30, 32, 28, 33, 29]
}
df=pd.DataFrame(data)
print(df)
