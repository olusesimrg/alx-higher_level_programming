#!/usr/bin/python3
"""

"""

def say_my_name(first_name, last_name=""):
    """
        Raises:
        TypeError: if either argument is not a string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError('last_name must be a string')
    if not(last_name):
        print("My name is {} ".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
