# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 07:36:12 2022

@author: durga
"""

def hello_dec(fun):

	def inner1():
		print("Hello, this is before function execution")
		# calling the actual function now
		# inside the wrapper function.
		fun()
		print("This is after function execution")
		
	return inner1


# defining a function, to be called inside wrapper
def fun():
	print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behaviour
fun = hello_dec(fun)


# calling the function
fun()