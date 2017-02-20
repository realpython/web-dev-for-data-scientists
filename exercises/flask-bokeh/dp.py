import sqlite3


def drop_table():
    with sqlite3.connect('bokeh.db') as connection:
        c = connection.cursor()
        c.execute("""DROP TABLE IF EXISTS greenhouse;""")
    return True


def create_db():
    with sqlite3.connect('bokeh.db') as connection:
        c = connection.cursor()
        c.execute("""CREATE TABLE greenhouse (time REAL, temp REAL, type TEXT);""")
    return True


def seed(file_name, temp_from):
    with sqlite3.connect('bokeh.db') as connection:
        c = connection.cursor()
        with open(file_name, 'r') as data:
            for value in data:
                value.replace('\n', '')
                array = value.split(',')
                values = [array[0], array[1], temp_from]
                c.execute('INSERT INTO greenhouse VALUES(?, ?, ?)', values)


if __name__ == '__main__':
    drop_table()
    create_db()
    seed('DataTemp1.dat', 'inside')
    seed('DataTemp2.dat', 'outside')
