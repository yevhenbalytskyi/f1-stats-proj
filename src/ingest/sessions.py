from api.openf1 import get_sessions
from db.connection import get_connection
from db.repositories import insert_session
import json

def ingest_sessions():
    sessions = get_sessions()

    conn = get_connection()
    cur = conn.cursor()

    for session in sessions:
        insert_session(cur, session)

    conn.commit()
    conn.close()