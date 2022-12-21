# EX 12

"""
12. Write a program that generates 100 random integers that are either 0 or 1. Then find the
longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.
"""
from random import randint
L = [randint(0, 1) for i in range(20)]
print(L)

counter = 0
largest = 0

for num in L:
    if num == 0: counter += 1
    else: counter = 0
    largest = max(counter, largest)

print(largest)
