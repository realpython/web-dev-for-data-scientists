import sqlite3


def drop_table():
    with sqlite3.connect('bitcoin.db') as connection:
        c = connection.cursor()
        c.execute("""DROP TABLE IF EXISTS rates;""")
    return True


def create_db():
    with sqlite3.connect('bitcoin.db') as connection:
        c = connection.cursor()
        table = """CREATE TABLE rates(
                    currency TEXT,
                    price REAL,
                    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                );
                """
        c.execute(table)
    return True


if __name__ == '__main__':
    drop_table()
    create_db()
