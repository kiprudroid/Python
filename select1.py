# Description: This file is used to select data from the database
import sqlite3

conn = sqlite3.connect('example.db')
print('opened database successfuly')

cursor = conn.execute("SELECT * FROM EMPLOYEES WHERE ID > 0")
for row in cursor:
    print('ID       :',row[0])
    print('Name     :',row[1])
    print('Age      :',row[2])
    print("Salary   :",row[3])
    print('''


''')

print('Records found')
conn.close()

