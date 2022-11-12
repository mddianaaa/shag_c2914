import sqlite3


connection = sqlite3.connect("p10test.sl3", 5)
cur = connection.cursor()
cur.execute("UPDATE first_table SET name='Marsel' WHERE rowid=3;")
connection.commit()
connection.close()

