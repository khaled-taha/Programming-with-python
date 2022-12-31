"""
4. Write a program that uses a dictionary that contains ten user names and passwords. The
program should ask the user to enter their username and password. If the username is not in
the dictionary, the program should indicate that the person is not a valid user of the system. If
the username is in the dictionary, but the user does not enter the right password, the program
should say that the password is invalid. If the password is correct, then the program should
tell the user that they are now logged in to the system
"""

users = {"khaled":123, "Mohamed":456, "Ahmed":789}
username = input('Enter the username: ')
password = eval(input('Enter the password: '))


if not username in users:
    print('Invalid user of the system')
elif not password in users.values():
    print('Invalid Password')
else:
    print('logged in to the system')
