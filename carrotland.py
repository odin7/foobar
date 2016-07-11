'''
Carrotland
==========

The rabbits are free at last, free from that horrible zombie science experiment. They need a happy, safe home, where they can recover.

You have a dream, a dream of carrots, lots of carrots, planted in neat rows and columns! But first, you need some land. And the only person who's selling land is Farmer Frida. Unfortunately, not only does she have only one plot of land, she also doesn't know how big it is - only that it is a triangle. However, she can tell you the location of the three vertices, which lie on the 2-D plane and have integer coordinates.

Of course, you want to plant as many carrots as you can. But you also want to follow these guidelines: The carrots may only be planted at points with integer coordinates on the 2-D plane. They must lie within the plot of land and not on the boundaries. For example, if the vertices were (-1,-1), (1,0) and (0,1), then you can plant only one carrot at (0,0).

Write a function answer(vertices), which, when given a list of three vertices, returns the maximum number of carrots you can plant.

The vertices list will contain exactly three elements, and each element will be a list of two integers representing the x and y coordinates of a vertex. All coordinates will have absolute value no greater than 1000000000. The three vertices will not be collinear.
'''


from math import ceil, floor


def answer(vertices):
    vertices = sorted(vertices)
    # select shotest axis y vs x
    alt_vertices = sorted(vertices, key=lambda a: a[1])
    if abs(vertices[0][0] - vertices[2][0]) > abs(alt_vertices[0][1] - alt_vertices[2][1]):
        vertices = [list(reversed(a)) for a in alt_vertices]
    carrots_cnt = 0
    # no carrots to plant if x or y stretch is less than 2
    if vertices[2][0] - vertices[0][0] < 2 or vertices[2][1] - vertices[0][1] < 2:
        return carrots_cnt
    # calculate carrots for the leftmost part of the triangle
    equations = [get_equation(vertices[0], a) for a in vertices[1:]]
    carrots_cnt += calc_carrots(rng=range(vertices[0][0] + 1, vertices[1][0]), eqtns=equations)
    # calculate carrots for the rightmost part of the triangle
    equations = [get_equation(vertices[2], a) for a in vertices[:-1]]
    carrots_cnt += calc_carrots(rng=range(vertices[1][0], vertices[2][0]), eqtns=equations)
    return carrots_cnt


def calc_carrots(rng, eqtns):
    # calculates carrots count for a given pair of equations and x span
    total_carrots = 0
    for x_val in rng:
        y = sorted([get_y(x_val, a) for a in eqtns])
        ubound = floor(y[1]) - (0 if floor(y[1]) < y[1] else 1)
        lbound = ceil(y[0]) + (0 if ceil(y[0]) > y[0] else 1)
        total_carrots += ubound - lbound + 1
    return total_carrots


def get_equation(p1, p2):
    # returns a tuple with parameters of a linear equation
    # xcf * x +  ycf * y + fval = 0
    xcf = p1[1] - p2[1]
    ycf = p2[0] - p1[0]
    fval = p1[0] * p2[1] - p2[0] * p1[1]
    return (xcf, ycf, fval)


def get_y(x, func):
    # calculates y for a given x and equation func
    return -(func[0] * x + func[2]) / func[1]
