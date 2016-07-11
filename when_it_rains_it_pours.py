'''
When it rains it pours
======================

It's raining, it's pouring. You and your agents are nearing the building where
the captive rabbits are being held, but a sudden storm puts your escape plans at
risk. The structural integrity of the rabbit hutches you've built to house the
fugitive rabbits is at risk because they can buckle when wet. Before the rabbits
can be rescued from Professor Boolean's lab, you must compute how much standing
water has accumulated on the rabbit hutches.

Specifically, suppose there is a line of hutches, stacked to various heights and
water is poured from the top (and allowed to run off the sides). We'll assume
all the hutches are square, have side length 1, and for the purposes of this
problem we'll pretend that the hutch arrangement is two-dimensional.

For example, suppose the heights of the stacked hutches are `[1,4,2,5,1,2,3]` (the
hutches are shown below):

    ...X...
    .X.X...
    .X.X..X
    .XXX.XX
    XXXXXXX
    1425123

When water is poured over the top at all places and allowed to runoff, it will
remain trapped at the 'O' locations:

    ...X...
    .XOX...
    .XOXOOX
    .XXXOXX
    XXXXXXX
    1425123

The amount of water that has accumulated is the number of Os, which, in this
instance, is 5.

Write a function called answer(heights) which, given the heights of the stacked
hutches from left-to-right as a list, computes the total area of standing water
accumulated when water is poured from the top and allowed to run off the sides.

The heights array will have at least 1 element and at most 9000 elements. Each
element will have a value of at least 1, and at most 100000.

Test cases
==========

Inputs:

    (int list) heights = [1, 4, 2, 5, 1, 2, 3]

Output:

    (int) 5


Inputs:

    (int list) heights = [1, 2, 3, 2, 1]

Output:

    (int) 0
'''


import random
import time


def timing(f):
    # will only work on 3.3+, use time.clock instead on 2.x
    def wrap(*args):
        time1 = time.process_time()
        ret = f(*args)
        time2 = time.process_time()
        print('function {} took {} ms'.format(f.__name__, (time2 - time1) * 1000.0))
        return ret
    return wrap


@timing
def answer2(heights):
    # this one was good enough to pass the tests, but is not optimal
    res = 0
    max_left = heights[0]
    max_right = max(heights[1:])
    for ind in range(1, len(heights) - 1):
        max_left = max(max_left, heights[ind])
        res += min(max_left, max_right) - heights[ind]
        if max_right == heights[ind]:
            max_right = max(heights[ind + 1:])
    return res


@timing
def answer(heights):
    length = len(heights) - 1
    tops = []
    res = 0
    temp_top = heights[0]
    for i in range(1, length):
        temp_top = max(temp_top, heights[i])
        tops.append(temp_top)

    temp_top = heights[length]
    for i in range(length - 1, 0, -1):
        temp_top = max(temp_top, heights[i])
        res += min(tops[i - 1], temp_top) - heights[i]
    return res


if __name__ == '__main__':
    random.seed()
    a = [random.randint(1, 1000) for b in range(0, 100000)]
    print(answer2(a))
    print(answer(a))
