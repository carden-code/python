a = int(input())
b = int(input())
a2 = int(input())
b2 = int(input())
if (a2 > a) and (b2 > b) and (a2 == b2):
    print('YES')
elif (a2 > a) and (b2 > b) and (a2 - b2 == 2) or (a2 - b2 == 4):
    print('YES')
else:
    print('NO')
