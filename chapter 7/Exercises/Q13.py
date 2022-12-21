# EX 13

"""
13. Write a program that removes any repeated items from a list so that each item appears at most
once. For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0]
"""

L = [1,1,2,3,4,3,0,0]

# Way 1
# L = list(set(L))
# print(L)

# way 2
# M = []
# for num in L:
#     if num not in M:
#         M.append(num)
# print(M)

# Way 3
L.sort()
length = len(L)
M = [L[0]]
for i in range(1, length):
    if L[i] != L[i - 1]: M.append(L[i])
print(M)
