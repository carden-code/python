# Описание проекта:
#     Программа загадывает слово, а пользователь должен его угадать.
#     Изначально все буквы слова неизвестны.
#     Также рисуется виселица с петлей. Пользователь предлагает букву, которая может входить в это слово.
#     Если такая буква есть в слове, то программа ставит букву столько раз, сколько она встречается в слове.
#     Если такой буквы нет, к виселице добавляется круг в петле, изображающий голову.
#     Пользователь продолжает отгадывать буквы до тех пор, пока не отгадает всё слово.
#     За каждую неудачную попытку добавляется еще одна часть туловища висельника
#     (обычно их 6: голова, туловище, 2 руки и 2 ноги.
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
    if '_' in list_h:
        return True
    else:
        return False


def hangman(error, array):
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


while True:
    hidden_word = input('Загадайте слово.: ').strip()
    if is_valid(hidden_word):
        break
    else:
        print('Загаданное слово может содержать только буквы, попробуйте ещё раз.')
        continue

list_word = [c for c in hidden_word]
list_hidden = ['_' for c in range(len(hidden_word))]
hangman_list = ["\t___________", "\t|/        |", "\t|", "\t|", "\t|", "\t|", "\t|__________"]
named_letters = []
letter = ''
attempts = 6


while True:
    if finish(list_hidden):
        letter = input('Угадайте слово. Введите 1 букву: ').strip()
        named_letters.append(letter)
        if is_valid(letter) and len(letter) == 1:
            if letter in list_word:
                print(f'Вы угадали, буква: "{letter}" присутствует в слове.')
                find_letter(letter, list_word, list_hidden)
                print(list_hidden)
                hangman(attempts, hangman_list)
                print(*[c for c in hangman_list], sep='\n')
            else:
                attempts -= 1
                print(f'Буква "{letter}" отсутствует в слове.')
                print(list_hidden)
                hangman(attempts, hangman_list)
                print(*[c for c in hangman_list], sep='\n')
                if attempts == 0:
                    print('Вы проиграли!')
                    break
        else:
            print('Не известная буква! Попробуйте ещё раз.')
            continue
    else:
        print('Поздравляю вы отгадали слово!')
        break
