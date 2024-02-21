# This file explains how decorators work in Python
#
# Decorators are a way to modify the behavior of a function or a class.
#
# For example:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()
# This will output the following:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
#
# You can also use the @ symbol to use a decorator
# For example:
@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# This will output the following:
# Something is happening before the function is called.
# Hello!