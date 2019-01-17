food = {
    'coffee': 'beverage',
    'pizza': 'entree',
    'cookie': 'dessert',
    'tea': 'beverage',
}

categories = {
    category for category in food.values()
}

print(categories)