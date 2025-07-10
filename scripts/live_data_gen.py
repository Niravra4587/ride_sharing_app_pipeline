import time
import random
import json
from datetime import datetime, timedelta
from faker import Faker
from mimesis import Address

fake = Faker()
address_gen = Address()
from collections import deque

fake = Faker()

trip_id_counter = 0


with open("inputs/rides.jsonl", "a") as f:
    

    while True:

        pickup_time = datetime.now()
        dropoff_time = pickup_time + timedelta(minutes=random.randint(5, 60))

        trip_id = f"trip_{trip_id_counter}" if random.random() > 0.02 else None
        fare_amount = round(random.uniform(5, 50), 2) if random.random() > 0.05 else None
        pickup_location = address_gen.address().replace("\n", ", ")
        if random.random() < 0.05:
                pickup_location = None

        dropoff_location = address_gen.address().replace("\n", ", ")
        if random.random() < 0.05:
                dropoff_location = None
        ride = {
            "trip_id": trip_id,
            "driver_id": f"driver_{random.randint(1, 20)}",
            "user_id": f"user_{random.randint(45, 78)}",
            "pickup_time": pickup_time.strftime('%Y-%m-%d %H:%M:%S'),
            "dropoff_time": dropoff_time.strftime('%Y-%m-%d %H:%M:%S'),
            "pickup_location": pickup_location,
            "dropoff_location": dropoff_location,
            "fare_amount": fare_amount,
            "status": random.choice(["completed", "cancelled", "in_progress"])
        }

        f.write(json.dumps(ride) + "\n")
        f.flush()  

        trip_id_counter += 1
        time.sleep(1)  

