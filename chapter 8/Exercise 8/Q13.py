"""
13. Let L be a list of strings. Write list comprehensions that create new lists from L for each of the
following.
(a) A list that consists of the strings of s with their first characters removed
(b) A list of the lengths of the strings of s
(c) A list that consists of only those strings of s that are at least three characters long
"""

L = ["Khaled", "Taha", "Mohamed"]

# a) 
M = [x[1:] for x in L]
print(M)

# b)
N = [len(i) for i in L]
print(N)

# c)
P = [i for i in L if len(i) >= 3]
print(P)