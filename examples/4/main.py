# This file shows you how to use Python modules
#
# A module allows you to logically organize your Python code. 
# Grouping related code into a module makes the code easier to understand and use. 
# A module is a Python object with arbitrarily named attributes that you can bind and reference.

# Simply, a module is a file consisting of Python code. A module can define functions, classes and variables.
# A module can also include runnable code.

# For example, if you had a file called mymodule.py containing the following:
def my_function():
    print("Hello, World!")

# You could import the module as follows:
# import mymodule


# It's hard to show in this single file as an example, so let's import another file
import example

example.Foo()