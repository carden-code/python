import re
a = 'Стефанос Циципас'
b = 'Циципас, Стефанос'


def sravnenie(a, b):
    arr_a = re.sub('[/,-]', ' ', a).split()
    arr_b = re.sub('[/,-]', ' ', b).split()
    arr_a.sort(key=lambda x: len(list(x)))
    arr_b.sort(key=lambda x: len(list(x)))

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
            for s in range(len(arr_slovo1)):
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