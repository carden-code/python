# Write a function number_of_factors (num) that takes a number as an argument and
# returns the number of divisors for the given number.
#
# Note 1. Use the already implemented get_factors (num) function from the previous task.
def get_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]


def number_of_factors(num):
    return len(get_factors(num))


n = int(input())
print(number_of_factors(n))
