# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 08:05:35 2022

@author: durga
"""

list1 = ["orange","lemon","grapes","banana"]
print(list1)

print(id(list1))#address of the list
#nesting

list inside another list is called nesting

list1 = ["orange","lemon","grapes","banana",["rose","lilli","lotus"]]

print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list1[4][0])
print(list1[4][1])
print(list1[4][2])

#list inside list, list inside another list
list1 = [["rose","lilli","lotus"],"orange","lemon","grapes","banana"]

print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

print(list1[0][1])
print(list1[0][2])
print(list1[0][0])


list1 = [["rose","lilli","lotus"],"orange",["lemon","mango","popaya"],"grapes","banana"]


print(list1[0][1])
print(list1[0][2])
print(list1[0][0])

print(list1[2])
print(list1[2][0])
print(list1[2][1])
print(list1[2][2])


list1 = [["rose","lilli","lotus"],"orange",["lemon","mango","popaya",["royalstag",600,"vodka",700]],"grapes","banana"]

print(list1[2])

print(list1[2][0])
print(list1[2][3])

print(list1[2][3][2])
print(list1[2][3][0])
print(list1[2][3][1])
print(list1[2][3][3])


list1 = ["orange","lemon","grapes","banana"]
for i in list1:
    print(i)
    
    
list1 = ["orange","lemon","grapes","banana"]
for i in range(0,len(list1)):
    print(list1[i])

#aliasing
list1 = ["orange","lemon","grapes","banana"]
#as---keyword
#list1 as l1

list2 = list1

print(list1)
print(list2)

print(id(list1))
print(id(list2))

list2.append("mango")
print(list2)
print(list1)

#sending list to functions
def fun1(a):
    print(a)
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    print(a[4])
    
    
a = [1,2,3,4,5]
fun1(a)


def fun1(a):
    print(a)
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])
    
 
a = ["orange","lemon","grapes","banana"]
fun1(a)
    


#string to list
a = "banana"
print(type(a))
list3 =[]#empty list
for i in a:
    #print(i)
    list3.append(i)
    
print(list3)
print(type(list3))



a = "india is the best country"
print(type(a))
list3 =[]#empty list
for i in a:
    #print(i)
    list3.append(i)
    
print(list3)
print(type(list3))
print(list3[5])
print(list3[4])


#casting ----->converting 

tup1 = (1,2,3,4,5)
print(tup1)
print(type(tup1))

list4 = list(tup1) #type casting
print(list4)
print(type(list4))

# ex2

list4 = list((1,2,3,4,5)) #type casting
print(list4)
print(type(list4))

#methods of the list
dir(list1)

['__add__', '__class__',
 '__class_getitem__', '__contains__',
 '__delattr__', '__delitem__',
 '__dir__', '__doc__',
 '__eq__', '__format__',
 '__ge__', '__getattribute__',
 '__getitem__', '__gt__', '__hash__', '__iadd__',
 '__imul__', '__init__', '__init_subclass__', '__iter__',
 '__le__', '__len__', '__lt__', '__mul__', '__ne__',
 '__new__', '__reduce__', '__reduce_ex__', '__repr__',
 '__reversed__', '__rmul__', '__setattr__', '__setitem__',
 '__sizeof__', '__str__', '__subclasshook__',
 'append', 'clear', 'copy', 'count', 'extend',
 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

list1 = ["orange","lemon","grapes","banana"]
list2 = list1.copy()

print(list1)
print(id(list1))

print(list2)
print(id(list2))

list2.append("jackfroot")
print(list2)
print(list1)


