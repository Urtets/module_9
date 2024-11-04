# def func_generator(n):
#     i = 0
#     while i != n:
#         yield i
#         i += 1
#
#
# obj = func_generator(10)
# print(obj)
#
# for i in obj:
#     print(i)

def fibonacci_v1(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def fibonacci_v2(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib_1 = fibonacci_v1(n=10)
print(fib_1)

for value in fib_1:
    print(value)


fib_2 = fibonacci_v2(n=10)
print(fib_2)
for value in fib_2:
    print(value)