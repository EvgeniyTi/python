# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def inputUser():
    return int(input('Введите положительнок число: '))


def selectNum(number):
    if number == 0:
        return "Введите число больше нуля!"

    newList = []
    mult = 1
    for i in range(1, number+1):
        mult = mult * i
        newList.append(mult)

    return newList


number = inputUser()
finalNumber = selectNum(number)
print(f'N = {number} -> {finalNumber}')
