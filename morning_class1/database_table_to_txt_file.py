# -*- coding: utf-8 -*-
"""
Created on Wed May 25 19:40:13 2022

@author: durga
"""


import pymysql


file1 = open("test3.txt",'a')
#file1.write("extraline append to  nextline")
#print(file1)


conn = pymysql.connect(host='localhost',user='root',password = "",db='eveningbatch22')
cursor1 = conn.cursor()
#print(cursor1)

cursor1.execute("SELECT * FROM  student_detail")
#print(cursor1)
for i in cursor1:
    #print(i)
    #print(type(i))
    i = i[1]
    i = str(i)
    file1.write(i)
    