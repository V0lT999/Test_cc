import psycopg2
from psycopg2 import Error


def insert(values):
    try:
        with psycopg2.connect(dbname='crypt', user='postgres',
                            password='qwerty', host='localhost') as conn:
            cursor = conn.cursor()
            request = f"INSERT INTO Current_Currency (Name_Currency, Value_Currency) VALUES {values}"
            cursor.execute(request)
            conn.commit()
    except (Exception, Error) as error:
        print("Error with PostgreSQL: ", error)


def update(name, value):
    try:
        with psycopg2.connect(dbname='crypt', user='postgres',
                            password='qwerty', host='localhost') as conn:
            cursor = conn.cursor()
            request = f"UPDATE Current_Currency set Value_Currency = {value} where Name_Currency = '{name}'"
            cursor.execute(request)
            conn.commit()
    except (Exception, Error) as error:
        print("Error with PostgreSQL: ", error)


def join():
    try:
        with psycopg2.connect(dbname='crypt', user='postgres',
                              password='qwerty', host='localhost') as conn:
            cursor = conn.cursor()
            request = """SELECT Current_Currency.Id_currency, Current_Currency.Value_Currency
                        FROM Current_Currency EXCEPT
                        SELECT History_Updates.Id_currency, History_Updates.Value_Currency
                        FROM History_Updates
            """
            cursor.execute(request)
            rows = cursor.fetchall()
            for row in rows:
                request_rows = f"INSERT INTO History_Updates (Id_currency, Value_Currency) VALUES {row}"
                cursor.execute(request_rows)
            conn.commit()
    except (Exception, Error) as error:
        print("Error with PostgreSQL: ", error)


def insert_history():
    try:
        with psycopg2.connect(dbname='crypt', user='postgres',
                              password='qwerty', host='localhost') as conn:
            cursor = conn.cursor()
            request = f"INSERT INTO History_Updates (id_currency, Value_Currency) SELECT id_currency, Value_Currency FROM Current_Currency"
            cursor.execute(request)
            conn.commit()
    except (Exception, Error) as error:
        print("Error with PostgreSQL: ", error)