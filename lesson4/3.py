# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import os
os.system('clear')


def sayUser():
    ask = list(map(int, input('Задайте числа через пробел: ').split()))
    return ask


def funcN(d):
    num = []
    for i in range(len(d)):
        unique = True
        for j in range(len(d)):
            if i == j:
                continue
            if d[i] == d[j]:
                unique = False
                break
        if unique:
            num.append(d[i])

    return num


askUser = sayUser()
finalResult = funcN(askUser)
print(f'{askUser} -> {finalResult}')
