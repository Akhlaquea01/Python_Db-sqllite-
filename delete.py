import sqlite3

conn = sqlite3.connect('test.db')
print("Opened Data Successfully")

conn.execute("DELETE from COMPANY where ID = 3")
conn.commit()

print("Total numbers of Rows updated :",conn.total_changes)