# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 19:36:22 2022

@author: durga
"""

#tuple---advanced data type in python

syntax----()

tuple1 =(1,2,3)

print(tuple1)
print(type(tuple1))


dir(tuple1)

#different types of tuples

a =(1,2,3,4,5)----->integer type tuple

a = (12.9,13.4,56.9)-----> float type tuple

a = ("appy","vodka","beer")----->string type tuple



a =(1,2,3,4,5)
print(a)
print(type(a))


a = (12.9,13.4,56.9)
print(a)
print(type(a))


a = ("appy","vodka","beer")
print(a)
print(type(a))

a = ("appy","vodka","beer",1,2,3.2,True)
print(a)
print(type(a))


a.append("tc")
print(a)
print(type(a))


#insert method also not works
a = ("appy","vodka","beer",1,2,3.2,True)
print(a)

a.insert(0,"tc")
print(a)
print(type(a))


dir(tuple)

#interview question
a = ("appy","vodka","beer",1,2,3.2,True)

b = list(a)

print(a)
print(b)

print(type(a))
print(type(b))

b.append(30)
print(b)
print(type(b))

a = tuple(b)
print(a)
print(type(a))


a = ("appy","vodka","beer",1,2,3.2,True)

b = list(a)
b.append(30)
a = tuple(b)
print(a)
print(type(a))

#indexing
a = ("appy","vodka","beer",1,2,3.2,True)
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

print(a[6])


print(a[0:2])

print(a[0:5])
print(a[0:7])



print(a[10])


print(a[-1])
print(a[-5])


print(a[-1:-5])













