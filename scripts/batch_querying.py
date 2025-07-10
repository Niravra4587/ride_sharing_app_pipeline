import sqlite3
conn = sqlite3.connect('rides.db')
cursor = conn.cursor()

res=cursor.execute(""" SELECT * FROM fact_trips """).fetchall()
for row in res:
    print(row)

res=cursor.execute(""" SELECT driver_id,SUM(fare_amount) AS Total_revenue FROM fact_trips group by driver_id """).fetchall()
for row in res:
    print(row)

res = cursor.execute("""SELECT strftime('%H', pickup_time) AS Hour, COUNT(*) AS Trip_Count FROM fact_trips GROUP BY Hour ORDER BY Hour""").fetchall()

for row in res:
    print(row)
