# Ex 14

"""
14. Write a program that asks the user to enter a length in feet. The program should then give
the user the option to convert from feet into inches, yards, miles, millimeters, centimeters,
meters, or kilometers. Say if the user enters a 1, then the program converts to inches, if they
enter a 2, then the program converts to yards, etc. While this can be done with if statements,
it is much shorter with lists and it is also easier to add new conversions if you use lists
"""


# inches = feet * 12
# yards = feet / 3
# miles = feet / 5280
# millimeters = feet * 304.8
# centimeters = feet * 30.48
# meters = feet * 0.3048
# kilometers = feet / 3280.84

feet = eval(input('Enter a length in feet: '))
units = [feet * 12, feet / 3, feet / 5280, feet * 304.8, feet * 30.48, feet * 0.3048, feet / 3280.84]

print('Choose an option : ')
print("1 - inches")
print("2 - yards")
print("3 - miles")
print("4 - millimeters")
print("5 - centimeters")
print("6 - meters")
print("7 - kilometers")

option = 0
while option < 1 or option > 7:
    option = eval(input('Enter an option: '))
    if option < 1 or option > 7: print('Invalid Option')

print('Convertion: ', units[option])