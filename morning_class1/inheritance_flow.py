# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 07:26:27 2022

@author: durga
"""

# class A:
#     def __init__(self):
#         print("cursor comes here first")
        
        
        
# class B(A):
#     def __init__(self):
#         print("This is default constructor of B")
#         A.__init__(self)
 
        

# ab = B()
# print(ab)





# class A:
#     def __init__(self):
#         print("1 cursor comes here first")
        
#     def house(self):
#         print("2 this is class A house")
        
        
# class B(A):
#     def __init__(self):
#         print("3 This is default constructor of B")
#         A.__init__(self)
        
        
# class C(B):
#     def __init__(self):
#         print("4 This is default constructor of C")
#         B.__init__(self)
        
        

# ab = C()
# ab.house()
# #print(ab)


class X:
    def __init__(self):
        print("1 cursor comes here first")
        
    def house(self):
        print("2 this is class A house")
        
class Y:
    def __init__(self):
        print("3 cursor comes here first")
        
    def house(self):
        print("4 this is class A house")
        
class Z:
    def __init__(self):
        print("5 cursor comes here first")
        
    def house(self):
        print("6 this is class A house")
        
        
class B(X,Y):
    def __init__(self):
        print("7 This is default constructor of B")
        X.__init__(self)
        Y.__init__(self)
        
        
class C(B,Z):
    def __init__(self):
        B.__init__(self)
        print("8 This is default constructor of C")
        Z.__init__(self)        
        

ab = C()
ab.house()
#78654321
#87135246
#print(C.mro())














