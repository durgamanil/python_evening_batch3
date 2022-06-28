# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 19:32:19 2022

@author: durga
"""

#single line comments 

#----->single line comments

a = 100
b = 200


print(a+b)


#print(100+200)

print(100+200)# where 100 is num1 and 200 is num2


#multiline comments

'''

try:
    for i in range(0,len(df)):   
        CustomerID1 = df["CustomerID"].iloc[i]
        CustomerName = df["CustomerName"].iloc[i]
        ContactName = df["ContactName"].iloc[i]
        Address = df["Address"].iloc[i]
        City =  df["City"].iloc[i]
        PostalCode = df["PostalCode"].iloc[i]
        Country = df["Country"].iloc[i]
        sql = "INSERT INTO employee3 (CustomerID, CustomerName,ContactName,Address,City,PostalCode,Country) VALUES (%s, %s, %s,%s,%s,%s,%s)"
        #val = ("02","02","ramcharan1", "cheery","hyderabad","telangana","500101","india")
        val = (CustomerID1,CustomerName,ContactName, Address,City,PostalCode,Country)
        cursor1.execute(sql, val)
        conn.commit()
    
except :
    print("error in the query")
    
'''




"""
try:
    for i in range(0,len(df)):   
        CustomerID1 = df["CustomerID"].iloc[i]
        CustomerName = df["CustomerName"].iloc[i]
        ContactName = df["ContactName"].iloc[i]
        Address = df["Address"].iloc[i]
        City =  df["City"].iloc[i]
        PostalCode = df["PostalCode"].iloc[i]
        Country = df["Country"].iloc[i]
        sql = "INSERT INTO employee3 (CustomerID, CustomerName,ContactName,Address,City,PostalCode,Country) VALUES (%s, %s, %s,%s,%s,%s,%s)"
        #val = ("02","02","ramcharan1", "cheery","hyderabad","telangana","500101","india")
        val = (CustomerID1,CustomerName,ContactName, Address,City,PostalCode,Country)
        cursor1.execute(sql, val)
        conn.commit()
    
except :
    print("error in the query")
    
"""


# =============================================================================
#  documentation string
# =============================================================================
