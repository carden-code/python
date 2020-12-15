# Write a function number_to_words (num) that takes a natural number num as an argument
# and returns its verbal description in Russian.
#
# Note. Consider the number 1 <= num <= 99.
def number_to_words(num):
    units = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь',
             'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
             'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

    if num < 20:
        return units[num - 1]
    elif num >= 20:
        if str(num)[1] != '0':
            return tens[int(str(num)[0]) - 2] + ' ' + units[int(str(num)[1]) - 1]
    return tens[int(str(num)[0]) - 2]


n = int(input())


print(number_to_words(n))
