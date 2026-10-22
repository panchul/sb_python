'''
A decorator for a class(from https://builtin.com/software-engineering-perspectives/python-class-decorator):

% python class_decorator.py        
  Initializing Power with argument <function multiply_together at 0x10068bd90>
print(multiply_together)
<__main__.Power object at 0x100787fd0>
print(multiply_together(2, 2))
  Calling __call__ with arguments 2 2
  Calling multiply_together with arguments 2 2
16

'''

class Power(object):
	def __init__(self, arg):
		print("  Initializing Power with argument", arg)
		self._arg = arg

	def __call__(self, a, b):
		print("  Calling __call__ with arguments", a, b)
		retval = self._arg(a, b)
		return retval ** 2

@Power
def multiply_together(a, b):
	print("  Calling multiply_together with arguments", a, b)
	return a * b


print("print(multiply_together)")
print(multiply_together)

print("print(multiply_together(2, 2))")
print(multiply_together(2, 2))
