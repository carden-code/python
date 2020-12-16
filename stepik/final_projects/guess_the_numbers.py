# Описание проекта:
#     программа запрашивает имя пользователя и
#     генерирует случайное число в диапазоне который ввел пользователь от 1 до ...
#     и просит пользователя угадать это число.
#     Если догадка пользователя больше случайного числа,
#      то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'.
#     Если догадка меньше случайного числа,
#      то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'.
#     Если пользователь угадывает число,
#      то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'
#      и предлогает поиграть ещё.
from random import randint


def is_valid(number):
    return True if number.isdigit() and int(number) in range(1, num_r + 1) else False


print("Игра - 'Угадайка число!'")
name = input('Пожалуйста введите ваше имя: ')
num = 0
num_r = 0
count = 0
flag = True
yes_no = ''

while True:
    if yes_no == 'нет':
        break
    if count == 0 and flag:
        num_r = input("До какого числа загадываю? от 1 до ... : ")
        if num_r.isdigit() and int(num_r) > 1:
            num_r = int(num_r)
            flag = False
        else:
            print('Не корректный диапазон!')
            continue
        num = randint(1, num_r)

    user_num = input(f'{name} введите целое число от 1 до {num_r}: ')
    if not is_valid(user_num):
        print(f'А может быть все-таки введем целое число от 1 до {num_r}?')
        continue
    user_num = int(user_num)

    if user_num < num:
        count += 1
        print('Ваше число меньше загаданного, попробуйте еще разок')
        print(f'Колличество попыток {count}')
    elif user_num > num:
        count += 1
        print('Ваше число больше загаданного, попробуйте еще разок')
        print(f'Колличество попыток {count}')
    else:
        count += 1
        print('Вы угадали, поздравляем!')
        print(f'Колличество попыток {count}')
        while True:
            yes_no = input(f"{name} сыгрем ещё? Напишите 'Да' или 'Нет': ").lower()
            if yes_no != 'да' and yes_no != 'нет':
                print('А может быть все-таки введем Да или Нет ?')
                continue
            elif yes_no == 'да':
                count = 0
                flag = True
                break
            elif yes_no == 'нет':
                print(f'{name} Спасибо, что играли в числовую угадайку. Еще увидимся...')
                break
