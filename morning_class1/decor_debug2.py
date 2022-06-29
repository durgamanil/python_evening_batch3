
# # Python code to illustrate
# # Decorators with parameters in Python

def decorator(*args, **kwargs):
	print("Inside decorator")
	
	def inner(func):
		# code functionality here
		print("Inside inner function")
		print("I like", kwargs['like'])
		func()
	# returning inner function
	return inner

#@decorator(like = "geeksforgeeks")
def my_func():
	print("Inside actual function")
    #decorator(my_func)

if __name__ == "__main__":
    my_func()

