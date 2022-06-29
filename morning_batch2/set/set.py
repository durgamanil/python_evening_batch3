# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 08:07:08 2022

@author: durga
"""

# =============================================================================
# Set
# =============================================================================
#set is also one of the advanced data types
#it will also store multiple values in single variable
#it will not accept duplicates
#set is unordered----->you can't call with indexes

syntax:
    set1 ={variable1,var2,var3}
    
example1:

set1 = {1,2,3,4,5}
print(set1)
print(type(set1))

set2 = {1,2,3,4,1,2,3,5,7,8,9}
print(set2)

set3 = {"mahesh","ramesh","mukesh"}
print(set3)


set3 = {"mahesh","ramesh","mukesh","mahesh"}
print(set3)

#using for loop

set3 = {"mahesh","ramesh","mukesh","mahesh"}
print(set3)
for i in set3:
    print(i)
    

ips = {"186.0.0.1","186.0.0.2","186.0.0.3","186.0.0.1"}
print(ips)


#len of the set
set3 = {"mahesh","ramesh","mukesh"}
print(set3)
print(len(set3))

set3 = {"mahesh","ramesh","mukesh","mahesh"}
print(set3)  
print(len(set3))  

set1 ={1,2,3,4,5}
set2 =  {"mahesh","ramesh","mukesh"}
set3 = {True,False,True,False}
print(set1)
print(set2)
print(set3)
    
#mixed data types

set4  = {1,2,3,True,"mahesh","ramesh","rupesh",17.6,18.4,False}   
print(set4)   
    
#tuple to set convert
#constructor

tuple1 = (1,2,3,4,5,4,5)
print(tuple1)

set1 = set(tuple1)
print(set1)

#access the elements
set1 ={1,2,3,4,5}
for i in set1:
    print(i)
    

#member ship operator

set1 ={1,2,3,4,5}
print(1 in set1)

#different methods
dir(set1)
['__and__', '__class__', '__class_getitem__',
 '__contains__', '__delattr__',
 '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__gt__',
 '__hash__', '__iand__',
 '__init__', '__init_subclass__',
 '__ior__', '__isub__', '__iter__', '__ixor__',
 '__le__', '__len__', '__lt__', '__ne__',
 '__new__', '__or__', '__rand__', '__reduce__',
 '__reduce_ex__', '__repr__', '__ror__', '__rsub__',
 '__rxor__', '__setattr__', '__sizeof__', '__str__',
 '__sub__', '__subclasshook__', '__xor__', 'add',
 'clear', 'copy', 'difference', 'difference_update',
 'discard', 'intersection', 'intersection_update',
 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove',
 'symmetric_difference', 'symmetric_difference_update',
 'union', 'update']
    

#set is mutable
set1 ={1,2,3,4,5}
print(set1)

#add method
set1.add(6)
print(set1)


set2 =  {"mahesh","ramesh","mukesh"}
print(set2)
set2.add("rupeesh")
print(set2)


#clear method will remove the all the elements

set1 ={1,2,3,4,5}
print(set1)
set1.clear()
print(set1)

Note:
{}---->dictionary
set()------>empty set


#copy method will create the extra copy

set1 ={1,2,3,4,5}
print(set1)
set5 = set1.copy()
print(set1)
print(set5)

print(id(set1))
print(id(set5))



#update

set1 =  {"mahesh","ramesh","mukesh"}
set2 =  {"roopa","deepa","moopa"}

print(set1)
print(set2)

set1.update(set2)

print(set1)
print(set2)


set1 =  {"mahesh","ramesh","mukesh"}
set2 =  {"roopa","deepa","moopa"}

print(set1)
print(set2)

set2.update(set1)

print(set1)
print(set2)


#
set1 =  {"mahesh","ramesh","mukesh"}
list1 =  ["roopa","deepa","moopa"]

print(set1)
print(list1)

set1.update(list1)
print(set1)
print(list1)


#pop method
set1 =  {"mahesh","mukesh","ramesh"}

set1.pop()#dnot use
print(set1)


#remove method

set1 =  {"mahesh","mukesh","ramesh"}

set1.remove("mahesh")
print(set1)

set1 =  {"mahesh","mukesh","ramesh"}

set1.remove("mukesh")
print(set1)



























    
    
    
    
    
    
    
    
    