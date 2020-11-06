# The input to the program is a natural number nn.
# Write a program that evaluates the value of an expression (1/1 + 1/2 + 1/3 ... + 1/n) - log(n)

from math import log
n = int(input())
total = 0
ln = log(n)
for i in range(1, n + 1):
    total += 1 / i
print(total - ln)
