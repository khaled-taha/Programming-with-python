"""
17. Write a program that finds the average of all of the entries in a 4 × 4 list of integers
"""

L = [[eval(input('Enter a number: ')) for i in range(4)] for j in range(4)]

avg = sum(i for list in L for i in list) / 16
print(avg)

