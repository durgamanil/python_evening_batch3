# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:42:36 2022

@author: durga
"""

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