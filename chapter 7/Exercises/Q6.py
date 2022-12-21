
# EX 6
"""
6. Create the following lists using a for loop.
(a) A list consisting of the integers 0 through 49
(b) A list containing the squares of the integers 1 through 50.
(c) The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z.
"""
L = []

# A
for i in range(0, 50):
    L.append(i)

# B
for i in range(1, 51):
    L.append(i ** 2)

# C
s = 'abcdefghijklmnopqrstuvwxyz';
L = []
for i in range(1, 27):
    L.append(s[i-1] * i)
print(L)