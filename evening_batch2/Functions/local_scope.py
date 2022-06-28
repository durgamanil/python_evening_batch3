# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 19:36:00 2022

@author: durga
"""

#local parameters , global parameter

#local scope and global scope

def local2_fun():
    #a =20
    print(a)
    print(b)
    
    
def local_scope():
    #a =10
    print(a)
    print(b)
    

    
b =20
a =30
print(b)
local_scope()   
print(a)


#################################
def local2_fun():
    a =20
    print(a)#20

def local_scope():
    a =50
    print(a)#50

    
a =10
local_scope()  
local2_fun() 
print(a)#10

################################
def local2_fun(a):
    print(a)

def local_scope(a):
    a =30
    print(a)

    
a =10
local_scope(a)  
local2_fun(a) 
print(a)

##################################


def local2_fun(a):
    a =40
    print(a)

def local_scope(a):
    a =30
    print(a)

    
a =10
local_scope(a)  
a =30
print(a)
local2_fun(a) 
print(a)

#30,10,40,30
#30,10,40,30


##################################
def local2_fun(a):
    a =40
    return a

def local_scope(a):
    a =30
    return a

    
a =10
a= local_scope(a)  
print(a)
a =30
print(a)
a=local2_fun(a) 
print(a)

#vandana====>30,30,40
#monu====>30,10,30,40,30
#sohan====>30,40,30




# def my_fun():
#     c =10+20
#     return c


# #print(my_fun())
# a = my_fun()
# print(a)


#

def my_fun2():
    print("this is testing")
    
    
def my_fun():
    c =10+20
    return c


#print(my_fun())
# =10
b= my_fun()
print(b)
my_fun2()
#print(a)














