# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:11:18 2022

@author: durga
"""

# =============================================================================
# try except finally
# =============================================================================

a =10
b =0

if True:
    a/b
else:
    20/a
    
    
print("this is after the code ")
print(10/20)
print("this si agin testing")



def sum(func):
    def inner(a,b):
        print("this is from sum ",a+b)
        func(a,b)
    return inner


def divide(func):
    def inner(a,b):
        print("this is from sum ",a/b)
        func(a,b)
    return inner

@sum
@divide
def math(a,b):
    print("this is math",a,b)
    
math(10, 20)



# =============================================================================
# 
# =============================================================================
a =10
b =0

try:
    print("try block")
    a/b
except:
    print("except")
    20/a
    
    
print("this is after the code ")
print(10/20)
print("this si agin testing")



def sum(func):
    def inner(a,b):
        print("this is from sum ",a+b)
        func(a,b)
    return inner


def divide(func):
    def inner(a,b):
        print("this is from sum ",a/b)
        func(a,b)
    return inner

@sum
@divide
def math(a,b):
    print("this is math",a,b)
    
math(10, 20)




