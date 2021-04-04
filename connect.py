# Connect With DataBase
import sqlite3
conn = sqlite3.connect('test.db')
print("Opened Data Successfully")

# Create Table
conn.execute(''' CREATE TABLE COMPANY
(ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')
print("Table Created Successfully")

conn.close()
