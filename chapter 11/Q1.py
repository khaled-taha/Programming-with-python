"""
1. Write a program that repeatedly asks the user to enter product names and prices. Store all
of these in a dictionary whose keys are the product names and whose values are the prices.
When the user is done entering products and prices, allow them to repeatedly enter a product
name and print the corresponding price or a message if the product is not in the dictionary.
"""

produts = {}

while True:
    product = input('Enter the product name: ')
    if product == '':
        break
    price = eval(input('Enter the product price: '))
    produts[product] = price

print(produts)

while True:
    product = input('Enter the product name: ')
    if product == '':
        break
    elif product in produts:
        print('Product Name: ', product)
        print('product Price: ', produts[product])
    else:
        print('No Result')

        