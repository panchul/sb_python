'''
Example originally from https://www.geeksforgeeks.org/decorators-in-python/

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
