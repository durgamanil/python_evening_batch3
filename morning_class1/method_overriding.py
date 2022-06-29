# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 07:18:36 2022

@author: durga
"""

class Animal:  
    def speak(self):  
        print("speaking")
        
class Dog(Animal):  
    def speak(self):  
        print("Barking")  
        
        
d = Dog()  
d.speak()  