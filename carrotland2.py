'''
Carrotland
==========

The rabbits are free at last, free from that horrible zombie science experiment. They need a happy, safe home, where they can recover.

You have a dream, a dream of carrots, lots of carrots, planted in neat rows and columns! But first, you need some land. And the only person who's selling land is Farmer Frida. Unfortunately, not only does she have only one plot of land, she also doesn't know how big it is - only that it is a triangle. However, she can tell you the location of the three vertices, which lie on the 2-D plane and have integer coordinates.

Of course, you want to plant as many carrots as you can. But you also want to follow these guidelines: The carrots may only be planted at points with integer coordinates on the 2-D plane. They must lie within the plot of land and not on the boundaries. For example, if the vertices were (-1,-1), (1,0) and (0,1), then you can plant only one carrot at (0,0).

Write a function answer(vertices), which, when given a list of three vertices, returns the maximum number of carrots you can plant.

The vertices list will contain exactly three elements, and each element will be a list of two integers representing the x and y coordinates of a vertex. All coordinates will have absolute value no greater than 1000000000. The three vertices will not be collinear.
'''

from math import sqrt
from fractions import gcd


def answer(vertices):
    x = [min([a[0] for a in vertices]), max(a[0] for a in vertices)]
    y = [min([a[1] for a in vertices]), max(a[1] for a in vertices)]
    # points in full rectangle
    res = (x[1] - x[0] - 1) * (y[1] - y[0] - 1)
    print(res)
    for i in range(0, 3):
        point1 = vertices[i]
        point2 = vertices[(i + 1) % 3]
        if not is_axis_parallel(p1=point1, p2=point2):
            lpc = latice_points_count(p1=point1, p2=point2)
            print(lpc)
            res -= lpc + ((abs(point1[0] - point2[0]) - 1) * (abs(point1[1] - point2[1]) - 1) - lpc) / 2
            if point1[0] not in x and point1[1] not in y:
                point3 = vertices[(i + 2) % 3]
                rec1 = [point2[0], point3[1]]
                rec2 = [point3[0], point2[1]]
                closest_corner = sorted([rec1, rec2], key=lambda a: get_line_len(point=point1, rect=a))[0]
                res -= abs(closest_corner[0] - point1[0]) * abs(closest_corner[1] - point1[1])
    return int(res)


def latice_points_count(p1, p2):
    # http://math.stackexchange.com/questions/628117 + exclude endpoints
    return abs(gcd((p2[0] - p1[0]), (p2[1] - p1[1]))) - 1


def is_axis_parallel(p1, p2):
    return p1[0] == p2[0] or p1[1] == p2[1]


def get_line_len(point, rect):
    return sqrt(pow(point[0] - rect[0], 2) + pow(rect[1] - point[1], 2))
