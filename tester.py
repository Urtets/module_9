def get_multiplier_v1(n):
    if n == 2:
        def multiplier(x):
            return x * 2

    elif n == 3:
        def multiplier(x):
            return x * 3

    else:
        raise Exception("Я могу сделать умножители только на 2 и 3")
    return multiplier






my_func = lambda x: x + 10

print(my_func(x=42))
print(type(my_func))

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]

by_2 = get_multiplier_v1(2)
by_3 = get_multiplier_v1(3)

result = map(by_2, my_numbers)
print(list(result))
result = map(by_3, my_numbers)
print(list(result))

result = map(lambda x: x + 10, my_numbers)
print(list(result))

result = map(lambda x, y: x + y, my_numbers, they_numbers)
print(list(result))