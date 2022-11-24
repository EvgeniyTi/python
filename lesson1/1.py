# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def weeks(number):
    if number == 6 or number == 7:
        print(f"{number} -> да")
    else:
        print(f"{number} -> нет")


def Calluser():
    num = int(input('Введите число обозначающую день недели (1, 2 ... 7): '))
    if (num in range(1, 8)):
        return num


numberWeek = Calluser()
weeks(numberWeek)
