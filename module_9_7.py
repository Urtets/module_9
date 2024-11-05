def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == int:
            print("Простое")
        else:
            print("Составное")
        return result

    return wrapper

@is_prime
def sum_three(one, two, three):
    return one + two + three


result = sum_three(2, 3, 6)
print(result)