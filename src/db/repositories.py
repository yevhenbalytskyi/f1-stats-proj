def insert_driver(cur, driver):
    cur.execute(
        """
        INSERT INTO drivers (driver_number, full_name)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING
        """,
        (driver["driver_number"], driver["full_name"])
    )