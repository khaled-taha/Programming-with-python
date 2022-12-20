# Ex 5

"""
5. Ask the user to enter a list of strings. Create a new list that consists of those strings with their
first characters removed.
"""

print('Enter a list of strings. Strings must be in one line and separated by a space')
s = input()
strings = s.split(' ')
strings = [string.replace(string[0], '') for string in strings]
