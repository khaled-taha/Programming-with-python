"""
2. Write a program that allows the user to enter five numbers (read as strings). Create a string
that consists of the user's numbers separated by plus signs. For instance, if the user enters 2,
5, 11, 33, and 55, then the string should be '2+5+11+33+55'.
"""
numbers = '+'.join([input('Enter a number: ') for i in range(5)])
print(numbers)

