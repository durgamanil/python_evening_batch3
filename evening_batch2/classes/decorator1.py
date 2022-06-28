# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:06:15 2022

@author: durga
"""
#general function output
def decor(func):
	def inner(name):
		print("this is decorator function")
		func(name)
	return inner


def greet(name):
	print("good evening",name)
	
greet("mohan")


# =============================================================================
# 
# =============================================================================
def decor(func):
	def inner(name):
		print("this is decorator function")
		func(name)
	return inner

@decor
def greet(name):
	print("good evening",name)
	
	
greet("mohan")


# =============================================================================
# function calling from other function
# =============================================================================

def decor(func):
	def inner(name):
		print("this is decorator function")
		func(name)
	return inner


def fun2():
    print("this is thefunc2")

def greet(name):
	
   fun2()
   print("good evening",name)
	
	
greet("mohan")



# =============================================================================
# example3
# =============================================================================

def sum(func):
    def inner(a,b):
        print("this is from sum ",a,b)
        func(a,b)
    return inner

@sum
def sum_calculation(a,b):
    print("this is addition fun",a+b)
    
sum_calculation(10, 20)



# =============================================================================
# 
# =============================================================================
def decor(func):
	def inner(name):
		print("this is decorator1 function")
		func(name)
	return inner


def decor2(func):
	def inner(name):
		print("this is decorator2 function")
		func(name)
	return inner

@decor2
@decor
def greet(name):
	print("good evening",name)
	
	
greet("mohan")


# =============================================================================
# 
# =============================================================================
def decor(func):
	def inner(name):
		print("this is decorator1 function")
		func(name)
	return inner


def decor2(func):
	def inner(name):
		print("this is decorator2 function")
		func(name)
	return inner

def decor3(func):
	def inner(name):
		print("this is decorator3 function")
		func(name)
	return inner


@decor
@decor2
@decor3
def greet(name):
	print("good evening",name)
	
	
greet("mohan")




# =============================================================================
# 
# =============================================================================
