"""
18. Write a program that creates a 10×10 list of random integers between 1 and 100. Then do the
following:
(a) Print the list.
(b) Find the largest value in the third row.
(c) Find the smallest value in the sixth column.
"""

from random import randint
L = [[randint(1, 100) for i in range(10)] for j in range(10)]

# a)

for i in range(10):
    for j in range(10):
        print(L[i][j], end=' ')
        if j == 9:
            print()

# b)
print(max(L[2]))

# c)
print(min(L[5]))


