import pandas as pd
from datetime import datetime
import sqlite3

rides= pd.read_csv("inputs/rides.csv")
rides = rides.dropna(subset=[
        "trip_id", "driver_id", "pickup_time", "dropoff_time", "fare_amount",
        "pickup_location", "dropoff_location", "status"
    ])
rides = rides[rides["status"].isin(["completed", "cancelled"])]
rides = rides[rides["pickup_time"] < rides["dropoff_time"]]
rides = rides[rides["fare_amount"] > 0]

rides['pickup_time'] = pd.to_datetime(rides['pickup_time'], format='%Y-%m-%d %H:%M:%S')
rides['dropoff_time'] = pd.to_datetime(rides['dropoff_time'], format='%Y-%m-%d %H:%M:%S')


rides['duration'] = (rides['dropoff_time'] - rides['pickup_time']).dt.total_seconds() / 60

conn = sqlite3.connect('rides.db')
table_name = 'fact_trips'
rides.to_sql(table_name, conn, if_exists="append", index=False)
conn.close()




