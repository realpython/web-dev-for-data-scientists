import csv
import sqlite3


def drop_table():
    with sqlite3.connect('greenhouse.db') as connection:
        c = connection.cursor()
        c.execute('DROP TABLE IF EXISTS greenhouse')
    return True


def create_db():
    with sqlite3.connect('greenhouse.db') as connection:
        c = connection.cursor()
        c.execute('CREATE TABLE greenhouse (time REAL, temp REAL)')
    return True


def seed():
    # open the database
    with sqlite3.connect('greenhouse.db') as connection:
        c = connection.cursor()
        # open the datafile
        with open('data.dat') as data:
            reader = csv.reader(data)
            # iterate through the datafile
            for row in reader:
                c.execute('INSERT INTO greenhouse VALUES(?, ?)', row)
    return True


if __name__ == '__main__':
    drop_table()
    create_db()
    seed()
