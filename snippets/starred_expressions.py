'''
About starred expressions
http://yaoyao.codes/python/2016/09/25/python-starred-expression
'''
def func(a, b ,c):
    print(a, b, c)
    
# func(c=3, 1, 2)              # SyntaxError: positional argument follows keyword argument
func(c=3, *(1,2))              # OK. 1 2 3
func(c=3, **dict(a=1,b=2))     # OK. 1 2 3
func(c=3, *(1,), **dict(b=2))  # OK. 1 2 3
    
# Another one, with args

def func2(*args, **kwargs):
    print(args)
    print(kwargs)
    print(locals())
    
func2(1, a=2)
    
# output:
#   (1,)
#   {'a': 2}
#   {'kwargs': {'a': 2}, 'args': (1,)}      