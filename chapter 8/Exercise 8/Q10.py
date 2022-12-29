"""
10. Write a censoring program. Allow the user to enter some text and your program should print
out the text with all the curse words starred out. The number of stars should match the length
of the curse word. For the purposes of this program, just use the“curse” words darn, dang,
freakin, heck, and shoot. Sample output is below:

Enter some text: Oh shoot, I thought I had the dang problem
figured out. Darn it. Oh well, it was a heck of a freakin try.
Oh *****, I thought I had the **** problem figured out.
**** it. Oh well, it was a **** of a ****** try.
"""

text = input('Enter some text: ').split()
for i in range(len(text)):
    if text[i].__contains__('dran'):
        text[i] = text[i].replace('dran', '*' * 4)
    elif text[i].__contains__('dang'):
        text[i] = text[i].replace('dang', '*' * 4)
    elif text[i].__contains__('freakin'):
        text[i] = text[i].replace('freakin', '*' * 7)
    elif text[i].__contains__('heck'):
        text[i] = text[i].replace('heck', '*' * 4)
    elif text[i].__contains__('shoot'):
        text[i] = text[i].replace('shoot', '*' * 5)


print(' '.join(text))
