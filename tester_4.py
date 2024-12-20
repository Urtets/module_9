import time
import sys
def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)

        print(f"Функция работала {elapsed} секунд(ы)")
        return result
    return surrogate

@time_track
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))

sys.set_int_max_str_digits(100000)

result = digits(3141, 5926, 2718, 2818)
print(result)