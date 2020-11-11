# A natural number is given. Write a program that computes:
#
# the sum of its digits;
# the number of digits in it;
# the product of its numbers;
# the arithmetic mean of its digits;
# its first digit;
# the sum of its first and last digits.
# Input data format
# One natural number is fed into the program.
#
# Output data format
# The program should output the values of the specified values in the specified order.
num = int(input())
sum_num = 0
number_digits = 0
product_num = 1
average = 0
str_num = str(num)
first_num = int(str_num[0])
last_num = num % 10
sum_last_first = last_num + first_num
while num != 0:
    last_num = num % 10
    sum_num += last_num
    product_num *= last_num
    number_digits += 1
    num = num // 10

average = sum_num / number_digits

print(sum_num)
print(number_digits)
print(product_num)
print(average)
print(first_num)
print(sum_last_first)

