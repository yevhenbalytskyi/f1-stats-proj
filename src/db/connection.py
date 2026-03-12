import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        dbname="f1stats",
        user="postgres",
        password="admin",
        port=5432
    )