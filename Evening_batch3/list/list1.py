# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 20:20:20 2022

@author: durga
"""

# =============================================================================
# list
# =============================================================================

#list is also a variable which will store multiple values
#is mutable..on runtime you can add, append del, remove
#list follow the index

syntax:
    list----keyword
    l1 = [1,2,3,4] #this is list
    
examples:
    
    
list1 = [1,2,3,4]
print(list1)
#type
print(type(list1))

#memory location
print(id(list1))

#methods
# to check the methods you need pass your list variable
#in dir() function

dir(list1)
['__add__', '__class__', '__class_getitem__',
 '__contains__', '__delattr__',
 '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__getitem__',
 '__gt__', '__hash__',
 '__iadd__', '__imul__',
 '__init__', '__init_subclass__', '__iter__',
 '__le__', '__len__',
 '__lt__', '__mul__',
 '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__',
 '__reversed__', '__rmul__',
 '__setattr__', '__setitem__',
 '__sizeof__', '__str__', '__subclasshook__',
 'append',
 'clear',
 'copy',
 'count',
 'extend',
 'index',
 'insert',
 'pop',
 'remove',
 'reverse',
 'sort']

#passing different datatypes in the list

#interger

list1 = [1,2,3,4,5,6]
print(list1)

#string types
list2 = ["robin","shailaja","nadeesh","mukesh"]
print(list2)

#list follow the order
#float type
list3 = [12.3,14.7,55.2,128.12]
print(list3)

#boool type

list4 = [True,False,True,False]
print(list4)

#mixed type list
list5 = [1,"apple",True,17.8,"yellow",False]
print(list5)

#indexing
list2 = ["robin","shailaja","nadeesh","mukesh"]
print(len(list2))
print(list2)
print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])

#reverse index
print(list2[-1])
print(list2[-2])
print(list2[-3])
print(list2[-4])

#for loops
for element in list2:
    print(element)
    
for index in range(0,len(list2)):
    print(list2[index])   
    
    
#slicing
syntax:
    [start index: end index]

list2 = ["robin","shailaja","nadeesh","mukesh"]
list2[0:1]
list2[0:4]

list2[0:2]

list2[0:3]

list2[-1:-3]
list2[-3:-1] #this order

#methods of the list

#append', this method will add the element to existing list
list2 = ["robin","shailaja","nadeesh","mukesh"]
print(list2)
list2.append("mahesh")
print(list2)

list3 = [1,2,3,4,5]
print(list3)
list3.append(6)
print(list3)




#'clear',--->this method will clear the total elements from list
list3 = [1,2,3,4,5]
print(list3)
list3.clear()
print(list3)

#empty list
list2 = []
print(list2)
print(type(list2))

list2 = ["robin","shailaja","nadeesh","mukesh"]
print(list2)
list2.clear()
print(list2)

#'copy',----will create the extra copy
list1 = [1,2,3,4,5]
list2 = list1
print(list1)
print(list2)
print(id(list1))
print(id(list2))

list1.append(6)
print(list1)
print(list2)
print(id(list1))
print(id(list2))

#copy
list1 = [1,2,3,4,5]
list2 = list1.copy()
print(list1)
print(list2)
print(id(list1))
print(id(list2))

list1.append(6)
print(list1)
print(list2)
print(id(list1))
print(id(list2))


#'count',---number of the elements existing...similar elements
list1 = ["robin","shailaja","nadeesh","mukesh","robin","shailaja"]
print(list1.count("robin"))
print(list1.count("nadeesh"))
print(list1.count("shailaja"))

#'extend', this method will add iterable object..like list
list1 = ["robin","shailaja","nadeesh","mukesh"]
list2 = [1,22,3,44,5,4,12]
print(list1)
list1.extend(list2)
print(list1)
print(list2)

#'index',----index postion it will return
list1 = ["robin","shailaja","nadeesh","mukesh"]
print(list1)
print(list1.index("robin"))
print(list1.index("shailaja"))
print(list1.index("mukesh"))
print(list1.index("nadeesh"))

#'insert',----->it will insert whereever you want
list1 = ["robin","shailaja","nadeesh","mukesh"]
print(list1)
list1.insert(1, "mahesh")
print(list1)
list1.insert(2, "roopesh")
print(list1)



#'pop',

list1 = ["robin","shailaja","nadeesh","mukesh"]
print(list1)
list1.pop()
print(list1)

#'remove',---need to pass the element name
list1 = ["robin","shailaja","nadeesh","mukesh"]
print(list1)
list1.remove("robin")
print(list1)
#'reverse',----reverse the elements
list1 = [1,2,3,4,5]
print(list1)
list1.reverse()
print(list1)

#'sort']
#
list1 = [1,22,3,44,5,4,12]
print(list1)
list1.sort()
print(list1)














    
