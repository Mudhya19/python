# Largest Square Inside A Circle
import math


def area_largest_square(r):

    if r == 0:
        return 0

    return math.pi * r ** 2
