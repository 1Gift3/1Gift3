import sqlite3

connection = sqlite3.connect("users.db")

cursor = connection.cursor()

cursor.execute("INSERT INTO users VALUES ('Rishab', '1234567890', 13)")
cursor.execute("INSERT INTO users VALUES ('josh', '7890', 45)")
cursor.execute("INSERT INTO users VALUES ('james', '14567890', 99)")

connection.commit()

