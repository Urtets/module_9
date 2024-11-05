def is_prime(func):
    def wrapper(*args):
        answer = [True if type(x) != int or x != 1 else False for x in args]
        result = func(*args)
        if False in answer:
            print("Составное")
        else:
            print("Простое")
        return result

    return wrapper

@is_prime
def sum_three(one, two, three):
    return one + two + three


result = sum_three(2, 3, 6)
print(result)