# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 08:13:35 2022

@author: durga
"""

# =============================================================================
# docstring
# =============================================================================

#this is the addition function
def myfun():
	"""
	this is the addition function
    here two variables required
    c is the another variable uses for get the output
	"""
	a =10
	b =20
	c = a + b
	print(c)
    
myfun()

print(myfun.__doc__)



def myfun():
	'''
	this is the addition function
	'''
	a =10
	b =20
	c = a + b
	print(c)
    
    
myfun()

print(myfun.__doc__)