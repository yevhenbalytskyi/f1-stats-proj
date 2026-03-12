def insert_driver(cur, driver):
    cur.execute(
        """
        INSERT INTO drivers (driver_number, full_name, first_name, last_name, name_acronym)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING
        """,
        (driver["driver_number"], driver["full_name"], driver["first_name"], driver["last_name"], driver["name_acronym"])
    )