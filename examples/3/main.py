# This file will show you how to create a Python class, they are similar to Java and other languages yet have their own qualities

# A very simple class would look something like this:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

# We'll explain why you have to include that "self" as a parameter a little bit later. First, to assign the above class(template) to an object you would do the following:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

# This would create a new instance of the class and assign this object to the local variable myobjectx.
# Lets call the function

myobjectx.function()

# This would print out the message "This is a message inside the class."
# Now the variable "myobjectx" holds an object of the class "MyClass" that contains the variable and the "function" defined within the class called "MyClass".

# Accessing Object Variables

# To access the variable inside of the newly created object "myobjectx" you would do the following:
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")


myobjectx = MyClass()

myobjectx.variable

# So for instance the below would output the string "blah":
print(myobjectx.variable)