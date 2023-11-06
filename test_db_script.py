import string
from pprint import pprint
from random import choice

import psycopg2


def generate_login(uid):
    name = choice(string.ascii_lowercase)
    surname = "".join(choice(string.ascii_lowercase) for _ in range(5))
    return f'{name}_{uid}_{surname}'


def generate_name():
    return "".join(choice(string.ascii_lowercase) for _ in range(6)).title()


if __name__ == "__main__":
    conn = psycopg2.connect(
        host="IP_or_nostname",
        port=5432,  # Порт должен быть числом, не строкой
        database='test_db',
        user='test_user',
        password='test_password'
    )

    cur = conn.cursor()

    cur.execute(
        """
            CREATE TABLE app_table(uid int not null, login text not null, name text not null);
        """
    )

    for i in range(1, 101):
        login = generate_login(i)
        name = generate_name()
        cur.execute("INSERT INTO app_table(uid, login, name) VALUES (%s, %s, %s);", (i, login, name))

    cur.execute("SELECT * FROM app_table;")
    sql_data = cur.fetchall()

    pprint(sql_data)

    conn.commit()
    cur.close()
    conn.close()
