import sqlite3
import csv


with sqlite3.connect('bokeh.db') as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE temperature (time REAL, temperature REAL)""")
    with open('DataTemp1.dat', 'r') as data:
        for value in data:
            value.replace('\n', '')
            array = value.split(',')
            c.execute('INSERT INTO temperature VALUES({0}, {1})'.format(
                array[0], array[1]))
