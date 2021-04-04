import sqlite3

conn = sqlite3.connect('test.db')
print("Opened Data Successfully")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
    VALUES (1,'Atts',32,'cALIFORNIA',2000.00)")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
    VALUES (2,'Akhlaque',32,'cALIFORNIA',2000.00)")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
    VALUES (3,'Ashfaque',32,'cALIFORNIA',2000.00)")

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)\
    VALUES (4,'Firoz',32,'cALIFORNIA',2000.00)")

conn.commit()
print("Records created successfully")
conn.close()