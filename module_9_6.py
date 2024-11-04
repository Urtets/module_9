from itertools import combinations

def all_variants(text):
    for i in range(1, len(text) + 1):
        some_list = []
        b = combinations(text, i)
        some_list.extend(b)
        for j in some_list:
            j = list(j)
            yield (''.join(j))


a = all_variants("abc")
for i in a:
    print(i)


some_writing = "something"
some_combination = combinations(some_writing, 3)
print(list(some_combination))
help(combinations)