# <<<<Lists and the random module>>>>
from random import *

L = [num for num in range(33)]

# picks a random item from L
rand_num = choice(L)

# picks a group of n random items from L
group = sample(L, 8)
# =======================================================
# <<<<split>>>>
s = 'Hi! This is a test.'
words = s.split()
print(words)

s = '1-800-271-8281'
numbers = s.split('-')
print(numbers)

# =======================================================
# <<<<join>>>>
# Convert list of Strings to single String
L = ["1", "1", "1"]
numbers = ''.join(L)
print(numbers)

numbers = ' '.join(L)
print(numbers)

numbers = ', '.join(L)
print(numbers)

numbers = '-'.join(L)
print(numbers)

# Convert String to list of String
s = 'Hi! This is a test.'
chars = list(s)
print(chars)
# =======================================================

# <<<<List comprehensions>>>>

#  create the list [0,1,2,3,4]
L = [num for num in range(5)]

# create the list [[0, 0], [0, 1], [1, 0], [1, 1]]
L = [[i, j] for i in range(2) for j in range(2)]

# Examples
# Write a program that generates a list L of 50 random numbers between 1 and 100
L = [randint(1, 101) for i in range(50)]

# Replace each element in a list L with its square.
L = [num ** 2 for num in L]

# Count how many items in a list L are greater than 50
len([num for num in L if num > 50])

# Given a list L that contains numbers between 1 and 100, create a new list whose first
# element is how many ones are in L, whose second element is how many twos are in L, etc.
freq = [L.count(i) for i in range(1, 101)]

# Suppose we have a list whose elements are lists of size 2, like below: L = [[1,2], [3,4], [5,6]]
# flip the order of the entries in the lists.
L = [[1,2], [3,4], [5,6]]
flip = [[y, x] for x,y in L]
# =======================================================
# <<<<Two-dimensional lists>>>>

# Create a list of zeroes with 100 rows and 50 columns.
L = [[0]*50 for i in range(100)]

# Access an element
element = L[1][0]

# printing with loops
for r in range(len(L)):
    for c in range(len(L[0])):
        print(L[r][c], end=' ')
    print('\n')

# printing with pprnit functiom
from pprint import pprint 
pprint(L)

# Counts how many entries in a 10 × 5 list are even.
count = sum(1 for i in range(10) for j in range(5) if L[i][j] % 2 == 0)

# Create a 5 × 5 × 5 list

L = [[[0] * 5 for i in range(5)] for j in range(5)]
