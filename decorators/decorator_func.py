'''
Example originally from https://www.geeksforgeeks.org/decorators-in-python/

% python runit.py
400
200
'''

# code for testing decorator chaining 
def decor1(func): 
    print("  Initializing decor1 with func", func.__name__)
    def inner(): 
        print("  Calling inner() of decor1 with func", func.__name__)
        x = func() 
        return x * x 
    return inner 

def decor(func): 
    print("  Initializing decor with func", func.__name__)
    def inner(): 
        print("  Calling inner() of decor with func", func.__name__)
        x = func() 
        return 2 * x 
    return inner 

@decor1
@decor
def num(): 
    print("  Calling num")
    return 10

@decor
@decor1
def num2():
    print("  Calling num2")
    return 10
  
## The below is basically this:
# decor1(decor(num))
# decor(decor1(num2))

print("print(num())")
print(num()) 

print("print(num2())")
print(num2())
