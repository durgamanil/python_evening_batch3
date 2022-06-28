# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:46:07 2022

@author: durga
"""

def school1():
    a =10
    b =20
    #c = a+b
    global c
    print("1 before====>",c)
    #global c
    c =30
    
    print("1 after ====>",c)
    d = a+b+c
    print("1====>",c)
    print(d)
    print("school1 fun id",id(c))


def school2():
    a =20
    b =20
    #c = a+b
    print("2====>",c)
    print("school2 fun id",id(c))


c =10
print("id in main before function 1",id(c))
school1() 
#school2()    
d = 50+c
print("id in main before function 2",id(c))
print(c)
school2()  
print(c) 