'''
with a static info about calls
originally from https://builtin.com/software-engineering-perspectives/python-class-decorator

A test run:

% python runit.py
<__main__.Power object at 0x7f9c4e1235d0>
16
36
144
[16, 36, 144]

or, with tracing:

% python class_fancier_decorator.py 
  Initializing Power with argument <function multiply_together at 0x104bcb1c0>
print(multiply_together)
<__main__.Power object at 0x104b9bfd0>
print(multiply_together(2, 2))
  Calling __call__ with arguments 2 2
16
print(multiply_together(3, 2))
  Calling __call__ with arguments 3 2
36
print(multiply_together(2, 6))
  Calling __call__ with arguments 2 6
144
print(multiply_together.memory())
  Calling memory(self)
[16, 36, 144]

'''

class Power(object):
    def __init__(self, arg):
        print("  Initializing Power with argument", arg)
        self._arg = arg
        self._memory = []

    def __call__(self, a, b):
        print("  Calling __call__ with arguments", a, b)
        retval = self._arg(a, b)
        self._memory.append(retval **2)
        return retval ** 2

    def memory(self):
        print("  Calling memory(self)")
        return self._memory

@Power
def multiply_together(a, b):
    return a * b

print("print(multiply_together)")
print(multiply_together)

print("print(multiply_together(2, 2))")
print(multiply_together(2, 2))

print("print(multiply_together(3, 2))")
print(multiply_together(3, 2))

print("print(multiply_together(2, 6))")
print(multiply_together(2, 6))

print("print(multiply_together.memory())")
print(multiply_together.memory())
