minutes = int(input())
if minutes >= 1440:
    h = minutes // 60 % 24
    m = minutes % 60
else:
    h = minutes // 60
    m = minutes % 60
print(h, m)
