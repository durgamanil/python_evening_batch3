# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 08:55:04 2022

@author: durga
"""

# =============================================================================
# identity operators 
# =============================================================================


#is---> keyword

list1 = ["banana","mango"]
list2 = ["banana","mango"]

list3 = list1

print(id(list1))
print(id(list2))
print(id(list3))

print(list1)
print(list3)

print(list3 is list1)#True

print(list2 is list3)#False

print(list1 == list2)


#is not operator

print(list3 is not list1)#False

print(list2 is not list3)# True







