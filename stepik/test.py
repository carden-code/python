num = 1000
system = 16
a = 1
b = ''
while num > 0:
    num = num // system
    num2 = num % system
    if num > system:
        num // system
    elif num < system:
        b += str(num % system)

