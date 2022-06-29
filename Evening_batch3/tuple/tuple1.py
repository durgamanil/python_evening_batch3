# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 20:07:38 2022

@author: durga
"""

# =============================================================================
# Tuple
# =============================================================================
#tuple immutable
#tuple---constructor
#ordered

syntax:
    tuple1 = (1,2,3,4,5)
    
    
tuple1 = (1,2,3,4,5)
print(tuple1)
print(type(tuple1))

#len of the tuple

print(len(tuple1))

tuple2 = (22,33,45)
print(len(tuple2))


#methods of the tuple
#dir()

dir(tuple2)

['__add__', '__class__', '__class_getitem__',
 '__contains__', '__delattr__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__getitem__',
 '__getnewargs__', '__gt__',
 '__hash__', '__init__', '__init_subclass__',
 '__iter__', '__le__', '__len__', '__lt__',
 '__mul__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__',
 '__rmul__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__',
 'count',
 'index']


#how to fetch the elements from the tuple

tuple1 = (1,2,3,4,5)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])
print(tuple1[4])

#tuple negative/reverse index

tuple1 = (1,2,3,4,5)
print(tuple1[-5])
print(tuple1[-4])
print(tuple1[-3])
print(tuple1[-2])
print(tuple1[-1])

# passing to for looops
for i in tuple1:
    print(i)
    
    
for i in range(0,len(tuple1)):
    print(tuple1[i])
    
    
tuple1 = ("Sony","MI","LG","SAMSUNG","Realme")
print(tuple1[-5])
print(tuple1[-4])
print(tuple1[-3])
print(tuple1[-2])
print(tuple1[-1])


#count
tuple1 = ("Sony","MI","LG","SAMSUNG","Realme")

print(tuple1.count("Sony"))


tuple1 = ("Sony","MI","LG","SAMSUNG","Realme","Sony","sony")

print(tuple1.count("Sony"))


#index method
tuple1 = ("Sony","MI","LG","SAMSUNG","Realme","Sony","sony")

print(tuple1.index("MI"))


tuple1 = ("Sony","MI","LG","SAMSUNG","Realme","Sony","sony")

print(tuple1.index("sony"))


tuple1 = ("Sony","MI","LG","SAMSUNG","Realme","Sony","sony")

print(tuple1.index("Sony"))

#how to add element to list
tuple1.append("vue")
tuple1.insert(0,"vue")


tuple1 = ("Sony","MI","LG","SAMSUNG","Realme","Sony","sony")

list1 = list(tuple1)
print(list1)

list1.append("bajaj")
print(list1)
tuple1 = tuple(list1)

print(tuple1)

#nested tuples

tuple2  = (1,2,3,"apple",12.9,True)
print(tuple2)

#nesting
tuple2  = (1,2,3,"apple",12.9,True,(5,6,7))

print(tuple2)
print(tuple2[6])
print(tuple2[6][0])

#slicing
tuple2  = (1,2,3,"apple",12.9,True,(5,6,7))

print(tuple2[:])











    
    
    
    

    
























