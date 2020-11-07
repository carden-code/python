# The input to the program is a natural number n. Write a program for calculating the alternating sum.
#
# Input data
# The input to the program is a natural number nn.
#
# Output
# The program should output a single number in accordance with the condition of the problem.
n = int(input())
total = 1
for i in range(2, n + 1):
    if i % 2 == 0:
        total -= i
    else:
        total += i
print(total)
