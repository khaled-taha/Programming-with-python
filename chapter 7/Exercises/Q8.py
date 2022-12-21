# EX 8

"""
8. Write a program that asks the user for an integer and creates a list that consists of the factors
of that integer
"""

number = eval(input('Enter an integer: '))
L = [num for num in range(1, number // 2 + 1) if number % num == 0] + [number]
print(L)

