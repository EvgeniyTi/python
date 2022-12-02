# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# Пример:

# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

def inputUser():
    return int(input('Введите положительнок число: '))


def selectNum(number):
    if number == 0:
        return "Введите число больше нуля!"

    newList = []
    mult = 1
    for i in range(1, number+1):
        mult = (1 + 1/i)**i
        newList.append(mult)

    return newList


number = inputUser()
finalNumber = selectNum(number)
print(f'N = {number} -> {finalNumber}')
