# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 23:55:25 2022

@author: durga
"""

class DemoClass:
    num = 101

    # parameterized constructor
    def __init__(self, data):
        print("===============")
        self.num = data

    # a method
    def read_number(self):
        print(self.num)


# creating object of the class
# this will invoke parameterized constructor
obj = DemoClass(55)

# calling the instance method using the object obj
obj.read_number()

# creating another object of the class
obj2 = DemoClass(66)

# calling the instance method using the object obj
obj2.read_number()