"""
2. Using the dictionary created in the previous problem, allow the user to enter a dollar amount
and print out all the products whose price is less than that amount.
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
    amount = eval(input('Enter the amount: '))
    if str(amount) == '':
        break
    for product in produts:
        if produts[product] < amount:
            print(product)
    print('===================================')
    
