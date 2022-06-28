# -*- coding: utf-8 -*-
"""
Created on Thu May  5 19:14:11 2022

@author: durga
"""


# def myfun():
#     "statement"
    
    
    
#syntax 1:
class class_name:
    "statement"
    
    
#syntax 2:    
class class_name():
    "statement"
   
    
   
    
   
# =============================================================================
#   
# =============================================================================

class fun_class:
    x = 20
    #print(x)
    
    
a = fun_class()
print(a.x)


# =============================================================================
# 
# =============================================================================
class fun_class:
    x = 20
    y =30
    #print(x)
    
    
a = fun_class()
print(a.x)
print(a.y)

var1 = a.x
var2 = a.y

print("var1",var1)
print("var2",var2)



# =============================================================================
# doc string
# =============================================================================

class fun_class:
    """
        this is the class 
        just calculate the values
    """
    x = 20
    y =30
    #print(x)
    
    
a = fun_class()


print(a.__doc__)




# =============================================================================
# methods of the class
# =============================================================================

dir(a)
Out[6]: 
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'x',
 'y']


# =============================================================================
# default constructor
# =============================================================================

class student:
    #this is method
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
a1 = student("sohan",20)
print(a1.name)
print(a1.age)


#this is function
# def my_fun(a,b):

#     num1  = a
#     num2 = b
#     print(num1,num2)
    
    
# my_fun(10,20)





# def my_fun(a,b):

#     a  = b
#     b = a
#     print(a,b)
    
    
# my_fun(10,20)


# =============================================================================
# accessing variable outside the class
# =============================================================================
class student:
    #this is method
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
a1 = student("sohan",20)
print(a1.name)
print(a1.age)




# =============================================================================
# accessing variables inside the class
# =============================================================================

class student:
    #this is method
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display(self):
        print(self.name)
        print(self.age)
        
        
a1 = student("sohan",20)
a1.display()


# =============================================================================
# change self name
# =============================================================================

class student:
    #this is method
    def __init__(vandana,name,age):
        vandana.name = name
        vandana.age = age
        
    def display(vandana):
        print(vandana.name)
        print(vandana.age)
        
        
a1 = student("sohan",20)
a1.display()


# =============================================================================
# without using self keyword
# =============================================================================

class student:
    #this is method
    def __init__(name,age):
        name = name
        age = age
        
    # def display():
    #     print(name)
    #     print(age)
        
        
a1 = student("sohan",20)
#a1.display()


# =============================================================================
# 
# =============================================================================

class student:
    #this is method
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def display(self):
        print(self.name)
        print(self.age)
        
    def test(self):
        print("this is yet another method")
        
        
a1 = student("sohan",20)
a1.display()
#a1.test()



