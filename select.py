import sqlite3
from sqlite3.dbapi2 import Cursor

conn = sqlite3.connect('test.db')
print("Opened Data Successfully")

cursor=conn.execute("SELECT id,name,address,salary from COMPANY")
for row in cursor:
    print ("ID = ",row[0])
    print("NAME =",row[1])
    print("ADDRESS =",row[2])
    print("SALARY =",row[3],"\n")

print("operation done")
conn.close()