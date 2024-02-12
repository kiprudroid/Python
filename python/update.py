# Description: This file is used to update data from the database
import sqlite3

conn = sqlite3.connect('example.db')
print('opened database successfuly')

conn.execute("UPDATE EMPLOYEES SET AGE = 28 WHERE ID=5")
conn.commit()

cursor = conn.execute("SELECT * FROM EMPLOYEES")
for row in cursor:
    print('ID       :',row[0])
    print('Name     :',row[1])
    print('Age      :',row[2])
    print("Salary   :",row[3])
    print('''


''')

print('Updated')
conn.close()