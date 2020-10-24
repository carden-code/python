a = int(input())
b = int(input())
n = int(input())
sum_kop = (a * 100 + b) * n
rub = sum_kop // 100
kop = sum_kop % 100
print(rub, kop)
