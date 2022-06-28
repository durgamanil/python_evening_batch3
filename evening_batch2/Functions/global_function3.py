# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 20:18:19 2022

@author: durga
"""



def school1_fn():
    a =10
    b =20
    #global c
    c = a+b
    print(c)
    print(id(c))


def school2_fn():
    a =20
    b =20
    global c 
    c = a+b
    print(c)


# c=0
# print(id(c))

school1_fn()   
d = 50+c
print("d====>",d)
print(c)
school2_fn()  
print(c) 