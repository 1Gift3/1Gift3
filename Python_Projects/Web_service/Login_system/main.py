import sqlite3
import hashlib 

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VACHAR(255) NOT NULL,
    password VACHAR(255) NOT NULL)           
""")

username1, password1 = "mike213", hashlib.sha256("mikepassword".encode()).hexdigest()
username2, password2 = "Josh", hashlib.sha256("ooomg123".encode()).hexdigest()
username3, password3 = "Josha113", hashlib.sha256("jso1123".encode()).hexdigest()
username4, password4 = "Pheeman121", hashlib.sha256("whathappended".encode()).hexdigest()
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password4))

conn.commit()