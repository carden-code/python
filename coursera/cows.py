n = int(input())
s = n % 10
if 10 < n < 20 or s == 0 or 5 <= s <= 9:
    print(n, 'korov')
elif s == 1:
    print(n, 'korova')
else:
    print(n, 'korovy')
