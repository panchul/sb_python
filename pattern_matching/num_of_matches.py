#
# $ echo sometext more sometext | python -i num_of_matches.py 
# Number of matches : 2
# >>> 
#

import re

Test_String = raw_input()
Regex_Pattern = r'sometext'
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))
