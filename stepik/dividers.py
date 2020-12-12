# Write a function get_factors (num) that takes a natural number as an argument and
# returns a list of all the divisors of the given number.
def get_factors(num):
    return [i for i in range(1, num + 1) if num % i == 0]


n = int(input())
print(get_factors(n))
