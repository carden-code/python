# The input to the program is two natural numbers a and b (a <b).
# Write a program that finds a natural number from the segment [a; b] with the maximum sum of divisors.
#
# Input data format
# The program receives two numbers as input, each on a separate line.
#
# Output data format
# The program should print two numbers on one line, separated by a space:
# the number with the maximum sum of divisors and the sum of its divisors.
#
# Note. If there are several such numbers, then output the largest of them.
a = int(input())
b = int(input())

count = 0
count2 = 0
total = 0
total2 = 0
num = 0

for i in range(a, b + 1):
    for j in range(1, b + 1):
        if i % j == 0:
            total += j
            count += 1
    if total >= total2:
        total2 = total
        num = i
    if count >= count2:
        count2 = count
    count = 0
    total = 0

print(num, total2)
