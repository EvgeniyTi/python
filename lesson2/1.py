# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def inputUser():
    return input('Введите вещественное число: ')


def selectNum(number):
    number = number.replace('-', '').replace(',', '').replace('.', '')

    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    return sum


number = inputUser()
finalNumber = selectNum(number)
print(f'{number} -> {finalNumber}')
