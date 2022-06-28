# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 19:14:21 2022

@author: durga
"""

# =============================================================================
# string slicing
# =============================================================================

str1 = "testing"

print(str1)
print(type(str1))

#slicing---small pieces
#indexing
print(str1[0])
#print(str1[1])
print(str1[2])
print(str1[6])


str2 = "mahendra bahubali son is amrendra bahubali"
print(len(str2))
print(str2[16])


a =0
for i in str1:
    #print(i)
    print("index ",a,str1[a])
    a =a+1

print(str1.index('t'))
print(str1.index('e'))


print(str1[-1])
print(str1[-2])
print(str1[-3])
print(str1[-4])
print(str1[-5])
print(str1[-6])
print(str1[-7])




# =============================================================================
# slicing
# =============================================================================

str1 = "helmet"

#slicing---> can  cut the string


str1[0:6]



str2 = "NarayanaMurthy"

print(str2)
print(str2[1:3])

print(str2[8:15])

print(str2[0:8])


# =============================================================================
# interview question
# =============================================================================

q1:
    
str3 ="ramakrishna"

print(str3[10])
print(str3[11])

q2:

    
str3 ="ramakrishna"
print(str3[-12])






