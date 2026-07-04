import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/aqi_data.csv")

plt.bar(df["City"], df["AQI"])

plt.title("AQI of Different Cities")
plt.xlabel("City")
plt.ylabel("AQI")

plt.show()