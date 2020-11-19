# The input to the program is a natural number n.
# Write a program that finds the digital root of a given number.
# The digital root of the number nn is obtained as follows: if you add up all the digits of this number,
# then all the digits of the found sum and repeat this process, the result will be a single-digit number (digit),
# which is called the digital root of this number.
#
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should print the digital root of the entered number.
#
# Note. Use nested while loops.
#
# Sample Input:
# 192
# Sample Output:
# 3
num = int(input())
count = 0

while num != 0:
    count += num % 10
    num //= 10
    if num == 0 and count >= 10:
        count += num
        num = count
        count = 0

print(count)
