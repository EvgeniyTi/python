# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум
# - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2
from random import randint


def inputUser():
    return int(input('Введите положительное число: '))


def selectNum(number):
    if number == 0:
        return "Введите число больше нуля!"

    lst = [randint(-number, number) for i in range(number)]

    mult = 1
    for num in lst:
        mult *= num
    return mult, lst


def openFile(lst):
    with open('file.txt', 'w') as data:
        for i in lst:
            data.write(f'{i}\n')


number = inputUser()
finalNumber, lst = selectNum(number)
openFile(lst)
print(f'N = {number} -> {lst} -> произведение элементов массива -> {finalNumber}')

###############################################################################################################
# Часть 2
###############################################################################################################


def inputUser():
    lst = list(map(int, input('Введите позиции через запятую: ').split(',')))
    return lst[0], lst[1], lst


def readFile(x, y, n):
    with open("file.txt", "r") as f:
        mas = []
        for i in range(n):
            mas.append(int(f.readline()))

        return mas[x] * mas[y]


number1, number2, lst = inputUser()
readFileUser = readFile(number1, number2, number)
print(
    f'Номера позиций {number1}, {number2} -> произведение элементов массива -> {readFileUser}')
