import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="f1stats",
    user="postgres",
    password="admin",
    port=5432
)

cur = conn.cursor()

cur.execute("SELECT version();")

version = cur.fetchone()

print(version)

cur.close()
conn.close()