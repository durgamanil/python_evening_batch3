# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 22:27:55 2022

@author: durga
"""

# 1.mysql
# 2.mongodb
# 3.sqlite
#import pymysql

'''
Connecting to MySQL
The proper way to get an instance of this class is to call connect() method. 
This method establishes a connection to the MySQL database and accepts several arguments:

Parameters :

host – Host where the database server is located
user – Username to log in as
password – Password to use.
database – Database to use, None to not use a particular one.
port – MySQL port to use, default is usually OK. (default: 3306)

'''


import pymysql

# =============================================================================
# how to check the methods of the pymysql
# =============================================================================
dir(pymysql)


# To connect MySQL database
conn = pymysql.connect(host='localhost',user='root',password = "",db='atm_project')
cursor1 = conn.cursor()
print(cursor1)


# =============================================================================
# to create new database
# =============================================================================
mydb = pymysql.connect( host="localhost",  user="root",  password="")
mycursor = mydb.cursor()

a = mycursor.execute("CREATE DATABASE Hotel4")
if a ==1:
    print("database created successfully")
else:
    print("database already exists")
    
    
    
# =============================================================================
# how to delete the database
# =============================================================================

mydb = pymysql.connect( host="localhost",  user="root",  password="")
mycursor = mydb.cursor()
a = mycursor.execute("DROP DATABASE Kumar")
print(a)
if a ==0:
    print("database deleted successfully")
else:
    print("database not deleted")


# =============================================================================
# existing database are there or not 
# =============================================================================

mydb = pymysql.connect( host="localhost",  user="root",  password="")

mycursor = mydb.cursor()
a = mycursor.execute("SHOW DATABASES")
print(a)

for i in mycursor:
    print(i)


# =============================================================================
# show tables in the database
# =============================================================================
conn = pymysql.connect(host='localhost',user='root',password = "",db='atm_project')
cursor1 = conn.cursor()
#print(cursor1)

cursor1.execute("SHOW TABLES")
#print(cursor1)
for i in cursor1:
    print(i)


# =============================================================================
# create tables in the database
# =============================================================================
# syntax:
    
# CREATE TABLE Persons (
#     PersonID int,
#     LastName varchar(255),
#     FirstName varchar(255),
#     Address varchar(255),
#     City varchar(255)
# );

conn = pymysql.connect(host='localhost',user='root',password = "",db='kumar2')
cursor1 = conn.cursor()
cursor1.execute("CREATE TABLE employee3 ( sno int,\
                sur_name varchar(255), \
                last_name varchar(255),\
                father_name varchar(255) \
                ) \
")


# =============================================================================
# insert data into table
# =============================================================================
    
conn = pymysql.connect(host='localhost',user='root',password = "",db='kumar2')
cursor1 = conn.cursor()
print(cursor1)


sql = "INSERT INTO employee3 (sur_name, last_name,father_name) VALUES (%s, %s,%s)"
val = ("ramcharan", "chiranjivi","teacher")

cursor1.execute(sql, val)

conn.commit()

# =============================================================================
# update the query
# =============================================================================

conn = pymysql.connect(host='localhost',user='root',password = "",db='atm_project')
cursor1 = conn.cursor()
#print(cursor1)


# sql = "INSERT INTO employee (name, father_name,designation) VALUES (%s, %s,%s)"
# val = ("ramcharan", "chiranjivi","teacher")

# cursor1.execute(sql, val)
cursor1.execute("UPDATE `employee1` SET `father_name` = 'chiranjivi2' WHERE `employee`.`s.no` = 4;")

conn.commit()


# =============================================================================
# delete table
# =============================================================================
conn = pymysql.connect(host='localhost',user='root',password = "",db='atm_project')
cursor1 = conn.cursor()
#print(cursor1)
cursor1.execute("DROP TABLE employee")

conn.commit()


def mysqlconnect():
	# To connect MySQL database
	conn = pymysql.connect(
		host='localhost',
		user='root',
		password = "pass",
		db='College',
		)
	
	cur = conn.cursor()
	cur.execute("select @@version")
	output = cur.fetchall()
	print(output)
	
	# To close the connection
	conn.close()

# Driver Code
if __name__ == "__main__" :
	mysqlconnect()
