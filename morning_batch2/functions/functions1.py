# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 08:11:09 2022

@author: durga
"""

# =============================================================================
# functions
# =============================================================================

print("this is testing")
print("this is testing1")
print("this is testing2")
print("this is testing3")
print("this is testing4")
print("this is testing5")


print("this is testing")
print("this is testing1")
print("this is testing2")
print("this is testing3")
print("this is testing4")
print("this is testing5")




def is the keyword:

to create functions we will use def keyword

syntax:
    def function_name(args):#function defination
        """statements"""
        
        to call this function
        function_name()
        

example1:
    
def greeting():
    print("Good morning")  


print("from here your main function")
greeting()  


example2:
    
def greeting():#Zero arguments based function
    print("Good morning")  
    print("this is inside function")


print("from here your main function")
greeting()  

#type  
print(type(greeting()))
print(type(greeting))

#one argument
def greeting(a):#Zero arguments based function
    print("Good morning")  
    print("this is inside function")
    a+=1
    print(a)
   


print("from here your main function")
greeting(1)  

#string arguments
def greeting(name):#Zero arguments based function
    print("Good morning "+name)  
    
print("from here your main function")
greeting("ramcharan") 

#id

def greeting(name):#Zero arguments based function
    print("Good morning "+name)  
    
print("from here your main function")
greeting("ramcharan") 
print(id(greeting))

#methods
def greeting(name):#Zero arguments based function
    print("Good morning "+name)  
    
print("from here your main function")
greeting("ramcharan") 
dir(greeting)
['__annotations__', '__call__', '__class__', '__closure__',
 '__code__', '__defaults__', '__delattr__',
 '__dict__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__',
 '__get__', '__getattribute__',
 '__globals__', '__gt__',
 '__hash__', '__init__', '__init_subclass__',
 '__kwdefaults__', '__le__',
 '__lt__', '__module__', '__name__',
 '__ne__', '__new__', '__qualname__',
 '__reduce__', '__reduce_ex__',
 '__repr__', '__setattr__',
 '__sizeof__', '__str__', '__subclasshook__']

#docstring

def greeting(name):#Zero arguments based function
    """===============
    This function will greet the person
    ======================="""
    print("Good morning "+name)  
    """===============
    This function will greet the person
    ======================="""
    
print("from here your main function")
greeting("ramcharan") 
print(greeting.__doc__)

#input function 
def greeting(name):#Zero arguments based function
    """
    This function will greet the person
    """
    print("Good morning "+name)  
    """===============
    This function will greet the person
    ======================="""
    
a = input("enter your name")
greeting(a) 
print(greeting.__doc__)















 
        
        
        
        
        
        