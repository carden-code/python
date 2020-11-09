even = 0
odd = 0
for _ in range(10):
    num = int(input())
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
if odd > 0:
    print('NO')
else:
    print('YES')
