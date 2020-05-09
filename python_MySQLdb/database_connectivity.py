import mysql.connector

conn = mysql.connector.connect(host = 'localhost', username = 'root', password = 'root', database = 'new_database')

my_cursor = conn.cursor()

# query = "CREATE DATABASE new_database"
query = "SHOW DATABASES"
# query = "CREATE TABLE student(name VARCHAR(50), age INT)" VALUES (%s, %s)
# values = [
#     (),
#     ()
# ]

my_cursor.execute(query)
# my_cursor.execute(query, values)  # for values

# for database_name in my_cursor :   # give output in tuple
#     print(database_name)

print(my_cursor.fetchall())

conn.commit()
conn.close()