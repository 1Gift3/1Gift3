import sqlite3

connection = sqlite3.connect("users.db")

cursor = connection.cursor()

command = "CREATE TABLE IF NOT EXISTS users(name TEXT, password TEXT, age INTEGER)"

cursor.execute(command)

# I cant seem to delete password Here 