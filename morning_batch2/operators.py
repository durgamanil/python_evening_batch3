# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 08:08:01 2022

@author: durga
"""

# =============================================================================
# power
# =============================================================================

a =2
b = 3

print(a**b)

print((a**b)**2)

# =============================================================================
# BODMAS rule
# 
# B---->brackets
# O--->off
# D---->division
# M---->multiplication
# A---->position
# S---->substraction
# =============================================================================

print(5*4*3+2*5+6-2)
print((5*4*3)+(2*5)+6-2)


# =============================================================================
# Assignments
# =============================================================================

"="----->assign right value to left side variable
a = b
a = 10
b = 25

"+="----->addition operation then assign
a+=b

a = 5
a +=10   #=======> a = a + 10
print(a)


python approch...
1.right side operation will done then assigned to leftside
2.top to bottom



"-="----------------->substraction option then assign
a =20
a -= 10========> a = a-10
print(a)


"*="======================>multiplication an assign to leftside

a =20
a *= 10 #========> a = a*10
print(a)


"/="======================> divion operation done first then assigned to left

a =20
a /= 10 #========> a = a/10
print(a)

print(type(int(a)))
print(type(a))


"//="======================>division operation done here after that it will assign to leftside

a =20
a //= 10 #========> a = a%10
print(a)
print(type(a))


modulus operation

print(45%9)
print(46%9)
print(19%2)


"**=" =======> muitiplication operation will be done then assignment


a =2
a **= 10 #========> a = a**10
print(a)
print(type(a))



"&=" bitwise operation and assign to left


a =2
a &= 1 #========> a = a&10
print(a)


a =3
a &= 1 #========> a = a&10
print(a)


"|=" Bitwise or operation assigned to left side


a =3
a |= 1 #========> a = a|10
print(a)

a =4
a |= 1 #========> a = a|10
print(a)

"^="====>xor bitwise operation afther that assigned to left side


a =4
a ^= 1 #========> a = a^0
print(a)


">>=" first shift will happen then assigned to leftside

a =2
a >>=1
print(a)


a =4
a >>=1
print(a)

a =4
a >>=2
print(a)


a =4
a >>=3
print(a)

"<<=" left shift will be done then assigne to left side


a =4
a <<=1
print(a)






















