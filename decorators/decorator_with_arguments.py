'''
Originally from here:
https://builtin.com/software-engineering-perspectives/python-class-decorator


% python decorator_with_arguments.py 
16
64

'''

class Power(object):
	def __init__(self, arg):
		self._arg = arg

	def __call__(self, *param_arg):
		"""If there are decorator arguments, __call__() is only called once
		as part of the decoration process. You can only give it a single argument,
		which is the function object
		If there are no decorator arguments, the function
		to be decorated is passed to the constructor.
		"""
		if len(param_arg) == 1:
			def wrapper(a, b):
				retval = param_arg[0](a, b)
				return retval ** self._arg
			return wrapper
		else:
			expo = 2
			retval = self._arg(param_arg[0], param_arg[1])
			return retval ** expo


@Power
def multiply_together1(a, b):
	return a * b

@Power(3)
def multiply_together2(a, b):
	return a * b


print(multiply_together1(2, 2)) # (2 * 2) **2
print(multiply_together2(2, 2)) # (2 * 2) **3
