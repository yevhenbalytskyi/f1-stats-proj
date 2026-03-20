from api.openf1 import get_pits
from db.connection import get_connection
from db.repositories import insert_pit_stop
import json

def ingest_pits():
    pit_stops = get_pits()

    conn = get_connection()
    cur = conn.cursor()

    for pit_stop in pit_stops:
        insert_pit_stop(cur, pit_stop)

    conn.commit()
    conn.close()