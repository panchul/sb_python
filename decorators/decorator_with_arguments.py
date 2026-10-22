'''
Originally from here:
https://builtin.com/software-engineering-perspectives/python-class-decorator


% python decorator_with_arguments.py 
16
64

or, with tracing:

% python decorator_with_arguments.py
  Initializing Power with argument <function multiply_together1 at 0x10484f2e0>
  Initializing Power with argument 3
  Creating wrapper with exponent 3
print(multiply_together1(2, 2)) # (2 * 2) **2
  Calling __call__ without decorator arguments with arguments 2 2
16
print(multiply_together2(2, 2)) # (2 * 2) **3
  Calling wrapper with arguments 2 2
64

'''

class Power(object):
	def __init__(self, arg):
		print("  Initializing Power with argument", arg)
		self._arg = arg

	def __call__(self, *param_arg):
		"""If there are decorator arguments, __call__() is only called once
		as part of the decoration process. You can only give it a single argument,
		which is the function object
		If there are no decorator arguments, the function
		to be decorated is passed to the constructor.
		"""
		if len(param_arg) == 1:
			print("  Creating wrapper with exponent", self._arg)
			def wrapper(a, b):
				print("  Calling wrapper with arguments", a, b)
				retval = param_arg[0](a, b)
				return retval ** self._arg
			return wrapper
		else:
			print("  Calling __call__ without decorator arguments with arguments", param_arg[0], param_arg[1])
			expo = 2
			retval = self._arg(param_arg[0], param_arg[1])
			return retval ** expo


@Power
def multiply_together1(a, b):
	return a * b

@Power(3)
def multiply_together2(a, b):
	return a * b


print("print(multiply_together1(2, 2)) # (2 * 2) **2")
print(multiply_together1(2, 2)) # (2 * 2) **2
print("print(multiply_together2(2, 2)) # (2 * 2) **3")
print(multiply_together2(2, 2)) # (2 * 2) **3
