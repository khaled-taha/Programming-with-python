"""
12. Write a program that gets a string from the user containing a potential telephone number.
The program should print Valid if it decides the phone number is a real phone number, and
Invalid otherwise. A phone number is considered valid as long as it is written in the form
abc-def-hijk or 1-abc-def-hijk. The dashes must be included, the phone number should contain
only numbers and dashes, and the number of digits in each group must be correct. Test your
program with the output shown below.
Enter a phone number: 1-301-447-5820
Valid
Enter a phone number: 301-447-5820
Valid
Enter a phone number: 301-4477-5820
Invalid
Enter a phone number: 3X1-447-5820
Invalid
Enter a phone number: 3014475820
Invalid
"""

phone_number = input('Enter the phone number: ').split('-')
length = len(phone_number)

if length != 3 and length != 4:
    print('Invalid')
    quit(0)

if phone_number[0] == '1':
    if not (phone_number[1].isnumeric() and len(phone_number[1]) == 3
       and phone_number[2].isnumeric()  and len(phone_number[2]) == 3
       and phone_number[3].isnumeric()  and len(phone_number[3]) == 4):
        print('Invalid')
        quit(0)
else:
    if not (phone_number[0].isnumeric() and len(phone_number[0]) == 3
       and phone_number[1].isnumeric()  and len(phone_number[1]) == 3
       and phone_number[2].isnumeric()  and len(phone_number[2]) == 4):
        print('Invalid')
        quit(0)

print('Valid')



    
