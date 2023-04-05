#!/usr/bin/python3
"""
Prototype: def print_square(size):
    size is the size length of the square
    size must be an integer otherwise raise alarm
    if size < 0 raise valueError
    size float < 0 raise typeError
    """

def print_square(size):
    """
    this function print square
    if size is the size length of the square
    size < 0 and == float and not an int
    raise TypeError: size must be int
    """

    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
     if type(size) != int:
         raise TypeError("size must be an integer")
     if size < 0:
         raise ValueError("size must be >= 0")
     for i in range(size):
         print(size * '#')
