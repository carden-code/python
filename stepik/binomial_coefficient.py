# Write a function compute_binom (n, k) that takes two natural numbers n and
# k as arguments and returns the binomial coefficient.
from math import factorial


def compute_binom(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


n = int(input())
k = int(input())

print(compute_binom(n, k))