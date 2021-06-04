# Дана строка текста.
# Напишите программу для подсчета стоимости строки, исходя из того,
# что один любой символ (в том числе пробел) стоит 6060 копеек. Ответ дайте в рублях и копейках.
# Sample Input 1:
#
# Привет, как дела?!
# Sample Output 1:
#
# 10 р. 80 коп.

def line_cost(string):
    characters = len(string)
    cost_one_symbol = 60
    total = characters * cost_one_symbol
    rub = total // 100
    kop = total % 100
    print(f"{rub} р. {kop} коп.")


line_cost('Привет, как дела?!')
