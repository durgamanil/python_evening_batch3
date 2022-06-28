# -*- coding: utf-8 -*-
"""
Created on Wed May 18 19:52:37 2022

@author: durga
"""
ABCs
---------
abstract base classes


import abc

class food(abc.ABC):
    @abc.abstractmethod
    def taste(self):
        print("this is testing")

class fast_food(food):
    def taste(self):
        print("tasty in fastfood")
    
a_obj = fast_food()
print(isinstance(a_obj, food))



#example2


import abc

class myclass(abc.ABC):
    @abc.abstractmethod
    def calling(self):
        print("this is calling method")
    
class room(myclass):
    def calling(self):
        print("this is testing")
        
        
        
a_obj = room()
print(isinstance(a_obj, test))



