import math


def firstrun():
    return "success"


def circleArea(radius):
    squared = radius ** 2
    return math.pi * squared


def check_circleArea(result):
    result = circleArea(3)
    assert(result == 28.27)
    

def listGet(list1):
    elements = [list1[0], list1[-1]]
    return elements
