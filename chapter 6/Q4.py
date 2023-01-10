"""
4. Write a program that asks the user to enter a word and prints out whether that word contains
any vowels.
"""

word = input('Enter a word: ').upper()
containVowels = word.find('A') or word.find('E') or word.find('I') or word.find('O') or word.find('U')
print(containVowels)