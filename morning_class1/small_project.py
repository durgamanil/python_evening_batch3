# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 06:34:09 2022

@author: durga
"""
import os
import time


print("This is the  hotel management")

cust_name = input("please enter your name")
cust_address = input("please enter your address")
cust_phonenum = int(input("please enter your mobile num"))

if os.listdir(os.path.join("D:\python\morning_class")):
    #cust_details = open("cust_details.txt",'x')
    pass
else:
    print("file directory is not available")
    

time.sleep(2)
cust_details = open("cust_details.txt",'a')

cust_details.write(cust_name + cust_address + str(cust_phonenum))


time.sleep(2)
cust_details = open("cust_details.txt",'r')
print(cust_details.read())
    



 