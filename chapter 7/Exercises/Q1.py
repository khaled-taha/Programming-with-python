# Ex 1

print('Enter a list of integers')
L = []
size = eval(input('Enter the list size: '))
while size != 0:
    L.append(eval(input('Enter the number: ')))
    size -= 1

# (a) Print the total numbers in the list
print('Number: ', L)

# (b) print the last number in the list
print('Last number', L[-1])

# (c) print the list in reverse order
print('List in reverse order',  L[-1: : -1])

# (d) Print Yes if the list contains a 5 and No otherwise
if 5 in L:
     print('yes')
else:
     print('No')


# (e) Print the number of fives in the list
print(L.count(5))

# (f) Remove the first and last items from the list, sort the remaining items, and print the
# result
L = L[1:-1]
L.sort()
print(L)

# (g) Print how many integers in the list are less than 5

# way 1
print(len([number for number in L if number < 5]))

# way 2
print(sum([1 if num < 5 else 0 for num in L]))

