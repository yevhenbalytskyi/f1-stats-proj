from ingest.drivers import ingest_drivers
from ingest.meetings import ingest_meetings
from ingest.sessions import ingest_sessions
from ingest.pit_stops import ingest_pits
from db.init_db import init_db
from db.connection import get_connection

init_db()
ingest_drivers()

ingest_meetings()
ingest_sessions()

ingest_pits()