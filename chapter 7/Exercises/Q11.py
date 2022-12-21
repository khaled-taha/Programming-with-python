# EX 11

"""
11. Using a for loop, create the list below, which consists of ones separated by increasingly many
zeroes. The last two ones in the list should be separated by ten zeroes.
[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]
"""

L = []

for i in range(1001):
    L.append(1)
    L = L + [0] * i

print(L)