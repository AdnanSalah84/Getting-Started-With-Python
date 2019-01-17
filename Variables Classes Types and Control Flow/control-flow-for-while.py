# nums = [1, 2, 3, 4, 5, 6, 7, 8 ]
nums = range(0,100)

# for num in nums:
#     print(num)
# else:
#     print(sum(nums))


# counter = 0

# while counter < len(nums):
#     print("index: {}, value: {}".format(counter, nums[counter]))
#     counter = counter + 1
# else:
#     print("sum: {}".format(sum(nums)))

for num in nums:
    if num % 2 == 0:
        continue
    if num == 51:
        break
    print(num)
else:
    print(sum(nums))
