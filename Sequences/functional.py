from functools import reduce

nums = [1, 2, 3, 4, 5]

# sum = reduce(lambda acc, current: acc + current, nums)

def sum(total, next_val):
    print("total: {}, next_val: {}".format(total, next_val))
    return total + next_val

sum = reduce(sum, nums)

print(sum)



# nums = [1, 2, 3, 4, 5]


# def square(x):
#     return x**2

# print(nums)
# print(list(map(square, nums)))

# people = [
#     ("Bob", 34), 
#     ("Jen", 13), 
#     ("Abe", 24), 
#     ("Karen", 56)
# ]

# print(list(filter(lambda p : p[1] > 30, people)))