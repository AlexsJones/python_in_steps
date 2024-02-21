# This file shows you how to declare and use a python function

# Functions are used to perform a specific task
# In python, you can declare a function using the keyword def
# For example:
def my_function():
    print("Hello, World!")

# You can also pass arguments to a function
    
def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

# You can also return a value from a function
def sum_two_numbers(a, b):
    return a + b

# Lets print out the results of our functions

# print a simple greeting
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print(x)