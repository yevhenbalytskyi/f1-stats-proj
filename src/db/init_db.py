from db.connection import get_connection

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        DROP TABLE sessions;
        DROP TABLE meetings;
        DROP TABLE drivers;
        """
    )

    with open("sql/schema.sql", "r") as f:
        cur.execute(f.read())

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()