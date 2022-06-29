# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 08:03:02 2022

@author: durga
"""

# =============================================================================
# advanced datatypes
# =============================================================================
1.List
2.tuple
3.dictionary
4.Set


#list----collection of different datatypes and similary datatypes also you store

syntax: 
    list1 = []
    list is the key word so dnot use that for variable
    
    list2 = [1,2,3,4,5]
    list3 = ["mango","apple","popaya"]
    list4 = [True,False,True]
    list5 = [12.3,16.4,56.5]
    list6 = [1,"raju",12.5,True]
    

    
list2 = [1,2,3,4,5]
print(list2)
print(type(list2))
print(len(list2))

print(list2[0])
print(list2[1])
print(list2[2])
print(list2[3])
print(list2[4])
#negative index
print(list2[-1])
print(list2[-2])
print(list2[-3])
print(list2[-4])
print(list2[-5])

print(list2[100])

print(list2[-6])

for i in list2:
    print(i)

for i in range(0,len(list2)):
    print(list2[i])
    
print("before list2",list2)
list2.append(2)
print("after append list2",list2)

#in the list duplicates are allowed

list-----constructor

tup1 = ("ramesh","suresh","mahesh")
# print(tup1)
# print(type(tup1))

list2 = list(tup1)

print(list2)
print(type(list2))

# =============================================================================
# ranges
# =============================================================================
list3 = ["mango","apple","popaya","mango","apple","popaya"]
list3[0:1]

#ist3[start:stop:step]
#stop====>stop-1

list3[0:6]

list3[2:5]

list3[:5]


#negative index
list3[-5:-1]

# membership operator

list3 = ["mango","apple","popaya","mango","apple","banana"]

if "banana" in list3:
    print("yes that element is available")


#changing the elements from the list
print
print(list3)
list3[0] ="orange"
print("after ",list3)




list3 = ["mango","apple","popaya"]
print(list3)
print(type(list3))
print(len(list3))

#insert mehtod
#this method will insert the element at particular index

syntax:
    yourlist.insert(index,"element name")
    
list3.insert(2, "pineapple")
print(list3)
list3.insert(5, "lemon")
print(list3)

list3.insert(100,"sapota")
print(list3)

print(list3[100])



list3 = ["mango","apple","popaya","sapota"]
list3.pop()
print(list3)

#remove method
list3 = ["mango","apple","popaya","sapota"]
list3.remove("sapota")

print(list3)

list3 = ["mango","apple","popaya","sapota"]
list3.remove("apple")

print(list3)

#sort method
list4 = [4,7,6,10,40,9,3]
print(list4)
list4.sort()
print(list4)

#clear

#clear method will clear the all the elements from the given list

list4 = [4,7,6,10,40,9,3]
print(list4)
list4.clear()
print(list4)


#del keyword

#using del keyword you can remove complete list

list4 = [4,7,6,10,40,9,3]
print(list4)
del list4
print(list4)

#reverse method
#it will reverse the given list

list4 = [4,7,6,10,40,9,3]
print(list4)
list4.reverse()
print(list4)



list4 = [True,False,True]
print(list4)
print(type(list4))
print(len(list4))




list5 = [12.3,16.4,56.5]
print(list5)
print(type(list5))
print(len(list5))





list6 = [1,"raju",12.5,True]
print(list6)
print(type(list6))
print(len(list6))

print(id(list6))
    
    