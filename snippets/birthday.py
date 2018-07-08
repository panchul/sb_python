
# Simple birthday attack calculator(from wikipedia.org).
#And you can run in a REPL like so:
#$ python -i birthday.py
#>>> birthday(-15, 128)
#824963474247.1193
#>>> birthday(-6, 32)
#92.68192319417072

from math import log1p, sqrt

def birthday(probability_exponent, bits):
    probability = 10. ** probability_exponent
    outputs     =  2. ** bits
    return sqrt(2. * outputs * -log1p(-probability))

print birthday(-15, 128)
# 824963474247.1193

print birthday(-6, 32)
#92.68192319417072