# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 07:34:19 2022

@author: durga
"""

# =============================================================================
# SET
# =============================================================================
#set is one of the datatype
#set  will also accept different datatypes
#no duplicates allowed
#different methods available
#unordered type


set---->

syntax:
    
    set1 ={1,2,3,4}
    
    
#example1
set1 ={1,2,3,4}
print(set1)
print(type(set1))
print(id(set1))

#example
set1 = {1,"meghana",14.5,True}
print(set1)
print(type(set1))



set1 = {1,2,2,3,5,4,1,3}
print(set1)


#checking the different methods

dir(set1)

['__and__',
 '__class__',
 '__class_getitem__',
 '__contains__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__iand__',
 '__init__',
 '__init_subclass__',
 '__ior__',
 '__isub__',
 '__iter__',
 '__ixor__',
 '__le__',
 '__len__',
 '__lt__',
 '__ne__',
 '__new__',
 '__or__',
 '__rand__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__ror__',
 '__rsub__',
 '__rxor__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__sub__',
 '__subclasshook__',
 '__xor__',
 'add',
 'clear',
 'copy',
 'difference',
 'difference_update',
 'discard',
 'intersection',
 'intersection_update',
 'isdisjoint',
 'issubset',
 'issuperset',
 'pop',
 'remove',
 'symmetric_difference',
 'symmetric_difference_update',
 'union',
 'update']



set1 = {"beer1","beer2","vodka1","vodka2","beer1","beer2","vodka1","vodka2"}
print(set1)


set1 = {"beer1","beer2","vodka1","vodka2",}
print(set1)

set1 = {"beer1","beer2","vodka1","vodka2",}
print(set1)
#print(set1[1])

print(set1[0])
#a = set1["beer1"]
#print(a)



set1 = {"255.255.255.0", "255.255.255.1", "255.255.255.0"}
print(set1)


set1 = {"apple", "banana", "cherry"}

print(len(set1))

#len functions
str1="apple"
print(len(str1))


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)


#accessing the elements 
set1 = {"apple", "banana", "cherry"}

for x in set1:
  print(x)
  
  
# 

set1 = {"apple", "banana", "cherry"}

print("banana" in set1)



#
thisset = {"apple", "banana", "cherry"}

print("orange" in thisset)




# =============================================================================
# 
# Method Description
# add() Adds an element to the set
# clear() Removes all the elements from the set
# copy() Returns a copy of the set
# difference() Returns a set containing the difference between two or more sets
# difference_update() Removes the items in this set that are also included in another, specified set
# discard() Remove the specified item
# intersection() Returns a set, that is the intersection of two other sets
# intersection_update() Removes the items in this set that are not present in other, specified set(s)
# isdisjoint() Returns whether two sets have a intersection or not
# issubset() Returns whether another set contains this set or not
# issuperset() Returns whether this set contains another set or not
# pop() Removes an element from the set
# remove() Removes the specified element
# symmetric_difference() Returns a set with the symmetric differences of two sets
# symmetric_difference_update() inserts the symmetric differences from this set and another
# union() Return a set containing the union of sets
# update() Update the set with the union of this set and others
# 
# 
# =============================================================================


set1 = {"apple", "banana", "cherry"}

set1.add("orange")

print(set1)

#clear method


set1 = {"apple", "banana", "cherry"}

set1.clear()
print(set1)

#copy method


set1 = {"apple", "banana", "cherry"}

set2 = set1.copy()
print(set1)
print(set2)

print(id(set1))
print(id(set2))



set1 = {"apple", "banana", "cherry"}

set2 = set1
print(set1)


set1.add("orange")
print(set1)
print(set2)

print(id(set1))
print(id(set2))

#difference method
set1 = {"apple", "banana", "cherry"}
set2 = {"apple","orange","cherry"}

print(set2.difference(set1))
print(set1)
print(set2)

set1 = {"apple", "banana", "cherry"}
set2 = {"apple","orange","cherry"}

print(set1.difference(set2))

print(set1)
print(set2)

#difference_update

set1 = {"apple", "banana", "cherry"}
set2 = {"apple","orange","cherry"}

set1.difference_update(set2)#update the elements into the same set

print(set1)
print(set2)


set1 = {"apple", "banana", "cherry"}
set2 = {"apple","orange","cherry"}

set2.difference_update(set1)#update the elements into the same set

print(set1)
print(set2)


#union method
set1 = {"apple", "banana", "cherry"}
set2 = {"apple","orange","cherry"}

print(set1.union(set2))
#print(set1)
#print(set2)

#intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"apple","orange","cherry"}

print(set1.intersection(set2))
print(set2.intersection(set1))
print(set1)
print(set2)


#intersection_update

set1 = {"apple", "banana", "cherry"}
set2 = {"apple","orange","cherry"}

set1.intersection_update(set2)
print(set1)
print(set2)
#===============================
set1 = {"apple", "banana", "cherry"}
set2 = {"apple","orange","cherry"}

set2.intersection_update(set1)
print(set1)
print(set2)


#pop() Removes an element from the set
set1 = {"apple", "banana", "cherry"}
print(set1)
set1.pop()
print(set1)
set1.pop()
print(set1)
set1.pop()
print(set1)

# remove() Removes the specified element
set1 = {"apple", "banana", "cherry"}
set1.remove("apple")
print(set1)
set1.remove("banana")
print(set1)
set1.remove("cherry")
print(set1)



#


s1 ={1,2,3,4}
s2 = {3,4,5,6}

print(s1,s2)
print("intersection o/p",s1.intersection(s2))
print("after intersecion",s1,s2)




s1 ={1,2,3,4}#====>{3,4}
s2 = {3,4,5,6}
print("before",s1,s2)
s1.intersection_update(s2)
print("after intersecion",s1,"\n",s2)



#
s1 ={1,2,3,4}#====>{3,4}
s2 = {3,4,5,6}
print("before",s1,s2)
s2.intersection_update(s1)
print("after intersecion",s1,"\n",s2)


#symmetic_difference

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(x)
print(y)
print("="*30)
z = y.symmetric_difference(x)
print(z)
print("="*30)
print("after",x,y)



x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(x)
print(y)
print("="*30)
z = x.symmetric_difference(y)
print(z)
print("="*30)
print("after",x,y)







x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(x)
print(y)
print("="*30)
x.symmetric_difference_update(y)
print("x===>",x)
print("="*30)
print("after y=====>",y)



#
a =10
b =20
c =a+b

print(c)
-----------------------


a = a+b
print(a)
------------------
a =10
b =20
b = a+b
print(b)
---------------------------




# Python program to demonstrate working of
# issubset().

A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}

# Returns True
print(A.issubset(B))

# Returns False
# B is not subset of A
print(B.issubset(A))





A = {4, 1,7, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}

# Returns True
print(A.issubset(B))

# Returns False
# B is not subset of A
print(B.issubset(A))



#Discard method ======> to delete the particular element
A = {4, 1,7, 3, 5}
print(A.discard(4))
print(A)

print(A.discard(5))
print(A)


A = {4, 1,7, 3, 5}
print(A.discard(5))
print(A)



#isdisjoint() Returns whether two sets have a intersection or not


A = {1,2,3}
B = {1,2,3,5,6}

c = A.isdisjoint(B)

print(c)
print(A)
print(B)


# =============================================================================
# 
# =============================================================================
A = {1,2,3}
B = {4,5,6}

c = A.isdisjoint(B)

print(c)
print(A)
print(B)


#interview 
Q1: how to convert list to set
#ans:
a = [1,2,3,4]
b = set(a)
print(b)
print(type(b))


Q2:
a = {2,3}
b = {1,2,3,4,5}

print(a.issubset(b))#True

print(b.issubset(a))#False


Q3:
a = {2,3}
b = {1,2,3,4,5}
a <= b


Q4:
   
a = {2,3}
print(a.issubset(a))#True

Q5:
    
b = {1,2,3,4,5}

1 is not in b

1 is in b

Q6:
    
b = {'a','b','c'}

print('a' not in b)



#
print("beer"*10)
print(10*10)



























