import sqlite3

def print_name_loop(query):
    for result in cursor.execute(query):
        print(f'{result[0]} {result[1]}')

connection = sqlite3.connect('sample.db')
cursor = connection.cursor()

# Prints people named Brian ordered by their last names in ascending order
query = 'SELECT name,surname FROM people WHERE name="Brian" ORDER BY surname'
print_name_loop(query)

print("")

# Prints people with a name that begins with an S and ends with a n in ascending order first
# by first name then by surname
query = 'SELECT name,surname FROM people WHERE name LIKE "S%on" ORDER BY name,surname'
print_name_loop(query)

cursor.close()
connection.close()