# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

import os
os.system('clear')


def sayUser():
    ask = input('Задайте натуральное число N: ')
    if (not ask.isdigit()):
        print('Введите число')
        return sayUser()
    ask = int(ask)
    if ask < 0:
        print('Введите число больше нуля')
        return sayUser()

    return ask


def funcN(d):
    newList = []

    for i in range(2, d):
        trueandfalse = True
        for j in range(2, i):
            if i == j:
                continue
            if i % j == 0:
                trueandfalse = False
                break

        if trueandfalse:
            newList.append(i)

    finalList = []
    for i in newList:
        if d % i == 0:
            finalList.append(i)

    return finalList


askUser = sayUser()
finalResult = funcN(askUser)
print(f'{askUser} -> {finalResult}')
