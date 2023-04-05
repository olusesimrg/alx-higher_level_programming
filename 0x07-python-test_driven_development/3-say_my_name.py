#!/usr/bin/python3

"""Prototype: def say_my_name(first_name, last_name=""):
    both the argument must be str
    one of the argument much be a str
    raise alarm if not str
"""


def say_my_name(first_name, last_name=""):
    """set first and last name 
        both the argument must be a str
        Raises:
        TypeError: if either argument is not a string
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError('last_name must be a string')
    elif not(last_name):
        print("My name is {} ".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
