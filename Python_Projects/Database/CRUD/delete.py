import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("DELETE FROM users WHERE password = 'password-james'")

connection.commit()

# I cant seem to delete password Here 