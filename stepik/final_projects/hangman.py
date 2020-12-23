def is_valid(word):
    flag = True
    for c in word:
        if not c.isalpha():
            flag = False
        elif c == ' ':
            flag = False
    return flag


def find_letter(let, arr, hid_arr):
    for c in range(len(arr)):
        if arr[c] == let:
            hid_arr[c] = let
    return hid_arr


def finish(list_h):
    if '_' in list_h:
        return True
    else:
        return False


def hangman(error):
    if error == 6:
        print("\t___________")
        print("\t|/        |")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|__________")
    if error == 5:
        print("\t___________")
        print("\t|/        |")
        print("\t|         O")
        print("\t|")
        print("\t|")
        print("\t|")
        print("\t|__________")
    if error == 4:
        print("\t___________")
        print("\t|/        |")
        print("\t|         O")
        print("\t|         |")
        print("\t|")
        print("\t|")
        print("\t|__________")
    if error == 3:
        print("\t___________")
        print("\t|/        |")
        print("\t|         O")
        print("\t|        /|")
        print("\t|")
        print("\t|")
        print("\t|__________")
    if error == 2:
        print("\t___________")
        print("\t|/        |")
        print("\t|         O")
        print("\t|        /|\\")
        print("\t|")
        print("\t|")
        print("\t|__________")
    if error == 1:
        print("\t___________")
        print("\t|/        |")
        print("\t|         O")
        print("\t|        /|\\")
        print("\t|        / ")
        print("\t|")
        print("\t|__________")
    if error == 0:
        print("\t___________")
        print("\t|/        |")
        print("\t|         O")
        print("\t|        /|\\")
        print("\t|        / \\")
        print("\t|")
        print("\t|__________")


while True:
    hidden_word = input('Загадайте слово.: ').strip()
    if is_valid(hidden_word):
        break
    else:
        print('Загаданное слово может содержать только буквы, попробуйте ещё раз.')
        continue

list_word = [c for c in hidden_word]
list_hidden = ['_' for c in range(len(hidden_word))]
letter = ''
attempts = 6


while True:
    if finish(list_hidden):
        letter = input('Угадайте слово. Введите 1 букву: ').strip()
        if is_valid(letter):
            if letter in list_word:
                print(f'Вы угадали, буква: "{letter}" присутствует в слове.')
                find_letter(letter, list_word, list_hidden)
                print(list_hidden)
                hangman(attempts)
            else:
                attempts -= 1
                print(f'Буква "{letter}" отсутствует в слове.')
                print(list_hidden)
                hangman(attempts)
                if attempts == 0:
                    print('Вы проиграли!')
        else:
            print('Можно использовать только буквы, попробуйте ещё раз.')
            continue
    else:
        print('Поздравляю вы отгадали слово!')
        break
