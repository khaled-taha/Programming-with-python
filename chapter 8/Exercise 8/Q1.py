"""
1. Write a program that asks the user to enter some text and then counts how many articles are
in the text. Articles are the words 'a', 'an', and 'the'.
"""

text = input('Enter some text: ')
print('a: ', text.count('a'))
print('an: ', text.count('an'))
print('and: ', text.count('and'))

