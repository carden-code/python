# Дана строка, состоящая из слов, разделенных пробелами.
# Напишите программу, которая подсчитывает количество слов в этой строке.
#
# Формат входных данных
# На вход программе подается строка.
#
# Формат выходных данных
# Программа должна вывести количество слов в строке.
#
# Примечание 1.
#   Кроме слов в тексте могут присутствовать пробелы и знаки препинания .,!?:;. Других символов в тексте нет.
#
# Примечание 2.
#   Решите задачу в одну строчку кода.

print(len([s for s in input().split(' ') if s not in '.,!?:;']))