import re
from difflib import SequenceMatcher

a = 'К.Кристиэн V С.Сантамария'.lower()
b = 'Кристиан/ V Сантамарея'.lower()


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Сравнение отличающихся строк
def sravnenie(string_1, string_2):
    if '/' in string_1 or '/' in string_2:
        res = similar(string_1, string_2)
        print(res)
        if res > 0.77:
            return True
        else:
            return False

    arr_a = re.sub('[/,-]', ' ', a).split()
    arr_b = re.sub('[/,-]', ' ', b).split()
    arr_a.sort(key=lambda x: len(list(x)))
    arr_b.sort(key=lambda x: len(list(x)))

    if len(' '.join(arr_a)) != len(' '.join(arr_b)):
        res = similar(a, b)
        if res > 0.8:
            return True
        else:
            return False

    result_fast = [x for x in arr_a if x in arr_b]
    if len(result_fast) == len(arr_a):
        return True

    result = []
    count_x = 0
    for i in range(len(arr_a)):
        slovo1 = arr_a[i]
        slovo2 = arr_b[i]
        if slovo1 == slovo2:
            result.append(slovo1)
        else:
            arr_slovo1 = list(slovo1)
            arr_slovo2 = list(slovo2)

            if len(arr_slovo1) < len(arr_slovo2):
                arr_range = len(arr_slovo1)
            else:
                arr_range = len(arr_slovo2)

            for s in range(arr_range):
                if arr_slovo1[s] == arr_slovo2[s]:
                    count_x += 1
            if count_x == len(arr_a) or count_x + 1 == len(arr_a):
                result.append(arr_slovo1)
            count_x = 0
    if len(result) == len(arr_a):
        return True
    else:
        return False


a = sravnenie(a, b)
print(a)
