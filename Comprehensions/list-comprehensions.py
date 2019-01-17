import random
from functools import reduce

cart = [
    ['Coffee', 7.99, 2],
    ['Bread', 2.99, 1],
    ['Apple', 0.99, 2],
    ['Milk', 4.99, 1],
    ['Cola', 1.99, 4],
]

sales_tax = 0.07

#######################################################    
# cart_subtotal = reduce(lambda x, y : x + y[0] * y[1],
#                         [item[1:] for item in cart],0)

# print(cart_subtotal)

#######################################################

# item_prices = [item[1] for item in cart]

# print(item_prices)

# item_prices_plus_tax = [round(price * (1 + sales_tax), 2)
#                         for price in item_prices]

# print(item_prices_plus_tax)

#######################################################

# cart_item_totals = [item_name + ' ' + str(item_price *  item_qty)
#                     for(item_name,item_price,item_qty) in cart]

# print(cart_item_totals)


#######################################################
# letters = [chr(code) for code in range(ord('a'), ord('z'))]

# random_letters = [random.choice(letters) for _ in range(100)]

# print(random_letters)
