numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_nums = list(filter(lambda x: x % 2 == 0, numbers))
print(even_nums)

doubled_nums = list(map(lambda x: x * 2, even_nums))
print(doubled_nums)

sorted_nums = sorted(doubled_nums, key=lambda x: x, reverse=True)
print(sorted_nums)
