# This file shows you how to throw and catch exceptions in Python
#
# Exceptions are used to handle errors in a program
# Try and except blocks are used to catch exceptions
# For example:
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
# This will output the following:
# Handling run-time error: division by zero
#
# You can also catch multiple exceptions at once
# For example:
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
except:
    print('Caught an exception')
# This will output the following:
# Handling run-time error: division by zero
#
# You can also catch all exceptions at once
# For example:
try:
    this_fails()
except:
    print('Caught an exception')
# This will output the following:
# Caught an exception
