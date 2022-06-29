# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 08:36:45 2022

@author: durga
"""

# =============================================================================
# slicing
# =============================================================================

# string slicing


str1 ="python"
str1 ='python'

str2 ='''this is the testing case for the python testing
        it is working very fine'''
        
        
str2 ="""this is the testing case for the python testing
    it is working very fine"""
print(str2)


for i in str1:
    print(i)
    
    
for i in "python":
    print(i)
    
# len----by using len function we will get the length

print(len(str1))

print(len("xyz"))


# slicing

syntax:
    str[start:endposition:step]
    
    
str3 = "python"
str3[0:5:1]

str3[::]

str3[:5]
str3[:6]

str3[-5:-1:1]

#it will return True if the given string is in capital letter 
print(str3.isupper())

str4 = "PYTHON"
print(str4.isupper())


str5 = "Python"
print(str5.isupper())


str6 ="pYTHON"
print(str6.isupper())


# =============================================================================
# islower()
#this is method will return all characters in the given string
#is smaller case the return True
#else it will return False
# =============================================================================


str7 = "jython"
print(str7.islower())


str7 = "Jython"
print(str7.islower())

str7 = "jYTHON"
print(str7.islower())



# =============================================================================
# Upper()
# =============================================================================

str8 = "testing"
print(str8.upper())


str8 = "Testing"
print(str8.upper())



# =============================================================================
# lower
# =============================================================================

str8 = "TESTING"
print(str8.lower())


str8 = "Testing"
print(str8.lower())













