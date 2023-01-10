"""
1. Write a program that asks the user to enter a string. The program should then print the
following:
(a) The total number of characters in the string
(b) The string repeated 10 times
(c) The first character of the string (remember that string indices start at 0)
(d) The first three characters of the string
(e) The last three characters of the string
(f) The string backwards
(g) The seventh character of the string if the string is long enough and a message otherwise
(h) The string with its first and last characters removed
(i) The string in all caps
(j) The string with every a replaced with an e
(k) The string with every letter replaced by a space
"""
name = input('Enter your name: ')

# a)
print(len(name))

# b)
print(name * 10)

# c)
print(name[0])

# d)
print(name[ : 3])

# e)
print(name[-3 : ])

# f)
print(name[ : : -1])

# g)
if len(name) >= 7: print(name[6])

# h)
print(name[1 : -1])

# i)
print(name.upper())

# j)
print(name.replace('a', 'e'))

# k)
print(' ' * len(name))


