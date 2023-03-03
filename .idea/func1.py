from functools import reduce

num_list = [2, 3, 4, 5]
product = reduce(lambda x, y: x*y, num_list)

print("The product of all the numbers in the list is:", product)