"""
7. Write a program that estimates the average number of drawings it takes before the user’s
numbers are picked in a lottery that consists of correctly picking six different numbers that
are between 1 and 10. To do this, run a loop 1000 times that randomly generates a set of
user numbers and simulates drawings until the user’s numbers are drawn. Find the average
number of drawings needed over the 1000 times the loop runs
"""
from random import *
numbers = [i for i in range(1, 11)]

avg = 0

for i in range(1000):
    user_numbers = randint(1, 11)
    lot = choice(numbers)
    if lot == user_numbers:
        avg += 1

print(round(avg / 1000, 4))
