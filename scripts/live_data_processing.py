import json
import time
from datetime import datetime
from collections import deque

rolling_window = deque(maxlen=60)

with open("inputs/rides.jsonl", "r") as ride_file, open("live_ride_metrics.jsonl", "a") as out_file:
    for line in ride_file:
        ride = json.loads(line)
        if not ride.get("trip_id") or not ride.get("fare_amount"):
            continue
        fare = ride["fare_amount"]
        if fare > 0:
            rolling_window.append(fare)
        pickup_time = datetime.strptime(ride["pickup_time"], "%Y-%m-%d %H:%M:%S")
        metrics = {
            "timestamp_minute": pickup_time.strftime('%M'),
            "rolling_trip_count": len(rolling_window),
            "rolling_avg_fare": round(sum(rolling_window) / len(rolling_window), 2) if rolling_window else 0
        }

        record = {
            "event_number": ride["trip_id"],
            "ride": ride,
            "rolling_metrics": metrics
        }

        out_file.write(json.dumps(record) + "\n")
        out_file.flush()

       