import sqlite3 

conn = sqlite3.connect('example.db')

conn.execute("INSERT INTO EMPLOYEES VALUES (1,'FAITH KARIMI',23,345000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'BOB KURIA',23,305000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3,'ALICE WANJALA',23,245000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'ABEL KAMAU',27,145000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5,'PAUL KAMAU',45,50000.00)")

conn.commit()
print('Records inserted successfully')
conn.close()
