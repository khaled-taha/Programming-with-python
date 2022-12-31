# <<<<Dictionary>>>>

# create a dictionary {key: value}
dic = {'A': 1, 'B': 2}

# Access the value by the key
print(dic['A'])

# update value
dic['A'] = 3

# delete value
del(dic['A'])

# printing
print(dic)

# conditions with dictionary
key = 'B'
if key in dic:
    print('The value of the key {} is {}'. format(key, dic[key])) 

# loop over the dictionary
# way 1
for key in dic:
    print(dic[key])

# way 2
for key, value in dic.items():
    print(key, ' : ', value)

# print values only
for value in dic.values():
    print(value)

# =====================================================

# create lists from the dictionary

# List of keys
L = list(dic)

# list of values
L = list(dic.values())

# list of (kay, value)
L = list(dic.items())

    #loop over this list 
for k, v in L:
    print(k, v)

    # create a dictionary from this list
dic = dict(L)
# =====================================================

# create a dictionary {word: length of word} from ths String: khaled Taha Abd El-fattah
s = 'Khaled Taha Abd El-fattah'

# create a list of word
words = s.split()

# create the dictionary
dic = {word: len(word) for word in words}

print(dic)
# =====================================================
# Sort the dictionary

people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

# Sort by key
people = dict(sorted(people.items()))
# {1: 'Jill', 2: 'Jack', 3: 'Jim', 4: 'Jane'}

 # Sort by value
people = dict(sorted(people.items(), key=lambda item: item[1]))
# {2: 'Jack', 4: 'Jane', 1: 'Jill', 3: 'Jim'}

# =====================================================
# <<<<Examples>>>>

# Sort the values of first list using second list
list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [0,   1,   1,    0,   1,   2,   2,   0,   1]

dic = {}

# Addition of two list in one dictionary
dic = {list1[i]:list2[i] for i in range(len(list1))}

# sorting of dictionary based on value
dic = {k: v for k, v in sorted(dic.items(), key=lambda item:item[1])}

# Element addition in the list
list1 = [item for item in dic]
print(list1)
# =====================================================

# Count of how many time each char appears in : s = 'Khaled Taha Abd El-fattah'
s = 'Khaled Taha Abd El-fattah'
s = s.replace('', ' ')

dic = {}
for ch in list(s):
    if ch in dic:
        dic[ch] += 1
    else:
        dic[ch] = 1


print(dic)
# =====================================================

