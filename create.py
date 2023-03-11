import sqlite3
from faker import Faker

connection = sqlite3.connect('sample.db')

try:
    table = 'CREATE TABLE people (id integer primary key, name TEXT, surname TEXT)'
    cursor = connection.cursor()
    cursor.execute(table)
    connection.commit()
except Exception as e:
    print(f"An exception has occurred when creating the table. Report: {repr(e)}")

fake = Faker()
names = [fake.name().split() for i in range(100)]
names = [name for name in names if len(name) == 2]
cursor.close()
connection.close()

connection = sqlite3.connect("sample.db")
cursor = connection.cursor()
insert_query = 'INSERT INTO people (name, surname) VALUES (?, ?)'
for name in names:
    cursor.execute(insert_query, name)
connection.commit()
cursor.close()
connection.close()