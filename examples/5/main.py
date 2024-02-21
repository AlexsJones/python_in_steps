# This file explains what packages are in Python
# 
# A package is a way of organizing related modules into a single directory hierarchy.
# Packages are namespaces which contain multiple packages and modules themselves. 
# They are simply directories, but with a twist.
#   
# The twist is, each package in Python is a directory which MUST contain a special file called __init__.py.
# This file can be empty, and it indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported.

# This file shows you how to declare and use a python function

# Here is an example directory tree
# root/ 
#     main.py
#     submodule/
#         __init__.py
#         example.py
#         example2.py
#         example3.py

# To use the module example.py in main.py you would do the following:
# import submodule.example
#
# submodule.example.Foo()