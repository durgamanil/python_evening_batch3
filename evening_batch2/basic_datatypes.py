# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 18:36:46 2022

@author: durga
"""

# print(id(10))#2013672204880
# print(type(10))#<class 'int'>

# a =10000
# print(type(a))

# b =100176769989754387834593845983
# print(type(b))#<class 'int'>

# =============================================================================
# This is the floating type
# =============================================================================

# print(17.3) #17.3
# print(type(17.3)) #<class 'float'>
# print(id(17.3)) #17.3


# a =17.3
# print(id(a))
# print(type(a))

# b =17.3
# print("before change",id(b))
# print(type(b))


# print("*"*30)


# b = 18.6
# print("after change",id(b))
# print(type(b))


# <class 'float'>
# 2013838536880
# 2013838536880
# <class 'float'>
# before change 2013838536880
# <class 'float'>
# ******************************
# after change 2013839921392
# <class 'float'>


# a = 456464545454545.478475847588435784375#456464545454545.5
# print(a)#456464545454545.5

# b = 234.474637546375643756#234.47463754637565
# print(b)
# print(id(b))#234.47463754637565


# =============================================================================
# strings type
# =============================================================================


#string---->str

# syntax:
#     str---->1."test"
#             2.'test'
            
            
# print("Hello world") #Hello world        
# print('Hello world') #Hello world    

# a = "Hello world"
# b = "Hello world"

#a and b are same

# print(id(a))#2013835663024

# print(id(b))#2013835663024

#a and b are not same
# a = "Hello world"
# b = "Hello World"

# print(id(a))
# print(id(b))


# print(type(a))#<class 'str'>
# print(type(b))#<class 'str'>

#print(dir(a))

['__add__', 
 '__class__',
 '__contains__', 
 '__delattr__', 
 '__dir__',
 '__doc__', 
 '__eq__', 
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__', 
 '__getnewargs__',
 '__gt__',
 '__hash__', 
 '__init__',
 '__init_subclass__', 
 '__iter__',
 '__le__', 
 '__len__',
 '__lt__',
 '__mod__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__', 
 '__repr__',
 '__rmod__', 
 '__rmul__', 
 '__setattr__',
 '__sizeof__',
 '__str__', 
 '__subclasshook__',
 'capitalize',
 'casefold',
 'center',
 'count', 
 'encode', 
 'endswith', 
 'expandtabs',
 'find', 
 'format', 
 'format_map', 
 'index', 
 'isalnum',
 'isalpha',
 'isascii',
 'isdecimal',
 'isdigit',
 'isidentifier',
 'islower',
 'isnumeric',
 'isprintable',
 'isspace', 
 'istitle',
 'isupper', 
 'join', 
 'ljust', 
 'lower', 
 'lstrip',
 'maketrans',
 'partition',
 'removeprefix',
 'removesuffix', 
 'replace', 
 'rfind', 'rindex',
 'rjust', 'rpartition', 
 'rsplit', 'rstrip', 'split',
 'splitlines', 'startswith', 
 'strip', 'swapcase', 'title',
 'translate', 'upper', 'zfill']


# =============================================================================
# string methods
# =============================================================================
a = "testing"
print(a)#testing
print(a.capitalize())#Testing
# b = a.upper()#TESTING
# print("b:",b)
# print(type(b))

#assigning to same variable
a = a.upper()#TESTING
print("a:",a)
print(type(a))

# =============================================================================
# changing datatype integer to string
# =============================================================================
a =10
print(type(a))
a ="naveen"
print(type(a))


# =============================================================================
# string methods
# =============================================================================

a = "testing python general"

print(a.capitalize())#Testing


#upper

a = "testing python general"

print(a.upper())

a = a.upper()

print("after upper",a)

print(a.lower())


#isupper
a = "testing python general"

print(a.isupper())

a = a.upper()

print(a.isupper())



a = "testing python general"
print(a.islower())


#len funtion
a ="test mailkjdfskjkdfsjgkdfjgkjdfkgjdskjgkdfjgksj"
print(len(a))



















