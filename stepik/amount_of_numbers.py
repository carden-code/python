# The input to the program is two integers a and b (a <= b).
# Write a program that counts the number of numbers in the range a through b, inclusive, whose cube ends in 44 or 99.
#
# Input data format
# The input to the program is two integers a and b (a <= b).
#
# Output data format
# The program should output one integer in accordance with the condition of the program.
a = int(input())
b = int(input())
counter = 0
for i in range(a, b + 1):
    iq = str(i**3)
    if int(iq[-1]) == 4:
        counter += 1
    elif int(iq[-1]) == 9:
        counter += 1
print(counter)
