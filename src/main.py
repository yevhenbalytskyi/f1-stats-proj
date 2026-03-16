from ingest.drivers import ingest_drivers
from ingest.meetings import ingest_meetings
from ingest.sessions import ingest_sessions

session_key = "latest"

ingest_drivers(session_key)

ingest_meetings()
ingest_sessions()
