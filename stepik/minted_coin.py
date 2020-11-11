# Everyone knows that the witcher is able to defeat any monsters, but his services will not be cheap, moreover,
# the witcher does not accept bills, he only accepts minted coins. In the world of the witcher,
# there are coins with denominations of 1, 5, 10, 25.
#
# Write a program that determines the minimum number of minted coins you need to pay the witcher.
#
# Input data format
# At the entrance to the program, one natural number is served, the price for the witchery's service.
#
# Output data format
# The program should display the minimum possible number of minted coins for payment.
num = int(input())
total = 0

total += (num // 25)
num = (num % 25)
total += (num // 10)
num = (num % 10)
total += (num // 5)
num = (num % 5)
total += (num // 1)

print(total)
