# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 07:36:01 2022

@author: durga
"""


import gc

a =10
b =10

print("a",id(a))
print("b",id(b))

def fn1(c):
    c =10
    print("c",id(c))
    c =20
    print("c",id(c))
    #del c
    
for i in range(5):
    fn1(a)
#print(c)
a =20
print("a",id(a))

# collected = gc.collect()

# print("Garbage collector: collected %d objects." % (collected))

#del a 
count = gc.get_count()
print("gc count", count)

objects = gc.get_objects()
print("gc objects", objects)

collected = gc.collect()

print("Garbage collector: collected %d objects." % (collected))
