from random import choice


class MysticBall:
    def __init__(self, *ls):
        self.words = ls
        print(ls)

    def __call__(self):
        return choice(self.words)


def get_advanced_writer(f_name):

    def write_everything(*data_set):
        with open(f_name, 'a') as file:
            for i in data_set:
                file.write(f'{i}\n')

    return write_everything


first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

first_ball = MysticBall('Синий', 'Красный', 'Зеленый')
print(first_ball())
print(first_ball())
print(first_ball())
