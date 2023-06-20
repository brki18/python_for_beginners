import psycopg2
import psycopg2 as db


# conn = db.connect(
#     host="192.168.0.13",
#     database="brki",
#     user="brki",
#     password="brki"
# )
#
# cur = conn.cursor()
#
# cur.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#     id INT PRIMARY KEY,
#     name  VARCHAR(255),
#     age INT,
#     gender char
#     );
# """)
#
# conn.commit()
# cur.close()
# conn.close()

def add_user(name, age, gender):
    try:
        with psycopg2.connect(
                host="192.168.0.13",
                database="brki",
                user="brki",
                password="brki"
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(f"INSERT INTO users(name, age, gender) VALUES ('{name}', {age}, '{gender}')")
        cur.close()
    except Exception as err:
        print(err)


# add_user('Marko', 36, 'm')


def login(username, password):
    print(f"SELECT FROM users WHERE username == {username} AND password == {password}")
    # try:
    #     with psycopg2.connect(
    #             host="192.168.0.13",
    #             database="brki",
    #             user="brki",
    #             password="brki"
    #     ) as conn:
    #         with conn.cursor() as cur:
    #             cur.execute(f"SELECT FROM users WHERE username == {username} AND password == {password}")
    #     cur.close()
    # except Exception as err:
    #     print(err)

login('admin', 'test OR 1 == 1')