# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def askUser():
    answer = int(input('Введите номер четверти от 1 до 4: '))
    if answer in range(1, 4):
        return answer
    else:
        print('Введите номер четверти от 1 до 4')


def Coordinate(number):
    if number == 1:
        return "x >= 0", "y >= 0"
    elif number == 2:
        return "x >= 0", "y <= 0"
    elif number == 3:
        return "x <= 0", "y <= 0"
    else:
        return "x <= 0", "y >= 0"


number = askUser()
x, y = Coordinate(number)
print(f'Диапозон возможных координат точек в этой четверти {x} и {y}')
