# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 06:54:56 2022

@author: durga
"""

def decorator_fun(func_to):
    #print("Inside decorator")

    def inner(*args, **kwargs):
        print("Inside inner function")
        print("Decorated the function")
        # do operations with func
        func_to()
    return inner

@decorator_fun
def func_to():
 	print("Inside actual function")



if __name__ == '__main__' :
    func_to()
    #pass