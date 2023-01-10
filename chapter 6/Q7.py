"""
7. Write a program that asks the user to enter a word and determines whether the word is a
palindrome or not. A palindrome is a word that reads the same backwards as forwards
"""
word = input("Enter a word: ")
if word == word[ : : -1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")

