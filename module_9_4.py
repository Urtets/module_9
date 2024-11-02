"""Лямбда-функция"""
from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = map(lambda x, y: x == y, first, second)
print(list(result))

"""Замыкание"""


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding="utf-8") as some_data:
            for data in data_set:
                print(data)
                if not isinstance(data, str):
                    some_data.write(str(data) + "\n")
                else:
                    some_data.write(data + "\n")

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


"""Метод __call__"""


class MysticBall:
    def __init__(self, *words):
        self.words = words


    def __call__(self):
        any_unit = choice(self.words)
        return any_unit


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())