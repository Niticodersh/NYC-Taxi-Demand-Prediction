import sys

import pandas as pd

file_path = sys.argv[1]
output_path = sys.argv[2]

df = pd.read_parquet(file_path)

df = df[df["passenger_count"] >= 1]
df = df[df["fare_amount"] > 0]
df = df[df["total_amount"] > 0]
df = df[df["trip_distance"] > 0]
y_m = file_path.split("_")[-1]
y_m = y_m.split(".")[0]
y, m = y_m.split("-")

df["tpep_pickup_datetime"] = df["tpep_pickup_datetime"].astype("datetime64[ns]")
df["hour"] = df["tpep_pickup_datetime"].dt.hour
df["day"] = df["tpep_pickup_datetime"].dt.day
df["time"] = pd.to_datetime(
    f"{y}-{m}-" + df["day"].astype(str) + " " + df["hour"].astype(str) + ":00:00",
    errors="coerce",
)

columns = ["time", "total_amount", "fare_amount", "passenger_count", "trip_distance"]
df = df[columns]
df = df.dropna()
params = {
    "total_amount": ("total_amount", "sum"),
    "mean_amount": ("total_amount", "mean"),
    "mean_fare_amount": ("fare_amount", "mean"),
    "passenger_count": ("passenger_count", "sum"),
    "mean_passenger_per_trip": ("passenger_count", "mean"),
    "total_trip_distance": ("trip_distance", "sum"),
    "mean_trip_distance": ("trip_distance", "mean"),
    "number_trips": ("passenger_count", "count"),
}
df_final = df.groupby("time").agg(**params).reset_index()
df_final.to_parquet(output_path, index=False)
