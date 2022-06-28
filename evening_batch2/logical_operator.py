# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 18:50:57 2022

@author: durga
"""


#single line comments

#multiline comments
"""
kdsjfkljdsfkj
dlfskjsdklfjksf
dslfjsdklfjkdslf
dddd
"""


'''
sdkfjdskfgkfdjgkjfdg
dfgjlfdkgjkldfjgkldf
sdkjdfklgjklfdjgkdfjg
dfslkgjfkdl
'''

# =============================================================================
# logical operator 
# =============================================================================
"""
1. and
2. or
3. not
"""


# =============================================================================
# Boolean values
# =============================================================================

1--> True

0 ---> False


print(type(True))

print(type(False))


x = 4
(x < 5) and (x > 6)


print((x < 5) and (x < 6))#True

print((x < 5) and (x > 6))#False



# =============================================================================
#  or logical operator
# =============================================================================

x = 4

(x < 5) or (x > 6)


print((x < 5) or (x < 6))

print((x > 5) or (x > 6))


print(x >5  or x< 6)

print(x>5 or )



# =============================================================================
#  not logical operator
# =============================================================================


a = True

print(not a )


a = False

print(not a )



# =============================================================================
#  conditional operator
# =============================================================================


if  and else:
    
    
a =10
b =20

if a == b:
    print("a and b are equal")
    
else:
    print("a and b are not equal")
    
  
    
  
a =10
b =20

if a <= b:
    print("a and b are equal")
    
else:
    print("a and b are not equal")
    

a =10
b =20

min1 = a if a < b else b

print(min1)



# =============================================================================
# list
# =============================================================================
    
list1 = []

print(type(list1))


#list---> different type of data types
int()
float()
str
bool


list2 =[10,20,30,40]
print(list2)
print(type(list2))


list2 =[10.0,20.5,30.3,40.9]
print(list2)
print(type(list2))


list2 =["naveen","medhana","vandana","sohan"]
print(list2)
print(type(list2))



list2 =[10,20,"naveen",10.0,20.5,30.3,40.9,"medhana","vandana","sohan",30,40]
print(list2)
print(type(list2))


list2 =[10,20,True,10.0,20.5,30.3,40.9,"medhana","vandana","sohan",30,40]
print(list2)
print(type(list2))



# =============================================================================
# identity operators
# =============================================================================

syntax: 
1. x is y
2.x is not y




x = ["naveen","meghana","vandana","sohan"]
y = ["naveen","meghana","vandana","sohan"]

z = x

print("x=",id(x))
print("z=",id(z))
print("y=",id(y))

print(x is z)


x = ["naveen","meghana","vandana","sohan"]
y = ["naveen","meghana","vandana","sohan"]

z = x

print("x=",id(x))
print("z=",id(z))
print("y=",id(y))

print(x is  not z)



x = ["naveen","meghana","vandana","sohan"]
y = ["naveen","meghana","vandana","sohan"]

z = x

print("x=",id(x))
print("z=",id(z))
print("y=",id(y))

print(x is  not y)


# =============================================================================
#  membership operator
# =============================================================================
    
syntax:
1. in 
2. not in


x = ["naveen","meghana","vandana","sohan"]
print(x)
print(type(x))



print("naveen" in x)

print("pawankalyan" in x)




not in


x = ["naveen","meghana","vandana","sohan"]

print("kalyan" not in x)

print("kalyan" not in x)


# =============================================================================
# Bitwise operator
# =============================================================================


1.&---> AND
2.|----->OR
3.^ ---->XOR
4.~------>NOT
5.<<----->left shift
6.>>----->Right shift



print(2 & 3)

#5 & 6

print(2 |3 )


print(2^4 )

print(~True)

print(~1)

print(~2)


print(2<<1)

print(1<<2)


a = 6 
print(a<<1)

a =4
print(a>>1)

a =4
print(a>>2)

a =4
print(a>>3)











