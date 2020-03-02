import math
import date


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


def dateGet(date1, date2):
    dif = date2 - date1
    return abs(dif).days


def check_dateGet():
    date1 = date(01,02,2020)
    date2 = date(01,13,2020)
    result = dateGet(date1, date2)
    assert(result == 11)
