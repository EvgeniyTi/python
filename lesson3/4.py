# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def inputUser():
    return int(input('Введите десятичное число: '))


def listNew(number):
    numberb = ''

    while number > 0:
        numberb = str(number % 2) + numberb
        number = number // 2
    return numberb


numUser = inputUser()
finalSum = listNew(numUser)
print(f'{numUser} => {finalSum}')
