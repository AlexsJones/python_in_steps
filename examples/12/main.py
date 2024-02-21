# This file explains how to profile in Python
#
# Profiling is a way to measure the performance of your code
#
# For example:
import cProfile

def my_function():
    print("Hello, World!")

cProfile.run('my_function()')
# This will output the following:
# Hello, World!
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 main.py:3(my_function)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#
# You can also use the following command to profile your code:
# python -m cProfile main.py
# This will output the following:
# Hello, World!