food = {
    'coffee': 'beverage',
    'pizza': 'entree',
    'cookie': 'dessert',
    'tea': 'beverage',
}

beverages = {food:category.upper() for (food,category) in food.items() if category == 'beverage'}

print(beverages)

food_groups = {
    food_group for food_group in food.values()
}

print(food_groups)