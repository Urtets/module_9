def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = func(int_list)
    return results


def min(int_list):
    res = int_list[0]
    for i in int_list:
        if i < res:
            res = i
    return res


def max(int_list):
    res = int_list[0]
    for i in int_list:
        if i > res:
            res = i
    return res


def len(int_list):
    length = 0
    for i in int_list:
        length += 1
    return length


def sum(int_list):
    sum_up = 0
    for i in int_list:
        sum_up += i
    return sum_up


def sorted(int_list):
    int_list.sort()
    return int_list


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
