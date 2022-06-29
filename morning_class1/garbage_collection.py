# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 06:45:51 2022

@author: durga
"""

# =============================================================================
# Garbage collection 
# =============================================================================
# Literal 9 is an object
b = 9
print("this is the testing---->",id(b))

print("*"*30)

del b
# Reference count of object 9
# becomes 0.
#b = 9
print(id(b))


# =============================================================================
# 
# =============================================================================
def create_cycle():
    # create a list x
    x = [ ]
    x.append(x)
    print(x)
    print(id(x))
    

create_cycle()


# =============================================================================
# ways to make an objext eligible for garbage collection
# =============================================================================
x = []
x.append(1)
x.append(2)
print(x)
print(id(x))

# delete the list from memory or
# assigning object x to None(Null)
del x
# x = None


# =============================================================================
# Automatic Garbage collection of cycles
# =============================================================================
# loading gc
import gc

# get the current collection
# thresholds as a tuple
print("Garbage collection thresholds:",gc.get_threshold())





# =============================================================================
# manual garbage collection
# =============================================================================
# Importing gc module
import gc

# Returns the number of
# objects it has collected
# and deallocated
print(dir(gc))
collected = gc.collect()

# Prints Garbage collector
# as 0 object
print("Garbage collector: collected","%d objects." % collected)



# =============================================================================
# 
# =============================================================================


import gc
i = 0

# create a cycle and on each iteration x as a dictionary
# assigned to 1
def create_cycle():
	x = { }
	x[i+1] = x
	print(x)

# lists are cleared whenever a full collection or
# collection of the highest generation (2) is run
collected = gc.collect() # or gc.collect(2)
print("Garbage collector: collected %d objects." % (collected))

print("Creating cycles...")
for i in range(10):
    #print(id(i))
    create_cycle()

collected = gc.collect()

print("Garbage collector: collected %d objects." % (collected))




import gc

a =10
b =10

print("a",id(a))
print("b",id(b))

def fn1():
    c =10
    print("c",id(c))
    c =20
    print("c",id(c))
    
    
fn1()
#print(c)
a =20
print("a",id(a))

collected = gc.collect()

print("Garbage collector: collected %d objects." % (collected))



# =============================================================================
# to check the methods of 
# =============================================================================
import gc

print(dir(gc))









