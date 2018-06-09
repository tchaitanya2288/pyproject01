#!/usr/bin/python
import MySQLdb as sqldb

# Open database connection
db = sqldb.connect(host="localhost", user="root", password="P@ssw0rd", db="mysql")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "select * from emp where emp_age=25"
# execute SQL query using execute() method.
cursor.execute(sql)

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print(data)
for i in data:
    print(i)
#print("Database version : %s " % data)

# disconnect from server
db.close()
