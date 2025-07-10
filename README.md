# 🚕 Ride-Sharing Analytics Pipeline

A simplified ride-sharing analytics pipeline built using Python to simulate both **batch** and **streaming** data ingestion and processing. This project uses realistic mock data to compute insights like hourly trends and rolling metrics.

---
## ER Diagram
<img width="1169" height="668" alt="image" src="https://github.com/user-attachments/assets/8a180962-94fc-417e-a3ee-249d047d1e3a" />

## Architecture Diagram
<img width="644" height="488" alt="architecture_diagram drawio" src="https://github.com/user-attachments/assets/b2cae660-2158-445e-ae02-a0399a45f756" />

---

## 📁 Project Structure

```
├── inputs/
│   ├── rides.csv               # Batch data (mock ride events)
│   ├── hourly_csv.log          # Output of hourly analytics from querying
│   └── rides.jsonl             # Live-streamed rides (one record per line)
│
├── scripts/
│   ├── batch_data_generator.py     # Generate rides.csv
│   ├── live_data_gen.py            # Simulate live ride stream to JSONL
│   ├── etl_batch.py                # ETL: clean and load batch data to SQLite
│   ├── data_querying.py            # SQL queries for reporting
│   ├── live_data_processing.py     # Rolling metrics from live JSONL stream
│   └── data_modelling.py           # Create star schema: fact & dimension tables
│__ live_ride_metrics.jsonl
├── rides.db                   # SQLite database
├── README.md
```

---

## 🚀 Features

- ✅ Mock batch and streaming data generation
- ✅ Batch ETL pipeline with cleaning rules
- ✅ SQLite-based storage and querying
- ✅ Star schema modeling with `fact_trips` and `dim_drivers`
- ✅ Real-time metrics via rolling window over live data
- ✅ All output stored as `.jsonl` or `.log` files

---

## 🛠️ Setup Instructions

### 1. 📦 Install dependencies

No external libraries beyond standard Python needed, except:

```bash
pip install pandas faker
```

---

## 📊 Data Generation

### Generate batch data (`rides.csv`)
```bash
python scripts/batch_data_generator.py
```

### Simulate live data stream (to `rides.jsonl`)
```bash
python scripts/live_data_gen.py
```

---

## 🧹 Batch ETL Pipeline

### Clean and load `rides.csv` into SQLite
```bash
python scripts/etl_batch.py
```

- Removes records with nulls or inconsistent times
- Adds ride duration column
- Loads into `fact_trips` table in `rides.db`

---

## 🧱 Data Modeling

### Create star schema tables
```bash
python scripts/data_modelling.py
```

Creates:
- `fact_trips`: fact table for trips
- `dim_drivers`: minimal driver dimension

---

## 📈 SQL-Based Reporting

### Query hourly trends, revenue, etc.
```bash
python scripts/data_querying.py
```

Outputs:
- `hourly_csv.log`: hourly trip counts
- Revenue per driver and other aggregations

---

## 📡 Live Data Processing

### Read `rides.jsonl`, calculate rolling metrics
```bash
python scripts/live_data_processing.py
```

- Maintains rolling window of last 60 valid fares
- Calculates:
  - Trips per minute
  - Average fare
- Writes metrics to `live_ride_metrics.jsonl`

---

## 📁 Sample Data Format

### rides.csv

| trip_id | driver_id | pickup_time | dropoff_time | pickup_location | fare_amount | status     |
|---------|-----------|-------------|--------------|------------------|-------------|------------|
| trip_1  | driver_3  | 2025-07-08 14:00 | 2025-07-08 14:30 | Delhi           | 35.5        | completed  |

### rides.jsonl (streaming format)

```json
{"trip_id": "trip_101", "fare_amount": 30.0, "pickup_time": "2025-07-09 12:45:01", ...}
```

---






 
