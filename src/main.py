import requests
import psycopg2
import json

conn = psycopg2.connect(
    host="localhost",
    dbname="f1stats",
    user="postgres",
    password="admin",
    port=5432
)
cur = conn.cursor()

cur.execute("SELECT version();")
version = cur.fetchone()
#print(version)


url = f"https://api.openf1.org/v1/drivers?session_key=9158"

response = requests.get(url)
drivers = response.json()

unique_drivers = {}

for d in drivers:
    number = d["driver_number"]
    unique_drivers[number] = {
        "name": d["full_name"],
        "team": d["team_name"],
        "acronym": d["name_acronym"]
    }

for num, info in unique_drivers.items():
    print(num, info["name"], "-", info["team"])


# Close communication with the database
cur.close()  
conn.close()     