# -*- coding: utf-8 -*-
"""
Created on Fri May 13 19:16:57 2022

@author: durga
"""

#multiple inheritance

class a:
    def __init__(self):
        print("this is default constructor for class A")
class b:
    """statements"""
    def __init__(self):
        print("this is default constructor for class b")
           
class c(b,a):
    """statements"""
    def __init__(self):
        b.__init__(self)
        a.__init__(self)
        print("this is default constructor for class c")
        
class d(c,b):
    def __init__(self):
        c.__init__(self)
        b.__init__(self)
        print("this is default constructor for class d")
    
d_obj = d()

#MRO---method resolution order
print(d.mro())