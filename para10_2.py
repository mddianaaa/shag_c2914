import sqlite3


connection = sqlite3.connect("p10test.sl3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Eliot');")
connection.commit()
connection.close()
