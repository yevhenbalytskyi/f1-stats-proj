import requests

BASE_URL = "https://api.openf1.org/v1"


def get_meetings():
    url = f"{BASE_URL}/meetings"
    return requests.get(url).json()


def get_sessions():
    url = f"{BASE_URL}/sessions"
    return requests.get(url).json()


def get_drivers():
    url = f"{BASE_URL}/drivers?session_key=latest"
    return requests.get(url).json()


def get_pits():
    url = f"{BASE_URL}/pit"
    return requests.get(url).json()