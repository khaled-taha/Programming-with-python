"""
5. Write a program that asks the user to enter a string. The program should create a new string
called new_string from the user’s string such that the second character is changed to an
asterisk and three exclamation points are attached to the end of the string. Finally, print
new_string. Typical output is shown below:

Enter your string: Qbert
Q*ert!!!
"""
original_string = input('Enter a string: ')
new_string = original_string[0] + '*' + original_string[2: ] + '!!!'
print(new_string)

