# Write a function print_digit_sum () that takes a single integer num and prints the sum of its digits.
def print_digit_sum(_num):
    print(sum([int(i) for i in str(_num)]))


num = int(input())

print_digit_sum(num)
