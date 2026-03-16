from api.openf1 import get_meetings
from db.connection import get_connection
from db.repositories import insert_meeting
import json

def ingest_meetings():
    meetings = get_meetings()

    conn = get_connection()
    cur = conn.cursor()

    for meeting in meetings:
        insert_meeting(cur, meeting)
        #print(meeting)

    conn.commit()
    conn.close()