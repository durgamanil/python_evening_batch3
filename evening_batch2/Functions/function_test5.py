# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 07:48:55 2022

@author: durga
"""

# =============================================================================
# function without arguments
# =============================================================================

def my_fn():
    print("this is zero arguments based function")
    c =10+20
    print(c)
    
    
my_fn()





# =============================================================================
# function with arguments
# =============================================================================

def my_fn(a1,b1):
    print("testing2")
    c =a1+b1
    print(c)
    

a = int(input("enter your first number"))
b = int(input("enter your second number"))

my_fn(a,b)




# =============================================================================
# postional arguments
# =============================================================================


def my_fn(a1,b1):
    print("testing2")
    print("a1--->",a1)
    print("b1--->",b1)
    c =a1+b1
    print(c)
    


my_fn(100,200)


def my_fn(a1,b1):
    print("testing2")
    print("a1--->",a1)
    print("b1--->",b1)
    c =a1+b1
    print(c)
    
my_fn(200,100)




def my_fn(a1,b1):
    print("testing2")
    print("a1--->",a1)
    print("b1--->",b1)
    c =a1+b1
    print(c)
    

a=200
b=100
my_fn(a,b)




def my_fn(a,b,c):
    print("testing2")
    print("a1--->",a)
    print("b1--->",b)
    print("c1--->",c)
    d =a+b+c
    print(d)
    

a=200
b=100
c=300
my_fn(b,a,c)






















