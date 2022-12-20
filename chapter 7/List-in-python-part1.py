
# <<<<List (Basics)>>>>

# Create a List: 
L = [1, 2, 3]

# read an element in the list
element = L[0]

# Update an item
L[0] = 0

# delete an element
del(L[0])

# print the list
print(L)

# get the length of the list
print(len(L))

# Loop over the list:
for member in L:
    print(member * 2)

for i in range(len(L)):
    print(L[i])
# Condition with list

number = 2
if number in L: print('{} is in the List'.format(number))

if number + 2 not in L: print('{} is not in the List'.format(number + 2))

# Operators 
# The + operator adds one list to the end of another. 
# The * operator repeats a list.
new_list = L + [4, 5] * 2 
print(new_list)

# =============================================================================

# <<<<Built-in functions>>>>:

# get the length of the list: 
length = len(L)

# get the summation of all items in the list
summation = sum(L)

# get the average of all items in the list
ave = sum(L) / len(L)

# get the minimum of the items in the list
min_item = min(L)

# get the maximum of the items in the list
max_item = max(L)

# =============================================================================

# <<<<List Methods>>>>

# How to Add new item?
L.append(0)

# How to sort the list?
L.sort() # In ASC By default

# Sort the list in Descending order
L.sort(reverse=True)


"""
count(x)    :returns the number of times x occurs in the list
index(x)    :returns the location of the first occurrence of x
reverse()   :reverses the list
remove(x)   :removes first occurrence of x from the list
pop(p)      :removes the item at index p and returns its value
insert(p,x) :inserts x at index p of the list
"""
# =============================================================================

# <<<<Examples>>>>

# Write a program that generates a list L of 50 random numbers between 1 and 100
from random import randint
L = [randint(1, 100) for i in range(50)]

# Given a list L that contains numbers between 1 and 100, create a new list whose first
# element is how many ones are in L, whose second element is how many twos are in L, etc.

freq = []
for i in range(1, 101):
    freq.append(L.count(i))

# sort on the second character of each word in the last
words = ["aa", "ab", "ac", "ba", "cb", "ca"]
def select_second_character(word):
        return word[1]

words = sorted(words, key=select_second_character)

print(words)
