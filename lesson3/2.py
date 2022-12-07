# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5])


def inputUser():
    return list(map(int, input('Введите несколько цифр через запятую: ').split(',')))


def listNew(number):
    lst = []
    i = 0
    j = len(number)-1
    while i <= j:
        lst.append(number[i]*number[j])
        i += 1
        j -= 1
    return lst


listUser = inputUser()
finalSum = listNew(listUser)
print(f'{listUser} -> {finalSum}')
