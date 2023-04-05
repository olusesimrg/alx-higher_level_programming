#!/usr/bin/python3
""" add a and b
    raise Error if not integer or float:
"""

def add_integer(a, b=98):
    """
    add 2 inerger a and b
    check if a and b are float or int, else raise alarm
    if a or b is float, cast value to integer
    """
    if (type(a) not in [int, float]):
        raise TypeError("a must be an integer")
    elif (type(b) not in [int, float]):
        raise TypeError("b must be integer")
    return (int(a) + int(b))
