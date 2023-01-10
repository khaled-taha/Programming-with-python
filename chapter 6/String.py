# Strings in python

# create a string in python:
name = 'khaled taha'
name = "khaled Taha"
details = """
name: Khaled Taha,
phone: 011*******
"""
# ==========================================
# convert the input from string to int:
number = eval(input('Enter a number: '))

# get the length of the string:
length = len(name)

# ==========================================

# Concatenation and repetition:
sub1 = 'AB'
sub2 = 'BC'
# create a string ABBCABBC from the sub1 and sub2
sub = (sub1 + sub2) * 2
# ==========================================

# check if this substring in the string or not:
name = 'Khaled Taha'
if 'Khaled' in name:
    print('yes')
# ==========================================
# indexing with string
name = 'Khaled'

print('first char: ', name[0])
print('last char: ', name[-1])
# ==========================================
# Slices if string
# string name[starting location : ending location+1]
letters = 'abcdefghij'

print(letters[ : ])   # abcdefghij
print(letters[ :5])   # abcde (0 ---> 5 - 1)
print(letters[5 : ])  # fghij
print(letters[2 : 5]) # cde

print(letters[1 : 7 : 2]) # bdf (characters from index 1 to 6, by twos)
"""
letters[1] = b
letters[3] = d
letters[5] = f
"""
print(letters[ : : -1]) # reverse the string
# ==========================================

# looping

name = 'khaled'
# print all characters in the name
for i in range(len(name)):
    print(name[i])

for char in name:
    print(char)
# ==========================================

# String methods:
name = 'khaled, taha'

# upper method
name = name.upper()

# lower method
name = name.lower()

# title method: makes each word start with capital letter.
name = name.title()

# count method
spaces = name.count(' ')

# index method
indexOf_K = name.index('K')

# replace method
name = name.replace(' ', '')

# find and rfind

## find: returns the first index of the target in the string
found = name.find('le')

# find method can take a target and the index where we start searching from it
found = name.find('le', 2)

## rfind: retruns the last index of the target in the string
found = name.rfind('h')

# convert the string to a list

letters = 'A, B, C'
L = letters.split()       # split by a space: ['A,', 'B,', 'C']
L = letters.split(',')    # split by a comma: ['A', ' B', ' C']
L = letters.split(',', 1) # split by a comma one time: ['A', ' B, C']

# convert a list to string
list_to_string = ' '.join(L)
list_to_string = ','.join(L)

# String validation

# isalpha method: returns True if every character or a character of the string is a letter
isAlpha = name.isalpha() 
isLetter = name[0].isalpha()

# isalnum: returns True if the string contains letters and numbers only.
# isdigit: returns True if the string contains numbers only.
# istitle: returns True if each word in the string starts with npper case.
# isupper: returns True if all chars in the string are upper case.
# islower: returns True if all chars in the string are lower case. 
# isspace: returns True if all chars in the string are spaces only.
# ==========================================

# remove spaces from string
sentence = '   \n khaled     '.strip() # remove space and new lines from the right and left of the string.
print(sentence, '.')
sentence = '    khaled     '.lstrip()# remove space from the right of the string only.
print(sentence, '.')
sentence = '    khaled     '.rstrip()# remove space from the left of the string only.
print(sentence, '.')
# ==========================================

# format method
first_name = "khaled"
last_name = "taha"
age = 24

details = 'Full Name: {}, {} and the age is {}'.format(first_name, last_name, age)
print(details)
details = 'Full Name: {1}, {0} and the age is {2}'.format(last_name, first_name, age)
print(details)
details = 'Full Name: {fname}, {lname} and the age is {age}'.format(fname = first_name, lname = last_name, age = age)
print(details)
# ==========================================















