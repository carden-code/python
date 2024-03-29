# На вход программе подается строка текста, содержащая натуральные числа.
# Из данной строки формируется список чисел.
#
# Напишите программу, которая подсчитывает количество элементов полученного списка,
# больших предыдущего (элемента с предыдущим номером).
#
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.
#
# Формат выходных данных
# Программа должна вывести одно число – количество элементов списка, больших предыдущего.

string = input()

list_string = string.split(' ')
num_list = [int(i) for i in list_string]
count = 0
for index, elem in enumerate(num_list):
    if index > 0 and elem > num_list[index - 1]:
        count += 1
print(count)
