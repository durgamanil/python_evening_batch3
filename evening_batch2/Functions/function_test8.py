# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 20:01:20 2022

@author: durga
"""

# =============================================================================
# nested functions 
# =============================================================================

def function2():
    function1()
    

def function1():
    print("this is fun1")
    #function2()
    

function2()





# =============================================================================
# nested function
# =============================================================================



   
    

def outer_fun():
    print("this is outer function")
    #function2()
    
    def inner_fun():
        print("this is inner function")
        
        
    inner_fun()
    

outer_fun()






def outer_fun():
    print("this is outer function")
    #function2()
    
    def inner_fun():
        print("this is inner function")
        
        
    def inner_fun2():
        print("this is inner function2")
        
        
    inner_fun2()
    inner_fun()
    

outer_fun()



def outer_fun():
    print("this is outer function")
    #function2()
    
    def inner_fun():
        print("this is inner function")
        
        
        def inner_fun2():
            print("this is inner function2")
        
        
        inner_fun2()
        
    inner_fun()
    

outer_fun()




























