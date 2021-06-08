# На вход программе подается строка текста, содержащая натуральные числа.
# Из строки формируется список чисел. Напишите программу циклического сдвига элементов списка направо:
# каждый из элементов сдвинуть на одну позицию вперед, а последний поставить первым.
#
# Формат входных данных
# На вход программе подается строка текста, состоящая из натуральных чисел, разделенных пробелами.
#
# Формат выходных данных
# Программа должна вывести измененный список с циклическим сдвигом.
# from collections import deque
#
# list_digits = [int(i) for i in input().split(' ')]
#
# new_list = deque(list_digits)
# new_list.rotate()
#
# print(*new_list)
n = input().split()
print(n.pop(), *n)
