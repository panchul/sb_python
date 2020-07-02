# This is how it works:
# $ python life.py
# set([(0, 1), (2, 0), (1, 0), (1, -1), (2, 1)])
# set([(0, 0), (2, -1), (1, -1), (2, 1), (2, 0)])
# set([(3, 0), (2, 0), (2, -1), (1, -1), (1, 1)])
# set([(3, 0), (2, -1), (1, -1), (3, -1), (2, 1)])
# set([(3, 0), (1, 0), (2, -2), (3, -1), (2, -1)])
# set([(3, 0), (2, -2), (1, -1), (3, -1), (3, -2)])
# set([(2, 0), (2, -2), (3, -2), (3, -1), (4, -1)])
# set([(3, 0), (2, -2), (4, -1), (3, -2), (4, -2)])
# set([(4, -2), (2, -1), (4, -1), (3, -2), (3, -3)])
# set([(4, -3), (2, -2), (4, -2), (4, -1), (3, -3)])
#

import itertools
# from itertools import *


def neighbors(point):
    x, y = point
    yield x+1, y
    yield x-1, y
    yield x, y+1
    yield x, y-1
    yield x+1, y+1
    yield x-1, y+1
    yield x+1, y-1
    yield x-1, y-1


def advance(board):
    newstate = set()
    # print "board is "
    # print board
    recalc = board | set(itertools.chain(*map(neighbors, board)))
    # print "recalc is "
    # print recalc
    for point in recalc:
        count = sum((neigh in board)
                    for neigh in neighbors(point))
        if count == 3 or (count == 2 and point in board):
            newstate.add(point)
    return newstate


def pretty_print(board):
    print(board)


glider = set([(0, 0), (1, 0), (2, 0), (2, 1), (1, 2)])
for i in range(10):
    glider = advance(glider)
    pretty_print(glider)

