class Cart:

    def __init__(self, items):
        self.__items = items

    def __str__(self):
        return str(self.__items)

    def __add__(self, another_cart):
        return Cart(self.__items + another_cart.__items)

    def __mul__(self, qty_multiply):
        return Cart(list(map(lambda item: {
            'name': item['name'],
            'qty': item['qty'] * qty_multiply
        }, self.__items)))

        
    def __gt__(self, another_cart):
        left = sum(item['qty'] for item in self.__items)
        right = sum(item['qty'] for item in another_cart.__items)

        return left > right

        # return sum(item['qty'] for item in self.__items) > sum(item['qty'] for item in another_cart.__items)

        
    def __lt__(self, another_cart):
                return sum(item['qty'] for item in self.__items) < sum(item['qty'] for item in another_cart.__items)

# cart1 = Cart([
#     'coffee creamer', 'butter', 'bottled water',
# ])

# cart2 = Cart([
#     'bread', 'apples', 'apple cider vinegar',
# ])

# print(cart1 + cart2)

cart = Cart([
    {'name': 'coffee creamer', 'qty': 2},
    {'name': 'butter', 'qty': 3},
    {'name': 'bottled water', 'qty': 4}
])

# cart2 = Cart([
#     { 'name':'bread', 'qty': 2 },
#     { 'name':'apples', 'qty': 2 },
#     { 'name':'apple cider vinegar', 'qty': 2 }
# ])

print(cart * 2)

