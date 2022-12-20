# Ex 2

"""
Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.
(d) Print the second largest and second smallest entries in the list
(e) Print how many even numbers are in the list
"""

from random import randint
L = [randint(1, 100) for i in range(21)]

# A
print(L)

# B
print('{:0.2f}'.format(sum(L) / len(L)))

# C
L.sort()
print('Largest: ', L[-1])
print('Smallest: ', L[0])

# D
print('Second Largest: ', L[-2])
print('Second Smallest: ', L[1])

# E
print(sum([1 if num % 2 == 0 else 0 for num in L]))
