# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def inputUser():
    return list(map(int, input('Введите несколько цифр через запятую: ').split(',')))


def selectNum(number):
    sum = 0
    for i in range(len(number)):
        if i % 2 != 0:
            sum += number[i]
    return sum


listUser = inputUser()
finalSum = selectNum(listUser)
print(f'{listUser} -> {finalSum}')
