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




