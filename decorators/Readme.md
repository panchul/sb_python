## Decorators

---

Example of a decorator for a function(from https://www.geeksforgeeks.org/decorators-in-python/):

```
'''
% python runit.py
400
200
'''

# code for testing decorator chaining 
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 

def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 

@decor1
@decor
def num(): 
    return 10

@decor
@decor1
def num2():
    return 10
  
## The below is basically this:
# decor1(decor(num))
# decor(decor1(num2))

print(num()) 
print(num2())
```    
---

A decorator for a class(from https://builtin.com/software-engineering-perspectives/python-class-decorator):

```
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
```

---

And even better, with a static info about calls(from https://builtin.com/software-engineering-perspectives/python-class-decorator):

```
class Power(object):
    def __init__(self, arg):
        self._arg = arg
        self._memory = []

    def __call__(self, a, b):
        retval = self._arg(a, b)
        self._memory.append(retval **2)
        return retval ** 2

    def memory(self):
        return self._memory

@Power
def multiply_together(a, b):
    return a * b

print(multiply_together)
print(multiply_together(2, 2))
print(multiply_together(3, 2))
print(multiply_together(2, 6))
print(multiply_together.memory())
```

A test run:

```
% python runit.py
<__main__.Power object at 0x7f9c4e1235d0>
16
36
144
[16, 36, 144]
```
