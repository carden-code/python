# The input to the program is a natural number nn.
# Write a program that prints the numbers 11 through nn, inclusive, except:
#
# numbers from 5 to 9 inclusive;
# numbers from 17 to 37 inclusive;
# numbers from 78 to 87 inclusive.
#
# Input data format
# One natural number nn is fed to the input of the program.
#
# Output data format
# The program should output numbers in accordance with the condition of the problem, each on a separate line.
#
# Note. Use the continue statement.
num = int(input())
for i in range(1, num + 1):
    if i in range(5, 10) or i in range(17, 38) or i in range(78, 88):
        continue
    print(i)
