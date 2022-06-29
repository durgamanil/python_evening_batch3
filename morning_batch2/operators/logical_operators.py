# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 08:24:48 2022

@author: durga
"""

# =============================================================================
# 4.Logical operators
# =============================================================================
# 1. and---keyword
# 2. or----keyword
# 3. not----keyword

and = 5
or = 10

#and 
#when two conditions are there that time only you can use and operator


#if both statements are true then only output will true
(5<=6) and (6<7)
print( 4<5 and 6>3)

print( 4<5 and 6>3 and 4 <5)#True
print( (4<5 and 6>3) and 4 <5)#True

# or operator
#when two conditions are there that time you can use or operator
#one condition is true...the complete expression will true
(5<=6) or (6<7)#True
print( 4<5 and 6>3)#True

print(5<=6 or 6<=5)#True


print( (4<5 and 6>3) or 4 <5)#True



# not operator

not----> keyword

print(not(5<4))

print(not(True))#False
print(not(False))#True

print(not(5<4 and 100>50))#True

print(not((20<30 or 40>30) and 50<60))
print(not(True and True))
print(not(True))#False











