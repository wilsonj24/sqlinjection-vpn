import sqlite3

with sqlite3.connect("data.db") as connection:
    c = connection.cursor()
