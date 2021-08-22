number = 3

a = [1, 1]
b = []
for i in range(number):
    for index, j in enumerate(a):
       if len(a) > 2:
           if index > 0 and index != -1:
                b.append(j)