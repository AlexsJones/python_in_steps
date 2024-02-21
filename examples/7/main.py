# This file will demonstrate python I/O which means intercation with the user
#
# You can use the input() function to get input from the user
# For example:
#
username = input("Enter username:")
print("Username is: " + username)

# You can also use the print() function to output data to the user
# For example:

print("Hello, World!")

# You can also use the open() function to open a file
# For example:

file = open("README.md", "r")
# print out the last line
print(file.readlines()[-10])
file.close()
