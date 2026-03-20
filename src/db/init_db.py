from db.connection import get_connection

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        DROP TABLE meetings CASCADE;
        DROP TABLE sessions CASCADE;
        DROP TABLE drivers CASCADE;
        DROP TABLE pit_stops CASCADE;
        """
    )

    with open("sql/schema.sql", "r") as f:
        cur.execute(f.read())

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()