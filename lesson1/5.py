# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from cmath import sqrt


def coordinate():
    point1 = list(
        map(int, input('Введите координаты 1й точки черз запятую: ').split(',')))
    point2 = list(
        map(int, input('Введите координаты 2й точки черз запятую: ').split(',')))
    return point1[0], point1[1], point2[0], point2[1]


def twopoint(x1, x2, y1, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


x1, y1, x2, y2 = coordinate()
distance = twopoint(x1, x2, y1, y2)
print(f'A ({x1},{y1}); B ({x2},{y2}) -> {round(float(distance.real), 2)}')
