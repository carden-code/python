# There is 100 rubles.
# How many bulls, cows and calves can be bought with all this money if the payment for
# a bull is 10 rubles, for a cow - 5 rubles, for a calf - 0.5 rubles and you need to buy 100 head of cattle?
#
# Note. Use a nested for loop.
bull = 10
cow = 5
calf = 0.5
for i in range(1, 100):
    for j in range(1, 100):
        for k in range(1, 100):
            if bull * i + cow * j + calf * k == 100:
                print(i, j, k)
