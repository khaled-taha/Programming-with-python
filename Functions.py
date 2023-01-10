# Create a function with no argument
def hello_world():
    print('Hello World')

# Create a function with arguments
def details(name, age):
    print('Name: {}, age: {}'.format(name, age))

# Create a function with return value
def calculate_temp(temp):
    return temp*9/5+32

# Create a function with default argument
def print_message(message='Hello!'):
    print(message)
# =================================================

# Scopes in functions:
"""
Not all objects are accessible everywhere in a script
Scope - part of the program where an object or name may be
accessible
1 - Global scope - de,ned in the main body of a script
2 - Local scope - de,ned inside a function
3 - Built-in scope - names in the pre-de,ned built-ins module
"""

# local variable: new_val
def square(value):
    """new_val: local variable"""
    new_val = value ** 2
    return new_val


new_val = 10
def square(value):
    """Returns the square of a number."""
    new_val = value ** 2
    return new_val

print(square(3)) # 9
print(new_val)   # 10

# ############################
# global variable: new_val

new_val = 10
def square(value):
    """Returns the square of a number."""
    global new_val
    new_val = new_val ** 2
    return new_val

print(square(3)) # 100
print(new_val)   # 100

# =================================================

# Advanced Functions:

# positional and Keyword arguments
def details(name, age):
    print('Name: {}, age: {}'.format(name, age))

# positional arguments: We must put the values in their natural order
details('khaled', 24)

# Keyword arguments
"""
It is not necessary to care about the order, but the keyword must be the same as the parameter
"""
details(age=24, name='khaled')
# -----------------------------------------------------
# Argument packing and Argument Unpacking

# Argument packing:
"""
An unlimited number of values can be passed
When passing it is saved in Tuple
"""
def summation(*number):
    total = sum(number)
    return total

print(summation(1, 2, 3))

# Argument Unpacking

numbers = [1, 2, 3]
print(summation(*numbers))

numbers = 1, 2, 3
print(summation(*numbers))
# -----------------------------------------------------

# Dictionary Packing and Dictionary Packing

# Dictionary Packing
"""
1 - We can pass number of keyword arguments as a dictionary
2 - the name of keyword is the same name of the key in the dict
3 - the value of keyword is the same value in the dict
4 - we use ** to applay packing
"""

def info(**kwargs):
    print('Name: {}, age: {}'.format(kwargs['name'], kwargs['age']))

info(name='khaled', age=24)

# Dictionary Packing
def info(name, age):
    print('Name: {}, age: {}'.format(name, age))

details = {'name':'khaled', 'age':24}
info(**details)