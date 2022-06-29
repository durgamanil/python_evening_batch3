# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 06:28:47 2022

@author: durga
"""
# =============================================================================
# exceptions
# =============================================================================
# initialize the amount variable
amount = 10000

# check that You are eligible to
# purchase Dsa Self Paced or not
if(amount > 2999)
    print("You are eligible to purchase Dsa Self Paced")



# =============================================================================
# 
# =============================================================================


# initialize the amount variable
marks = 100

# perform division with 0
a = marks / 0
print(a)

# =============================================================================
# 
# =============================================================================
# Python program to handle simple runtime error
#Python 3

a = [1, 2, 3]

print ("Fourth element = %d" %(a[-10]))


print ("Fourth element = %d" %(a[3]))





a = [1, 2, 3]
try:
	print ("Second element = %d" %(a[1]))

	# Throws error since there are only 3 elements in array
	print ("Fourth element = %d" %(a[3]))

except:
	print ("list out of range")


# =============================================================================
# 
# =============================================================================

try:
    # statement(s)
except IndexError:
    # statement(s)
except ValueError:
    # statement(s)
    
# =============================================================================
# 
# =============================================================================
# Program to handle multiple errors with one
# except statement
# Python 3

def fun(a):
	if a < 4:

		# throws ZeroDivisionError for a = 3
		b = a/(a-3)

	# throws NameError if a >= 4
	print("Value of b = ", b)
	
try:
	fun(3)
	fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
	print("ZeroDivisionError Occurred and Handled")
except NameError:
	print("NameError Occurred and Handled")

    
# =============================================================================
# 
# =============================================================================
# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
def fun(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

# Driver program to test above function

fun(3.0, 3.0)

fun(2.0, 3.0)

# =============================================================================
# 
# =============================================================================
try:
    # Some Code.... 

except:
    # optional block
    # Handling of exception (if required)

else:
    # execute if no exception

finally:
    # Some code .....(always executed)

    
# =============================================================================
# 
# =============================================================================
# Python program to demonstrate finally

# No exception Exception raised in try block
print(4.0/2.0)
print(5//2)
print(4//2)


try:
	k = 5//0 # raises divide by zero exception.
	print(k)

# handles zerodivision exception
except ZeroDivisionError:
	print("Can't divide by zero")

finally:
	# this block is always executed
	# regardless of exception generation.
	print('This is always executed')
    
    
# =============================================================================
# 
# =============================================================================
# Program to depict Raising Exception

try:
	raise NameError("Hi there") # Raise Error
except NameError:
	print ("An exception")
	raise # To determine whether the exception was raised or not

# =============================================================================
# 
# =============================================================================
Some of the common Exception Errors are : 
 

IOError: if the file can’t be opened
KeyboardInterrupt: when an unrequired key is pressed by the user
ValueError: when built-in function receives a wrong argument
EOFError: if End-Of-File is hit without reading any data
ImportError: if it is unable to find the module
 
# =============================================================================
# 
# =============================================================================
# Python code to illustrate
# working of try()
def divide(x, y):
	try:
		# Floor Division : Gives only Fractional Part as Answer
		result = x // y
		print("Yeah ! Your answer is :", result)
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of Program
divide(3, 2)

# =============================================================================
# 
# =============================================================================
# Python code to illustrate
# working of try()
def divide(x, y):
	try:
		# Floor Division : Gives only Fractional Part as Answer
		result = x // y
		print("Yeah ! Your answer is :", result)
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of Program
divide(3, 0)

# =============================================================================
# custom exceptions
# =============================================================================
class CustomError(Exception):
     print("Sorry ! You are dividing by zero ")
 

try:
	# Floor Division : Gives only Fractional Part as Answer
	result = 5 // 0
	print("Yeah ! Your answer is :", result)
except CustomError:
    
	#print("Sorry ! You are dividing by zero ")
    pass

# =============================================================================
# 
# =============================================================================

# define Python user-defined exceptions
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass

class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly.")

# =============================================================================
# 
# =============================================================================
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)