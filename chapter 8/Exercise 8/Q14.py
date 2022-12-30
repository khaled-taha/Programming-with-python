"""
14. Use a list comprehension to produce a list that consists of all palindromic numbers between
100 and 1000.
"""
print([i for i in range(100, 10001) if str(i) == str(i)[: : -1]])

