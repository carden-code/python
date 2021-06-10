# Дана строка текста, состоящая из букв русского алфавита "О" и "Р".
# Буква "О" – соответствует выпадению Орла, а буква "Р" – соответствует выпадению Решки.
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.
#
# Формат входных данных
# На вход программе подается строка текста, состоящая из букв русского алфавита "О" и "Р".
#
# Формат выходных данных
# Программа должна вывести наибольшее количество подряд выпавших Решек.
#
# Примечание. Если выпавших Решек нет, то необходимо вывести число 0.

# string = input()
# count = 0
# list_count = []
# for index, elem in enumerate(string):
#     if elem == 'Р':
#         count += 1
#     if index == len(string) - 1:
#         list_count.append(count)
#         break
#     if string[index + 1] != string[index]:
#         list_count.append(count)
#         count = 0
# print(max(list_count))
print(max(map(len, input().split('О'))))
