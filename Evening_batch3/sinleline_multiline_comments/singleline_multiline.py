# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:47:51 2022

@author: durga
"""

# =============================================================================
# comments
# =============================================================================


1.single line comment
2.multiline comments

1.single line comments

we will present with "#"

#chakradar  is my variable
chakradar = 10
print("this is testing single comments")
print(a)

a = 10
#print("this is testing single comments")
#print("this is yet another test")
print(a)




a  =10 #this is my variable
print("this is testing ",a) #this is a variable print

2.multiline comments


indicated as """start postion """end position

"""
#chakradar  is my variable
chakradar = 10
print("this is testing single comments")
print(a)

a = 10
#print("this is testing single comments")
#print("this is yet another test")
print(a)
"""

'''
#chakradar  is my variable
chakradar = 10
print("this is testing single comments")
print(a)

a = 10
#print("this is testing single comments")
#print("this is yet another test")
print(a)
'''


#doc string

#documentation string
functions and classes we will use this

def doc_test():
    """this is testing of doc string"""
    a = 10
    print(a)

doc_test()

print(doc_test.__doc__)




def calc_test():
    """this is the function developed for sum addition
    multiplication and division operation 
    and many other math operations
    """
    a = 10
    print(a)

calc_test()

print(calc_test.__doc__)




#not doc string

def calc_test():

    a = 10
    print(a)
    
    """this is the function developed for sum addition
    multiplication and division operation 
    and many other math operations
    """
    print(a)

calc_test()

print(calc_test.__doc__)