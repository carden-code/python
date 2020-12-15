# Write a function get_month (language, number), which takes two arguments language as input - the language ru or en and
# number - the number of the month (from 1 to 12) and returns the name of the month in Russian or English.
def get_month(language, number):
    d = {'ru': {1: 'январь', 2: 'февраль', 3: 'март', 4: 'апрель', 5: 'май', 6: 'июнь', 7: 'июль', 8: 'август',
                9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь', 12: 'декабрь'},
         'en': {1: 'january', 2: 'february',
                3: 'march', 4: 'april', 5: 'may', 6: 'june', 7: 'july', 8: 'august',
                9: 'september', 10: 'october', 11: 'november', 12: 'december'}}
    return d[language][number]


lan = input()
num = int(input())


print(get_month(lan, num))
