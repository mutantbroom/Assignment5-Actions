import math


def firstrun():
    return "success"


def circleArea(radius):
    squared = radius ** 2
    return math.pi * squared


def check_circleArea():
    result = circleArea(3)
    assert(result == 28.27)


def listGet(list1):
    elements = [list1[0], list1[-1]]
    return elements


def check_listGet():
    list1 = [2, 3, 4, 5]
    result = listGet(list1)
    assert(result == [2, 5])
