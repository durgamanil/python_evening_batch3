date:20-05-2022

topic: decorators

Decorator is the function which will added functionality of other function
or
we can feature of the another function to existing function

add beauty to the existing function


syntax:

def function1(function_name):
	def inner_function(parameter):
		"""statements"
		return
	return inner_function

@function1------>decorator function	
def function2(args):
	"""statements""""
	
	
function2(args)