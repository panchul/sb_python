'''
A decorator for a class(from https://builtin.com/software-engineering-perspectives/python-class-decorator):

'''

class Power(object):
	def __init__(self, arg):
		self._arg = arg

	def __call__(self, a, b):
		retval = self._arg(a, b)
		return retval ** 2

@Power
def multiply_together(a, b):
	return a * b

print(multiply_together)
print(multiply_together(2, 2))
