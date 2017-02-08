import sqlite3

with sqlite3.connect('calc.db') as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE calculations (num1 INTEGER, num2 INTEGER, operator TEXT, solution REAL)""")
    c.execute("""INSERT INTO calculations VALUES(9, 3, "add", 12)""")
