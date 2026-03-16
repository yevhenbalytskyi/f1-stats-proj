def insert_driver(cur, driver):
    cur.execute(
        """
        INSERT INTO drivers (driver_number, full_name, first_name, last_name, name_acronym)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING
        """,
        (driver["driver_number"], driver["full_name"], driver["first_name"], driver["last_name"], driver["name_acronym"])
    )

def insert_meeting(cur, meeting):
    cur.execute(
        """
        INSERT INTO meetings (meeting_key, year_, meeting_name, country, location_, circuit_short_name)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING
        """,
        (meeting["meeting_key"], meeting["year"], meeting["meeting_name"], meeting["country_name"], meeting["location"], meeting["circuit_short_name"])
    )

def insert_session(cur, session):
    cur.execute(
        """
        INSERT INTO sessions (session_key, meeting_key, session_name, session_type, date_start, date_end)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING
        """,
        (session["session_key"], session["meeting_key"], session["session_name"], session["session_type"], session["date_start"], session["date_end"])
    )