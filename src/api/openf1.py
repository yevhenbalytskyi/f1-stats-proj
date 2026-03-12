import requests

BASE_URL = "https://api.openf1.org/v1"

def get_sessions(year: int):
    url = f"{BASE_URL}/sessions?year={year}"
    return requests.get(url).json()


def get_drivers(session_key: int):
    url = f"{BASE_URL}/drivers?session_key={session_key}"
    return requests.get(url).json()


def get_laps(session_key: int):
    url = f"{BASE_URL}/laps?session_key={session_key}"
    return requests.get(url).json()