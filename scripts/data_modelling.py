import sqlite3
import pandas as pd
from faker import Faker

fake = Faker()
conn = sqlite3.connect('rides.db')
cursor = conn.cursor()
df=pd.read_csv("inputs/rides.csv")
dim_drivers = df[['driver_id']].drop_duplicates().copy()
dim_drivers['driver_name'] = [fake.name() for _ in range(len(dim_drivers))]
dim_users = df[['user_id']].drop_duplicates().copy()
dim_users['user_name'] = [fake.name() for _ in range(len(dim_users))]

cursor.execute("DROP TABLE IF EXISTS dim_drivers;")
cursor.execute("DROP TABLE IF EXISTS dim_users;")
cursor.execute("DROP TABLE IF EXISTS fact_trips;")
cursor.execute("""
    CREATE TABLE dim_drivers (driver_id TEXT PRIMARY KEY,driver_name TEXT);""")
cursor.execute("""
    CREATE TABLE dim_users (user_id TEXT PRIMARY KEY,user_name TEXT);""")
cursor.execute("""CREATE TABLE fact_trips (trip_id TEXT PRIMARY KEY,driver_id TEXT,user_id TEXT,pickup_time TEXT,dropoff_time TEXT,pickup_location TEXT,dropoff_location TEXT,fare_amount REAL,
        status TEXT,duration REAL,
        FOREIGN KEY (driver_id) REFERENCES dim_drivers(driver_id),
        FOREIGN KEY (user_id) REFERENCES dim_users(user_id)
    );""")

for _, row in dim_drivers.iterrows():
    cursor.execute("INSERT INTO dim_drivers (driver_id, driver_name) VALUES (?, ?)",(row['driver_id'], row['driver_name']))
for _, row in dim_users.iterrows():
    cursor.execute("INSERT INTO dim_users (user_id, user_name) VALUES (?, ?)",(row['user_id'], row['user_name']))



conn.close()