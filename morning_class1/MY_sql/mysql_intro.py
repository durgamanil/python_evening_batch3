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
conn = pymysql.connect(host='localhost',user='root',password = "",db='eveningbatch22')
cursor1 = conn.cursor()
print(cursor1)


# =============================================================================
# to create new database
# =============================================================================
mydb = pymysql.connect( host="localhost",  user="root",  password="")
mycursor = mydb.cursor()

a = mycursor.execute("CREATE DATABASE vinod")
if a ==1:
    print("database created successfully")
else:
    print("database already exists")
    
    
    
# =============================================================================
# how to delete the database
# =============================================================================

mydb = pymysql.connect( host="localhost",  user="root",  password="")
mycursor = mydb.cursor()
a = mycursor.execute("DROP DATABASE vinod")
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
conn = pymysql.connect(host='localhost',user='root',password = "",db='eveningbatch22')
cursor1 = conn.cursor()
#print(cursor1)

cursor1.execute("SHOW TABLES")
#print(cursor1)
for i in cursor1:
    print(i)
    
    
# =============================================================================
# create tables in mysql
# =============================================================================
conn = pymysql.connect(host='localhost',user='root',password = "",db='eveningbatch22')
cursor1 = conn.cursor()
#print(cursor1)

cursor1.execute("CREATE TABLE student_details")
#print(cursor1)
# for i in cursor1:
#     print(i)

# =============================================================================
# fetching the details from tables
# =============================================================================
conn = pymysql.connect(host='localhost',user='root',password = "",db='eveningbatch22')
cursor1 = conn.cursor()
#print(cursor1)

cursor1.execute("SELECT * FROM  student_detail")
#print(cursor1)
for i in cursor1:
    print(i)

# =============================================================================
# students names want to fetch
# =============================================================================
conn = pymysql.connect(host='localhost',user='root',password = "",db='eveningbatch22')
cursor1 = conn.cursor()
#print(cursor1)

cursor1.execute("SELECT student_name FROM  student_marks")
#print(cursor1)
for i in cursor1:
    #print(i)
    #print(type(i))
    #print(i[0])
    name= i[0]
    if name == "vinod":
        print(f"welcome to python world {name}")
    
# =============================================================================
# two or more columns fetching from the table
# =============================================================================
    
conn = pymysql.connect(host='localhost',user='root',password = "",db='eveningbatch22')
cursor1 = conn.cursor()
#print(cursor1)

cursor1.execute("SELECT student_name,telugu FROM  student_marks")
#print(cursor1)
for i in cursor1:
    print(i)
    
 
# =============================================================================
#     3 or more
# =============================================================================
conn = pymysql.connect(host='localhost',user='root',password = "",db='eveningbatch22')
cursor1 = conn.cursor()
#print(cursor1)

cursor1.execute("SELECT student_name,telugu,GrandTotal FROM  student_marks")
#print(cursor1)
for i in cursor1:
    print(i)


# =============================================================================
# Where keyword use in mysql
# =============================================================================
conn = pymysql.connect(host='localhost',user='root',password = "",db='eveningbatch22')
cursor1 = conn.cursor()
#print(cursor1)

cursor1.execute("SELECT student_name FROM  student_marks WHERE student_name='somu'")
#print(cursor1)
for i in cursor1:
    print(i)


# =============================================================================
# two or more conditions    
# =============================================================================
conn = pymysql.connect(host='localhost',user='root',password = "",db='eveningbatch22')
cursor1 = conn.cursor()
#print(cursor1)

cursor1.execute("SELECT student_name FROM  student_marks WHERE  hindi>94 AND GrandTotal>=500")
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


conn = pymysql.connect(host='localhost',user='root',password = "",db='kumar2')
cursor1 = conn.cursor()
cursor1.execute("CREATE TABLE employee3 ( sno int,sur_name varchar(255), last_name varchar(255),father_name varchar(255) ) ")


#insert the different values into db
#=================================
conn = pymysql.connect(host='localhost',user='root',password = "",db='eveningbatch22')
cursor1 = conn.cursor()
#print(cursor1)

cursor1.execute("INSERT INTO student_marks (student_name, telugu, hindi, english, maths, science, social, GrandTotal) VALUES ( 'monu', '96', '94', '94', '98', '97', '97', '499')")
conn.commit()


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

conn = pymysql.connect(host='localhost',user='root',password = "",db='eveningbatch22')
cursor1 = conn.cursor()
#print(cursor1)


# sql = "INSERT INTO employee (name, father_name,designation) VALUES (%s, %s,%s)"
# val = ("ramcharan", "chiranjivi","teacher")

# cursor1.execute(sql, val)
cursor1.execute("UPDATE `student_marks` SET `student_name` = 'vinod' WHERE `student_marks`.`rollno` = 20221;")

conn.commit()


# =============================================================================
# delete table
# =============================================================================
conn = pymysql.connect(host='localhost',user='root',password = "",db='eveningbatch22')
cursor1 = conn.cursor()
#print(cursor1)
cursor1.execute("DROP TABLE student_marks")

conn.commit()

#
conn = pymysql.connect(host='localhost',user='root',password = "",db='eveningbatch22')
cursor1 = conn.cursor()
#print(cursor1)
cursor1.execute("DROP TABLE student_detail")

conn.commit()



# =============================================================================
# fetch command
# =============================================================================
conn = pymysql.connect(host='localhost',user='root',password = "",db='eveningbatch22')
cursor1 = conn.cursor()
#print(cursor1)

cursor1.execute("SELECT student_name,telugu FROM  student_marks")
#print(cursor1)
for i in cursor1:
    print(i)







# =============================================================================
# 
# =============================================================================
def mysqlconnect():
	# To connect MySQL database
	 conn = pymysql.connect(
		host     = 'localhost',
		user     = 'root',
		password =  "",
		db       = 'College',
		)
     cur = conn.cursor()
     cur.execute("select @@version")
     print(cur.execute("select @@version"))
	  output = cur.fetchall()
	  print(output)
	
	# To close the connection
	conn.close()

# Driver Code
if __name__ == "__main__" :
	mysqlconnect()
