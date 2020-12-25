# Описание проекта:
#     Программа загадывает слово, а пользователь должен его угадать.
#     Изначально все буквы слова неизвестны.
#     Также рисуется виселица с петлей. Пользователь предлагает букву, которая может входить в это слово.
#     Если такая буква есть в слове, то программа ставит букву столько раз, сколько она встречается в слове.
#     Если такой буквы нет, к виселице добавляется круг в петле, изображающий голову.
#     Пользователь продолжает отгадывать буквы до тех пор, пока не отгадает всё слово.
#     За каждую неудачную попытку добавляется еще одна часть туловища висельника
#     (обычно их 6: голова, туловище, 2 руки и 2 ноги.
from random import choice


def get_word(list_w):
    return choice(list_w).upper()


def is_valid(word):
    flag = True
    for c in word:
        if not c.isalpha():
            flag = False
        elif c == ' ':
            flag = False
    return flag


def find_letter(let, array, hid_arr):
    for c in range(len(array)):
        if array[c] == let:
            hid_arr[c] = let
    return hid_arr


def finish(list_h):
    return True if '_' in list_h else False


def hangman(error):
    array = ["\t___________", "\t|/        |", "\t|", "\t|", "\t|", "\t|", "\t|__________"]
    for c in range(len(array)):
        if error < 6:
            array[2] = "\t|         O"
        if error < 5:
            array[3] = "\t|         |"
        if error < 4:
            array[3] = "\t|        /|"
        if error < 3:
            array[3] = "\t|        /|\\"
        if error < 2:
            array[4] = "\t|        / "
        if error < 1:
            array[4] = "\t|        / \\"
    return array


def play(tries):
    print('Давайте играть в угадайку слов!')
    print('_' * len(hidden_word))
    print(*[c for c in hangman(tries)], sep='\n')

    while True:
        if finish(list_hidden):
            print(f'Количеством допустимых промахов: {tries}')
            answer = input('Угадайте слово. Введите 1 букву или слово целиком: ').strip().upper()
            if answer in guessed_letters:
                print(f'Вы уже вводили букву - "{answer}", поробуйте снова.')
                continue

            if len(answer) > 1 and len(answer) != len(hidden_word):
                print(f'В загаданном слове - "{len(hidden_word)}" букв. Попробуйте снова.')
                continue

            if len(answer) == 1:
                guessed_letters.append(answer)

            if is_valid(answer) and len(answer) == 1:
                if answer in list_word:
                    print(f'Вы угадали, буква: "{answer}" присутствует в слове.')
                    print(*find_letter(answer, list_word, list_hidden))
                    print(*[c for c in hangman(tries)], sep='\n')
                else:
                    tries -= 1
                    print(f'Буква "{answer}" отсутствует в слове.')
                    print(*list_hidden)
                    print(*[c for c in hangman(tries)], sep='\n')
                    if tries == 0:
                        print(f'Вы проиграли! Загаданное слово - "{hidden_word}"')
                        break
            elif is_valid(answer) and len(answer) > 1:
                if answer == hidden_word:
                    print(f'Вы угадали слово: "{answer}". Поздравляем!')
                    print(hidden_word)
                    print(*[c for c in hangman(tries)], sep='\n')
                    break
                else:
                    tries = 0
                    print(f'"{answer}" - не правильно! Загаданное слово - "{hidden_word}"')
                    print(*list_hidden)
                    print(*[c for c in hangman(tries)], sep='\n')
                    break
            else:
                print('Пожалуйста используйте только буквы! Попробуйте ещё раз.')
                continue
        else:
            print(f'Поздравляю вы отгадали слово! {hidden_word}')
            break


word_list = ["человек", "слово", "лицо", "дверь", "земля", "работа", "ребенок", "история", "женщина", "развитие",
             "власть", "правительство", "начальник", "спектакль", "автомобиль", "экономика", "литература", "граница",
             "магазин", "председатель", "сотрудник", "республика", "личность"]
while True:
    hidden_word = get_word(word_list)
    list_word = [c for c in hidden_word]
    list_hidden = ['_' for c in range(len(hidden_word))]
    guessed_letters = []
    attempts = 6

    play(attempts)

    game = input('Желате сиграть ещё? Введите "Д" - Да или "Н" - Нет: ').lower()
    if game in ['да', 'д', 'da', 'd']:
        continue
    else:
        print("До свидания!")
        break
