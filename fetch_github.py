import requests
import psycopg2

SESSION_KEY = 9140

laps = requests.get(
    f"https://api.openf1.org/v1/laps?session_key={SESSION_KEY}"
).json()

print(laps)