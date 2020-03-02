import math


def firstrun():
    return "success"


def circleArea(radius):
    squared = radius ** 2
    return math.pi * squared


def check_circleArea(result):
    result = circleArea(3)
    assert(result == 28.27)
