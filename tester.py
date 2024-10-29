def is_odd(x):
    return x % 2


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

result = filter(is_odd, my_numbers)
print(result)
print(list(result))