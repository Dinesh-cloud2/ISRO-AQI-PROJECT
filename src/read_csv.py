# import pandas as pd
# df=pd.read_csv("data/aqi_data.csv")
# print(df)                                

import pandas as pd

df = pd.read_csv("data/aqi_data.csv")

print("First 5 Rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nDataset Shape:")
print(df.shape)

print("\nBasic Statistics:")
print(df.describe())