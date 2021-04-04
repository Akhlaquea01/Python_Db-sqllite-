import sqlite3

conn = sqlite3.connect('test.db')
print("Opened Data Successfully")

conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()

print("Total numbers of Rows updated :",conn.total_changes)
