"""
15. Use a list comprehension to create the list below, which consists of ones separated by increasingly many zeroes.
The last two ones in the list should be separated by ten zeroes.
[1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]
"""

L = [['1'] + (['0'] * i) for i in range(11)]
print([item for list in L for item in list])

