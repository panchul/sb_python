#
# run is as
# $ python mypass.py
#

import re


# Passwords will contain at least (1) upper case letter
# Passwords will contain at least (1) lower case letter
# Passwords will contain at least (1) number or special character
# Passwords will contain at least (8) characters in length
# Password maximum length is 64
def test_password(password):
    # return password #
    return re.match(r'(?=^.{8,64}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$', password)


print("now lets try it")

print(test_password("govno"))
print(test_password("g2vNoasc34&56"))
print(test_password("govno"))


