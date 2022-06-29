# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 08:31:03 2022

@author: durga
"""

# =============================================================================
# Assignment operators
# =============================================================================

#"=" operators

a = 5
print(a)

print(type(a))
print(id(a))


#"+=" addition first then assign

a =10
a += 5  #a = a+5
print(a)

print(type(a))
print(id(a))


#"-=" substraction first then assign

a =10
a -= 5  #a = a-5
print(a)

print(type(a))
print(id(a))


#"*=" multiplication first then assign

a =10
a *= 5  #a = a*5
print(a)

print(type(a))
print(id(a))

#"/=" division operators

a =10
a /= 5  #a = a*5
print(a)

print(type(a))
print(id(a))

#"//=" floor division operators with integer

a =10
a //= 5  #a = a*5
print(a)

print(type(a))
print(id(a))



#"&=" and operation then assign

a = 2
b = 3

print(a&b)

a =4
b =5
print(a&b)

#"|=" or operation then assign
a = 2
b = 3

print(a|b)

a =4 #0100
b =5 #0101
print(a|b)#0101


#"!=" not operation then it will assign
a = 2

print(a != 2)
print(a != 3)



#"^=" xor operation the it will assign

a = 2
a^=3
print(a)


#shift operations
 
print(2 >>1)
print(2 <<1)

a =2

a>>=1
print(a)

a =4
a >>=2
print(a)


a =4
a <<=2
print(a)






















