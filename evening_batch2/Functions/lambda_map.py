# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 19:47:49 2022

@author: durga
"""

#keyword lambda


#lambda arguments : expression

#single line expression 

add = lambda a : a+20

print(add(10))



def add(a):
    b = a+20
    print(b)
    
    
add(10)



add = lambda a,b : a**b

print(add(10,3))



# =============================================================================
# single variable
# =============================================================================

def add(a):
    b = a+20
    print(b)
    
    
add(10)

# =============================================================================
# two variable
# =============================================================================

add = lambda a,b : a**b

print(add(10,3))

# =============================================================================
# three variables
# =============================================================================

add = lambda a,b,c : a**b*c

print(add(10,3,4))



def my_fn(b):
    
    print(b)
    return lambda a:a*b



mult = my_fn(5)
print(mult(6))




#map and filter

def fun1(a):
    return a*a

# fun1(5)
# fun1(6)
# fun1(7)
# fun1(10)

x = map(fun1,(5,6,7,10))
#print(x)
print(type(x))
print(set(x))
#print(list(x))


#lambda and map

syntax:
    map(function,tuple)
    map(fun(lambda),(a,b,c,d))

tup1 = (1,2,3,4,5,6)
tup2 =tuple(map(lambda x: x+5,tup1))
print(tup2)


#tup1 = (1,2,3,4,5,6)
tup2 =tuple(map(lambda x: x+5,(1,2,3,4,5,6)))
print(tup2)







    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
