# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 23:23:47 2022

@author: durga
"""
# #syntax
# def decorators(*args, **kwargs):
#  	def inner(func):
#           return func
#  	return inner #this is the fun_obj mentioned in the above content

# @decorators(params)
# def func():
#  	"""
# 		function implementation
#  	"""
#      return value
 
# func()


# # =============================================================================
# # Decorators
# # =============================================================================
# # Python program to illustrate functions
# # can be treated as objects
# def shout(text):
# 	return text.upper()

# print(shout('Hello'))

# yell = shout

# print(yell('Hello'))

# # =============================================================================
# # 
# # =============================================================================
# # Python program to illustrate functions
# # can be passed as arguments to other functions
# def shout(text):
# 	return text.upper()

# def whisper(text):
# 	return text.lower()

# def greet(func):
# 	# storing the function in a variable
# 	greeting = func("""Hi, I am created by a function passed as an argument.""")
# 	print (greeting)

# greet(shout)
# greet(whisper)



# =============================================================================
# 
# =============================================================================
# defining a decorator
# def hello_decorator(func):
# 	# inner1 is a Wrapper function in
# 	# which the argument is called
# 	# inner function can access the outer local
# 	# functions like in this case "func"
# 	def inner1():
# 		print("Hello, this is before function execution")
# 		# calling the actual function now
# 		# inside the wrapper function.
# 		func()
# 		print("This is after function execution")
# 		
# 	return inner1


# # defining a function, to be called inside wrapper
# def function_to_be_used():
# 	print("This is inside the function !!")


# # passing 'function_to_be_used' inside the
# # decorator to control its behaviour
# function_to_be_used = hello_decorator(function_to_be_used)


# # calling the function
# function_to_be_used()




# # =============================================================================
# # 
# # =============================================================================
# importing libraries
# import time
# import math

# # decorator to calculate duration
# # taken by any function.
# def calculate_time(func):
#  	# added arguments inside the inner1,
#  	# if function takes any arguments,
#  	# can be added like this.
#  	def inner1(*args, **kwargs):

# 		# storing time before function execution
#  	  begin = time.time()
# 		
#  	  func(*args, **kwargs)

# 		# storing time after function execution
#  	  end = time.time()
#  	  print("Total time taken in : ", func.__name__, end - begin)

#  	return inner1



# # this can be added to any function present,
# # in this case to calculate a factorial
# @calculate_time
# def factorial(num):

#  	# sleep 2 seconds because it takes very less time
#  	# so that you can see the actual difference
#  	time.sleep(2)
#  	print(math.factorial(num))

# # calling the function.
# factorial(5)


# # =============================================================================
# # 
# # =============================================================================
# def hello_decorator(func):
#  	def inner1(*args, **kwargs):
#          print("before Execution")
#          # getting the returned value
#          returned_value = func(*args, **kwargs)
#          print("after Execution")
#          return returned_value
# 		
#  	return inner1


# # adding decorator to the function
# @hello_decorator
# def sum_two_numbers(a, b):
#  	print("Inside the function")
#  	return a + b

# a, b = 1, 2

# # getting the value through return of the function
# print("Sum =", sum_two_numbers(a, b))


# # =============================================================================
# # 
# # =============================================================================
# import time
# import math

# # decorator to calculate duration
# # taken by any function.
# def calculate_time(func):
#  	# added arguments inside the inner1,
#  	# if function takes any arguments,
#  	# can be added like this.
#  	def inner1(*args, **kwargs):

# 		# storing time before function execution
#  	  begin = time.time()
# 		
#  	  func(*args, **kwargs)

# 		# storing time after function execution
#  	  end = time.time()
#  	  print("Total time taken in : ", func.__name__, end - begin)

#  	return inner1
 
    
# # # code for testing decorator chaining
# def decor1(func):
#  	def inner():
#          x = func()
#          print("decor1--x::",x)
#          return x * x
#  	return inner

# def decor(func):
#  	def inner():
#          x = func()
#          print("decor ::x",x)
#          return 2 * x
#  	return inner
 
    
# @calculate_time
# @decor
# @decor1
# def num():
#  	return 10

# print(num())




# # =============================================================================
# # 
# # =============================================================================
# # Python code to illustrate
# # Decorators basic in Python

# def decorator_fun(func_to):
#     print("Inside decorator")

#     def inner(*args, **kwargs):
#         print("Inside inner function")
#         print("Decorated the function")
#         # do operations with func
#         func_to()
#     return inner

# @decorator_fun
# def func_to():
#  	print("Inside actual function")



#func_to()

# # =============================================================================
# # 
# # =============================================================================

# Python code to illustrate
# Decorators with parameters in Python

def decorator(*args, **kwargs):
 	print("Inside decorator")
 	
 	def inner(func):
         print("Inside inner function")
         print("I like", kwargs['like'])
         func()
		
 	# returning inner function
 	return inner

@decorator(like = "geeksforgeeks")
def my_func():
 	print("Inside actual function")
    
# # =============================================================================
# #  
# # =============================================================================
    
# # Python code to illustrate
# # Decorators with parameters in Python

# def decorator_func(x, y):

#  	def Inner(func):
#          def wrapper(*args, **kwargs):
#              print("I like Geeksforgeeks")
#              print("Summation of values - {}".format(x+y) )
#              func(*args, **kwargs)
#          return wrapper
#  	return Inner


# # Not using decorator
# def my_fun(*args):
#  	for ele in args:
#          print(ele)

# # another way of using decorators
# decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks')


# # =============================================================================
# # 
# # =============================================================================
# # Python code to illustrate
# # Decorators with parameters in Python (Multi-level Decorators)


def decorator1(dataType, message1, message2):
 	def decorator(fun):
          print(message1)
          a = a=30
          def wrapper(*args, **kwargs):
              print(message2)
              if all([type(arg) == dataType for arg in args]):
                  return fun(*args, **kwargs)
              return "Invalid Input"
          return wrapper
 	return decorator


@decorator1(str, "Decorator for 'stringJoin'", "stringJoin started ...")
def stringJoin(*args):
 	st = ''
 	for i in args:
          st += i
 	return st


@decorator1(int, "Decorator for 'summation'\n", "summation started ...")
def summation(*args):
 	summ = 0
 	for arg in args:
         summ += arg
 	return summ


print(stringJoin("I ", 'like ', "Geeks", 'for', "geeks"))
print()
print(summation(19, 2, 8, 533, 67, 981, 119))

