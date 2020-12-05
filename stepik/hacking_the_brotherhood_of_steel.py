# Формат входных данных
# На первой строке вводится символ решётки и сразу же натуральное число nn — количество строк в программе,
# не считая первой. Далее следует nn строк кода.
#
# Формат выходных данных
# Нужно вывести те же строки, но удалить комментарии и символы пустого пространства в конце строк.
# Пустую строку вместо первой строки ввода выводить не надо.

first_string = input()
num = int(first_string[1:])  # преобразуем строку в число начиная со второго сивола.
strings = []

for _ in range(num):
    strings.append(input())  # добавляем строки в список.

list_new = []
for c in strings:  # перебираем строки.
    if '#' in c:  # если в строке встречается символ "#".
        index_sym = c.index('#')  # сохраняем индекс этого символа в строке в переменную.
        list_new.append(c[:index_sym].rstrip())  # добавляем в список строку до индекса(#) без пробелов в конце.
    else:
        list_new.append(c)  # если в строке отсутствует символ '#' просто добавляем в список.
print(*list_new, sep='\n')  # печатаем список.