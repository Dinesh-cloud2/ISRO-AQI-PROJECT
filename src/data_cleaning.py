import pandas as pd

df = pd.read_csv("data/dirty_aqi.csv")

print("Original Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df = df.dropna()

print("\nClean Dataset:")
print(df)