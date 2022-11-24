# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def sayUser():
    x = int(input('Введите координату \'x\': '))
    y = int(input('Введите координату \'y\': '))
    if x != 0 and y != 0:
        return x, y
    else:
        print('Введите координаты отличные от нуля!')
        try:
            sayUser()
        except TypeError:
            print('Ошибка')


def target(x, y):
    if x >= 0 and y >= 0:
        return 1
    elif x >= 0 and y < 0:
        return 2
    elif x <= 0 and y < 0:
        return 3
    else:
        return 4


x, y = sayUser()
coordinate = target(x, y)
print(f'x = {x}; y = {y} -> {coordinate}')
