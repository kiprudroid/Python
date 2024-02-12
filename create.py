import sqlite3


#create a database
conn = sqlite3.connect('example.db')
print('Opened database successfuly')

#CREATE A NEW TABLE
conn.execute('''CREATE TABLE EMPLOYEES(
             ID INT PRIMARY KEY NOT NULL,
             NAME TEXT NOT NULL,
             AGE INT  NOT NULL,
             SALARY REAL NOT NULL

);''')
print('Table created successfully')
conn.close()