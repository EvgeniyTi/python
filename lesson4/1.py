# 1'. Вычислить число Пи c заданной точностью d

# *Пример:*

# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415

# использование формулы Лейбница

def sayD():
    return input('Задайте точность числа pi -> d = ')


def opocity(d):
    return len([i for i in d]) - 2


def piNumber(d):
    koef = 1
    sum = 0
    for i in range(1000000):
        if i % 2 == 0:
            sum += 4 / koef
        else:
            sum -= 4 / koef
        koef += 2
    return round(sum, d)


inputUser = sayD()
op = opocity(inputUser)
pi = piNumber(op)
print(f'd = {inputUser}, π = {pi}')
