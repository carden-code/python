from collections import Counter
a = int(input())
b = int(input())

arr = []
arr2 = []
d = {}
count = 0
count2 = 0


for i in range(a, b + 1):
    for j in range(1, b + 1):
        if i % j == 0:
            arr.append(i)


# for t in arr:
#     for s in range(1, b + 1):
#         count2 = t // s


for y in arr:
    d[y] = arr.count(y)

max_val = max(d.values())

for key, value in d.items():
    if value == max_val:
        arr2.append(key)

for k in arr:
    for n in range(1, b + 1):
        if k % n == 0:
            print(k)
            count2 += n

for h in range(1, b + 1):
    if max(arr2) % h == 0:
        count += h

print(max(arr2), count)
print(arr)
print(d)
print(count2)


