import psycopg2
import os

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

cur = conn.cursor()
cur.execute("SELECT version();")
print("PostgreSQL bağlantısı başarılı:", cur.fetchone()[0])
cur.close()
conn.close()
