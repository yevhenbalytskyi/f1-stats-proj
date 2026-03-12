from ingest.drivers import ingest_drivers
from ingest.meetings import ingest_meetings

session_key = "latest"
year = 2026

ingest_drivers(session_key)

ingest_meetings(year)
