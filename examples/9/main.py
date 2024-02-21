# This file shows how generators work in Python

# Generators are a simple way to create iterators using functions. You can also use a generator expression to create a generator.

# For example:
def my_generator():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

a = my_generator()
print(next(a))
print(next(a))
print(next(a))
# This will output the following:
# This is printed first
# 1
# This is printed second
# 2
# This is printed at last
# 3
# You can also use a generator expression to create a generator
# For example:
my_generator = (x*x for x in range(3))
for i in my_generator:
    print(i)

