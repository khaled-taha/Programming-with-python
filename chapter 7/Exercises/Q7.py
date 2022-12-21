# Ex 7

"""
7. Write a program that takes any two lists L and M of the same size and adds their elements
together to form a new list N whose elements are sums of the corresponding elements in L
and M. For instance, if L=[3,1,4] and M=[1,5,9], then N should equal [4,6,13]
"""
print('Create two lists with the same size')
size = eval(input('Enter the size of the lists: '))

print(f'Create the first list with size {size}: ')
L = []
for i in range(size):
    L.append(eval(input(f'Enter number {i + 1} : ')))

print(f'Create the second list with size {size} : ')
M = []
for i in range(size):
    M.append(eval(input(f'Enter number {i + 1} : ')))

print('The result: ')
N = [L[i]+M[i] for i in range(size)]
print(N)