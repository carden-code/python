# A natural number is given. Write a program that computes:
#
# the number of digits is 3 in it;
# how many times the last digit appears in it;
# the number of even digits;
# the sum of his digits greater than five;
# the product of numbers greater than seven (if there are no numbers greater than seven, then output 1,
# if there is only one such figure, then output it);
# how many times it contains the numbers 0 and 5 (in total).
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should output the values of the specified values in the specified order.
num = int(input())
last = num % 10
count_3 = 0
count_last_digit = 0
count_even = 0
total_num_5 = 0
prod_num_7 = 1
count_0_5 = 0

while num != 0:
    last_digit = num % 10
    if last_digit == 3:
        count_3 += 1
    if last_digit == last:
        count_last_digit += 1
    if last_digit % 2 == 0:
        count_even += 1
    if last_digit > 5:
        total_num_5 += last_digit
    if last_digit > 7:
        prod_num_7 *= last_digit
    if last_digit == 0 or last_digit == 5:
        count_0_5 += 1
    num //= 10

print(count_3)
print(count_last_digit)
print(count_even)
print(total_num_5)
print(prod_num_7)
print(count_0_5)
