import os
import random
import time

os.system('clear')


sum_candy = 117
sum_user1 = 0
sum_user2 = 0


# Кто первый ходит?

first_round = random.randint(1, 2)

# первый ходит

if first_round == 1:
    #sum_user1 += random.randint(1, 28)
    print('Ваш ход первый!')
    userAsk1 = int(input('Вы: Введите количество конфет до 28: '))
    sum_user1 += userAsk1
    sum_candy -= sum_user1
    print(f'Вы забрали себе {userAsk1} конфет')
    print(f'Осталось конфет: {sum_candy}\n')


else:
    print('Бот ходит первым')
    time.sleep(2)
    botAsk1 = random.randint(1, 28)
    sum_user2 += botAsk1
    sum_candy -= sum_user2
    print(f'Бот забрал себе {botAsk1} конфет')
    print(f'Осталось конфет: {sum_candy}\n')


for i in range(first_round+1, 50):
    if i % 2 != 0:
        user1 = int(input('Вы: Введите количество конфет до 28: '))
        sum_user1 += user1
        sum_candy -= user1
        if sum_candy <= 0:
            sum_user1 += sum_user2 + sum_candy
            sum_user2 = 0
            print('\nВы выиграли')
            break

        print(f'Вы забрали себе {user1} конфет')
        print(f'Осталось конфет: {sum_candy}\n')
    else:
        print('Хот бота...')
        time.sleep(2)
        user2 = random.randint(1, 28)
        sum_user2 += user2
        sum_candy -= user2
        if sum_candy <= 0:
            sum_user2 += sum_user1 + sum_candy
            sum_user1 = 0
            print('\nБот выиграл')
            break
        print(f'Бот забрал себе {user2} конфет')
        print(f'Осталось конфет: {sum_candy}\n')

print(f'Вы забрали себе {sum_user1} конфет')
print(f'Бот забрал себе {sum_user2} конфет')
