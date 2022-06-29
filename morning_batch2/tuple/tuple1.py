# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 08:04:23 2022

@author: durga
"""

# =============================================================================
#  Tuple
# =============================================================================
#tuple also accept diffrent data types
#ex: str,int,float,mix type
#run time adding element is not possible, this called immutable 

syntax:
    tuple1 = (element1,element2,element3)
    
ex:

tuple1 = ("ramesh","suresh","mahesh")
print(tuple1)
print(type(tuple1))

#they will be in ordered,if we want access the elements we can use the index
tup1 = ("ramesh","suresh","mahesh")
print(tup1[0])
print(tup1[1])
print(tup1[2])


#it will allow duplicates
tup1 = ("ramesh","suresh","mahesh","suresh")
print(tup1)
print(tup1[0])
print(tup1[1])
print(tup1[2])
print(tup1[3])

#len function will give the length of the tuple

tup1 = ("ramesh","suresh","mahesh","suresh")
print(tup1)

print(len(tup1))


#integer type

tup1 = ("ramesh","suresh","mahesh","suresh")
print(tup1)
print(type(tup1))


tup2 = (1,2,3,4,5)
print(tup2)
print(type(tup2))


tup3 = (12.3,22.5,33.6,54.7,5.9)
print(tup3)
print(type(tup3))

tup4 = (True,False,False,True)
print(tup4)
print(type(tup4))

tup5 =("mahesh",) # need to give comma
print(tup5)
print(type(tup5))

#not a tuple , it is string
tup5 =("mahesh")
print(tup5)
print(type(tup5))

a = 10,20,30
print(a)
print(type(a))


a,b,c = 10,20,30
print(a,b,c)
print(type(a))
print(type(b))
print(type(c))

#mixed datatypes
tup6 = ("mahesh",50,"suresh",12.5,True)
print(tup6)
print(type(tup6))


#constructor
print(type(("ramesh","suresh","mahesh")))
list1 = [1,2,3,4,5]
mytup =tuple(list1)
print(mytup)
print(type(mytup))

#reverse index
mytup2 = (1,2,3,4,5)
print(mytup2)

print(mytup2[-1])
print(mytup2[-2])
print(mytup2[-3])
print(mytup2[-4])
print(mytup2[-5])


#range function
tup6 = (1,2,3,4,5)
for i in range(0,len(tup6)): #range(start,stop,step)#stop-1
    print(i, tup6[i])
    
    
    
    
mytup2 = (1,2,3,4,5)
print(mytup2)
print(mytup2[1:4]) #stop range -1
#total elements

print(mytup2[0:5])
print(mytup2[2:5])

print(mytup2[:5])
print(mytup2[0:])

print(mytup2[2:3])

print(mytup2[-5:-1])

print(mytup2[0:1])

#if condition membership operator

tup6 = ("mahesh",50,"suresh",12.5,True)
if "mahesh" in tup6:
    print("mahesh is there in tup6")



#interview question

tup6 = ("mahesh",50,"suresh",12.5,True)

dir(tup6)

['__add__', '__class__', '__class_getitem__',
 '__contains__', '__delattr__',
 '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__getitem__',
 '__getnewargs__', '__gt__',
 '__hash__', '__init__', '__init_subclass__',
 '__iter__', '__le__', '__len__', '__lt__',
 '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
 '__repr__', '__rmul__',
 '__setattr__', '__sizeof__',
 '__str__', '__subclasshook__', 'count', 'index']

tup6.append("mango")

list1 = list(tup6)
list1.append("mango")
print(list1)
tup6 = tuple(list1)
print(tup6)

#tuple addition

tup6 = ("mahesh","suresh","mallesh")
tup7 = ("mukesh",)
#tup6 = tup6+tup7
tup6 +=tup7
print(tup6)

#remove

tup6 = ("mahesh","suresh","mallesh")
#tup6.remove("mallesh")

list1 = list(tup6)
list1.remove("mallesh")
tup6= tuple(list1)
print(tup6)

#del key word...it will be used delete the complete tuple
tup6 = ("mahesh","suresh","mallesh")
print(tup6)
del tup6
print(tup6)

#unpacking the tuple elements

tup6 = ("mahesh","suresh","mallesh")

(name1,name2,name3) = tup6
print(name1)
print(name2)
print(name3)


#*asterisk

tup6 = ("mahesh","suresh","mallesh","mukesh","veeresh","veerupesh")

(name1,name2,*name3) = tup6
print(name1)
print(name2)
print(name3)


tup6 = ("mahesh","suresh","mallesh","mukesh","veeresh","veerupesh")

(name1,*name2,name3) = tup6
print(name1)
print(name2)
print(name3)

tup6 = ("mahesh","suresh","mallesh","mukesh","veeresh","veerupesh")

(*name1,name2,name3) = tup6
print(name1)
print(name2)
print(name3)

tup6 = ("mahesh","suresh","mallesh","mukesh","veeresh","veerupesh")

for element in tup6:
    print(element)
    
    
tup6 = ("mahesh","suresh","mallesh","mukesh","veeresh","veerupesh")

for i in range(0,len(tup6)):
    print(tup6[i])
    
#multiplication
tup2 = (1,2,3,4,5)

tup3 =tup2*2
print(tup3)


#count method will return numbers of times occurance
tup3 = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5,5,5,1,2,4,3,5)
print(tup3)
a = tup3.count(5)
print(a)
a = tup3.count(1)
print(a)


#index method will return the postion of index

tup3 = (1, 2, 3, 4, 5)
print(tup3.index(5))  





















