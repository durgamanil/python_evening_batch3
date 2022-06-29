# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 20:21:11 2022

@author: durga
"""
# =============================================================================
# identity operator
# =============================================================================
#1.is
#2.is not


# 1.is---->return true if both variable are object

list1 = ["orange","banana"]
list2 = ["orange","banana"]

list3 = list1

print(list1)
print(list2)

print(id(list1))

print(id(list3))
print(id(list2))

print(list1 is list3)

print(list1 is list2)
print(list3 is list2)


#2.is not
#return true if both variable object are diffrent
#return false if both variables objects are same


list1 = ["orange","banana"]
list2 = ["orange","banana"]

list3 = list1

print(list1)
print(list2)
print(list1 is not list3)

print(list1 is not list2)

print(list3 is not list2)



