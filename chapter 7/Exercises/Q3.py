# Ex 2

"""
3. Start with the list [8,9,10]. Do the following:
(a) Set the second entry (index 1) to 17
(b) Add 4, 5, and 6 to the end of the list
(c) Remove the first entry from the list
(d) Sort the list
(e) Double the list
(f) Insert 25 at index 3
"""

L = [8, 9, 10]

# A
L[1] = 17

# B
L = L + [4, 5, 6]

# C
L.remove(L[0])

# D
L.sort()

# E
L = L * 2

# F
L.insert(3, 25) # Note: insert(index, entry)
print(L)
