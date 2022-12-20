# Ex 4

"""
4. Ask the user to enter a list containing numbers between 1 and 12. Then replace all of the
entries in the list that are greater than 10 with 10
"""

L = [num for num in range(1, 13)]
L = [10 if num > 10 else num for num in L]
