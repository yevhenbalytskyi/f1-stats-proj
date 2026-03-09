import requests
import json

url = f"https://api.openf1.org/v1/sessions?country_name=Belgium"

response = requests.get(url)

data = response.json()

print(data[2])