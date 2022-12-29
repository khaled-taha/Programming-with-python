"""
8. Write a program that simulates drawing names out of a hat. In this drawing, the number of
hat entries each person gets may vary. Allow the user to input a list of names and a list of
how many entries each person has in the drawing, and print out who wins the drawing.
"""
names = []
while True:
    name = input('Enter a name: ')
    if name == '':
        break
    names.append(name)


entries = []
for i in range(len(names)):
    entries.append(eval(input('Enter the number of entries: ')))

print("winner: ", names[entries.index(max(entries))])

