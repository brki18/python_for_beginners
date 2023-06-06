import psycopg2 as db

conn = db.connect(
    host="192.168.0.13",
    database="brki",
    user="brki",
    password="brki"
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY,
    name  VARCHAR(255),
    age INT,
    gender char
    );
""")

conn.commit()
cur.close()
conn.close()
