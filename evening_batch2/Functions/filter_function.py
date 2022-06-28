# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:10:19 2022

@author: durga
"""

# import os
# import time


# =============================================================================
# filter syntax
# =============================================================================

syntax:
    filter(function, iterable)


even_num = filter(lambda x:(x%2==0),[1,2,3,4,5,6])

a = list(even_num)
print(a)


even_num = filter(lambda x:(x%2==0),(1,2,3,4,5,6))

a = list(even_num)
print(a)


#assignment
#1. need to pass list to function
#2.need to check even number or not
#3.multiple numbers should be returned  

