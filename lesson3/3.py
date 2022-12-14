# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части
# элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def inputUser():
    return list(map(float, input('Введите несколько вещественных цифр через запятую: ').split(',')))


def listNew(number):
    max = number[0] - int(number[0])
    min = number[0] - int(number[0])

    for i in range(1, len(number)):
        if (number[i] - int(number[i])) >= max:
            max = number[i] - int(number[i])
    for i in range(1, len(number)):
        if (number[i] - int(number[i])) < min:
            min = number[i] - int(number[i])
    return max - min


listUser = inputUser()
finalSum = listNew(listUser)
print(f'{listUser} => {round(finalSum, 2)}')
