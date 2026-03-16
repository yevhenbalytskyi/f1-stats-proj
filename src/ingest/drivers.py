from api.openf1 import get_drivers
from db.connection import get_connection
from db.repositories import insert_driver


def ingest_drivers():
    drivers = get_drivers()

    conn = get_connection()
    cur = conn.cursor()

    for driver in drivers:
        insert_driver(cur, driver)

    conn.commit()
    conn.close()