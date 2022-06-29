# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 21:03:59 2022

@author: durga
"""

c = "this is 'india' biggest project"
print(c.capitalize())


c = "india"
print(c.capitalize())


#count will gives to how many times it is occured 
c = "this is 'india' biggest this project this"
print(c.count("this"))
print(c.count("india"))

c = "this is 'india' biggest this project this"
print(c.count("this"),c.count("india"))



c = "this is 'india' biggest this project this"
print(c.count("is"))

c = "isisisisisissisisssisis"
print(c.count("is"))

c = "this is 'india' biggest this project this"
print(c.isupper())


#isupper method will return
# the true if all character are capital letters  
c = "INDIA"
print(c.isupper())

c = "INDIa"
print(c.isupper())

#islower method will return True
#if all the character are smaller
c = "india"
print(c.islower())

c = "INDIA"
print(c.islower())


#split method will split the string
c ="apple,banana,mango"
x = c.split(",")
print(x)

print(x[0])
print(x[1])
print(x[2])

txt = "Hello World"[::-1]
print(txt)













