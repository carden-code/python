# На вход программе подается строка текста из натуральных чисел.
# Из элементов строки формируется список чисел.
# Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.).
# Если в списке нечетное количество элементов, то последний остается на своем месте.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.
#
# Формат выходных данных
# Программа должна вывести измененный список, разделяя его элементы одним пробелом.

# string = input().split(' ')
# list_num = list(map(int, string))
# new_list = [0 for _ in range(len(string))]
# count = 1
#
# for index, num in enumerate(list_num):
#     if count % 2 == 0:
#         new_list[index] = list_num[index - 1]
#     else:
#         if index == len(list_num) - 1 and len(list_num) % 2 == 1:
#             new_list[index] = list_num[-1]
#             break
#         new_list[index] = list_num[index + 1]
#
#     if index == len(list_num) - 1:
#         break
#
#     count += 1
# print(*new_list)

digits = [int(c) for c in input().split()]

for i in range(1, len(digits), 2):
    digits[i - 1], digits[i] = digits[i], digits[i - 1]

print(*digits)
