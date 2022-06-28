# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 18:51:21 2022

@author: durga
"""

#list-day2

dir(list)

list.__doc__

#aliasing

chintu = [1,2,3,4,5]
print("chintu",chintu)
print(type(chintu))


naveen = chintu

print("naveen",naveen)
print(type(naveen))

print(id(naveen))
print(id(chintu))


naveen.append(10)
print("naveen",naveen)
print("chintu",chintu)


chintu.append(20)
print("naveen",naveen)
print("chintu",chintu)


# =============================================================================
# converting string to list
# =============================================================================

typecasting----> 

a =1234
print(a)

b = str(a)
print(b)


a =20
print(a)

b = float(a)
print(b)

a = "rayudu"
b = list(a)

print(a)
print(b)


a ="1234"
b = list(a)

print(a)
print(b)

print(b[0])
print(type(b[0]))



# =============================================================================
# list in functions
# =============================================================================

def funtion(a):
    print(10+20)
    print(20-3)
    print(a)
    

if __name__ == '__main__': 
    a = [1,2,3,4]
    funtion(a)

# =============================================================================
# 
# =============================================================================


def funtion(a):
    #print(10+20)
    #print(20-3)
    print(a)
    


a = [1,2,3,4]
funtion(a)
print("this is after function call")



