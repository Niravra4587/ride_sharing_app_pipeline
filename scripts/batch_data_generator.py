import csv
import random
from datetime import timedelta
from faker import Faker
from mimesis import Address

fake = Faker()
address_gen = Address()
statuses = ["completed", "cancelled", "in_progress"]

def generate_ride_data(filename="inputs/rides.csv", n=2000):
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "trip_id", "driver_id", "user_id","pickup_time", "dropoff_time",
            "pickup_location", "dropoff_location", "fare_amount", "status"
        ])

        for i in range(n):
            pickup_time = fake.date_time_between(start_date="-1d", end_date="now")
            dropoff_time = pickup_time + timedelta(minutes=random.randint(5, 60))
            pickup_location = address_gen.address().replace("\n", ", ")
            if random.random() < 0.05:
                pickup_location = None

            dropoff_location = address_gen.address().replace("\n", ", ")
            if random.random() < 0.05:
                dropoff_location = None
            fare = round(random.uniform(5, 50), 2) if random.random() > 0.15 else None
            status = "completed" if fare and random.random() > 0.19 else random.choice(statuses)
            writer.writerow([
                f"trip_{i}", f"driver_{random.randint(1, 20)}",
            f"user_{random.randint(45, 78)}",
                pickup_time, dropoff_time,
                pickup_location, dropoff_location,
                fare, status
            ])


generate_ride_data(n=2000)
