import sqlite3

connection = sqlite3.connect('sample.db')
cursor = connection.cursor()

table_query = 'CREATE TABLE IF NOT EXISTS people (id int primary key, name TEXT, surname TEXT)'
cursor.execute(table_query)
connection.commit()