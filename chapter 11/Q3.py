"""
3. For this problem, use the dictionary from the beginning of this chapter whose keys are month
names and whose values are the number of days in the corresponding months.
(a) Ask the user to enter a month name and use the dictionary to tell them how many days
are in the month.
(b) Print out all of the keys in alphabetical order.
(c) Print out all of the months with 31 days.
(d) Print out the (key-value) pairs sorted by the number of days in each month
(e) Modify the program from part (a) and the dictionary so that the user does not have to
know how to spell the month name exactly. That is, all they have to do is spell the first
three letters of the month name correctly.
"""

days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30,
        'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}

# a)
month = input('Enter the name of month: ')
print(f'days of {month} is: ', days[month])

# b)
dic = dict(sorted(days.items()))
print(dic)

# c)
print([month for month in days if days[month] == 31])

# d)
print(dict(sorted(days.items(), key= lambda item:item[1])))

# e)
chars = input('Enter the first three characters of the month: ')
for month in days:
    if month[0:3] == chars:
        print(f'days of {month} is: ', days[month])
        
