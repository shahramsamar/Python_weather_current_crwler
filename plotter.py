import matplotlib.pyplot as plt
import pandas as pd

# read cvs file
df = pd.read_csv("weather_data.csv")


# convert time colum to datetime object
df["time"] = pd.to_datetime(df["time"])

# plot each metric as a separate time series
plt.figure(figsize=(10, 6))

metrics = [
    "relative_humidity_2m",
    "wind_speed_180m",
    "temperature_180m",
    "soil_temperature_54cm",
]

for metric in metrics:
    plt.plot(df["time"], df[metric], label=metric)

plt.xlabel("time")
plt.ylabel("value")
plt.title("metrics over time")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
