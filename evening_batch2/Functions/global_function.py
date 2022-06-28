# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 19:03:50 2022

@author: durga
"""

# =============================================================================
# Global variable
# =============================================================================

#keyword ---> global


def school_fn():
    a =10
    b =20
    global c
    c = a+b
    print(c)



school_fn()   
d = 50+c
print(d) 





#Q1
def school1_fn():
    a =10
    b =20
    global c
    c = a+b
    print(c)


def school2_fn():
    a =20
    b =20
    c = a+b
    print(c)


school1_fn()   
d = 50+c
print(c)
school2_fn()  
print(c) 


# print(d)
# print(a)
# print(b)
# print(c)

global c

def school1_fn():
    a =10
    b =20
    #global c
    c = a+b
    print(c)


def school2_fn():
    a =20
    b =20
    #global c 
    c = a+b
    print(c)


#c=0
school1_fn()   
d = 50+c
print(c)
school2_fn()  
print(c) 


# =============================================================================
# #multiple returns
# =============================================================================
def school2_fn():
    a =20
    b =20
    c = a+b
    return c,a,b

d = school2_fn()  
print(d[0]) 
print(type(d))




#

def school2_fn():
    a =20
    b =20
    c = a+b
    return b
    return a
    return c


d = school2_fn()  
print(d)



# =============================================================================
# #pass by value
# =============================================================================
def school2_fn(a,b):
    print(a,b)
    a =a
    b =b
    c = a+b
    return c


d = school2_fn(10,20)  
print(d)


#pass by reference
def school2_fn(a,b):
    print(a,b)
    a =a
    b =b
    c = a+b
    return c

#
a = 20
b = 40
d = school2_fn(a,b)  
print(d)













    

