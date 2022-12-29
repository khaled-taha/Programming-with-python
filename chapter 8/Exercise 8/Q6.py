"""
6. Write a simple lottery drawing program. The lottery drawing should consist of six different
numbers between 1 and 48.
"""

from random import randint, sample
numbers = [randint(1, 48) for i in range(48)]
print(sample(numbers, 6))
