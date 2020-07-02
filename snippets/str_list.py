#
# difference between 'is' and '=='
#

first = "python"
second = "python"

print(first is second)
# True
print(first == second)
# True

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
print(list1 is list2)
# False
print(list1 == list2)
# True

a = 4 < 5 < 6
b = (6 > 5) > 4
print(a, b)
