# -*- coding: utf-8 -*-
"""
Created on Wed May 25 19:15:52 2022

@author: durga
"""
import pymysql

def mysqlconnect():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password = "",
        db='eveningbatch22')
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