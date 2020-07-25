#
# this will result in an infinite loop, will keep printing:
# x is now:  ['ab', 'bc', 'AB', 'BC', 'AB', 'BC', ...
#

x = ['ab','bc']
for s in x:
    x.append(s.upper())
    print("x is now: ", x)

print("final x is: ", x)
