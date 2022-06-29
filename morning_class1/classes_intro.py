# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 06:54:23 2022

@author: durga
"""

# syntax : class class_name():
#             variable declarations
#             init method
#             other methods(def)


# =============================================================================
# with out parenthesis
# =============================================================================

# class my_class1:
#     print("inside class myclass1")  

# my_class1()   

# =============================================================================
# passing the class
# =============================================================================
# class my_class1:
#     pass

# my_class1()   

# =============================================================================
# doc string
# =============================================================================
# class my_class1:
#     """this is general class
#         here we are doing mathematical operations"""

# my_class1.__doc__


     
            
# class my_class():
#     a = 10
#     print("inside class",a)
    

# my_class()


# class my_class():
#     a = 10
#     print("inside class",a)
    
#     def fun1():
#         print("this is inside class method")
        
#     fun1()
    

# my_class()



# =============================================================================
# type checking
# =============================================================================
# class my_class():
#     a = 10
#     print("inside class",a)
    
#     def fun1():
#         print("this is inside class method")
        
#     fun1()
    

# my_class()

# print(type(my_class()))


# =============================================================================
# accessing method outside
# =============================================================================
# class my_class():
#     a = 10
#     print("inside class",a)
    
#     def fun1():
#         print("this is inside class method")
        
#     #fun1()
    

# fun1()


# =============================================================================
# 
# =============================================================================

# class my_class():
#     a = 10
#     print("inside class",a)
    
#     def fun1():
#         print("this is inside class method")
        
#     #fun1()
    

# my_class.fun1()

# =============================================================================
# string slicing
# =============================================================================

# str1 = "this is testing string"

# str1[5:10]

# len(str1)


# =============================================================================
# 
# =============================================================================

# class my_class():
#     a = 10
#     print("inside class",a)
    
#     def fun1():
#         print("this is inside class method")
        
#     #fun1()
    

# #print(my_class.fun1)

# print(id(my_class.fun1))

# print(id(my_class))


class my_class:
    a = 10
    print("inside class",a)
    
    def fun1(self):
        print("this is inside class method",self.a)
        
    def fun2(self):
        print("this is inside class method2",self.a)
    

#print(my_class.fun1)

# var1 = my_class()

# var1.fun1()
# var1.fun2()

my_class().fun1()
my_class().fun2()







