cart = [
    ['Coffee', 7.99, 2],
    ['Bread', 2.99, 1],
    ['Apple', 0.99, 2],
    ['Milk', 4.99, 1],
    ['Cola', 1.99, 4],
]

# cart_item_count = sum(item[2] for item in cart)

cart_item_count = sum(qty for (name, price, qty) in cart)

print(cart_item_count)

max_item_price = max(price for (name, price, qty) in cart)

print(max_item_price)

max_item = max((item for item in cart), key=lambda item: item[1])

print(max_item)