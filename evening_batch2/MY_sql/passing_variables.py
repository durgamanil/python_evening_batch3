# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 19:23:21 2022

@author: durga
"""
import pymysql

#import pymysql.connector

name1  = "emmawatson"
join1  = "2019-03-23"
sal1 = 10000

name2  = "willsmith"
join2  = "2019-03-23"
sal2 = 20000
try:
    connection = pymysql.connect(host='localhost',
                                         database='evening',
                                         user='root',
                                         password = '')

    cursor = connection.cursor()
    # Parameterized query
    sql_insert_query = """ INSERT INTO Employee
                       (id, Name, Joining_date, salary) VALUES (%s,%s,%s,%s)"""
    # tuple to insert at placeholder
    tuple1 = (3, name1, join1, sal1)
    #tuple2 = (2, "Emma", "2019-05-19", 9500)

    cursor.execute(sql_insert_query, tuple1)
    #cursor.execute(sql_insert_query, tuple2)
    connection.commit()
    print("Data inserted successfully into employee table using the prepared statement")

except :
    print("parameterized query failed {}")
finally:
    # if connection.is_connected():
    #     cursor.close()
    #     connection.close()
    #     print("MySQL connection is closed")
    pass