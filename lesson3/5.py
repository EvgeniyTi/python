# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def inputUser():
    return int(input('Введите десятичное число: '))


def listNew(number):
    lst1 = [0, 1]
    lst2 = []

    for i in range(2, number+1):
        lst1.append(lst1[i-1] + lst1[i-2])

    for i in lst1:
        lst2.append(i * (-1))

    lst2.sort()

    lst = lst2 + lst1
    lst.pop(number+1)

    return lst


numUser = inputUser()
lst = listNew(numUser)
print(f'{lst}')
